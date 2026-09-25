---
id: catalogo-requisitos-classificacao
title: Application Classification Requirements Catalogue
description: Canonical catalogue of application criticality classification requirements (CLA-001 to CLA-008), with applicability by risk level and acceptance criteria for formal classification, reclassification, residual risk and proportionality of controls.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:classificacao, CLA, classificacao, reclassificacao, risco-residual, proporcionalidade, inventario, L1, L2, L3, auditoria]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/addon/00-catalogo-requisitos.md
  source_sha256: 11eacf25b9f79bf870d3ad05ea0a1855838c39aab61d72adcd090da67e227613
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 7d599623e43e27e749bc273980c144577568ac802ad1ed155242fb4db9e07af7
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: f3ae07385fc10c458f9087ea5ea231fd2bbf0e4852b0e4c0e84ec84618762443
  glossary_keys: [avaliacao, cycle_iteration, gap_family, lifecycle_phase, mapping, practitioner_manual, requirement_runtime, risk_level, sbdtoe_sbd, threat, traceability]
  glossary_sha256: d562ba09427b74d39736099084d363d09fa13380d898268693378ae0a346c42f
  translated_at: 2026-09-25T17:59:11Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Application Classification Requirements Catalogue

## Scope: classification as a foundational control of proportionality {#âmbito-a-classificação-como-controlo-fundacional-de-proporcionalidade}

This catalogue covers the **application criticality classification requirements** — the controls that determine with what rigour, frequency and depth security is applied in each project or application.

Classification is not an administrative label: it is the mechanism that activates the set of controls proportional to the real risk. A misclassified application has the wrong controls — typically insufficient ones — and that gap is invisible until the incident.

The CLA requirements are verifiable: the existence of an approved classification, of documented reclassification criteria, of an active review cycle and of residual risk with a TTL are auditable facts. Absence of evidence is equivalent to absence of control.

For the complete mapping of all SbD-ToE requirements catalogues by technical domain, canonical prefix and owner, see [Ch. 02 - Catalogue Mapping](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **On curation:** Consolidated from NIST SSDF, NIST SP 800-30, ISO/IEC 27001, ISO/IEC 27005, OWASP SAMM v2.1, OWASP DSOMM, BSIMM13 and risk-oriented application governance practices. It should be adapted to the organisational risk model, but without losing traceability to L1, L2 and L3.

For instantiation in a project and operational naming (`SEC-Lx-CLA-CODIGO`), see [Taxonomy and Traceability](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Conventions {#convenções}

| Symbol | Meaning |
|---------|-------------|
| ✔ | Mandatory requirement for this level |
| - | Not applicable or not mandatory at this level |

The levels are cumulative: L3 includes all L1 and L2 requirements; L2 includes all L1 requirements.

---

## CLA Catalogue - Application Classification {#catálogo-cla---classificação-de-aplicações}

Requirements that ensure each application has a formal criticality classification, proportional to the real risk, kept up to date and used as the basis for control selection.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| CLA-001 | Formal classification according to the risk axes model | ✔ | ✔ | ✔ | Each application has a criticality classification formalised according to the axes of exposure, data sensitivity and incident impact; the classification is documented, approved by the security owner and recorded in an inventory or GRC tool; it is used as direct input for control selection and pipeline gates. |
| CLA-002 | Approval proportional to the assigned risk level | ✔ | ✔ | ✔ | The classification of each application is approved by the entity proportional to the risk: L1 by the tech lead or equivalent, L2 by the team's AppSec referent, L3 by the CISO or equivalent; the approval is documented, dated and traceable to the person responsible. |
| CLA-003 | Activation of baseline controls determined by the classification | ✔ | ✔ | ✔ | The classification level determines the set of mandatory baseline controls — including CI/CD gates, testing requirements, review frequency and monitoring obligations; the activation of the controls is verifiable through traceability between the classification and the current pipeline or backlog. |
| CLA-004 | Reclassification criteria documented and monitored | ✔ | ✔ | ✔ | Explicit reclassification criteria are documented: new sensitive data flows, integration with systems of higher criticality, exposure to new regulatory contexts, a relevant security incident or a change in the threat model; each criterion has an associated review trigger. |
| CLA-005 | Periodic classification review cycle differentiated by level | ✔ | ✔ | ✔ | L1 applications are reviewed annually, L2 every six months, L3 quarterly; each review produces traceable evidence with date, reviewer and conclusion; when the classification is maintained, the justification is documented; an overdue review is treated as an active non-conformity. |
| CLA-006 | Classification reassessment after a significant change event | ✔ | ✔ | ✔ | After a significant change — new critical integration, change in exposure, security incident or relevant regulatory change — the classification is reassessed within a maximum of 30 days; the reassessment is traceable to the event that triggered it and to the person responsible who conducted it. |
| CLA-007 | Residual risk with formalised compensation, owner and TTL | - | ✔ | ✔ | When the classification results in partially applied controls (accepted deviation), the residual risk is documented with explicit compensation, exception owner, resolution deadline and expiry date; an expired exception without renewal is treated as an active non-conformity and reported to the security owner. |
| CLA-008 | Application inventory kept up to date and accessible for audit | ✔ | ✔ | ✔ | A central inventory or GRC exists with a record of each application, including current classification level, date of last review, security owner and compliance status; the inventory is updated after each classification change or transfer of responsibility; accessible for audit without manual preparation. |

---

## Explanatory notes {#notas-explicativas}

- **CLA-001**: Multi-axis classification (exposure, data, impact) prevents underestimating the risk of applications that look simple on the surface but hold sensitive data or have critical impact if compromised. A single classification axis is invariably incomplete.
- **CLA-002**: Proportionality in approval is not bureaucracy — it is the mechanism that gives the classification its authority. A classification approved only by the developer who created it has no force to impose onerous controls and is not defensible in audit.
- **CLA-003**: Without explicit activation of controls proportional to the classification, the assigned level is merely decorative. This requirement closes the link between the classification decision and the operational consequences that follow from it.
- **CLA-004 and CLA-005**: The distinction is operationally relevant: CLA-004 verifies that active reclassification triggers exist (the classification responds to events); CLA-005 verifies that a proactive cycle independent of events exists (the classification is revisited even in the absence of incidents or changes). Both are necessary.
- **CLA-006**: The 30-day deadline for reassessment after a significant event is deliberately conservative — long enough for a rigorous assessment, but short enough to prevent outdated classifications in applications whose risk profile has changed. For L3, the deadline may be more restrictive by organisational policy.
- **CLA-007**: Residual risk documented with a TTL serves two purposes: it informs the owner of the existing gap and creates a commitment to resolution by a date. The absence of a TTL turns a temporary exception into an invisible permanent deviation.
- **CLA-008**: The inventory is the primary evidence artefact in compliance audits. An inventory that can be updated manually but is not in fact updated is equivalent to no inventory for audit purposes.

---

> For the formal classification model by axes, see [Classification Model by Axes](./modelo-classificacao-eixos).
> For the risk lifecycle associated with classification, see [Risk Lifecycle](./ciclo-vida-risco).
> For risk acceptance criteria by level, see [Risk Acceptance Criteria](./criterios-aceitacao-risco).
> For residual risk management, see [Residual Risk](./risco-residual).
> For activation of baseline controls by risk level, see [Controls Matrix by Risk](./matriz-controlos-por-risco).
> For classification KPIs and metrics, see [Classification KPIs and Metrics](./12-kpis-metricas.md).
