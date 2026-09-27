---
id: dominios-monitorizacao
title: Monitoring and Observability Domains
sidebar_position: 1
description: Identification and definition of the technical and operational domains to be monitored in modern systems.
tags: [monitorização, observabilidade, logging, segurança, runtime, infraestrutura]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/addon/01-dominios-monitorizacao.md
  source_sha256: f9c11fa3390f1d70f6e68a9d67550b62c232bd92110b905a90fa781794c70257
  source_commit: 5e4b3eab6144ef4347232513856d6d9cb86a487c
  target_sha256: a2ca5d1c3eee3eeb74e8c743952e4d9678e257e2d1977b862d9ff7126407e1df
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [audit_trail, risk_level, traceability]
  glossary_sha256: e9dc350fc47e063712862528255aba4899b0f8b9ae0a25ac913c0a4b6bf3a623
  translated_at: 2026-09-27T15:08:29Z
  stamped_at: 2026-09-27T15:08:29Z
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
- **L1 applications**: structured, persistent *logging* and a catalogue of critical security events are mandatory; the remaining coverage may be limited to technical metrics, provided that this is justified and accepted by security.

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
