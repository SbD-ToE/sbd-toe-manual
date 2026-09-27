---
id: achievable-maturity
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/achievable-maturity.md
  source_sha256: f6ba61340ce9f7c3be56cb0de70dc72f700d0613c6b32a09a88167f941c55978
  source_commit: e341b40c451d9ef4be61e6cd59d994cda54c1aa0
  target_sha256: 51e7a9b35cbf60a8761f438b82a402e5fce5c6e1fc280591d73503e7ef3a84cb
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, framework_source_corpus, mapping, maturity, practitioner_manual, sbdtoe_sbd, shacl_owl, slug_threat_modeling, traceability, validation_evaluation]
  glossary_sha256: b9a440ee8c48bfeeb24e55901bf47fc25eb5a4d8680bcff16ce067d461b9d79f
  translated_at: 2026-09-26T13:36:56Z
  stamped_at: 2026-09-26T18:33:15Z
  reviewed_by: null
---

# Achievable Maturity — Threat Modelling

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
| MaturityMapping | `03-threat-modeling:maturity:owasp-dsomm:owasp-dsomm-architecture-risk-analysis-requirements:architecture` | OWASP DSOMM | Architecture, Risk Analysis, Requirements | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:owasp-dsomm:owasp-dsomm-architecture-risk-analysis-requirements:requirements` | OWASP DSOMM | Architecture, Risk Analysis, Requirements | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:owasp-dsomm:owasp-dsomm-architecture-risk-analysis-requirements:risk-analysis` | OWASP DSOMM | Architecture, Risk Analysis, Requirements | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Integration into the SDLC, traceability, reusable threat maps | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:owasp-samm:owasp-samm-design-threat-assessment:1` | OWASP SAMM | Design → Threat Assessment | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:owasp-samm:owasp-samm-design-threat-assessment:2` | OWASP SAMM | Design → Threat Assessment | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:owasp-samm:owasp-samm-design-threat-assessment:3` | OWASP SAMM | Design → Threat Assessment | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | Structured modelling with STRIDE, DFDs and risk-based analysis | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:slsa:slsa-supply-chain-risk-awareness:1` | SLSA | Supply Chain Risk Awareness | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:slsa:slsa-supply-chain-risk-awareness:2` | SLSA | Supply Chain Risk Awareness | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:slsa:slsa-supply-chain-risk-awareness:3` | SLSA | Supply Chain Risk Awareness | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Indirect support for the proportional definition of controls | external | derived |

---

## § SAMM v2 / DSOMM maturity progression {#-samm-v2--dsomm-maturity-progression}

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per the `confidence` field of the KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Architecture, Risk Analysis, Requirements | Architecture and dependency analysis with threat mapping | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Architecture, Risk Analysis, Requirements | Generation of requirements from threat modelling and their validation | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Architecture, Risk Analysis, Requirements | Integration with risk classification and acceptance | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Integration into the SDLC, traceability, reusable threat maps | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Design → Threat Assessment | Threats identified systematically | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Design → Threat Assessment | Structured analysis with formal models and traceability | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Design → Threat Assessment | Continuous integration and organisational automation | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | — | Structured modelling with STRIDE, DFDs and risk-based analysis | `achievable-maturity.md` | 0.90 | Explicit |

---

## § SLSA build/integrity progression {#-slsa-buildintegrity-progression}

SLSA progression mapping (per §26 §4: SLSA only where it makes sense as a build/integrity progression — this chapter qualifies).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Supply Chain Risk Awareness | — | Classification and threat modelling | `achievable-maturity.md` | Explicit |
| Supply Chain Risk Awareness | — | Out of scope | `achievable-maturity.md` | Explicit |
| Supply Chain Risk Awareness | — | Handled in other chapters (CI/CD) | `achievable-maturity.md` | Explicit |
| — | — | Indirect support for the proportional definition of controls | `achievable-maturity.md` | Explicit |

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
