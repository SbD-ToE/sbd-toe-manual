---
id: kpis-dominio-governacao
title: Domain KPIs - Governance and Contracting
sidebar_position: 13
description: Technical and process indicators specific to the domain of organisational security governance (GOV), with thresholds by risk level and mapping to the cross-cutting governance dimensions of SbD-ToE.
tags: [kpi, metricas, GOV, governanca, excecoes, ownership, contratos, fornecedores, L1, L2, L3]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/addon/13-kpis-dominio-gov.md
  source_sha256: 2133f17ac6b1e2583f743c9967aaf282124e6e4d75e168b85859f9b14e498cf7
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 15a9863db0203f8bb76fa7a43f7752e20754ae7b6ded8ad13edf7672d313f822
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [alcada, avaliacao, cycle_iteration, discipline, framework_source_corpus, mapping, programme_line, risk_level, sbdtoe_sbd, traceability, transversal, validation_evaluation]
  glossary_sha256: e260d703dd327d6940b9413ec21c716b5d2fe8a8b799e32af2a4408a0d949b10
  translated_at: 2026-09-26T12:00:20Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Domain KPIs - Governance and Contracting

## Scope and purpose {#âmbito-e-propósito}

The indicators of this domain assess the **health and effectiveness of the organisational security governance structure**: ownership coverage per application, the quality and validity of active exceptions, contractual compliance with suppliers, and the completeness of organisational traceability.

The GOV domain is the only one whose indicators measure the **governance process itself**, not the technical controls that this process governs. An indicator such as "% of exceptions with a complete chain of authority" does not measure technical security - it measures the discipline with which the organisation manages the deviations from security that it has decided to accept. That discipline is, in itself, a control.

These indicators complement the cross-cutting KPIs defined in `kpis-governanca.md` and feed directly into the dimensions **T-02 (Exception health)**, **T-04 (Ownership)** and **T-05 (Supply chain)**.

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
| Bin | Binary - verifiable existence with mandatory evidence |

---

## Indicator catalogue {#catálogo-de-indicadores}

| ID | Indicator | Type | L1 | L2 | L3 | Dim. T | Period |
|----|-----------|:----:|:--:|:--:|:--:|:------:|---------|
| GOV-K01 | % of applications with a security owner formally designated, registered and with valid training (&lt; 12 months) | Q% | 100% | 100% | 100% | T-04 | Quarterly |
| GOV-K02 | % of active exceptions with a complete chain of authority (who requested, who assessed, who approved) | Q% | 100% | 100% | 100% | T-02 | Monthly |
| GOV-K03 | % of active exceptions with a defined expiry date and a scheduled reassessment date | Q% | ≥ 80% | 100% | 100% | T-02 | Monthly |
| GOV-K04 | # of expired exceptions without formal renewal (must be treated as active non-compliance) | Q# ↓ | = 0 | = 0 | = 0 | T-02 | Weekly |
| GOV-K05 | % of contracts with suppliers of L2/L3 systems with signed security clauses proportional to the risk | Q% | ≥ 80% | 100% | 100% | T-05 | Half-yearly |
| GOV-K06 | % of L3 suppliers with the annual security validation completed and documented | Q% | - | - | 100% | T-05 | Annual |
| GOV-K07 | % of applications with complete and up-to-date organisational traceability (risk → requirements → exceptions → owner) | Q% | - | ≥ 80% | 100% | T-04 | Quarterly |
| GOV-K08 | % of deviations identified in continuous validation cycles with a corrective action assigned to an owner with a deadline | Q% | ≥ 80% | 100% | 100% | T-02 | Per cycle |

---

## Complementary definitions {#definições-complementares}

**GOV-K01 - Owner with valid training:** valid training is the completion of a training programme in SbD-ToE (or an organisational equivalent) within the last 12 months. Owners designated without valid training count towards the denominator but not towards the numerator. Team turnover is the main trigger of invalidity.

**GOV-K02 - Complete chain of authority:** an exception has a complete chain of authority when the record explicitly identifies: (a) who requested the exception (name and function); (b) who carried out the risk assessment (name and function); (c) who approved it (name, function and an approval authority proportional to the risk level). The documentary medium is free (ticket, GRC, wiki, ADR) - traceability is mandatory.

**GOV-K03 - Exception with scheduled reassessment:** the reassessment date must be recorded in the traceability system and must be earlier than or equal to the expiry date. Exceptions with an expiry date but without a scheduled reassessment do not fully satisfy this indicator.

**GOV-K04 - Expired exception:** an exception is considered expired on the day after its expiry date without formal renewal. Expired exceptions without renewal are equivalent to active non-compliance and must be treated with the same SLA as a critical finding.

**GOV-K05 - Clauses proportional to the risk:** proportionality is assessed by the correspondence between the risk level of the integrated application and the clauses applied, as defined in `addon/02-clausulas-contratuais.md`. Contracts with generic clauses without security specificity do not satisfy this criterion.

**GOV-K07 - Complete traceability:** traceability is considered complete when the organisational record (per application) reflects the current status of: (a) risk classification; (b) requirements applied per domain; (c) active exceptions with a reference; (d) a designated and active owner. Records out of date for more than one review cycle do not satisfy this criterion.

**GOV-K08 - Deviation with corrective action:** a deviation identified in a continuous validation review has a corrective action assigned when there is: a ticket or record with an owner, a resolution deadline, and follow-up planned in the next cycle. Deviations recorded without an owner or a deadline do not satisfy this criterion.

---

## Collection and instrumentation {#recolha-e-instrumentação}

| Indicator | Primary source | Instrumentation support | Automation |
|-----------|---------------|--------------------------|-----------|
| GOV-K01 | Register of owners + training record | GRC, HRIS, training platform | Partial |
| GOV-K02 | Exception management system (GRC, Jira, wiki) | Audit of mandatory fields | Partial |
| GOV-K03 | Exception management system | Automatic alerts for imminent expiry | Partial |
| GOV-K04 | Exception management system + calendar | Automatic scan of expiry dates | Yes |
| GOV-K05 | Contract repository + GRC | Contractual audit + clauses checklist | No |
| GOV-K06 | Register of supplier validations | GRC + onboarding questionnaires | No |
| GOV-K07 | Organisational traceability register | Audit of field completeness | Partial |
| GOV-K08 | Continuous validation records + backlog | Review cycles with tracking of actions | Partial |

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|-----------|---------|
| `addon/00-catalogo-requisitos.md` | Requirements GOV-001..012 on which the indicators are based |
| `addon/12-processo-excecoes.md` | Canonical exception process (GOV-K02/K03/K04) |
| `addon/02-clausulas-contratuais.md` | Contractual proportionality criteria (GOV-K05) |
| `addon/03-modelo-validacao-fornecedores.md` | Annual supplier validation (GOV-K06) |
| `addon/06-validacao-continuada.md` | Review cycles that produce deviations (GOV-K08) |
| `addon/kpis-governanca.md` | Cross-cutting dimensions T-02, T-04, T-05 |
