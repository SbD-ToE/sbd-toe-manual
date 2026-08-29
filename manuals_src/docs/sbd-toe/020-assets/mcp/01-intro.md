---
id: intro
title: MCP Server — Introdução
description: Servidor MCP oficial do SbD-ToE — ligar Claude, Copilot, Cursor e outros clientes MCP ao manual com grounding determinístico.
sidebar_label: Introdução
sidebar_position: 1
tags:
  - mcp
  - integracao
  - tooling
  - sbd-toe
---

# MCP Server (SbD-ToE)

Quando se pede a um agente que escreva código seguro, ele tem duas opções: ou recorre ao que reteve do treino — uma aproximação plausível, mas sem âncora nem fonte —, ou consulta o manual numa fonte que devolve requisitos e controlos com identificadores citáveis. O **`@shiftleftpt/sbd-toe-mcp`** existe para tornar a segunda opção trivial.

É o servidor [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) oficial do SbD-ToE. Expõe o manual (capítulos 00–14), a ontologia *AppSec Core v1* e os cross-checks normativos publicados através de **tools, resources e prompts MCP** — para que o Claude, o GitHub Copilot, o Cursor, o Windsurf, o Zed (ou qualquer outro cliente MCP) deixem de responder a partir do que treinaram e passem a perguntar à fonte, no momento em que escrevem, com IDs reais. Em prática: cada `CTRL-*`, `REQ-*`, `THR-*` ou `ART-*` que o agente refere passa a ser verificável.

