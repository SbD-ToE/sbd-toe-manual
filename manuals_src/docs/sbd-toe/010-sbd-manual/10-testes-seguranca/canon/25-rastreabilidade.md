# 25. Rastreabilidade — Testes de Segurança

## Sumário

Este capítulo é a **âncora primária** das slices AppSec Core V1: `ACO-TSV` (Testes de segurança e validação empírica).

Cobertura V1 entity-level: **19 entidades** primárias (7 ControlObjectives + 7 Practices + 5 Mechanisms). Cada entidade é listada abaixo com cobertura no Manual (prose anchor) e fontes externas substrate v7 que contribuem para a sua substantive coverage.

---

## Slice `ACO-TSV` — Testes de segurança e validação empírica

### ControlObjectives (7)

#### `ACO-TSV-001` — Risk-Proportional Security Testing Strategy

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (29 grounded claims em 9 fontes):
  - NIST SP 800-53 Rev. 5 — 15 refs (`SP800-53-CP-8.5`, `SP800-53-PL-2`, `SP800-53-PM-4` + 2 more)
  - OWASP SAMM v2.1 — 7 refs (`SAMM-ACTIVITY-D_SR_2_A`, `SAMM-ACTIVITY-D_SR_3_A`, `SAMM-ACTIVITY-D_TA_1_A` + 2 more)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-420`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-16.14`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-47419324E263415B815DE7161B6B905E`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-12.3.2`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-EXP-5`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PW.1.1`)

#### `ACO-TSV-002` — Static Analysis Signal Quality And Baseline Governance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (8 grounded claims em 4 fontes):
  - OWASP DSOMM — 4 refs (`DSOMM-ACTIVITY-E237176BBEC5447DA926E37D6DD60E4B`, `DSOMM-ACTIVITY-6C05C8378C9946E2828B7C903E27DBA4`, `DSOMM-ACTIVITY-EE68331F9B1D4F61844BB2EA04753A84` + 1 more)
  - OWASP SAMM v2.1 — 2 refs (`SAMM-ACTIVITY-G_PC_1_B`, `SAMM-ACTIVITY-G_PC_2_B`)
  - NIST SP 800-53 Rev. 5 — 1 refs (`SP800-53-SA-11.1`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-OPS-4`)

#### `ACO-TSV-003` — Security Finding Triage And Correction Closure

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (65 grounded claims em 13 fontes):
  - NIST SP 800-53 Rev. 5 — 25 refs (`SP800-53-AC-3.5`, `SP800-53-AU-6`, `SP800-53-CP-2` + 2 more)
  - PCI DSS v4.0.1 — 21 refs (`PCI-3.3.2`, `PCI-3.3.3`, `PCI-3.6.1` + 2 more)
  - OWASP ASVS v5.0.0 — 5 refs (`ASVS-REQ-V14.2.4`, `ASVS-REQ-V14.2.7`, `ASVS-REQ-V15.4.2` + 2 more)
  - MITRE CAPEC v3.9 — 2 refs (`CAPEC-54`, `CAPEC-144`)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-358`, `CWE-414`)
  - OWASP SAMM v2.1 — 2 refs (`SAMM-ACTIVITY-I_DM_1_A`, `SAMM-ACTIVITY-O_IM_2_A`)
  - PCI Secure SLC v1.1 — 2 refs (`PCISSLC-3.4`, `PCISSLC-4.2`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-17.9`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-5`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-308a6`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-C1ACC8AF312E4503A817A26220C993A0`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A09-2021`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-VULN-RESPONSE`)

