---

id: controle-enforcement
title: Execution Control and Policy Enforcement in IaC
sidebar_position: 6
description: Technical and organisational mechanisms to ensure automatic enforcement of security policies in IaC pipelines.
tags: [enforcement, controlo, políticas, iac, pipelines, segurança]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/addon/06-controle-enforcement.md
  source_sha256: cf7bd411d8e583170ae1db952e2dce91df9b57c148202932b94b6c40271414d1
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: a8a3f740b2e64795bc4cc6f731bb2fed8e42a96a820c18ad652ea7bd6442b277
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [cycle_iteration, discipline, lifecycle_phase, practitioner_manual, verification_taxonomy]
  glossary_sha256: 3cfda390a0457ad76a85d92317363d986f2836edea34a9646d46f66012265948
  translated_at: 2026-09-26T09:25:36Z
  reviewed_by: null
-------------------------------------------------------------------

# 🛡️ Continuous Enforcement of Security Policies and Rules in IaC

## 🌟 Objective

Ensure that all Infrastructure as Code (IaC) projects meet **minimum security requirements in an automatic, consistent and verifiable way**, through *policy enforcement* mechanisms integrated into the development and operations lifecycle.

This file defines **how policies are applied technically**, not which policies they are - that definition takes place in the requirements and in organisational policies.

> Enforcement is a **structural defence mechanism**: when it fails, the organisation depends solely on human discipline.

---

## 🔖 What must be done {#-o-que-deve-ser-feito}

1. Define **formal organisational policies** applicable to IaC (security, identity, network, data);
2. Translate those policies into **executable and testable rules** (*policy-as-code*);
3. Integrate enforcement in a **blocking** way into the CI/CD pipelines (pre-merge, pre-apply);
4. Centralise the rules in a **controlled repository**, with versioning and formal approval;
5. Allow **temporary exceptions** that are justified, traceable and have automatic *expiry*;
6. Continuously measure and review the effectiveness of enforcement (blocks, exceptions, bypass).

---

## ⚖️ How it must be done {#️-como-deve-ser-feito}

| Component          | Technical prescription                                                  |
| ------------------- | ------------------------------------------------------------------- |
| Policy engine | OPA/Rego, Sentinel (HashiCorp), Conftest, InSpec                    |
| Model              | Declarative, versioned and testable *Policy-as-Code*                 |
| Trigger             | Mandatory execution on PR/MR, *pre-merge* and *pre-apply*            |
| Severity          | Classification by impact (warn / block), aligned with L1–L3        |
| Feedback            | Clear, actionable messages per violated rule                     |
| Logging             | Central record of results per project, commit, author and environment |
| Exceptions            | Controlled per rule, with justification, TTL and AppSec/GRC approval |

---

## 🗓️ When to apply {#️-quando-aplicar}

| Moment                      | Expected action                                    |
| ---------------------------- | ------------------------------------------------ |
| Pull Request with IaC         | Mandatory execution of *policy checks*          |
| Pre-apply in real environments | Blocking enforcement before any `apply` |
| Policy update     | Review and controlled *rollout* of the rules        |
| Bypass detection           | Immediate alert + root cause analysis          |

---

## 💼 Practical examples {#-exemplos-práticos}

### ✏️ Example Rego rule (OPA) {#️-exemplo-de-regra-rego-opa}

```rego
deny[msg] {
  input.resource_type == "aws_s3_bucket"
  not input.tags.Environment
  msg := "Missing mandatory 'Environment' tag on S3 bucket"
}
```

### 🌍 Integration into the pipeline (GitHub Actions) {#-integração-em-pipeline-github-actions}

```yaml
- name: Policy enforcement (OPA)
  run: conftest test ./iac/envs/prod
```

**Expected result:**

* Violation → immediate *fail* of the job;
* Clear message associated with the rule;
* Evidence persisted for auditing.

---

## 📈 Direct benefits {#-benefícios-diretos}

* Reduction of risk from human error or omission;
* Consistent application of organisational policies;
* Objective and reproducible auditing;
* Less dependence on manual review;
* Solid technical foundation for *zero trust* in IaC.

---

## 🔗 Cross-references {#-referências-cruzadas}

| Document                                       | Relation to this file                                 |
| ----------------------------------------------- | --------------------------------------------------------- |
| `addon/02-validacoes-e-checks.md`               | Technical validations and quality before enforcement      |
| `addon/04-principios-sbd-iac.md`                | Fail securely, least privilege, controlled visibility |
| `addon/11-uso-ferramentas-automatizadas-iac.md` | Specific rules for automation and external tools  |
| `canon/20-checklist-revisao.md`                 | Binary verification of policy application            |
