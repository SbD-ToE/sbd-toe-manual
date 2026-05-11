# 25. Rastreabilidade — Threat Modeling

## Sumário

Este capítulo é a **âncora primária** das slices AppSec Core V1: `ACO-TMR` (Threat modeling, gestão de risco e rastreabilidade de mitigações).

Cobertura V1 entity-level: **25 entidades** primárias (8 ControlObjectives + 9 Practices + 8 Mechanisms). Cada entidade é listada abaixo com cobertura no Manual (prose anchor) e fontes externas substrate v7 que contribuem para a sua substantive coverage.

---

## Slice `ACO-TMR` — Threat modeling, gestão de risco e rastreabilidade de mitigações

### ControlObjectives (8)

#### `ACO-TMR-001` — Threat Modeling Scope And Trigger Discipline

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (7 grounded claims em 4 fontes):
  - OWASP SAMM v2.1 — 3 refs (`SAMM-ACTIVITY-D_TA_1_B`, `SAMM-ACTIVITY-D_TA_2_B`, `SAMM-ACTIVITY-D_TA_3_B`)
  - OWASP DSOMM — 2 refs (`DSOMM-ACTIVITY-47419324E263415B815DE7161B6B905E`, `DSOMM-ACTIVITY-48F97F31931C46EB9B3EE2FEC0CD0426`)
  - NIST SP 800-53 Rev. 5 — 1 refs (`SP800-53-PM-9`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-EXP-3`)

#### `ACO-TMR-002` — Architecture-Grounded Threat Representation

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (10 grounded claims em 3 fontes):
  - NIST SP 800-53 Rev. 5 — 5 refs (`SP800-53-PL-8.1`, `SP800-53-PM-7`, `SP800-53-SA-8.10` + 2 more)
  - OWASP SAMM v2.1 — 4 refs (`SAMM-ACTIVITY-V_AA_1_A`, `SAMM-ACTIVITY-V_AA_1_B`, `SAMM-ACTIVITY-V_AA_2_A` + 1 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.M0017`)

