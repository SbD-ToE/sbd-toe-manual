---
id: exemplos-aplicacao
title: Practical Example of Applying Requirements
description: Case study illustrating the application of requirements throughout the lifecycle
tags: [exemplo, aplicação, requisitos, rastreabilidade, validação]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/02-requisitos-seguranca/addon/15-exemplos-aplicacao.md
  source_sha256: 233c05d691a4e060c3aba8f3c4f3c8ef1f5cd16cbe22ad6b667da315257e37e3
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: cb6c8f18970a488d73d7a8256a3e5acaff450830440baa8bd77e2d069ff734a4
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, cycle_iteration, lifecycle_phase, papel_suporte, prescriptive, requirement_runtime, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 8baa563e081f295b80017e2f420f256f7c746466eb6aa29673cd4fc9d6be1b71
  translated_at: 2026-09-25T20:20:13Z
  stamped_at: 2026-09-26T18:33:06Z
  reviewed_by: null
---

# Examples of Applying Security Requirements

This annex illustrates, in practical terms, how to apply security requirements throughout the lifecycle of a new feature, based on the application's risk classification.

> ℹ️ This document presents a **complete practical example** of applying the security requirements defined in Chapter 2, showing how to apply them to a new feature throughout the development lifecycle.  
> It is not a prescriptive document but a **reusable case study** that follows the logic:  
> **classification → selection → traceability → validation**.  
> It can be adapted and replicated in other contexts, keeping the principles of proportionality and traceability.

## Scenario: New document upload feature in a B2B web application {#cenário-nova-funcionalidade-de-upload-de-documentos-numa-aplicação-web-b2b}

### 🧩 1. Context {#-1-contexto}

- Application: Contract management web portal
- Type: Web application with federated authentication
- Data: Contractual and personal (some sensitive)
- Classification: Level 2 (medium risk), as per Chapter 1
- New feature: Allow authenticated users to upload PDF documents

---

### 🔎 2. Review of the risk classification {#-2-revisão-da-classificação-de-risco}

Before defining requirements, the team reviews the application's classification in the light of the new feature:

| Factor                          | Change with the new feature         |
|-------------------------------|--------------------------------------|
| Exposure surface       | ↑ Direct upload by end users |
| Data sensitivity       | ↔ Unchanged (data was already sensitive)    |
| Third-party dependency      | ↔ No changes                     |

**Decision**: Remains at Level 2, but exposure increases.

---

### 📝 3. Identification of the relevant requirements {#-3-identificação-dos-requisitos-relevantes}

Based on the catalogue themes (Ch. 2) and the domains affected by the feature (input, files, authentication, logs), the following requirements are selected:

| ID       | Description                                                                 | Theme                            |
|----------|---------------------------------------------------------------------------|---------------------------------|
| REQ-003  | Sessions with a 15-minute inactivity timeout                          | Sessions and State                |
| EX-REQ-010  | Validation of type, extension and size on file upload             | Input and Output Validation     |
| EX-REQ-011  | Malware analysis before file storage                   | Antivirus and Malware             |
| EX-REQ-015  | Logging of upload attempts and associated errors                        | Logging and Auditing             |
| EX-REQ-018  | Creation of automated tests for malformed inputs on the API endpoint | Security Testing             |

*Illustrative identifiers (`EX-…`); they do not correspond to the Requirements Catalogue of Ch. 02.*

---

### 🔗 4. Traceability (risk → requirement → control → validation) {#-4-rastreabilidade-risco--requisito--controlo--validação}

| Identified risk                          | Requirement | Control implemented                       | Validation                     |
|--------------------------------------------|-----------|----------------------------------------------|-------------------------------|
| Upload of malicious files             | EX-REQ-011   | Antivirus integration in the pipeline         | CI/CD with automatic scan     |
| Abuse of the endpoint with large files    | EX-REQ-010   | 10 MB limit + MIME type check   | Functional test + logs        |
| Abusively long sessions                | REQ-003   | 15-minute timeout with re-authentication         | UI test + Selenium script |
| Lack of visibility over critical actions | EX-REQ-015   | Logging with alert level and centralisation  | Log review + alerts     |

*Illustrative identifiers (`EX-…`); they do not correspond to the Requirements Catalogue of Ch. 02.*

---

### 👥 5. Roles involved {#-5-papéis-envolvidos}

| Role                 | Contribution                                  |
|----------------------|---------------------------------------------|
| Dev Team             | Integration of the controls in the endpoints/API  |
| QA/Testing            | Writing the automated tests            |
| Security (AppSec)   | Validation of requirements and traceability   |
| Product Owner        | Inclusion of the criteria in the backlog and user stories |

---

### 📆 6. Checkpoint in the lifecycle {#-6-ponto-de-verificação-no-ciclo-de-vida}

- The requirements were included in the **user stories**
- The acceptance criteria were defined in Gherkin
- The tests were validated in the continuous integration (CI) phase
- Traceability validation was carried out during the sprint review with support from security

---

## Conclusion {#conclusão}

This example demonstrates the practical application of security requirements from risk identification through to technical validation, ensuring traceability, proportionality and integration with agile development processes.

> This same process can be reused in other cases with minimal adaptation, as long as the logic is kept: **classification → selection → traceability → validation**.
