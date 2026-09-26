---
id: achievable-maturity
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/achievable-maturity.md
  source_sha256: ffc27266299928c1d84a2ed289758fa457608baf5d8865db485ddbe2c29584a8
  source_commit: e341b40c451d9ef4be61e6cd59d994cda54c1aa0
  target_sha256: 7f259e0f302b2301775f7af1417732b7ae8abc9ccfdf2d61ea4606d15a0672fc
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [chapter_role, framework_source_corpus, maturity, practitioner_manual, provenance, sbdtoe_sbd, shacl_owl, traceability, validation_evaluation]
  glossary_sha256: c549f75e0f101e1e0301dde3ae439a4c8223117053e0bb967c29e3b829cc38b3
  translated_at: 2026-09-26T13:37:02Z
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

Total: **14 MaturityMapping entities** mapped to this chapter (via `sbd-toe-knowledge-graph/data/entities/maturity_mappings.json`).

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
