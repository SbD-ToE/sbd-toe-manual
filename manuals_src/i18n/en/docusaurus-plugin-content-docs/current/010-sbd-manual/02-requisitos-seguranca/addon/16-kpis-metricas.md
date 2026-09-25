---
id: kpis-metricas-requisitos
title: KPIs and Metrics - Security Requirements
sidebar_position: 16
description: Technical and process indicators for assessing the coverage, traceability and effective validation of the security requirements applied by risk level, with mapping to the cross-cutting SbD-ToE governance dimensions.
tags: [kpi, metricas, RQS, requisitos, rastreabilidade, cobertura, L1, L2, L3]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/02-requisitos-seguranca/addon/16-kpis-metricas.md
  source_sha256: 03af6b58e9639eadee6c3d24db60904a2957f9650b1c509bde6e07e0495cd629
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 4d1d9314133d3296c0a14ce26b0ed1f2a2465a6c66cc8b895a7b7d6061ba165a
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [avaliacao, cycle_iteration, framework_source_corpus, gap_family, layer, mapping, maturity, requirement_runtime, risk_level, sbdtoe_sbd, traceability, transversal, validation_evaluation]
  glossary_sha256: 56b389efb6c662a9afc5acb3cf4e54a5390a6c47d0073df97ed569c7c649c7a4
  translated_at: 2026-09-25T20:20:14Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# KPIs and Metrics - Security Requirements

## Scope and purpose {#âmbito-e-propósito}

The indicators of this domain assess the **effective application, traceability and validation of the security requirements** defined in the SbD-ToE catalogue. The requirements catalogue is the link between the risk classification (Ch. 01) and the technical controls implemented in the domain chapters (Ch. 04–12). Without this link, the technical domains operate without a normative reference, and governance has no basis on which to assess compliance.

The specific risk of this domain is declarative compliance: an application may list the requirements applied without these being effectively implemented or validated. The RQS indicators measure not only the declaration but the evidence of validation.

The RQS indicators feed the cross-cutting dimensions **T-01 (Control coverage)** and **T-06 (SbD-ToE maturity)**.

---

## Denominator and portfolio foundation {#denominador-e-fundação-de-portfólio}

The RQS indicators use as their denominator **F-02 - applications with a formal risk classification**, defined in Ch. 01 (`addon/12-kpis-metricas.md`, CLA-K01). RQS-K01 establishes F-03 - applications with mapped requirements - which in turn is the denominator of the next layer of the SbD-ToE adoptability funnel.

The interpretation of any RQS percentage assumes that F-02 is complete for the risk level in question. See `kpis-governanca.md` - section "Portfolio foundation".

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

---

## Indicator catalogue {#catálogo-de-indicadores}

| ID | Indicator | Type | L1 | L2 | L3 | Dim. T | Period |
|----|-----------|:----:|:--:|:--:|:--:|:------:|---------|
| RQS-K01 | % of applications with security requirements formally mapped to the classified risk level | Q% | ≥ 80% | ≥ 95% | 100% | T-01 | Half-yearly |
| RQS-K02 | % of mandatory requirements per level with evidence of implementation or a documented formal exception | Q% | ≥ 70% | ≥ 90% | ≥ 98% | T-01 | Per release |
| RQS-K03 | % of applied requirements with complete traceability (requirement → control implemented → test evidence) | Q% | - | ≥ 75% | ≥ 95% | T-01 | Half-yearly |
| RQS-K04 | % of L2/L3 applications with formal requirements validation carried out in the last release cycle | Q% | - | ≥ 85% | 100% | T-01 | Per release |
| RQS-K05 | % of requirements with the acceptance criterion verified (tested or audited) vs only declared as applied | Q% | - | ≥ 70% | ≥ 90% | T-01 | Half-yearly |
| RQS-K06 | # of requirements mandatory for the risk level with no implementation and no formal exception (ungoverned gaps) | Q# ↓ | = 0 | = 0 | = 0 | T-01 | Per release |

---

## Complementary definitions {#definições-complementares}

**RQS-K01 - Formal mapping:** a mapping is considered formal when it identifies, per application: (a) the classified risk level; (b) the mandatory requirements for that level in each relevant domain; (c) the status of each requirement (applied, excepted, not applicable with justification). Requirements tables without an up-to-date status do not satisfy this criterion.

**RQS-K02 - Evidence of implementation:** the evidence may be technical (scanner result, validation log, pipeline output) or procedural (review record, release checklist, audit result). The evidence must be traceable to the specific requirement, not generic to the application.

**RQS-K03 - Complete traceability:** the requirement → control → evidence chain is complete when it is possible to start from a canonical requirement (e.g. AUT-003) and reach concrete evidence that it is implemented in the application in question. Partial traceability (requirement declared but no control identified) does not satisfy this criterion.

**RQS-K04 - Cycle validation:** formal requirements validation must be an explicit event in the release process, with documented output. It may be integrated into a release checklist, an AppSec review, or an automated pipeline with a report. Implicit validation ("CI runs, therefore it is validated") does not satisfy this criterion without explicit traceability to the requirement.

**RQS-K05 - Verified vs declared criterion:** a requirement is "verified" when the acceptance criterion defined in the catalogue has been assessed with evidence (test, scan, audit). It is "declared" when the owner states that it is applied without traceable evidence. RQS-K05 measures the proportion of requirements in the verified state vs the total of requirements declared as applied.

**RQS-K06 - Ungoverned gap:** a requirement is an ungoverned gap when it is mandatory for the application's risk level, is not implemented, and has no active formal exception. This situation amounts to an active non-compliance and must be handled with the same SLA as a critical finding.

---

## Collection and instrumentation {#recolha-e-instrumentação}

| Indicator | Primary source | Instrumentation support | Automation |
|-----------|---------------|--------------------------|-----------|
| RQS-K01 | Requirements register per application (GRC, wiki, ALM) | Requirements matrix per application | Partial |
| RQS-K02 | Requirements register + evidence + exception register | GRC integrated with pipeline and findings management | Partial |
| RQS-K03 | Traceability system (ALM, structured wiki) | Chain completeness audit | No |
| RQS-K04 | Release register + validation checklists | Release log + validation output | Partial |
| RQS-K05 | Requirements register with an evidence field | Audit of the "evidence" vs "declared" field | No |
| RQS-K06 | Requirements register + register of active exceptions | Automatic cross-check between the catalogue and the status per application | Partial |

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|-----------|---------|
| `addon/02-lista-requisitos-base.md` | Canonical catalogue and mapping of prefixes by domain |
| `addon/03-taxonomia-rastreabilidade.md` | Traceability model underpinning RQS-K03 |
| `addon/07-validacao-requisitos.md` | Requirements validation process (RQS-K04/K05) |
| `addon/08-gestao-excecoes.md` | Excepted requirements (RQS-K02, RQS-K06) |
| Ch. 14 `addon/kpis-governanca.md` | Cross-cutting dimensions T-01, T-06 |
