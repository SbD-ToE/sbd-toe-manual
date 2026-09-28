---
# Proveniência da geração: não se mostra ao leitor (extraída do corpo na v1.17.1).
sbdtoe_provenance:
  ontology_v2: 'sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml (meta.version: ''2.0'')'
  kg_state: sbd-toe-knowledge-graph master @ 5550a743bb9de205676c503da5e81863ed62ab54 (2026-05-11; commit de governação imediatamente a seguir à tag kg-v1-cycle-b-iter-3-aligned-2026-05-11 @ 482ece916cc254126894019432ebd113695365d9)
  generated_by: Manual Agent Run 2 (achievable-maturity enrichment)
  cycle: Cycle B Run 2 — last content work pre frozen ceremony
  notes:
  - 'Maturity mappings: data/entities/maturity_mappings.json (168 items)'
  - '§26 methodology layer: 00-fundamentos/canon/26-metodologia-validacao-claims.md (Run 1 state @ a9e70c98937d41587e86712199fab46854a8d6aa)'
  - '§26 label rule: deterministic per confidence field (≥0.85 Explícito; ≥0.65 Semântico; ≥0.4 Parcial; <0.4 Gap)'
  - '§26 §4 discipline applied: SAMM/DSOMM primary; SLSA conditional; regulatory ≠ maturity'
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/achievable-maturity.md
  source_sha256: 2d1a4ad98d217a9fc14c9dc94a7b81d8c98c9496f0f983910478584603ea1897
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: 8cd367d452e8c8f57f6a65c8cd9bf5d9a1223058aa4d4558d3b44b0b72c506db
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [chapter_role, framework_source_corpus, mapping, maturity, practitioner_manual, shacl_owl, slug_threat_modeling, traceability, validation_evaluation]
  glossary_sha256: 5565d2f8151ef275661b2fe24cd03f9629f66e91d5bd699b2e905e897b049c01
  translated_at: 2026-09-28T09:11:58Z
  stamped_at: 2026-09-28T09:11:58Z
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

Total: **12 MaturityMapping entities** mapped to this chapter.

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
