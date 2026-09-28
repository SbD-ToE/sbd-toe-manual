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
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/achievable-maturity.md
  source_sha256: 4aa9a354a611c6dc905cc63d3364c8aa1dc8862b159114e57296bd7d5dc4edeb
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: b8969ce2c5c428c1fe6f920268002acd359f751004701bbf6b221e6ef7ddd019
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [chapter_role, framework_source_corpus, maturity, practitioner_manual, shacl_owl, traceability]
  glossary_sha256: d037c8da2648ece471ef78f0523b89c1a6321b871dce98cddf615418a10c2057
  translated_at: 2026-09-28T09:11:52Z
  stamped_at: 2026-09-28T09:11:52Z
  reviewed_by: null
---

# Achievable Maturity — Application Classification

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
| MaturityMapping | `01-classificacao-aplicacoes:maturity:owasp-dsomm:owasp-dsomm-governance-risk-management-requirements:compliance-mapping` | OWASP DSOMM | Governance, Risk Management, Requirements | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:owasp-dsomm:owasp-dsomm-governance-risk-management-requirements:governance-metrics` | OWASP DSOMM | Governance, Risk Management, Requirements | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:owasp-dsomm:owasp-dsomm-governance-risk-management-requirements:risk-management` | OWASP DSOMM | Governance, Risk Management, Requirements | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:owasp-dsomm:owasp-dsomm-governance-risk-management-requirements:security-requirements` | OWASP DSOMM | Governance, Risk Management, Requirements | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Requirements derivation, traceability, proportional decision | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:owasp-samm:owasp-samm-governance-risk-management:1` | OWASP SAMM | Governance → Risk Management | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:owasp-samm:owasp-samm-governance-risk-management:2` | OWASP SAMM | Governance → Risk Management | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:owasp-samm:owasp-samm-governance-risk-management:3` | OWASP SAMM | Governance → Risk Management | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | Risk classification by axes, integration into the SDLC | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:slsa:slsa-supply-chain-levels-for-software-artifacts:1` | SLSA | Supply Chain Levels for Software Artifacts | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:slsa:slsa-supply-chain-levels-for-software-artifacts:2` | SLSA | Supply Chain Levels for Software Artifacts | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:slsa:slsa-supply-chain-levels-for-software-artifacts:3` | SLSA | Supply Chain Levels for Software Artifacts | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:slsa:slsa-supply-chain-levels-for-software-artifacts:4` | SLSA | Supply Chain Levels for Software Artifacts | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Proportional definition of requirements according to criticality | external | derived |

---

## § SAMM v2 / DSOMM maturity progression {#-samm-v2--dsomm-maturity-progression}

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per the `confidence` field of the KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Governance, Risk Management, Requirements | Traceability to reference frameworks present | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Governance, Risk Management, Requirements | Does not define quantitative KPIs or formal reporting | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Governance, Risk Management, Requirements | Structured classification model applied systematically | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Governance, Risk Management, Requirements | Allows proportional, risk-based derivation | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Requirements derivation, traceability, proportional decision | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Governance → Risk Management | Basic classification of application risks is carried out | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Governance → Risk Management | Integration with organisational processes and traceability | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Governance → Risk Management | Quantitative analysis and continuous feedback | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | — | Risk classification by axes, integration into the SDLC | `achievable-maturity.md` | 0.90 | Explicit |

---

## § SLSA build/integrity progression {#-slsa-buildintegrity-progression}

SLSA progression mapping (per §26 §4: SLSA only where it makes sense as a build/integrity progression — this chapter qualifies).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Supply Chain Levels for Software Artifacts | — | Classification by axes | `achievable-maturity.md` | Explicit |
| Supply Chain Levels for Software Artifacts | — | Out of scope | `achievable-maturity.md` | Explicit |
| Supply Chain Levels for Software Artifacts | — | Covered in other chapters | `achievable-maturity.md` | Explicit |
| Supply Chain Levels for Software Artifacts | — | Covered in other chapters | `achievable-maturity.md` | Explicit |
| — | — | Proportional definition of requirements according to criticality | `achievable-maturity.md` | Explicit |

---

## § Out-of-Maturity scope (regulatory alignment is NOT maturity) {#-out-of-maturity-scope-regulatory-alignment-não-maturity}

Per the §26 §4 discipline: regulatory alignment (PCI DSS, GDPR, NIS2, DORA, CRA, HIPAA) **must NOT be treated as a maturity score**. Regulatory items are recorded here for editorial visibility; conformance lives in separate obligations, not in the maturity progression.

_(Regulatory alignment for this chapter is handled via Manual ontology V2 ExternalObligation entities + the governance chapters (Ch. 14); not enumerated here to avoid conflation with the maturity claim.)_

---

## § Future-work register (maturity gaps) {#-future-work-register-maturity-gaps}

_(No maturity claim in gap state for this chapter.)_
