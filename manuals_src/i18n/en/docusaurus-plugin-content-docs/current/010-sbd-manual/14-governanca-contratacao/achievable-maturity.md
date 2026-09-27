---
id: achievable-maturity
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/achievable-maturity.md
  source_sha256: 86565e0a2fac0831cdf14ba54a6822400aa6013f0d3bdbe108ed73e051c9449f
  source_commit: e341b40c451d9ef4be61e6cd59d994cda54c1aa0
  target_sha256: 074157776e9b8083fc4b2aeacb9497916d21b6b4ca73e053b05d0e7e45328230
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, framework_source_corpus, maturity, practitioner_manual, sbdtoe_sbd, shacl_owl, traceability, validation_evaluation]
  glossary_sha256: 2071f9ebe9dd8c20a023fec0a7eb71e60f97693332419f69c4a89ba4d5910d79
  translated_at: 2026-09-26T13:37:11Z
  stamped_at: 2026-09-26T18:36:10Z
  reviewed_by: null
---

# Achievable Maturity — Governance and Contracting

## Summary {#sumário}

Credible maturity posture attainable if this chapter is implemented as written. The analysis follows the **§26 canon §4 discipline**: SAMM v2.1 + DSOMM are the primary sources; SLSA only where it makes sense as a build/integrity progression; **regulatory alignment is NOT a maturity score** and is recorded in § Out-of-Maturity scope.

Five sections:

- **§ Manual ontology V2 entities** — relevant MaturityMapping + Practice + Control entities
- **§ SAMM v2 / DSOMM maturity progression** — primary maturity sources per §26 §4
- **§ SLSA build/integrity progression** — where applicable to this chapter
- **§ Out-of-Maturity scope** — regulatory alignment (NOT a maturity score)
- **§ Future-work register** — maturity gaps registered for P8 §10

---

## § Manual ontology V2 — entities relevant to maturity {#-manual-ontology-v2--entities-relevantes-para-maturity}

Total: **14 MaturityMapping entities** mapped to this chapter (via `sbd-toe-knowledge-graph/data/entities/maturity_mappings.json`).

| Entity type | ID | Framework | Framework area | Authority class | Source mode |
|---|---|---|---|---|---|
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-dsomm:owasp-dsomm:3rd-party` | OWASP DSOMM | Supplier validation, contractual requirements, traceability | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-dsomm:owasp-dsomm:governance` | OWASP DSOMM | Clear definition of ownership, policies, continuous control | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-dsomm:owasp-dsomm:tooling-metrics` | OWASP DSOMM | Governance KPIs and continuous feedback | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-dsomm:owasp-dsomm:training` | OWASP DSOMM | Formal onboarding of stakeholders | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-dsomm:visao-geral-de-alinhamento:dsomm` | OWASP DSOMM | Exceptions, KPIs, onboarding, validation, maturity | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-samm:owasp-samm-governance-e-education:education-guidance` | OWASP SAMM | Governance and Education | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-samm:owasp-samm-governance-e-education:governance` | OWASP SAMM | Governance and Education | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-samm:owasp-samm-governance-e-education:incident-management` | OWASP SAMM | Governance and Education | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-samm:visao-geral-de-alinhamento:samm-v2-1` | OWASP SAMM | Ownership, exceptions, traceability, training | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:slsa:slsa-supply-chain:1` | SLSA | Supply Chain | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:slsa:slsa-supply-chain:2` | SLSA | Supply Chain | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:slsa:slsa-supply-chain:3` | SLSA | Supply Chain | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:slsa:slsa-supply-chain:4` | SLSA | Supply Chain | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Contractual requirements, risk acceptance, traceability | external | derived |

---

## § SAMM v2 / DSOMM maturity progression {#-samm-v2--dsomm-maturity-progression}

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per the `confidence` field of the KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | — | Supplier validation, contractual requirements, traceability | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Clear definition of ownership, policies, continuous control | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Governance KPIs and continuous feedback | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Formal onboarding of stakeholders | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Exceptions, KPIs, onboarding, validation, maturity | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Governance and Education | — | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Governance and Education | — | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Governance and Education | — | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | — | Ownership, exceptions, traceability, training | `achievable-maturity.md` | 0.90 | Explicit |

---

## § SLSA build/integrity progression {#-slsa-buildintegrity-progression}

SLSA progression mapping (per §26 §4: SLSA only where it makes sense as a build/integrity progression — this chapter qualifies).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Supply Chain | — | Roles and third parties registered | `achievable-maturity.md` | Explicit |
| Supply Chain | — | Formal security clauses | `achievable-maturity.md` | Explicit |
| Supply Chain | — | Partial - validations without external attestation | `achievable-maturity.md` | Explicit |
| Supply Chain | — | Not applicable | `achievable-maturity.md` | Explicit |
| — | — | Contractual requirements, risk acceptance, traceability | `achievable-maturity.md` | Explicit |

---

## § Out-of-Maturity scope (regulatory alignment is NOT maturity) {#-out-of-maturity-scope-regulatory-alignment-não-maturity}

Per the §26 §4 discipline: regulatory alignment (PCI DSS, GDPR, NIS2, DORA, CRA, HIPAA) **must NOT be treated as a maturity score**. Regulatory items are recorded here for editorial visibility; conformance lives in separate obligations, not in the maturity progression.

_(Regulatory alignment for this chapter is handled via Manual ontology V2 ExternalObligation entities + the governance chapters (Ch. 14); not enumerated here to avoid conflation with the maturity claim.)_

---

## § Future-work register (maturity gaps) {#-future-work-register-maturity-gaps}

_(No maturity claim in gap state for this chapter.)_

---

## Generation provenance {#generation-provenance}

- **Manual ontology V2 canonical:** `sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml` (`meta.version: '2.0'`)
- **KG canonical state:** sbd-toe-knowledge-graph master @ `5550a74`
- **Maturity mappings:** `data/entities/maturity_mappings.json` (168 items)
- **§26 methodology layer:** `00-fundamentos/canon/26-metodologia-validacao-claims.md` (Run 1 state @ a9e70c98)
- **§26 label rule:** deterministic per `confidence` field (≥0.85 Explicit; ≥0.65 Semantic; ≥0.4 Partial; &lt;0.4 Gap)
- **§26 §4 discipline applied:** SAMM/DSOMM primary; SLSA conditional; regulatory ≠ maturity
- **Generated by:** Manual Agent Run 2 (achievable-maturity enrichment)
- **Cycle:** Cycle B Run 2 — last content work pre frozen ceremony
