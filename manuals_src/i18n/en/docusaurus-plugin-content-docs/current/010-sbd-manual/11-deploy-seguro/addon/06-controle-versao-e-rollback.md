---
id: controle-versao-e-rollback
title: Version Control and Rollback Strategies
description: Techniques for ensuring traceable and reversible versions with automatic, tested and documented rollback.
tags: [tipo:anexo, grupo:execucao, tema:rollback, versionamento, reversibilidade]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/addon/06-controle-versao-e-rollback.md
  source_sha256: b60966715c070634ea20cd876e8fb3d3fd501c7bd7c2cbb43dc1e0af67026b33
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: b99a719c8e757767f0030131690579d9080f6c5db8d8d343b446a3fcf37b4bbc
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 112d795f9bd927f0d4c24114e389470217eb00c1d6b919ae2df2e4f7bdb4878d
  glossary_keys: [cycle_iteration, lifecycle_phase, practitioner_manual, traceability, validation_evaluation]
  glossary_sha256: a6acbb1e762ee0c5eb79c8747aa9f83cececf7ec7e064de56f26947a3e448db2
  translated_at: 2026-09-26T11:00:50Z
  reviewed_by: null
---


# Version Control and Secure Rollback

Ensuring reversibility and traceability is essential to reduce the impact of failures in production. This document defines the recommended practices for version control, reliable rollback and the preparation of secure releases.

---

## 📂 Versioning as a pillar of security {#-versionamento-como-pilar-de-segurança}

- Use **semantic versioning** (`vX.Y.Z`) with a clear meaning:
  - `X` = breaking change
  - `Y` = new functionality
  - `Z` = fixes / hotfixes
- Associate each release with:
  - Commit hash or Git tag
  - Deployment date and time
  - Environment and scope
  - Release owner

> 🔗 There must be a 1:1 relationship between version, binary and validation documentation

---

## 🔄 Rollback: not an exception, a plan {#-rollback-não-é-exceção-é-plano}

Rollback must be planned as part of each release.

| Rollback type        | Description                                     | Example                          |
|-------------------------|-----------------------------------------------|----------------------------------|
| **Binary**             | Revert the artefact to the previous version       | Previous Git tag                 |
| **Configuration**        | Change feature flags / environment variables   | Toggle off                       |
| **Database**       | Revert the migration or use automatic rollback | Flyway, Liquibase                |
| **Infrastructure**      | Restore the previous state of resources         | Terraform rollback, snapshots    |

### Requirements: {#requisitos}

- Rollback must be **automatic or documented**
- Tested in staging before go-live
- Linked to rollback events in the logging system

---

## 🚫 Anti-patterns to avoid {#-antipadrões-a-evitar}

- Releases without a Git tag or verifiable hash
- Multiple artefacts with the same version number
- Untested / manual rollback
- Migrations with no possible reversal
- Changing production configuration manually and without a record

---

## 🌐 Tools and good practices {#-ferramentas-e-boas-práticas}

| Objective               | Tool / Practice                                     |
|------------------------|-----------------------------------------------------------|
| Git versioning      | `git tag`, `git describe`, `git hash-object`              |
| Idempotent build      | Hash included in the artefact, via the pipeline                 |
| Infra rollback         | Terraform, Helm + `helm rollback`                         |
| Reversible migration    | Reverse SQL scripts, Flyway `undo`, Liquibase `rollback` |
| Release audit  | Logging, CI/CD dashboards, audit trail                    |

---

## 🔀 Integration with the application lifecycle {#-integração-com-ciclo-de-vida-da-aplicação}

- Define rollback as a formal step in release planning
- Include rollback tests in the QA/staging environments
- Document the rollback in the functional changelog
- Associate releases with tickets, justifications and technical owners

---

## ✅ Version control and rollback checklist {#-checklist-de-controlo-de-versão-e-rollback}

- [ ] Is there a Git tag for the published version?
- [ ] Is the artefact signed and uniquely identified?
- [ ] Is there a documented and tested rollback plan?
- [ ] Can the migrations be reverted automatically?
- [ ] Was the rollback validated before go-live?
- [ ] Are the configuration changes versioned?

> 📊 These points are essential to maintain **resilience and confidence** in sensitive execution environments.
