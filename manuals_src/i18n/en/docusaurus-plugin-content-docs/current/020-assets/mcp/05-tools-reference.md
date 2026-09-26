---
id: tools-reference
title: Tools — complete reference
description: Every tool of the SbD-ToE MCP — parameters, deterministic vs heuristic semantics, input/output examples, and when to prefer one over another.
sidebar_label: Tools reference
sidebar_position: 5
tags:
  - mcp
  - tools
  - referencia
translation:
  source_locale: pt
  source_path: 020-assets/mcp/05-tools-reference.md
  source_sha256: 37162bf58e5f7dc5a2d3ac366b41d4b9edc762359c95df3384740af705bc3404
  source_commit: 058f86265e07bc86cb7f19162dd2c6b87fbcc0a7
  target_sha256: cdd21c0481d05ff69bff57b18fc40c6cfc08478da976d61999bf5cf3de2d266d
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: da8c4621ee3f200794cd49e34ddc29239ba89f55effb1e5e578d388e50580b8d
  glossary_keys: [appsec_core, chapter_role, cycle_iteration, deterministic, discipline, framework_source_corpus, gap_family, layer, lifecycle_phase, macro_processo, macroprocess_entity, mcp, mcp_reading_programa, mirror_osf, normative_empirical, open_closed_world, papel_suporte, practitioner_manual, programme_line, provenance, requirement_runtime, sbdtoe_sbd, slice, traceability, travessia_generica, travessia_relacao, validation_evaluation, verification_taxonomy]
  glossary_sha256: faa86e1cdafe343c70e211aae90c326d6fc7ef228fec86bb4ba32316bba7e15f
  translated_at: 2026-09-26T17:58:18Z
  reviewed_by: null
---

# Tools — complete reference

The tools are organised by reading — CONSULT, GUIDE, SETUP, IMPL (implementation view), NORMATIVA and PROGRAMA — and have **different semantics**:

- **Deterministic**: given the same input, they return the same output. Use them for citable grounding (`select_sbd_toe_requirements`, `consult_security_requirements`, `get_guide_by_role`, `get_threat_landscape`, `prepare_sbd_toe_codegen_context`).
- **Heuristic / search**: textual ranking over the manual. Use them for narrative/concepts (`search_sbd_toe_manual`).

Each tool below lists its parameters, expected *output*, and recommended pattern. The complete list for the installed version, with the served descriptions, is the one `tools/list` returns.

---

## Entry point — the declarative contract {#porta-de-entrada--o-contrato-declarativo}

### `select_sbd_toe_requirements` {#select_sbd_toe_requirements}

**Deterministic and reproducible.** It is the tool that the served descriptions mark as *START HERE*: for a concrete task, it selects the applicable requirements from what the agent **declares** — not from what the server guesses.

**The contract:**

- The agent declares what it has read: `risk_level`, `concerns`, `exposure`, `data_sensitivity`, `technologies`, `changed_files`. The accepted values are in [`sbd://toe/activation-vocabulary`](./06-resources-prompts.md), along with what each one activates.
- `changed_files` activates chapters through the published table — it is the direct way to bring a *diff* into the selection.
- The task text (`task`) is recorded as context, not interpreted.
- Without a declaration, the response is `needs_input`: it returns the vocabulary, the candidates to confirm and, for inert declarations, the `valid_values`. The agent confirms with the user and calls again with the complete declaration.
- `exposure` accepts four values. `local` is valid and inert, it activates nothing: declared on its own, it gives `needs_input`, never a silently empty selection. `internal` and `authenticated` activate `auth` and `logging`. `public` activates `auth`, `logging`, `api`, `validation` and `architecture`. The source is `sbd://toe/activation-vocabulary`.

**The response carries:**

- `selection`, with `selected[]`, `narrowed_out` and `excluded_by_level`. Each entry of `selected[]` carries `requirement_id`, `name`, `category`, `type`, `source_chapter` and `selection_trace[]`, with the layer, the source, the trigger and the `basis` (`declared` or `lexical`).
- `context`, with the chapters and categories activated.
- `out_of_scope_chapters`, with what no declaration activated, by chapter and count, and the way to bring it in.
- `task`, recorded as `recorded_context`, with `affects_selection: false`.
- `basis_summary`, `coverage` (total, page, `nextOffset`, and the counts of `narrowed_out` and `excluded_by_level`), `denominators` (the named denominators) and `cross_surface_check` (agreement with `consult_security_requirements` on the comparable part).
- `overlay`, `activation_trace`, `provenance` and `next`.

