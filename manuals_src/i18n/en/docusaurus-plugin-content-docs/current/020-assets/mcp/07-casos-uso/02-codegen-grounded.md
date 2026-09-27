---
id: codegen-grounded
title: Grounded codegen
description: Generating code with prepare_sbd_toe_codegen_context — branching by status, citations discipline, mandatory security_rationale.
sidebar_label: Grounded codegen
sidebar_position: 2
tags:
  - mcp
  - casos-uso
  - codegen
  - citations
translation:
  source_locale: pt
  source_path: 020-assets/mcp/07-casos-uso/02-codegen-grounded.md
  source_sha256: 27ccb90e82593ab53a612d5b5a877ff84128d1e7f5573570c9a50753fb82482e
  source_commit: 058f86265e07bc86cb7f19162dd2c6b87fbcc0a7
  target_sha256: b9816cdecdbc421d4b0ba4f463848a2f37b4076af203a78c605b27e58fe32f24
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [appsec_core, discipline, framework_source_corpus, lifecycle_phase, mcp, open_closed_world, requirement_runtime, shacl_owl, slug_threat_modeling, traceability, verificacao_check, verification_taxonomy]
  glossary_sha256: 39dbf6c10a94a684d91fd6c88b6bd170c9e62239d5daef726ce3453b1071226f
  translated_at: 2026-09-26T17:58:19Z
  stamped_at: 2026-09-26T18:36:37Z
  reviewed_by: null
---

# Use case — Grounded codegen

When an agent is asked to implement something sensitive — a login endpoint with lockout, an encryption routine, an upload handler — the usual temptation is to let it write the code first and audit afterwards. The problem is that, without *grounding*, the agent will cite *good practices* that look right but have no traceable origin.

The `prepare_sbd_toe_codegen_context` was designed to invert that order. Before proposing a single line of code, the agent asks the server for the *context* that covers the task: active requirements, applicable controls, relevant *threats* and — if the request concerns a regulation — the normative *overlay*. It returns a `citations` block — the closed-world set of valid ids. From there, the generated code comes with a `security_rationale` in which each decision references real IDs or states explicitly *"no control covered — flag for human review"*.

## Prior requirements {#pré-requisitos}

