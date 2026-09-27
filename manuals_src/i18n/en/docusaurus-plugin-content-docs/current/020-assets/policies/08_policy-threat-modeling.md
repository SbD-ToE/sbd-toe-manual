---
id: policy-threat-modeling
title: Threat Modelling Policy
description: Organisational policy that defines the mandatory nature, methodology, execution triggers, formal approval requirements, traceability and management of threat modelling artefacts throughout the lifecycle of applications classified L2 and L3.
tags: [policy, threat modeling, STRIDE, LINDDUN, PASTA, ameaças, cap03, cap04, L2, L3, governance, arquitetura, rastreabilidade]
grupo: design-analise
sidebar_position: 8
translation:
  source_locale: pt
  source_path: 020-assets/policies/08_policy-threat-modeling.md
  source_sha256: df1b585158d73d61ef95cce5d1e232d4f53fd5c73406eb82ebce57e0fac5b047
  source_commit: 50f5914ebc90e4135e6678b2278709d5082dd237
  target_sha256: c4ff583d27d96fa5558818ad0829041cf69c08bd429cd4069d1cf00781ddb454
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [alcada, cycle_iteration, gap_family, lifecycle_phase, nist_sp_800_154_title, owasp_threat_modeling_cheat_sheet, requirement_runtime, risk_level, role_tech_lead, sbdtoe_sbd, threat, traceability]
  glossary_sha256: 0ed186f3703cb74264ad6c652f0dbf6244477db2bc9c60212228da1676bd5da3
  translated_at: 2026-09-27T07:06:13Z
  stamped_at: 2026-09-27T07:06:13Z
  reviewed_by: null
---

# Threat Modelling Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for carrying out **threat modelling** - systematic modelling of threats - in applications classified as L2 or L3.

Threat modelling is the link between risk classification, security requirements and the controls applied. Without threat modelling, security requirements lose their context and the controls applied no longer have a justified origin: they are applied out of habit or convention, not through analysis of real risk.

The objective of this policy is to ensure that:

- The threats relevant to each application are identified systematically
- Decisions to mitigate, accept or transfer risk are documented and approved
- The threat model remains valid and up to date throughout the lifecycle
- The artefacts produced are traceable, protected and auditable

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

| Level | Applicability |
|---|---|
| L1 | Optional; recommended for applications with critical logic or external exposure |
| L2 | Mandatory |
| L3 | Mandatory; with independent review and formal approval |

---

## 3. Methodologies {#3-metodologias}

The organisation adopts the following methodologies, selected proportionally to the context:

| Methodology | Focus | When to apply |
|---|---|---|
| **STRIDE** | Technical threats (Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege) | Exposed applications or those with critical logic - base use at L2 and L3 |
| **LINDDUN** | Privacy threats | Systems with personal data, subject to the GDPR or consent obligations |
| **PASTA** | Modelling based on business risk | Regulated or critical systems, or contexts with high formal demands |

At L2, STRIDE is sufficient as the base methodology. At L3, LINDDUN must be applied whenever personal data exists, and PASTA must be considered in regulatory contexts.

---

## 4. When to carry out threat modelling {#4-quando-realizar-threat-modeling}

### 4.1 Mandatory triggers {#41-triggers-obrigatórios}

| Event | Applicability |
|---|:---:|
| Start of a new project or product (L2/L3) | Mandatory |
| New external integration or additional exposure | Mandatory |
| Significant architecture change | Mandatory |
| New type of sensitive data processed | Mandatory |
| Addition of a new user profile with privileges | Mandatory |
| Pentest result revealing a gap in the model | Mandatory |
| Post-incident originating in an unmodelled threat | Mandatory |

### 4.2 Periodic cadence {#42-cadência-periódica}

In addition to the triggers, the threat model must be reviewed at a minimum cadence:

| Level | Minimum cadence |
|---|---|
| L2 | Annual or with each major release |
| L3 | Half-yearly or with each major release |

---

## 5. Threat modelling process {#5-processo-de-threat-modeling}

### 5.1 Mandatory steps {#51-passos-obrigatórios}

1. **Define scope and assumptions** - system boundaries, components included, trust assumptions, attacker profiles
2. **Create or update the architecture diagram** - DFD (Data Flow Diagram) or equivalent, with explicit trust boundaries
3. **Identify threats** - using the selected methodology (STRIDE, LINDDUN, PASTA)
4. **Assess and prioritise** - impact, likelihood, severity per threat
5. **Decide per threat** - mitigate / accept / transfer / reject - with documented justification
6. **Map to requirements and controls** - link each mitigated threat to the corresponding requirement or control
7. **Approve formally** - by the approval authority appropriate to the risk level
8. **Archive** - approved version with traceability metadata

### 5.2 Minimum model content checklist {#52-checklist-de-conteúdo-mínimo-do-modelo}

- [ ] Scope, assumptions and boundaries documented
- [ ] Architecture diagram with trust boundaries
- [ ] List of threats identified per component/flow
- [ ] Documented decision per threat (mitigate / accept / transfer / reject)
- [ ] Link to security requirements (`REQ-*`) or controls (`CTRL-*`) for mitigated threats
- [ ] Accepted risks with justification and reference to the risk acceptance process
- [ ] Version, date and person responsible for preparing it
- [ ] Formal approval recorded

