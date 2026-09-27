---
id: validacoes-e-checks
title: Automated Validations and Quality Control in the IaC Project
sidebar_position: 1
description: Prescriptive validation, evidence and control strategies to ensure a secure, auditable and verifiable adoption of Infrastructure as Code.
tags: [planeamento, controlo, iac, segurança, validação, governação]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/addon/02-validacoes-e-checks.md
  source_sha256: 75050b241ce9cbe1e9a460691fbc288ad89f72ebac0416e97632e4d9e875e6a5
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 64a25027fee13cd04cf1f2802e687df0ab9e03ede85c4326b1f827fa81c339e6
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, papel_suporte, requirement_runtime, sbdtoe_sbd, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: a3539c00fbe42326acb2b6715adac54e7b9f264ac9b40348fa561949372694c8
  translated_at: 2026-09-26T09:25:34Z
  stamped_at: 2026-09-26T18:34:32Z
  reviewed_by: null
---

# Automated Validations and Quality Control in the IaC Project

## 🌟 Objective {#-objetivo}

Ensure that **all changes in Infrastructure as Code (IaC) projects** are treated as **untrusted input**, subject to **blocking automated validations**, and accompanied by **auditable evidence** before any application in a real environment.

This file establishes the **mandatory technical minimum** to ensure that the IaC project:

- is **correct** (syntax and structure);
- is **secure** (configuration, permissions, exposure);
- is **understood** (real impact of the `plan`);
- is **auditable** (evidence linked to the decision and to execution);
- does not degrade control when supported by **automation or assisted tools**.

> In the SbD-ToE model, automated validation is a **control mechanism**, not an optional optimisation.  
> Without blocking validation and minimum evidence, there is no effective governance of IaC.

---

## 🧩 Base principle: untrusted input by origin {#-princípio-base-entrada-não-confiável-por-origem}

In a modern engineering context, IaC changes may be produced by:
- humans,
- templates,
- normalisers,
- scripts,
- generators,
- assisted or automated mechanisms.

**Fundamental prescription:**  
👉 **The origin of a change is never a guarantee of security.**  
👉 **All proposed IaC is treated as untrusted input**, with additional reinforcement when the change is produced or modified by automated mechanisms.

Consequently:
- no change may reach `apply` without blocking validation;
- validation must address **real effects**, not only form;
- the decision to execute must be **explicit, traceable and evidenced**.

This principle is operationalised by the technical validations and gates defined in this document.

---

## 📌 What must be done (minimum prescription) {#-o-que-deve-ser-feito-prescrição-mínima}

The organisation **must ensure**, at a minimum:

1. Execution of **linters and syntax validators** (e.g. `terraform validate`, `tflint`);
2. Application of **IaC-specific security scanners**;
3. Validation of **compliance with internal policies** (naming, tagging, permissions, modules);
4. Integration of **all validations into the CI/CD pipeline**, with **mandatory failure**;
5. Generation and validation of **`terraform plan` (or equivalent)** before any `apply`;
6. **Semantic validation of the real impact** of the `plan`;
7. Automatic blocking when **critical requirements are not met**;
8. **Storage and correlation of minimum evidence** (plan + reports + approval).

---

## ⚙️ How to apply (types of validation) {#️-como-aplicar-tipos-de-validação}

| Type of Validation | Technical purpose |
|------------------|-------------------|
| **Syntactic** | Ensure that the code is valid and executable |
| **Structural / Linting** | Enforce standards, avoid recurring bad practices |
| **Security** | Detect exposures, excessive permissions, insecure configurations |
| **Policy-as-Code** | Enforce organisational rules automatically |
| **Semantic validation** | Assess the real impact of the `plan` |
| **Execution control** | Prevent `apply` without validation and approval |
| **Evidence** | Ensure decision → execution traceability |

### Illustrative tools and techniques {#ferramentas-e-técnicas-exemplificativas}

| Category | Examples |
|---------|----------|
| Syntax / format | `terraform fmt`, `terraform validate`, `yamllint` |
| Linting | `tflint`, `actionlint`, `ansible-lint` |
| Security | `tfsec`, `checkov`, `kics`, `terrascan` |
| Policies | OPA/Rego, Sentinel, Conftest |
| Pipeline | Mandatory gates on PR/MR and pre-`apply` |
| Local | Mandatory pre-commit hooks |

> Tools are **means**; the requirement is the **verifiable effect**.

---

## 🔍 Semantic validation of the `plan` (mandatory where applicable) {#-validação-semântica-do-plan-obrigatória-quando-aplicável}

Beyond syntax, the **real impact of the `plan`** must be assessed, including:

- creation, change or destruction of resources per environment;
- expansion of permissions (e.g. IAM, roles, wildcards);
- network exposure (public endpoints, permissive rules);
- absence of encryption or logging on critical resources;
- indirect changes through modules, providers or dependencies;
- unexpected or unexplained *diffs*.

**Prescription:**  
👉 Semantic validation **must work as a blocking gate**, not as an informational warning.

---

## 🧾 Mandatory minimum evidence {#-evidência-mínima-obrigatória}

For validation to be auditable, the organisation must ensure:

- `plan` generated in CI associated with:
  - PR/MR,
  - commit hash,
  - target environment;
- reports from linters, scanners and policies associated with the same PR/MR;
- explicit record of **approval before `apply`**;
- retention of artefacts proportional to risk and internal obligations.

Without this evidence, **there is no proof of control**, only technical execution.

---

## 🕒 When to apply {#-quando-aplicar}

| Moment | Expected validations |
|-------|----------------------|
| Commit / Push | Local linters, pre-commit hooks |
| Pull Request | Linters + scanners + policies + `plan` |
| Merge to release | Reinforced validation + complete evidence |
| Pre-`apply` | Final verification of plan, hashes and environment |
| Periodically | Drift, revalidation of modules and dependencies |

---

## 👥 Profiles involved {#-perfis-envolvidos}

| Role | Responsibility |
|-----|------------------|
| DevOps / Infra | Technical integration of the validations into the pipeline |
| AppSec / Security | Definition and maintenance of policies |
| Development | Remediation of findings and explanation of impact |
| Cloud / Architecture | Validation of real effects and secure design |

---

## 🧪 Practical examples {#-exemplos-práticos}

- Pipeline blocked by `tfsec` on overly broad IAM permissions;
- `checkov` preventing a merge because of an unencrypted bucket;
- OPA policy blocking a `plan` that creates a public endpoint;
- Mandatory `validate-iac` job before `apply`;
- PR rejected because of an unexplained *diff* on a critical resource.

---

## ✅ Control checklist (per project) {#-checklist-de-controlo-por-projeto}

- [ ] All changes are treated as untrusted input
- [ ] Automated validations are blocking
- [ ] Semantic validation of the `plan` exists
- [ ] `plan` and reports are linked to PR/MR + commit
- [ ] Approval before `apply` is recorded and auditable
- [ ] Evidence is retained according to criticality

---

## 🔗 Cross-references {#-referências-cruzadas}

| Document | Relation |
|---------|---------|
| `15-aplicacao-lifecycle.md` | User stories for validation, plan and approval |
| `addon/04-principios-sbd-iac.md` | SbD principles applied to IaC |
| `addon/11-uso-ferramentas-automatizadas-iac.md` | Rules for automation/assistance |

---

> ⚠️ The absence of blocking automated validations and minimum evidence turns IaC into a **privileged channel of systemic risk**, compromising security, auditing and governance.
