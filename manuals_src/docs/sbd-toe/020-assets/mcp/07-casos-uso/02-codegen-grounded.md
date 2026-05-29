---
id: codegen-grounded
title: Codegen grounded
description: Gerar código com prepare_sbd_toe_codegen_context — 4 status, disciplina de citation_map, security_rationale obrigatório.
sidebar_label: Codegen grounded
sidebar_position: 2
tags:
  - mcp
  - casos-uso
  - codegen
  - citation-map
---

# Caso de uso — Codegen grounded

Quando se pede a um agente para implementar algo sensível — um endpoint de login com lockout, uma rotina de cifra, um manipulador de uploads — a tentação habitual é deixá-lo escrever o código primeiro e auditar depois. O problema é que, sem *grounding*, o agente vai citar *boas práticas* que parecem certas mas não têm origem rastreável.

O `prepare_sbd_toe_codegen_context` foi desenhado para inverter essa ordem. Antes de propor uma linha de código, o agente pede ao servidor o *contexto* que cobre a tarefa: requisitos activos, controlos aplicáveis, *threats* relevantes e — se o pedido for sobre um regulamento — a *overlay* normativa. Devolve um `citation_map` fechado de IDs válidos. A partir daí, o código gerado vem acompanhado de um `security_rationale` em que cada decisão referencia IDs reais ou diz explicitamente *"nenhum controlo coberto — flag para revisão humana"*.

## Pré-requisitos

