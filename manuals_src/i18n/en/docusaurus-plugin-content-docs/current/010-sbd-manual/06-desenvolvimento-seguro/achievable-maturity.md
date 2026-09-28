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
  source_path: 010-sbd-manual/06-desenvolvimento-seguro/achievable-maturity.md
  source_sha256: ecb3fe8c6646c78005300a16a6bc3aba0e34d04557287c35c71bfb49a8efab3e
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: 5efd3e8859d0259f212e68bc1034f24f8e8d59ef2cafa7ba29ff2c9570bf46e1
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [chapter_role, framework_source_corpus, maturity, practitioner_manual, provenance, shacl_owl, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 1d8557e31dd420e253484e95d15ea2de563f77dd57f710b5f719af2405ec7234
  translated_at: 2026-09-28T09:12:05Z
  stamped_at: 2026-09-28T09:12:05Z
  reviewed_by: null
---

# Achievable Maturity — Secure Development

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
| MaturityMapping | `06-desenvolvimento-seguro:maturity:owasp-dsomm:owasp-dsomm-design-development-tooling-metrics:design-dev` | OWASP DSOMM | Design & Development, Tooling, Metrics | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:owasp-dsomm:owasp-dsomm-design-development-tooling-metrics:metrics` | OWASP DSOMM | Design & Development, Tooling, Metrics | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:owasp-dsomm:owasp-dsomm-design-development-tooling-metrics:tooling` | OWASP DSOMM | Design & Development, Tooling, Metrics | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Structured practices, automatic validations, evidence and ownership | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:owasp-samm:owasp-samm-implementation:1` | OWASP SAMM | Implementation | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:owasp-samm:owasp-samm-implementation:2` | OWASP SAMM | Implementation | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:owasp-samm:owasp-samm-implementation:3` | OWASP SAMM | Implementation | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | Linters, automatic validation, traceability, PR validation | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:slsa:slsa-build-validation-provenance:1` | SLSA | Build Validation & Provenance | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:slsa:slsa-build-validation-provenance:2` | SLSA | Build Validation & Provenance | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:slsa:slsa-build-validation-provenance:34` | SLSA | Build Validation & Provenance | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Integration of validations and provenance into the build | external | derived |

---

## § SAMM v2 / DSOMM maturity progression {#-samm-v2--dsomm-maturity-progression}

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per the `confidence` field of the KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Design & Development, Tooling, Metrics | Structured secure development practices | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Design & Development, Tooling, Metrics | Traceability, evidence, ownership and handling of exceptions | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Design & Development, Tooling, Metrics | Linters, integrable automatic validations | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Structured practices, automatic validations, evidence and ownership | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Implementation | Basic manual verification practices | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Implementation | Integration of automated validations into the pipeline | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Implementation | Continuous integration and structured testing | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | — | Linters, automatic validation, traceability, PR validation | `achievable-maturity.md` | 0.90 | Explicit |

---

## § SLSA build/integrity progression {#-slsa-buildintegrity-progression}

SLSA progression mapping (per §26 §4: SLSA only where it makes sense as a build/integrity progression — this chapter qualifies).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Build Validation & Provenance | — | Linters and PR validation | `achievable-maturity.md` | Explicit |
| Build Validation & Provenance | — | Change tracking and ownership | `achievable-maturity.md` | Explicit |
| Build Validation & Provenance | — | Out of scope for this chapter | `achievable-maturity.md` | Explicit |
| — | — | Integration of validations and provenance into the build | `achievable-maturity.md` | Explicit |

---

## § Out-of-Maturity scope (regulatory alignment is NOT maturity) {#-out-of-maturity-scope-regulatory-alignment-não-maturity}

Per the §26 §4 discipline: regulatory alignment (PCI DSS, GDPR, NIS2, DORA, CRA, HIPAA) **must NOT be treated as a maturity score**. Regulatory items are recorded here for editorial visibility; conformance lives in separate obligations, not in the maturity progression.

_(Regulatory alignment for this chapter is handled via Manual ontology V2 ExternalObligation entities + the governance chapters (Ch. 14); not enumerated here to avoid conflation with the maturity claim.)_

---

## § Future-work register (maturity gaps) {#-future-work-register-maturity-gaps}

_(No maturity claim in gap state for this chapter.)_
