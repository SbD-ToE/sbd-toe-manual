---
id: checklist-revisao
title: Checklist - Training and Secure Onboarding
sidebar_label: Review Checklist
description: Binary, traceable verification checklist of the adoption of the practices of Chapter 13.
tags: [checklist, formacao, onboarding, controlo, validacao, auditoria]
sidebar_position: 20
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/canon/20-checklist-revisao.md
  source_sha256: c7545fdc5649bd6f6b62e4794234dc0decc813f19e8857ae61bdb8e55df4249e
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: d12a0d9612cc077c38de50beda23b1d90830fc8c56ccfdce57e7aca37bcfb1b9
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, capacitacao, chapter_role, cycle_iteration, lifecycle_phase, maturity, mcp_reading_programa, papel_suporte, practitioner_manual, programme_line, sbdtoe_sbd, trilho_formativo, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 657b81e19efa78ef55777cde45760d195230607f7aa353454ab54176214091fa
  translated_at: 2026-09-26T12:49:03Z
  stamped_at: 2026-09-26T18:36:05Z
  reviewed_by: null
---


# Periodic Review Checklist - Training and Secure Onboarding

This checklist applies to all **technical staff, internal or external**, with a direct impact on the development, operation or maintenance of software.
It enables a **binary, objective and traceable** assessment of the practical adoption of the prescriptions of **Chapter 13 - Training and Secure Onboarding** (`TRN-001` to `TRN-009`).

> 🛠️ This control mechanism is essential to validate **risk-proportional training**, **technical validation before permissions**, **third-party management** and the **existence of an active security culture**.

---

## 📋 Verification Items {#-itens-de-verificação}

| Item                                                                                                              | Verified? |
|-------------------------------------------------------------------------------------------------------------------|-------------|
| Are there training tracks defined by functional profile and criticality level (L1–L3), with mandatory modules, duration and periodicity? (`TRN-001`) | ☐           |
| Is the track assigned to the staff member before the start of autonomous technical activity? (`TRN-002`)                    | ☐           |
| Is security onboarding (policies, secrets handling, incident process, controls of the role) completed before autonomous work? (`TRN-002`) | ☐           |
| Is there objective validation of completion with a defined minimum threshold and a remediation path for results below it? (`TRN-003`) | ☐           |
| Is the validation result traceable to the staff member and to the content version, archived in an institutional repository? (`TRN-003`) | ☐           |
| Is access to L2+ repositories, pipelines or environments conditional on evidence of valid onboarding? (`TRN-004`) | ☐           |
| Is there continuous training differentiated by level (L2 ≥ half-yearly, L3 ≥ quarterly), with attendance recorded? (`TRN-005`) | ☐           |
| Is the training content under version control and reviewed after triggers (incidents, policy changes, new vulnerability classes)? (`TRN-006`) | ☐           |
| Is there an equivalent onboarding process for third parties, with a responsibility statement and a record (name, entity, date, validator)? (`TRN-007`) | ☐           |
| Is there a formal Security Champions programme in L3 teams (documented role, allocated time, traceable appointment)? (`TRN-008`) | ☐           |
| Are there training effectiveness KPIs defined and collected, with deviations triggering corrective action (owner and deadline)? (`TRN-009`) | ☐           |
| Is there an active practical reinforcement mechanism (PR clinics, war rooms, CTFs or labs) and a repository of PR good practices? | ☐           |
| Is there mandatory training in the secure use of AI and tooling (when to trust vs. validate outputs, guardrails, validation of generated code and tests)? | ☐           |
| Do the teams have access to the SbD-ToE training manual per chapter and to a formal support channel (SPOC/Champion) during onboarding? | ☐           |
| Is there an isolated sandbox environment for contractors to practise in before access to real systems? | ☐           |
| Do incidents whose root cause is training result in an update of the training content? | ☐           |

---

## 🔄 Operational Integration {#-integração-operacional}

- This checklist may be integrated into **onboarding flows, permission reviews, initial PRs, internal audits or quarterly security cycles**.
- Verification must be based on **concrete evidence**: quizzes, PR comments, LMS records or attachments to tickets.
- The data may be aggregated by project, team or supplier, feeding security dashboards and reports.

> ⚠️ **Practices not met must have a documented formal justification**, approved by AppSec, GRC or technical management (waiver or temporary exception).

---

## ✅ Compliance and KPI {#-conformidade-e-kpi}

- This checklist makes it possible to declare **compliance with the practices of Chapter 13** in an auditable and measurable way.
- The number of affirmative answers may be used as an **indicator of the organisation's maturity** in upskilling-based security.
- The data generated must be included in **continuous improvement plans, lifecycle audits and technical quality objectives**.

> 📌 This mechanism ensures that **training is applied, validated and tracked**, as a structuring component of organisational security in the SbD-ToE model.
