---
id: kpis-metricas-desenvolvimento
title: KPIs and Metrics - Secure Development
sidebar_position: 11
description: Technical and process indicators for the assessment of the effectiveness of secure development controls, with thresholds per risk level and mapping to the cross-cutting SbD-ToE governance dimensions.
tags: [kpi, metricas, DEV, desenvolvimento, sast, secrets, code-review, L1, L2, L3]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/06-desenvolvimento-seguro/addon/11-kpis-metricas.md
  source_sha256: b469f2cc361b1c0ce471333236a1b0d077f2982a6456a5503936fb85dc349eba
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: 4e124fab717cafb0108fd5200a1176545096a2f7505d5cfad4b67af3f4e3d684
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [avaliacao, framework_source_corpus, mapping, risk_level, sbdtoe_sbd, traceability, transversal, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 128a402e6c476555ea03664ca566067d5eddb32cf87161653352578aea7f5ba3
  translated_at: 2026-09-26T12:48:43Z
  stamped_at: 2026-09-26T18:34:06Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# KPIs and Metrics - Secure Development

## Scope and purpose {#âmbito-e-propósito}

The indicators of this domain assess the **integration of security practices into the software development process**: from the quality of code reviews to the speed of resolution of static findings, including the control of secrets and the traceability of the exceptions declared in the code.

Secure development is measured not only by what is blocked but by what is learnt: the regression rate - vulnerabilities that reappear after resolution - is an indicator of the quality of the remediation process, not only of the detection tool.

The DEV indicators feed the cross-cutting dimensions **T-01 (Control coverage)**, **T-02 (Exception health)** and **T-03 (Resolution speed)**.

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
| DEV-K01 | % of SAST findings of critical/high severity resolved within SLA | Q% | ≥ 70% (SLA: 30d) | ≥ 85% (SLA: 14d) | ≥ 98% (SLA: 7d) | T-03 | Per release |
| DEV-K02 | # of secrets detected in commits and not removed/rotated in less than 24h | Q# ↓ | ≤ 2/month | = 0 | = 0 | T-01 | Continuous |
| DEV-K03 | % of PRs in L2/L3 applications with explicit verification of a security criterion in the code review | Q% | - | ≥ 80% | 100% | T-01, T-04 | Monthly |
| DEV-K04 | % of SAST exceptions (mutes/waives) with a recorded and traceable formal approval | Q% | ≥ 80% | 100% | 100% | T-02 | Monthly |
| DEV-K05 | % of high/critical severity findings that reappear after declared resolution (regression rate) | Q% ↓ | - | ≤ 10% | ≤ 5% | T-03 | Quarterly |
| DEV-K06 | % of repositories with SAST active and configured for the technology stack in use | Q% | ≥ 60% | ≥ 90% | 100% | T-01 | Monthly |

---

## Complementary definitions {#definições-complementares}

**DEV-K01 - SAST resolution SLA:** counts from the date of detection by the scanner in the pipeline. A finding is considered resolved when: (a) the code is fixed and the scanner confirms its absence; or (b) a formal exception with compensation is recorded (which suspends the counter but does not close the indicator - see DEV-K04). False positives confirmed by the formal triage process do not count.

**DEV-K02 - Exposed secret:** includes credentials, API tokens, private keys, passwords and any value that satisfies the detection rules of secret scanners (GitLeaks, TruffleHog, detect-secrets). The 24h deadline counts from detection, not from the commit. "Removed" requires removal from the git history AND rotation of the credential in the target system - removing the file without rotation does not close the indicator.

**DEV-K03 - Security criterion in code review:** it is considered verified when there is evidence that at least one reviewer explicitly assessed: input validation, error handling, use of sensitive APIs and the absence of prohibited patterns. The evidence may be a review comment, a PR checklist or a security review label.

**DEV-K04 - Traceable SAST exception:** an exception is considered traceable if it includes: the finding ID, the technical justification, the person responsible for the approval and the validity period. Annotations without a recorded approver do not satisfy this criterion.

**DEV-K05 - Regression:** a finding is classified as a regression if it was marked as resolved and reappears in the same location (file + line ± 10 lines) within 90 days. Tools such as DefectDojo support the automatic tracking of regressions.

---

## Collection and instrumentation {#recolha-e-instrumentação}

| Indicator | Primary source | Reference tools | Automation |
|-----------|---------------|--------------------------|-----------|
| DEV-K01 | SAST pipeline + findings management system | SonarQube, Semgrep, CodeQL + DefectDojo | Yes |
| DEV-K02 | Pre-commit hooks + CI scanner | GitLeaks, TruffleHog, detect-secrets | Yes |
| DEV-K03 | Pull request reviews (SCM) | GitHub/GitLab API (labels, reviewers) | Partial |
| DEV-K04 | `excecoes-aprovadas.yml` file + approval system | PR review + GRC register | Partial |
| DEV-K05 | Findings management platform with history | DefectDojo, Vulcan Cyber | Yes |
| DEV-K06 | Pipeline configuration + repository inventory | Pipeline YAML audit | Partial |

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|-----------|---------|
| `addon/00-catalogo-requisitos.md` | Requirements DEV-001..009 that underpin the indicators |
| `addon/05-excecoes-e-justificacoes.md` | SAST exception process (DEV-K04) |
| Ch. 10 `addon/08-gestao-findings.md` | Centralisation and triage of the findings that feed DEV-K01/K05 |
| Ch. 14 `kpis-governanca.md` | Cross-cutting dimensions T-01, T-02, T-03 |
