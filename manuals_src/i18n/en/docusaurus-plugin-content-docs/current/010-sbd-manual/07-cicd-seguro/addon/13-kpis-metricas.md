---
id: kpis-metricas-cicd
title: KPIs and Metrics - Secure CI/CD
sidebar_position: 13
description: Technical and operational indicators for assessing the effectiveness of security controls in continuous integration and delivery pipelines, with thresholds by risk level and mapping to the cross-cutting SbD-ToE governance dimensions.
tags: [kpi, metricas, CIC, cicd, pipeline, gates, artefactos, secrets, L1, L2, L3]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/addon/13-kpis-metricas.md
  source_sha256: 4eaf03f6c7e32c911dce1ce24ee460cff40290c827c177bdb595cfa22b50b921
  source_commit: 036d74010f423f247be988e4a417375c74edb9d9
  target_sha256: ae66935e0f0d7d369777ac3f964fbf8b666d55bf5ecd06d9c88fe91610bad563
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [avaliacao, framework_source_corpus, mapping, practitioner_manual, provenance, risk_level, sbdtoe_sbd, traceability, transversal, verificacao_check, verification_taxonomy]
  glossary_sha256: def10fc568e77372e4ec5973c0ae4df1f03a0f463ee40df5796da2409a1e3a21
  translated_at: 2026-09-27T07:53:45Z
  stamped_at: 2026-09-27T07:53:45Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# KPIs and Metrics - Secure CI/CD

## Scope and purpose {#âmbito-e-propósito}

The indicators of this domain assess the **structural security of CI/CD pipelines**: the presence and effectiveness of the security gates, the integrity and provenance of artefacts, secrets management in an automation context, and visibility over bypasses and deviations from the defined process.

The pipeline is at the same time a control mechanism and an attack vector. Its security is not binary - it is measurable through the coverage of the gates, the traceability of the artefacts and the speed with which detected vulnerabilities are resolved. A pipeline in which all the gates exist but can be bypassed without a record is not a control: it is an illusion of control.

The CIC indicators feed the cross-cutting dimensions **T-01 (Control coverage)**, **T-02 (Exception health)** and **T-03 (Resolution speed)**.

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
| CIC-K01 | % of production pipelines with security gates active and in blocking mode (not report only) | Q% | ≥ 60% | ≥ 90% | 100% | T-01 | Monthly |
| CIC-K02 | % of security gate bypasses with a recorded and traceable formal approval (vs total bypasses) | Q% | ≥ 80% | 100% | 100% | T-02 | Per event |
| CIC-K03 | % of build artefacts digitally signed and with signature verification before deploy | Q% | - | ≥ 70% | 100% | T-01 | Per release |
| CIC-K04 | % of pipeline secrets injected via a centralised vault (Vault, KMS, secret store) vs hardcoded or unmanaged env vars | Q% | ≥ 60% | ≥ 90% | 100% | T-01 | Quarterly |
| CIC-K05 | MTTR - time from detection of a critical vulnerability in a pipeline to confirmed mitigation | Qt | ≤ 30d | ≤ 7d | ≤ 3d | T-03 | Per event |
| CIC-K06 | % of CI/CD runners/agents with effective isolation between jobs from different trust contexts | Q% | - | ≥ 80% | 100% | T-01 | Quarterly |
| CIC-K07 | # pipelines with no record of a security review within the cadence (annual at L1/L2; half-yearly at L3) | Q# ↓ | - | ≤ 5 | = 0 | T-01 | Half-yearly |

---

## Complementary definitions {#definições-complementares}

**CIC-K01 - Security gate in blocking mode:** a gate counts for this indicator only if its failure prevents the pipeline from advancing to the next environment without explicit, recorded intervention. Gates configured as `continue-on-error: true` or equivalent do not satisfy this criterion.

**CIC-K02 - Bypass with formal approval:** a bypass is any pipeline run that circumvents or ignores an active security gate. Formal approval requires: identification of the person responsible, technical justification, a reference to the corresponding ticket or exception, and a timestamp. Generic approvals without context are not valid.

**CIC-K03 - Artefact signing:** includes container images (Cosign/Notary), binaries (GPG, Sigstore) and release packages. Verification of the signature before deploy is mandatory - the existence of the signature without verification does not satisfy this indicator.

**CIC-K04 - Pipeline secret:** secrets injected via an environment variable defined manually in the SCM (without automatic rotation, without access auditing) do not count as "managed via a vault". Only integration with secrets management systems with auditing (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager) satisfies the criterion.

**CIC-K05 - Pipeline MTTR:** counts from the date/time of detection by the scanner (job log) to the date/time at which the fix is confirmed in a clean build. Formal exceptions that suspend remediation must be excluded from the MTTR calculation but recorded separately.

**CIC-K06 - Runner isolation:** a runner is considered isolated if it: (a) is ephemeral (destroyed after each job); or (b) has a workspace and context clean-up policy between jobs from different repositories/organisations; or (c) is on a segregated network without access to the credentials of other projects.

---

## Collection and instrumentation {#recolha-e-instrumentação}

| Indicator | Primary source | Reference tools | Automation |
|-----------|---------------|--------------------------|-----------|
| CIC-K01 | Pipeline configuration (YAML) + job results | GitHub Actions, GitLab CI, Azure DevOps (config audit) | Partial |
| CIC-K02 | Pipeline logs + approval records | SCM audit log + exception register | Partial |
| CIC-K03 | Signature records + admission policy | Cosign, Sigstore, Notary + verification at deploy | Yes |
| CIC-K04 | Inventory of pipeline variables vs secret store integrations | Pipeline configuration audit | Partial |
| CIC-K05 | Findings platform + pipeline logs | DefectDojo + pipeline timestamps | Partial |
| CIC-K06 | Runner configuration + network topology | Configuration audit + IaC review | Partial |
| CIC-K07 | Register of pipeline reviews (git log, tickets) | Manual audit or tagged reviews | No |

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|-----------|---------|
| `addon/00-catalogo-requisitos.md` | Requirements CIC-001..010 that underpin the indicators |
| `addon/09-controle-excecoes-visibilidade.md` | Pipeline exception process (CIC-K02) |
| `addon/06-politicas-gates-pipeline.md` | Definition of the gates that feed CIC-K01 |
| Ch. 14 `kpis-governanca.md` | Cross-cutting dimensions T-01, T-02, T-03 |
