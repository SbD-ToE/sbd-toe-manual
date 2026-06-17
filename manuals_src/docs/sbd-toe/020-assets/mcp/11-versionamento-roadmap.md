---
id: versionamento-roadmap
title: Versionamento e roadmap
description: Política de versionamento do SbD-ToE MCP, relação com versões do manual, e roadmap público.
sidebar_label: Versionamento & roadmap
sidebar_position: 11
tags:
  - mcp
  - versionamento
  - roadmap
  - changelog
---

# Versionamento e roadmap

O MCP server vive dois ritmos: o ritmo do *software* (releases no npm, *bugfixes*, novas tools) e o ritmo do *conteúdo* (cada *snapshot* traz consigo a versão do manual em que foi publicado). Os dois não andam sincronizados — e essa assimetria é a fonte da maior parte das perguntas de versionamento. Esta página explica como ler cada um, e o que está previsto a seguir.

## Política de versionamento

O servidor segue **SemVer 2.0.0** com a seguinte semântica:

| Tipo | Quando | Exemplos |
|---|---|---|
| **Major** (`X.0.0`) | *Breaking changes* na superfície MCP (tools renomeadas/removidas, parâmetros incompatíveis, resources renomeados) | `1.0.0` (futuro: estabilização) |
| **Minor** (`0.X.0`) | Novas tools, novos resources, novos parâmetros opcionais, novos *concerns* ou *roles* — backward-compatible | `0.10.0` (atual) |
| **Patch** (`0.0.X`) | Correções de bug, melhorias de retrieval, refinamento de outputs sem mudar schema | `0.9.1`, `0.9.2`, … |

O servidor está actualmente em **0.x** — pré-estável; *breaking changes* podem ocorrer em *minor* até `1.0.0`.

## Como saber a versão actual

Sempre via o resource:

```
sbd://toe/version
```

Ou via npm:

```bash
npm view @shiftleftpt/sbd-toe-mcp version
npm view @shiftleftpt/sbd-toe-mcp versions  # histórico completo
```

---

## Relação com versões do manual