---

## 6. Formal approval {#6-aprovação-formal}

The threat model is only valid as a security control when there is documented **formal approval**.

| Level | Minimum approval required |
|---|---|
| L2 | AppSec Engineer + Tech Lead |
| L3 | AppSec Engineer + Software Architect + independent review |

The approval must include:
- Confirmation that the scope is correct and complete
- Confirmation that the decisions per threat are technically grounded
- Date and identification of the approver

---

## 7. Update upon technical change {#7-atualização-por-alteração-técnica}

Whenever a significant change occurs, the threat model must be updated **before promotion to production**:

- [ ] Significant change identified and documented
- [ ] New or changed threats recorded
- [ ] Mitigation or acceptance decisions updated
- [ ] New version formally approved
- [ ] Link to the commit or PR that gave rise to the change

The CI/CD pipeline must include a gate that checks whether the threat model is up to date with respect to relevant changes, blocking promotion at L2/L3 when the model is out of date without an approved justification.

---

## 8. Integration with architecture {#8-integração-com-arquitetura}

Threat modelling and secure architecture must be synchronised bidirectionally:

- Architecture decisions must reflect the threats prioritised in the model
- Architectural changes must trigger an update of the threat model where applicable
- Architecture Decision Records (ADR) must reference relevant threats when the decision has a security impact

---

## 9. Protection and retention of artefacts {#9-proteção-e-retenção-dos-artefactos}

Threat modelling artefacts (diagrams, models, decisions) are **sensitive assets** - they contain information about the internal architecture, data flows and identified vulnerabilities.

### 9.1 Access control {#91-controlo-de-acesso}

- Access restricted according to the principle of least privilege
- Sharing only with functions that need access to carry out their responsibilities
- Do not publish in public repositories or in systems without access control

### 9.2 Classification {#92-classificação}

| Level | Minimum recommended classification |
|---|---|
| L2 | Confidential - internal to the product and security team |
| L3 | Confidential / Restricted - access limited to AppSec, architecture and management |

### 9.3 Retention {#93-retenção}

| Artefact | Minimum retention |
|---|---|
| Threat model (active version) | While the application is active |
| Approved historical versions | 3 years after replacement |
| Approval records | 1 year (L1), 2 years (L2), 3 years (L3) |
| Associated accepted risks | As per the Residual Risk Acceptance Policy |

---

## 10. Reuse of previous models {#10-reutilização-de-modelos-anteriores}

Reusing a previous threat model as the basis for a new project or review is permitted, provided that:

- [ ] The previous model is explicitly identified as the reference
- [ ] Differences in context, architecture and flows are analysed and documented
- [ ] Inherited critical decisions are explicitly revalidated
- [ ] The reuse is recorded together with the person responsible for the review

Reuse without explicit review is equivalent to having no threat modelling - the original model is not valid for a different context.

---

## 11. Proportionality by level {#11-proporcionalidade-por-nível}

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Threat modelling mandatory | No | Yes | Yes |
| STRIDE as base methodology | Recommended | Mandatory | Mandatory |
| LINDDUN (personal data) | Optional | Recommended | Mandatory |
| Formal approval | Not applicable | AppSec + Tech Lead | AppSec + Architect + independent review |
| Gate in the CI/CD pipeline | Not applicable | Recommended | Mandatory |
| Periodic review | On request | Annual / major release | Half-yearly / major release |
| Artefacts with access control | Recommended | Mandatory | Mandatory |

---

## 12. Responsibilities {#12-responsabilidades}

| Role | Responsibility |
|---|---|
| Software Architect | Lead or coordinate threat modelling; keep the architecture diagram up to date |
| AppSec Engineer | Support threat identification; approve the model; ensure traceability |
| Tech Lead / Developer | Take part in the threat modelling session; implement assigned mitigations |
| DevOps / SRE | Configure the consistency gate in the pipeline; manage protected storage of the artefacts |
| GRC / Compliance | Ensure that all L2/L3 applications have an approved and up-to-date model |

---

## 13. Review and audit of this policy {#13-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Incident originating in an unmodelled threat
- Update of the reference methodologies (STRIDE, LINDDUN, PASTA)
- Regulatory change with an impact on the mandatory nature of threat modelling

---

## 14. Normative and technical references {#14-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 03 - Threat Modelling | Methodologies, user stories, artefacts, integration into the SDLC |
| SbD-ToE Ch. 04 - Secure Architecture | Threat modelling ↔ architecture synchronisation |
| SbD-ToE Ch. 02 - Security Requirements | Threat → requirement link |
| STRIDE (Microsoft) | Methodology for categorising technical threats |
| LINDDUN | Privacy threat methodology |
| PASTA | Process for Attack Simulation and Threat Analysis |
| OWASP Threat Modeling Cheat Sheet | Practical implementation guide |
| NIST SP 800-154 | Guide to Data-Centric System Threat Modeling |
| SSDF PW.1 | Threat analysis as the basis for security requirements |
| ISO/IEC 27005 | Information security risk management |
