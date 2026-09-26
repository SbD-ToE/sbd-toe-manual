---
id: policies-relevantes
title: Policies
sidebar_position: 60
description: Formal policies that sustain the governance, exception and supplier management practices described in this chapter
tags: [policy, organizacional, governance, excecoes, fornecedores, contratacao]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/policies-relevantes.md
  source_sha256: d5aa2276274a5a2a4746abdb84a6a48b2ffeb20dccf824b28f0eeb5195ae9cfb
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 96f4c5b7e02737a349bd868cf7b01b53e40c124e1cf665b7354c6b20efddc8cf
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, cycle_iteration, layer, lifecycle_phase, mcp_reading_programa, papel_suporte, programme_line, requirement_runtime, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: 1b8016914a449e110869812ad2b5b64e95d4c15c3d48180cea8549e5c37798d4
  translated_at: 2026-09-26T12:00:28Z
  stamped_at: 2026-09-26T18:36:30Z
  reviewed_by: null
---


# Organisational Policies - Governance and Contracting

The effective adoption of Chapter 14 - Governance and Contracting - requires the existence of **formal organisational policies** that **legitimise risk decisions, exceptions, third-party onboarding and contractual security requirements**.

---

## 📌 Fundamental note {#-nota-fundamental}

> ✅ Governance is not an administrative layer: it is a **structuring control** that ensures the application of all the others.

These policies:

* Establish **clear responsibilities** for the approval of exceptions and validations;
* Ensure that **risk decisions are traceable and justified**;
* Impose contractual criteria on third parties, aligned with the SbD model;
* Enable **formal integration with training, risk, lifecycle and audit flows**.

> ⚡️ Without these policies, it is not possible to ensure or audit the consistent application of SbD practices.

---

## 📎 Recommended policies {#-políticas-recomendadas}

| Policy Name                                     | Mandatory? | Application                                           | Summary of required content                                                                    |
| ---------------------------------------------------- | ------------ | --------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| [Exception Approval and Justification Policy](/sbd-toe/assets/policies/policy-gestao-excecoes)     | ✅ Yes        | Projects with security requirements                | Criteria for the submission, approval, validity and reassessment of exceptions.                         |
| [Risk Decision Responsibilities Policy](/sbd-toe/assets/policies/policy-rastreabilidade-organizacional)    | ✅ Yes        | All applications classified by risk         | Definition of owners per domain, authority, recording and traceability.                          |
| [Third-Party Integration and Validation Policy](/sbd-toe/assets/policies/policy-contratacao-segura)      | ✅ Yes        | Suppliers, outsourcing, contractors              | Onboarding process, training validation, mandatory contractual requirements.              |
| [Contractual Security Requirements Policy](/sbd-toe/assets/policies/policy-contratacao-segura)      | ✅ Yes        | Contracting of software, services, critical operations | Minimum requirements per risk type, templates and mandatory legal review.                     |
| [Approver and Decision-Maker Training Policy](/sbd-toe/assets/policies/policy-formacao-seguranca)      | ⚠️ Optional  | Owners of exceptions, risk, compliance             | Requirement for up-to-date training on SbD before authorising decisions with a security impact. |
| [Exception and Contract Review Cycle Policy](/sbd-toe/assets/policies/policy-gestao-excecoes) | ⚠️ Optional  | Exceptions, contracts, critical systems              | Mandatory revalidation at each release or significant change in risk.                      |

---

## 📄 Suggested structure of each policy {#-estrutura-sugerida-de-cada-política}

Each organisational policy must contain:

* A clear **objective and scope** (to whom it applies, when and in what context);
* **Mandatory criteria and rules**, based on risk and on the decision-maker's role;
* **Approval and recording flow** for decisions (who approves, where it is recorded);
* **Integration with training and competence validation**;
* **Periodicity of the formal review of the policy**;
* **Operational traceability mechanisms** (e.g. exception → owner → deadline → affected release);

> ✅ The application of these policies is essential for SbD-ToE practices to be effective, auditable and sustainable.

---

## ✅ Final recommendations {#-recomendações-finais}

* Policies must be **formulated jointly by the security, development and legal teams**;
* They must be **communicated, versioned and accessible** to all parties involved;
* Their application must be integrated into **validation, approval and audit tools**;
* The existence of these policies is a **prior requirement for any security programme that aims to be effective and accountable**.

> 📁 Templates for these policies may be included in future as complementary annexes (`60-*.md`).
