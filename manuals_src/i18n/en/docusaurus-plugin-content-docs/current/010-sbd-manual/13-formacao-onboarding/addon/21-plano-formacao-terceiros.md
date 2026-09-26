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
  terms_sha256: d743dfcba33f930c34618b93d1eaaa34f697328d45aaf3bb657c33b8b3c59c9a
  glossary_keys: [capacitacao, schema, traceability, validation_evaluation]
  glossary_sha256: 1afc4d6cc0bf48b172d0009029342e291d57711d05c05ef98a938a41afd652c2
  translated_at: 2026-09-26T11:44:25Z
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
