---
id: kpis-kri-executivo
title: Risk Indicators - Executive View
sidebar_position: 88
description: Eight key risk indicators for reporting to the CISO, senior management and the board. Focus on risk exposure and response capability, aggregating the technical indicators of the SbD-ToE domains into an actionable executive reading.
tags: [kri, executivo, ciso, board, dashboard, risco, governacao]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/kpis-kri-executivo.md
  source_sha256: 03407345a715efd962af50e6e06169438b85c924fb8f497e049394d70b0135e7
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 6ddd053f27e2eae3b89579e6d64fb1a25a5eac326b01c500611ff40a96ab9629
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [alcada, avaliacao, chapter_role, cycle_iteration, mcp_reading_programa, papel_suporte, programme_line, risk_level, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: 1373fc8c0608265b333d70ac68786a865da562a6d991b47855c3616e84b703bd
  translated_at: 2026-09-26T12:00:27Z
  stamped_at: 2026-09-26T18:36:29Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Risk Indicators - Executive View

## What this document is for {#para-que-serve-este-documento}

The SbD-ToE programme produces dozens of detailed technical indicators - one per domain, per chapter, per type of control. That detail is necessary for the operational teams, but it is not the right reading for senior management or the board.

This document presents **eight risk indicators** that answer the questions management needs to see answered: does the organisation know what it has? are the critical applications protected? if something goes wrong, can we detect and react in time?

The eight indicators are a **curated subset** of the technical indicators - they create no new measurement, they synthesise what the domains already measure.

> **Reading note:** The targets vary according to the risk level of the application - L1 (low risk), L2 (medium risk), L3 (high or critical risk). The most critical systems have higher requirements.

---

## The eight indicators - quick view {#os-oito-indicadores---visão-rápida}

| # | Question | L1 | L2 | L3 | Reviewed |
|---|----------|----|----|----|---------|
| 1 | Do we have all applications catalogued and classified by risk? | 100% | 100% | 100% | Quarterly |
| 2 | Does each application have an identified security owner? | 100% | 100% | 100% | Quarterly |
| 3 | How many applications in production are free of known critical flaws? | ≥ 70% | ≥ 90% | 100% | Monthly |
| 4 | Are there exposed credentials or expired risk authorisations? | = 0 | = 0 | = 0 | Weekly |
| 5 | How long does it take to detect a security incident? | ≤ 24h | ≤ 4h | ≤ 30 min | Monthly |
| 6 | How long does it take to react after detecting the incident? | ≤ 48h | ≤ 4h | ≤ 1h | Monthly |
| 7 | Do the teams have up-to-date security training? | ≥ 80% | ≥ 90% | 100% | Quarterly |
| 8 | Have the critical applications been tested by an independent entity? | - | ≥ 80% | 100% | Half-yearly |

---

## How to read the traffic light {#como-ler-o-semáforo}

| Colour | Meaning |
|-----|-------------|
| **Green** | Target met for the risk level of the applications concerned |
| **Amber** | Result between 80% and 99% of the target - degradation detected, still without non-compliance |
| **Red** | Result below 80% of the target - or any non-zero value in indicator 4 |

For the time indicators (5 and 6): amber = up to twice the target; red = above twice the target.

---

## Each indicator in detail {#cada-indicador-em-detalhe}

---

### 1 - Portfolio inventory and classification {#1---inventário-e-classificação-do-portfólio}

**The question:** do we know how many applications we have and the risk level of each one?

Without a complete inventory with assigned risk levels, all the other indicators lose validity - there is no reliable denominator for calculating percentages, nor any way of knowing whether the right controls are in the right places. This is the base indicator of the whole programme.

**Target:** 100% of applications classified, at all risk levels. An application without classification is, by definition, an unmanaged risk.

**When it is red, the question to ask:** is there an active inventory and classification process? Who is responsible for keeping it up to date?

*Technical reference: CLA-K01 (Ch. 01 - Application Classification)*

---

### 2 - Accountability per application {#2---responsabilidade-por-aplicação}

**The question:** for each application, is there a named individual responsible for its security?

Without an identified owner, there is no escalation point when something goes wrong, no one to answer in an audit, and no one to ensure that the controls are maintained over time. Diffuse accountability is equivalent to the absence of accountability.

**Target:** 100% of applications with a named owner, with a formal role and approval authority. Applications without an owner must be escalated immediately.

**When it is red, the question to ask:** does the application onboarding process include the appointment of an owner? Is there a periodic review when there is team turnover?

*Technical reference: GOV-K01 (Ch. 14 - Governance and Contracting)*

---

### 3 - Exposure to critical flaws in production {#3---exposição-a-falhas-críticas-em-produção}

**The question:** how many of our applications in production have known serious security flaws that have not yet been fixed?

Known critical flaws - publicly identified, with a published vulnerability database - are the most exploited vector in attacks. An application with an unfixed critical flaw is operating with an open door whose address is public. This indicator aggregates exposure across two vectors: the software libraries and components the applications use, and the operating system and runtime images on which they run.

**Target:** L1 ≥ 70%, L2 ≥ 90%, L3 = 100% of applications without unmitigated critical flaws. Formal documented exceptions with technical compensation are admissible - flaws without any record of treatment are not.

**When it is red, the question to ask:** are the processes for updating dependencies and base images automatic or manual? What is the average time between the publication of a critical flaw and its remediation?

*Technical reference: Dependencies (Ch. 05) + Containers (Ch. 09)*

---

### 4 - Controls that can never fail {#4---controlos-que-nunca-podem-falhar}

**The question:** are there access credentials exposed in code, or risk authorisations that have already expired without renewal?

Two controls whose only acceptable value is zero - not "few", not "being resolved", but zero:

- **Exposed credentials not rotated:** passwords, access tokens, encryption keys or certificates found in code repositories or automation systems, without the access having been invalidated. The risk is immediate and the damage may be irrecoverable.
- **Expired risk authorisations:** exceptions to security controls that were approved with a defined deadline and whose deadline has passed without renewal or closure. They represent controls that the organisation consciously decided not to apply - and then forgot.

**Target:** zero in both, at all risk levels. Any non-zero value triggers the red traffic light and requires immediate action.

**When it is red, the question to ask:** are there automatic processes for detecting exposed credentials? Is there an active inventory of all approved exceptions with an expiry date?

*Technical reference: Secure development (Ch. 06) + Governance and Contracting (Ch. 14)*

---

### 5 - Detection speed {#5---velocidade-de-detecção}

**The question:** when an incident or attack occurs, how much time passes before we know?

The time that elapses between an attack and its detection determines the size of the damage. An attack detected in minutes can be contained; an attack that goes unseen for weeks can compromise the entire infrastructure. This indicator measures the effectiveness of the monitoring and alerting systems - not the number of alerts, but the speed with which real events are flagged.

**Target:** L1 ≤ 24 hours, L2 ≤ 4 hours, L3 ≤ 30 minutes - for high or critical severity events.

**When it is red, the question to ask:** do the critical systems have active centralised monitoring? Are the alerts calibrated to the organisation's context or are they the tools' default values?

*Technical reference: OPS-K03 (Ch. 12 - Monitoring and Operations)*

---

### 6 - Response speed {#6---velocidade-de-resposta}

**The question:** once the incident has been detected, how much time passes before the organisation acts?

Detecting an incident does not solve the problem - it is the response that limits the damage. This indicator measures the time between the alert and the first concrete containment action: isolation of systems, blocking of access, activation of a response plan. Detecting quickly and reacting late is as dangerous as not detecting.

**Target:** L1 ≤ 48 hours, L2 ≤ 4 hours, L3 ≤ 1 hour - for high or critical severity events.

**Reading together with indicator 5:** high detection speed with low response speed points to a lack of operational capability or of response processes; the problem is not the monitoring technology, it is the incident response organisation.

*Technical reference: OPS-K04 (Ch. 12 - Monitoring and Operations)*

---

### 7 - Team training {#7---formação-das-equipas}

**The question:** do the people who develop and operate the systems have up-to-date security knowledge?

Most security incidents originate in human error - a wrong configuration, an insecure code pattern, a decision taken without knowledge of its implications. Security training is the lowest-cost, highest-impact investment in reducing this risk. "Up to date" means carried out or renewed in the last year - training from three years ago does not cover current threats.

**Target:** L1 ≥ 80%, L2 ≥ 90%, L3 = 100% of teams with up-to-date training.

**When it is red, the question to ask:** is there a training plan with a defined cycle? Is training mandatory or voluntary? Is there tracking of who completed it and when?

*Technical reference: TRN-K01 (Ch. 13 - Training and Onboarding)*

---

### 8 - Independent validation {#8---validação-independente}

**The question:** have the most critical applications been tested by someone from outside the organisation?

Internal security processes validate that the controls exist - but they do not guarantee that they are effective against a real adversary. An independent assessment - penetration test, architecture review by an external entity, red team exercise - provides the perspective that internal processes cannot give: that of someone actively trying to compromise the system. For L2 and L3 systems, this validation is part of the reasonable assurance that senior management and the board need to have.

**Target:** not applicable to L1; L2 ≥ 80%, L3 = 100% with an independent assessment in the last 12 months.

**When it is red, the question to ask:** is there a budget and a process for independent security testing? Is the scheduling based on risk level or is it ad hoc?

*Technical reference: TST-K02 (Ch. 10 - Security Testing)*

---

## Situations that require immediate attention {#situações-que-requerem-atenção-imediata}

The following conditions require the CISO's attention regardless of the usual review period:

| Situation | Minimum action |
|----------|-------------|
| Exposed credentials not invalidated (indicator 4) | Immediate notification to the CISO; forced invalidation in less than 24 hours |
| Risk authorisations expired for more than 7 days (indicator 4) | Review of the exception portfolio; forced renewal or closure |
| Response time to an active incident above twice the target (indicator 6) | Response escalation; activation of the contingency plan |
| Less than 95% of applications classified (indicator 1) | Suspend new starts without prior classification; activate an urgent process |
| L3 application without an independent assessment for more than 18 months (indicator 8) | Activate a priority security test |

---

## When an indicator is red - where to analyse {#quando-um-indicador-está-vermelho---onde-analisar}

The executive view does not include root-cause detail - that is in the technical domain indicators. When an indicator is red, the in-depth analysis is done here:

| Indicator | Where to find the detail |
|-----------|--------------------------|
| 1 - Classification | Ch. 01 - Application Classification |
| 2 - Accountability | Ch. 14 - Governance and Contracting |
| 3 - Critical flaws | Ch. 05 - Dependencies and SBOM; Ch. 09 - Containers |
| 4 - Absolute controls | Ch. 06 - Secure Development; Ch. 14 - Governance and Contracting |
| 5 - Detection; 6 - Response | Ch. 12 - Monitoring and Operations |
| 7 - Training | Ch. 13 - Training and Onboarding |
| 8 - Independent validation | Ch. 10 - Security Testing |

For the full architecture of the measurement hierarchy, see [`kpis-arquitetura-visao-geral`](./kpis-arquitetura-visao-geral). For the full technical catalogue of indicators per domain, see [`kpis-governanca`](./kpis-governanca).
