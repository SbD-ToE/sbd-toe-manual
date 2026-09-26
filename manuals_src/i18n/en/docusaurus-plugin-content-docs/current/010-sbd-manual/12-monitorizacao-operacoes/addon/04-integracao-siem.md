---
id: integracao-siem
title: Integration with SIEM and Correlation Platforms
sidebar_position: 4
description: Integration with SIEM systems for parsing, visualisation and correlation of events.
tags: [siem, integração, parsing, dashboards, correlação]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/addon/04-integracao-siem.md
  source_sha256: 9e0507859faa92d892dd29d44855588608060271759c26358e6c54f2d0138824
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: f0db58fa6464c9c48242ba0cb6575dca92805e14aaf5bc0b23f0b304f0365980
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, layer, requirement_runtime, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 0c3935e8eaee69200f4962bf89d692020345cd0716d8eea334289adccaf0ce65
  translated_at: 2026-09-26T12:48:56Z
  stamped_at: 2026-09-26T18:35:40Z
  reviewed_by: null
---


# Integration with Detection Systems (SIEM)

## 🌟 Objective {#-objetivo}

Ensure a **reliable, secure and auditable integration** between the event sources (applications, infrastructure, pipelines) and the analysis and correlation system (SIEM), guaranteeing support for effective detection, response and traceability.

---

## 🧬 What SIEM integration is {#-o-que-é-a-integração-com-siem}

It is the chain of **collection, transport, transformation and ingestion** of the relevant events into a SIEM, guaranteeing:

* A suitable format compatible with parsing;
* Reduced latency and resilience to failures;
* Effective correlation capability across sources.

> 🧑‍💻 The application must never communicate directly with the SIEM - always use a forwarder as an isolation layer.

---

## 📀 Typical integration architecture {#-arquitetura-típica-de-integração}

```
[Aplicação] → [Logger] → [Forwarder/Agent] → [Parser] → [SIEM]
```

| Component          | Main function                                      |
| ------------------- | ----------------------------------------------------- |
| **Logger**          | Emission of structured logs (e.g. JSON, ECS)          |
| **Forwarder**       | Local collection, buffering and secure forwarding                |
| **Parser/Ingester** | Transform logs into a normalised, indexable format |
| **SIEM**            | Analysis, correlation, visualisation and alerting            |

---

## 🛠️ Functional requirements of the integration {#️-requisitos-funcionais-da-integração}

| Requirement                            | Description                                      |
| ------------------------------------ | ---------------------------------------------- |
| **Supported format**                | JSON, CEF, LEEF, ECS, structured Syslog       |
| **Secure channel**                     | TLS 1.2+ with authentication (key, token, mTLS) |
| **Local buffering**                  | The forwarder must tolerate network failures          |
| **Tagging by application / environment** | Facilitates filters and dashboards                  |
| **Normalised timestamps**          | UTC, ISO 8601, synchronised via NTP            |

---

## 🔧 Common tools {#-ferramentas-comuns}

| Category           | Examples                                            |
| ------------------- | --------------------------------------------------- |
| **Forwarders**      | Filebeat, Fluentbit, Vector, rsyslog                |
| **SIEMs**           | Splunk, Azure Sentinel, Elastic SIEM, QRadar        |
| **Normalisers**  | Logstash, Cribl, ingest pipelines (OpenSearch, ELK) |
| **Observability** | Grafana, Loki, Datadog, Prometheus                  |

---

## ✅ Integration good practices {#-boas-práticas-de-integração}

* Validate logs with `tcpdump`, `wireshark` or ingestion dashboards;
* Use **enrichment filters** (e.g. geolocation, `user-agent`, `env`);
* Avoid redundancy (the same event sent to several destinations);
* Test forwarding with `logger`, `curl`, replay of real logs;
* Ensure safe reversion (rollback of the forwarder version, tags, etc.).

---

## 🔍 Validation of the integration {#-validação-da-integração}

| Verification                         | Suggested method                               |
| ----------------------------------- | --------------------------------------------- |
| Event reached the SIEM               | Confirm via index or forwarder log          |
| Fields were parsed correctly | Check in a dashboard or inspection query         |
| Latency between generation and ingestion    | Measured with timestamp vs ingest time           |
| Duplicates or losses                | Verification by hash / ID / expected count |

---

## 🔒 Security considerations {#-considerações-de-segurança}

* Isolate the forwarders' network from the SIEM network;
* Monitor forwarding or parsing failures with alerts;
* Protect agent configurations (tokens, paths, endpoints);
* Validate that events do not contain sensitive data in the clear.

---

## 📂 Advanced integrations {#-integrações-avançadas}

* Logging of pipeline execution (CI/CD, DevOps);
* Sending events directly via API gateways and proxies;
* Correlation with session, user, `trace.id`, etc.;
* Dashboards per application, environment, component.

---

## 🧹 Link with other controls {#-ligação-com-outros-controlos}

| Document                          | Relation to this topic                        |
| ---------------------------------- | ---------------------------------------------- |
| `02-logging-centralizado.md`       | Defines the sources and formats of the events        |
| `06-correlacao-anomalias.md`       | Uses the events for detection and correlation   |
| `09-ameacas-mitigadas.md`          | Shows how the integration supports response      |
| `08-matriz-controles-por-risco.md` | Determines whether SIEM integration is mandatory |

> 🧠 The quality of the SIEM integration directly determines the effectiveness of the response and the traceability of the systems.
