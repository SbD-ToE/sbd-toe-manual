---
id: policy-irp
title: IRP (Incident Response Plan) Integration Policy
description: Organisational policy that defines the requirements for integration between security monitoring and the incident response process (IRP), including activation criteria, mandatory playbooks, response phases, regulatory notification, post-mortem and periodic testing, proportional to the criticality level (L1, L2, L3).
tags: [policy, IRP, incident response, playbook, SOAR, contenção, notificação, post-mortem, cap12, L1, L2, L3, governance, DORA]
grupo: operacoes
sidebar_position: 32
translation:
  source_locale: pt
  source_path: 020-assets/policies/32_policy-irp.md
  source_sha256: 2aea934bd2fedbcbe331e39f00e83e3ead56b3b2a6e55ef7568a6ed08ef7440d
  source_commit: 7374046ddbdd39c675f87192be9d72abc31356ae
  target_sha256: b4ba80ac10c3398524c94f07cd45c6eab85b3343bb20d19d8b4b50d94f1b8d5a
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, cra_actively_exploited_vulnerability, cra_pde, dora_financial_entity, dora_major_ict_incident, gdpr_personal_data_breach, lifecycle_phase, nis2_essential_entity, nis2_significant_incident, role_tech_lead, sbdtoe_sbd, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 471c1bbbd1f708cb6d3e1bdf796065d2ca7f828b8dd21e4226df3789b003b6e3
  translated_at: 2026-09-27T00:04:46Z
  stamped_at: 2026-09-27T00:04:46Z
  reviewed_by: null
---

# IRP Integration Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for the **integration between the security monitoring systems and the organisation's formal incident response process (IRP)**.

The detection of a security incident only has operational value when it leads to a structured response. Alerts without associated playbooks become ad-hoc decisions under pressure - precisely when the most important decisions need to be the fastest and most correct. The IRP turns detection into response: it defines who does what, in what order, with what authority and with what evidence.

The objective of this policy is to ensure that:

- Each security alert category has an associated response playbook
- IRP activation is judicious, proportional and auditable
- The containment, eradication and recovery phases are executed in an orderly manner
- Regulatory notification is made within the applicable deadlines
- A post-mortem is carried out after each significant incident
- The playbooks and the IRP itself are tested periodically

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

| Level | Applicability |
|---|---|
| L1 | Recommended; documented response process; escalation contacts defined |
| L2 | Mandatory; playbooks defined; integration with the incident management system; post-mortem |
| L3 | Mandatory; automated playbooks (SOAR); regulatory notification; half-yearly tests; war room |

---

## 3. IRP activation criteria {#3-critérios-de-activação-do-irp}

The IRP is formally activated when a security alert or event is confirmed as an incident. The activation criteria include:

| Category | Examples | Activation |
|---|---|---|
| Credential compromise | Production credential exposed, unauthorised access confirmed | Immediate |
| Data exfiltration | Anomalous data download confirmed, PII exposed | Immediate |
| Ransomware / malware | Encrypted files, suspicious binary running | Immediate |
| Availability | Prolonged unavailability with a suspected security cause | After 15 minutes of impact |
| High-severity security anomaly | Suspicious behavioural pattern confirmed by the SIEM | After positive triage |
| Critical vulnerability in production | Critical CVE with an active exploit on an exposed system | Preventive activation |

An unconfirmed alert does not formally activate the IRP - it activates the triage phase. Formal activation occurs after confirmation.

---

## 4. Incident response phases {#4-fases-de-resposta-a-incidentes}

### 4.1 Triage (T0 - ≤ 15 minutes from detection) {#41-triagem-t0----15-minutos-de-detecção}

- [ ] Alert classified: true positive or false positive
- [ ] Severity assigned (P1/P2/P3)
- [ ] Person responsible for the incident designated (Incident Commander)
- [ ] Incident communication channel opened (war room if P1)

### 4.2 Containment (T1 - immediate start after confirmation) {#42-contenção-t1---início-imediato-após-confirmação}

- [ ] Immediate containment actions executed (system isolation, credential revocation, IP blocking)
- [ ] Containment documented with timestamp and the identity of the executor
- [ ] No destruction of evidence during containment (preserve first, contain second when possible)
- [ ] Internal communication to the Tech Lead, AppSec Engineer and GRC

### 4.3 Investigation {#43-investigação}

- [ ] Collection of relevant logs, traces and evidence
- [ ] Incident timeline reconstructed
- [ ] Root cause identified or working hypothesis documented
- [ ] Scope of the impact determined (affected systems, data, users)

### 4.4 Eradication {#44-erradicação}

- [ ] Root cause eliminated (patch, access revocation, malware removal)
- [ ] Affected systems rebuilt from scratch when persistence is suspected
- [ ] Verification that the entry vector has been closed

### 4.5 Recovery {#45-recuperação}

- [ ] Systems restored with clean and verified versions
- [ ] Reinforced monitoring in the post-recovery period
- [ ] Confirmation of a normal operating state

