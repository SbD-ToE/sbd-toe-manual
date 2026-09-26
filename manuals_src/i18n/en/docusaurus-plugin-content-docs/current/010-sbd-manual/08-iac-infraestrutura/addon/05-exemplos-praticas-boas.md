---

id: exemplos-praticas-boas
title: Examples of Secure IaC Good Practices
sidebar_position: 5
description: Annotated examples of code and secure practices to apply in Infrastructure as Code repositories.
tags: [exemplos, boas práticas, iac, código seguro, repositórios]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/addon/05-exemplos-praticas-boas.md
  source_sha256: c06f373263cab3c2f465040032d6391fa4fe39b7542b23e4c3720510e9e6d60c
  source_commit: 4430e7c4ca4536589773f3f465bd05857a1e6c38
  target_sha256: c1268f241613ae9df1249bedcb87d95ac71528e45cedf8c7769aea2c7cf8104a
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, traceability, validation_evaluation]
  glossary_sha256: 9c7b5947e75e98242f407d95526ddbe46a8d217cdf459331467e6f932143bf1e
  translated_at: 2026-09-26T09:45:04Z
  stamped_at: 2026-09-26T18:34:35Z
  reviewed_by: null
---

# 🛠️ Examples of Secure Structure and Practices in IaC Projects

## 🌟 Objective {#-objetivo}

Present **concrete, reusable and auditable examples** of how to structure and operate Infrastructure as Code (IaC) projects in a secure, coherent way aligned with the practices prescribed in this chapter.

This file is **illustrative and operational** in nature: it does not introduce new requirements, but demonstrates **how to apply the existing ones correctly**.

---

## 📁 Recommended repository structure {#-estrutura-recomendada-de-repositório}

```text
iac/
├── modules/
│   └── networking/
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       └── README.md
├── envs/
│   ├── dev/
│   │   ├── main.tf
│   │   └── backend.tf
│   ├── staging/
│   └── prod/
├── policies/
│   ├── opa/
│   └── conftest/
├── .github/workflows/
│   └── validate.yaml
├── .pre-commit-config.yaml
├── LICENSE
└── README.md
```

**Security properties ensured:**

* Physical and logical separation of environments;
* Controlled and reusable modularisation;
* Native integration of *policy-as-code*;
* Direct support for traceability and auditing.

---

## 🏷️ Example of mandatory tagging {#️-exemplo-de-tagging-obrigatório}

```hcl
tags = {
  Environment = var.environment
  Owner       = var.owner
  Application = var.application
  Criticality = var.criticality
  ManagedBy   = "Terraform"
}
```

* *Tags* are applied **by default** to all resources;
* The absence of any mandatory *tag* must result in a **blocking failure** via OPA/Rego.

---

## 🔐 Example of permission control (least privilege) {#-exemplo-de-controlo-de-permissões-privilégio-mínimo}

```hcl
resource "aws_iam_role" "example" {
  name = "app-deploy-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })

  managed_policy_arns = [aws_iam_policy.least_privilege.arn]
}
```

**Security notes:**

* No broad policy (`*`) is permitted by default;
* Permissions are explicitly attached and validated in *policy-as-code*;
* Mandatory review for any change to IAM.

---

## 🔄 Example of secure use of external modules {#-exemplo-de-uso-seguro-de-módulos-externos}

```hcl
module "vpc" {
  source = "git::https://github.com/org/vpc-module.git?ref=v1.2.3"

  cidr_block  = "10.0.0.0/16"
  environment = var.environment
}
```

**Good practices demonstrated:**

* Explicit reference to an immutable *tag* (`ref=vX.Y.Z`);
* Verifiable origin;
* Compatible with *digest* and *attestation* validation in the pipeline.

---

## 💪 Example of a CI workflow for IaC validation {#-exemplo-de-workflow-ci-para-validação-iac}

```yaml
name: Validate IaC

on:
  pull_request:
    paths:
      - 'iac/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Terraform Format
        run: terraform fmt -check -recursive

      - name: Terraform Validate
        run: terraform validate

      - name: TFLint
        uses: terraform-linters/setup-tflint@v1

      - name: tfsec
        run: tfsec ./iac

      - name: Checkov
        run: checkov -d ./iac
```

**Guarantees provided by the pipeline:**

* Syntactic and structural validation;
* Early detection of misconfigurations;
* Automatic blocking of non-conformities;
* Auditable evidence per PR/MR.

---

## 🧷 *Pre-commit hooks* template {#-template-de-pre-commit-hooks}

```yaml
repos:
  - repo: https://github.com/antonbabenko/pre-commit-terraform
    rev: v1.66.1
    hooks:
      - id: terraform_fmt
      - id: terraform_validate
      - id: terraform_tflint
      - id: terraform_tfsec
```

**Objective:**

* Shorten the *feedback loop*;
* Eliminate trivial errors before CI;
* Normalise quality across contributors.

---

## 🔗 Link to requirements {#-ligação-a-requisitos}

| Applied example                 | Related requirements   |
| -------------------------------- | ------------------------- |
| Modular repository structure | IAC-002, IAC-005, REQ-004 |
| Mandatory tagging              | IAC-002, IAC-008, REQ-006 |
| Use of versioned modules       | IAC-004, REQ-007          |
| CI workflow with scanners         | IAC-003, REQ-005, REQ-006 |
| Pre-commit hooks                 | IAC-003, REQ-006          |

---

## ✅ Direct benefits {#-benefícios-diretos}

* Accelerates the consistent adoption of secure IaC;
* Reduces variation between projects and teams;
* Facilitates auditing and technical *onboarding*;
* Turns security into an *operational default*.

---

> 🔗 These examples are aligned with the practices of **SSDF (PW.6)**, **SLSA (Build L2)** and **OWASP SAMM (AA2.1, CM1.1)**, serving as operational reference material for technical teams.
