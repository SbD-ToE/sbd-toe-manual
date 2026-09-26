---
id: policy-classificacao-risco
title: Application Risk Classification Policy
description: Organisational policy that defines the mandatory axis-based risk classification model (Exposure, Data, Impact), the moments of application, the review criteria and the formal recording requirements for all applications developed or operated by the organisation.
tags: [policy, classificação, risco, L1, L2, L3, cap01, eixos, exposição, dados, impacto, governance]
grupo: risco
sidebar_position: 2
translation:
  source_locale: pt
  source_path: 020-assets/policies/02_policy-classificacao-risco.md
  source_sha256: 0f16da8f5b21911712d28e75de766c02afca0e7c659715a42859fe4d9cbbec10
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: f605c55d24469afef5a13f853e8a2b38f4f84e4085a9c3959f0442fafa2f1f79
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bc04ded428e40ee1c214f8535dfb1904655b64166d0aa82b5df521e4230b8cb0
  glossary_keys: [alcada, audit_trail, avaliacao, cycle_iteration, gap_family, programme_line, risk_level, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: d90c5b7c0ce1d2f029601b0a27e9f35cb14a66610e76f27ea91dfde8af441de8
  translated_at: 2026-09-26T14:10:42Z
  reviewed_by: null
---

# Application Risk Classification Policy

## 1. Objective {#1-objetivo}

This policy defines the mandatory application risk classification model adopted by the organisation, based on the SbD-ToE model.

Risk classification is the **entry point for the proportional application of security controls**. Without a formal, validated and traceable classification, it is not possible to ensure that the controls applied are appropriate to the technical and business context of each application.

The policy establishes:

- The classification model to be used and its assessment axes;
- The mandatory moments of application and reassessment;
- The risk tier criteria (L1, L2, L3) and their implications;
- The requirements for formal recording, approval and traceability.

---

## 2. Scope {#2-âmbito}

This policy applies to **all applications developed, operated or contracted** by the organisation, regardless of their nature (internal, external, public, API, backend service, product), technology or delivery model.

Classification must be carried out **before development begins** or, for existing applications without a prior classification, in the first review cycle after adoption of the SbD-ToE model.

---

## 3. Classification model - E+D+I axes {#3-modelo-de-classificação---eixos-edi}

Risk classification is based on the assessment of three independent axes:

| Axis | Designation | What it assesses |
|:---:|---|---|
| **E** | Exposure | Attack surface and accessibility of the application |
| **D** | Data | Sensitivity and volume of the data processed |
| **I** | Impact | Consequence of a security incident for the business and for third parties |

The combined score of the three axes determines the overall criticality level of the application.

### 3.1 Risk tiers {#31-escalões-de-risco}

| Level | General description | Typical examples |
|---|---|---|
| **L1** | Low risk - internal application, no sensitive data, limited impact | Internal tools, dashboards without PII, utilities |
| **L2** | Medium risk - public exposure or user data, moderate impact | Public APIs, applications with authentication, customer portals |
| **L3** | High risk - regulated systems, PII, critical data, severe impact | Financial systems, healthcare, critical infrastructure, regulated data |

### 3.2 Criteria per axis {#32-critérios-por-eixo}

**Axis E - Exposure:**

| Value | Criterion |
|---|---|
| Low | Access restricted to the internal network, no external exposure |
| Medium | Authenticated access by external users or partners |
| High | Public access without authentication, or an API exposed to third parties |

**Axis D - Data:**

| Value | Criterion |
|---|---|
| Low | No personal data, no regulated data, no business secrets |
| Medium | Users' personal data, confidential business data |
| High | Sensitive PII, regulated data (GDPR, health, financial), critical secrets |

**Axis I - Impact:**

| Value | Criterion |
|---|---|
| Low | Limited operational impact; no consequences for third parties |
| Medium | Significant operational impact; possible reputational damage |
| High | Critical business impact; regulatory, legal or third-party consequences |

### 3.3 Automation and decision-support contexts {#33-contextos-de-automação-e-apoio-à-decisão}

The use of automation or decision-support mechanisms (including AI systems) **does not create new risk axes**, but must be taken into account when it modifies relevant attributes of the existing risk, namely:

- Introduction of a new exposure surface or external integration;
- Additional processing of personal or regulated data, secrets or confidential information;
- Increased delegation, reach or speed of decisions with real impact.

Whenever any of these conditions applies, the team must adjust the affected axes and explicitly record the rationale for the decision.

---

## 4. Mandatory moments of application {#4-momentos-obrigatórios-de-aplicação}

| Moment | Mandatory status |
|---|:---:|
| Start of a new project or product | Mandatory |
| Before the first deployment to production (go-live) | Mandatory |
| After a significant architectural change | Mandatory |
| After a new external integration or additional exposure | Mandatory |
| After a change to the type or volume of data processed | Mandatory |
| Periodic review with a defined cadence | Mandatory |
| After a relevant security incident | Mandatory |

---

## 5. Periodic review cadence {#5-cadência-de-revisão-periódica}

The classification must be reassessed at a minimum cadence defined per level:

| Level | Minimum cadence |
|---|---|
| L1 | Annual (12 months) |
| L2 | Half-yearly (6 months) |
| L3 | Quarterly (3 months) |

Each reassessment must document:

- [ ] Reassessment of the three axes E, D and I based on the current state of the application
- [ ] Decision: keep the level / change the level (with technical justification)
- [ ] Date of the next scheduled review
- [ ] Approval by the responsible AppSec Engineer

---

## 6. Classification process {#6-processo-de-classificação}

### 6.1 Mandatory steps {#61-passos-obrigatórios}

1. **Apply the E+D+I model** - assess each axis against the criteria defined in section 3
2. **Determine the overall level** - L1, L2 or L3, based on the combined score
3. **Document the rationale** - record the criteria that determined each axis and the final level
4. **Obtain validation** - review and approval by an AppSec Engineer
5. **Record formally** - versioned classification document, with date and owner
6. **Communicate to the teams** - the level determines the mandatory controls to be applied across all SbD-ToE chapters

### 6.2 Approvals by level {#62-aprovações-por-nível}

| Level | Minimum approval required |
|---|---|
| L1 | Tech Lead or AppSec Engineer |
| L2 | AppSec Engineer |
| L3 | AppSec Engineer + CISO or equivalent |

---

## 7. Formal recording and traceability {#7-registo-formal-e-rastreabilidade}

Every classification and its reassessment must be:

- Recorded in a versioned document, identified per application
- Associated with the classification date and the person responsible for approval
- Accessible for consultation by AppSec, GRC and auditors
- Updated whenever the level changes, with history preserved

**Main artefact:** `risk-classification.md` (or equivalent in the project repository or in the organisation's GRC platform)

---

## 8. Implications of the classification {#8-implicações-da-classificação}

The assigned risk level directly determines:

- The **active SbD-ToE chapters** and the mandatory controls to be applied
- The **applicable organisational policies** and their degree of mandatoriness
- The **security artefacts** that must be produced and maintained
- The required **review and security testing cadences**
- The **approval authorities** for exceptions, deploys and risk changes

:::warning
An incorrect or outdated classification invalidates the proportionality of all the controls applied. Actively maintaining the classification is an ongoing responsibility of the team, not a one-off onboarding act.
:::

---

## 9. Responsibilities {#9-responsabilidades}

| Role | Responsibility |
|---|---|
| Tech Lead / Team Lead | Initiate the classification process at project start-up |
| AppSec Engineer | Validate and approve the classification; conduct periodic reassessments |
| Developer | Notify technical changes with potential impact on the E, D or I axes |
| GRC / Compliance | Ensure that all applications have a recorded and up-to-date classification |
| CISO | Approval of L3 classifications; oversight of the classification programme |
| Product Management | Report business changes with an impact on the axes |

---

## 10. Review and audit of this policy {#10-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Change to the SbD-ToE classification model
- Regulatory change that introduces new risk criteria
- Incident that reveals a gap in the classification model

Evidence of the application of this policy (classification documents, reassessment history, approvals) must be auditable by GRC functions and by external auditors.

---

## 11. Normative and technical references {#11-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 01 - Application Classification | E+D+I model, level criteria, classification user stories |
| SbD-ToE Ch. 14 - Governance and Contracting | Approval authorities, organisational traceability |
| ISO/IEC 27001 - Clause 6.1 | Risk assessment and treatment |
| NIST SP 800-30 | Guide for Conducting Risk Assessments |
| OWASP Risk Rating Methodology | Application risk assessment criteria |
| SSDF PW.1 | Risk-based definition of security requirements |
