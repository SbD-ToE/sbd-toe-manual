---
id: policy-aceitacao-risco
title: Residual Risk Acceptance Policy
description: Organisational policy that defines the criteria, the formal process, the approval authorities and the traceability requirements for accepting residual risk in applications classified L1 to L3, including risks arising from controls not applied, unfixed findings and threats identified in threat modelling.
tags: [policy, risco residual, aceitação de risco, exceções, cap01, cap03, cap10, governance, L1, L2, L3]
grupo: risco
sidebar_position: 3
translation:
  source_locale: pt
  source_path: 020-assets/policies/03_policy-aceitacao-risco.md
  source_sha256: 13ec483762279b491858c8168444dfb1fb0820ca2c86d3597bff7c796756b6b2
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: dfdb4cfad1db1a372dd3d1a83452a88bd6396b8a3f78bb670c31642ebacf278c
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bc04ded428e40ee1c214f8535dfb1904655b64166d0aa82b5df521e4230b8cb0
  glossary_keys: [alcada, cycle_iteration, programme_line, requirement_runtime, risk_level, sbdtoe_sbd, threat, traceability]
  glossary_sha256: abbe3e1eea703f641a6bfb399c503862115846961d5e6764158924df1dfa87b1
  translated_at: 2026-09-26T14:10:43Z
  reviewed_by: null
---

# Residual Risk Acceptance Policy

## 1. Objective {#1-objetivo}

This policy defines the formal process for **accepting residual risk** in applications developed or operated by the organisation.

Residual risk is the risk that remains after the security controls defined for the application's criticality level have been applied. Accepting it is not, in itself, a failure - it is an informed management decision, provided that it is formalised, approved by the appropriate approval authority, time-bound and traceable.

The absence of a formal risk acceptance process leads to risk decisions being taken implicitly, without visibility, without assigned responsibility and without a review mechanism.

---

## 2. Scope {#2-âmbito}

This policy applies to all situations in which there is identified and accepted residual risk, including:

- Mandatory controls for the criticality level that have not been applied
- Security findings (SAST, DAST, IAST, SCA, fuzzing, pentest) that have not been fixed
- Threats identified in threat modelling for which no mitigation has been implemented
- Architectural exceptions with an impact on the security posture
- Dependencies with known vulnerabilities for which no fix is available or viable

---

## 3. Types of residual risk {#3-tipos-de-risco-residual}

| Type | Origin | Examples |
|---|---|---|
| **Control not applied** | SbD-ToE control matrix | Mandatory requirement for the level not implemented |
| **Unfixed finding** | SAST, DAST, IAST, SCA, fuzzing, pentest | Identified vulnerability without remediation within the SLA |
| **Accepted threat** | Threat modelling | Documented STRIDE threat without a technical mitigation |
| **Architectural exception** | Architecture review | Insecure pattern kept because of a technical or business constraint |
| **Vulnerable dependency** | SCA / SBOM | Active CVE with no fix available or with an impact assessed as acceptable |

---

## 4. Criteria for risk acceptance {#4-critérios-para-aceitação-de-risco}

A residual risk may only be formally accepted if it meets **all** of the following criteria:

- [ ] The risk is **compatible with the criticality level** of the application (L1, L2 or L3)
- [ ] The residual risk is **within the defined thresholds** for acceptance at the level concerned
- [ ] There is **sufficient evidence of the controls applied** that reduce the risk to the residual level
- [ ] A **compensating mitigation** has been identified and documented, where technically feasible
- [ ] The acceptance decision is **time-bound** - with an expiry and reassessment date
- [ ] The decision is **formally approved** by the approval authority appropriate to the risk level

:::warning
Risk acceptance does not replace remediation. It is a temporary, documented decision, not a permanent solution. All accepted risk must have an expiry date and a reassessment mechanism.
:::

---

## 5. Acceptance thresholds by level {#5-limiares-de-aceitação-por-nível}

| Level | Maximum severity acceptable without escalation | Maximum acceptance period |
|---|---|---|
| L1 | High (with justification and compensation) | 90 days |
| L2 | Medium without escalation; High requires AppSec approval | 60 days |
| L3 | Medium requires AppSec; High requires CISO; Critical is not acceptable | 30 days |

:::note
Findings of **Critical** severity may not be accepted as residual risk at any level without an active remediation plan with a defined deadline. Accepting a Critical finding is a last-resort exception, subject to CISO approval and formal recording with a maximum period of 7 days.
:::

---

