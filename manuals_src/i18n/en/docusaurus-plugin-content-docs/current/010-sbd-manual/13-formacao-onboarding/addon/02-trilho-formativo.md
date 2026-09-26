---
id: trilho-formativo
title: Training Track by Risk Level
description: Training path adapted to the risk level (L1–L3) and to the technical profile of each member of staff.
tags: [formacao, trilho, risco, perfis, onboarding]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/addon/02-trilho-formativo.md
  source_sha256: 94e748cc3083c32ada128306534ec12ddae39abdffbea5fafe6ca87c12765086
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: fedec8ae064dca45b87b4c70f590a93f23a8ade84fb54ff6eb9d562c031f15aa
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, papel_suporte, provenance, risk_level, sbdtoe_sbd, trilho_formativo, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 0d4b4968475025a749bbb6889ecee11a5303c56e9c4f6122a4aed616cad19bf0
  translated_at: 2026-09-26T11:44:16Z
  stamped_at: 2026-09-26T18:35:53Z
  reviewed_by: null
---


# Training Tracks by Role and Risk

## 🌟 Objective {#-objetivo}

To define the **minimum mandatory content** to include in initial (onboarding) and continuous training, by functional profile and **application risk level**, in alignment with Chapter 01 - Risk Management.

> 📌 This matrix makes it possible to configure coherent training tracks on platforms such as an LMS, internal portals, the technical backlog or permission pipelines.

---

## 🧬 What a Training Track is {#-o-que-é-um-trilho-formativo}

A **training track** is a set of mandatory or recommended content assigned to a member of staff or role, based on their technical role and on the risk of the application they take part in. These tracks make it possible to align knowledge with the specific security demands of the project.

---

## 📋 Base Matrix by Profile and Risk Level {#-matriz-base-por-perfil-e-nível-de-risco}

| Role / Risk | L1 (low)                                    | L2 (medium)                                                  | L3 (high)                                                          |
|----------------|-----------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------------------|
| **Dev**        | Basic secure coding, dependencies            | Lightweight threat modelling, SCA, secure PR                        | Formal threat modelling, secure architecture, labs on vulnerable apps |
| **QA**         | Basic security testing                   | Acceptance criteria, lightweight fuzzing                        | Advanced fuzzing, validation of exceptions, SAST/DAST                    |
| **PO**         | Minimum requirements, secure backlog            | Risk classification, justified exceptions               | Formal acceptance process, review with AppSec                      |
| **DevOps**     | Secrets management, environment configuration | Secure integration in CI/CD, pipelines with scanners          | SLSA, provenance, continuous alerts, hardening                      |
| **AppSec**     | -                                             | Base tools, internal policies                        | Technical deepening, coaching for teams, advanced threat modelling |
| **Third parties**  | Organisation policy, support channels      | Minimum requirements, secure PR template                      | Customised training, conditional access, formal record             |

---

## 🛠️ How to apply {#️-como-aplicar}

- Instantiate the matrix in:
  - 🎓 Tracks in the learning management system (LMS)
  - 📋 Onboarding checklists by role
  - 📦 Tasks in the technical backlog (e.g. `formacao:secure-coding`)
- Ensure:
  - Explicit assignment by project and role
  - Formal record of completion (LMS, ticket, signature)
  - Regular updates in the face of new risks or technologies

---

## ✅ Good practices {#-boas-práticas}

- Incorporate the training tracks into the organisation's annual training plan
- Review the content based on lessons learnt from incidents
- Adjust the tracks based on feedback from champions and technical teams
- Link the tracks to permission profiles or access to environments

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                         | Relevance                                       |
|-----------------------------------|--------------------------------------------------|
| `01-catalogo-formativo.md`        | Defines the training topics by chapter       |
| `10-checklist-onboarding.md`      | Uses this matrix as the basis for verification       |
| `03-programa-champions.md`        | Champions help to maintain and adjust the tracks   |
| `90-indicadores-metricas.md`      | Measures coverage of and adherence to the tracks            |

---

> 🔒 This matrix operationalises the **proportional application of the SbD-ToE**, guaranteeing that every participant receives training appropriate to their role and to the risk involved.