#### `ACO-TSV-004` — Reproducible Security Test Evidence And Build Traceability

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (47 grounded claims em 14 fontes):
  - OWASP ASVS v5.0.0 — 9 refs (`ASVS-REQ-V1.4.1`, `ASVS-REQ-V1.4.3`, `ASVS-REQ-V15.1.1` + 2 more)
  - OWASP SAMM v2.1 — 7 refs (`SAMM-ACTIVITY-I_SB_1_A`, `SAMM-ACTIVITY-I_SB_2_B`, `SAMM-ACTIVITY-I_SB_3_A` + 2 more)
  - SLSA Specification v1.0 — Build Track — 6 refs (`SLSA-BUILD-L1`, `SLSA-BUILD-L2`, `SLSA-BUILD-L3` + 2 more)
  - OWASP DSOMM — 5 refs (`DSOMM-ACTIVITY-A340F46B63604CB8847BA0D3483D09D3`, `DSOMM-ACTIVITY-7121B0C76ACE4D6B95D094535DBCCB57`, `DSOMM-ACTIVITY-517B095749814AC0B4C70D8D1934C474` + 2 more)
  - PCI DSS v4.0.1 — 5 refs (`PCI-5.2.1`, `PCI-5.3.4`, `PCI-6.2.3` + 2 more)
  - NIST SP 800-53 Rev. 5 — 4 refs (`SP800-53-AU-12.1`, `SP800-53-PM-6`, `SP800-53-SA-10.4` + 1 more)
  - MITRE CAPEC v3.9 — 2 refs (`CAPEC-190`, `CAPEC-690`)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-215`, `CWE-494`)
  - NIST SSDF (SP 800-218 v1.1) — 2 refs (`SSDF-TASK-PW.6.1`, `SSDF-TASK-PW.8.1`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-16.11`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C9`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-OPS-9`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-LOGGING`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEV-BUILD`)

#### `ACO-TSV-005` — Staged Dynamic Validation And Release Gate Discipline

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (22 grounded claims em 7 fontes):
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 6 refs (`AML.T0054`, `AML.T0073`, `AML.T0079` + 2 more)
  - NIST SP 800-53 Rev. 5 — 5 refs (`SP800-53-CM-3`, `SP800-53-CM-3.5`, `SP800-53-CM-8.3` + 2 more)
  - MITRE CAPEC v3.9 — 4 refs (`CAPEC-443`, `CAPEC-671`, `CAPEC-672` + 1 more)
  - OWASP SAMM v2.1 — 3 refs (`SAMM-ACTIVITY-I_SD_1_A`, `SAMM-ACTIVITY-I_SD_2_A`, `SAMM-ACTIVITY-I_SD_3_B`)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-179`, `CWE-408`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 1 refs (`NIST-AI-100-2-E2025-3.4.4`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-6.5.5`)

