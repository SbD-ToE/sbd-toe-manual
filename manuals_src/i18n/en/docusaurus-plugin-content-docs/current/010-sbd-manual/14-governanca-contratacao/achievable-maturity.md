---
id: achievable-maturity
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/achievable-maturity.md
  source_sha256: c61331bc4d3a82320cf3347e2b3b868692633b2e013829deaef10e63f67292a6
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 58c2c5ac4a7955e38d0c86455d4c550895675178061e063a105631de0e4bcfbf
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [chapter_role, framework_source_corpus, maturity, practitioner_manual, sbdtoe_sbd, shacl_owl, traceability, validation_evaluation]
  glossary_sha256: b53be3c3016c35427636086bb5cfba650674a05b0c5118f4428bb85c6db03944
  translated_at: 2026-09-26T12:00:10Z
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
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-dsomm:owasp-dsomm:3rd-party` | OWASP DSOMM | Supplier validation, contractual requirements, traceabi | external | derived |
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
