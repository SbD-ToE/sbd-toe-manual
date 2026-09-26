---
id: kpis-metricas-formacao
title: KPIs and Metrics - Training and Onboarding
sidebar_position: 11
description: Technical and process indicators for the assessment of the effectiveness, coverage and impact of the security training and onboarding programme, with thresholds by risk level and mapping to the cross-cutting SbD-ToE governance dimensions.
tags: [kpi, metricas, TRN, formacao, onboarding, champions, L1, L2, L3]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/addon/11-kpis-metricas.md
  source_sha256: 0201793f053a19aa7c8ddd21094582b56fe5a1866638e258c4115ca1bd026b04
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: 1bf61338d077e6e6766e0f19bdc120e7cb077149b273ad8f8b442723e3991f06
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [avaliacao, framework_source_corpus, gap_family, mapping, mcp_reading_programa, programme_line, requirement_runtime, risk_level, sbdtoe_sbd, transversal]
  glossary_sha256: 003b36c90a58f5ead594d43759f36018025633f3bf8db9de4bed72c270474e3c
  translated_at: 2026-09-26T12:49:00Z
  stamped_at: 2026-09-26T18:35:58Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# KPIs and Metrics - Training and Onboarding

## Scope and purpose {#âmbito-e-propósito}

The indicators of this domain assess the **effectiveness, coverage and measurable impact of the security training and onboarding programme**. Training is an organisational control, not a compliance event: its value lies in observable behaviour change, not in the completion of modules.

The measurement of training faces a causality problem - it is difficult to attribute a reduction in incidents exclusively to training. The TRN indicators approach this problem from two angles: (a) coverage and process indicators that are directly observable and controllable; and (b) impact indicators that establish observable correlations between training and technical behaviour, without requiring exclusive causality.

The TRN indicators feed the cross-cutting dimension **T-04 (Ownership coverage)**, which aggregates the training of those responsible for critical security functions.

> This file defines the indicators in the canonical SbD-ToE format. The file `90-indicadores-metricas.md` contains a lighter operational synthesis for the teams' day-to-day use.

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
| Qt | Quantitative, temporal (days) |
| Mixed | Combination of a quantitative component and contextual assessment |

---

## Indicator catalogue {#catálogo-de-indicadores}

| ID | Indicator | Type | L1 | L2 | L3 | Dim. T | Period |
|----|-----------|:----:|:--:|:--:|:--:|:------:|---------|
| TRN-K01 | % of new members of staff with security onboarding completed within ≤ 7 working days of starting | Q% | ≥ 90% | ≥ 95% | 100% | T-04 | Monthly |
| TRN-K02 | % of security owners and exception approvers with valid SbD training (≤ 12 months) | Q% | ≥ 80% | ≥ 95% | 100% | T-04 | Quarterly |
| TRN-K03 | % of suppliers with access to code, pipelines or data of L2/L3 systems with security training or a security questionnaire completed before onboarding | Q% | - | ≥ 90% | 100% | T-04 | Per onboarding |
| TRN-K04 | % of training content updated after a significant change to the requirements catalogue or to the threat model | Q% | ≥ 80% | 100% | 100% | T-04 | Per change |
| TRN-K05 | # of security incidents with a root cause attributed to an identified and unaddressed training gap | Q# ↓ | = 0 | = 0 | = 0 | T-04 | Per incident |
| TRN-K06 | % of PRs/commits in L2/L3 systems that repeat security patterns identified in training (absorption proxy) | Q% | - | ≥ 75% | ≥ 90% | T-04 | Quarterly |
| TRN-K07 | % of teams with at least one active Security Champion with valid training (≤ 12 months) | Q% | - | ≥ 80% | 100% | T-04 | Quarterly |

---

## Complementary definitions {#definições-complementares}

**TRN-K01 - Onboarding completed:** onboarding is considered completed when the member of staff has completed the mandatory security module (defined in the training catalogue `addon/01-catalogo-formativo.md`) and there is a traceable record of completion with a date. Partial or in-progress modules do not satisfy this criterion.

**TRN-K02 - Valid SbD training:** training completed within the last 12 months is considered valid. Critical functions include: security owners, exception approvers, those responsible for production releases, and architecture reviewers. The list of critical functions must be defined in the organisational training policy.

**TRN-K03 - Supplier with training:** for suppliers of L3 systems, the requirement is security training or a security questionnaire specific to the context (not generic). For L2 systems, a documented security questionnaire is sufficient. The criterion for complete supplier onboarding is defined in Ch. 14 `addon/03-modelo-validacao-fornecedores.md`.

**TRN-K04 - Updated content:** content is out of date when: (a) it references revoked or changed requirements; (b) it does not reflect changes in the threat catalogue relevant to the domain; or (c) it has gone more than 24 months without review. The deadline for updating after a significant change to the catalogue is 90 days.

**TRN-K05 - Incident with a training root cause:** an incident has a training root cause when the post-mortem analysis identifies that: (a) the behaviour that gave rise to the incident was covered by existing training content; and (b) the member of staff involved had not completed the training or had let it expire. This indicator must tend towards zero, and any non-zero value is an immediate warning sign.

**TRN-K06 - Absorption of patterns (proxy):** this indicator measures the proportion of PRs/commits that follow the secure-code patterns identified as priorities in training (e.g. not using deprecated cryptographic functions, not building queries by concatenation, not hardcoding secrets). Measurement requires the prior definition of the patterns measurable by a code scanner.

**TRN-K07 - Active Security Champion:** a champion is considered active when they: (a) have valid training (≤ 12 months); (b) have taken part in at least one security review or awareness activity in the last 90 days; (c) are the point of contact known to the team for security questions. Formal designation without activity does not satisfy this criterion.

---

## Collection and instrumentation {#recolha-e-instrumentação}

| Indicator | Primary source | Instrumentation support | Automation |
|-----------|---------------|--------------------------|-----------|
| TRN-K01 | Training platform + start date (HRIS) | LMS (Moodle, Docebo, etc.) + HRIS | Yes |
| TRN-K02 | Training record + list of critical functions | LMS + GRC register of owners/approvers | Partial |
| TRN-K03 | Supplier onboarding record + training platform | GRC + questionnaire register | No |
| TRN-K04 | Content review history (git log, LMS versioning) | LMS with content version control | Partial |
| TRN-K05 | Incident database + post-mortem reports | IR system + root cause analysis | No |
| TRN-K06 | Code scanner with priority-pattern rules | Semgrep (custom rules), SonarQube | Yes |
| TRN-K07 | Champions register + activity register | Wiki/GRC + log of participation in reviews | No |

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|-----------|---------|
| `addon/01-catalogo-formativo.md` | Mandatory content that defines the baseline of TRN-K01/K02 |
| `addon/03-programa-champions.md` | Champion activity criteria (TRN-K07) |
| `addon/90-indicadores-metricas.md` | Operational synthesis of metrics for the teams' day-to-day use |
| Ch. 14 `addon/03-modelo-validacao-fornecedores.md` | Supplier training requirements (TRN-K03) |
| Ch. 14 `kpis-governanca.md` | Cross-cutting dimension T-04 (ownership and training) |
