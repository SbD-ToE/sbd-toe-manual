---
id: exemplos-eventos
title: Examples of Events Relevant to Monitoring
sidebar_position: 9
description: Catalogue of typical events to monitor for operational and security purposes.
tags: [eventos, logging, segurança, observabilidade, catálogo]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/addon/09-exemplos-eventos.md
  source_sha256: f11cec6e100bc16890d8eddd1b43c09add29450685160042ce0e0430a2649e99
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: fe3702fbc492c294905eec297b3248ecd9daec14abc7c80f67c46f9785897b3a
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: ebb6c6bf48bf281085379aa982dcfe014d642265f07b08070d51366e58764173
  glossary_keys: [chapter_role, mapping, threat]
  glossary_sha256: 03d9b6d6908c0c801610fdd0178da14ec514065465496f699ffd47c35faa0f5d
  translated_at: 2026-09-26T11:17:30Z
  reviewed_by: null
---


# Threats Mitigated by Monitoring and Operations

## 🌟 Objective {#-objetivo}

To map the attack vectors that can be **detected, anticipated or correlated** by the practices described in this chapter, contributing to response capacity and to the improvement of the security posture.

---

## 📊 Threat categories addressed {#-categorias-de-ameaça-abordadas}

| Category (OSC\&R / ATT\&CK)         | Summary description                             |
| ------------------------------------ | ---------------------------------------------- |
| **Credential abuse**             | Use of compromised passwords or tokens          |
| **Brute force / guessing**           | Repeated authentication attempts           |
| **Privilege escalation / tampering** | Improper elevation or alteration of permissions   |
| **Access abuse / insider misuse**    | Illegitimate use of valid access               |
| **Data exfiltration**                | Unauthorised outflow of data                  |
| **Pipeline compromise**              | Improper execution in CI/CD pipelines           |
| **Configuration tampering**          | Modification of parameters or secrets           |
| **Availability sabotage (DoS)**      | Suspicious inactivity, loss of logs, sabotage |

---

## 🔍 Mapping practices → mitigated threats {#-mapeamento-práticas--ameaças-mitigadas}

| Monitoring practice                 | Mitigated threats                    |
| ---------------------------------------- | ------------------------------------ |
| Logging of authentications and failures        | Brute force, credential abuse    |
| Alerts for out-of-profile logins         | Insider misuse, improper use         |
| Correlation: role change + config change  | Privilege escalation, tampering      |
| Monitoring of uploads/downloads       | Exfiltration, lateral movement       |
| Detecting unusual executions in the pipeline | Compromise in CI/CD             |
| Logging of structured exceptions         | Reconnaissance, probing, bug hunting |
| Alert on loss of logs or inactivity   | Sabotage, forwarding tampering   |

---

## 📄 Examples of practical coverage {#-exemplos-de-cobertura-prática}

| Identified threat        | Indicative event(s)                            | Associated practice                     |
| -------------------------- | ------------------------------------------------ | ------------------------------------- |
| **Brute force**            | >10 failures in 3 min from one IP                      | Threshold alerts, auth logs          |
| **Compromised token**     | Login with a valid token outside the usual country     | Correlation with IP/geolocation      |
| **Privilege abuse**        | User creation + secret change            | Logging + correlation between sources     |
| **Silent exfiltration** | High data transfer off-hours             | Behavioural detection               |
| **Log sabotage**      | Loss of logs + change to the forwarder config | Inactivity alerts + system logs |

---

## ✅ Final recommendations {#-recomendações-finais}

* Use this mapping as the basis for the **justification of monitoring controls**;
* Relate directly to OSC\&R / MITRE ATT\&CK in coverage plans and threat modelling;
* Prioritise threats with **high impact and low visibility without active logging**.

> 🧠 Monitoring is not blocking - it is **detecting and reacting in time**. Visibility is the first step of resilience.
