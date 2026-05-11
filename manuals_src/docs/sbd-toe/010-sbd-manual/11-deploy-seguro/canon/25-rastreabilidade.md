# 25. Rastreabilidade — Deploy Seguro

## Sumário

Este capítulo é a **âncora primária** das slices AppSec Core V1: `ACO-RPR` (Release promotion, rollout controlado e readiness para rollback).

Cobertura V1 entity-level: **27 entidades** primárias (10 ControlObjectives + 9 Practices + 8 Mechanisms). Cada entidade é listada abaixo com cobertura no Manual (prose anchor) e fontes externas substrate v7 que contribuem para a sua substantive coverage.

---

## Slice `ACO-RPR` — Release promotion, rollout controlado e readiness para rollback

### ControlObjectives (10)

#### `ACO-RPR-001` — Release Authorization And Irreversible Change Accountability

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (50 grounded claims em 8 fontes):
  - NIST SP 800-53 Rev. 5 — 38 refs (`SP800-53-AC-1`, `SP800-53-AC-14`, `SP800-53-AC-16` + 2 more)
  - CIS Controls v8.1.2 — 4 refs (`CIS-2.2`, `CIS-2.5`, `CIS-6.2` + 1 more)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-212`, `CWE-283`)
  - PCI Secure SLC v1.1 — 2 refs (`PCISSLC-5.1`, `PCISSLC-7.1`)
  - OWASP ASVS v5.0.0 — 1 refs (`ASVS-REQ-V8.3.2`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-308a4`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM06-2025`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-D_TA_2_A`)

#### `ACO-RPR-002` — Verified Artifact Promotion

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (36 grounded claims em 13 fontes):
  - SLSA Specification v1.0 — Build Track — 8 refs (`SLSA-BUILD-L1`, `SLSA-BUILD-L2`, `SLSA-PRINCIPLE-TRUST-PLATFORMS` + 2 more)
  - NIST SP 800-53 Rev. 5 — 5 refs (`SP800-53-MP-3`, `SP800-53-SA-3.2`, `SP800-53-SA-12.10` + 2 more)
  - MITRE CAPEC v3.9 — 4 refs (`CAPEC-523`, `CAPEC-524`, `CAPEC-532` + 1 more)
  - NIST SSDF (SP 800-218 v1.1) — 4 refs (`SSDF-PRACTICE-PS.2`, `SSDF-TASK-PS.2.1`, `SSDF-TASK-PS.3.2` + 1 more)
  - OWASP DSOMM — 3 refs (`DSOMM-ACTIVITY-9F10792761E9457485AD3F2B4BCA8665`, `DSOMM-ACTIVITY-5786959D0C6F46A68E1CA32FF1A50222`, `DSOMM-ACTIVITY-8F2B4D5A3C1E4B7A9D8F2E6C4A1B5D7F`)
  - OWASP ASVS v5.0.0 — 2 refs (`ASVS-REQ-V6.7.1`, `ASVS-REQ-V15.1.2`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0111`, `AML.CS0008`)
  - OWASP Machine Learning Top 10 — 2 refs (`ML06-2023`, `ML08-2023`)
  - SAFECode — Software Integrity Controls (2010) — 2 refs (`SCSIC-SOURCING-OSS`, `SCSIC-DELIVERY-SIGNING`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-353`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MAP-2.3`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM04-2025`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-I_SB_1_A`)

#### `ACO-RPR-003` — Pre-Promotion Security Gates And Staging Assurance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (1 grounded claims em 1 fontes):
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.T0054`)

#### `ACO-RPR-004` — End-to-End Deployment Traceability

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (41 grounded claims em 12 fontes):
  - OWASP DSOMM — 10 refs (`DSOMM-ACTIVITY-67E1A9AA9FBF4EC5A2DE400F01960C51`, `DSOMM-ACTIVITY-2A44B708734F4463B0CB86DC46344B2F`, `DSOMM-ACTIVITY-830570280B774D2E813540969768AE88` + 2 more)
  - NIST SP 800-53 Rev. 5 — 9 refs (`SP800-53-IR-5`, `SP800-53-MA-2`, `SP800-53-MA-3` + 2 more)
  - OWASP SAMM v2.1 — 7 refs (`SAMM-ACTIVITY-I_SB_1_B`, `SAMM-ACTIVITY-I_SB_3_A`, `SAMM-ACTIVITY-I_SD_2_A` + 2 more)
  - OWASP ASVS v5.0.0 — 4 refs (`ASVS-REQ-V13.4.4`, `ASVS-REQ-V13.4.5`, `ASVS-REQ-V16.1.1` + 1 more)
  - CIS Controls v8.1.2 — 3 refs (`CIS-1`, `CIS-8.5`, `CIS-13.6`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0095.000`, `AML.M0024`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-144`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MEASURE-4`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM10-2025`)
  - OWASP MCP — Third-Party Servers v1.0 — 1 refs (`OWASP-MCP-3P-GOVERNANCE-REGISTRY`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP08-2025`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A08-2021`)

