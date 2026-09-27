---
id: matriz-controles-por-risco
title: Controls Matrix by Risk Level
sidebar_position: 8
description: Proportional application of the monitoring and response controls according to the application's risk classification.
tags: [proporcionalidade, risco, matriz, controles, L1, L2, L3]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/addon/08-matriz-controles-por-risco.md
  source_sha256: 436df5318df5b381ff615bf7fba76c3c60f016ce9536904b8d3c1439f7869710
  source_commit: 50f5914ebc90e4135e6678b2278709d5082dd237
  target_sha256: b0ff0d0eb78891a5fc6f2949c264a6e3b0ca4e0307e9ccec42acba3b9977f708
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [avaliacao, chapter_role, cycle_iteration, lifecycle_phase, maturity, requirement_runtime, risk_level, traceability]
  glossary_sha256: 9582a04bbd3949571c2f6f7403eac2f07af5d0a9f857b676a5d71878d224738d
  translated_at: 2026-09-27T07:06:02Z
  stamped_at: 2026-09-27T07:06:02Z
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
| Minimum retention in line with Policy 29 (security logs: 90 days L1, 1 year L2, 2 years L3) |  ✔️ |  ✔️ |  ✔️ |
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
