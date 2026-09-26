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

## Resources {#resources}

Todos os resources usam o esquema `sbd://toe/*` e devolvem `text/markdown`, `application/json` ou `application/yaml` consoante o tipo. O MIME de cada um é o que `resources/list` publica:

| resource | MIME |
|---|---|
| `sbd://toe/model` | `application/json` |
| `sbd://toe/notes` · `sbd://toe/notes/{id}` | `application/json` |
| `sbd://toe/codegen-instructions/{mode}` | `application/json` |
| `sbd://toe/quick-start` | `application/json` |
| `sbd://toe/activation-vocabulary` | `application/json` |
| `sbd://toe/index-compact` | `application/json` |
| `sbd://toe/chapter-applicability/{riskLevel}` | `application/json` |
| `sbd://toe/version` | `application/json` |
| `sbd://toe/ontology` | `application/yaml` |
| `sbd://toe/agent-guide` · `sbd://toe/grounded-codegen-guide` | `text/markdown` |
| `sbd://toe/skill/{role}` · `sbd://toe/subagent/{role}` | `text/markdown` |

### `sbd://toe/agent-guide` {#sbdtoeagent-guide}

**MIME:** `text/markdown`
**Conteúdo:** guia operacional completo do agente — modos (CONSULT / GUIDE / SETUP), roteamento por fase / domínio / tipo de pergunta, padrões epistémicos, vocabulário controlado, mapa dos 15 capítulos.

**Quando ler:** **uma vez por sessão**, antes de qualquer chamada. É o *system prompt* canónico.

> Este resource é a fonte do que `generate_sbd_toe_skill` devolve — guardar como *skill file* é exactamente injectá-lo permanentemente no contexto do cliente.

### `sbd://toe/index-compact` {#sbdtoeindex-compact}

**MIME:** `application/json`
**Conteúdo:** mapa compacto do manual — JSON estruturado com, por capítulo, `chapterId`, `readableTitle`, `demand_by_level` (a exigência em cada nível — a aplicabilidade é graduada) e `technologies`.

**Quando ler:** *injectar no system prompt* para eliminar exploratory discovery — o agente já "sabe" o índice antes de fazer qualquer chamada.

### `sbd://toe/chapter-applicability/{riskLevel}` {#sbdtoechapter-applicabilityrisklevel}

**MIME:** `application/json`
**Parâmetro:** `{riskLevel}` = `L1` | `L2` | `L3` (interpolado no URI)
**Conteúdo:** a aplicabilidade **graduada** para esse *risk level* — todos os capítulos se aplicam a todos os níveis; o que muda é a exigência de cada um. Nenhum capítulo é excluído, e o próprio recurso o declara no campo `semantics`.

**Exemplo:**

```
sbd://toe/chapter-applicability/L2
```

Devolve um objeto com esta forma. O objecto de topo traz `riskLevel`, `semantics`, `canonical_anchor` e `chapters`. Cada capítulo de `chapters[]` traz `chapter_id`, `title` e `applicable`, que é sempre `true`: nenhum capítulo é excluído. Traz também:

- `demand`: as contagens `obrigatorio`, `recomendado`, `opcional` e `specific` nesse nível;
- `dominant`: o perfil dominante do capítulo;
- `roles` e `user_stories`: contagens;
- `source`: de onde vem a linha. Um capítulo fundacional sem *assignments* no bundle declara um *fallback*.

```json
{
  "riskLevel": "L2",
  "semantics": "…",
  "canonical_anchor": "…",
  "chapters": [ … ]
}
```

**Quando usar:** inicialização rápida sem chamar `consult_security_requirements` (que devolve muito mais conteúdo).

### `sbd://toe/ontology` {#sbdtoeontology}

**MIME:** `application/yaml`
**Conteúdo:** ontologia completa — `domain_mapping` (requirement category → control domains), regras de inferência com prioridades, *resolution pipelines* (consult / guide / threats / review), *concerns* lexicon, *role aliases*, schemas de entidade.

**Quando ler:** **uma vez por sessão** para entender o modelo de resolução determinístico antes de combinar tools complexas.

### `sbd://toe/grounded-codegen-guide` {#sbdtoegrounded-codegen-guide}