- MCP instalado, skill carregada.
- Ler [`sbd://toe/grounded-codegen-guide`](../06-resources-prompts.md#sbdtoegrounded-codegen-guide) **uma vez por sessão** antes de qualquer chamada.

## Fluxo

### 1. Decompor mentalmente — *bite-size*

Critérios:
- **1 surface técnica** (1 endpoint, 1 módulo, 1 grupo de ficheiros)
- **1 fase do SDLC** (`implement` | `test` | `deploy` | `operate`)
- **1–3 *concerns***

Se a tarefa exceder isto, o servidor devolve `needs_decomposition` — antecipar.

### 2. Chamar a tool

```json
prepare_sbd_toe_codegen_context({
  "task": "Implementar endpoint POST /login com lockout após 5 falhas em 10 minutos",
  "risk_level": "L2",
  "mode": "codegen",
  "stack": "node-express-typescript",
  "exposure": "public",
  "data_sensitivity": "credentials",
  "concerns": ["auth", "logging"],
  "regulatory_frameworks": ["GDPR"],
  "include_regulatory_overlay": true
})
```

### 3. Ramificar por `status`

#### `ready_for_codegen`

Procede. Disciplina obrigatória:

| Campo | Como preencher |
|---|---|
| `security_rationale.decisions[].cited_ids` | ≥1 ID de `citation_map` por decisão não-trivial; se nenhum encaixa → `"none"` + justificação |
| `security_rationale.validations[]` | Validações concretas implementadas (surface, regra, comportamento de rejeição) |
| `security_rationale.expected_evidence[]` | Test path, log shape, SBOM entry, attestation, scan report — **código não é evidência** |
| `security_rationale.residual_risk` | O que **não** foi endereçado neste *change* |

Se `completeness_report.m_recall < 1.0` → **sinalizar cobertura parcial ao utilizador**.

#### `needs_clarification`

**STOP**. Não gerar nada. Responder:
1. `reasons[]` em linguagem clara.
2. Perguntas mínimas derivadas de `suggestions[]`.

Não re-chamar a tool até o utilizador responder.

#### `needs_decomposition`

**STOP**. Não escolher um sub-task silenciosamente. Responder:
1. `reasons[]`.
2. 2–4 sub-tarefas, cada uma com surface/phase/concerns explícitos (derivados de `partial_activation_trace`).
3. **Pergunta ao utilizador qual atacar primeiro.**

#### `unsupported_scope`

**STOP**. Reportar o problema verbatim — não fabricar IDs para continuar:

| Causa | Resposta |
|---|---|
| `AppSec Core v1 runtime ausente` | "Deploy incompleto — re-correr `npm run checkout:backend` ou *pin* outra KG snapshot." |
| `Overlay regulatório ausente` | "Remover `regulatory_frameworks` / `include_regulatory_overlay`, ou esperar publicação." |
| `Framework regulatório desconhecida` | Listar os *short codes* suportados de `regulatory_overlay.frameworks`. |

## Disciplina de output (`ready_for_codegen`)

### Três classes de artefacto — distinguir sempre

| Classe | Definição | Exemplo |
|---|---|---|
| **Code** | Source proposto | `src/auth/login.ts` |
| **Tests** | Verificações automatizadas que exercitam `security_rationale.validations[]` | `test/auth/lockout.spec.ts` |
| **Evidence** | Artefactos que um *reviewer* inspecciona — log lines, SBOM, attestation, audit report, scan output. **Tests são evidência; código não é.** | Log: `auth.lockout.activated`, schema X |

### Onde citar IDs

- ✅ **PR description / commit message / `security_rationale`** — sempre.
- ⚠️ **Source files** — só se o *WHY* não for óbvio do código. Evitar `// per ACO-IVF-001`.

### Nomenclatura

- Entidades sem `name` retornado → referir por `entity_id` exacto.
- Manter ordenação relativa dos `evidence_patterns` (já vem capada/ordenada).

## Anti-patterns

- ❌ Inventar IDs `ACO-...`, `ACM-...`, `EXT-...`, `EP-...`, `CTRL-...` fora do `citation_map`.
- ❌ Re-chamar a tool com o **mesmo payload** após `needs_*` para "tentar de novo" — *bypass* do *scope gate*.
- ❌ Declarar conformidade ("este código cumpre GDPR Art. 32") — o *regulatory overlay* é *cross-check*, **não** sinal de conformidade.
- ❌ Propor controlos `L3` numa tarefa `L1` — respeitar o *risk level*.
- ❌ Copiar nomes de entidades não publicados pela rastreabilidade.

## Skill / subagent — Claude Code

`.claude/agents/sbd-toe-codegen.md`:

```markdown
---
name: sbd-toe-codegen
description: Gera código grounded com prepare_sbd_toe_codegen_context. Respeita os 4 status. Nunca inventa IDs nem declara conformidade.
tools: Read, Write, Edit, Grep, Glob, mcp__sbd-toe__*
---

# Workflow obrigatório

1. Ler sbd://toe/grounded-codegen-guide (1× por sessão).
2. Decompor a tarefa em bite-size (1 surface, 1 fase, 1–3 concerns).
3. Chamar prepare_sbd_toe_codegen_context com TODOS os parâmetros que se sabe.
4. Ramificar por status conforme tabela. NUNCA gerar código antes de ler status.
5. Em ready_for_codegen: gerar code + tests + security_rationale citando apenas IDs do citation_map.
6. Em needs_*: STOP, dialogar com o utilizador, não tentar contornar.

# Hard rules

- citation_map é o mundo fechado de IDs válidos para esta tarefa.
- Tests são evidência; código não é.
- Regulatory overlay é cross-check, não conformidade.
- Em m_recall < 1.0, sinalizar cobertura parcial.
```

## Modos `review` e `test-plan`

A mesma tool serve `mode: "review"` e `mode: "test-plan"`:

| Mode | Output esperado |
|---|---|
| `codegen` | code + tests + security_rationale |
| `review` | findings por ficheiro alterado, cada um mapeado a 1+ IDs do `citation_map` |
| `test-plan` | checklist agrupado por `validated_id`; cada teste: input → outcome → `evidence_patterns[].id` que satisfaz |

## Relacionado

- [Auditoria de PR](./auditoria-pr) — `mode: "review"` para PRs (alternativa mais simples sem `prepare_sbd_toe_codegen_context`).
- [Threat modeling](./threat-modeling) — antes do *codegen*, perceber as ameaças.
- [`sbd://toe/grounded-codegen-guide`](../06-resources-prompts.md#sbdtoegrounded-codegen-guide) — fonte canónica.
