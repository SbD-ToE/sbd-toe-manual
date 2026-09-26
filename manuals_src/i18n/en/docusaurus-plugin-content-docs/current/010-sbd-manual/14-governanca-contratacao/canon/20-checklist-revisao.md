---
id: checklist-revisao
title: Checklist SbD-ToE - Governance and Contracting
sidebar_position: 20
description: Binary control checklist of the application of governance practices per project
tags: [checklist, revisao, controlo, projeto, excecoes, aprovacao, contratacao]
sidebar_label: Review Checklist
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/canon/20-checklist-revisao.md
  source_sha256: f6c7205315c4523a3a66fef8246ab0db2be27dd04abdb0cb411a6beac7cbe728
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 67079d60e671d93a0a6c08e83f982ffbac334433c9d5c275bde7aebbc3188040
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [alcada, avaliacao, chapter_role, cycle_iteration, maturity, risk_level, sbdtoe_sbd, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: b925518857ea7b624a0c808d4b3ba8f2f92e2e76538ca9b0a4c37a6cef8f2d17
  translated_at: 2026-09-26T12:00:22Z
  reviewed_by: null
---


# Periodic Review Checklist - Governance and Contracting

This checklist applies to **projects, applications or contracts** with a technical impact and aims to validate the practical application of the practices prescribed in Chapter 14 - Governance and Contracting (`GOV-001` to `GOV-012`).

> 📌 It must be used in formal reviews, internal audits, project milestones or technical revalidation cycles.

---

## 📋 Verification Items {#-itens-de-verificação}

| Item                                                                                                                   | Verified? |
|------------------------------------------------------------------------------------------------------------------------|-------------|
| Is there a formal security governance model approved by management and reviewed within ≤12 months? (`GOV-001`)             | ☐           |
| Does the application or project have a formally designated and registered security owner? (`GOV-002`)                          | ☐           |
| Is the criticality level (L1–L3) documented and justified?                                                         | ☐           |
| Are the approval authorities per risk level documented and known to the decision-makers, with traceable escalation? (`GOV-003`) | ☐           |
| Are the risk-proportional minimum requirements identified and applied?                                         | ☐           |
| Is there a formal exception management process, recording each exception with owner, compensating measure, referenceable evidence, expiry date and revalidation alert (max. 90 days)? (`GOV-004`/`GOV-005`) | ☐           |
| Do contracts with third parties include risk-proportional security clauses? (`GOV-006`)                         | ☐           |
| Have suppliers with technical access been validated (questionnaire/checklist; L3: SBOM, incident SLA, right to audit) before onboarding? (`GOV-007`) | ☐           |
| Is there organisational traceability per application linking risk → requirements → exceptions → suppliers → owner? (`GOV-008`) | ☐           |
| Is the chain of authority of each risk decision (who requested, assessed, approved) verifiable, with referenceable and retained evidence? (`GOV-009`) | ☐           |
| Is there a periodic compliance review cycle per asset type (L3 quarterly, L2 half-yearly, suppliers annually), with corrective actions (owner and deadline)? (`GOV-010`) | ☐           |
| Are there governance KPIs defined, collected and reported to management, with thresholds that trigger corrective action? (`GOV-011`) | ☐           |
| Is there an active maturity assessment (SAMM/DSOMM or equivalent) within ≤12 months, with an evolution plan (L3)? (`GOV-012`) | ☐           |
| Is the application included in the control matrix of SbD-ToE practices, and are the relevant organisational policies formally approved and audited? | ☐           |
| Do contracts with AI model providers include data retention, training opt-out, GDPR localisation (Art. 44–49), audit rights, a change-notification SLA and AI Act compliance (Art. 53/55 GPAI), with the provider on the approved list (`DEP-014`)? | ☐           |
| Is there a formal secure offboarding process (access revocation, asset recovery, secret rotation), and do the decision-makers have valid SbD training within the last 12 months (Ch. 13)? | ☐           |
| Do third parties complete technical onboarding and mandatory training (by profile, with quiz and sandbox) with a recorded *sign-off* **before** access to systems, with the record traceable and retained as required by regulation (`GOV-013`)? | ☐           |
| Is the access of active contractors reviewed periodically (half-yearly L1 / quarterly L2–L3) with validation of need, same-day removal of excessive access, a signed review and changes in the *audit trail* (`GOV-014`)? | ☐           |

---

## 🔄 Operational Integration {#-integração-operacional}

- It may be used as a **recurring review template** in Jira, Confluence, SharePoint or Forms;
- It must have joint validation by **AppSec, GRC and product management**;
- Each item requires **traceable and versioned evidence**, in accordance with the practices of Ch. 14.

---

## 🎯 Compliance and Indicators {#-conformidade-e-indicadores}

- Positive validation of this checklist makes it possible to declare **compliance with Chapter 14 - Governance and Contracting**.
- The results may be integrated into **dashboards, audit cycles and maturity metrics**.
- It makes it possible to derive **objective KPIs** such as:
  - % of applications with formally approved exceptions;
  - % of validated suppliers;
  - % of contracts with security clauses;
  - % of projects with an up-to-date SbD-ToE control matrix.

---

## 🔗 Cross-links {#-ligações-cruzadas}

- **Ch. 01** - Risk classification (basis for proportional application)
- **Ch. 02** - Security requirements (target of exceptions, traceability)
- **Ch. 05** - Dependencies and SBOM (contractual clauses and validations)
- **Ch. 10** - Security testing (practical validation of controls)
- **Ch. 13** - Training (mandatory validation of critical functions)
- **Ch. 14** `addon/11-controlos-praticas-sbd` - Consolidated control of SbD-ToE practices

> ✅ This checklist is a central mechanism for the continuous, proportional and traceable control of the adoption of the SbD-ToE model in real governance and contracting contexts.
