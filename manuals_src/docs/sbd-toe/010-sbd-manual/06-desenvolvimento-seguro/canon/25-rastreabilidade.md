# 25. Rastreabilidade — Desenvolvimento Seguro

## Sumário

Este capítulo é a **âncora primária** das slices AppSec Core V1: `ACO-IVF` (Validação de input, parsing seguro e tratamento controlado de erros), `ACO-SPC` (Gestão de segredos, configuração protegida e identidades operacionais).

Cobertura V1 entity-level: **37 entidades** primárias (15 ControlObjectives + 13 Practices + 9 Mechanisms). Cada entidade é listada abaixo com cobertura no Manual (prose anchor) e fontes externas substrate v7 que contribuem para a sua substantive coverage.

---

## Slice `ACO-IVF` — Validação de input, parsing seguro e tratamento controlado de erros

### ControlObjectives (8)

#### `ACO-IVF-001` — External Input Contract Validation

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (22 grounded claims em 8 fontes):
  - NIST SP 800-53 Rev. 5 — 9 refs (`SP800-53-AC-20`, `SP800-53-AC-20.1`, `SP800-53-CA-3.5` + 2 more)
  - OWASP ASVS v5.0.0 — 4 refs (`ASVS-REQ-V2.1.1`, `ASVS-REQ-V2.2.1`, `ASVS-REQ-V2.2.2` + 1 more)
  - MITRE CWE — Software Development View (v4.19.1) — 3 refs (`CWE-1284`, `CWE-1286`, `CWE-1287`)
  - OWASP LLM Top 10 (2025) — 2 refs (`LLM02-2025`, `LLM10-2025`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-15.4`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C5`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-11.4.3`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-SOURCING-CONTRACT`)

