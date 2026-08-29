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
| **Minor** (`0.X.0`) | Novas tools, novos resources, novos parâmetros opcionais, novos *concerns* ou *roles* — backward-compatible | `0.10.0` |
| **Patch** (`0.0.X`) | Correções de bug, melhorias de retrieval, refinamento de outputs sem mudar schema | `0.10.2` (atual), `0.10.1` |

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
| **Cross-checks normativos** | Aditivos sobre o canon — viajam dentro do *snapshot* MCP **se publicados antes** dele; caso contrário, vivem só no manual web até nova publicação | Manual web em `/sbd-toe/cross-check-normativo/`; cobertura actual no MCP (`0.10.2`): CRA, DORA, NIS2, GDPR, AI Act, ENISA/CSA (✅ — os seis) |
| **Ontologia AppSec Core v1** | Versão pinned dentro do MCP | `sbd://toe/ontology` (declara a versão) |

**Importante** — não há mapeamento 1-para-1:

- Uma release de servidor (`0.10.2`) **não** corresponde a uma tag do manual (o *snapshot* actual traz o manual `v1.7.0`, sobre o KG formal `v1.6.0`)
- O servidor traz uma *snapshot* do canon na altura da publicação, e um índice KG construído a partir dela
- Exemplo histórico: entre `0.10.0` e `0.10.2`, o cross-check do **AI Act** esteve no *snapshot* do manual mas fora do índice KG — uma lacuna de **indexação**, não de versão; resolvido em `0.10.2` (ver [content lag](./10-troubleshooting-faq.md#content-lag))

---

## Release actual

`@shiftleftpt/sbd-toe-mcp@0.10.2` (latest no npm) — *snapshot* do manual `v1.7.0`, KG formal `v1.6.0` (contrato de consumo v1.11).

Inclui:
- Canon 00–14, fundamentos (incluindo os [cinco macro-processos](/sbd-toe/sbd-manual/fundamentos/macro-processos)), policies e addons dos capítulos, ontologia AppSec Core v1
- Cross-checks normativos **CRA**, **DORA**, **NIS2**, **GDPR**, **AI Act** e **ENISA/CSA** — os seis indexados no KG (narrativa citável via `search_sbd_toe_manual` e overlay regulatório via `map_sbd_toe_regulatory_activation` / `resolve_entities`)
- **256 requisitos** em 27 categorias (inclui `REQ-AGN-001…004` e `OPS-015`), com ligações requisito→controlo completas — `coverage_gaps.requirements_without_control_link` devolve `count: 0` em L1/L2/L3
- Concern **`agents`** (enum fechado de 13 valores) e campo `coverage_gaps` em `consult_security_requirements`; `declared_gap` / `citation_note` (`status: "informative"`) em `query_sbd_toe_entities` / `resolve_entities`; gramática de IDs *fullmatch* — ver [tools reference](./05-tools-reference.md)
- **21 tools** (inalterado desde `0.10.0`) — CONSULT + GUIDE + SETUP + DIAG + a **vista de implementação** (`get_sbd_toe_chapter_implementation_checklist`, `get_sbd_toe_operating_model`, `plan_sbd_toe_rollout`, `get_sbd_toe_verification_matrix`, `assess_sbd_toe_implementation`) e o overlay regulatório (`map_sbd_toe_regulatory_activation`) — ver [tools reference](./05-tools-reference.md)
- `generate_sbd_toe_skill` com `role` / `format` / `flavour` (role-skills) + resources `sbd://toe/{skill,subagent}/{role}`
- 8 resources `sbd://toe/*` — ver [resources & prompts](./06-resources-prompts.md)
- 3 prompts (`setup_sbd_toe_agent`, `ask_sbd_toe_manual`, `prepare_grounded_codegen`)
- `prepare_sbd_toe_codegen_context` com `mode` em `codegen`, `review` ou `test-plan`

Não inclui:
- A *state layer* / *stateful-assess* (verificação contra o estado real de CI/repo) — ver roadmap
- Conteúdo do manual posterior ao *snapshot* `v1.7.0` — vive só no manual web até nova publicação (ver [content lag](./10-troubleshooting-faq.md#content-lag))

---

## Roadmap (público)

> Roadmap indicativo, sem datas duras. Prioridades podem mudar conforme feedback.

### Entregue (`0.10.x`)

- **Vista de implementação (V5)** — checklist por capítulo, operating model, rollout, *verification matrix*, *assess* de KPIs.
- **Role-skills** — `generate_sbd_toe_skill` com `role` / `format` / `flavour` + resources `sbd://toe/{skill,subagent}/{role}`.
- **Overlay regulatório como tool** — `map_sbd_toe_regulatory_activation` (framework → capítulos activados).
- **Two-band `next` + coverage-preserving** — afordances de encadeamento e paginação sem truncar em todas as tools.
- **`0.10.2` — alinhamento ao KG formal `v1.6.0` / manual `v1.7.0`** — AI Act e ENISA/CSA indexados; `REQ-AGN-001…004` e `OPS-015` servidos; `coverage_gaps` e concern `agents`; `declared_gap` / `citation_note`; gramática de IDs *fullmatch*.
- **Policies e addons servidos** — `020-assets/policies/` e `addon/` dos capítulos (incluindo `macro-processos`) estão nos *chunks* consultáveis.

### Curto prazo

- **Estabilização para `1.0.0`** — fechar superfície de tools / resources, congelar *schemas*.
- **Refinamento de `prepare_sbd_toe_codegen_context`** — mais *stacks* suportadas no `regulatory_overlay`.
- **Documentação cliente-específica** — guias para Zed e Windsurf no GitHub do servidor.

### Médio prazo

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

### `0.10.2` — actual

Alinhamento ao KG formal `v1.6.0` e ao manual `v1.7.0`: AI Act e ENISA/CSA indexados (os seis cross-checks), `REQ-AGN-001…004` e `OPS-015` servidos, ligações requisito→controlo completas com `coverage_gaps` declarado, concern `agents` (13 valores), `declared_gap` / `citation_note` em `query_sbd_toe_entities` / `resolve_entities`, gramática de IDs *fullmatch* (`EX-…` nunca resolve). 21 tools, 8 resources, 3 prompts. (`0.10.1`: re-*pin* intermédio ao mesmo bundle, sem alterações de superfície.)

### `0.10.0`

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
| [Manual web — Cross-check normativo](/sbd-toe/cross-check-normativo/intro) | Conteúdo regulatório actualizado |

## Como contribuir

Issues e PRs no repositório do servidor: [Shiftleftpt/sbd-toe-mcp-poc](https://github.com/Shiftleftpt/sbd-toe-mcp-poc).

Para sugestões ao **conteúdo do manual** (capítulos 00–14, cross-checks, policies), o repositório alvo é [Shiftleftpt/SbD-ToE-Manual](https://github.com/Shiftleftpt/SbD-ToE-Manual). O MCP serve a *snapshot* do que está nesse repositório à data da publicação.

## A seguir

- [Casos de uso](./casos-uso/) — quando precisares de receitas prontas.
- [Troubleshooting / FAQ](./10-troubleshooting-faq.md) — quando algo não fizer sentido.
