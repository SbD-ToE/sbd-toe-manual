# 25. Rastreabilidade — Dependências, SBOM e SCA

## Sumário

Este capítulo é a **âncora primária** das slices AppSec Core V1: `ACO-SCBI` (Integridade da supply chain de software e do build).

Cobertura V1 entity-level: **20 entidades** primárias (7 ControlObjectives + 7 Practices + 6 Mechanisms). Cada entidade é listada abaixo com cobertura no Manual (prose anchor) e fontes externas substrate v7 que contribuem para a sua substantive coverage.

---

## Slice `ACO-SCBI` — Integridade da supply chain de software e do build

### ControlObjectives (7)

#### `ACO-SCBI-001` — Dependency Inventory And SBOM Traceability

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (48 grounded claims em 12 fontes):
  - NIST SP 800-53 Rev. 5 — 19 refs (`SP800-53-CM-8`, `SP800-53-CM-8.1`, `SP800-53-CM-8.2` + 2 more)
  - CIS Controls v8.1.2 — 8 refs (`CIS-1`, `CIS-1.1`, `CIS-2` + 2 more)
  - OWASP DSOMM — 3 refs (`DSOMM-ACTIVITY-2858AC12017940D99ACF1B839C030473`, `DSOMM-ACTIVITY-2A44B708734F4463B0CB86DC46344B2F`, `DSOMM-ACTIVITY-13E9757E58E24277BC0FEADC674891E6`)
  - OWASP SAMM v2.1 — 3 refs (`SAMM-ACTIVITY-I_SB_1_B`, `SAMM-ACTIVITY-O_EM_1_A`, `SAMM-ACTIVITY-O_EM_1_B`)
  - NIST SSDF (SP 800-218 v1.1) — 3 refs (`SSDF-TASK-PO.1.3`, `SSDF-TASK-PO.3.1`, `SSDF-TASK-PW.4.2`)
  - OWASP ASVS v5.0.0 — 2 refs (`ASVS-REQ-V15.1.2`, `ASVS-REQ-V16.1.1`)
  - MITRE CAPEC v3.9 — 2 refs (`CAPEC-446`, `CAPEC-516`)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-1103`, `CWE-1104`)
  - PCI DSS v4.0.1 — 2 refs (`PCI-6.3.2`, `PCI-12.5.1`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 2 refs (`SCAGILE-OPS-5`, `SCAGILE-OPS-6`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP04-2025`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEV-MANIFEST`)

#### `ACO-SCBI-002` — Dependency Risk Evaluation And Policy Gating

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (17 grounded claims em 6 fontes):
  - NIST SP 800-53 Rev. 5 — 7 refs (`SP800-53-CA-7.4`, `SP800-53-PM-9`, `SP800-53-PM-28` + 2 more)
  - NIST AI RMF 1.0 — 6 refs (`NIST-AI-RMF-GOVERN-1.3`, `NIST-AI-RMF-GOVERN-1.5`, `NIST-AI-RMF-GOVERN-2` + 2 more)
  - CIS Controls v8.1.2 — 1 refs (`CIS-15.2`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-D_TA_3_A`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-12.3.2`)

#### `ACO-SCBI-003` — Controlled Dependency And Image Sources

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (28 grounded claims em 6 fontes):
  - NIST SP 800-53 Rev. 5 — 19 refs (`SP800-53-AC-3.3`, `SP800-53-AC-3.9`, `SP800-53-AC-3.11` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 4 refs (`CWE-1220`, `CWE-1230`, `CWE-434` + 1 more)
  - CIS Controls v8.1.2 — 2 refs (`CIS-2.5`, `CIS-2.6`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 1 refs (`NIST-AI-100-2-E2025-4.2.1`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-066084C6113546359CC59E75C7C5459F`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C7`)

#### `ACO-SCBI-004` — Build Definition And Execution Integrity

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (81 grounded claims em 14 fontes):
  - OWASP SAMM v2.1 — 17 refs (`SAMM-ACTIVITY-D_SA_3_A`, `SAMM-ACTIVITY-D_SA_3_B`, `SAMM-ACTIVITY-I_SB_1_A` + 2 more)
  - OWASP DSOMM — 13 refs (`DSOMM-ACTIVITY-F6F7737F25A943178DE209BF59F29B5B`, `DSOMM-ACTIVITY-9F10792761E9457485AD3F2B4BCA8665`, `DSOMM-ACTIVITY-67E1A9AA9FBF4EC5A2DE400F01960C51` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 13 refs (`SSDF-PRACTICE-PO.1`, `SSDF-PRACTICE-PO.4`, `SSDF-PRACTICE-PO.5` + 2 more)
  - MITRE CAPEC v3.9 — 7 refs (`CAPEC-443`, `CAPEC-523`, `CAPEC-524` + 2 more)
  - NIST SP 800-53 Rev. 5 — 7 refs (`SP800-53-CM-7.7`, `SP800-53-SA-10.4`, `SP800-53-SA-15` + 2 more)
  - PCI Secure SLC v1.1 — 5 refs (`PCISSLC-2.3`, `PCISSLC-2.6`, `PCISSLC-6.1` + 2 more)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 5 refs (`SCAGILE-OPS-2`, `SCAGILE-OPS-8`, `SCAGILE-OPS-9` + 2 more)
  - SLSA Specification v1.0 — Build Track — 3 refs (`SLSA-BUILD-L3`, `SLSA-PRINCIPLE-TRUST-CODE`, `SLSA-BUILD-PLATFORM-ISOLATION`)
  - OWASP ASVS v5.0.0 — 2 refs (`ASVS-REQ-V15.2.3`, `ASVS-REQ-V15.4.2`)
  - CIS Controls v8.1.2 — 2 refs (`CIS-16.1`, `CIS-16.12`)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-1127`, `CWE-733`)
  - PCI DSS v4.0.1 — 2 refs (`PCI-6.5.3`, `PCI-6.5.4`)
  - SAFECode — Software Integrity Controls (2010) — 2 refs (`SCSIC-DEVELOPMENT`, `SCSIC-DEV-BUILD`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-TOOL-DESIGN`)

#### `ACO-SCBI-005` — Release Promotion And Human Approval Integrity

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (46 grounded claims em 11 fontes):
  - NIST SP 800-53 Rev. 5 — 27 refs (`SP800-53-AC-4.9`, `SP800-53-AC-13`, `SP800-53-AC-14` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 5 refs (`CWE-205`, `CWE-250`, `CWE-268` + 2 more)
  - PCI DSS v4.0.1 — 3 refs (`PCI-3.7.8`, `PCI-7.2.3`, `PCI-9.2.2`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0054`, `AML.M0029`)
  - NIST AI RMF 1.0 — 2 refs (`NIST-AI-RMF-GOVERN-1`, `NIST-AI-RMF-GOVERN-1.7`)
  - OWASP SAMM v2.1 — 2 refs (`SAMM-ACTIVITY-G_PC_2_B`, `SAMM-ACTIVITY-O_OM_3_A`)
  - OWASP ASVS v5.0.0 — 1 refs (`ASVS-REQ-V2.3.5`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-5`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-312b`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-3F63BDBCC75F4780A941E6AD42E894E1`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM01-2025`)

