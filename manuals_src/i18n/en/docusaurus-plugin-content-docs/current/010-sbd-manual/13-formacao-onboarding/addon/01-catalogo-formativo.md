---
id: catalogo-formativo
title: Training Catalogue by Technical Profile
description: List of minimum training content by technical profile for onboarding and continuous upskilling.
tags: [formacao, perfis, conteudos, catalogo, onboarding]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/addon/01-catalogo-formativo.md
  source_sha256: 784468a409bdd3aeb072d4bcc35ae79a5f439392b792e8369e81cf58865723e1
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 092bdef9e45d29fa76f7d7c0c3291ee2c70a77032939fa2f90255b7bd5f08631
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [avaliacao, capacitacao, chapter_role, cycle_iteration, lifecycle_phase, practitioner_manual, risk_level, role_procurement, role_tech_lead, sbdtoe_sbd, trilho_formativo, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 7b04fcf0f6adef64092b748ec217b0823f7f85c0ce7df0fcfcd452465a180302
  translated_at: 2026-09-26T11:44:16Z
  stamped_at: 2026-09-26T18:35:52Z
  reviewed_by: null
---


# SbD-ToE Training Content Catalogue

## 🌟 Objective {#-objetivo}

To cross the **14 technical chapters of the SbD-ToE manual** with the **essential training content**, so as to guide:

- The creation of **training tracks** by role and criticality;
- The proportional assignment of content to **risk levels (L1–L3)**;
- The choice of **appropriate pedagogical formats** by profile and context.

This catalogue serves as the basis for training programmes, onboarding, labs and internal CTFs - and can be instantiated as a curricular structure in an LMS.


> The training content described here assumes a context of strong support from automated tools throughout the lifecycle, without this replacing the need for human understanding of the associated processes, limits and responsibilities.

---

## 🧬 What it contains {#-o-que-contém}

The matrix defines, for each technical chapter of the manual:

- The **topics to teach**
- The **target audience** (roles)
- The **minimum risk level** applicable
- The **suggested learning format**

> 📌 It serves as a reference for tracks, for training by context (e.g. an incident), and as the basis for the expanded training manual.

---

## 📋 Table Structure {#-estrutura-da-tabela}

| Chapter | Topic to teach                   | Target audience       | Risk level | Suggested format                         |
|----------|------------------------------------|---------------------|----------------|------------------------------------------|

---

## 📘 Map by Chapter {#-mapa-por-capítulo}

| Chapter | Topic to teach                              | Target audience       | Level | Suggested format                    |
|----------|-----------------------------------------------|---------------------|--------|-------------------------------------|
| 1. Risk Management         | Application classification             | PO, Dev, QA         | Medium  | Practical exercise + template       |
|                            | Technical risk assessment              | PO, AppSec          | High| Workshop + simulation               |
| 2. Security Requirements | Secure specification of user stories   | PO, QA              | Medium  | Lab + cross-review              |
|                            | Use of the internal requirements catalogue  | Dev, PO             | Medium  | Quiz + practical application           |
| 3. Threat Modelling         | Modelling by real functionality      | Dev, QA, PO         | Medium  | Practical session + lead rotation   |
|                            | Use of checklists in design            | QA, AppSec          | Low  | Template + peer-led explanation     |
| 4. Secure Architecture      | Architecture patterns and anti-patterns    | Dev, Tech Leads      | High| Comparative workshop + pairing      |
| 5. Dependency Control| SBOM, lockfiles and SCA control      | Dev, DevOps         | Medium  | PR clinic + lab with a scanner        |
|                            | Alert triage                     | AppSec, Dev          | High| Rotating review + internal lab     |
| 6. Secure Development  | Secure PR and code validation        | Dev, QA             | Medium  | Public review + annotated guide   |
|                            | Common mistakes / top 5 failures         | Dev                 | Low  | Quiz + example of a real PR          |
| 7. Secure CI/CD            | Pipelines with scanners                 | DevOps              | Medium  | Practical workshop + checklist        |
|                            | permission scopes in tokens        | DevOps              | High| Lab + abuse simulation           |
| 8. Secure IaC              | Use of scanners (e.g. TFSec)            | DevOps, CloudEng    | Medium  | Lab with insecure Terraform         |
|                            | Good practices in IaC pipelines         | DevOps              | Medium  | PR review + clinic                 |
| 9. *containers* & Images   | Secure Dockerfiles                    | Dev, DevOps         | Medium  | Lab + analysis of a real image       |
|                            | Base images and hardening               | DevOps              | High| Validation checklist + pairing   |
| 10. Security Testing    | Use of DAST in staging                 | QA, Testers         | Medium  | Hands-on lab + bug template     |
|                            | Introduction to fuzzing                  | QA, AppSec          | High| Demo + guided exercise          |
| 11. Secure Deployment          | Secure configuration and rollback         | DevOps              | Medium  | Simulation + educational post-mortem   |
| 12. Monitoring and Operations          | Relevant alerts and false positives | DevOps, QA          | Medium  | Detection game + dashboard        |
| 13. Training & Onboarding  | Rotating labs, PR clinics, CTF        | All               | All  | Regular sessions + rotation        |
| 14. Governance & Contracting | Security clauses in contracts | Management, Procurement | High| Case study + legal checklist   |

---

## 🛠️ How to apply {#️-como-aplicar}

- Instantiate as a reference matrix in:
  - Onboarding programmes by role
  - Curricular structure in an LMS
  - Annual upskilling plans
- Relate to:
  - Entry checklists (e.g. `10-checklist-onboarding.md`)
  - Third-party contracting policies (e.g. `21-plano-formacao-terceiros.md`)
  - Metrics and indicators (e.g. `90-indicadores-metricas.md`)

---

## ✅ Good practices {#-boas-práticas}

- Review the topics by chapter and role annually
- Use the matrix as the basis for creating internal labs and workshops
- Validate learning with quizzes, clinics or realistic simulations
- Use it in training derived from real incidents

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                           | Relation                                     |
|-------------------------------------|---------------------------------------------|
| `02-trilho-formativo.md`            | Defines the application of the matrix by risk      |
| `03-programa-champions.md`          | Support for dissemination                      |
| `10-checklist-onboarding.md`        | Verification of the content learnt           |
| `20-modelo-inclusao-terceiros.md`   | Application adapted to external suppliers  |
| `90-indicadores-metricas.md`        | Measurement of training adoption and effectiveness    |

---

> 📚 This catalogue may evolve into **Volume II - SbD-ToE Training Manual**, with content, exercises and labs by chapter, role and risk level.
