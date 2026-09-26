---
id: matriz-controles-por-risco
title: Controls Matrix by Risk Level
sidebar_position: 8
description: Proportional application of the monitoring and response controls according to the application's risk classification.
tags: [proporcionalidade, risco, matriz, controles, L1, L2, L3]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/addon/08-matriz-controles-por-risco.md
  source_sha256: 2270ef8a7a0d517699e2f52f2a85425c20f4ff05a9db00a85e1ef8c8a6950dba
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: e6fef72692696fb4f0ad4db400ad20b24581b1d671b61d5ddcacce51fbbf5536
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: ebb6c6bf48bf281085379aa982dcfe014d642265f07b08070d51366e58764173
  glossary_keys: [avaliacao, chapter_role, cycle_iteration, lifecycle_phase, maturity, requirement_runtime, risk_level, traceability]
  glossary_sha256: 2933ddb34be223869044546f5619d821977f97c3754096a9e62389471d11756b
  translated_at: 2026-09-26T11:17:30Z
  reviewed_by: null
---

# Controls Matrix by Risk Level - Monitoring and Operations

This matrix defines the **minimum mandatory monitoring requirements** for applications, according to their risk level (L1 to L3). It serves as the basis for compliance assessment and for the planning of controls throughout the lifecycle.

> ⚠️ This matrix applies to **applications classified according to the risk model of Chapter 1**.

---

## 📊 Coverage matrix {#-matriz-de-cobertura}

| Control / Requirement                           |  L1 |  L2 |  L3 |
| ---------------------------------------------- | :-: | :-: | :-: |
| Structured and persistent logging              |  ✔️ |  ✔️ |  ✔️ |
| Critical events defined (login, error, etc.) |  ✔️ |  ✔️ |  ✔️ |
| Minimum retention (>= 30 days)                   |     |  ✔️ |  ✔️ |
| Logs sent to a centralised system (SIEM) |     |  ✔️ |  ✔️ |
| Automatic alerts configured               |     |  ✔️ |  ✔️ |
| Trigger simulations tested                 |     |  ✔️ |  ✔️ |
| Correlation between sources                        |     |     |  ✔️ |
| Behavioural detection / adaptive profiles    |     |     |  ✔️ |
| Integration with incident response (IRP)     |     |  ✔️ |  ✔️ |
| MTTD / MTTR metrics monitored          |     |     |  ✔️ |
| Continuous operational health/readiness signal for critical services |     |  ✔️ |  ✔️ |

---

## ✅ Interpretation {#-interpretação}

* ✔️ = mandatory for that level
* **L1**: local and basic logging for traceability
* **L2**: centralisation of events, fundamental operational alerts and a continuous health signal for critical services
* **L3**: contextual detection, correlation, integrated response and full coverage of operational health/readiness signals

> 🥉 This matrix must be cross-referenced with the requirements catalogue (Ch. 2) and the maturity criteria (`addon/achievable-maturity`).

---

## 📌 Additional recommendations {#-recomendações-adicionais}

* Applications with external exposure and sensitive data must, even when L1, meet L2 or L3 requirements;
* Use this matrix as the **basis for review in architecture, design and production readiness**;
* Include these requirements in the definition of "Done" and in the acceptance criteria of releases.

> 🔒 The matrix works as a reference for minimum control, not as a ceiling on ambition. Mature projects must go further.
