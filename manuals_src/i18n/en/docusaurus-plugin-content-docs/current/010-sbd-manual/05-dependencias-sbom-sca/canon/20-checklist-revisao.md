---
id: checklist-revisao
title: Checklist - Dependencies, SBOM and SCA
description: Binary verification of the application of the practices prescribed in Chapter 05
tags: [checklist, controlo, dependencias, sbom, sca, supply-chain]
sidebar_position: 20
sidebar_label: Review Checklist
translation:
  source_locale: pt
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/canon/20-checklist-revisao.md
  source_sha256: bd271277ee75c31c9012fa549c822f49170ee130ae20060bce2afa3714944799
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 29cb9c37683ee2b9cab2e70df52e665ba5aac5af1768b7c29835284d1447dcf2
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, instrument, lifecycle_phase, maturity, mcp, sbdtoe_sbd, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 1e1c1592af6e9f665439287c1fc5c79a87df1b481e9caa9098e0a46b3fda3929
  translated_at: 2026-09-26T08:45:28Z
  stamped_at: 2026-09-26T18:33:53Z
  reviewed_by: null
---


# Periodic Review Checklist - Dependencies, SBOM and SCA

This checklist applies to all applications that use third-party libraries, SDKs, open-source packages or binary artefacts.
It serves as a binary, auditable verification instrument of the **practical adoption of the prescriptions of Chapter 05** (`DEP-001` to `DEP-014`), enabling:

* Continuous control of the application of SCA and SBOM practices
* Verification per project at key moments of the lifecycle
* Generation of operational indicators that can be aggregated by team or organisation

> 🗓️ **It is recommended that it be reviewed at every release, dependency change or security exception**, as indicated in `aplicacao-lifecycle`.

---

## 📋 Verification Items {#-itens-de-verificação}

| Item                                                                                               | Verified? |
| -------------------------------------------------------------------------------------------------- | ----------- |
| Is there an SBOM generated automatically per build (CycloneDX or SPDX), including transitive dependencies, versioned and linked to the artefact? (`DEP-001`) | ☐           |
| Is the SBOM archived and accessible for audit, and signed with verified integrity (L3)? (`DEP-001`) | ☐           |
| Is there an SCA scanner integrated into the CI/CD pipeline? (`DEP-002`)                                         | ☐           |
| Is there a documented severity policy that distinguishes findings that block from those that only alert? (`DEP-002`) | ☐           |
| Does the pipeline block promotion in the face of unjustified critical/high findings, according to the level's threshold? (`DEP-002`) | ☐           |
| Are the SCA reports accessible and associated with each version/release, with findings triaged by severity, exposure and fix? (`DEP-002`) | ☐           |
| Is there a versioned lockfile without `latest`/`*`/unbounded range references, with integrity verifiable by hash? (`DEP-003`) | ☐           |
| Are there no libraries copied manually outside the package manager, with periodic audit and enforcement in CI/CD (L2–L3)? (`DEP-004`) | ☐           |
| Are only approved registries used in the build (allowlist enforced), with fallback to external registries controlled and audited? (`DEP-005`) | ☐           |
| Is there a formal approval process for new dependencies (maintenance, licence, CVEs, popularity), with a traceable record (version, hash, owner, date)? (`DEP-006`) | ☐           |
| Is there automatic validation of licence compatibility against an organisational allowlist?        | ☐           |
| Is there an update policy with an SLA/TTL per CVE severity and an active bot that generates PRs with impact analysis, requiring human intervention for breaking changes? (`DEP-007`/`DEP-008`) | ☐           |
| Is there traceability between findings, CVEs, exceptions and delivered artefacts (CVE → release)? (`DEP-010`) | ☐           |
| Are vulnerability exceptions formalised (justification, context of use, deadline, approver, compensation) and expired ones reviewed? | ☐           |
| Is the inventory boundary (SBOM boundary) defined and documented, with detection of emergent dependencies (unexpected delta) and an approval process? (`DEP-009`) | ☐           |
| Is there detection of composition drift between the SBOM and the runtime, with an incident opened in the event of divergence (L3)? | ☐           |
| Do systems with AI/ML components have an inventory of AI dependencies (models, datasets, MCP servers/tools, prompts) and an AI BOM per build (CycloneDX 1.6 `ml-bom`) linked to the SBOM? (`DEP-011`/`DEP-012`) | ☐           |
| Do the AI models have a pinned version (no `latest`/aliases), appear on a list of approved providers with a risk classification, and does a major version change trigger a new eval suite and a review of the threat model? (`DEP-013`/`DEP-014`) | ☐           |
| Are the practices documented and traceable in the repository or pipeline? | ☐           |

---

## 🔄 Operational Integration {#-integração-operacional}

* This checklist can be integrated into **pipelines, PR reviews, release gates or technical audits**.
* The results can be tracked per commit, per release or per artefact.
* Each item must be validated with **objective evidence** (e.g. `.sbom.json` files, reports, PR comments, issues).

> ⚠️ In the event of a negative answer, an approved formal exception must exist and be documented according to the chapter's exception model.

---

## ✅ Compliance and KPI {#-conformidade-e-kpi}

* Validation of this checklist makes it possible to declare **compliance with Chapter 05 - Dependencies, SBOM and SCA**.
* The count of affirmative answers can be used to **measure the degree of adoption of the prescribed practices**.
* This result can be aggregated by team, domain or organisation as an **indicator of operational maturity**.

> 📌 This operational mechanism is aligned with the model of continuous control and traceability defined in SbD-ToE.
