---
id: rastreabilidade-e-tags
title: Traceability and Versioning with Tags in IaC
sidebar_position: 7
description: Techniques to ensure traceability of changes, use of tagging and secure version management in IaC.
tags: [rastreabilidade, versionamento, tags, iac, git, segurança]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/addon/07-rastreabilidade-e-tags.md
  source_sha256: 9105d367c24ae92aaa1d02d10f17e9420a3760babba0bfad247526b428a715f5
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 2d2d6e3311375603bff381613f6091eac1afaa7fb0b81943763794153347142a
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [traceability]
  glossary_sha256: f2f188ebb3928e3a4139a39f31496c2554909ce8ad65b7f289e6c6f9380aa34d
  translated_at: 2026-09-26T09:25:37Z
  reviewed_by: null
---


# Traceability and Use of Tags in IaC Projects

## 🌟 Objective {#-objetivo}

Ensure that all changes, resources and environments defined via Infrastructure as Code (IaC) are **traceable, auditable and identifiable**, through tagging conventions, metadata and control of versioned changes.

> Traceability is a pillar of organisational security: it makes it possible to understand "who changed what, when, with what justification, and with what impact".

---

## 🔖 What must be done {#-o-que-deve-ser-feito}

1. **Apply mandatory tags to all resources created via IaC**, including environment, owner, criticality and origin;
2. **Maintain formal naming conventions** for resources, files, environments and releases;
3. **Record all changes in a version control system**, with readable commit messages linked to tickets;
4. **Include metadata in the code** that makes it possible to map changes to the affected resource and context;
5. **Document the relationships between files, modules and impacted environments**;
6. **Include application, team and purpose identification** in IaC manifests, outputs or logs.

---

## ⚖️ How it must be done {#️-como-deve-ser-feito}

| Element                 | Recommended practice                                                           |
| ------------------------ | ----------------------------------------------------------------------------- |
| Tags on resources         | `Environment`, `Owner`, `Application`, `Criticality`, `ManagedBy`             |
| Informative comments | Indicate the task ID, context and objective of the change                        |
| Commit messages          | Pattern: `[IaC] Alterar recurso X em ambiente Y (issue-123)`                   |
| Metadata in the manifests   | `locals` with application, team, version and date                                 |
| Release tracking     | Git tags: `iac-prod-v2025.07.10`, versioned artefacts with hash and timestamp |
| Execution output       | Logs with author, date, PR, executed plan, target environment                      |

---

## 🗓️ When to apply {#️-quando-aplicar}

| Moment                           | Expected action                                                     |
| --------------------------------- | ----------------------------------------------------------------- |
| Creation of a new resource           | Apply mandatory tags                                         |
| Significant change           | Record the justification, environment and associated ticket                |
| Execution of `plan/apply`          | Keep the output with hash, date and author identity               |
| Audit or security review | Verify metadata, naming, tagging and traceability per version |

---

## 💼 Practical examples {#-exemplos-práticos}

### 🌍 Tags in Terraform {#-tags-em-terraform}

```hcl
resource "aws_s3_bucket" "logs" {
  bucket = "app-logs-prod"

  tags = {
    Environment = "prod"
    Owner       = "devops-team"
    Criticality = "high"
    Application = "web-api"
    ManagedBy   = "Terraform"
  }
}
```

### 🔍 Local metadata {#-metadata-local}

```hcl
locals {
  app_name    = "billing-service"
  maintainer  = "infra-team@org"
  version     = "v1.3.2"
  last_update = "2025-07-10"
}
```

### 💪 Commit message with traceability {#-commit-message-com-rastreabilidade}

```
[IaC] Corrigir timeout no ALB do ambiente staging (ISSUE-8723)
```

---

## ✅ Direct benefits {#-benefícios-diretos}

* Enables auditing and incident investigation in an objective way;
* Increases visibility of the impact and authorship of changes;
* Supports rollback or approval decisions based on documented context;
* Reduces the risk of inconsistencies and facilitates quality control.

---

> 🔗 Aligned with requirements `IAC-002`, `IAC-005`, `IAC-008`, `REQ-004`, `REQ-006`, SSDF (CM.5), SAMM (AA2.1), CIS Controls (8.3, 4.6).
