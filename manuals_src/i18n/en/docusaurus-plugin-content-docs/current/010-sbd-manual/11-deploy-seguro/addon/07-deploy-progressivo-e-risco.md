---
id: deploy-progressivo-e-risco
title: Progressive Deployment and Risk Control
description: Practices such as canary releases, blue/green and staged rollout to mitigate risk in critical deployments.
tags: [tipo:anexo, grupo:execucao, tema:deploy-progressivo, risco, staging]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/addon/07-deploy-progressivo-e-risco.md
  source_sha256: a968d52d14e41e0d9cfb4b8d867566128cbf0ffd87114623bb6cfc11c2814074
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 11953b4d8692b5f82ab9dce8fb6cff67c6fd760040d2f7d232e6f18f79c9ea0b
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 112d795f9bd927f0d4c24114e389470217eb00c1d6b919ae2df2e4f7bdb4878d
  glossary_keys: [avaliacao, chapter_role, lifecycle_phase, maturity, validation_evaluation]
  glossary_sha256: 72a53dfae40ec0ddffd1c72ef58eb013e94bfbab2fca5f045c03cf9ae242be4f
  translated_at: 2026-09-26T11:00:50Z
  reviewed_by: null
---


# Progressive Deployment and Risk Assessment

Progressive deployment is an essential practice for mitigating risks during the delivery of new software versions. It allows a **gradual and controlled exposure** of functionality, with the capacity to **measure impact, gather feedback and stop quickly** in case of error.

---

## 🔄 Common progressive deployment models {#-modelos-comuns-de-deploy-progressivo}

| Strategy           | Description                                                                 | Advantages                                  |
|----------------------|---------------------------------------------------------------------------|--------------------------------------------|
| **Canary Release**   | Delivery to a small percentage of users                       | Detecting errors with reduced impact         |
| **Blue/Green Deploy**| Two parallel environments: the new one is activated after validation                 | Fast rollback, no downtime             |
| **Shadow Traffic**   | Routes traffic to the new system without a response to the user                | Realistic tests without direct impact         |
| **Feature Flags**    | Activates functionality at runtime for controlled segments                 | Flexible, reversible, segmentable           |

---

## 🚨 Risk assessment in progressive releases {#-avaliação-de-risco-em-releases-progressivas}

Before starting a progressive rollout, a **formal assessment of the release risk** must be carried out, based on:

- Severity of the changes (breaking changes, new flows)
- History of the component / team
- Reversibility and rollback coverage
- Maturity of the automated tests
- Level of exposure and potential impact

> 📊 High-risk releases must **start in canary + gated environments**.

---

## 🌐 Rollout control {#-controlo-do-rollout}

- **Common scopes**:
  - Percentage of users (e.g. 1%, 5%, 20%)
  - Segments by geo / tenant / profile / device
  - Time period (e.g. active for 3 hours)

- **Blocking / rollback criteria**:
  - Latency > X ms
  - 5xx errors > Y%
  - Security alerts or anomalous spikes

---

## 🔹 Integration with pipelines {#-integração-com-pipelines}

- Define gates per rollout segment (canary, general availability)
- Monitor events by release hash and active toggle
- Automate promotion between stages with validations
- Integrate security validations into the process (e.g. unexpected behaviour)

---

## 👨‍💻 Team responsible for the rollout {#-equipa-responsável-pelo-rollout}

| Role          | Key responsibilities                              |
|----------------|-----------------------------------------------------------|
| DevOps         | Implements the rollout and rollback strategy               |
| QA / AppSec    | Defines the blocking criteria and validates the result           |
| Product        | Defines the functional scope, approves the promotion                 |
| Engineering     | Monitors behaviour and acts if there is an incident       |

---

## ✅ Secure rollout checklist {#-checklist-de-rollout-seguro}

- [ ] Does the release have a defined rollout plan?
- [ ] Are there success / error metrics for monitoring?
- [ ] Is the rollout reversible at each phase?
- [ ] Is there documentation of the initial scope and the promotion criteria?
- [ ] Are the toggles visible and controlled by an owner?
- [ ] Are the responsible teams identified for each stage?

> 🌟 A good rollout is a technical + organisational process, not just a configuration in the pipeline.
