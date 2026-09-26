---
id: ciclo-vida-risco
title: Risk Classification Lifecycle
sidebar_position: 2
tags: [tipo:ciclo, tema:revisao, classificacao, eventos]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/addon/02-ciclo-vida-risco.md
  source_sha256: 0faecf7cee41766e31acab40fa5c2cf979152b5bc08e02bce2ead89fa6ba3400
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 2e804fa2be50f78922b7768384ed0dd8efde51593e7119fbb8ea0e7b9a4efaea
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [avaliacao, chapter_role, cycle_iteration, evidenciabilidade, lifecycle_phase, mapping, maturity, papel_suporte, sbdtoe_sbd, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: fe05ef689fab5993e3fcaa8b5ad03ba0b0b71b47d2e793b594575a845af8c10a
  translated_at: 2026-09-25T20:18:44Z
  stamped_at: 2026-09-26T18:32:44Z
  reviewed_by: null
---

<!--template: sbdtoe-core -->

# Risk Classification Lifecycle

Risk management in software should not be seen as a one-off event, but as an **iterative and evolving process** throughout the application lifecycle.

In SbD-ToE, risk is treated as a **single concept**, whose relevance and severity may vary over time as a result of technical, organisational or process changes.  
The ability to **identify, reassess and treat risks contextually** is decisive in ensuring that the controls applied remain proportional, effective and justified.

This file describes the **minimum practices** for integrating risk classification and reassessment into the application lifecycle.

---

## 📅 Integration by Lifecycle Phase {#-integração-por-fase-do-ciclo-de-vida}

| Phase                     | Risk Management Actions                                                                 |
| ------------------------ | ---------------------------------------------------------------------------------------- |
| Planning / Requirements | Initial identification of risks based on impact, data, exposure, planned architecture and process assumptions |
| Design / Architecture     | Preliminary assessment of the risks and their **attributes**; mapping to architecture controls |
| Development          | Reassessment of existing risks against new functionality; validation of assumptions and control requirements |
| Testing / Validation       | Confirmation that the defined controls are applied; verification of evidence and pre-release risk review |
| Release / Operations    | Formal recording of residual risk acceptance; continuous monitoring and regression detection |

> 📌 In every phase, changes in the **attributes of the risk** (e.g. detectability, evidentiability or reproducibility) must trigger explicit reassessment.

---

## 📅 Triggers for Risk Reassessment {#-triggers-para-reavaliação-de-risco}

Risk must be reassessed whenever any event occurs that changes its **profile or attributes**, namely:

- Introduction of new relevant functionality or flows;
- Changes to the architecture (e.g. new API exposure, external integrations, change of trust boundaries);
- Changes in the legal, regulatory or contractual context;
- Introduction or modification of automation or decision-support mechanisms (including AI), **when these change validation, evidence or reproducibility assumptions**;
- Detection of critical or recurring vulnerabilities;
- Relevant results from audits, security tests or independent assessments.

---

## 👥 Responsibilities Throughout the Cycle {#-responsabilidades-ao-longo-do-ciclo}

| Role                  | Responsibilities in risk management                                                |
| ---------------------- | ----------------------------------------------------------------------------------- |
| Product Owner          | Assess the impact of the risk on the business and on prioritisation                                 |
| Architecture / Dev Lead | Apply the risk model, identify changes in attributes and propose controls   |
| Sec / AppSec           | Validate the classification, the applied controls and the residual risk                          |
| Operations Team    | Monitor risk at runtime and detect regressions in controls or context            |

> ✅ Risk decisions and reviews must always be **recorded, assigned to responsible persons and traceable**.

---

## 🛠️ Supporting Mechanisms {#️-mecanismos-de-suporte}

Operationalising the risk lifecycle can be supported by:

- Integration of the classification and risk status into backlog tools (e.g. Jira);
- Versioned recording of risks, assumptions and decisions (e.g. YAML or Markdown in Git);
- Risk dashboards based on objective metrics and transparent scoring;
- Explicit risk validation gates in CI/CD pipelines, proportional to the L1–L3 level.

---

## ⚖️ Link with the L1–L3 Thresholds {#️-ligação-com-os-limiares-l1l3}

The risk classification lifecycle must be applied in proportion to the **criticality level of the application**:

- In **L3** applications, risk reassessment must be mandatory at every release or relevant change;
- In **L2** applications, it must take place whenever there are significant changes in architecture, data or process;
- In **L1** applications, it may be based on identified risk events or on a fixed calendar.

This proportionality allows a balance between rigour, operational cost and effectiveness.

---

## 🚀 Recommendations for Maturity {#-recomendações-para-maturidade}

- Formalise cyclical risk reassessment through a checklist, workflow or policy;
- Explicitly monitor residual risk over time;
- Integrate risk decisions with the audit record (*audit trail*);
- Involve non-technical decision-makers whenever the risk has legal, reputational or strategic impact.

> Risk is not a static value: it is a **living process**, which must keep pace with the evolution of the application, the context and development practices.
