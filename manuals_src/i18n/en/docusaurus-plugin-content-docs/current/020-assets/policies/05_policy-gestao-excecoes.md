---
id: policy-gestao-excecoes
title: Security Exception Management Policy
description: Cross-cutting organisational policy that defines the formal process for the submission, assessment, approval, recording and reassessment of exceptions to mandatory security controls, with approval authorities proportional to the application's risk level. It applies to all SbD-ToE chapters in which there are controls with formal mandatory status.
tags: [policy, exceções, gestão de exceções, aprovação, alçadas, TTL, mitigação compensatória, cap01, cap02, cap05, cap06, cap07, cap14, L1, L2, L3, governance, transversal]
grupo: risco
sidebar_position: 5
translation:
  source_locale: pt
  source_path: 020-assets/policies/05_policy-gestao-excecoes.md
  source_sha256: b9adf494a568662f0823bb2c74746b9632b92b3279069ace506b28852b1a4a13
  source_commit: 036d74010f423f247be988e4a417375c74edb9d9
  target_sha256: 2db99a05272685ac724d0909d44df169ee529c3ff9dda4062e4c263883360f9b
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [alcada, avaliacao, cycle_iteration, mcp_reading_programa, practitioner_manual, programme_line, requirement_runtime, risk_level, role_tech_lead, sbdtoe_sbd, transversal, validation_evaluation]
  glossary_sha256: a5302cbd5b98385fac17cd6ac1b703a0b26bf260a6ba51d8206b8655aee9bdad
  translated_at: 2026-09-27T07:54:09Z
  stamped_at: 2026-09-27T07:54:09Z
  reviewed_by: null
---

# Security Exception Management Policy

## 1. Objective {#1-objetivo}

This policy defines the formal, cross-cutting process for managing **exceptions to mandatory security controls** defined in the SbD-ToE model.

An exception occurs whenever a control that is mandatory for the application's criticality level **cannot be applied** within the expected timeframe, or when there is a deliberate and justified deviation from a security practice or requirement.

Exceptions are inevitable in any mature security programme. The problem is not the exception itself - it is the **informal, unrecorded exception, with no deadline and no mitigation**. Unmanaged exceptions become permanent risk debt and are frequently the vector for security incidents.

This policy is **cross-cutting** - it applies to all domains and chapters of the SbD-ToE Manual in which there are controls with formal mandatory status.

---

## 2. Scope {#2-âmbito}

This policy applies to the whole organisation and covers exceptions arising in any of the following contexts:

| Context | Examples |
|---|---|
| Requirement controls not applied | Mandatory requirement for the level not implemented (Ch. 02) |
| Dependencies with active CVEs | Vulnerability with no fix available or with an impact assessed as acceptable (Ch. 05) |
| Insecure code patterns kept | Anti-pattern kept because of a technical constraint (Ch. 06) |
| CI/CD gates bypassed | Override of a security gate without formal approval (Ch. 07) |
| Unfixed test findings | Vulnerability identified by SAST/DAST/fuzzing without remediation within the SLA (Ch. 10) |
| Architectural exceptions | Insecure pattern kept by business or technical decision (Ch. 04) |
| IaC or container exceptions | Configuration not compliant with the security baseline (Ch. 08, Ch. 09) |
| Deploy controls not applied | Gate or validation not executed before promotion (Ch. 11) |

---

## 3. Fundamental principles {#3-princípios-fundamentais}

- **Every exception is temporary** - there is no permanent exception; every exception has an expiry date
- **Every exception is documented** - without a formal record, there is no exception; there is non-compliance
- **Every exception has an owner** - someone is explicitly responsible for follow-up
- **Every exception has a mitigation** - where technically feasible, there is an active compensating control during the exception period
- **Approval is proportional to risk** - the approval authority scales with the criticality level and the severity of the control under exception

---

## 4. Types of exception {#4-tipos-de-exceção}

| Type | Description |
|---|---|
| **Technical exception** | Technical control that cannot be implemented within the deadline; dependency with an active vulnerability |
| **Process exception** | Mandatory step of the security process not executed (e.g. gate bypassed) |
| **Architectural exception** | Design decision that does not meet the defined secure architecture standards |
| **Regulatory exception** | Deviation from a requirement with normative compliance implications |

---

## 5. Formal exception process {#5-processo-formal-de-exceção}

### 5.1 Mandatory steps {#51-passos-obrigatórios}

1. **Identify the control under exception** - which requirement, control or practice is not being met
2. **Justify technically** - why the control cannot be applied (technical constraint, external dependency, deadline, implementation cost)
3. **Assess the impact** - what additional risk the exception introduces in the context of the application
4. **Define a compensating mitigation** - which alternative control remains active during the exception period
5. **Define the expiry deadline (TTL)** - the date until which the exception is valid; there is no automatic renewal
6. **Submit for approval** - to the approval authority appropriate to the risk level (see section 6)
7. **Record formally** - in the application's exception repository or GRC platform
8. **Communicate** - to the Security Champion and the responsible team

### 5.2 Checklist per exception record {#52-checklist-por-registo-de-exceção}

- [ ] Unique identifier of the exception
- [ ] Control under exception (requirement ID or SbD-ToE control ID, where applicable)
- [ ] Type of exception (technical / process / architectural / regulatory)
- [ ] Technical description of the deviation and its origin
- [ ] Severity of the risk introduced by the exception (Critical / High / Medium / Low)
- [ ] Technical and business justification
- [ ] Compensating mitigation defined and verifiable
- [ ] Exception owner (responsible for follow-up)
- [ ] Start date of the exception
- [ ] Expiry date (TTL)
- [ ] Formal approval (name, role, date)
- [ ] Scheduled reassessment date

