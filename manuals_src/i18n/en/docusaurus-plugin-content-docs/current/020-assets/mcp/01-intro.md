---
id: intro
title: MCP Server — Introduction
description: Official MCP server of the SbD-ToE — connecting Claude, Copilot, Cursor and other MCP clients to the Manual with deterministic grounding.
sidebar_label: Introduction
sidebar_position: 1
tags:
  - mcp
  - integracao
  - tooling
  - sbd-toe
translation:
  source_locale: pt
  source_path: 020-assets/mcp/01-intro.md
  source_sha256: 7d558250f0aa5e109f5539269f8e9fdc24bf0ee2e6cae00fec5a31cb6d2212fd
  source_commit: 4e04c6c26f9325b8a3515d4ccd3b126f58be3b1e
  target_sha256: ce9f4282a412f9145f3ee1c373adbb32e13461ac0488cebf18fb36a0c1375092
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 211df96a27d713b5934d7534d61f1972d877902236e63b858563d206c67ccaa8
  glossary_keys: [appsec_core, chapter_role, deterministic, discipline, framework_source_corpus, lifecycle_phase, llm, macro_processo, mcp, mcp_reading_normativa, mcp_reading_programa, normative_empirical, open_closed_world, papel_suporte, practitioner_manual, programme_line, requirement_runtime, sbdtoe_sbd, threat, validation_evaluation, verification_taxonomy]
  glossary_sha256: 389740950037ea3b1d08520e6fa3d3754c24260c08286864ac0163a795cedcd9
  translated_at: 2026-09-26T14:55:13Z
  reviewed_by: null
---

# MCP Server (SbD-ToE)

When an agent is asked to write secure code, it has two options: either it falls back on what it retained from training — a plausible approximation, but without anchor or source —, or it consults the Manual through a source that returns requirements and controls with citable identifiers. The **`@shiftleftpt/sbd-toe-mcp`** exists to make the second option trivial.

