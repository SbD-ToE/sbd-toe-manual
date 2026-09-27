---
id: modelo-governancao
title: Governance Model for Application Security
sidebar_position: 1
description: Definition of formal roles, responsibilities and the application security decision flow
tags: [governanca, ownership, excecoes, validacao]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/addon/01-modelo-governancao.md
  source_sha256: cbd5a8290cce46f3fb0991843c90868504f20d19a55621de767872774095bdbb
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: f04e4c8c263ccf11b9926d25ac216306d737825005cd1eb69744d3f9e3940bf9
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [alcada, chapter_role, cycle_iteration, papel_suporte, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: 0c60bf4526c120743fad5713b008ac512edadd4289e3346a86e6a32e2acbab6e
  translated_at: 2026-09-26T12:00:12Z
  stamped_at: 2026-09-26T18:36:11Z
  reviewed_by: null
---



# Governance Model for Security by Design

## 🌟 Objective {#-objetivo}

To establish a **formal structure of decision, validation and accountability** that makes it possible to apply, coherently and sustainably, the practices defined in the SbD-ToE model across the whole organisation.

This model ensures that:

- Risk classification guides formal decisions;
- The application of requirements is demanded, not optional;
- Risk acceptance, exceptions and compensations are traceable;
- There is a clear chain of **technical, functional and executive accountability**.

This model assumes that the authority to decide, approve exceptions or accept risk always resides in explicitly defined organisational roles.

The technical execution of those decisions may be supported by automated processes or mechanisms, but the responsibility for and legitimacy of the decision remain human, explicit and traceable.

---

## 👥 Roles and responsibilities {#-papéis-e-responsabilidades}

The practical application of the SbD-ToE depends on well-defined roles, formally assigned and kept up to date.

| Role / Function         | Main responsibilities                                                                 |
|------------------------|-----------------------------------------------------------------------------------------------|
| **AppSec / Security** | Define minimum criteria, approve applied controls, validate exceptions, consolidate evidence |
| **Architecture**        | Ensure that risk decisions translate into coherent technical options                   |
| **Product Manager**  | Prioritise security requirements, propose compensations or accept impact                     |
| **DevOps Team**   | Apply controls in the pipeline, monitor technical compliance                               |
| **GRC / CISO**         | Oversee risk decisions, maintain policies and adoption indicators                     |
| **Procurement / Legal**    | Incorporate security requirements and clauses into contracts with suppliers                 |

> ✅ These roles must be described in formal policies and internal governance models.

---

## 🛠️ How to apply {#️-como-aplicar}

### 📌 Typical decisions with formal governance {#-decisões-típicas-com-governação-formal}

- Risk acceptance when minimum controls are not applied;
- Approval of exceptions to practices of the technical chapters;
- Validation of compensations (e.g. alternative or temporary mitigation);
- Approval of suppliers with security deviations or gaps;
- Escalation of deviations detected in release or production.

### 🗂️ Evidence and traceability {#️-evidência-e-rastreabilidade}

Each decision must include:

- Identification of the application, risk and controls;
- Technical and organisational justification;
- Person responsible for the decision (name and function);
- Validity (temporary or permanent);
- Reference to the evidence (scanner, review, exception form).
- Identification of the processes or technical mechanisms involved in executing the decision, where applicable.

> A formal system (Jira, versioned wiki, SharePoint, etc.) may be used for structured recording.

---

## 🔁 Typical governance cycle {#-ciclo-típico-de-governação}

1. Risk classification assigned (Ch. 1);
2. Selection of the applicable minimum requirements (Ch. 2);
3. Validation of the effective application of controls;
4. Recording of exceptions or compensations;
5. Formal approval (according to criticality);
6. Periodic review or planned audit.

> This cycle repeats per release, project, contract or change of risk.

---

## 📄 Recommended documentation {#-documentação-recomendada}

- **Security by Design Policy** (roles, principles and obligations);
- **Risk Decision Model** (risk levels and approval authority);
- **Exceptions template** (mandatory fields and evidence);
- **Register of owners per application/project**.

---

## ✅ Good practices {#-boas-práticas}

- Formalise the model in writing and with executive validation;
- Require the justification and formal approval of exceptions;
- Clearly assign the security owner per project;
- Consolidate decisions in a traceable repository;
- Periodically review active decisions and exceptions.

---

## 🔗 Cross-references {#-referências-cruzadas}

| Document / Chapter         | Relationship with this model                             |
|------------------------------|-----------------------------------------------------|
| Chapter 01 - Risk Management | Starting point: risk classification           |
| Chapter 02 - Requirements     | Defines the applicable requirements per level           |
| Chapter 06 - Secure Development | Implies formal validations                     |
| addon/06-validacao-continuada.md | Applies the logic of reassessment and exceptions        |
| addon/12-processo-excecoes.md | Canonical exception process and chain of authority |

---
