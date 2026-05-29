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

Quando um agente de código quer aplicar o SbD-ToE, tem duas opções: ou *adivinha* o manual a partir do que treinou, ou *consulta-o* numa fonte que devolve respostas estruturadas com identificadores citáveis. O **`@shiftleftpt/sbd-toe-mcp`** existe para tornar a segunda opção trivial.

É o servidor [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) oficial do SbD-ToE. Expõe o manual (capítulos 00–14), a ontologia *AppSec Core v1* e os cross-checks normativos publicados através de **tools, resources e prompts MCP** — para que o Claude, o GitHub Copilot, o Cursor, o Windsurf, o Zed (ou qualquer outro cliente MCP) parem de citar o manual de memória e passem a pedir-lho à fonte, com IDs reais. Em prática: cada `CTRL-*`, `REQ-*`, `THR-*` ou `ART-*` que o agente refere passa a ser verificável.

| Atributo | Valor |
|---|---|
| **Package** | [`@shiftleftpt/sbd-toe-mcp`](https://www.npmjs.com/package/@shiftleftpt/sbd-toe-mcp) (npm) |
| **Repositório** | [`Shiftleftpt/sbd-toe-mcp-poc`](https://github.com/Shiftleftpt/sbd-toe-mcp-poc) (GitHub) |
| **Binário** | `sbd-toe-mcp` |
| **Requisitos** | Node.js ≥ 20.9.0 |
| **Licenciamento** | Apache-2.0 (código/runtime) · CC BY-SA 4.0 (snapshots de manual incluídos) |
| **Transporte** | `stdio` (compatível com todos os clientes MCP padrão) |

:::info Versão actual e *content lag*
A versão actualmente publicada (**`@shiftleftpt/sbd-toe-mcp@0.9.0`**) inclui o **canon (capítulos 00–14)**, a **ontologia AppSec Core v1** e os cross-checks normativos **CRA**, **DORA**, **NIS2**, **GDPR** e **ENISA/CSA** — todos indexados no KG e citáveis via `search_sbd_toe_manual`.

**Excepção:** o cross-check do **AI Act** (Regulamento (UE) 2024/1689), adicionado ao manual web na release **v1.3.0** posterior ao *snapshot* do servidor, ainda **não está indexado**. Para perguntas sobre AI Act, consultar directamente o manual web em [`/sbd-toe/cross-check-normativo/ai-act/intro`](/sbd-toe/cross-check-normativo/ai-act/intro) até nova publicação do MCP.
:::

---

## Para que serve

Há três tipos de momento em que um agente recorre ao SbD-ToE — perceber **o que o manual diz**, perceber **como aplicar o que o manual diz**, e configurar-se a si próprio para o fazer bem. O MCP atende cada um com um conjunto distinto de *tools*:

| Modo | Quando usar | Tools-chave |
|---|---|---|
| **CONSULT** | "O que o manual diz?", "O que se aplica a este projecto?", "Que controlos estão activos?" | `consult_security_requirements`, `search_sbd_toe_manual`, `map_sbd_toe_applicability`, `query_sbd_toe_entities` |
| **GUIDE** | "Como implemento isto?", "Como reviso este PR?", "Que threats aplicam aqui?" | `get_guide_by_role`, `get_threat_landscape`, `plan_sbd_toe_repo_governance`, `map_sbd_toe_review_scope`, `prepare_sbd_toe_codegen_context` |
| **SETUP** | "Configurar o meu cliente AI para usar o SbD-ToE" | `generate_sbd_toe_skill`, `setup_sbd_toe_agent` |

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
| `get_guide_by_role` | GUIDE | Práticas por *role* (developer, appsec, devops, …) e fase do SDLC |
| `get_threat_landscape` | GUIDE | *Threats* relevantes por *risk level* e *concern* (com confiança de mitigação) |
| `plan_sbd_toe_repo_governance` | GUIDE | Lista artefactos requeridos pelo manual, agrupados por capítulo |
| `map_sbd_toe_review_scope` | GUIDE | Bundles a rever dado um conjunto de ficheiros alterados |
| `prepare_sbd_toe_codegen_context` | GUIDE | Contexto determinístico para *codegen* / *review* / *test-plan* (com `citation_map` fechado) |
| `inspect_sbd_toe_retrieval` | DIAG | Diagnóstico do retriever |
| `generate_sbd_toe_skill` | SETUP | Devolve o conteúdo canónico da *skill* a guardar no cliente |

### Resources (URIs `sbd://toe/*`)

| Resource URI | Conteúdo |
|---|---|
| `sbd://toe/agent-guide` | Guia operacional completo (LER PRIMEIRO) — modos, roteamento, padrões epistémicos |
| `sbd://toe/index-compact` | Mapa compacto JSON do manual |
| `sbd://toe/chapter-applicability/{riskLevel}` | Capítulos activos/condicionais/excluídos por *risk level* |
| `sbd://toe/ontology` | Ontologia YAML — `domain_mapping`, regras de inferência, *concerns* |
| `sbd://toe/grounded-codegen-guide` | Guia agente para `prepare_sbd_toe_codegen_context` (workflow + disciplina de output) |
| `sbd://toe/version` | Nome / versão / descrição do servidor a correr |

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

`developer` · `appsec` · `devops` · `grc` · `qa` · `security_champion` · `software_architect` · `product_owner` · `scrum_master` · `team_lead` · `ciso` · `executive_management` · `ops` · `pentester` · `compliance` · `auditor` · `ir` · `sre`

---

## Convenções de identificadores

- **Artefactos**: `ART-<chapterId>-<name>` — listar via `get_sbd_toe_chapter_brief`
- **Controlos**: `CTRL-<chapter>-<number>` — pesquisar via `query_sbd_toe_entities`
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
