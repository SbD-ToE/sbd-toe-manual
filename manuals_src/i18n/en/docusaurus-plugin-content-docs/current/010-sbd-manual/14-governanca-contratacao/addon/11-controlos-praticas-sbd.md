---
id: controlos-praticas-sbd
title: Governance Controls over the SbD-ToE Practices
sidebar_position: 11
description: Ways of validating, reinforcing and governing the application of the controls defined in other chapters of SbD-ToE
tags: [governanca, controlo, validacao, enforcement]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/addon/11-controlos-praticas-sbd.md
  source_sha256: fdebdb692f7e999f482455a9375d918f4f50bbb8c43f28d0112340ec8b002b9c
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 8c43d735c1d33ffe28be7f0d625903d76decb9bffaec8742bf23fdbbc3f237ee
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, lifecycle_phase, maturity, practitioner_manual, sbdtoe_sbd, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: a12d6ab9dfdf3cf9a4ed3e07275ffc4d86cffd85bbf01418d32a31bf82e5df76
  translated_at: 2026-09-26T12:00:18Z
  stamped_at: 2026-09-26T18:36:18Z
  reviewed_by: null
---


# Systematic Control of the SbD-ToE Practices

This document defines the model for the **systematic and continuous control** of the application of the practices prescribed across all the chapters of the manual *Security by Design - Theory of Everything (SbD-ToE)*.

> 📌 The objective is to ensure that **all security practices are effectively applied, traced, validated and audited** per application, over time.

---

## 🧭 Governance of practices by technical domain {#-governação-das-práticas-por-domínio-técnico}

| Chapter / Technical Domain             | Expected Governance Mechanisms                                               | Examples of Evidence / KPI                         |
|----------------------------------------|----------------------------------------------------------------------------------|-----------------------------------------------------|
| **Ch. 02 - Requirements**               | Validation of the application by L1–L3, exception management, traceability evidence | Checklist applied, % of REQ applied / justified |
| **Ch. 03 - Threat Modelling**          | Execution per milestone, defined owner, periodic update                   | Models per application, review history        |
| **Ch. 05 - Dependencies and SBOM**      | Automatic generation of SBOM, SCA analysis, record of findings                    | Findings reports, % resolved and justified |
| **Ch. 07 - Secure CI/CD**             | Validation of pipelines, tracing of executions, bypass control               | Audited executions, formal bypass approvals   |
| **Ch. 08 - Secure IaC**               | Continuous validation of modules, owners per environment, traceability             | Issues + owners per resource, % of modules validated |
| **Ch. 09 - Containers and Images**     | Application of image policies, origin and signature validations             | Validated catalogue, scanner evidence             |
| **Ch. 10 - Security Testing**      | Execution by L1–L3, findings management, periodic revalidation                   | Test evidence, resolution plan             |
| **Ch. 11 - Deployment and Execution**        | Runtime validation, isolation, controlled executions                         | Execution control, versioned logs             |
| **Ch. 13 - Training and Third Parties**     | Verification of training by profile, onboarding with validation                    | List of training by function, onboarding checklist  |

---

## 🧩 Format of the control per application {#-formato-do-controlo-por-aplicação}

Each application must have a **compliance repository**, with:

- Binary checklist per chapter (`20-checklist-revisao.md`)
- Application status per practice (yes / exception / not applicable)
- Evidence of validation and approval
- History of changes and decisions
- Identification of the person responsible for accepting the status of each practice, when supported by automated validations.


> ⚠️ There must be traceable and versioned files (e.g. `.yaml`, `.md`, GRC dashboards).

---

## 🔁 Continuous validation cycle {#-ciclo-de-validação-contínua}

| Phase                      | Expected action                                    |
|---------------------------|--------------------------------------------------|
| 🧱 Project start       | Activate control mechanisms and owners per practice |
| 📥 Integration of changes  | Review the status of the impacted controls            |
| 🚀 Pre-release             | Verify compliance and justified exceptions   |
| 📊 Audit / review     | Validate the overall status by chapter and domain       |

---

## 📡 Supervision, KPIs and Escalation {#-supervisão-kpis-e-escalonamento}

- The status of the practices must be **consolidated in operational dashboards** with:

  - % of practices fulfilled per application / team
  - Open exceptions per chapter
  - Average revalidation cycle

- Persistent failures must be **reported to risk management or GRC** with an action plan.

---

## ✅ Conclusion {#-conclusão}

This model makes it possible to:

- Govern the adoption of SbD-ToE in a continuous, transparent and auditable way
- Consolidate security information from all applications in a single point
- Support decisions, audits and the evolution of maturity based on evidence

> 📌 This control is the basis of the **comprehensive governance of application security**, and must be activated by all the teams that adopt SbD-ToE.
