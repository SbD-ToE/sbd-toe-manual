---
id: catalogo-requisitos-operacoes
title: Monitoring and Operations Requirements Catalogue
description: Canonical catalogue of requirements for the security monitoring and operations programme (OPS-001 to OPS-015), with applicability by risk level and acceptance criteria for centralised logging, critical events, retention, SIEM, alerts, response SLA, correlation, integration with the IRP, behavioural detection, effectiveness metrics and continuous operational health signals.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:operacoes, OPS, monitorizacao, SIEM, alertas, IRP, correlacao, MTTD, MTTR, health, readiness, liveness, disponibilidade, rastreabilidade, L1, L2, L3, auditoria]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/addon/00-catalogo-requisitos.md
  source_sha256: abdf627252d0d11989a2e5841395ac6676493c1b3ad738b8a327be4897f2706b
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 312173f17eceb6446b330707d56c9a02723074b45082bf428672a0a26bf5ae2d
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: ebb6c6bf48bf281085379aa982dcfe014d642265f07b08070d51366e58764173
  glossary_keys: [audit_trail, cycle_iteration, framework_source_corpus, mapping, maturity, mcp, plain_rag, programme_line, requirement_runtime, risk_level, sbdtoe_sbd, traceability]
  glossary_sha256: 60dfbb1b8bebf1aa375a1d90f59bc40f71723b4b0ee58dfe97ce1501f43d4d12
  translated_at: 2026-09-26T11:17:24Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Monitoring and Operations Requirements Catalogue

## Scope: the monitoring programme as an operational control {#âmbito-o-programa-de-monitorização-como-controlo-operacional}

This catalogue covers **requirements of the security monitoring and operations programme** - the controls that guarantee continuous visibility over the security state in production, the capacity to detect anomalous events and integration with formal incident response processes.

It is important to distinguish this catalogue from the `LOG-` domain of Ch. 02: `LOG-` defines the **properties of logging as a software requirement** (what the application must record, how to protect log integrity); `OPS-` defines the **controls of the operational programme** that receives, processes, correlates and acts on those logs - SIEM, alerts, IRP, metrics. Both are necessary and complementary.

