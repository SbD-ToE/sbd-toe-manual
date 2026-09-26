---
id: kpis-metricas-iac
title: KPIs and Metrics - IaC and Infrastructure
sidebar_position: 12
description: Technical and operational indicators for assessing the effectiveness of security controls in Infrastructure as Code, with thresholds by risk level and mapping to the cross-cutting SbD-ToE governance dimensions.
tags: [kpi, metricas, IAC, infraestrutura, policy-as-code, drift, opa, sentinel, L1, L2, L3]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/addon/12-kpis-metricas.md
  source_sha256: f6fc93f3e09ffb5fe06069c09834a6a9401aac0980294def325cd222a5fa8559
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 3f66e63d0bb895fb8fd8157caa7f823b89d5304825c2776f60d633646e50b6ca
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [avaliacao, framework_source_corpus, gap_family, mapping, practitioner_manual, risk_level, sbdtoe_sbd, transversal]
  glossary_sha256: d12c51842620dc03f0614f51c0db140c54a70afa0197dde6ee110492a1e8eb9f
  translated_at: 2026-09-26T09:25:40Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# KPIs and Metrics - IaC and Infrastructure

## Scope and purpose {#âmbito-e-propósito}

The indicators of this domain assess the **security of infrastructure defined as code**: the coverage of policy-as-code, the detection and resolution of configuration drift, the absence of secrets in IaC repositories, and the proportion of infrastructure managed declaratively vs provisioned manually.

IaC inverts the classic problem of infrastructure security: instead of auditing the states of systems in production, the code that defines them is audited. This shift to the left only has value if policy enforcement is effective and drift is detected and resolved quickly. Residual manual infrastructure in critical systems is a control gap, not an operational exception.

The IAC indicators feed the cross-cutting dimensions **T-01 (Control coverage)** and **T-02 (Exception health)**.

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
| IAC-K01 | % of IaC modules/stacks with policy-as-code active and in blocking mode in the pipeline | Q% | ≥ 50% | ≥ 90% | 100% | T-01 | Monthly |
| IAC-K02 | # of infrastructure resources with drift detected and unresolved for more than 7 days | Q# ↓ | ≤ 10 | ≤ 3 | = 0 | T-01 | Weekly |
| IAC-K03 | % of production infrastructure of L2/L3 systems provisioned manually (not managed by IaC) | Q% ↓ | - | ≤ 10% | = 0% | T-01 | Quarterly |
| IAC-K04 | % of active policy exceptions in IaC with a formal record, approver and expiry date | Q% | ≥ 80% | 100% | 100% | T-02 | Monthly |
| IAC-K05 | # of secrets detected in IaC repositories and not removed and rotated within 24h | Q# ↓ | = 0 | = 0 | = 0 | T-01 | Continuous |
| IAC-K06 | % of reusable IaC modules (internal or from a private registry) without an active security review | Q% ↓ | - | ≤ 15% | = 0% | T-01 | Half-yearly |
| IAC-K07 | % of IaC pipelines with a mandatory plan + review before apply in production | Q% | ≥ 70% | ≥ 95% | 100% | T-01 | Monthly |

---

## Complementary definitions {#definições-complementares}

**IAC-K01 - Policy-as-code in blocking mode:** only modules where a policy failure (OPA/Rego, Sentinel, Checkov, tfsec, kube-linter, cfn-guard) blocks the pipeline count. Runs in `plan-only` mode without blocking do not satisfy this criterion.

**IAC-K02 - Drift:** a deviation between the state declared in the IaC code and the effective state of the resource in the cloud/on-premise. Drift detection tools: `terraform plan` with analysed output, AWS Config, Azure Policy, Driftctl. The 7-day deadline counts from the first record of detected drift.

**IAC-K03 - Manual infrastructure:** includes resources created through the web console, CLI without IaC, or imperative scripts without a declarative equivalent. Emergency resources created manually with an associated ticket and a migration plan to IaC have a 30-day deadline before entering this count.

**IAC-K04 - Policy exception:** an exception is considered formal if it includes: the ID of the excepted policy, a technical justification, an owner, an approver with authority proportional to the risk level, and an expiry date. Comments in the code without external approval do not satisfy this criterion.

**IAC-K05 - Secret in IaC:** includes any value that satisfies the detection rules of secret scanners applied to infrastructure repositories (Terraform, Helm, Ansible, CloudFormation). "Removed and rotated" requires: removal from the git history (rebase or filter-repo) AND rotation of the credential in the target system.

**IAC-K06 - Module with an active review:** a module is considered to have an active review if it has been subject to security analysis in the last 12 months or since the last major version, with documented evidence.

---

## Collection and instrumentation {#recolha-e-instrumentação}

| Indicator | Primary source | Reference tools | Automation |
|-----------|---------------|--------------------------|-----------|
| IAC-K01 | Pipeline configuration + policy results | Checkov, tfsec, OPA/Rego, Sentinel | Yes |
| IAC-K02 | Drift detection tool | Driftctl, `terraform plan`, AWS Config | Yes |
| IAC-K03 | Inventory of cloud resources vs IaC repository | Cloud asset inventory + IaC state | Partial |
| IAC-K04 | `exceptions/` directory + approval system | File review + GRC record | Partial |
| IAC-K05 | Pre-commit hooks + CI scanner in IaC repositories | GitLeaks, TruffleHog (IaC config) | Yes |
| IAC-K06 | Register of internal modules + review history | Wiki/Confluence + git log | No |
| IAC-K07 | Pipeline configuration (workflow YAML) | IaC pipeline audit | Partial |

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|-----------|---------|
| `addon/08-matriz-requisitos-iac.md` | Requirements IAC-001..013 that underpin the indicators |
| `addon/09-gestao-excecoes.md` | IaC policy exception process (IAC-K04) |
| `addon/06-controle-enforcement.md` | Enforcement mechanisms that feed IAC-K01/K07 |
| Ch. 14 `addon/kpis-governanca.md` | Cross-cutting dimensions T-01, T-02 |
