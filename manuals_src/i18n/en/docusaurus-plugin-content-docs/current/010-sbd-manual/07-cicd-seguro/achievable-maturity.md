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
  source_path: 010-sbd-manual/07-cicd-seguro/achievable-maturity.md
  source_sha256: 010bf7f68cd8f2589f0044894a799008bc7d65678ff481c529c5e7b1c2b97e91
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: df723133a08cfb19d12a0e33cc37554af1d7f6952d4601a80e300e06d91f4ccd
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [chapter_role, framework_source_corpus, maturity, practitioner_manual, provenance, shacl_owl, traceability, validation_evaluation]
  glossary_sha256: 07cc006a9711d7d13de948d5eebbfd3db881f4820d466348764a8aeb810650b6
  translated_at: 2026-09-28T09:12:08Z
  stamped_at: 2026-09-28T09:12:08Z
  reviewed_by: null
---

# Achievable Maturity — Secure CI/CD

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

Total: **14 MaturityMapping entities** mapped to this chapter.

| Entity type | ID | Framework | Framework area | Authority class | Source mode |
|---|---|---|---|---|---|
| MaturityMapping | `07-cicd-seguro:maturity:owasp-dsomm:owasp-dsomm-build-test-release-operate:build` | OWASP DSOMM | Build, Test, Release, Operate | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:owasp-dsomm:owasp-dsomm-build-test-release-operate:operate` | OWASP DSOMM | Build, Test, Release, Operate | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:owasp-dsomm:owasp-dsomm-build-test-release-operate:release` | OWASP DSOMM | Build, Test, Release, Operate | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:owasp-dsomm:owasp-dsomm-build-test-release-operate:test` | OWASP DSOMM | Build, Test, Release, Operate | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Secure execution, artefact validation, signatures, traceability | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:owasp-samm:owasp-samm-build-deployment-automation:1` | OWASP SAMM | Build & Deployment Automation | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:owasp-samm:owasp-samm-build-deployment-automation:2` | OWASP SAMM | Build & Deployment Automation | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:owasp-samm:owasp-samm-build-deployment-automation:3` | OWASP SAMM | Build & Deployment Automation | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | Security integrated into the pipeline, segregation of environments | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:slsa:slsa-provenance-ci-cd-control:1` | SLSA | Provenance & CI/CD Control | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:slsa:slsa-provenance-ci-cd-control:2` | SLSA | Provenance & CI/CD Control | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:slsa:slsa-provenance-ci-cd-control:3` | SLSA | Provenance & CI/CD Control | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:slsa:slsa-provenance-ci-cd-control:4` | SLSA | Provenance & CI/CD Control | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Provenance, trusted builders, execution control, hardening of pipelines | external | derived |

---

## § SAMM v2 / DSOMM maturity progression {#-samm-v2--dsomm-maturity-progression}

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per the `confidence` field of the KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Build, Test, Release, Operate | Authenticated execution, trusted runners, provenance | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Build, Test, Release, Operate | Logs, audit and CI/CD flow control | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Build, Test, Release, Operate | Artefact signing and integrity | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Build, Test, Release, Operate | Validation and continuous traceability of results | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Secure execution, artefact validation, signatures, traceability | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Build & Deployment Automation | Minimum formalisation required | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Build & Deployment Automation | Authenticated and validated execution | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Build & Deployment Automation | Partial - depends on control external to the pipeline | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | — | Security integrated into the pipeline, segregation of environments | `achievable-maturity.md` | 0.90 | Explicit |

---

## § SLSA build/integrity progression {#-slsa-buildintegrity-progression}

SLSA progression mapping (per §26 §4: SLSA only where it makes sense as a build/integrity progression — this chapter qualifies).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Provenance & CI/CD Control | — | Authenticated execution with logs | `achievable-maturity.md` | Explicit |
| Provenance & CI/CD Control | — | Validation and signing of artefacts | `achievable-maturity.md` | Explicit |
| Provenance & CI/CD Control | — | Trusted environments and runners | `achievable-maturity.md` | Explicit |
| Provenance & CI/CD Control | — | Out of scope for this chapter (see Ch. 08 and 09) | `achievable-maturity.md` | Explicit |
| — | — | Provenance, trusted builders, execution control, hardening of pipelines | `achievable-maturity.md` | Explicit |

---

## § Out-of-Maturity scope (regulatory alignment is NOT maturity) {#-out-of-maturity-scope-regulatory-alignment-não-maturity}

Per the §26 §4 discipline: regulatory alignment (PCI DSS, GDPR, NIS2, DORA, CRA, HIPAA) **must NOT be treated as a maturity score**. Regulatory items are recorded here for editorial visibility; conformance lives in separate obligations, not in the maturity progression.

_(Regulatory alignment for this chapter is handled via Manual ontology V2 ExternalObligation entities + the governance chapters (Ch. 14); not enumerated here to avoid conflation with the maturity claim.)_

---

## § Future-work register (maturity gaps) {#-future-work-register-maturity-gaps}

_(No maturity claim in gap state for this chapter.)_
