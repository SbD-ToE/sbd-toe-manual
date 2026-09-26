---
id: metricas-indicadores
title: Metrics, Indicators and KPIs for Detection and Response
sidebar_position: 7
description: Definition and calculation of indicators such as MTTD and MTTR, and their application in operational dashboards.
tags: [métricas, indicadores, mttd, mttr, dashboards, kpi]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/addon/07-metricas-indicadores.md
  source_sha256: 2a384392751a7403aff635737c5129752fc0a243c6bbab3cfd132a5957e7c4d1
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: 1a55108c4c06538bcbdc0b936253d290a9c692cf8431f588578ac747167ade3e
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [maturity, practitioner_manual, validation_evaluation]
  glossary_sha256: 3956127a2db6f8da73678646769aa190831ada6098b1dfc75c5c2aed08211ef5
  translated_at: 2026-09-26T12:48:57Z
  reviewed_by: null
---

# Metrics, Indicators and Coverage

## 🌟 Objective {#-objetivo}

To define metrics and indicators to assess the **effectiveness, coverage and maturity** of the monitoring, detection and response controls, enabling continuous improvement based on operational data.

> This file is an **operational synthesis** for day-to-day reading. The canonical catalogue of `OPS-Kxx` is in [`11-kpis-metricas.md`](./11-kpis-metricas.md).

---

## 📏 Coverage indicators {#-indicadores-de-cobertura}

| Metric                             | Objective                                              |
| ----------------------------------- | ----------------------------------------------------- |
| % of critical flows with logging    | Assess minimum visibility over sensitive operations |
| % of logs sent to the SIEM        | Measure adherence to centralisation                       |
| % of alerts with a tested trigger    | Validation of the effectiveness of the alerts                     |
| % of components with ECS tagging    | Assess consistency and normalisation                   |
| % of pipelines that produce events | CI/CD coverage in the detection of suspicious events       |

---

## ⏱️ Operational indicators {#️-indicadores-operacionais}

| Metric                        | Meaning                                      | Calculation example                   |
| ------------------------------ | ------------------------------------------------ | ------------------------------------ |
| **MTTD** (Time to Detect)      | Mean time from event to alert              | timestamp\_alert - timestamp\_event  |
| **MTTR** (Time to Respond)     | Mean time until the start of mitigation              | timestamp\_action - timestamp\_alert |
| **False positive rate**        | % of non-relevant alerts                      | invalid alerts / total alerts    |
| **Events per user/day** | Normal average activity for the baseline profile          | comparative baseline                 |
| **Incidents by category**   | Classification of cases by type (access, fraud) | logs or IR tickets                   |

> 🌟 **MTTD and MTTR** are key indicators of operational maturity.

---

## 📊 Suggested dashboards and reports {#-dashboards-e-relatórios-sugeridos}

| Dashboard type           | Data included                                   |
| ------------------------ | ------------------------------------------------- |
| **Logging coverage** | Apps without structured logs, by criticality       |
| **Alert quality** | Active/tested triggers, % of false positives      |
| **Events and context**   | Events by type, IP, user, system               |
| **Detection and response**   | MTTD, MTTR, by severity, as a time series |
| **Anomalous patterns**     | Outliers by role, geography, time of day, device        |

---

## 🌄 Integration with maturity {#-integração-com-maturidade}

| Maturity level | Expected indicators                                              |
| ------------------- | ------------------------------------------------------------------ |
| **L1 (minimum)**     | Local logging active, occasional manual analysis                      |
| **L2 (moderate)**   | Automatic alerts with tuning, basic operational dashboards     |
| **L3 (advanced)**     | Correlation of sources, behavioural detection, KPIs such as MTTD/MTTR |

> 📊 These metrics also contribute to Chapters 10 (Security Testing) and 11 (Execution Control).

---

## ✅ Final recommendations {#-recomendações-finais}

* Measure and publish metrics **at least monthly**
* Set improvement targets (e.g. -20% MTTD in 3 months)
* Correlate metrics with real events and simulated exercises
* Prioritise visibility and coverage of critical assets

> 💡 *Without measurement, there is no improvement.* Quantitative visibility is essential to security maturity.
