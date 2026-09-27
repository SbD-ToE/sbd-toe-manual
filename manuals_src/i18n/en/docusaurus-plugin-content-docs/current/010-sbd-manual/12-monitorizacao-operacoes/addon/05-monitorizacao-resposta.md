---
id: monitorizacao-operacoes
title: Integration of Monitoring with Incident Response
sidebar_position: 5
description: Link between detection mechanisms and the operational and automated response processes.
tags: [resposta a incidentes, IRP, SOAR, integração, playbooks]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/addon/05-monitorizacao-resposta.md
  source_sha256: 74d8b0a39cc83662eed5cded5700ec88e07adaba48f7935db1875d7c5fdccef0
  source_commit: 50f5914ebc90e4135e6678b2278709d5082dd237
  target_sha256: 66a3da48aef90b8ed958b88b3c1745bc49dd5dfc6618a2299c12aaa4536edd8d
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, cycle_iteration, requirement_runtime, validation_evaluation]
  glossary_sha256: f54d9bfabf1a57875d5f9fd1a792f0cf1058f991156ab7731da2c3405e013022
  translated_at: 2026-09-27T07:06:01Z
  stamped_at: 2026-09-27T07:06:01Z
  reviewed_by: null
---

# Monitoring as Support for Response

## 🌟 Objective {#-objetivo}

Demonstrate how monitoring - including logs, alerts and event correlation - constitutes an essential pillar for the **triage, containment, forensic analysis and continuous improvement** of the incident response capability.

---

## 💢 Functions of monitoring in response {#-funções-da-monitorização-na-resposta}

| Function                    | Main objective                                 |
| ------------------------- | -------------------------------------------------- |
| **Rapid triage**        | Assess the severity, origin and impact of the event     |
| **Containment and mitigation** | Identify affected systems and isolate them quickly |
| **Forensic analysis**       | Reconstruct the timeline of events              |
| **Feedback for detection** | Correct or improve alert rules              |
| **Auditable evidence**   | Support actions before audits or stakeholders |

---

## ⟲ Detection-to-response cycle {#-ciclo-de-deteção-para-resposta}

```
[Evento gerado] → [Log criado] → [Alerta disparado] → [Triagem] → [Contenção] → [Análise] → [Melhoria]
```

Each stage depends on the **quality, context and availability** of the monitored data.

---

## 🚧 Requirements for supporting response {#-requisitos-de-suporte-à-resposta}

| Requirement                          | Justification                                     |
| ---------------------------------- | ------------------------------------------------ |
| **Normalised timestamps**        | Necessary for reconstructing timelines       |
| **User/session context**  | Attribute actions and trace movements             |
| **Correlation across sources**        | Unify events from application, infra, CI/CD      |
| **Integration with IRP**             | Automates tickets, response workflow         |
| **Retention in line with Policy 29** (1 year at L2, 2 years at L3) | Enables retrospective investigation and audit |

---

## 🛠️ Integration with IRP platforms {#️-integração-com-plataformas-irp}

| Type                       | Examples                                               |
| -------------------------- | ------------------------------------------------------ |
| **Integrated SIEMs**       | Splunk, Sentinel, QRadar                               |
| **Incident managers** | TheHive, Jira Security, PagerDuty, OpsGenie            |
| **SOAR/Playbooks**         | IP blocking, token revocation, isolation via API |

> 💡 Each relevant alert must have an **associated action** and, where possible, an **automated playbook**.

---

## 📘 Examples of monitoring-based response {#-exemplos-de-resposta-baseada-em-monitorização}

| Incident identified       | Support via logs and alerts                              |
| ---------------------------- | ------------------------------------------------------- |
| Unauthorised access        | Login logs + alert on suspicious origin               |
| DoS or brute force attacks   | Failure count + real-time threshold rule      |
| Use of invalid credentials | Correlation between app, CI/CD, infra                      |
| Configuration change    | Alert + configuration diff + permission validation |
| Data exfiltration         | Download/upload logs + anomalous patterns              |

---

## ⟲ Integration with continuous improvement {#-integração-com-melhoria-contínua}

Each incident or near-incident must generate:

* Adjustments to the **detection rules** (new patterns, false negatives);
* Expansion of **logging coverage** and emitted events;
* Improvement of **alerts and thresholds** (avoiding overload or omissions);
* Recording of **operational metrics**: MTTD, response time, event volume.

---

## ✅ Recommendations {#-recomendações}

* Define and maintain **playbooks per alert type** and an escalation route;
* Link logs to IR tools for immediate access to the context;
* Run **regular simulations** of detection and response;
* Automate **context extraction** (user, IP, origin, request ID);
* Monitor the **effectiveness of the response** with quantitative metrics.

> 🌟 Effective monitoring **reduces detection time and accelerates response** - being an essential vector of operational resilience.