| Atributo | Valor |
|---|---|
| **Package** | [`@shiftleftpt/sbd-toe-mcp`](https://www.npmjs.com/package/@shiftleftpt/sbd-toe-mcp) (npm) |
| **Repositório** | [`Shiftleftpt/sbd-toe-mcp-poc`](https://github.com/Shiftleftpt/sbd-toe-mcp-poc) (GitHub) |
| **Binário** | `sbd-toe-mcp` |
| **Requisitos** | Node.js ≥ 20.9.0 |
| **Licenciamento** | Apache-2.0 (código/runtime) · CC BY-SA 4.0 (snapshots de manual incluídos) |
| **Transporte** | `stdio` (compatível com todos os clientes MCP padrão) |

:::info Versão actual e *content lag*
A versão publicada (**`@shiftleftpt/sbd-toe-mcp@0.10.2`**) serve o *snapshot* do manual **`v1.7.0`** sobre o KG formal **`v1.6.0`** (contrato de consumo v1.11): o **canon (capítulos 00–14)** e os fundamentos (incluindo os [cinco macro-processos](/sbd-toe/sbd-manual/fundamentos/macro-processos)), a **ontologia AppSec Core v1** e os seis cross-checks normativos — **CRA**, **DORA**, **NIS2**, **GDPR**, **AI Act** e **ENISA/CSA** — todos indexados e citáveis.

O servidor serve sempre o *snapshot* do manual da altura da publicação; a versão exacta (manual, KG, ontologia) está em `sbd://toe/version`. Se o manual web tiver conteúdo posterior ao *snapshot*, ver [content lag](./10-troubleshooting-faq.md#content-lag).
:::

---

## Para que serve

Há três tipos de momento em que um agente recorre ao SbD-ToE — perceber **o que o manual diz**, perceber **como aplicar o que o manual diz**, e configurar-se a si próprio para o fazer bem. O MCP atende cada um com um conjunto distinto de *tools*:

| Modo | Quando usar | Tools-chave |
|---|---|---|
| **CONSULT** | "O que o manual diz?", "O que se aplica a este projecto?", "Que controlos estão activos?" | `consult_security_requirements`, `search_sbd_toe_manual`, `map_sbd_toe_applicability`, `query_sbd_toe_entities` |
| **GUIDE** | "Como implemento isto?", "Como reviso este PR?", "Que threats aplicam aqui?" | `get_guide_by_role`, `get_threat_landscape`, `plan_sbd_toe_repo_governance`, `map_sbd_toe_review_scope`, `prepare_sbd_toe_codegen_context` |
| **SETUP** | "Configurar o meu cliente AI para usar o SbD-ToE" | `generate_sbd_toe_skill`, `setup_sbd_toe_agent` |
| **IMPL** (vista de implementação) | "Como pôr de pé e governar o SbD?" — checklist por capítulo, operating model, rollout, verificação, KPIs | `get_sbd_toe_chapter_implementation_checklist`, `get_sbd_toe_operating_model`, `plan_sbd_toe_rollout`, `get_sbd_toe_verification_matrix`, `assess_sbd_toe_implementation` |

A vista de implementação (IMPL) responde a *como pôr de pé e governar* o SbD numa organização — distinta da vista operacional (GUIDE), que diz *o que fazer em cada fase do SDLC*.

A linha editorial atravessa todos os modos: **o MCP devolve aquilo que o manual diz; o LLM gera o conteúdo final**. Isso obriga a uma disciplina de rotulagem — cada afirmação na resposta vem marcada como `manual-grounded`, `observed`, `inferred` ou `not verified`. É a forma de manter visível o que veio da fonte, o que veio da observação directa, o que foi inferido pelo modelo e o que ainda está por confirmar.

---

## Tools, resources e prompts disponíveis

### Tools (operações)

| Tool | Modo | Propósito |
|---|---|---|
| `search_sbd_toe_manual` | CONSULT | Pesquisa narrativa/conceptual com citações |
| `consult_security_requirements` | CONSULT | Determinístico: requisitos + controlos activos por *risk level* (com *concerns*) |
| `map_sbd_toe_applicability` | CONSULT | Que capítulos/controlos se aplicam ao projecto |
| `get_sbd_toe_chapter_brief` | CONSULT | Resumo estruturado de um capítulo (fases, artefactos, tópicos) |
| `list_sbd_toe_chapters` | CONSULT | Índice dos capítulos com aplicabilidade |
| `query_sbd_toe_entities` | CONSULT | Procurar controlos (`CTRL-*`), artefactos (`ART-*`), práticas |
| `resolve_entities` | CONSULT | Filtro de baixo nível sobre a ontologia |
| `get_guide_by_role` | GUIDE | Práticas por *role* (developer, appsec-engineer, devops-sre, …) e fase do SDLC |
| `get_threat_landscape` | GUIDE | *Threats* relevantes por *risk level* e *concern* (com confiança de mitigação) |
| `plan_sbd_toe_repo_governance` | GUIDE | Lista artefactos requeridos pelo manual, agrupados por capítulo |
| `map_sbd_toe_review_scope` | GUIDE | Bundles a rever dado um conjunto de ficheiros alterados |
| `prepare_sbd_toe_codegen_context` | GUIDE | Contexto determinístico para *codegen* / *review* / *test-plan* (com `citation_map` fechado) |
| `answer_sbd_toe_manual` | CONSULT | Q&A *grounded* (degrada para retrieval sem *MCP sampling*) |
| `map_sbd_toe_regulatory_activation` | CONSULT | Framework (DORA/NIS2/CRA/RGPD) → capítulos do manual que activa |
| `get_sbd_toe_chapter_implementation_checklist` | IMPL | "Como implementar o cap. NN" — narrativa canon/20 |
| `get_sbd_toe_operating_model` | IMPL | RACI / governança / cadências (do *rollout playbook*) |
| `plan_sbd_toe_rollout` | IMPL | Roadmap por fases — ordem de implementação |
| `get_sbd_toe_verification_matrix` | IMPL | Lado EXPECTED: validação + evidência esperada por requisito |
| `assess_sbd_toe_implementation` | IMPL | Postura de KPIs vs *thresholds* por nível |
| `inspect_sbd_toe_retrieval` | DIAG | Diagnóstico do retriever |
| `generate_sbd_toe_skill` | SETUP | Skill/subagent por *role* (`format`, `flavour`) — ou o *agent guide* sem `role` |

### Resources (URIs `sbd://toe/*`)

| Resource URI | Conteúdo |
|---|---|
| `sbd://toe/agent-guide` | Guia operacional completo (LER PRIMEIRO) — modos, roteamento, padrões epistémicos |
| `sbd://toe/index-compact` | Mapa compacto JSON do manual |
| `sbd://toe/chapter-applicability/{riskLevel}` | Capítulos activos/condicionais/excluídos por *risk level* |
| `sbd://toe/ontology` | Ontologia YAML — `domain_mapping`, regras de inferência, *concerns* |
| `sbd://toe/grounded-codegen-guide` | Guia agente para `prepare_sbd_toe_codegen_context` (workflow + disciplina de output) |
| `sbd://toe/skill/{role}` | *Skill* de um *role* canónico (= `generate_sbd_toe_skill(role, format=skill)`) |
| `sbd://toe/subagent/{role}` | Definição de *subagent* de um *role* (= `format=subagent`, *harnessed*) |
| `sbd://toe/version` | Nome / versão / *provenance* (manual, KG, ontologia) do servidor a correr |

### Prompts

| Prompt | Quando |
|---|---|
| `setup_sbd_toe_agent(riskLevel, projectRole)` | Setup de sessão — capítulos activos + regras específicas do *risk level* |
| `ask_sbd_toe_manual(question)` | Q&A directo *grounded* |

---

## Vocabulário controlado

O servidor expõe valores **fechados** para parâmetros — usar fora destes valores não devolve resultados.

**Risk levels:**

| Nível | Âmbito |
|---|---|
| `L1` | Baixo risco — interno, sem dados sensíveis |
| `L2` | Médio risco — APIs públicas, dados de utilizador (desbloqueia capítulos 06 e 11) |
| `L3` | Alto risco — PII, sistemas regulados (desbloqueia adicionalmente o capítulo 13) |

**Concerns** (vocabulário ontológico, *lowercase* exacto):

`auth` · `logging` · `validation` · `api` · `config` · `integrity` · `distribution` · `ide` · `requirements` · `architecture` · `iac` · `encryption`

**Roles canónicos** (aceitam aliases):

`developer` · `appsec-engineer` · `arquitetos-software` · `devops-sre` · `qa` · `security-champion` · `product-owner` · `scrum-master` · `operacoes` · `grc-compliance` · `gestao-executiva` · `auditores` · `fornecedores-terceiros`

> São os **13 papéis canónicos** do manual ([Papéis e Responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)). O servidor aceita *aliases* comuns (ex.: `appsec`→`appsec-engineer`, `devops`/`sre`→`devops-sre`, `ciso`→`gestao-executiva`, `compliance`→`grc-compliance`) e resolve-os sempre para um destes 13.

---

## Convenções de identificadores

- **Requisitos**: `<CAT>-NNN` (ex.: `AUT-001`, `LOG-003`) — resolver por id exato via `query_sbd_toe_entities`
- **Controlos**: `CTRL-<domain>-<slug>-<hash>` (ex.: `CTRL-identity-gestao-de-identidades-acessos-e-ownership-d0919c69af`). **Não** existe a forma `CTRL-<capítulo>-<número>`.
- **Ameaças**: `MT-NNN` · **Artefactos**: `ART-<slug>-<hash>` — listar via `get_sbd_toe_chapter_brief`
- **Gramática de IDs** (*fullmatch*): `^(?:REQ-[A-Z]{3}-\d{3}|[A-Z]{3}-\d{3})$`. Identificadores **`EX-…`** (ex.: `EX-AUT-003`, `EX-REQ-010`) são **ilustrativos** e nunca resolvem; um `REQ-NNN` fora do catálogo devolve uma `citation_note` informativa (`status: "informative"`), não um requisito — ver [`query_sbd_toe_entities`](./05-tools-reference.md#query_sbd_toe_entities)
- Em modo `prepare_sbd_toe_codegen_context`, o `citation_map` devolvido é o **mundo fechado** de IDs válidos para a tarefa — IDs fora do `citation_map` **não existem** para efeitos de *grounding*.

---

## Padrão epistémico exigido

Toda a resposta gerada com base no MCP deve rotular cada afirmação:

| Rótulo | Significado |
|---|---|
| **manual-grounded** | Recuperado via MCP — citar `chapterId` ou ID de controlo |
| **observed** | Directamente visível no repositório/codebase |
| **inferred** | Conclusão lógica a partir de factos *grounded* ou *observed* — marcar explicitamente |
| **not verified** | Não confirmado — nunca apresentar como facto |

Em particular, o servidor **nunca** deve ser usado para declarar conformidade regulamentar com base em código gerado: o *overlay* regulamentar serve como *cross-check*, não como sinal de conformidade.

---

## Próximos passos

1. [Quickstart](./02-quickstart.md) — pôr a correr em 60 segundos (Claude Code, Cursor).
2. [Instalação por cliente](./03-instalacao.md) — Claude Code, Claude Desktop, Cursor, VS Code (Copilot), Windsurf, Zed.
3. [Skills e agentes](./04-skills-agentes.md) — onde guardar a *skill* e como inicializar a sessão.
4. [Tools reference](./05-tools-reference.md) e [resources / prompts](./06-resources-prompts.md) — API completa.
5. [Casos de uso](./casos-uso/) — receitas prontas: auditoria de PR, *codegen grounded*, *threat modeling*, *bootstrap* de governança, *onboarding*, *cross-check* normativo.
6. [Padrões avançados](./08-padroes-avancados.md) · [Disciplina epistémica](./09-epistemica-anti-patterns.md) · [Troubleshooting / FAQ](./10-troubleshooting-faq.md) · [Versionamento / roadmap](./11-versionamento-roadmap.md).