**MIME:** `text/markdown`
**Conteúdo:** guia agente para `prepare_sbd_toe_codegen_context` — *workflow*, ramificação por *status* (`ready_for_codegen` / `needs_clarification` / `needs_decomposition` / `needs_input` / `unsupported_scope`), disciplina de *output* (citar ids de `citations`, preencher `security_rationale`, distinguir code/tests/evidence), e **proibições explícitas** (não inventar IDs, não declarar conformidade, não poluir código com rastreabilidade-noise).

**Quando ler:** sempre antes de qualquer trabalho de *codegen* ou *review* via `prepare_sbd_toe_codegen_context`.

### `sbd://toe/skill/{role}` · `sbd://toe/subagent/{role}` {#sbdtoeskillrole--sbdtoesubagentrole}

**MIME:** `text/markdown`
**Parâmetro:** `{role}` = um dos 13 *roles* canónicos (aliases resolvem)
**Conteúdo:** o mesmo que `generate_sbd_toe_skill(role, format=skill)` (skill) e `…(role, format=subagent)` (definição de *subagent*, *flavour* `harnessed` por omissão — concede as tools `mcp__sbd-toe__*`). Risco `L2` por omissão.

**Quando usar:** instalar a configuração de um papel sem chamar a tool — ler o resource e guardar no caminho do cliente.

### `sbd://toe/activation-vocabulary` {#sbdtoeactivation-vocabulary}

**Conteúdo:** o vocabulário fechado de ativação — os valores aceites nas declarações (*concerns* e restantes campos, incluindo `roles`) e o que cada valor ativa.

**Quando ler:** antes da primeira declaração em `select_sbd_toe_requirements` ou `prepare_sbd_toe_codegen_context`. É a fonte dos valores — as páginas deste mini-site não os copiam, porque o vocabulário muda entre versões.

### `sbd://toe/quick-start` {#sbdtoequick-start}

**Conteúdo:** o arranque barato da sessão.

**Quando ler:** no início da sessão, quando se quer entrar depressa sem carregar logo o guia completo.

### `sbd://toe/notes/{id}` · `sbd://toe/notes` {#sbdtoenotesid--sbdtoenotes}

**Parâmetro:** `{id}` = um `note_id` (interpolado no URI)
**MIME:** `application/json`
**Conteúdo:** o registo das notas por referência. As respostas do prepare trazem um `note_id` em vez de repetirem a prosa, mais um cabeçalho `notes`. `sbd://toe/notes` devolve o índice `{ids, notes}`, com todos os ids e textos. `sbd://toe/notes/{id}` devolve `{id, text}`. Um id desconhecido devolve um erro declarado com os ids válidos.

### `sbd://toe/model` · `sbd://toe/codegen-instructions/{mode}` {#sbdtoemodel--sbdtoecodegen-instructionsmode}

**MIME:** `application/json` (ambos)

**`sbd://toe/model`** é o mapa do conhecimento servido, não a lista de tools. Traz as entidades com as contagens reais, as relações com as cardinalidades reais, e os capítulos e as categorias com a forma de os alcançar. Mostra as três formas de pedir: por conceito (o atalho `concerns`), por estrutura (`chapters`/`categories`, sempre possível) e por navegação (o grafo), com quando usar cada uma. Tudo é derivado do bundle servido; nada enumerável é escrito à mão. Ler quando o atalho de `concerns` não tiver a pergunta. Blocos: `how_to_ask`, `entities`, `relations`, `chapters`, `categories` e `see_also`.

**`sbd://toe/codegen-instructions/{mode}`** é a cópia de referência, por modo (`codegen`, `review`, `test-plan`), do texto estático do prepare. Contém os slots de `llm_codegen_instructions`, com as regras de montagem, e o esqueleto de `security_rationale_template`. Montados pelas regras embutidas, dão o mesmo texto que o prepare põe inline. Contém ainda a legenda `detail_encoding`, que explica como ler um *payload* `lista`/`standard`. As instruções e o *template* vêm inline em todos os níveis: este resource é a referência, não uma dependência. Com `read_sbd_toe_resource`, `slot` devolve um só slot.

### `sbd://toe/version` {#sbdtoeversion}

**MIME:** `application/json`
**Conteúdo:** identidade do servidor + *provenance* do conhecimento servido (manual, KG, ontologia, contrato), lido do *pin* do bundle consumido.

```json
{
  "name": "…",
  "version": "…",
  "manual": "…",
  "kg": "…",
  "ontology": "…",
  "serving_contract": "…",
  "surface_history": "…"
}
```

