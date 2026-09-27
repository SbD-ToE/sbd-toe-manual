---
id: kpis-governanca
title: Cross-cutting SbD-ToE KPIs - Governance Dashboard
sidebar_position: 90
description: Six cross-cutting dimensions for measuring the health of the SbD-ToE programme, aggregating domain indicators from all chapters for executive and risk management visibility.
tags: [kpi, metricas, governanca, transversal, dashboard, executivo, L1, L2, L3]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/kpis-governanca.md
  source_sha256: 241894422ba7d8b3b0fbbe1c7fe4f23b6aa46a98270275ea38264ade66206974
  source_commit: 036d74010f423f247be988e4a417375c74edb9d9
  target_sha256: 0d478195886f6d171986d0fd0c987f5c2e7d990b520252d7992a45dae93fff20
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [atomic_composite, avaliacao, chapter_role, cycle_iteration, layer, maturity, mcp_reading_programa, programme_line, risk_level, role_procurement, sbdtoe_sbd, traceability, transversal, validation_evaluation]
  glossary_sha256: e85b50d4956bf3aa0ed8b11f98f9be00bf1310af09331fcd01a2d5873713cc27
  translated_at: 2026-09-27T07:54:06Z
  stamped_at: 2026-09-27T07:54:06Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Cross-cutting SbD-ToE KPIs - Governance Dashboard

For a visual representation of the measurement architecture, see [`kpis-arquitetura-visao-geral`](./kpis-arquitetura-visao-geral). For the curated set of indicators for the CISO/senior management/board, see [`kpis-kri-executivo`](./kpis-kri-executivo). To assess whether the model is adopted ("are we doing SbD-ToE?"), see [`checklist-aderencia-sbd-toe`](./checklist-aderencia-sbd-toe).

---

## Purpose and architecture {#propósito-e-arquitectura}

This file defines the **cross-cutting measurement structure** of the SbD-ToE programme in three layers:

```
Fundação de portfólio (F-01..F-04)          ← denominador comum a todo o programa
        ↓  estabelece
Indicadores de domínio (por capítulo)        ← o que cada domínio mede, com o mesmo denominador
        ↓  alimentam
Dimensões transversais T-01..T-06            ← agregação por perspectiva de risco
        ↓  resumem para
Dashboard executivo (secção final)           ← síntese para gestão e GRC
```

