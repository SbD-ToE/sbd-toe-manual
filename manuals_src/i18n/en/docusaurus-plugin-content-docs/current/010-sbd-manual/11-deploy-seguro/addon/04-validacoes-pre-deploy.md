---
id: validacoes-pre-deploy
title: Technical and Functional Pre-Deployment Validations
description: Mandatory verifications before the promotion of code to production, including security, functionality and readiness.
tags: [tipo:anexo, grupo:execucao, tema:validacao, pre-deploy, segurança]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/addon/04-validacoes-pre-deploy.md
  source_sha256: 904aa9bd9a30705c6459206ee73f93655b944ce3617abf2820c1cce2044dc63f
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 5e3c0e522538b3b2745c5a127b375dc06d3825ea4b78f4343cd4b4859f9ea9df
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 112d795f9bd927f0d4c24114e389470217eb00c1d6b919ae2df2e4f7bdb4878d
  glossary_keys: [practitioner_manual, risk_level, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: 8a38510c8381c5af51546e49c39f51516c0e5c08aa6477f9f64eba32fd9006cf
  translated_at: 2026-09-26T11:00:49Z
  reviewed_by: null
---

# Security Validations before Deployment

This document defines the **technical and security validations that are mandatory before the approval of a deployment**, based on the application's risk, the criticality of the release and the execution context.

It applies to **QA, staging and production** environments, and must be incorporated as a *gate* in the pipeline or validated manually in organisations with less automation.

---

## 📊 Table of validations by type {#-tabela-de-validações-por-tipo}

| Validation type       | Description                                                        | Example / Tool             |
|-------------------------|------------------------------------------------------------------|----------------------------------|
| **Functional tests**   | Validation of the main functionality                           | Regression tests / QA         |
| **Security tests** | Verification of vulnerabilities, credentials, misconfiguration     | SAST, DAST, trivy, Semgrep       |
| **SBOM / dependencies** | Generation and validation of the list of components (SBOM)             | CycloneDX, Syft, OWASP Dependency Check |
| **Findings analysis** | List of open findings, with classification and a justified decision  | Jira, Kiuwan, AppSec backlog     |
| **Control rules**  | Compliance with specific criteria by risk                    | Checklists, conditional gates   |
| **Formal approval**     | Approval by a segregated profile (AppSec, QA, management)             | Azure DevOps, GitHub reviewers   |

---

## 🚫 Examples of recommended blocks (gates) {#-exemplos-de-bloqueios-gates-recomendados}

| Risk level | Blocking gate if...                                       |
|----------------|--------------------------------------------------------------|
| **L1 (low)** | Open critical findings OR tests fail                    |
| **L2 (medium)** | Open findings ≥ high OR no SBOM OR no rollback defined |
| **L3 (high)**| No AppSec review OR no dynamic tests OR no validated rollback plan |

> 🔎 These gates must be parameterised in the pipeline or included in the manual validation checklist.

---

## 🔗 Recommended integration in the CI/CD pipeline {#-integração-recomendada-no-pipeline-cicd}

1. **Build stage**:
   - Generates the SBOM automatically
   - Runs SAST + semantic linting

2. **Validation stage**:
   - Analyses open findings
   - Verifies that a rollback plan is present

3. **Gating / approval stage**:
   - Blocks if the risk level is ≥ L2 and there has been no review
   - Allows manual approval by a security reviewer

---

## 🏢 Integration with organisational control {#-integração-com-controlo-organizacional}

- Releases must be linked to a validation artefact:
  - Findings report by risk
  - Release signature (hash, metadata, date)
  - Approvers and justifications

- There must be a record of:
  - Who approved the deployment
  - Under what conditions (version, environment, scope)
  - Link to tests or requirements traceability

---

## ✅ Examples of approval criteria {#-exemplos-de-critérios-de-aprovação}

- [ ] All automated tests passed
- [ ] Open findings were reviewed and justified
- [ ] A validated, functional rollback exists
- [ ] SBOM generated and stored for audit
- [ ] The release was approved by a qualified reviewer
- [ ] Cards/tasks were created for pending findings (if applicable)

> 👍 These criteria must be **binary, verifiable and traceable**.
