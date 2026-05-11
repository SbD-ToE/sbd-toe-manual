# 25. Rastreabilidade — Threat Modeling

## Sumário

Este capítulo é a **âncora primária** das slices AppSec Core V1: `ACO-TMR` (Threat modeling, gestão de risco e rastreabilidade de mitigações).

Cobertura V1 entity-level: **25 entidades** primárias. Estrutura abaixo expõe four-way routing (per P8 pipeline primitive demonstration 2026-05-11):

- **§ Core-mapped coverage** — V1 entity → Manual section anchor → ES grounding
- **§ Manual-only coverage** — Manual sections out-of-Core-scope mas com ES grounding direct
- **§ Out-of-AppSec coverage** — Pure editorial sections (examples, narratives) sem ES grounding
- **§ Future-work register** — Content gaps registered as P8 §10 candidates

---

## § Core-mapped coverage

Tabela exposing V1 entity-level coverage with Manual section anchor + substrate v7 ES grounding. Three-way alignment per row: V1 (ontology) ↔ Manual (prose) ↔ ES (substrate).

### Slice `ACO-TMR` — Threat modeling, gestão de risco e rastreabilidade de mitigações

| V1 entity | Type | Manual section anchor | ES grounding |
|---|---|---|---|
| `ACM-TMR-001` — Threat Representation Models | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-SA-8.10, SP800-53-SA-8.16; CWE SDV v4.19.1: CWE-807; PCI SSLC v1.1: PCISSLC-3.2 |
| `ACM-TMR-002` — Structured Threat Analysis Frameworks | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-CP-12, SP800-53-IR-10; EU DORA: DORA-ART-6, DORA-ART-13; SAMM v2.1: SAMM-ACTIVITY-D_TA_1_A, SAMM-ACTIVITY-D_TA_2_A; SSDF v1.1: SSDF-TASK-PW.1.1, SSDF-TASK-RV.2.1; + 9 more sources |
| `ACM-TMR-003` — Threat Model Versioning Controls | M | addon/00-catalogo-requisitos.md (mechanism) | MITRE ATLAS: AML.TA0006, AML.T0010.003; SP 800-53 r5: SP800-53-CM-2.3, SP800-53-CP-2; CAPEC v3.9: CAPEC-166, CAPEC-186; SAMM v2.1: SAMM-ACTIVITY-D_SA_3_A, SAMM-ACTIVITY-D_TA_2_B; + 10 more sources |
| `ACM-TMR-004` — Explicit Threat Disposition Register | M | addon/00-catalogo-requisitos.md (mechanism) | HIPAA: HIPAA-164-308a6; SP 800-53 r5: SP800-53-AT-2.2; SAMM v2.1: SAMM-ACTIVITY-G_SM_1_A |
| `ACM-TMR-005` — Threat Mitigation Linkage Controls | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-AC-3.5, SP800-53-AC-3.6; CAPEC v3.9: CAPEC-37, CAPEC-38; MITRE ATLAS: AML.T0003, AML.T0008; PCI DSS v4.0.1: PCI-REQ-5, PCI-1.2.3; + 17 more sources |
| `ACM-TMR-006` — Reviewer Accountability And Consistency Gates | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-AC-4.9, SP800-53-AC-6.7; CIS Controls v8.1.2: CIS-8.1, CIS-8.11; SAMM v2.1: SAMM-ACTIVITY-G_EG_2_A, SAMM-ACTIVITY-G_EG_3_A; HIPAA: HIPAA-164-308a8; + 1 more sources |
| `ACM-TMR-007` — Requirements Registry And Derivation Traceability | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-PL-2, SP800-53-PM-3; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_B, SAMM-ACTIVITY-D_SA_2_A; PCI DSS v4.0.1: PCI-REQ-8, PCI-1.2.4; SSDF v1.1: SSDF-PRACTICE-PO.1, SSDF-PRACTICE-PO.3; + 10 more sources |
| `ACM-TMR-008` — Compliance Monitoring And Regulatory Change Feeds | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-AU-1, SP800-53-AU-2; SAMM v2.1: SAMM-ACTIVITY-G_PC_1_A, SAMM-ACTIVITY-G_PC_1_B; CIS Controls v8.1.2: CIS-4.4, CIS-7.5; DSOMM: DSOMM-ACTIVITY-67E1A9AA9FBF4EC5A2DE400F01960C51, DSOMM-ACTIVITY-8AE0B92C10E04602BA227524D6AED488; + 9 more sources |
| `ACO-TMR-001` — Threat Modeling Scope And Trigger Discipline | CO | intro.md; aplicacao-lifecycle.md | SAMM v2.1: SAMM-ACTIVITY-D_TA_1_B, SAMM-ACTIVITY-D_TA_2_B; DSOMM: DSOMM-ACTIVITY-47419324E263415B815DE7161B6B905E, DSOMM-ACTIVITY-48F97F31931C46EB9B3EE2FEC0CD0426; SP 800-53 r5: SP800-53-PM-9; SAFECode Agile: SCAGILE-EXP-3 |
| `ACO-TMR-002` — Architecture-Grounded Threat Representation | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-PL-8.1, SP800-53-PM-7; SAMM v2.1: SAMM-ACTIVITY-V_AA_1_A, SAMM-ACTIVITY-V_AA_1_B; MITRE ATLAS: AML.M0017 |
| `ACO-TMR-003` — Structured Threat Analysis Method Discipline | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-IR-4.13, SP800-53-PM-28; SSDF v1.1: SSDF-PRACTICE-RV.3, SSDF-TASK-RV.2.1; PCI DSS v4.0.1: PCI-6.2.4, PCI-11.4.1; CAPEC v3.9: CAPEC-425; + 5 more sources |
| `ACO-TMR-004` — Threat Disposition, Risk Acceptance And Ownership | CO | intro.md; aplicacao-lifecycle.md | CWE SDV v4.19.1: CWE-1230, CWE-212; SP 800-53 r5: SP800-53-AT-2.2, SP800-53-IR-4.6; CAPEC v3.9: CAPEC-414, CAPEC-418; MITRE ATLAS: AML.T0048, AML.T0051.001; + 1 more sources |
| `ACO-TMR-005` — Threat-To-Mitigation And Validation Traceability | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AC-2.13, SP800-53-AC-25; CAPEC v3.9: CAPEC-51, CAPEC-81; MITRE ATLAS: AML.TA0002, AML.TA0007; PCI DSS v4.0.1: PCI-1.4.3, PCI-5.2.1; + 22 more sources |
| `ACO-TMR-006` — Independent Review And Threat Model Lifecycle Governance | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AU-2.3, SP800-53-AU-10.3; NIST AI RMF 1.0: NIST-AI-RMF-GOVERN-1.5; SAMM v2.1: SAMM-ACTIVITY-G_PC_3_B |
| `ACO-TMR-007` — Threat Modeling And Risk Governance Integrity | CO | intro.md; aplicacao-lifecycle.md | SAMM v2.1: SAMM-ACTIVITY-D_TA_2_A, SAMM-ACTIVITY-G_EG_2_A; EU NIS2: NIS2-ART-20 |
| `ACO-TMR-008` — Security Requirements Lifecycle Management | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-3.3; PCI DSS v4.0.1: PCI-REQ-1, PCI-REQ-2; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_A, SAMM-ACTIVITY-D_SA_1_B; CIS Controls v8.1.2: CIS-2.2, CIS-4; + 13 more sources |
| `ACP-TMR-001` — Threat Model Creation And Triggered Refresh | P | addon/00-catalogo-requisitos.md | MITRE ATLAS: AML.TA0006, AML.T0018; SP 800-53 r5: SP800-53-CP-2, SP800-53-SA-3.3; SAMM v2.1: SAMM-ACTIVITY-D_TA_1_B, SAMM-ACTIVITY-D_TA_2_B; NIST AI 100-2 e2025: NIST-AI-100-2-E2025-2.3.4, NIST-AI-100-2-E2025-3.2.2; + 5 more sources |
| `ACP-TMR-002` — DFD And Trust-Boundary Grounding | P | addon/00-catalogo-requisitos.md | SP 800-53 r5: SP800-53-SA-8.10, SP800-53-SA-9.3; CIS Controls v8.1.2: CIS-4.9; CWE SDV v4.19.1: CWE-807; PCI SSLC v1.1: PCISSLC-3.2 |
| `ACP-TMR-003` — Structured Threat Analysis Method Selection | P | addon/00-catalogo-requisitos.md | SP 800-53 r5: SP800-53-AT-2.6, SP800-53-CP-6.1; SSDF v1.1: SSDF-PRACTICE-RV.2, SSDF-TASK-PW.1.1; SAMM v2.1: SAMM-ACTIVITY-D_TA_2_A, SAMM-ACTIVITY-I_DM_2_A; CAPEC v3.9: CAPEC-420, CAPEC-427; + 7 more sources |
| `ACP-TMR-004` — Threat Disposition And Accepted Risk Governance | P | addon/00-catalogo-requisitos.md | SAMM v2.1: SAMM-ACTIVITY-G_SM_1_A |
| `ACP-TMR-005` — Threat Traceability Into Requirements And Validation | P | addon/00-catalogo-requisitos.md | SP 800-53 r5: SP800-53-AC-4.19, SP800-53-AC-17.6; CAPEC v3.9: CAPEC-37, CAPEC-51; MITRE ATLAS: AML.TA0011, AML.T0002; ASVS v5: ASVS-REQ-V1.3.6, ASVS-REQ-V1.5.2; + 22 more sources |
| `ACP-TMR-006` — Independent Review And Threat Model Approval | P | chapter prose (go-live, model, models kws verified) | SP 800-53 r5: SP800-53-AC-13, SP800-53-AU-2.3; CIS Controls v8.1.2: CIS-17.8; SAMM v2.1: SAMM-ACTIVITY-G_EG_3_A |
| `ACP-TMR-007` — Threat Model Artifact Governance | P | chapter prose (access, artifacts, lifecycle kws verified) | NIST AI RMF 1.0: NIST-AI-RMF-GOVERN-2; SAMM v2.1: SAMM-ACTIVITY-G_SM_1_A |
| `ACP-TMR-008` — Security Requirements Identification And Derivation | P | chapter prose (models, policies, requirements kws verified) | SP 800-53 r5: SP800-53-AC-2, SP800-53-AC-3.5; PCI DSS v4.0.1: PCI-REQ-2, PCI-REQ-6; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_A, SAMM-ACTIVITY-D_SA_2_A; PCI SSLC v1.1: PCISSLC-1.2, PCISSLC-1.3; + 11 more sources |
| `ACP-TMR-009` — Requirements Communication And Compliance Monitoring | P | chapter prose (compliance, development, requirements kws verified) | SP 800-53 r5: SP800-53-AU-1, SP800-53-AU-6.1; SAMM v2.1: SAMM-ACTIVITY-G_EG_2_B, SAMM-ACTIVITY-G_PC_1_A; PCI DSS v4.0.1: PCI-1.1.2, PCI-2.1.2; PCI SSLC v1.1: PCISSLC-2.1, PCISSLC-5.1; + 3 more sources |

