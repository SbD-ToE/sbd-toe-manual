---
id: policies-relevantes
title: Policies
sidebar_position: 60
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/policies-relevantes.md
  source_sha256: b46a4c59e1010fd807bf3800ca08ae7543a2aeb051c302e594eb97465c00cd5f
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 0538c61627ba420e4d1a236ceb07482f20a48138d9f3a3c9efab428b9eb631fb
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, risk_level, slug_threat_modeling, threat, traceability, validation_evaluation]
  glossary_sha256: 8e3f26441eb9aa27b7a316969b13da92c28adea94a3116b4ab43dfd5d09f725a
  translated_at: 2026-09-25T20:17:07Z
  stamped_at: 2026-09-26T18:33:29Z
  reviewed_by: null
---

# Organisational Policies - Threat Modelling

The effective adoption of Chapter 03 - Threat Modelling - depends on the existence of **formal organisational policies** that sustain:

- The mandatory nature of threat modelling in medium- or high-risk contexts;
- The integration of the activity into the development lifecycle;
- Traceability between threats, requirements and the controls applied;
- The reuse and validation of models in standardised environments.

---

## 📌 Fundamental note {#-nota-fundamental}

> ✅ Threat modelling must be treated as a **mandatory activity in L2 and L3 applications**, with formal criteria defined by organisational policy.

These policies:

- Make *threat modelling* a **systematic, auditable and traceable** practice;
- Sustain risk-based decision-making, as defined in Chapters 01 and 02;
- Allow technical teams to be aligned with mature secure-engineering practices.

> 🧩 This chapter **implements, in practice, what the organisational policies determine**. The policy legitimises, the chapter operationalises.

---

## 🧾 Recommended policies {#-políticas-recomendadas}

| Policy Name                               | Mandatory | Application                                             | Minimum expected content                                                                 |
|------------------------------------------------|-------------|--------------------------------------------------------|------------------------------------------------------------------------------------------|
| [Threat Modelling Policy](/sbd-toe/assets/policies/policy-threat-modeling)                    | ✅ Yes      | All applications classified as L2 or L3        | Criteria for mandatory application, moments of application in the cycle, roles involved, permitted tools |
| [Threat Model Validation Policy](/sbd-toe/assets/policies/policy-threat-modeling)     | ⚠️ Recommended | Projects with a new architecture or critical changes | Technical review process, cross-validation by security, formal risk acceptance  |
| [Threat Model Reuse Policy](/sbd-toe/assets/policies/policy-threat-modeling)  | ⚠️ Recommended | Organisations with standardised architectures           | Criteria for the safe reuse of earlier models, validation by context     |

---

## 📋 Suggested structure of each policy {#-estrutura-sugerida-de-cada-política}

Each organisational policy must contain, at a minimum:

- **Objective and scope** of the policy;
- **When to apply** (e.g. by risk level, type of change, moment in the cycle);
- **Roles and responsibilities** (architecture, security, development, product);
- **Requirement for traceable outputs** (e.g. STRIDE model, DFD, mitigation plan);
- **Validation and reuse criteria**;
- **Mandatory documentation by project type**;
- **Review periodicity of the policy itself** (e.g. annual);
- **Risk acceptance criteria and justified exceptions**.

---

## ✅ Final recommendations {#-recomendações-finais}

- These policies must be **formal, approved and communicated** to all technical teams;
- They must be **aligned with the Requirements Catalogue of Chapter 2** and with the risk criteria defined in Chapter 1;
- They must provide for **periodic review and controlled reuse** of existing models;
- Their application must be **integrated into the development lifecycle** and validated in every critical release.

> 📌 The absence of these policies compromises the proportional, continuous and effective application of Threat Modelling in an organisational context.

