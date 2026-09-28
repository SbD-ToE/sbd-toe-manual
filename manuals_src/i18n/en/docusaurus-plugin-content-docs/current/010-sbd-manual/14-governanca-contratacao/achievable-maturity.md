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
  source_path: 010-sbd-manual/14-governanca-contratacao/achievable-maturity.md
  source_sha256: 4b2b7a1c40e53d0bff42e754f012e99174e10ef998de50b645cddc0b890ccb80
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: f68f6a0219b71e4af0585d35c7d47a0c117cc27ad2ec3e2cf9cb6c2a449b4ff3
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [chapter_role, framework_source_corpus, maturity, practitioner_manual, shacl_owl, traceability, validation_evaluation]
  glossary_sha256: 0ffa4b86f028b03bd34d442629eeee9c1a7b220f318c137c01fe7cab7298b0b6
  translated_at: 2026-09-28T09:12:23Z
  stamped_at: 2026-09-28T09:12:23Z
  reviewed_by: null
---

# Achievable Maturity — Governance and Contracting

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
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-dsomm:owasp-dsomm:3rd-party` | OWASP DSOMM | Supplier validation, contractual requirements, traceability | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-dsomm:owasp-dsomm:governance` | OWASP DSOMM | Clear definition of ownership, policies, continuous control | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-dsomm:owasp-dsomm:tooling-metrics` | OWASP DSOMM | Governance KPIs and continuous feedback | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-dsomm:owasp-dsomm:training` | OWASP DSOMM | Formal onboarding of stakeholders | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-dsomm:visao-geral-de-alinhamento:dsomm` | OWASP DSOMM | Exceptions, KPIs, onboarding, validation, maturity | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-samm:owasp-samm-governance-e-education:education-guidance` | OWASP SAMM | Governance and Education | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-samm:owasp-samm-governance-e-education:governance` | OWASP SAMM | Governance and Education | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-samm:owasp-samm-governance-e-education:incident-management` | OWASP SAMM | Governance and Education | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-samm:visao-geral-de-alinhamento:samm-v2-1` | OWASP SAMM | Ownership, exceptions, traceability, training | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:slsa:slsa-supply-chain:1` | SLSA | Supply Chain | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:slsa:slsa-supply-chain:2` | SLSA | Supply Chain | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:slsa:slsa-supply-chain:3` | SLSA | Supply Chain | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:slsa:slsa-supply-chain:4` | SLSA | Supply Chain | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Contractual requirements, risk acceptance, traceability | external | derived |

---

## § SAMM v2 / DSOMM maturity progression {#-samm-v2--dsomm-maturity-progression}

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per the `confidence` field of the KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | — | Supplier validation, contractual requirements, traceability | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Clear definition of ownership, policies, continuous control | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Governance KPIs and continuous feedback | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Formal onboarding of stakeholders | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Exceptions, KPIs, onboarding, validation, maturity | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Governance and Education | — | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Governance and Education | — | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Governance and Education | — | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | — | Ownership, exceptions, traceability, training | `achievable-maturity.md` | 0.90 | Explicit |

---

## § SLSA build/integrity progression {#-slsa-buildintegrity-progression}

SLSA progression mapping (per §26 §4: SLSA only where it makes sense as a build/integrity progression — this chapter qualifies).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Supply Chain | — | Roles and third parties registered | `achievable-maturity.md` | Explicit |
| Supply Chain | — | Formal security clauses | `achievable-maturity.md` | Explicit |
| Supply Chain | — | Partial - validations without external attestation | `achievable-maturity.md` | Explicit |
| Supply Chain | — | Not applicable | `achievable-maturity.md` | Explicit |
| — | — | Contractual requirements, risk acceptance, traceability | `achievable-maturity.md` | Explicit |

---

## § Out-of-Maturity scope (regulatory alignment is NOT maturity) {#-out-of-maturity-scope-regulatory-alignment-não-maturity}

Per the §26 §4 discipline: regulatory alignment (PCI DSS, GDPR, NIS2, DORA, CRA, HIPAA) **must NOT be treated as a maturity score**. Regulatory items are recorded here for editorial visibility; conformance lives in separate obligations, not in the maturity progression.

_(Regulatory alignment for this chapter is handled via Manual ontology V2 ExternalObligation entities + the governance chapters (Ch. 14); not enumerated here to avoid conflation with the maturity claim.)_

---

## § Future-work register (maturity gaps) {#-future-work-register-maturity-gaps}

_(No maturity claim in gap state for this chapter.)_
