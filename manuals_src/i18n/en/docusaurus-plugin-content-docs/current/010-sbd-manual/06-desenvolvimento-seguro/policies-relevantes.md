---
id: policies-relevantes
title: Policies
description: Policies needed to frame and reinforce the secure development practices defined in this chapter
tags: [políticas, desenvolvimento, validação, codificação segura, GenAI, exceções]
sidebar_position: 60
translation:
  source_locale: pt
  source_path: 010-sbd-manual/06-desenvolvimento-seguro/policies-relevantes.md
  source_sha256: 2c511561a975b933b96c40ad5f39af023d103bc71c67371bc4baad1dc149fe5e
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: eec08c15de5ed80c98a5a377634913cfbbb92fd2fe1c0d1bbd3943c747a8f113
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, cycle_iteration, lifecycle_phase, maturity, practitioner_manual, role_tech_lead, traceability, validation_evaluation]
  glossary_sha256: 18e6658b7d6ef6bf3a3b9838bb590a179dcf86cb6784d79da4b1bd484c1b07db
  translated_at: 2026-09-26T08:57:18Z
  stamped_at: 2026-09-26T18:34:11Z
  reviewed_by: null
---


# Organisational Policies - Secure Development

The effective application of Chapter 06 - Secure Development - requires the existence of **formal organisational policies** that frame, reinforce and legitimise the practices of secure coding, code review and validation.

These policies ensure that:

- Security is treated as an essential quality criterion;
- Security requirements have concrete expression in the development lifecycle;
- There are clear, auditable rules that can be applied across engineering teams.

---

## 📄 Relevant Organisational Policies {#-políticas-organizacionais-relevantes}

| Policy Name                                  | Mandatory? | Application                            | Summary of the required content |
|---------------------------------------------------|--------------|---------------------------------------|-------------------------------|
| [Secure Coding Standards Policy](/sbd-toe/assets/policies/policy-guidelines-desenvolvimento)         | ✅ Yes       | All development teams  | Formal guide with good practices, prohibited patterns and mandatory rules per stack or language. |
| [Code Validation and Review Policy](/sbd-toe/assets/policies/policy-revisao-codigo)         | ✅ Yes       | All repositories and pipelines     | Requirements for peer review, use of linters, `@sec:` tags, traceability and blocking. |
| [Code Dependency Approval Policy](/sbd-toe/assets/policies/policy-dependencias)   | ✅ Yes       | Introduction of libraries and packages    | Formal process to approve and track reused external or internal dependencies. |
| [Technical Exception Justification Policy](/sbd-toe/assets/policies/policy-gestao-excecoes)     | ⚠️ Optional | Security team, tech leads        | Acceptable exception cases, documentation requirements, deadline and formal approval. |
| [Policy on the Controlled Use of GenAI in Development](/sbd-toe/assets/policies/policy-uso-ferramentas-apoio) | ⚠️ Optional | Teams with access to GenAI tools | Criteria for the use of automatic suggestions (e.g. Copilot); validation, origin annotation, mandatory review. |

---

## 📃 Minimum structure of each policy {#-estrutura-mínima-de-cada-política}

Each organisational policy must contain, at a minimum:

- **Objective and scope** of the policy;
- **Mandatory criteria** per application type, language, stack or team;
- **Roles and responsibilities** (devs, reviewers, tech leads, security);
- **Mandatory integration points** in the SDLC or pipeline;
- **Requirement for traceable evidence** (tags, logs, reports);
- **Review frequency** and validation of the policy itself.

---

## ✅ Final recommendations {#-recomendações-finais}

- The policies must be **officially approved and published** by security and engineering management;
- They must be accessible, communicated effectively and integrated into onboarding and technical review processes;
- There must be **mechanisms for validating and auditing the application of the policies**;
- Their existence and application are **formal criteria of maturity in secure development**;
- It is recommended that the policies be accompanied by practical examples, checklists and reusable templates.

> 📁 Policy templates may be included as complementary `60-*.md` files in future versions of the manual.
