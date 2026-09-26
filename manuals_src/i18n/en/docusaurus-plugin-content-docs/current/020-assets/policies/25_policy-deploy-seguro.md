---
id: policy-deploy-seguro
title: Secure Deployment Policy
description: Organisational policy that defines the security requirements for the process of deploying software to production, including verification of signed artefacts, separation of environments, progressive rollout strategies, separation between automation and human authorisation, and end-to-end traceability, proportional to the criticality level (L1, L2, L3).
tags: [policy, deploy, deploy seguro, rollout, canary, blue-green, artefactos assinados, rollback, rastreabilidade, cap11, L1, L2, L3, governance]
grupo: pipeline-entrega
sidebar_position: 25
translation:
  source_locale: pt
  source_path: 020-assets/policies/25_policy-deploy-seguro.md
  source_sha256: 2b2cb981f00e7ffb97be36cee7888ee7822807525c1c6057d4748c08ff80e6e2
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 754a21b2a2629b93ca4185bfb3be410dec2bd5d9620d46a576e07ac0c599fda6
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [framework_source_corpus, practitioner_manual, provenance, role_tech_lead, sbdtoe_sbd, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 4a2a7b0692910162a880f92df27cb308ba85deaadfe00adee7f96599f0985bdd
  translated_at: 2026-09-26T14:10:58Z
  stamped_at: 2026-09-26T18:36:58Z
  reviewed_by: null
---

# Secure Deployment Policy

## 1. Objective {#1-objetivo}

This policy defines the security requirements for the **process of deploying software to production environments**, covering everything from verification of the artefact's integrity to post-deploy monitoring and rollback capability.

Deploy is the moment at which the risk accumulated during development reaches the environment where it has real impact. A deploy without verification of the artefact's integrity, without formal approval, without a controlled rollout strategy or without rapid rollback capability turns a potentially contained incident into an unavailability or compromise event that is difficult to recover from.

The objective of this policy is to ensure that:

- Only signed and verified artefacts are promoted to production
- Deploy is a deliberate act with recorded approval, not an implicit automatic promotion
- Progressive rollout strategies reduce the blast radius of undetected regressions
- Rollback is automated or can be executed in minimal time
- Commit→pipeline→artefact→deploy traceability is verifiable in audit

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

| Level | Applicability |
|---|---|
| L1 | Recommended; deploy via pipeline; rollback available |
| L2 | Mandatory; signed artefact; formal approval; complete traceability |
| L3 | Mandatory; dual approval; progressive rollout; active post-deploy monitoring |

---

## 3. Verification of the artefact before deploy {#3-verificação-do-artefacto-antes-do-deploy}

Before starting any deploy to staging or production, the pipeline must verify:

| Verification | L1 | L2 | L3 |
|---|---|---|---|
| Artefact identified by SHA256 digest (not by floating tag) | Recommended | Mandatory | Mandatory |
| Valid artefact signature (Cosign or equivalent) | Recommended | Mandatory | Mandatory + automatic blocking |
| SBOM associated with the artefact present and accessible | Recommended | Mandatory | Mandatory |
| Artefact is the same one that passed the security gates (no rebuild) | Recommended | Mandatory | Mandatory |
| Pre-release security gate with an APPROVED result | Recommended | Mandatory | Mandatory |

:::warning
An artefact rebuilt from the same code is not equivalent to the artefact that passed the tests - dependencies may have changed, build environment variables may differ. The deploy must always use the original tested artefact, identified by its digest.
:::

---

## 4. Formal deployment approval {#4-aprovação-formal-de-deploy}

Deploy to production requires explicit human approval, recorded with identity and timestamp:

| Level | Minimum approver | Record format |
|---|---|---|
| L1 | Tech Lead | Comment or approval on the deploy PR |
| L2 | Tech Lead + DevOps/SRE | Formal approval in the pipeline or release system |
| L3 | Tech Lead + DevOps/SRE + AppSec Engineer (dual approval) | Formal record with identity, timestamp, approved digest |

The approval must reference:
- [ ] Version and digest of the approved artefact
- [ ] Result of the pre-release security gate
- [ ] Target environment

### 4.1 Separation between automation and irreversible authorisation {#41-separação-entre-automação-e-autorização-irreversível}

Automation tools may execute deploys, but may not authorise irreversible actions without prior recorded human approval:

- The pipeline mechanically executes what has been approved - it does not decide
- Approval must precede execution in staging and production environments
- Automatic deploys without human approval are permitted only in development environments

---

## 5. Progressive rollout strategies (L2/L3) {#5-estratégias-de-rollout-progressivo-l2l3}

At L2/L3, deploy to production must use a progressive rollout strategy to limit the blast radius of regressions not detected in testing:

| Strategy | Description | Application |
|---|---|---|
| **Canary** | Increasing percentage of traffic (e.g. 1% → 5% → 20% → 100%) with metrics analysis between stages | L2/L3 |
| **Blue-Green** | Two equivalent environments; routing switch after validation | L2/L3 |
| **Rolling update** | Gradual replacement of instances/pods, with health checks at each stage | L1/L2/L3 |

### 5.1 Promotion criteria between stages {#51-critérios-de-promoção-entre-etapas}

Promotion from one rollout stage to the next must be conditional on:

- [ ] HTTP error rate below the defined threshold (e.g. < 0.1% of 5xx)
- [ ] Response latency within normal limits (e.g. P99 < 500ms)
- [ ] Absence of active security alerts
- [ ] Absence of crash loops or unexpected restarts

### 5.2 Automatic rollback on criterion failure {#52-rollback-automático-por-falha-de-critério}

If a promotion criterion fails during the rollout:

- [ ] Rollback to the previous version is started automatically
- [ ] The rollout is paused and the alert is generated
- [ ] The decision to attempt a new promotion or to abort is human

---

## 6. Separation of environments and data {#6-separação-de-ambientes-e-dados}

The production environment must be strictly separated from the test and staging environments:

- [ ] Production credentials distinct from those of staging - no sharing of service accounts
- [ ] Production data never copied to staging without anonymisation
- [ ] Functional tests in staging with synthetic or anonymised data
- [ ] No write access to the production environment from test jobs

---

## 7. Secrets management in deploy {#7-gestão-de-segredos-no-deploy}

The secrets needed at runtime are injected exclusively at the moment of deploy, not embedded in the artefact:

- [ ] Secrets obtained from the centralised vault via workload identity (OIDC) or via Kubernetes Secrets
- [ ] No secret present in the deploy artefact (image, JAR, wheel)
- [ ] Secret scanning run before deploy as an additional gate (L2/L3)

---

## 8. Deployment traceability {#8-rastreabilidade-do-deploy}

Each deploy operation must produce a traceable record that allows the complete chain to be reconstructed:

```
commit SHA → pipeline run → artefacto (digest) → gate pré-release → aprovação → deploy → ambiente
```

Evidence artefacts:

| Artefact | Description | Retention |
|---|---|---|
| Deploy execution log | Complete output of the deploy pipeline | 90 days (L2), 1 year (L3) |
| Approval record | Identity, timestamp, approved digest | 1 year (L2), 2 years (L3) |
| Rollout configuration | Strategy and promotion criteria | Active version |
| CHANGELOG and Git tags | Versioning and release metadata | History |
| End-to-end traceability | Commit→artefact→deploy cross-reference | As per the Traceability Policy |

---

## 9. Feature flags and dark launches {#9-feature-flags-e-dark-launches}

At L2/L3, risky functionality may be activated in a controlled manner via feature flags:

- [ ] Feature flags versioned in configuration (YAML/JSON) and not hardcoded
- [ ] Activation and deactivation of feature flags audited (who, when, which flag)
- [ ] Security feature flags (e.g. new authentication logic) tested with limited traffic before global activation
- [ ] No feature flags dependent on unmanaged secrets

---

## 10. Responsibilities {#10-responsabilidades}

| Role | Responsibility |
|---|---|
| Developer | Ensure that the artefact is the same one that passed the tests; do not carry out a manual deploy outside the pipeline |
| DevOps / SRE | Configure the deploy pipeline; implement the rollout strategy; configure post-deploy monitoring |
| AppSec Engineer | Verify security gates before approval; define rollout thresholds; review deploy configurations |
| Tech Lead | Approve deploy at L2/L3; coordinate rollback if necessary |
| GRC / Compliance | Audit approval records; verify traceability; validate log retention |

---

## 11. Review and audit of this policy {#11-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Incident caused by the deploy of an unverified artefact or one without formal approval
- Change of the orchestration platform or of the rollout strategy
- Incident of secrets exposure during the deploy process

---

## 12. Normative and technical references {#12-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 11 - Secure Deployment | Signed artefacts, gates, rollout, rollback, traceability |
| Secure Release Policy (`20_policy-release-seguro.md`) | Pre-release gate and security checklist |
| Release Approval Policy (`26_policy-aprovacao-release.md`) | Formal approval process |
| Rollback Policy (`27_policy-rollback.md`) | Rollback criteria and process |
| Secrets Management Policy (`18_policy-gestao-segredos.md`) | Injection of secrets at runtime |
| SLSA Framework | Integrity of artefacts and provenance |
| NIST SP 800-218 (SSDF) | PW.8, RV.1: deploy and monitoring |
| CIS Software Supply Chain Security | Secure deploy controls |
