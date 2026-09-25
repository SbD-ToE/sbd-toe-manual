---
id: kpis-metricas-classificacao
title: KPIs and Metrics - Application Classification
sidebar_position: 12
description: Technical and process indicators for assessing the quality, coverage and currency of application risk classification, with thresholds per risk level and mapping to SbD-ToE cross-cutting governance dimensions.
tags: [kpi, metricas, CLA, classificacao, risco, L1, L2, L3]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/addon/12-kpis-metricas.md
  source_sha256: 016d5cd62b7af002c89710043c1b5bdfc41956381f02bfe10577c259ef421daf
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 461b335f94e5ef03d5f3f35f7d9e3e40e39958ba28120509e136ecc5b19ef20e
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [alcada, avaliacao, cycle_iteration, framework_source_corpus, mapping, maturity, programme_line, risk_level, sbdtoe_sbd, transversal, validation_evaluation]
  glossary_sha256: 7e949b678f0f1294401594e5b96bbdf77262fb43b3b3ce769164e7b215c2dee2
  translated_at: 2026-09-25T20:18:50Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# KPIs and Metrics - Application Classification

## Scope and purpose {#âmbito-e-propósito}

The indicators in this domain assess the **quality, coverage and currency of the application risk classification process**. Classification is the starting point of the entire SbD-ToE model: without a correct classification, the requirements applied are the wrong ones, exceptions carry inadequate approval authority, and controls are not proportional to the real risk.

Classification is not a one-off event - it is a continuous process that must reflect architectural, regulatory or functional changes. A system classified as L1 that has evolved to process large-scale personal data and was never reclassified is not an L1 system: it is an L3 system with L1 controls.

The CLA indicators feed the cross-cutting dimensions **T-01 (Control coverage)** and **T-06 (SbD-ToE maturity)**.

---

## Denominator and portfolio foundation {#denominador-e-fundação-de-portfólio}

The CLA indicators are the **origin of the denominator** for all domain KPIs of the SbD-ToE programme. CLA-K01 establishes F-02 - the inventory of applications classified by risk level, which serves as the shared denominator for all chapters. Without a complete and up-to-date CLA-K01, the percentages of the other chapters have no interpretable basis.

The relationship is direct: F-01 (total inventory) and F-02 (classified by level) are absolute metrics that precede any domain percentage. See `kpis-governanca.md` - section "Portfolio foundation".

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
| Q% | Quantitative percentage |
| Q# | Quantitative count |
| Qt | Quantitative temporal (days) |
| Bin | Binary - verifiable existence with mandatory evidence |

---

## Indicator catalogue {#catálogo-de-indicadores}

| ID | Indicator | Type | L1 | L2 | L3 | Dim. T | Period |
|----|-----------|:----:|:--:|:--:|:--:|:------:|---------|
| CLA-K01 | % of portfolio applications with a formal risk classification documented and accessible | Q% | 100% | 100% | 100% | T-01 | Quarterly |
| CLA-K02 | % of classifications reviewed within the cycle defined per level (L3: quarterly; L2: half-yearly; L1: annual) | Q% | ≥ 90% | ≥ 95% | 100% | T-01 | Per cycle |
| CLA-K03 | % of applications with a significant change (architecture, data, regulation) whose classification was updated within ≤ 30 days | Q% | ≥ 80% | ≥ 95% | 100% | T-01 | Per event |
| CLA-K04 | % of L2/L3 system classifications validated by AppSec or GRC (not only the owner's self-assessment) | Q% | - | ≥ 90% | 100% | T-01 | Half-yearly |
| CLA-K05 | % of applications with residual risk formally documented and accepted by an owner with proportional authority | Q% | - | ≥ 85% | 100% | T-01 | Half-yearly |
| CLA-K06 | # of applications classified as L1 without review in the last 12 months and with a significant functional change recorded | Q# ↓ | = 0 | = 0 | = 0 | T-01 | Half-yearly |

---

## Supplementary definitions {#definições-complementares}

**CLA-K01 - Documented classification:** a classification is considered documented when it includes: (a) the risk level assigned (L1/L2/L3); (b) the criteria that determined the level (data type, exposure, criticality); (c) the owner responsible for the classification; (d) the date of the last review. Informal or verbal classifications do not satisfy this criterion.

**CLA-K02 - Review cycles per level:**
- L3: quarterly review or at each major release, whichever occurs first
- L2: half-yearly review or at each major release that changes the attack surface
- L1: annual review or after any significant functional change

**CLA-K03 - Significant change:** includes any of the following: (a) introduction of new types of personal or sensitive data; (b) integration with new external or third-party systems; (c) architecture change with impact on the attack surface; (d) change in the applicable regulatory context; (e) security incident revealing an underestimation of risk.

**CLA-K04 - Validation by AppSec/GRC:** validation may be carried out in a formal review, in the application onboarding process, or in an audit cycle. The criterion is the existence of a second pair of eyes with competence and independence relative to the application owner.

**CLA-K05 - Accepted residual risk:** residual risk is the risk that remains after the controls have been applied. Its formal acceptance requires: identification of the requirements not applied or partially applied, justification, compensating measures, and approval by an owner with authority proportional to the risk level (see Ch. 14 `addon/12-processo-excecoes.md`).

**CLA-K06 - Undetected under-classification:** this indicator is intended to detect situations in which an L1 application has evolved functionally without reclassification. Detection may be based on: changelog audit, review of product tickets, or analysis of integration with new systems.

---

## Collection and instrumentation {#recolha-e-instrumentação}

| Indicator | Primary source | Instrumentation support | Automation |
|-----------|---------------|--------------------------|-----------|
| CLA-K01 | Application inventory / CMDB / GRC | Centralised application register | Partial |
| CLA-K02 | Classification register + review dates | GRC with review-expiry alerts | Partial |
| CLA-K03 | Change management system + classification register | Correlation between change tickets and reclassification date | No |
| CLA-K04 | Review register with validator identification | GRC + approval register | No |
| CLA-K05 | Residual risk register per application | GRC / risk decision repository | No |
| CLA-K06 | L1 application inventory + functional change log | Cross-audit between CMDB and changelog | No |

---

## Cross-references {#referências-cruzadas}

| Document | Relationship |
|-----------|---------|
| `addon/01-modelo-classificacao-eixos.md` | Classification model and criteria underpinning CLA-K01/K03 |
| `addon/04-risco-residual.md` | Residual risk documentation process (CLA-K05) |
| `addon/02-ciclo-vida-risco.md` | Review cycles that define the CLA-K02 thresholds |
| Ch. 14 `addon/12-processo-excecoes.md` | Residual risk acceptance (CLA-K05) |
| Ch. 14 `addon/kpis-governanca.md` | Cross-cutting dimensions T-01, T-06 |
