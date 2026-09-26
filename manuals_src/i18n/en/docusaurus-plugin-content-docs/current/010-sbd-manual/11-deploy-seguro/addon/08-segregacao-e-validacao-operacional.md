---
id: 08-segregacao-e-validacao-operacional
title: Operational Validation with Segregated Environments
description: Strategies for validation in staging and pre-prod environments that ensure readiness and operational security.
tags: [tipo:anexo, grupo:execucao, tema:validacao, staging, segregacao, readiness]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/addon/08-segregacao-e-validacao-operacional.md
  source_sha256: 9a93eed1509b816802e1cace1119e35d3e29e184911929e0274baaa85c46f473
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: c12d735d64cfcbf2338f697615237511a420842f42c98789f617b6d8bacfaae7
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [requirement_runtime, traceability, validation_evaluation]
  glossary_sha256: 6152b3aba3f7abe5427f15240df77801c41069771b4d4841c3f5d2248486cae3
  translated_at: 2026-09-26T11:00:51Z
  stamped_at: 2026-09-26T18:35:29Z
  reviewed_by: null
---


# Environment Segregation and Operational Validation

A clear separation between environments (development, QA, staging, production) is an essential practice for mitigating risks and preventing unvalidated code from being executed in sensitive contexts. This document defines practices for **secure segregation and validation before promotion to production**.

---

## 🌐 Separating is protecting {#-separar-é-proteger}

| Environment      | Main objective                           | Suggested restrictions                        |
|---------------|-----------------------------------------------|-----------------------------------------------|
| **Dev**       | Active development                         | Open access, fictitious data               |
| **QA/Test**   | Functional and regression tests                | Controlled data, access by QA              |
| **Staging**   | Environment identical to production for validation | Same versions and configuration              |
| **Production** | Real execution and sensitive data               | Only authorised and segregated access          |

> 💡 Shared environments increase the risk of data exposure and unexpected side effects.

---

## 🛡️ Security requirements per environment {#️-requisitos-de-segurança-por-ambiente}

- **Access and authentication**:
  - MFA for staging and production
  - Distinct RBAC profiles per environment

- **Data used**:
  - Real data **only in production**
  - Masking or synthetic data in the others

- **Infrastructure segregation**:
  - Distinct VPCs/subnets
  - Separate secrets and vaults
  - Pipelines with segregated tokens and permissions

---

## 🔢 Final validation before production {#-validação-final-antes-de-produção}

| Validation type                  | Description                                                       |
|------------------------------------|------------------------------------------------------------------|
| **Functional checklist**            | All requirements validated?                                   |
| **Security checklist**        | Findings, toggles, rollback, logging                              |
| **Reversibility test**       | Functional rollback tested?                                       |
| **Formal approval**              | By whom? QA, AppSec, manager?                                      |
| **Change audit**        | Which code / config was changed?                                  |

---

## 🚑 Testing in production safely {#-testes-em-produção-com-segurança}

In some contexts, it may be necessary to validate in production:
- With feature flags and a limited scope
- With reinforced logs and alerts
- With immediate rollback prepared

> ❌ Never carry out manual tests with real users without traceability, approval and guaranteed rollback.

---

## 💼 Mandatory recording and audit {#-registo-e-auditoria-obrigatória}

- Which version was promoted
- By whom
- Which validators passed (security, functionality)
- Justification of exceptions, if applicable
- Evidence of tested rollback

---

## ✅ Operational validation checklist {#-checklist-de-validação-operacional}

- [ ] Is the staging environment equivalent to production?
- [ ] Is the production pipeline segregated from the others?
- [ ] Are all accesses controlled by MFA and RBAC?
- [ ] Were the final validations executed and documented?
- [ ] Is there a tested rollback ready to use?
- [ ] Are the configurations audited and versioned?

> 🔒 Environment segregation is a fundamental requirement for organisational security and compliance.