#### `ACO-RPR-005` — Tested Rollback Readiness And Reversibility

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (11 grounded claims em 3 fontes):
  - NIST SP 800-53 Rev. 5 — 7 refs (`SP800-53-CM-2.3`, `SP800-53-CP-2`, `SP800-53-CP-4.4` + 2 more)
  - CIS Controls v8.1.2 — 3 refs (`CIS-7.7`, `CIS-11.5`, `CIS-18.3`)
  - EU Digital Operational Resilience Act (DORA) — 1 refs (`DORA-ART-12`)

#### `ACO-RPR-006` — Controlled Rollout And Blast-Radius Containment

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (1 grounded claims em 1 fontes):
  - NIST SP 800-53 Rev. 5 — 1 refs (`SP800-53-PE-3.6`)

#### `ACO-RPR-007` — Release Promotion And Reversible Rollout Assurance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (10 grounded claims em 7 fontes):
  - NIST SP 800-53 Rev. 5 — 4 refs (`SP800-53-AC-3.9`, `SP800-53-MP-8.3`, `SP800-53-SI-19.3` + 1 more)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-439`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-4.11`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-1341`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-13`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-O_OM_3_B`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-PRACTICE-PS.3`)

#### `ACO-RPR-008` — Secure Defaults And Hardened Baseline Selection

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (5 grounded claims em 5 fontes):
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-1188`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-5992C38C8597403589DBD15820D81C3A`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-I_SB_3_A`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-2.2.2`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PW.9.1`)

#### `ACO-RPR-009` — Security-Relevant Configuration Integrity And Override Control

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (660 grounded claims em 25 fontes):
  - NIST SP 800-53 Rev. 5 — 253 refs (`SP800-53-AC-2`, `SP800-53-AC-2.6`, `SP800-53-AC-3.2` + 2 more)
  - MITRE CAPEC v3.9 — 95 refs (`CAPEC-12`, `CAPEC-13`, `CAPEC-14` + 2 more)
  - PCI DSS v4.0.1 — 82 refs (`PCI-REQ-1`, `PCI-REQ-2`, `PCI-REQ-5` + 2 more)
  - CIS Controls v8.1.2 — 35 refs (`CIS-2.6`, `CIS-3`, `CIS-3.1` + 2 more)
  - OWASP SAMM v2.1 — 29 refs (`SAMM-ACTIVITY-D_SA_1_A`, `SAMM-ACTIVITY-D_SA_1_B`, `SAMM-ACTIVITY-D_SA_2_A` + 2 more)
  - OWASP ASVS v5.0.0 — 28 refs (`ASVS-REQ-V1.2.6`, `ASVS-REQ-V2.4.1`, `ASVS-REQ-V3.1.1` + 2 more)
  - OWASP DSOMM — 25 refs (`DSOMM-ACTIVITY-DF428C9DEFA042269F47A15BB53F822B`, `DSOMM-ACTIVITY-94A96F798BD6490497C0994FF88F176A`, `DSOMM-ACTIVITY-A511799B045E4B9698437D63D8C1E2AD` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 19 refs (`CWE-1037`, `CWE-1220`, `CWE-15` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 19 refs (`AML.TA0012`, `AML.TA0007`, `AML.T0008` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 16 refs (`SSDF-PRACTICE-PO.1`, `SSDF-PRACTICE-PO.5`, `SSDF-PRACTICE-PS.1` + 2 more)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 12 refs (`NIST-AI-100-2-E2025-2.1`, `NIST-AI-100-2-E2025-2.1.2`, `NIST-AI-100-2-E2025-2.1.3` + 2 more)
  - PCI Secure SLC v1.1 — 9 refs (`PCISSLC-1.2`, `PCISSLC-1.3`, `PCISSLC-2.2` + 2 more)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 9 refs (`SCAGILE-OPS-8`, `SCAGILE-OPS-12`, `SCAGILE-OPS-13` + 2 more)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 6 refs (`SCFPSSD-SECURITY-CONTROLS`, `SCFPSSD-DESIGN-PRINCIPLES`, `SCFPSSD-THREAT-MODELING` + 2 more)
  - OWASP LLM Top 10 (2025) — 4 refs (`LLM01-2025`, `LLM03-2025`, `LLM07-2025` + 1 more)
  - HIPAA Security Rule — 3 refs (`HIPAA-164-308a2`, `HIPAA-164-308a5`, `HIPAA-164-310a1`)
  - OWASP MCP — Secure Server Development v1.0 — 3 refs (`OWASP-MCP-RISK-LANDSCAPE`, `OWASP-MCP-DEPLOYMENT`, `OWASP-MCP-GOVERNANCE`)
  - OWASP MCP — Third-Party Servers v1.0 — 2 refs (`OWASP-MCP-3P-CLIENT-SECURITY-DISCOVERY`, `OWASP-MCP-3P-AUTH-AUTHZ-REGISTRATION`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 2 refs (`MCP01-2025`, `MCP02-2025`)
  - OWASP Proactive Controls (2018) — 2 refs (`OPC-C1`, `OPC-C2`)
  - OWASP Top 10 (2021) — 2 refs (`TOP10-A05-2021`, `TOP10-A06-2021`)
  - SAFECode — Software Integrity Controls (2010) — 2 refs (`SCSIC-DEVELOPMENT`, `SCSIC-DEV-REPO`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-13`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-32`)

#### `ACO-RPR-010` — Baseline Review, Exception Visibility And Change Discipline

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (84 grounded claims em 15 fontes):
  - NIST SP 800-53 Rev. 5 — 25 refs (`SP800-53-AU-2`, `SP800-53-AU-6`, `SP800-53-AU-6.4` + 2 more)
  - OWASP SAMM v2.1 — 18 refs (`SAMM-ACTIVITY-D_TA_3_A`, `SAMM-ACTIVITY-G_EG_3_A`, `SAMM-ACTIVITY-G_PC_2_B` + 2 more)
  - PCI DSS v4.0.1 — 9 refs (`PCI-10.3.4`, `PCI-10.4.1`, `PCI-10.4.3` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 6 refs (`SSDF-TASK-PO.4.1`, `SSDF-TASK-PW.7.2`, `SSDF-TASK-PW.8.1` + 2 more)
  - CIS Controls v8.1.2 — 5 refs (`CIS-8.1`, `CIS-8.4`, `CIS-16.4` + 2 more)
  - OWASP DSOMM — 5 refs (`DSOMM-ACTIVITY-3F63BDBCC75F4780A941E6AD42E894E1`, `DSOMM-ACTIVITY-1CD5E4B8BE364726ADC7D8F843F47AC8`, `DSOMM-ACTIVITY-44F2C8A94AAA4C72942D63F78B89F385` + 2 more)
  - PCI Secure SLC v1.1 — 4 refs (`PCISSLC-2.1`, `PCISSLC-2.6`, `PCISSLC-5.1` + 1 more)
  - OWASP ASVS v5.0.0 — 3 refs (`ASVS-REQ-V16.2.2`, `ASVS-REQ-V16.5.1`, `ASVS-REQ-V16.5.3`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 3 refs (`SCAGILE-OPS-4`, `SCAGILE-OPS-7`, `SCAGILE-OPS-9`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-13`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-32`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-308a1`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-GOVERN-1.5`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML07-2023`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-MITIGATIONS`)


### Practices (9)

#### `ACP-RPR-001` — Accountable Release Approval

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (20 grounded claims em 6 fontes):
  - NIST SP 800-53 Rev. 5 — 11 refs (`SP800-53-AT-1`, `SP800-53-AU-1`, `SP800-53-AU-2.4` + 2 more)
  - OWASP SAMM v2.1 — 5 refs (`SAMM-ACTIVITY-D_TA_2_A`, `SAMM-ACTIVITY-G_EG_2_A`, `SAMM-ACTIVITY-G_EG_3_A` + 2 more)
  - CIS Controls v8.1.2 — 1 refs (`CIS-17.3`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-283`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.M0029`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-7.1`)

