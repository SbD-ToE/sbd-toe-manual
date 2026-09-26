---
id: policies-relevantes
title: Policies
description: Policies required to support logging, detection and continuous response practices.
tags: [policy, organizacional, monitorizacao, deteccao, resposta, operacoes]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/policies-relevantes.md
  source_sha256: 761ce76d56f7920b98ea9a2c2167c631ced3eb56d9e4b4a0a5622fdb6b620e95
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: e5639de46a84e06b96fefe7778ef94c31d5eeaaab88f8acfcb0a7169cce4600d
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: ebb6c6bf48bf281085379aa982dcfe014d642265f07b08070d51366e58764173
  glossary_keys: [chapter_role, cycle_iteration, lifecycle_phase, maturity]
  glossary_sha256: cb3678cf0362a9c66766c626a784d8b9238542bda3d36bdeb7ee7808053c826f
  translated_at: 2026-09-26T11:17:38Z
  reviewed_by: null
---


# Organisational Policies - Monitoring and Operations

The effective adoption of **Chapter 12 - Monitoring and Operations** requires the existence of **formal organisational policies** that regulate and sustain **detection, correlation and response to security events in real time**.

---

## 📌 Fundamental note {#-nota-fundamental}

> ⚠️ The practices described in this chapter - structured logging, alert rules, event correlation, IRP integration, MTTD/MTTR measurement - **must be underpinned by clear, auditable organisational policies applicable to all operational environments**.

These policies:

- Make the technical application of monitoring practices **mandatory and measurable**;
- Establish **responsibilities for triage, escalation and incident response**;
- Ensure that **operational visibility is coherent and effective across all systems and pipelines**;
- Serve as a reference for **audits, post-incident analyses and continuous improvement of operational maturity**.

---

## 🧾 Recommended policies {#-políticas-recomendadas}

| Policy Name                                 | Mandatory? | Application                                 | Summary of required content                                                  |
|--------------------------------------------------|--------------|--------------------------------------------|---------------------------------------------------------------------------------|
| [Monitoring and Logging Policy](/sbd-toe/assets/policies/policy-logging-estruturado)              | ✅ Yes        | All services and applications             | Definition of events, logging levels, structured formats, centralised destinations. |
| [Alerting and Behaviour Detection Policy](/sbd-toe/assets/policies/policy-gestao-alertas)  | ✅ Yes        | Critical systems and production environments  | Types of sensitive events, thresholds, false-positive tolerance, response. |
| [Service Observability Policy](/sbd-toe/assets/policies/policy-monitorizacao-seguranca)          | ⚠️ Optional  | Microservices and distributed architectures  | Minimum metrics, mandatory dashboards, correlation with logs.                |
| [Log Retention and Access Policy](/sbd-toe/assets/policies/policy-logging-estruturado)         | ✅ Yes        | All security and operations logs      | Retention ≥30 days, ACL, encryption, access logging.                          |
| [Operational Incident Response Policy](/sbd-toe/assets/policies/policy-irp)   | ✅ Yes        | All domains with active detection        | Response channels, playbooks, reporting, domain owners.                     |
| [Agent Coverage and Instrumentation Policy](/sbd-toe/assets/policies/policy-monitorizacao-seguranca)| ⚠️ Optional  | Infrastructure, cloud, endpoints           | Types of mandatory agents, minimum coverage, maintenance of visibility.   |

---

## 🧱 Expected structure of each policy {#-estrutura-esperada-de-cada-política}

Each organisational policy must contain:

- **Objective and scope** (which systems or environments it covers);
- **Types of events or conditions monitored** (e.g. failed login, privilege escalation);
- **Rules for triage, escalation and mitigation**;
- **Minimum log retention and the corresponding format and security**;
- **Coverage required from agents or technical sensors**;
- **Integration with the development and response lifecycle**;
- **Periodicity of policy review, testing and audit**.

---

## ✅ Final recommendations {#-recomendações-finais}

- Policies must be **reviewed regularly** based on the evolution of threats and of the architecture;
- They must be **accessible to and understood by all technical and operational teams**;
- They must be **reflected in CI/CD practices, in production environments and in release requirements**;
- They must be **validated by internal audits and supported by continuous evidence (dashboards, tested alerts, visible logs)**.

> 📌 Well-defined policies are the foundation for **effective operational observability and reaction** - without them, even the most instrumented systems remain vulnerable to silent failures.
