---
id: catalogo-requisitos-deploy
title: Secure Deployment Requirements Catalogue
description: Canonical catalogue of security requirements for the deployment process (DPL-001 to DPL-011), with applicability by risk level and acceptance criteria for formal approval, artefact provenance, automated gates, rollback, deployment credentials, staging, post-deployment monitoring, release gates for agentic systems and end-to-end traceability.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:deploy, DPL, deploy-seguro, rollback, proveniencia, gates, aprovacao, rastreabilidade, L1, L2, L3, auditoria]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/addon/00-catalogo-requisitos.md
  source_sha256: bfe0f24d6e18a3724fecec4a3a26a44d2b0f172673adb3186efa3a96a7191689
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 5c480c2fe2a85f41739a5a3223918b95d3f6feb8bfe391ecdd7b7a58024ef2eb
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, cycle_iteration, lifecycle_phase, mapping, papel_suporte, provenance, requirement_runtime, risk_level, sbdtoe_sbd, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: efb659fb3d56858ee45fc3a432848ac268a64e6c85589a757d7438d8e66654cd
  translated_at: 2026-09-26T11:00:46Z
  stamped_at: 2026-09-26T18:35:22Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Secure Deployment Requirements Catalogue

## Scope: the deployment process as a security boundary {#âmbito-o-processo-de-deploy-como-fronteira-de-segurança}

This catalogue covers **security requirements applicable to the deployment process** - the phase of promotion of software artefacts between environments, and in particular to production. The deployment process is a critical boundary: it is the moment at which code, credentials, configuration and artefacts combine to modify state in live systems.

The scope includes: formal approval before production, verification of artefact provenance at deployment time, automated security gates, management of deployment credentials with minimum scope, validation in staging, configured and tested rollback, post-deployment monitoring and complete traceability of each promotion.

