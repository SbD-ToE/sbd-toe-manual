---
id: checklist-revisao
title: Checklist - Secure Deployment
sidebar_label: Review Checklist
description: Objective and binary verification of the application of secure deployment practices in a specific project.
tags: [checklist, controlo, deploy, rollback, validação]
sidebar_position: 20
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/canon/20-checklist-revisao.md
  source_sha256: f1bd2ca2a40aacbfd57058595c7fb93dfa4da7053108607da9287db43f5a2af0
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 60bff5d3ed63a3f1619f8f956a9f5670108be96ba5b8923119f26f706f4e223b
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 112d795f9bd927f0d4c24114e389470217eb00c1d6b919ae2df2e4f7bdb4878d
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, instrument, lifecycle_phase, maturity, provenance, sbdtoe_sbd, validation_evaluation, verification_taxonomy]
  glossary_sha256: 49c8a63b7c1f4846074d2584ccdce62ae49deaf41cf9caef783013e2d58a0969
  translated_at: 2026-09-26T11:00:54Z
  reviewed_by: null
---

# Periodic Review Checklist - Secure Deployment

This checklist applies to all applications about to be placed in production, especially those classified as L2 or L3.
It serves as an instrument of binary and auditable verification of the **practical adoption of the prescriptions of Chapter 11** (`DPL-001` to `DPL-009`), enabling:

- Formal control of secure execution
- Verification of the existence of a tested rollback
- Confirmation of operational validation before deployment

> 🗓️ **Its review is recommended before any release, rollback or relevant configuration change**, as indicated in `aplicacao-lifecycle`.

---

## 📋 Verification Items {#-itens-de-verificação}

| Item                                                                                              | Verified? |
|---------------------------------------------------------------------------------------------------|-------------|
| Is there a formal human approval of the deployment recorded with a timestamp and the approver's identity? (`DPL-001`) | ☐           |
| Do the promoted artefacts have a signature/hash and provenance (commit SHA, run id) verified at deployment, with automatic rejection of those that lack them? (`DPL-002`) | ☐           |
| Do the automatic security gates (critical CVEs, tests, secret scanning) block the deployment in the event of failure, with evidence of execution? (`DPL-003`) | ☐           |
| Are the validations integrated into conditional gates parameterised by criticality (L1–L3)?     | ☐           |
| Is there an up-to-date SBOM linked to the artefact, and are all findings resolved or covered by a formally approved exception (approver and validity)? | ☐           |
| Does each deployment have a unique ID and a record that associates who approved it, the artefact, commit SHA, time, environment and gates, making it possible to trace from incident to commit? (`DPL-004`) | ☐           |
| Is there a documented rollback procedure, tested in the last release cycle or year, with the date and maximum time verified? (`DPL-005`) | ☐           |
| Are there mechanisms for immediate reversibility (blue/green, toggles), with previous releases documented and reversible? (`DPL-009`) | ☐           |
| Do the deployment credentials have minimum scope and a short life (OIDC/workload identity), not shared between applications, with usage logs? (`DPL-006`) | ☐           |
| Was validation in a representative staging environment (same versions/configuration, non-real data) carried out before promotion (L2/L3)? (`DPL-007`) | ☐           |
| Is the production pipeline segregated, with secrets in separate vaults and access via MFA and RBAC? | ☐           |
| Is there monitoring during the deployment window and a post-deployment observation period by level, with thresholds for automatic rollback and a response playbook per incident? (`DPL-008`) | ☐           |
| For critical components, is the deployment progressive (canary, blue-green or feature flags), with thresholds and rollback criteria per stage (L3)? (`DPL-009`) | ☐           |
| Do the feature flags have mandatory metadata (owner, scope, activation, expiry), are they versioned as code, auditable, evaluated in the backend and reviewed periodically? | ☐           |
| Does the release follow semantic versioning with a technical and security changelog (fixed CVEs, breaking changes)? | ☐           |
| Do exceptions to gates follow a versioned template (approver by severity, maximum validity 6 months), and do irreversible actions and go/no-go decisions require a human record (who, when, why, evidence)? | ☐           |
| In systems with a *load-bearing* AI agent or model, does the *eval suite* run as a mandatory gate whenever the model/*skill files*/*system prompts* change, is the *rollback* of the model and of the *prompt/skill* independent of the application rollback, and do the *release notes* record the model/skill/eval version + `mandate_ref` (`DPL-010`)? | ☐           |
| In L3 agentic systems, is a major model version change promoted via *canary* with objective criteria, and is there an automatic gate that lowers the `autonomy_level` when the *eval suite* does not confirm the level (`DPL-011`)? | ☐           |

---

## 🔄 Operational Integration {#-integração-operacional}

- This checklist may be integrated into **pipelines, release approval flows, production gates or technical audits**.
- Each item must be validated with **objective evidence** (e.g. approval logs, SBOM files, rollback reports, pipeline screenshots).
- The results may be linked to the lifecycle of the artefact, the application or the service.

> ⚠️ In the event of a negative answer, a formal, approved and documented exception must exist, in line with the chapter's model.

---

## ✅ Compliance and KPI {#-conformidade-e-kpi}

- Validation of this checklist makes it possible to declare **compliance with Chapter 11 - Secure Deployment**.
- The count of affirmative answers may be used to **measure the degree of adoption of the prescribed practices**.
- This result may be aggregated by team, domain or organisation as an **indicator of operational maturity**.

> 📌 This control mechanism is aligned with the model of traceable and reversible trust advocated by the SbD-ToE.
