---
id: policy-revisao-periodica-risco
title: Periodic Risk Review Policy
description: Organisational policy that defines the mandatory cadence and the review triggers for the application risk classification, ensuring that the criticality level and the associated controls remain appropriate to the technical and business context throughout the entire lifecycle of the application.
tags: [policy, revisão periódica, risco, classificação, cap01, cap14, cadência, triggers, event-based, time-based, L1, L2, L3, governance]
grupo: risco
sidebar_position: 4
translation:
  source_locale: pt
  source_path: 020-assets/policies/04_policy-revisao-periodica-risco.md
  source_sha256: abc4bc1a901e7bb9be3c51e458919d0d19e23015e5c38bc23bcef471d93d4c57
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 0955f71c08688774a63b8cca900812d174be2b6d8c0082f2845d32d127fab040
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [alcada, avaliacao, cycle_iteration, lifecycle_phase, mcp_reading_programa, programme_line, risk_level, role_tech_lead, sbdtoe_sbd, verificacao_check, verification_taxonomy]
  glossary_sha256: 24dcf33bc58faa933548c4084bfc00d9a3f08faeabe0993196d4d80717b9def8
  translated_at: 2026-09-26T14:10:44Z
  stamped_at: 2026-09-26T18:36:44Z
  reviewed_by: null
---

# Periodic Risk Review Policy

## 1. Objective {#1-objetivo}

This policy defines the mandatory mechanisms for reviewing the application risk classification and the associated security controls throughout the entire lifecycle of each application.

Risk classification is not a one-off onboarding act - it is a dynamic state that must be kept up to date. Technical, business or regulatory changes may modify the exposure, the data processed or the potential impact of an incident, without this being immediately visible. Without structured review, the classification ages silently and the controls applied cease to be proportional to the real risk.

This policy establishes two complementary review mechanisms:

- **Time-based** - review at a fixed periodic cadence, independent of changes
- **Event-based** - review triggered by relevant technical or business events

---

## 2. Scope {#2-âmbito}

This policy applies to **all applications with an active risk classification** (L1, L2 or L3), regardless of their development status (under construction, in production, in maintenance or being discontinued).

Applications in the process of decommissioning retain the review obligation until their formal deactivation and the recording of their closure.

---

## 3. Time-based review - periodic cadence {#3-revisão-time-based---cadência-periódica}

### 3.1 Mandatory minimum cadences {#31-cadências-mínimas-obrigatórias}

| Level | Minimum cadence | Mandatory status |
|---|---|---|
| L1 | Annual (12 months) | Recommended |
| L2 | Half-yearly (6 months) | Mandatory |
| L3 | Quarterly (3 months) | Mandatory |

The date of the next review must be recorded in the classification document at the time of each review. The absence of a scheduled review date is treated as non-compliance.

### 3.2 What to assess in each periodic review {#32-o-que-avaliar-em-cada-revisão-periódica}

- [ ] Reassessment of the three axes E, D and I based on the current state of the application
- [ ] Verification of technical changes since the last review (new integrations, changes in exposure, new data types)
- [ ] Verification of business changes with a potential impact on the risk level
- [ ] Review of the status of the controls applied and of their adequacy to the current level
- [ ] Review of the accepted residual risks and of their validity
- [ ] Documented decision: keep the level / change the level
- [ ] Scheduling of the next review

### 3.3 Outcome of the periodic review {#33-resultado-da-revisão-periódica}

| Decision | Action |
|---|---|
| Level maintained | Record the reassessment with date, owner and justification; schedule the next review |
| Level raised | Update the classification; review the mandatory controls; communicate to the teams; obtain approval |
| Level lowered | Update the classification with detailed technical justification; obtain AppSec approval |

:::warning
Lowering the criticality level requires rigorous technical justification and approval by an AppSec Engineer. It is not acceptable to lower the level solely for reasons of operational convenience or to reduce the compliance effort.
:::

---

## 4. Event-based review - mandatory triggers {#4-revisão-event-based---triggers-obrigatórios}

### 4.1 Triggers that require an immediate review {#41-triggers-que-obrigam-a-revisão-imediata}

The review of the classification must be triggered **immediately** (within a maximum of 5 working days) when any of the following events occurs:

