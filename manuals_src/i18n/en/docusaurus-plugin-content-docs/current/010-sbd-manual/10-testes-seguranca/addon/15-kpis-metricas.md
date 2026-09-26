---
id: kpis-metricas-testes
title: KPIs and Metrics - Security Testing
sidebar_position: 15
description: Technical and operational indicators for the assessment of the effectiveness of the security testing programme, with thresholds by risk level and mapping to the cross-cutting SbD-ToE governance dimensions.
tags: [kpi, metricas, TST, testes, sast, dast, pentest, findings, regressao, L1, L2, L3]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/addon/15-kpis-metricas.md
  source_sha256: e5d8034c3fcae11cd566d10366756f249c7eecb53b14812c91f5c69b64ff6e1a
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: ab7ba1197d2b6a8f25c9256a0b403003574ab8eed71bb1b0afc3450f1325929f
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [avaliacao, framework_source_corpus, mapping, maturity, mcp_reading_programa, practitioner_manual, programme_line, risk_level, sbdtoe_sbd, transversal]
  glossary_sha256: 2c92163b752775c634a63056ec96fa60207e7acd9504b68d32116da8f73463a7
  translated_at: 2026-09-26T12:48:50Z
  stamped_at: 2026-09-26T18:35:14Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# KPIs and Metrics - Security Testing

## Scope and purpose {#âmbito-e-propósito}

The indicators of this domain assess the **effectiveness, coverage and maturity of the security testing programme**: coverage by type of test (SAST, DAST, pentest), the speed of resolution of findings within the defined SLAs, the centralisation of findings management, and the regression rate as a proxy for the quality of the remediation process.

Security tests do not produce security - they produce visibility. The value of the indicators of this domain lies in their capacity to reveal gaps in what is tested, in how the results are handled, and in the consistency of the response over time. A testing programme with good coverage but a high regression rate indicates a structurally deficient remediation process.

The TST indicators feed the cross-cutting dimensions **T-01 (Control coverage)** and **T-03 (Resolution speed)**.

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
| TST-K01 | % of applications with SAST active and executed on every build/PR | Q% | ≥ 70% | ≥ 95% | 100% | T-01 | Monthly |
| TST-K02 | % of L2/L3 applications with DAST executed per release (or equivalent dynamic coverage) | Q% | - | ≥ 80% | 100% | T-01 | Per release |
| TST-K03 | % of critical findings resolved within SLA TST-003 (by severity and level) | Q% | ≥ 70% | ≥ 85% | ≥ 98% | T-03 | Per release |
| TST-K04 | % of critical/high findings in regression - vulnerability declared resolved that reappears within 90 days | Q% ↓ | - | ≤ 5% | ≤ 2% | T-03 | Quarterly |
| TST-K05 | % of reported findings centralised in a management platform (vs. dispersed across individual tools) | Q% | ≥ 60% | ≥ 90% | 100% | T-01 | Monthly |
| TST-K06 | % of L3 applications with an external pentest carried out in the last year (or per major release) | Q% | - | - | 100% | T-01 | Annual |
| TST-K07 | # of false positives confirmed by formal triage vs. total reported findings (noise rate) | Q% ↓ | - | ≤ 30% | ≤ 15% | T-01 | Quarterly |

---

## Complementary definitions {#definições-complementares}

**TST-K03 - SLA by severity and level (reference TST-003):**

| Severity | L1 | L2 | L3 |
|------------|:--:|:--:|:--:|
| Critical (CVSS ≥ 9.0) | 30 days | 14 days | 7 days |
| High (CVSS 7.0–8.9) | 90 days | 30 days | 14 days |
| Medium (CVSS 4.0–6.9) | - | 90 days | 60 days |

Findings with an active formal exception are excluded from the TST-K03 calculation but recorded separately.

**TST-K04 - Regression:** a finding is classified as a regression if: (a) it was marked as resolved in the findings management system; (b) it reappears in the same location (file + line ± 10 lines) or in the same endpoint/parameter; (c) within 90 days of the declared resolution. The regression rate is an indicator of the quality of the remediation process, not of the quality of the scanner.

**TST-K05 - Centralisation:** a finding is considered centralised when it is recorded, with an up-to-date state, in a management platform (DefectDojo, Vulcan Cyber, Security Hub, or equivalent) and associated with the application, version and owner. Findings that exist only in PDF reports, emails or an unstructured backlog do not satisfy this criterion.

**TST-K06 - External pentest:** must be carried out by an entity external to the organisation (not only by an internal team), with a documented scope, a formal methodology (PTES, OWASP Testing Guide, TIBER-EU for regulated sectors), and a report with traceable findings. TLPT (Threat-Led Penetration Testing) satisfies this criterion for sectors with a DORA obligation.

**TST-K07 - Noise rate:** a false positive is confirmed when the formal triage process (with a security analyst) classifies the finding as irrelevant to the application's context. Untriaged false positives do not enter this calculation. A high noise rate indicates a need to adjust the detection rules, not an absence of vulnerabilities.

---

## Collection and instrumentation {#recolha-e-instrumentação}

| Indicator | Primary source | Reference tools | Automation |
|-----------|---------------|--------------------------|-----------|
| TST-K01 | Pipeline configuration + SAST results | SonarQube, Semgrep, CodeQL | Yes |
| TST-K02 | Pipeline logs + DAST results | OWASP ZAP, Burp Suite Enterprise, Nuclei | Partial |
| TST-K03 | Findings management platform + timestamps | DefectDojo (SLA tracking) | Yes |
| TST-K04 | Findings history in the management platform | DefectDojo (re-open tracking) | Yes |
| TST-K05 | Audit of findings platforms vs. tool reports | Count of findings per source vs. central platform | Partial |
| TST-K06 | Pentest register (contract, report, date) | Manual - GRC register or report repository | No |
| TST-K07 | Management platform with a triage field | DefectDojo (false positive flag + documented triage) | Partial |

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|-----------|---------|
| `addon/00-catalogo-requisitos.md` | Requirements TST-001..010 that underpin the indicators |
| `addon/08-gestao-findings.md` | Centralisation (TST-K05) and triage (TST-K07) process |
| `addon/05-validacao-regressao.md` | Regression detection methodology (TST-K04) |
| Ch. 14 `kpis-governanca.md` | Cross-cutting dimensions T-01, T-03 |
