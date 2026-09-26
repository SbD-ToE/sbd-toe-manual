---
id: alertas-eventos-criticos
title: Generation and Management of Alerts for Critical Events
sidebar_position: 3
description: Rules, thresholds and best practices for effective alerts based on sensitive events.
tags: [alertas, eventos críticos, deteção, thresholds, severidade]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/addon/03-alertas-eventos-criticos.md
  source_sha256: 59bed96f99d654358062662bb618c7cd661a5c9951f865c35a79f0a6cc1d5a7e
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 0e9ba963a17723b142304c657f9aebe3be1a5b955c83ee97c1047550a674c293
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: ebb6c6bf48bf281085379aa982dcfe014d642265f07b08070d51366e58764173
  glossary_keys: [framework_source_corpus, maturity, validation_evaluation]
  glossary_sha256: 25d0b23ee5446525e78f119764dac5869f2b480e8cfcd4491ed252f148bfc5c6
  translated_at: 2026-09-26T11:17:27Z
  reviewed_by: null
---

# Alerts Based on Critical Events

## 🌟 Objective {#-objetivo}

Prescribe practices for the definition, activation and validation of **automatic alerts based on critical events**, with a focus on timely detection, reduction of false positives and effective integration with the response teams.

---

## 🧬 What critical alerts are {#-o-que-são-alertas-críticos}

Critical alerts are **automatically generated notifications** based on event patterns that indicate anomalies, security failures or undesired behaviour - requiring human validation or an immediate response.

> 🌟 A good alert is timely, actionable, and based on traceable and structured events.

---

## 📌 Types of events that must generate alerts {#-tipos-de-eventos-que-devem-gerar-alertas}

| Event type              | Practical examples                                 | Suggested severity |
| --------------------------- | ------------------------------------------------- | ------------------- |
| **Failed authentication**    | Several consecutive failures from one IP or user | High / Medium        |
| **Privilege elevation** | Profile change without a formal process             | High                |
| **Critical changes**     | Permission configuration, API keys              | High / Medium        |
| **Repeated failures**        | Continuous 5xx errors in an API or microservice      | Medium               |
| **Unusual inactivity**     | Drop in logs from an active module                  | Medium / Low       |
| **Anomalous calls**       | Out-of-hours access, unusual geolocation    | High / Medium        |

> ⚠️ The set of alerts must be proportional to the **application's criticality** and to the **sensitivity of the data processed**.

---

## 🛠️ How to define an effective alert {#️-como-definir-um-alerta-eficaz}

Each alert rule must contain:

* **Condition**: e.g. 5 login failures within a 3-minute interval;
* **Data source**: log file or index in the SIEM (e.g. `auth.log`);
* **Severity**: High, Medium, Low - according to impact and urgency;
* **Notification channel**: e-mail, Slack, webhook, PagerDuty, etc.;
* **Runbook (optional)**: link to a standardised response.

### Example (generic YAML): {#exemplo-yaml-genérico}

```yaml
alert_name: login_failures_high
condition: count(auth.event == "login_failed") by ip > 5 in 3m
severity: high
notify: slack_channel_security
runbook: https://wiki.exemplo.org/runbooks/login-failures
```

---

## 🧪 Alert validation {#-validação-de-alertas}

| Technique                    | Description                                        |
| -------------------------- | ------------------------------------------------ |
| **Active simulation**        | Force the event in a staging environment             |
| **Rule unit test**     | Automated tests of the condition logic          |
| **Replay with real data** | Apply the rule retroactively to historical data |
| **Triage playbooks**   | Associate operational actions with the alert               |

> ✅ Only validated alerts should be considered active in production.

---

## 📊 Tuning and management of false positives {#-tuning-e-gestão-de-falsos-positivos}

Poorly calibrated alerts cause noise and discredit the system. Recommended practices:

* Define thresholds based on real data and context
* Use silencing mechanisms (e.g. snooze, threshold decay)
* Document false positives and their causes
* Review conditions periodically

> 💡 Per-alert statistics help to prioritise (e.g. signal/noise).

---

## 🧹 Integration with other controls {#-integração-com-outros-controlos}

| Document                          | Link to this topic                          |
| ---------------------------------- | ------------------------------------------------ |
| `02-logging-centralizado.md`       | Defines the source events for alert generation |
| `06-correlacao-anomalias.md`       | Correlation of multiple events and domains       |
| `05-monitorizacao-operacoes.md`     | Uses alerts as a response trigger         |
| `08-matriz-controles-por-risco.md` | Sets out alert requirements by criticality      |

---

## ✅ Final recommendations {#-recomendações-finais}

* Start with 5 to 10 high-value alerts (impact + frequency)
* Prioritise alerts linked to critical flows or sensitive data
* Document all rules, parameters and validations
* Integrate alerts into observability and response pipelines

> 🔒 An effective alerting capability is one of the pillars of operational security maturity. It must evolve on the basis of feedback, real detection and incident response.
