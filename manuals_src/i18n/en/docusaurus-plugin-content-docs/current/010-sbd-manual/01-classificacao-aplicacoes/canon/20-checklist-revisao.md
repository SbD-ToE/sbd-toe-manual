---
id: checklist-revisao
title: Review Checklist - Application Classification
sidebar_position: 20
sidebar_label: Review Checklist
tags: [canon, checklist, controlo, projeto, aplicacao]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/canon/20-checklist-revisao.md
  source_sha256: 3f66b9c3f9c495f6f234d4a00d3dd7373fa8008b44c8317fcbcfa6130dbededf
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 53562c351c5fe046b3d9c19654f801d7daae84ccab5d014bd433b6f2a7098cf6
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: f3ae07385fc10c458f9087ea5ea231fd2bbf0e4852b0e4c0e84ec84618762443
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, deterministic, instrument, maturity, sbdtoe_sbd, threat, validation_evaluation, verification_taxonomy]
  glossary_sha256: 66c24c2c24ff0cdc40e251c03583d31e247c986b34255a457d37f63e584e05b6
  translated_at: 2026-09-25T17:59:19Z
  reviewed_by: null
---

# Review Checklist - Application Criticality Classification

This checklist applies to all applications classified according to the criteria defined in **Chapter 01 - Application Criticality Classification**.
It serves as an **instrument for periodic verification, internal audit and an operational maturity KPI**, making it possible to confirm whether:

- The classification is up to date and justified;
- The corresponding minimum controls have been applied;
- There is traceable evidence supporting the risk decisions.

> 🗓️ **Review is recommended at least every 6 months**, or whenever relevant changes occur (functionality, data, exposure).

---

## 📋 Verification Items {#-itens-de-verificação}

| Item                                                                                               | Verified? |
|----------------------------------------------------------------------------------------------------|-------------|
| Is there a formal, documented criticality classification covering the three axes (exposure, data, impact)? | ☐           |
| Was the classification approved by the authority proportional to the level (L1 tech lead, L2 AppSec, L3 CISO), dated and assigned to a responsible person? | ☐           |
| Does the assigned level determine and activate the minimum controls, traceable to the current pipeline or backlog? | ☐           |
| Was it assessed whether the risk attributes (detectability, non-determinism, delegation or automatic execution) require reinforcement to the next level up, and was this applied where indicated? | ☐           |
| Whenever automation or decision support (incl. AI) alters exposure, data or delegation, were the axes reassessed with the rationale recorded? | ☐           |
| Are reclassification criteria and triggers documented?                                      | ☐           |
| After each significant change, was the classification reassessed within the defined maximum period (≤30 days)? | ☐           |
| Was the classification reviewed within the periodic cycle for its level (L1 annual, L2 half-yearly, L3 quarterly), with evidence? | ☐           |
| Do risk acceptance decisions verify the formal criteria for the level (sufficient evidence; residual risk within the threshold L1≤9 / L2≤6 / L3≤4)? | ☐           |
| Is the accepted residual risk documented with compensation, owner and expiry date, with no expired exceptions awaiting renewal? | ☐           |
| Is each risk validated by at least one threat from a recognised catalogue (STRIDE, MITRE ATT&CK or CAPEC)? | ☐           |
| Is the application listed in a central inventory or GRC with level, review date, owner and compliance status, accessible for audit? | ☐           |
| Is the classification decision recorded in a versioned, traceable repository?                  | ☐           |
| Where a tool took part in the classification, are the tool, version, date and final human decision recorded? | ☐           |

---

## 🔄 Final Notes {#-notas-finais}

- This checklist may be used as a **digital form or review template**, and integrated into pipelines, dashboards or backlog tools.
- Complete validation makes it possible to assert compliance with Chapter 01 - constituting **objective evidence of maturity and security control** in the SbD-ToE model.
- It must be archived as an auditable record and associated with the corresponding release cycle.
