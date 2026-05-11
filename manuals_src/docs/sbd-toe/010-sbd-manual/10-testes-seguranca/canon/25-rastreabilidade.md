# 25. Rastreabilidade — Testes de Segurança

## Sumário

Este capítulo é a **âncora primária** das slices AppSec Core V1: `ACO-TSV` (Testes de segurança e validação empírica).

Cobertura V1 entity-level: **19 entidades** primárias. Estrutura abaixo expõe four-way routing (per P8 pipeline primitive demonstration 2026-05-11):

- **§ Core-mapped coverage** — V1 entity → Manual section anchor → ES grounding
- **§ Manual-only coverage** — Manual sections out-of-Core-scope mas com ES grounding direct
- **§ Out-of-AppSec coverage** — Pure editorial sections (examples, narratives) sem ES grounding
- **§ Future-work register** — Content gaps registered as P8 §10 candidates

---

## § Core-mapped coverage

Tabela exposing V1 entity-level coverage with Manual section anchor + substrate v7 ES grounding. Three-way alignment per row: V1 (ontology) ↔ Manual (prose) ↔ ES (substrate).

### Slice `ACO-TSV` — Testes de segurança e validação empírica

| V1 entity | Type | Manual section anchor | ES grounding |
|---|---|---|---|
| `ACM-TSV-001` — Integrated Security Scanners | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-AU-6.2, SP800-53-CA-3.1; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_A, SAMM-ACTIVITY-D_SA_1_B; DSOMM: DSOMM-ACTIVITY-47419324E263415B815DE7161B6B905E, DSOMM-ACTIVITY-48F97F31931C46EB9B3EE2FEC0CD0426; PCI DSS v4.0.1: PCI-REQ-2, PCI-REQ-5; + 17 more sources |
| `ACM-TSV-002` — Test Execution Surfaces | M | addon/00-catalogo-requisitos.md (mechanism) | DSOMM: DSOMM-ACTIVITY-A340F46B63604CB8847BA0D3483D09D3, DSOMM-ACTIVITY-BFDACB521E3F431DAE72D844A5E86415; SP 800-53 r5: SP800-53-CA-8.2, SP800-53-CM-2.6; SAMM v2.1: SAMM-ACTIVITY-I_SB_3_B, SAMM-ACTIVITY-I_SD_2_A; MITRE ATLAS: AML.TA0005, AML.T0011; + 4 more sources |
| `ACM-TSV-003` — CI/CD Gate And Release Promotion | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-AC-3.9, SP800-53-AU-10.3; PCI DSS v4.0.1: PCI-1.2.2, PCI-1.3.1; SAMM v2.1: SAMM-ACTIVITY-I_SD_3_B, SAMM-ACTIVITY-O_OM_1_A; MITRE ATLAS: AML.T0054, AML.M0001; + 7 more sources |
| `ACM-TSV-004` — Findings Workflow And Exception Governance | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-AC-4.9, SP800-53-AU-1; SAMM v2.1: SAMM-ACTIVITY-G_EG_3_A, SAMM-ACTIVITY-G_PC_1_A; CIS Controls v8.1.2: CIS-17, CIS-17.1; PCI DSS v4.0.1: PCI-2.1.2, PCI-6.5.2; + 10 more sources |
| `ACM-TSV-005` — Static Analysis Profile Management | M | addon/00-catalogo-requisitos.md (mechanism) | DSOMM: DSOMM-ACTIVITY-71699DAFB2A4466BA0B289F7DBB18506, DSOMM-ACTIVITY-E237176BBEC5447DA926E37D6DD60E4B; SP 800-53 r5: SP800-53-CM-2, SP800-53-CM-8; NIST AI RMF 1.0: NIST-AI-RMF-MEASURE-4.3, NIST-AI-RMF-MANAGE-4.3; SAMM v2.1: SAMM-ACTIVITY-D_TA_3_A, SAMM-ACTIVITY-O_EM_3_A; + 1 more sources |
| `ACO-TSV-001` — Risk-Proportional Security Testing Strategy | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-CP-8.5, SP800-53-PL-2; SAMM v2.1: SAMM-ACTIVITY-D_SR_2_A, SAMM-ACTIVITY-D_SR_3_A; CAPEC v3.9: CAPEC-420; CIS Controls v8.1.2: CIS-16.14; + 5 more sources |
| `ACO-TSV-002` — Static Analysis Signal Quality And Baseline Governance | CO | intro.md; aplicacao-lifecycle.md | DSOMM: DSOMM-ACTIVITY-E237176BBEC5447DA926E37D6DD60E4B, DSOMM-ACTIVITY-6C05C8378C9946E2828B7C903E27DBA4; SAMM v2.1: SAMM-ACTIVITY-G_PC_1_B, SAMM-ACTIVITY-G_PC_2_B; SP 800-53 r5: SP800-53-SA-11.1; SAFECode Agile: SCAGILE-OPS-4 |
| `ACO-TSV-003` — Security Finding Triage And Correction Closure | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AC-3.5, SP800-53-AU-6; PCI DSS v4.0.1: PCI-3.3.2, PCI-3.3.3; ASVS v5: ASVS-REQ-V14.2.4, ASVS-REQ-V14.2.7; CAPEC v3.9: CAPEC-54, CAPEC-144; + 9 more sources |
| `ACO-TSV-004` — Reproducible Security Test Evidence And Build Traceability | CO | intro.md; aplicacao-lifecycle.md | ASVS v5: ASVS-REQ-V1.4.1, ASVS-REQ-V1.4.3; SAMM v2.1: SAMM-ACTIVITY-I_SB_1_A, SAMM-ACTIVITY-I_SB_2_B; SLSA v1.0: SLSA-BUILD-L1, SLSA-BUILD-L2; DSOMM: DSOMM-ACTIVITY-A340F46B63604CB8847BA0D3483D09D3, DSOMM-ACTIVITY-7121B0C76ACE4D6B95D094535DBCCB57; + 10 more sources |
| `ACO-TSV-005` — Staged Dynamic Validation And Release Gate Discipline | CO | intro.md; aplicacao-lifecycle.md | MITRE ATLAS: AML.T0054, AML.T0073; SP 800-53 r5: SP800-53-CM-3, SP800-53-CM-3.5; CAPEC v3.9: CAPEC-443, CAPEC-671; SAMM v2.1: SAMM-ACTIVITY-I_SD_1_A, SAMM-ACTIVITY-I_SD_2_A; + 3 more sources |
| `ACO-TSV-006` — Specialized Empirical Testing Depth And Regression Assurance | CO | intro.md; aplicacao-lifecycle.md | NIST AI 100-2 e2025: NIST-AI-100-2-E2025-2.1, NIST-AI-100-2-E2025-2.1.3; MITRE ATLAS: AML.T0001, AML.T0016.000; DSOMM: DSOMM-ACTIVITY-F0E018143B884BD0A3A9F91DB001D20BADVANCED, DSOMM-ACTIVITY-5E0FF85BEC894EF096B15695FA0025DC; CAPEC v3.9: CAPEC-28, CAPEC-100; + 9 more sources |
| `ACO-TSV-007` — Security Testing And Empirical Assurance Integrity | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AU-6.2, SP800-53-CA-4; SAMM v2.1: SAMM-ACTIVITY-D_SA_2_A, SAMM-ACTIVITY-D_SA_3_B; DSOMM: DSOMM-ACTIVITY-12C90CC63D584D9B82FFD469D2A0C298, DSOMM-ACTIVITY-0B28367B75A04BAEA9263725C1BF9BB0; PCI SSLC v1.1: PCISSLC-1.3, PCISSLC-2.3; + 13 more sources |
| `ACP-TSV-001` — Risk-Based Security Test Planning | P | addon/00-catalogo-requisitos.md | SP 800-53 r5: SP800-53-CA-2, SP800-53-CA-7.4; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_A, SAMM-ACTIVITY-D_SR_1_A; CIS Controls v8.1.2: CIS-7, CIS-7.1; PCI DSS v4.0.1: PCI-REQ-6, PCI-5.2.3; + 7 more sources |
| `ACP-TSV-002` — Governed Static Analysis Execution | P | addon/00-catalogo-requisitos.md | DSOMM: DSOMM-ACTIVITY-517B095749814AC0B4C70D8D1934C474, DSOMM-ACTIVITY-E237176BBEC5447DA926E37D6DD60E4B; SAFECode Agile: SCAGILE-OPS-4, SCAGILE-OPS-9; CAPEC v3.9: CAPEC-190, CAPEC-191; SP 800-53 r5: SP800-53-SA-11.1, SP800-53-SA-11.8; + 2 more sources |
| `ACP-TSV-003` — Findings Triage, SLA And Retest Closure | P | addon/00-catalogo-requisitos.md | SP 800-53 r5: SP800-53-AU-1, SP800-53-CA-1; SAMM v2.1: SAMM-ACTIVITY-G_EG_3_A, SAMM-ACTIVITY-G_PC_1_A; CIS Controls v8.1.2: CIS-15.5; PCI SSLC v1.1: PCISSLC-5.1; + 2 more sources |
| `ACP-TSV-004` — Reproducible Test Evidence Management | P | addon/00-catalogo-requisitos.md | SP 800-53 r5: SP800-53-AU-2.1, SP800-53-AU-3; CIS Controls v8.1.2: CIS-3.1, CIS-8; PCI DSS v4.0.1: PCI-10.2.2, PCI-10.3.3; SLSA v1.0: SLSA-BUILD-L1, SLSA-BUILD-L2; + 6 more sources |
| `ACP-TSV-005` — Staged Dynamic Testing And Gate Enforcement | P | addon/00-catalogo-requisitos.md | SP 800-53 r5: SP800-53-AC-3.12, SP800-53-CM-3.5; CAPEC v3.9: CAPEC-121, CAPEC-443; MITRE ATLAS: AML.TA0001, AML.T0011.000; SAMM v2.1: SAMM-ACTIVITY-I_SD_2_A, SAMM-ACTIVITY-I_SD_3_B; + 7 more sources |
| `ACP-TSV-006` — Specialized Empirical Testing | P | addon/00-catalogo-requisitos.md | SSDF v1.1: SSDF-PRACTICE-PW.8, SSDF-PRACTICE-RV.1; CAPEC v3.9: CAPEC-28, CAPEC-215; NIST AI 100-2 e2025: NIST-AI-100-2-E2025-3.3.1, NIST-AI-100-2-E2025-3.6; MITRE ATLAS: AML.T0001, AML.M0008; + 5 more sources |
| `ACP-TSV-007` — Human Review Of Security Test Signals | P | chapter prose (final, release, review kws verified) | SP 800-53 r5: SP800-53-AC-4.9, SP800-53-AU-6.2; PCI DSS v4.0.1: PCI-1.2.2, PCI-5.4.1; SAMM v2.1: SAMM-ACTIVITY-D_SA_3_B, SAMM-ACTIVITY-I_SD_2_A; PCI SSLC v1.1: PCISSLC-2.6, PCISSLC-6.2; + 11 more sources |

