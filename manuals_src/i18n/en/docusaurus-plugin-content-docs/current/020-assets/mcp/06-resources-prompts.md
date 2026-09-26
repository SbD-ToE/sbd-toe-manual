---
id: resources-prompts
title: Resources and prompts
description: MCP resources (sbd://toe/*) and pre-packaged prompts of the SbD-ToE MCP — when to use each one.
sidebar_label: Resources & prompts
sidebar_position: 6
tags:
  - mcp
  - resources
  - prompts
translation:
  source_locale: pt
  source_path: 020-assets/mcp/06-resources-prompts.md
  source_sha256: 792e62db3dd10423dec8c9512bb93832d01b222f1bae6718c73957ae08ac0797
  source_commit: 4e04c6c26f9325b8a3515d4ccd3b126f58be3b1e
  target_sha256: 8353c476d245a4a5f9f590103e66e90ea316fa8481670ec351f9b4af00940d37
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 211df96a27d713b5934d7534d61f1972d877902236e63b858563d206c67ccaa8
  glossary_keys: [chapter_role, deterministic, discipline, esquema_regime, framework_source_corpus, lifecycle_phase, mcp, papel_suporte, practitioner_manual, sbdtoe_sbd, schema, traceability]
  glossary_sha256: 3872ab6453f9771a21801a6ab600dc3f921e34e9e667e787431939f7de212c9c
  translated_at: 2026-09-26T14:55:16Z
  reviewed_by: null
---

# Resources and prompts

Beyond the **tools**, the MCP protocol exposes two additional mechanisms that the SbD-ToE server uses extensively:

- **Resources** (`sbd://toe/*`) — documents / structured data accessible by URI, read by the client as context.
- **Prompts** — pre-packaged prompt templates that the client can run with parameters.

The practical difference:

| Mechanism | How it is read | Typical case |
|---|---|---|
| **Tool** | Client calls, receives a result | Deterministic operation with parameters (consulting requirements, listing chapters) |
| **Resource** | Client injects into context | Stable content worth always having at hand (guide, index, ontology) |
| **Prompt** | Client runs it as a user message | Canonical *workflow* (initialising a session, Q&A) |

---

## Resources {#resources}

All resources use the `sbd://toe/*` scheme and return `text/markdown`, `application/json` or `application/yaml` depending on the type.

### `sbd://toe/agent-guide` {#sbdtoeagent-guide}

**MIME:** `text/markdown`
**Content:** the agent's complete operational guide — modes (CONSULT / GUIDE / SETUP), routing by phase / domain / question type, epistemic patterns, controlled vocabulary, map of the 15 chapters.

**When to read:** **once per session**, before any call. It is the canonical *system prompt*.

> This resource is the source of what `generate_sbd_toe_skill` returns — saving it as a *skill file* is exactly injecting it permanently into the client's context.

### `sbd://toe/index-compact` {#sbdtoeindex-compact}

**MIME:** `application/json`
**Content:** compact map of the Manual — structured JSON with, per chapter, `chapterId`, `readableTitle`, `demand_by_level` (what is demanded at each level — applicability is graded) and `technologies`.

**When to read:** *inject into the system prompt* to eliminate exploratory discovery — the agent already "knows" the index before making any call.

### `sbd://toe/chapter-applicability/{riskLevel}` {#sbdtoechapter-applicabilityrisklevel}

**MIME:** `application/json`
**Parameter:** `{riskLevel}` = `L1` | `L2` | `L3` (interpolated into the URI)
**Content:** the **graded** applicability for that *risk level* — every chapter applies at every level; what changes is what each one demands. No chapter is excluded, and the resource itself declares this in the field `semantics`.

**Example:**

```
sbd://toe/chapter-applicability/L2
```

Returns an object with this shape, in which `chapters[]` carries what each chapter demands at that level:

```json
{
  "riskLevel": "L2",
  "semantics": "…",
  "canonical_anchor": "…",
  "chapters": [ … ]
}
```

**When to use:** quick initialisation without calling `consult_security_requirements` (which returns much more content).

### `sbd://toe/ontology` {#sbdtoeontology}

**MIME:** `application/yaml`
**Content:** the complete ontology — `domain_mapping` (requirement category → control domains), inference rules with priorities, *resolution pipelines* (consult / guide / threats / review), *concerns* lexicon, *role aliases*, entity schemas.

**When to read:** **once per session** to understand the deterministic resolution model before combining complex tools.

### `sbd://toe/grounded-codegen-guide` {#sbdtoegrounded-codegen-guide}

**MIME:** `text/markdown`
**Content:** agent guide for `prepare_sbd_toe_codegen_context` — *workflow*, branching by *status* (`ready_for_codegen` / `needs_clarification` / `needs_decomposition` / `unsupported_scope`), *output* discipline (cite ids from `citations`, fill in `security_rationale`, distinguish code/tests/evidence), and **explicit prohibitions** (do not invent IDs, do not declare compliance, do not pollute code with traceability noise).

**When to read:** always before any *codegen* or *review* work via `prepare_sbd_toe_codegen_context`.

### `sbd://toe/skill/{role}` · `sbd://toe/subagent/{role}` {#sbdtoeskillrole--sbdtoesubagentrole}

**MIME:** `text/markdown`
**Parameter:** `{role}` = one of the 13 canonical *roles* (aliases resolve)
**Content:** the same as `generate_sbd_toe_skill(role, format=skill)` (skill) and `…(role, format=subagent)` (*subagent* definition, *flavour* `harnessed` by default — grants the `mcp__sbd-toe__*` tools). Risk `L2` by default.

**When to use:** installing a role's configuration without calling the tool — read the resource and save it at the client's path.

### `sbd://toe/activation-vocabulary` {#sbdtoeactivation-vocabulary}

**Content:** the closed activation vocabulary — the values accepted in declarations (*concerns* and the remaining fields, including `roles`) and what each value activates.

**When to read:** before the first declaration in `select_sbd_toe_requirements` or `prepare_sbd_toe_codegen_context`. It is the source of the values — the pages of this mini-site do not copy them, because the vocabulary changes between versions.

### `sbd://toe/quick-start` {#sbdtoequick-start}

**Content:** the cheap session start.

**When to read:** at the start of the session, when the aim is to get going quickly without loading the complete guide straight away.

### `sbd://toe/notes/{id}` · `sbd://toe/notes` {#sbdtoenotesid--sbdtoenotes}

**Parameter:** `{id}` = a `note_id` (interpolated into the URI)
**Content:** the notes that responses carry by reference. Instead of repeating the same note in every response, the server returns a `note_id`, and `sbd://toe/notes/{id}` resolves it. The description of `sbd://toe/notes` is in the served list (`resources/list`).

### `sbd://toe/model` · `sbd://toe/codegen-instructions/{mode}` {#sbdtoemodel--sbdtoecodegen-instructionsmode}

The description of both is in the served list (`resources/list`).

### `sbd://toe/version` {#sbdtoeversion}

**MIME:** `application/json`
**Content:** server identity + *provenance* of the knowledge served (Manual, KG, ontology, contract), read from the *pin* of the consumed bundle.

```json
{
  "name": "…",
  "version": "…",
  "manual": "…",
  "kg": "…",
  "ontology": "…",
  "serving_contract": "…",
  "surface_history": "…"
}
```

**When to use:** *troubleshooting* — confirming the active version and the *provenance* (which Manual/KG/ontology the server serves), and whether it covers the expected content (see [troubleshooting / FAQ](./10-troubleshooting-faq.md) on *content lag*).

---

## Prompts {#prompts}

### `setup_sbd_toe_agent(riskLevel, projectRole)` {#setup_sbd_toe_agentrisklevel-projectrole}

Initialises the session.

**Parameters:**
- `riskLevel`: `L1` | `L2` | `L3`
- `projectRole`: one of the 13 canonical *roles*

**Result:** a user message that fixes the `riskLevel` and the role and leads the agent to make the initialisation calls. The response describes what each chapter demands at that level — applicability is graded, no chapter is excluded — and the rules of the role.

Being an MCP *prompt*, it only exists in clients that support *prompts*; Claude Desktop, for example, does not expose it. In those clients, the session starts from the resources (`sbd://toe/quick-start`, `sbd://toe/activation-vocabulary`) and from the first declaration in `select_sbd_toe_requirements`.

### `ask_sbd_toe_manual(question)` {#ask_sbd_toe_manualquestion}

Direct Q&A *grounded* in the Manual.

**Parameters:**
- `question`: question in natural language

**Result:** the agent is instructed to use `search_sbd_toe_manual` or `consult_security_requirements` depending on the type of question, and to answer with citable IDs.

### `prepare_grounded_codegen(task, mode?, riskLevel?, concerns?, stack?, regulatoryFrameworks?, includeRegulatoryOverlay?)` {#prepare_grounded_codegentask-mode-risklevel-concerns-stack-regulatoryframeworks-includeregulatoryoverlay}

End-to-end *grounded codegen*: embeds the `sbd://toe/grounded-codegen-guide` guide (above) and the task in a single message, and instructs the agent to call `prepare_sbd_toe_codegen_context` **before** producing code.

**Parameters:**
- `task`: concrete coding task (mandatory; e.g. "Add payload validation to PATCH /users/:id/email")
- `mode`: `codegen` | `review` | `test-plan` (default `codegen`)
- `riskLevel`: `L1` | `L2` | `L3` · `concerns`: explicit list — in declarative mode nothing is inferred from the `task`: without a declaration, the response is `needs_input`, with the accepted vocabulary · `stack`: informative
- `regulatoryFrameworks` (e.g. `RGPD`, `EXT-DORA`; published codes: `RGPD`, `DORA`, `NIS2`, `CRA`, `AI-ACT`, `ENISA-CSA`, or the form `EXT-…`) · `includeRegulatoryOverlay`: when true, exposes the context of the regulatory overlay

**Result:** the agent is required to cite ids from `citations`, fill in the `security_rationale_template`, distinguish code, tests and evidence, make no compliance claims, and route `needs_clarification` / `needs_decomposition` / `unsupported_scope` to dialogue with the user instead of guessing silently.

---

## Good practice — minimal session *bootstrap* {#boa-prática--bootstrap-mínimo-de-sessão}

```
1. Ler sbd://toe/quick-start  (arranque barato)
2. Ler sbd://toe/agent-guide  (ou ter skill instalada)
3. Ler sbd://toe/index-compact  (mapa compacto — barato)
4. Ler sbd://toe/activation-vocabulary  (valores aceites, antes da primeira declaração)
5. Executar prompt setup_sbd_toe_agent(riskLevel, projectRole)  (se o cliente expõe prompts)
6. Pronto para a primeira declaração — select_sbd_toe_requirements — e para CONSULT/GUIDE
```

If the session is for *codegen* / *review*: add `sbd://toe/grounded-codegen-guide` before any call to `prepare_sbd_toe_codegen_context`.

## Next {#a-seguir}

- [Use cases](./casos-uso/) — ready-made recipes combining these resources, prompts and tools.
- [Advanced patterns](./08-padroes-avancados.md) — multi-tool sequences for complex problems.