- MCP installed, skill loaded.
- Read [`sbd://toe/grounded-codegen-guide`](../06-resources-prompts.md#sbdtoegrounded-codegen-guide) **once per session** before any call.

## Flow {#fluxo}

### 1. Decompose mentally — *bite-size* {#1-decompor-mentalmente--bite-size}

Criteria:
- **1 technical surface** (1 endpoint, 1 module, 1 group of files)
- **1 SDLC phase** (`implement` | `test` | `deploy` | `operate`)
- **1–3 *concerns***

If the task exceeds this, the server returns `needs_decomposition` — anticipate it.

### 2. Call the tool {#2-chamar-a-tool}

```json
prepare_sbd_toe_codegen_context({
  "task": "Implementar endpoint POST /login com lockout após 5 falhas em 10 minutos",
  "risk_level": "L2",
  "mode": "codegen",
  "detail": "lista",
  "concerns": ["auth", "logging"],
  "technologies": ["jwt"]
})
```

The response is `ready_for_codegen`, within the envelope. The `task` is recorded as context; what drives the selection is the declaration — `risk_level`, `concerns`, `technologies`. The response's `adjacency` warns of what was left undeclared and would change the set: in this case, public exposure.

:::note What changes when declaring more
Also declaring `"exposure": "public"` widens the selection to 70 requirements, more than the `lista` level promises to fit. The response then becomes `needs_decomposition`, with executable batches whose union is the whole selection. Batches may share requirements: what the preserved `technologies` bring in by themselves (here, SES-008 via `jwt`) comes in all of them. That is why the sum of the counts may exceed the total. It is not an error: it is the server saying that the task, as declared, does not fit in a single response at that level, and proposing how to go through it without losing anything.
:::

### 3. Branch by `status` {#3-ramificar-por-status}

#### `ready_for_codegen` {#ready_for_codegen}

Proceed. Mandatory discipline:

| Field | How to fill it in |
|---|---|
| `security_rationale.decisions[].cited_ids` | ≥1 id from `citations` per non-trivial decision; if none fits → `"none"` + justification |
| `security_rationale.validations[]` | Concrete validations implemented (surface, rule, rejection behaviour) |
| `security_rationale.expected_evidence[]` | Test path, log shape, SBOM entry, attestation, scan report — **code is not evidence** |
| `security_rationale.residual_risk` | What was **not** addressed in this *change* |

If `completeness_report.m_recall < 1.0` → **flag partial coverage to the user**.

#### `needs_input` {#needs_input}

**STOP**. Nothing was declared, and the server does not guess from the `task`. The response brings the accepted vocabulary, the candidates to confirm and, for inert declarations, the `valid_values`. Respond with:
1. The candidates, in plain language, for the user to confirm.
2. After confirmation, call again with the complete declaration.

#### `needs_clarification` {#needs_clarification}

**STOP**. Generate nothing. Respond with:
1. `reasons[]` in plain language.
2. Minimal questions derived from `suggestions[]`.

Do not call the tool again until the user replies.

#### `needs_decomposition` {#needs_decomposition}

**STOP**. Do not silently choose a sub-task. Respond with:
1. `reasons[]`.
2. When the selection goes beyond what the `detail` level promises to fit, the response carries in `requirement_ceiling.batches` the executable batches (`categories` + the preserved activators) whose union is the whole selection; batches may share requirements — present those batches, instead of redesigning sub-tasks by hand.
3. **Ask the user which batch to start with.**

#### `unsupported_scope` {#unsupported_scope}

**STOP**. Report the problem verbatim — do not fabricate IDs to carry on:

| Cause | Response |
|---|---|
| `AppSec Core v1 runtime ausente` | "Incomplete installation — reinstall or update the published package and report to the operator." |
| `Overlay regulatório ausente` | "Remove `regulatory_frameworks` / `include_regulatory_overlay`, or wait for publication." |
| `Framework regulatório desconhecida` | List the supported *short codes* of `regulatory_overlay.frameworks`. |

## Shape of the response {#forma-da-resposta}

What arrives with `ready_for_codegen` is designed to fit in the agent's context without losing traceability:

- **One object per requirement** — `{id, name, type, description, verify, evidence}`: the requirement, how it is verified and what evidence is expected, in the same place.
- **`detail` levels** — `lista`, `standard` and `full` serve the same set of citable ids and the same complete requirement; what changes is what comes *inline* and what comes by reference (see the [tool reference](../05-tools-reference.md#prepare_sbd_toe_codegen_context)). `lista` is the natural choice to start with.
- **Token envelope** — `lista` and `standard` promise to fit in an envelope, measured on the *payload* the client receives. Above it, the response is `needs_decomposition`, with the measured batches of `requirement_ceiling.batches`, which together cover the whole selection. `full` has no envelope and declares the price in `size_estimate`.
- **`adjacency`** — what was not declared and would change the selected set. It is the server's way of saying «this could also count» without deciding it for the agent.
- **`size_estimate`** — the size of the response itself; `within_envelope: false` warns that it exceeds the expected envelope.
- **Notes by reference** — instead of repeating the same note, the response carries a `note_id`, which resolves to `sbd://toe/notes/{id}`.

## Output discipline (`ready_for_codegen`) {#disciplina-de-output-ready_for_codegen}

### Three classes of artefact — always distinguish {#três-classes-de-artefacto--distinguir-sempre}

| Class | Definition | Example |
|---|---|---|
| **Code** | Proposed source | `src/auth/login.ts` |
| **Tests** | Automated checks that exercise `security_rationale.validations[]` | `test/auth/lockout.spec.ts` |
| **Evidence** | Artefacts that a *reviewer* inspects — log lines, SBOM, attestation, audit report, scan output. **Tests are evidence; code is not.** | Log: `auth.lockout.activated`, schema X |

### Where to cite IDs {#onde-citar-ids}

- ✅ **PR description / commit message / `security_rationale`** — always.
- ⚠️ **Source files** — only if the *WHY* is not obvious from the code. Avoid `// per ACO-IVF-001`.

### Naming {#nomenclatura}

- Entities with no `name` returned → refer to them by the exact `entity_id`.
- Verification comes per requirement: each object carries `verify` and `evidence`; the evidence pattern ids are in `completeness_report.verification.by_ref`.

## Anti-patterns {#anti-patterns}

- ❌ Inventing `ACO-...`, `ACM-...`, `EXT-...`, `EP-...`, `CTRL-...` IDs outside `citations`.
- ❌ Calling the tool again with the **same payload** after `needs_*` to "try again" — a *bypass* of the *scope gate*.
- ❌ Declaring compliance ("this code complies with GDPR Art. 32") — the *regulatory overlay* is a *cross-check*, **not** a compliance signal.
- ❌ Proposing `L3` controls in an `L1` task — respect the *risk level*.
- ❌ Copying entity names that traceability has not published.

## Skill / subagent — Claude Code {#skill--subagent--claude-code}

`.claude/agents/sbd-toe-codegen.md`:

```markdown
---
name: sbd-toe-codegen
description: Gera código grounded com prepare_sbd_toe_codegen_context. Respeita os status. Nunca inventa IDs nem declara conformidade.
tools: Read, Write, Edit, Grep, Glob, mcp__sbd-toe__*
---

# Workflow obrigatório

1. Ler sbd://toe/grounded-codegen-guide (1× por sessão).
2. Decompor a tarefa em bite-size (1 surface, 1 fase, 1–3 concerns).
3. Chamar prepare_sbd_toe_codegen_context com TODOS os parâmetros que se sabe.
4. Ramificar por status conforme tabela. NUNCA gerar código antes de ler status.
5. Em ready_for_codegen: gerar code + tests + security_rationale citando apenas ids de citations.
6. Em needs_*: STOP, dialogar com o utilizador, não tentar contornar (em needs_decomposition, seguir os lotes de requirement_ceiling.batches).

# Hard rules

- citations é o mundo fechado de ids válidos para esta tarefa.
- Tests são evidência; código não é.
- Regulatory overlay é cross-check, não conformidade.
- Em m_recall < 1.0, sinalizar cobertura parcial.
```

## `review` and `test-plan` modes {#modos-review-e-test-plan}

The same tool serves `mode: "review"` and `mode: "test-plan"`:

| Mode | Expected output |
|---|---|
| `codegen` | code + tests + security_rationale |
| `review` | findings per changed file, each mapped to 1+ ids from `citations` |
| `test-plan` | checklist grouped by `validated_id`; each test: input → outcome → the requirement's `verify` / `evidence` as the expectation (pattern ids via `completeness_report.verification.by_ref`) |

## Related {#relacionado}

- [PR audit](./auditoria-pr) — `mode: "review"` for PRs (simpler alternative without `prepare_sbd_toe_codegen_context`).
- [Threat modelling](./threat-modeling) — before *codegen*, understand the threats.
- [`sbd://toe/grounded-codegen-guide`](../06-resources-prompts.md#sbdtoegrounded-codegen-guide) — canonical source.
