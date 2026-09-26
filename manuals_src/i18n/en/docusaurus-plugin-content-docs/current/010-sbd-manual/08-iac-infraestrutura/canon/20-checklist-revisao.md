---
id: checklist-revisao
title: Review Checklist - Infrastructure as Code (IaC)
sidebar_position: 20
sidebar_label: Review Checklist
description: Binary and auditable checklist to verify the practical application of the security prescriptions for IaC.
tags: [checklist, validação, revisão, iac, infraestrutura como código, controlo]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/canon/20-checklist-revisao.md
  source_sha256: dcd632fe6158b4301485ce60347ed3a969bdb41f69bd6fec0054c07eece75c6d
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 733d5f242f309f480113facc82728375a8304b16f3f81083359a93a96c77c378
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [audit_trail, chapter_role, instrument, maturity, practitioner_manual, provenance, sbdtoe_sbd, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: 2996cf5377eba22fd1142cc2488a1a478aa9b39e32903a906c7529bdd0ae3967
  translated_at: 2026-09-26T09:25:41Z
  reviewed_by: null
---


# Periodic Review Checklist of IaC Practices

This checklist applies to all **Infrastructure as Code (IaC)** projects developed or maintained internally. It serves as an instrument of binary and auditable verification of the **practical adoption of the prescriptions of Chapter 08**, enabling:

* Objective control of the application of requirements `IAC-001` to `IAC-013`;
* Integration with PR, release, audit and onboarding processes;
* Generation of operational and compliance indicators.

> 🗓️ **Review is recommended at each new release, relevant PR or change to a critical environment.**

---

## 📋 Verification Items {#-itens-de-verificação}

| Item                                                                             | Verified? |
| -------------------------------------------------------------------------------- | ----------- |
| Is the remote backend configured with authentication and locking, with lock logs available? (`IAC-001`) | ☐           |
| Are the dev/staging/prod environments segregated and versioned in distinct directories or workspaces? (`IAC-002`) | ☐           |
| Does the pipeline run blocking validations (lint/syntax, security scanner and policy) whose failure prevents the `apply`? (`IAC-003`) | ☐           |
| Do modules use a fixed version or hash (no `latest`/`main`), from allowlisted sources, with verified provenance/integrity? (`IAC-004`) | ☐           |
| Is there a versioned history with semantic tags and notes per release? (`IAC-005`) | ☐           |
| Are naming/tagging/layout conventions validated automatically, and are resources without mandatory tags rejected? (`IAC-006`) | ☐           |
| Does each `apply` occur only after recorded human approval of the `plan` attached to the PR, with no manual `apply` outside the pipeline? (`IAC-007`) | ☐           |
| Is it possible to trace, for any resource, the originating IaC file, environment and pipeline? (`IAC-008`) | ☐           |
| Is policy-as-code enforcement blocking at pre-merge and pre-apply, with versioned policy and blocking logs? (`IAC-009`) | ☐           |
| Are `plan`/manifest artefacts versioned with a hash, with integrity confirmed before the `apply` and without reuse across environments? (`IAC-010`) | ☐           |
| Is there automated secret scanning and a prohibition of secrets in code, with vault integration (Vault/KMS/OIDC) and short-lived ephemeral credentials? (`IAC-011`) | ☐           |
| Is there automated detection of drift between the IaC and the real state, with alerts, treated as a security failure corrected via PR? (`IAC-012`) | ☐           |
| Is there a formal periodic review of modules/templates with records (date, owner, findings) and removal of obsolete or vulnerable ones? (`IAC-013`) | ☐           |
| Is all proposed IaC treated as untrusted input by origin (human, template, generator or assisted tool)? | ☐           |
| Are exceptions managed in a versioned format with a blocking TTL, and is there a rollback/kill-switch procedure for `destroy` in production? | ☐           |

---

## 🔄 Operational Integration {#-integração-operacional}

* This checklist may be applied manually (e.g. PR review) or integrated into CI/CD as a gate.
* It may be used in formal architecture reviews, releases or the onboarding of new repositories.
* Each item must be validated with **objective evidence**:

  * `backend.tf` files, `tfsec` logs, CI screenshots, hashes in releases, etc.

> ⚠️ Negative answers require a formal, approved and documented exception (see governance model).

---

## 📊 Compliance and KPI {#-conformidade-e-kpi}

* Validation of this checklist makes it possible to declare **compliance with Chapter 08 - Infrastructure as Code**.
* The count of verified items may be used for **operational KPIs of adoption and maturity**.
* It may be included as evidence in audits, exception processes or release gates.

> 📌 This mechanism is aligned with the model of **continuous control and traceability** defined in SbD-ToE.
