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
  source_path: 010-sbd-manual/09-containers-imagens/achievable-maturity.md
  source_sha256: 50e98df0b4be75729865f9e0d9d5f1cf82ac24a40cfdd278e3674e318747a61f
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: bf2c5e27a8528af71b0a7d4b393135d2babaf003e95c42d12c43baa9468ead02
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [audit_trail, chapter_role, framework_source_corpus, maturity, practitioner_manual, provenance, shacl_owl, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: c497e7e4b146e251a0c0af0557ca44e0df170a86a1f4d47b55d478575145b311
  translated_at: 2026-09-28T09:12:12Z
  stamped_at: 2026-09-28T09:12:12Z
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

Total: **13 MaturityMapping entities** mapped to this chapter.

| Entity type | ID | Framework | Framework area | Authority class | Source mode |
|---|---|---|---|---|---|
| MaturityMapping | `09-containers-imagens:maturity:owasp-dsomm:owasp-dsomm-build-deploy-supply-chain-ops-monitoring:build-deploy` | OWASP DSOMM | Build & Deploy / Supply Chain / Ops Monitoring | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-dsomm:owasp-dsomm-build-deploy-supply-chain-ops-monitoring:ops-monitoring` | OWASP DSOMM | Build & Deploy / Supply Chain / Ops Monitoring | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-dsomm:owasp-dsomm-build-deploy-supply-chain-ops-monitoring:supply-chain` | OWASP DSOMM | Build & Deploy / Supply Chain / Ops Monitoring | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Deterministic build, provenance, hardening and runtime observability | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-samm:owasp-samm-deployment-verification-e-governance:1` | OWASP SAMM | Deployment, Verification and Governance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-samm:owasp-samm-deployment-verification-e-governance:2` | OWASP SAMM | Deployment, Verification and Governance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-samm:owasp-samm-deployment-verification-e-governance:3` | OWASP SAMM | Deployment, Verification and Governance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | Secure build, policy-as-code, signing, control of registries and validation of manifests | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:slsa:slsa-v1-0-build-integrity-provenance:1` | SLSA | Build Integrity & Provenance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:slsa:slsa-v1-0-build-integrity-provenance:2` | SLSA | Build Integrity & Provenance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:slsa:slsa-v1-0-build-integrity-provenance:3` | SLSA | Build Integrity & Provenance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:slsa:slsa-v1-0-build-integrity-provenance:4` | SLSA | Build Integrity & Provenance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Signatures, attestations, trusted pipelines and digest pinning | external | derived |

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
| OWASP SAMM | — | Secure build, policy-as-code, signing, control of registries and validation of manifests | `achievable-maturity.md` | 0.90 | Explicit |

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
