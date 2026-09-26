---
id: checklist-revisao
title: Checklist - Monitoring and Operations
sidebar_label: Review Checklist
sidebar_position: 20
description: Binary control checklist of the adoption of monitoring, alerting, incident response and continuous operational health signal practices.
tags: [checklist, controlo, validacao, monitorizacao, deteccao, resposta, health, readiness, disponibilidade]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/canon/20-checklist-revisao.md
  source_sha256: 932e1f55583713428db7786a470e2e365297b39262209dacc6630d32416043c6
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 6e3439e4479ae58ea48292cdd72bf12b9a9cb24534f6d15703fbe7c0de164297
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: ebb6c6bf48bf281085379aa982dcfe014d642265f07b08070d51366e58764173
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, instrument, lifecycle_phase, maturity, piso_limiar, piso_relacao, risk_level, sbdtoe_sbd, schema, traceability, verification_taxonomy]
  glossary_sha256: fac54ac8d7ec78480d41bc0538dce771685bac18b176a3949a0adfc812ec4e91
  translated_at: 2026-09-26T11:17:35Z
  reviewed_by: null
---


# Review Checklist - Chapter 12: Monitoring and Operations

This checklist applies to all applications that require the capability for **structured logging, automatic alerts, event correlation, operational health signals and incident response**.
It serves as an instrument of binary and auditable verification of the **practical adoption of the prescriptions of Chapter 12** (`OPS-001` to `OPS-015`), enabling:

- Continuous control of the proportional application of monitoring practices;
- Systematic verification per project or application;
- Generation of operational and organisational maturity indicators.

> 🗓️ **Its execution is recommended per release, on changes to the monitored domains or after relevant incidents.**

---

## 📋 Verification Items {#-itens-de-verificação}

| Item                                                                                                            | Verified? |
|-----------------------------------------------------------------------------------------------------------------|-------------|
| Do all components in production emit structured logs (JSON/CEF/ECS) persisted outside the instance, with the minimum fields normalised and no sensitive data in the clear? (`OPS-001`) | ☐           |
| Is there a catalogue of critical security events per application, with evidence that they are generated and retained, and are the monitoring domains mapped? (`OPS-002`) | ☐           |
| Is the integrity of the logs protected (WORM retention, restricted and audited access, signature/hash, isolated logging function)? | ☐           |
| Is there a log retention policy by type and regulatory context, with the minimum retention met and auditable archiving/purging? (`OPS-003`) | ☐           |
| Are the logs centralised in a SIEM with verifiable ingestion, TLS+authentication transport, buffering in the forwarder and detection/alerting of ingestion failures? (`OPS-004`) | ☐           |
| Are events normalised to a common schema with tagging by application/environment and UTC timestamps synchronised via NTP? | ☐           |
| Are there automatic alert rules for the critical events, with documented thresholds, tested before activation? (`OPS-005`) | ☐           |
| Are false positives documented with their cause and the conditions reviewed periodically, and does each critical alert have an associated runbook? | ☐           |
| Is there an alert response SLA (time-to-acknowledge and time-to-resolve) defined by severity? (`OPS-006`) | ☐           |
| Is there integration with the incident management process (IRP/SOAR), with evidence of playbook activation in an incident or exercise? (`OPS-007`) | ☐           |
| Are alerts correlated across multiple sources by active rules in the SIEM, with behavioural detection and a baseline for the critical sources? (`OPS-008`/`OPS-009`) | ☐           |
| Do the detection rules declare the MITRE ATT&CK techniques they cover, with the ATT&CK version in use recorded? | ☐           |
| Are the MTTD and MTTR metrics measured and reported, with up-to-date dashboards and evidence of continuous improvement? (`OPS-010`) | ☐           |
| Does remediation prioritisation apply EPSS and KEV on top of the SLAs by severity, keeping the SLA by severity as the floor? | ☐           |
| Are the controls adjusted to the risk level (L1–L3) with traceability, and do exceptions to monitoring have a justification, an end date and a compensating visibility control? | ☐           |
| Do irreversible actions (log purge, alert deactivation, baseline changes) require human approval, and does the alert kill-switch have a time limit, mandatory notification and an RCA before reactivation? | ☐           |
| For critical L2/L3 services, is there a service inventory with a monitored health/readiness/availability signal (health endpoint, heartbeat, readiness/liveness probe or equivalent), an actionable alert and integration with incident or rollback where applicable? (`OPS-015`) | ☐           |
| Do systems with AI/ML components record model inputs/outputs (with PII sanitisation), drift, prompt input anomalies and model/dataset versions; does each agent tool invocation (A1+) generate a structured audit event in the SIEM; is there a token spend budget with a kill-switch; and is there jailbreak/off-policy detection for A2+? (`OPS-011` to `OPS-014`) | ☐           |
| Are the practices integrated into the lifecycle (pipeline, PR, release)? | ☐           |

---

## 🔄 Operational Integration {#-integração-operacional}

- This checklist may be used in **technical audits, release gates or security reviews**;
- Each affirmative answer must be supported by **objective evidence**: rules, dashboards, tickets, configs, test captures;
- Proportionality must follow the [risk-based control matrix](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/matriz-controles-por-risco).

> ⚠️ **Negative answers require a formal, approved and justified exception.**

---

## 📊 Compliance and Governance {#-conformidade-e-governação}

- This instrument validates **compliance with Chapter 12 - Monitoring and Operations**;
- It may be integrated into **regular review cycles or as an organisational KPI**;
- The evolution of the metrics (e.g. % with tested alerts, log coverage, average MTTD) reflects the **team's maturity**.

> 📅 This checklist is an integral part of the SbD-ToE canonical control model, and supports evidence-based governance.
