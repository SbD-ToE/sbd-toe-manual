---
id: checklist-revisao
title: SbD-ToE Checklist - Threat Modelling
sidebar_label: Review Checklist
sidebar_position: 20
description: Binary, auditable checklist of the adoption of the threat modelling practices of Chapter 03
tags: [checklist, threat-modeling, validação, auditoria, rastreabilidade]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/canon/20-checklist-revisao.md
  source_sha256: 604fa5256daa2049db24c636f31a94fa869a580ea6f3f74aa6ee4b402f7c8669
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 6267bf6d78b0b87ca3433b881106a952053b3fcc25272dda85ffb299056066ab
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, instrument, maturity, requirement_runtime, sbdtoe_sbd, threat, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 27953e85849dea2c3aa24ac31650e0833963f7ace68f68958556908745594aa9
  translated_at: 2026-09-25T20:17:04Z
  stamped_at: 2026-09-26T18:33:24Z
  reviewed_by: null
---

# Periodic Review Checklist - Threat Modelling

This checklist applies to all applications with L2 or L3 criticality, or that involve sensitive flows, external exposures or relevant architecture changes.

It serves as a binary, auditable verification instrument of the **practical adoption of the prescriptions of Chapter 3 - Threat Modelling** (`THR-001` to `THR-008`), enabling:

- Formal verification in technical reviews and audits;
- Control of traceability between threats, requirements and controls;
- Generation of operational indicators that can be aggregated by project or team.

> 🗓️ **Review is recommended at the start of each epic or critical feature, and before significant changes to the system.**

---

## 📋 Verification Items {#-itens-de-verificação}

| Item                                                                                                  | Verified? |
|-------------------------------------------------------------------------------------------------------|-------------|
| Is there a formal, documented threat model for the application (L2+), traceable to the architecture version assessed? | ☐           |
| Does the model include up-to-date DFDs with explicit, justified trust boundaries?                      | ☐           |
| Was a structured methodology applied, with STRIDE as the baseline?                                    | ☐           |
| Do systems that process personal data apply LINDDUN over the same DFD?                               | ☐           |
| Does each threat have an explicit formal disposition (mitigated, accepted, transferred or excluded) with a named owner? | ☐           |
| Does each accepted risk have a documented justification, formal approval and a reassessment deadline?              | ☐           |
| Is there verifiable threat → requirement → backlog → validation traceability, with the threat ID referenced? | ☐           |
| Is the threat model versioned, and was it updated within the defined period (≤30 days after a trigger or per release), with a freshness gate in the CI/CD? | ☐           |
| Was the threat model reviewed by independent AppSec before go-live (L2+), with evidence?             | ☐           |
| Do systems with AI/ML components have an extended threat model (prompt injection, model poisoning) referenced to MITRE ATLAS or NIST AI 100-2? | ☐           |
| Do AI agents with tool use have an agentic DFD and a threat library cited by canonical ID and anchored to controls? | ☐           |
| Were abuse/misuse cases derived and integrated into the backlog as traceable requirements?               | ☐           |
| Was the threat model validated and approved by an explicitly responsible person, distinct from the supporting artefacts? | ☐           |
| Do the threat modelling artefacts have defined access control, classification and retention?          | ☐           |
| Were the threats prioritised by business impact, and is that prioritisation reflected in the backlog?         | ☐           |

---

## 🔄 Operational Integration {#-integração-operacional}

- This checklist can be integrated into **architecture reviews, release gates, CI/CD pipelines or sprint planning sessions.**
- Each item must be validated with **objective evidence**: DFD models, STRIDE files, comments in PRs, links to requirements in the backlog, session records, etc.

> ⚠️ In the event of a negative answer, a documented formal exception must exist, with an owner and a reassessment deadline, in accordance with the Ch. 2 model.

---

## ✅ Compliance and KPI {#-conformidade-e-kpi}

- Validation of this checklist makes it possible to declare **compliance with Chapter 3 - Threat Modelling**.
- The count of affirmative answers can be used to **measure the degree of adoption of the prescribed practices**.
- This result can be aggregated by team, domain or organisation as an **indicator of maturity and risk coverage**.

> 📌 This operational mechanism is aligned with the model of traceability and continuous control defined in SbD-ToE.