---

## 6. Approval authorities by level and severity {#6-alçadas-de-aprovação-por-nível-e-severidade}

| Severity of the risk introduced | L1 | L2 | L3 |
|---|---|---|---|
| Low | Tech Lead | AppSec Engineer | AppSec Engineer |
| Medium | AppSec Engineer | AppSec Engineer | AppSec Engineer + GRC |
| High | AppSec Engineer | AppSec Engineer + Product Management | CISO |
| Critical | Not recommended | CISO | Not acceptable as an exception |

:::warning
Exceptions to controls with a **Critical** risk impact are not acceptable at L3. At L2, they require CISO approval and an active remediation plan with a maximum period of 7 days. Accepting Critical risk is always a last-resort measure.
:::

---

## 7. Maximum validity periods (TTL) {#7-prazos-máximos-de-validade-ttl}

| Level | Severity | Maximum TTL |
|---|---|---|
| L1 | Low / Medium / High | 90 days |
| L2 | Low / Medium | 60 days |
| L2 | High | 30 days |
| L3 | Low / Medium | 30 days |
| L3 | High | 14 days |
| L1 | Critical | 7 days (with a mandatory remediation plan) |
| L2 | Critical | 7 days (CISO approval and remediation plan mandatory) |
| L3 | Critical | Not acceptable |

This table is the master for exception validity periods: Policies 03 and 12 and the chapters refer to it, and 90 days is the absolute ceiling. Revalidation takes place on the expiry date, with an alert to the owner 15 days before (or at the midpoint of the TTL, if it is shorter than 30 days).

Renewing an exception requires **new explicit approval** with a documented reassessment. Renewal by default or by timeout is not valid.

---

## 8. Reassessment and closure {#8-reavaliação-e-encerramento}

Each exception must be reassessed on its expiry date. The responsible team must:

1. **Reassess the risk** - has the context changed? Is the compensating mitigation still effective?
2. **Check whether the control can now be applied**
3. **Decide**: close (control applied) / renew (new approval) / escalate

Expired exceptions without reassessment are treated as **active non-compliance** and must be escalated to an AppSec Engineer.

The reassessment cycle follows the minimum cadence:

| Level | Reassessment cadence |
|---|---|
| L1 | On the expiry date |
| L2 | Half-yearly or on the expiry date, whichever comes first |
| L3 | Quarterly or on the expiry date, whichever comes first |

---

## 9. Integration with the development lifecycle {#9-integração-com-o-ciclo-de-desenvolvimento}

| Moment | Expected action |
|---|---|
| Release / go-live | Check all active exceptions; confirm that they are within their TTL and have an active mitigation |
| Sprint review (L3) | Review the status of the exceptions associated with the application |
| Risk classification review | Check whether active exceptions remain compatible with the level |
| Security incident | Check whether any active exception contributed to the incident; force immediate reassessment |
| Audit | Make available the complete register of active and historical exceptions |

---

## 10. Bypass of controls without a formal record {#10-bypass-de-controlos-sem-registo-formal}

Bypassing a mandatory security control **without a formal exception record** is treated as:

- Non-compliance with this policy
- Mandatory escalation to an AppSec Engineer
- Recording in the GRC system as an unauthorised deviation
- In regulated contexts (L3), potential non-compliance with normative obligations

The CI/CD pipeline and the release processes must, wherever possible, technically prevent gates from being bypassed without a formal record.

---

## 11. Artefacts {#11-artefactos}

| Artefact | Suggested location | Retention |
|---|---|---|
| Exception record | `docs/security/exceptions/` or GRC platform | 1 year (L1), 2 years (L2), 3 years (L3) after closure |
| Evidence of compensating mitigation | Attached to the record | While the exception is active |
| Formal approvals | Attached to the record | 1 year (L1), 2 years (L2), 3 years (L3) after closure |
| Report of active exceptions | GRC / compliance dashboard | Continuously updated |

---

## 12. Responsibilities {#12-responsabilidades}

| Role | Responsibility |
|---|---|
| Developer / Tech Lead | Identify and report the need for an exception; initiate the process |
| Security Champion | First point of contact for exceptions in the team; check the completeness of the record |
| AppSec Engineer | Assess, approve and monitor exceptions; ensure effective mitigation |
| GRC / Compliance | Maintain the centralised register; issue periodic reports; alert on upcoming TTLs |
| CISO | Approve high-risk exceptions; oversee the exception management programme |
| Product Management | Take part in decisions with a business impact; sign off exceptions that involve delivery trade-offs |

---

## 13. Review and audit of this policy {#13-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Security incident originating in a poorly managed or unrecorded exception
- Change to the organisation's risk tolerance thresholds
- Regulatory change with an impact on the exception management requirements

The exception register must be made available in full in internal and external audits.

---

## 14. Normative and technical references {#14-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 01 - Application Classification | Proportionality of exceptions by level |
| SbD-ToE Ch. 02 - Security Requirements | Exceptions to requirements with a short TTL at L3 |
| SbD-ToE Ch. 05 - Dependencies, SBOM and SCA | Policy on exceptions to CVEs |
| SbD-ToE Ch. 06 - Secure Development | Management of technical exceptions |
| SbD-ToE Ch. 07 - Secure CI/CD | Exceptions and controlled bypass of gates |
| SbD-ToE Ch. 14 - Governance and Contracting | Formal exception process with approval authorities by level |
| ISO/IEC 27001 - Clause 6.1.3 | Risk treatment - acceptance option |
| NIST SP 800-53 - CA-7 | Continuous monitoring and management of deviations |
| SSDF PW.4 | Software review for risk management |
