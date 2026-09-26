---
id: dominios-monitorizacao
title: Monitoring and Observability Domains
sidebar_position: 1
description: Identification and definition of the technical and operational domains to be monitored in modern systems.
tags: [monitorização, observabilidade, logging, segurança, runtime, infraestrutura]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/addon/01-dominios-monitorizacao.md
  source_sha256: ef52d5fc7e8f650d874b51ffb0ae12b649e1fe0240b72e217315c55c8189a0c3
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 5410d1fa50d22992db122a9e7e972dbfab95db60ab6459c0c8fca642a43ee97b
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: ebb6c6bf48bf281085379aa982dcfe014d642265f07b08070d51366e58764173
  glossary_keys: [audit_trail, risk_level, traceability]
  glossary_sha256: b046c0596f10666098c9369400e2c2eb48616d2a7dda603af61db5d823fc3447
  translated_at: 2026-09-26T11:17:25Z
  reviewed_by: null
---

# Monitoring Domains and Coverage

## 🌟 Objective {#-objetivo}

Define a practical taxonomy of the **monitoring domains** applicable to applications and systems, allowing detection, operation, traceability and security controls to be structured, with proportionality to the risk level and to the critical flows.

---

## 🧬 What monitoring domains are {#-o-que-são-domínios-de-monitorização}

Application and infrastructure monitoring can be classified into specific domains according to the type of data observed and the objectives of detection, analysis or traceability. Each domain focuses on a distinct subset of the system's behaviour, and requires its own tools and approaches.

---

## 🗂️ Types of monitoring {#️-tipos-de-monitorização}

| Type                        | Main purpose                                  | Practical examples                                     |
|-----------------------------|--------------------------------------------------------|--------------------------------------------------------|
| **Technical (runtime)**       | Detection of failures, exceptions, performance problems | Error logs, CPU/memory metrics, tracebacks     |
| **Security (SIEM)**        | Detection of suspicious or abusive events              | Failed logins, permission changes, DoS         |
| **Business / functional**     | Visibility over critical flows                    | Checkout events, access to sensitive areas        |
| **Compliance / audit**| Traceability and proof of compliance               | Who accessed what, when, with which profile              |
| **Infrastructure / CI/CD**  | Monitoring of the environment and the pipeline               | Config changes, builds, use of secrets           |

> 🌐 Correct classification allows requirements to be applied proportionally, with a focus on detection, traceability or operational optimisation.

---

## 🔎 How to apply {#-como-aplicar}

1. **Identify critical flows** of the application and the system;
2. **Map the applicable domains** to each flow (e.g. functional, security, CI/CD);
3. **Select data sources** compatible with each domain (see below);
4. **Integrate observability tools** suited to the context (e.g. Prometheus, ELK, Splunk, Datadog);
5. **Correlate events across domains**, whenever possible, for more effective detection.

---

## 📘 Typical data sources for each domain {#-fontes-típicas-de-dados-para-cada-domínio}

| Origin              | Data type                         | Common tools                    |
|---------------------|----------------------------------------|----------------------------------------|
| Application           | Structured logs (JSON, ECS...)       | Logback, Winston, Serilog              |
| Infrastructure      | Syslog, metrics, events               | Filebeat, Fluentbit, Prometheus        |
| CI/CD               | Pipeline output, build traces    | GitHub Actions, GitLab, Azure DevOps   |
| API Gateway / WAF   | Requests, errors, blocks             | Kong, NGINX, AWS WAF, Azure Frontdoor  |
| SIEM                | Aggregated events                      | Splunk, Sentinel, Elastic, QRadar      |

---

## 📊 Proportionality by risk level {#-proporcionalidade-por-nível-de-risco}

The selection of domains and the depth of monitoring must be proportional to the application's criticality:

- **L3 applications**: full coverage of the domains, with SIEM integration and active alerts.
- **L2 applications**: focus on runtime, infrastructure and security; centralised logging mandatory.
- **L1 applications**: may be limited to technical metrics, provided that this is justified and accepted by security.

> 📌 The `addon/08-matriz-controles-por-risco.md` details the minimums per risk level.

---

## ✅ Good practices {#-boas-práticas}

- Apply structured logging (e.g. JSON, ECS) with context enrichment;
- Prioritise domains that support active detection and response (e.g. security, CI/CD);
- Review domain coverage throughout the SDLC;
- Integrate with a common observability platform (e.g. ELK stack, Datadog, Grafana/Loki);
- Correlate events across domains to detect attacks or chained failures.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                           | Relation to this topic                         |
|-------------------------------------|--------------------------------------------------|
| `08-matriz-controles-por-risco.md` | Defines minimums per domain and per criticality     |
| `04-integracao-siem.md`            | Integration of events with detection platforms |
| `05-monitorizacao-operacoes.md`     | Response to events and alerts                     |
| `06-correlacao-anomalias.md`       | Strategies for correlation across domains         |

---

> 🔍 Clear classification of the monitoring domains is essential for an approach that is effective, auditable and proportional to the detection of anomalies and to the secure operation of modern systems.
