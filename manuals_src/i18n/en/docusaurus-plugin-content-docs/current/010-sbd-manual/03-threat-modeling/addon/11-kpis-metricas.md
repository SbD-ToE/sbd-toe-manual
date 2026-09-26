---
id: kpis-metricas-threat-modeling
title: KPIs and Metrics - Threat Modelling
sidebar_position: 11
description: Technical and process indicators for assessing the coverage, quality and integration of threat modelling in the development cycle, with thresholds by risk level and mapping to the cross-cutting SbD-ToE governance dimensions.
tags: [kpi, metricas, THR, threat-modeling, ameacas, L1, L2, L3]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/addon/11-kpis-metricas.md
  source_sha256: 80db15bdd6932964d1d3ed2ed8278bafe04194342a054b7cb573716261423235
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: 4781945a6512071c54e160e7503b75da86efbb71c5266ecbd5d0c3ee498872d3
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [avaliacao, chapter_role, cycle_iteration, framework_source_corpus, gap_family, mapping, maturity, microsoft_threat_modeling_tool, practitioner_manual, requirement_runtime, risk_level, sbdtoe_sbd, slug_threat_modeling, threat, traceability, transversal, validation_evaluation]
  glossary_sha256: ed6c925dce3a58d8b99b3808551625275c3e4c1dfaf548cc2eab7326b80a80c6
  translated_at: 2026-09-26T12:48:41Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# KPIs and Metrics - Threat Modelling

## Scope and purpose {#âmbito-e-propósito}

The indicators of this domain assess the **coverage, currency and operational quality of the threat modelling process** in the software development cycle. Threat modelling is the mechanism by which threats are identified before they become exploitable vulnerabilities - it is structured risk analysis applied to the architecture, before implementation.

Measuring threat modelling faces a specific challenge: the quality of a threat model is not directly observable through simple quantitative metrics. An extensive threat model may be superficial; a concise threat model may be exhaustive. The THR indicators combine coverage metrics (quantitative) with process quality indicators (ordinal and binary) that are observable without requiring subjective line-by-line assessment.

The THR indicators feed the cross-cutting dimensions **T-01 (Control coverage)** and **T-06 (SbD-ToE maturity)**.

---

## Denominator and portfolio foundation {#denominador-e-fundação-de-portfólio}

The THR indicators use as their denominator **F-02 - applications with a formal risk classification** (Ch. 01, CLA-K01). The percentages in this chapter are interpretable only in relation to the set of applications classified at the relevant risk level - not in relation to the total portfolio or to ad-hoc subsets.

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
| Ord | Qualitative, ordinal (level 1–3) |
| Bin | Binary - verifiable existence with mandatory evidence |

---

## Indicator catalogue {#catálogo-de-indicadores}

| ID | Indicator | Type | L1 | L2 | L3 | Dim. T | Period |
|----|-----------|:----:|:--:|:--:|:--:|:------:|---------|
| THR-K01 | % of L2/L3 applications with a documented, up-to-date and accessible threat model | Q% | - | ≥ 85% | 100% | T-01 | Half-yearly |
| THR-K02 | % of threats identified in the threat model with an associated control or formally accepted risk | Q% | - | ≥ 90% | 100% | T-01 | Per threat model |
| THR-K03 | % of threat models of L2/L3 systems reviewed by AppSec before going into production | Q% | - | ≥ 80% | 100% | T-01 | Per major release |
| THR-K04 | % of threat models updated within ≤ 30 days after a significant architectural change | Q% | - | ≥ 85% | 100% | T-01 | Per event |
| THR-K05 | % of threats identified in the threat model mapped to canonical SbD-ToE requirements | Q% | - | ≥ 70% | ≥ 90% | T-01 | Per threat model |
| THR-K06 | Maturity level of the threat modelling process (methodology, integration, tools) | Ord | level 1 | level 2 | level 3 | T-06 | Annual |

---

## Complementary definitions {#definições-complementares}

**THR-K01 - Up-to-date threat model:** a threat model is considered up to date when it reflects the current architecture and has been reviewed after the last significant architectural change or within the maximum period of the defined cycle. The tool is free (manual STRIDE, IriusRisk, Threat Dragon, Microsoft Threat Modeling Tool); the evidence of review is mandatory.

**THR-K02 - Associated control or accepted risk:** each threat must have an explicit disposition - (a) control implemented with a reference to the requirement; (b) mitigation in progress with a deadline; or (c) risk formally accepted with an owner and a record. Threats without a disposition are process gaps, not conscious risk positions.

**THR-K03 - Review by AppSec:** the review may be carried out as part of a security design review, an ADR review, or a formal threat model review process. The criterion is the existence of a reviewer with security competence who is independent of the team that produced the threat model.

**THR-K04 - Significant architectural change:** includes the same categories defined in CLA-K03 (Ch. 01): new data types, new external integrations, architecture changes with impact on the attack surface, regulatory changes. The 30-day period is for updating the threat model, not for resolving the threats identified.

**THR-K05 - Mapping to canonical requirements:** a threat is mapped when the line can be traced between the identified threat and the SbD-ToE requirement that mitigates it (e.g. privilege escalation threat → AUT-003, AUT-007). The mapping may be automatic (IriusRisk) or manual and documented. Threats without a mapping indicate a potential gap in requirements coverage.

**THR-K06 - Threat modelling maturity levels:**
- Level 1: threat modelling carried out ad hoc, without a defined methodology, without integration in the development cycle
- Level 2: defined methodology (STRIDE, PASTA, or another), carried out on new systems and significant changes, with documented output reviewed by AppSec
- Level 3: integrated in the development pipeline (ideally continuous or per PR/release), with automatic mapping to requirements, traceability of threats over time, and evidence of evolution compared with previous cycles

---

## Collection and instrumentation {#recolha-e-instrumentação}

| Indicator | Primary source | Reference tools | Automation |
|-----------|---------------|--------------------------|-----------|
| THR-K01 | Threat model repository (wiki, Git, dedicated tool) | IriusRisk, Threat Dragon, Microsoft TMT | Partial |
| THR-K02 | Threat model with a disposition column per threat | Any tool with threat + mitigation tracking | Partial |
| THR-K03 | Record of reviews (tickets, comments, minutes) | Ticketing system + review record | No |
| THR-K04 | Correlation between the change log and the threat model review date | Audit of git log vs threat model date | No |
| THR-K05 | Threat model with a requirement field per threat | IriusRisk (automatic mapping), or manual table | Partial |
| THR-K06 | Qualitative assessment by AppSec or security architect | Annual structured assessment | No |

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|-----------|---------|
| `addon/01-metodologias-e-ferramentas.md` | Methodologies and tools that underpin THR-K06 |
| `addon/03-validacao-evidencia-threat-modeling.md` | Validation process that feeds THR-K03/K05 |
| `addon/07-mapeamento-threats-requisitos.md` | Threat → requirement mapping (THR-K05) |
| Ch. 04 `addon/10-kpis-metricas.md` | ARC-K01 (threat model per architecture) complements THR-K01 |
| Ch. 14 `kpis-governanca.md` | Cross-cutting dimensions T-01, T-06 |
