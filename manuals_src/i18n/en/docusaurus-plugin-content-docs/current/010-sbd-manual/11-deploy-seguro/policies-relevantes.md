---
id: policies-relevantes
title: Policies
description: Formal policies required to ensure the security, reversibility and traceability of deployments in production.
tags: [policy, organizacional, deploy, rollback, validação, rastreabilidade]
sidebar_position: 60
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/policies-relevantes.md
  source_sha256: 37f2627f609f511be4700cb91808807880d9cc4e71123e0d203ae6205e238d80
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: b3aa5cf76ead49a69918c526e77b87edc8ecbfcf4df5a46a2204da7f45469a6d
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 112d795f9bd927f0d4c24114e389470217eb00c1d6b919ae2df2e4f7bdb4878d
  glossary_keys: [audit_trail, chapter_role, practitioner_manual, requirement_runtime, traceability, validation_evaluation]
  glossary_sha256: f4a70027520beefec026546c7156565a95521d22161e190dd349a027540a59e9
  translated_at: 2026-09-26T11:00:56Z
  reviewed_by: null
---


# Organisational Policies - Secure Deployment

The consistent and effective application of Chapter 11 - **Secure Deployment** - requires the existence of **formal organisational policies** that regulate the technical and operational conditions for running code in production, with a focus on:

- Pre-deployment validation (readiness);
- Gating and formal approval;
- Logging, traceability and reversibility;
- Requirements for tested and documented rollback.

---

## 📌 Fundamental note {#-nota-fundamental}

> ⚠️ The secure execution of software in production **depends on well-defined and formalised technical and operational criteria**.

These policies must:

- Establish rules for release approval and deployment gates;
- Make the existence of a tested rollback plan mandatory;
- Define roles and responsibilities for the authorisation, validation and execution of the deployment;
- Stipulate how traceability and reversibility are ensured.

> 📑 These policies must be aligned with the processes defined in the chapter and be auditable.

---

## 📓 Recommended policies {#-políticas-recomendadas}

| Policy Name                                  | Mandatory? | Application                                     | Summary of required content                                             |
|---------------------------------------------------|--------------|--------------------------------------------------|-------------------------------------------------------------------------|
| [Release Approval Policy](/sbd-toe/assets/policies/policy-aprovacao-release)              | ✅ Yes      | All releases to production                | Readiness criteria, mandatory checklist, owners and formal approval |
| [Rollback and Reversibility Policy](/sbd-toe/assets/policies/policy-rollback)           | ✅ Yes      | All releases with operational impact        | Requirement for a rollback plan, prior testing, documented execution        |
| [Logging and Traceability Policy](/sbd-toe/assets/policies/policy-deploy-seguro)            | ✅ Yes      | All production and staging environments       | Requirements for logging, versioning, toggles and auditability           |
| [Deployment Gating and Automation Policy](/sbd-toe/assets/policies/policy-deploy-seguro)      | ⚠️ Optional | Pipelines with automated deployment               | Definition of gates, automatic approval, blocking on findings         |
| [Staging Environment Validation Policy](/sbd-toe/assets/policies/policy-deploy-seguro)    | ✅ Yes      | Projects with staging or pre-prod                | Functional validation, metrics and readiness with evidence                   |
| [Deployment Autonomy and Responsibility Policy](/sbd-toe/assets/policies/policy-deploy-seguro) | ⚠️ Optional | Teams with self-service or continuous deployment     | Who may authorise, minimum requirements, record of decisions             |

---

## 📄 Suggested structure of each policy {#-estrutura-sugerida-de-cada-política}

Each organisational policy must contain:

- Objective and scope;
- Mandatory rules and constraints (e.g. no deployment without a tested rollback);
- Roles and responsibilities (Dev, QA, AppSec, Product);
- Traceability, logging and evidence requirements;
- Mode of integration with pipelines (automatic, manual, gated);
- Periodicity of review and audit.

---

## ✅ Final recommendations {#-recomendações-finais}

- These policies must be approved by the **security, QA and product** areas;
- They must be **accessible, versioned and known** to all teams involved in deployment;
- They must be **implemented via CI/CD whenever possible**, with integrated gates, validators and logs;
- Their existence is an essential requirement for secure, auditable and reversible deployment.

> 📁 Policy templates may be included in additional `60-*.md` files in future versions of the manual.
