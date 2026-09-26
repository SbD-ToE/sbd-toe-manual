---
id: plano-formacao-terceiros
title: Training Plan for Third Parties
description: Technical plan of the minimum mandatory upskilling for suppliers, contractors and partners with technical access.
tags: [formacao, terceiros, fornecedores, plano, acesso seguro]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/addon/21-plano-formacao-terceiros.md
  source_sha256: 670a81202914f6fe0f1ab355f3761b58acfde1dcb50d6cff288e1b2ff63def42
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 95e37012beaa4c95fd1e6c127063f2c842f746eb28c27085a5aaedbcd51e4cd8
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [capacitacao, esquema_regime, schema, traceability, validation_evaluation]
  glossary_sha256: e41eed8e6ee05202a8fd6eb413154d69d57f6cb48d4da3c854767a615f2d448e
  translated_at: 2026-09-26T11:44:25Z
  stamped_at: 2026-09-26T18:36:02Z
  reviewed_by: null
---


# Minimum Training for Third Parties and Suppliers

This document defines the **minimum mandatory content** of security upskilling for all external staff with relevant technical access - including suppliers, contractors and external teams - ensuring traceability and formal validation before permissions are assigned.

---

## 🎯 Objective {#-objetivo}

- Ensure that **third parties meet the same minimum security criteria** as internal staff
- **Ensure formal validation of the applied knowledge**
- **Reduce the risk** of error, exposure or improper access through lack of knowledge
- **Standardise the training requirement** in contractual and operational processes

---

## 🧭 Scope of application {#-âmbito-de-aplicação}

This model applies to:

- Service providers with access to code, infrastructure or sensitive data
- Consultants, freelancers or contractors who are technically integrated
- Suppliers with continuous access (e.g. via VPN, GitHub, ADO, bastion)
- External teams integrated into internal squads, SCRUMs or DevOps

---

## 📋 Minimum mandatory content {#-conteúdos-mínimos-obrigatórios}

| Topic                           | Description                                                         | Suggested format     |
|--------------------------------|---------------------------------------------------------------------|-----------------------|
| Internal security policy  | Rules, expected behaviours, formal channels                  | Institutional PDF or short video |
| Secure PR                      | Minimum submission standards, positive and negative examples       | Guide + practical quiz   |
| Secrets management             | What must not be submitted (e.g. `.env`, hardcoded tokens)        | Guided demonstration   |
| Permissions flow            | Schema: permissions only after complete validation                     | Project checklist  |
| Support contact              | SPOC or channel for technical and security support                  | Email, Teams, Slack   |

---

## ✅ Mandatory validation {#-validação-obrigatória}

All third parties with technical access must:

- ✅ Confirm that they have read and understood the materials
- ✅ Take a **knowledge validation quiz** with a result of ≥ 80%
- ✅ Have a **formal record** of technical onboarding archived
- ✅ Receive technical permissions **only after formal validation**

**Mandatory record:**

| Field                 | Required? |
|----------------------|----------|
| Full name         | ✔️        |
| Company / supplier  | ✔️        |
| Contact email     | ✔️        |
| Completion date     | ✔️        |
| Quiz result     | ✔️        |
| Internal validator     | ✔️        |

---

## 🔗 Integration with internal processes {#-integração-com-processos-internos}

| Process                         | Application of the model                                           |
|----------------------------------|---------------------------------------------------------------|
| Onboarding checklists         | Validation of third parties against the same criteria as Ch. 13    |
| Contracts and clauses            | Include a reference to training as a condition of access         |
| Access management                | Block access until the process has been formally fulfilled           |
| Audits and compliance          | Use the records as objective evidence of an applied control |

---

## 🧩 Links to other documents {#-ligações-a-outros-documentos}

| Document                         | Practical relevance                             |
|-----------------------------------|------------------------------------------------|
| `04-modelo-inclusao-terceiros.md` | Overall strategy for third-party onboarding   |
| `03-checklist-onboarding.md`      | Traceable checklist applicable to all profiles |
| `trilho-formativo.md`            | Cross-reference by role and risk          |
| `14-governanca-contratacao.md`   | Contractual clauses and formal responsibilities |

---

> 📌 The inclusion of third parties requires the same rigour applied to the internal team:  
> **training, validation, traceability, accountability.**
>
> This model reduces supply chain risks and strengthens the organisation's governance capacity.
