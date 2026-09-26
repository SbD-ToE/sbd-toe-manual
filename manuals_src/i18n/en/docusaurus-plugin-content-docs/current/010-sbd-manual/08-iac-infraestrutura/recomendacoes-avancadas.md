---
id: recomendacoes-avancadas
title: Advanced Recommendations for Security in Infrastructure as Code (IaC)
sidebar_position: 30
description: Reinforced practices for contexts of greater maturity or regulatory requirements in IaC projects.
tags: [tipo:anexo, grupo:avancado, tema:iac, maturidade, reforço]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/recomendacoes-avancadas.md
  source_sha256: e289025c826a23ae31de75405dd8fca99b84955f95d34b5d60c41092fd4dedd4
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 554d1c088fdd0b68c1bbdb3e0365aab98e9237fd9b4178ed87e9a1dfae483331
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [audit_trail, cycle_iteration, maturity, mirror_osf, provenance, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: a85207602cbc623f8337e2fe85a5af629dcab6cf70e125df9d6615cd46e96ed1
  translated_at: 2026-09-26T09:25:46Z
  reviewed_by: null
---


# Advanced Recommendations for Secure IaC

This annex presents **reinforced practices** for security in **Infrastructure as Code (IaC)** projects. The recommendations described here **are not mandatory**, but should be considered in:

* Organisations with high security maturity;
* Regulated environments or environments with certification requirements;
* Projects with high exposure or risk (e.g. critical infrastructure);
* Supply chains that require proof of compliance (e.g. SLSA, ISO 27001, DSOMM level 3).

---

## 📌 Policy and semantic enforcement with OPA / Sentinel {#-enforcement-político-e-semântico-com-opa--sentinel}

| Theme                               | Description                                                            |
| ---------------------------------- | -------------------------------------------------------------------- |
| OPA with detailed Rego rules     | Create rules by resource type, environment and project                  |
| Enforcement with Sentinel (TFC/TFE) | Apply organisational policies with a Terraform execution gate      |
| Linters with adapted rulesets     | Use of Conftest, Checkov or tfsec with a customised profile per project |
| Comparison with the security baseline | Validate deviations from policy per repository/project             |
| Integration with CI/CD               | CI fails if the execution violates policies                             |

> 🎯 Reinforces trust, standardises the application of rules and enables proof of compliance.

---

## 📊 Reinforced provenance and traceability {#-proveniência-e-rastreabilidade-reforçada}

| Theme                                 | Description                                                                   |
| ------------------------------------ | --------------------------------------------------------------------------- |
| Hash and retention of `plan` files | Each execution must generate a `plan` file with a hash and retention per version     |
| Execution metadata                 | Commit, branch, tag, user, runner and hash associated with the applied plan |
| IaC template version               | Include in the repository and in the artefact being deployed                             |
| Tamper-proof application record      | Store the effective `plan` and `apply` in an auditable repository                |

> 📎 Facilitates audit, rollback, proof of state and forensic analysis.

---

## 🔁 Integration with cost and “drift” {#-integração-com-custo-e-drift}

| Theme                                 | Description                                                            |
| ------------------------------------ | -------------------------------------------------------------------- |
| Integration with `Infracost`           | Compare the estimated cost per `plan` with the approved baseline             |
| Continuous drift detection           | Active monitoring of differences between code and real infrastructure |
| Alerts for modifications outside Git | Verification of whether an `apply` occurred outside PRs or the pipeline               |

> 🧩 Integration with cost and drift enables early detection of anomalies, and financial and technical control.

---

## 🔐 Security in module provenance {#-segurança-na-proveniência-de-módulos}

| Theme                             | Description                                                                 |
| -------------------------------- | ------------------------------------------------------------------------- |
| Generation of SBOM for templates    | Record the modules, resources and providers used in a readable format           |
| Semantic validation of providers | Blocking of unaudited or untested versions                         |
| Replacement of external sources  | Specify internal mirrors, private registries and trusted repositories  |
| Audit of changes to modules | Validate whether changes introduce insecure configurations (e.g. open ACLs) |

> 💡 These practices help treat IaC modules as software, subject to a secure SDLC.

---

## 🧪 Programmatic infrastructure tests {#-testes-programáticos-de-infraestrutura}

| Theme                         | Description                                                                 |
|------------------------------|---------------------------------------------------------------------------|
| `terratest` with Go           | Tests of resource application and rollback, validating outputs and routes     |
| `opa test` for policies    | Unit tests for security rules written in Rego                |
| `kitchen-terraform`          | Integration tests of temporary environments                             |
| Integration into the pipeline       | Automatic tests per PR or release, with archived logs and results    |

> 🧬 Guarantees that the provisioned infrastructure is functional and secure, validating behaviour beyond syntax.

---

## 📋 Governance of technical exceptions {#-governação-de-exceções-técnicas}

| Theme                                | Description                                                                 |
|-------------------------------------|---------------------------------------------------------------------------|
| Validation of exceptions with a cycle     | Each exception with an owner, deadline and formal review                            |
| Audit of executions with bypass   | Logs of bypasses or forced flags analysed periodically               |
| Automation of reassessment           | Jobs that flag expired exceptions or exceptions due for review                       |
| Exception reports per stack    | Compliance dashboards per project and environment                         |

> 🧾 Continuous governance of exceptions ensures that technical *"security debt"* is visible, traceable and reviewed.

---

## ✅ Conclusion {#-conclusão}

These recommendations **are not mandatory**, but they constitute **valuable reinforcements for teams with high maturity** or that operate in regulated contexts.

> 📌 Their application directly reinforces the **Design & Development**, **Build & Test** and **Operate & Monitor** domains of OWASP DSOMM, making it possible to reach **level 3 maturity** in security practices applied to IaC.

For applications with an **L3** risk classification, it is recommended to consider a subset of these practices as a mandatory baseline.