For the complete mapping of all SbD-ToE requirements catalogues by technical domain, canonical prefix and owner, see [Ch. 02 - Catalogue Mapping](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **On curation:** Consolidated from NIST SSDF (RV.3, DS.1), SLSA (Deployment requirements), DORA (operational resilience, change management), OWASP SAMM (Practice: Environment Management) and good practice for secure release engineering. It must be adapted to the deployment platform in use and reviewed with each significant change to the release process.

For instantiation in a project and operational naming (`SEC-Lx-DPL-CODIGO`), see [Taxonomy and Traceability](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Conventions {#convenções}

| Symbol | Meaning |
|---------|-------------|
| ✔ | Requirement mandatory at this level |
| - | Not applicable or not mandatory at this level |

Levels are cumulative: L3 includes all L1 and L2 requirements; L2 includes all L1 requirements.

---

## DPL Catalogue - Secure Deployment {#catálogo-dpl---deploy-seguro}

Requirements ensuring that each promotion to production is approved, traceable, reversible and proportional to the application's risk.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| DPL-001 | Mandatory formal approval before deployment to production | ✔ | ✔ | ✔ | Deployment to production requires explicit approval by an authorised role; approval recorded with a timestamp and the approver's identity; no automatic promotion to production without a human approval gate. |
| DPL-002 | Promotion only of artefacts with verified provenance | ✔ | ✔ | ✔ | Artefacts promoted to production with a digital signature or hash verified at deployment time; traceable provenance (commit SHA, pipeline run ID); artefacts without verifiable provenance rejected automatically. |
| DPL-003 | Automated security gates as a condition of promotion | ✔ | ✔ | ✔ | Gates that verify the absence of critical CVEs, passed security tests and the absence of detected secrets run before each promotion; failure of any gate blocks the deployment; evidence of execution available per deployment. |
| DPL-004 | End-to-end traceability of each deployment | ✔ | ✔ | ✔ | Each deployment identifiable by a unique ID with a record of: who approved, what was deployed (artefact + commit SHA), when, to which environment and which gates were executed; traceability from an incident back to the original commit. |
| DPL-005 | Rollback configured, tested and with a defined SLA | ✔ | ✔ | ✔ | Rollback procedure defined, documented and tested periodically (at least once per release cycle or annually); maximum rollback time defined and verified in testing; last rollback test with a recorded date. |
| DPL-006 | Deployment credentials with minimum scope and a short life | ✔ | ✔ | ✔ | Credentials used in the deployment with scope limited to what is necessary and minimum duration (short-lived tokens preferred over permanent credentials); no deployment credentials shared between applications; credential usage logs available. |
| DPL-007 | Validation in staging before promotion to production | - | ✔ | ✔ | Staging environment with functional and security validation before promotion; staging acceptance criteria documented and evidenced; staging sufficiently representative of production for the purposes of validation. |
| DPL-008 | Active monitoring during and after deployment | - | ✔ | ✔ | Health metrics and alerts active during the deployment window and in the post-deployment observation period; observation period defined by risk level; anomalies in that period trigger automatic rollback or an urgent alert with a response SLA. |
| DPL-009 | Progressive deployment with impact containment for critical applications | - | - | ✔ | Progressive deployment implemented for releases of critical components (canary, blue-green, feature flags); automatic promotion thresholds and rollback criteria defined; capacity for containment without full rollback verifiable. |
| DPL-010 | Release gates for systems with AI agents | - | ✔ | ✔ | Applicable when the system includes an AI agent or AI model as a *load-bearing* dependency. When a promotion changes the model version, *skill files* or *system prompts*, the *eval suite* (Ch. 10 §C5) runs as a **mandatory gate** and a *fail* blocks the promotion; *rollback* procedures for the model version and for the *system prompt*/*skill file* exist **independently** of the application *rollback*; the *release notes* record the model version, the *skill files* version, the *eval suite* version and `mandate_ref` as archived evidence (`eval_run_id` linked to the release). |
| DPL-011 | Canary and autonomy demotion in model releases | - | - | ✔ | Applicable to systems with AI agents. A major model version change (provider, new *fine-tune* or *system prompt* with material impact) is promoted via **canary** — a controlled fraction of traffic during an observable window, with objective criteria for promotion and for automatic rollback (error rate, *off-policy events*, latency); an **automatic gate** lowers the agent's `autonomy_level` (e.g. A3 → A2) when the *eval suite* does not confirm the intended level, until resolution. |

---

## Explanatory notes {#notas-explicativas}

- **DPL-001**: "Human approval" is not bureaucracy - it is the mechanism that ensures that an irreversible decision (modifying state in production) has an identifiable owner. In high-frequency deployment contexts (multiple deployments per day), approval may be implemented as a release gate, not necessarily per individual deployment, provided that the scope and the criteria are documented.
- **DPL-002**: Provenance verification at deployment time is distinct from provenance generation at build time (CIC-007). It is possible to generate a valid signature and never verify it - the effective control requires downstream verification, at promotion.
- **DPL-005**: An untested rollback is a theoretical plan, not a security control. Real incidents regularly show that rollback procedures that have never been exercised fail or are slower than expected when they are most needed.
- **DPL-006**: The use of OIDC/workload identity federation to eliminate long-lived deployment credentials is the recommended practice for L2/L3 - ephemeral tokens per pipeline execution eliminate the risk of credentials compromised through exfiltration.
- **DPL-009**: Progressive deployment is simultaneously a security control and an operational resilience control. For L3 applications with regulatory or business continuity impact, the capacity to contain a problematic deployment to a fraction of the traffic is an integral part of operational risk management.
- **DPL-010**: In an agentic system, the application binary is no longer the only artefact that changes behaviour in production. Model version, *skill files*/*system prompts* and *eval suite* are three dimensions of their own on the critical path of the release — a model change without a code change can materially alter behaviour. Treating the *rollback* of these dimensions as independent of the application *rollback* is what makes the release as reversible as a code change. The runtime counterpart is `OPS-011`/`OPS-014` (observability and detection of *off-policy actions*).
- **DPL-011**: Automatic autonomy demotion closes the cycle between the evidence (eval suite, Policy 38 §5.4) and the operation: an agent only operates at the level that the *eval suite* confirms. The model *canary* is the agentic analogue of DPL-009 — the difference is that the promotion/rollback signal includes *off-policy events* and not only application metrics.

---

> For the runtime execution control model, see [Execution Control Model](./modelo-controle-execucao).
> For pre-deployment validations, see [Pre-Deployment Validations](./validacoes-pre-deploy).
> For rollback management and version control, see [Version Control and Rollback](./controle-versao-e-rollback).
> For progressive deployment and risk management in releases, see [Progressive Deployment and Risk](./deploy-progressivo-e-risco).
> For monitoring during and after deployment, see [Monitoring and Response](./monitorizacao-e-reacao).
