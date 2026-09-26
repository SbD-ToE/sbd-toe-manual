---
id: clausulas-contratuais
title: Security Contractual Clauses
sidebar_position: 3
description: Security contractual clauses in contracts with suppliers, contractors and technical third parties
tags: [fornecedores, validacao, terceiros, contratacao]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/addon/02-clausulas-contratuais.md
  source_sha256: def489d0f6a08e18b7f87ae765d97c6d8b309b7fe2e32cf9abdd8ae18fb0d8bc
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: cb758983d634067eaf59bf5922ea0b798d47b2a3983aa633f15499a50aa33e55
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [chapter_role, cycle_iteration, framework_source_corpus, lifecycle_phase, requirement_runtime, risk_level, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: 8d1537cb3830101f261667640f3ab1b3c13a0b8f8a25bae438b95d1e40673d63
  translated_at: 2026-09-26T12:00:12Z
  reviewed_by: null
---



# Security Contractual Clauses

## 🌟 Objective {#-objetivo}

To provide a set of **reusable contractual clauses proportional to risk**, adaptable to the type of contracting, to ensure that security requirements are **formally demanded, traceable and auditable**.

These clauses must:

- Reflect the **minimum requirements by risk** (Chapter 1 and 2);
- Be applicable to different types of contract: SaaS, outsourcing, licensing or mixed teams;
- Be valid throughout **the whole contractual lifecycle**, and not only in the initial phase;
- Provide for mechanisms of validation, penalty and objective accountability.

---

## 📘 What security contractual clauses are {#-o-que-são-cláusulas-contratuais-de-segurança}

They are formal provisions incorporated into contracts with suppliers, partners or contractors, which aim to guarantee **compliance with technical, legal and organisational security requirements**, including:

- Application of minimum controls;
- Incident notification;
- Delivery of evidence (e.g. SBOM, tests, reports);
- Vulnerability and update management;
- Accountability for failures or breaches.

> 📎 These clauses are essential to transfer security obligations and to align the supplier with the principles of the SbD-ToE.

The use of automated technical processes or mechanisms to support compliance with these clauses neither alters nor reduces the supplier's contractual responsibilities.
The supplier remains fully responsible for the compliance, evidence and results obtained, regardless of the degree of automation used.


---

## 🛠️ How to apply {#️-como-aplicar}

### 🧩 By type of contract {#-por-tipo-de-contrato}

#### 🏷️ SaaS / Managed services {#️-saas--serviços-geridos}

| Theme                    | Suggested clause                                                                                 |
|-------------------------|--------------------------------------------------------------------------------------------------|
| Minimum security        | The supplier guarantees compliance with the controls defined according to the risk level of the application. |
| Vulnerabilities        | Commitment to remediate critical CVEs in `<`72h after public disclosure.                        |
| SBOM / transparency    | Provision of an up-to-date SBOM with critical dependencies, upon request.             |
| Incidents              | Notification of security incidents within a maximum of 24h after detection.                      |
| Audit / evidence   | Right of the organisation to request evidence of controls or to carry out formal audits.         |

#### 🛠️ Development outsourcing {#️-outsourcing-de-desenvolvimento}

| Theme                    | Suggested clause                                                                                 |
|-------------------------|--------------------------------------------------------------------------------------------------|
| Requirements by risk    | Application of the requirements of the SbD-ToE Catalogue according to the risk level of the application.             |
| Integration into CI/CD     | Delivered artefacts must integrate pipelines with automated security tests.             |
| Security reviews   | Acceptance of code and architecture reviews by the organisation's security team.            |
| Intellectual property | Source code and security documentation are the property of the contracting organisation.             |

#### 👥 Internal development (contractors or mixed teams) {#-desenvolvimento-interno-contratados-ou-equipas-mistas}

| Theme                    | Suggested clause                                                                                 |
|-------------------------|--------------------------------------------------------------------------------------------------|
| Restricted access         | Access only to development environments, with temporary and traceable credentials.         |
| Training in SbD         | Mandatory training in Security by Design practices before technical contribution.     |
| Responsibilities       | Application of the assigned security requirements via documented tickets.                       |
| Traceability         | Complete record of the work linked to security tasks and validations.                         |

#### 💽 Licensing contracts (external software) {#-contratos-de-licenciamento-software-externo}

| Theme                    | Suggested clause                                                                                 |
|-------------------------|--------------------------------------------------------------------------------------------------|
| Compliance            | Compliance with recognised standards (e.g. ISO 27001, OWASP ASVS).                                |
| CVEs and updates     | Obligation to communicate and mitigate critical vulnerabilities promptly.                       |
| Security updates | Right of the organisation to corrective updates during the contract.                          |
| Data and telemetry      | Transparency and explicit consent for the collection of data or metrics.                       |

---

## 📊 Additional clauses per risk level {#-cláusulas-adicionais-por-nível-de-risco}

| Risk Level | Recommended additional clauses                                                                      |
|----------------|--------------------------------------------------------------------------------------------------------|
| **L1 (low)** | Generic commitment to good practices; incident notification policy                         |
| **L2 (medium)** | Application of the SbD-ToE Catalogue; provision of technical evidence on request                      |
| **L3 (high)** | Mandatory security tests; SBOM delivered; SLA for critical fixes; formal right to audit |

> 📘 Use the requirements application matrix (Ch. 1 - Annex 06) as the basis for deciding the contractual level required.

---

## 📋 Recommended fields per clause {#-campos-recomendados-por-cláusula}

Each clause must include:

- Reference to the **applicable requirement** (e.g. LOG-002, ARC-005);
- Indication of the **risk level** (L1–L3);
- Expected form of validation (technical evidence, audit, tests);
- Penalties or contractual impact in the event of breach;
- Review periodicity (e.g. at renewals, new versions or releases).
- Identification of the technical processes or mechanisms used to support compliance with the clause, where applicable.


---

## 📂 Integration with procurement and legal {#-integração-com-procurement-e-jurídico}

- Make clauses available in a **modular format** (blocks by type and by risk);
- Maintain a repository of validated versions (e.g. Git, Confluence, SharePoint);
- Integrate into the supplier onboarding model (see `03-modelo-validacao-fornecedores.md`);
- Ensure basic training of stakeholders in the link between risk and contractual requirement.

---

## ✅ Good practices {#-boas-práticas}

- Prefer **objective, auditable and risk-proportional** clauses;
- Avoid vague or generic language without validation criteria;
- Align clauses with real security requirements (Ch. 2 and 7);
- Reassess clauses periodically, especially at renewals or technical changes;
- Record the clauses actually applied to each contract.

---

## 🔗 Cross-references {#-referências-cruzadas}

| Document / Chapter                 | Relationship with contractual clauses                   |
|--------------------------------------|-----------------------------------------------------|
| Chapter 01 - Risk Management        | Defines proportionality per level L1–L3         |
| Chapter 02 - Security Requirements| Catalogue and applicable requirements by risk         |
| addon/03-modelo-validacao-fornecedores.md | Contractual onboarding requirements               |
| addon/00-catalogo-requisitos.md      | GOV-006/GOV-007: contractual acceptance criteria |

---