### 4.6 Post-mortem {#46-post-mortem}

- [ ] Held within a maximum of 5 working days after resolution
- [ ] Participation of all the functions involved
- [ ] Root cause analysis (5 Whys or equivalent)
- [ ] Corrective action plan with owner and deadline
- [ ] Document archived and lessons learned shared internally

---

## 5. Response playbooks {#5-playbooks-de-resposta}

Each incident category must have a playbook that details the specific actions per phase:

| Incident category | Mandatory playbook |
|---|---|
| Compromised credential | Revocation, rotation, audit of access during the exposure period |
| Data / PII exfiltration | Containment, scope analysis, regulatory notification |
| Ransomware | Isolation, forensics, recovery from backup |
| Critical vulnerability in production | Emergency patching, temporary containment, communication |
| Deploy of malicious code | Rollback, analysis of the pipeline, revocation of CI credentials |
| Dependency compromise (supply chain) | Identification of scope, removal, rebuild |

At L3, playbooks must be integrated with SOAR to automate immediate containment actions (e.g. IP blocking, token revocation, pod isolation).

---

## 6. Regulatory notification {#6-notificação-regulatória}

Some incidents require notification to regulatory authorities within defined deadlines:

| Regulation | Type of incident | Deadline |
|---|---|---|
| GDPR - Art. 33 | Personal data breach | ≤ 72 hours after becoming aware |
| DORA - Art. 19 + Delegated Regulation (EU) 2025/301, Art. 5 | Major ICT-related incident (financial entity) | Initial notification ≤ 4 h after classification as major and ≤ 24 h after becoming aware; intermediate report ≤ 72 h after the initial notification; final report ≤ 1 month after the latest intermediate report |
| NIS2 - Art. 23 | Significant incident in an essential/important entity | ≤ 24 hours (early warning) + 72 hours (notification) |
| CRA - Art. 14 (applicable since 11.9.2026) | Actively exploited vulnerability or severe incident in a product with digital elements placed on the market by the organisation | To the CSIRT designated as coordinator and to ENISA, via the single reporting platform: early warning ≤ 24 h; notification ≤ 72 h; final report ≤ 14 days after the corrective measure (vulnerability) or ≤ 1 month after the notification (severe incident) |

:::warning
The determination of whether an incident is notifiable must be made by GRC/Compliance with the support of the Data Protection Officer (DPO) where applicable. The time limit starts to run from the moment the organisation becomes aware of the incident - not when the root cause is identified. Under DORA, the 4 h time limit runs from the classification of the incident as major (with a limit of 24 h from awareness) and the 72 h time limit runs from the initial notification (Delegated Regulation (EU) 2025/301, Art. 5).
:::

---

## 7. Communication during the incident {#7-comunicação-durante-o-incidente}

- [ ] Channel dedicated to the incident (without noise from other channels)
- [ ] Incident Commander responsible for internal and external communication
- [ ] Regular updates to management in P1 incidents (e.g. every 30 minutes)
- [ ] Communication to affected users where applicable - honest and without compromising the investigation
- [ ] No unauthorised public communication by members of the technical team

---

## 8. Periodic IRP testing {#8-testes-periódicos-do-irp}

| Level | Cadence | Type of test |
|---|---|---|
| L1 | Annual | Tabletop review (scenario discussion) |
| L2 | Half-yearly | Tabletop + playbook simulation |
| L3 | Half-yearly | War room with active simulation; validation of escalation and notification |

Test results must be documented, and the gaps identified must result in corrective actions with a defined deadline.

---

## 9. Responsibilities {#9-responsabilidades}

| Role | Responsibility |
|---|---|
| AppSec Engineer | Maintain playbooks; coordinate the technical response; ensure preservation of evidence |
| Incident Commander (senior on-call) | Coordinate the incident; manage communication; take containment decisions |
| DevOps / SRE | Execute technical containment and recovery actions |
| GRC / Compliance | Determine notification obligations; contact regulatory authorities; manage the post-mortem |
| Management / CISO | Be notified of P1s; authorise external communications; approve public statements |

---

## 10. Review and audit of this policy {#10-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- A real incident that revealed gaps in the IRP
- A regulatory change that modifies notification deadlines or requirements
- A test result that identifies failures in the response process

---

## 11. Normative and technical references {#11-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 12 - Monitoring and Operations | US-04: integration with the IRP; playbooks; automation |
| Security Monitoring Policy (`30_policy-monitorizacao-seguranca.md`) | Incident detection |
| Alert Management Policy (`31_policy-gestao-alertas.md`) | IRP activation by alert |
| NIST SP 800-61 rev.2 | Computer Security Incident Handling Guide |
| ISO/IEC 27035 | Information Security Incident Management |
| GDPR - Art. 33-34 | Notification of personal data breaches |
| DORA - Art. 17-20 | ICT incident management and reporting |
| NIS2 - Art. 23 | Incident notification obligations |
| MITRE ATT&CK | Tactics and techniques for incident investigation |
