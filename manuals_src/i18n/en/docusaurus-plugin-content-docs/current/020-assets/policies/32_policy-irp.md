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
  source_sha256: f3c425d0ab4fa88640d291c540df7f622df4ad3315d8ca4c728e81669358a18c
  source_commit: 8eb6a0aba53db254727866b9715b6a7e56eb7490
  target_sha256: b1f61e5c97ac9ca3c4491cc695ce1e96c0226447e20129afa0efb08b5abdf6d3
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [audit_trail, avaliacao, cra_actively_exploited_vulnerability, cra_pde, dora_financial_entity, dora_major_ict_incident, eu_ai_deployer, eu_ai_gpai_model, eu_ai_high_risk_system, eu_ai_system, eu_ai_widespread_infringement, eu_market_surveillance_authority, eu_startups, gdpr_controller, gdpr_personal_data_breach, lifecycle_phase, nis2_early_warning, nis2_essential_entity, nis2_significant_incident, practitioner_manual, role_tech_lead, sbdtoe_sbd, threat, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: a1e4933004116abfb7355f31e91e83977a1887f4ebc300963bf37daa335e55af
  translated_at: 2026-09-27T19:34:15Z
  stamped_at: 2026-09-27T19:34:15Z
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
- A post-mortem is carried out after each incident, from L2; under DORA or NIS2, also at L1 for incidents that reach the notification threshold
- The playbooks and the IRP itself are tested periodically

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

| Level | Applicability |
|---|---|
| L1 | Recommended; documented response process; escalation contacts defined; incidents recorded |
| L2 | Mandatory; playbooks defined; integration with the incident management system; post-mortem |
| L3 | Mandatory; automated playbooks (SOAR); half-yearly tests; war room |

Regulatory notification (section 6) is mandatory whenever applicable, at any level: it depends on the incident and the entity, not on the L level.

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
- [ ] Severity assigned (P1–P4; P1 is the top of the scale)
- [ ] Person responsible for the incident designated (Incident Commander)
- [ ] Notifiability assessment: if there is an indication of a personal data breach, a significant incident (NIS2), a major ICT-related incident (DORA), an actively exploited vulnerability or severe incident (CRA) or a serious incident (AI Act), the incident follows the **regulatory track**, at any severity and at any level, and is raised to at least P2: GRC/Compliance and the DPO informed ≤ 1 h after confirmation; the moment of awareness recorded in the ticket; notifiability decision ≤ 4 h (the Manual's choice; see section 6), recorded with its rationale, also when it is negative
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
- [ ] Impact data recorded: users or clients affected, duration and period of unavailability, geographical spread, data affected (confidentiality, integrity, availability), estimated financial losses, critical services or functions affected; these are the data that the notifiability criteria of section 6.1 require

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
- [ ] Review of the affected artefacts, with a disposition recorded per artefact (reviewed or unchanged, with the reason): risk analysis and classification, threat model, access model, configurations, architecture, supplier contracts, KPIs and the IRP itself

### 4.7 Recurrence analysis {#47-análise-de-recorrência}

Incidents are also analysed together, to find patterns and recurrences (the same apparent root cause). The analysis is quarterly at L2 and monthly at L3, and recommended at L1 (the Manual's choice). Each recurrence opens a problem, with root cause and corrective actions with owner and deadline. The aggregation rules for notification purposes belong to the regimes (DORA, NIS2) and are set out in the regulatory overlay.

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
| GDPR - Art. 33(1) | Personal data breach (unless it is unlikely to result in a risk to the rights and freedoms of natural persons) | To the supervisory authority (in Portugal, the CNPD): without undue delay and, where feasible, not later than 72 hours after having become aware of it; after 72 h, accompanied by the reasons for the delay; may be provided in phases (paragraph 4) |
| GDPR - Art. 33(2) | Breach of which the processor becomes aware | To the controller, without undue delay (the contract may set a time limit in hours) |
| GDPR - Art. 34 | Breach likely to result in a high risk to the rights and freedoms of natural persons | To the data subjects, without undue delay (exceptions in paragraph 3) |
| DORA - Art. 19 + Delegated Regulation (EU) 2025/301, Art. 5 | Major ICT-related incident (financial entity) | Initial notification ≤ 4 h after classification as major and ≤ 24 h after becoming aware; intermediate report ≤ 72 h after the initial notification; final report ≤ 1 month after the latest intermediate report |
| DORA - Art. 19(3) | Major ICT-related incident with an impact on the clients' financial interests | To clients, without undue delay as soon as the entity becomes aware of it |
| NIS2 - Art. 23(4) (as transposed nationally) | Significant incident in an essential/important entity | To the CSIRT or, where applicable, the competent authority: early warning ≤ 24 h; incident notification ≤ 72 h (trust service providers: ≤ 24 h); intermediate report upon request; final report ≤ 1 month after the incident notification (if the incident is ongoing: an intermediate report at that time and a final report ≤ 1 month after it has been handled) |
| CRA - Art. 14 (applicable since 11.9.2026) | Actively exploited vulnerability or severe incident in a product with digital elements placed on the market by the organisation | To the CSIRT designated as coordinator and to ENISA, via the single reporting platform: early warning ≤ 24 h; notification ≤ 72 h; final report ≤ 14 days after the corrective measure (vulnerability) or ≤ 1 month after the notification (severe incident) |
| CRA - Art. 14(8) | Actively exploited vulnerability or severe incident | To the impacted users (and, where appropriate, all users), with the risk mitigation and corrective measures they can take |
| AI Act - Art. 73 | Serious incident involving a high-risk AI system | To the market surveillance authority of the Member State where it occurred: immediately after establishing the causal link (or its reasonable likelihood) and, at the latest, 15 days after the provider or the deployer becomes aware; 10 days in the event of death; 2 days in the event of a widespread infringement or of a serious incident under Article 3, point (49)(b); an incomplete initial report is allowed (paragraph 5) |
| AI Act - Art. 75(1a) | Serious incident involving a high-risk AI system under the competence of the AI Office (system based on a general-purpose model from the same provider) | To the AI Office, instead of the market surveillance authority, with the time limits of Art. 73 |
| AI Act - Art. 55(1)(c) | Serious incident involving a general-purpose AI model with systemic risk (provider of the model) | To the AI Office and, as appropriate, to the national competent authorities, without undue delay, with possible corrective measures |
| CSA - Art. 56(8) | Vulnerability or irregularity detected after certification that may affect the compliance of a product holding a European cybersecurity certificate | To the body that issued the certificate (or the authority that issued it) |

:::warning
The determination of whether an incident is notifiable must be made by GRC/Compliance with the support of the Data Protection Officer (DPO) where applicable. Time limits run from awareness of the incident or breach - not from identification of the root cause -, except for the steps that the law anchors to another moment: the NIS2 final report runs from the incident notification; the CRA final report for a vulnerability runs from the availability of the corrective or mitigating measure. Under DORA, the 4 h time limit runs from the classification of the incident as major (with a limit of 24 h from awareness) and the 72 h time limit runs from the initial notification (Delegated Regulation (EU) 2025/301, Art. 5).
:::

**Retention of incident records.** The timeline, the post-mortem and the notifications sent are kept for 1 year at L1 and L2 and for 3 years at L3 (the Manual's choice; see [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos)). Under DORA, the period is defined by the entity (Delegated Regulation (EU) 2024/1774, Art. 22, point (d)).

### 6.1 Criterion and minimum content per regime {#61-critério-e-conteúdo-mínimo-por-regime}

The incident record (section 4.3) collects the impact data; the notifiability criterion and the thresholds are those of each regime, which the regulatory overlay sets out in detail. The minimum content is what the law requires; it does not replace the authorities' forms.

| Regime | Criterion | Minimum content |
|---|---|---|
| GDPR - Art. 33 | Risk to the rights and freedoms of natural persons | Nature of the breach, with the categories and approximate number of data subjects and of records; contact of the DPO; likely consequences; measures taken or proposed. All breaches are documented, whether notified or not |
| DORA - Art. 19 | Major incident under Art. 18 and Delegated Regulation (EU) 2024/1772, including the aggregation of recurring incidents | Templates of Implementing Regulation (EU) 2025/302 for the initial notification, the intermediate report and the final report |
| NIS2 - Art. 23 | Significant incident (Art. 23(3)); for relevant entities, the thresholds of Arts. 3 and 4 of Implementing Regulation (EU) 2024/2690 | Early warning: suspicion of an unlawful or malicious act and cross-border impact. Notification: initial assessment, severity, impact and indicators of compromise. Final report: detailed description, severity and impact, type of threat or root cause, mitigation measures, cross-border impact |
| CRA - Art. 14 | Severe incident (Art. 14(5)): affects the availability, authenticity, integrity or confidentiality of data or functions, or introduces malicious code | Final report: detailed description, severity and impact, type of threat or root cause, mitigation measures applied and ongoing |
| AI Act - Art. 73 | Serious incident (Art. 3, point 49) | As provided for in Art. 73 |

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
