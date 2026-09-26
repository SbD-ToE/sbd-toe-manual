---
id: achievable-maturity
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/achievable-maturity.md
  source_sha256: aa3ac6445f991ebc662368d810023530a2c4de59bd662e65d9b0866fd6b926e6
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 3b6f26f373c70056ca75e90e90d691d9ee29534853bb1c354b04d384040b040f
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 6163399f3326e10bced3afe0b9ddfa197cae2c643b2beeb28c226f7164a47a99
  glossary_keys: [audit_trail, chapter_role, framework_source_corpus, maturity, practitioner_manual, provenance, sbdtoe_sbd, shacl_owl, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: f1c7971f2339e29a94eac291d077ea4cba9f03650a1190206d6eb56bef540599
  translated_at: 2026-09-26T09:58:12Z
  reviewed_by: null
---

# Achievable Maturity — Containers and Images

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

Total: **13 MaturityMapping entities** mapped to this chapter (via `sbd-toe-knowledge-graph/data/entities/maturity_mappings.json`).

| Entity type | ID | Framework | Framework area | Authority class | Source mode |
|---|---|---|---|---|---|
| MaturityMapping | `09-containers-imagens:maturity:owasp-dsomm:owasp-dsomm-build-deploy-supply-chain-ops-monitoring:build-deploy` | OWASP DSOMM | Build & Deploy / Supply Chain / Ops Monitoring | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-dsomm:owasp-dsomm-build-deploy-supply-chain-ops-monitoring:ops-monitoring` | OWASP DSOMM | Build & Deploy / Supply Chain / Ops Monitoring | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-dsomm:owasp-dsomm-build-deploy-supply-chain-ops-monitoring:supply-chain` | OWASP DSOMM | Build & Deploy / Supply Chain / Ops Monitoring | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Deterministic build, provenance, hardening and observa | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-samm:owasp-samm-deployment-verification-e-governance:1` | OWASP SAMM | Deployment, Verification and Governance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-samm:owasp-samm-deployment-verification-e-governance:2` | OWASP SAMM | Deployment, Verification and Governance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-samm:owasp-samm-deployment-verification-e-governance:3` | OWASP SAMM | Deployment, Verification and Governance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | Secure build, policy-as-code, signing, control of regist | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:slsa:slsa-v1-0-build-integrity-provenance:1` | SLSA | Build Integrity & Provenance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:slsa:slsa-v1-0-build-integrity-provenance:2` | SLSA | Build Integrity & Provenance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:slsa:slsa-v1-0-build-integrity-provenance:3` | SLSA | Build Integrity & Provenance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:slsa:slsa-v1-0-build-integrity-provenance:4` | SLSA | Build Integrity & Provenance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Signatures, attestations, trusted pipelines and digest pin | external | derived |

---

## § SAMM v2 / DSOMM maturity progression {#-samm-v2--dsomm-maturity-progression}

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per the `confidence` field of the KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Build & Deploy / Supply Chain / Ops Monitoring | Deterministic pipelines, provenance verification and attestation. | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Build & Deploy / Supply Chain / Ops Monitoring | Observability, drift detection and shadow containers. | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Build & Deploy / Supply Chain / Ops Monitoring | Signing, traceability and governance of registries and dependencies. | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Deterministic build, provenance, hardening and runtime observability | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Deployment, Verification and Governance | Minimum governance of images and registries | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Deployment, Verification and Governance | Scanning and signing in CI/CD | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Deployment, Verification and Governance | Policy-as-code, admission controllers, auditable traceability | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | — | Secure build, policy-as-code, signing, control of registries and validation of ma | `achievable-maturity.md` | 0.90 | Explicit |

---

## § SLSA build/integrity progression {#-slsa-buildintegrity-progression}

SLSA progression mapping (per §26 §4: SLSA only where it makes sense as a build/integrity progression — this chapter qualifies).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Build Integrity & Provenance | — | Versioned Dockerfiles and auditable CI/CD | `achievable-maturity.md` | Explicit |
| Build Integrity & Provenance | — | Digest pinning and origin attestation | `achievable-maturity.md` | Explicit |
| Build Integrity & Provenance | — | Signatures, attestations and automatic verification | `achievable-maturity.md` | Explicit |
| Build Integrity & Provenance | — | Out of scope (infrastructure integration level) | `achievable-maturity.md` | Explicit |
| — | — | Signatures, attestations, trusted pipelines and digest pinning | `achievable-maturity.md` | Explicit |

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
