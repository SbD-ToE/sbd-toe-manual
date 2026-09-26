---
id: kpis-metricas-containers
title: KPIs and Metrics - Containers and Images
sidebar_position: 11
description: Technical and operational indicators for the assessment of the effectiveness of security controls in container images and orchestration environments, with thresholds by risk level and mapping to the cross-cutting SbD-ToE governance dimensions.
tags: [kpi, metricas, CNT, containers, imagens, kubernetes, admission-controller, assinatura, L1, L2, L3]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/addon/11-kpis-metricas.md
  source_sha256: e1ae462dfdc909c770edcf2cc8dad38ab9d1c2f0e344de79a572125278965802
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: 06943880f2631d057d2d68a9c294f610d7866a675a36caf362864313f3dc9624
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [avaliacao, cycle_iteration, framework_source_corpus, lifecycle_phase, mapping, provenance, risk_level, sbdtoe_sbd, transversal, verification_taxonomy]
  glossary_sha256: 53c2d7ec71d3519ed4cdaccfb337c5fb32e3463c7fb316edee86f1294efc4b5e
  translated_at: 2026-09-26T12:48:48Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# KPIs and Metrics - Containers and Images

## Scope and purpose {#âmbito-e-propósito}

The indicators of this domain assess the **security of the lifecycle of container images**: from their composition and the absence of known vulnerabilities, to signing and provenance verification, the application of admission policies at runtime, and the speed of response to critical CVEs in production images.

Containers introduce a specific measurement challenge: the image is immutable after the build, but the vulnerability ecosystem is dynamic. An image that was secure at the moment of the build can become vulnerable 48 hours later. The CNT indicators must reflect this continuous character, not only the state at the moment of deploy.

The CNT indicators feed the cross-cutting dimensions **T-01 (Control coverage)**, **T-03 (Resolution speed)** and **T-05 (Supply chain)**.

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
| CNT-K01 | % of production images without critical CVEs (CVSS ≥ 9.0) without a valid formal exception | Q% | ≥ 70% | ≥ 90% | 100% | T-01, T-03 | Weekly |
| CNT-K02 | MTTR - time from the identification of a critical CVE in a production image to its replacement/patch | Qt | ≤ 14d | ≤ 7d | ≤ 3d | T-03 | Per event |
| CNT-K03 | % of production images digitally signed and with signature verification before deploy | Q% | - | ≥ 70% | 100% | T-01, T-05 | Per release |
| CNT-K04 | % of workloads in an orchestrator with an admission controller policy active and in blocking mode | Q% | - | ≥ 80% | 100% | T-01 | Monthly |
| CNT-K05 | % of production base images updated within the cycle defined by policy (without mutable tags) | Q% | ≥ 70% | ≥ 90% | 100% | T-01, T-05 | Monthly |
| CNT-K06 | % of images with an associated SBOM accessible in the registry or artefact repository | Q% | ≥ 50% | ≥ 85% | 100% | T-05 | Per release |
| CNT-K07 | # of workloads running as root (UID 0) without a formal technical justification | Q# ↓ | ≤ 5 | = 0 | = 0 | T-01 | Weekly |

---

## Complementary definitions {#definições-complementares}

**CNT-K01 - CVE without a formal exception:** an image is compliant if it has no critical CVEs, or if the identified CVEs have an active (unexpired) formal exception with documented compensation. Images with critical CVEs without an exception, even if the patch is not available, do not satisfy this indicator - they must have a formal exception.

**CNT-K02 - Container MTTR:** counts from the date the CVE is made available in NVD/OSV (or its detection by the scanner, if later) to the date of deploy to production of the corrected image. If the patch is not available upstream, replacing the base image with an alternative without the vulnerability also closes the indicator.

**CNT-K03 - Signature verification:** the existence of a signature without a verification process before deploy does not satisfy this indicator. Verification may be implemented via an admission controller (Kyverno + Cosign verification), or through explicit verification in the deploy pipeline with a traceable log.

**CNT-K04 - Admission controller in blocking mode:** policies configured in `audit` or `warn` mode do not satisfy this criterion. Only `enforce` (Kyverno) or `Deny` (OPA Gatekeeper) count. Exceptions to policies must be formal objects in the orchestrator (not global deactivation).

**CNT-K05 - Mutable tag:** a mutable tag (e.g. `latest`, `stable`, `main`) points to different layers over time, making it impossible to guarantee the reproducibility and auditability of what is in production. Immutable tags require reference by digest (`image@sha256:...`) or by a semantic tag pinned and immutable in the registry.

**CNT-K07 - Execution as root:** includes containers with an explicit `securityContext.runAsUser: 0` or without `runAsNonRoot: true` defined. Legacy applications with a formal justification and active compensation (e.g. seccomp, AppArmor, restricted capabilities) may have an exception, but are counted in this indicator until resolution.

---

## Collection and instrumentation {#recolha-e-instrumentação}

| Indicator | Primary source | Reference tools | Automation |
|-----------|---------------|--------------------------|-----------|
| CNT-K01 | Image vulnerability scanner + exception register | Trivy, Grype, Snyk Container + DefectDojo | Yes |
| CNT-K02 | CVE feed + deploy log + scan history | NVD/OSV + pipeline timestamps | Partial |
| CNT-K03 | Image registry + deploy logs | Cosign, Notary + admission controller logs | Yes |
| CNT-K04 | Orchestrator configuration (Kubernetes manifests) | Kyverno, OPA Gatekeeper, Polaris | Yes |
| CNT-K05 | Image registry + update policy | Dependabot for containers, Renovate, Trivy advisories | Yes |
| CNT-K06 | Artefact repository + build process | Syft + OCI registry with support for SBOM attach | Yes |
| CNT-K07 | Workload configuration in the orchestrator | Kube-bench, Polaris, Checkov (Kubernetes) | Yes |

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|-----------|---------|
| `addon/00-catalogo-requisitos.md` | Requirements CNT-001..012 that underpin the indicators |
| `addon/10-excecoes-containers.md` | Container exception process (CNT-K01, CNT-K04) |
| `addon/07-vulnerabilidades-imagens.md` | Vulnerability management that feeds CNT-K01/K02 |
| Ch. 14 `kpis-governanca.md` | Cross-cutting dimensions T-01, T-03, T-05 |