The central principle of this architecture is that **the denominator of all domain KPIs is the same**: the set of applications classified at the relevant risk level, defined by the Portfolio foundation. "80% of L3 systems have a threat model" is interpretable only if the denominator (# classified L3 systems) is shared by all chapters.

The cross-cutting KPIs do not replace the domain indicators - they complement them with a second-order perspective: *what does the set of domains say about the health of the programme?*

---

## Portfolio foundation {#fundação-de-portfólio}

The Portfolio foundation is layer zero of the dashboard - the absolute metrics that make all domain percentages interpretable. Without this layer, the percentages of the domain chapters lack a shared denominator and do not make it possible to answer the fundamental question: *is SbD-ToE being applied in the organisation?*

### SbD-ToE adoptability funnel {#funil-de-adoptabilidade-sbd-toe}

```
F-01: Total de aplicações no portfólio
  └─ F-02: Aplicações com classificação de risco formal (L1 / L2 / L3)
        └─ F-03: Aplicações com requisitos de segurança formalmente mapeados
              └─ F-04: Aplicações com controlos de pelo menos um domínio validados com evidência
```

Each layer of the funnel is the denominator of the next layer. The difference between layers reveals where adoption loses traction.

### Foundation metrics {#métricas-de-fundação}

| ID | Metric | Type | Threshold | Period |
|----|---------|:----:|-----------|---------|
| F-01 | Total # of applications in the organisational portfolio (active inventory) | Q# | Complete inventory mandatory - absence of data invalidates all subsequent KPIs | Quarterly |
| F-02 | # applications with a formal risk classification, per level (L1 / L2 / L3) | Q# | = F-01 (every application must be classified) | Quarterly |
| F-03 | # applications with SbD-ToE requirements formally mapped to the risk level | Q# | L1: ≥ 80% of F-02(L1); L2: ≥ 95% of F-02(L2); L3: 100% of F-02(L3) | Half-yearly |
| F-04 | # applications with evidence of validated controls in at least one technical domain | Q# | L1: ≥ 70% of F-03; L2: ≥ 90% of F-03; L3: 100% of F-03 | Half-yearly |

**Note on the denominator of the domain KPIs:** each chapter (Ch. 01–13) defines indicators of the type "% applications with X". The denominator of those percentages is always F-02 segmented by the relevant risk level. The `addon/XX-kpis-metricas.md` files of each chapter take this denominator as their basis - their validity depends on F-01 and F-02 being complete and up to date.

### Interpretation of the funnel {#interpretação-do-funil}

| Situation | Diagnosis | Action |
|----------|-------------|-------|
| F-01 unknown or incomplete | No application inventory - invalid governance basis | Priority zero: establish an inventory |
| F-02 &lt; F-01 | Applications without classification - the domain KPIs have no denominator | Complete the classification before reporting |
| F-03 &lt;&lt; F-02 | Requirements not mapped - technical domains operate without a normative reference | Alignment Ch. 01 → Ch. 02 |
| F-04 &lt;&lt; F-03 | Requirements mapped but without validation - declarative compliance | Activate validation processes per domain |
| F-04 ≈ F-03 | Controls applied and evidenced - programme at operational maturity | Focus on continuous improvement and T-06 |

---

## Type conventions {#convenções-de-tipo}

| Code | Meaning |
|--------|-------------|
| Q% | Quantitative, percentage - aggregates domain percentages |
| Qt | Quantitative, temporal - aggregates or compares times |
| Ord | Qualitative, ordinal - aggregates maturity levels (1–3) |
| Comp | Composite - combines multiple domain indicators into a derived metric |

---

## Cross-cutting dimensions {#dimensões-transversais}

### T-01 - Control Coverage {#t-01---cobertura-de-controlos}

**Definition:** percentage of applications, per risk level (L1/L2/L3), that have the mandatory controls of each domain applied and verified.

**Interpretation:** T-01 answers the question *"is the model being applied?"*. High coverage in all domains indicates that the requirements are being met. Gaps per domain reveal where adoption is weakest.

| Threshold | L1 | L2 | L3 |
|-----------|:--:|:--:|:--:|
| Minimum coverage per domain | ≥ 60% | ≥ 85% | ≥ 95% |
| Overall coverage (weighted average) | ≥ 65% | ≥ 88% | ≥ 97% |

**Domain indicators that feed T-01:**

| Chapter | Reference indicator |
|----------|------------------------|
| Ch. 01 - Classification | CLA-K01 (documented classification), CLA-K02 (reviews in the cycle) |
| Ch. 02 - Requirements | RQS-K01 (mapped requirements), RQS-K02 (implementation evidence) |
| Ch. 03 - Threat Modelling | THR-K01 (up-to-date threat model), THR-K03 (AppSec review) |
| Ch. 04 - Architecture | ARC-K01 (threat model), ARC-K04 (review with AppSec) |
| Ch. 05 - Dependencies | DEP-K01 (SBOM), DEP-K05 (SCA with gate) |
| Ch. 06 - Development | DEV-K06 (active SAST), DEV-K03 (code review with security) |
| Ch. 07 - CI/CD | CIC-K01 (gates in blocking mode), CIC-K04 (secrets via vault) |
| Ch. 08 - IaC | IAC-K01 (policy-as-code), IAC-K07 (plan+review before apply) |
| Ch. 09 - Containers | CNT-K04 (admission controller), CNT-K05 (up-to-date base images) |
| Ch. 10 - Testing | TST-K01 (SAST per build), TST-K02 (DAST per release) |
| Ch. 11 - Deployment | DPL-K01 (pre-deploy checklist), DPL-K06 (traceable evidence) |
| Ch. 12 - Monitoring and Operations | OPS-K01 (centralised logging), OPS-K02 (tested alerts) |
| Ch. 14 - Governance and Contracting | GOV-K07 (complete organisational traceability) |

**Measurement frequency:** monthly per domain; quarterly for the cross-cutting synthesis.

---

### T-02 - Exception Health {#t-02---saúde-de-excepções}

**Definition:** qualitative and quantitative state of the active exceptions in the programme - chain of authority coverage, temporal validity, and rate of exceptions in non-compliance (expired or without formal approval).

**Interpretation:** T-02 answers the question *"are deviations from the model under control?"*. A programme with many exceptions is not necessarily insecure - it is insecure when those exceptions are incomplete, expired, or without documented compensation. The health of exceptions is a proxy for the maturity of the risk management process.

| Composite indicator | Threshold |
|-------------------|-----------|
| % exceptions with a complete chain of authority | 100% (absolute - there is no lower threshold) |
| % exceptions with a deadline and a scheduled reassessment | ≥ 80% (L1), 100% (L2/L3) |
| # expired exceptions without renewal | = 0 (absolute - an expired exception is active non-compliance) |
| % gate bypasses with formal approval | 100% (L2/L3) |
| % emergency deploys with post-facto approval &lt; 24h | 100% (absolute) |

**Domain indicators that feed T-02:**

| Chapter | Reference indicator |
|----------|------------------------|
| Ch. 06 - Development | DEV-K04 (SAST exceptions with approval) |
| Ch. 07 - CI/CD | CIC-K02 (bypasses with formal approval) |
| Ch. 08 - IaC | IAC-K04 (policy exceptions with a record) |
| Ch. 11 - Deployment | DPL-K02, DPL-K03, DPL-K07 (break-glass) |
| Ch. 14 - Governance and Contracting | GOV-K02, GOV-K03, GOV-K04, GOV-K08 |

**Measurement frequency:** weekly for expired exceptions (automatable); monthly for the overall state.

---

### T-03 - Resolution Speed {#t-03---velocidade-de-resolução}

**Definition:** mean time to resolution (MTTR) of critical and high findings, aggregated by origin (SAST, SCA, containers, testing, operations), weighted by the risk level of the affected applications.

**Interpretation:** T-03 answers the question *"does the organisation react with a speed appropriate to the risk?"*. A high MTTR in critical domains indicates bottlenecks in the remediation process - lack of capacity, of prioritisation, or of a formal process. The comparison between domains reveals where the response is slowest.

| MTTR threshold - critical findings | L1 | L2 | L3 |
|------------------------------------|:--:|:--:|:--:|
| SCA/Dependencies (CVE ≥ 9.0) | 30 days | 7 days | 3 days |
| SAST (critical severity) | 30 days | 7 days | 3 days |
| Containers (CVE ≥ 9.0 in image) | 30 days | 7 days | 3 days |
| Pipeline (detection → mitigation) | 30 days | 7 days | 3 days |
| Operations (alert → mitigation, OPS-K04) | 8h | 4h | 1h |

**Domain indicators that feed T-03:**

| Chapter | Reference indicator |
|----------|------------------------|
| Ch. 05 - Dependencies | DEP-K02, DEP-K03 (MTTR of CVEs by severity) |
| Ch. 06 - Development | DEV-K01 (MTTR SAST), DEV-K05 (regression rate) |
| Ch. 07 - CI/CD | CIC-K05 (pipeline MTTR) |
| Ch. 09 - Containers | CNT-K02 (MTTR of CVEs in images) |
| Ch. 10 - Testing | TST-K03 (% findings within SLA), TST-K04 (regression rate) |
| Ch. 11 - Deployment | DPL-K04 (security rollbacks) |
| Ch. 12 - Monitoring and Operations | OPS-K03 (MTTD), OPS-K04 (MTTR) |

**Measurement frequency:** continuous (per event for critical findings); monthly for trends.

---

### T-04 - Ownership Coverage {#t-04---cobertura-de-ownership}

**Definition:** percentage of applications, per risk level, with a security owner who is formally designated, active and holds valid training. It also includes the coverage of approvers and reviewers in critical processes (exceptions, releases, architecture reviews).

**Interpretation:** T-04 answers the question *"is there formal accountability for each asset?"*. Ownership without valid training is a partial control. Applications without a designated owner are governance blind spots - deviations in those applications have no recipient, and decisions have no legitimate authority.

| Threshold | L1 | L2 | L3 |
|-----------|:--:|:--:|:--:|
| % applications with a designated and active owner | 100% | 100% | 100% |
| % owners with valid SbD training (&lt; 12 months) | ≥ 80% | ≥ 95% | 100% |
| % architecture reviews with formal AppSec | - | ≥ 80% | 100% |
| % L2/L3 PRs with a security reviewer | - | ≥ 80% | 100% |

**Domain indicators that feed T-04:**

| Chapter | Reference indicator |
|----------|------------------------|
| Ch. 04 - Architecture | ARC-K04 (AppSec in reviews) |
| Ch. 06 - Development | DEV-K03 (code review with security) |
| Ch. 13 - Training | TRN-K02 (owners with valid training), TRN-K07 (active champions) |
| Ch. 14 - Governance and Contracting | GOV-K01, GOV-K07 |

**Measurement frequency:** quarterly for ownership coverage; monthly for training.

---

### T-05 - Supply Chain {#t-05---cadeia-de-fornecimento}

**Definition:** security state of the software supply chain - SBOM coverage, contractual compliance with suppliers, validation of L3 suppliers, and artefact signing coverage.

**Interpretation:** T-05 answers the question *"does the organisation know and control what third parties introduce into its systems?"*. The supply chain is a risk vector that cuts across multiple domains: dependencies (ch. 05), containers (ch. 09), and contracts (ch. 14). Dimension T-05 aggregates those signals into a supply chain security perspective.

| Composite indicator | Threshold L1 | Threshold L2 | Threshold L3 |
|-------------------|:------------:|:------------:|:------------:|
| % applications with an up-to-date SBOM | ≥ 50% | ≥ 90% | 100% |
| % L2/L3 contracts with security clauses | ≥ 80% | 100% | 100% |
| % of L3 suppliers with half-yearly validation | - | - | 100% |
| % production images signed and verified | - | ≥ 70% | 100% |
| # EOL dependencies without an active maintainer in production | ≤ 5 | ≤ 2 | = 0 |

**Domain indicators that feed T-05:**

| Chapter | Reference indicator |
|----------|------------------------|
| Ch. 05 - Dependencies | DEP-K01 (SBOM), DEP-K04 (EOL), DEP-K06 (licences) |
| Ch. 09 - Containers | CNT-K03 (signing), CNT-K05 (base images), CNT-K06 (image SBOM) |
| Ch. 14 - Governance and Contracting | GOV-K05 (contractual clauses), GOV-K06 (supplier validation) |

**Measurement frequency:** monthly for SBOM and images; half-yearly for contracts; annual (L1/L2) or half-yearly (L3) for supplier validation.

---

### T-06 - SbD-ToE Maturity {#t-06---maturidade-sbd-toe}

**Definition:** maturity level per domain (scale 1–3, aligned with L1/L2/L3), derived from an annual structured assessment. The evolution compared with the previous cycle is a mandatory component.

**Interpretation:** T-06 answers the question *"is the programme evolving?"*. Maturity levels are not final targets - they are states of a continuum. A domain that remains at the same level for two consecutive cycles without an active evolution plan represents stagnation, not stability.

| Level | Characterisation |
|-------|---------------|
| 1 | Controls applied on an ad hoc basis and dependent on individuals; minimal traceability |
| 2 | Process defined and in use; owners designated; exceptions recorded; KPIs collected |
| 3 | Process automated where possible; complete traceability; KPIs with thresholds and corrective action; evolution compared with the previous cycle |

**Maturity scale per domain (assessment reference):**

| Domain | Minimum expected level L1 | Minimum expected level L2 | Minimum expected level L3 |
|---------|:------------------------:|:------------------------:|:------------------------:|
| Ch. 04 - Architecture | 1 | 2 | 3 |
| Ch. 05 - Dependencies | 1 | 2 | 3 |
| Ch. 06 - Development | 1 | 2 | 3 |
| Ch. 07 - CI/CD | 1 | 2 | 3 |
| Ch. 08 - IaC | 1 | 2 | 3 |
| Ch. 09 - Containers | 1 | 2 | 3 |
| Ch. 10 - Testing | 1 | 2 | 3 |
| Ch. 11 - Deployment | 1 | 2 | 3 |
| Ch. 12 - Monitoring and Operations | 1 | 2 | 3 |
| Ch. 14 - Governance and Contracting | 1 | 2 | 3 |

**Measurement frequency:** annual - structured assessment with evidence per domain; mandatory comparison with the previous cycle.

**Domain indicators that feed T-06:**

| Chapter | Reference indicator |
|----------|------------------------|
| Ch. 01 - Classification | CLA-K01, CLA-K02 |
| Ch. 02 - Requirements | RQS-K01, RQS-K02 |
| Ch. 03 - Threat Modelling | THR-K01, THR-K03 |
| Ch. 04 - Architecture | ARC-K01, ARC-K04 |
| Ch. 05 - Dependencies | DEP-K01, DEP-K05 |
| Ch. 06 - Development | DEV-K03, DEV-K06 |
| Ch. 07 - CI/CD | CIC-K01, CIC-K04 |
| Ch. 08 - IaC | IAC-K01, IAC-K07 |
| Ch. 09 - Containers | CNT-K04, CNT-K05 |
| Ch. 10 - Testing | TST-K01, TST-K02 |
| Ch. 11 - Deployment | DPL-K01, DPL-K06 |
| Ch. 12 - Monitoring and Operations | OPS-K01, OPS-K03, OPS-K04, OPS-K08 |
| Ch. 13 - Training | TRN-K01, TRN-K02, TRN-K07 |
| Ch. 14 - Governance and Contracting | GOV-K01, GOV-K07, GOV-K08 |

---

## Executive dashboard - synthesis {#dashboard-executivo---síntese}

The executive dashboard is a condensed view of the six dimensions, oriented towards communication with management, GRC and the CISO. It introduces no new data - it summarises the cross-cutting KPIs in a synthesis format.

| Dimension | Synthesis indicator | Reporting frequency |
|----------|-------------------|----------------------|
| T-01 Coverage | Average % of control coverage per domain and risk level | Quarterly |
| T-02 Exceptions | # active exceptions / # expired without renewal / % with a complete chain of authority | Monthly |
| T-03 Speed | Average MTTR weighted by severity and risk level | Monthly |
| T-04 Ownership | % applications with an owner and valid training | Quarterly |
| T-05 Supply Chain | % active SBOM / % compliant contracts / % validated L3 suppliers | Half-yearly |
| T-06 Maturity | Average level per domain + delta compared with the previous cycle | Annual |

**Alert criteria for executive reporting:**

- T-01: any domain below the minimum threshold per risk level → **red alert**
- T-02: any expired exception without renewal → **immediate red alert**
- T-03: MTTR of a critical finding above twice the defined threshold → **red alert**
- T-04: % of owners with valid training below 80% at any level → **amber alert**
- T-05: any L3 supplier without half-yearly validation → **red alert**
- T-06: any domain below the minimum expected level for the organisation's dominant risk level → **amber alert with a mandatory plan**

---

## Collection and responsibilities {#recolha-e-responsabilidades}

| Dimension | Collection owner | Instrumentation support |
|----------|-----------------|--------------------------|
| T-01 | AppSec | Pipeline audit + application inventory |
| T-02 | GRC / AppSec | Exception management system (automatic alerts) |
| T-03 | AppSec | Findings platform (DefectDojo, Vulcan) + pipeline logs |
| T-04 | GRC | Owner register + training platform |
| T-05 | AppSec + Procurement | SBOM registry + contract repository |
| T-06 | CISO / GRC | Annual structured assessment with evidence per domain |

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|-----------|---------|
| `addon/13-kpis-dominio-gov.md` | GOV domain KPIs that feed T-02, T-04, T-05 |
| Ch. 01 `addon/12-kpis-metricas.md` | CLA indicators → T-01, T-06 |
| Ch. 02 `addon/16-kpis-metricas.md` | RQS indicators → T-01, T-06 |
| Ch. 03 `addon/11-kpis-metricas.md` | THR indicators → T-01, T-06 |
| Ch. 04 `addon/10-kpis-metricas.md` | ARC indicators → T-01, T-04, T-06 |
| Ch. 05 `addon/10-kpis-metricas.md` | DEP indicators → T-01, T-03, T-05 |
| Ch. 06 `addon/11-kpis-metricas.md` | DEV indicators → T-01, T-02, T-03 |
| Ch. 07 `addon/13-kpis-metricas.md` | CIC indicators → T-01, T-02, T-03 |
| Ch. 08 `addon/12-kpis-metricas.md` | IAC indicators → T-01, T-02 |
| Ch. 09 `addon/11-kpis-metricas.md` | CNT indicators → T-01, T-03, T-05 |
| Ch. 10 `addon/15-kpis-metricas.md` | TST indicators → T-01, T-03 |
| Ch. 11 `addon/10-kpis-metricas.md` | DPL indicators → T-01, T-02 |
| Ch. 12 `addon/07-metricas-indicadores.md` | OPS indicators → T-03 |
| Ch. 13 `addon/11-kpis-metricas.md` | TRN indicators → T-04 |
| `addon/00-catalogo-requisitos.md` | GOV-011 requirements (KPIs defined and reported) |
