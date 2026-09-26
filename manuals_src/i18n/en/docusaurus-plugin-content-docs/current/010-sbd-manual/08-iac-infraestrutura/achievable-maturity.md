---
id: achievable-maturity
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/achievable-maturity.md
  source_sha256: 2e61eef103af2bc98cf8d063dfbb2b02878eaf51f94082334cb8c11f7c11be32
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: c3c05e0d5c1eae73635eabe989eca23cc6c126b11af458a3c1657f2ec2c980d8
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [chapter_role, framework_source_corpus, maturity, practitioner_manual, provenance, sbdtoe_sbd, shacl_owl, traceability, validation_evaluation]
  glossary_sha256: c549f75e0f101e1e0301dde3ae439a4c8223117053e0bb967c29e3b829cc38b3
  translated_at: 2026-09-26T09:25:33Z
  reviewed_by: null
---

# Achievable Maturity — IaC and Infrastructure

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
| MaturityMapping | `08-iac-infraestrutura:maturity:owasp-dsomm:owasp-dsomm-aplicacao-a-projetos-iac:build-test` | OWASP DSOMM | Application to IaC Projects | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:owasp-dsomm:owasp-dsomm-aplicacao-a-projetos-iac:design-dev` | OWASP DSOMM | Application to IaC Projects | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:owasp-dsomm:owasp-dsomm-aplicacao-a-projetos-iac:tooling` | OWASP DSOMM | Application to IaC Projects | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Validation, segregation of environments, state control | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:owasp-samm:owasp-samm-secure-build-para-iac:1` | OWASP SAMM | Secure Build for IaC | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:owasp-samm:owasp-samm-secure-build-para-iac:2` | OWASP SAMM | Secure Build for IaC | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:owasp-samm:owasp-samm-secure-build-para-iac:3` | OWASP SAMM | Secure Build for IaC | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | Control of IaC pipelines, linting, enforcement | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:slsa:slsa-fonte-build-e-proveniencia:1` | SLSA | Source, Build and Provenance | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:slsa:slsa-fonte-build-e-proveniencia:2` | SLSA | Source, Build and Provenance | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:slsa:slsa-fonte-build-e-proveniencia:3` | SLSA | Source, Build and Provenance | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:slsa:slsa-fonte-build-e-proveniencia:4` | SLSA | Source, Build and Provenance | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Validation of plans, provenance, segregation, control of b | external | derived |

---

## § SAMM v2 / DSOMM maturity progression {#-samm-v2--dsomm-maturity-progression}

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per the `confidence` field of the KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Application to IaC Projects | Linting, validation of plans, test pipelines | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Application to IaC Projects | IaC requirements, separation of environments, secure architecture | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Application to IaC Projects | Static analysis tools and automated validation | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Validation, segregation of environments, state control | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Secure Build for IaC | Manual configuration, without traceability | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Secure Build for IaC | Use of linters, automated control and pipelines | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Secure Build for IaC | Continuous integration with traceable artefacts | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | — | Control of IaC pipelines, linting, enforcement | `achievable-maturity.md` | 0.90 | Explicit |

---

## § SLSA build/integrity progression {#-slsa-buildintegrity-progression}

SLSA progression mapping (per §26 §4: SLSA only where it makes sense as a build/integrity progression — this chapter qualifies).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Source, Build and Provenance | — | Validators and formal manual approval | `achievable-maturity.md` | Explicit |
| Source, Build and Provenance | — | Control of plans and environments | `achievable-maturity.md` | Explicit |
| Source, Build and Provenance | — | Out of scope for this chapter | `achievable-maturity.md` | Explicit |
| Source, Build and Provenance | — | Out of scope for this chapter | `achievable-maturity.md` | Explicit |
| — | — | Validation of plans, provenance, segregation, control of builds | `achievable-maturity.md` | Explicit |

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
