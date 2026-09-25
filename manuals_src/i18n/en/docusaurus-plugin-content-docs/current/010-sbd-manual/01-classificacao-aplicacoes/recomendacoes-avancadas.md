---
id: recomendacoes-avancadas
title: Advanced Recommendations for Risk Classification
tags: [canon, recomendacoes, maturidade, risco]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/recomendacoes-avancadas.md
  source_sha256: 1ea6071773c9f4c333b95e7f033ba979f96810ec54f7f8d0ac0066d88fed7b25
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: ab4c6c8a87cd7e5da46d53d4f336a4c62ea7bf9b3095dc35c4a44fb1c7c701e1
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [audit_trail, avaliacao, chapter_role, cycle_iteration, lifecycle_phase, maturity, sbdtoe_sbd, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: d3c61299c4b7550a7a84d4d7206f01052879fe10f58214fb2891139559bbc145
  translated_at: 2026-09-25T20:18:56Z
  reviewed_by: null
---


# Advanced Recommendations - Risk Management

This annex presents **non-mandatory** but highly recommended practices for organisations that wish to reach **higher levels of maturity and auditability** in risk management applied to the software lifecycle.

These recommendations **complement the mandatory practices of Chapter 01** and may be adopted progressively according to:

- The applicable regulatory context;
- The organisation's risk appetite and tolerance;
- The intended maturity level (e.g. ISO 27001, SOC 2, PCI-DSS);
- The strategic objectives for visibility and governance.

---

## 1. Integration with GRC Tools {#1-integração-com-ferramentas-de-grc}

- Integrate the risk classification and acceptance model with corporate GRC (Governance, Risk & Compliance) tools, such as:
  - **ServiceNow Risk**
  - **Archer GRC**
  - **Riskonnect**, among others.
- This integration makes it possible to:
  - Align technical decisions with organisational risks;
  - Support internal and external audit processes;
  - Guarantee centralised traceability of decisions.

---

## 2. Structured Justifications for Risk Acceptance {#2-justificativas-estruturadas-de-aceitação-de-risco}

- Adopt a **formal model of informed risk acceptance**, with the following minimum fields:
  - Description and impact of the risk;
  - Reason for acceptance;
  - Alternatives considered;
  - Compensations applied (if any);
  - Person responsible for the decision and temporal validity;
- It must be versioned, traceable and auditable.

---

## 3. SLA for Risk Classification Review {#3-sla-para-revisão-da-classificação-de-risco}

- Establish **maximum deadlines for the formal review of the classification**, such as:
  - L3: reassessment every 90 days;
  - L2: every 180 days;
  - L1: up to 365 days.
- Automate alerts and tasks in the security backlog.

---

## 4. Decision Support with Risk Visualisation {#4-suporte-à-decisão-com-visualização-de-risco}

- Use visualisation tools for:
  - Heat matrices (heatmaps) per application or team;
  - Dashboards cross-referencing risk vs control applied;
  - Visual alerts for expired classifications.
- This facilitates **communication with management, audit and non-technical stakeholders**.

---

## 5. Versioning and Auditing of Classifications {#5-versionamento-e-auditoria-de-classificações}

- Keep a historical record of all classifications with:
  - Timestamp and author;
  - Reason for the change;
  - Cross-reference to the release or technical change;
  - (Optional) Digital hash for integrity verification.
- Essential for compliance with **ISO 27001, SOC 2, NIS2** and similar.

---

## 6. Alignment with the Organisation's Risk Appetite {#6-alinhamento-com-apetite-ao-risco-da-organização}

- Define **risk levels (L1/L2/L3) aligned with the organisation's formal appetite**.
- This allows:
  - Customisation by application type (e.g. SaaS, internal, regulated);
  - Support for the budgetary prioritisation of controls;
  - Coherence between accepted risk and security investment.

---

## 7. Cross-Review between Teams (Peer Review) {#7-revisão-cruzada-entre-equipas-peer-review}

- Establish a process of **cross-validation of classifications** by other teams (e.g. between products, AppSec, architecture).
- Benefits:
  - Reduced individual bias;
  - Increased collective maturity;
  - Promotion of consistency and good practice.

---

## 8. Specialised Technical Training {#8-formação-técnica-especializada}

- Include in training plans:
  - Technical risk assessment applied to the SDLC;
  - Reading and interpreting the classification axes;
  - Documentation and traceability for audits.
- Preferably linked to the **training tracks by profile** defined in Ch. 13.

---

## 📌 Final Note {#-nota-final}

These practices are not mandatory for minimum compliance with the SbD-ToE model, but they are **highly recommended** for organisations that wish to:

- Increase the **efficiency and visibility** of risk management;
- Obtain gains in **maturity, traceability and auditability**;
- **Reduce dependence on informal processes** in critical security decisions.

> ✅ Their adoption may be gradual, aligned with the organisation's capacity and with the applicable regulatory requirements.
