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
  source_path: 010-sbd-manual/11-deploy-seguro/achievable-maturity.md
  source_sha256: ea2b4e96811c8e648d8157db192c3f7eab0edd5997d2c63754e78091560f40d4
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: 1951b4bde97ae6aa884150fa2ce53d594f5b67774f3223b2e0eb01870318b14c
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [chapter_role, framework_source_corpus, maturity, practitioner_manual, provenance, shacl_owl, traceability, validation_evaluation]
  glossary_sha256: 07cc006a9711d7d13de948d5eebbfd3db881f4820d466348764a8aeb810650b6
  translated_at: 2026-09-28T09:12:16Z
  stamped_at: 2026-09-28T09:12:16Z
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

Total: **11 MaturityMapping entities** mapped to this chapter.

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
