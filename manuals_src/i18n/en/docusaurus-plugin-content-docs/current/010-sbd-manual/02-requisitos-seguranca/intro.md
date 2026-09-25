---
id: intro
title: Security Requirements
description: Definition, application, validation and traceability of application security requirements by risk level
tags: [tipo:prescricao, tema:requisitos, segurança, rastreabilidade, validação, proporcionalidade, SSDF, SAMM, DSOMM, ASVS]
sidebar_position: 1
translation:
  source_locale: pt
  source_path: 010-sbd-manual/02-requisitos-seguranca/intro.md
  source_sha256: 61552256461a73af801de74226dee216a866c7389722a0f4376d48127d3b3ba7
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 65027768c82f59ae0b05ce93a1f93da2e77b22eecbc1cb2d4f5e7b478bf2e594
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [audit_trail, basilar, chapter_role, cycle_iteration, lifecycle_phase, mapping, normative_empirical, practitioner_manual, provenance, requirement_runtime, risk_level, sbdtoe_sbd, traceability, transversal, validation_evaluation]
  glossary_sha256: 27916dda11391bea413b8a50d02a1f45c3eb9b52973c556d24d12a2eab413602
  translated_at: 2026-09-25T20:20:18Z
  reviewed_by: null
---

import ChapterTypeCallout from '@site/src/components/ChapterTypeCallout';

<ChapterTypeCallout kind="basilar" title="Capítulo Basilar">

This chapter is considered **foundational** in the *Security by Design – Theory of Everything (SbD-ToE)* model.
Its application is **mandatory** to guarantee the coherence, traceability and effectiveness of the remaining security practices.

The foundational chapters constitute the **technical and methodological foundation** of the model. The absence or partial application of any of them compromises the **overall integrity** of SbD-ToE, making the coherent adoption of operational and governance practices unfeasible.

</ChapterTypeCallout>

# Security Requirements

This chapter defines the **normative framework of application security requirements** of SbD-ToE, as well as the **process for their correct application, validation and traceability** throughout the entire development lifecycle.

The central focus is on:
- **proportionality to risk**, determined by the classification of the application (L1–L3);
- **practical verifiability**, ensuring that each requirement can be validated objectively;
- **complete traceability**, linking risk, requirement, control and evidence;
- **governance of the requirement lifecycle**, ensuring review, versioning and explicit updating whenever material changes occur in risk, architecture, exposure or integrations.

The chapter also addresses good practices in **requirements management**, the definition of **acceptance criteria**, the use of **reusable catalogues** and the integration of security requirements into agile development processes (e.g. backlog, user stories, acceptance criteria).

In this sense, the chapter functions not only as a **normative catalogue**, but also as the **governance centre for security requirements**: from here derive the minimum rules for risk-proportional selection, review and versioning, the link to *Threat Modelling*, the link to validation and the formal handling of exceptions.

It includes, in particular:

- A **normative catalogue of technical requirements**, organised by theme and application type  
  → see [Requirements Catalogue](/sbd-toe/sbd-manual/requisitos-seguranca/addon/catalogo-requisitos)
- A **traceability taxonomy** with normalised identifiers and tags  
  → see [Traceability Taxonomy](/sbd-toe/sbd-manual/requisitos-seguranca/addon/rastreabilidade-controlo)
- Recommendations for the **objective and testable validation** of requirements  
  → see [Requirements Validation](/sbd-toe/sbd-manual/requisitos-seguranca/addon/validacao-requisitos)
- A **formal exception management process**, including justification and risk acceptance  
  → see [Exception Management](/sbd-toe/sbd-manual/requisitos-seguranca/addon/gestao-excecoes)
- Detailed explanations of the **rationale behind the requirements** and their alignment with frameworks such as **OWASP ASVS** and **NIST SSDF** (see the corresponding sections in this chapter)

---

## 📊 Summary Table of Requirements Themes {#-tabela-resumo-dos-temas-de-requisitos}

