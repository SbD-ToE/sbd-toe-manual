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
  source_sha256: 859275c6675e7e43dbe05511cc41601d8bdc25d44426b8c6c542af513c158ffc
  source_commit: d394b0928bbec912dd0391bedb6cc4f403b46015
  target_sha256: 5e3e8e735f8d8ae75ccd17c7f5a3ebe003f5bd4d304ba3317e0504f535b96e76
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [appsec_core, chapter_role, cycle_iteration, deterministic, discipline, eu_startups, framework_source_corpus, lifecycle_phase, llm, macro_processo, mcp, mcp_reading_programa, mirror_osf, normative_empirical, open_closed_world, papel_suporte, practitioner_manual, programme_line, requirement_runtime, sbdtoe_sbd, threat, travessia_generica, travessia_relacao, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: fe25ece2cf0c305c63fe86e4af02a96a52aac86c2a5ec15f34941f453e0abc87
  translated_at: 2026-09-28T09:12:59Z
  stamped_at: 2026-09-28T09:12:59Z
  reviewed_by: null
---

# MCP Server (SbD-ToE)

When an agent is asked to write secure code, it can rely only on what it retained from training — a plausible approximation, but with no anchor or source — or consult the manual through a source that returns requirements and controls with citable identifiers. The **`@shiftleftpt/sbd-toe-mcp`** makes that consultation simple. It does not replace the model, which still generates the code: it gives it the source.

It is the official [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server of SbD-ToE. It exposes the manual (chapters 00–14), the *AppSec Core v1* ontology and the published normative cross-checks through MCP **tools, resources and prompts** — so that Claude, GitHub Copilot, Cursor, Windsurf, Zed (or any other MCP client) can ask the source at the moment they write, with real IDs, instead of relying only on what they were trained on. In practice: every requirement, control, threat or artefact the agent mentions can be verified.

:::note What the server guarantees and what depends on the client
The server guarantees **retrieval**: for the same question and the same *snapshot*, it returns the same requirements and controls, with real identifiers, and selects them deterministically from what the agent declares. The rest depends on the client and the model: the **context selection** the agent passes to the model; the **generation** of the code (retrieval is deterministic, generation is not); **citation verification** (that the agent cites what it received); and **implementation verification** (that the code meets the requirement, with the chapters' tests, review and validations). A valid citation does not make code secure.
:::

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
| `explain_sbd_toe_topic` | CONSULT | «What does the Manual say about X», by concept or by structure: requirements, guidance, proof, threats, anti-patterns and place in the lifecycle |
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
| `get_sbd_toe_macro_processes` | PROGRAMA | Where to start and in what sequence: adoption order, macro-processes and prerequisites; with `mp_id`, one macro-process in detail |
| `get_sbd_toe_chapter_implementation_checklist` | IMPL | "How to implement Ch. NN" — canon/20 narrative |
| `get_sbd_toe_chapter_capability` | IMPL | Capability to implement a chapter: KPIs with `thresholds_by_level` and artefacts to produce |
| `get_sbd_toe_operating_model` | IMPL | RACI / governance / cadences (from the *rollout playbook*) |
| `plan_sbd_toe_rollout` | IMPL | Roadmap by phases — order of implementation |
| `get_sbd_toe_verification_matrix` | IMPL | EXPECTED side: validation + expected evidence per requirement |
| `assess_sbd_toe_implementation` | IMPL | KPI posture vs *thresholds* per level |
| `inspect_sbd_toe_retrieval` | DIAG | Retriever diagnostics |
| `generate_sbd_toe_skill` | SETUP | Skill/subagent per *role* (`format`, `flavour`) — or the *agent guide* without `role` |
| `read_sbd_toe_resource` | — | Mirror of `resources/read` for clients without MCP *resources*: reads a `sbd://toe/*` resource by URI (e.g. `read_sbd_toe_resource(uri="sbd://toe/version")`) |
| `trace_sbd_toe_requirement_sources` | — | Where each requirement comes from: the Manual's direct sources, kept apart from the compensated chain REQ→CTRL→ACO→sources |
| `trace_sbd_toe_graph` | — | Traverses the AppSec Core graph over multiple hops, by lens (`slice_implementation`, `objective_realization`, `mechanism_provenance`) |

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
| `sbd://toe/notes` | The index of notes by reference: `{ids, notes}`, with every id and text |
| `sbd://toe/model` | The map of the served knowledge: entities, relations, chapters and categories, and the three ways of asking |
| `sbd://toe/codegen-instructions/{mode}` | The reference copy, per mode, of the prepare's static text (instructions and the `security_rationale` *template*) |

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

**Risk levels:** `L1`, `L2` and `L3`, the levels of the [Ch. 01 classification model](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), which computes them from the exposure, data and impact axes (E+D+I). The level is not deduced from the type of data or the applicable regime alone: an internal application with personal data and low impact can be `L1`, and the regulatory context (e.g. GDPR, DORA) is declared separately, in the regulatory overlay. The examples are illustrative, neither necessary nor sufficient:

| Level | Typical example (illustrative) |
|---|---|
| `L1` | Low risk — e.g. internal application with low impact |
| `L2` | Medium risk — e.g. public APIs with user data |
| `L3` | High risk — e.g. public exposure, sensitive data and high impact |

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
5. [Use cases](./casos-uso/) — ready-made recipes: PR audit, *grounded codegen*, *threat modelling*, governance *bootstrap*, *onboarding*, normative *cross-check*, Agentic SDLC.
6. [Advanced patterns](./08-padroes-avancados.md) · [Epistemic discipline](./09-epistemica-anti-patterns.md) · [Troubleshooting / FAQ](./10-troubleshooting-faq.md) · [Versioning / roadmap](./11-versionamento-roadmap.md).
