---
id: correlacao-anomalias
title: Event Correlation and Anomaly Detection
sidebar_position: 6
description: Strategies for correlating logs across sources and detecting suspicious behaviour.
tags: [correlação, anomalias, eventos, deteção, multi-sistema]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/addon/06-correlacao-anomalias.md
  source_sha256: d34789fd43b0efbb7ca7868aff79aadf6cfc8f8dcf65d81e6d323d6b5b9ff1b1
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 0ca24a1378f18bd41eaa84c785ca24871f690328b05ebcfdf18b91ce2774de03
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: ebb6c6bf48bf281085379aa982dcfe014d642265f07b08070d51366e58764173
  glossary_keys: [atomic_composite, framework_source_corpus, threat]
  glossary_sha256: 0917066591d22dea423ceca2d7ba774c31433bed2344f53f6c816c6a209b8c5b
  translated_at: 2026-09-26T11:17:29Z
  reviewed_by: null
---


# Correlation and Anomaly Detection

## 🌟 Objective {#-objetivo}

Apply event correlation and anomaly detection techniques to identify behaviour patterns which, although harmless in isolation, may indicate significant risk when analysed together.

---

## 🎯 Objectives of applying correlation {#-objetivos-da-aplicação-de-correlação}

* Detect **suspicious behaviour** emerging from discrete patterns
* Reduce **false positives** through cross-referenced context
* Prioritise **real incidents** on the basis of multiple pieces of evidence
* Support **proactive and adaptive detection**

---

## 🥁 Types of correlation {#-tipos-de-correlação}

| Type               | Practical example                               |
| ------------------ | --------------------------------------------- |
| **Temporal**       | Suspicious actions within a short interval            |
| **Contextual**     | Out-of-hours login + unusual IP              |
| **Behavioural** | Deviation from the user's pattern                |
| **Cross-source**   | Event in the app followed by firewall or SIEM     |
| **Session / flow** | Events with the same `trace.id` or session token |

---

## 🛠️ Supporting techniques and tools {#️-técnicas-e-ferramentas-de-suporte}

| Technique                 | Application / example                           |
| ----------------------- | --------------------------------------------- |
| **Rules in the SIEM**      | Splunk, Sentinel, QRadar                      |
| **Chaining / graphs**   | Identity and session graphs                 |
| **Baseline models** | Deviations by IP, endpoint, time                |
| **Composite threshold**  | Multiple accumulated conditions                |
| **Aggregate score**      | Score per user, device or application |

> ⚠️ Rule-based correlation is the best starting point for most organisations.

---

## 🧠 Examples of correlated patterns {#-exemplos-de-padrões-correlacionados}

| Pattern identified                | Interpretation             |
| ---------------------------------- | ------------------------- |
| Login + massive download           | Credential abuse      |
| Repeated failures + success         | Successful brute force  |
| Role change + config change | Privilege escalation   |
| API key + out-of-hours access   | Misuse              |
| Commit + atypical CI/CD execution    | Compromise in the chain |

---

## 🪧 Good practices {#-boas-práticas}

* Normalise events before correlation (formats, fields)
* Use limited time windows (e.g. 5m, 15m)
* Correct false negatives with new correlation factors
* Use persistent IDs: `user.id`, `session.id`, `trace.id`
* Assess the severity of the set, not of the isolated events

---

## 📊 Behaviour-based detection {#-deteção-baseada-em-comportamento}

| Technique                     | Purpose                                    |
| --------------------------- | --------------------------------------------- |
| **Baseline per user** | Individual deviations (time, volume, endpoint) |
| **Profile per role**         | Actions not expected for a given profile   |
| **Aggregated metrics**      | API calls, latency, variation in the pattern |
| **Supervised feedback** | Reinforcement of rules based on real cases     |

> 💡 Requires progressive tuning and the active participation of the teams.

---

## 🧹 Integration with other controls {#-integração-com-outros-controlos}

| Document                        | Relation to this topic                      |
| -------------------------------- | -------------------------------------------- |
| `02-logging-centralizado.md`     | Source of the events for correlation            |
| `04-integracao-siem.md`          | Channel and format of ingestion                   |
| `03-alertas-eventos-criticos.md` | Pattern-based alert generation        |
| `09-ameacas-mitigadas.md`        | Maps detection to threat scenarios (OSC\&R) |

---

## ✅ Final recommendations {#-recomendações-finais}

* Start with simple correlation, based on high-impact events
* Test with real data, simulated data and old logs
* Track quality metrics (signal/noise, triage time)
* Evolve towards scoring, dynamic baseline and assisted detection

> 🌟 Effective correlation reduces false positives and reveals complex patterns that would otherwise go unnoticed.
