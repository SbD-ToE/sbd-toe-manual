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

## Política de versionamento {#política-de-versionamento}

O servidor segue **SemVer 2.0.0** com a seguinte semântica:

| Tipo | Quando | Exemplos |
|---|---|---|
| **Major** (`X.0.0`) | *Breaking changes* na superfície MCP (tools renomeadas/removidas, parâmetros incompatíveis, resources renomeados) | A passagem a `1.0.0` (estabilização) |
| **Minor** (`0.X.0`) | Novas tools, novos resources, novos parâmetros opcionais, novos *concerns* ou *roles* — backward-compatible | Uma tool ou um resource novos |
| **Patch** (`0.0.X`) | Correções de bug, melhorias de retrieval, refinamento de outputs sem mudar schema | Uma correção de retrieval |

Enquanto a versão *major* for `0`, o servidor é pré-estável: *breaking changes* podem ocorrer em *minor* até `1.0.0`.

## Como saber a versão actual {#como-saber-a-versão-actual}

Sempre via o resource:

```
sbd://toe/version
```

Ou via npm:

```bash
npm view @shiftleftpt/sbd-toe-mcp version
npm view @shiftleftpt/sbd-toe-mcp versions  # histórico completo
```

O que a versão servida contém está em `sbd://toe/version`; o que cada release mudou está no CHANGELOG do servidor e nas [GitHub Releases de `SbD-ToE/sbd-toe-mcp`](https://github.com/SbD-ToE/sbd-toe-mcp/releases). A lista de tools, resources e *prompts* da versão instalada é a que o próprio servidor devolve (`tools/list`, `resources/list`, `prompts/list`).

---

## Relação com versões do manual {#relação-com-versões-do-manual}

| Componente | Versionamento | Onde |
|---|---|---|
| **Servidor MCP** | SemVer no npm | `@shiftleftpt/sbd-toe-mcp@<x.y.z>` |
| **Canon do manual** (caps. 00–14) | Tags Git no repositório do manual | `vX.Y.Z` em [`SbD-ToE/sbd-toe-manual`](https://github.com/SbD-ToE/sbd-toe-manual/tags) |
| **Cross-checks normativos** | Aditivos sobre o canon — viajam dentro do *snapshot* MCP **se publicados antes** dele; caso contrário, vivem só no manual web até nova publicação | Manual web em `/sbd-toe/cross-check-normativo/`; a cobertura do *snapshot* servido está em `sbd://toe/version` |
| **Ontologia AppSec Core v1** | Versão pinned dentro do MCP | `sbd://toe/ontology` (declara a versão) |

**Importante** — não há mapeamento 1-para-1:

- Uma release de servidor **não** corresponde a uma tag do manual: cada release traz o manual e o KG da altura da publicação, e `sbd://toe/version` diz quais
- O servidor traz uma *snapshot* do canon na altura da publicação, e um índice KG construído a partir dela
- Um conteúdo pode estar no *snapshot* do manual e, ainda assim, fora do índice KG — é uma lacuna de **indexação**, não de versão (ver [content lag](./10-troubleshooting-faq.md#content-lag))

---

## Roadmap (público) {#roadmap-público}

> Roadmap indicativo, sem datas duras. Prioridades podem mudar conforme feedback.

### Curto prazo {#curto-prazo}

- **Estabilização para `1.0.0`** — fechar superfície de tools / resources, congelar *schemas*.
- **Refinamento de `prepare_sbd_toe_codegen_context`** — mais *stacks* suportadas no `regulatory_overlay`.
- **Documentação cliente-específica** — guias para Zed e Windsurf no GitHub do servidor.

### Médio prazo {#médio-prazo}

- **Tools de comparação** — *diff* entre versões do canon, *diff* entre risk levels.

### Longo prazo {#longo-prazo}

- **State layer / *stateful-assess*** (tier Premium) — verificação contra o estado real de CI / repo / runtime (o lado *observed* que hoje fica `not verified — runtime`).
- **Protocolo de interação** — encadeamento dirigido pelo servidor para além da banda `next`.
- **Multi-language manual support** — quando o manual existir em outras línguas além de PT, expor selector via parameter.
- **Streaming responses** para outputs grandes (L3 *full coverage*).
- **MCP transport HTTP/SSE** além de stdio (consumo a partir de cloud agents).

---

## Como acompanhar {#como-acompanhar}

| Canal | Para |
|---|---|
| [GitHub Releases](https://github.com/SbD-ToE/sbd-toe-mcp/releases) e o CHANGELOG do [repositório do servidor](https://github.com/SbD-ToE/sbd-toe-mcp) | O que cada release mudou |
| `npm view @shiftleftpt/sbd-toe-mcp` | Verificar última versão |
| `npm view @shiftleftpt/sbd-toe-mcp time` | Datas de cada versão |
| `sbd://toe/version` em sessão | Saber o que o cliente está realmente a usar |
| [Manual web — Cross-check normativo](/sbd-toe/cross-check-normativo/intro) | Conteúdo regulatório actualizado |

## Como contribuir {#como-contribuir}

Issues e PRs no repositório do servidor: [`SbD-ToE/sbd-toe-mcp`](https://github.com/SbD-ToE/sbd-toe-mcp).

Para sugestões ao **conteúdo do manual** (capítulos 00–14, cross-checks, policies), o repositório alvo é [`SbD-ToE/sbd-toe-manual`](https://github.com/SbD-ToE/sbd-toe-manual). O MCP serve a *snapshot* do que está nesse repositório à data da publicação.

## A seguir {#a-seguir}

- [Casos de uso](./casos-uso/) — quando precisares de receitas prontas.
- [Troubleshooting / FAQ](./10-troubleshooting-faq.md) — quando algo não fizer sentido.