The requirements catalogue is organised into **20 technical themes**, identified by the codes **T01–T20**.  
Each theme groups requirements with technical and operational affinity, and is applied proportionally to the **risk level of the application**.

| Code | Theme                                     | Short description                                                     |
|--------|------------------------------------------|------------------------------------------------------------------------|
| T01    | Authentication and Identity Management       | MFA, sessions, credential management                                    |
| T02    | Access Control                        | RBAC, least privilege, segregation of duties                          |
| T03    | Logging, Auditing and Monitoring        | Logs, critical events, retention, SIEM                                 |
| T04    | Session Management                         | Tokens, timeouts, logout, protection against theft                        |
| T05    | Data Validation and Sanitisation          | Input validation, safe output, protection against injection            |
| T06    | Protection of Sensitive Data               | Ciphers, hashing, classification, access policies                    |
| T07    | Cryptography and Key Management           | Algorithms, rotation, secure storage, use of vaults               |
| T08    | Error and Message Handling           | Stack traces, generic messages, exceptions                            |
| T09    | API and Integration Security            | Mutual authentication, whitelisting, rate limiting, mTLS                  |
| T10    | Secure Configuration                       | Environment separation, parameterisation, configuration validation      |
| T11    | Code and Build Security               | Linters, SAST, pipelines, internal dependencies                        |
| T12    | Dependency Management and SBOM             | Updates, SCA, SBOM, severity policies                       |
| T13    | Secure CI/CD                              | Environment control, provenance, pipelines and validation             |
| T14    | Infrastructure as Code                | Terraform, Ansible, policy validation                             |
| T15    | Containers and Isolated Execution             | Trusted images, hardening, scanning, runtime controls             |
| T16    | Deploy, Release and Runtime Controls        | Reversibility, pre-production validation, environment segregation       |
| T17    | Security Testing                       | SAST, DAST, fuzzing, pipeline integration                            |
| T18    | Continuous Monitoring and Alerting          | Incident detection, real-time alerts                           |
| T19    | Training, Onboarding and Profiles             | Secure profiles, segregation, awareness                             |
| T20    | Governance, Reviews and Compliance       | Security reviews, contractual clauses, risk acceptance       |

> 📌 The selection of the themes to apply is made on the basis of the  
> [Controls Matrix by Risk](./addon/matriz-controlos-por-risco).

---

## 🧪 Practical prescription: what, who, how, when, why and to what end {#-prescrição-prática-o-quê-quem-como-quando-porquê-e-para-quê}

### 📌 What must be done {#-o-que-deve-ser-feito}

1. Identify and document security requirements on the basis of risk  
   (see [Chapter 1 - Classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro))
2. Ensure that all requirements are **verifiable and testable**
3. Integrate security requirements into the application's **functional backlog**
4. Guarantee **systematic traceability** between risk, requirement, control and evidence, using the defined taxonomy
5. Establish **clear acceptance criteria** for each requirement
6. Review and version requirements whenever there are material changes in risk, architecture, exposure, integrations or data processed
7. Review, maintain and justify exceptions on the basis of formal risk acceptance criteria

### ⚙️ How it must be done {#️-como-deve-ser-feito}

- Use catalogues such as the one proposed in this manual or consolidated references such as the **OWASP ASVS**
- Adapt the requirements to the **risk level and application type**
- Keep the requirements in a **versioned and auditable** format (e.g. Markdown, Excel, Jira)
- Associate requirements with **clear acceptance criteria** (e.g. Gherkin, checklists)
- Identify requirements with **normalised tags** from the `SEC-Lx-XXX` taxonomy
- Record review decisions, changes and the *re-triggering* of analysis whenever the application context changes materially
- Validate the requirements against the criteria defined in the validation section

> 🧩 Use traceability matrices (risk → requirement → control → validation)  
> 🎯 Define objective rules for the testability of each requirement

### 📆 When to apply {#-quando-aplicar}

