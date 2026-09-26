---
id: gestao-codigo-fonte
title: Secure Source Code Management
sidebar_position: 0
description: Practices to protect branches, control changes and ensure traceable versioning of the code used in pipelines.
tags: [cicd, código-fonte, scm, revisão, branches, pipelines]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/addon/00-gestao-segura-codigo-fonte.md
  source_sha256: 336629349f66b32436eafffa3beb9c1f79016229980f00cb6bc40e3ce612d64f
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: c3a9528269f16bbacf516c2ff3ef05f41568c3df765c088c21c2eaed7f1ef39e
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [audit_trail, cycle_iteration, framework_source_corpus, lifecycle_phase, risk_level, traceability, validation_evaluation]
  glossary_sha256: 8e99f0f36c353a2fd2025d1cbb975ecd71c3ecc5b7c64c3a7509e6f0b10bbe09
  translated_at: 2026-09-26T09:09:11Z
  reviewed_by: null
---


# Secure source code management

Pipeline security begins **before automated execution** - it begins in the repository. Secure source code management is the **first link in the CI/CD chain**, and ensures that only legitimate, reviewed and traceable code reaches the build.

> A well-protected pipeline is of no use if the repository can be manipulated directly, silently or without validation.

---

## 🎯 Objectives {#-objetivos}

- Ensure that **all code included in the pipeline is legitimate and authorised**;
- Prevent malicious or accidental changes to production branches;
- Ensure traceability, review and integrity of the history of commits and tags.

---

## 🛠️ Practices {#️-práticas}

1. **Protection of main branches (`main`, `release`, `prod`)**  
   - Prevent direct `push`: only allow changes via pull/merge request;
   - Require reviewers (e.g. two-eyes for L1, four-eyes for L3).

2. **Mandatory review with an auditable history**  
   - All changes must go through technical review;
   - Review must be traceable, with logs preserved.

3. **Signing of commits or tags in critical applications**  
   - For L3, digital signing of commits, or at least of release tags, is mandatory;
   - E.g. GPG, Sigstore, SSH verified.

4. **Prohibition of history rewriting (`force push`, retroactive `rebase`)**  
   - Repositories must block `push --force` on protected branches;
   - The change policy must be clearly documented.

5. **Granular, role-based permission management**  
   - Write access restricted by branch or project;
   - Integration with enterprise identity mechanisms (SSO, RBAC, etc.).

6. **Controlled branch lifecycle**  
   - Branches must be kept clean, with standardised naming and a known lifetime;
   - Short-lived branches (feature/bugfix) must not have access to secrets.

---

## ⚖️ Proportional application by risk level {#️-aplicação-proporcional-por-nível-de-risco}

| Level | Mandatory requirements                     | Enhanced requirements                             |
|-------|----------------------------------------------|---------------------------------------------------|
| **L1** | Branch protection; minimum review         | Standard naming; no `force push`                   |
| **L2** | Mandatory review; history locking   | Standardised merge and naming policy            |
| **L3** | Digital signatures; segregated access       | Formal audit of changes and protected tags  |

---

## 📌 Practical examples {#-exemplos-práticos}

- **GitHub**  
  - Branch protection rules: prevent `force push`, require a PR with approval;
  - `verified` commits with GPG or Sigstore (OIDC).

- **GitLab**  
  - Protected branches: write control per member;
  - Merge request rules with code owner approval.

- **Azure Repos**  
  - Branch policies: mandatory reviewers, build validation;
  - Prohibition of squash or rebase on critical branches.

- **Bitbucket**  
  - Merge checks, branch restrictions, commit signature enforcement.

---

## 📉 Mitigated risks {#-riscos-mitigados}

- Introduction of malicious code directly into the repository (OSC&R: SC0001);
- Silent substitution of code (OSC&R: CI0004);
- Unauthorised releases by tag or branch outside the process;
- Manipulation of history to conceal malicious activity.

---
