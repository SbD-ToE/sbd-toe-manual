---
id: checklist-onboarding
title: Technical Onboarding Checklist
description: Formal verification checklist for secure technical onboarding, with a record and validation per role.
tags: [onboarding, checklist, permissao, rastreabilidade, controlo]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/addon/10-checklist-onboarding.md
  source_sha256: 915ad63187ee842ed0c452db8668fc47b4025a7f9b1cb37dfbfabe70dede7414
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 822587b00048e91f8e98e57b87baf943c18bdd8da46dbabfce243339b025ad94
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, practitioner_manual, sbdtoe_sbd, traceability, trilho_formativo, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 6d4a84460d3e9999f3cdab4c2dfceeeeabf3e3c9cf16a73aaeef6c587ecaa61c
  translated_at: 2026-09-26T11:44:21Z
  stamped_at: 2026-09-26T18:35:58Z
  reviewed_by: null
---


# Secure Technical Onboarding Checklist

This checklist makes it possible to verify whether the onboarding process of a member of staff (internal or external) meets the minimum requirements defined in **Chapter 13 - Training and Onboarding**, in a way that is **proportional to the risk and to the assigned role**, and with **formal traceability**.

> 📌 It may be used by Dev Leads, AppSec, Champions, HR or project managers to ensure that the person is fit to intervene technically in the system.

---

## 📋 Items to validate (per member of staff) {#-itens-a-validar-por-colaborador}

| Item                                                                                                 | Verified? |
|------------------------------------------------------------------------------------------------------|-------------|
| Assignment of the correct training track, based on the role and on the risk of the application                  | ☐           |
| Completion of the training track (videos, labs, synchronous sessions, guided reading)                   | ☐           |
| Knowledge validation (quiz, practical exercise or simulation) successfully carried out              | ☐           |
| Participation in or submission of a real or simulated PR with a security focus (e.g. guided review)   | ☐           |
| Access to the repository of good practices, templates, policies and tools confirmed               | ☐           |
| Technical access (Git, pipelines, environments) conditional on completion of the process                     | ☐           |
| Formal record of completion archived (SharePoint, LMS, Git, issue tracker or form)           | ☐           |
| Support contact identified (e.g. SPOC, Champion, Teams/Slack channel or reference document)       | ☐           |

---

## 🧭 Application notes {#-notas-de-aplicação}

- Applicable to **Dev, QA, DevOps, AppSec** profiles and to **third parties with access to systems or pipelines**
- Must be **carried out before any significant technical activity**
- May be formalised as:
  - A form in the onboarding system (HR)
  - An issue or task in the technical backlog
  - An automatic record in the LMS or in the permissions system (RBAC)
- A **periodic review of the track per role** is recommended, especially after updates to the SbD-ToE Manual

---

## 🔗 Cross-references {#-referências-cruzadas}

| Document                         | Role                                                   |
|-----------------------------------|-----------------------------------------------------------|
| `trilho-formativo.md`             | Matrix of tracks by profile and risk                      |
| `90-catalogo-formativo.md`        | List of content to teach per chapter and role        |
| `manual-formacao-por-perfil.md`   | Suggested training modules per role                   |
| `02-formacao-onboarding.md`       | Description of the onboarding objectives and flow             |

---

> 🔐 Access to critical systems must be **conditional on the formal verification of this checklist**, ensuring that all members of staff have been adequately trained and prepared.
