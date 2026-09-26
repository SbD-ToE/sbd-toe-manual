---
id: achievable-maturity
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/achievable-maturity.md
  source_sha256: fcc5c5a30e6b1beed330b5d64b3e84b50676f65c721da8c52a06ce07be165884
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 570899bc69361314c238b0f1cc52105eecb65016437586500b50d1728068452d
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5536afdcc04f76a07c66e747133c73d68308884707c296abf945937a9630a312
  glossary_keys: [chapter_role, framework_source_corpus, maturity, practitioner_manual, sbdtoe_sbd, shacl_owl, traceability, validation_evaluation]
  glossary_sha256: b53be3c3016c35427636086bb5cfba650674a05b0c5118f4428bb85c6db03944
  translated_at: 2026-09-26T08:32:01Z
  reviewed_by: null
---

# Achievable Maturity — Secure Architecture

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
| MaturityMapping | `04-arquitetura-segura:maturity:owasp-dsomm:owasp-dsomm-architecture-requirements-risk:architecture` | OWASP DSOMM | Architecture, Requirements, Risk | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:owasp-dsomm:owasp-dsomm-architecture-requirements-risk:requirements` | OWASP DSOMM | Architecture, Requirements, Risk | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:owasp-dsomm:owasp-dsomm-architecture-requirements-risk:risk-analysis` | OWASP DSOMM | Architecture, Requirements, Risk | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Architecture requirements, traceability, trust zones | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:owasp-samm:owasp-samm-design-architecture-design:1` | OWASP SAMM | Design → Architecture & Design | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:owasp-samm:owasp-samm-design-architecture-design:2` | OWASP SAMM | Design → Architecture & Design | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:owasp-samm:owasp-samm-design-architecture-design:3` | OWASP SAMM | Design → Architecture & Design | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | Formal principles, validation and documentation of the architecture | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:slsa:slsa-provenance-isolation:1` | SLSA | Provenance & Isolation | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:slsa:slsa-provenance-isolation:2` | SLSA | Provenance & Isolation | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:slsa:slsa-provenance-isolation:34` | SLSA | Provenance & Isolation | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Segmentation and isolation of the architecture | external | derived |

---

## § SAMM v2 / DSOMM maturity progression {#-samm-v2--dsomm-maturity-progression}

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per the `confidence` field of the KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Architecture, Requirements, Risk | Segmentation, trust zones, explicit treatment | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Architecture, Requirements, Risk | Formal requirements by component type | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Architecture, Requirements, Risk | Integration with threat modelling and risk acceptance by exception | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Architecture requirements, traceability, trust zones | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Design → Architecture & Design | Architecture defined informally | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Design → Architecture & Design | Documentation with proportional validation | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Design → Architecture & Design | Continuous integration and automated review | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | — | Formal principles, validation and documentation of the architecture | `achievable-maturity.md` | 0.90 | Explicit |

---

## § SLSA build/integrity progression {#-slsa-buildintegrity-progression}

SLSA progression mapping (per §26 §4: SLSA only where it makes sense as a build/integrity progression — this chapter qualifies).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Provenance & Isolation | — | Segmentation and trust zones | `achievable-maturity.md` | Explicit |
| Provenance & Isolation | — | Documented requirements | `achievable-maturity.md` | Explicit |
| Provenance & Isolation | — | Out of scope (see Ch. 06 and 08) | `achievable-maturity.md` | Explicit |
| — | — | Segmentation and isolation of the architecture | `achievable-maturity.md` | Explicit |

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
