---
id: checklist-revisao
title: Checklist - Secure CI/CD
sidebar_label: Review Checklist
description: Objective verification checklist of the adoption of security practices in CI/CD pipelines
tags: [checklist, auditoria, cicd, devsecops, pipelines]
sidebar_position: 20
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/canon/20-checklist-revisao.md
  source_sha256: acb8e6b96ee3da656d82317f1717ded44b2e98310c7313fb7628edf8159fb583
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: bb05f8ae3db9417e124a95a06c794be1ac0bae201ca5f4c6b6098406102b8e6c
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [audit_trail, chapter_role, instrument, maturity, provenance, risk_level, sbdtoe_sbd, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: befbf92743e13bab6a6453913382a166f2f3f68cc68eb29d1897a3701d6c57dc
  translated_at: 2026-09-26T09:09:20Z
  reviewed_by: null
---

# Periodic Review Checklist - Secure CI/CD

This checklist applies to all applications with continuous integration and delivery pipelines, assessed according to the criteria of **Chapter 07 - Secure CI/CD** (`CIC-001` to `CIC-010`).
It serves as an instrument of verification and audit of **compliance with the minimum controls prescribed for the security of pipelines, artefacts, secrets and execution environments**.

This file works as:

- An instrument of **binary control** (yes / no) per project
- A technical and organisational **audit mechanism**
- An **operational KPI** of DevSecOps maturity
- An objective criterion for the **promotion of applications** to production

> 🗓️ **Review is recommended at least every 6 months**, or whenever there are relevant changes to the pipeline, runners, secrets, policies, external integrations or promotion model.

---

## 📋 Verification Items {#-itens-de-verificação}

| Item                                                                                                               | Verified? |
|--------------------------------------------------------------------------------------------------------------------|-------------|
| Is the pipeline defined as code and versioned, with changes subject to PR and protected main branches (no direct push or force push)? (`CIC-001`) | ☐           |
| Is write access granular per branch/project with enterprise identity (SSO/RBAC), and do L3 applications require signing of commits or tags? | ☐           |
| Are triggers restricted to authorised sources, with executions originating from external forks disabled or mediated by approval? (`CIC-002`) | ☐           |
| Are CI and CD separated by function, with versioned reusable templates, and is the effective execution configuration recorded for audit? | ☐           |
| Are secrets injected via a vault or protected variables, outside YAML/logs/artefacts, masked in logs and deleted after use? (`CIC-003`) | ☐           |
| Do secrets have minimum scope, segregated by environment and application, with periodic rotation and immediate revocation of compromised ones? (`CIC-009`) | ☐           |
| Does the pipeline use OIDC or short-lived tokens instead of long-lived static secrets, with no credentials shared between distinct applications? (`CIC-009`) | ☐           |
| Does the pipeline run the applicable security validations (SAST, secrets scanning, IaC scanning, container scanning, SBOM/SCA and DAST in staging for L2/L3)? (`CIC-004`) | ☐           |
| Do scanner results correspond to observable execution (logs, run id, exit code), and does the build fail automatically on unjustified critical findings? | ☐           |
| Is the risk level (L1–L3) declared and does it condition the pipeline, with policies applied as versioned policy-as-code? | ☐           |
| Are security gates explicit, binary and blocking before irreversible actions, with named human approval and separation between automatic signal and decision? (`CIC-004`/`CIC-011`) | ☐           |
| Is each promotion between environments attributable to an identified person — whoever decided it or, when the promotion is automatic, whoever approved the criteria — with a record of the person (not only a role or service account), of the criterion applied and of the evidence assessed, the criteria for automatic promotion being deterministic, versioned and pre-approved, with the level of autonomy declared when the promotion is executed by an agent, and with no promotion decided by the output of a probabilistic model? (`CIC-011`) | ☐           |
| Are runners ephemeral and segregated by project/risk, with hardening and verified integrity of base images, without privileged execution or access to the Docker socket or to production? (`CIC-006`/`CIC-010`) | ☐           |
| Are the build, test and deploy phases separated, without cross permissions and with credential scope per stage? (`CIC-008`) | ☐           |
| Are artefacts signed with automatic provenance (SLSA model), verified before promotion, with secure storage/transport and tamper detection? (`CIC-007`) | ☐           |
| Is there end-to-end traceability (commit → pipeline → artefact → release → deploy) with a unique ID per execution and retention of logs/evidence in accordance with policy? (`CIC-005`) | ☐           |
| Are exceptions to CI/CD controls recorded, approved, temporary and flagged in the pipeline, and do the AI agents that operate it receive ephemeral OIDC credentials with audit per tool invocation and a kill-switch? | ☐           |

---

## 🔄 Final notes {#-notas-finais}

- This checklist must be applied **per pipeline and per application**, not only in a generic way.
- The result can be used directly as:
  - a technical task (`[SEC] Revisão CI/CD Seguro`);
  - audit evidence;
  - input for maturity dashboards;
  - an objective criterion for *release* approval.
- An item marked as **non-compliant** implies:
  - technical correction,
  - a formal exception record,
  - or blocking of promotion, according to the application's risk level.

Complete validation of this checklist makes it possible to assert **practical and auditable compliance** with Chapter 07 of SbD-ToE.
