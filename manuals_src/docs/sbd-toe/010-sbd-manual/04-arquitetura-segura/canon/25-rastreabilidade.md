# 25. Rastreabilidade — Arquitetura Segura

## Sumário

Este capítulo é a **âncora primária** das slices AppSec Core V1: `ACO-ATB` (Arquitetura segura e fronteiras de confiança), `ACO-IAT` (Identidade, autenticação e gestão de sessões), `ACO-ITS` (Integração e segurança service-to-service).

Cobertura V1 entity-level: **56 entidades** primárias (21 ControlObjectives + 19 Practices + 16 Mechanisms). Cada entidade é listada abaixo com cobertura no Manual (prose anchor) e fontes externas substrate v7 que contribuem para a sua substantive coverage.

---

## Slice `ACO-ATB` — Arquitetura segura e fronteiras de confiança

### ControlObjectives (7)

#### `ACO-ATB-001` — Architecture Baseline And Decision Traceability

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (3 grounded claims em 2 fontes):
  - OWASP SAMM v2.1 — 2 refs (`SAMM-ACTIVITY-V_AA_1_A`, `SAMM-ACTIVITY-V_AA_1_B`)
  - NIST SP 800-53 Rev. 5 — 1 refs (`SP800-53-SA-5.3`)

#### `ACO-ATB-002` — Trust Boundary Clarity And Protected Data Flows

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (200 grounded claims em 22 fontes):
  - NIST SP 800-53 Rev. 5 — 91 refs (`SP800-53-AC-1`, `SP800-53-AC-3`, `SP800-53-AC-3.5` + 2 more)
  - PCI DSS v4.0.1 — 32 refs (`PCI-REQ-3`, `PCI-1.2.2`, `PCI-1.2.3` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 19 refs (`CWE-1220`, `CWE-182`, `CWE-183` + 2 more)
  - CIS Controls v8.1.2 — 13 refs (`CIS-3`, `CIS-3.1`, `CIS-3.2` + 2 more)
  - OWASP ASVS v5.0.0 — 10 refs (`ASVS-REQ-V1.3.6`, `ASVS-REQ-V1.5.2`, `ASVS-REQ-V2.3.5` + 2 more)
  - MITRE CAPEC v3.9 — 7 refs (`CAPEC-10`, `CAPEC-39`, `CAPEC-69` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 5 refs (`AML.T0041`, `AML.T0054`, `AML.T0111` + 2 more)
  - NIST AI RMF 1.0 — 4 refs (`NIST-AI-RMF-GOVERN-1`, `NIST-AI-RMF-GOVERN-1.3`, `NIST-AI-RMF-GOVERN-2` + 1 more)
  - EU GDPR (RGPD) — 3 refs (`GDPR-ART-5`, `GDPR-ART-32`, `GDPR-ART-35`)
  - OWASP DSOMM — 2 refs (`DSOMM-ACTIVITY-72737130472C498480F89AB2F1C2ED5D`, `DSOMM-ACTIVITY-6DF508EF86FC4C22BD9F646C3127CE7D`)
  - OWASP SAMM v2.1 — 2 refs (`SAMM-ACTIVITY-O_OM_2_A`, `SAMM-ACTIVITY-O_OM_3_A`)
  - PCI Secure SLC v1.1 — 2 refs (`PCISSLC-3.2`, `PCISSLC-7.2`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-308a1`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 1 refs (`NIST-AI-100-2-E2025-4.2.1`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM08-2025`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML06-2023`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C8`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A08-2021`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-SOURCING-TRANSFER`)
  - SLSA Specification v1.0 — Build Track — 1 refs (`SLSA-PRINCIPLE-TRUST-CODE`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-PRACTICE-PS.2`)

#### `ACO-ATB-003` — External Exposure Justification And Boundary Mediation

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (5 grounded claims em 2 fontes):
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 3 refs (`AML.T0048`, `AML.T0048.002`, `AML.T0051.001`)
  - NIST SP 800-53 Rev. 5 — 2 refs (`SP800-53-IR-9.4`, `SP800-53-MP-5.1`)

#### `ACO-ATB-004` — Technical Segmentation And Sensitive Domain Isolation

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (42 grounded claims em 8 fontes):
  - NIST SP 800-53 Rev. 5 — 32 refs (`SP800-53-AC-4.23`, `SP800-53-AC-6.4`, `SP800-53-CM-7.9` + 2 more)
  - MITRE CAPEC v3.9 — 3 refs (`CAPEC-390`, `CAPEC-516`, `CAPEC-646`)
  - CIS Controls v8.1.2 — 2 refs (`CIS-3.12`, `CIS-16.8`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-653`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-E14DE74194B3447C8B07EEA947D82E61`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML07-2023`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-O_OM_1_A`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-11.4.5`)

#### `ACO-ATB-005` — Architecture Review And Change Trigger Discipline

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (17 grounded claims em 5 fontes):
  - NIST SP 800-53 Rev. 5 — 12 refs (`SP800-53-AU-1`, `SP800-53-AU-2.3`, `SP800-53-CA-1` + 2 more)
  - OWASP SAMM v2.1 — 2 refs (`SAMM-ACTIVITY-D_TA_3_A`, `SAMM-ACTIVITY-V_AA_3_B`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-17.8`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-GOVERN-1.5`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-5.1`)

#### `ACO-ATB-006` — Architectural Topology Validation And Pattern Conformance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (31 grounded claims em 11 fontes):
  - NIST SP 800-53 Rev. 5 — 11 refs (`SP800-53-CM-3.2`, `SP800-53-CM-6.1`, `SP800-53-CM-6.4` + 2 more)
  - OWASP SAMM v2.1 — 5 refs (`SAMM-ACTIVITY-V_AA_2_A`, `SAMM-ACTIVITY-V_RT_1_A`, `SAMM-ACTIVITY-V_RT_2_A` + 2 more)
  - MITRE CAPEC v3.9 — 3 refs (`CAPEC-80`, `CAPEC-231`, `CAPEC-678`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 3 refs (`AML.T0042`, `AML.M0008`, `AML.M0033`)
  - OWASP DSOMM — 3 refs (`DSOMM-ACTIVITY-48E92BB1FDBA40E8B6C235DE0D431833`, `DSOMM-ACTIVITY-017D9E2642B549A4B9459F59B308FB99`, `DSOMM-ACTIVITY-13367D8FE37F4197A6109FFCA4FDE261`)
  - OWASP ASVS v5.0.0 — 1 refs (`ASVS-REQ-V2.1.2`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-12.1`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM02-2025`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-CONTINUOUS-VALIDATION`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML06-2023`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C5`)

#### `ACO-ATB-007` — Secure Architecture Governance And Boundary Integrity

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (113 grounded claims em 20 fontes):
  - NIST SP 800-53 Rev. 5 — 25 refs (`SP800-53-PL-2`, `SP800-53-PL-8`, `SP800-53-PL-8.1` + 2 more)
  - OWASP SAMM v2.1 — 25 refs (`SAMM-ACTIVITY-D_SA_1_A`, `SAMM-ACTIVITY-D_SA_1_B`, `SAMM-ACTIVITY-D_SA_2_A` + 2 more)
  - CIS Controls v8.1.2 — 10 refs (`CIS-4`, `CIS-4.1`, `CIS-4.2` + 2 more)
  - MITRE CAPEC v3.9 — 9 refs (`CAPEC-184`, `CAPEC-440`, `CAPEC-523` + 2 more)
  - OWASP DSOMM — 8 refs (`DSOMM-ACTIVITY-6217FE115ED74CF49DE4555BCFA6FE87`, `DSOMM-ACTIVITY-7121B0C76ACE4D6B95D094535DBCCB57`, `DSOMM-ACTIVITY-F994A55D71BB45A4A8870A213D72C504` + 2 more)
  - OWASP ASVS v5.0.0 — 6 refs (`ASVS-REQ-V15.1.4`, `ASVS-REQ-V15.1.5`, `ASVS-REQ-V15.2.1` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 6 refs (`AML.T0008.001`, `AML.T0011.000`, `AML.M0013` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 4 refs (`SSDF-PRACTICE-PO.5`, `SSDF-PRACTICE-PW.1`, `SSDF-PRACTICE-PW.4` + 1 more)
  - PCI DSS v4.0.1 — 3 refs (`PCI-REQ-1`, `PCI-REQ-2`, `PCI-REQ-6`)
  - PCI Secure SLC v1.1 — 3 refs (`PCISSLC-2.3`, `PCISSLC-2.4`, `PCISSLC-8.2`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 3 refs (`SCFPSSD-SECURITY-CONTROLS`, `SCFPSSD-DESIGN-PRINCIPLES`, `SCFPSSD-THREAT-MODELING`)
  - OWASP MCP — Secure Server Development v1.0 — 2 refs (`OWASP-MCP-TOOL-DESIGN`, `OWASP-MCP-GOVERNANCE`)
  - OWASP Proactive Controls (2018) — 2 refs (`OPC-C1`, `OPC-C2`)
  - ENISA — Multilayer AI Cybersecurity Practices (2023) — 1 refs (`ENISA-AI-FAICP-LAYER-II`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-13`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-308a2`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 1 refs (`NIST-AI-100-2-E2025-4.2.6`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM03-2025`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEVELOPMENT`)


### Practices (7)

#### `ACP-ATB-001` — Architecture Baseline Definition

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (11 grounded claims em 6 fontes):
  - OWASP SAMM v2.1 — 4 refs (`SAMM-ACTIVITY-D_SA_3_A`, `SAMM-ACTIVITY-I_SB_3_A`, `SAMM-ACTIVITY-O_EM_2_A` + 1 more)
  - NIST SP 800-53 Rev. 5 — 3 refs (`SP800-53-CM-2`, `SP800-53-PL-2`, `SP800-53-PL-10`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-12.2`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-5992C38C8597403589DBD15820D81C3A`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-8.3`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PW.9.1`)

#### `ACP-ATB-002` — Architectural Decision And Solution Traceability

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (34 grounded claims em 9 fontes):
  - NIST SP 800-53 Rev. 5 — 19 refs (`SP800-53-AU-12.1`, `SP800-53-CM-8`, `SP800-53-CM-8.4` + 2 more)
  - OWASP SAMM v2.1 — 4 refs (`SAMM-ACTIVITY-I_DM_3_A`, `SAMM-ACTIVITY-O_EM_1_A`, `SAMM-ACTIVITY-V_AA_1_A` + 1 more)
  - MITRE CAPEC v3.9 — 3 refs (`CAPEC-580`, `CAPEC-581`, `CAPEC-702`)
  - PCI DSS v4.0.1 — 2 refs (`PCI-REQ-8`, `PCI-10.4.2`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 2 refs (`SCFPSSD-LOGGING`, `SCFPSSD-MITIGATIONS`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-2`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-1092`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-GOVERN-1.6`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PO.3.1`)

#### `ACP-ATB-003` — Trust-Boundary And Flow Review

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (70 grounded claims em 14 fontes):
  - NIST SP 800-53 Rev. 5 — 32 refs (`SP800-53-AC-4`, `SP800-53-AC-4.1`, `SP800-53-AC-4.2` + 2 more)
  - OWASP DSOMM — 6 refs (`DSOMM-ACTIVITY-0DE465A655A74343AF79948BB5FF10BA`, `DSOMM-ACTIVITY-AE22DAFDBCD641EEBA018B7FE6FC1AD9`, `DSOMM-ACTIVITY-7121B0C76ACE4D6B95D094535DBCCB57` + 2 more)
  - OWASP SAMM v2.1 — 6 refs (`SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-D_SA_3_B`, `SAMM-ACTIVITY-D_SR_1_A` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 6 refs (`SSDF-PRACTICE-PO.4`, `SSDF-PRACTICE-PO.5`, `SSDF-PRACTICE-PW.2` + 2 more)
  - PCI DSS v4.0.1 — 4 refs (`PCI-1.2.4`, `PCI-1.4.1`, `PCI-1.4.2` + 1 more)
  - OWASP ASVS v5.0.0 — 3 refs (`ASVS-REQ-V8.4.2`, `ASVS-REQ-V15.1.4`, `ASVS-REQ-V15.2.4`)
  - SAFECode — Software Integrity Controls (2010) — 3 refs (`SCSIC-SOURCING-CONTRACT`, `SCSIC-SOURCING-TRANSFER`, `SCSIC-DEVELOPMENT`)
  - CIS Controls v8.1.2 — 2 refs (`CIS-4.1`, `CIS-4.2`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 2 refs (`SCFPSSD-THREAT-MODELING`, `SCFPSSD-PLANNING`)
  - SLSA Specification v1.0 — Build Track — 2 refs (`SLSA-PRINCIPLE-TRUST-PLATFORMS`, `SLSA-PRINCIPLE-TRUST-CODE`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-501`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM04-2025`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-GOVERNANCE`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-3.2`)

#### `ACP-ATB-004` — External Exposure And Boundary Mediation Design

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (10 grounded claims em 4 fontes):
  - NIST SP 800-53 Rev. 5 — 6 refs (`SP800-53-IR-9.4`, `SP800-53-MP-5.1`, `SP800-53-PE-3.7` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-1230`, `CWE-497`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-308a6`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.T0048`)

#### `ACP-ATB-005` — Architecture Review And Approval Governance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (6 grounded claims em 2 fontes):
  - OWASP SAMM v2.1 — 4 refs (`SAMM-ACTIVITY-G_PC_1_B`, `SAMM-ACTIVITY-G_SM_1_A`, `SAMM-ACTIVITY-V_AA_1_A` + 1 more)
  - NIST SP 800-53 Rev. 5 — 2 refs (`SP800-53-MA-3`, `SP800-53-PL-2.2`)

#### `ACP-ATB-006` — Architecture Change Trigger Discipline

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 5 keywords × 76 ocorrências; principais: architecture, governance, review, thresholds, trigger)
- **Substrate v7 contributing sources** (11 grounded claims em 2 fontes):
  - NIST SP 800-53 Rev. 5 — 10 refs (`SP800-53-AU-1`, `SP800-53-AU-6`, `SP800-53-CM-1` + 2 more)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-D_TA_3_A`)

#### `ACP-ATB-007` — Automatable Topology And Pattern Validation

- **Manual prose:** cobertura **cross-chapter** — content encontrado em Cap. 03 (`03-threat-modeling`), Cap. 08 (`08-iac-infraestrutura`), Cap. 13 (`13-formacao-onboarding`). Cap. expected (04-arquitetura-segura) tem cobertura fraca; ler em chapter(s) listada(s).
- **Substrate v7 contributing sources** (20 grounded claims em 7 fontes):
  - NIST SP 800-53 Rev. 5 — 10 refs (`SP800-53-CM-2.2`, `SP800-53-CM-3.2`, `SP800-53-CM-5.7` + 2 more)
  - OWASP SAMM v2.1 — 4 refs (`SAMM-ACTIVITY-V_AA_2_A`, `SAMM-ACTIVITY-V_RT_1_A`, `SAMM-ACTIVITY-V_RT_2_A` + 1 more)
  - OWASP DSOMM — 2 refs (`DSOMM-ACTIVITY-48E92BB1FDBA40E8B6C235DE0D431833`, `DSOMM-ACTIVITY-017D9E2642B549A4B9459F59B308FB99`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-80`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.M0033`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C5`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-EXP-2`)


### Mechanisms (5)

#### `ACM-ATB-001` — Versioned Diagrams And ADR Records

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (295 grounded claims em 18 fontes):
  - NIST SP 800-53 Rev. 5 — 119 refs (`SP800-53-AC-1`, `SP800-53-AC-2`, `SP800-53-AC-3.6` + 2 more)
  - PCI DSS v4.0.1 — 62 refs (`PCI-REQ-1`, `PCI-REQ-2`, `PCI-REQ-7` + 2 more)
  - CIS Controls v8.1.2 — 21 refs (`CIS-2`, `CIS-2.2`, `CIS-2.5` + 2 more)
  - OWASP SAMM v2.1 — 17 refs (`SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-D_SR_2_A`, `SAMM-ACTIVITY-G_PC_1_A` + 2 more)
  - MITRE CAPEC v3.9 — 16 refs (`CAPEC-75`, `CAPEC-445`, `CAPEC-518` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 16 refs (`SSDF-PRACTICE-PS.2`, `SSDF-PRACTICE-PS.3`, `SSDF-TASK-PO.1.1` + 2 more)
  - PCI Secure SLC v1.1 — 9 refs (`PCISSLC-2.3`, `PCISSLC-3.3`, `PCISSLC-5.1` + 2 more)
  - OWASP ASVS v5.0.0 — 8 refs (`ASVS-REQ-V14.2.4`, `ASVS-REQ-V15.1.1`, `ASVS-REQ-V15.1.2` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 6 refs (`AML.T0002.001`, `AML.T0011.000`, `AML.T0079` + 2 more)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 6 refs (`SCAGILE-OPS-1`, `SCAGILE-OPS-2`, `SCAGILE-OPS-5` + 2 more)
  - OWASP DSOMM — 5 refs (`DSOMM-ACTIVITY-47419324E263415B815DE7161B6B905E`, `DSOMM-ACTIVITY-B597928E54D648A5A8068003DCD56AAB`, `DSOMM-ACTIVITY-CF81922530CB47028E3260225EEDC33D` + 2 more)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 3 refs (`SCFPSSD-SECURITY-CONTROLS`, `SCFPSSD-LOGGING`, `SCFPSSD-CODING-STANDARDS`)
  - SAFECode — Software Integrity Controls (2010) — 2 refs (`SCSIC-SOURCING-TRANSFER`, `SCSIC-DELIVERY-SIGNING`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-215`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-13`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-316b1`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MAP-2.3`)
  - SLSA Specification v1.0 — Build Track — 1 refs (`SLSA-BUILD-L1`)

#### `ACM-ATB-002` — Trust-Boundary And DFD Modeling

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (38 grounded claims em 10 fontes):
  - NIST SP 800-53 Rev. 5 — 16 refs (`SP800-53-AC-4.19`, `SP800-53-CP-7.5`, `SP800-53-PL-2` + 2 more)
  - OWASP DSOMM — 6 refs (`DSOMM-ACTIVITY-0DE465A655A74343AF79948BB5FF10BA`, `DSOMM-ACTIVITY-48F97F31931C46EB9B3EE2FEC0CD0426`, `DSOMM-ACTIVITY-DD5ED7C1BDBF400FB75F6D3953A1A04E` + 2 more)
  - OWASP SAMM v2.1 — 5 refs (`SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-D_SA_3_B`, `SAMM-ACTIVITY-D_TA_2_A` + 2 more)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 3 refs (`SCFPSSD-DESIGN-PRINCIPLES`, `SCFPSSD-THREAT-MODELING`, `SCFPSSD-PLANNING`)
  - SLSA Specification v1.0 — Build Track — 2 refs (`SLSA-PRINCIPLE-TRUST-PLATFORMS`, `SLSA-PRINCIPLE-TRUST-CODE`)
  - NIST SSDF (SP 800-218 v1.1) — 2 refs (`SSDF-PRACTICE-PO.5`, `SSDF-PRACTICE-PW.1`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-16.14`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-501`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MEASURE-4`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-3.2`)

#### `ACM-ATB-003` — Boundary Mediation Controls

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (11 grounded claims em 2 fontes):
  - NIST SP 800-53 Rev. 5 — 9 refs (`SP800-53-AT-3.1`, `SP800-53-CP-10.3`, `SP800-53-IR-9.4` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-497`, `CWE-654`)

#### `ACM-ATB-004` — Architecture Review Gates

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (14 grounded claims em 4 fontes):
  - NIST SP 800-53 Rev. 5 — 6 refs (`SP800-53-AU-2.3`, `SP800-53-CM-2.1`, `SP800-53-CM-3` + 2 more)
  - OWASP SAMM v2.1 — 6 refs (`SAMM-ACTIVITY-D_SA_2_B`, `SAMM-ACTIVITY-O_OM_3_B`, `SAMM-ACTIVITY-V_AA_1_A` + 2 more)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-GOVERN-1.5`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-3F63BDBCC75F4780A941E6AD42E894E1`)

#### `ACM-ATB-005` — Automated Topology Validation Jobs

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (22 grounded claims em 9 fontes):
  - NIST SP 800-53 Rev. 5 — 7 refs (`SP800-53-CA-5.1`, `SP800-53-CM-2.2`, `SP800-53-CM-3.2` + 2 more)
  - OWASP SAMM v2.1 — 4 refs (`SAMM-ACTIVITY-I_SB_2_A`, `SAMM-ACTIVITY-V_RT_2_A`, `SAMM-ACTIVITY-V_RT_2_B` + 1 more)
  - OWASP DSOMM — 3 refs (`DSOMM-ACTIVITY-67E1A9AA9FBF4EC5A2DE400F01960C51`, `DSOMM-ACTIVITY-017D9E2642B549A4B9459F59B308FB99`, `DSOMM-ACTIVITY-598897A2358E441F984CE12EC4F6110A`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.M0008`, `AML.M0033`)
  - OWASP MCP — Secure Server Development v1.0 — 2 refs (`OWASP-MCP-DATA-VALIDATION`, `OWASP-MCP-CONTINUOUS-VALIDATION`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-309`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-18.4`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C5`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-TESTING`)


---

## Slice `ACO-IAT` — Identidade, autenticação e gestão de sessões

### ControlObjectives (7)

#### `ACO-IAT-001` — Authentication Strength And Identity Assurance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (99 grounded claims em 15 fontes):
  - OWASP ASVS v5.0.0 — 22 refs (`ASVS-REQ-V6.1.1`, `ASVS-REQ-V6.3.1`, `ASVS-REQ-V6.3.3` + 2 more)
  - PCI DSS v4.0.1 — 16 refs (`PCI-REQ-4`, `PCI-REQ-8`, `PCI-4.2.1` + 2 more)
  - NIST SP 800-53 Rev. 5 — 12 refs (`SP800-53-AC-7`, `SP800-53-AC-7.4`, `SP800-53-IA-5.1` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 11 refs (`CWE-290`, `CWE-305`, `CWE-306` + 2 more)
  - MITRE CAPEC v3.9 — 10 refs (`CAPEC-2`, `CAPEC-16`, `CAPEC-36` + 2 more)
  - OWASP DSOMM — 9 refs (`DSOMM-ACTIVITY-03643CA203C2472B8E19956BF02FE9B7`, `DSOMM-ACTIVITY-FFE86CAF2FEC4630B5142DB83983984D`, `DSOMM-ACTIVITY-4CAE98C2416344EDBB883C67C569533A` + 2 more)
  - CIS Controls v8.1.2 — 6 refs (`CIS-4.1`, `CIS-5.2`, `CIS-6.3` + 2 more)
  - OWASP SAMM v2.1 — 3 refs (`SAMM-ACTIVITY-D_SR_1_A`, `SAMM-ACTIVITY-V_RT_1_A`, `SAMM-ACTIVITY-V_RT_3_B`)
  - HIPAA Security Rule — 2 refs (`HIPAA-164-308a5`, `HIPAA-164-312d`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0087`, `AML.CS0033`)
  - OWASP Top 10 (2021) — 2 refs (`TOP10-A02-2021`, `TOP10-A07-2021`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 1 refs (`NIST-AI-100-2-E2025-4.2.1`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP07-2025`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C1`)

#### `ACO-IAT-002` — Authorization Policy Integrity And Least Privilege

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (224 grounded claims em 19 fontes):
  - NIST SP 800-53 Rev. 5 — 122 refs (`SP800-53-AC-1`, `SP800-53-AC-2`, `SP800-53-AC-2.6` + 2 more)
  - PCI DSS v4.0.1 — 25 refs (`PCI-REQ-7`, `PCI-REQ-9`, `PCI-REQ-12` + 2 more)
  - MITRE CAPEC v3.9 — 15 refs (`CAPEC-1`, `CAPEC-13`, `CAPEC-17` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 12 refs (`CWE-1220`, `CWE-183`, `CWE-213` + 2 more)
  - CIS Controls v8.1.2 — 10 refs (`CIS-2.2`, `CIS-2.5`, `CIS-2.6` + 2 more)
  - OWASP ASVS v5.0.0 — 9 refs (`ASVS-REQ-V8.1.1`, `ASVS-REQ-V8.1.2`, `ASVS-REQ-V8.1.4` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 6 refs (`AML.TA0012`, `AML.T0054`, `AML.M0005` + 2 more)
  - OWASP LLM Top 10 (2025) — 4 refs (`LLM01-2025`, `LLM02-2025`, `LLM06-2025` + 1 more)
  - OWASP SAMM v2.1 — 3 refs (`SAMM-ACTIVITY-D_SA_3_B`, `SAMM-ACTIVITY-I_SD_1_A`, `SAMM-ACTIVITY-V_RT_3_B`)
  - PCI Secure SLC v1.1 — 3 refs (`PCISSLC-1.2`, `PCISSLC-2.2`, `PCISSLC-8.3`)
  - NIST SSDF (SP 800-218 v1.1) — 3 refs (`SSDF-PRACTICE-PO.4`, `SSDF-TASK-PS.1.1`, `SSDF-TASK-PW.1.2`)
  - Anthropic MCP — Official Security Foundations (2025) — 2 refs (`MCP-AUTH-DISCOVERY-METADATA`, `MCP-AUTH-SCOPE-NEGOTIATION`)
  - OWASP DSOMM — 2 refs (`DSOMM-ACTIVITY-82E499D1F4634A4BBE9068812A874AF6`, `DSOMM-ACTIVITY-070BB14BE04A4F3D896AA08EBA7A35F9`)
  - OWASP Machine Learning Top 10 — 2 refs (`ML06-2023`, `ML08-2023`)
  - SAFECode — Software Integrity Controls (2010) — 2 refs (`SCSIC-DEV-REPO`, `SCSIC-DEV-DEFAULTS`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-308a3`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C7`)
  - SLSA Specification v1.0 — Build Track — 1 refs (`SLSA-PRINCIPLE-PREFER-ATTESTATIONS`)

#### `ACO-IAT-003` — Access Revocation And Privilege Lifecycle Integrity

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (24 grounded claims em 7 fontes):
  - NIST SP 800-53 Rev. 5 — 16 refs (`SP800-53-AC-2`, `SP800-53-AC-2.3`, `SP800-53-AC-2.4` + 2 more)
  - MITRE CAPEC v3.9 — 2 refs (`CAPEC-447`, `CAPEC-675`)
  - CIS Controls v8.1.2 — 2 refs (`CIS-6`, `CIS-6.2`)
  - OWASP ASVS v5.0.0 — 1 refs (`ASVS-REQ-V10.4.9`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-308a4`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-6.5.6`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-6.1`)

#### `ACO-IAT-004` — Session And Token Trust Boundaries

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (47 grounded claims em 8 fontes):
  - OWASP ASVS v5.0.0 — 21 refs (`ASVS-REQ-V4.4.3`, `ASVS-REQ-V4.4.4`, `ASVS-REQ-V7.1.1` + 2 more)
  - MITRE CAPEC v3.9 — 10 refs (`CAPEC-31`, `CAPEC-39`, `CAPEC-59` + 2 more)
  - NIST SP 800-53 Rev. 5 — 6 refs (`SP800-53-IA-13.3`, `SP800-53-SC-12.5`, `SP800-53-SC-23` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 3 refs (`CWE-488`, `CWE-565`, `CWE-613`)
  - Anthropic MCP — Official Security Foundations (2025) — 2 refs (`MCP-TOKEN-PASSTHROUGH`, `MCP-SESSION-HIJACKING`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0080.000`, `AML.CS0040`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 2 refs (`MCP01-2025`, `MCP10-2025`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-4.3`)

#### `ACO-IAT-005` — API Caller Trust And Service Boundary Enforcement

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (19 grounded claims em 4 fontes):
  - OWASP ASVS v5.0.0 — 10 refs (`ASVS-REQ-V2.2.2`, `ASVS-REQ-V3.5.1`, `ASVS-REQ-V4.1.2` + 2 more)
  - NIST SP 800-53 Rev. 5 — 7 refs (`SP800-53-SA-8.10`, `SP800-53-SA-9.3`, `SP800-53-SA-10.4` + 2 more)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-461`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-017D9E2642B549A4B9459F59B308FB99`)

#### `ACO-IAT-006` — Access Abuse Detection And Auditability

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (167 grounded claims em 20 fontes):
  - NIST SP 800-53 Rev. 5 — 81 refs (`SP800-53-AC-1`, `SP800-53-AC-2.12`, `SP800-53-AC-8` + 2 more)
  - PCI DSS v4.0.1 — 22 refs (`PCI-2.3.2`, `PCI-8.2.7`, `PCI-9.2.2` + 2 more)
  - MITRE CAPEC v3.9 — 11 refs (`CAPEC-5`, `CAPEC-54`, `CAPEC-69` + 2 more)
  - OWASP DSOMM — 10 refs (`DSOMM-ACTIVITY-BACF85B65BC0405DB5BAA5D971467CC1`, `DSOMM-ACTIVITY-0A929C3EAB9A42068761ADF84B74622E`, `DSOMM-ACTIVITY-6DF508EF86FC4C22BD9F646C3127CE7D` + 2 more)
  - CIS Controls v8.1.2 — 8 refs (`CIS-8`, `CIS-8.1`, `CIS-8.3` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 7 refs (`AML.TA0011`, `AML.T0006`, `AML.T0049` + 2 more)
  - OWASP SAMM v2.1 — 6 refs (`SAMM-ACTIVITY-O_IM_1_A`, `SAMM-ACTIVITY-O_IM_1_B`, `SAMM-ACTIVITY-O_IM_2_A` + 2 more)
  - OWASP ASVS v5.0.0 — 3 refs (`ASVS-REQ-V2.4.1`, `ASVS-REQ-V16.3.3`, `ASVS-REQ-V16.4.3`)
  - OWASP Machine Learning Top 10 — 3 refs (`ML02-2023`, `ML07-2023`, `ML08-2023`)
  - EU Digital Operational Resilience Act (DORA) — 2 refs (`DORA-ART-5`, `DORA-ART-10`)
  - HIPAA Security Rule — 2 refs (`HIPAA-164-308a1`, `HIPAA-164-308a6`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 2 refs (`NIST-AI-100-2-E2025-3.3.3`, `NIST-AI-100-2-E2025-3.4.1`)
  - PCI Secure SLC v1.1 — 2 refs (`PCISSLC-2.1`, `PCISSLC-3.2`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 2 refs (`SCFPSSD-LOGGING`, `SCFPSSD-FINDINGS`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-779`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-32`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-DATA-VALIDATION`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP08-2025`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C9`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A09-2021`)

#### `ACO-IAT-007` — Identity And Access Control Integrity

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (57 grounded claims em 9 fontes):
  - NIST SP 800-53 Rev. 5 — 28 refs (`SP800-53-AC-4.17`, `SP800-53-AC-17.2`, `SP800-53-AC-19.5` + 2 more)
  - OWASP ASVS v5.0.0 — 11 refs (`ASVS-REQ-V6.8.1`, `ASVS-REQ-V8.4.2`, `ASVS-REQ-V10.1.2` + 2 more)
  - MITRE CAPEC v3.9 — 7 refs (`CAPEC-113`, `CAPEC-277`, `CAPEC-523` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 4 refs (`AML.T0021`, `AML.T0073`, `AML.T0083` + 1 more)
  - MITRE CWE — Software Development View (v4.19.1) — 3 refs (`CWE-289`, `CWE-322`, `CWE-649`)
  - OWASP MCP — Third-Party Servers v1.0 — 1 refs (`OWASP-MCP-3P-TOOLS-UTILITIES`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C6`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-IAM`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-SOURCING-TRANSFER`)


### Practices (6)

#### `ACP-IAT-001` — Strong Authentication And Step-Up Enforcement

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (178 grounded claims em 17 fontes):
  - NIST SP 800-53 Rev. 5 — 64 refs (`SP800-53-AC-7`, `SP800-53-AC-7.3`, `SP800-53-AC-7.4` + 2 more)
  - OWASP ASVS v5.0.0 — 29 refs (`ASVS-REQ-V6.1.1`, `ASVS-REQ-V6.1.3`, `ASVS-REQ-V6.2.10` + 2 more)
  - MITRE CAPEC v3.9 — 26 refs (`CAPEC-2`, `CAPEC-16`, `CAPEC-36` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 16 refs (`CWE-1392`, `CWE-290`, `CWE-303` + 2 more)
  - PCI DSS v4.0.1 — 16 refs (`PCI-REQ-4`, `PCI-REQ-8`, `PCI-4.2.1` + 2 more)
  - CIS Controls v8.1.2 — 7 refs (`CIS-4.1`, `CIS-5.2`, `CIS-6.3` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 4 refs (`AML.TA0012`, `AML.TA0013`, `AML.T0087` + 1 more)
  - OWASP DSOMM — 3 refs (`DSOMM-ACTIVITY-8098E416E1ED4AE4A56183EFBE76BF57`, `DSOMM-ACTIVITY-598E9F131AC84A01B85E8FAB93EE81DE`, `DSOMM-ACTIVITY-61E10F9CE1264FFAAF12FDBE0D0A831F`)
  - OWASP SAMM v2.1 — 3 refs (`SAMM-ACTIVITY-D_SA_1_A`, `SAMM-ACTIVITY-I_SD_3_B`, `SAMM-ACTIVITY-V_RT_3_B`)
  - HIPAA Security Rule — 2 refs (`HIPAA-164-312c1`, `HIPAA-164-312d`)
  - NIST SSDF (SP 800-218 v1.1) — 2 refs (`SSDF-PRACTICE-PS.1`, `SSDF-TASK-PW.9.1`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 1 refs (`NIST-AI-100-2-E2025-4.2.1`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-MINIMUM-BAR`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP07-2025`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A07-2021`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-OPS-16`)

#### `ACP-IAT-002` — Least-Privilege Authorization Governance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (162 grounded claims em 20 fontes):
  - NIST SP 800-53 Rev. 5 — 98 refs (`SP800-53-AC-1`, `SP800-53-AC-2`, `SP800-53-AC-2.1` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 11 refs (`CWE-1220`, `CWE-183`, `CWE-250` + 2 more)
  - CIS Controls v8.1.2 — 10 refs (`CIS-2.2`, `CIS-2.6`, `CIS-2.7` + 2 more)
  - MITRE CAPEC v3.9 — 8 refs (`CAPEC-1`, `CAPEC-13`, `CAPEC-69` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 8 refs (`AML.TA0012`, `AML.T0017`, `AML.T0054` + 2 more)
  - OWASP LLM Top 10 (2025) — 4 refs (`LLM01-2025`, `LLM02-2025`, `LLM06-2025` + 1 more)
  - OWASP ASVS v5.0.0 — 3 refs (`ASVS-REQ-V8.1.2`, `ASVS-REQ-V8.2.3`, `ASVS-REQ-V13.3.2`)
  - PCI DSS v4.0.1 — 3 refs (`PCI-6.5.4`, `PCI-7.2.1`, `PCI-8.2.2`)
  - PCI Secure SLC v1.1 — 3 refs (`PCISSLC-1.1`, `PCISSLC-1.2`, `PCISSLC-3.2`)
  - NIST AI RMF 1.0 — 2 refs (`NIST-AI-RMF-GOVERN-1`, `NIST-AI-RMF-GOVERN-2`)
  - OWASP Machine Learning Top 10 — 2 refs (`ML06-2023`, `ML08-2023`)
  - OWASP SAMM v2.1 — 2 refs (`SAMM-ACTIVITY-G_EG_2_A`, `SAMM-ACTIVITY-I_SD_1_A`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-308a2`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-070BB14BE04A4F3D896AA08EBA7A35F9`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-GOVERNANCE`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP02-2025`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C7`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEV-REPO`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PS.1.1`)

#### `ACP-IAT-003` — Access Review And Timely Revocation

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (16 grounded claims em 5 fontes):
  - NIST SP 800-53 Rev. 5 — 9 refs (`SP800-53-AC-1`, `SP800-53-AC-2`, `SP800-53-AC-3.8` + 2 more)
  - OWASP ASVS v5.0.0 — 2 refs (`ASVS-REQ-V10.4.9`, `ASVS-REQ-V12.1.4`)
  - CIS Controls v8.1.2 — 2 refs (`CIS-5.5`, `CIS-6.6`)
  - HIPAA Security Rule — 2 refs (`HIPAA-164-308a4`, `HIPAA-164-312a1`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-359`)

#### `ACP-IAT-004` — Bounded Session And Token Management

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (46 grounded claims em 9 fontes):
  - OWASP ASVS v5.0.0 — 14 refs (`ASVS-REQ-V4.4.3`, `ASVS-REQ-V4.4.4`, `ASVS-REQ-V7.1.3` + 2 more)
  - NIST SP 800-53 Rev. 5 — 11 refs (`SP800-53-AC-10`, `SP800-53-AC-12`, `SP800-53-AC-12.1` + 2 more)
  - MITRE CAPEC v3.9 — 10 refs (`CAPEC-21`, `CAPEC-39`, `CAPEC-59` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 3 refs (`CWE-312`, `CWE-488`, `CWE-613`)
  - Anthropic MCP — Official Security Foundations (2025) — 2 refs (`MCP-SESSION-HIJACKING`, `MCP-SCOPE-MINIMIZATION`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0080.000`, `AML.CS0036`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 2 refs (`MCP01-2025`, `MCP10-2025`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-4.3`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM02-2025`)

#### `ACP-IAT-005` — Authenticated API Boundary Enforcement

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (93 grounded claims em 10 fontes):
  - OWASP ASVS v5.0.0 — 35 refs (`ASVS-REQ-V1.3.6`, `ASVS-REQ-V2.2.2`, `ASVS-REQ-V3.5.1` + 2 more)
  - MITRE CAPEC v3.9 — 17 refs (`CAPEC-8`, `CAPEC-14`, `CAPEC-36` + 2 more)
  - NIST SP 800-53 Rev. 5 — 17 refs (`SP800-53-AC-4.7`, `SP800-53-AC-4.29`, `SP800-53-SA-5.2` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 10 refs (`AML.T0040`, `AML.T0011.000`, `AML.T0008.004` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 4 refs (`CWE-204`, `CWE-551`, `CWE-648` + 1 more)
  - OWASP DSOMM — 3 refs (`DSOMM-ACTIVITY-29318D6018CE452680EAF5928E49F639`, `DSOMM-ACTIVITY-65A2D7D9544146BFA4E3F76919857750`, `DSOMM-ACTIVITY-017D9E2642B549A4B9459F59B308FB99`)
  - Anthropic MCP — Official Security Foundations (2025) — 2 refs (`MCP-AUTH-ERROR-HANDLING`, `MCP-CONFUSED-DEPUTY`)
  - OWASP MCP — Third-Party Servers v1.0 — 2 refs (`OWASP-MCP-3P-CLIENT-SECURITY-DISCOVERY`, `OWASP-MCP-3P-TOOLS-UTILITIES`)
  - OWASP SAMM v2.1 — 2 refs (`SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-V_AA_2_A`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-1.4.2`)

#### `ACP-IAT-006` — Access Abuse Monitoring And Audit Trail

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (333 grounded claims em 24 fontes):
  - NIST SP 800-53 Rev. 5 — 136 refs (`SP800-53-AC-2`, `SP800-53-AC-2.4`, `SP800-53-AC-2.12` + 2 more)
  - PCI DSS v4.0.1 — 41 refs (`PCI-REQ-11`, `PCI-1.1.1`, `PCI-1.2.4` + 2 more)
  - CIS Controls v8.1.2 — 38 refs (`CIS-1`, `CIS-2.3`, `CIS-3` + 2 more)
  - OWASP SAMM v2.1 — 31 refs (`SAMM-ACTIVITY-D_SA_1_B`, `SAMM-ACTIVITY-D_SR_1_B`, `SAMM-ACTIVITY-D_TA_1_A` + 2 more)
  - OWASP DSOMM — 16 refs (`DSOMM-ACTIVITY-BACF85B65BC0405DB5BAA5D971467CC1`, `DSOMM-ACTIVITY-0A929C3EAB9A42068761ADF84B74622E`, `DSOMM-ACTIVITY-535F301AE8E84EDAAD77A08B035C92DE` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 12 refs (`SSDF-PRACTICE-PO.4`, `SSDF-PRACTICE-PW.1`, `SSDF-PRACTICE-PW.2` + 2 more)
  - MITRE CAPEC v3.9 — 10 refs (`CAPEC-54`, `CAPEC-69`, `CAPEC-93` + 2 more)
  - OWASP ASVS v5.0.0 — 9 refs (`ASVS-REQ-V14.2.7`, `ASVS-REQ-V16.1.1`, `ASVS-REQ-V16.2.1` + 2 more)
  - PCI Secure SLC v1.1 — 7 refs (`PCISSLC-2.1`, `PCISSLC-2.4`, `PCISSLC-2.5` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 6 refs (`AML.TA0011`, `AML.T0003`, `AML.T0006` + 2 more)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 5 refs (`SCAGILE-OPS-1`, `SCAGILE-OPS-2`, `SCAGILE-OPS-7` + 2 more)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 4 refs (`SCFPSSD-LOGGING`, `SCFPSSD-CODING-STANDARDS`, `SCFPSSD-FINDINGS` + 1 more)
  - EU Digital Operational Resilience Act (DORA) — 3 refs (`DORA-ART-5`, `DORA-ART-9`, `DORA-ART-10`)
  - HIPAA Security Rule — 3 refs (`HIPAA-164-308a1`, `HIPAA-164-308a6`, `HIPAA-164-312b`)
  - OWASP Machine Learning Top 10 — 3 refs (`ML02-2023`, `ML07-2023`, `ML08-2023`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-779`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-32`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 1 refs (`NIST-AI-100-2-E2025-3.3.3`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM08-2025`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP08-2025`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C9`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A09-2021`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEV-TESTING`)


### Mechanisms (6)

#### `ACM-IAT-001` — Authentication And Federation Protocols

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (90 grounded claims em 14 fontes):
  - NIST SP 800-53 Rev. 5 — 41 refs (`SP800-53-AC-7.4`, `SP800-53-CP-13`, `SP800-53-IA-1` + 2 more)
  - OWASP ASVS v5.0.0 — 16 refs (`ASVS-REQ-V6.3.3`, `ASVS-REQ-V6.3.5`, `ASVS-REQ-V6.3.7` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 10 refs (`CWE-1392`, `CWE-294`, `CWE-301` + 2 more)
  - MITRE CAPEC v3.9 — 5 refs (`CAPEC-90`, `CAPEC-151`, `CAPEC-220` + 2 more)
  - CIS Controls v8.1.2 — 5 refs (`CIS-3.1`, `CIS-4.9`, `CIS-12.6` + 2 more)
  - OWASP DSOMM — 3 refs (`DSOMM-ACTIVITY-8098E416E1ED4AE4A56183EFBE76BF57`, `DSOMM-ACTIVITY-AD23BE9C56614F1F81A35A5DC7061629`, `DSOMM-ACTIVITY-598E9F131AC84A01B85E8FAB93EE81DE`)
  - PCI DSS v4.0.1 — 3 refs (`PCI-REQ-4`, `PCI-4.2.1`, `PCI-8.3.11`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-312d`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.T0091`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-AUTH`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP07-2025`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C6`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A07-2021`)

#### `ACM-IAT-002` — Access Policy Enforcement

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (422 grounded claims em 24 fontes):
  - NIST SP 800-53 Rev. 5 — 198 refs (`SP800-53-AC-1`, `SP800-53-AC-2`, `SP800-53-AC-2.1` + 2 more)
  - MITRE CAPEC v3.9 — 44 refs (`CAPEC-1`, `CAPEC-8`, `CAPEC-9` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 34 refs (`AML.TA0000`, `AML.TA0012`, `AML.T0016` + 2 more)
  - PCI DSS v4.0.1 — 34 refs (`PCI-REQ-7`, `PCI-REQ-9`, `PCI-1.5.1` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 19 refs (`CWE-1220`, `CWE-1230`, `CWE-183` + 2 more)
  - CIS Controls v8.1.2 — 17 refs (`CIS-2.2`, `CIS-2.5`, `CIS-2.6` + 2 more)
  - OWASP ASVS v5.0.0 — 16 refs (`ASVS-REQ-V1.5.2`, `ASVS-REQ-V2.3.5`, `ASVS-REQ-V2.4.1` + 2 more)
  - OWASP DSOMM — 12 refs (`DSOMM-ACTIVITY-72737130472C498480F89AB2F1C2ED5D`, `DSOMM-ACTIVITY-B597928E54D648A5A8068003DCD56AAB`, `DSOMM-ACTIVITY-CF81922530CB47028E3260225EEDC33D` + 2 more)
  - HIPAA Security Rule — 8 refs (`HIPAA-164-308a2`, `HIPAA-164-308a3`, `HIPAA-164-308a4` + 2 more)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 7 refs (`NIST-AI-100-2-E2025-2.1`, `NIST-AI-100-2-E2025-3.1.2`, `NIST-AI-100-2-E2025-3.1.3` + 2 more)
  - OWASP Machine Learning Top 10 — 6 refs (`ML02-2023`, `ML03-2023`, `ML05-2023` + 2 more)
  - OWASP SAMM v2.1 — 6 refs (`SAMM-ACTIVITY-D_SA_1_A`, `SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-D_SA_3_B` + 2 more)
  - OWASP LLM Top 10 (2025) — 5 refs (`LLM01-2025`, `LLM02-2025`, `LLM03-2025` + 2 more)
  - PCI Secure SLC v1.1 — 5 refs (`PCISSLC-1.2`, `PCISSLC-2.2`, `PCISSLC-3.3` + 2 more)
  - OWASP Proactive Controls (2018) — 2 refs (`OPC-C2`, `OPC-C7`)
  - EU Digital Operational Resilience Act (DORA) — 1 refs (`DORA-ART-9`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - Anthropic MCP — Official Security Foundations (2025) — 1 refs (`MCP-AUTH-ERROR-HANDLING`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-GOVERN-1`)
  - OWASP MCP — Third-Party Servers v1.0 — 1 refs (`OWASP-MCP-3P-CLIENT-SECURITY-DISCOVERY`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP02-2025`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A01-2021`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEV-REPO`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-PRACTICE-PS.1`)

#### `ACM-IAT-003` — Periodic Review And Access Audit

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (54 grounded claims em 9 fontes):
  - NIST SP 800-53 Rev. 5 — 38 refs (`SP800-53-AC-2`, `SP800-53-AC-2.4`, `SP800-53-AC-4.9` + 2 more)
  - OWASP SAMM v2.1 — 5 refs (`SAMM-ACTIVITY-D_SA_2_B`, `SAMM-ACTIVITY-G_EG_3_A`, `SAMM-ACTIVITY-G_PC_2_B` + 2 more)
  - CIS Controls v8.1.2 — 4 refs (`CIS-5.5`, `CIS-6.2`, `CIS-6.8` + 1 more)
  - HIPAA Security Rule — 2 refs (`HIPAA-164-308a8`, `HIPAA-164-312b`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-GOVERN-1.5`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-3F63BDBCC75F4780A941E6AD42E894E1`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML07-2023`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-12.10.2`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-2.1`)

#### `ACM-IAT-004` — Short-Lived Token Controls

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (25 grounded claims em 7 fontes):
  - MITRE CAPEC v3.9 — 9 refs (`CAPEC-39`, `CAPEC-59`, `CAPEC-60` + 2 more)
  - OWASP ASVS v5.0.0 — 6 refs (`ASVS-REQ-V7.2.3`, `ASVS-REQ-V7.2.4`, `ASVS-REQ-V7.4.1` + 2 more)
  - NIST SP 800-53 Rev. 5 — 5 refs (`SP800-53-AC-12`, `SP800-53-AC-12.1`, `SP800-53-SC-23.1` + 2 more)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 2 refs (`MCP01-2025`, `MCP10-2025`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-565`)
  - Anthropic MCP — Official Security Foundations (2025) — 1 refs (`MCP-SESSION-HIJACKING`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM02-2025`)

#### `ACM-IAT-005` — API Gateway Mutual Authentication

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 4 keywords × 35 ocorrências; principais: boundaries, gateway, identity, service)
- **Substrate v7 contributing sources** (31 grounded claims em 6 fontes):
  - OWASP ASVS v5.0.0 — 23 refs (`ASVS-REQ-V4.1.2`, `ASVS-REQ-V4.1.3`, `ASVS-REQ-V4.1.4` + 2 more)
  - NIST SP 800-53 Rev. 5 — 3 refs (`SP800-53-IA-2.11`, `SP800-53-SA-9.3`, `SP800-53-SC-7.8`)
  - MITRE CAPEC v3.9 — 2 refs (`CAPEC-384`, `CAPEC-461`)
  - Anthropic MCP — Official Security Foundations (2025) — 1 refs (`MCP-CONFUSED-DEPUTY`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-D_SA_2_A`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-1.4.2`)

#### `ACM-IAT-006` — Structured Logging And Effective Configuration Recording

- **Manual prose:** cobertura **cross-chapter** — content encontrado em Cap. 03 (`03-threat-modeling`), Cap. 12 (`12-monitorizacao-operacoes`), Cap. 14 (`14-governanca-contratacao`). Cap. expected (04-arquitetura-segura) tem cobertura fraca; ler em chapter(s) listada(s).
- **Substrate v7 contributing sources** (316 grounded claims em 22 fontes):
  - NIST SP 800-53 Rev. 5 — 130 refs (`SP800-53-AU-2`, `SP800-53-AU-4.1`, `SP800-53-AU-5.4` + 2 more)
  - OWASP SAMM v2.1 — 34 refs (`SAMM-ACTIVITY-D_SA_1_B`, `SAMM-ACTIVITY-D_SA_3_B`, `SAMM-ACTIVITY-D_SR_1_B` + 2 more)
  - PCI DSS v4.0.1 — 34 refs (`PCI-REQ-10`, `PCI-1.1.1`, `PCI-1.1.2` + 2 more)
  - CIS Controls v8.1.2 — 28 refs (`CIS-1`, `CIS-3.1`, `CIS-3.13` + 2 more)
  - OWASP DSOMM — 19 refs (`DSOMM-ACTIVITY-67E1A9AA9FBF4EC5A2DE400F01960C51`, `DSOMM-ACTIVITY-994151396B50441B89E10AA59ACCD43D`, `DSOMM-ACTIVITY-C72DA77986CC45B1A339190CE5093171` + 2 more)
  - MITRE CAPEC v3.9 — 18 refs (`CAPEC-75`, `CAPEC-81`, `CAPEC-93` + 2 more)
  - OWASP ASVS v5.0.0 — 16 refs (`ASVS-REQ-V15.1.2`, `ASVS-REQ-V15.1.5`, `ASVS-REQ-V16.1.1` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 12 refs (`SSDF-PRACTICE-PO.3`, `SSDF-PRACTICE-PS.2`, `SSDF-TASK-PO.1.2` + 2 more)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 6 refs (`SCAGILE-OPS-2`, `SCAGILE-OPS-5`, `SCAGILE-OPS-6` + 2 more)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 4 refs (`SCFPSSD-LOGGING`, `SCFPSSD-CODING-STANDARDS`, `SCFPSSD-VULN-RESPONSE` + 1 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 3 refs (`AML.T0037`, `AML.T0049`, `AML.M0024`)
  - EU Digital Operational Resilience Act (DORA) — 2 refs (`DORA-ART-5`, `DORA-ART-12`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-779`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-32`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-316b1`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM10-2025`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP08-2025`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C9`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A09-2021`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-3.2`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEV-BUILD`)


---

## Slice `ACO-ITS` — Integração e segurança service-to-service

### ControlObjectives (7)

#### `ACO-ITS-001` — Authenticated Service Interaction And Machine Identity Binding

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (76 grounded claims em 11 fontes):
  - NIST SP 800-53 Rev. 5 — 37 refs (`SP800-53-AC-2`, `SP800-53-AC-4.17`, `SP800-53-AC-17.10` + 2 more)
  - OWASP ASVS v5.0.0 — 8 refs (`ASVS-REQ-V6.3.3`, `ASVS-REQ-V6.6.1`, `ASVS-REQ-V7.1.3` + 2 more)
  - MITRE CAPEC v3.9 — 8 refs (`CAPEC-21`, `CAPEC-36`, `CAPEC-196` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 7 refs (`CWE-1392`, `CWE-289`, `CWE-301` + 2 more)
  - CIS Controls v8.1.2 — 5 refs (`CIS-6.4`, `CIS-6.6`, `CIS-12.5` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 5 refs (`AML.T0090`, `AML.T0091`, `AML.T0091.000` + 2 more)
  - OWASP MCP — Third-Party Servers v1.0 — 2 refs (`OWASP-MCP-3P-AUTH-AUTHZ-REGISTRATION`, `OWASP-MCP-3P-TOOLS-UTILITIES`)
  - Anthropic MCP — Official Security Foundations (2025) — 1 refs (`MCP-CONFUSED-DEPUTY`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-AUTH`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP07-2025`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C6`)

#### `ACO-ITS-002` — Secure Transport And Insecure Protocol Exclusion

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (140 grounded claims em 12 fontes):
  - NIST SP 800-53 Rev. 5 — 96 refs (`SP800-53-AC-3.3`, `SP800-53-AC-3.5`, `SP800-53-AC-4.1` + 2 more)
  - PCI DSS v4.0.1 — 18 refs (`PCI-REQ-2`, `PCI-REQ-4`, `PCI-1.2.3` + 2 more)
  - OWASP DSOMM — 5 refs (`DSOMM-ACTIVITY-72737130472C498480F89AB2F1C2ED5D`, `DSOMM-ACTIVITY-29318D6018CE452680EAF5928E49F639`, `DSOMM-ACTIVITY-AD23BE9C56614F1F81A35A5DC7061629` + 2 more)
  - OWASP ASVS v5.0.0 — 4 refs (`ASVS-REQ-V3.4.1`, `ASVS-REQ-V12.1.2`, `ASVS-REQ-V12.2.1` + 1 more)
  - MITRE CAPEC v3.9 — 4 refs (`CAPEC-157`, `CAPEC-390`, `CAPEC-582` + 1 more)
  - CIS Controls v8.1.2 — 4 refs (`CIS-3.1`, `CIS-4.6`, `CIS-12.3` + 1 more)
  - HIPAA Security Rule — 3 refs (`HIPAA-164-310a1`, `HIPAA-164-310c`, `HIPAA-164-312e1`)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-420`, `CWE-654`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-ARCH`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C1`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A02-2021`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-ENCRYPTION`)

#### `ACO-ITS-003` — Message Integrity And Authorized Peer Validation

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (142 grounded claims em 20 fontes):
  - NIST SP 800-53 Rev. 5 — 52 refs (`SP800-53-AC-3.12`, `SP800-53-AC-4.19`, `SP800-53-AC-17.6` + 2 more)
  - OWASP ASVS v5.0.0 — 25 refs (`ASVS-REQ-V1.5.2`, `ASVS-REQ-V2.3.5`, `ASVS-REQ-V3.5.5` + 2 more)
  - MITRE CAPEC v3.9 — 19 refs (`CAPEC-12`, `CAPEC-22`, `CAPEC-145` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 16 refs (`CWE-179`, `CWE-209`, `CWE-212` + 2 more)
  - PCI DSS v4.0.1 — 7 refs (`PCI-1.2.2`, `PCI-7.2.2`, `PCI-7.2.3` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 5 refs (`AML.T0042`, `AML.T0067`, `AML.M0013` + 2 more)
  - OWASP Machine Learning Top 10 — 2 refs (`ML06-2023`, `ML08-2023`)
  - PCI Secure SLC v1.1 — 2 refs (`PCISSLC-6.1`, `PCISSLC-6.2`)
  - SAFECode — Software Integrity Controls (2010) — 2 refs (`SCSIC-DEV-TESTING`, `SCSIC-DELIVERY`)
  - NIST SSDF (SP 800-218 v1.1) — 2 refs (`SSDF-PRACTICE-PS.2`, `SSDF-TASK-PS.2.1`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-18.4`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-32`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-312c1`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 1 refs (`NIST-AI-100-2-E2025-3.4.2`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-3F63BDBCC75F4780A941E6AD42E894E1`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM04-2025`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-GOVERNANCE`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A08-2021`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-OPS-7`)
  - SLSA Specification v1.0 — Build Track — 1 refs (`SLSA-PRINCIPLE-TRUST-CODE`)

#### `ACO-ITS-004` — Boundary-Mediated External Exposure And Integration Path Control

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (4 grounded claims em 3 fontes):
  - NIST SP 800-53 Rev. 5 — 2 refs (`SP800-53-MP-5.1`, `SP800-53-PE-3`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-433`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-73`)

#### `ACO-ITS-005` — Integration Security Review And Contract Assurance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (33 grounded claims em 13 fontes):
  - CIS Controls v8.1.2 — 7 refs (`CIS-4`, `CIS-4.1`, `CIS-4.2` + 2 more)
  - NIST SP 800-53 Rev. 5 — 6 refs (`SP800-53-CA-3`, `SP800-53-CA-4`, `SP800-53-CM-5.7` + 2 more)
  - OWASP SAMM v2.1 — 6 refs (`SAMM-ACTIVITY-D_SR_1_B`, `SAMM-ACTIVITY-D_SR_2_B`, `SAMM-ACTIVITY-G_PC_3_B` + 2 more)
  - HIPAA Security Rule — 3 refs (`HIPAA-164-308a1`, `HIPAA-164-308b1`, `HIPAA-164-314a1`)
  - OWASP DSOMM — 2 refs (`DSOMM-ACTIVITY-F57D55F2DC054B349D1FF8CE5BFB0715`, `DSOMM-ACTIVITY-AAFFA73F59F64267B0AB732F3D13E90D`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 2 refs (`SCAGILE-EXP-2`, `SCAGILE-EXP-8`)
  - OWASP ASVS v5.0.0 — 1 refs (`ASVS-REQ-V15.1.2`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-18`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-22`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-TOOL-DESIGN`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-8.1`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-FINDINGS`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-SOURCING-CONTRACT`)

#### `ACO-ITS-006` — External Interaction Auditability

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (48 grounded claims em 8 fontes):
  - NIST SP 800-53 Rev. 5 — 29 refs (`SP800-53-AU-2`, `SP800-53-AU-2.2`, `SP800-53-AU-2.3` + 2 more)
  - OWASP ASVS v5.0.0 — 5 refs (`ASVS-REQ-V13.4.5`, `ASVS-REQ-V16.1.1`, `ASVS-REQ-V16.2.3` + 2 more)
  - OWASP DSOMM — 4 refs (`DSOMM-ACTIVITY-E9A6D403A467445EB98A74F0C29DA0B1`, `DSOMM-ACTIVITY-1CD5E4B8BE364726ADC7D8F843F47AC8`, `DSOMM-ACTIVITY-D03BC41074A74E9282CBD01A020CB6BF` + 1 more)
  - PCI DSS v4.0.1 — 4 refs (`PCI-10.3.3`, `PCI-10.4.2`, `PCI-11.3.2` + 1 more)
  - CIS Controls v8.1.2 — 3 refs (`CIS-1`, `CIS-8.1`, `CIS-8.7`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-749`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP08-2025`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-LOGGING`)

#### `ACO-ITS-007` — Integration Trust And Service Interaction Assurance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (18 grounded claims em 6 fontes):
  - NIST SP 800-53 Rev. 5 — 11 refs (`SP800-53-CA-6.1`, `SP800-53-CA-6.2`, `SP800-53-CA-9` + 2 more)
  - OWASP ASVS v5.0.0 — 3 refs (`ASVS-REQ-V8.4.2`, `ASVS-REQ-V12.2.2`, `ASVS-REQ-V12.3.4`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-677`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MEASURE-4`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-12.8.1`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-3.2`)


### Practices (6)

#### `ACP-ITS-001` — Trust Boundary And Integration Review

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (6 grounded claims em 5 fontes):
  - OWASP SAMM v2.1 — 2 refs (`SAMM-ACTIVITY-G_EG_2_A`, `SAMM-ACTIVITY-G_SM_1_A`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.T0054`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MEASURE-4`)
  - NIST SP 800-53 Rev. 5 — 1 refs (`SP800-53-SA-13`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-3.2`)

#### `ACP-ITS-002` — Machine Identity And Mutual Authentication Discipline

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (69 grounded claims em 10 fontes):
  - NIST SP 800-53 Rev. 5 — 32 refs (`SP800-53-AC-3.2`, `SP800-53-AC-17.10`, `SP800-53-AU-10.1` + 2 more)
  - OWASP ASVS v5.0.0 — 10 refs (`ASVS-REQ-V6.3.3`, `ASVS-REQ-V6.5.3`, `ASVS-REQ-V6.8.4` + 2 more)
  - MITRE CAPEC v3.9 — 10 refs (`CAPEC-21`, `CAPEC-36`, `CAPEC-59` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 7 refs (`AML.T0012`, `AML.T0083`, `AML.T0090` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 4 refs (`CWE-289`, `CWE-306`, `CWE-308` + 1 more)
  - OWASP DSOMM — 2 refs (`DSOMM-ACTIVITY-8098E416E1ED4AE4A56183EFBE76BF57`, `DSOMM-ACTIVITY-598E9F131AC84A01B85E8FAB93EE81DE`)
  - Anthropic MCP — Official Security Foundations (2025) — 1 refs (`MCP-CONFUSED-DEPUTY`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP07-2025`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C6`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A07-2021`)

#### `ACP-ITS-003` — Transport And Protocol Hardening

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (224 grounded claims em 19 fontes):
  - NIST SP 800-53 Rev. 5 — 118 refs (`SP800-53-AC-3.5`, `SP800-53-AC-3.6`, `SP800-53-AC-4.1` + 2 more)
  - PCI DSS v4.0.1 — 25 refs (`PCI-REQ-2`, `PCI-1.1.1`, `PCI-1.2.5` + 2 more)
  - MITRE CAPEC v3.9 — 17 refs (`CAPEC-36`, `CAPEC-57`, `CAPEC-89` + 2 more)
  - CIS Controls v8.1.2 — 12 refs (`CIS-3.1`, `CIS-4`, `CIS-4.1` + 2 more)
  - OWASP SAMM v2.1 — 11 refs (`SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-D_SA_3_B`, `SAMM-ACTIVITY-I_DM_1_A` + 2 more)
  - OWASP DSOMM — 10 refs (`DSOMM-ACTIVITY-72737130472C498480F89AB2F1C2ED5D`, `DSOMM-ACTIVITY-03643CA203C2472B8E19956BF02FE9B7`, `DSOMM-ACTIVITY-FFE86CAF2FEC4630B5142DB83983984D` + 2 more)
  - PCI Secure SLC v1.1 — 6 refs (`PCISSLC-2.3`, `PCISSLC-5.1`, `PCISSLC-8.1` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 5 refs (`SSDF-PRACTICE-PO.5`, `SSDF-PRACTICE-PW.4`, `SSDF-PRACTICE-PW.9` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 4 refs (`CWE-1220`, `CWE-212`, `CWE-213` + 1 more)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 3 refs (`SCAGILE-EXP-8`, `SCAGILE-EXP-11`, `SCAGILE-EXP-12`)
  - OWASP ASVS v5.0.0 — 2 refs (`ASVS-REQ-V3.4.1`, `ASVS-REQ-V17.2.1`)
  - EU Cyber Resilience Act (CRA) — 2 refs (`CRA-ART-18`, `CRA-ART-19`)
  - HIPAA Security Rule — 2 refs (`HIPAA-164-308a6`, `HIPAA-164-312e1`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 2 refs (`SCFPSSD-DESIGN-PRINCIPLES`, `SCFPSSD-ENCRYPTION`)
  - EU Digital Operational Resilience Act (DORA) — 1 refs (`DORA-ART-9`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-DEPLOYMENT`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML06-2023`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEV-DEFAULTS`)

#### `ACP-ITS-004` — Message Integrity And Authorized Peer Validation

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (129 grounded claims em 14 fontes):
  - NIST SP 800-53 Rev. 5 — 62 refs (`SP800-53-AC-4.19`, `SP800-53-AC-22`, `SP800-53-AU-5.3` + 2 more)
  - OWASP ASVS v5.0.0 — 29 refs (`ASVS-REQ-V2.2.2`, `ASVS-REQ-V2.3.3`, `ASVS-REQ-V2.3.5` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 10 refs (`CWE-209`, `CWE-294`, `CWE-346` + 2 more)
  - PCI DSS v4.0.1 — 6 refs (`PCI-1.1.2`, `PCI-1.2.4`, `PCI-2.1.2` + 2 more)
  - OWASP SAMM v2.1 — 4 refs (`SAMM-ACTIVITY-I_SD_3_A`, `SAMM-ACTIVITY-V_AA_2_A`, `SAMM-ACTIVITY-V_RT_3_B` + 1 more)
  - NIST SSDF (SP 800-218 v1.1) — 4 refs (`SSDF-PRACTICE-PS.2`, `SSDF-PRACTICE-PW.2`, `SSDF-PRACTICE-PW.7` + 1 more)
  - MITRE CAPEC v3.9 — 3 refs (`CAPEC-69`, `CAPEC-330`, `CAPEC-475`)
  - SAFECode — Software Integrity Controls (2010) — 3 refs (`SCSIC-DEVELOPMENT`, `SCSIC-DEV-TESTING`, `SCSIC-DELIVERY-SIGNING`)
  - CIS Controls v8.1.2 — 2 refs (`CIS-12.1`, `CIS-18.4`)
  - OWASP Machine Learning Top 10 — 2 refs (`ML06-2023`, `ML08-2023`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-312c1`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.M0013`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A08-2021`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-6.1`)

#### `ACP-ITS-005` — Integration Contract And Change Assurance

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 4 keywords × 49 ocorrências; principais: integration, interface, review, trust)
- **Substrate v7 contributing sources** (8 grounded claims em 3 fontes):
  - NIST SP 800-53 Rev. 5 — 5 refs (`SP800-53-CA-3`, `SP800-53-CM-1`, `SP800-53-SA-10` + 2 more)
  - HIPAA Security Rule — 2 refs (`HIPAA-164-308b1`, `HIPAA-164-314a1`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-5.1`)

#### `ACP-ITS-006` — External Interaction Audit Logging

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 5 keywords × 33 ocorrências; principais: calls, context, logging, record, review)
- **Substrate v7 contributing sources** (185 grounded claims em 20 fontes):
  - NIST SP 800-53 Rev. 5 — 87 refs (`SP800-53-AC-2.4`, `SP800-53-AC-3.10`, `SP800-53-AC-4.26` + 2 more)
  - PCI DSS v4.0.1 — 17 refs (`PCI-REQ-10`, `PCI-5.3.4`, `PCI-8.2.7` + 2 more)
  - OWASP ASVS v5.0.0 — 16 refs (`ASVS-REQ-V13.4.5`, `ASVS-REQ-V16.1.1`, `ASVS-REQ-V16.2.1` + 2 more)
  - CIS Controls v8.1.2 — 16 refs (`CIS-3.1`, `CIS-8`, `CIS-8.1` + 2 more)
  - OWASP SAMM v2.1 — 12 refs (`SAMM-ACTIVITY-I_SB_3_A`, `SAMM-ACTIVITY-O_EM_3_A`, `SAMM-ACTIVITY-O_EM_3_B` + 2 more)
  - MITRE CAPEC v3.9 — 9 refs (`CAPEC-54`, `CAPEC-93`, `CAPEC-268` + 2 more)
  - OWASP DSOMM — 9 refs (`DSOMM-ACTIVITY-4ECED38A79044C45ADB050B663065540`, `DSOMM-ACTIVITY-FE875E17AE4A45F8A359244AA4FCBC04`, `DSOMM-ACTIVITY-CCFDD0A8991E4269AD77C0A54CA655CB` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 3 refs (`CWE-749`, `CWE-778`, `CWE-779`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 3 refs (`AML.TA0011`, `AML.T0006`, `AML.M0024`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 2 refs (`SCFPSSD-LOGGING`, `SCFPSSD-VULN-RESPONSE`)
  - NIST SSDF (SP 800-218 v1.1) — 2 refs (`SSDF-TASK-PW.2.1`, `SSDF-TASK-RV.1.1`)
  - EU Digital Operational Resilience Act (DORA) — 1 refs (`DORA-ART-5`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-312b`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM10-2025`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP08-2025`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML07-2023`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C9`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A09-2021`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-OPS-5`)


### Mechanisms (5)

#### `ACM-ITS-001` — API Gateway With Mutual Authentication

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (146 grounded claims em 16 fontes):
  - OWASP ASVS v5.0.0 — 55 refs (`ASVS-REQ-V2.2.2`, `ASVS-REQ-V4.1.2`, `ASVS-REQ-V4.1.3` + 2 more)
  - NIST SP 800-53 Rev. 5 — 33 refs (`SP800-53-CA-3.5`, `SP800-53-CM-3.5`, `SP800-53-IA-2.1` + 2 more)
  - MITRE CAPEC v3.9 — 15 refs (`CAPEC-14`, `CAPEC-21`, `CAPEC-22` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 8 refs (`AML.T0012`, `AML.T0075`, `AML.T0083` + 2 more)
  - OWASP DSOMM — 6 refs (`DSOMM-ACTIVITY-8098E416E1ED4AE4A56183EFBE76BF57`, `DSOMM-ACTIVITY-598E9F131AC84A01B85E8FAB93EE81DE`, `DSOMM-ACTIVITY-F57D55F2DC054B349D1FF8CE5BFB0715` + 2 more)
  - OWASP SAMM v2.1 — 6 refs (`SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-I_SB_2_B`, `SAMM-ACTIVITY-I_SD_2_B` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 5 refs (`CWE-1392`, `CWE-289`, `CWE-290` + 2 more)
  - CIS Controls v8.1.2 — 3 refs (`CIS-6.4`, `CIS-12.5`, `CIS-16.11`)
  - Anthropic MCP — Official Security Foundations (2025) — 3 refs (`MCP-AUTH-TOKEN-VALIDATION`, `MCP-CONFUSED-DEPUTY`, `MCP-TOKEN-PASSTHROUGH`)
  - OWASP MCP — Secure Server Development v1.0 — 3 refs (`OWASP-MCP-RISK-LANDSCAPE`, `OWASP-MCP-AUTH`, `OWASP-MCP-DEPLOYMENT`)
  - OWASP MCP — Third-Party Servers v1.0 — 3 refs (`OWASP-MCP-3P-CLIENT-SECURITY-DISCOVERY`, `OWASP-MCP-3P-AUTH-AUTHZ-REGISTRATION`, `OWASP-MCP-3P-TOOLS-UTILITIES`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 2 refs (`NIST-AI-100-2-E2025-3.2`, `NIST-AI-100-2-E2025-3.4.3`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP01-2025`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML06-2023`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A07-2021`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-IAM`)

#### `ACM-ITS-002` — Trust Boundary Models

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (20 grounded claims em 7 fontes):
  - NIST SP 800-53 Rev. 5 — 7 refs (`SP800-53-AU-2.3`, `SP800-53-AU-10.3`, `SP800-53-RA-7` + 2 more)
  - OWASP SAMM v2.1 — 7 refs (`SAMM-ACTIVITY-D_SA_3_B`, `SAMM-ACTIVITY-G_EG_3_A`, `SAMM-ACTIVITY-G_PC_1_B` + 2 more)
  - NIST AI RMF 1.0 — 2 refs (`NIST-AI-RMF-GOVERN-3`, `NIST-AI-RMF-MEASURE-4`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.T0054`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-0DE465A655A74343AF79948BB5FF10BA`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-2.5`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-FINDINGS`)

#### `ACM-ITS-003` — Transport Security Controls

- **Manual prose:** cobertura **cross-chapter** — content encontrado em Cap. 14 (`14-governanca-contratacao`). Cap. expected (04-arquitetura-segura) tem cobertura fraca; ler em chapter(s) listada(s).
- **Substrate v7 contributing sources** (207 grounded claims em 18 fontes):
  - NIST SP 800-53 Rev. 5 — 137 refs (`SP800-53-AC-1`, `SP800-53-AC-2`, `SP800-53-AC-2.1` + 2 more)
  - CIS Controls v8.1.2 — 15 refs (`CIS-3`, `CIS-3.1`, `CIS-3.3` + 2 more)
  - PCI DSS v4.0.1 — 14 refs (`PCI-REQ-3`, `PCI-REQ-7`, `PCI-REQ-9` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 7 refs (`CWE-1220`, `CWE-312`, `CWE-654` + 2 more)
  - HIPAA Security Rule — 6 refs (`HIPAA-164-308a2`, `HIPAA-164-308a4`, `HIPAA-164-308a5` + 2 more)
  - OWASP SAMM v2.1 — 6 refs (`SAMM-ACTIVITY-D_SA_1_A`, `SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-D_SA_2_B` + 2 more)
  - MITRE CAPEC v3.9 — 5 refs (`CAPEC-146`, `CAPEC-200`, `CAPEC-439` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 3 refs (`AML.TA0014`, `AML.M0020`, `AML.M0032`)
  - NIST SSDF (SP 800-218 v1.1) — 3 refs (`SSDF-PRACTICE-PW.1`, `SSDF-TASK-PW.1.3`, `SSDF-TASK-PW.9.1`)
  - OWASP DSOMM — 2 refs (`DSOMM-ACTIVITY-AE22DAFDBCD641EEBA018B7FE6FC1AD9`, `DSOMM-ACTIVITY-72737130472C498480F89AB2F1C2ED5D`)
  - PCI Secure SLC v1.1 — 2 refs (`PCISSLC-3.3`, `PCISSLC-9.3`)
  - OWASP ASVS v5.0.0 — 1 refs (`ASVS-REQ-V17.2.1`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-32`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM10-2025`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML06-2023`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C7`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-SECURITY-CONTROLS`)

#### `ACM-ITS-004` — Message Integrity And Authorized Peer Policies

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (183 grounded claims em 18 fontes):
  - NIST SP 800-53 Rev. 5 — 96 refs (`SP800-53-AC-3.12`, `SP800-53-AC-8`, `SP800-53-AC-14` + 2 more)
  - PCI DSS v4.0.1 — 25 refs (`PCI-1.2.2`, `PCI-1.2.3`, `PCI-1.4.3` + 2 more)
  - OWASP ASVS v5.0.0 — 13 refs (`ASVS-REQ-V2.3.5`, `ASVS-REQ-V4.1.5`, `ASVS-REQ-V9.1.2` + 2 more)
  - MITRE CAPEC v3.9 — 13 refs (`CAPEC-330`, `CAPEC-418`, `CAPEC-422` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 8 refs (`CWE-209`, `CWE-348`, `CWE-349` + 2 more)
  - CIS Controls v8.1.2 — 5 refs (`CIS-2.2`, `CIS-2.5`, `CIS-2.7` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 5 refs (`SSDF-PRACTICE-PS.2`, `SSDF-PRACTICE-PW.2`, `SSDF-PRACTICE-PW.7` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0054`, `AML.M0013`)
  - OWASP DSOMM — 2 refs (`DSOMM-ACTIVITY-FFE86CAF2FEC4630B5142DB83983984D`, `DSOMM-ACTIVITY-AC8730A2CCC0465C9550D91EDAE9D5EE`)
  - OWASP MCP — Secure Server Development v1.0 — 2 refs (`OWASP-MCP-GOVERNANCE`, `OWASP-MCP-MINIMUM-BAR`)
  - OWASP Machine Learning Top 10 — 2 refs (`ML06-2023`, `ML08-2023`)
  - OWASP SAMM v2.1 — 2 refs (`SAMM-ACTIVITY-I_SB_3_B`, `SAMM-ACTIVITY-V_RT_3_B`)
  - PCI Secure SLC v1.1 — 2 refs (`PCISSLC-6.1`, `PCISSLC-6.2`)
  - SAFECode — Software Integrity Controls (2010) — 2 refs (`SCSIC-DELIVERY`, `SCSIC-DELIVERY-SIGNING`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-32`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-312c1`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A08-2021`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-OPS-16`)

#### `ACM-ITS-005` — Structured External Call Logging

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 5 keywords × 33 ocorrências; principais: calls, context, logging, record, review)
- **Substrate v7 contributing sources** (87 grounded claims em 16 fontes):
  - NIST SP 800-53 Rev. 5 — 35 refs (`SP800-53-AU-2`, `SP800-53-AU-4`, `SP800-53-AU-4.1` + 2 more)
  - CIS Controls v8.1.2 — 12 refs (`CIS-8`, `CIS-8.1`, `CIS-8.2` + 2 more)
  - PCI DSS v4.0.1 — 8 refs (`PCI-REQ-10`, `PCI-5.3.4`, `PCI-9.3.4` + 2 more)
  - OWASP DSOMM — 7 refs (`DSOMM-ACTIVITY-4ECED38A79044C45ADB050B663065540`, `DSOMM-ACTIVITY-FE875E17AE4A45F8A359244AA4FCBC04`, `DSOMM-ACTIVITY-CCFDD0A8991E4269AD77C0A54CA655CB` + 2 more)
  - MITRE CAPEC v3.9 — 6 refs (`CAPEC-54`, `CAPEC-93`, `CAPEC-268` + 2 more)
  - OWASP SAMM v2.1 — 6 refs (`SAMM-ACTIVITY-I_SB_3_A`, `SAMM-ACTIVITY-I_SB_3_B`, `SAMM-ACTIVITY-O_IM_1_A` + 2 more)
  - OWASP ASVS v5.0.0 — 4 refs (`ASVS-REQ-V16.1.1`, `ASVS-REQ-V16.2.1`, `ASVS-REQ-V16.2.3` + 1 more)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-779`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.M0024`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM10-2025`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP08-2025`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C9`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A09-2021`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-OPS-5`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-LOGGING`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-PRACTICE-PO.3`)


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
