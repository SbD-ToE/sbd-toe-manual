---
id: epistemica-anti-patterns
title: Epistemic discipline and anti-patterns
description: How to label answers generated with the MCP — manual-grounded vs observed vs inferred vs not verified — and the most common mistakes to avoid.
sidebar_label: Epistemics & anti-patterns
sidebar_position: 9
tags:
  - mcp
  - epistemica
  - anti-patterns
  - rigor
translation:
  source_locale: pt
  source_path: 020-assets/mcp/09-epistemica-anti-patterns.md
  source_sha256: 000fe2edbb0518e606b6a01c215919ad3ca70e43fe1ec2577ae41f293c29d361
  source_commit: 4e04c6c26f9325b8a3515d4ccd3b126f58be3b1e
  target_sha256: be28be7d64a9793d38081c0e8aed18b56a981579cc4251f2532747fbf6e506b0
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 211df96a27d713b5934d7534d61f1972d877902236e63b858563d206c67ccaa8
  glossary_keys: [avaliacao, chapter_role, discipline, framework_source_corpus, llm, mcp, normative_empirical, practitioner_manual, sbdtoe_sbd, slug_threat_modeling, validation_evaluation]
  glossary_sha256: 9976562dbfc7768ff3f2c7ead0e84b1b11d2490fb7cd007023dbd2815d44d0af
  translated_at: 2026-09-26T14:55:22Z
  reviewed_by: null
---

# Epistemic discipline and anti-patterns

The MCP server returns **structured data**; the LLM **generates content from it**. Joining the two creates a temptation: presenting *LLM inferences* as if they were *facts from the manual*. For the output to earn the trust of auditors, *legal counsel* and *security champions*, every statement must be **labellable**.

## The 4 epistemic labels {#os-4-rótulos-epistémicos}

| Label | Definition | Green light for the user |
|---|---|---|
| **manual-grounded** | Retrieved via MCP — cite `chapterId` or ID (`CTRL-*`, `<CAT>-NNN`, `MT-*`, `ART-*`) | "The manual says: `AUT-001` (MFA mandatory). `<texto verbatim ou parafraseado fielmente>`." |
| **observed** | Directly visible in the repository / codebase | "In file `src/auth/login.ts:42`, I observe: `<…>`." |
| **inferred** | A logical conclusion drawn from *grounded* + *observed* — mark it explicitly | "Inference: given that `AUT-001` requires MFA, and the code only validates the password, the second factor is missing." |
| **not verified** | Not confirmed | "Not verified: `<…>`. Human inspection / test / log is recommended." |

### Golden rule {#regra-de-ouro}

> **When in doubt, prefer `not verified` to presenting something as fact.**
>
> Marking as `not verified` lets the user act; wrongly marking as `manual-grounded` creates *false positives* that cost review effort and credibility.

---

## Where to apply each label {#onde-aplicar-cada-rótulo}

### `manual-grounded` {#manual-grounded}

Allowed only when:
- Returned by an MCP tool (`consult_*`, `get_*`, `query_*`, `resolve_*`, `prepare_*`)
- The cited ID exists in the output of the call
- The text reflects what the output says (neither amplifies nor reduces it)

❌ Do **not** mark as *grounded*:
- Results of `search_sbd_toe_manual` that **were not read** (only seen as a *snippet*) — those are a lead, not evidence
- Cross-tool synthesis (e.g. "`AUT-001` + `LOG-003` imply X") — that is `inferred`

### `observed` {#observed}

Allowed only when:
- The file/line was read (not inferred from the file name)
- The observation is literally verifiable

❌ Do **not** mark as *observed*:
- "The system probably does X" — without having read the code
- Behaviour expected because of the *framework* — that is `inferred`

### `inferred` {#inferred}

Always mark explicitly when:
- `manual-grounded` + `observed` are combined to reach a conclusion
- General security knowledge is applied to a specific context
- A link without `mitigation_confidence: "derived"` is extended to another situation

Recommended form: **"Inference: `<conclusão>`. Based on: `<grounded ID>` + `<observação>`."**

### `not verified` {#not-verified}

Use generously. Cases:
- The tool returned an empty list (`controls: []`, `threats: []`, `assignments: []`)
- The *risk level* was not confirmed by the user
- The result needs a test / scan / log that has not run yet
- The question touches content later than the served *snapshot* (see `sbd://toe/version`)

---

## MCP-specific confidence flags {#confidence-flags-específicos-do-mcp}

Some tools return their own confidence fields. Translate them into labels:

| MCP field | Translation |
|---|---|
| `mitigation_confidence: "derived"` | `manual-grounded` (structural link) |
| link without `mitigation_confidence: "derived"` | `inferred` — flag explicitly |
| `completeness_report.m_recall < 1.0` | signal **partial coverage** — what is missing is `not verified` |
| `coverage.hasMore: true` / `coverage_gaps` | a **paginated / with declared gaps** result — continue via `nextOffset`; the server is *coverage-preserving* (nothing silently truncated), but "page 1" ≠ "everything" |
| `rule_trace` without `CONCERNS_FILTER_*` when concerns were passed | a sign of a problem — it may be returning more than was filtered for |

---

## General anti-patterns {#anti-patterns-gerais}

### 1. Inventing IDs {#1-inventar-ids}

❌ "Control `CTRL-09-99` covers this."
✅ Verify via `query_sbd_toe_entities({query: "CTRL-09-99"})` before citing. If it does not exist, say: *"No applicable control found in the manual for this case — flag for human review."*

