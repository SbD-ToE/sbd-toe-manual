---

id: governanca-modulos
title: Module Governance and Secure Reuse
sidebar_position: 3
description: Prescriptive practices for the governance, validation and control of reusable modules in IaC, ensuring security, provenance and traceability.
tags: [governação, módulos, iac, reutilização, segurança, supply-chain, rastreabilidade]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/addon/03-governanca-modulos.md
  source_sha256: 06dd1db1d25aed958b9758815f7f3dc6910067007c1fd90f807813ea4d7257df
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: de55817bd73c7b0a0628651f5bd7f9178623f44b244f005bd9733e521b2bacdc
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, lifecycle_phase, provenance, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: f311aac6f5bc95780781a4c838f4b75f36169f6a425fa320fbe2fba386bcbed3
  translated_at: 2026-09-26T09:25:34Z
  reviewed_by: null
----------------------------------------------------------------------------------------

# 🛡️ Governance of Reusable Modules in IaC

## 🌟 Objective

Ensure that **all modules reused in Infrastructure as Code (IaC) projects** - internal or external - are treated as **supply chain components**, subject to formal governance, continuous validation and auditable evidence.

Specifically, this file establishes how to ensure that modules are:

* sourced from **trusted and identifiable sources**;
* **versioned, immutable and deterministic**;
* **validated before reuse**;
* **explicitly approved** for use per environment;
* **traceable** throughout the lifecycle;
* resistant to risks introduced by **automation and assisted tools**.

> Reuse without formal module governance represents a **systemic supply chain risk**: a single bad practice can propagate across multiple projects and environments.

---

## 🧩 Base principle: modules as untrusted code by origin {#-princípio-base-módulos-como-código-não-confiável-por-origem}

Regardless of whether they are:

* internal,
* external,
* automatically generated,
* suggested by templates or assisted tools,

👉 **every module must be treated as untrusted code by origin**.

Consequently:

* no module may be consumed without prior validation;
* trust is not implicit (neither from the author nor from the tool);
* the decision to reuse must be **explicit, traceable and evidenced**.

This principle aligns IaC module governance with modern **software supply chain security** practices.

---

## 📌 What must be done (minimum prescription) {#-o-que-deve-ser-feito-prescrição-mínima}

The organisation **must ensure**, at a minimum:

1. Formal registration of internal modules with:

   * origin,
   * accountable person (*owner*),
   * version,
   * approval status;
2. Validation of the **provenance and integrity** of external modules before adoption;
3. Definition of **trusted sources (allowlist)** and blocking of unauthorised origins;
4. Rigorous version control, avoiding floating references (`main`, `latest`, open ranges);
5. Mandatory minimum documentation per module (inputs, outputs, dependencies, effects);
6. Automated validation of internal modules before publication;
7. Inventory/SBOM of the modules actually used per environment;
8. Periodic review of critical modules in active use.

---

## ⚙️ How to apply (technical mechanisms) {#️-como-aplicar-mecanismos-técnicos}

| Dimension                 | Prescription                                                                 |
| ------------------------ | -------------------------------------------------------------------------- |
| **Internal modules**     | Central versioned repository, mandatory CI/CD, immutable releases      |
| **External modules**     | Reference with a fixed version or digest (`?ref=v1.2.3` or SHA)                |
| **Trusted sources**    | Explicit allowlist (e.g. `registry.terraform.io/org/`, `github.com/org/`) |
| **Version control**  | Prohibit `main`, `latest` and open ranges in L2/L3                         |
| **Integrity**          | Hash/digest verification where applicable                                |
| **Approval**            | Explicit association with risk analysis and approval decision             |
| **Automated validation** | Lint, security and documentation before `publish`                          |
| **Inventory / SBOM**    | List of modules used per deploy/environment                                |

---

## 🔍 Reinforced validation and control for automation/assistance {#-validação-e-controlo-reforçado-para-automaçãoassistência}

When modules are:

* automatically generated,
* changed in bulk,
* suggested by assisted tools,

**reinforced rules** must apply:

* semantic validation of the module's impact (resources, permissions, exposure);
* mandatory human review before approval;
* explicit evidence of the decision (who approved, why, for which environments).

> This control prevents **systematic errors or insecure defaults** from propagating automatically.

---

## 🕒 When to apply {#-quando-aplicar}

| Moment                             | Expected action                                         |
| ----------------------------------- | ----------------------------------------------------- |
| Inclusion of an external module          | Validate origin, version, integrity and compliance    |
| Creation/change of an internal module | Validate syntax, security and outputs before release |
| Build/deploy pipeline            | Confirm that only approved modules are used     |
| Periodic review                   | Check maintenance, vulnerabilities and active use    |
| Incident or alert                 | Reassess all projects that depend on the module     |

---

## 👥 Profiles involved {#-perfis-envolvidos}

| Role              | Responsibility                                    |
| ------------------ | --------------------------------------------------- |
| DevOps / Infra     | Technical integration and consumption of modules             |
| Architecture        | Definition of modular standards and authorised sources |
| AppSec / Security | Validation of origin, integrity and risk            |
| Cloud / Platform | Management of the internal repository and lifecycle       |
| GRC / Compliance   | Oversight of approval and traceability           |

---

## 🧪 Practical examples {#-exemplos-práticos}

**Secure reference to an external module**

```hcl
source = "git::https://github.com/org/vpc-module.git?ref=v1.2.3"
```

**Blocking unauthorised sources in the pipeline**

```bash
ALLOW_MODULE_SOURCES = [
  "registry.terraform.io/org/",
  "github.com/org/"
]
```

**Internal module publication pipeline**

* `tflint` (linting)
* `checkov` or `tfsec` (security)
* `terraform-docs` (up-to-date documentation)
* explicit approval before `release`

**Internal inventory (example)**

* Module name
* Owner
* Version
* Last validation
* Environments where it is used

---

## ⚖️ Proportionality L1–L3 {#️-proporcionalidade-l1l3}

| Control              | L1          | L2          | L3                             |
| --------------------- | ----------- | ----------- | ------------------------------ |
| Source allowlist   | Recommended | Mandatory | Mandatory                    |
| Version pinning     | Mandatory | Mandatory | Mandatory                    |
| Automated validation  | Recommended | Mandatory | Mandatory                    |
| Formal approval      | Recommended | Mandatory | Mandatory (reinforced)        |
| Inventory/SBOM       | Recommended | Mandatory | Mandatory                    |
| Periodic revalidation | Recommended | Mandatory | Mandatory + higher frequency |

---

## 🔗 Cross-references {#-referências-cruzadas}

| Document                                       | Relation                                    |
| ----------------------------------------------- | ------------------------------------------ |
| `addon/02-validacoes-e-checks.md`               | Validation and evidence of modules           |
| `addon/11-uso-ferramentas-automatizadas-iac.md` | Automation/assistance and process risks |
| SSDF (PW.4, CM.3)                               | Governance of reused components     |
| SLSA (Source L2+)                               | Code provenance and integrity       |
| CIS Controls (2, 8)                             | Secure management of reused software      |

---

> 📌 Module governance is a **structural supply chain control** in IaC. Without explicit validation, approval and evidence, reuse becomes a **risk multiplier**.