#### `ACO-TMR-003` — Structured Threat Analysis Method Discipline

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (26 grounded claims em 9 fontes):
  - NIST SP 800-53 Rev. 5 — 13 refs (`SP800-53-IR-4.13`, `SP800-53-PM-28`, `SP800-53-RA-1` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 4 refs (`SSDF-PRACTICE-RV.3`, `SSDF-TASK-RV.2.1`, `SSDF-TASK-RV.2.2` + 1 more)
  - PCI DSS v4.0.1 — 3 refs (`PCI-6.2.4`, `PCI-11.4.1`, `PCI-12.3.2`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-425`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-17.9`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 1 refs (`NIST-AI-100-2-E2025-2.1`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-297BE0018D9441EEAB29207020D423C0`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-D_TA_1_A`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-OPS-4`)

#### `ACO-TMR-004` — Threat Disposition, Risk Acceptance And Ownership

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (21 grounded claims em 5 fontes):
  - MITRE CWE — Software Development View (v4.19.1) — 8 refs (`CWE-1230`, `CWE-212`, `CWE-213` + 2 more)
  - NIST SP 800-53 Rev. 5 — 6 refs (`SP800-53-AT-2.2`, `SP800-53-IR-4.6`, `SP800-53-IR-4.7` + 2 more)
  - MITRE CAPEC v3.9 — 4 refs (`CAPEC-414`, `CAPEC-418`, `CAPEC-423` + 1 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0048`, `AML.T0051.001`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM09-2025`)

#### `ACO-TMR-005` — Threat-To-Mitigation And Validation Traceability

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (304 grounded claims em 26 fontes):
  - NIST SP 800-53 Rev. 5 — 75 refs (`SP800-53-AC-2.13`, `SP800-53-AC-25`, `SP800-53-AU-5.3` + 2 more)
  - MITRE CAPEC v3.9 — 56 refs (`CAPEC-51`, `CAPEC-81`, `CAPEC-93` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 48 refs (`AML.TA0002`, `AML.TA0007`, `AML.TA0008` + 2 more)
  - PCI DSS v4.0.1 — 17 refs (`PCI-1.4.3`, `PCI-5.2.1`, `PCI-5.3.4` + 2 more)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 16 refs (`NIST-AI-100-2-E2025-2.1`, `NIST-AI-100-2-E2025-2.1.2`, `NIST-AI-100-2-E2025-2.1.3` + 2 more)
  - OWASP ASVS v5.0.0 — 12 refs (`ASVS-REQ-V2.2.2`, `ASVS-REQ-V2.4.1`, `ASVS-REQ-V6.1.1` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 12 refs (`CWE-179`, `CWE-182`, `CWE-183` + 2 more)
  - NIST AI RMF 1.0 — 9 refs (`NIST-AI-RMF-GOVERN-1`, `NIST-AI-RMF-GOVERN-3.2`, `NIST-AI-RMF-GOVERN-6` + 2 more)
  - OWASP DSOMM — 9 refs (`DSOMM-ACTIVITY-FFE86CAF2FEC4630B5142DB83983984D`, `DSOMM-ACTIVITY-4CAE98C2416344EDBB883C67C569533A`, `DSOMM-ACTIVITY-F0E018143B884BD0A3A9F91DB001D20BADVANCED` + 2 more)
  - OWASP SAMM v2.1 — 7 refs (`SAMM-ACTIVITY-I_DM_1_A`, `SAMM-ACTIVITY-I_DM_3_A`, `SAMM-ACTIVITY-I_SB_3_A` + 2 more)
  - CIS Controls v8.1.2 — 6 refs (`CIS-3`, `CIS-7.7`, `CIS-10.5` + 2 more)
  - OWASP Machine Learning Top 10 — 6 refs (`ML01-2023`, `ML02-2023`, `ML03-2023` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 5 refs (`SSDF-PRACTICE-PS.2`, `SSDF-PRACTICE-RV.1`, `SSDF-PRACTICE-RV.2` + 2 more)
  - PCI Secure SLC v1.1 — 4 refs (`PCISSLC-3.2`, `PCISSLC-4.1`, `PCISSLC-4.2` + 1 more)
  - SLSA Specification v1.0 — Build Track — 4 refs (`SLSA-BUILD-L3`, `SLSA-PRINCIPLE-TRUST-PLATFORMS`, `SLSA-PRINCIPLE-TRUST-CODE` + 1 more)
  - OWASP LLM Top 10 (2025) — 3 refs (`LLM03-2025`, `LLM04-2025`, `LLM08-2025`)
  - OWASP MCP — Third-Party Servers v1.0 — 3 refs (`OWASP-MCP-3P-TOOL-INTERFERENCE`, `OWASP-MCP-3P-CLIENT-SECURITY-DISCOVERY`, `OWASP-MCP-3P-GOVERNANCE-REGISTRY`)
  - ENISA — Multilayer AI Cybersecurity Practices (2023) — 2 refs (`ENISA-AI-FAICP-LAYER-III`, `ENISA-AI-FAICP-SURVEY`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 2 refs (`MCP01-2025`, `MCP02-2025`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 2 refs (`SCAGILE-OPS-1`, `SCAGILE-EXP-2`)
  - EU Digital Operational Resilience Act (DORA) — 1 refs (`DORA-ART-10`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-23`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-308a6`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-DATA-VALIDATION`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A09-2021`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-MITIGATIONS`)

#### `ACO-TMR-006` — Independent Review And Threat Model Lifecycle Governance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (5 grounded claims em 3 fontes):
  - NIST SP 800-53 Rev. 5 — 3 refs (`SP800-53-AU-2.3`, `SP800-53-AU-10.3`, `SP800-53-RA-1`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-GOVERN-1.5`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-G_PC_3_B`)

#### `ACO-TMR-007` — Threat Modeling And Risk Governance Integrity

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (4 grounded claims em 2 fontes):
  - OWASP SAMM v2.1 — 3 refs (`SAMM-ACTIVITY-D_TA_2_A`, `SAMM-ACTIVITY-G_EG_2_A`, `SAMM-ACTIVITY-G_SM_1_A`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-20`)

#### `ACO-TMR-008` — Security Requirements Lifecycle Management

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (285 grounded claims em 17 fontes):
  - NIST SP 800-53 Rev. 5 — 85 refs (`SP800-53-AC-1`, `SP800-53-AC-3.3`, `SP800-53-AC-4.11` + 2 more)
  - PCI DSS v4.0.1 — 77 refs (`PCI-REQ-1`, `PCI-REQ-2`, `PCI-REQ-3` + 2 more)
  - OWASP SAMM v2.1 — 34 refs (`SAMM-ACTIVITY-D_SA_1_A`, `SAMM-ACTIVITY-D_SA_1_B`, `SAMM-ACTIVITY-D_SA_2_B` + 2 more)
  - CIS Controls v8.1.2 — 23 refs (`CIS-2.2`, `CIS-4`, `CIS-4.1` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 19 refs (`SSDF-PRACTICE-PO.1`, `SSDF-PRACTICE-PO.2`, `SSDF-PRACTICE-PO.3` + 2 more)
  - OWASP DSOMM — 13 refs (`DSOMM-ACTIVITY-12C90CC63D584D9B82FFD469D2A0C298`, `DSOMM-ACTIVITY-0B28367B75A04BAEA9263725C1BF9BB0`, `DSOMM-ACTIVITY-6217FE115ED74CF49DE4555BCFA6FE87` + 2 more)
  - PCI Secure SLC v1.1 — 11 refs (`PCISSLC-1.1`, `PCISSLC-1.2`, `PCISSLC-1.3` + 2 more)
  - OWASP ASVS v5.0.0 — 6 refs (`ASVS-REQ-V8.1.4`, `ASVS-REQ-V8.2.4`, `ASVS-REQ-V11.1.1` + 2 more)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 4 refs (`SCFPSSD-SECURITY-CONTROLS`, `SCFPSSD-LOGGING`, `SCFPSSD-LIFECYCLE-FEEDBACK` + 1 more)
  - EU NIS2 Directive — 2 refs (`NIS2-ART-21`, `NIS2-ART-22`)
  - HIPAA Security Rule — 2 refs (`HIPAA-164-308a1`, `HIPAA-164-308a2`)
  - OWASP Proactive Controls (2018) — 2 refs (`OPC-C1`, `OPC-C2`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 2 refs (`SCAGILE-EXP-8`, `SCAGILE-EXP-9`)
  - SAFECode — Software Integrity Controls (2010) — 2 refs (`SCSIC-SOURCING-CONTRACT`, `SCSIC-DEV-REPO`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-13`)
  - EU Digital Operational Resilience Act (DORA) — 1 refs (`DORA-ART-9`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-32`)


### Practices (9)

#### `ACP-TMR-001` — Threat Model Creation And Triggered Refresh

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (19 grounded claims em 9 fontes):
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 5 refs (`AML.TA0006`, `AML.T0018`, `AML.T0018.000` + 2 more)
  - NIST SP 800-53 Rev. 5 — 3 refs (`SP800-53-CP-2`, `SP800-53-SA-3.3`, `SP800-53-SI-4.5`)
  - OWASP SAMM v2.1 — 3 refs (`SAMM-ACTIVITY-D_TA_1_B`, `SAMM-ACTIVITY-D_TA_2_B`, `SAMM-ACTIVITY-V_AA_3_B`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 2 refs (`NIST-AI-100-2-E2025-2.3.4`, `NIST-AI-100-2-E2025-3.2.2`)
  - OWASP DSOMM — 2 refs (`DSOMM-ACTIVITY-47419324E263415B815DE7161B6B905E`, `DSOMM-ACTIVITY-F8E80F1825034E3EB3BC7F67BB28DEFE`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-166`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-7.1`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM04-2025`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-EXP-3`)

#### `ACP-TMR-002` — DFD And Trust-Boundary Grounding

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (6 grounded claims em 4 fontes):
  - NIST SP 800-53 Rev. 5 — 3 refs (`SP800-53-SA-8.10`, `SP800-53-SA-9.3`, `SP800-53-SA-13`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-4.9`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-807`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-3.2`)

#### `ACP-TMR-003` — Structured Threat Analysis Method Selection

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (48 grounded claims em 11 fontes):
  - NIST SP 800-53 Rev. 5 — 30 refs (`SP800-53-AT-2.6`, `SP800-53-CP-6.1`, `SP800-53-CP-7.1` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 4 refs (`SSDF-PRACTICE-RV.2`, `SSDF-TASK-PW.1.1`, `SSDF-TASK-RV.2.1` + 1 more)
  - OWASP SAMM v2.1 — 3 refs (`SAMM-ACTIVITY-D_TA_2_A`, `SAMM-ACTIVITY-I_DM_2_A`, `SAMM-ACTIVITY-O_IM_2_A`)
  - MITRE CAPEC v3.9 — 2 refs (`CAPEC-420`, `CAPEC-427`)
  - CIS Controls v8.1.2 — 2 refs (`CIS-7.6`, `CIS-17.9`)
  - NIST AI RMF 1.0 — 2 refs (`NIST-AI-RMF-GOVERN-1.3`, `NIST-AI-RMF-MANAGE-1.3`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-13`)
  - EU Digital Operational Resilience Act (DORA) — 1 refs (`DORA-ART-6`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 1 refs (`NIST-AI-100-2-E2025-2.1`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-12.3.2`)

#### `ACP-TMR-004` — Threat Disposition And Accepted Risk Governance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (1 grounded claims em 1 fontes):
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-G_SM_1_A`)

#### `ACP-TMR-005` — Threat Traceability Into Requirements And Validation

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (355 grounded claims em 26 fontes):
  - NIST SP 800-53 Rev. 5 — 105 refs (`SP800-53-AC-4.19`, `SP800-53-AC-17.6`, `SP800-53-AU-2` + 2 more)
  - MITRE CAPEC v3.9 — 56 refs (`CAPEC-37`, `CAPEC-51`, `CAPEC-54` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 31 refs (`AML.TA0011`, `AML.T0002`, `AML.T0019` + 2 more)
  - OWASP ASVS v5.0.0 — 26 refs (`ASVS-REQ-V1.3.6`, `ASVS-REQ-V1.5.2`, `ASVS-REQ-V2.2.2` + 2 more)
  - OWASP SAMM v2.1 — 18 refs (`SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-I_DM_1_A`, `SAMM-ACTIVITY-I_DM_2_A` + 2 more)
  - PCI DSS v4.0.1 — 16 refs (`PCI-5.2.1`, `PCI-5.3.1`, `PCI-5.3.4` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 14 refs (`CWE-1118`, `CWE-1230`, `CWE-209` + 2 more)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 14 refs (`NIST-AI-100-2-E2025-2.1`, `NIST-AI-100-2-E2025-2.1.2`, `NIST-AI-100-2-E2025-2.3` + 2 more)
  - OWASP DSOMM — 14 refs (`DSOMM-ACTIVITY-0DE465A655A74343AF79948BB5FF10BA`, `DSOMM-ACTIVITY-517B095749814AC0B4C70D8D1934C474`, `DSOMM-ACTIVITY-F0E018143B884BD0A3A9F91DB001D20BADVANCED` + 2 more)
  - CIS Controls v8.1.2 — 10 refs (`CIS-3`, `CIS-3.1`, `CIS-3.13` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 9 refs (`SSDF-PRACTICE-PS.2`, `SSDF-PRACTICE-PW.7`, `SSDF-PRACTICE-RV.1` + 2 more)
  - PCI Secure SLC v1.1 — 6 refs (`PCISSLC-2.6`, `PCISSLC-3.2`, `PCISSLC-4.1` + 2 more)
  - SLSA Specification v1.0 — Build Track — 6 refs (`SLSA-BUILD-L1`, `SLSA-BUILD-L3`, `SLSA-PRINCIPLE-TRUST-PLATFORMS` + 2 more)
  - OWASP Machine Learning Top 10 — 5 refs (`ML02-2023`, `ML05-2023`, `ML06-2023` + 2 more)
  - OWASP LLM Top 10 (2025) — 4 refs (`LLM03-2025`, `LLM04-2025`, `LLM08-2025` + 1 more)
  - NIST AI RMF 1.0 — 3 refs (`NIST-AI-RMF-MAP-2.3`, `NIST-AI-RMF-MAP-4`, `NIST-AI-RMF-MEASURE-2.6`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 3 refs (`MCP01-2025`, `MCP04-2025`, `MCP08-2025`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 3 refs (`SCAGILE-OPS-1`, `SCAGILE-OPS-7`, `SCAGILE-EXP-2`)
  - OWASP MCP — Secure Server Development v1.0 — 2 refs (`OWASP-MCP-TOOL-DESIGN`, `OWASP-MCP-DATA-VALIDATION`)
  - OWASP MCP — Third-Party Servers v1.0 — 2 refs (`OWASP-MCP-3P-CLIENT-SECURITY-DISCOVERY`, `OWASP-MCP-3P-GOVERNANCE-REGISTRY`)
  - OWASP Top 10 (2021) — 2 refs (`TOP10-A08-2021`, `TOP10-A09-2021`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 2 refs (`SCFPSSD-DATA-HANDLING`, `SCFPSSD-THIRD-PARTY`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-13`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-32`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-312c1`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEV-BUILD`)

#### `ACP-TMR-006` — Independent Review And Threat Model Approval

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 5 keywords × 381 ocorrências; principais: go-live, model, models, review, threat)
- **Substrate v7 contributing sources** (4 grounded claims em 3 fontes):
  - NIST SP 800-53 Rev. 5 — 2 refs (`SP800-53-AC-13`, `SP800-53-AU-2.3`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-17.8`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-G_EG_3_A`)

#### `ACP-TMR-007` — Threat Model Artifact Governance

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 7 keywords × 391 ocorrências; principais: access, artifacts, lifecycle, model, review)
- **Substrate v7 contributing sources** (2 grounded claims em 2 fontes):
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-GOVERN-2`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-G_SM_1_A`)

#### `ACP-TMR-008` — Security Requirements Identification And Derivation

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 5 keywords × 305 ocorrências; principais: models, policies, requirements, risk, threat)
- **Substrate v7 contributing sources** (137 grounded claims em 15 fontes):
  - NIST SP 800-53 Rev. 5 — 62 refs (`SP800-53-AC-2`, `SP800-53-AC-3.5`, `SP800-53-AC-4.1` + 2 more)
  - PCI DSS v4.0.1 — 28 refs (`PCI-REQ-2`, `PCI-REQ-6`, `PCI-REQ-8` + 2 more)
  - OWASP SAMM v2.1 — 14 refs (`SAMM-ACTIVITY-D_SA_1_A`, `SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-D_SA_2_B` + 2 more)
  - PCI Secure SLC v1.1 — 7 refs (`PCISSLC-1.2`, `PCISSLC-1.3`, `PCISSLC-2.2` + 2 more)
  - CIS Controls v8.1.2 — 6 refs (`CIS-4.1`, `CIS-4.2`, `CIS-12.2` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 5 refs (`SSDF-PRACTICE-PO.1`, `SSDF-PRACTICE-PW.1`, `SSDF-TASK-PO.1.1` + 2 more)
  - OWASP DSOMM — 4 refs (`DSOMM-ACTIVITY-0B28367B75A04BAEA9263725C1BF9BB0`, `DSOMM-ACTIVITY-9768F154357A4C06AF6FD66570677C9B`, `DSOMM-ACTIVITY-31833D5635AF4EF39300F23D27646CE7` + 1 more)
  - OWASP ASVS v5.0.0 — 2 refs (`ASVS-REQ-V3.1.1`, `ASVS-REQ-V14.1.2`)
  - HIPAA Security Rule — 2 refs (`HIPAA-164-308a2`, `HIPAA-164-308a6`)
  - OWASP Proactive Controls (2018) — 2 refs (`OPC-C1`, `OPC-C2`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-671`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-13`)
  - EU Digital Operational Resilience Act (DORA) — 1 refs (`DORA-ART-9`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-32`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MAP-1.6`)

#### `ACP-TMR-009` — Requirements Communication And Compliance Monitoring

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 3 keywords × 13 ocorrências; principais: compliance, development, requirements)
- **Substrate v7 contributing sources** (55 grounded claims em 7 fontes):
  - NIST SP 800-53 Rev. 5 — 33 refs (`SP800-53-AU-1`, `SP800-53-AU-6.1`, `SP800-53-CA-1` + 2 more)
  - OWASP SAMM v2.1 — 10 refs (`SAMM-ACTIVITY-G_EG_2_B`, `SAMM-ACTIVITY-G_PC_1_A`, `SAMM-ACTIVITY-G_PC_1_B` + 2 more)
  - PCI DSS v4.0.1 — 4 refs (`PCI-1.1.2`, `PCI-2.1.2`, `PCI-4.1.2` + 1 more)
  - PCI Secure SLC v1.1 — 4 refs (`PCISSLC-2.1`, `PCISSLC-5.1`, `PCISSLC-9.1` + 1 more)
  - CIS Controls v8.1.2 — 2 refs (`CIS-15`, `CIS-15.6`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-MITIGATIONS`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PO.1.3`)


### Mechanisms (8)

#### `ACM-TMR-001` — Threat Representation Models

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (4 grounded claims em 3 fontes):
  - NIST SP 800-53 Rev. 5 — 2 refs (`SP800-53-SA-8.10`, `SP800-53-SA-8.16`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-807`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-3.2`)

#### `ACM-TMR-002` — Structured Threat Analysis Frameworks

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (52 grounded claims em 13 fontes):
  - NIST SP 800-53 Rev. 5 — 28 refs (`SP800-53-CP-12`, `SP800-53-IR-10`, `SP800-53-PE-23` + 2 more)
  - EU Digital Operational Resilience Act (DORA) — 4 refs (`DORA-ART-6`, `DORA-ART-13`, `DORA-ART-15` + 1 more)
  - OWASP SAMM v2.1 — 4 refs (`SAMM-ACTIVITY-D_TA_1_A`, `SAMM-ACTIVITY-D_TA_2_A`, `SAMM-ACTIVITY-G_EG_1_B` + 1 more)
  - NIST SSDF (SP 800-218 v1.1) — 3 refs (`SSDF-TASK-PW.1.1`, `SSDF-TASK-RV.2.1`, `SSDF-TASK-RV.2.2`)
  - EU NIS2 Directive — 2 refs (`NIS2-ART-20`, `NIS2-ART-21`)
  - NIST AI RMF 1.0 — 2 refs (`NIST-AI-RMF-GOVERN-1.3`, `NIST-AI-RMF-MEASURE-4.3`)
  - PCI DSS v4.0.1 — 2 refs (`PCI-12.3.2`, `PCI-12.10.6`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 2 refs (`SCFPSSD-THREAT-MODELING`, `SCFPSSD-FINDINGS`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-17.9`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-13`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-6217FE115ED74CF49DE4555BCFA6FE87`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM09-2025`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C2`)

#### `ACM-TMR-003` — Threat Model Versioning Controls

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (39 grounded claims em 14 fontes):
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 8 refs (`AML.TA0006`, `AML.T0010.003`, `AML.T0018` + 2 more)
  - NIST SP 800-53 Rev. 5 — 7 refs (`SP800-53-CM-2.3`, `SP800-53-CP-2`, `SP800-53-CP-10.4` + 2 more)
  - MITRE CAPEC v3.9 — 4 refs (`CAPEC-166`, `CAPEC-186`, `CAPEC-447` + 1 more)
  - OWASP SAMM v2.1 — 4 refs (`SAMM-ACTIVITY-D_SA_3_A`, `SAMM-ACTIVITY-D_TA_2_B`, `SAMM-ACTIVITY-I_SD_3_B` + 1 more)
  - OWASP DSOMM — 3 refs (`DSOMM-ACTIVITY-066084C6113546359CC59E75C7C5459F`, `DSOMM-ACTIVITY-5C61FD6B81064C68AC28A8A42F1C67DC`, `DSOMM-ACTIVITY-F8E80F1825034E3EB3BC7F67BB28DEFE`)
  - PCI DSS v4.0.1 — 3 refs (`PCI-5.3.1`, `PCI-6.5.1`, `PCI-7.2.1`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 2 refs (`SCFPSSD-SECURITY-CONTROLS`, `SCFPSSD-COMPILER`)
  - NIST SSDF (SP 800-218 v1.1) — 2 refs (`SSDF-PRACTICE-PS.3`, `SSDF-TASK-PS.3.1`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-7.1`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 1 refs (`NIST-AI-100-2-E2025-2.3.4`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MANAGE-3`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML03-2023`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A06-2021`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-5.2`)

#### `ACM-TMR-004` — Explicit Threat Disposition Register

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (3 grounded claims em 3 fontes):
  - HIPAA Security Rule — 1 refs (`HIPAA-164-308a6`)
  - NIST SP 800-53 Rev. 5 — 1 refs (`SP800-53-AT-2.2`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-G_SM_1_A`)

#### `ACM-TMR-005` — Threat Mitigation Linkage Controls

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (289 grounded claims em 21 fontes):
  - NIST SP 800-53 Rev. 5 — 100 refs (`SP800-53-AC-3.5`, `SP800-53-AC-3.6`, `SP800-53-AC-4.12` + 2 more)
  - MITRE CAPEC v3.9 — 61 refs (`CAPEC-37`, `CAPEC-38`, `CAPEC-51` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 36 refs (`AML.T0003`, `AML.T0008`, `AML.T0019` + 2 more)
  - PCI DSS v4.0.1 — 17 refs (`PCI-REQ-5`, `PCI-1.2.3`, `PCI-1.4.2` + 2 more)
  - CIS Controls v8.1.2 — 13 refs (`CIS-3`, `CIS-3.1`, `CIS-3.2` + 2 more)
  - OWASP ASVS v5.0.0 — 11 refs (`ASVS-REQ-V1.3.6`, `ASVS-REQ-V8.4.2`, `ASVS-REQ-V14.2.3` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 11 refs (`CWE-1230`, `CWE-209`, `CWE-215` + 2 more)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 11 refs (`NIST-AI-100-2-E2025-2.3.1`, `NIST-AI-100-2-E2025-3.1.2`, `NIST-AI-100-2-E2025-3.2.3` + 2 more)
  - OWASP SAMM v2.1 — 6 refs (`SAMM-ACTIVITY-I_DM_1_A`, `SAMM-ACTIVITY-I_SB_3_A`, `SAMM-ACTIVITY-I_SB_3_B` + 2 more)
  - OWASP DSOMM — 5 refs (`DSOMM-ACTIVITY-6DF508EF86FC4C22BD9F646C3127CE7D`, `DSOMM-ACTIVITY-F0E018143B884BD0A3A9F91DB001D20BADVANCED`, `DSOMM-ACTIVITY-B217C8BB5D614B41A6751083993F83B1` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 4 refs (`SSDF-PRACTICE-PS.1`, `SSDF-PRACTICE-RV.1`, `SSDF-TASK-RV.1.2` + 1 more)
  - OWASP LLM Top 10 (2025) — 3 refs (`LLM08-2025`, `LLM09-2025`, `LLM10-2025`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 2 refs (`MCP01-2025`, `MCP08-2025`)
  - PCI Secure SLC v1.1 — 2 refs (`PCISSLC-3.2`, `PCISSLC-8.2`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MAP-4`)
  - OWASP MCP — Third-Party Servers v1.0 — 1 refs (`OWASP-MCP-3P-TOOL-INTERFERENCE`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML09-2023`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-EXP-9`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-DATA-HANDLING`)
  - SLSA Specification v1.0 — Build Track — 1 refs (`SLSA-PRINCIPLE-TRUST-CODE`)

#### `ACM-TMR-006` — Reviewer Accountability And Consistency Gates

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (20 grounded claims em 5 fontes):
  - NIST SP 800-53 Rev. 5 — 13 refs (`SP800-53-AC-4.9`, `SP800-53-AC-6.7`, `SP800-53-AC-13` + 2 more)
  - CIS Controls v8.1.2 — 3 refs (`CIS-8.1`, `CIS-8.11`, `CIS-17.8`)
  - OWASP SAMM v2.1 — 2 refs (`SAMM-ACTIVITY-G_EG_2_A`, `SAMM-ACTIVITY-G_EG_3_A`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-308a8`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM09-2025`)

#### `ACM-TMR-007` — Requirements Registry And Derivation Traceability

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (90 grounded claims em 14 fontes):
  - NIST SP 800-53 Rev. 5 — 26 refs (`SP800-53-PL-2`, `SP800-53-PM-3`, `SP800-53-PS-3.4` + 2 more)
  - OWASP SAMM v2.1 — 16 refs (`SAMM-ACTIVITY-D_SA_1_B`, `SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-D_SA_2_B` + 2 more)
  - PCI DSS v4.0.1 — 15 refs (`PCI-REQ-8`, `PCI-1.2.4`, `PCI-2.2.6` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 10 refs (`SSDF-PRACTICE-PO.1`, `SSDF-PRACTICE-PO.3`, `SSDF-PRACTICE-PO.4` + 2 more)
  - PCI Secure SLC v1.1 — 5 refs (`PCISSLC-1.3`, `PCISSLC-2.2`, `PCISSLC-2.4` + 2 more)
  - OWASP ASVS v5.0.0 — 4 refs (`ASVS-REQ-V8.1.4`, `ASVS-REQ-V14.1.2`, `ASVS-REQ-V15.1.2` + 1 more)
  - OWASP DSOMM — 4 refs (`DSOMM-ACTIVITY-B597928E54D648A5A8068003DCD56AAB`, `DSOMM-ACTIVITY-CF81922530CB47028E3260225EEDC33D`, `DSOMM-ACTIVITY-2B7CC923BDAF43E38FB4A995B7783969` + 1 more)
  - MITRE CAPEC v3.9 — 2 refs (`CAPEC-80`, `CAPEC-671`)
  - NIST AI RMF 1.0 — 2 refs (`NIST-AI-RMF-MAP-1.6`, `NIST-AI-RMF-MEASURE-2.3`)
  - SLSA Specification v1.0 — Build Track — 2 refs (`SLSA-BUILD-L1`, `SLSA-BUILD-PLATFORM-PROVENANCE-GENERATION`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-13`)
  - EU Digital Operational Resilience Act (DORA) — 1 refs (`DORA-ART-27`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C1`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEV-BUILD`)

#### `ACM-TMR-008` — Compliance Monitoring And Regulatory Change Feeds

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (99 grounded claims em 13 fontes):
  - NIST SP 800-53 Rev. 5 — 54 refs (`SP800-53-AU-1`, `SP800-53-AU-2`, `SP800-53-AU-5.2` + 2 more)
  - OWASP SAMM v2.1 — 15 refs (`SAMM-ACTIVITY-G_PC_1_A`, `SAMM-ACTIVITY-G_PC_1_B`, `SAMM-ACTIVITY-G_PC_2_B` + 2 more)
  - CIS Controls v8.1.2 — 7 refs (`CIS-4.4`, `CIS-7.5`, `CIS-13.1` + 2 more)
  - OWASP DSOMM — 6 refs (`DSOMM-ACTIVITY-67E1A9AA9FBF4EC5A2DE400F01960C51`, `DSOMM-ACTIVITY-8AE0B92C10E04602BA227524D6AED488`, `DSOMM-ACTIVITY-E9A6D403A467445EB98A74F0C29DA0B1` + 2 more)
  - PCI DSS v4.0.1 — 5 refs (`PCI-REQ-11`, `PCI-10.2.1`, `PCI-10.3.4` + 2 more)
  - PCI Secure SLC v1.1 — 4 refs (`PCISSLC-2.1`, `PCISSLC-5.1`, `PCISSLC-9.2` + 1 more)
  - EU Cyber Resilience Act (CRA) — 2 refs (`CRA-ART-13`, `CRA-ART-14`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-23`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-32`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-316b1`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM10-2025`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C9`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-MITIGATIONS`)


---

## Generation provenance

- **Substrate version:** v7 (SUPPLIER sha256 `596783ed984d9c0e8c8ef6439a0eaee8fbaf2d863af37138cde8fad55d62be04`)
- **V1 entity index:** `ontology-v1.1-fair-baseline` @ `84fe8bf` em sbd-toe-ontology
- **Per-entity source map:** `data/p8_inputs/per_entity_source_map.json` @ ESI commit `aa3c13c`
- **Phase 2/3 gap analysis:** `data/p8_gap_analysis/phase2_3/phase2_3_per_entity_classification.json` @ ESI commit `b8cd401`
- **Slice → chapter map:** `data/p7_olir_audit/p7_v2_corrected/canon_rewrite/slice_to_chapter_map.yaml`
- **Generated by:** Manual Agent Iter 3 Path D (recreate; Bundle G2 deprecated)
- **Format:** entity-first (per V1 entity → Manual prose anchor + substrate v7 contributing sources)
- **Cycle:** Cycle B Iteration 3 (Stage 5 Editorial Feedback applied)
