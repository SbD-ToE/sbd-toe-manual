---
id: codegen-grounded
title: Codegen grounded
description: Gerar código com prepare_sbd_toe_codegen_context — ramificação por status, disciplina de citations, security_rationale obrigatório.
sidebar_label: Codegen grounded
sidebar_position: 2
tags:
  - mcp
  - casos-uso
  - codegen
  - citations
---

# Caso de uso — Codegen grounded

Quando se pede a um agente para implementar algo sensível — um endpoint de login com lockout, uma rotina de cifra, um manipulador de uploads — a tentação habitual é deixá-lo escrever o código primeiro e auditar depois. O problema é que, sem *grounding*, o agente vai citar *boas práticas* que parecem certas mas não têm origem rastreável.

O `prepare_sbd_toe_codegen_context` foi desenhado para inverter essa ordem. Antes de propor uma linha de código, o agente pede ao servidor o *contexto* que cobre a tarefa: requisitos activos, controlos aplicáveis, *threats* relevantes e — se o pedido for sobre um regulamento — a *overlay* normativa. Devolve um bloco `citations` — o mundo fechado de ids válidos. A partir daí, o código gerado vem acompanhado de um `security_rationale` em que cada decisão referencia IDs reais ou diz explicitamente *"nenhum controlo coberto — flag para revisão humana"*.

## Pré-requisitos {#pré-requisitos}

