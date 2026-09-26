---
id: kpis-metricas-deploy
title: KPIs and Metrics - Secure Deployment
sidebar_position: 10
description: Technical and operational indicators for the assessment of the effectiveness of the security controls in the deployment process and release management, with thresholds by risk level and mapping to the cross-cutting SbD-ToE governance dimensions.
tags: [kpi, metricas, DPL, deploy, release, break-glass, rollback, L1, L2, L3]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/addon/10-kpis-metricas.md
  source_sha256: c45039608f1617fb6c2289a13d0819928d215887177d4c525d6884ebe649596d
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: fb86e8887f3b0ec812ebd5660ab07db0af5caead302c584b4c401dff3a715e24
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 112d795f9bd927f0d4c24114e389470217eb00c1d6b919ae2df2e4f7bdb4878d
  glossary_keys: [audit_trail, avaliacao, discipline, framework_source_corpus, mapping, risk_level, sbdtoe_sbd, traceability, transversal, verification_taxonomy]
  glossary_sha256: 49d24a87c78aab8aadc094bde8dedd2f8fa0ad044b777e1c0b9cbd64e682e2ad
  translated_at: 2026-09-26T11:00:52Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# KPIs and Metrics - Secure Deployment

## Scope and purpose {#âmbito-e-propósito}

The indicators of this domain assess the **security of the deployment process and release management**: the coverage of pre-deployment validations, the control and traceability of emergency deployments (break-glass), the quality of deployment evidence artefacts, and the effective separation of configuration between environments.

Deployment is the moment at which the implemented controls become effective - or fail. The DPL indicators focus on the discipline of the process: a deployment without a validated security checklist is not necessarily insecure, but it is a deployment without evidence that security was verified. That distinction is auditable and relevant.

The DPL indicators feed the cross-cutting dimensions **T-01 (Control coverage)** and **T-02 (Exception health)**.

---

## Denominator and portfolio foundation {#denominador-e-fundação-de-portfólio}

The indicators of this domain use as their denominator **F-02 - applications with a formal risk classification** (Ch. 01, CLA-K01). The percentages are interpretable only in relation to the set of applications classified at the relevant risk level - not in relation to the total portfolio or to ad-hoc subsets.

See `kpis-governanca.md` - section "Portfolio foundation" - for the SbD-ToE adoptability funnel and the relation between denominators.

---

## Conventions {#convenções}

| Symbol | Meaning |
|---------|-------------|
| ✔ | Mandatory threshold for this level |
| - | Not applicable or not mandatory at this level |
| ↓ | Inverse indicator - a lower value indicates better performance |

Thresholds are cumulative: L3 includes all the obligations of L1 and L2.

**Indicator types:**

| Code | Meaning |
|--------|-------------|
| Q% | Quantitative, percentage |
| Q# | Quantitative, count |
| Qt | Quantitative, temporal (hours/days) |

---

## Indicator catalogue {#catálogo-de-indicadores}

| ID | Indicator | Type | L1 | L2 | L3 | Dim. T | Period |
|----|-----------|:----:|:--:|:--:|:--:|:------:|---------|
| DPL-K01 | % of production deployments with a validated and recorded pre-deployment security checklist | Q% | ≥ 70% | ≥ 95% | 100% | T-01 | Per release |
| DPL-K02 | % of emergency deployments (break-glass) with post-facto approval recorded in less than 24h | Q% | 100% | 100% | 100% | T-02 | Per event |
| DPL-K03 | % of emergency deployments with notification to the CISO (or equivalent) carried out before or during the deployment | Q% | - | 100% | 100% | T-02 | Per event |
| DPL-K04 | # of production rollbacks for security reasons per quarter | Q# | mandatory record | ≤ 2 | ≤ 1 | T-03 | Quarterly |
| DPL-K05 | % of production environments with verified separation of secrets and configuration from non-production | Q% | - | ≥ 90% | 100% | T-01 | Half-yearly |
| DPL-K06 | % of releases with a traceable deployment evidence artefact (pipeline ID, artefact hash, timestamp) | Q% | ≥ 70% | ≥ 95% | 100% | T-01 | Per release |
| DPL-K07 | % of emergency deployments with a security post-mortem carried out in less than 5 working days | Q% | - | ≥ 80% | 100% | T-02 | Per event |

---

## Complementary definitions {#definições-complementares}

**DPL-K01 - Validated checklist:** a checklist is considered validated when it: (a) was completed by the technical owner of the deployment; (b) includes verification of the pipeline's security gates; (c) is associated with the deployment identifier (pipeline run ID, ticket, change record). Generic checklists with no association to the specific deployment do not satisfy this criterion.

**DPL-K02 - Emergency deployment (break-glass):** any deployment that bypasses one or more mandatory security gates, or that is carried out outside the change management process defined for L2/L3 systems. Post-facto approval is an exception to the normal process - it is not a permanent alternative. The 24h deadline is absolute; there is no extension.

**DPL-K03 - Notification to the CISO:** for L3 systems, the notification must be made in real time (during the deployment) or before. For L2 systems, it may be post-event but within the 24h of DPL-K02. The notification channel (email, Slack, ticket) is free; the evidence of notification is mandatory.

**DPL-K04 - Rollback for security reasons:** includes rollbacks initiated by: discovery of a vulnerability in production, failure of a security control after deployment, insecure configuration detected after deployment, or instruction from the CISO/AppSec. Rollbacks for other reasons (performance, functional bugs) do not enter this indicator.

**DPL-K05 - Configuration separation:** the separation is considered verified when: (a) production secrets are not accessible in non-production environments; (b) production-specific environment variables do not exist in staging/dev; (c) the verification was carried out by technical audit (configuration scan or IaC review) with recorded evidence.

**DPL-K07 - Security post-mortem:** must include: the timeline of the event, the root cause, the security impact (actual and potential), corrective actions with an owner and a deadline, and a review of the process that allowed the emergency deployment. Post-mortems without a security root cause analysis do not satisfy this criterion.

---

## Collection and instrumentation {#recolha-e-instrumentação}

| Indicator | Primary source | Reference tools | Automation |
|-----------|---------------|--------------------------|-----------|
| DPL-K01 | Change management system + pipeline logs | Jira, ServiceNow + pipeline (GitHub Actions, GitLab) | Partial |
| DPL-K02 | Emergency deployment register + approval system | Change record + exception register | No |
| DPL-K03 | Notification log + communication record | Email/Slack with timestamp + GRC register | No |
| DPL-K04 | Change management system + incident tracking | Jira, PagerDuty, ServiceNow | Partial |
| DPL-K05 | Configuration audit + IaC review | Environment variable audit + IaC scan | Partial |
| DPL-K06 | Pipeline logs + release register | CI/CD platform (run ID, artefact hash, timestamp) | Yes |
| DPL-K07 | Post-mortem repository | Confluence, GitHub (post-mortem templates) | No |

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|-----------|---------|
| `addon/00-catalogo-requisitos.md` | Requirements DPL-001..009 that underpin the indicators |
| `addon/09-excecoes-deploy.md` | Break-glass process and post-facto approval (DPL-K02/K03/K07) |
| `addon/04-validacoes-pre-deploy.md` | Pre-deployment security checklist (DPL-K01) |
| Ch. 14 `addon/kpis-governanca.md` | Cross-cutting dimensions T-01, T-02 |
