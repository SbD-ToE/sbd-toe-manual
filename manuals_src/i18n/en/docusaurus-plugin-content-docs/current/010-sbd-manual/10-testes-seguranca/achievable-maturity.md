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
  source_path: 010-sbd-manual/10-testes-seguranca/achievable-maturity.md
  source_sha256: 786965da9910ca94bc69d218bfaa2d309a9f724024f0446845ed4cf5958b3678
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: 6469a95a2af522979070c02e0cf010b42e5080a63101d2a2a5ade13bcb3a6cb6
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [chapter_role, framework_source_corpus, maturity, practitioner_manual, shacl_owl, traceability, validation_evaluation]
  glossary_sha256: 0ffa4b86f028b03bd34d442629eeee9c1a7b220f318c137c01fe7cab7298b0b6
  translated_at: 2026-09-28T09:12:14Z
  stamped_at: 2026-09-28T09:12:14Z
  reviewed_by: null
---

# Achievable Maturity — Security Testing

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
| MaturityMapping | `10-testes-seguranca:maturity:owasp-dsomm:owasp-dsomm-dominios-testing-design-development:design-development` | OWASP DSOMM | Testing + Design & Development domains | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:owasp-dsomm:owasp-dsomm-dominios-testing-design-development:testing` | OWASP DSOMM | Testing + Design & Development domains | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:owasp-dsomm:visao-geral-de-alinhamento:dsomm` | OWASP DSOMM | Continuous integration, traceability per release, automatic gates | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:owasp-samm:owasp-samm-verification-security-testing:1` | OWASP SAMM | Verification → Security Testing | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:owasp-samm:owasp-samm-verification-security-testing:2` | OWASP SAMM | Verification → Security Testing | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:owasp-samm:owasp-samm-verification-security-testing:3` | OWASP SAMM | Verification → Security Testing | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:owasp-samm:visao-geral-de-alinhamento:samm-v2-1` | OWASP SAMM | Automated tests, validation gates, findings management | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:slsa:slsa-build-test-coverage:1` | SLSA | Build/Test Coverage | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:slsa:slsa-build-test-coverage:2` | SLSA | Build/Test Coverage | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:slsa:slsa-build-test-coverage:3` | SLSA | Build/Test Coverage | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:slsa:slsa-build-test-coverage:4` | SLSA | Build/Test Coverage | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Limited coverage, validation of artefacts before deploy | external | derived |

---

## § SAMM v2 / DSOMM maturity progression {#-samm-v2--dsomm-maturity-progression}

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per the `confidence` field of the KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Testing + Design & Development domains | Validation per release, findings control, technical reporting | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Testing + Design & Development domains | Integrated SAST/DAST, fuzzing, feedback, gates | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Continuous integration, traceability per release, automatic gates | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Verification → Security Testing | Basic manual security tests | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Verification → Security Testing | Integration of automated tests into the pipeline | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Verification → Security Testing | Active findings management and continuous feedback | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | — | Automated tests, validation gates, findings management | `achievable-maturity.md` | 0.90 | Explicit |

---

## § SLSA build/integrity progression {#-slsa-buildintegrity-progression}

SLSA progression mapping (per §26 §4: SLSA only where it makes sense as a build/integrity progression — this chapter qualifies).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Build/Test Coverage | — | Minimum coverage via pipelines | `achievable-maturity.md` | Explicit |
| Build/Test Coverage | — | Traceable evidence and analysis | `achievable-maturity.md` | Explicit |
| Build/Test Coverage | — | Partial - depends on governance | `achievable-maturity.md` | Explicit |
| Build/Test Coverage | — | Not covered by the chapter | `achievable-maturity.md` | Explicit |
| — | — | Limited coverage, validation of artefacts before deploy | `achievable-maturity.md` | Explicit |

---

## § Out-of-Maturity scope (regulatory alignment is NOT maturity) {#-out-of-maturity-scope-regulatory-alignment-não-maturity}

Per the §26 §4 discipline: regulatory alignment (PCI DSS, GDPR, NIS2, DORA, CRA, HIPAA) **must NOT be treated as a maturity score**. Regulatory items are recorded here for editorial visibility; conformance lives in separate obligations, not in the maturity progression.

_(Regulatory alignment for this chapter is handled via Manual ontology V2 ExternalObligation entities + the governance chapters (Ch. 14); not enumerated here to avoid conflation with the maturity claim.)_

---

## § Future-work register (maturity gaps) {#-future-work-register-maturity-gaps}

_(No maturity claim in gap state for this chapter.)_
