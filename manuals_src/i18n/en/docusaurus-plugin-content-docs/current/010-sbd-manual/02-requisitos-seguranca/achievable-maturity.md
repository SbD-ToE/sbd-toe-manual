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
  source_path: 010-sbd-manual/02-requisitos-seguranca/achievable-maturity.md
  source_sha256: bcf68a235b8bba7caa79244d0cf6407715fbc931eb0d902b690da04baba74a9b
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: 3e5361e37d6751a287c1908468b739604a8666f8c0ed9bc4b3a45bf5ede87d8e
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [chapter_role, framework_source_corpus, mapping, maturity, practitioner_manual, shacl_owl, validation_evaluation]
  glossary_sha256: a6eb7aa95f3969df33e703480390b72fa8cdfe5d2ade93d7c45faf3d0b3053d6
  translated_at: 2026-09-28T09:11:55Z
  stamped_at: 2026-09-28T09:11:55Z
  reviewed_by: null
---

# Achievable Maturity — Security Requirements

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
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-dsomm:owasp-dsomm-requirements-architecture-verification:architecture` | OWASP DSOMM | Requirements, Architecture, Verification | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-dsomm:owasp-dsomm-requirements-architecture-verification:requirements` | OWASP DSOMM | Requirements, Architecture, Verification | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-dsomm:owasp-dsomm-requirements-architecture-verification:verification` | OWASP DSOMM | Requirements, Architecture, Verification | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Validated catalogue, risk-based derivation, acceptance criteria | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-samm:owasp-samm-design-security-requirements:1` | OWASP SAMM | Design → Security Requirements | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-samm:owasp-samm-design-security-requirements:2` | OWASP SAMM | Design → Security Requirements | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-samm:owasp-samm-design-security-requirements:3` | OWASP SAMM | Design → Security Requirements | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | Proportional, traceable requirements with formal validation | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:slsa:slsa-build-verification-requirements:1` | SLSA | Build & Verification Requirements | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:slsa:slsa-build-verification-requirements:2` | SLSA | Build & Verification Requirements | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:slsa:slsa-build-verification-requirements:3` | SLSA | Build & Verification Requirements | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Definition of acceptance criteria based on requirements | external | derived |

---

## § SAMM v2 / DSOMM maturity progression {#-samm-v2--dsomm-maturity-progression}

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per the `confidence` field of the KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Requirements, Architecture, Verification | Risk-based mapping and dependency on architecture | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Requirements, Architecture, Verification | Testable, traceable and validated requirements | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Requirements, Architecture, Verification | Criteria defined for the validation of requirements | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Validated catalogue, risk-based derivation, acceptance criteria | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Design → Security Requirements | Define minimum security requirements | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Design → Security Requirements | Requirements defined on the basis of risks | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Design → Security Requirements | Requirements linked to metrics and effectiveness controls | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | — | Proportional, traceable requirements with formal validation | `achievable-maturity.md` | 0.90 | Explicit |

---

## § SLSA build/integrity progression {#-slsa-buildintegrity-progression}

SLSA progression mapping (per §26 §4: SLSA only where it makes sense as a build/integrity progression — this chapter qualifies).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Build & Verification Requirements | — | Explicit application of criteria | `achievable-maturity.md` | Explicit |
| Build & Verification Requirements | — | Out of scope | `achievable-maturity.md` | Explicit |
| Build & Verification Requirements | — | Implemented in other chapters | `achievable-maturity.md` | Explicit |
| — | — | Definition of acceptance criteria based on requirements | `achievable-maturity.md` | Explicit |

---

## § Out-of-Maturity scope (regulatory alignment is NOT maturity) {#-out-of-maturity-scope-regulatory-alignment-não-maturity}

Per the §26 §4 discipline: regulatory alignment (PCI DSS, GDPR, NIS2, DORA, CRA, HIPAA) **must NOT be treated as a maturity score**. Regulatory items are recorded here for editorial visibility; conformance lives in separate obligations, not in the maturity progression.

_(Regulatory alignment for this chapter is handled via Manual ontology V2 ExternalObligation entities + the governance chapters (Ch. 14); not enumerated here to avoid conflation with the maturity claim.)_

---

## § Future-work register (maturity gaps) {#-future-work-register-maturity-gaps}

_(No maturity claim in gap state for this chapter.)_