- MCP instalado, skill carregada.
- Ler [`sbd://toe/grounded-codegen-guide`](../06-resources-prompts.md#sbdtoegrounded-codegen-guide) **uma vez por sessão** antes de qualquer chamada.

## Fluxo {#fluxo}

### 1. Decompor mentalmente — *bite-size* {#1-decompor-mentalmente--bite-size}

Critérios:
- **1 surface técnica** (1 endpoint, 1 módulo, 1 grupo de ficheiros)
- **1 fase do SDLC** (`implement` | `test` | `deploy` | `operate`)
- **1–3 *concerns***

Se a tarefa exceder isto, o servidor devolve `needs_decomposition` — antecipar.

### 2. Chamar a tool {#2-chamar-a-tool}

```json
prepare_sbd_toe_codegen_context({
  "task": "Implementar endpoint POST /login com lockout após 5 falhas em 10 minutos",
  "risk_level": "L2",
  "mode": "codegen",
  "detail": "lista",
  "concerns": ["auth", "logging"],
  "technologies": ["jwt"]
})
```

A resposta é `ready_for_codegen`, dentro do envelope. O `task` fica registado como contexto; o que conduz a seleção é a declaração — `risk_level`, `concerns`, `technologies`. A `adjacency` da resposta avisa o que ficou por declarar e mudaria o conjunto: neste caso, a exposição pública.

:::note O que muda ao declarar mais
Declarar também `"exposure": "public"` alarga a seleção para 70 requisitos — acima do tecto do nível `lista`. A resposta passa então a `needs_decomposition`, com dois lotes executáveis (de 48 e de 23 requisitos) cuja união é a seleção inteira. Não é um erro: é o servidor a dizer que a tarefa, assim declarada, não cabe numa só resposta desse nível, e a propor como a percorrer sem perder nada.
:::

### 3. Ramificar por `status` {#3-ramificar-por-status}

#### `ready_for_codegen` {#ready_for_codegen}

Procede. Disciplina obrigatória:

| Campo | Como preencher |
|---|---|
| `security_rationale.decisions[].cited_ids` | ≥1 id de `citations` por decisão não-trivial; se nenhum encaixa → `"none"` + justificação |
| `security_rationale.validations[]` | Validações concretas implementadas (surface, regra, comportamento de rejeição) |
| `security_rationale.expected_evidence[]` | Test path, log shape, SBOM entry, attestation, scan report — **código não é evidência** |
| `security_rationale.residual_risk` | O que **não** foi endereçado neste *change* |

Se `completeness_report.m_recall < 1.0` → **sinalizar cobertura parcial ao utilizador**.

#### `needs_input` {#needs_input}

**STOP**. Nada foi declarado, e o servidor não adivinha a partir do `task`. A resposta traz o vocabulário aceite, os candidatos a confirmar e, para declarações inertes, os `valid_values`. Responder:
1. Os candidatos, em linguagem clara, para o utilizador confirmar.
2. Depois da confirmação, chamar de novo com a declaração completa.

#### `needs_clarification` {#needs_clarification}

**STOP**. Não gerar nada. Responder:
1. `reasons[]` em linguagem clara.
2. Perguntas mínimas derivadas de `suggestions[]`.

Não re-chamar a tool até o utilizador responder.

#### `needs_decomposition` {#needs_decomposition}

**STOP**. Não escolher um sub-task silenciosamente. Responder:
1. `reasons[]`.
2. Quando a seleção ultrapassa o tecto do nível de `detail`, a resposta traz em `requirement_ceiling.batches` os lotes executáveis (`categories` + os ativadores preservados) cuja união é a seleção inteira — apresentar esses lotes, em vez de redesenhar sub-tarefas à mão.
3. **Pergunta ao utilizador por que lote começar.**

#### `unsupported_scope` {#unsupported_scope}

**STOP**. Reportar o problema verbatim — não fabricar IDs para continuar:

| Causa | Resposta |
|---|---|
| `AppSec Core v1 runtime ausente` | "Instalação incompleta — reinstalar ou atualizar o pacote publicado e reportar ao operador." |
| `Overlay regulatório ausente` | "Remover `regulatory_frameworks` / `include_regulatory_overlay`, ou esperar publicação." |
| `Framework regulatório desconhecida` | Listar os *short codes* suportados de `regulatory_overlay.frameworks`. |

## Forma da resposta {#forma-da-resposta}

O que chega com `ready_for_codegen` está desenhado para caber no contexto do agente sem perder rastreabilidade:

- **Um objeto por requisito** — `{id, name, type, description, verify, evidence}`: o requisito, como se verifica e que evidência se espera, no mesmo sítio.
- **Níveis de `detail`** — `lista`, `standard` e `full` definem quanto de cada requisito vem *inline*. O que cada nível inclui está na descrição servida da tool; a `lista` é a escolha natural para começar.
- **Tectos por contagem** — cada nível aceita até um certo número de requisitos. Acima do tecto, a resposta é `needs_decomposition`, com os lotes de `requirement_ceiling.batches` que somam o todo.
- **`adjacency`** — o que não foi declarado e mudaria o conjunto selecionado. É a forma de o servidor dizer «isto também podia contar» sem o decidir pelo agente.
- **`size_estimate`** — o tamanho da própria resposta; `within_envelope: false` avisa que excede o envelope previsto.
- **Notas por referência** — em vez de repetir a mesma nota, a resposta traz um `note_id`, que se resolve em `sbd://toe/notes/{id}`.

## Disciplina de output (`ready_for_codegen`) {#disciplina-de-output-ready_for_codegen}

### Três classes de artefacto — distinguir sempre {#três-classes-de-artefacto--distinguir-sempre}

| Classe | Definição | Exemplo |
|---|---|---|
| **Code** | Source proposto | `src/auth/login.ts` |
| **Tests** | Verificações automatizadas que exercitam `security_rationale.validations[]` | `test/auth/lockout.spec.ts` |
| **Evidence** | Artefactos que um *reviewer* inspecciona — log lines, SBOM, attestation, audit report, scan output. **Tests são evidência; código não é.** | Log: `auth.lockout.activated`, schema X |

### Onde citar IDs {#onde-citar-ids}

- ✅ **PR description / commit message / `security_rationale`** — sempre.
- ⚠️ **Source files** — só se o *WHY* não for óbvio do código. Evitar `// per ACO-IVF-001`.

### Nomenclatura {#nomenclatura}

- Entidades sem `name` retornado → referir por `entity_id` exacto.
- A verificação vem por requisito: cada objeto traz `verify` e `evidence`; os ids de padrão de evidência estão em `completeness_report.verification.by_ref`.

## Anti-patterns {#anti-patterns}

- ❌ Inventar IDs `ACO-...`, `ACM-...`, `EXT-...`, `EP-...`, `CTRL-...` fora de `citations`.
- ❌ Re-chamar a tool com o **mesmo payload** após `needs_*` para "tentar de novo" — *bypass* do *scope gate*.
- ❌ Declarar conformidade ("este código cumpre GDPR Art. 32") — o *regulatory overlay* é *cross-check*, **não** sinal de conformidade.
- ❌ Propor controlos `L3` numa tarefa `L1` — respeitar o *risk level*.
- ❌ Copiar nomes de entidades não publicados pela rastreabilidade.

## Skill / subagent — Claude Code {#skill--subagent--claude-code}

`.claude/agents/sbd-toe-codegen.md`:

```markdown
---
name: sbd-toe-codegen
description: Gera código grounded com prepare_sbd_toe_codegen_context. Respeita os status. Nunca inventa IDs nem declara conformidade.
tools: Read, Write, Edit, Grep, Glob, mcp__sbd-toe__*
---

# Workflow obrigatório

1. Ler sbd://toe/grounded-codegen-guide (1× por sessão).
2. Decompor a tarefa em bite-size (1 surface, 1 fase, 1–3 concerns).
3. Chamar prepare_sbd_toe_codegen_context com TODOS os parâmetros que se sabe.
4. Ramificar por status conforme tabela. NUNCA gerar código antes de ler status.
5. Em ready_for_codegen: gerar code + tests + security_rationale citando apenas ids de citations.
6. Em needs_*: STOP, dialogar com o utilizador, não tentar contornar (em needs_decomposition, seguir os lotes de requirement_ceiling.batches).

# Hard rules

- citations é o mundo fechado de ids válidos para esta tarefa.
- Tests são evidência; código não é.
- Regulatory overlay é cross-check, não conformidade.
- Em m_recall < 1.0, sinalizar cobertura parcial.
```

## Modos `review` e `test-plan` {#modos-review-e-test-plan}

A mesma tool serve `mode: "review"` e `mode: "test-plan"`:

| Mode | Output esperado |
|---|---|
| `codegen` | code + tests + security_rationale |
| `review` | findings por ficheiro alterado, cada um mapeado a 1+ ids de `citations` |
| `test-plan` | checklist agrupado por `validated_id`; cada teste: input → outcome → o `verify` / `evidence` do requisito como expectativa (ids de padrão via `completeness_report.verification.by_ref`) |

## Relacionado {#relacionado}

- [Auditoria de PR](./auditoria-pr) — `mode: "review"` para PRs (alternativa mais simples sem `prepare_sbd_toe_codegen_context`).
- [Threat modeling](./threat-modeling) — antes do *codegen*, perceber as ameaças.
- [`sbd://toe/grounded-codegen-guide`](../06-resources-prompts.md#sbdtoegrounded-codegen-guide) — fonte canónica.