---

## § Manual-only coverage (out-of-Core-scope; ES-grounded direct)

Manual sections that cover topics outside V1 AppSec Core ontology scope (maturity models, organizational policies, KPIs/metrics, glossaries) but with direct ES grounding to substrate v7 sources.

| Manual section | ES grounding (direct) |
|---|---|
| `achievable-maturity.md` | SAMM v2.1 ST maturity; DSOMM testing activities |
| `policies-relevantes.md` | Política de Testes de Segurança |
| `addon/00-catalogo-requisitos.md` | Catálogo de requisitos com componentes meta-testing (não-Core) |

---

## § Out-of-AppSec coverage (pure editorial)

Manual sections that are pure editorial content (worked examples, narratives, illustrative cases, vendor-specific tooling integration). Sem ES grounding.

| Manual section | Content type |
|---|---|
| `addon/11-pen-testing.md` | Pen-testing narrative e operacional |
| `addon/13-ia-nos-testes.md` | AI in testing — operational guidance (covered also in Iter 2 prose) |

---

## § Future-work register (P8 §10 candidates)

_(Sem entradas no future-work register para este capítulo.)_

---

## Generation provenance

- **Substrate version:** v7 (SUPPLIER sha256 `596783ed984d9c0e8c8ef6439a0eaee8fbaf2d863af37138cde8fad55d62be04`)
- **V1 entity index:** `ontology-v1.1-fair-baseline` @ `84fe8bf` em sbd-toe-ontology
- **Per-entity source map:** `data/p8_inputs/per_entity_source_map.json` @ ESI commit `aa3c13c`
- **Phase 2/3 gap analysis:** `phase2_3_per_entity_classification.json` @ ESI commit `b8cd401`
- **Slice → chapter map:** `slice_to_chapter_map.yaml` @ ESI commit `adbe4e0`
- **Generated by:** Manual Agent Iter 4 (rastreabilidade richness extension)
- **Format:** 4-section tabular (Core-mapped + Manual-only + Out-of-AppSec + Future-work) per dispatch vision 2026-05-11
- **Cycle:** Cycle B Iteration 4 (P8 pipeline primitive demonstration)