#### `ACP-RPR-002` — Verified Artifact Promotion

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 5 keywords × 108 ocorrências; principais: artifact, identity, promotion, provenance, release)
- **Substrate v7 contributing sources** (50 grounded claims em 13 fontes):
  - NIST SP 800-53 Rev. 5 — 15 refs (`SP800-53-AU-10.5`, `SP800-53-IA-4.3`, `SP800-53-IA-12` + 2 more)
  - OWASP ASVS v5.0.0 — 7 refs (`ASVS-REQ-V4.1.5`, `ASVS-REQ-V6.7.1`, `ASVS-REQ-V6.8.2` + 2 more)
  - SLSA Specification v1.0 — Build Track — 7 refs (`SLSA-BUILD-L1`, `SLSA-BUILD-L2`, `SLSA-PRINCIPLE-TRUST-PLATFORMS` + 2 more)
  - MITRE CAPEC v3.9 — 5 refs (`CAPEC-476`, `CAPEC-523`, `CAPEC-524` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 4 refs (`SSDF-PRACTICE-PS.2`, `SSDF-TASK-PS.2.1`, `SSDF-TASK-PS.3.2` + 1 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 3 refs (`AML.T0111`, `AML.M0013`, `AML.CS0008`)
  - OWASP DSOMM — 2 refs (`DSOMM-ACTIVITY-9F10792761E9457485AD3F2B4BCA8665`, `DSOMM-ACTIVITY-8F2B4D5A3C1E4B7A9D8F2E6C4A1B5D7F`)
  - SAFECode — Software Integrity Controls (2010) — 2 refs (`SCSIC-SOURCING-TRANSFER`, `SCSIC-DELIVERY-SIGNING`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-348`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MAP-2.3`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM04-2025`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML08-2023`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-I_SB_1_A`)

#### `ACP-RPR-003` — Pre-Promotion Gates And Staging Validation

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 5 keywords × 117 ocorrências; principais: gate, gates, policy, promotion, staging)
- **Substrate v7 contributing sources** (6 grounded claims em 3 fontes):
  - OWASP ASVS v5.0.0 — 4 refs (`ASVS-REQ-V2.3.1`, `ASVS-REQ-V2.3.4`, `ASVS-REQ-V2.3.5` + 1 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.M0020`)
  - NIST SP 800-53 Rev. 5 — 1 refs (`SP800-53-CP-12`)

#### `ACP-RPR-004` — End-to-End Deploy Traceability

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (75 grounded claims em 14 fontes):
  - OWASP DSOMM — 24 refs (`DSOMM-ACTIVITY-F6F7737F25A943178DE209BF59F29B5B`, `DSOMM-ACTIVITY-A340F46B63604CB8847BA0D3483D09D3`, `DSOMM-ACTIVITY-F3C4971E9F4D4E598ED0F0BDB6262477` + 2 more)
  - NIST SP 800-53 Rev. 5 — 14 refs (`SP800-53-CM-8.2`, `SP800-53-CM-8.7`, `SP800-53-MA-3` + 2 more)
  - OWASP SAMM v2.1 — 13 refs (`SAMM-ACTIVITY-I_SB_1_B`, `SAMM-ACTIVITY-I_SB_2_A`, `SAMM-ACTIVITY-I_SB_3_A` + 2 more)
  - OWASP ASVS v5.0.0 — 5 refs (`ASVS-REQ-V13.4.4`, `ASVS-REQ-V13.4.5`, `ASVS-REQ-V13.4.6` + 2 more)
  - CIS Controls v8.1.2 — 5 refs (`CIS-1`, `CIS-7.1`, `CIS-12.1` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 3 refs (`AML.T0011.000`, `AML.T0104`, `AML.T0002.002`)
  - OWASP LLM Top 10 (2025) — 3 refs (`LLM03-2025`, `LLM04-2025`, `LLM10-2025`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 2 refs (`SCAGILE-OPS-1`, `SCAGILE-OPS-6`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MEASURE-4`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-DEPLOYMENT`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP04-2025`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML06-2023`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEV-BUILD`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-PRACTICE-PO.3`)

#### `ACP-RPR-005` — Tested Rollback Discipline

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 4 keywords × 198 ocorrências; principais: production, rollback, rollout, runtime)
- **Substrate v7 contributing sources** (15 grounded claims em 4 fontes):
  - CIS Controls v8.1.2 — 6 refs (`CIS-11`, `CIS-11.1`, `CIS-11.2` + 2 more)
  - NIST SP 800-53 Rev. 5 — 4 refs (`SP800-53-CM-2.3`, `SP800-53-CP-4.4`, `SP800-53-CP-9.2` + 1 more)
  - OWASP SAMM v2.1 — 4 refs (`SAMM-ACTIVITY-O_EM_3_A`, `SAMM-ACTIVITY-O_OM_3_A`, `SAMM-ACTIVITY-O_OM_3_B` + 1 more)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-TESTING`)

#### `ACP-RPR-006` — Progressive Rollout And Containment

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 3 keywords × 29 ocorrências; principais: change, progressive, rollout)
- **Substrate v7 contributing sources** (1 grounded claims em 1 fontes):
  - EU Digital Operational Resilience Act (DORA) — 1 refs (`DORA-ART-5`)

#### `ACP-RPR-008` — Define Hardened Baseline Profiles For Security-Relevant Components

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 4 keywords × 27 ocorrências; principais: baseline, components, define, policy)
- **Substrate v7 contributing sources** (67 grounded claims em 13 fontes):
  - NIST SP 800-53 Rev. 5 — 15 refs (`SP800-53-AC-16`, `SP800-53-AC-16.7`, `SP800-53-CM-2` + 2 more)
  - OWASP SAMM v2.1 — 13 refs (`SAMM-ACTIVITY-D_SR_2_A`, `SAMM-ACTIVITY-D_SR_3_A`, `SAMM-ACTIVITY-D_TA_1_A` + 2 more)
  - OWASP DSOMM — 12 refs (`DSOMM-ACTIVITY-47419324E263415B815DE7161B6B905E`, `DSOMM-ACTIVITY-B597928E54D648A5A8068003DCD56AAB`, `DSOMM-ACTIVITY-CF81922530CB47028E3260225EEDC33D` + 2 more)
  - PCI DSS v4.0.1 — 6 refs (`PCI-REQ-2`, `PCI-REQ-8`, `PCI-1.2.1` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 6 refs (`SSDF-PRACTICE-PO.1`, `SSDF-PRACTICE-PO.5`, `SSDF-PRACTICE-PW.1` + 2 more)
  - MITRE CAPEC v3.9 — 5 refs (`CAPEC-166`, `CAPEC-523`, `CAPEC-524` + 2 more)
  - CIS Controls v8.1.2 — 3 refs (`CIS-12.2`, `CIS-16.1`, `CIS-16.7`)
  - OWASP Proactive Controls (2018) — 2 refs (`OPC-C1`, `OPC-C2`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-547`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.T0054`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 1 refs (`NIST-AI-100-2-E2025-4.1.3`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM03-2025`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-DESIGN-PRINCIPLES`)

#### `ACP-RPR-009` — Review Security-Relevant Overrides Before Promotion Or Deployment

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 4 keywords × 16 ocorrências; principais: change, deployment, promotion, review)
- **Substrate v7 contributing sources** (205 grounded claims em 18 fontes):
  - NIST SP 800-53 Rev. 5 — 95 refs (`SP800-53-AC-1`, `SP800-53-AC-3`, `SP800-53-AC-3.4` + 2 more)
  - PCI DSS v4.0.1 — 23 refs (`PCI-REQ-12`, `PCI-1.2.7`, `PCI-1.5.1` + 2 more)
  - CIS Controls v8.1.2 — 19 refs (`CIS-4.1`, `CIS-4.2`, `CIS-4.8` + 2 more)
  - MITRE CAPEC v3.9 — 17 refs (`CAPEC-69`, `CAPEC-122`, `CAPEC-180` + 2 more)
  - OWASP SAMM v2.1 — 16 refs (`SAMM-ACTIVITY-D_SR_1_A`, `SAMM-ACTIVITY-D_SR_1_B`, `SAMM-ACTIVITY-D_TA_2_A` + 2 more)
  - OWASP DSOMM — 13 refs (`DSOMM-ACTIVITY-1B9281B948E24C019AC69DB9931C4885`, `DSOMM-ACTIVITY-DD5ED7C1BDBF400FB75F6D3953A1A04E`, `DSOMM-ACTIVITY-0A929C3EAB9A42068761ADF84B74622E` + 2 more)
  - HIPAA Security Rule — 3 refs (`HIPAA-164-308a2`, `HIPAA-164-308a5`, `HIPAA-164-308a6`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 3 refs (`SCAGILE-OPS-2`, `SCAGILE-OPS-16`, `SCAGILE-EXP-9`)
  - ENISA — Multilayer AI Cybersecurity Practices (2023) — 2 refs (`ENISA-AI-FAICP-SURVEY`, `ENISA-AI-FAICP-CONCLUSIONS`)
  - EU NIS2 Directive — 2 refs (`NIS2-ART-20`, `NIS2-ART-21`)
  - NIST AI RMF 1.0 — 2 refs (`NIST-AI-RMF-GOVERN-4`, `NIST-AI-RMF-MANAGE-4`)
  - OWASP MCP — Secure Server Development v1.0 — 2 refs (`OWASP-MCP-GOVERNANCE`, `OWASP-MCP-MINIMUM-BAR`)
  - PCI Secure SLC v1.1 — 2 refs (`PCISSLC-3.3`, `PCISSLC-9.2`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 2 refs (`SCFPSSD-FINDINGS`, `SCFPSSD-VULN-RESPONSE`)
  - OWASP ASVS v5.0.0 — 1 refs (`ASVS-REQ-V8.4.2`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-213`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.TA0007`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-RV.1.3`)

#### `ACP-RPR-010` — Record And Periodically Review Exceptions Against The Intended Baseline

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 3 keywords × 9 ocorrências; principais: baseline, record, review)
- **Substrate v7 contributing sources** (138 grounded claims em 15 fontes):
  - NIST SP 800-53 Rev. 5 — 77 refs (`SP800-53-AC-2`, `SP800-53-AC-2.12`, `SP800-53-AC-25` + 2 more)
  - CIS Controls v8.1.2 — 13 refs (`CIS-3.1`, `CIS-3.8`, `CIS-8.1` + 2 more)
  - PCI DSS v4.0.1 — 12 refs (`PCI-6.5.2`, `PCI-9.3.1`, `PCI-10.2.2` + 2 more)
  - OWASP ASVS v5.0.0 — 9 refs (`ASVS-REQ-V7.5.1`, `ASVS-REQ-V14.2.7`, `ASVS-REQ-V16.2.1` + 2 more)
  - OWASP SAMM v2.1 — 9 refs (`SAMM-ACTIVITY-D_TA_3_A`, `SAMM-ACTIVITY-G_PC_2_B`, `SAMM-ACTIVITY-G_PC_3_B` + 2 more)
  - OWASP DSOMM — 5 refs (`DSOMM-ACTIVITY-CCFDD0A8991E4269AD77C0A54CA655CB`, `DSOMM-ACTIVITY-E9A6D403A467445EB98A74F0C29DA0B1`, `DSOMM-ACTIVITY-ED715B38C34B40CD83FDCE807F306FC1` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 3 refs (`SSDF-TASK-PO.4.1`, `SSDF-TASK-RV.1.2`, `SSDF-TASK-RV.3.2`)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-307`, `CWE-358`)
  - EU GDPR (RGPD) — 2 refs (`GDPR-ART-5`, `GDPR-ART-32`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-316b1`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-GOVERN-1.5`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML07-2023`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A09-2021`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-2.6`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-LOGGING`)


### Mechanisms (8)

#### `ACM-RPR-001` — Release Promotion Controls

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (17 grounded claims em 3 fontes):
  - NIST SP 800-53 Rev. 5 — 15 refs (`SP800-53-AC-3.9`, `SP800-53-AC-22`, `SP800-53-AT-3.1` + 2 more)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-677`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-SOURCING`)

#### `ACM-RPR-002` — Approval Gates And Separation Of Signal From Promotion Decision

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 3 keywords × 58 ocorrências; principais: gate, gates, promotion)
- **Substrate v7 contributing sources** (12 grounded claims em 5 fontes):
  - NIST SP 800-53 Rev. 5 — 4 refs (`SP800-53-MA-2`, `SP800-53-MA-3`, `SP800-53-PM-1` + 1 more)
  - MITRE CWE — Software Development View (v4.19.1) — 3 refs (`CWE-184`, `CWE-807`, `CWE-841`)
  - NIST AI RMF 1.0 — 3 refs (`NIST-AI-RMF-GOVERN-1.6`, `NIST-AI-RMF-GOVERN-1.7`, `NIST-AI-RMF-MAP-3.5`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.M0029`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PO.4.2`)

#### `ACM-RPR-003` — Provenance And Signature Verification At Promotion

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 5 keywords × 109 ocorrências; principais: identity, promotion, provenance, release, verification)
- **Substrate v7 contributing sources** (58 grounded claims em 14 fontes):
  - NIST SP 800-53 Rev. 5 — 14 refs (`SP800-53-AU-10.5`, `SP800-53-CM-14`, `SP800-53-IA-5.14` + 2 more)
  - SLSA Specification v1.0 — Build Track — 8 refs (`SLSA-BUILD-L1`, `SLSA-BUILD-L2`, `SLSA-PRINCIPLE-TRUST-PLATFORMS` + 2 more)
  - OWASP ASVS v5.0.0 — 7 refs (`ASVS-REQ-V4.1.5`, `ASVS-REQ-V6.7.1`, `ASVS-REQ-V6.8.2` + 2 more)
  - MITRE CAPEC v3.9 — 7 refs (`CAPEC-459`, `CAPEC-475`, `CAPEC-476` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 6 refs (`CWE-283`, `CWE-347`, `CWE-348` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 4 refs (`SSDF-PRACTICE-PS.2`, `SSDF-TASK-PS.2.1`, `SSDF-TASK-PS.3.2` + 1 more)
  - OWASP DSOMM — 3 refs (`DSOMM-ACTIVITY-9F10792761E9457485AD3F2B4BCA8665`, `DSOMM-ACTIVITY-5786959D0C6F46A68E1CA32FF1A50222`, `DSOMM-ACTIVITY-8F2B4D5A3C1E4B7A9D8F2E6C4A1B5D7F`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0111`, `AML.CS0008`)
  - OWASP Machine Learning Top 10 — 2 refs (`ML06-2023`, `ML08-2023`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-2.2`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM04-2025`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-I_SB_1_A`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-6.2`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DELIVERY-SIGNING`)

#### `ACM-RPR-004` — Rollback And Containment Controls

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (67 grounded claims em 11 fontes):
  - NIST SP 800-53 Rev. 5 — 29 refs (`SP800-53-CM-2.3`, `SP800-53-CM-3`, `SP800-53-CM-8.2` + 2 more)
  - CIS Controls v8.1.2 — 13 refs (`CIS-3`, `CIS-3.1`, `CIS-3.4` + 2 more)
  - OWASP SAMM v2.1 — 10 refs (`SAMM-ACTIVITY-D_SR_3_B`, `SAMM-ACTIVITY-I_DM_1_A`, `SAMM-ACTIVITY-I_DM_2_B` + 2 more)
  - OWASP DSOMM — 4 refs (`DSOMM-ACTIVITY-A511799B045E4B9698437D63D8C1E2AD`, `DSOMM-ACTIVITY-C72DA77986CC45B1A339190CE5093171`, `DSOMM-ACTIVITY-066084C6113546359CC59E75C7C5459F` + 1 more)
  - MITRE CAPEC v3.9 — 3 refs (`CAPEC-517`, `CAPEC-518`, `CAPEC-675`)
  - EU Digital Operational Resilience Act (DORA) — 3 refs (`DORA-ART-5`, `DORA-ART-9`, `DORA-ART-12`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.TA0011`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-OPS-5`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-MITIGATIONS`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-PRACTICE-PS.3`)

#### `ACM-RPR-005` — Deployment Pipeline Traceability And Audit Controls

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 6 keywords × 332 ocorrências; principais: audit, deploy, deployment, environment, logs)
- **Substrate v7 contributing sources** (89 grounded claims em 16 fontes):
  - OWASP DSOMM — 27 refs (`DSOMM-ACTIVITY-F6F7737F25A943178DE209BF59F29B5B`, `DSOMM-ACTIVITY-A340F46B63604CB8847BA0D3483D09D3`, `DSOMM-ACTIVITY-F3C4971E9F4D4E598ED0F0BDB6262477` + 2 more)
  - NIST SP 800-53 Rev. 5 — 19 refs (`SP800-53-AU-2`, `SP800-53-AU-6.3`, `SP800-53-AU-9.2` + 2 more)
  - OWASP SAMM v2.1 — 13 refs (`SAMM-ACTIVITY-D_SA_1_B`, `SAMM-ACTIVITY-I_SB_1_B`, `SAMM-ACTIVITY-I_SB_2_A` + 2 more)
  - CIS Controls v8.1.2 — 10 refs (`CIS-1`, `CIS-8.1`, `CIS-8.2` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 4 refs (`AML.T0002`, `AML.T0075`, `AML.T0002.002` + 1 more)
  - PCI DSS v4.0.1 — 4 refs (`PCI-5.1.2`, `PCI-10.2.2`, `PCI-10.3.3` + 1 more)
  - OWASP ASVS v5.0.0 — 2 refs (`ASVS-REQ-V16.1.1`, `ASVS-REQ-V16.2.3`)
  - OWASP LLM Top 10 (2025) — 2 refs (`LLM03-2025`, `LLM10-2025`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MEASURE-2.3`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-CONTINUOUS-VALIDATION`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP08-2025`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML06-2023`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-2.4`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-LOGGING`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEV-BUILD`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-PRACTICE-PO.3`)

#### `ACM-RPR-008` — Baseline Configuration Template Or Policy Bundle

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (24 grounded claims em 6 fontes):
  - NIST SP 800-53 Rev. 5 — 10 refs (`SP800-53-CM-1`, `SP800-53-CM-2`, `SP800-53-CM-2.6` + 2 more)
  - OWASP SAMM v2.1 — 4 refs (`SAMM-ACTIVITY-D_SR_3_A`, `SAMM-ACTIVITY-I_SB_1_A`, `SAMM-ACTIVITY-I_SB_3_A` + 1 more)
  - MITRE CAPEC v3.9 — 3 refs (`CAPEC-523`, `CAPEC-524`, `CAPEC-532`)
  - CIS Controls v8.1.2 — 3 refs (`CIS-4.1`, `CIS-4.2`, `CIS-16.7`)
  - OWASP DSOMM — 3 refs (`DSOMM-ACTIVITY-B597928E54D648A5A8068003DCD56AAB`, `DSOMM-ACTIVITY-CF81922530CB47028E3260225EEDC33D`, `DSOMM-ACTIVITY-5992C38C8597403589DBD15820D81C3A`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PW.9.1`)

#### `ACM-RPR-009` — Gate Or Policy Check For Prohibited Or Unsafe Overrides

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (235 grounded claims em 19 fontes):
  - NIST SP 800-53 Rev. 5 — 84 refs (`SP800-53-AC-1`, `SP800-53-AC-2.11`, `SP800-53-AC-3` + 2 more)
  - PCI DSS v4.0.1 — 45 refs (`PCI-REQ-1`, `PCI-REQ-5`, `PCI-REQ-12` + 2 more)
  - MITRE CAPEC v3.9 — 22 refs (`CAPEC-2`, `CAPEC-13`, `CAPEC-35` + 2 more)
  - OWASP ASVS v5.0.0 — 20 refs (`ASVS-REQ-V2.2.1`, `ASVS-REQ-V2.2.2`, `ASVS-REQ-V2.3.2` + 2 more)
  - OWASP SAMM v2.1 — 20 refs (`SAMM-ACTIVITY-D_SA_1_A`, `SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-D_SA_3_B` + 2 more)
  - CIS Controls v8.1.2 — 11 refs (`CIS-3.3`, `CIS-4.4`, `CIS-10.2` + 2 more)
  - OWASP DSOMM — 9 refs (`DSOMM-ACTIVITY-9768F154357A4C06AF6FD66570677C9B`, `DSOMM-ACTIVITY-F88D1B173D7D4C3D8139AD44FC4942D4`, `DSOMM-ACTIVITY-72737130472C498480F89AB2F1C2ED5D` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 4 refs (`SSDF-PRACTICE-PS.1`, `SSDF-PRACTICE-PW.1`, `SSDF-TASK-PW.1.2` + 1 more)
  - MITRE CWE — Software Development View (v4.19.1) — 3 refs (`CWE-267`, `CWE-391`, `CWE-654`)
  - HIPAA Security Rule — 3 refs (`HIPAA-164-308a5`, `HIPAA-164-308a6`, `HIPAA-164-316a`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.TA0007`, `AML.T0054`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 2 refs (`NIST-AI-100-2-E2025-3.3.3`, `NIST-AI-100-2-E2025-3.4.4`)
  - NIST AI RMF 1.0 — 2 refs (`NIST-AI-RMF-GOVERN-3.2`, `NIST-AI-RMF-GOVERN-6`)
  - PCI Secure SLC v1.1 — 2 refs (`PCISSLC-3.2`, `PCISSLC-3.3`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 2 refs (`SCAGILE-OPS-8`, `SCAGILE-EXP-2`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM04-2025`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-MINIMUM-BAR`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C7`)

#### `ACM-RPR-010` — Change Review Control For Security-Relevant Baseline Deviations

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 4 keywords × 18 ocorrências; principais: baseline, change, record, review)
- **Substrate v7 contributing sources** (95 grounded claims em 11 fontes):
  - NIST SP 800-53 Rev. 5 — 55 refs (`SP800-53-AC-1`, `SP800-53-AC-2`, `SP800-53-AC-2.4` + 2 more)
  - CIS Controls v8.1.2 — 10 refs (`CIS-3.1`, `CIS-3.2`, `CIS-3.7` + 2 more)
  - OWASP SAMM v2.1 — 10 refs (`SAMM-ACTIVITY-D_TA_3_A`, `SAMM-ACTIVITY-G_EG_3_A`, `SAMM-ACTIVITY-G_PC_2_B` + 2 more)
  - PCI DSS v4.0.1 — 8 refs (`PCI-6.2.3`, `PCI-6.5.1`, `PCI-6.5.2` + 2 more)
  - OWASP DSOMM — 4 refs (`DSOMM-ACTIVITY-95CAEF9636ED458CA0875C35D4F9DEC2`, `DSOMM-ACTIVITY-3F63BDBCC75F4780A941E6AD42E894E1`, `DSOMM-ACTIVITY-0C10A7F7F78F49F2943D19FDEF248FED` + 1 more)
  - OWASP ASVS v5.0.0 — 3 refs (`ASVS-REQ-V7.5.1`, `ASVS-REQ-V8.3.2`, `ASVS-REQ-V14.2.7`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-447`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-32`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-GOVERN-1.5`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML07-2023`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-5.1`)


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
