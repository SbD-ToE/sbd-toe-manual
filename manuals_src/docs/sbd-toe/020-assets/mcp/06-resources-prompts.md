---
id: resources-prompts
title: Resources e prompts
description: Resources MCP (sbd://toe/*) e prompts pré-empacotados do SbD-ToE MCP — quando usar cada um.
sidebar_label: Resources & prompts
sidebar_position: 6
tags:
  - mcp
  - resources
  - prompts
---

# Resources e prompts

Para além das **tools**, o protocolo MCP expõe dois mecanismos adicionais que o servidor SbD-ToE usa amplamente:

- **Resources** (`sbd://toe/*`) — documentos / dados estruturados acessíveis por URI, lidos pelo cliente como contexto.
- **Prompts** — templates de prompt pré-empacotados que o cliente pode executar com parâmetros.

A diferença prática:

| Mecanismo | Lê-se | Caso típico |
|---|---|---|
| **Tool** | Cliente chama, recebe resultado | Operação determinística com parâmetros (consultar requisitos, listar capítulos) |
| **Resource** | Cliente injecta em contexto | Conteúdo estável que vale a pena ter sempre acessível (guia, índice, ontologia) |
| **Prompt** | Cliente executa como mensagem do utilizador | *Workflow* canónico (inicializar sessão, Q&A) |

---

## Resources

Todos os resources usam o esquema `sbd://toe/*` e devolvem `text/markdown`, `application/json` ou `application/yaml` consoante o tipo.

### `sbd://toe/agent-guide`

**MIME:** `text/markdown`
**Conteúdo:** guia operacional completo do agente — modos (CONSULT / GUIDE / SETUP), roteamento por fase / domínio / tipo de pergunta, padrões epistémicos, vocabulário controlado, mapa dos 15 capítulos.

**Quando ler:** **uma vez por sessão**, antes de qualquer chamada. É o *system prompt* canónico.

> Este resource é a fonte do que `generate_sbd_toe_skill` devolve — guardar como *skill file* é exactamente injectá-lo permanentemente no contexto do cliente.

### `sbd://toe/index-compact`

**MIME:** `application/json`
**Conteúdo:** mapa compacto do manual — JSON estruturado com `chapters[]`, `chapter_id`, `title`, `min_level`, `domains`, *topics* ⨯ contagens.

**Quando ler:** *injectar no system prompt* para eliminar exploratory discovery — o agente já "sabe" o índice antes de fazer qualquer chamada.

### `sbd://toe/chapter-applicability/{riskLevel}`

**MIME:** `application/json`
**Parâmetro:** `{riskLevel}` = `L1` | `L2` | `L3` (interpolado no URI)
**Conteúdo:** capítulos **activos**, **condicionais** e **excluídos** para esse *risk level*.

**Exemplo:**

```
sbd://toe/chapter-applicability/L2
```

Devolve algo como:

```json
{
  "active": ["00-fundamentos", "01-classificacao-aplicacoes", "02-...", "06-desenvolvimento-seguro", "11-deploy-seguro", ...],
  "conditional": [...],
  "excluded": ["13-formacao-onboarding"]
}
```

**Quando usar:** inicialização rápida sem chamar `consult_security_requirements` (que devolve muito mais conteúdo).

### `sbd://toe/ontology`

**MIME:** `application/yaml`
**Conteúdo:** ontologia completa — `domain_mapping` (requirement category → control domains), regras de inferência com prioridades, *resolution pipelines* (consult / guide / threats / review), *concerns* lexicon, *role aliases*, schemas de entidade.

**Quando ler:** **uma vez por sessão** para entender o modelo de resolução determinístico antes de combinar tools complexas.

### `sbd://toe/grounded-codegen-guide`

**MIME:** `text/markdown`
**Conteúdo:** guia agente para `prepare_sbd_toe_codegen_context` — *workflow*, ramificação por *status* (`ready_for_codegen` / `needs_clarification` / `needs_decomposition` / `unsupported_scope`), disciplina de *output* (citar `citation_map`, preencher `security_rationale`, distinguir code/tests/evidence), e **proibições explícitas** (não inventar IDs, não declarar conformidade, não poluir código com rastreabilidade-noise).

**Quando ler:** sempre antes de qualquer trabalho de *codegen* ou *review* via `prepare_sbd_toe_codegen_context`.

### `sbd://toe/skill/{role}` · `sbd://toe/subagent/{role}`

**MIME:** `text/markdown`
**Parâmetro:** `{role}` = um dos 13 *roles* canónicos (aliases resolvem)
**Conteúdo:** o mesmo que `generate_sbd_toe_skill(role, format=skill)` (skill) e `…(role, format=subagent)` (definição de *subagent*, *flavour* `harnessed` por omissão — concede as tools `mcp__sbd-toe__*`). Risco `L2` por omissão.

**Quando usar:** instalar a configuração de um papel sem chamar a tool — ler o resource e guardar no caminho do cliente.

### `sbd://toe/version`

**MIME:** `application/json`
**Conteúdo:** identidade do servidor + *provenance* do conhecimento servido (manual, KG, ontologia), lido do *pin* do bundle consumido.

```json
{
  "name": "@shiftleftpt/sbd-toe-mcp",
  "version": "0.10.2",
  "manual":   { "tag": "v1.7.0", "version": "1.7.0", "commit": "d5c2586a…" },
  "kg":       { "release_tag": "v1.6.0", "sha256": "baf5913b…", "source": "release", "consumer_contract_version": "v1.11" },
  "ontology": { "tag": "ontology-v1.1-fair-baseline", "commit": "…" }
}
```

**Quando usar:** *troubleshooting* — confirmar a versão activa e a *provenance* (que manual/KG/ontologia o servidor serve), e se cobre o conteúdo esperado (ver [troubleshooting / FAQ](./10-troubleshooting-faq.md) sobre *content lag*).

---

## Prompts

### `setup_sbd_toe_agent(riskLevel, projectRole)`

Inicializa a sessão.

**Parâmetros:**
- `riskLevel`: `L1` | `L2` | `L3`
- `projectRole`: um dos 13 *roles* canónicos

**Resultado:** mensagem do utilizador equivalente a "Estou a trabalhar num projecto `riskLevel=L2`, role `appsec-engineer`. Carrega as regras e capítulos activos." — o agente executa imediatamente as chamadas adequadas para inicializar o contexto.

### `ask_sbd_toe_manual(question)`

Q&A directo *grounded* no manual.

**Parâmetros:**
- `question`: pergunta em linguagem natural

**Resultado:** o agente é instruído a usar `search_sbd_toe_manual` ou `consult_security_requirements` consoante o tipo de pergunta, e a responder com IDs citáveis.

### `prepare_grounded_codegen(task, mode?, riskLevel?, concerns?, stack?, regulatoryFrameworks?, includeRegulatoryOverlay?)`

*Codegen grounded* de ponta a ponta: embute o guia `sbd://toe/grounded-codegen-guide` (acima) e a tarefa numa única mensagem, e instrui o agente a chamar `prepare_sbd_toe_codegen_context` **antes** de produzir código.

**Parâmetros:**
- `task`: tarefa concreta de código (obrigatório; ex.: "Add payload validation to PATCH /users/:id/email")
- `mode`: `codegen` | `review` | `test-plan` (por omissão `codegen`)
- `riskLevel`: `L1` | `L2` | `L3` · `concerns`: lista explícita (senão inferidos pelo motor de activação) · `stack`: informativo
- `regulatoryFrameworks` (ex.: `GDPR`, `EXT-DORA`) · `includeRegulatoryOverlay`: quando verdadeiro, expõe o contexto do overlay regulatório

**Resultado:** o agente é obrigado a citar IDs do `citation_map`, preencher o `security_rationale_template`, distinguir código, testes e evidência, não fazer afirmações de conformidade, e encaminhar `needs_clarification` / `needs_decomposition` / `unsupported_scope` para diálogo com o utilizador em vez de adivinhar em silêncio.

---

## Boa prática — *bootstrap* mínimo de sessão

```
1. Ler sbd://toe/agent-guide  (ou ter skill instalada)
2. Ler sbd://toe/index-compact  (mapa compacto — barato)
3. Executar prompt setup_sbd_toe_agent(riskLevel, projectRole)
4. Pronto para CONSULT/GUIDE
```

Se a sessão for de *codegen* / *review*: acrescentar `sbd://toe/grounded-codegen-guide` antes de qualquer chamada a `prepare_sbd_toe_codegen_context`.

## A seguir

- [Casos de uso](./casos-uso/) — 6 receitas prontas combinando estes resources, prompts e tools.
- [Padrões avançados](./08-padroes-avancados.md) — sequências multi-tool para problemas complexos.
