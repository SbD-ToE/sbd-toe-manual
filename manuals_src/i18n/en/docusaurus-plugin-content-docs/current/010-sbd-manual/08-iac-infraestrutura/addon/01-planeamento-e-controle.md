---
id: planeamento-e-controle
title: Planning and Control of Secure IaC Application
sidebar_position: 1
description: Planning and control strategies to ensure an effective and auditable adoption of security practices in Infrastructure as Code.
tags: [planeamento, controlo, iac, segurança, adoção, governação]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/addon/01-planeamento-e-controle.md
  source_sha256: 642701368b5bd293a909ed20dddefe0589156d4a28ec5ab88d3076cf198bc88d
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: a9eb0f8fb46943bf07e2dd92f09d94ff151d5a588af616596b7df2ceb5eecaf2
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, lifecycle_phase, maturity, papel_suporte, practitioner_manual, sbdtoe_sbd, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 0cfcedee5995a836a86fbb9a4853e6100e3ecf67898f4fcefdca08594af72b77
  translated_at: 2026-09-26T09:25:33Z
  stamped_at: 2026-09-26T18:34:32Z
  reviewed_by: null
---

# Execution Planning and State Control

## 🌟 Objective {#-objetivo}

Ensure that all Infrastructure as Code (IaC) projects maintain **consistent, secure and traceable control** of the **infrastructure state** and of the **execution plans** (`plan`) generated before any change.

This practice makes it possible to:

- Prevent *drift* and unauthorised changes;
- Avoid concurrency and conflicts between multiple operators;
- Enable secure auditing and rollback;
- Enable integration with CI/CD pipelines and approval processes;
- Ensure integrity and compliance with execution policies.

---

## 📌 What must be done {#-o-que-deve-ser-feito}

1. **Configure an authenticated remote backend** to store the state (`terraform.tfstate`, or equivalent);
2. **Enable a locking mechanism** to avoid concurrency during `apply`;
3. **Generate and version execution plans (`plan`)** before applying changes;
4. **Associate `plans` with approval mechanisms** (e.g. Pull Request, Change Request);
5. **Store plan artefacts and execution logs with verifiable integrity**;
6. **Detect and alert on *drift*** (the difference between actual and expected state);
7. **Prohibit manual local executions** outside a validated and controlled context.

---

## ⚙️ How to apply {#️-como-aplicar}

| Action                | Prescription                                                                 |
|---------------------|----------------------------------------------------------------------------|
| **Remote backend**  | S3 + DynamoDB (AWS), Azure Blob + CosmosDB, or GCS, with strong authentication |
| **Locking**         | `lock = true` + a mechanism such as DynamoDB, Consul or equivalent              |
| **CI/CD execution**  | Prohibit manual `apply`; `plan` generated and versioned in the pipeline              |
| **Traceability** | Tags, branches, PR/MR ID, release name and readable output in the diff          |
| **Auditing**       | Keep `plan` and logs with hashes and metadata (timestamp, hash, author)       |
| **Drift detection** | `terraform plan -detailed-exitcode`, `driftctl`, `tfsec`, or scheduled CI    |

---

## 🕒 When to apply {#-quando-aplicar}

| Moment                       | Expected action                                                        |
|-------------------------------|-----------------------------------------------------------------------|
| Start of the IaC project         | Define and document backend, environment and locking                     |
| New `apply` in production      | Generate `plan`, submit for approval, version the artefact              |
| After a rollback, error or patch  | Validate the current state and correct any divergence                          |
| Periodically (e.g. scheduled CI) | Check for *drift* between expected state and reality               |

---

## 👥 Profiles involved {#-perfis-envolvidos}

| Role            | Responsibility                                               |
|------------------|---------------------------------------------------------------|
| DevOps/Cloud     | Backend configuration, execution via pipeline                |
| Security        | Definition of the controlled execution policy                  |
| Architecture      | Approval of environments and isolation mechanisms             |
| GRC/Compliance   | Verification of traceability and audit mechanisms      |

---

## 🧪 Practical examples {#-exemplos-práticos}

- `terraform backend "s3"` with `encrypt = true`, `lock_table` and versioning;
- Pipeline with a job that runs `terraform plan`, stores the `.plan` and waits for approval before `apply`;
- DynamoDB table configured for locking, with TTL and per-project tags;
- Storage of plans and logs in a versioned bucket (`branch + timestamp + PR` as the artefact name).

---

## ✅ Good practices {#-boas-práticas}

- Never execute `terraform apply` locally in production environments;
- Validate and record `plan` before any significant change;
- Use artefacts with integrity hashes and cross-traceability with the PR or release;
- Periodically monitor divergences between the actual and the expected state (**drift detection**);
- Establish a formal organisational policy on controlled infrastructure execution.

---

## 🔗 Cross-references {#-referências-cruzadas}

| Document                      | Relation to this practice                            |
|--------------------------------|-----------------------------------------------------|
| `08-rastreabilidade-vulnerabilidades.md` | Reinforces auditing and traceability               |
| `04-integracao-ci-cd.md`       | Automated execution and validation of plans         |
| `02-matriz-requisitos-iac.md`  | Requirements `IAC-001`, `REQ-004`, `REQ-005`          |
| SSDF (PW.5) / SLSA (Build L2)  | Normative requirements on controlled execution     |

---

> 🔐 This control is essential to ensure integrity, traceability and compliance in the lifecycle of infrastructure as code - being one of the pillars of maturity in secure IaC according to the SbD-ToE model.
