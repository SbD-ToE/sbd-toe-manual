---
id: kpis-metricas-dependencias
title: KPIs and Metrics - Dependencies, SBOM and SCA
sidebar_position: 10
description: Technical and operational indicators for the assessment of the effectiveness of the controls for dependency management, SBOM generation and software composition analysis, with thresholds per risk level and mapping to the cross-cutting SbD-ToE governance dimensions.
tags: [kpi, metricas, DEP, sbom, sca, dependencias, cve, supply-chain, L1, L2, L3]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/addon/10-kpis-metricas.md
  source_sha256: 9a1494a5907537dee035a3718973f523c947df4885856033103360e810715d43
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: 2fbe2954b35a6504e086f1baa00c40145578ad9e23303a082864db43712d11e5
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [avaliacao, framework_source_corpus, mapping, practitioner_manual, risk_level, sbdtoe_sbd, snyk_license, traceability, transversal]
  glossary_sha256: 20ba8acde860b8d1572a6ab7662ac94fa868798e283c1c9d4717832a59ec58af
  translated_at: 2026-09-26T12:48:43Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# KPIs and Metrics - Dependencies, SBOM and SCA

## Scope and purpose {#âmbito-e-propósito}

The indicators of this domain assess the **capacity of an organisation to know, control and react to the risk introduced by software dependencies**. Dependency management is a highly quantifiable domain: the SBOM is a structured artefact, CVEs have normalised CVSS scores, and remediation deadlines are traceable with temporal precision.

The absence of visibility over dependencies is not a neutral position - it is the implicit acceptance of unquantified risk. These indicators turn that risk into actionable data.

The DEP indicators feed the cross-cutting dimensions **T-01 (Control coverage)**, **T-03 (Resolution speed)** and **T-05 (Supply chain)**.

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

---

## Indicator catalogue {#catálogo-de-indicadores}

| ID | Indicator | Type | L1 | L2 | L3 | Dim. T | Period |
|----|-----------|:----:|:--:|:--:|:--:|:------:|---------|
| DEP-K01 | % of applications with an SBOM generated automatically and updated at each release | Q% | ≥ 50% | ≥ 90% | 100% | T-01, T-05 | Per release |
| DEP-K02 | % of critical CVEs (CVSS ≥ 9.0) in direct dependencies mitigated within SLA | Q% | ≥ 70% (SLA: 30d) | ≥ 90% (SLA: 14d) | 100% (SLA: 5d) | T-03 | Continuous |
| DEP-K03 | % of high CVEs (CVSS 7.0–8.9) in direct dependencies mitigated within SLA | Q% | ≥ 60% (SLA: 90d) | ≥ 80% (SLA: 30d) | ≥ 95% (SLA: 14d) | T-03 | Monthly |
| DEP-K04 | # of direct dependencies without an active maintainer (EOL, abandoned ≥ 24 months) in production | Q# ↓ | ≤ 5 | ≤ 2 | = 0 | T-05 | Quarterly |
| DEP-K05 | % of pipelines with automated SCA integrated with a blocking gate for critical CVEs | Q% | ≥ 60% | ≥ 90% | 100% | T-01 | Monthly |
| DEP-K06 | % of dependencies with a licence incompatible with organisational policy active in production | Q% ↓ | - | = 0% | = 0% | T-05 | Quarterly |
| DEP-K07 | % of L3 applications with an SBOM delivered to relevant stakeholders (GRC, procurement, customer) | Q% | - | - | ≥ 80% | T-05 | Per major release |

---

## Complementary definitions {#definições-complementares}

**DEP-K02/K03 - Mitigation SLA:** the SLA counts from the date of publication of the CVE in NVD/OSV, or from the date of detection by the SCA scanner, whichever is later. Valid mitigation includes: update of the dependency, removal of the dependency, or a formal documented exception with compensation (which suspends the counter but does not close the indicator).

**DEP-K04 - Abandoned dependency:** a dependency is considered to have no active maintainer when the repository has had no relevant commits for ≥ 24 months AND there is no active long-term support version. Dependencies with an active internal fork are excluded from this count if the fork has a documented patch policy.

**DEP-K05 - Blocking gate:** the SCA only counts for this indicator if it blocks the pipeline in the event of a critical CVE without a formal exception. SCA in report-only mode does not satisfy this criterion.

**DEP-K06 - Incompatible licence:** defined by the organisational licensing policy. In the absence of a formal policy, the reference used is incompatibility with strong copyleft licences (GPL v3, AGPL) in the context of proprietary software, or licences without OSI approval in an open-source context.

---

## Collection and instrumentation {#recolha-e-instrumentação}

| Indicator | Primary source | Reference tools | Automation |
|-----------|---------------|--------------------------|-----------|
| DEP-K01 | Build pipeline; release register | Syft, CycloneDX, SPDX tools | Yes |
| DEP-K02/K03 | SCA scanner + NVD/OSV feed | Grype, Trivy, Snyk, Dependabot | Yes |
| DEP-K04 | SCA scanner + repos.github.com / deps.dev | OSS Insight, deps.dev API | Partial |
| DEP-K05 | Pipeline configuration (YAML audit) | Pipeline inspection + SCA results | Partial |
| DEP-K06 | SCA licence scanner | FOSSA, LicenseFinder, Snyk License | Yes |
| DEP-K07 | GRC delivery register / contract | Manual or GRC integration | No |

---

## SLA thresholds per level - summary {#thresholds-de-sla-por-nível---resumo}

| Severity (CVSS) | L1 | L2 | L3 |
|-------------------|:--:|:--:|:--:|
| Critical (≥ 9.0) | 30 days | 14 days | 5 days |
| High (7.0–8.9) | 90 days | 30 days | 14 days |
| Medium (4.0–6.9) | - | 90 days | 60 days |
| Low (&lt; 4.0) | - | - | 180 days |

These thresholds are a baseline reference. Sectoral regulation (DORA, NIS2) may impose shorter deadlines, which prevail.

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|-----------|---------|
| `addon/00-catalogo-requisitos.md` | Requirements DEP-001..010 that underpin the indicators |
| `addon/08-rastreabilidade-vulnerabilidades.md` | CVE → application → resolution traceability model |
| `addon/09-excecoes-e-aceitacao-risco.md` | CVEs without resolution within SLA require a formal exception |
| Ch. 14 `kpis-governanca.md` | Cross-cutting dimensions T-01, T-03, T-05 |
