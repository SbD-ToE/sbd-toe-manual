---
id: inclusao-terceiros
title: Model for the Inclusion of Third Parties and Suppliers
description: Standardised procedure for the secure onboarding of third parties, with the minimum required training.
tags: [terceiros, onboarding, formacao, rastreabilidade, inclusao]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/addon/20-modelo-inclusao-terceiros.md
  source_sha256: 6325a11b21c221a7b5812aaa85413bba14ca5c57eade055a4d0485a4e9fcdc38
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 8c78a34453c8082a82d6f1d9f9311642a79bb562a45fe3031dc4d372846154b8
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, requirement_runtime, traceability, trilho_formativo, validation_evaluation]
  glossary_sha256: 1ee88263ad58f33a6b38d765ab48828d1d9ba700c49866afb68ea10160a7e48f
  translated_at: 2026-09-26T11:44:25Z
  stamped_at: 2026-09-26T18:36:01Z
  reviewed_by: null
---


# Inclusion of Third Parties in Training Programmes

This document defines a practical and verifiable approach to ensure that **external suppliers, contractors and outsourcing** are properly integrated into the security training programmes before they obtain technical access to projects, systems or sensitive data.

---

## 🎯 Objective {#-objetivo}

- **Standardise the training criteria** for external parties with a technical impact
- Avoid security disparities between internal and external teams
- **Ensure traceability and accountability** in audits and post-incident
- Formalise training as a **precondition for technical access**

---

## ✅ Minimum applicable requirements {#-requisitos-mínimos-aplicáveis}

Every third party (individual or organisation) must fulfil the following points **before obtaining technical permissions**:

| Requirement                                                                                   | Mandatory? |
|---------------------------------------------------------------------------------------------|--------------|
| Signature of a statement of responsibility (may be digital)                                  | ✔️           |
| Formal assignment of a training track according to the technical role                               | ✔️           |
| Completion and validation of the training (e.g. quiz, validated PR)                                   | ✔️           |
| Training record in a validated repository (project, LMS, GitHub, etc.)                   | ✔️           |
| Integration session with an internal member (e.g. AppSec, PO, Champion)                        | ✔️           |

---

## 🧩 Practical arrangements by type of third party {#-modalidades-práticas-por-tipo-de-terceiro}

| Type of third party         | Suggested training arrangement                                      | Expected record                        |
|--------------------------|---------------------------------------------------------------------|------------------------------------------|
| Individual contractor    | Technical track + online quiz + PR validation                     | Checkpoint in onboarding                 |
| Supplier with a team    | Synchronous session + shared content (LMS, internal repository) | Attendance list + evidence per user |
| Continuous outsourcing     | Formal training with a contractual clause + control by SLA         | Contract + LMS logs                     |

---

## 🧭 Good implementation practices {#-boas-práticas-de-implementação}

- Include a reference to **Chapter 13 - Training** in the contracting process
- Formalise the requirements via **Chapter 14 - Governance and Contracting**
- Maintain an **internal repository of evidence of third-party onboarding**
- Ensure that the **Champions** or AppSec are involved in receiving third parties
- Provide for **periodic audits** of training at critical suppliers

---

## 🔗 Links to other documents {#-ligações-a-outros-documentos}

| Document                         | Relevance                                   |
|-----------------------------------|----------------------------------------------|
| `03-checklist-onboarding.md`      | Also applicable to third parties with technical access |
| `trilho-formativo.md`            | Defines the tracks to apply per role        |
| `14-governanca-contratacao.md`   | Formalises the requirements via contractual clauses |

---

> 🔐 Ensuring that third parties are trained **is not a courtesy - it is an organisational security obligation.**
>  
> The application of this model contributes directly to reducing supply chain risks and exposure through poor external practice.
