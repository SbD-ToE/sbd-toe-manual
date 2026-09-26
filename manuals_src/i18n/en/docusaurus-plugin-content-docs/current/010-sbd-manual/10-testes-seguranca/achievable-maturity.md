---
id: achievable-maturity
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/achievable-maturity.md
  source_sha256: ffd8fb4b698c40cb24ff300c24bd8c384bbf0a2f6ed319005a4a3d0945dcdade
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: fce99ce0f4ade3e73b2fb798ad9daf77795ab53504552ce1dc6fd3efcb7ee68b
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 2ffd43fd37c8802a693f5fa1e43a3d3a9df1ca9d5ea898c88f6f405bedc9d687
  glossary_keys: [chapter_role, framework_source_corpus, maturity, practitioner_manual, sbdtoe_sbd, shacl_owl, traceability, validation_evaluation]
  glossary_sha256: b53be3c3016c35427636086bb5cfba650674a05b0c5118f4428bb85c6db03944
  translated_at: 2026-09-26T10:31:23Z
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

Total: **12 MaturityMapping entities** mapped to this chapter (via `sbd-toe-knowledge-graph/data/entities/maturity_mappings.json`).

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
