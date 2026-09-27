---
id: policy-cicd-seguro
title: Secure CI/CD Policy
description: Organisational policy that defines the security requirements for continuous integration and delivery pipelines, including mandatory gates, integrated scanners, environment separation, artefact signing, secrets management in the pipeline and promotion approvals, proportional to the criticality level (L1, L2, L3).
tags: [policy, CI/CD, pipeline, SAST, SCA, secret detection, gates, assinatura, artefactos, separação de ambientes, cap07, L1, L2, L3, governance, DevSecOps]
grupo: pipeline-entrega
sidebar_position: 17
translation:
  source_locale: pt
  source_path: 020-assets/policies/17_policy-cicd-seguro.md
  source_sha256: 763b4d415ad77071901e76bc3d4eedbac1fd2a2ace2bec09b8a6cb62b84b1268
  source_commit: 50f5914ebc90e4135e6678b2278709d5082dd237
  target_sha256: 75b68a510c0e87ffc720127f094f411ae33df8a20e925dbc9f400c1b3e65a28f
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [framework_source_corpus, practitioner_manual, requirement_runtime, role_tech_lead, sbdtoe_sbd, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 3ab65579479763a74a25d09c08b15d3e952c3cfb3c97e236360972fe1b2e559c
  translated_at: 2026-09-27T07:06:16Z
  stamped_at: 2026-09-27T07:06:16Z
  reviewed_by: null
---

# Secure CI/CD Policy

## 1. Objective {#1-objetivo}

This policy defines the security requirements applicable to the **design, configuration and operation of continuous integration and delivery (CI/CD) pipelines** for applications classified as L1, L2 or L3.

The CI/CD pipeline is a critical component of an organisation's security posture: it is the path by which code reaches production. A compromised, misconfigured pipeline, or one without adequate controls, is equivalent to a service door without a lock - it can be used to introduce malicious code, escalate privileges or exfiltrate secrets without the code review process being of any relevance.

The objective of this policy is to ensure that:

- Pipelines are configured securely and versioned as code
- Security gates are automated, with documented and blocking thresholds
- The secrets used in the pipeline are managed centrally and never exposed in logs
- Promotion between environments is controlled and requires approval proportional to the risk
- The artefacts produced are signed and verified before any deploy

---

## 2. Scope {#2-âmbito}

This policy applies to all CI/CD pipelines that produce artefacts intended for test, acceptance or production environments, including build, test, analysis, packaging, containerisation and deploy pipelines.

---

## 3. Pipeline as versioned code {#3-pipeline-como-código-versionado}

The pipeline must be defined as code, versioned in the application's repository, subject to code review and with traceable changes:

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Pipeline defined as code (`ci-pipeline.yml` or equivalent) | Mandatory | Mandatory | Mandatory |
| Changes to the pipeline subject to code review and approval | Recommended | Mandatory | Mandatory + AppSec |
| Pipeline versioned in the same repository as the application (or a controlled monorepo) | Mandatory | Mandatory | Mandatory |
| No direct editing of the pipeline in the execution environment (no manual override) | Recommended | Mandatory | Mandatory |

---

## 4. Mandatory security gates {#4-gates-de-segurança-obrigatórios}

The following gates must be configured in the pipeline, with documented thresholds and blocking behaviour according to the proportionality table:

### 4.1 Code and dependency analysis gates {#41-gates-de-análise-de-código-e-dependências}

| Gate | L1 | L2 | L3 |
|---|---|---|---|
| **Secret detection** (TruffleHog, Gitleaks, detect-secrets) | Alert | Blocks any finding | Blocks any finding |
| **SAST** (Semgrep, CodeQL, SonarQube, Bandit) | Alert | Blocks High/Critical | Blocks Medium+ |
| **Security linters** per stack | Recommended | Mandatory | Mandatory |
| **SCA** (Dependency-Check, Trivy, Grype) | Alert | Blocks High/Critical | Blocks Medium+ |
| **Licence validation** | Recommended | Mandatory | Mandatory |

### 4.2 Build and artefact gates {#42-gates-de-build-e-artefactos}

| Gate | L1 | L2 | L3 |
|---|---|---|---|
| **SBOM generation** per build | Mandatory (basic) | Mandatory (complete) | Mandatory (complete + signed) |
| **Artefact signing** (Cosign or equivalent) | Recommended | Mandatory | Mandatory |
| **Signature verification** before promotion | Not applicable | Mandatory | Mandatory |
| **Vulnerability scan of container images** | Recommended | Mandatory | Mandatory |

### 4.3 General gate rules {#43-regras-gerais-de-gates}

- Thresholds (minimum blocking severity) must be documented and versioned (`gates-config.yaml` or equivalent)
- Changing a threshold requires approval from an AppSec Engineer
- A gate that is disabled or whose threshold is temporarily lowered must be recorded as a formal exception

:::warning
Gates configured in "warn-only" mode (without blocking) at L2/L3 do not comply with this policy, except during a formally approved exception period with a defined expiry date.
:::

---

## 5. Secrets management in the pipeline {#5-gestão-de-segredos-no-pipeline}

Secrets used in the pipeline (CI tokens, deploy keys, registry credentials, etc.) must be managed in accordance with the Secrets Management Policy. The specific principles for the pipeline context are:

- [ ] Secrets injected through environment variables managed by the CI system, never hardcoded in the pipeline file
- [ ] Secrets never printed in logs (masking configuration mandatory)
- [ ] Access to production secrets restricted to jobs that genuinely need it (principle of least privilege)
- [ ] Secrets rotated in accordance with policy; rotation verifiable without changing the pipeline
- [ ] No secrets in build artefacts (images, JARs, packages)

---

## 6. Environment separation and controlled promotion {#6-separação-de-ambientes-e-promoção-controlada}

The pipeline must implement physical or logical separation between environments (development, integration, staging, production), with controlled promotion:

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Separate environments with distinct credentials | Recommended | Mandatory | Mandatory |
| Promotion to staging requires green CI + gates OK | Recommended | Mandatory | Mandatory |
| Promotion to production requires human approval | Recommended | Mandatory | Mandatory (dual approval) |
| Promotion to production uses the immutable build artefact (no rebuild) | Recommended | Mandatory | Mandatory |
| Automatic rollback available in the event of a health check failure | Recommended | Mandatory | Mandatory |

The identity that performs the deploy to production must have minimum permissions - the pipeline must never have write access to development and production infrastructure simultaneously.

---

## 7. Pipeline identity and permissions {#7-identidade-e-permissões-do-pipeline}

The CI/CD system operates with its own identities (service accounts, CI tokens), which must follow the principle of least privilege:

- [ ] Each pipeline has a dedicated identity; no use of developers' personal credentials
- [ ] Pipeline permissions limited to what is necessary for each job (reading code, writing to the image registry, deploying to a specific environment)
- [ ] CI tokens with a short TTL; automated rotation
- [ ] Auditing of pipeline access active at L3
- [ ] No PR approval permission for the pipeline identity (prevents automated self-merge)

---

## 8. Reproducibility and traceability {#8-reprodutibilidade-e-rastreabilidade}

Each pipeline execution must be traceable:

- [ ] Execution logs retained in accordance with the Traceability Policy (minimum 90 days at L2, 1 year at L3)
- [ ] Build artefacts associated with the commit SHA that originated them
- [ ] SBOM associated with the artefact produced
- [ ] Scanner results archived as artefacts of the execution
- [ ] Promotion approvals recorded with the approver's identity, timestamp and a reference to the approved artefact

---

## 9. Pipeline integrity {#9-integridade-do-pipeline}

The pipeline itself is an attack vector - it must be treated with the same rigour as application code:

- [ ] Pipeline dependencies (actions, plugins, external steps) pinned to specific versions with a hash (e.g. `uses: actions/checkout@sha256:abc...`)
- [ ] No use of `latest` in pipeline steps at L2/L3
- [ ] External actions or plugins assessed before adoption (origin, maintenance, permissions required)
- [ ] The pipeline does not execute arbitrary code from the input of external PRs without an adequate sandbox

---

## 10. Expected artefacts {#10-artefactos-esperados}

| Artefact | Description | Retention |
|---|---|---|
| `ci-pipeline.yml` | Versioned pipeline definition | Version history |
| Execution logs | Complete output of each run | 90 days (L2), 1 year (L3) |
| Scanner reports (SAST, SCA, secrets) | Results per run, linked to the commit | 90 days (L2), 1 year (L3) |
| SBOM per build | See SBOM Policy | See SBOM Policy |
| Promotion approval records | Identity, timestamp, approved artefact | 2 years (L2), 3 years (L3) |
| Gate/threshold configuration | Documented and versioned thresholds | Version history |

---

## 11. Responsibilities {#11-responsabilidades}

| Role | Responsibility |
|---|---|
| Developer | Maintain the pipeline as code; submit changes to the pipeline for review |
| DevOps / SRE | Configure and operate the CI/CD platform; manage pipeline identities; configure environment separation |
| AppSec Engineer | Define gate thresholds; approve changes to the pipeline's security configurations; review the use of external actions |
| Tech Lead | Approve promotions to production in accordance with the level's requirements |
| GRC / Compliance | Audit logs and approval records; verify compliance with the defined thresholds |

---

## 12. Review and audit of this policy {#12-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Incident originating in the pipeline (compromise, promotion of vulnerable code)
- Adoption of a new CI/CD platform
- Significant change in the integrated analysis tools

---

## 13. Normative and technical references {#13-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 07 - Secure CI/CD | Gates, scanners, artefacts, environment separation |
| SbD-ToE Ch. 05 - Dependencies, SBOM and SCA | SCA and SBOM in the pipeline |
| SbD-ToE Ch. 11 - Secure Deployment | Promotion approval gates |
| Secrets Management Policy (`18_policy-gestao-segredos.md`) | Secrets in the pipeline |
| SBOM Policy (`11_policy-sbom.md`) | Generation and archiving of SBOM per build |
| SLSA Framework | Pipeline supply chain integrity levels |
| OWASP CI/CD Security Top 10 | Security risks in CI/CD pipelines |
| CIS Software Supply Chain Security Guide | Reference controls for secure pipelines |
| NIST SP 800-218 (SSDF) | PO.3, PW.8: secure infrastructure and protection of builds |
