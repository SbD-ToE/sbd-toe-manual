---
id: policy-gestao-alertas
title: Alert Management Policy
description: Organisational policy that defines the requirements for the configuration, classification, response SLAs, escalation, runbooks and calibration of security and operational alerts, including the prevention of alert fatigue and quality metrics, proportional to the criticality level (L1, L2, L3).
tags: [policy, alertas, SLA, on-call, runbook, escalamento, fadiga de alertas, SIEM, cap12, L1, L2, L3, governance, operações]
grupo: operacoes
sidebar_position: 31
translation:
  source_locale: pt
  source_path: 020-assets/policies/31_policy-gestao-alertas.md
  source_sha256: 32211e5a22176118c52bc37d2cc925eb551635ecca6a9a29b7bb64bba3a69b7f
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 460512b58a77be7d50b4715feb012ab49173a7818ec899a2c9fa0577ad7f2c03
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bc04ded428e40ee1c214f8535dfb1904655b64166d0aa82b5df521e4230b8cb0
  glossary_keys: [candidate, cycle_iteration, lifecycle_phase, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: 4f4ef36a601d01a4dadb3132c6c3c8b64a0c6cc53c9f6f62b3c94f7315037157
  translated_at: 2026-09-26T14:11:02Z
  reviewed_by: null
---

# Alert Management Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for **managing the complete lifecycle of alerts** - from configuration and classification, through the response SLA and escalation, to the calibration and elimination of alerts that do not fulfil their purpose.

An alert without a response deadline is just noise. A system with hundreds of active alerts that nobody responds to is worse off than a system without alerts - it has created the illusion of monitoring without the substance. Alert fatigue is one of the most documented causes of undetected incidents: when everything alerts, nothing alerts. Effective alert management is a disciplined practice of signal/noise ratio, not of accumulating rules.

The objective of this policy is to ensure that:

- Each alert has a defined and tested response SLA
- Each alert has an associated runbook that guides the response
- Automatic escalation acts when the SLA is exceeded
- Alert quality metrics are tracked and used for calibration
- Alert fatigue is monitored and actively corrected

---

## 2. Scope {#2-âmbito}

This policy applies to all security and operational alerts configured in the organisation's monitoring systems, SIEM, APM and on-call platforms.

---

## 3. Alert classification {#3-classificação-de-alertas}

All alerts must be classified by severity, which determines the response SLA and the notification channel:

| Severity | Criterion | First-response SLA | Channel |
|---|---|---|---|
| **P1 - Critical** | Immediate impact on production or confirmed security compromise | ≤ 5 minutes | PagerDuty/OpsGenie (phone call) + Slack |
| **P2 - High** | Significant impact on production or high-severity security anomaly | ≤ 15 minutes | PagerDuty/OpsGenie + Slack |
| **P3 - Medium** | Service degradation or anomaly that requires attention but does not cause immediate impact | ≤ 60 minutes | Slack + ticket |
| **P4 - Low** | Informational event with potential for degradation if ignored | ≤ 4 hours (working hours) | Ticket |

---

## 4. Mandatory runbooks {#4-runbooks-obrigatórios}

Each configured alert must have an associated **runbook** that guides the response:

| Minimum runbook content | Description |
|---|---|
| What this alert detects | Clear description of the event or condition |
| How to verify (diagnosis) | Concrete steps to confirm whether it is a true positive |
| Normal vs anomalous context | What normal behaviour is, to distinguish it from the anomalous |
| Immediate actions | What to do in the first 5 minutes |
| Escalation | To whom to escalate and under what conditions |
| Relevant links | Dashboard, logs, incident playbook if applicable |

Runbooks without the minimum fields or not reviewed for more than 6 months are treated as out of date, and the alert is a candidate for review.

---

## 5. Automatic escalation {#5-escalonamento-automático}

When the first-response SLA is exceeded without any recorded action, the alert must be escalated automatically:

| Level | L1 | L2 | L3 |
|---|---|---|---|
| Automatic escalation on SLA exceeded | Not applicable | Mandatory (to Tech Lead) | Mandatory (to Tech Lead + AppSec/GRC) |
| Notification to a manager when a P1 persists > 30 minutes | Not applicable | Recommended | Mandatory |

The escalation chain must be documented and tested periodically (at least once every six months).

---

## 6. Prevention of alert fatigue {#6-prevenção-de-fadiga-de-alertas}

Alert fatigue is an operational risk that must be monitored and actively managed:

### 6.1 Alert quality metrics {#61-métricas-de-qualidade-de-alertas}

The following metrics must be tracked monthly:

| Metric | Description | Target |
|---|---|---|
| True positive rate (TPR) | % of P1/P2 alerts that correspond to real incidents | > 70% |
| False positive rate (FPR) | % of P1/P2 alerts that are noise | &lt; 30% |
| Mean response time | Mean time between the alert and the first recorded action | ≤ SLA per severity |
| Alerts without action in 24h | Number of P3/P4 alerts without action in 24h | &lt; 10% |
| Total alert volume per day | Indicator of systemic noise | Downward or stable trend |

### 6.2 Intervention criteria {#62-critérios-de-intervenção}

If quality metrics worsen systematically:

- [ ] Review of the thresholds of the alerts with the highest false positive rate
- [ ] Suspension of alerts with TPR < 30% until recalibration
- [ ] Aggregation of correlated alerts into a single event
- [ ] Removal of alerts that have never given rise to action in 90 days

---

## 7. P1 alerts outside working hours (on-call) {#7-alertas-p1-em-horas-não-laborais-on-call}

For L2/L3 systems, there must be an on-call rotation that guarantees 24/7 response availability for P1 alerts:

- [ ] On-call rotation documented and known to the team
- [ ] Primary on-call and secondary on-call (backup) defined for each period
- [ ] On-call tool configured with the escalation chain
- [ ] On-call compensation and limits established in accordance with the HR policy

---

## 8. Periodic review of the alert inventory {#8-revisão-periódica-do-inventário-de-alertas}

| Level | Cadence | Scope |
|---|---|---|
| L1 | Annual | Existing alerts; removal of obsolete alerts |
| L2 | Half-yearly | Existing alerts + quality metrics + runbooks |
| L3 | Quarterly | Alerts + metrics + runbooks + escalation simulation |

The review must result in:
- Removal or reworking of alerts with TPR < 30%
- Updating of out-of-date runbooks
- Addition of alerts for newly identified risks

---

## 9. Responsibilities {#9-responsabilidades}

| Role | Responsibility |
|---|---|
| DevOps / SRE | Configure and maintain alerts; manage on-call; track quality metrics |
| AppSec Engineer | Define security alerts; validate security runbooks; calibrate thresholds |
| On-Call | Respond within the SLA; record the action taken; escalate when necessary; provide feedback |
| Tech Lead | Ensure that the team has up-to-date runbooks; manage escalations received |
| GRC / Compliance | Audit SLA compliance; verify the escalation chain; reports |

---

## 10. Review and audit of this policy {#10-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- An incident in which the alert was not responded to within the SLA
- A period of documented alert fatigue (TPR < 50% for > 30 days)
- A change of on-call tool or SIEM

---

## 11. Normative and technical references {#11-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 12 - Monitoring and Operations | US-03, US-10: alerts with SLA, validation and tuning |
| Security Monitoring Policy (`30_policy-monitorizacao-seguranca.md`) | Definition of critical events to alert on |
| IRP Integration Policy (`32_policy-irp.md`) | Integration of alerts with incident response |
| PagerDuty / OpsGenie | Reference on-call and alert management tools |
| Site Reliability Engineering (Google SRE Book) | Alert Philosophy, SLO-based alerting |
| NIST SP 800-61 | Computer Security Incident Handling - detection and analysis |