It is the official [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server of the SbD-ToE. It exposes the Manual (chapters 00–14), the *AppSec Core v1* ontology and the published normative cross-checks through **MCP tools, resources and prompts** — so that Claude, GitHub Copilot, Cursor, Windsurf, Zed (or any other MCP client) stop answering from what they were trained on and start asking the source, at the moment they write, with real IDs. In practice: every requirement, control, threat or artefact the agent refers to becomes verifiable.

| Attribute | Value |
|---|---|
| **Package** | [`@shiftleftpt/sbd-toe-mcp`](https://www.npmjs.com/package/@shiftleftpt/sbd-toe-mcp) (npm) |
| **Repository** | [`SbD-ToE/sbd-toe-mcp`](https://github.com/SbD-ToE/sbd-toe-mcp) (GitHub) |
| **Binary** | `sbd-toe-mcp` |
| **Requirements** | Node.js ≥ 20.9.0 |
| **Licensing** | Apache-2.0 (code/runtime) · CC BY-SA 4.0 (included Manual snapshots) |
| **Transport** | `stdio` (compatible with every standard MCP client) |

:::info Served version and *content lag*
The server serves a dated *snapshot* of the Manual and the KG: the **canon (chapters 00–14)** and the fundamentals (including the [five macro-processes](/sbd-toe/sbd-manual/fundamentos/macro-processos)), the **AppSec Core v1 ontology** and the published normative cross-checks — **CRA**, **DORA**, **NIS2**, **GDPR**, **AI Act** and **ENISA/CSA** —, indexed and citable.

The exact version — server, Manual, KG, ontology and contract — is in `sbd://toe/version`; the history, in the server's CHANGELOG and in the GitHub Releases of [`SbD-ToE/sbd-toe-mcp`](https://github.com/SbD-ToE/sbd-toe-mcp/releases). If the web Manual has content later than the *snapshot*, see [content lag](./10-troubleshooting-faq.md#content-lag).
:::

---

## What it is for {#para-que-serve}

There are three kinds of moment in which an agent turns to the SbD-ToE — understanding **what the Manual says**, understanding **how to apply what the Manual says**, and configuring itself to do it well. The MCP serves each with a distinct set of *tools*:

| Mode | When to use | Key tools |
|---|---|---|
| **CONSULT** | "What does the Manual say?", "What applies to this project?", "Which controls are active?" | `consult_security_requirements`, `search_sbd_toe_manual`, `explain_sbd_toe_topic`, `map_sbd_toe_applicability`, `query_sbd_toe_entities` |
| **GUIDE** | "Which requirements apply to this task?", "How do I implement this?", "How do I review this PR?", "Which threats apply here?" | `select_sbd_toe_requirements` (entry point), `get_guide_by_role`, `get_threat_landscape`, `plan_sbd_toe_repo_governance`, `map_sbd_toe_review_scope`, `prepare_sbd_toe_codegen_context` |
| **NORMATIVA** | "Which playbook does the Manual publish for this legal instrument?" | `get_sbd_toe_playbook` |
| **PROGRAMA** | "How is the SbD programme organised within an organisation?" | `get_sbd_toe_macro_processes` |
| **SETUP** | "Configure my AI client to use the SbD-ToE" | `generate_sbd_toe_skill` (tool) and the *prompt* `setup_sbd_toe_agent` |
| **IMPL** (implementation view) | "How to stand up and govern SbD?" — checklist per chapter, operating model, rollout, verification, KPIs | `get_sbd_toe_chapter_implementation_checklist`, `get_sbd_toe_chapter_capability`, `get_sbd_toe_operating_model`, `plan_sbd_toe_rollout`, `get_sbd_toe_verification_matrix`, `assess_sbd_toe_implementation` |

The implementation view (IMPL) answers *how to stand up and govern* SbD in an organisation — distinct from the operational view (GUIDE), which says *what to do in each phase of the SDLC*.

For a concrete task, the entry point is `select_sbd_toe_requirements` — the tool that the served descriptions mark as *START HERE*. It works by **declarative contract**: the agent declares what it has read (*risk level*, *concerns*, exposure, data sensitivity, technologies, changed files) and the server selects the requirements deterministically. The `task` is recorded, but not interpreted; without a declaration, the response is `needs_input`, with the accepted vocabulary. See the [reference](./05-tools-reference.md).

The editorial line runs through every mode: **the MCP returns what the Manual says; the LLM generates the final content**. That demands a labelling discipline — every claim in the response comes marked as `manual-grounded`, `observed`, `inferred` or `not verified`. It is the way to keep visible what came from the source, what came from direct observation, what was inferred by the model and what is still to be confirmed.

---

## Available tools, resources and prompts {#tools-resources-e-prompts-disponíveis}

### Tools (operations) {#tools-operações}

| Tool | Mode | Purpose |
|---|---|---|
| `select_sbd_toe_requirements` | GUIDE | Entry point (*START HERE*): declarative, deterministic and reproducible selection of the requirements from what the agent declares; without a declaration → `needs_input` |
| `search_sbd_toe_manual` | CONSULT | Narrative/conceptual search with citations (non-normative) |
| `explain_sbd_toe_topic` | CONSULT | CONSULT reading — parameters and response in the served description (`tools/list`) |
| `consult_security_requirements` | CONSULT | Deterministic: requirements + active controls by *risk level* (with *concerns*) |
| `map_sbd_toe_applicability` | CONSULT | What each chapter demands for the project's *risk level* and profile |
| `get_sbd_toe_chapter_brief` | CONSULT | Structured summary of a chapter (phases, artefacts, topics) |
| `list_sbd_toe_chapters` | CONSULT | Index of chapters with applicability |
| `query_sbd_toe_entities` | CONSULT | Search controls (`CTRL-*`), artefacts (`ART-*`), practices |
| `resolve_entities` | CONSULT | Low-level filter over the ontology |
| `get_guide_by_role` | GUIDE | Practices by *role* (developer, appsec-engineer, devops-sre, …) and SDLC phase |
| `get_threat_landscape` | GUIDE | Relevant *threats* by *risk level* and *concern* (with mitigation confidence) |
| `plan_sbd_toe_repo_governance` | GUIDE | Lists the artefacts required by the Manual, grouped by chapter |
| `map_sbd_toe_review_scope` | GUIDE | Bundles to review given a set of changed files |
| `prepare_sbd_toe_codegen_context` | GUIDE | Deterministic context for *codegen* / *review* / *test-plan* (with `citations` — the closed-world set of legal ids) |
| `answer_sbd_toe_manual` | CONSULT | *Grounded* Q&A (degrades to retrieval without *MCP sampling*) |
| `map_sbd_toe_regulatory_activation` | CONSULT | Framework (DORA/NIS2/CRA/GDPR) → Manual chapters it activates |
| `get_sbd_toe_playbook` | NORMATIVA | Playbooks published per legal instrument, with declared authority; `no_cross_check` for frameworks without a published cross-check (ISO, PCI, SOC2, …) |
| `get_sbd_toe_macro_processes` | PROGRAMA | PROGRAMA reading — parameters and response in the served description (`tools/list`) |
| `get_sbd_toe_chapter_implementation_checklist` | IMPL | "How to implement Ch. NN" — canon/20 narrative |
| `get_sbd_toe_chapter_capability` | IMPL | IMPL reading — parameters and response in the served description (`tools/list`) |
| `get_sbd_toe_operating_model` | IMPL | RACI / governance / cadences (from the *rollout playbook*) |
| `plan_sbd_toe_rollout` | IMPL | Roadmap by phases — order of implementation |
| `get_sbd_toe_verification_matrix` | IMPL | EXPECTED side: validation + expected evidence per requirement |
| `assess_sbd_toe_implementation` | IMPL | KPI posture vs *thresholds* per level |
| `inspect_sbd_toe_retrieval` | DIAG | Retriever diagnostics |
| `generate_sbd_toe_skill` | SETUP | Skill/subagent per *role* (`format`, `flavour`) — or the *agent guide* without `role` |
| `read_sbd_toe_resource` | — | Reads an `sbd://toe/*` resource by URI (e.g. `read_sbd_toe_resource(uri="sbd://toe/version")`) |
| `trace_sbd_toe_requirement_sources` | — | Parameters and response in the served description (`tools/list`) |
| `trace_sbd_toe_graph` | — | Parameters and response in the served description (`tools/list`) |

The served list is the source: `tools/list` returns the tools of the installed version, with the complete descriptions.

### Resources (`sbd://toe/*` URIs) {#resources-uris-sbdtoe}

| Resource URI | Content |
|---|---|
| `sbd://toe/quick-start` | Cheap session start |
| `sbd://toe/agent-guide` | Complete operational guide (READ FIRST) — modes, routing, epistemic patterns |
| `sbd://toe/activation-vocabulary` | Closed activation vocabulary — accepted values (including `roles`) and what each one activates; read before the first declaration |
| `sbd://toe/index-compact` | Compact JSON map of the Manual |
| `sbd://toe/chapter-applicability/{riskLevel}` | Graded applicability: what each chapter demands at that *risk level* (every chapter applies at every level) |
| `sbd://toe/ontology` | YAML ontology — `domain_mapping`, inference rules, *concerns* |
| `sbd://toe/grounded-codegen-guide` | Agent guide for `prepare_sbd_toe_codegen_context` (workflow + output discipline) |
| `sbd://toe/skill/{role}` | *Skill* of a canonical *role* (= `generate_sbd_toe_skill(role, format=skill)`) |
| `sbd://toe/subagent/{role}` | *Subagent* definition of a *role* (= `format=subagent`, *harnessed*) |
| `sbd://toe/version` | Name / version / *provenance* (Manual, KG, ontology) of the running server |
| `sbd://toe/notes/{id}` | Resolves the `note_id` values that responses carry by reference |
| `sbd://toe/notes` | Description in the served list (`resources/list`) |
| `sbd://toe/model` | Description in the served list (`resources/list`) |
| `sbd://toe/codegen-instructions/{mode}` | Description in the served list (`resources/list`) |

### Prompts {#prompts}

| Prompt | When |
|---|---|
| `setup_sbd_toe_agent(riskLevel, projectRole)` | Session setup — what each chapter demands at the *risk level* (no chapter excluded) + role-specific rules |
| `ask_sbd_toe_manual(question)` | Direct *grounded* Q&A |
| `prepare_grounded_codegen(task, …)` | End-to-end *grounded codegen* — instructs the agent to call `prepare_sbd_toe_codegen_context` before producing code |

*Prompts* are an MCP mechanism of their own: clients without *prompt* support (such as Claude Desktop) do not expose them. In those clients, the session starts from the resources and the tools.

---

## Controlled vocabulary {#vocabulário-controlado}

The server exposes **closed** values for parameters — using values outside these returns no results.

**Risk levels:**

| Level | Scope |
|---|---|
| `L1` | Low risk — internal, no sensitive data |
| `L2` | Medium risk — public APIs, user data |
| `L3` | High risk — PII, regulated systems |

No chapter is unlocked by level: all of them apply at every level, and what escalates from `L1` to `L3` is what is demanded (matrix of Ch. 01).

**Concerns** (ontological vocabulary, exact *lowercase*): the vocabulary is closed and is published in `sbd://toe/activation-vocabulary`, with the values and what each one activates. That is the source to consult, instead of a copied list.

**Canonical roles** (aliases accepted):

`developer` · `appsec-engineer` · `arquitetos-software` · `devops-sre` · `qa` · `security-champion` · `product-owner` · `scrum-master` · `operacoes` · `grc-compliance` · `gestao-executiva` · `auditores` · `fornecedores-terceiros`

> These are the Manual's **13 canonical roles** ([Roles and Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)). The server accepts common *aliases* (e.g. `appsec`→`appsec-engineer`, `devops`/`sre`→`devops-sre`, `ciso`→`gestao-executiva`, `compliance`→`grc-compliance`) and always resolves them to one of these 13.

---

## Identifier conventions {#convenções-de-identificadores}

- **Requirements**: `<CAT>-NNN` (e.g. `AUT-001`, `LOG-003`) — resolve by exact id via `query_sbd_toe_entities`
- **Controls**: `CTRL-<domain>-<slug>-<hash>` (e.g. `CTRL-identity-gestao-de-identidades-acessos-e-ownership-d0919c69af`). The form `CTRL-<capítulo>-<número>` does **not** exist.
- **Threats**: `MT-NNN` · **Artefacts**: `ART-<slug>-<hash>` — list via `get_sbd_toe_chapter_brief`
- **ID grammar** (*fullmatch*): `^(?:REQ-[A-Z]{3}-\d{3}|[A-Z]{3}-\d{3})$`. **`EX-…`** identifiers (e.g. `EX-AUT-003`, `EX-REQ-010`) are **illustrative** and never resolve; a `REQ-NNN` outside the catalogue returns an informative `citation_note` (`status: "informative"`), not a requirement — see [`query_sbd_toe_entities`](./05-tools-reference.md#query_sbd_toe_entities)
- In `prepare_sbd_toe_codegen_context` mode, the returned `citations` block is the **closed-world** set of valid ids for the task (legend by source + ids referenced by *payload* path) — ids outside `citations` **do not exist** for *grounding* purposes.

---

## Required epistemic pattern {#padrão-epistémico-exigido}

Every response generated on the basis of the MCP must label each claim:

| Label | Meaning |
|---|---|
| **manual-grounded** | Retrieved via MCP — cite `chapterId` or control ID |
| **observed** | Directly visible in the repository/codebase |
| **inferred** | Logical conclusion from *grounded* or *observed* facts — mark explicitly |
| **not verified** | Not confirmed — never present as fact |

In particular, the server must **never** be used to declare regulatory compliance on the basis of generated code: the regulatory *overlay* serves as a *cross-check*, not as a compliance signal.

---

## Next steps {#próximos-passos}

1. [Quickstart](./02-quickstart.md) — up and running in 60 seconds (Claude Code, Cursor).
2. [Installation by client](./03-instalacao.md) — Claude Code, Claude Desktop, Cursor, VS Code (Copilot), Windsurf, Zed.
3. [Skills and agents](./04-skills-agentes.md) — where to save the *skill* and how to initialise the session.
4. [Tools reference](./05-tools-reference.md) and [resources / prompts](./06-resources-prompts.md) — complete API.
5. [Use cases](./casos-uso/) — ready-made recipes: PR audit, *grounded codegen*, *threat modelling*, governance *bootstrap*, *onboarding*, normative *cross-check*.
6. [Advanced patterns](./08-padroes-avancados.md) · [Epistemic discipline](./09-epistemica-anti-patterns.md) · [Troubleshooting / FAQ](./10-troubleshooting-faq.md) · [Versioning / roadmap](./11-versionamento-roadmap.md).