#### `ACO-SCBI-006` — Artifact Attestation And Provenance Integrity

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (42 grounded claims em 14 fontes):
  - NIST SP 800-53 Rev. 5 — 8 refs (`SP800-53-CP-9.1`, `SP800-53-IA-12`, `SP800-53-SA-10.3` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 6 refs (`AML.TA0009`, `AML.T0002`, `AML.T0007` + 2 more)
  - OWASP DSOMM — 5 refs (`DSOMM-ACTIVITY-F3C4971E9F4D4E598ED0F0BDB6262477`, `DSOMM-ACTIVITY-A854B48D83BD4F8D8621A0BDD470837F`, `DSOMM-ACTIVITY-8F2B4D5A3C1E4B7A9D8F2E6C4A1B5D7F` + 2 more)
  - SLSA Specification v1.0 — Build Track — 5 refs (`SLSA-BUILD-L1`, `SLSA-PRINCIPLE-PREFER-ATTESTATIONS`, `SLSA-PRODUCER-DISTRIBUTE-PROVENANCE` + 2 more)
  - MITRE CAPEC v3.9 — 4 refs (`CAPEC-523`, `CAPEC-524`, `CAPEC-530` + 1 more)
  - NIST SSDF (SP 800-218 v1.1) — 3 refs (`SSDF-PRACTICE-PS.2`, `SSDF-TASK-PS.2.1`, `SSDF-TASK-PS.3.1`)
  - OWASP ASVS v5.0.0 — 2 refs (`ASVS-REQ-V6.7.1`, `ASVS-REQ-V11.1.2`)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-353`, `CWE-354`)
  - PCI Secure SLC v1.1 — 2 refs (`PCISSLC-7.1`, `PCISSLC-7.2`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MAP-2.3`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM04-2025`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML08-2023`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-I_SB_1_A`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-SOURCING-CONTRACT`)