#### `ACO-IVF-002` — Schema, Type And Allowlist Discipline

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (30 grounded claims em 9 fontes):
  - NIST SP 800-53 Rev. 5 — 10 refs (`SP800-53-AC-3.11`, `SP800-53-AC-4.1`, `SP800-53-AC-4.5` + 2 more)
  - MITRE CAPEC v3.9 — 8 refs (`CAPEC-13`, `CAPEC-80`, `CAPEC-95` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 4 refs (`CWE-1056`, `CWE-1070`, `CWE-1117` + 1 more)
  - CIS Controls v8.1.2 — 3 refs (`CIS-2.5`, `CIS-2.6`, `CIS-3.3`)
  - OWASP ASVS v5.0.0 — 1 refs (`ASVS-REQ-V9.1.2`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.T0054`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-6DF508EF86FC4C22BD9F646C3127CE7D`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-PROMPT-INJECTION`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-D_SA_2_B`)

#### `ACO-IVF-003` — Injection-Resistant Input Handling And Dangerous Pattern Exclusion

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (75 grounded claims em 10 fontes):
  - MITRE CAPEC v3.9 — 42 refs (`CAPEC-3`, `CAPEC-6`, `CAPEC-7` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 12 refs (`CWE-115`, `CWE-186`, `CWE-242` + 2 more)
  - OWASP ASVS v5.0.0 — 5 refs (`ASVS-REQ-V1.2.4`, `ASVS-REQ-V1.2.7`, `ASVS-REQ-V1.2.8` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 5 refs (`AML.T0051`, `AML.T0051.000`, `AML.T0051.001` + 2 more)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 4 refs (`NIST-AI-100-2-E2025-3.1.3`, `NIST-AI-100-2-E2025-3.3`, `NIST-AI-100-2-E2025-3.4` + 1 more)
  - OWASP DSOMM — 2 refs (`DSOMM-ACTIVITY-00E91A8A397246928679674AB8547486`, `DSOMM-ACTIVITY-5E0FF85BEC894EF096B15695FA0025DC`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 2 refs (`MCP05-2025`, `MCP06-2025`)
  - NIST SP 800-53 Rev. 5 — 1 refs (`SP800-53-SC-41`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM02-2025`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A03-2021`)

#### `ACO-IVF-004` — Validation Before Internal Use And Trust Crossing

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (14 grounded claims em 5 fontes):
  - NIST SP 800-53 Rev. 5 — 5 refs (`SP800-53-AC-4.19`, `SP800-53-CA-3.6`, `SP800-53-CA-3.7` + 2 more)
  - OWASP ASVS v5.0.0 — 4 refs (`ASVS-REQ-V2.3.1`, `ASVS-REQ-V2.3.3`, `ASVS-REQ-V2.3.5` + 1 more)
  - CIS Controls v8.1.2 — 2 refs (`CIS-3.4`, `CIS-18.4`)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-346`, `CWE-349`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-1.4.2`)

#### `ACO-IVF-005` — Controlled Failure And Non-Revealing Client Error Surface

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (198 grounded claims em 21 fontes):
  - NIST SP 800-53 Rev. 5 — 45 refs (`SP800-53-AC-3.5`, `SP800-53-AC-3.6`, `SP800-53-AC-3.9` + 2 more)
  - MITRE CAPEC v3.9 — 39 refs (`CAPEC-2`, `CAPEC-8`, `CAPEC-14` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 26 refs (`CWE-1058`, `CWE-1073`, `CWE-1118` + 2 more)
  - PCI DSS v4.0.1 — 17 refs (`PCI-1.2.2`, `PCI-1.2.3`, `PCI-2.2.5` + 2 more)
  - OWASP ASVS v5.0.0 — 16 refs (`ASVS-REQ-V1.4.3`, `ASVS-REQ-V4.2.5`, `ASVS-REQ-V6.1.1` + 2 more)
  - OWASP DSOMM — 12 refs (`DSOMM-ACTIVITY-760F1056B0EE4F22A35BF65446F944CA`, `DSOMM-ACTIVITY-E5386ABF91544752A1A8C3A8900F732D`, `DSOMM-ACTIVITY-ED715B38C34B40CD83FDCE807F306FC1` + 2 more)
  - PCI Secure SLC v1.1 — 7 refs (`PCISSLC-2.6`, `PCISSLC-3.2`, `PCISSLC-3.3` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 5 refs (`AML.T0049`, `AML.T0080.001`, `AML.T0094` + 2 more)
  - OWASP SAMM v2.1 — 5 refs (`SAMM-ACTIVITY-I_DM_1_A`, `SAMM-ACTIVITY-I_SB_3_B`, `SAMM-ACTIVITY-V_RT_1_A` + 2 more)
  - OWASP Top 10 (2021) — 4 refs (`TOP10-A01-2021`, `TOP10-A07-2021`, `TOP10-A08-2021` + 1 more)
  - CIS Controls v8.1.2 — 3 refs (`CIS-3.13`, `CIS-9.1`, `CIS-16`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 3 refs (`NIST-AI-100-2-E2025-2.1.2`, `NIST-AI-100-2-E2025-3.4.1`, `NIST-AI-100-2-E2025-4.1.3`)
  - OWASP MCP — Third-Party Servers v1.0 — 3 refs (`OWASP-MCP-3P-TOOL-POISONING`, `OWASP-MCP-3P-AUTH-AUTHZ-REGISTRATION`, `OWASP-MCP-3P-TOOLS-UTILITIES`)
  - NIST SSDF (SP 800-218 v1.1) — 3 refs (`SSDF-PRACTICE-RV.2`, `SSDF-TASK-PW.1.2`, `SSDF-TASK-RV.1.2`)
  - OWASP LLM Top 10 (2025) — 2 refs (`LLM07-2025`, `LLM10-2025`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 2 refs (`MCP02-2025`, `MCP07-2025`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 2 refs (`SCAGILE-OPS-7`, `SCAGILE-OPS-12`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - Anthropic MCP — Official Security Foundations (2025) — 1 refs (`MCP-AUTH-ERROR-HANDLING`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-DATA-VALIDATION`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-VULN-RESPONSE`)

#### `ACO-IVF-006` — Centralized Error Handling And Sensitive Error Logging Hygiene

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (120 grounded claims em 16 fontes):
  - NIST SP 800-53 Rev. 5 — 55 refs (`SP800-53-AC-4.24`, `SP800-53-AU-1`, `SP800-53-AU-2` + 2 more)
  - CIS Controls v8.1.2 — 13 refs (`CIS-3.14`, `CIS-4.9`, `CIS-7` + 2 more)
  - OWASP SAMM v2.1 — 11 refs (`SAMM-ACTIVITY-D_SA_3_B`, `SAMM-ACTIVITY-G_EG_2_B`, `SAMM-ACTIVITY-G_PC_3_A` + 2 more)
  - OWASP ASVS v5.0.0 — 10 refs (`ASVS-REQ-V16.1.1`, `ASVS-REQ-V16.2.1`, `ASVS-REQ-V16.2.2` + 2 more)
  - OWASP DSOMM — 8 refs (`DSOMM-ACTIVITY-95CAEF9636ED458CA0875C35D4F9DEC2`, `DSOMM-ACTIVITY-8B994601575E4EA5B228ACCB18C8E514`, `DSOMM-ACTIVITY-4ECED38A79044C45ADB050B663065540` + 2 more)
  - PCI DSS v4.0.1 — 8 refs (`PCI-1.2.4`, `PCI-2.2.3`, `PCI-5.3.4` + 2 more)
  - MITRE CAPEC v3.9 — 4 refs (`CAPEC-81`, `CAPEC-93`, `CAPEC-268` + 1 more)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 3 refs (`SCFPSSD-IAM`, `SCFPSSD-LOGGING`, `SCFPSSD-CODING-STANDARDS`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-779`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.M0024`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM10-2025`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP08-2025`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C9`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A09-2021`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-OPS-1`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PW.1.3`)

#### `ACO-IVF-007` — Input Validation And Safe Failure Integrity

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (19 grounded claims em 10 fontes):
  - NIST SP 800-53 Rev. 5 — 6 refs (`SP800-53-PE-5`, `SP800-53-SC-7`, `SP800-53-SC-7.24` + 2 more)
  - CIS Controls v8.1.2 — 3 refs (`CIS-16.1`, `CIS-16.8`, `CIS-16.9`)
  - MITRE CAPEC v3.9 — 2 refs (`CAPEC-522`, `CAPEC-624`)
  - OWASP Machine Learning Top 10 — 2 refs (`ML02-2023`, `ML09-2023`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-1289`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.T0011.000`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 1 refs (`NIST-AI-100-2-E2025-3.6`)
  - NIST AI RMF 1.0 — 1 refs (`NIST-AI-RMF-MEASURE-2.6`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-0DE465A655A74343AF79948BB5FF10BA`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-TOOL-DESIGN`)

#### `ACO-IVF-008` — Context-Aware Output Encoding And Rendering Safety

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (56 grounded claims em 7 fontes):
  - MITRE CAPEC v3.9 — 28 refs (`CAPEC-18`, `CAPEC-19`, `CAPEC-32` + 2 more)
  - OWASP ASVS v5.0.0 — 18 refs (`ASVS-REQ-V1.2.1`, `ASVS-REQ-V1.2.2`, `ASVS-REQ-V1.2.3` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 3 refs (`CWE-1021`, `CWE-79`, `CWE-838`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 3 refs (`AML.T0054`, `AML.T0077`, `AML.CS0029`)
  - NIST SP 800-53 Rev. 5 — 2 refs (`SP800-53-AC-4.29`, `SP800-53-AC-16.5`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-E1F37ABBD8484A3AB3DF65E91A89DCB7`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C4`)


### Practices (7)

#### `ACP-IVF-001` — Boundary Input Validation

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (16 grounded claims em 6 fontes):
  - MITRE CWE — Software Development View (v4.19.1) — 6 refs (`CWE-1173`, `CWE-1284`, `CWE-1285` + 2 more)
  - OWASP ASVS v5.0.0 — 4 refs (`ASVS-REQ-V1.1.1`, `ASVS-REQ-V2.2.2`, `ASVS-REQ-V4.2.3` + 1 more)
  - NIST SP 800-53 Rev. 5 — 2 refs (`SP800-53-SI-10`, `SP800-53-SI-10.2`)
  - OWASP LLM Top 10 (2025) — 2 refs (`LLM02-2025`, `LLM10-2025`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.M0033`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C5`)

#### `ACP-IVF-002` — Schema And Allowlist Enforcement

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 4 keywords × 13 ocorrências; principais: accepted, allowlist, enforcement, validation)
- **Substrate v7 contributing sources** (125 grounded claims em 18 fontes):
  - NIST SP 800-53 Rev. 5 — 34 refs (`SP800-53-AC-3`, `SP800-53-AC-3.8`, `SP800-53-AC-3.11` + 2 more)
  - OWASP ASVS v5.0.0 — 21 refs (`ASVS-REQ-V1.2.6`, `ASVS-REQ-V1.5.1`, `ASVS-REQ-V1.5.2` + 2 more)
  - PCI DSS v4.0.1 — 19 refs (`PCI-REQ-8`, `PCI-REQ-9`, `PCI-1.2.5` + 2 more)
  - MITRE CAPEC v3.9 — 12 refs (`CAPEC-13`, `CAPEC-58`, `CAPEC-80` + 2 more)
  - OWASP SAMM v2.1 — 10 refs (`SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-D_SA_2_B`, `SAMM-ACTIVITY-D_SA_3_B` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 8 refs (`CWE-1070`, `CWE-112`, `CWE-1230` + 2 more)
  - CIS Controls v8.1.2 — 3 refs (`CIS-2.5`, `CIS-2.6`, `CIS-2.7`)
  - OWASP DSOMM — 3 refs (`DSOMM-ACTIVITY-CF81922530CB47028E3260225EEDC33D`, `DSOMM-ACTIVITY-6DF508EF86FC4C22BD9F646C3127CE7D`, `DSOMM-ACTIVITY-070BB14BE04A4F3D896AA08EBA7A35F9`)
  - PCI Secure SLC v1.1 — 3 refs (`PCISSLC-6.1`, `PCISSLC-6.2`, `PCISSLC-8.1`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0054`, `AML.T0079`)
  - OWASP LLM Top 10 (2025) — 2 refs (`LLM01-2025`, `LLM06-2025`)
  - OWASP MCP — Secure Server Development v1.0 — 2 refs (`OWASP-MCP-TOOL-DESIGN`, `OWASP-MCP-PROMPT-INJECTION`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-5`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-312c1`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 1 refs (`NIST-AI-100-2-E2025-3.1.2`)
  - OWASP MCP — Third-Party Servers v1.0 — 1 refs (`OWASP-MCP-3P-CLIENT-SECURITY-DISCOVERY`)
  - SLSA Specification v1.0 — Build Track — 1 refs (`SLSA-BUILD-L1`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-PRACTICE-PW.7`)

#### `ACP-IVF-003` — Dangerous Pattern Exclusion

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (63 grounded claims em 11 fontes):
  - MITRE CAPEC v3.9 — 29 refs (`CAPEC-6`, `CAPEC-7`, `CAPEC-28` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 9 refs (`CWE-115`, `CWE-184`, `CWE-186` + 2 more)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 7 refs (`NIST-AI-100-2-E2025-2.3.3`, `NIST-AI-100-2-E2025-3.2.2`, `NIST-AI-100-2-E2025-3.3` + 2 more)
  - OWASP ASVS v5.0.0 — 6 refs (`ASVS-REQ-V1.2.8`, `ASVS-REQ-V1.2.9`, `ASVS-REQ-V1.3.2` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 5 refs (`AML.T0011`, `AML.T0068`, `AML.T0107` + 2 more)
  - OWASP DSOMM — 2 refs (`DSOMM-ACTIVITY-D918CD44A97243E9A974EFF3F4A5DCFE`, `DSOMM-ACTIVITY-D17DBFF01F10492AB4C717BB59A0A711`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM02-2025`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP06-2025`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-D_TA_2_A`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A03-2021`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-THREAT-MODELING`)

#### `ACP-IVF-004` — Pre-Use Data Validation Discipline

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (77 grounded claims em 14 fontes):
  - NIST SP 800-53 Rev. 5 — 27 refs (`SP800-53-CA-3.6`, `SP800-53-CA-7.4`, `SP800-53-CP-7.4` + 2 more)
  - CIS Controls v8.1.2 — 18 refs (`CIS-1.1`, `CIS-3`, `CIS-3.1` + 2 more)
  - OWASP ASVS v5.0.0 — 7 refs (`ASVS-REQ-V2.2.3`, `ASVS-REQ-V2.3.1`, `ASVS-REQ-V2.3.3` + 2 more)
  - OWASP SAMM v2.1 — 7 refs (`SAMM-ACTIVITY-D_TA_1_A`, `SAMM-ACTIVITY-D_TA_3_A`, `SAMM-ACTIVITY-I_DM_3_B` + 2 more)
  - EU GDPR (RGPD) — 3 refs (`GDPR-ART-5`, `GDPR-ART-32`, `GDPR-ART-35`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 3 refs (`AML.T0010.002`, `AML.T0111`, `AML.M0008`)
  - OWASP LLM Top 10 (2025) — 3 refs (`LLM02-2025`, `LLM04-2025`, `LLM08-2025`)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-348`, `CWE-454`)
  - NIST SSDF (SP 800-218 v1.1) — 2 refs (`SSDF-PRACTICE-RV.1`, `SSDF-PRACTICE-RV.2`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-72737130472C498480F89AB2F1C2ED5D`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-DATA-VALIDATION`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML02-2023`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A02-2021`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-6.5.3`)

#### `ACP-IVF-005` — Non-Revealing Error Surface Control

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (237 grounded claims em 22 fontes):
  - NIST SP 800-53 Rev. 5 — 123 refs (`SP800-53-AC-1`, `SP800-53-AC-2`, `SP800-53-AC-3.5` + 2 more)
  - PCI DSS v4.0.1 — 21 refs (`PCI-REQ-1`, `PCI-1.1.1`, `PCI-1.2.2` + 2 more)
  - MITRE CAPEC v3.9 — 20 refs (`CAPEC-12`, `CAPEC-22`, `CAPEC-36` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 20 refs (`CWE-1073`, `CWE-1084`, `CWE-1118` + 2 more)
  - OWASP ASVS v5.0.0 — 6 refs (`ASVS-REQ-V6.1.1`, `ASVS-REQ-V8.2.4`, `ASVS-REQ-V15.3.4` + 2 more)
  - CIS Controls v8.1.2 — 6 refs (`CIS-4.11`, `CIS-6.8`, `CIS-13.5` + 2 more)
  - HIPAA Security Rule — 5 refs (`HIPAA-164-308a6`, `HIPAA-164-310a1`, `HIPAA-164-310b` + 2 more)
  - OWASP DSOMM — 5 refs (`DSOMM-ACTIVITY-82E499D1F4634A4BBE9068812A874AF6`, `DSOMM-ACTIVITY-E5386ABF91544752A1A8C3A8900F732D`, `DSOMM-ACTIVITY-ED715B38C34B40CD83FDCE807F306FC1` + 2 more)
  - PCI Secure SLC v1.1 — 5 refs (`PCISSLC-2.6`, `PCISSLC-3.2`, `PCISSLC-3.3` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 4 refs (`AML.TA0014`, `AML.T0049`, `AML.T0094` + 1 more)
  - OWASP LLM Top 10 (2025) — 4 refs (`LLM01-2025`, `LLM03-2025`, `LLM07-2025` + 1 more)
  - OWASP SAMM v2.1 — 4 refs (`SAMM-ACTIVITY-I_DM_1_A`, `SAMM-ACTIVITY-I_SD_2_A`, `SAMM-ACTIVITY-O_IM_2_B` + 1 more)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 2 refs (`MCP01-2025`, `MCP02-2025`)
  - OWASP Machine Learning Top 10 — 2 refs (`ML06-2023`, `ML08-2023`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 2 refs (`SCFPSSD-SECURITY-CONTROLS`, `SCFPSSD-VULN-RESPONSE`)
  - NIST SSDF (SP 800-218 v1.1) — 2 refs (`SSDF-TASK-PO.5.2`, `SSDF-TASK-PW.1.2`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-13`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-5`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A01-2021`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 1 refs (`SCAGILE-EXP-8`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEVELOPMENT`)

#### `ACP-IVF-006` — Centralized Error Governance

- **Manual prose:** cobertura **cross-chapter** — content encontrado em Cap. 00 (`00-fundamentos`), Cap. 07 (`07-cicd-seguro`), Cap. 10 (`10-testes-seguranca`), Cap. 12 (`12-monitorizacao-operacoes`), Cap. 13 (`13-formacao-onboarding`), Cap. 14 (`14-governanca-contratacao`). Cap. expected (06-desenvolvimento-seguro) tem cobertura fraca; ler em chapter(s) listada(s).
- **Substrate v7 contributing sources** (54 grounded claims em 9 fontes):
  - NIST SP 800-53 Rev. 5 — 28 refs (`SP800-53-AU-1`, `SP800-53-AU-2`, `SP800-53-AU-2.3` + 2 more)
  - OWASP SAMM v2.1 — 10 refs (`SAMM-ACTIVITY-G_EG_2_B`, `SAMM-ACTIVITY-G_EG_3_A`, `SAMM-ACTIVITY-G_PC_1_B` + 2 more)
  - OWASP DSOMM — 5 refs (`DSOMM-ACTIVITY-95CAEF9636ED458CA0875C35D4F9DEC2`, `DSOMM-ACTIVITY-8B994601575E4EA5B228ACCB18C8E514`, `DSOMM-ACTIVITY-4ECED38A79044C45ADB050B663065540` + 2 more)
  - CIS Controls v8.1.2 — 4 refs (`CIS-8.1`, `CIS-8.3`, `CIS-8.9` + 1 more)
  - NIST AI RMF 1.0 — 3 refs (`NIST-AI-RMF-GOVERN-4`, `NIST-AI-RMF-GOVERN-4.3`, `NIST-AI-RMF-MEASURE-1.3`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-GOVERNANCE`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C9`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-10.4.1`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-LOGGING`)

#### `ACP-IVF-007` — Context-Aware Output Encoding At Rendering Boundaries

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 4 keywords × 14 ocorrências; principais: encoding, escaping, html, output)
- **Substrate v7 contributing sources** (30 grounded claims em 7 fontes):
  - OWASP ASVS v5.0.0 — 12 refs (`ASVS-REQ-V1.1.2`, `ASVS-REQ-V1.2.1`, `ASVS-REQ-V1.2.2` + 2 more)
  - MITRE CAPEC v3.9 — 12 refs (`CAPEC-19`, `CAPEC-32`, `CAPEC-64` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0054`, `AML.T0077`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-838`)
  - NIST SP 800-53 Rev. 5 — 1 refs (`SP800-53-AC-16.5`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-E1F37ABBD8484A3AB3DF65E91A89DCB7`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C4`)


### Mechanisms (5)

#### `ACM-IVF-001` — Code Review For Input And Error Discipline

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (127 grounded claims em 19 fontes):
  - NIST SP 800-53 Rev. 5 — 35 refs (`SP800-53-AC-4.9`, `SP800-53-AC-13`, `SP800-53-AU-2.3` + 2 more)
  - OWASP ASVS v5.0.0 — 15 refs (`ASVS-REQ-V1.2.5`, `ASVS-REQ-V1.2.6`, `ASVS-REQ-V1.3.6` + 2 more)
  - MITRE CAPEC v3.9 — 14 refs (`CAPEC-14`, `CAPEC-24`, `CAPEC-54` + 2 more)
  - OWASP SAMM v2.1 — 14 refs (`SAMM-ACTIVITY-D_SR_1_B`, `SAMM-ACTIVITY-D_TA_3_A`, `SAMM-ACTIVITY-G_EG_3_A` + 2 more)
  - CIS Controls v8.1.2 — 12 refs (`CIS-3.1`, `CIS-3.2`, `CIS-3.7` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 10 refs (`SSDF-PRACTICE-PO.4`, `SSDF-PRACTICE-PW.5`, `SSDF-PRACTICE-PW.7` + 2 more)
  - OWASP DSOMM — 6 refs (`DSOMM-ACTIVITY-7121B0C76ACE4D6B95D094535DBCCB57`, `DSOMM-ACTIVITY-95CAEF9636ED458CA0875C35D4F9DEC2`, `DSOMM-ACTIVITY-55F4C9163A34474DAD969A9F7A4F6A83` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 4 refs (`CWE-1085`, `CWE-115`, `CWE-391` + 1 more)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 3 refs (`SCFPSSD-CODING-STANDARDS`, `SCFPSSD-DATA-HANDLING`, `SCFPSSD-TESTING`)
  - OWASP LLM Top 10 (2025) — 2 refs (`LLM09-2025`, `LLM10-2025`)
  - OWASP Proactive Controls (2018) — 2 refs (`OPC-C9`, `OPC-C10`)
  - PCI DSS v4.0.1 — 2 refs (`PCI-6.2.3`, `PCI-10.4.1`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 2 refs (`SCAGILE-OPS-2`, `SCAGILE-OPS-7`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-32`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-308a1`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-CONTINUOUS-VALIDATION`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML02-2023`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-3.2`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEV-TESTING`)

#### `ACM-IVF-002` — Static Rulepacks And Security Linters

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (90 grounded claims em 14 fontes):
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 17 refs (`AML.T0010.001`, `AML.T0020`, `AML.T0054` + 2 more)
  - MITRE CAPEC v3.9 — 13 refs (`CAPEC-15`, `CAPEC-35`, `CAPEC-38` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 10 refs (`CWE-183`, `CWE-184`, `CWE-186` + 2 more)
  - NIST SP 800-53 Rev. 5 — 10 refs (`SP800-53-AC-4.1`, `SP800-53-AC-4.6`, `SP800-53-AC-4.14` + 2 more)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 9 refs (`NIST-AI-100-2-E2025-2.1.3`, `NIST-AI-100-2-E2025-2.3.1`, `NIST-AI-100-2-E2025-3.2` + 2 more)
  - OWASP SAMM v2.1 — 7 refs (`SAMM-ACTIVITY-I_SB_1_A`, `SAMM-ACTIVITY-I_SB_2_B`, `SAMM-ACTIVITY-I_SB_3_A` + 2 more)
  - OWASP ASVS v5.0.0 — 5 refs (`ASVS-REQ-V1.3.7`, `ASVS-REQ-V1.3.12`, `ASVS-REQ-V9.1.2` + 2 more)
  - OWASP DSOMM — 5 refs (`DSOMM-ACTIVITY-B597928E54D648A5A8068003DCD56AAB`, `DSOMM-ACTIVITY-CF81922530CB47028E3260225EEDC33D`, `DSOMM-ACTIVITY-F0E018143B884BD0A3A9F91DB001D20BADVANCED` + 2 more)
  - PCI DSS v4.0.1 — 5 refs (`PCI-2.2.6`, `PCI-6.3.3`, `PCI-7.3.3` + 2 more)
  - CIS Controls v8.1.2 — 3 refs (`CIS-2.6`, `CIS-3.7`, `CIS-10`)
  - PCI Secure SLC v1.1 — 3 refs (`PCISSLC-8.1`, `PCISSLC-8.2`, `PCISSLC-8.3`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM03-2025`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-TOOL-DESIGN`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PO.3.3`)

#### `ACM-IVF-003` — Schema And Contract Validators

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (36 grounded claims em 11 fontes):
  - OWASP ASVS v5.0.0 — 10 refs (`ASVS-REQ-V2.1.1`, `ASVS-REQ-V2.1.2`, `ASVS-REQ-V2.1.3` + 2 more)
  - NIST SP 800-53 Rev. 5 — 7 refs (`SP800-53-SA-9.3`, `SP800-53-SA-10.1`, `SP800-53-SA-12.10` + 2 more)
  - MITRE CAPEC v3.9 — 6 refs (`CAPEC-95`, `CAPEC-146`, `CAPEC-218` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 4 refs (`CWE-112`, `CWE-353`, `CWE-354` + 1 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 3 refs (`AML.M0008`, `AML.M0019`, `AML.M0033`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-3.4`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-312c1`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-017D9E2642B549A4B9459F59B308FB99`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM04-2025`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C5`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-3.2`)

#### `ACM-IVF-004` — Centralized Error Translation And Redaction

- **Manual prose:** ⚠️ **content gap confirmado** — Phase 2/3 kw-match não encontrou cobertura substantive. Registado como future-work P8 §10 limitations (decisão programme-lead 2026-05-11).
- **Substrate v7 contributing sources** (158 grounded claims em 15 fontes):
  - NIST SP 800-53 Rev. 5 — 69 refs (`SP800-53-AC-1`, `SP800-53-AC-2.4`, `SP800-53-AC-4.24` + 2 more)
  - PCI DSS v4.0.1 — 20 refs (`PCI-REQ-1`, `PCI-1.1.1`, `PCI-1.1.2` + 2 more)
  - CIS Controls v8.1.2 — 19 refs (`CIS-2`, `CIS-4.9`, `CIS-6.7` + 2 more)
  - OWASP DSOMM — 12 refs (`DSOMM-ACTIVITY-994151396B50441B89E10AA59ACCD43D`, `DSOMM-ACTIVITY-8AE0B92C10E04602BA227524D6AED488`, `DSOMM-ACTIVITY-F2594F8F1CD645F9AF29EAF3315698EB` + 2 more)
  - OWASP SAMM v2.1 — 12 refs (`SAMM-ACTIVITY-G_EG_2_B`, `SAMM-ACTIVITY-I_DM_1_A`, `SAMM-ACTIVITY-I_SD_1_A` + 2 more)
  - MITRE CAPEC v3.9 — 10 refs (`CAPEC-12`, `CAPEC-61`, `CAPEC-187` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 5 refs (`SSDF-PRACTICE-PS.3`, `SSDF-TASK-PO.1.3`, `SSDF-TASK-PO.3.2` + 2 more)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 3 refs (`SCAGILE-OPS-1`, `SCAGILE-OPS-5`, `SCAGILE-OPS-6`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 2 refs (`SCFPSSD-VULN-RESPONSE`, `SCFPSSD-MITIGATIONS`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-13`)
  - EU Digital Operational Resilience Act (DORA) — 1 refs (`DORA-ART-9`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-32`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.T0104`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-5.2`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-SOURCING-TRANSFER`)

#### `ACM-IVF-005` — Context-Aware Encoder Selection And Application

- **Manual prose:** coberto neste capítulo (verificação Phase 2/3 deterministic kw-match: 3 keywords × 19 ocorrências; principais: html, json, output)
- **Substrate v7 contributing sources** (46 grounded claims em 7 fontes):
  - MITRE CAPEC v3.9 — 26 refs (`CAPEC-18`, `CAPEC-19`, `CAPEC-32` + 2 more)
  - OWASP ASVS v5.0.0 — 13 refs (`ASVS-REQ-V1.1.2`, `ASVS-REQ-V1.2.1`, `ASVS-REQ-V1.2.2` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-1021`, `CWE-838`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0054`, `AML.T0077`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-E1F37ABBD8484A3AB3DF65E91A89DCB7`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM10-2025`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C4`)


---

## Slice `ACO-SPC` — Gestão de segredos, configuração protegida e identidades operacionais

### ControlObjectives (7)

#### `ACO-SPC-001` — Secret Leak Prevention And Hardcoded-Secret Exclusion

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (17 grounded claims em 10 fontes):
  - MITRE CWE — Software Development View (v4.19.1) — 3 refs (`CWE-215`, `CWE-348`, `CWE-434`)
  - NIST SP 800-53 Rev. 5 — 3 refs (`SP800-53-AC-4.31`, `SP800-53-PE-19`, `SP800-53-SR-2`)
  - MITRE CAPEC v3.9 — 2 refs (`CAPEC-65`, `CAPEC-242`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0057`, `AML.T0068`)
  - NIST SSDF (SP 800-218 v1.1) — 2 refs (`SSDF-PRACTICE-PS.1`, `SSDF-PRACTICE-PW.5`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-D17DBFF01F10492AB4C717BB59A0A711`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM09-2025`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-I_DM_1_A`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-9.3`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEV-REPO`)

#### `ACO-SPC-002` — Protected Secret Storage And Controlled Retrieval

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (70 grounded claims em 11 fontes):
  - NIST SP 800-53 Rev. 5 — 38 refs (`SP800-53-AC-3.6`, `SP800-53-AC-3.9`, `SP800-53-AC-11.1` + 2 more)
  - CIS Controls v8.1.2 — 10 refs (`CIS-3`, `CIS-3.1`, `CIS-3.2` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 10 refs (`CWE-256`, `CWE-257`, `CWE-260` + 2 more)
  - MITRE CAPEC v3.9 — 3 refs (`CAPEC-37`, `CAPEC-204`, `CAPEC-636`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.T0037`, `AML.M0012`)
  - PCI DSS v4.0.1 — 2 refs (`PCI-3.3.2`, `PCI-9.4.6`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-5`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C3`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-O_OM_2_A`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-7.2`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PS.1.1`)

#### `ACO-SPC-003` — Secret Rotation And Expiry Discipline

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (7 grounded claims em 2 fontes):
  - OWASP ASVS v5.0.0 — 4 refs (`ASVS-REQ-V6.2.10`, `ASVS-REQ-V6.4.1`, `ASVS-REQ-V13.1.4` + 1 more)
  - MITRE CWE — Software Development View (v4.19.1) — 3 refs (`CWE-262`, `CWE-263`, `CWE-324`)

#### `ACO-SPC-004` — Operational Identity Binding And Short-Lived Credentials

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (53 grounded claims em 13 fontes):
  - NIST SP 800-53 Rev. 5 — 23 refs (`SP800-53-AC-2`, `SP800-53-IA-2`, `SP800-53-IA-2.1` + 2 more)
  - MITRE CAPEC v3.9 — 6 refs (`CAPEC-21`, `CAPEC-59`, `CAPEC-196` + 2 more)
  - OWASP ASVS v5.0.0 — 5 refs (`ASVS-REQ-V6.3.4`, `ASVS-REQ-V6.8.4`, `ASVS-REQ-V7.1.3` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 5 refs (`CWE-1392`, `CWE-289`, `CWE-306` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 5 refs (`AML.TA0013`, `AML.T0021`, `AML.T0012` + 2 more)
  - OWASP SAMM v2.1 — 2 refs (`SAMM-ACTIVITY-I_SD_1_A`, `SAMM-ACTIVITY-V_ST_3_A`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-5`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-65A2D7D9544146BFA4E3F76919857750`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-AUTH`)
  - OWASP MCP — Third-Party Servers v1.0 — 1 refs (`OWASP-MCP-3P-TOOLS-UTILITIES`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP07-2025`)
  - OWASP Top 10 (2021) — 1 refs (`TOP10-A07-2021`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-IAM`)

#### `ACO-SPC-005` — Secret Usage Isolation Across Pipeline, Workload And Deploy Surfaces

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (18 grounded claims em 8 fontes):
  - OWASP DSOMM — 6 refs (`DSOMM-ACTIVITY-DA4FF665DCB94E939D2048CDEDC50FC2`, `DSOMM-ACTIVITY-DF428C9DEFA042269F47A15BB53F822B`, `DSOMM-ACTIVITY-3A94D55EFD8249969EB320D23FF2A873` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 3 refs (`AML.T0008.000`, `AML.T0024`, `AML.T0105`)
  - NIST SP 800-53 Rev. 5 — 3 refs (`SP800-53-SC-7.20`, `SP800-53-SC-39`, `SP800-53-SC-39.1`)
  - CIS Controls v8.1.2 — 2 refs (`CIS-4.12`, `CIS-16.8`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-574`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-214`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML07-2023`)
  - SLSA Specification v1.0 — Build Track — 1 refs (`SLSA-BUILD-PLATFORM-ISOLATION`)

#### `ACO-SPC-006` — Secret Change Auditability And Governance

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (53 grounded claims em 9 fontes):
  - NIST SP 800-53 Rev. 5 — 44 refs (`SP800-53-AC-2.7`, `SP800-53-AC-3.10`, `SP800-53-AC-4.23` + 2 more)
  - PCI DSS v4.0.1 — 2 refs (`PCI-10.3.2`, `PCI-11.5.2`)
  - OWASP ASVS v5.0.0 — 1 refs (`ASVS-REQ-V11.1.4`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-678`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-312b`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-3F63BDBCC75F4780A941E6AD42E894E1`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML07-2023`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-5.1`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-LOGGING`)

#### `ACO-SPC-007` — Secret Handling And Operational Identity Integrity

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (169 grounded claims em 20 fontes):
  - NIST SP 800-53 Rev. 5 — 85 refs (`SP800-53-AC-1`, `SP800-53-AC-3`, `SP800-53-AC-3.5` + 2 more)
  - PCI DSS v4.0.1 — 16 refs (`PCI-REQ-2`, `PCI-REQ-7`, `PCI-1.2.6` + 2 more)
  - CIS Controls v8.1.2 — 11 refs (`CIS-3.5`, `CIS-4`, `CIS-4.1` + 2 more)
  - OWASP SAMM v2.1 — 9 refs (`SAMM-ACTIVITY-D_SA_1_A`, `SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-D_SA_2_B` + 2 more)
  - MITRE CAPEC v3.9 — 8 refs (`CAPEC-122`, `CAPEC-212`, `CAPEC-511` + 2 more)
  - PCI Secure SLC v1.1 — 5 refs (`PCISSLC-1.2`, `PCISSLC-2.3`, `PCISSLC-8.1` + 2 more)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 5 refs (`SCAGILE-OPS-8`, `SCAGILE-OPS-12`, `SCAGILE-OPS-14` + 2 more)
  - OWASP ASVS v5.0.0 — 4 refs (`ASVS-REQ-V13.3.3`, `ASVS-REQ-V15.1.5`, `ASVS-REQ-V15.4.2` + 1 more)
  - HIPAA Security Rule — 4 refs (`HIPAA-164-308a1`, `HIPAA-164-308a2`, `HIPAA-164-308a5` + 1 more)
  - NIST SSDF (SP 800-218 v1.1) — 4 refs (`SSDF-PRACTICE-PO.5`, `SSDF-TASK-PO.1.1`, `SSDF-TASK-PO.1.2` + 1 more)
  - OWASP DSOMM — 3 refs (`DSOMM-ACTIVITY-AE22DAFDBCD641EEBA018B7FE6FC1AD9`, `DSOMM-ACTIVITY-82E499D1F4634A4BBE9068812A874AF6`, `DSOMM-ACTIVITY-070BB14BE04A4F3D896AA08EBA7A35F9`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 3 refs (`SCFPSSD-SECURITY-CONTROLS`, `SCFPSSD-DESIGN-PRINCIPLES`, `SCFPSSD-CODING-STANDARDS`)
  - SAFECode — Software Integrity Controls (2010) — 3 refs (`SCSIC-SOURCING`, `SCSIC-SOURCING-TRANSFER`, `SCSIC-DELIVERY-SIGNING`)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-358`, `CWE-649`)
  - EU GDPR (RGPD) — 2 refs (`GDPR-ART-5`, `GDPR-ART-32`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.T0054`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM03-2025`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-TOOL-DESIGN`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C2`)


### Practices (6)

#### `ACP-SPC-001` — Secret Leak Prevention In Source And Pipeline

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (141 grounded claims em 18 fontes):
  - OWASP DSOMM — 24 refs (`DSOMM-ACTIVITY-F3C4971E9F4D4E598ED0F0BDB6262477`, `DSOMM-ACTIVITY-8AE0B92C10E04602BA227524D6AED488`, `DSOMM-ACTIVITY-12C90CC63D584D9B82FFD469D2A0C298` + 2 more)
  - MITRE CAPEC v3.9 — 18 refs (`CAPEC-38`, `CAPEC-44`, `CAPEC-131` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 18 refs (`SSDF-PRACTICE-PO.1`, `SSDF-PRACTICE-PS.2`, `SSDF-PRACTICE-PW.2` + 2 more)
  - OWASP SAMM v2.1 — 12 refs (`SAMM-ACTIVITY-I_DM_1_A`, `SAMM-ACTIVITY-I_DM_2_A`, `SAMM-ACTIVITY-I_SB_1_A` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 10 refs (`AML.TA0009`, `AML.T0007`, `AML.T0104` + 2 more)
  - NIST SP 800-53 Rev. 5 — 10 refs (`SP800-53-AC-4.28`, `SP800-53-RA-5.11`, `SP800-53-SA-10` + 2 more)
  - CIS Controls v8.1.2 — 9 refs (`CIS-3.8`, `CIS-3.13`, `CIS-16.1` + 2 more)
  - OWASP ASVS v5.0.0 — 6 refs (`ASVS-REQ-V15.1.1`, `ASVS-REQ-V15.1.4`, `ASVS-REQ-V15.1.5` + 2 more)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 5 refs (`NIST-AI-100-2-E2025-3.2`, `NIST-AI-100-2-E2025-3.2.3`, `NIST-AI-100-2-E2025-3.3.2` + 2 more)
  - PCI DSS v4.0.1 — 5 refs (`PCI-1.2.4`, `PCI-5.2.1`, `PCI-5.2.3` + 2 more)
  - SLSA Specification v1.0 — Build Track — 5 refs (`SLSA-BUILD-L1`, `SLSA-BUILD-L2`, `SLSA-BUILD-L3` + 2 more)
  - OWASP LLM Top 10 (2025) — 4 refs (`LLM03-2025`, `LLM04-2025`, `LLM08-2025` + 1 more)
  - PCI Secure SLC v1.1 — 4 refs (`PCISSLC-4.1`, `PCISSLC-4.2`, `PCISSLC-6.1` + 1 more)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 4 refs (`SCAGILE-OPS-2`, `SCAGILE-OPS-7`, `SCAGILE-OPS-14` + 1 more)
  - SAFECode — Software Integrity Controls (2010) — 3 refs (`SCSIC-SOURCING-OSS`, `SCSIC-DEV-REPO`, `SCSIC-DELIVERY`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 2 refs (`SCFPSSD-CODING-STANDARDS`, `SCFPSSD-LIFECYCLE-FEEDBACK`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-494`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-TOOL-DESIGN`)

#### `ACP-SPC-002` — Vault-Backed Secret Storage

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (166 grounded claims em 18 fontes):
  - NIST SP 800-53 Rev. 5 — 81 refs (`SP800-53-AC-3.13`, `SP800-53-AC-4.4`, `SP800-53-AC-4.25` + 2 more)
  - PCI DSS v4.0.1 — 17 refs (`PCI-REQ-3`, `PCI-REQ-4`, `PCI-REQ-6` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 14 refs (`CWE-256`, `CWE-257`, `CWE-278` + 2 more)
  - CIS Controls v8.1.2 — 13 refs (`CIS-3`, `CIS-3.1`, `CIS-3.2` + 2 more)
  - OWASP ASVS v5.0.0 — 12 refs (`ASVS-REQ-V6.5.2`, `ASVS-REQ-V6.5.3`, `ASVS-REQ-V11.1.2` + 2 more)
  - MITRE CAPEC v3.9 — 10 refs (`CAPEC-24`, `CAPEC-37`, `CAPEC-204` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 4 refs (`AML.TA0006`, `AML.TA0012`, `AML.T0037` + 1 more)
  - OWASP SAMM v2.1 — 4 refs (`SAMM-ACTIVITY-D_SA_2_A`, `SAMM-ACTIVITY-D_SA_2_B`, `SAMM-ACTIVITY-I_SD_2_B` + 1 more)
  - EU GDPR (RGPD) — 2 refs (`GDPR-ART-5`, `GDPR-ART-32`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-312d`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-0FF45FB87EEF46ED9B3A84C955CD7060`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-DEPLOYMENT`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML05-2023`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C3`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-7.2`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-ENCRYPTION`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PS.1.1`)

#### `ACP-SPC-003` — Secret Rotation And Renewal Discipline

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (10 grounded claims em 7 fontes):
  - NIST SP 800-53 Rev. 5 — 3 refs (`SP800-53-IA-5.13`, `SP800-53-PS-1`, `SP800-53-PS-6`)
  - OWASP ASVS v5.0.0 — 2 refs (`ASVS-REQ-V6.4.5`, `ASVS-REQ-V13.3.4`)
  - CIS Controls v8.1.2 — 1 refs (`CIS-14.1`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-308a6`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.T0054`)
  - OWASP SAMM v2.1 — 1 refs (`SAMM-ACTIVITY-G_SM_3_A`)
  - PCI Secure SLC v1.1 — 1 refs (`PCISSLC-5.1`)

#### `ACP-SPC-004` — Operational Identity Binding And OIDC Use

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (81 grounded claims em 12 fontes):
  - NIST SP 800-53 Rev. 5 — 44 refs (`SP800-53-AC-2`, `SP800-53-AC-4.12`, `SP800-53-AC-4.18` + 2 more)
  - OWASP ASVS v5.0.0 — 20 refs (`ASVS-REQ-V6.8.1`, `ASVS-REQ-V6.8.2`, `ASVS-REQ-V6.8.4` + 2 more)
  - PCI DSS v4.0.1 — 6 refs (`PCI-1.1.1`, `PCI-4.1.1`, `PCI-8.1.1` + 2 more)
  - MITRE CAPEC v3.9 — 2 refs (`CAPEC-21`, `CAPEC-196`)
  - MITRE CWE — Software Development View (v4.19.1) — 2 refs (`CWE-289`, `CWE-322`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.T0021`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-65A2D7D9544146BFA4E3F76919857750`)
  - OWASP LLM Top 10 (2025) — 1 refs (`LLM06-2025`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-AUTH`)
  - OWASP MCP — Third-Party Servers v1.0 — 1 refs (`OWASP-MCP-3P-TOOLS-UTILITIES`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C6`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-IAM`)

#### `ACP-SPC-005` — Secret Isolation Across Technical Surfaces

- **Manual prose:** cobertura **cross-chapter** — content encontrado em Cap. 07 (`07-cicd-seguro`), Cap. 08 (`08-iac-infraestrutura`), Cap. 11 (`11-deploy-seguro`). Cap. expected (06-desenvolvimento-seguro) tem cobertura fraca; ler em chapter(s) listada(s).
- **Substrate v7 contributing sources** (142 grounded claims em 14 fontes):
  - NIST SP 800-53 Rev. 5 — 53 refs (`SP800-53-AC-17.6`, `SP800-53-AC-20`, `SP800-53-CM-4.1` + 2 more)
  - MITRE CAPEC v3.9 — 24 refs (`CAPEC-22`, `CAPEC-36`, `CAPEC-113` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 23 refs (`AML.TA0013`, `AML.TA0010`, `AML.T0008` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 16 refs (`CWE-1104`, `CWE-1220`, `CWE-213` + 2 more)
  - OWASP DSOMM — 10 refs (`DSOMM-ACTIVITY-31833D5635AF4EF39300F23D27646CE7`, `DSOMM-ACTIVITY-82E499D1F4634A4BBE9068812A874AF6`, `DSOMM-ACTIVITY-AD23BE9C56614F1F81A35A5DC7061629` + 2 more)
  - CIS Controls v8.1.2 — 5 refs (`CIS-1`, `CIS-4.12`, `CIS-14.8` + 2 more)
  - OWASP SAMM v2.1 — 3 refs (`SAMM-ACTIVITY-D_SA_1_B`, `SAMM-ACTIVITY-D_SA_3_B`, `SAMM-ACTIVITY-O_OM_1_A`)
  - SLSA Specification v1.0 — Build Track — 2 refs (`SLSA-PRINCIPLE-TRUST-CODE`, `SLSA-BUILD-PLATFORM-ISOLATION`)
  - HIPAA Security Rule — 1 refs (`HIPAA-164-310c`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 1 refs (`NIST-AI-100-2-E2025-4.2.1`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP01-2025`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML07-2023`)
  - PCI DSS v4.0.1 — 1 refs (`PCI-8.2.7`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEV-BUILD`)

#### `ACP-SPC-006` — Secret Configuration Governance

- **Manual prose:** cobertura **cross-chapter** — content encontrado em Cap. 00 (`00-fundamentos`), Cap. 05 (`05-dependencias-sbom-sca`), Cap. 07 (`07-cicd-seguro`), Cap. 13 (`13-formacao-onboarding`), Cap. 14 (`14-governanca-contratacao`). Cap. expected (06-desenvolvimento-seguro) tem cobertura fraca; ler em chapter(s) listada(s).
- **Substrate v7 contributing sources** (64 grounded claims em 13 fontes):
  - NIST SP 800-53 Rev. 5 — 34 refs (`SP800-53-AC-1`, `SP800-53-AC-4.20`, `SP800-53-AC-13` + 2 more)
  - NIST AI RMF 1.0 — 9 refs (`NIST-AI-RMF-GOVERN-1`, `NIST-AI-RMF-GOVERN-1.3`, `NIST-AI-RMF-GOVERN-1.6` + 2 more)
  - OWASP SAMM v2.1 — 8 refs (`SAMM-ACTIVITY-G_EG_2_A`, `SAMM-ACTIVITY-G_EG_3_A`, `SAMM-ACTIVITY-G_PC_1_A` + 2 more)
  - PCI DSS v4.0.1 — 3 refs (`PCI-REQ-2`, `PCI-2.2.1`, `PCI-6.5.4`)
  - PCI Secure SLC v1.1 — 2 refs (`PCISSLC-2.1`, `PCISSLC-8.2`)
  - OWASP ASVS v5.0.0 — 1 refs (`ASVS-REQ-V13.3.2`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-678`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-13`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-20`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-GOVERNANCE`)
  - OWASP Machine Learning Top 10 — 1 refs (`ML06-2023`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-PLANNING`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEV-DEFAULTS`)


### Mechanisms (4)

#### `ACM-SPC-001` — Secret Management Systems

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (317 grounded claims em 23 fontes):
  - NIST SP 800-53 Rev. 5 — 169 refs (`SP800-53-AC-3.5`, `SP800-53-AC-3.6`, `SP800-53-AC-4.4` + 2 more)
  - MITRE CAPEC v3.9 — 27 refs (`CAPEC-24`, `CAPEC-39`, `CAPEC-97` + 2 more)
  - OWASP ASVS v5.0.0 — 18 refs (`ASVS-REQ-V6.1.2`, `ASVS-REQ-V6.5.2`, `ASVS-REQ-V6.5.3` + 2 more)
  - NIST SSDF (SP 800-218 v1.1) — 17 refs (`SSDF-PRACTICE-PO.1`, `SSDF-PRACTICE-PO.4`, `SSDF-PRACTICE-PO.5` + 2 more)
  - PCI DSS v4.0.1 — 13 refs (`PCI-REQ-5`, `PCI-REQ-6`, `PCI-1.2.3` + 2 more)
  - OWASP DSOMM — 10 refs (`DSOMM-ACTIVITY-1B9281B948E24C019AC69DB9931C4885`, `DSOMM-ACTIVITY-12C90CC63D584D9B82FFD469D2A0C298`, `DSOMM-ACTIVITY-F88D1B173D7D4C3D8139AD44FC4942D4` + 2 more)
  - OWASP SAMM v2.1 — 10 refs (`SAMM-ACTIVITY-D_SA_1_A`, `SAMM-ACTIVITY-D_SA_2_B`, `SAMM-ACTIVITY-D_SA_3_B` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 9 refs (`CWE-1230`, `CWE-309`, `CWE-312` + 2 more)
  - CIS Controls v8.1.2 — 8 refs (`CIS-3`, `CIS-3.1`, `CIS-3.3` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 7 refs (`AML.T0037`, `AML.T0057`, `AML.T0068` + 2 more)
  - HIPAA Security Rule — 5 refs (`HIPAA-164-308a4`, `HIPAA-164-308a5`, `HIPAA-164-310a1` + 2 more)
  - OWASP LLM Top 10 (2025) — 4 refs (`LLM04-2025`, `LLM07-2025`, `LLM08-2025` + 1 more)
  - OWASP Proactive Controls (2018) — 3 refs (`OPC-C1`, `OPC-C3`, `OPC-C8`)
  - PCI Secure SLC v1.1 — 3 refs (`PCISSLC-2.3`, `PCISSLC-6.1`, `PCISSLC-6.2`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 3 refs (`SCFPSSD-DESIGN-PRINCIPLES`, `SCFPSSD-ENCRYPTION`, `SCFPSSD-CODING-STANDARDS`)
  - OWASP Machine Learning Top 10 — 2 refs (`ML05-2023`, `ML07-2023`)
  - SAFECode — Practical Security Stories and Tasks for Agile Development (2012) — 2 refs (`SCAGILE-EXP-1`, `SCAGILE-EXP-12`)
  - SLSA Specification v1.0 — Build Track — 2 refs (`SLSA-PRINCIPLE-TRUST-PLATFORMS`, `SLSA-PRINCIPLE-TRUST-CODE`)
  - EU NIS2 Directive — 1 refs (`NIS2-ART-21`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-32`)
  - NIST AI 100-2 e2025 — Adversarial Machine Learning Taxonomy — 1 refs (`NIST-AI-100-2-E2025-4.2.1`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-DEPLOYMENT`)
  - SAFECode — Software Integrity Controls (2010) — 1 refs (`SCSIC-DEV-REPO`)

#### `ACM-SPC-002` — OIDC-Based Operational Identity

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (75 grounded claims em 11 fontes):
  - NIST SP 800-53 Rev. 5 — 45 refs (`SP800-53-AC-4.12`, `SP800-53-AC-14`, `SP800-53-AC-16.1` + 2 more)
  - OWASP ASVS v5.0.0 — 17 refs (`ASVS-REQ-V6.8.4`, `ASVS-REQ-V7.5.3`, `ASVS-REQ-V8.4.2` + 2 more)
  - MITRE CAPEC v3.9 — 3 refs (`CAPEC-21`, `CAPEC-151`, `CAPEC-681`)
  - PCI DSS v4.0.1 — 3 refs (`PCI-8.2.1`, `PCI-8.2.2`, `PCI-8.3.3`)
  - MITRE CWE — Software Development View (v4.19.1) — 1 refs (`CWE-322`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 1 refs (`AML.T0087`)
  - OWASP DSOMM — 1 refs (`DSOMM-ACTIVITY-65A2D7D9544146BFA4E3F76919857750`)
  - OWASP MCP — Secure Server Development v1.0 — 1 refs (`OWASP-MCP-AUTH`)
  - OWASP MCP — Third-Party Servers v1.0 — 1 refs (`OWASP-MCP-3P-TOOLS-UTILITIES`)
  - OWASP Proactive Controls (2018) — 1 refs (`OPC-C6`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-IAM`)

#### `ACM-SPC-003` — Short-Lived Credential Controls

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (9 grounded claims em 5 fontes):
  - OWASP ASVS v5.0.0 — 2 refs (`ASVS-REQ-V6.1.1`, `ASVS-REQ-V6.2.10`)
  - CIS Controls v8.1.2 — 2 refs (`CIS-5`, `CIS-6.8`)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 2 refs (`AML.TA0013`, `AML.T0098`)
  - NIST SP 800-53 Rev. 5 — 2 refs (`SP800-53-AC-2.4`, `SP800-53-AC-2.8`)
  - MITRE CAPEC v3.9 — 1 refs (`CAPEC-226`)

#### `ACM-SPC-004` — Secret Scope And Binding Controls

- **Manual prose:** coberto na anchor canon/addon/intro deste capítulo (Phase 1 baseline classification).
- **Substrate v7 contributing sources** (111 grounded claims em 17 fontes):
  - NIST SP 800-53 Rev. 5 — 56 refs (`SP800-53-AC-1`, `SP800-53-AC-2.7`, `SP800-53-AC-3.1` + 2 more)
  - MITRE CAPEC v3.9 — 9 refs (`CAPEC-13`, `CAPEC-35`, `CAPEC-38` + 2 more)
  - MITRE ATLAS — Adversarial Threat Landscape for AI Systems — 9 refs (`AML.T0109`, `AML.T0002.002`, `AML.M0005` + 2 more)
  - NIST AI RMF 1.0 — 7 refs (`NIST-AI-RMF-GOVERN-1`, `NIST-AI-RMF-GOVERN-1.6`, `NIST-AI-RMF-GOVERN-2` + 2 more)
  - OWASP SAMM v2.1 — 6 refs (`SAMM-ACTIVITY-I_SB_1_A`, `SAMM-ACTIVITY-I_SB_2_B`, `SAMM-ACTIVITY-I_SB_3_A` + 2 more)
  - PCI DSS v4.0.1 — 6 refs (`PCI-5.2.3`, `PCI-6.5.3`, `PCI-6.5.4` + 2 more)
  - MITRE CWE — Software Development View (v4.19.1) — 3 refs (`CWE-1220`, `CWE-268`, `CWE-829`)
  - PCI Secure SLC v1.1 — 3 refs (`PCISSLC-5.1`, `PCISSLC-8.1`, `PCISSLC-8.3`)
  - CIS Controls v8.1.2 — 2 refs (`CIS-2.2`, `CIS-2.6`)
  - OWASP DSOMM — 2 refs (`DSOMM-ACTIVITY-CF81922530CB47028E3260225EEDC33D`, `DSOMM-ACTIVITY-E5386ABF91544752A1A8C3A8900F732D`)
  - OWASP LLM Top 10 (2025) — 2 refs (`LLM01-2025`, `LLM06-2025`)
  - EU Cyber Resilience Act (CRA) — 1 refs (`CRA-ART-13`)
  - EU GDPR (RGPD) — 1 refs (`GDPR-ART-5`)
  - Anthropic MCP — Official Security Foundations (2025) — 1 refs (`MCP-SCOPE-MINIMIZATION`)
  - OWASP MCP Top 10 (v0.1, 2025 beta) — 1 refs (`MCP02-2025`)
  - SAFECode — Fundamental Practices for Secure Software Development (2018) — 1 refs (`SCFPSSD-VULN-RESPONSE`)
  - NIST SSDF (SP 800-218 v1.1) — 1 refs (`SSDF-TASK-PO.3.2`)


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