**Quando usar:** *troubleshooting* — confirmar a versão activa e a *provenance* (que manual/KG/ontologia o servidor serve), e se cobre o conteúdo esperado (ver [troubleshooting / FAQ](./10-troubleshooting-faq.md) sobre *content lag*).

---

## Prompts {#prompts}

### `setup_sbd_toe_agent(riskLevel, projectRole)` {#setup_sbd_toe_agentrisklevel-projectrole}

Inicializa a sessão.

**Parâmetros:**
- `riskLevel`: `L1` | `L2` | `L3`
- `projectRole`: um dos 13 *roles* canónicos

**Resultado:** uma mensagem do utilizador que fixa o `riskLevel` e o papel e leva o agente a fazer as chamadas de inicialização. A resposta descreve a exigência de cada capítulo nesse nível — a aplicabilidade é graduada, nenhum capítulo fica excluído — e as regras do papel.

Por ser um *prompt* MCP, só existe em clientes que suportam *prompts*; o Claude Desktop, por exemplo, não o expõe. Nesses clientes, a sessão arranca pelos resources (`sbd://toe/quick-start`, `sbd://toe/activation-vocabulary`) e pela primeira declaração em `select_sbd_toe_requirements`.

### `ask_sbd_toe_manual(question)` {#ask_sbd_toe_manualquestion}

Q&A directo *grounded* no manual.

**Parâmetros:**
- `question`: pergunta em linguagem natural

**Resultado:** o agente é instruído a usar `search_sbd_toe_manual` ou `consult_security_requirements` consoante o tipo de pergunta, e a responder com IDs citáveis.

### `prepare_grounded_codegen(task, mode?, riskLevel?, concerns?, stack?, regulatoryFrameworks?, includeRegulatoryOverlay?)` {#prepare_grounded_codegentask-mode-risklevel-concerns-stack-regulatoryframeworks-includeregulatoryoverlay}

*Codegen grounded* de ponta a ponta: embute o guia `sbd://toe/grounded-codegen-guide` (acima) e a tarefa numa única mensagem, e instrui o agente a chamar `prepare_sbd_toe_codegen_context` **antes** de produzir código.

**Parâmetros:**
- `task`: tarefa concreta de código (obrigatório; ex.: "Add payload validation to PATCH /users/:id/email")
- `mode`: `codegen` | `review` | `test-plan` (por omissão `codegen`)
- `riskLevel`: `L1` | `L2` | `L3` · `concerns`: lista explícita — em modo declarativo nada se infere do `task`: sem declaração, a resposta é `needs_input`, com o vocabulário aceite · `stack`: informativo
- `regulatoryFrameworks` (ex.: `RGPD`, `EXT-DORA`; códigos publicados: `RGPD`, `DORA`, `NIS2`, `CRA`, `AI-ACT`, `ENISA-CSA`, ou a forma `EXT-…`) · `includeRegulatoryOverlay`: quando verdadeiro, expõe o contexto do overlay regulatório

**Resultado:** o agente é obrigado a citar ids de `citations`, preencher o `security_rationale_template`, distinguir código, testes e evidência, não fazer afirmações de conformidade, e encaminhar `needs_clarification` / `needs_decomposition` / `unsupported_scope` para diálogo com o utilizador em vez de adivinhar em silêncio.

---

## Boa prática — *bootstrap* mínimo de sessão {#boa-prática--bootstrap-mínimo-de-sessão}

```
1. Ler sbd://toe/quick-start  (arranque barato)
2. Ler sbd://toe/agent-guide  (ou ter skill instalada)
3. Ler sbd://toe/index-compact  (mapa compacto — barato)
4. Ler sbd://toe/activation-vocabulary  (valores aceites, antes da primeira declaração)
5. Executar prompt setup_sbd_toe_agent(riskLevel, projectRole)  (se o cliente expõe prompts)
6. Pronto para a primeira declaração — select_sbd_toe_requirements — e para CONSULT/GUIDE
```

Se a sessão for de *codegen* / *review*: acrescentar `sbd://toe/grounded-codegen-guide` antes de qualquer chamada a `prepare_sbd_toe_codegen_context`.

## A seguir {#a-seguir}

- [Casos de uso](./casos-uso/) — receitas prontas combinando estes resources, prompts e tools.
- [Padrões avançados](./08-padroes-avancados.md) — sequências multi-tool para problemas complexos.
