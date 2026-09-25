---
id: achievable-maturity
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/achievable-maturity.md
  source_sha256: ccd05f4ff6699e7c7dcf520df8e184739fee47b6da119a44dcbcc174ba7b7d3b
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 022d2e3a638a94a09b059d52c3cfc1d577e0afd262244e8463a23c3683a893e6
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [chapter_role, framework_source_corpus, maturity, practitioner_manual, sbdtoe_sbd, shacl_owl, traceability]
  glossary_sha256: 0cd1e6309433d4e75cb1b588a32a8a222349580641d4ab09d983b24c6528e57c
  translated_at: 2026-09-25T20:18:42Z
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

Total: **14 MaturityMapping entities** mapped to this chapter (via `sbd-toe-knowledge-graph/data/entities/maturity_mappings.json`).

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