| Componente | Versionamento | Onde |
|---|---|---|
| **Servidor MCP** | SemVer no npm | `@shiftleftpt/sbd-toe-mcp@<x.y.z>` |
| **Canon do manual** (caps. 00–14) | Tags Git no repositório do manual | `vX.Y.Z` em [SbD-ToE-Manual](https://github.com/Shiftleftpt/SbD-ToE-Manual/tags) |
| **Cross-checks normativos** | Aditivos sobre o canon — viajam dentro do *snapshot* MCP **se publicados antes** dele; caso contrário, vivem só no manual web até nova publicação | Manual web em `/sbd-toe/cross-check-normativo/`; cobertura actual no MCP: CRA, DORA, NIS2, GDPR, ENISA/CSA (✅) · AI Act (❌ no MCP `0.10.0`) |
| **Ontologia AppSec Core v1** | Versão pinned dentro do MCP | `sbd://toe/ontology` (declara a versão) |

**Importante** — não há mapeamento 1-para-1:

- Uma release de servidor (`0.10.0`) **não** corresponde a uma tag do manual (o *snapshot* actual traz o manual `v1.6.4`)
- O servidor traz uma *snapshot* do canon na altura da publicação, e um índice KG construído a partir dela
- O caso actual do **AI Act**: está presente no *snapshot* do manual (`v1.6.4`) mas o **índice KG** ainda não cobre o cross-check `ai-act/` — é uma lacuna de **indexação**, não de versão (ver [content lag](./10-troubleshooting-faq.md#content-lag))

---

## Release actual

`@shiftleftpt/sbd-toe-mcp@0.10.0` (latest no npm).

Inclui:
- Canon 00–14 + ontologia AppSec Core v1
- Cross-checks normativos **CRA**, **DORA**, **NIS2**, **GDPR**, **ENISA/CSA** indexados no KG
- **21 tools** — CONSULT + GUIDE + SETUP + DIAG + a **vista de implementação** (`get_sbd_toe_chapter_implementation_checklist`, `get_sbd_toe_operating_model`, `plan_sbd_toe_rollout`, `get_sbd_toe_verification_matrix`, `assess_sbd_toe_implementation`) e o overlay regulatório (`map_sbd_toe_regulatory_activation`) — ver [tools reference](./05-tools-reference.md)
- `generate_sbd_toe_skill` com `role` / `format` / `flavour` (role-skills) + resources `sbd://toe/{skill,subagent}/{role}`
- 8 resources `sbd://toe/*` — ver [resources & prompts](./06-resources-prompts.md)
- 2 prompts (`setup_sbd_toe_agent`, `ask_sbd_toe_manual`)
- `prepare_sbd_toe_codegen_context` com `mode` em `codegen`, `review` ou `test-plan`

Não inclui:
- Cross-check do **AI Act** (Reg. (UE) 2024/1689) — presente no *snapshot* do manual mas **ainda não indexado no KG** (ver [content lag](./10-troubleshooting-faq.md#content-lag))
- A *state layer* / *stateful-assess* (verificação contra o estado real de CI/repo) — ver roadmap
- Conteúdo das policies (`020-assets/policies/`) e dos addons (`addon/`) dos capítulos

---

## Roadmap (público)

> Roadmap indicativo, sem datas duras. Prioridades podem mudar conforme feedback.

### Entregue (`0.10.0`)

- **Vista de implementação (V5)** — checklist por capítulo, operating model, rollout, *verification matrix*, *assess* de KPIs.
- **Role-skills** — `generate_sbd_toe_skill` com `role` / `format` / `flavour` + resources `sbd://toe/{skill,subagent}/{role}`.
- **Overlay regulatório como tool** — `map_sbd_toe_regulatory_activation` (framework → capítulos activados).
- **Two-band `next` + coverage-preserving** — afordances de encadeamento e paginação sem truncar em todas as tools.

### Curto prazo

- **Estabilização para `1.0.0`** — fechar superfície de tools / resources, congelar *schemas*.
- **Refinamento de `prepare_sbd_toe_codegen_context`** — mais *stacks* suportadas no `regulatory_overlay`.
- **Documentação cliente-específica** — guias para Zed e Windsurf no GitHub do servidor.

### Médio prazo

- **Re-snapshot com AI Act incluído** — nova publicação npm que indexe o cross-check do AI Act (e quaisquer outros adicionados ao manual após `0.10.0`).
- **Indexação das policies** (`020-assets/policies/`) — útil para *bootstrap* de governança mais completo.
- **Tools de comparação** — *diff* entre versões do canon, *diff* entre risk levels.

### Longo prazo

- **State layer / *stateful-assess*** (tier Premium) — verificação contra o estado real de CI / repo / runtime (o lado *observed* que hoje fica `not verified — runtime`).
- **Protocolo de interação** — encadeamento dirigido pelo servidor para além da banda `next`.
- **Multi-language manual support** — quando o manual existir em outras línguas além de PT, expor selector via parameter.
- **Streaming responses** para outputs grandes (L3 *full coverage*).
- **MCP transport HTTP/SSE** além de stdio (consumo a partir de cloud agents).

---

## Changelog (resumo público)

Para o changelog detalhado por release, consultar:

- [GitHub Releases](https://github.com/Shiftleftpt/sbd-toe-mcp-poc/releases)
- npm: `npm view @shiftleftpt/sbd-toe-mcp time` (datas de cada versão)

### `0.10.0` — actual

Vista de implementação (checklist / operating model / rollout / verification matrix / assess de KPIs), role-skills (`role`/`format`/`flavour`), overlay regulatório como tool, banda `next` e outputs *coverage-preserving*. 21 tools, 8 resources, 2 prompts.

### `0.9.x`

Estabilização do conjunto `consult` + `guide` + `codegen`. Refinamento da ontologia. Disciplina de *epistemic labels* documentada no *agent guide*.

### `0.8.x` e anteriores

Iterações pré-publicação — adição progressiva de tools, refinamento de retrieval, primeiros clientes (Claude Code, Cursor).

---

## Como acompanhar

| Canal | Para |
|---|---|
| [GitHub Releases](https://github.com/Shiftleftpt/sbd-toe-mcp-poc/releases) | Notas detalhadas por versão |
| `npm view @shiftleftpt/sbd-toe-mcp` | Verificar última versão |
| `sbd://toe/version` em sessão | Saber o que o cliente está realmente a usar |
| [Manual web — Cross-check normativo](/sbd-toe/cross-check-normativo/intro) | Conteúdo regulatório actualizado (em particular, o AI Act enquanto não estiver no MCP) |

## Como contribuir

Issues e PRs no repositório do servidor: [Shiftleftpt/sbd-toe-mcp-poc](https://github.com/Shiftleftpt/sbd-toe-mcp-poc).

Para sugestões ao **conteúdo do manual** (capítulos 00–14, cross-checks, policies), o repositório alvo é [Shiftleftpt/SbD-ToE-Manual](https://github.com/Shiftleftpt/SbD-ToE-Manual). O MCP serve a *snapshot* do que está nesse repositório à data da publicação.

## A seguir

- [Casos de uso](./casos-uso/) — quando precisares de receitas prontas.
- [Troubleshooting / FAQ](./10-troubleshooting-faq.md) — quando algo não fizer sentido.
