---
id: design-seguro-pipelines
title: Secure Pipeline Design
sidebar_position: 1
description: Rules for the secure construction and review of pipelines as code, with controlled triggers and predictable environments.
tags: [cicd, pipelines, yaml, triggers, revisão, automação]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/addon/01-design-seguro-pipelines.md
  source_sha256: 0765aa5c8fe05fd2b3371b65b7fd5825202906abd9ca3b59d5ad25c4f60c5197
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 584db92257f63e2af2ecf596d9fb36a304964558b0ea6720a8f0845d4939c282
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [framework_source_corpus, risk_level, traceability, validation_evaluation]
  glossary_sha256: 85f7842de51022e7f3ad114754bd482469d7ac6b0a99b7c89a9f2fb0471a0321
  translated_at: 2026-09-26T09:09:12Z
  stamped_at: 2026-09-26T18:34:15Z
  reviewed_by: null
---


# Secure pipeline design

The secure design of CI/CD pipelines is a fundamental control to ensure that only **legitimate, authorised and traceable** changes are processed automatically. The pipeline must be treated as **sensitive infrastructure**, with the same security precautions that apply to source code, infrastructure scripts or privileged configurations.

> The integrity of continuous delivery depends directly on the integrity of the pipelines themselves.

---

## 🎯 Objectives {#-objetivos}

- Ensure that **only authorised changes** trigger executions;
- Ensure that the **execution flow is controlled and predictable**;
- Protect against **malicious manipulation of the pipeline** (e.g. substitution of scripts, bypassing of stages);
- Enable **traceability and independent review** of everything the pipeline does.

---

## 🛠️ Practices {#️-práticas}

1. **Pipelines as code (PaC)**  
   - Pipelines must be defined as versioned files (e.g. YAML, JSON, HCL), in controlled repositories;
   - All changes must be traceable and subject to formal review via pull/merge request.

2. **Controlled and explicit triggers**  
   - Only triggers from authorised sources must be accepted (e.g. merge to the main branch, push to a monitored branch, signed tag);
   - Executions on forks or external branches must be disabled or mediated.

3. **Mandatory review of changes to the pipeline**  
   - Changes to pipeline files (e.g. `.github/workflows/*.yml`) must require technical and/or security review;
   - A "four-eyes" policy must apply (at least two reviewers).

4. **Separation of pipelines by function or criticality**  
   - CI and CD must be distinct pipelines, with differentiated controls and permissions;
   - Applications classified as L3 must have dedicated pipelines, segregated from generic pipelines.

5. **Reusable, centralised templates**  
   - The use of templates enables centralised validation and reduces the risk of error or manipulation;
   - Templates must be versioned, auditable and reviewed periodically.

---

## ⚖️ Proportional application by risk level {#️-aplicação-proporcional-por-nível-de-risco}

| Level | Mandatory requirements                         | Enhanced requirements                                 |
|-------|--------------------------------------------------|--------------------------------------------------------|
| **L1** | Versioned pipelines; controlled triggers      | -                                                      |
| **L2** | Mandatory review; separate CI/CD             | Reusable templates; automated validation          |
| **L3** | Security review; isolated pipelines        | Formal approval of changes to the pipeline             |

---

## 📌 Practical examples {#-exemplos-práticos}

- **GitHub Actions**  
  - `required reviewers` for `.github/workflows`;
  - Disable automatic executions on forks (`pull_request_target`).

- **GitLab CI**  
  - Use of `rules:` and `only:` to control triggers;
  - Mandatory approval rules for `.gitlab-ci.yml`.

- **Azure DevOps**  
  - Branch protection policy and PR gates for `azure-pipelines.yml`;
  - YAML templates in a separate repository with controlled access.

- **Jenkins**  
  - Declarative pipelines versioned in Git;
  - Protection of scripts with the *Script Approval Plugin*.

---

## 📉 Mitigated risks {#-riscos-mitigados}

- Unauthorised executions (OSC&R: CI0001, CI0004);
- Malicious substitution of scripts (OSC&R: CI0011);
- Manipulation of the build flow (OSC&R: CI0002);
- Abuse of automatic triggers (OSC&R: CI0006, CI0015).

---
