---
id: exemplos-aplicacao-governanca
title: Application and Onboarding Examples
sidebar_position: 5
description: Practical cases of applying security governance in projects, exceptions and contracting
tags: [exemplos, excecoes, onboarding, governance]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/addon/05-exemplos-praticos.md
  source_sha256: 194699e6a5227d853480ed41f5f36cee7321cd07dd3dcbb9643fbf9a9cb80c22
  source_commit: c4dc5e0ab3a1644a96f34a49ecae3686b35086ed
  target_sha256: 93896b455a5822268454f58688393f99a4c289f225eb887446a9b0c07a59256e
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [cycle_iteration, framework_source_corpus, requirement_runtime, risk_level, sbdtoe_sbd, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 99e5db07a804d01bb5f51b91db49d7723358aa258b6db13bbf3fe4112c80823b
  translated_at: 2026-09-27T08:02:36Z
  stamped_at: 2026-09-27T08:02:36Z
  reviewed_by: null
---



# Application Examples in the Governance Cycle

This annex provides **practical and reusable examples** for applying the concepts of governance and contracting operationally, aligned with the other elements of the SbD-ToE model.  
It also includes the verification of **mandatory training** for critical functions (owners, approvers, validators), in accordance with Ch. 13.

---

## 📜 1. Example of an exception approval {#-1-exemplo-de-aprovação-de-exceção}

**Title:** [SEC] Approval of an exception to the input validation control for the "GestDoc" app

**Justification:**  

The application uses a legacy framework without native support for automatic validation. The risk was mitigated with an external validation proxy and reinforced logging.

**Risk level:** L2  

**Controls replaced:** VAL-002, VAL-006  
**Compensation applied:** Validation in a proxy with schema + fuzzing tests  

**Exception validity:** 60 days (L2, Low/Medium — Policy 05 §7)  
**Owner:** paula.lima@empresa  

**Approvers:** AppSec + product manager  
**Mandatory training validated:** ✔️ Owners and approvers with active SbD training (Ch. 13)

---

## 📄 2. Example of supplier onboarding {#-2-exemplo-de-onboarding-de-fornecedor}

**Title:** [ONB] Supplier validation for an external payment integration ("XPay" service)

**Risk classification of the system:** L3

**Onboarding checklist:**
- [x] Security questionnaire completed
- [x] SBOM provided
- [x] Security contractual clauses signed
- [x] Incident response SLA < 24h
- [ ] External validation of controls (in progress)

**Integration owner:** ana.gomes@empresa  

**Note:** onboarding conditional on the delivery of test evidence before go-live  
**Mandatory training validated:** ✔️ Owner and AppSec analyst with training in third-party validation (Ch. 13)

---

## 🔄 4. Example of a contract renewal with a review of requirements {#-4-exemplo-de-renovação-contratual-com-revisão-de-requisitos}

**Title:** [REV] Review of clauses and requirements at the renewal of the contract with supplier “DataStore”

**Context:**  

Licensing contract for cloud storage software, used by L2 systems.

**Actions carried out:**
- [x] Update of the contractual clauses to reflect new requirements (EX-DAT-004, EX-BKP-002 — illustrative identifiers; they do not correspond to the Requirements Catalogue of Ch. 02)
- [x] Technical validation of the SBOM of the synchronisation agent
- [x] Formal acceptance of an SLA for mitigation of CVEs in `<`5 days
- [x] Updated training of the PO and of the DevOps / SRE team involved

**Renewal owner:** sofia.rodrigues@empresa  

**Date of the new signature:** 2025-07-10  
**Mandatory training validated:** ✔️ Documented in an internal repository (Ch. 13)

---

## 🧪 5. Example of a temporary exception with planned reassessment {#-5-exemplo-de-exceção-temporária-com-reavaliação-planeada}

**Title:** [SEC] Exceptional approval for the absence of MFA in the build management tool

**Justification:**  

The tool used (BuilderX) does not support multi-factor authentication. The risk was compensated with IP restriction and continuous logging.

**Risk level:** L3  

**Missing requirement:** ACC-007
**Compensation:** Access limited via VPN + daily analysis of the logs  

**Approval:** AppSec team + DevSecOps + CISO  
**Validity:** 3 months with reassessment scheduled in the security backlog  

**Mandatory training validated:** ✔️ CISO and technical owner with training in exceptions (Ch. 13)

---

## 🛠️ 6. Example of a supplier rejected after incomplete onboarding {#️-6-exemplo-de-fornecedor-rejeitado-após-onboarding-incompleto}

**Title:** [ONB] Rejection of supplier “CloudParser” for a data transformation pipeline

**Risk classification of the application:** L3

**Reason for rejection:**
- [x] Failure to deliver an up-to-date SBOM
- [x] Refusal of contractual clauses on audit
- [x] Inability to demonstrate an incident response channel

**Decision:** Rejected by the technical approval committee (AppSec, Owner, GRC)  

**Owner:** miguel.pinto@empresa  
**Notes:** viable alternative already identified (supplier “ParseVault”)

---

## 📆 3. Risk decision record template {#-3-template-de-registo-de-decisão-de-risco}

**Suggested format:** Jira / SharePoint / traceable Excel

| Field                     | Value                                                          |
|--------------------------|----------------------------------------------------------------|
| Application name         | app-inventario                                                |
| Risk level            | L2                                                             |
| Requirements not applied  | LOG-005, EX-AUD-003                                            |
| Technical justification      | No infrastructure for extended retention; compensated with snapshots  |
| Compensation applied      | Alerts via SIEM + external backup                             |
| Owner and approval         | nuno.ferreira@empresa + CISO                                  |
| Validity of the decision       | 3 months + scheduled reassessment                              |
| Mandatory training      | ✔️ Both with valid internal certification (`<`12 months)

*Illustrative identifiers (`EX-…`); they do not correspond to the Requirements Catalogue of Ch. 02.*

---

## ✅ Recommendations {#-recomendações}

- These models must be **normalised and reused** across projects
- They may be made available via templates in Confluence, Git or ALM
- They must be associated with the application, supplier or release artefacts
- The existence of these records supports audits, governance and executive decision
- **Mandatory training for critical functions** (Ch. 13) must be verified before formal validations
- Whenever part of the process is supported by automated mechanisms, the record must make explicit who validated and took on the final decision.

---