- In the requirements definition and/or architecture phase
- After **Threat Modelling** is completed (Ch. 3)
- Whenever the risk, exposure or context of the application changes
- In security reviews, *design reviews*, *sprint planning* or *milestones*

### 👥 Who is involved {#-quem-está-envolvido}

| Role/Function             | Main contribution                                                  |
|--------------------------|------------------------------------------------------------------------|
| Software Architects / DevOps / SRE | Translation of risks into concrete technical requirements          |
| Product Owner       | Integration into the backlog and user stories                        |
| AppSec Engineer          | Definition of models, validation and alignment                          |
| QA                       | Definition of acceptance criteria and practical validation                |

> ✅ Traceability and testability are shared responsibilities.

### 🎯 Why / To what end {#-porquê--para-quê}

- Reduce risk from the earliest phases
- Avoid rework and late correction costs
- Support audits and compliance obligations
- Increase confidence in *releases*
- Integrate security natively into agile processes

---

## ⚠️ Caveats and limitations {#️-caveats-e-limitações}

- Generic or untestable requirements add no value
- The uncritical application of checklists can create a false sense of security
- Manual traceability can be burdensome without the support of adequate tools
- The use of heavily automated processes **does not dispense with independent validation, explicit responsibility or verifiable evidence**

---

## 🔍 What more can be done (and why) {#-o-que-pode-ser-feito-mais-e-porquê}

- Create reusable internal catalogues, taking the catalogue in this manual as a basis
- Adopt formal or semi-formal languages for acceptance criteria
- Link requirements to technical documentation, diagrams and automated tests
- Automate traceability between risk and requirement with ALM tools

---

## 📌 Note on scope, process and extensibility {#-nota-sobre-âmbito-processo-e-extensibilidade}

This chapter defines an **essential and cross-cutting set of application security requirements**, applicable to most enterprise, web and *cloud-native* systems.

The **characteristics of the development and delivery process** - including a high degree of automation, automatic generation of artefacts, use of *low-code/no-code* platforms or greater dependence on third parties - **do not change the base requirements catalogue or the L1–L3 classification of the application**, which continue to be determined by the impact and exposure of the system.

However, these contexts **demand greater rigour in the application, validation, evidence and traceability of requirements**, implying the reinforcement of the practices described in the technical chapters of the manual, namely **Secure Architecture, CI/CD, Infrastructure as Code, Secure Development and Security Testing**.

Applications with specific technical profiles (e.g. embedded systems, IoT, SCADA, mobile, medical or industrial applications) may also require additional requirements and controls, and should be complemented with specialised references such as:

- OWASP Mobile Security Testing Guide (MSTG)
- OWASP Internet of Things Project
- IEC 62443 - Security for Industrial Systems
- NIST SP 800-213 - IoT Device Cybersecurity

> The definition and maintenance of the requirements catalogue and its validation must always follow the principles of structural coherence, proportionality by risk level and complete traceability.

---

## 📜 Relevant Organisational Policies {#-políticas-organizacionais-relevantes}

| Policy                           | Mandatory | Application           | Minimum expected content                                 |
|------------------------------------|:-----------:|---------------------|----------------------------------------------------------|
| [Security Requirements Policy](/sbd-toe/assets/policies/policy-requisitos-seguranca) | Yes         | All applications | Definition, review, traceability, risk acceptance  |
| [Security Testing Strategy Policy](/sbd-toe/assets/policies/policy-estrategia-testes)    | Yes         | L2/L3 apps          | Criteria, evidence, acceptance, review cycle        |
| [Traceability Policy](/sbd-toe/assets/policies/policy-rastreabilidade)        | Optional    | Critical apps       | Requirement→control→validation mapping, audit       |
| [Exception Management Policy](/sbd-toe/assets/policies/policy-gestao-excecoes)     | Yes         | All               | Formal process of justification, recording and acceptance     |

[📎 See the details of the policies recommended for this chapter](./policies-relevantes)  
For the printed version, see the **manual's policy annex**.
