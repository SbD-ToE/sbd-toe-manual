---
id: policy-monitorizacao-seguranca
title: Security Monitoring Policy
description: Organisational policy that defines the requirements for security monitoring in production, including the definition of critical events, SIEM integration, behavioural correlation, coverage of monitoring domains and periodic review of detection rules, proportional to the criticality level (L1, L2, L3).
tags: [policy, monitorização, segurança, SIEM, correlação, detecção, anomalias, eventos críticos, cap12, L1, L2, L3, governance, SOC]
grupo: operacoes
sidebar_position: 30
translation:
  source_locale: pt
  source_path: 020-assets/policies/30_policy-monitorizacao-seguranca.md
  source_sha256: e03d74c34c107ac290b4312b6240f9219648aaa3947d26fc5b4d58cbf4188d94
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 8a7f925e99db0faa09db6ceb71f64a6cbe1b4262d681e4794f77b5e89e875453
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [framework_source_corpus, llm, requirement_runtime, risk_level, sbdtoe_sbd, threat, validation_evaluation]
  glossary_sha256: 36ddfa8729b4f13864bfaf945ad7615e7d3491e54ea8e6f62cd1fc0d7f49f9aa
  translated_at: 2026-09-26T14:11:01Z
  stamped_at: 2026-09-26T18:37:01Z
  reviewed_by: null
---

# Security Monitoring Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for the **continuous security monitoring of systems in production**, covering the definition of critical events, SIEM integration, behavioural correlation and the periodic review of detection rules.

Security monitoring turns logs into operational intelligence. Without active monitoring, ongoing attacks, credential compromises and data exfiltration can persist for weeks or months without being detected. Security monitoring is not an optional compliance feature - it is the primary mechanism for detecting incidents that were not prevented by the preceding security controls.

The objective of this policy is to ensure that:

- Critical security events are defined, covered and being monitored in production
- SIEM integration enables correlation between events from multiple sources
- Suspicious behavioural patterns are detected and generate alerts of appropriate severity
- Detection rules are validated and calibrated to minimise false positives
- Monitoring coverage is proportional to the application's criticality level

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

| Level | Applicability |
|---|---|
| L1 | Recommended; basic monitoring of health and errors |
| L2 | Mandatory; security events defined; alerts with SLA; SIEM integration recommended |
| L3 | Mandatory; complete monitoring; SIEM mandatory; behavioural correlation; quarterly review |

---

## 3. Definition of critical security events {#3-definição-de-eventos-críticos-de-segurança}

The list of critical security events to be monitored must be formally defined, approved by the AppSec Engineer and reviewed periodically. At a minimum, it must cover:

### 3.1 Authentication and access {#31-autenticação-e-acesso}

| Event | Alert trigger |
|---|---|
| Multiple authentication failures (same user or same IP) | > 5 failures in 5 minutes |
| Login from a new geographic location | First access from an unusual country/region |
| Login outside normal hours | Access outside the user's historical pattern |
| Use of a service account in an unexpected context | Access to resources outside the account's scope |
| Privilege escalation | Any role or permission change event |
| Access to resources with permission denied (403) in volume | > threshold defined per service |

### 3.2 Exfiltration and data access {#32-exfiltração-e-acesso-a-dados}

| Event | Alert trigger |
|---|---|
| Download of an anomalous volume of data | > threshold per user/session |
| Access to classified data outside the normal profile | First access or volume above the usual |
| Mass export of records | Volume above the threshold defined per operation |

### 3.3 Pipeline and infrastructure {#33-pipeline-e-infraestrutura}

| Event | Alert trigger |
|---|---|
| Deploy to production outside the change window | Any deploy outside the defined window |
| Change to security configuration | WAF, CORS, TLS, security groups |
| Access to the secrets vault outside the pattern | Reading of production secrets in a development context |
| CI/CD job with an anomaly (systematic failure, anomalous duration) | Deviation > 3σ from the baseline |

---

## 4. Monitoring domains {#4-domínios-de-monitorização}

Monitoring coverage must span the following domains, proportionally to the level:

When the technical domain includes health signals, heartbeat, readiness/liveness probes or an equivalent operational availability mechanism for critical services, the applicable canonical obligation is [`OPS-015`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-015). This policy keeps its focus on security monitoring and operational correlation.