#### `ACO-TSV-006` — Specialized Empirical Testing Depth And Regression Assurance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (67 grounded claims em 13 fontes):
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 25 refs (`NIST-AI-100-2-E2025-2.1`, `NIST-AI-100-2-E2025-2.1.3`, `NIST-AI-100-2-E2025-2.1.4` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 17 refs (`AML.T0001`, `AML.T0016.000`, `AML.T0019` + 2 more)
  - OWASP DSOMM — 6 refs (`DSOMM-ACTIVITY-F0E018143B884BD0A3A9F91DB001D20BADVANCED`, `DSOMM-ACTIVITY-5E0FF85BEC894EF096B15695FA0025DC`, `DSOMM-ACTIVITY-F2F0F274C1A0450192FE7FC4452BC8AD` + 2 more)
  - MITRE CAPEC v3.9 — 3 refs (`CAPEC-28`, `CAPEC-100`, `CAPEC-670`)
  - OWASP LLM Top 10 (2025) — 3 refs (`LLM03-2025`, `LLM04-2025`, `LLM09-2025`)
  - OWASP Machine Learning Top 10 — 3 refs (`ML01-2023`, `ML03-2023`, `ML10-2023`)
  - NIST SSDF (SP 800-218 v1.1) — 3 refs (`SSDF-PRACTICE-RV.3`, `SSDF-TASK-RV.3.1`, `SSDF-TASK-RV.3.3`)
  - NIST SP 800-53 Rev. 5 — 2 refs (`SP800-53-IR-4.13`, `SP800-53-RA-5`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-RISK-LANDSCAPE`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-V_RT_1_B`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-11.4.4`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-EXP-3`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-THREAT-MODELING`)

#### `ACO-TSV-007` — Security Testing And Empirical Assurance Integrity

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (62 grounded claims em 17 fontes):
  - NIST SP 800-53 Rev. 5 — 17 refs (`SP800-53-AU-6.2`, `SP800-53-CA-4`, `SP800-53-CP-9.1` + 2 more)
  - OWASP SAMM v2.1 — 12 refs (`SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-D_SA_3_B`, `SAMM-ACTIVITY-G_EG_1_B` + 2 more)
  - OWASP DSOMM — 8 refs (`DSOMM-ACTIVITY-12C90CC63D584D9B82FFD469D2A0C298`, `DSOMM-ACTIVITY-0B28367B75A04BAEA9263725C1BF9BB0`, `DSOMM-ACTIVITY-F88D1B173D7D4C3D8139AD44FC4942D4` + 2 more)
  - PCI Secure SLC v1.1 — 5 refs (`PCISSLC-1.3`, `PCISSLC-2.3`, `PCISSLC-2.4` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 4 refs (`SSDF-PRACTICE-PO.5`, `SSDF-PRACTICE-PW.2`, `SSDF-PRACTICE-PW.7` + 1 more)
  - MITRE CAPEC v3.9 — 3 refs (`CAPEC-184`, `CAPEC-330`, `CAPEC-440`)
  - CIS Controls v8.1.2 — 2 refs (`CIS-14.1`, `CIS-18.4`)
  - PCI DSS v4.0.1 — 2 refs (`PCI-1.2.6`, `PCI-12.6.1`)
  - OWASP ASVS v5.0.0 — 1 refs (`ASVS-REQ-V11.6.2`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-308a5`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.M0008`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MEASURE-2.3`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM04-2025`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-GOVERNANCE`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-OPS-15`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-PLANNING`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEVELOPMENT`)


### Practices (7)

#### `ACP-TSV-001` — Risk-Based Security Test Planning

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (78 grounded claims em 11 fontes):
  - NIST SP 800-53 Rev. 5 — 32 refs (`SP800-53-CA-2`, `SP800-53-CA-7.4`, `SP800-53-CA-8` + 2 more)
  - OWASP SAMM v2.1 — 15 refs (`SAMM-ACTIVITY-D_SA_1_A`, `SAMM-ACTIVITY-D_SR_1_A`, `SAMM-ACTIVITY-D_SR_1_B` + 2 more)
  - CIS Controls v8.1.2 — 8 refs (`CIS-7`, `CIS-7.1`, `CIS-7.5` + 2 more)
  - PCI DSS v4.0.1 — 6 refs (`PCI-REQ-6`, `PCI-5.2.3`, `PCI-5.3.1` + 2 more)
  - OWASP DSOMM — 5 refs (`DSOMM-ACTIVITY-DD5ED7C1BDBF400FB75F6D3953A1A04E`, `DSOMM-ACTIVITY-6217FE115ED74CF49DE4555BCFA6FE87`, `DSOMM-ACTIVITY-72737130472C498480F89AB2F1C2ED5D` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 5 refs (`SSDF-PRACTICE-PO.1`, `SSDF-PRACTICE-PW.1`, `SSDF-TASK-PW.1.1` + 2 more)
  - EU NIS2 Directive — 3 refs (`NIS2-ART-20`, `NIS2-ART-21`, `NIS2-ART-22`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-GOVERN-1.3`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C1`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-3.3`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-PLANNING`)

#### `ACP-TSV-002` — Governed Static Analysis Execution

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (16 grounded claims em 6 fontes):
  - OWASP DSOMM — 7 refs (`DSOMM-ACTIVITY-517B095749814AC0B4C70D8D1934C474`, `DSOMM-ACTIVITY-E237176BBEC5447DA926E37D6DD60E4B`, `DSOMM-ACTIVITY-6C05C8378C9946E2828B7C903E27DBA4` + 2 more)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 3 refs (`SCAGILE-OPS-4`, `SCAGILE-OPS-9`, `SCAGILE-EXP-10`)
  - MITRE CAPEC v3.9 — 2 refs (`CAPEC-190`, `CAPEC-191`)
  - NIST SP 800-53 Rev. 5 — 2 refs (`SP800-53-SA-11.1`, `SP800-53-SA-11.8`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-16.12`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-V_AA_2_A`)

#### `ACP-TSV-003` — Findings Triage, SLA And Retest Closure

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (22 grounded claims em 6 fontes):
  - NIST SP 800-53 Rev. 5 — 11 refs (`SP800-53-AU-1`, `SP800-53-CA-1`, `SP800-53-CA-7.2` + 2 more)
  - OWASP SAMM v2.1 — 7 refs (`SAMM-ACTIVITY-G_EG_3_A`, `SAMM-ACTIVITY-G_PC_1_A`, `SAMM-ACTIVITY-G_PC_1_B` + 2 more)
  - CIS Controls v8.1.2 — 1 refs (`CIS-15.5`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-5.1`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-MITIGATIONS`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PO.4.2`)

#### `ACP-TSV-004` — Reproducible Test Evidence Management

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (41 grounded claims em 10 fontes):
  - NIST SP 800-53 Rev. 5 — 22 refs (`SP800-53-AU-2.1`, `SP800-53-AU-3`, `SP800-53-AU-3.2` + 2 more)
  - CIS Controls v8.1.2 — 6 refs (`CIS-3.1`, `CIS-8`, `CIS-8.1` + 2 more)
  - PCI DSS v4.0.1 — 3 refs (`PCI-10.2.2`, `PCI-10.3.3`, `PCI-10.5.1`)
  - SLSA Specification v1.0 — Build Track — 3 refs (`SLSA-BUILD-L1`, `SLSA-BUILD-L2`, `SLSA-BUILD-PLATFORM-PROVENANCE-GENERATION`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.M0025`, `AML.CS0008`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MAP-2.3`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM04-2025`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-I_DM_1_A`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-LOGGING`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PS.3.2`)

#### `ACP-TSV-005` — Staged Dynamic Testing And Gate Enforcement

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (52 grounded claims em 11 fontes):
  - NIST SP 800-53 Rev. 5 — 15 refs (`SP800-53-AC-3.12`, `SP800-53-CM-3.5`, `SP800-53-CM-5.1` + 2 more)
  - MITRE CAPEC v3.9 — 12 refs (`CAPEC-121`, `CAPEC-443`, `CAPEC-445` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 6 refs (`AML.TA0001`, `AML.T0011.000`, `AML.T0042` + 2 more)
  - OWASP SAMM v2.1 — 6 refs (`SAMM-ACTIVITY-I_SD_2_A`, `SAMM-ACTIVITY-I_SD_3_B`, `SAMM-ACTIVITY-O_OM_1_A` + 2 more)
  - OWASP ASVS v5.0.0 — 3 refs (`ASVS-REQ-V2.4.1`, `ASVS-REQ-V13.3.3`, `ASVS-REQ-V15.2.3`)
  - OWASP DSOMM — 3 refs (`DSOMM-ACTIVITY-7BB7076493924462935DE55B2E148199`, `DSOMM-ACTIVITY-DCCF1949B9A84CE8B9926A4A7F3A623A`, `DSOMM-ACTIVITY-CB6321AA0FBF49969E0805AB26EF4C1E`)
  - PCI DSS v4.0.1 — 2 refs (`PCI-6.5.5`, `PCI-11.4.4`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 2 refs (`SCAGILE-OPS-15`, `SCAGILE-EXP-4`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 1 refs (`NIST-AI-100-2-E2025-3.4.4`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM03-2025`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-LIFECYCLE-FEEDBACK`)

#### `ACP-TSV-006` — Specialized Empirical Testing

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (22 grounded claims em 9 fontes):
  - NIST SSDF (SP 800-218 v1.1) — 6 refs (`SSDF-PRACTICE-PW.8`, `SSDF-PRACTICE-RV.1`, `SSDF-PRACTICE-RV.3` + 2 more)
  - MITRE CAPEC v3.9 — 4 refs (`CAPEC-28`, `CAPEC-215`, `CAPEC-261` + 1 more)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 4 refs (`NIST-AI-100-2-E2025-3.3.1`, `NIST-AI-100-2-E2025-3.6`, `NIST-AI-100-2-E2025-4.1.3` + 1 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0001`, `AML.M0008`)
  - OWASP DSOMM — 2 refs (`DSOMM-ACTIVITY-D03BC41074A74E9282CBD01A020CB6BF`, `DSOMM-ACTIVITY-87B54313FAFD4860930F5EF132B3E4AD`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MEASURE-2.11`)
  - NIST SP 800-53 Rev. 5 — 1 refs (`SP800-53-IR-4.13`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-V_RT_1_B`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-TESTING`)

#### `ACP-TSV-007` — Human Review Of Security Test Signals

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 4 keywords × 100 ocorrências; principais: final, release, review, test)
- **Substrate v7 contributing sources** (67 grounded claims em 15 fontes):
  - NIST SP 800-53 Rev. 5 — 32 refs (`SP800-53-AC-4.9`, `SP800-53-AU-6.2`, `SP800-53-CA-3.1` + 2 more)
  - PCI DSS v4.0.1 — 8 refs (`PCI-1.2.2`, `PCI-5.4.1`, `PCI-10.4.1` + 2 more)
  - OWASP SAMM v2.1 — 5 refs (`SAMM-ACTIVITY-D_SA_3_B`, `SAMM-ACTIVITY-I_SD_2_A`, `SAMM-ACTIVITY-V_AA_2_A` + 2 more)
  - PCI Secure SLC v1.1 — 4 refs (`PCISSLC-2.6`, `PCISSLC-6.2`, `PCISSLC-8.3` + 1 more)
  - OWASP DSOMM — 3 refs (`DSOMM-ACTIVITY-7121B0C76ACE4D6B95D094535DBCCB57`, `DSOMM-ACTIVITY-95CAEF9636ED458CA0875C35D4F9DEC2`, `DSOMM-ACTIVITY-3F63BDBCC75F4780A941E6AD42E894E1`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 3 refs (`SCAGILE-OPS-2`, `SCAGILE-OPS-16`, `SCAGILE-EXP-2`)
  - CIS Controls v8.1.2 — 2 refs (`CIS-14.7`, `CIS-17.6`)
  - HIPAA Security Rule — 2 refs (`HIPAA-164-308a6`, `HIPAA-164-308a8`)
  - NIST SSDF (SP 800-218 v1.1) — 2 refs (`SSDF-PRACTICE-PW.7`, `SSDF-TASK-PW.7.2`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-358`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-13`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-32`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-VULN-RESPONSE`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEV-TESTING`)


### Mechanisms (5)

#### `ACM-TSV-001` — Integrated Security Scanners

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (221 grounded claims em 21 fontes):
  - NIST SP 800-53 Rev. 5 — 42 refs (`SP800-53-AU-6.2`, `SP800-53-CA-3.1`, `SP800-53-CA-3.2` + 2 more)
  - OWASP SAMM v2.1 — 35 refs (`SAMM-ACTIVITY-D_SA_1_A`, `SAMM-ACTIVITY-D_SA_1_B`, `SAMM-ACTIVITY-D_SA_2_A` + 2 more)
  - OWASP DSOMM — 30 refs (`DSOMM-ACTIVITY-47419324E263415B815DE7161B6B905E`, `DSOMM-ACTIVITY-48F97F31931C46EB9B3EE2FEC0CD0426`, `DSOMM-ACTIVITY-AE22DAFDBCD641EEBA018B7FE6FC1AD9` + 2 more)
  - PCI DSS v4.0.1 — 30 refs (`PCI-REQ-2`, `PCI-REQ-5`, `PCI-REQ-6` + 2 more)
  - CIS Controls v8.1.2 — 23 refs (`CIS-7`, `CIS-7.1`, `CIS-7.4` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 13 refs (`SSDF-PRACTICE-PO.1`, `SSDF-PRACTICE-PW.1`, `SSDF-PRACTICE-PW.2` + 2 more)
  - MITRE CAPEC v3.9 — 12 refs (`CAPEC-54`, `CAPEC-300`, `CAPEC-305` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 6 refs (`AML.TA0007`, `AML.T0001`, `AML.T0006` + 2 more)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 6 refs (`NIST-AI-100-2-E2025-2.3.1`, `NIST-AI-100-2-E2025-3.2`, `NIST-AI-100-2-E2025-3.4.4` + 2 more)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 5 refs (`SCAGILE-OPS-1`, `SCAGILE-OPS-2`, `SCAGILE-EXP-3` + 2 more)
  - PCI Secure SLC v1.1 — 4 refs (`PCISSLC-1.2`, `PCISSLC-1.3`, `PCISSLC-2.3` + 1 more)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 3 refs (`SCFPSSD-THREAT-MODELING`, `SCFPSSD-CODING-STANDARDS`, `SCFPSSD-FINDINGS`)
  - OWASP LLM Top 10 (2025) — 2 refs (`LLM03-2025`, `LLM09-2025`)
  - OWASP Machine Learning Top 10 — 2 refs (`ML07-2023`, `ML09-2023`)
  - OWASP Proactive Controls (2018) — 2 refs (`OPC-C2`, `OPC-C9`)
  - OWASP ASVS v5.0.0 — 1 refs (`ASVS-REQ-V16.4.3`)
  - ENISA — Multilayer AI Cybersecurity Practices (2023) — 1 refs (`ENISA-AI-FAICP-SURVEY`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MEASURE-2.7`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-TOOL-DESIGN`)
  - OWASP MCP — Third-Party Servers v1.0 — 1 refs (`OWASP-MCP-3P-GOVERNANCE-REGISTRY`)

#### `ACM-TSV-002` — Test Execution Surfaces

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (31 grounded claims em 8 fontes):
  - OWASP DSOMM — 13 refs (`DSOMM-ACTIVITY-A340F46B63604CB8847BA0D3483D09D3`, `DSOMM-ACTIVITY-BFDACB521E3F431DAE72D844A5E86415`, `DSOMM-ACTIVITY-7BB7076493924462935DE55B2E148199` + 2 more)
  - NIST SP 800-53 Rev. 5 — 9 refs (`SP800-53-CA-8.2`, `SP800-53-CM-2.6`, `SP800-53-CM-4.1` + 2 more)
  - OWASP SAMM v2.1 — 3 refs (`SAMM-ACTIVITY-I_SB_3_B`, `SAMM-ACTIVITY-I_SD_2_A`, `SAMM-ACTIVITY-V_RT_3_B`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.TA0005`, `AML.T0011`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-121`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-REQ-10`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-EXP-7`)
  - SLSA Specification v1.0 — Build Track — 1 refs (`SLSA-BUILD-L3`)

#### `ACM-TSV-003` — CI/CD Gate And Release Promotion

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (28 grounded claims em 11 fontes):
  - NIST SP 800-53 Rev. 5 — 11 refs (`SP800-53-AC-3.9`, `SP800-53-AU-10.3`, `SP800-53-CM-7.5` + 2 more)
  - PCI DSS v4.0.1 — 5 refs (`PCI-1.2.2`, `PCI-1.3.1`, `PCI-1.3.2` + 2 more)
  - OWASP SAMM v2.1 — 3 refs (`SAMM-ACTIVITY-I_SD_3_B`, `SAMM-ACTIVITY-O_OM_1_A`, `SAMM-ACTIVITY-O_OM_3_A`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0054`, `AML.M0001`)
  - EU Digital Operational Resilience Act (DORA) — 1 refs (`DORA-ART-5`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-308a8`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-77FFC53E9F3D41F492D302F04F9B6B0F`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-LIFECYCLE-FEEDBACK`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DELIVERY`)
  - SLSA Specification v1.0 — Build Track — 1 refs (`SLSA-PRINCIPLE-PREFER-ATTESTATIONS`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-PRACTICE-PS.3`)

#### `ACM-TSV-004` — Findings Workflow And Exception Governance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (98 grounded claims em 14 fontes):
  - NIST SP 800-53 Rev. 5 — 48 refs (`SP800-53-AC-4.9`, `SP800-53-AU-1`, `SP800-53-AU-2.3` + 2 more)
  - OWASP SAMM v2.1 — 16 refs (`SAMM-ACTIVITY-G_EG_3_A`, `SAMM-ACTIVITY-G_PC_1_A`, `SAMM-ACTIVITY-G_PC_1_B` + 2 more)
  - CIS Controls v8.1.2 — 9 refs (`CIS-17`, `CIS-17.1`, `CIS-17.2` + 2 more)
  - PCI DSS v4.0.1 — 8 refs (`PCI-2.1.2`, `PCI-6.5.2`, `PCI-9.3.1` + 2 more)
  - PCI Secure SLC v1.1 — 3 refs (`PCISSLC-4.2`, `PCISSLC-5.1`, `PCISSLC-10.1`)
  - NIST SSDF (SP 800-218 v1.1) — 3 refs (`SSDF-PRACTICE-PO.3`, `SSDF-TASK-PO.4.2`, `SSDF-TASK-PW.7.1`)
  - OWASP ASVS v5.0.0 — 2 refs (`ASVS-REQ-V16.5.1`, `ASVS-REQ-V16.5.3`)
  - NIST AI RMF 1.0 — 2 refs (`NIST-AI-RMF-MAP-2.3`, `NIST-AI-RMF-MEASURE-3.3`)
  - OWASP DSOMM — 2 refs (`DSOMM-ACTIVITY-3F63BDBCC75F4780A941E6AD42E894E1`, `DSOMM-ACTIVITY-EA6F69F754A54922AC15A77FF0C16162`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-1118`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-316b1`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM09-2025`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A08-2021`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-MITIGATIONS`)

#### `ACM-TSV-005` — Static Analysis Profile Management

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (14 grounded claims em 5 fontes):
  - OWASP DSOMM — 5 refs (`DSOMM-ACTIVITY-71699DAFB2A4466BA0B289F7DBB18506`, `DSOMM-ACTIVITY-E237176BBEC5447DA926E37D6DD60E4B`, `DSOMM-ACTIVITY-6C05C8378C9946E2828B7C903E27DBA4` + 2 more)
  - NIST SP 800-53 Rev. 5 — 3 refs (`SP800-53-CM-2`, `SP800-53-CM-8`, `SP800-53-SA-11.1`)
  - NIST AI RMF 1.0 — 2 refs (`NIST-AI-RMF-MEASURE-4.3`, `NIST-AI-RMF-MANAGE-4.3`)
  - OWASP SAMM v2.1 — 2 refs (`SAMM-ACTIVITY-D_TA_3_A`, `SAMM-ACTIVITY-O_EM_3_A`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 2 refs (`SCAGILE-OPS-4`, `SCAGILE-EXP-10`)


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
