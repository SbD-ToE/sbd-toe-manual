---
id: checklist-revisao
title: Checklist - Security Testing
description: Instrument for binary and auditable verification of the practical adoption of continuous security validation practices.
tags: [checklist, revisão, testes, segurança, conformidade, rastreabilidade]
sidebar_position: 20
sidebar_label: Review Checklist
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/canon/20-checklist-revisao.md
  source_sha256: d487231e053426cdae1b83c91694351131e57a425e91e3daf484c8d405b6d617
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: aa704493f0873234335abeea3454ecc90b741d2ee872559500efb58de1a95043
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, framework_source_corpus, instrument, lifecycle_phase, maturity, mcp_reading_programa, programme_line, risk_level, sbdtoe_sbd, traceability, transversal, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 56b338e390116ac26ed0cc0e611d63195b613f448ad9d677fbc70522e29b7b03
  translated_at: 2026-09-26T10:31:37Z
  stamped_at: 2026-09-26T18:35:18Z
  reviewed_by: null
---


# Periodic Review Checklist - Security Testing

This checklist applies to all applications that require security validation in their lifecycle, and serves as an instrument of **binary and auditable** verification of the **practical adoption of the prescriptions of Chapter 10 - Security Testing** (`TST-001` to `TST-010`), enabling:

- Control of the proportional application of tests (by level L1–L3);
- Objective verification of the presence, execution and treatment of tests;
- Generation of operational indicators that can be aggregated by project, team or organisation.

> 🗓️ **Its review is recommended at each release, architecture change or relevant regression**, as indicated in `aplicacao-lifecycle`.

---

## 📋 Verification Items {#-itens-de-verificação}

| Item                                                                                                      | Verified? |
|-----------------------------------------------------------------------------------------------------------|-------------|
| Is there a documented and versioned test strategy, proportional to risk (L1–L3), mapped to the requirements of Ch. 02 and reviewed in the last year or after a change in risk/architecture? (`TST-001`) | ☐           |
| Does the pipeline run automatic and traceable SAST, with a versioned rule profile and a false-positive baseline approved by AppSec? (`TST-002`) | ☐           |
| Is DAST run in staging with a defined scope, authentication and findings policy, without real data (where applicable)? (`TST-005`) | ☐           |
| Do L3 applications have IAST instrumented in staging with verified coverage of critical flows? (`TST-010`) | ☐           |
| Has fuzzing been applied to the components that process complex input, with a managed corpus (where applicable)? (`TST-009`) | ☐           |
| Does each fixed vulnerability have a security regression test integrated into the pipeline and linked to the original finding? (`TST-006`) | ☐           |
| Are minimum test coverage thresholds by risk level defined and measured? (`TST-007`)        | ☐           |
| Are the tests integrated into the pipeline with gates that block promotion when the minimum criteria are not met, and does the build block unjustified critical findings? | ☐           |
| Are findings triaged, classified and managed with a lifecycle and a remediation SLA by severity, centralised on a management platform? (`TST-003`) | ☐           |
| Are security exceptions formally approved, with justification, deadline and retest plan, and are expired ones revalidated? | ☐           |
| Is test evidence reproducible and auditable from the same code state, linked to the commit or release? (`TST-004`) | ☐           |
| Does each pass/fail decision and each override have an explicit human owner recorded?                        | ☐           |
| Are the assets of the testing process protected (real data forbidden by default, segregated least-privilege credentials, masking of secrets in logs)? | ☐           |
| Has PenTesting been carried out with a defined scope, documented methodology and rules of engagement, with retesting of fixes and integration of findings (where applicable)? (`TST-008`) | ☐           |
| Is the programme's effectiveness measured with KPIs (coverage, resolution SLA, regression, noise) and are findings automatically communicated to the teams? | ☐           |
| Is the use of AI in testing covered by policy (minimisation, masking, no auto-merge of patches), with versioned eval suites as a gate for AI agents, and TLPT readiness prepared for entities subject to DORA (where applicable)? | ☐           |
| **Boundary item** — has the complementary verification covered in other chapters been confirmed as executed: composition analysis/SCA (Ch. 05), scanning of secrets, IaC and container images (Chs. 06 to 09) and functional validation of security requirements (Ch. 02), without duplicating the respective controls? | ☐           |

---

> 📐 The **boundary item** above is a deliberate and localised exception to the top-down derivation of this checklist: the testing chapter is the natural lens through which the auditor asks *"is everything verified?"*, but real security verification is distributed across several chapters. The item confirms its execution without reopening the controls, which remain within the competence of the respective chapters. The complete map is in the [cross-cutting verification matrix](../addon/matriz-verificacao-transversal).

---

## 🔄 Operational Integration {#-integração-operacional}

- This checklist may be integrated into **pipelines, release reviews, internal audits or production gates**;
- Results may be traced by **commit, release, application or team**;
- Each item must be validated with **objective evidence** (e.g. pipeline logs, test reports, issues, PR comments, PenTesting reports).

> ⚠️ In the event of a negative answer, a formal, approved and documented exception must exist.

---

## ✅ Compliance and KPI {#-conformidade-e-kpi}

- Validation of this checklist makes it possible to declare **compliance with Chapter 10 - Security Testing**;
- The count of affirmative answers may be used to **measure the degree of adoption of the prescribed practices**;
- This result may be aggregated by team or project as an **indicator of operational maturity**.

> 📌 This mechanism is aligned with the model of continuous control, traceability and proportionality defined in the SbD-ToE.