---

## § Manual-only coverage (out-of-Core-scope; ES-grounded direct)

Manual sections that cover topics outside V1 AppSec Core ontology scope (maturity models, organizational policies, KPIs/metrics, glossaries) but with direct ES grounding to substrate v7 sources.

| Manual section | ES grounding (direct) |
|---|---|
| `achievable-maturity.md` | SAMM v2.1 maturity dimensions (D_TA, V_AA); DSOMM activities maturity levels |
| `policies-relevantes.md` | Política de Threat Modeling (organizational policy framing) |
| `addon/11-kpis-metricas.md` | KPIs e métricas operacionais de threat modeling (não-Core) |

---

## § Out-of-AppSec coverage (pure editorial)

Manual sections that are pure editorial content (worked examples, narratives, illustrative cases, vendor-specific tooling integration). Sem ES grounding.

| Manual section | Content type |
|---|---|
| `exemplo-privacidade.md` | Worked example: LINDDUN privacy threat modeling case |
| `exemplos-aplicacao-stride.md` | Worked examples: STRIDE application per architecture pattern |
| `addon/02-riscos-processo-threat-modeling.md` | Process-level reflections / lessons learned |
| `addon/10-integracao-iriusrisk.md` | Tooling integration example (IriusRisk-specific) |

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