For the complete mapping of all SbD-ToE requirements catalogues by technical domain, canonical prefix and owner, see [Ch. 02 - Catalogue Mapping](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

The scope includes: centralisation and persistence of logs in production, definition of critical security events, retention in accordance with policy and regulatory requirements, integration with SIEM, automatic alerts with thresholds and a response SLA, correlation of events across sources, integration with the incident response process, behavioural detection, continuous operational health/readiness signals and measurement of operational effectiveness.

> **On curation:** Consolidated from NIST SP 800-137 (Continuous Monitoring), NIST SP 800-61 (Incident Response), CIS Controls v8 (Controls 8, 13, 17), MITRE ATT&CK (Detection coverage), DORA (Art. 10, operational monitoring) and good practice of the modern SOC. It must be adapted to the monitoring platform context in use and reviewed with each operational security maturity cycle.

For instantiation in a project and operational naming (`SEC-Lx-OPS-CODIGO`), see [Taxonomy and Traceability](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Conventions {#convenções}

| Symbol | Meaning |
|---------|-------------|
| ✔ | Requirement mandatory at this level |
| - | Not applicable or not mandatory at this level |

Levels are cumulative: L3 includes all L1 and L2 requirements; L2 includes all L1 requirements.

---

## OPS Catalogue - Monitoring and Operations {#catálogo-ops---monitorização-e-operações}

Requirements ensuring that the organisation has effective operational visibility over its systems in production, with detection, correlation and response capacity proportional to the risk.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| OPS-001 | Structured and persistent logging for all components in production | ✔ | ✔ | ✔ | Logs of all components in production in a structured format (JSON, CEF or equivalent); persisted outside the instance (not only locally); accessible without direct access to the host; coverage verifiable by inventory. |
| OPS-002 | Catalogue of critical security events defined and verified | ✔ | ✔ | ✔ | Catalogue of critical events defined per application (authentication, permission changes, authorisation errors, access to sensitive data, etc.); evidence that those events are effectively generated and retained; reviewed with each significant release. |
| OPS-003 | Log retention in accordance with policy and regulatory requirements | - | ✔ | ✔ | Retention policy documented per log type and applicable regulatory context; logs retained for the minimum mandatory period; archiving and purge process documented and auditable; evidence of compliance available. |
| OPS-004 | Centralisation of logs in a SIEM system or equivalent | - | ✔ | ✔ | Logs sent to a centralised monitoring system with verifiable ingestion; no exclusive dependence on local logs for security analysis; evidence of logs received per source; forwarding failures detected and alerted. |
| OPS-005 | Automatic alerts for critical security events | - | ✔ | ✔ | Alerts configured for the critical events defined in OPS-002; thresholds documented and reviewed periodically; notification channel tested; alerts not silenced without justification. |
| OPS-006 | Alert response SLA defined and measured | - | ✔ | ✔ | Response SLA (time-to-acknowledge and time-to-resolve) defined per alert severity; MTTD and MTTR metrics collected and reported periodically; deviations from the SLA documented and handled. |
| OPS-007 | Integration with a formal incident response process | - | ✔ | ✔ | Response runbooks or playbooks defined for critical alert types; integration between the alerting system and the incident management system; evidence of activation in a real incident or documented exercise in the last cycle. |
| OPS-008 | Correlation of events across multiple sources | - | - | ✔ | Correlation rules active in the SIEM for distributed events (e.g. access + suspicious change correlated by session ID, IP or user ID); dashboards or queries that aggregate correlated events available; rules documented and maintained. |
| OPS-009 | Behavioural detection and baseline of normal activity | - | - | ✔ | Behaviour-based detection mechanisms (UEBA, activity baselines) active for critical sources; behavioural anomalies generate actionable alerts; baseline documented, updated periodically and with an approval process for deviations. |
| OPS-010 | Monitoring effectiveness metrics measured and reviewed | - | - | ✔ | MTTD and MTTR measured, reported and compared with previous cycles; alert coverage per event type mapped against the catalogue of relevant threats; periodic review of thresholds, rules and coverage with evidence of continuous improvement. |
| OPS-011 | Dedicated observability for AI/ML components in production | - | ✔ | ✔ | Systems with AI/ML components in production (LLMs, predictive models, RAG, autonomous agents) have dedicated telemetry: complete logging of model inputs and outputs (with PII sanitisation); logging of tool invocations in agents with agent identity, scope and context (`AML.M0024` AI Telemetry Logging); recording of behaviour drift and accuracy degradation; alerts for prompt input anomalies (potential prompt injection); complete audit trail of deployed model versions and dataset versions used in inference. Logs are integrated into the existing SIEM/observability pipeline (OPS-004); detection of AI/ML-specific anomalies (drift, prompt injection patterns, exfiltration via tool calls) is handled in OPS-009 with AI-aware baselines. |
| OPS-012 | Complete audit per AI agent *tool invocation* | - | ✔ | ✔ | For each AI agent at level A1+ (see [Ch. 02 — A0-A4](../../requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia)) in operational use, each *tool call* generates a structured *audit event* with `timestamp`, `agent_id`, `session_id`, `mandate_ref` (Policy 38), `autonomy_level`, `tool`, `tool_version`, `args` (PII redacted), `intent_event_ref` ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) at A2+), `outcome`, `external_effect`. Events integrated into the SIEM (OPS-004); divergence between the declared `intent` and the actual action generates an actionable alert; this builds the basis for auditing the `mandate_ref` and for the *post-mortem* reconstruction of any session. |
| OPS-013 | Budget and *runaway* detection in model consumption (token spend) | - | ✔ | ✔ | Per agent and per mandate, a maximum consumption *budget* per time window is defined (tokens, calls, cost); each inference counts towards the budget; on reaching the warning threshold, an alert goes to the *owner*; on reaching the maximum threshold, the session pauses or the *kill-switch* is triggered according to the autonomy level. Usage metrics reported at the cadence of the *mandate* review. Detects uncontrolled *loops*, abuse and model efficiency regressions after an *upgrade*. |
| OPS-014 | Detection of *jailbreak* / *off-policy actions* in production | - | - | ✔ | For A2+ agents, an active mechanism for detecting *jailbreak* attempts (LLM01-2025) and *off-policy actions* — actions outside the *scope* declared in the *mandate*. Signals include: divergence between the declared `intent` and the actual action (cross-link OPS-012), known adversarial patterns in the input, a *tool call* with arguments materially different from those expected, model refusals followed by a different attempt by the user. Actionable events feed IR (OPS-007) and the offline *eval suite* (Ch. 10 §C5). For L3 systems with an AI component, detection is mandatory — for A4 with a signed *mandate*, it is updated at the cadence declared in the *mandate*. |
| OPS-015 | Continuous operational health and availability signals | - | ✔ | ✔ | Critical services and applications in production expose an explicit health, readiness or availability signal, or an equivalent platform mechanism, monitored continuously outside the instance. Examples include a health endpoint, heartbeat, readiness/liveness probes, load balancer health checks or the supervisor's watchdog. Persistent failures generate an actionable alert and feed, where applicable, rollback ([`DPL-008`](/sbd-toe/sbd-manual/deploy-seguro/addon/catalogo-requisitos-deploy)) or incident response ([`OPS-007`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes)). The signal does not expose secrets, sensitive configuration or unauthorised internal diagnostics; coverage is verifiable by service inventory. |

---

## Explanatory notes {#notas-explicativas}

- **OPS-001 vs LOG- (Ch. 02)**: LOG- defines what the application must record and how to protect log integrity - these are software requirements. OPS-001 defines that those logs must be persisted and accessible in the monitoring infrastructure - it is a requirement of the operational programme. Both are necessary and complementary.
- **OPS-002**: The catalogue of critical events must be defined in collaboration with the development and AppSec teams - they are the ones who know which business events have relevant security implications. A SIEM receiving logs without a catalogue of critical events is observability without detection.
- **OPS-004**: Failure to forward logs to the SIEM must be detected and alerted - an unexpected silence from a source can be as significant as an explicit alert.
- **OPS-006**: MTTD (Mean Time to Detect) and MTTR (Mean Time to Respond/Resolve) are the operational metrics most directly relevant to security effectiveness - and they are the ones most frequently absent in monitoring programmes that are mature in technology but immature in process.
- **OPS-007**: An alert without an associated playbook is a notification that creates anxiety, not a response capability. The existence and periodic exercise of playbooks is what turns monitoring into an effective operational control.
- **OPS-009**: Behavioural detection is necessarily probabilistic and contextual - it does not detect known threats with signatures, but anomalies that deviate from established patterns. It requires active maintenance of the baselines and a contextually calibrated tolerance of false positives.
- **OPS-011**: AI/ML observability differs from traditional logging in three dimensions: (1) **input dimensionality** — prompts are arbitrarily complex free text, requiring logging with PII sanitisation and potentially differentiated retention decisions; (2) **probabilistic observability** — model outputs vary by design; the anomaly signal is not "output ≠ expected" but "output ≠ statistical baseline" (drift, accuracy degradation, confidence distribution); (3) **agentic action audit** — when the model invokes backend tools (e.g. via MCP, function calling), each invocation is an action with operational impact that must be treated as a first-order audit event, not as a sub-event of the model call. For the AI/ML architecture that originates these events, see [Ch. 04 — §AI/ML](../../arquitetura-segura/recomendacoes-avancadas#ai-ml).
- **OPS-015**: This requirement defines the continuous operational health/readiness/availability signal in production. [`DPL-008`](/sbd-toe/sbd-manual/deploy-seguro/addon/catalogo-requisitos-deploy) consumes that signal during deploys and rollback decisions; the [Post-Deployment Monitoring Policy](/sbd-toe/assets/policies/policy-monitorizacao-pos-deploy) operationalises the post-deployment window. Concrete platform patterns, such as Kubernetes probes or specific watchdogs, belong in service observability or cloud-native playbooks; the canonical requirement remains platform-neutral.

### Detailed note — OPS-012 {#ops-012}

Specialises OPS-011 for the *agentic* case. Each *tool invocation* has **three identities at stake** that matter for the record: the agent (`agent_id`), the session (`session_id`) and the *mandate* under which the agent operates (`mandate_ref`). Without all three, the *audit trail* does not allow the reconstruction of *who*, *when* and *with what authority*. In A2+ systems, the cross-check between `intent_event_ref` (declared by the agent before the action) and the actual result (`outcome`/`external_effect`) is what makes *off-policy actions* detectable in useful time — see OPS-014.
### Detailed note — OPS-013 {#ops-013}

The operational risk of LLMs in production has two faces: (a) *correctness* — covered by OPS-011 (drift, accuracy); (b) *consumption* — covered here. In agents with tool-use and multi-step *loops*, consumption can escalate exponentially in a few seconds (e.g. an agent in a *retry loop* calling 20 *tools* per iteration). Without an operational budget, the problem is discovered on the monthly invoice; with a budget, an alert fires at the moment and the *kill-switch* trips before material impact.
### Detailed note — OPS-014 {#ops-014}

This is the operational counterpart of the architectural control [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (Ch. 04). The *intent declaration* ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) creates the *evidence*; OPS-014 creates the *detection*. At A4, periodic updating of the detection corpus is mandatory because adversaries adapt to defences — it is not a *one-time setup*. The signal lands in IR (OPS-007) like any other incident.

### Detailed note — OPS-015 {#ops-015}

OPS-015 separates the continuous obligation in production from the post-deployment use of that same signal. Architecture decides which critical components must be observable; operations confirms that the signal is collected outside the instance, monitored continuously, linked to an actionable alert and covered by inventory. On platforms without an HTTP endpoint, the equivalent mechanism may be a health check by the supervisor, load balancer or managed platform, provided that it produces evidence of readiness/availability and does not expose sensitive internal detail.

---

> For monitoring domains and taxonomy, see [Monitoring Domains](./dominios-monitorizacao).
> For centralised logging, see [Centralised Logging Controls](./controles-logging-centralizado).
> For alerts and critical events, see [Alerts and Critical Events](./alertas-eventos-criticos).
> For integration with SIEM, see [SIEM Integration](./integracao-siem).
> For correlation and anomalies, see [Correlation and Anomalies](./correlacao-anomalias).
> For metrics and indicators, see [Metrics and Indicators](./metricas-indicadores).
> For the matrix of controls by risk level, see [Controls Matrix by Risk](./matriz-controles-por-risco).