### 2. Declaring regulatory compliance {#2-declarar-conformidade-regulatória}

❌ "This code is compliant with NIS2 Art. 21."
✅ "The manual's NIS2 cross-check maps Art. 21 ↔ chapters N and M. Not a declaration of compliance — it requires an assessment by *legal counsel* + operational evidence."

### 3. Treating code as evidence {#3-tratar-código-como-evidência}

❌ "I implemented the lockout, so the control is covered."
✅ "Proposed implementation. **Expected evidence:** a test in `test/auth/lockout.spec.ts` + log entry `auth.lockout.activated` with schema X."

### 4. Merging manual-grounded with inferred {#4-fundir-manual-grounded-com-inferred}

❌ "The manual says that rate limiting + monitoring prevent credential stuffing."
✅ "Manual-grounded: the output links `MT-NNN` (credential stuffing) to `CTRL-<domain>-<slug>-<hash>` with `mitigation_confidence: derived`. Inference (mine): applied together they cover the threat — marked as an inference, not as a fact from the manual."

### 5. Skipping the `needs_clarification` / `needs_decomposition` gate {#5-saltar-gate-needs_clarification--needs_decomposition}

❌ Calling `prepare_sbd_toe_codegen_context` again with the same payload to "try again".
✅ Stop, talk with the user, **call again only after new inputs**.

### 6. Showing an inferred link as a certainty {#6-mostrar-mitigation_confidence-heuristic-como-certeza}

❌ "`CTRL-…` mitigates `MT-NNN`." — presented as a certainty, without `mitigation_confidence: "derived"`.
✅ "`CTRL-…` mitigates `MT-NNN` — an **inferred** link (without `mitigation_confidence: derived`); validate with a test / human review."

### 7. Assuming the *snapshot* coverage without confirming it {#7-assumir-a-cobertura-do-snapshot-sem-a-confirmar}

❌ Answering about a normative cross-check (or any page) assuming that the MCP serves it — or that it does not.
✅ Read `sbd://toe/version` (manual, KG, ontology) and, when in doubt, validate with `inspect_sbd_toe_retrieval` whether the document appears among the *top-ranked records*. The published normative cross-checks — **CRA / DORA / NIS2 / GDPR / AI Act / ENISA-CSA** — are indexed in the served *snapshot*; content later than the *snapshot* lives only in the web manual until the next publication (see [content lag](./10-troubleshooting-faq.md#content-lag)).

### 8. Confusing (ontological) *concerns* with STRIDE domains {#8-confundir-concerns-ontológicos-com-domínios-stride}

❌ `concerns: ["spoofing", "tampering"]`
✅ `concerns: ["auth", "integrity"]` — the ontological vocabulary is closed and maps to STRIDE domains indirectly.

### 9. Skipping `setup_sbd_toe_agent` at the start of the session {#9-saltar-setup_sbd_toe_agent-no-início-da-sessão}

❌ Starting to call tools without initialising.
✅ First message of the security session: `setup_sbd_toe_agent(riskLevel, projectRole)` — it loads the per-chapter demand and the *role* rules. In clients that do not expose *prompts* (such as Claude Desktop), start with `sbd://toe/quick-start` and the declaration in `select_sbd_toe_requirements`.

### 10. Regenerating the skill at the start of every session {#10-re-gerar-a-skill-no-início-de-cada-sessão}

❌ Calling `generate_sbd_toe_skill()` every time.
✅ Generate once, save it at the canonical path (`.claude/skills/sbd-toe.md`, etc.), regenerate **only after an upgrade of the MCP**.

### 11. Confusing "consuming MCP" with "exposing an MCP server" (distinct security scope) {#11-confundir-consumir-mcp-com-expor-mcp-server-escopo-de-segurança-distinto}

This mini-site covers the use of the MCP server SbD-ToE — consumption. When the organisation starts to **expose its own MCP server** (not consume one), it enters an additional security scope that is **not covered** by this mini-site nor by the SbD-ToE manual in general.

❌ Assuming that reading this mini-site covers the security of an MCP server to be published by the organisation.
✅ For exposed MCP servers, consult the **OWASP MCP Top 10 (2025)** — a dedicated catalogue that covers prompt injection in an MCP context, *tool poisoning*, *excessive permissions*, inadequate authentication/authorisation, insecure transport, input validation, *output handling*, insufficient monitoring and insecure defaults. The relevant SbD-ToE controls (`ARC-015`, `REQ-AGN-001..004`, `OPS-011..014`, Policy 38, Policy 39) apply directly — the OWASP MCP Top 10 works as a *specific coverage checklist*, complementary to the threat modelling of [Ch. 03 §playbook-agentic](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic).

---

## Rigour checklist before submitting any output {#checklist-de-rigor-antes-de-submeter-qualquer-output}

1. Does every statement carry one of the 4 labels?
2. Do all cited IDs exist in MCP outputs from the session?
3. Are links without `mitigation_confidence: derived` marked as inferred?
4. Was `m_recall < 1.0` flagged?
5. Is there no declaration of compliance?
6. Was code not presented as evidence?
7. For regulatory questions — was the *snapshot* coverage confirmed in `sbd://toe/version` (and the web manual consulted for later content)?

If any check fails → **review before delivering**.

## Next steps {#a-seguir}

- [Troubleshooting / FAQ](./10-troubleshooting-faq.md) — symptoms vs solutions.
- [Advanced patterns](./08-padroes-avancados.md) — for combining tools without losing rigour.
