---
id: kpis-metricas-arquitetura
title: KPIs and Metrics - Secure Architecture
sidebar_position: 10
description: Technical and process indicators for assessing the effectiveness of secure architecture controls, with thresholds per risk level and a mapping to the SbD-ToE cross-cutting governance dimensions.
tags: [kpi, metricas, ARC, arquitectura, threat-model, L1, L2, L3]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/addon/10-kpis-metricas.md
  source_sha256: 393e75183cbbaba85957eb68f1dba988ae4b091eac2d5ba8269ceb6243f7e95f
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: 7187129e5f798385386aadefbd665e85077d224714b4d522fbc8e78ce0364fa7
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [avaliacao, cycle_iteration, framework_source_corpus, layer, lifecycle_phase, mapping, maturity, requirement_runtime, risk_level, sbdtoe_sbd, traceability, transversal, travessia_generica, travessia_relacao, validation_evaluation, verification_taxonomy]
  glossary_sha256: 0c482b7c3fb6daf7fe5ee29d511633c40527883c3fa7c87386fef32e3c4dac52
  translated_at: 2026-09-26T12:48:42Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# KPIs and Metrics - Secure Architecture

## Scope and purpose {#âmbito-e-propósito}

The indicators of this domain assess the **effective application of security architecture decisions and controls** throughout the lifecycle of applications. Architecture is a predominantly qualitative domain - what is measured is not the code produced, but the existence, currency and traceability of structural security decisions.

An architecturally secure system is not merely one that implements the correct controls. It is one that demonstrates **why** it implements them, **who** decided on them, and **what happens** when the premises change. Those elements are observable and auditable.

The ARC indicators feed the cross-cutting dimensions **T-01 (Control coverage)**, **T-04 (Ownership)** and **T-06 (SbD-ToE maturity)**.

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
| Ord | Qualitative, ordinal (level 1–3, aligned with L1/L2/L3) |
| Bin | Binary - verifiable existence with mandatory evidence |

---

## Indicator catalogue {#catálogo-de-indicadores}

| ID | Indicator | Type | L1 | L2 | L3 | Dim. T | Period |
|----|-----------|:----:|:--:|:--:|:--:|:------:|---------|
| ARC-K01 | % of applications with a threat model documented, reviewed and updated in the last assessment cycle | Q% | - | ≥ 80% | 100% | T-01 | Half-yearly / per major release |
| ARC-K02 | % of security architecture decisions with an ADR recorded and traceable to a canonical ARC requirement | Q% | - | ≥ 70% | ≥ 95% | T-01 | Per release |
| ARC-K03 | % of communication flows between distinct trust zones without encryption in transit (should tend to zero) | Q% ↓ | - | = 0% | = 0% | T-01 | Quarterly |
| ARC-K04 | % of architecture reviews with formal AppSec participation before going into production | Q% | - | ≥ 80% | 100% | T-01, T-04 | Per release |
| ARC-K05 | Level of defence-in-depth implementation per application (multiple independent layers of control) | Ord | level 1 | level 2 | level 3 | T-06 | Annual |
| ARC-K06 | % of critical components without documented and verified blast radius isolation | Q% ↓ | - | ≤ 20% | = 0% | T-01 | Half-yearly |

---

## Complementary definitions {#definições-complementares}

**ARC-K01 - Threat model:** a threat model is considered "reviewed and updated" when it reflects the current architecture and has been subject to formal review after the last significant architectural change or within the maximum period defined by the domain's assessment cycle (half-yearly for L2; per major release for L3). Tool and format are free; the evidence is mandatory.

**ARC-K02 - Traceable ADR:** an ADR (Architecture Decision Record) is considered traceable if it identifies the ARC requirement it responds to, the owner of the decision, the date and the context that motivated it. ADRs without an associated requirement do not count towards this indicator.

**ARC-K05 - Defence-in-depth levels:**
- Level 1: perimeter access control and basic logging
- Level 2: network segmentation, per-layer authentication, anomaly detection
- Level 3: controls at each layer with independent verification, zero-trust per zone, auditability of all crossings

**ARC-K06 - Blast radius:** documentation demonstrating that the compromise of one component does not propagate without restriction. It may include: network isolation, minimum permissions, circuit breakers, or formal failure propagation analysis.

---

## Collection and instrumentation {#recolha-e-instrumentação}

| Indicator | Primary source | Possible automation |
|-----------|---------------|-------------------|
| ARC-K01 | Documentation repository (wiki, Git) | Partial - presence of the file; currency requires human validation |
| ARC-K02 | ADR repository (Git, Confluence) | Partial - count of ADRs with the `requisito` field filled in |
| ARC-K03 | Network scans / IaC review / penetration tests | Yes - traffic analysis tools or policy-as-code in IaC |
| ARC-K04 | Review records (tickets, minutes, PR comments) | Partial - presence of an AppSec label/reviewer on the PR |
| ARC-K05 | Qualitative assessment by AppSec or a security architect | No - requires periodic structured assessment |
| ARC-K06 | Architecture documentation + IaC review | Partial - validation of network policies and permissions in IaC |

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|-----------|---------|
| `addon/01-catalogo-requisitos.md` | Requirements ARC-001..013 that underpin the indicators |
| `addon/06-rastreabilidade.md` | Threat→requirement→ADR→control→evidence traceability model |
| `addon/03-excecoes.md` | Deviations from ARC controls require a formal exception |
| Ch. 14 `kpis-governanca.md` | Cross-cutting dimensions T-01, T-04, T-06 |