#### `ACO-SCBI-007` — Container Image Supply Integrity

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (19 grounded claims em 5 fontes):
  - OWASP DSOMM — 9 refs (`DSOMM-ACTIVITY-DA4FF665DCB94E939D2048CDEDC50FC2`, `DSOMM-ACTIVITY-34869EAFF2E14926B0BD28C43402F057`, `DSOMM-ACTIVITY-16E39C8F5336400188EDA552D2447531` + 2 more)
  - NIST SP 800-53 Rev. 5 — 5 refs (`SP800-53-SA-12.3`, `SP800-53-SI-7.4`, `SP800-53-SR-4.4` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 3 refs (`AML.T0010.004`, `AML.M0032`, `AML.CS0028`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-19`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)


### Practices (7)

#### `ACP-SCBI-001` — Build-Linked SBOM Generation

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (11 grounded claims em 6 fontes):
  - OWASP SAMM v2.1 — 4 refs (`SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-I_SB_1_A`, `SAMM-ACTIVITY-I_SB_3_A` + 1 more)
  - OWASP DSOMM — 2 refs (`DSOMM-ACTIVITY-2858AC12017940D99ACF1B839C030473`, `DSOMM-ACTIVITY-2A44B708734F4463B0CB86DC46344B2F`)
  - SLSA Specification v1.0 — Build Track — 2 refs (`SLSA-PRODUCER-CHOOSE-BUILD-PLATFORM`, `SLSA-PRODUCER-CONSISTENT-BUILD`)
  - OWASP ASVS v5.0.0 — 1 refs (`ASVS-REQ-V15.1.2`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.T0061`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-5.2`)

#### `ACP-SCBI-002` — Automated Dependency And Image Risk Gating

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (164 grounded claims em 20 fontes):
  - OWASP DSOMM — 24 refs (`DSOMM-ACTIVITY-A340F46B63604CB8847BA0D3483D09D3`, `DSOMM-ACTIVITY-0DE465A655A74343AF79948BB5FF10BA`, `DSOMM-ACTIVITY-8AE0B92C10E04602BA227524D6AED488` + 2 more)
  - OWASP SAMM v2.1 — 20 refs (`SAMM-ACTIVITY-D_TA_1_A`, `SAMM-ACTIVITY-D_TA_2_A`, `SAMM-ACTIVITY-D_TA_3_A` + 2 more)
  - MITRE CAPEC v3.9 — 17 refs (`CAPEC-35`, `CAPEC-187`, `CAPEC-212` + 2 more)
  - NIST SP 800-53 Rev. 5 — 17 refs (`SP800-53-CA-7.4`, `SP800-53-CM-5.7`, `SP800-53-MA-3.2` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 15 refs (`SSDF-PRACTICE-PW.1`, `SSDF-PRACTICE-PW.5`, `SSDF-PRACTICE-PW.6` + 2 more)
  - PCI DSS v4.0.1 — 14 refs (`PCI-REQ-5`, `PCI-5.2.1`, `PCI-5.2.3` + 2 more)
  - CIS Controls v8.1.2 — 12 refs (`CIS-7.1`, `CIS-7.2`, `CIS-7.3` + 2 more)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 11 refs (`NIST-AI-100-2-E2025-2.1.2`, `NIST-AI-100-2-E2025-2.1.5`, `NIST-AI-100-2-E2025-2.3` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 10 refs (`AML.T0020`, `AML.T0059`, `AML.T0011.001` + 2 more)
  - OWASP ASVS v5.0.0 — 4 refs (`ASVS-REQ-V1.3.4`, `ASVS-REQ-V15.1.1`, `ASVS-REQ-V15.2.3` + 1 more)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 4 refs (`SCAGILE-OPS-7`, `SCAGILE-OPS-10`, `SCAGILE-OPS-11` + 1 more)
  - NIST AI RMF 1.0 — 3 refs (`NIST-AI-RMF-MEASURE-2.6`, `NIST-AI-RMF-MEASURE-4`, `NIST-AI-RMF-MEASURE-4.3`)
  - OWASP LLM Top 10 (2025) — 3 refs (`LLM03-2025`, `LLM04-2025`, `LLM09-2025`)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-209`, `CWE-676`)
  - PCI Secure SLC v1.1 — 2 refs (`PCISSLC-3.2`, `PCISSLC-4.1`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 2 refs (`SCFPSSD-THREAT-MODELING`, `SCFPSSD-THIRD-PARTY`)
  - EU Digital Operational Resilience Act (DORA) — 1 refs (`DORA-ART-24`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-RISK-LANDSCAPE`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP04-2025`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML01-2023`)

#### `ACP-SCBI-003` — Approved Source And Registry Governance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (56 grounded claims em 11 fontes):
  - NIST SP 800-53 Rev. 5 — 27 refs (`SP800-53-AC-3.11`, `SP800-53-AC-4.19`, `SP800-53-AT-1` + 2 more)
  - CIS Controls v8.1.2 — 7 refs (`CIS-2.2`, `CIS-2.6`, `CIS-4.1` + 2 more)
  - SAFECode — Software Integrity Controls (2010) — 5 refs (`SCSIC-SOURCING`, `SCSIC-SOURCING-OSS`, `SCSIC-DEVELOPMENT` + 2 more)
  - OWASP SAMM v2.1 — 4 refs (`SAMM-ACTIVITY-G_PC_1_A`, `SAMM-ACTIVITY-G_PC_1_B`, `SAMM-ACTIVITY-G_PC_2_B` + 1 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 3 refs (`AML.T0036`, `AML.T0095.000`, `AML.M0005`)
  - PCI DSS v4.0.1 — 3 refs (`PCI-3.4.2`, `PCI-7.2.6`, `PCI-9.4.7`)
  - MITRE CAPEC v3.9 — 2 refs (`CAPEC-647`, `CAPEC-678`)
  - SLSA Specification v1.0 — Build Track — 2 refs (`SLSA-PRINCIPLE-TRUST-CODE`, `SLSA-VERIFY-EXPECTATIONS`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-994151396B50441B89E10AA59ACCD43D`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-GOVERNANCE`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PW.4.1`)

#### `ACP-SCBI-004` — Pipeline Definition As Reviewed Code

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (1 grounded claims em 1 fontes):
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM03-2025`)

#### `ACP-SCBI-005` — Governed Promotion And Release Approval

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 7 keywords × 89 ocorrências; principais: approval, enforce, gates, generation, policy)
- **Substrate v7 contributing sources** (202 grounded claims em 18 fontes):
  - NIST SP 800-53 Rev. 5 — 122 refs (`SP800-53-AC-1`, `SP800-53-AC-2`, `SP800-53-AC-2.4` + 2 more)
  - PCI DSS v4.0.1 — 23 refs (`PCI-REQ-12`, `PCI-1.1.1`, `PCI-1.5.1` + 2 more)
  - MITRE CAPEC v3.9 — 8 refs (`CAPEC-2`, `CAPEC-13`, `CAPEC-36` + 2 more)
  - HIPAA Security Rule — 8 refs (`HIPAA-164-308a1`, `HIPAA-164-308a2`, `HIPAA-164-308a4` + 2 more)
  - PCI Secure SLC v1.1 — 8 refs (`PCISSLC-2.1`, `PCISSLC-2.2`, `PCISSLC-2.3` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 6 refs (`CWE-268`, `CWE-408`, `CWE-412` + 2 more)
  - OWASP SAMM v2.1 — 6 refs (`SAMM-ACTIVITY-G_EG_2_A`, `SAMM-ACTIVITY-I_DM_1_A`, `SAMM-ACTIVITY-O_IM_2_B` + 2 more)
  - CIS Controls v8.1.2 — 4 refs (`CIS-6.6`, `CIS-6.8`, `CIS-13.11` + 1 more)
  - NIST AI RMF 1.0 — 3 refs (`NIST-AI-RMF-GOVERN-1`, `NIST-AI-RMF-GOVERN-1.3`, `NIST-AI-RMF-GOVERN-4`)
  - EU GDPR (RGPD) — 2 refs (`GDPR-ART-5`, `GDPR-ART-32`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.TA0012`, `AML.T0054`)
  - OWASP DSOMM — 2 refs (`DSOMM-ACTIVITY-1B9281B948E24C019AC69DB9931C4885`, `DSOMM-ACTIVITY-3F63BDBCC75F4780A941E6AD42E894E1`)
  - OWASP Machine Learning Top 10 — 2 refs (`ML06-2023`, `ML08-2023`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 2 refs (`SCFPSSD-SECURITY-CONTROLS`, `SCFPSSD-FINDINGS`)
  - OWASP ASVS v5.0.0 — 1 refs (`ASVS-REQ-V2.3.5`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-13`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C7`)

#### `ACP-SCBI-006` — Artifact Signature And Provenance Validation

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (69 grounded claims em 17 fontes):
  - NIST SP 800-53 Rev. 5 — 31 refs (`SP800-53-AU-10.5`, `SP800-53-AU-12.1`, `SP800-53-AU-12.2` + 2 more)
  - OWASP ASVS v5.0.0 — 10 refs (`ASVS-REQ-V2.1.2`, `ASVS-REQ-V4.1.5`, `ASVS-REQ-V6.7.1` + 2 more)
  - OWASP DSOMM — 4 refs (`DSOMM-ACTIVITY-9F10792761E9457485AD3F2B4BCA8665`, `DSOMM-ACTIVITY-830570280B774D2E813540969768AE88`, `DSOMM-ACTIVITY-A854B48D83BD4F8D8621A0BDD470837F` + 1 more)
  - PCI DSS v4.0.1 — 4 refs (`PCI-1.1.2`, `PCI-2.1.2`, `PCI-3.3.2` + 1 more)
  - MITRE CWE — Software Development View (v4.19.1) — 3 refs (`CWE-347`, `CWE-353`, `CWE-354`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 3 refs (`AML.T0002`, `AML.T0035`, `AML.M0025`)
  - SLSA Specification v1.0 — Build Track — 3 refs (`SLSA-BUILD-L1`, `SLSA-PRODUCER-DISTRIBUTE-PROVENANCE`, `SLSA-VERIFY-BUILD-LEVEL`)
  - OWASP SAMM v2.1 — 2 refs (`SAMM-ACTIVITY-I_SB_1_A`, `SAMM-ACTIVITY-I_SD_3_A`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-476`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-11`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-312c1`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MAP-2.3`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM04-2025`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML08-2023`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A08-2021`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DELIVERY-SIGNING`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PS.3.2`)

#### `ACP-SCBI-007` — Trusted Container Image Supply

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 4 keywords × 164 ocorrências; principais: build, container, policy, supply)
- **Substrate v7 contributing sources** (26 grounded claims em 6 fontes):
  - NIST SP 800-53 Rev. 5 — 11 refs (`SP800-53-AC-19.5`, `SP800-53-MP-5`, `SP800-53-MP-5.1` + 2 more)
  - OWASP DSOMM — 6 refs (`DSOMM-ACTIVITY-16E39C8F5336400188EDA552D2447531`, `DSOMM-ACTIVITY-485A33837F2E4DBABB84479377070904`, `DSOMM-ACTIVITY-6B96E5A0CE344EA4A88F469D3B84546E` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 4 refs (`AML.T0010.004`, `AML.T0105`, `AML.M0032` + 1 more)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-426`, `CWE-829`)
  - PCI DSS v4.0.1 — 2 refs (`PCI-1.4.4`, `PCI-9.4.1`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-677`)


### Mechanisms (6)

#### `ACM-SCBI-001` — Versioned Pipelines

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (36 grounded claims em 8 fontes):
  - NIST SP 800-53 Rev. 5 — 16 refs (`SP800-53-AU-1`, `SP800-53-AU-2.3`, `SP800-53-CA-1` + 2 more)
  - OWASP SAMM v2.1 — 9 refs (`SAMM-ACTIVITY-G_PC_1_A`, `SAMM-ACTIVITY-G_PC_3_B`, `SAMM-ACTIVITY-I_SB_1_A` + 2 more)
  - PCI Secure SLC v1.1 — 3 refs (`PCISSLC-5.1`, `PCISSLC-5.2`, `PCISSLC-10.1`)
  - OWASP DSOMM — 2 refs (`DSOMM-ACTIVITY-C7D99B18C3E14D22B2E39AA9146C0B17`, `DSOMM-ACTIVITY-86D490B9D7984A5BA011AB9688014C46`)
  - OWASP LLM Top 10 (2025) — 2 refs (`LLM03-2025`, `LLM10-2025`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 2 refs (`SCFPSSD-MITIGATIONS`, `SCFPSSD-LIFECYCLE-FEEDBACK`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-1.2.4`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-OPS-6`)

#### `ACM-SCBI-002` — Automated Security Scanners

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (362 grounded claims em 19 fontes):
  - NIST SP 800-53 Rev. 5 — 69 refs (`SP800-53-AC-2.4`, `SP800-53-AC-4.28`, `SP800-53-AC-15` + 2 more)
  - OWASP SAMM v2.1 — 53 refs (`SAMM-ACTIVITY-D_SA_1_A`, `SAMM-ACTIVITY-D_SA_1_B`, `SAMM-ACTIVITY-D_SA_2_A` + 2 more)
  - OWASP DSOMM — 43 refs (`DSOMM-ACTIVITY-67E1A9AA9FBF4EC5A2DE400F01960C51`, `DSOMM-ACTIVITY-8AE0B92C10E04602BA227524D6AED488`, `DSOMM-ACTIVITY-08F27C262C6A47FE94585E88F188085D` + 2 more)
  - CIS Controls v8.1.2 — 41 refs (`CIS-2.4`, `CIS-3.13`, `CIS-4.1` + 2 more)
  - MITRE CAPEC v3.9 — 31 refs (`CAPEC-35`, `CAPEC-44`, `CAPEC-169` + 2 more)
  - PCI DSS v4.0.1 — 25 refs (`PCI-REQ-1`, `PCI-REQ-2`, `PCI-REQ-5` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 25 refs (`SSDF-PRACTICE-PO.4`, `SSDF-PRACTICE-PO.5`, `SSDF-PRACTICE-PS.1` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 24 refs (`AML.TA0007`, `AML.TA0001`, `AML.T0001` + 2 more)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 13 refs (`SCAGILE-OPS-1`, `SCAGILE-OPS-2`, `SCAGILE-OPS-7` + 2 more)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 8 refs (`NIST-AI-100-2-E2025-2.3.3`, `NIST-AI-100-2-E2025-3.2`, `NIST-AI-100-2-E2025-3.2.3` + 2 more)
  - OWASP ASVS v5.0.0 — 7 refs (`ASVS-REQ-V2.4.1`, `ASVS-REQ-V5.4.3`, `ASVS-REQ-V11.4.2` + 2 more)
  - OWASP Machine Learning Top 10 — 5 refs (`ML01-2023`, `ML06-2023`, `ML07-2023` + 2 more)
  - PCI Secure SLC v1.1 — 5 refs (`PCISSLC-2.6`, `PCISSLC-3.2`, `PCISSLC-3.4` + 2 more)
  - OWASP LLM Top 10 (2025) — 4 refs (`LLM03-2025`, `LLM04-2025`, `LLM08-2025` + 1 more)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 3 refs (`SCFPSSD-CODING-STANDARDS`, `SCFPSSD-TESTING`, `SCFPSSD-FIX-VULN`)
  - OWASP MCP — Secure Server Development v1.0 — 2 refs (`OWASP-MCP-RISK-LANDSCAPE`, `OWASP-MCP-CONTINUOUS-VALIDATION`)
  - OWASP Proactive Controls (2018) — 2 refs (`OPC-C2`, `OPC-C9`)
  - OWASP MCP — Third-Party Servers v1.0 — 1 refs (`OWASP-MCP-3P-GOVERNANCE-REGISTRY`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A09-2021`)

#### `ACM-SCBI-003` — Release Promotion Gates

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (96 grounded claims em 12 fontes):
  - NIST SP 800-53 Rev. 5 — 66 refs (`SP800-53-AC-1`, `SP800-53-AC-3.5`, `SP800-53-AC-3.9` + 2 more)
  - PCI DSS v4.0.1 — 7 refs (`PCI-3.7.2`, `PCI-3.7.3`, `PCI-3.7.4` + 2 more)
  - MITRE CAPEC v3.9 — 5 refs (`CAPEC-2`, `CAPEC-36`, `CAPEC-426` + 2 more)
  - OWASP SAMM v2.1 — 4 refs (`SAMM-ACTIVITY-G_EG_2_A`, `SAMM-ACTIVITY-I_DM_1_A`, `SAMM-ACTIVITY-O_IM_2_B` + 1 more)
  - PCI Secure SLC v1.1 — 4 refs (`PCISSLC-2.2`, `PCISSLC-2.5`, `PCISSLC-5.1` + 1 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 3 refs (`AML.TA0012`, `AML.T0054`, `AML.M0000`)
  - CIS Controls v8.1.2 — 2 refs (`CIS-6.6`, `CIS-17.9`)
  - OWASP ASVS v5.0.0 — 1 refs (`ASVS-REQ-V2.3.5`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-408`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-5`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-1B9281B948E24C019AC69DB9931C4885`)

#### `ACM-SCBI-004` — Artifact Signing And Attestation

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (104 grounded claims em 18 fontes):
  - NIST SP 800-53 Rev. 5 — 49 refs (`SP800-53-AU-9.1`, `SP800-53-AU-9.3`, `SP800-53-AU-10.2` + 2 more)
  - MITRE CAPEC v3.9 — 10 refs (`CAPEC-206`, `CAPEC-459`, `CAPEC-473` + 2 more)
  - OWASP ASVS v5.0.0 — 8 refs (`ASVS-REQ-V4.1.5`, `ASVS-REQ-V6.7.1`, `ASVS-REQ-V6.8.2` + 2 more)
  - OWASP DSOMM — 8 refs (`DSOMM-ACTIVITY-A340F46B63604CB8847BA0D3483D09D3`, `DSOMM-ACTIVITY-F3C4971E9F4D4E598ED0F0BDB6262477`, `DSOMM-ACTIVITY-9F10792761E9457485AD3F2B4BCA8665` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 4 refs (`CWE-347`, `CWE-353`, `CWE-354` + 1 more)
  - PCI DSS v4.0.1 — 4 refs (`PCI-1.1.2`, `PCI-2.1.2`, `PCI-3.3.2` + 1 more)
  - SLSA Specification v1.0 — Build Track — 4 refs (`SLSA-BUILD-L1`, `SLSA-BUILD-L2`, `SLSA-BUILD-L3` + 1 more)
  - OWASP SAMM v2.1 — 3 refs (`SAMM-ACTIVITY-I_SB_1_A`, `SAMM-ACTIVITY-I_SD_3_A`, `SAMM-ACTIVITY-V_RT_2_B`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0035`, `AML.M0014`)
  - OWASP Machine Learning Top 10 — 2 refs (`ML06-2023`, `ML08-2023`)
  - PCI Secure SLC v1.1 — 2 refs (`PCISSLC-6.1`, `PCISSLC-7.1`)
  - NIST SSDF (SP 800-218 v1.1) — 2 refs (`SSDF-PRACTICE-PS.2`, `SSDF-TASK-PS.2.1`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-11`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-312c1`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MAP-2.3`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM04-2025`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A08-2021`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DELIVERY-SIGNING`)

#### `ACM-SCBI-005` — Build And Image Inventory Generation

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (16 grounded claims em 7 fontes):
  - OWASP DSOMM — 5 refs (`DSOMM-ACTIVITY-2858AC12017940D99ACF1B839C030473`, `DSOMM-ACTIVITY-2A44B708734F4463B0CB86DC46344B2F`, `DSOMM-ACTIVITY-830570280B774D2E813540969768AE88` + 2 more)
  - CIS Controls v8.1.2 — 4 refs (`CIS-1`, `CIS-1.1`, `CIS-2.1` + 1 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0060`, `AML.M0023`)
  - NIST SP 800-53 Rev. 5 — 2 refs (`SP800-53-CM-8`, `SP800-53-SR-4.4`)
  - OWASP ASVS v5.0.0 — 1 refs (`ASVS-REQ-V15.1.2`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-12.5.1`)
  - SLSA Specification v1.0 — Build Track — 1 refs (`SLSA-PRODUCER-CONSISTENT-BUILD`)

#### `ACM-SCBI-006` — Registry Allowlisting And Approved Source Enforcement

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 5 keywords × 29 ocorrências; principais: enforcement, proxy, registries, registry, source)
- **Substrate v7 contributing sources** (70 grounded claims em 14 fontes):
  - NIST SP 800-53 Rev. 5 — 34 refs (`SP800-53-AC-3.3`, `SP800-53-AC-3.11`, `SP800-53-AC-4.6` + 2 more)
  - PCI DSS v4.0.1 — 10 refs (`PCI-REQ-7`, `PCI-1.3.2`, `PCI-1.4.2` + 2 more)
  - MITRE CAPEC v3.9 — 4 refs (`CAPEC-51`, `CAPEC-203`, `CAPEC-571` + 1 more)
  - CIS Controls v8.1.2 — 4 refs (`CIS-2.2`, `CIS-2.5`, `CIS-2.6` + 1 more)
  - MITRE CWE — Software Development View (v4.19.1) — 4 refs (`CWE-1220`, `CWE-1230`, `CWE-183` + 1 more)
  - OWASP DSOMM — 3 refs (`DSOMM-ACTIVITY-994151396B50441B89E10AA59ACCD43D`, `DSOMM-ACTIVITY-5992C38C8597403589DBD15820D81C3A`, `DSOMM-ACTIVITY-6DF508EF86FC4C22BD9F646C3127CE7D`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0095.000`, `AML.M0001`)
  - OWASP SAMM v2.1 — 2 refs (`SAMM-ACTIVITY-G_PC_1_B`, `SAMM-ACTIVITY-G_PC_2_B`)
  - SAFECode — Software Integrity Controls (2010) — 2 refs (`SCSIC-SOURCING-OSS`, `SCSIC-DEV-REPO`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-19`)
  - Anthropic MCP — Official Security Foundations (2025) — 1 refs (`MCP-AUTH-DISCOVERY-METADATA`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML06-2023`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-8.1`)
  - SLSA Specification v1.0 — Build Track — 1 refs (`SLSA-VERIFY-EXPECTATIONS`)


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
