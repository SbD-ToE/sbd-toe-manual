---
id: checklist-revisao
title: Review Checklist - Secure Architecture
description: Binary, auditable checklist for controlling the application of the secure architecture requirements
tags: [checklist, arquitetura, validação, requisitos]
sidebar_position: 20
sidebar_label: Review Checklist
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/canon/20-checklist-revisao.md
  source_sha256: b9cb3f76e79e0c4b45f9bf531351d7cd9c2209fac60139c32e735d56f5261ef0
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 8c1e3e9fd13385ea6a00cab5473a64e494f65047a4a4f7d912438e6a25b277c6
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, instrument, lifecycle_phase, maturity, provenance, requirement_runtime, sbdtoe_sbd, threat, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 6161bd4c7772c32efc82252c5c742b4bbf0effea5bb6179baee6bf15164687d4
  translated_at: 2026-09-26T08:32:09Z
  stamped_at: 2026-09-26T18:33:39Z
  reviewed_by: null
---

# Review Checklist - Secure Architecture

This checklist applies to all applications assessed according to the criteria defined in this chapter.
It serves as a binary, auditable verification instrument of the **practical adoption of the secure architecture prescriptions**, enabling:

- Continuous control of the application of requirements `ARC-001` to `ARC-015`
- Verification per project at key moments of the lifecycle
- Generation of operational indicators that can be aggregated by team or organisation

> 🗓️ **It must be reviewed at every release or significant architectural change**, as indicated in `aplicacao-lifecycle`.

---

## 📋 Verification Items {#-itens-de-verificação}

| Item                                                                                                                        | Verified? |
|-----------------------------------------------------------------------------------------------------------------------------|-------------|
| Are the trust zones delimited, justified and documented in a versioned diagram? (`ARC-001`)                   | ☐           |
| Are the externally exposed components inventoried, each with a technical justification and a boundary control (gateway, WAF, ACL)? (`ARC-002`) | ☐           |
| Is there a formal record of the security-focused architecture review (date, participants, decisions)? (`ARC-003`)         | ☐           |
| Are the significant structural decisions documented in an ADR (context, alternatives, trade-offs, owner)? (`ARC-004`) | ☐           |
| Was threat modelling of the critical flows carried out, archived and linked to the diagram? (`ARC-005`)                            | ☐           |
| Are there technical isolation controls between sensitive domains, testable and auditable? (`ARC-006`)                     | ☐           |
| Were only approved architectural patterns used, or was non-adherence formally justified? (`ARC-007`)             | ☐           |
| Are the data flows between zones represented in a DFD with an explicit control at each boundary, versioned? (`ARC-008`) | ☐           |
| Is there a documented threshold for "significant change" and evidence of review after the last one that reached it? (`ARC-009`)     | ☐           |
| Are the diagrams versioned, accessible and reviewed within the last ≤12 months or at the last significant release? (`ARC-010`)         | ☐           |
| For L3 applications, is there segregation of network, permissions and identity between dev, staging and production? (`ARC-011`)          | ☐           |
| For L3 applications, is there a formal approval checklist signed by a security owner before the deploy? (`ARC-012`) | ☐           |
| For L3 applications, is the topology validated automatically in CI/CD, with promotion blocked on failure? (`ARC-013`)        | ☐           |
| Do systems with AI/ML components have explicit trust boundaries (training/inference/agentic), anti-prompt-injection controls (input/output) and provenance of models/datasets, with the AI figuring as a distinct participant? (`ARC-014`) | ☐           |
| Does each AI agent with tool use operate with a dedicated ephemeral identity and minimum scope per tool and environment, without reusing human credentials? (`ARC-015`) | ☐           |
| At autonomy A2+, is there an intent declaration in the audit before a destructive tool-call, out-of-band human approval, an exercised kill-switch and an audit per tool invocation integrated with Ch. 12? (`ARC-015`) | ☐           |
| Is there ARC requirement → threat → decision/ADR → control → evidence traceability, with approved exceptions (compensation, owner, sunset)? | ☐           |

---

## 📌 Practical Application Notes {#-notas-de-aplicação-prática}

- This checklist **must be integrated** into sprint tasks, release gates or regular technical reviews.
- It must be used as an **instrument of control and operational reporting** by architecture, security and audit teams.
- All fields must be validated with **objective evidence** (e.g. versioned files, PR comments, internal links).

> ⚠️ In the event of a negative answer, an approved formal exception must exist (see `ARC-011`).

---

## 📊 Compliance and KPI {#-conformidade-e-kpi}

- Validation of this checklist makes it possible to declare **compliance with Chapter 04 - Secure Architecture**.
- The results per project can be **aggregated for the purposes of measuring organisational maturity and traceability**.
- This mechanism can be integrated into **dashboards, team metrics and continuous audit processes**.

> ✅ This instrument is aligned with the continuous-control logic defined in the SbD-ToE model.
