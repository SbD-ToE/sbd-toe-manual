---
id: policy-monitorizacao-pos-deploy
title: Post-Deployment Monitoring Policy
description: Organisational policy that defines the requirements for active monitoring after each deploy to production, including a mandatory observation window, minimum health metrics, alert thresholds, human validation and rollback activation criteria, proportional to the criticality level (L1, L2, L3).
tags: [policy, monitorização, pós-deploy, observabilidade, alertas, rollback, saúde, métricas, cap11, L1, L2, L3, governance]
grupo: operacoes
sidebar_position: 28
translation:
  source_locale: pt
  source_path: 020-assets/policies/28_policy-monitorizacao-pos-deploy.md
  source_sha256: fb501e56323533844f6cb2633ad35a10c524cada1be80b56c290f2f155224d5c
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: abb7d05bf04d9b0c927f15157c7088ef35fc2c7287973d8b4811ea7e6ac79ac1
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bc04ded428e40ee1c214f8535dfb1904655b64166d0aa82b5df521e4230b8cb0
  glossary_keys: [cycle_iteration, practitioner_manual, sbdtoe_sbd, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: df18abde5f32351b8d45735867e238e0b6e02fb1eb66b4b827b4fa749b7bc9d9
  translated_at: 2026-09-26T14:11:00Z
  reviewed_by: null
---

# Post-Deployment Monitoring Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for **active monitoring after each deploy to production**, covering the mandatory observation window, the minimum metrics and alerts, human validation and the criteria for automatic rollback activation.

During the post-deploy window, this policy uses the continuous health/readiness/availability signals defined in [`OPS-015`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-015); it does not replace the obligation of continuous monitoring in production outside the deploy window.

A deploy does not end with the successful promotion of the artefact - it ends when the version is stable in production and its behaviour has been verified. Without active post-deploy monitoring, anomalies can develop silently for hours before being detected by users or by external systems. The post-deploy window is the period of highest risk of a release: it is when unexpected behaviours under real production load manifest themselves.

The objective of this policy is to ensure that:

- Each deploy to production is followed by an active observation window with metrics and alerts configured
- Anomalies are detected and classified automatically, with routing for response
- Human validation of the health status is carried out before the release is closed
- The rollback activation criteria are predefined and applied consistently

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

| Level | Applicability |
|---|---|
| L1 | Recommended; basic health check monitoring |
| L2 | Mandatory; defined observation window; automatic alerts; human validation |
| L3 | Mandatory; complete monitoring; automatic response to critical anomalies; formal human validation |

---

## 3. Post-deploy observation window {#3-janela-de-observação-pós-deploy}

After each deploy to production, there must be an active observation window during which the operations team actively monitors the behaviour of the new version:

| Level | Minimum observation window | Activity during the window |
|---|---|---|
| L1 | 15 minutes | Manual verification of health checks |
| L2 | 30 minutes | Dashboard monitoring; alerts configured; on-call available |
| L3 | 60 minutes (or until the first complete rollout cycle in progressive deploys) | Active monitoring; automatic rollback criteria active; on-call available |

During deploys with progressive rollout (canary, blue-green), the observation window applies to each promotion stage.

---

## 4. Minimum health metrics {#4-métricas-de-saúde-mínimas}

The following metrics must be configured and being monitored during the post-deploy observation window:

| Metric | Description | Alert threshold (reference) |
|---|---|---|
| HTTP 5xx error rate | Percentage of responses with a server error | > 1% for 5 minutes |
| P99 latency | 99th percentile of response time | > 2x the baseline of the last 7 days |
| Crash/restart rate | Number of container/process restarts per minute | > threshold defined per service |
| Health check endpoint | Status of the `/health` endpoint or equivalent | Failure in ≥ 2 consecutive instances |
| Throughput | Number of requests per second vs baseline | Drop > 30% against the baseline without explanation |
| Authentication/authorisation errors | Anomalous increase in 401/403 | > 5x baseline for 5 minutes |

The specific thresholds must be calibrated per service on the basis of historical behaviour.

---

## 5. Alerts and routing {#5-alertas-e-encaminhamento}

Post-deploy alerts must be configured before any deploy to production - not configured after a problem is detected:

- [ ] Alerts associated with the deployment for the period of the observation window
- [ ] Alerts routed to an active on-call channel (not only email)
- [ ] Alerts clearly identify the deployment that originated them (version, deploy timestamp)
- [ ] Alerts classified by severity with a defined response SLA:
  - Critical: response in ≤ 5 minutes
  - High: response in ≤ 15 minutes
  - Medium: response in ≤ 60 minutes

---

## 6. Post-deploy rollback activation criteria {#6-critérios-de-activação-de-rollback-pós-deploy}

The automatic rollback criteria must be predefined and configured for the observation window:

| Criterion | Action |
|---|---|
| 5xx error rate > threshold during a defined window | Automatic rollback (L2/L3) or alert for human decision (L1) |
| P99 latency > 2x baseline during a defined window | Immediate alert; rollback if it persists after 10 minutes |
| Health check with persistent failure | Automatic rollback |
| Crash loop in instances/pods | Automatic rollback |
| Active security alert (runtime anomaly) | Immediate alert; human rollback decision |

Automatic rollback must be accompanied by immediate notification to the on-call and a record of the automated decision.

---

## 7. Post-deploy human validation {#7-validação-humana-pós-deploy}

At L2/L3, the deploy is only considered complete after explicit human validation of the health status:

- [ ] The on-call owner checks dashboards and confirms normal status
- [ ] Documented verification (timestamp, identity, observed status)
- [ ] If anomalies are detected but do not reach automatic rollback thresholds, the decision to keep or revert is human and recorded
- [ ] Release marked as "complete" only after positive validation

---

## 8. Post-deploy monitoring dashboards {#8-dashboards-de-monitorização-pós-deploy}

Monitoring dashboards must be configured and updated before each deploy:

- [ ] Dashboard specific to post-deploy with real-time metrics and comparison with the previous version
- [ ] Filter by active version/deployment
- [ ] Visualisation of the progressive rollout window (if applicable)
- [ ] History of previous deploys for comparison

---

## 9. Extension of the observation window {#9-extensão-da-janela-de-observação}

If, during the observation window, anomalies are detected that do not reach the rollback threshold but cause uncertainty, the window must be extended:

- [ ] Extension decision recorded with justification
- [ ] New duration of the window defined
- [ ] On-call kept available during the extension

---

## 10. Traceability {#10-rastreabilidade}

Each relevant event during the observation window must be recorded:

| Event | Record |
|---|---|
| Start of the observation window | Timestamp + deployed version + responsible on-call |
| Alert generated | Type, severity, timestamp, affected metric |
| Rollback decision (automatic or manual) | Criterion activated, timestamp, target version |
| Human validation completed | Identity, timestamp, observed status |
| Closure of the window | Timestamp + final status (complete, rollback, under extended observation) |

---

## 11. Responsibilities {#11-responsabilidades}

| Role | Responsibility |
|---|---|
| DevOps / SRE | Configure dashboards and alerts before the deploy; monitor during the window; execute rollback if necessary |
| On-Call | Respond to alerts within the SLAs; take the rollback decision when necessary; validate the post-deploy status |
| Tech Lead | Coordinate the response to anomalies; decide on rollback when the on-call escalates |
| AppSec Engineer | Define the security metrics to be monitored post-deploy; review security anomaly alerts |
| GRC / Compliance | Audit post-deploy observation records; verify compliance with windows and SLAs |

---

## 12. Review and audit of this policy {#12-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Incident in which a post-deploy anomaly was not detected within the observation window
- Change of the monitoring platform that affects the dashboards or alerts
- Change to the incident response SLAs

---

## 13. Normative and technical references {#13-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 11 - Secure Deployment | US-06 (post-deploy monitoring), US-13 (human validation) |
| SbD-ToE Ch. 12 - [`OPS-015`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-015) | Continuous health/readiness/availability signal consumed during the post-deploy window |
| Secure Deployment Policy (`25_policy-deploy-seguro.md`) | Rollout strategies and promotion criteria |
| Rollback Policy (`27_policy-rollback.md`) | Rollback process activated by monitoring |
| Security Monitoring Policy (`30_policy-monitorizacao-seguranca.md`) | Security monitoring in production |
| Alert Management Policy (`31_policy-gestao-alertas.md`) | Alert response SLAs |
| Site Reliability Engineering (Google SRE Book) | Monitoring practices and SLO/SLA |
| NIST SP 800-61 | Computer Security Incident Handling Guide |
