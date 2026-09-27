---
id: versionamento-roadmap
title: Versioning and roadmap
description: Versioning policy of the SbD-ToE MCP, relationship with Manual versions, and public roadmap.
sidebar_label: Versioning & roadmap
sidebar_position: 11
tags:
  - mcp
  - versionamento
  - roadmap
  - changelog
translation:
  source_locale: pt
  source_path: 020-assets/mcp/11-versionamento-roadmap.md
  source_sha256: 0142eff88bfa93cfb678feb12ff3c0b460bff0b9a7ff72859aa71bc367597656
  source_commit: 4e04c6c26f9325b8a3515d4ccd3b126f58be3b1e
  target_sha256: 4857d9fa8e3a9864777201cb1fb2a116458d13d89ea40b7925212415d2e4c8ff
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 211df96a27d713b5934d7534d61f1972d877902236e63b858563d206c67ccaa8
  glossary_keys: [appsec_core, framework_source_corpus, gap_family, mapping, mcp, normative_empirical, practitioner_manual, sbdtoe_sbd, verification_taxonomy]
  glossary_sha256: 5793b5a09cd27ec56e3ec6a68aa85fc9ad37efee803fbffcd1289466b74ea6a7
  translated_at: 2026-09-26T14:55:24Z
  reviewed_by: null
---

# Versioning and roadmap

The MCP server lives by two rhythms: the rhythm of the *software* (releases on npm, *bugfixes*, new tools) and the rhythm of the *content* (each *snapshot* carries the version of the Manual at which it was published). The two do not move in sync — and that asymmetry is the source of most versioning questions. This page explains how to read each one, and what is planned next.

## Versioning policy {#política-de-versionamento}

The server follows **SemVer 2.0.0** with the following semantics:

| Type | When | Examples |
|---|---|---|
| **Major** (`X.0.0`) | *Breaking changes* to the MCP surface (tools renamed/removed, incompatible parameters, resources renamed) | The move to `1.0.0` (stabilisation) |
| **Minor** (`0.X.0`) | New tools, new resources, new optional parameters, new *concerns* or *roles* — backward-compatible | A new tool or a new resource |
| **Patch** (`0.0.X`) | Bug fixes, retrieval improvements, refinement of outputs without changing the schema | A retrieval fix |

While the *major* version is `0`, the server is pre-stable: *breaking changes* may occur in a *minor* until `1.0.0`.

## How to find the current version {#como-saber-a-versão-actual}

Always via the resource:

```
sbd://toe/version
```

Or via npm:

```bash
npm view @shiftleftpt/sbd-toe-mcp version
npm view @shiftleftpt/sbd-toe-mcp versions  # histórico completo
```

What the served version contains is in `sbd://toe/version`; what each release changed is in the server's CHANGELOG and in the [GitHub Releases of `SbD-ToE/sbd-toe-mcp`](https://github.com/SbD-ToE/sbd-toe-mcp/releases). The list of tools, resources and *prompts* of the installed version is the one the server itself returns (`tools/list`, `resources/list`, `prompts/list`).

---

## Relationship with Manual versions {#relação-com-versões-do-manual}

| Component | Versioning | Where |
|---|---|---|
| **MCP server** | SemVer on npm | `@shiftleftpt/sbd-toe-mcp@<x.y.z>` |
| **Manual canon** (Ch. 00–14) | Git tags in the Manual repository | `vX.Y.Z` in [`SbD-ToE/sbd-toe-manual`](https://github.com/SbD-ToE/sbd-toe-manual/tags) |
| **Normative cross-checks** | Additive to the canon — they travel inside the MCP *snapshot* **if published before** it; otherwise, they live only in the web Manual until the next publication | Web Manual at `/sbd-toe/cross-check-normativo/`; the coverage of the served *snapshot* is in `sbd://toe/version` |
| **AppSec Core v1 ontology** | Version pinned inside the MCP | `sbd://toe/ontology` (declares the version) |

**Important** — there is no one-to-one mapping:

- A server release does **not** correspond to a Manual tag: each release carries the Manual and the KG as they stood at publication, and `sbd://toe/version` states which
- The server carries a *snapshot* of the canon at the time of publication, and a KG index built from it
- A piece of content may be in the Manual *snapshot* and, even so, outside the KG index — that is an **indexing** gap, not a version gap (see [content lag](./10-troubleshooting-faq.md#content-lag))

---

## Roadmap (public) {#roadmap-público}

> Indicative roadmap, with no hard dates. Priorities may change according to feedback.

### Short term {#curto-prazo}

- **Stabilisation for `1.0.0`** — close the tools / resources surface, freeze the *schemas*.
- **Refinement of `prepare_sbd_toe_codegen_context`** — more *stacks* supported in the `regulatory_overlay`.
- **Client-specific documentation** — guides for Zed and Windsurf on the server's GitHub.

### Medium term {#médio-prazo}

- **Comparison tools** — *diff* between canon versions, *diff* between risk levels.

### Long term {#longo-prazo}

- **State layer / *stateful-assess*** (Premium tier) — verification against the real state of CI / repo / runtime (the *observed* side that today remains `not verified — runtime`).
- **Interaction protocol** — server-driven chaining beyond the `next` band.
- **Multi-language manual support** — once the Manual exists in languages other than PT, expose a selector via parameter.
- **Streaming responses** for large outputs (L3 *full coverage*).
- **MCP transport HTTP/SSE** in addition to stdio (consumption from cloud agents).

---

## How to keep up {#como-acompanhar}

| Channel | For |
|---|---|
| [GitHub Releases](https://github.com/SbD-ToE/sbd-toe-mcp/releases) and the CHANGELOG of the [server repository](https://github.com/SbD-ToE/sbd-toe-mcp) | What each release changed |
| `npm view @shiftleftpt/sbd-toe-mcp` | Checking the latest version |
| `npm view @shiftleftpt/sbd-toe-mcp time` | Dates of each version |
| `sbd://toe/version` in session | Knowing what the client is actually using |
| [Web Manual — Normative cross-check](/sbd-toe/cross-check-normativo/intro) | Up-to-date regulatory content |

## How to contribute {#como-contribuir}

Issues and PRs in the server repository: [`SbD-ToE/sbd-toe-mcp`](https://github.com/SbD-ToE/sbd-toe-mcp).

For suggestions on the **Manual content** (chapters 00–14, cross-checks, policies), the target repository is [`SbD-ToE/sbd-toe-manual`](https://github.com/SbD-ToE/sbd-toe-manual). The MCP serves the *snapshot* of what is in that repository at the date of publication.

## Next {#a-seguir}

- [Use cases](./casos-uso/) — when ready-made recipes are needed.
- [Troubleshooting / FAQ](./10-troubleshooting-faq.md) — when something does not make sense.