## 6. Acceptance process {#6-processo-de-aceitação}

### 6.1 Mandatory steps {#61-passos-obrigatórios}

1. **Identify the residual risk** - origin, type, severity and technical context
2. **Assess the impact** - the real consequence in the context of the application and the business
3. **Define a compensating mitigation** - an alternative control active during the acceptance period
4. **Document the technical justification** - why the control was not applied or the finding was not fixed
5. **Define the validity period** - expiry date of the acceptance and reassessment date
6. **Obtain formal approval** - by the approval authority appropriate to the risk level (see section 7)
7. **Record** - in the application's exception repository or GRC platform

### 6.2 Checklist per accepted-risk record {#62-checklist-por-registo-de-risco-aceite}

- [ ] Unique identifier of the record
- [ ] Type of risk (control not applied / finding / threat / architectural exception / dependency)
- [ ] Technical description of the risk and its origin
- [ ] Assessed severity (Critical / High / Medium / Low)
- [ ] Evidence of the existing controls that reduce the risk
- [ ] Compensating mitigation defined and active
- [ ] Technical and business justification for the acceptance
- [ ] Start date of the acceptance
- [ ] Expiry date (sunset)
- [ ] Risk owner (responsible for follow-up)
- [ ] Formal approval (name, role, date)
- [ ] Scheduled reassessment date

---

## 7. Approval authorities {#7-alçadas-de-aprovação}

| Severity | L1 | L2 | L3 |
|---|---|---|---|
| Low | Tech Lead | AppSec Engineer | AppSec Engineer |
| Medium | AppSec Engineer | AppSec Engineer | AppSec Engineer + GRC |
| High | AppSec Engineer | AppSec Engineer + Management | CISO |
| Critical | Not recommended - remediation plan mandatory | Not acceptable without CISO | Not acceptable |

---

## 8. Reassessment and expiry {#8-reavaliação-e-expiração}

Every accepted-risk record has an **expiry date**. On the expiry date, the team must:

1. **Reassess the risk** - has the context changed? Is the compensating mitigation still effective?
2. **Decide**: fix / renew the acceptance / escalate
3. **Renew with new approval** if the acceptance is maintained - no automatic renewal
4. **Record the decision** with a new expiry date and updated approval

Expired records without a documented reassessment are treated as **unmanaged risk** and must be escalated to AppSec.

---

## 9. Integration with the development lifecycle {#9-integração-com-o-ciclo-de-desenvolvimento}

| Moment | Expected action |
|---|---|
| Release / go-live | Check all active accepted risks; confirm that they are within their deadline and approved |
| Sprint review | Review the status of accepted risks with associated findings |
| Risk classification review | Review whether the accepted risks remain compatible with the level |
| Security incident | Check whether any accepted risk contributed to the incident; force immediate reassessment |

---

## 10. Artefacts {#10-artefactos}

| Artefact | Suggested location | Retention |
|---|---|---|
| Accepted-risk record | `docs/security/risk-acceptance/` or GRC platform | 2 years after expiry |
| Evidence of compensating mitigation | Attached to the record | While the risk is active |
| Formal approvals | Attached to the record (PR, issue, signed document) | 2 years after expiry |

---

## 11. Responsibilities {#11-responsabilidades}

| Role | Responsibility |
|---|---|
| Developer / Tech Lead | Identify and report residual risks; initiate the acceptance process |
| AppSec Engineer | Assess, validate and approve acceptances; monitor active records |
| GRC / Compliance | Ensure the traceability and compliance of the register; issue periodic reports |
| CISO | Approve high-risk acceptances; oversee the residual risk management programme |
| Product Management | Take part in acceptance decisions with a business impact |

---

## 12. Review and audit of this policy {#12-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Security incident originating in a previously accepted risk
- Change to the organisation's risk tolerance thresholds
- Regulatory change with an impact on the acceptance criteria

The register of accepted risks must be made available in full in internal and external security audits.

---

## 13. Normative and technical references {#13-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 01 - Application Classification | Risk acceptance criteria by level |
| SbD-ToE Ch. 03 - Threat Modelling | Formal justification of accepted risk in threats |
| SbD-ToE Ch. 10 - Security Testing | Risk acceptance for test findings |
| SbD-ToE Ch. 14 - Governance and Contracting | Formal exception process with approval authorities |
| ISO/IEC 27001 - Clause 6.1.3 | Information security risk treatment |
| NIST SP 800-30 | Guide for Conducting Risk Assessments |
| SSDF PW.4 | Software review for risk management |