`selected` is paginated by id order, not by relevance: to reach a category, declare the *concern* that activates it, or ask by structure (`categories`). The `next` line pointing to the prepare announces the cost as an estimate.

The `select` has the same `detail` axis as the prepare:

- `full`, the default level, carries the full `selection_trace` in each item.
- `standard` moves the distinct justifications to `selection_trace_legend`, and each item references them in `trace`.
- `lista` is the same as `standard`, without the derivable fields `type` and `source_chapter`.

**Typical chaining:** `select_sbd_toe_requirements` → `prepare_sbd_toe_codegen_context` (to generate code with those requirements) → [`get_sbd_toe_verification_matrix(requirement_ids)`](#get_sbd_toe_verification_matrix) (the expected proof for each selected requirement).

---

## CONSULT mode {#consult-mode}

### `search_sbd_toe_manual` {#search_sbd_toe_manual}

Narrative search with citations — when the user asks conceptual questions ("what is threat modelling?", "how does SBOM work"). The served description marks it as **non-normative**: it serves to guide reading, not to ground an obligation.

**Parameters:** `question` (string, mandatory); `topK`, `useVectorRecall`, `debug` (optional)

**Output:** a list of excerpts with `chapter_id`, `section`, `score`, `text`.

**When to prefer:** open / explanatory questions.
**When NOT to use:** when there are structured filters (risk_level, concern, role) — prefer `consult_security_requirements`.

---

### `answer_sbd_toe_manual` {#answer_sbd_toe_manual}

Natural-language Q&A — retrieves context from the manual and asks the client's model to synthesise the answer via *MCP sampling*.

**Parameters:** `question` (string); `topK`, `useVectorRecall`, `debug` (optional)

:::info Honest degradation without *sampling*
In clients **without MCP sampling support** (e.g. Claude Code), the tool **does not invent** a synthesis: it returns the formatted retrieval with the note *"MCP sampling not available… use `search_sbd_toe_manual` directly"* and redirects to `search_sbd_toe_manual`. In those clients, prefer `search_sbd_toe_manual` from the start.
:::

---

### `explain_sbd_toe_topic` {#explain_sbd_toe_topic}

CONSULT reading: «what does the Manual say about X», with no task and no project. Ask by concept (`concern`) or by structure (`category` or `chapter`). The response walks through the requirements (with `applies_at`), the guidance (practices), the proof, the threats, the anti-patterns («what NOT to do») and the place in the lifecycle, distinguishing requirement from guidance and marking provenance. `risk_level` is optional and only annotates: it does not filter, and the response is the same without it. It is paginated over the requirements.

---

### `consult_security_requirements` {#consult_security_requirements}

**Deterministic**. Returns the set of active requirements + controls for a *risk level*, optionally filtered by *concerns*. It is the level's catalogue; for the selection that serves a concrete task, the entry point is [`select_sbd_toe_requirements`](#select_sbd_toe_requirements).

**Parameters:**
- `risk_level` (`L1` | `L2` | `L3`) — mandatory
- `concerns` (string[]) — optional, values from the **closed vocabulary** below
- `exposure`, `data_sensitivity` — optional (`exposure`: `local`, `internal`, `authenticated` or `public` — see [`select_sbd_toe_requirements`](#select_sbd_toe_requirements))
- `mode` (`full` | `index`) — optional

**`concerns` vocabulary (closed):** the accepted values, and what each one activates, are published in `sbd://toe/activation-vocabulary` — that is where they are confirmed, rather than in a copied list.

Values outside the vocabulary are **declared, not approximated** (there is no *fuzzy match*): use `logging` for monitoring, `distribution` for *supply chain* / third parties, `agents` for the AI agent requirements (`REQ-AGN-001…004`).

**Output:** (real id formats — requirements `<CAT>-NNN`, controls `CTRL-<domain>-<slug>-<hash>`)
```json
{
  "requirements": [{"requirement_id": "AUT-001", "name": "MFA obrigatório", "category": "AUT", "type": "base"}],
  "controls": [{
    "control_id": "CTRL-identity-gestao-de-identidades-acessos-e-ownership-d0919c69af",
    "name": "Gestão de identidades, acessos e ownership",
    "domain": "identity", "control_type": "preventive",
    "chapter_ids": ["08-iac-infraestrutura", "14-governanca-contratacao"],
    "_confidence": "direct"
  }],
  "active_domains": ["identity", "governance", "infrastructure"],
  "active_categories": ["ACC", "ARC", "AUT", "SES"],
  "rule_trace": [
    "REQUIREMENT_APPLIES_BY_RISK(risk_level=L2): 39 requirements active",
    "CONCERNS_FILTER_REQUIREMENTS(concerns=[auth])"
  ],
  "coverage_gaps": {
    "requirements_without_control_link": {"count": 0, "requirement_ids": [], "note": "…"}
  }
}
```

`coverage_gaps.requirements_without_control_link` is **always returned**. With the currently served knowledge, `count` is 0 at all three levels. If a requirement without a link to controls appears, it is listed here as a declared gap, not as an absence of obligation (the requirement is served; the controls are, at most, derived by domain, `_confidence: "derived"`).

**Size:** the complete L2/L3 response may exceed the client's context. The guide (`sbd://toe/agent-guide`) publishes the sizes measured on the served *build*, and each response declares its own in `size_estimate`.
**Rule of thumb:** **always** pass `concerns` at L2/L3 — the response becomes much smaller.

#### Example {#exemplo}

```json
consult_security_requirements({"risk_level": "L2", "concerns": ["auth", "logging"]})
```

Returns only requirements from the **AUT/ACC/SES** (auth) + **LOG** (logging) categories, with `rule_trace` confirming `CONCERNS_FILTER_REQUIREMENTS`.

---

### `map_sbd_toe_applicability` {#map_sbd_toe_applicability}

The demand of each chapter for a *risk level* and the project profile. Applicability is graded: every chapter applies at every level, and what changes is the demand.

**Parameters:** `riskLevel` (mandatory); `technologies`, `hasPersonalData`, `isPublicFacing`, `projectRole` (optional).

**Output:** `chapters` (with the demand per chapter), `conditional`, `activatedBundles`.

**When to prefer:** profiling a new project and comparing the effect of each level. The tool does not decide the *risk level* — it requires it; the decision follows the method of Ch. 01.

---

### `get_sbd_toe_chapter_brief` {#get_sbd_toe_chapter_brief}

Structured summary of a chapter — goal, role, phases, artefacts (`ART-*`).

**Parameters:** `chapterId` (e.g. `06-desenvolvimento-seguro`)

**Output:** `id`, `found`, `title`, `objective`, `role`, `phases`, `artifacts`, `artifacts_basis`.

---

### `list_sbd_toe_chapters` {#list_sbd_toe_chapters}

Index — `id`, `title`, `readableTitle`, `applicability`, `demand_by_level`.

**Parameters:** `riskLevel` (optional). It does not exclude chapters: all of them appear, with the demand per level.

---

### `query_sbd_toe_entities` {#query_sbd_toe_entities}

Resolves an entity by **exact id** or, if the token is not an id, *falls back* to semantic search.

**Parameters:** `query` (string, mandatory); `entityType`, `chapterId`, `riskLevel`, `topK` (optional)

**Example (exact id):**

```json
query_sbd_toe_entities({"query": "AUT-001"})
```
```json
{
  "entities": [{
    "entity_type": "requirement", "requirement_id": "AUT-001",
    "category": "AUT", "name": "MFA obrigatório",
    "applicable_levels": {"L1": false, "L2": true, "L3": true},
    "source_bundle": "02-requisitos-seguranca"
  }],
  "total": 1, "match": "exact_id"
}
```

:::warning Common category error
A token such as `"CTRL-06"` **is not an id** — the form `CTRL-<capítulo>-<número>` does not exist. Passing it does **not** return "the controls of chapter 06"; it falls into the semantic *fallback* (`match` ≠ `"exact_id"`). The real ids are `AUT-001`, `LOG-003` (requirements), `CTRL-<domain>-<slug>-<hash>` (controls), `MT-NNN` (threats), `ART-…` (artefacts). To **filter by type/domain** (instead of resolving an id), use `resolve_entities`.
:::

**`citation_note` and `declared_gap`.** The requirement ID grammar is *fullmatch* — `^(?:REQ-[A-Z]{3}-\d{3}|[A-Z]{3}-\d{3})$`; `EX-…` identifiers are illustrative and never resolve. A `REQ-NNN` that the manual cites as an example but that does not exist in the catalogue (e.g. `REQ-010`, in an example in Ch. 02) returns `entities` by semantic *fallback* **and** a `citation_note` with `status: "informative"` and `cited_in` (where it is cited) — informative, not a *gap*, and never resolved by approximation to another requirement. Legacy citations with the form `REQ-<CAT>-NNN` return `declared_gap`; today they do not exist in the manual and the field does not appear.

```json
query_sbd_toe_entities({"query": "REQ-010"})
// → "citation_note": {
//      "requirement_id": "REQ-010", "status": "informative",
//      "note": "`REQ-010` não é um requisito publicado: o Manual cita-o como identificador ilustrativo de exemplo ou é um token não-requisito com a forma <CAT>-NNN (CWE-, SHA-, …). Informativo, não é um gap; nunca resolvido por aproximação a outro requisito.",
//      "cited_in": {"mention_count": 2, "document_ids": ["010-sbd-manual-02-requisitos-seguranca-addon-15-exemplos-aplicacao"]}
//    }
```

---

### `resolve_entities` {#resolve_entities}

Low-level filter over the ontology — *dot-notation* in the `filters`.

**Parameters:** `record_type` (for example `control`, `requirement`, `role`, `practice`, `threat`, `artifact`, `evidence_pattern`, the `appsec_*` of AppSec Core v1 and the `regulatory_*` of the overlay — an unknown value returns the valid list), `filters` (*dot-path* object), `limit` (optional)

**Examples:**

```json
resolve_entities({"record_type": "role"})
// → lista os 13 roles canónicos

resolve_entities({"record_type": "control", "filters": {"domain": "architecture"}})
// → controlos do domínio architecture

resolve_entities({"record_type": "requirement", "filters": {"requirement_id": "REQ-010"}})
// → total: 0, com meta.note idêntica à citation_note (identificador ilustrativo; não é gap)
```

---

## GUIDE mode {#guide-mode}

### `get_guide_by_role` {#get_guide_by_role}

**Deterministic**. Practices assigned by *role* and/or SDLC phase.

**Parameters:**
- `risk_level` (`L1` | `L2` | `L3`) — mandatory
- `role` (string) — optional
- `phase` (string) — optional; canonical phases `plan` | `design` | `develop` | `build` | `test` | `deploy` | `operate` | `govern` (the *aliases* resolve: `implement`→`develop`, `requirements`→`plan`, `governance`→`govern`)

**Output without `role`/`phase`:** `role_summary{}` + `phase_summary{}` (counts) — useful for discovery.
**Output with `role` or `phase`:** `assignments[]` + *user stories*.

**Critical rule:** **always pass `role` or `phase`** to obtain details — without either of them, it returns only counts.

---

### `get_threat_landscape` {#get_threat_landscape}

**Deterministic**. *Threats* relevant to a *risk level* / *concern*, with mitigations.

**Parameters:**
- `risk_level` (`L1` | `L2` | `L3`) — mandatory
- `concerns` (string[]) — optional
- `detail` (`lista` | `standard` | `full`) — optional; `minimal` is refused, with the same warning as in the prepare
- `limit` — optional, 25 by default; `coverage` and `size_estimate` always come

**Order:** threats are ordered by membership of the declared scope. First come the domain chapters of the declared *concerns*. Chapters 01 and 02, with the process meta-threats, come last. Within each group, the order is by `mitigation_confidence`, chapter and id. That is why the first page is the relevant part, and the following ones add the general.

**Output:** (`MT-NNN` threats; each link cites the real `control_id`)
```json
{
  "threats": [
    {
      "id": "MT-055", "name": "Interfaces expostas sem isolamento",
      "chapter_id": "04-arquitetura-segura", "threat_category": "STRIDE",
      "mitigation_confidence": "derived", "mitigation_strength": "parcial",
      "mitigated_by": [
        {"control_id": "CTRL-infrastructure-segmentacao-e-controlo-arquitetural-dceb3c1f0b", "domain": "infrastructure"}
      ]
    }
  ]
}
```

**Important:**
- `mitigation_confidence: "derived"` → structural link (chapter/bundle-match), reliable; `mitigation_strength` is typically `"parcial"`. (There is no `"heuristic"` value in structural links — if a heuristic *fallback* appears, label it as inferred.)
- The tool **runs `consult` internally** — do not call `consult_security_requirements` beforehand.

:::info *Routing* of *concerns* — `routing_basis`
Every *concern* in the vocabulary is accepted, but only some have a threat chapter of their own (for example `architecture`, `iac`, `logging`, `supply_chain` and `threat_modeling`). For the others, the threats arrive through the chapters that define the activated controls. Each response declares, per *concern*, the basis of the *routing* in `routing_basis`: `domain_chapter` when the *concern* has a threat chapter of its own, `activated_controls` when the threats arrive through the chapters that define the activated controls. A *concern* with no route goes to `unsupported_concerns`.
:::

---

### `plan_sbd_toe_repo_governance` {#plan_sbd_toe_repo_governance}

Lists the artefacts that the manual identifies for a repository, grouped by chapter.

**Parameters:** `riskLevel`, `offset`, `limit` (paginated).

**Output:**

- `riskLevel` and `risk_level_effect`, which is `{filters, basis, note, asserts}` and says how much the level filters, and why;
- `totalArtefacts`, the number of chapter↔artefact rows;
- `artefact_totals`, with `distinct_count` (distinct artefacts) and `chapter_relation_count` (rows). Rows are never added up to count artefacts;
- `byChapter[]`, where each entry is `{chapterId, artefacts[]}` and each artefact is `{artefactId, chapterId, riskLevels[]}`, with ids in the form `ART-<slug>-<hash>`;
- `coverage`, which paginates over the chapters, plus `size_estimate`, `note` and `next`.

The chapter↔artefact relation is a projection: it does not say who owns the artefact nor oblige anyone to produce it.

**Pattern:** *governance bootstrap* in a new repo — generate from the list of artefacts per chapter, create the empty files + READMEs.

---

### `map_sbd_toe_review_scope` {#map_sbd_toe_review_scope}

Given a set of changed files, returns which **manual bundles** to review.

**Parameters:** `changed_files` (string[])

**Output:** chapters / bundles to review + *rationale* (e.g. "files under `iac/` → Ch. 08").

**Pattern:** *PR auditor*. Combine with `consult_security_requirements` to enumerate controls per chapter.

---

### `prepare_sbd_toe_codegen_context` {#prepare_sbd_toe_codegen_context}

The **most sophisticated** tool — returns deterministic context for *codegen*, *review* or *test-plan*.

**Parameters:**
- `task` (string) — in declarative mode (the *default*) it is **recorded** and optional context; it only drives the selection in `selection_mode: "discover"`
- `risk_level`, `mode` (`codegen` | `review` | `test-plan`), `concerns`, `exposure`, `data_sensitivity` (`low` | `personal` | `regulated` | `secrets`), `technologies`, `changed_files` — the declaration (pass everything that is known; values in `sbd://toe/activation-vocabulary`)
- `stack` — free text; it only counts when it carries a *token* from the vocabulary, so declaring `technologies` is preferable
- `chapters`, `categories`, `selection_mode`, `detail` (`lista` | `standard` | `full`), `include_relations`, `debug` — optional
- `regulatory_frameworks`, `include_regulatory_overlay` — optional

**Output (`status` field):**

| `status` | Meaning | Action |
|---|---|---|
| `ready_for_codegen` | Clear scope, context ready | Proceed — fill in `security_rationale` |
| `needs_input` | Nothing was declared | **STOP** — the response carries the vocabulary, the candidates to confirm and, for inert declarations, the `valid_values`; confirm with the user and declare |
| `needs_clarification` | Ambiguous inputs | **STOP** — ask the user, do not generate code |
| `needs_decomposition` | Scope too broad, or selection above what the `detail` level promises to fit | **STOP** — in that case, execute the measured batches of `requirement_ceiling.batches`, whose union is the whole selection (batches may share requirements) |
| `unsupported_scope` | Capability missing on the server | **STOP** — report verbatim |

**Shape of the response:**

- **One object per requirement** — `{id, name, type, description, verify, evidence}`: the requirement, how it is verified and what evidence is expected, in a single place.
- **`detail`** — the three levels serve the same set of citable ids and the same complete requirement, and the description is never cut at any level. What changes is what comes *inline* and what comes by reference:
  - **`lista`** carries inline the requirements, the controls and the graph entities grouped by *slice*, the `citations` block, the generation instructions and the `security_rationale` *template*. By reference come the `manual_grounding` (counts per group and `entries_ref` for `full`), the relations (`relations_summary`, with the exact accounting) and the activation *trace* (only with `debug: true`). The `adjacency` comes as a summary, with `detail_ref`.
  - **`standard`** is the same as `lista`, plus the `adjacency` detail inline, with all the signals.
  - **`full`** is the default level. It carries the same as `standard`, plus the `manual_grounding` verbatim, the `activation_trace` and a `relations_ref` executable in `trace_sbd_toe_graph`. With `include_relations: true`, the relations come inline.
- **Envelope** — `lista` and `standard` promise to fit in a token envelope, measured on the *payload* the client receives. Above it, the response is `needs_decomposition` with measured batches that together cover the whole selection. `full` has no envelope and declares the price in `size_estimate`.
- **`adjacency`** — what was not declared and would change the selected set (for example, declaring public exposure).
- **`completeness_report.verification`** — the verification coverage, with the pattern ids in `verification.by_ref`.
- **`size_estimate`** — the size of the response itself; `within_envelope: false` warns that it exceeds the expected envelope.
- **Notes by reference** — the `note_id` values resolve in `sbd://toe/notes/{id}`, instead of being repeated in every response.

**Mandatory discipline after `ready_for_codegen`:**

- The returned `citations` block is the **closed-world** set of valid ids — do not invent ids.
- Fill in `security_rationale.decisions[].cited_ids` with at least 1 ID per non-trivial decision.
- Fill in `security_rationale.validations[]` (concrete validations implemented).
- Fill in `security_rationale.expected_evidence[]` (artefacts for the reviewer — code alone is **not** evidence).
- Fill in `security_rationale.residual_risk` (what was not addressed).
- Flag `completeness_report.m_recall < 1.0` to the user (partial coverage).

See the detailed guide in [Use case — grounded codegen](./casos-uso/codegen-grounded) and in the [`sbd://toe/grounded-codegen-guide`](./06-resources-prompts.md#sbdtoegrounded-codegen-guide) resource.

---

## SETUP mode {#setup-mode}

### `generate_sbd_toe_skill` {#generate_sbd_toe_skill}

Generates configuration content for the client. **Without `role`** it returns the canonical *agent guide* (`sbd://toe/agent-guide`); **with `role`** it returns a *skill* or *subagent* specialised in the *slice* of that role.

**Parameters:**
- `role` (optional) — one of the **13 canonical personas** (aliases resolve; unknown role → error with the list of the 13).
- `format` (`skill` | `subagent`) — `skill` = guidance file (`.claude/skills/…`); `subagent` = installable agent definition (`.claude/agents/…`).
- `flavour` (`harnessed` | `skilled`) — `harnessed` (default) embeds the `mcp__sbd-toe__*` tools (consults the manual live); `skilled` embeds the frozen *slice*, **without** live tools (offline).
- `risk_level` (default `L2`), `phase`, `include_detail`, `clientType` — optional.

**Output:** `content` (markdown) + `suggested_path` + `meta.coverage{chapters, of_total_chapters, assignments, user_stories, checklist_items}` — coverage is **declared** ("nothing silently truncated").

Parallel resources: `sbd://toe/skill/{role}` and `sbd://toe/subagent/{role}` return the same content.

See [Skills and agents](./04-skills-agentes.md).

---

### `setup_sbd_toe_agent` (prompt) {#setup_sbd_toe_agent-prompt}

Technically a *prompt*, not a *tool* — but it works as the session initialiser.

**Parameters:** `riskLevel`, `projectRole`

**Output:** the dominant demand of each chapter at the level (graded applicability — no chapter excluded) + role-specific rules. Clients without *prompt* support (such as Claude Desktop) do not expose it.

---

## Implementation view {#implementation-view-v5}

These tools answer **"how to stand up and govern SbD"** — distinct from the operational view ("what to do in each SDLC phase"). All of them are *coverage-preserving* (pagination with `coverage.hasMore`/`nextOffset`; nothing silently truncated) and return a `next` band with the suggested next steps.

### `get_sbd_toe_chapter_implementation_checklist` {#get_sbd_toe_chapter_implementation_checklist}

A chapter's canon/20 implementation narrative (the "how to implement"), distinct from the structured *user story* DoD (that one is in `get_guide_by_role(include_detail=true)`).

**Parameters:** `chapter` (id or number), `risk_level?`, `limit?`, `offset?`
**Output:** `data.items[]` (prose with traceable `chunk_id`) + `next`.

### `get_sbd_toe_chapter_capability` {#get_sbd_toe_chapter_capability}

IMPL reading: to implement chapter N, what capability is needed, how one knows it exists and how it is measured. Returns the KPIs the Manual defines for the chapter, with `thresholds_by_level` (L1/L2/L3) as data, and the artefacts the capability should produce. Reached by `chapter`, `metric_id` or `dimension`. `risk_level` adds `target_at_level`, and without `chapter` it returns every published KPI. It closes the cycle with [`assess_sbd_toe_implementation`](#assess_sbd_toe_implementation). It is not the GUIDE reading: that is [`select_sbd_toe_requirements`](#select_sbd_toe_requirements).

### `get_sbd_toe_operating_model` {#get_sbd_toe_operating_model}

RACI, *decision rights*, governance cadences and organisation models, promoted from the *rollout playbook*.

**Parameters:** `orgScope?`, `limit?`, `offset?`
**Output:** `data.sections[]` (prose, paginated). It declares the boundary: **it does not prescribe an organisation chart** (it varies by sector/size).

### `plan_sbd_toe_rollout` {#plan_sbd_toe_rollout}

Phased roadmap — the canonical lifecycle phases mapped to chapters.

**Parameters:** `orgProfile?`, `horizon?`, `limit?`, `offset?`
**Output:** `data.phases[]` (`order`, `phase_id`, `label`, `chapter`), `model: "phase-ordered-mvp"`. The dependency DAG is **deferred** (declared, not faked).

### `get_sbd_toe_verification_matrix` {#get_sbd_toe_verification_matrix}

The **EXPECTED** side of verification: per requirement/control, the validation method + expected evidence + a reference to an *EvidencePattern*. A deterministic complement to the auditor and to the test plan.

**Parameters:** `risk_level` (mandatory), `requirement_ids?` (up to 50 per call — closing requirement→proof from a selection), `limit?`, `offset?`
**Output:** `data.rows[]` (`evidence_pattern_id` `EP-*`, `requirement_id`, `control_id`, `validation_method`, `expected_evidence`, `evidence_type`, `expected_artifact_type_ids[]`, `source`) + `coverage_gaps` (requirements without a pattern — declared).

### `assess_sbd_toe_implementation` {#assess_sbd_toe_implementation}

Posture self-report: compares submitted KPI values against the *thresholds* per level.

**Parameters:** `kpi_values` (a `metric_id`→number map; empty is rejected with `-32602`), `risk_level`, `chapter?` (restricts the universe), `offset?`, `limit?`
**Output:** `posture` (`below`/`at`/`above`) + `totals{applicable, meets, gaps, not_reported}` + `per_kpi` + `unknown_metrics`. **Stateless** (nothing is stored); an applicable KPI without a value is `not_reported`, **never** *pass*.

:::note Payload
Returns all applicable KPIs, which can make the output large — `chapter` restricts the universe and `offset`/`limit` walk through it. Submit the `kpi_values` that are available; the missing ones come marked `not_reported`.
:::

### `map_sbd_toe_regulatory_activation` {#map_sbd_toe_regulatory_activation}

Regulatory lens (the inverse of *provenance*): given a *framework*, which areas/chapters of the manual it activates.

**Parameters:** `framework` (`DORA` | `NIS2` | `CRA` | `RGPD`; or `EXT-DORA`…), `limit?`, `offset?`
**Output:** `data.activated[]` per chapter (`mapping_count`, `obligation_count`, `by_target_type`, `example_citation`) + `totals`. Unknown *framework* → error `-32602`. The provenance declares: **cross-check ≠ attestation of compliance**.

---

## NORMATIVA and PROGRAMA readings {#leituras-normativa-e-programa}

### `get_sbd_toe_playbook` {#get_sbd_toe_playbook}

**NORMATIVA** reading: returns the playbooks published per legal instrument, with the declared authority. For frameworks without a published cross-check (ISO, PCI, SOC2, …), the response declares `no_cross_check` instead of improvising a correspondence. It is the main path of the [normative cross-check use case](./casos-uso/cross-check-conformidade), alongside `map_sbd_toe_regulatory_activation`.

All parameters are optional:

- Without arguments, it returns the index.
- `framework`, by code (`DORA`, `NIS2`, `CRA`, `RGPD`, `AI-ACT`, `ENISA-CSA`) or id (`EXT-DORA`…), returns the playbooks for that legal instrument.
- `playbook_id`, an id taken from the index (e.g. `OVR-DORA-playbook`), returns the paginated sections.
- `kind` filters the index by type: `normative_cross_check`, `implementation_playbook`, `convergence_note`, `illustrative_example` or `illustrative_index`.
- `offset` and `limit` (10 by default) paginate the sections.

Illustrative examples come in a separate band, and a legal instrument without a published cross-check returns `no_cross_check`. The index carries `delimitation`, `scope`, `normative_playbooks`, `illustrative_examples`, `covered_frameworks`, `roadmap_declared_by_manual` and `coverage`.

### `get_sbd_toe_macro_processes` {#get_sbd_toe_macro_processes}

**PROGRAMA** reading: where to start and in what sequence. Without arguments, it returns the published adoption order, derived only from the dependency edges, the macro-processes and the prerequisites. With `mp_id` (e.g. `MP-01`), it returns one macro-process in detail: question, continuity, invariant, owner, participants, chapter traversal, indicators, control points, expected evidence and L1–L3 proportionality. It declares its limits: there is no «programme» entity, the MP↔SDLC-phase graph traversal is a published gap, and `traverses_bundles` is a chapter traversal, not a membership relation.

---

## Tracing and reading resources {#rastreio-e-leitura-de-resources}

### `read_sbd_toe_resource` {#read_sbd_toe_resource}

Mirror of `resources/read` for clients without support for MCP *resources*, such as Claude Desktop. Returns any resource by URI, including templated ones, with the value already in the URI (e.g. `sbd://toe/notes/prepare.repeat_call_hint`). `slot` returns a single slot of a JSON resource with slots (`codegen-instructions`). `char_offset` and `char_limit` paginate the text. An unknown URI returns a declared error with the valid list.

```
read_sbd_toe_resource(uri="sbd://toe/version")
```

### `trace_sbd_toe_requirement_sources` · `trace_sbd_toe_graph` {#trace_sbd_toe_requirement_sources--trace_sbd_toe_graph}

**`trace_sbd_toe_requirement_sources`** says where each requirement comes from. The direct sources (`source_anchors`, the Manual's own «Sources» marker) are kept apart from the compensated chain REQ→CTRL→ACO→sources, which has type and confidence per hop. That chain carries the label `coverage_compensated`: it is coverage by correspondence between models, not authorship, and `related` does not cover. It accepts 1 to 50 `requirement_ids` and is paginated. `include_chains: false` returns only counts and a reference. Requirements without a declared source and unknown ids are declared.

**`trace_sbd_toe_graph`** traverses, over multiple hops and in a curated way, the relation graph of AppSec Core (slices, control objectives, mechanisms, practices), for traceability questions that the high-level tools do not expose. A lens is chosen with `lens`:

- `slice_implementation`: slice → objectives → mechanisms and practices;
- `objective_realization`: objective → mechanisms and practices;
- `mechanism_provenance`: mechanism or practice → objectives → slices.

`anchor` restricts what it traverses to one entity. The result is deterministic and paginated (`page`, `pageSize` up to 200, `total` and `cursor`), and never truncates silently. It is the destination of the prepare's `relations_ref`.

---

## Diagnostics {#diagnóstico}

### `inspect_sbd_toe_retrieval` {#inspect_sbd_toe_retrieval}

Retriever diagnostics — useful when a query returns unexpected results. Shows ranking, scores, and the complete *rule_trace*.

**Parameters:** `question` (string)

---

## Combinatorics — recommended patterns {#combinatória--padrões-recomendados}

### Structured question {#pergunta-estruturada}

```
consult_security_requirements(L2, ["auth"])
```

### Narrative question {#pergunta-narrativa}

```
search_sbd_toe_manual("threat modeling stride")
```

### Complex answer (threat model / security plan) {#resposta-complexa-threat-model--security-plan}

```
1. consult_security_requirements(L2, concerns)   # requisitos + controlos
2. get_threat_landscape(L2, concerns)             # threats relevantes
3. get_guide_by_role(L2, role)                    # práticas do role
4. → gerar documento citando IDs dos 3 passos
```

### PR review {#pr-review}

```
1. map_sbd_toe_review_scope(changed_files)        # que capítulos
2. consult_security_requirements(risk_level, concerns)  # controlos activos
3. → enumerar findings citando CTRL-* + chapter_id
```

### Grounded codegen {#codegen-grounded}

```
1. prepare_sbd_toe_codegen_context(task, mode="codegen", detail, ...declaração)
2. ramificar por status (ver tabela acima)
   - needs_input → confirmar a declaração com o utilizador e voltar a chamar
   - needs_decomposition → seguir requirement_ceiling.batches, um lote de cada vez
3. se ready_for_codegen → gerar código + tests + security_rationale
```

## Next steps {#a-seguir}

[Resources and prompts](./06-resources-prompts.md) — `sbd://toe/*` URIs for structural *grounding* and pre-packaged prompts.
