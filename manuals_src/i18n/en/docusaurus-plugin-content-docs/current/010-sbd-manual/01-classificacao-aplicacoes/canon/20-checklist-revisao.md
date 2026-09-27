---
id: checklist-revisao
title: Review Checklist - Application Classification
sidebar_position: 20
sidebar_label: Review Checklist
tags: [canon, checklist, controlo, projeto, aplicacao]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/canon/20-checklist-revisao.md
  source_sha256: 68ff021f8f90c962dd15063740f61e25a6c49747d984dcf8d9a8ab9be41885ef
  source_commit: 036d74010f423f247be988e4a417375c74edb9d9
  target_sha256: 07d8ac01f377e89c1389a9105bd9a54892acecaf29732018b2066596f13414af
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, deterministic, instrument, maturity, role_tech_lead, sbdtoe_sbd, threat, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 5db6a4b25194691c747c03f273d909edd249bc4d5c6c1a0b2080d00bf13ad42d
  translated_at: 2026-09-27T07:53:37Z
  stamped_at: 2026-09-27T07:53:37Z
  reviewed_by: null
---

# Review Checklist - Application Criticality Classification

This checklist applies to all applications classified according to the criteria defined in **Chapter 01 - Application Criticality Classification**.
It serves as an **instrument for periodic verification, internal audit and an operational maturity KPI**, making it possible to confirm whether:

- The classification is up to date and justified;
- The corresponding minimum controls have been applied;
- There is traceable evidence supporting the risk decisions.

> 🗓️ **A review is recommended at least at the cadence of Policy 04 (annual at L1, half-yearly at L2, quarterly at L3)**, or whenever there are relevant changes (functionality, data, exposure).

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
