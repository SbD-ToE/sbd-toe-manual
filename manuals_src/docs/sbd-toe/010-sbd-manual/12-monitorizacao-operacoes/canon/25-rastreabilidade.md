# 25. Rastreabilidade — Monitorização e Operações

## Sumário

Este capítulo é a **âncora primária** das slices AppSec Core V1: `ACO-SLG` (Logging de eventos de segurança e audit trail).

Cobertura V1 entity-level: **18 entidades** primárias (7 ControlObjectives + 5 Practices + 6 Mechanisms). Cada entidade é listada abaixo com cobertura no Manual (prose anchor) e fontes externas substrate v7 que contribuem para a sua substantive coverage.

---

## Slice `ACO-SLG` — Logging de eventos de segurança e audit trail

### ControlObjectives (7)

#### `ACO-SLG-001` — Critical Security Event Coverage And Catalog Discipline

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (105 grounded claims em 16 fontes):
  - NIST SP 800-53 Rev. 5 — 36 refs (`SP800-53-AC-1`, `SP800-53-AU-5.2`, `SP800-53-CP-7.5` + 2 more)
  - PCI DSS v4.0.1 — 16 refs (`PCI-REQ-11`, `PCI-5.2.3`, `PCI-6.3.1` + 2 more)
  - OWASP DSOMM — 15 refs (`DSOMM-ACTIVITY-48F97F31931C46EB9B3EE2FEC0CD0426`, `DSOMM-ACTIVITY-0A929C3EAB9A42068761ADF84B74622E`, `DSOMM-ACTIVITY-6217FE115ED74CF49DE4555BCFA6FE87` + 2 more)
  - OWASP SAMM v2.1 — 12 refs (`SAMM-ACTIVITY-D_SA_1_A`, `SAMM-ACTIVITY-D_SR_1_B`, `SAMM-ACTIVITY-D_TA_2_A` + 2 more)
  - CIS Controls v8.1.2 — 6 refs (`CIS-13.11`, `CIS-16`, `CIS-17.2` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 3 refs (`CWE-360`, `CWE-766`, `CWE-778`)
  - EU Digital Operational Resilience Act (DORA) — 3 refs (`DORA-ART-5`, `DORA-ART-10`, `DORA-ART-19`)
  - EU NIS2 Directive — 3 refs (`NIS2-ART-21`, `NIS2-ART-22`, `NIS2-ART-23`)
  - PCI Secure SLC v1.1 — 3 refs (`PCISSLC-3.2`, `PCISSLC-3.4`, `PCISSLC-5.1`)
  - HIPAA Security Rule — 2 refs (`HIPAA-164-308a2`, `HIPAA-164-308a6`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-639`)
  - ENISA — Multilayer AI Cybersecurity Practices (2023) — 1 refs (`ENISA-AI-FAICP-SURVEY`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-14`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-GOVERN-1.5`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-FINDINGS`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PW.2.1`)

#### `ACO-SLG-002` — Structured Audit Fields And Machine-Readable Log Shape

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (12 grounded claims em 3 fontes):
  - NIST SP 800-53 Rev. 5 — 10 refs (`SP800-53-AC-4.1`, `SP800-53-AC-16`, `SP800-53-AC-16.1` + 2 more)
  - OWASP ASVS v5.0.0 — 1 refs (`ASVS-REQ-V15.3.1`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-1.2.4`)

#### `ACO-SLG-003` — Log Integrity Protection And Access Discipline

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (83 grounded claims em 13 fontes):
  - NIST SP 800-53 Rev. 5 — 36 refs (`SP800-53-AC-3`, `SP800-53-AC-3.4`, `SP800-53-AC-3.6` + 2 more)
  - PCI DSS v4.0.1 — 14 refs (`PCI-REQ-3`, `PCI-4.2.1`, `PCI-6.3.3` + 2 more)
  - CIS Controls v8.1.2 — 8 refs (`CIS-3.1`, `CIS-3.2`, `CIS-3.7` + 2 more)
  - OWASP ASVS v5.0.0 — 7 refs (`ASVS-REQ-V6.3.8`, `ASVS-REQ-V11.3.3`, `ASVS-REQ-V14.1.2` + 2 more)
  - MITRE CAPEC v3.9 — 6 refs (`CAPEC-36`, `CAPEC-69`, `CAPEC-81` + 2 more)
  - HIPAA Security Rule — 4 refs (`HIPAA-164-310c`, `HIPAA-164-312a1`, `HIPAA-164-312b` + 1 more)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-654`, `CWE-656`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.TA0013`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 1 refs (`NIST-AI-100-2-E2025-3.1.2`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML05-2023`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C8`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-6.1`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-PRACTICE-PS.1`)

#### `ACO-SLG-004` — Audit Record Retention And Lifecycle Governance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (18 grounded claims em 7 fontes):
  - NIST SP 800-53 Rev. 5 — 9 refs (`SP800-53-AU-7`, `SP800-53-AU-10.3`, `SP800-53-AU-11` + 2 more)
  - CIS Controls v8.1.2 — 3 refs (`CIS-3.4`, `CIS-6.2`, `CIS-8.1`)
  - PCI DSS v4.0.1 — 2 refs (`PCI-3.2.1`, `PCI-10.5.1`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-675`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM02-2025`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-O_OM_3_A`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PS.3.1`)

#### `ACO-SLG-005` — Centralized Log Ingestion And Source Accountability

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (34 grounded claims em 7 fontes):
  - NIST SP 800-53 Rev. 5 — 12 refs (`SP800-53-AC-2`, `SP800-53-AC-8`, `SP800-53-AU-6.4` + 2 more)
  - CIS Controls v8.1.2 — 7 refs (`CIS-1`, `CIS-2`, `CIS-6.7` + 2 more)
  - MITRE CAPEC v3.9 — 6 refs (`CAPEC-150`, `CAPEC-384`, `CAPEC-445` + 2 more)
  - OWASP DSOMM — 4 refs (`DSOMM-ACTIVITY-95CAEF9636ED458CA0875C35D4F9DEC2`, `DSOMM-ACTIVITY-82E499D1F4634A4BBE9068812A874AF6`, `DSOMM-ACTIVITY-4ECED38A79044C45ADB050B663065540` + 1 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 3 refs (`AML.T0008`, `AML.T0010`, `AML.T0095.000`)
  - Anthropic MCP — Official Security Foundations (2025) — 1 refs (`MCP-SCOPE-MINIMIZATION`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-I_SD_3_B`)

#### `ACO-SLG-006` — Logging Pipeline Health And Silent-Failure Visibility

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (2 grounded claims em 1 fontes):
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-117`, `CWE-391`)

#### `ACO-SLG-007` — Security Logging And Audit Trail Assurance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (79 grounded claims em 16 fontes):
  - NIST SP 800-53 Rev. 5 — 18 refs (`SP800-53-AT-4`, `SP800-53-AU-5`, `SP800-53-AU-6` + 2 more)
  - OWASP SAMM v2.1 — 14 refs (`SAMM-ACTIVITY-D_SA_1_B`, `SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-D_SA_3_B` + 2 more)
  - OWASP ASVS v5.0.0 — 11 refs (`ASVS-REQ-V6.1.3`, `ASVS-REQ-V6.3.4`, `ASVS-REQ-V7.5.3` + 2 more)
  - CIS Controls v8.1.2 — 10 refs (`CIS-4.1`, `CIS-4.2`, `CIS-8.7` + 2 more)
  - OWASP DSOMM — 8 refs (`DSOMM-ACTIVITY-B597928E54D648A5A8068003DCD56AAB`, `DSOMM-ACTIVITY-CF81922530CB47028E3260225EEDC33D`, `DSOMM-ACTIVITY-03643CA203C2472B8E19956BF02FE9B7` + 2 more)
  - PCI Secure SLC v1.1 — 4 refs (`PCISSLC-2.4`, `PCISSLC-2.5`, `PCISSLC-6.2` + 1 more)
  - MITRE CAPEC v3.9 — 2 refs (`CAPEC-581`, `CAPEC-673`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0075`, `AML.M0024`)
  - SAFECode — Software Integrity Controls (2010) — 2 refs (`SCSIC-SOURCING-TRANSFER`, `SCSIC-DELIVERY-SIGNING`)
  - NIST SSDF (SP 800-218 v1.1) — 2 refs (`SSDF-TASK-PO.4.1`, `SSDF-TASK-PS.2.1`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-32`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM03-2025`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C9`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-4.1.1`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-EXP-8`)
  - SLSA Specification v1.0 — Build Track — 1 refs (`SLSA-PRINCIPLE-TRUST-PLATFORMS`)


### Practices (5)

#### `ACP-SLG-001` — Critical Event Catalog Governance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (6 grounded claims em 3 fontes):
  - NIST SP 800-53 Rev. 5 — 4 refs (`SP800-53-AU-2`, `SP800-53-AU-2.2`, `SP800-53-AU-3` + 1 more)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-778`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-10.7.2`)

#### `ACP-SLG-002` — Structured And Centralized Security Logging

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (67 grounded claims em 8 fontes):
  - CIS Controls v8.1.2 — 24 refs (`CIS-1.1`, `CIS-1.4`, `CIS-4.2` + 2 more)
  - NIST SP 800-53 Rev. 5 — 20 refs (`SP800-53-AC-12.1`, `SP800-53-AU-2`, `SP800-53-AU-3.2` + 2 more)
  - OWASP DSOMM — 8 refs (`DSOMM-ACTIVITY-4ECED38A79044C45ADB050B663065540`, `DSOMM-ACTIVITY-FE875E17AE4A45F8A359244AA4FCBC04`, `DSOMM-ACTIVITY-7C7350896A83419F8B27C1E676CEDEA1` + 2 more)
  - OWASP SAMM v2.1 — 8 refs (`SAMM-ACTIVITY-I_DM_1_A`, `SAMM-ACTIVITY-I_SB_3_A`, `SAMM-ACTIVITY-I_SB_3_B` + 2 more)
  - MITRE CAPEC v3.9 — 2 refs (`CAPEC-150`, `CAPEC-571`)
  - PCI DSS v4.0.1 — 2 refs (`PCI-REQ-10`, `PCI-1.2.4`)
  - NIST SSDF (SP 800-218 v1.1) — 2 refs (`SSDF-PRACTICE-PO.3`, `SSDF-TASK-PW.1.3`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-EXP-11`)

#### `ACP-SLG-003` — Log Integrity And Protected Access

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (610 grounded claims em 26 fontes):
  - NIST SP 800-53 Rev. 5 — 299 refs (`SP800-53-AC-1`, `SP800-53-AC-2`, `SP800-53-AC-2.6` + 2 more)
  - PCI DSS v4.0.1 — 79 refs (`PCI-REQ-3`, `PCI-REQ-4`, `PCI-REQ-7` + 2 more)
  - OWASP ASVS v5.0.0 — 51 refs (`ASVS-REQ-V1.2.4`, `ASVS-REQ-V1.2.6`, `ASVS-REQ-V1.3.6` + 2 more)
  - MITRE CAPEC v3.9 — 39 refs (`CAPEC-21`, `CAPEC-22`, `CAPEC-36` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 29 refs (`CWE-1220`, `CWE-1230`, `CWE-209` + 2 more)
  - CIS Controls v8.1.2 — 21 refs (`CIS-2.5`, `CIS-3`, `CIS-3.1` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 14 refs (`SSDF-PRACTICE-PO.1`, `SSDF-PRACTICE-PO.4`, `SSDF-PRACTICE-PS.1` + 2 more)
  - OWASP SAMM v2.1 — 10 refs (`SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-D_SA_3_B`, `SAMM-ACTIVITY-D_SR_1_A` + 2 more)
  - PCI Secure SLC v1.1 — 9 refs (`PCISSLC-3.2`, `PCISSLC-3.3`, `PCISSLC-4.2` + 2 more)
  - HIPAA Security Rule — 8 refs (`HIPAA-164-308a1`, `HIPAA-164-308a4`, `HIPAA-164-308a5` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 8 refs (`AML.TA0013`, `AML.T0041`, `AML.T0011.000` + 2 more)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 6 refs (`NIST-AI-100-2-E2025-2.1`, `NIST-AI-100-2-E2025-3.1.2`, `NIST-AI-100-2-E2025-3.1.3` + 2 more)
  - SAFECode — Software Integrity Controls (2010) — 6 refs (`SCSIC-SOURCING-CONTRACT`, `SCSIC-SOURCING-TRANSFER`, `SCSIC-DEVELOPMENT` + 2 more)
  - OWASP Machine Learning Top 10 — 5 refs (`ML02-2023`, `ML05-2023`, `ML06-2023` + 2 more)
  - OWASP DSOMM — 4 refs (`DSOMM-ACTIVITY-72737130472C498480F89AB2F1C2ED5D`, `DSOMM-ACTIVITY-4CAE98C2416344EDBB883C67C569533A`, `DSOMM-ACTIVITY-82E499D1F4634A4BBE9068812A874AF6` + 1 more)
  - OWASP LLM Top 10 (2025) — 4 refs (`LLM02-2025`, `LLM04-2025`, `LLM07-2025` + 1 more)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 4 refs (`SCAGILE-OPS-2`, `SCAGILE-OPS-16`, `SCAGILE-EXP-2` + 1 more)
  - EU GDPR (RGPD) — 2 refs (`GDPR-ART-5`, `GDPR-ART-32`)
  - OWASP Proactive Controls (2018) — 2 refs (`OPC-C3`, `OPC-C8`)
  - OWASP Top 10 (2021) — 2 refs (`TOP10-A02-2021`, `TOP10-A08-2021`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 2 refs (`SCFPSSD-LOGGING`, `SCFPSSD-DATA-HANDLING`)
  - SLSA Specification v1.0 — Build Track — 2 refs (`SLSA-PRINCIPLE-TRUST-PLATFORMS`, `SLSA-PRINCIPLE-TRUST-CODE`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-DEPLOYMENT`)
  - OWASP MCP — Third-Party Servers v1.0 — 1 refs (`OWASP-MCP-3P-AUTH-AUTHZ-REGISTRATION`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP01-2025`)

#### `ACP-SLG-004` — Log Retention And Lifecycle Governance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (16 grounded claims em 5 fontes):
  - NIST SP 800-53 Rev. 5 — 8 refs (`SP800-53-AU-4`, `SP800-53-AU-5.1`, `SP800-53-AU-10.3` + 2 more)
  - OWASP SAMM v2.1 — 3 refs (`SAMM-ACTIVITY-G_PC_1_A`, `SAMM-ACTIVITY-G_PC_3_B`, `SAMM-ACTIVITY-V_ST_2_B`)
  - CIS Controls v8.1.2 — 2 refs (`CIS-3.4`, `CIS-8.1`)
  - PCI DSS v4.0.1 — 2 refs (`PCI-3.2.1`, `PCI-10.5.1`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM02-2025`)

#### `ACP-SLG-005` — Logging Pipeline Health Visibility

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 3 keywords × 129 ocorrências; principais: detect, logging, pipeline)
- **Substrate v7 contributing sources** (7 grounded claims em 4 fontes):
  - NIST SP 800-53 Rev. 5 — 3 refs (`SP800-53-AU-5.4`, `SP800-53-MA-1`, `SP800-53-MA-4`)
  - OWASP SAMM v2.1 — 2 refs (`SAMM-ACTIVITY-O_EM_3_A`, `SAMM-ACTIVITY-O_IM_3_A`)
  - OWASP ASVS v5.0.0 — 1 refs (`ASVS-REQ-V16.5.4`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM03-2025`)


### Mechanisms (6)

#### `ACM-SLG-001` — Machine-Readable Structured Logging

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (5 grounded claims em 4 fontes):
  - OWASP SAMM v2.1 — 2 refs (`SAMM-ACTIVITY-V_AA_1_A`, `SAMM-ACTIVITY-V_AA_1_B`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-637`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-7C7350896A83419F8B27C1E676CEDEA1`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-REQ-10`)

