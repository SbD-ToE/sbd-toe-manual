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
| **Minor** (`0.X.0`) | Novas tools, novos resources, novos parâmetros opcionais, novos *concerns* ou *roles* — backward-compatible | `0.9.0` (atual) |
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
| **Cross-checks normativos** | Aditivos sobre o canon — viajam dentro do *snapshot* MCP **se publicados antes** dele; caso contrário, vivem só no manual web até nova publicação | Manual web em `/sbd-toe/cross-check-normativo/`; cobertura actual no MCP: CRA, DORA, NIS2, GDPR, ENISA/CSA (✅) · AI Act (❌ no MCP `0.9.0`) |
| **Ontologia AppSec Core v1** | Versão pinned dentro do MCP | `sbd://toe/ontology` (declara a versão) |

**Importante** — não há mapeamento 1-para-1:

- Uma release de servidor (`0.9.0`) **não** corresponde a uma tag do manual (`v1.3.0`)
- O servidor traz uma *snapshot* do canon na altura da publicação
- Cross-checks adicionados ao manual web **depois** do *snapshot* do servidor não aparecem no MCP até nova publicação (caso actual: AI Act, em v1.3.0 do manual posterior a `0.9.0` do MCP — ver [content lag](./10-troubleshooting-faq.md#content-lag))

---

## Release actual

`@shiftleftpt/sbd-toe-mcp@0.9.0` (latest no npm).

Inclui:
- Canon 00–14 + ontologia AppSec Core v1
- Cross-checks normativos **CRA**, **DORA**, **NIS2**, **GDPR**, **ENISA/CSA** indexados no KG
- Conjunto completo de tools (CONSULT + GUIDE + SETUP + DIAG) — ver [tools reference](./05-tools-reference.md)
- 6 resources `sbd://toe/*` — ver [resources & prompts](./06-resources-prompts.md)
- 2 prompts (`setup_sbd_toe_agent`, `ask_sbd_toe_manual`)
- `prepare_sbd_toe_codegen_context` com `mode` em `codegen`, `review` ou `test-plan`

Não inclui:
- Cross-check do **AI Act** (Reg. (UE) 2024/1689) — adicionado ao manual web na v1.3.0, posterior ao *snapshot* do servidor (ver [content lag](./10-troubleshooting-faq.md#content-lag))
- Conteúdo das policies (`020-assets/policies/`)
- Conteúdo dos addons (`addon/`) dos capítulos

---

## Roadmap (público)

> Roadmap indicativo, sem datas duras. Prioridades podem mudar conforme feedback.

### Curto prazo

- **Estabilização para `1.0.0`** — fechar superfície de tools / resources, congelar *schemas*.
- **Refinamento de `prepare_sbd_toe_codegen_context`** — mais *stacks* suportadas no `regulatory_overlay`.
- **Documentação cliente-específica** — guias para Zed e Windsurf no GitHub do servidor.

### Médio prazo

- **Re-snapshot com AI Act incluído** — nova publicação npm que indexe o cross-check do AI Act (e quaisquer outros adicionados ao manual após `0.9.0`).
- **Indexação das policies** (`020-assets/policies/`) — útil para *bootstrap* de governança mais completo.
- **Tools de comparação** — *diff* entre versões do canon, *diff* entre risk levels.

### Longo prazo

- **Multi-language manual support** — quando o manual existir em outras línguas além de PT, expor selector via parameter.
- **Streaming responses** para outputs grandes (L3 *full coverage*).
- **MCP transport HTTP/SSE** além de stdio (consumo a partir de cloud agents).

---

## Changelog (resumo público)

Para o changelog detalhado por release, consultar:

- [GitHub Releases](https://github.com/Shiftleftpt/sbd-toe-mcp-poc/releases)
- npm: `npm view @shiftleftpt/sbd-toe-mcp time` (datas de cada versão)

### `0.9.x` — actual

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
