---

id: principios-sbd-iac
title: Security by Design Principles applied to IaC
sidebar_position: 4
description: Interpretation of Security by Design principles in the specific context of Infrastructure as Code.
tags: [princípios, security by design, iac, fundamentos, arquitetura segura]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/addon/04-principios-sbd-iac.md
  source_sha256: 78aa075498a9bb4a9856ac4dd65636ed06bcd67f03684b543bf78144b69249b2
  source_commit: 112711064196b71c545672fe3fb3ae412b36575e
  target_sha256: 096626757ee53ca45479a197704062f025e9a095ac468c9f362efc435edc5847
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, cycle_iteration, lifecycle_phase, provenance, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: a9ddc5e389cdb97f06a3ada03a34df5e98ddf5f50387c37319ee6c366b33184c
  translated_at: 2026-09-26T17:23:48Z
  stamped_at: 2026-09-26T18:34:34Z
  reviewed_by: null
---

# 🛡️ Security by Design Principles applied to IaC Projects

## 🌟 Objective {#-objetivo}

Ensure that all IaC projects are designed and maintained on the basis of structural principles of **security by definition**, reinforcing the reliability and resilience of the infrastructure they provision.

> The IaC project is a critical asset and must reflect, in its own code and structure, the security principles applicable to any application at risk.
> This includes preserving a **secure, versioned baseline** over time, and not merely validating a one-off configuration at a single moment.

---

## 📌 Essential principles applicable to IaC projects {#-princípios-essenciais-aplicáveis-a-projetos-iac}

| Principle                   | Practical application in the IaC context                                                                             |
| --------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Separation of environments**  | Independent directories, workspaces, pipelines and artefacts for `dev`, `staging`, `prod`                    |
| **Least privilege**       | Provisioned resources (e.g. roles, buckets, keys) must have only the strictly necessary permissions |
| **Traceability**         | All changes must be versioned and associated with author, ticket, environment and justification                |
| **Immutability**           | Critical resources must be redeployable, avoiding out-of-band changes                                   |
| **Consistency**            | Standardised naming conventions, tagging, directory layout and outputs                                      |
| **Controlled visibility** | Outputs, logs and metadata sufficient for auditing without exposing topology, secrets or permissions              |
| **Decoupling**          | Avoid hardcoded values, implicit dependencies and overlap between modules and environments                            |
| **Fail securely**           | Secure defaults (e.g. resources only created with tags and restrictive permissions by default)                     |
| **Baseline integrity** | Templates, modules, policies and exceptions keep review, versioning and deviation control over time |
| **Context minimisation** | Reduce to a minimum the exposure of plans, outputs, topology and metadata outside the controlled domain            |

---

## ⚠️ Untrusted code by origin {#️-código-não-confiável-por-origem}

Any IaC code that is:

* automatically generated,
* suggested by assisted tools,
* created from external templates,

**must be treated as untrusted code by origin**, regardless of the tool used.

Trust results exclusively from:

* automated technical validation;
* qualified human review;
* explicit evidence of approval;
* controlled execution in authorised pipelines.

This principle prevents systematic errors, insecure defaults or *hallucinations* from propagating automatically between environments.

---

## 📋 What must be done {#-o-que-deve-ser-feito}

1. Define and apply a structured layout for the repository, with logical separation of environments;
2. Use mandatory tags (environment, owner, type, criticality) on all provisioned resources;
3. Standardise names and variables, avoiding ambiguities and copy/paste errors;
4. Review permissions created by IaC, with particular attention to `iam_role`, `policy`, `security_group`, etc.;
5. Enforce a common structure across IaC projects, with base templates or approved scaffolding;
6. Avoid circular or implicit dependencies between modules and environments;
7. Treat *drift* and manual changes as a security failure and not as an acceptable exception;
8. Ensure that any automated change is validated and approved before execution.
9. Periodically review modules, templates, policies and exceptions to confirm that the secure baseline remains intact.

---

## ⚙️ Techniques and tools {#️-técnicas-e-ferramentas}

| Technique / Tool      | Practical application                                                          |
| ------------------------- | -------------------------------------------------------------------------- |
| IaC repository layout | `iac/ ├─ modules/ ├─ envs/ ├─ policies/ ├─ templates/`                     |
| Mandatory tagging       | `tags = { Environment = "prod", Owner = "appsec", ... }`                   |
| Pre-commit hooks          | Validation of naming, presence of tags and file structure             |
| Variable pattern       | `variable "environment" { type = string }` mandatory in all modules |
| Semantic tests         | OPA/Rego, Conftest to validate real impact and minimum policies           |
| Policy-as-Code            | Blocking of broad permissions, missing tags or incorrect naming        |
| Controlled reuse   | Validated base templates for `main.tf`, `variables.tf`, `outputs.tf`      |

---

## 🕒 When to apply {#-quando-aplicar}

| Lifecycle phase   | Expected action                                                 |
| ----------------------- | ------------------------------------------------------------- |
| Creation of the IaC project  | Define the layout and apply structural principles               |
| Addition of new modules | Review permissions, naming, outputs and tagging                   |
| Critical changes     | Revalidate adherence to the principles before approval         |
| Change of policy/template/provider | Revalidate the secure baseline and enforcement criteria   |
| Audit / review     | Verify traceability, tagging, exposure minimisation and baseline integrity |

---

## 👥 Profiles involved {#-perfis-envolvidos}

| Profile             | Responsibilities                                                  |
| ------------------ | ------------------------------------------------------------------ |
| DevOps / Cloud     | Implement structure, tagging, segregation and review of permissions |
| Security / AppSec | Define default policies and validate SbD principles                 |
| Architecture        | Approve layout, naming and output standards                      |
| DevOps / SRE (Platform) | Provide shared scaffolds, templates and validations             |

---

## 🧪 Practical examples {#-exemplos-práticos}

* `envs/prod/` directory with a `main.tf` file, where `variable "environment"` is mandatory;
* Mandatory tagging on resources such as `aws_instance`, `aws_s3_bucket`, validated by OPA;
* Example OPA rule:

```rego
deny[msg] {
  input.resource_type == "aws_s3_bucket"
  not input.tags["Environment"]
  msg := "Missing Environment tag on S3 bucket"
}
```

---

## ✅ Direct benefits {#-benefícios-diretos}

* Reduction of structural risk in the environments managed by IaC;
* Prevention of unintended exposure of topology and permissions;
* Consolidation of SbD principles across teams and projects;
* Capacity for consistent and auditable technical enforcement.

---

## 🔗 Cross-references {#-referências-cruzadas}

| Document                                       | Relation                                      |
| ----------------------------------------------- | -------------------------------------------- |
| `addon/02-validacoes-e-checks.md`               | Automated validations and evidence           |
| `addon/03-governanca-modulos.md`                | Module governance and supply chain         |
| `addon/11-uso-ferramentas-automatizadas-iac.md` | Automation and assisted tools           |
| SAMM (AA2.1, CM1.3)                             | Architecture standards and change control |
| SSDF (CM.5)                                     | Secure design and separation of environments       |
| SLSA                                            | Code provenance and traceability     |
