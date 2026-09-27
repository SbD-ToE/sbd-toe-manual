---
id: achievable-maturity
translation:
  source_locale: pt
  source_path: 010-sbd-manual/02-requisitos-seguranca/achievable-maturity.md
  source_sha256: 8c5929024495f6a448bb39b4d9892fb10e8658e5416e8981ba96e969f7077f35
  source_commit: e341b40c451d9ef4be61e6cd59d994cda54c1aa0
  target_sha256: 110ab275b959928d50539a68ac856a79a89cfe6e0c657f6c014b9cdfa23a7b2b
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, framework_source_corpus, mapping, maturity, practitioner_manual, sbdtoe_sbd, shacl_owl, validation_evaluation]
  glossary_sha256: 9481f522338ea6d9b695c5090091466fd23da5ae847bb2524859dc28827611ae
  translated_at: 2026-09-26T13:36:55Z
  stamped_at: 2026-09-26T18:32:57Z
  reviewed_by: null
---

# Achievable Maturity — Security Requirements

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

Total: **12 MaturityMapping entities** mapped to this chapter (via `sbd-toe-knowledge-graph/data/entities/maturity_mappings.json`).

| Entity type | ID | Framework | Framework area | Authority class | Source mode |
|---|---|---|---|---|---|
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-dsomm:owasp-dsomm-requirements-architecture-verification:architecture` | OWASP DSOMM | Requirements, Architecture, Verification | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-dsomm:owasp-dsomm-requirements-architecture-verification:requirements` | OWASP DSOMM | Requirements, Architecture, Verification | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-dsomm:owasp-dsomm-requirements-architecture-verification:verification` | OWASP DSOMM | Requirements, Architecture, Verification | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Validated catalogue, risk-based derivation, acceptance criteria | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-samm:owasp-samm-design-security-requirements:1` | OWASP SAMM | Design → Security Requirements | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-samm:owasp-samm-design-security-requirements:2` | OWASP SAMM | Design → Security Requirements | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-samm:owasp-samm-design-security-requirements:3` | OWASP SAMM | Design → Security Requirements | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | Proportional, traceable requirements with formal validation | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:slsa:slsa-build-verification-requirements:1` | SLSA | Build & Verification Requirements | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:slsa:slsa-build-verification-requirements:2` | SLSA | Build & Verification Requirements | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:slsa:slsa-build-verification-requirements:3` | SLSA | Build & Verification Requirements | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Definition of acceptance criteria based on requirements | external | derived |

---

## § SAMM v2 / DSOMM maturity progression {#-samm-v2--dsomm-maturity-progression}

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per the `confidence` field of the KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Requirements, Architecture, Verification | Risk-based mapping and dependency on architecture | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Requirements, Architecture, Verification | Testable, traceable and validated requirements | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Requirements, Architecture, Verification | Criteria defined for the validation of requirements | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Validated catalogue, risk-based derivation, acceptance criteria | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Design → Security Requirements | Define minimum security requirements | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Design → Security Requirements | Requirements defined on the basis of risks | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Design → Security Requirements | Requirements linked to metrics and effectiveness controls | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | — | Proportional, traceable requirements with formal validation | `achievable-maturity.md` | 0.90 | Explicit |

---

## § SLSA build/integrity progression {#-slsa-buildintegrity-progression}

SLSA progression mapping (per §26 §4: SLSA only where it makes sense as a build/integrity progression — this chapter qualifies).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Build & Verification Requirements | — | Explicit application of criteria | `achievable-maturity.md` | Explicit |
| Build & Verification Requirements | — | Out of scope | `achievable-maturity.md` | Explicit |
| Build & Verification Requirements | — | Implemented in other chapters | `achievable-maturity.md` | Explicit |
| — | — | Definition of acceptance criteria based on requirements | `achievable-maturity.md` | Explicit |

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
- **§26 label rule:** deterministic per the `confidence` field (≥0.85 Explicit; ≥0.65 Semantic; ≥0.4 Partial; &lt;0.4 Gap)
- **§26 §4 discipline applied:** SAMM/DSOMM primary; SLSA conditional; regulatory ≠ maturity
- **Generated by:** Manual Agent Run 2 (achievable-maturity enrichment)
- **Cycle:** Cycle B Run 2 — last content work pre frozen ceremony