#### `ACM-SLG-002` — Central Log Ingestion And Normalization

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 5 keywords × 134 ocorrências; principais: central, forwarding, ingestion, logs, normalization)
- **Substrate v7 contributing sources** (9 grounded claims em 5 fontes):
  - CIS Controls v8.1.2 — 3 refs (`CIS-1`, `CIS-1.1`, `CIS-8.9`)
  - NIST SP 800-53 Rev. 5 — 3 refs (`SP800-53-CM-8.7`, `SP800-53-SA-19.3`, `SP800-53-SC-36`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-2A44B708734F4463B0CB86DC46344B2F`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM03-2025`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-O_OM_3_A`)

#### `ACM-SLG-003` — Log Integrity And Access Controls

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (641 grounded claims em 25 fontes):
  - NIST SP 800-53 Rev. 5 — 341 refs (`SP800-53-AC-1`, `SP800-53-AC-2`, `SP800-53-AC-2.4` + 2 more)
  - PCI DSS v4.0.1 — 77 refs (`PCI-REQ-1`, `PCI-REQ-3`, `PCI-REQ-4` + 2 more)
  - MITRE CAPEC v3.9 — 51 refs (`CAPEC-1`, `CAPEC-21`, `CAPEC-31` + 2 more)
  - OWASP ASVS v5.0.0 — 29 refs (`ASVS-REQ-V1.2.4`, `ASVS-REQ-V1.5.2`, `ASVS-REQ-V6.1.1` + 2 more)
  - CIS Controls v8.1.2 — 26 refs (`CIS-2.5`, `CIS-2.6`, `CIS-3` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 26 refs (`CWE-1220`, `CWE-1230`, `CWE-183` + 2 more)
  - HIPAA Security Rule — 10 refs (`HIPAA-164-308a2`, `HIPAA-164-308a4`, `HIPAA-164-308a6` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 10 refs (`AML.TA0012`, `AML.TA0013`, `AML.T0041` + 2 more)
  - OWASP SAMM v2.1 — 10 refs (`SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-D_SA_2_B`, `SAMM-ACTIVITY-D_SA_3_B` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 9 refs (`SSDF-PRACTICE-PO.1`, `SSDF-PRACTICE-PS.1`, `SSDF-PRACTICE-PS.2` + 2 more)
  - PCI Secure SLC v1.1 — 8 refs (`PCISSLC-1.2`, `PCISSLC-3.2`, `PCISSLC-3.3` + 2 more)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 6 refs (`NIST-AI-100-2-E2025-2.1`, `NIST-AI-100-2-E2025-2.1.3`, `NIST-AI-100-2-E2025-3.1.2` + 2 more)
  - SAFECode — Software Integrity Controls (2010) — 6 refs (`SCSIC-SOURCING`, `SCSIC-SOURCING-CONTRACT`, `SCSIC-SOURCING-TRANSFER` + 2 more)
  - OWASP DSOMM — 5 refs (`DSOMM-ACTIVITY-72737130472C498480F89AB2F1C2ED5D`, `DSOMM-ACTIVITY-82E499D1F4634A4BBE9068812A874AF6`, `DSOMM-ACTIVITY-746025A6DBFB4087A000E46ACAB64EE1` + 2 more)
  - OWASP LLM Top 10 (2025) — 5 refs (`LLM02-2025`, `LLM04-2025`, `LLM07-2025` + 2 more)
  - OWASP Machine Learning Top 10 — 5 refs (`ML02-2023`, `ML03-2023`, `ML05-2023` + 2 more)
  - OWASP Proactive Controls (2018) — 4 refs (`OPC-C1`, `OPC-C3`, `OPC-C7` + 1 more)
  - OWASP Top 10 (2021) — 3 refs (`TOP10-A01-2021`, `TOP10-A02-2021`, `TOP10-A08-2021`)
  - EU GDPR (RGPD) — 2 refs (`GDPR-ART-5`, `GDPR-ART-32`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 2 refs (`SCFPSSD-IAM`, `SCFPSSD-LOGGING`)
  - SLSA Specification v1.0 — Build Track — 2 refs (`SLSA-PRINCIPLE-TRUST-PLATFORMS`, `SLSA-PRINCIPLE-TRUST-CODE`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - Anthropic MCP — Official Security Foundations (2025) — 1 refs (`MCP-SCOPE-MINIMIZATION`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-GOVERNANCE`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP01-2025`)

#### `ACM-SLG-004` — Logging Failure Visibility Controls

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (23 grounded claims em 8 fontes):
  - NIST SP 800-53 Rev. 5 — 11 refs (`SP800-53-AU-5.4`, `SP800-53-MA-1`, `SP800-53-MA-2` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 3 refs (`CWE-1118`, `CWE-391`, `CWE-455`)
  - OWASP SAMM v2.1 — 3 refs (`SAMM-ACTIVITY-I_DM_1_A`, `SAMM-ACTIVITY-O_IM_3_A`, `SAMM-ACTIVITY-O_OM_3_A`)
  - OWASP ASVS v5.0.0 — 2 refs (`ASVS-REQ-V16.5.2`, `ASVS-REQ-V16.5.4`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP08-2025`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A09-2021`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-3.4`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-MITIGATIONS`)

#### `ACM-SLG-005` — Security Event Catalog And Coverage Verification

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 5 keywords × 21 ocorrências; principais: audit, coverage, define, event, trail)
- **Substrate v7 contributing sources** (135 grounded claims em 16 fontes):
  - OWASP SAMM v2.1 — 33 refs (`SAMM-ACTIVITY-D_SR_1_B`, `SAMM-ACTIVITY-D_TA_3_A`, `SAMM-ACTIVITY-G_EG_1_A` + 2 more)
  - NIST SP 800-53 Rev. 5 — 27 refs (`SP800-53-AU-1`, `SP800-53-AU-2`, `SP800-53-AU-2.2` + 2 more)
  - OWASP DSOMM — 21 refs (`DSOMM-ACTIVITY-9768F154357A4C06AF6FD66570677C9B`, `DSOMM-ACTIVITY-F0E018143B884BD0A3A9F91DB001D20BADVANCED`, `DSOMM-ACTIVITY-CCFDD0A8991E4269AD77C0A54CA655CB` + 2 more)
  - PCI DSS v4.0.1 — 16 refs (`PCI-REQ-11`, `PCI-1.1.1`, `PCI-2.1.1` + 2 more)
  - CIS Controls v8.1.2 — 12 refs (`CIS-8.1`, `CIS-8.5`, `CIS-8.7` + 2 more)
  - OWASP ASVS v5.0.0 — 6 refs (`ASVS-REQ-V6.3.5`, `ASVS-REQ-V11.1.3`, `ASVS-REQ-V16.1.1` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 5 refs (`SSDF-PRACTICE-PW.8`, `SSDF-TASK-PW.2.1`, `SSDF-TASK-PW.8.1` + 2 more)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 4 refs (`SCAGILE-OPS-1`, `SCAGILE-OPS-2`, `SCAGILE-OPS-9` + 1 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0042`, `AML.CS0008`)
  - OWASP MCP — Third-Party Servers v1.0 — 2 refs (`OWASP-MCP-3P-CLIENT-SECURITY-DISCOVERY`, `OWASP-MCP-3P-GOVERNANCE-REGISTRY`)
  - PCI Secure SLC v1.1 — 2 refs (`PCISSLC-2.5`, `PCISSLC-4.1`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-95`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-CONTINUOUS-VALIDATION`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML07-2023`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-FINDINGS`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEV-TESTING`)

#### `ACM-SLG-006` — Log Retention Lifecycle Management Controls

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 6 keywords × 223 ocorrências; principais: lifecycle, logs, management, policies, rules)
- **Substrate v7 contributing sources** (19 grounded claims em 9 fontes):
  - NIST SP 800-53 Rev. 5 — 7 refs (`SP800-53-AU-5.1`, `SP800-53-CM-1`, `SP800-53-CM-2.3` + 2 more)
  - CIS Controls v8.1.2 — 5 refs (`CIS-3.4`, `CIS-5.3`, `CIS-5.5` + 2 more)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-546`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-7F36B9BABC054FD69A2A73344C249722`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM02-2025`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-DEPLOYMENT`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-I_SD_3_B`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-3.2.1`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PS.3.1`)


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
