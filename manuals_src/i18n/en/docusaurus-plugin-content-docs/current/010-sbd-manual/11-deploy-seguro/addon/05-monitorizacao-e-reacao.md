---
id: monitorizacao-e-reacao
title: Post-Deployment Monitoring and Response Actions
description: Observability practices, runtime metrics and automatic rollback mechanisms after deployment.
tags: [tipo:anexo, grupo:execucao, tema:monitorizacao, rollback, observabilidade]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/addon/05-monitorizacao-e-reacao.md
  source_sha256: c20747cb4f0ae7e797f14ab031116a536a5ccdd710b8c6cd670adbfcea34bd0b
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 476527ecdd15d17f3b8959af51f22ffb55b93e890bf86fd1b920c07ddeaa4a35
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 112d795f9bd927f0d4c24114e389470217eb00c1d6b919ae2df2e4f7bdb4878d
  glossary_keys: [cycle_iteration, lifecycle_phase, traceability]
  glossary_sha256: 273b72c17692561ca73b7f60b812ad96d6bbacf7e3818e71f67f43f1578e0fdd
  translated_at: 2026-09-26T11:00:49Z
  reviewed_by: null
---

# Monitoring and Response to Runtime Incidents

The execution phase of an application in production requires **adequate observability and the capacity for rapid response** to failures or anomalies. This document defines the essential mechanisms for detecting, analysing and responding to security or stability problems at runtime.

---

## 🔍 Observability domains {#-domínios-de-observabilidade}

| Domain               | Description                                                             | Tool examples       |
|------------------------|----------------------------------------------------------------------|------------------------------|
| **Structured logging**| Event records with context (user, request, IP, error)            | ELK, Loki, Datadog Logs      |
| **Execution metrics** | Performance and stability indicators                              | Prometheus, New Relic, App Insights |
| **Security alerts** | Automatic triggers on anomalous patterns or rule violations     | SIEM, Sentry, Azure Defender  |
| **Distributed tracing**| Tracking of calls between services, with times and errors               | Jaeger, OpenTelemetry        |

---

## 🚨 Examples of events that must generate alerts {#-exemplos-de-eventos-que-devem-gerar-alertas}

- Abnormal increase in 5xx errors
- Timeout in calls to critical dependencies
- Activation of a kill switch
- Access to functionality deactivated by toggle
- Logs with unhandled exception messages
- Detection of anomalous patterns (e.g. login spikes)

---

## 🚒 Incident response {#-reação-a-incidentes}

| Response type          | Example                                                          |
|---------------------------|------------------------------------------------------------------|
| **Automatic rollback**   | Revert the deployment if the error level or metrics exceed a threshold |
| **Toggle activation**   | Kill switch activates containment functionality                 |
| **Human escalation**  | Alert in an incident channel (e.g. Slack, PagerDuty)             |
| **Subsequent analysis**      | Generate a timeline and records for the post-mortem                      |

> 🔊 The response must not be exclusively human: it must be supported by automation and clear playbooks.

---

## 📊 Post-deployment traceability metrics {#-métricas-de-rastreabilidade-pós-deploy}

- Average latency per functionality
- Errors per endpoint / method
- No. of toggles activated at runtime
- Incidents resolved by rollback
- Users impacted by failure

These metrics must be linked to:
- Release version
- Functional and technical owner
- Activation/deactivation events of execution controls

---

## 💼 Requirements for audit and traceability {#-requisitos-para-auditoria-e-rastreabilidade}

- Logs must contain:
  - Release ID
  - Functionality identifier
  - Timestamp + context
- Configuration changes must be:
  - Versioned
  - Audited by an authorised profile
  - Linked to a reason/documentation

---

## ✅ Monitoring checklist {#-checklist-de-monitorização}

- [ ] Are alerts defined for security events?
- [ ] Do all critical toggles generate events in the logging system?
- [ ] Are metrics configured per functionality?
- [ ] Is there a dashboard or runtime execution panel?
- [ ] Are thresholds defined that trigger automatic rollback?
- [ ] Is there a response playbook per incident type?

> 🗓️ These practices must be validated at each release and maintained throughout the lifecycle of the active version.
