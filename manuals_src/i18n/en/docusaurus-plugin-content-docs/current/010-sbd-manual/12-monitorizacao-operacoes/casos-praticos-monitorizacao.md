---
id: casos-praticos-monitorizacao
title: Practical Cases of Monitoring and Detection
description: Applied examples of logging, alerts and correlation in real contexts
tags: [caso de estudo, exemplos, logging, alertas, deteção, correlação, telemetria, sbd-toe]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/casos-praticos-monitorizacao.md
  source_sha256: 3a8850c7980cc42f5f35352b566ff3bd2b8baa3dc4a099354661938b27cdaa57
  source_commit: 50f5914ebc90e4135e6678b2278709d5082dd237
  target_sha256: 5df24da2e76ad590bcd9c3effa1ec49b0c82c1af0126f1646cb162c19723045b
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, practitioner_manual, traceability, validation_evaluation]
  glossary_sha256: a3e31eca02d3feda6771afa947c017741f236504da7e545162132f66d5ef9b77
  translated_at: 2026-09-27T07:06:04Z
  stamped_at: 2026-09-27T07:06:04Z
  reviewed_by: null
---

# Practical Cases of Monitoring and Detection

This annex presents **practical examples** of the application of the monitoring, logging, alert and correlation recommendations. The scenarios described here help to understand how to apply the prescriptions of this chapter to concrete cases.

---

## 🚀 Case 1 - API Gateway with structured logging and alerts {#-caso-1---api-gateway-com-logging-estruturado-e-alertas}

> 🛡️ **Risk classification: L3 - Application with public exposure and critical operations**

**Context:** Application exposed through an API Gateway, token-based authentication, with critical endpoints (checkout, transfers).

**Controls applied:**

- JSON logging with ECS via customised NGINX
- Fields included: `user.id`, `request.path`, `status`, `latency`, `geo.country`
- Alerts:
  - Consecutive 5xx responses from one IP within a 5-minute interval
  - Access to `/checkout` outside the 06:00–22:00 window
- Logs sent to the Elastic Stack via Filebeat
- Dashboards with metrics per endpoint, errors, geo, by profile

**Result:** Reduction of MTTD for login anomalies and abuse by automated scripts.

---

## 💰 Case 2 - Monitoring of uploads in a document management application {#-caso-2---monitorização-de-uploads-em-aplicação-de-gestão-documental}

> 🛡️ **Risk classification: L3 - Application with sensitive data and risk of exfiltration**

**Context:** Internal platform for the management of sensitive documents with a review workflow.

**Controls applied:**

- Logging of `upload`, `download`, `delete` events, with user ID and checksum
- Event table replicated to the SIEM (QRadar) via structured syslog
- Active correlation: upload of >100MB + unusual IP + user role "editor"
- Generates a "potential internal exfiltration" alert
- Playbook triggers an investigation with log tagging and temporary isolation

**Result:** Detection of unauthorised movement in the context of team turnover.

---

## 👨‍💼 Case 3 - Monitoring of CI/CD pipelines and detection of unusual execution {#-caso-3---monitorização-de-pipelines-cicd-e-deteção-de-execução-invulgar}

> 🛡️ **Risk classification: L2 - Internal pipeline with supply chain impact**

**Context:** Pipelines with automatic execution via GitHub Actions + Kubernetes. The team wants to track changes in behaviour.

**Controls applied:**

- Structured logging of jobs, with the `pipeline.start`, `pipeline.command`, `pipeline.result` events
- Logs sent to Loki + Grafana Tempo with `trace.id`
- Alerts:
  - Execution of shell commands outside the usual ones (`curl`, `rm`, `base64`)
  - Job that lasts >2x the historical average time
  - Pipeline executed from a "legacy/" branch + unusual user
- Correlation with the image used in the job (e.g. `ubuntu:latest` outside the baseline)

**Result:** A corrupted build incident was detected and blocked before it reached the release.

---

## 🔎 Case 4 - Correlation of authentication logs with session movements {#-caso-4---correlação-de-logs-de-autenticação-com-movimentos-de-sessão}

> 🛡️ **Risk classification: L3 - Multi-user application with sensitive profiles and risk of hijacking**

**Context:** Application with internal and external users, with long sessions. Misuse was reported.

**Controls applied:**

- Session identified by `session.id` + `trace.id`
- Login, token refresh, logout and API call logs aggregated per session
- Correlation:
  - Login via an old token with a different IP/UA origin
  - Token refresh triggered without normal use of the session
- Triggers a "ghost / hijacked session" alert
- Cross-validation with load balancer and WAF logs

**Result:** Session blocking and revocation in real time. Reinforced timeout and earlier alerting.

---

## 🧪 Case 5 - Low-criticality internal application with local logging and manual validation {#-caso-5---aplicação-interna-de-baixa-criticidade-com-logging-local-e-validação-manual}

> 🛡️ **Risk classification: L1 - Technical support application, limited use**

**Context:** Internal application used only by the technical support team, with no external access and no sensitive data.

**Controls applied:**

- Local logging to a rotating file in a structured format (JSON)
- Events recorded: `login`, `erro`, `config.change`
- Retention of 30 days on local disk with weekly backups
- Manual validation of the logging operation in release reviews
- No SIEM, no automatic correlation and no real-time alerts

**Result:** Fulfilment of the minimum requirements of level L1, with basic visibility and sufficient traceability for internal audits.

> ✅ Example of application **proportional to the risk**, without over-engineering.

---

## 📊 Summary Table of the Cases {#-tabela-resumo-dos-casos}

| Case | Risk | Main Context                      | Key controls applied                           |
|------|-------|------------------------------------------|-----------------------------------------------------|
| 1    | L3    | API Gateway with critical endpoints       | ECS logging, out-of-hours alerts, Elastic Stack |
| 2    | L3    | Document management with risk of leakage      | Syslog, correlation, isolation, SOAR                |
| 3    | L2    | CI/CD with anomalous execution               | Pipeline logs, correlation by command and branch   |
| 4    | L3    | Multi-user with session hijacking             | trace.id, login/token/session correlation          |
| 5    | L1    | Internal support application             | Local logging, no SIEM, manual review             |

---

> These practical cases demonstrate how the integrated application of the logging, alert and correlation controls makes it possible to **detect behaviours that would be invisible in isolation**.

> ✅ For high-risk applications (L3), it is recommended to keep a validated repository of real and simulated examples, with validation of trigger and response.