| Trigger | Description |
|---|---|
| New external integration | Connection to an external system, third-party API or cloud service not previously foreseen |
| New type of sensitive data | Start of processing of PII, regulated data, health data, financial data |
| Change in exposure | Opening of a new public endpoint, authentication removed, new access channel |
| Significant architectural change | Change of deployment model, infrastructure migration, addition of a critical component |
| Introduction of automation or AI | When it modifies exposure, the data processed or the impact of decisions |
| Relevant security incident | Any incident that reveals a misalignment between the classified level and the real risk |
| Applicable regulatory change | New legal or normative obligation with an impact on the classification |
| Change of business model | Change in the target audience, jurisdiction or purpose of the application |

### 4.2 Triggers that recommend a review {#42-triggers-que-recomendam-revisão}

The following events do not require an immediate review, but must be assessed by the team as potential triggers:

- Significant change in the volume of data processed
- Addition of new user profiles with different access levels
- Change of the responsible team or of the security owner
- Pentest results that reveal exposure not foreseen in the classification

### 4.3 Event-based review process {#43-processo-de-revisão-event-based}

1. **Identify the trigger** - document the event that gave rise to the review
2. **Assess the impact** on the E, D and I axes
3. **Determine whether the level must be changed**
4. **Document the decision** with clear technical justification
5. **Obtain approval** from the approval authority appropriate to the resulting level
6. **Update** the classification document and communicate to the teams
7. **Restart the calendar** of periodic reviews based on the new level

---

## 5. Tool-assisted detection {#5-deteção-assistida-por-ferramentas}

The organisation may use automated tools to detect events that may constitute review triggers (e.g. analysis of commits, PRs, configuration changes).

When a tool proposes reclassification or alerts to a potentially relevant change:

- The alert must be assessed by an AppSec Engineer before any decision
- Patch updates to dependencies **do not constitute**, in themselves, a review trigger
- Minor/major changes to critical dependencies **must be assessed**
- The final decision is always **human** - the tool signals, it does not decide

---

## 6. Mandatory documentation of each review {#6-documentação-obrigatória-de-cada-revisão}

Each review (periodic or event-based) must produce a record with:

- [ ] Date of the review
- [ ] Type of review (time-based / event-based)
- [ ] Trigger (for event-based) or cadence (for time-based)
- [ ] Reassessment of the E, D and I axes
- [ ] Decision: level maintained / changed (with justification)
- [ ] Status of controls and accepted risks verified
- [ ] Person responsible for the review
- [ ] Approval (if applicable)
- [ ] Date of the next scheduled review

**Main artefact:** an entry in the application's classification document (`risk-classification.md` or equivalent), with the history of all previous reviews preserved.

---

## 7. Integration with the development lifecycle {#7-integração-com-o-ciclo-de-desenvolvimento}

| Moment | Expected action |
|---|---|
| Sprint planning (L3) | Check whether any event-based trigger occurred in the previous sprint |
| Release / go-live | Confirm that the classification is up to date and within its cadence |
| Incident retrospective | Check whether the periodic review would have detected the problem |
| Onboarding of a new team | Check the date of the last review and start a new one if necessary |

---

## 8. Responsibilities {#8-responsabilidades}

| Role | Responsibility |
|---|---|
| AppSec Engineer | Conduct and approve reviews; monitor the review calendar per application |
| Tech Lead / Developer | Identify and report technical events that may constitute triggers |
| GRC / Compliance | Monitor compliance with the cadences; issue alerts for overdue reviews |
| Product Management | Communicate business changes with a potential impact on the classification |
| CISO | Oversee the review programme; ensure organisational coverage |

---

## 9. Non-compliance {#9-incumprimento}

The absence of a review within the cadence defined for the level constitutes non-compliance with this policy and must be:

- Recorded as a non-conformity in the GRC system
- Escalated to the AppSec Engineer and the CISO
- Resolved through an immediate review and a record of the cause of the delay

---

## 10. Review and audit of this policy {#10-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Change to the SbD-ToE classification model
- Incident originating in an outdated classification
- Regulatory change with an impact on the mandatory review cadences

The review history of all applications must be made available in internal and external security audits.

---

## 11. Normative and technical references {#11-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 01 - Application Classification | E+D+I model, review cadences, event-based triggers |
| SbD-ToE Ch. 14 - Governance and Contracting | Continuous cycle of review and reassessment of exceptions |
| ISO/IEC 27001 - Clause 6.1 | Risk assessment and treatment with periodic review |
| NIST SP 800-30 | Guide for Conducting Risk Assessments |
| NIST CSF - Identify (ID.RA) | Risk Assessment with continuous review |
| SSDF PW.1 | Risk-based definition and review of security requirements |