| Domain | L1 | L2 | L3 |
|---|---|---|---|
| Technical (errors, latency, health) | Basic | Complete | Complete |
| Security (authentication, authorisation, anomalies) | Basic | Partial | Complete |
| Business (critical transactions, value flows) | Not applicable | Recommended | Mandatory |
| Compliance (auditable events, access to regulated data) | Not applicable | Recommended | Mandatory |
| CI/CD and pipeline (deploys, gates, approvals) | Recommended | Mandatory | Mandatory |

---

## 5. SIEM integration {#5-integração-com-siem}

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Forwarder configured (Filebeat, Fluentbit, Vector) | Not applicable | Mandatory | Mandatory |
| Secure transmission channel (TLS 1.2+, authentication) | Not applicable | Mandatory | Mandatory |
| Parsing and normalisation (ECS or common schema) | Not applicable | Mandatory | Mandatory |
| Enrichment with context (environment, application, classification) | Not applicable | Recommended | Mandatory |
| Correlation rules configured | Not applicable | Basic | Complete + quarterly review |
| SOAR integration (response automation) | Not applicable | Recommended | Mandatory |

---

## 6. Behavioural correlation {#6-correlação-comportamental}

At L3, the SIEM must be configured with correlation rules that detect suspicious behavioural patterns impossible to detect from an isolated event:

Examples of correlation rules:

- Successful login followed by a mass download of data within the next 10 minutes
- Authentication failures from multiple IPs for the same user (credential stuffing)
- Permission change followed by immediate access to a previously inaccessible resource
- Deploy to production followed by access to sensitive data by a new service account
- Sequence of 403 accesses → attempts with different endpoints (scanning)

Correlation rules must be:
- [ ] Documented with technical context (what they detect and why)
- [ ] Tested in staging before activation in production
- [ ] Reviewed quarterly for validity and calibration

---

## 7. Validation and tuning of detection rules {#7-validação-e-tuning-de-regras-de-detecção}

Poorly calibrated alerts cause alert fatigue - which is the functional equivalent of having no alerts. Maintaining detection rules is continuous work:

- [ ] Each alert has an associated runbook that defines what to do when it is triggered
- [ ] Periodic simulation of events that should trigger the alert (in staging)
- [ ] Alert quality metrics: true positive rate, response time, false positives
- [ ] Thresholds adjusted on the basis of historical data and on-call feedback
- [ ] Alerts not triggered in 90 days are reviewed (they may be removed or reworked)

---

## 8. Periodic coverage review {#8-revisão-periódica-de-cobertura}

| Level | Review cadence |
|---|---|
| L1 | Annual |
| L2 | Half-yearly |
| L3 | Quarterly |

The review must cover:
- [ ] Security events on the list are all being collected and reach the SIEM
- [ ] Correlation rules remain valid in the face of changes to architecture or behaviour
- [ ] New attack vectors relevant to the application are covered
- [ ] Alert thresholds calibrated to current behaviour

---

## 9. Agentic signals in production {#sinais-agentic}

When the system includes AI agents operating at level A1 or above (Policy 38), three classes of signals come within the scope of this policy — in addition to the classic signals described in sections 3 and 6. They do not replace the existing ones; they complement them for the agentic slice.

### 9.1 *Tool invocation* *audit events* {#91-audit-events-de-tool-invocation}

Each *tool* invocation by an AI agent emits a structured *audit event* with:

- `timestamp` · `agent_id` · `session_id` · `mandate_ref` (Policy 38) · `autonomy_level`
- `tool` · `tool_version` · `args` (PII redacted)
- `intent_event_ref` (mandatory at A2+; declared by the agent before the action — [`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn))
- `outcome` (success / failure / timeout / rejected_by_gate)
- `external_effect` (URL, resource, state change in an external system)

These events are integrated into the SIEM like any other *audit log* — they do not live in a separate *silo*. Operational coverage: see [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012).

### 9.2 *Token spend* / *runaway* detection {#92-token-spend--runaway-detection}

For each agent and each *mandate*, a model consumption *budget* (tokens, calls, cost) is defined per time window. Each inference counts towards the budget:

- **Warning threshold** → alert to the *owner*
- **Maximum threshold** → the session pauses or the *kill-switch* fires, depending on the autonomy level

Detects runaway *loops*, abuse, and regressions in model efficiency after an *upgrade*. Operational coverage: see [`OPS-013`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013).

### 9.3 Detection of *jailbreak* / *off-policy actions* {#93-detecção-de-jailbreak--off-policy-actions}

For A2+ agents, an active mechanism that cross-references signals to detect adversarial behaviour or behaviour outside the *mandate*:

- **Divergence between `intent` ↔ actual action** (cross-referencing 9.1) — the agent declared it would do X, and did Y
- **Known adversarial patterns** in user input (LLM01-2025 prompt injection patterns)
- **Arguments materially different from those expected** in the *tool call*
- **Refusals followed by a different retry** — a signal of multi-turn pressure

Actionable signals feed IR (section 4 of this policy + Ch. 12 US-04) and the offline *eval suite* (Ch. 10 §C5). Operational coverage: see [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014).

### 9.4 Proportionality {#94-proporcionalidade}

| Risk level | 9.1 signals | 9.2 signals | 9.3 signals |
|---|:--:|:--:|:--:|
| L1 | Recommended for A1+ | Recommended | — |
| L2 | Mandatory for A1+ | Mandatory | Recommended |
| L3 | Mandatory for A1+ | Mandatory | Mandatory (corpus updated according to the *mandate* cadence) |

### 9.5 Anti-patterns {#95-anti-padrões}

- ❌ Generic *tool invocation log* (without `agent_id`/`session_id`/`mandate_ref`) — the ability to audit the *mandate* is lost.
- ❌ *Budget* without an operational *kill-switch* — an alert without action is theatre.
- ❌ *Jailbreak* detector not kept up to date — adversaries adapt; the corpus has to evolve.
- ❌ 9.3 signals that stay only in dashboards without landing in IR — an incident is not a dashboard.

---

## 10. Responsibilities {#10-responsabilidades}

| Role | Responsibility |
|---|---|
| Developer | Ensure that the application emits the mandatory security events in the correct format |
| DevOps / SRE | Configure and maintain forwarders; manage SIEM integration; monitor the health of the event pipeline |
| AppSec Engineer | Define critical events and correlation rules; validate coverage; review and calibrate alerts |
| SOC / On-Call | Respond to alerts within the SLAs; escalate when necessary; provide feedback for calibration |
| GRC / Compliance | Audit monitoring coverage; verify retention; compliance reports |

---

## 11. Review and audit of this policy {#11-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- An incident in which monitoring did not detect the malicious activity in good time
- A significant change to the architecture that introduces new components or flows
- A change in the threat sources relevant to the organisation

---

## 12. Normative and technical references {#12-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 12 - Monitoring and Operations | US-02, US-08, US-09, US-10: events, SIEM, correlation, tuning; **US-13 — agentic telemetry** |
| SbD-ToE Ch. 12 — Catalogue ([`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012), [`OPS-013`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013), [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014)) | Agentic operational requirements |
| SbD-ToE Ch. 12 — [`OPS-015`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-015) | Continuous health/readiness/availability signals for critical services |
| SbD-ToE Ch. 04 — Secure Architecture ([`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)) | Complete audit per *tool invocation* — origin of the agentic signals |
| SbD-ToE Ch. 02 — Requirements ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) | *Intent declaration* — origin of signal 9.3 |
| Structured Logging Policy (`29_policy-logging-estruturado.md`) | Event base for monitoring |
| Policy 38 — AI Agent Mandates | `mandate_ref` in audit events |
| MITRE ATLAS | `AML.M0024` AI Telemetry Logging |
| OWASP Top 10 for LLM Applications (2025) | LLM01 Prompt Injection — detection corpus 9.3 |
| NIST AI RMF 1.0 — MANAGE-4.x | Operational review and revocation |
| Alert Management Policy (`31_policy-gestao-alertas.md`) | SLAs and alert response process |
| IRP Integration Policy (`32_policy-irp.md`) | Integration of monitoring with incident response |
| MITRE ATT&CK | Framework of tactics and techniques for defining detection rules |
| NIST SP 800-92 | Guide to Computer Security Log Management |
| NIST SP 800-137 | Information Security Continuous Monitoring |
| ISO/IEC 27001 - A.12.4 | Logging and monitoring |
| DORA - Art. 17 | ICT-related incident detection and reporting |
