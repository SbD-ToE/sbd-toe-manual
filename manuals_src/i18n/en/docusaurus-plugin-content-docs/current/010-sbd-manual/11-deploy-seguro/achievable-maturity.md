---
id: achievable-maturity
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/achievable-maturity.md
  source_sha256: 3e482f51e65af1c7a4b93217eccf33ca2cc7a12f04ffb0e8e13007033604b22d
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: b01fa48b90d3f1f5893057679c853a75ab3d243b894cdad31dbfba67f2921104
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, framework_source_corpus, maturity, practitioner_manual, provenance, sbdtoe_sbd, shacl_owl, traceability, validation_evaluation]
  glossary_sha256: 058360a7f0a15a01b32caa2b01030e8787bd192635b3e3830a1d0f3c814d961e
  translated_at: 2026-09-26T11:00:45Z
  stamped_at: 2026-09-26T18:35:22Z
  reviewed_by: null
---

# Achievable Maturity — Secure Deployment

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

Total: **11 MaturityMapping entities** mapped to this chapter (via `sbd-toe-knowledge-graph/data/entities/maturity_mappings.json`).

| Entity type | ID | Framework | Framework area | Authority class | Source mode |
|---|---|---|---|---|---|
| MaturityMapping | `11-deploy-seguro:maturity:owasp-dsomm:owasp-dsomm-deploy-seguro-como-dominio-tecnico:design-development` | OWASP DSOMM | Secure Deployment as a Technical Domain | external | derived |
| MaturityMapping | `11-deploy-seguro:maturity:owasp-dsomm:visao-geral-de-alinhamento:dsomm` | OWASP DSOMM | Secure deployment, traceability, formal production control | external | derived |
| MaturityMapping | `11-deploy-seguro:maturity:owasp-samm:owasp-samm-verification-security-testing:1` | OWASP SAMM | Verification → Security Testing | external | derived |
| MaturityMapping | `11-deploy-seguro:maturity:owasp-samm:owasp-samm-verification-security-testing:2` | OWASP SAMM | Verification → Security Testing | external | derived |
| MaturityMapping | `11-deploy-seguro:maturity:owasp-samm:owasp-samm-verification-security-testing:3` | OWASP SAMM | Verification → Security Testing | external | derived |
| MaturityMapping | `11-deploy-seguro:maturity:owasp-samm:visao-geral-de-alinhamento:samm-v2-1` | OWASP SAMM | Gates, final validation, rollback | external | derived |
| MaturityMapping | `11-deploy-seguro:maturity:slsa:slsa-controlo-de-build-e-proveniencia:1` | SLSA | Build Control and Provenance | external | derived |
| MaturityMapping | `11-deploy-seguro:maturity:slsa:slsa-controlo-de-build-e-proveniencia:2` | SLSA | Build Control and Provenance | external | derived |
| MaturityMapping | `11-deploy-seguro:maturity:slsa:slsa-controlo-de-build-e-proveniencia:3` | SLSA | Build Control and Provenance | external | derived |
| MaturityMapping | `11-deploy-seguro:maturity:slsa:slsa-controlo-de-build-e-proveniencia:4` | SLSA | Build Control and Provenance | external | derived |
| MaturityMapping | `11-deploy-seguro:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Promotion and artefact controls, validations | external | derived |

---

## § SAMM v2 / DSOMM maturity progression {#-samm-v2--dsomm-maturity-progression}

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per the `confidence` field of the KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Secure Deployment as a Technical Domain | Secure deployment, traceable rollback, exception control | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Secure deployment, traceability, formal production control | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Verification → Security Testing | Checklist and readiness gates | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Verification → Security Testing | Rollback with integrated validation | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Verification → Security Testing | Deployment justification, blocking and audit | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | — | Gates, final validation, rollback | `achievable-maturity.md` | 0.90 | Explicit |

---

## § SLSA build/integrity progression {#-slsa-buildintegrity-progression}

SLSA progression mapping (per §26 §4: SLSA only where it makes sense as a build/integrity progression — this chapter qualifies).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Build Control and Provenance | — | Pre-conditions and triggers defined | `achievable-maturity.md` | Explicit |
| Build Control and Provenance | — | Release validation and traceable rollback | `achievable-maturity.md` | Explicit |
| Build Control and Provenance | — | Partial - depends on integration with Ch. 07 and 12 | `achievable-maturity.md` | Explicit |
| Build Control and Provenance | — | Not addressed | `achievable-maturity.md` | Explicit |
| — | — | Promotion and artefact controls, validations | `achievable-maturity.md` | Explicit |

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
