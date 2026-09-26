---
id: controles-logging-centralizado
title: Structured and Centralised Logging Controls
sidebar_position: 2
description: Practices to guarantee structured logging, secure transport and centralisation of operational events.
tags: [logging, estruturação, centralização, ECS, transporte seguro]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/addon/02-controles-logging-centralizado.md
  source_sha256: 445323bea13bbfe86cc82a7534672ff263dc966caea19c89bde5e21162980423
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: f02b605ec3f3a3497d70be3eaee21b46e241de908b0fd2d377974f8f44eb46b8
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: ebb6c6bf48bf281085379aa982dcfe014d642265f07b08070d51366e58764173
  glossary_keys: [audit_trail, requirement_runtime, traceability, verification_taxonomy]
  glossary_sha256: 478249887e88cd12475069923f4f6cf2f667fcb718513bf0793aa580aa9e7f06
  translated_at: 2026-09-26T11:17:26Z
  reviewed_by: null
---


# Structured and Centralised Logging

## 🌟 Objective {#-objetivo}

Ensure that all applications record events in a structured, secure, traceable and auditable manner, enabling anomaly detection, correlation between systems and support for incident response.

---

## 🧬 What structured logging is {#-o-que-é-logging-estruturado}

Structured logging consists of the **emission of events with normalised fields**, in a machine-readable format (e.g. JSON), transported to a centralised system and with integrity and retention guarantees.

> 📌 The structure and consistency of logs are essential for detection, traceability and effective investigation.

---

## 🧱 Recommended event structure {#-estrutura-recomendada-dos-eventos}

Adopt a convention such as the Elastic Common Schema (ECS) or an in-house JSON-based format with common minimum fields.

| Field            | Example                                      | Notes                                   |
|------------------|----------------------------------------------|-----------------------------------------------|
| `timestamp`      | `2025-07-21T10:35:14Z`                        | ISO 8601 in UTC                               |
| `level`          | `INFO`, `ERROR`, `WARN`, `DEBUG`             | Standardised levels                           |
| `event.action`   | `user.login`, `file.upload`, `api.call`      | Consistent taxonomy                         |
| `user.id`        | `abcd-1234`                                   | Internal user ID, if applicable        |
| `src.ip`         | `192.168.1.20`                                | Source IP                                  |
| `trace.id`       | `xyz-9876`                                    | Support for distributed tracing                 |
| `application`    | `frontend-web`, `api-gateway`, `worker-job`  | Logical component of the application                |

---

## 📦 Log transport and centralisation {#-transporte-e-centralização-dos-logs}

- Use **forwarding agents** (e.g. Filebeat, Fluentbit, Vector)
- Ensure **secure transport (TLS)** and temporary persistence (buffers)
- Prefer **continuous streaming** (e.g. TCP, gRPC) over batch or UDP
- Separate logging from the main process (e.g. sidecar container, logging driver)

### Typical destinations: {#destinos-típicos}

| Category       | Examples                              |
|-----------------|----------------------------------------|
| SIEMs           | Splunk, Sentinel, QRadar              |
| Observability | Elastic Stack, Loki, Datadog          |
| Hybrid        | OpenSearch, Graylog, Grafana Tempo    |

---

## 🔒 Log security and integrity {#-segurança-e-integridade-dos-logs}

| Control                          | Description                                                        |
|-----------------------------------|------------------------------------------------------------------|
| **Protected retention (WORM)**     | Prevents alteration of logs after writing                            |
| **Restricted access**               | Writing only via the application; reading audited                   |
| **Signature or hash**            | Integrity verification per batch or file                  |
| **Function isolation**          | Logging separated from the application (e.g. forwarder, sidecar, service)  |

> ⚠️ Local-only logs are acceptable only for L1 applications - with periodic collection and documented justification.

---

## 📌 Minimum mandatory events {#-eventos-mínimos-obrigatórios}

| Event type        | Must contain…                                    |
|-----------------------|--------------------------------------------------|
| Failed authentication  | IP, user, timestamp, reason                |
| Sensitive changes  | Who, what, where, before and after                |
| Internal exceptions     | Stack trace (summarised), module, request ID       |
| Upload / download     | Name, size, user, method                |
| External API call   | Endpoint, status, response time              |

---

## ✅ Good practices {#-boas-práticas}

- Do not record sensitive data (e.g. passwords, tokens), even encrypted
- Separate logs by functional context (e.g. `app.log`, `auth.log`, `db.log`)
- Validate the presence and format of logs in automated tests
- Include `request.id` and `trace.id` for traceability of distributed requests
- Emit logs at every security state transition

---

## 🧩 Link with detection and response {#-ligação-com-deteção-e-resposta}

Structured logging serves as the **basis for the detection mechanisms** defined in other documents:

| Document                      | Relation to this topic                     |
|--------------------------------|----------------------------------------------|
| `03-alertas-eventos-criticos.md` | Generation of alerts from events      |
| `06-correlacao-anomalias.md`    | Correlation between events for detection       |
| `08-matriz-controles-por-risco.md` | Logging requirements per level L1–L3     |

---

> 🔐 A well-structured and centralised logging system is a prior requirement for effective detection, incident response, and compliance with frameworks such as SSDF, SLSA, ISO 27001.
