---
id: aplicacao-lifecycle
title: How to Do It
description: Practical integration of IaC security practices into the SDLC, with proportionality by risk, reusable user stories and auditable evidence
tags: [tipo:aplicacao, ciclo-vida, iac, infraestrutura, seguranca, pipelines]
genia: us-format-normalization
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/aplicacao-lifecycle.md
  source_sha256: 3abd164d67c86a67458782c9420984a5df721a21e7b59509a63275b05b403430
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 1424cfd6ea992dcbbdd0cc10b296c78818bb61e12d2140093379b64e20aa5792
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, avaliacao, chapter_role, como_fazer, cycle_iteration, deterministic, discipline, lifecycle_phase, mapping, papel_suporte, practitioner_manual, provenance, requirement_runtime, risk_level, segregacao_de_funcoes, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 681837b4b54f4d69b4aef0052aa232c1f13114b3793c45b0e466a44d937f2341
  translated_at: 2026-09-26T09:25:41Z
  stamped_at: 2026-09-26T18:34:40Z
  reviewed_by: null
---

# Applying in the Lifecycle - Infrastructure as Code (IaC)

This document operationalises the practices prescribed for **Infrastructure as Code (IaC)**.  
While `intro.md` defines the “what” and the “why”, this document shows the “how”: in which phases of the lifecycle each requirement applies, who is responsible for carrying it out, how to translate it into reusable user stories and which evidence ensures traceability and auditability.  
The intention is clear: to turn prescriptions into **verifiable actions**, with proportionality by risk and complete traceability.

:::caution Operational Note - IaC as an automated and assisted process
The execution of IaC typically takes place in automated pipelines and, increasingly, with the **support of code and configuration generation/suggestion mechanisms** (templates, normalisers, generators, assistants, etc.).  
To keep control effective and auditable, operational invariants apply:

- **Suggestion is not decision**: only approved changes may reach `apply` (formal gates and SoD when applicable).
- **Plausibility is not evidence**: the only truth is the effective `plan` (and the artefacts generated), not the “intent” described in the PR.
- **Determinism is mandatory**: versions, providers, modules, policies and the execution environment must allow the `plan` to be reproduced.
- **Context minimisation**: plans, logs, diffs and external integrations must not expose secrets or sensitive topology.
- **The secure baseline must remain intact**: changes to modules, providers, policies or templates must reopen the review of the hardening posture before the next `apply`.

The user stories below operationalise these principles in a verifiable way, proportional to risk (L1–L3).
:::

---

## 🧭 When to apply {#-quando-aplicar}

Security in IaC must be applied **from planning through to operation**, ensuring that any change to infrastructure is controlled, auditable and reversible.

| *Trigger* moment | Security objective | Main roles |
|------------------|-----------------------|------------------|
| Creation of an IaC module | Ensure trusted origin and *pinning* | DevOps / SRE, AppSec Engineers |
| Execution of `plan` | Validate changes and safe simulations | DevOps / SRE, AppSec Engineers |
| Execution of `apply` | Execute only approved and signed changes | DevOps / SRE, GRC / Compliance |
| *Drift* audits | Detect divergences between IaC and the real environment | DevOps / SRE, AppSec Engineers |
| Module updates | Review provenance and *attestations* | AppSec Engineers, Internal Auditors |
| Change to policy/provider/template | Revalidate the baseline, enforcement rules and impact on hardening | DevOps / SRE, AppSec Engineers |
| Review of exceptions | Reassess risks and compensation deadlines | GRC / Compliance, AppSec Engineers |

---

## 🔁 Baseline integrity rule {#-regra-de-integridade-do-baseline}

In IaC, the object to protect is not only the final resource in the cloud or on-prem. The object to protect is also the **versioned baseline** that defines how that resource is born, is validated and may be changed. For this reason, the following must be treated as mandatory review events:

- change to modules, templates or providers;
- change to blocking policies or to `plan` / `apply` criteria;
- change of target environment, segregation or naming with operational impact;
- new exceptions that reduce hardening, validation or enforcement;
- *drift detection* results that reveal divergence between the baseline and the real state.

When one of these events occurs, the team must at least:

- confirm that the approved baseline remains secure for the current context;
- review whether the automatic validations and gates still block *unsafe overrides*;
- record the review decision and the respective *owner*;
- maintain traceability between module/template, `plan`, validation evidence and applicable exceptions.

---

## 👥 Who carries out each action {#-quem-executa-cada-ação}

| Operational action | Responsible | Support | Evidence/Artefacts |
|-------------------|--------------|--------|----------------------|
| Version modules and remote backends | DevOps / SRE | AppSec Engineers | `backend.tf`, `state.tf`, locking logs |
| Validate IaC format and syntax | Developers | Quality Assurance | Automatic validation reports |
| Apply *policy-as-code* in the *pipelines* | AppSec Engineers | DevOps / SRE | OPA/Sentinel reports |
| Sign *plans* and generate *attestations* | DevOps / SRE | AppSec Engineers | Digital signatures and `attestation.json` |
| Detect and correct *drift* | DevOps / SRE | AppSec Engineers | `plan -refresh-only` reports |
| Manage exceptions and reviews | GRC / Compliance | AppSec Engineers | `excecoes-iac.json`, approval logs |

---

## 🧾 Normalised User Stories {#-user-stories-normalizadas}

Each practice is expressed as a **reusable user story**, with verifiable criteria, concrete artefacts and proportionality by risk level (L1–L3).

---

### US-01 - Remote backend, locking and traceability {#us-01---backend-remoto-locking-e-rastreabilidade}

**Context.**  
Infrastructure state must be centralised, protected and versioned. Without a remote backend, the risks include loss of state, concurrency conflicts and the impossibility of audit.

:::userstory
**Story.**  
As **DevOps / SRE**, I want **to store state in a remote backend with locking and encryption**, so that *drift*, conflicts and loss of integrity are avoided.

**Acceptance criteria (BDD).**
- **Given** a new IaC project  
  **When** it is initialised  
  **Then** it uses a **remote backend** (S3+DynamoDB, Azure Blob, GCS) with **locking** active and **KMS encryption**.  
- **Given** a `terraform apply` in progress  
  **When** another operator attempts to execute  
  **Then** they are blocked until the **lock is released**.  
- **Given** an execution plan  
  **When** it is generated  
  **Then** it is stored versioned with **metadata** (timestamp, author, PR/MR ID).

**Checklist.**
- [ ] Remote backend configured and audited  
- [ ] Locking active (DynamoDB, Consul, or equivalent)  
- [ ] Encryption in transit and at rest  
- [ ] Versioned plan history  
:::

**🧾 Artefacts & evidence.**  
`backend.tf`, locking logs, state hash, plan metadata.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Yes | Remote backend + basic locking |
| L2 | Yes | Backend + locking + KMS encryption |
| L3 | Yes | Backend + locking + encryption + MFA + audit |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Project start | Initialisation of a new IaC project | DevOps / SRE | Remote backend, locking and KMS encryption at initialisation |
| Operations | Concurrent execution attempt during an `apply` | DevOps / SRE | Blocked until the lock is released |
| Development / Review | Generation of an execution plan | DevOps / SRE | Versioned plan with metadata (timestamp, author, PR/MR ID) |

---

### US-02 - Environment segregation, tagging and minimum permissions {#us-02---segregação-de-ambientes-tagging-e-permissões-mínimas}

**Context.**  
Environments (dev, staging, prod) must be isolated, with mandatory tags and restrictive permissions by principle. "Fail securely" begins here: resources are created without permissions, which are added only as needed.

:::userstory
**Story.**  
As **DevOps / SRE** and **Software Architects**, I want **segregated environments with mandatory tagging and minimum permissions by default**, so that accidental changes are avoided and traceability is ensured.

**Acceptance criteria (BDD).**
- **Given** a new IaC project  
  **When** it is initialised  
  **Then** it has segregated directories (`envs/dev/`, `envs/staging/`, `envs/prod/`) and a mandatory `variable "environment"`.  
- **Given** a created resource (e.g. S3 bucket, security group)  
  **When** it is provisioned  
  **Then** it has **mandatory tags**: Environment, Owner, Application, Criticality, ManagedBy.  
- **Given** a role or permission  
  **When** it is created  
  **Then** it has **minimum scope** (e.g. `s3:GetObject` for a single bucket only, not `s3:*`).

**Checklist.**
- [ ] Segregated environment directories  
- [ ] Mandatory tags on all resources  
- [ ] Permissions following the principle of least privilege  
- [ ] Validation of tagging + permissions in policy-as-code  
:::

**🧾 Artefacts & evidence.**  
Repository structure (`envs/`), module code with mandatory `tags`, OPA/Rego policy validating the presence of tags, `terraform plan` output showing permissions.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Yes | Minimum segregation + basic tags |
| L2 | Yes | Segregation + complete tags + validation of permissions |
| L3 | Yes | Segregation + tags + minimum permissions + enforcement in OPA |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Project start | Initialisation of a new IaC project | DevOps / SRE + Software Architects | Segregated environment directories and mandatory `variable "environment"` |
| Provisioning | Provisioning of a resource | DevOps / SRE + Software Architects | Mandatory tags: Environment, Owner, Application, Criticality, ManagedBy |
| Development / Review | Creation of a role or permission | DevOps / SRE + Software Architects | Minimum scope at creation |

---

### US-03 - Integrated automatic validations {#us-03---validações-automáticas-integradas}

**Context.**  
Syntax errors, insecure configurations and policy violations must be detected **before** any application in a real environment.

:::userstory
**Story.**  
As **Developers** and **AppSec Engineers**, I want **mandatory automatic validations in the pipeline** (lint, security, policies), so that errors and dangerous configurations are blocked.

**Acceptance criteria (BDD).**
- **Given** a commit with IaC  
  **When** it is pushed  
  **Then** **linters** (`terraform fmt`, `tflint`) and **security scanners** (`tfsec`, `checkov`) run automatically.  
- **Given** a critical policy violation  
  **When** it is detected  
  **Then** the pipeline **blocks the merge** and reports it in the PR.  
- **Given** a failed `plan`  
  **When** it does not pass minimum validation  
  **Then** the `apply` is prevented.

**Checklist.**
- [ ] Linters (`terraform validate`, `tflint`) in CI/CD  
- [ ] Security scanners (`tfsec`, `checkov`)  
- [ ] Policy-as-code (OPA/Rego, Sentinel)  
- [ ] Mandatory pre-commit hooks  
:::

**🧾 Artefacts & evidence.**  
Lint reports, scanner outputs, pipeline logs, compliance badges.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Yes | Linters + warning |
| L2 | Yes | Linters + scanners + blocking on severe findings |
| L3 | Yes | Linters + scanners + policies + 100% coverage |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| CI/CD | Push of a commit with IaC | Developers + AppSec Engineers | Linters and security scanners on every push |
| PR/MR | Critical policy violation detected | Developers + AppSec Engineers | Merge blocked, reported in the PR |
| Deploy / Operation | `plan` that does not pass minimum validation | Developers + AppSec Engineers | `apply` prevented |

---

### US-04 - Governance and trusted origin of modules {#us-04---governança-e-origem-confiável-de-módulos}

**Context.**  
Poorly maintained or unverified modules propagate risks through the supply chain. Origin, version, compliance and provenance must be validated before use is permitted.

:::userstory
**Story.**  
As **AppSec Engineers**, **Software Architects** and **DevOps / SRE**, I want **formal module governance with verification of trusted origin**, so that the propagation of bad practice is avoided and supply chain risk is reduced.

**Acceptance criteria (BDD).**

**Phase 1: Governance & Approval**
- **Given** a new external module  
  **When** it is referenced in the project  
  **Then** it must be on the **allowlist** and be **pinned to an exact version** (no `main`, `latest`).  
- **Given** an internal module  
  **When** it is published  
  **Then** it has gone through **automated tests**, **linting** and **explicit review**.  
- **Given** a module update  
  **When** it has a reported vulnerability  
  **Then** it is flagged and a review of its use is **mandatory**.

**Phase 2: Trusted Origin & Verification**
- **Given** a new module  
  **When** it is referenced in the repository  
  **Then** it must be on the **allowlist** and be **versioned** (no *ranges*) with a verified **digest**.  
- **Given** a module update  
  **When** the *pipeline* runs  
  **Then** it validates the **attestation** and refuses it if the origin does not comply with the policy.  
- **Given** a *private* module  
  **When** it is consumed  
  **Then** a **signature** from the internal producer and review by **AppSec** are required.

**Checklist.**
- [ ] Versioned central repository of internal modules  
- [ ] **Whitelist/allowlist** of external sources published  
- [ ] **Version pinning** verified in the pipeline  
- [ ] Module **SBOM** on every deploy  
- [ ] **Allowlist/denylist** policy published  
- [ ] **Digest/SHA256** verified in the *pipeline*  
- [ ] **Attestation** required for external sources  
:::

**🧾 Artefacts & evidence.**  
Module registry, whitelist policy, SBOM, approval records, update history, digest/attestation verification, pipeline logs with an origin gate.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Yes | Simple whitelist + versioning + pinning |
| L2 | Yes | Whitelist + automatic validation + SBOM + verified digest |
| L3 | Yes | Whitelist + validation + SBOM + attestation and AppSec review; active denylist |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Governance | Reference to a new external module | AppSec Engineers + Software Architects + DevOps / SRE | On the allowlist and pinned to an exact version, with neither `main` nor `latest` |
| Governance | Publication of an internal module | AppSec Engineers + Software Architects + DevOps / SRE | Automated tests, linting and explicit review before publication |
| Governance | Vulnerability reported in a module update | AppSec Engineers + Software Architects + DevOps / SRE | Flagging and mandatory review of use |
| CI/CD | Reference to a new module in the repository | AppSec Engineers + Software Architects + DevOps / SRE | On the allowlist, versioned without ranges and with a verified digest |
| CI/CD | Pipeline execution on a module update | AppSec Engineers + Software Architects + DevOps / SRE | Attestation validation; refusal if the origin does not comply with the policy |
| CI/CD | Consumption of a private module | AppSec Engineers + Software Architects + DevOps / SRE | Signature from the internal producer and review by AppSec |

---

### US-05 - Traceability, versioning and naming {#us-05---rastreabilidade-versionamento-e-naming}

**Context.**  
Changes must be traceable via Git with formal conventions for commits, tagging and releases. Resource names must follow a consistent pattern.

:::userstory
**Story.**  
As **DevOps / SRE** and **GRC / Compliance**, I want **a complete history of changes with naming conventions, git tags and versioned releases**, so that rollback and audit are supported.

**Acceptance criteria (BDD).**
- **Given** an infrastructure change  
  **When** it is committed  
  **Then** it follows the pattern: `[IaC] Tipo de mudança em ambiente Y (issue-XXX)` and links to a ticket.  
- **Given** a release that is ready  
  **When** it is promoted to production  
  **Then** a git tag is created in semantic format (`iac-prod-v2025.07.10`, hash, timestamp).  
- **Given** a naming convention  
  **When** it is violated  
  **Then** the change is rejected by a pre-commit hook or linter.

**Checklist.**
- [ ] Naming conventions defined (`app-env-resource-counter`)  
- [ ] Pre-commit hooks validate the pattern  
- [ ] Semantic tagging on releases  
- [ ] Changelog documentation  
:::

**🧾 Artefacts & evidence.**  
`NAMING.md` file, Git logs with structured commits, tags and releases in the repository, pre-commit validation output.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Recommended | Simple naming + basic git |
| L2 | Yes | Naming + commit conventions + tagging |
| L3 | Yes | Naming + conventions + semantic tagging + CHANGELOG |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Development / Review | Commit of an infrastructure change | DevOps / SRE + GRC / Compliance | Message pattern and link to a ticket in the commit |
| Release | Promotion of a release to production | DevOps / SRE + GRC / Compliance | Semantic git tag with hash and timestamp at promotion |
| CI/CD | Violation of a naming convention | DevOps / SRE + GRC / Compliance | Rejection by a pre-commit hook or linter |

---

### US-06 - Formal plan review before apply {#us-06---revisão-formal-de-plan-antes-de-apply}

**Context.**  
The `terraform plan` (or equivalent) must be reviewed and approved before any application. This makes it possible to validate impact, detect unexpected changes and associate the change with a change request.

:::userstory
**Story.**  
As **DevOps / SRE** and **AppSec Engineers**, I want **formal approval of the `terraform plan` in the PR before `apply`**, so that impact is validated and associated with change control.

**Acceptance criteria (BDD).**
- **Given** a PR with an IaC change  
  **When** it is submitted  
  **Then** the pipeline runs `terraform plan` and attaches readable output in a PR comment.  
- **Given** the plan is reviewed  
  **When** there are no unexpected changes  
  **Then** it receives explicit approval (co-sign by at least 2 roles: DevOps + AppSec).  
- **Given** a scheduled `apply`  
  **When** it concerns a critical environment (staging/prod)  
  **Then** it requires **dual approval** and a **change window**.

**Checklist.**
- [ ] Pipeline runs `terraform plan` in the PR  
- [ ] Readable plan output attached  
- [ ] Approval required (at least 2 roles)  
- [ ] Approval audit recorded  
:::

**🧾 Artefacts & evidence.**  
PR with the plan attached, approval comments, gate logs in the pipeline, approval trail.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Recommended | Plan attached to the PR |
| L2 | Yes | Plan + simple approval |
| L3 | Yes | Plan + dual approval + change window |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| PR/MR | Submission of a PR with an IaC change | DevOps / SRE + AppSec Engineers | `terraform plan` executed and attached to the PR on submission |
| Development / Review | `plan` reviewed with no unexpected changes | DevOps / SRE + AppSec Engineers | Explicit approval with co-sign by at least two roles |
| Deploy / Operation | `apply` scheduled for a critical environment (staging/prod) | DevOps / SRE + AppSec Engineers | Dual approval and change window before the `apply` |

---

### US-07 - File → resource → environment traceability {#us-07---rastreabilidade-ficheiro--recurso--ambiente}

**Context.**  
There must be a clear mapping between changes to IaC files, resources created and environments affected. This supports accountability and impact assessment.

:::userstory
**Story.**  
As **GRC / Compliance** and **Internal Auditors**, I want **a documented mapping of IaC file → resource → environment**, so that impact and traceability can be validated.

**Acceptance criteria (BDD).**
- **Given** a resource in production  
  **When** I need to identify its origin  
  **Then** I can map: `.tf` file (branch + commit) → resource (ID, name) → environment (prod).  
- **Given** a compliance audit  
  **When** it is executed  
  **Then** I can generate a report of "resource created in environment X by whom, when, with what code".  
- **Given** metadata in code  
  **When** it is preserved (e.g. `locals { application = "..." }`, tags with the application)  
  **Then** it facilitates automatic traceability.

**Checklist.**
- [ ] Metadata in `locals` with application, owner, version  
- [ ] Tags include application and team  
- [ ] Dashboard/script that maps resource → file → commit  
- [ ] Documentation of relationships between modules  
:::

**🧾 Artefacts & evidence.**  
Metadata in code, tags on resources, traceability dashboard, mapping script, `terraform apply` logs with artefacts.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Recommended | Metadata in locals |
| L2 | Yes | Metadata + tags + documentation |
| L3 | Yes | Metadata + tags + automatic traceability dashboard |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Operations | Need to identify the origin of a resource in production | GRC / Compliance + Internal Auditors | `.tf` file (branch + commit) → resource → environment mapping available |
| Audit | Execution of a compliance audit | GRC / Compliance + Internal Auditors | Report of resource, environment, author, date and code |
| Development / Review | Preservation of metadata in code | GRC / Compliance + Internal Auditors | Metadata in `locals` and tags kept in the change |

---

### US-08 - Automatic policy enforcement {#us-08---enforcement-automático-de-políticas}

**Context.**  
Security policies must be applied automatically via OPA/Sentinel/Rego in the pipeline, without relying exclusively on manual review.

:::userstory
**Story.**  
As **AppSec Engineers** and **DevOps / SRE**, I want **automatic policy enforcement in the pipeline** (blocking of broad permissions, missing tags, etc.), so that compliance is applied systematically.

**Acceptance criteria (BDD).**
- **Given** a resource with broad permissions (e.g. `s3:*`)  
  **When** it is validated in `conftest` or OPA  
  **Then** it is **rejected automatically** with a clear message.  
- **Given** a configured policy (e.g. "all S3 buckets must have versioning")  
  **When** it is executed in the pipeline  
  **Then** it blocks the `apply` if it is not met.  
- **Given** a justified exception  
  **When** it is recorded (e.g. comment `# opa-exception: IAC-003`)  
  **Then** it is audited and counted in compliance metrics.

**Checklist.**
- [ ] OPA/Rego/Sentinel rules defined and versioned  
- [ ] Integration into the pipeline (pre-merge, pre-apply)  
- [ ] Traceable exception mechanism  
- [ ] Compliance metrics (% blocks, active exceptions)  
:::

**🧾 Artefacts & evidence.**  
OPA rules in the repository, execution output, block logs, recorded exceptions, compliance metrics.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Recommended | Basic validation in the pipeline |
| L2 | Yes | OPA/Rego with enforcement, block logs |
| L3 | Yes | OPA/Rego + formal exceptions + metrics + quarterly review |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| CI/CD | Resource with broad permissions validated in OPA or `conftest` | AppSec Engineers + DevOps / SRE | Automatic rejection with a clear message |
| Deploy / Operation | Execution of a policy in the pipeline | AppSec Engineers + DevOps / SRE | `apply` blocked if the policy is not met |
| Governance | Record of a justified exception | AppSec Engineers + DevOps / SRE | Audited and counted in metrics; quarterly review at L3 |

---

### US-09 - Signing and Provenance of IaC artefacts {#us-09---assinatura-e-proveniência-de-artefactos-iac}

**Context.**  
Without verifiable provenance, *plans* and *applies* can be tampered with. Signatures and **attestations** must be verified **before promotion**.

:::userstory
**Story.**  
As **DevOps / SRE** and **AppSec Engineers**, I want **to sign *plans* and record *pipeline* *attestations***, so that end-to-end integrity is ensured up to the *apply* in a critical environment.

**Acceptance criteria (BDD).**
- **Given** a generated `terraform plan`  
  **When** it is submitted for review  
  **Then** it must be **signed** and have a *pipeline* **attestation**.  
- **Given** a promotion to `prod`  
  **When** the *gate* validates artefacts  
  **Then** it rejects any *plan/apply* **without a valid signature** or **attestation**.

**Checklist.**
- [ ] Signing of the `plan` and *apply logs*  
- [ ] *Pipeline* **attestation** (SLSA-like)  
- [ ] Verification gate before `prod`  
:::

**🧾 Artefacts & evidence.**  
Signature files; `attestation.json`; *gate* *logs*; approval trail.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Recommended | Signing of the `plan` |
| L2 | Yes | Signing + automatic verification |
| L3 | Yes | Signing + **attestation** and blocking *gate* |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Development / Review | Submission of the `terraform plan` for review | DevOps / SRE + AppSec Engineers | `plan` signed and with a pipeline attestation |
| Deploy / Operation | Promotion to `prod` assessed by the gate | DevOps / SRE + AppSec Engineers | Rejection of any `plan`/`apply` without a valid signature or attestation, before promotion |

> **Common Pattern:** Signing and provenance verification take place in **multiple contexts** (CI/CD, IaC, images, deploy).
> This US focuses on the context of **IaC modules and *plans***; see also **Ch. 07-US-06** (CI/CD),
> **Ch. 09-US-03** (images), **Ch. 11-US-01** (deploy). All apply the **same principle** (sign → validate → use).

---

### US-10 - Management of secrets and identities for IaC {#us-10---gestão-de-segredos-e-identidades-para-iac}

**Context.**  
Static keys in *providers* or *runners* represent a high risk. **OIDC / workload identity**, minimum *scopes* and **short TTL** are preferred.

:::userstory
**Story.**  
As **DevOps / SRE** and **AppSec Engineers**, I want **to issue temporary credentials via OIDC/workload identity** with **minimum permissions**, so that long-lived keys are eliminated and abuse is reduced.

**Acceptance criteria (BDD).**
- **Given** an IaC *pipeline*  
  **When** it needs to access the *provider*  
  **Then** it obtains an **ephemeral token** via OIDC, with minimum *scope* and **TTL ≤ 1h**.  
- **Given** a compromised *runner*  
  **When** the token expires  
  **Then** reuse or escalation is **not** possible.

**Checklist.**
- [ ] OIDC/workload identity configured  
- [ ] Minimum *scopes* and *boundaries* per environment  
- [ ] Prohibition of static keys in the repository  
:::

**🧾 Artefacts & evidence.**  
Secrets policy; OIDC configuration; issuance/expiry *logs*.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Yes | Secrets encrypted and rotated |
| L2 | Yes | Mandatory OIDC with short TTL |
| L3 | Yes | OIDC + *Just-In-Time* + audited *break-glass* |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| CI/CD | IaC pipeline that needs to access the provider | DevOps / SRE + AppSec Engineers | Ephemeral token via OIDC with minimum scope and TTL ≤ 1h |
| Operations | Token expiry | DevOps / SRE + AppSec Engineers | No reuse or escalation after expiry |

---

### US-11 - Detection and correction of *drift* {#us-11---deteção-e-correção-de-drift}

**Context.**  
Manual changes at *runtime* create **misalignment** (*drift*) with the IaC. It must be **audited** and **corrected** in a controlled way.

:::userstory
**Story.**  
As **AppSec Engineers** and **DevOps / SRE**, I want **periodic *drift* audits** and **controlled correction**, so that coherence between IaC and infrastructure is maintained.

**Acceptance criteria (BDD).**
- **Given** a fortnightly cycle  
  **When** `terraform plan -refresh-only` runs  
  **Then** ***drift* reports** are generated per environment.  
- **Given** critical *drift* in `prod`  
  **When** it is confirmed  
  **Then** a correction task is created with **approval** before the *apply*.

**Checklist.**
- [ ] Scheduled *drift* job per environment  
- [ ] Versioned reports  
- [ ] Corrections via PR + review  
:::

**🧾 Artefacts & evidence.**  
*Drift* reports; correction PRs; approvals.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Yes | Monthly audit |
| L2 | Yes | Fortnightly + alerts |
| L3 | Yes | Weekly + *gate* for critical *drift* |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Governance | Scheduled `terraform plan -refresh-only` cycle | AppSec Engineers + DevOps / SRE | Monthly (L1), fortnightly (L2), weekly (L3) |
| Operations | Critical drift confirmed in `prod` | AppSec Engineers + DevOps / SRE | Correction task with approval before the `apply` |

---

### US-12 - *Rollback* and *destroy* safeguard {#us-12---rollback-e-salvaguarda-de-destroy}

**Context.**  
Failed *applies* and accidental *destroys* have a high impact. A ***rollback* strategy** and *guardrails* are required.

:::userstory
**Story.**  
As **DevOps / SRE**, I want **restore points**, **explicit confirmations** for *destroy* and a ***rollback* procedure**, so that *downtime* is reduced and data loss is avoided.

**Acceptance criteria (BDD).**
- **Given** a failed *apply*  
  **When** a *rollback* is triggered  
  **Then** critical resources return to their previous state.  
- **Given** a `destroy` operation  
  **When** it runs in `prod`  
  **Then** it requires **dual confirmation** and a **change window**.

**Checklist.**
- [ ] *Snapshots* of state/critical resources  
- [ ] Tested *rollback* procedure  
- [ ] *Kill-switch* for *destroy* in `prod`  
:::

**🧾 Artefacts & evidence.**  
`rollback.md` procedure; *snapshots*; dual confirmation *logs*.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Yes | Documented manual *rollback* |
| L2 | Yes | Automatic *snapshots* |
| L3 | Yes | Automated *rollback* and *kill-switch* |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Operations | Rollback triggered after a failed `apply` | DevOps / SRE | Critical resources restored to their previous state |
| Deploy / Operation | `destroy` operation in `prod` | DevOps / SRE | Dual confirmation and change window before execution |

---

### US-13 - Change window and approvals by role {#us-13---janela-de-mudança-e-aprovações-por-papel}

**Context.**  
Changes in critical environments require a **change window** and **multi-level approval**.

:::userstory
**Story.**  
As **GRC / Compliance**, **AppSec Engineers** and **Internal Auditors**, I want **defined change windows** and **approvals by role** before the *apply* in `prod`, so that operational risk is reduced.

**Acceptance criteria (BDD).**
- **Given** a change to `prod`  
  **When** the *plan* is approved  
  **Then** the *apply* takes place **only** within the authorised window and with **PO/AppSec/GRC** approvals.

**Checklist.**
- [ ] Change windows published  
- [ ] Multi-level approval flow  
- [ ] Complete audit trail  
:::

**🧾 Artefacts & evidence.**  
Change calendar; approval records; *apply* *logs*.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Optional | Simple approval |
| L2 | Yes | PO + AppSec approval |
| L3 | Yes | PO + AppSec + GRC approval |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Deploy / Operation | `plan` approved for a change in `prod` | GRC / Compliance + AppSec Engineers + Internal Auditors | `apply` only within the authorised window, with PO/AppSec/GRC approvals |

---

### US-14 - Formal exceptions in IaC {#us-14---exceções-formais-em-iac}

**Context.**  
Not all policies can be met in all circumstances. Exceptions must be **temporary**, **justified** and have **compensations** (addon/09).

:::userstory
**Story.**  
As **GRC / Compliance** and **AppSec Engineers**, I want **recorded exceptions** with a **deadline** and **countermeasures**, so that structural debt is avoided.

**Acceptance criteria (BDD).**
- **Given** an exception request  
  **When** it is analysed  
  **Then** it is only approved with a **deadline** and **compensations**; **expired** → **revoke** and restore the policy.

**Checklist.**
- [ ] Exception record with an owner  
- [ ] Deadline and countermeasures  
- [ ] Automated periodic review  
:::

**🧾 Artefacts & evidence.**  
`excecoes-iac.json`; decisions; review and expiry *logs*.

> **Reference:** This US implements the formal exceptions process (governance) in the context of Infrastructure-as-Code. Approval, TTL and compensations must follow the applicable organisational policy.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Yes | Single approval |
| L2 | Yes | Dual approval (AppSec+PO) |
| L3 | Yes | AppSec+GRC approval and *review* per sprint |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Governance | Exception request submitted for analysis | GRC / Compliance + AppSec Engineers | Approval only with a deadline and compensations; review per sprint at L3 |
| Exception | Expired exception | GRC / Compliance + AppSec Engineers | Revocation and restoration of the policy on expiry |

---

## 🛡️ SbD Principles Reinforced in IaC {#️-princípios-de-sbd-reforçados-em-iac}

### Fail Securely (Failing Securely) {#fail-securely-falhar-com-segurança}

The principle of **fail securely** in IaC establishes that resources and permissions must have **secure defaults** by default, with **explicit refusal** instead of broad permission:

**Practical implementation (US-02, US-08):**
- Resources created **without permissions**; permissions are added explicitly after justification
- Example: `aws_s3_bucket` with `block_public_acls = true` as an automatic default
- Policy-as-code rejects any S3 bucket **without** *server-side encryption* enabled
- Rego rule: `deny[msg] { input.resource == "aws_s3_bucket" }` with no encryption

**Validation checklist (reinforced in US-03, US-08):**
- [ ] Validation of secure defaults in **policy-as-code** (OPA/Sentinel)
- [ ] Automatic rejection of resources without minimum compliance
- [ ] Documentation of exceptions to defaults (traceable and temporary)

---

### Decoupling between Modules and Environments {#desacoplamento-entre-módulos-e-ambientes}

The principle of **decoupling** prevents circular or implicit dependencies that compromise reuse and testability:

**Practical implementation (US-02, US-04):**
- IaC modules do not contain **hardcoded** outputs of other modules
- WRONG example: `security_group_id = module.network.security_group_id` hardcoded
- RIGHT example: `security_group_id = var.security_group_id` (passed as a variable)
- Segregated environments do not contain cross-references between backend states

**Validation checklist (reinforced in US-03, US-06):**
- [ ] Linter detects hardcodes and invalid interdependencies
- [ ] Modules published with documented and typed outputs
- [ ] Automated tests validate module independence

---

## 📦 Expected Artefacts & Evidence {#-artefactos--evidências-esperadas}

Each practice leaves an objective footprint.  
Without evidence, there is no compliance. The table below summarises the expected outputs.

| Artefact/Evidence | Origin / US | Remarks |
|---|---|---|
| `backend.tf` + locking logs | US-01 | Proof of locking and KMS encryption |
| `plan` history with metadata | US-01 | Timestamp, author, PR/MR ID, hash |
| Directory structure per environment | US-02 | `envs/dev/`, `envs/staging/`, `envs/prod/` |
| Mandatory tags on resources | US-02 | Environment, Owner, Application, Criticality, ManagedBy |
| Evidence of minimum permissions (IAM/policies) | US-02 | `plan` outputs + validations in policy-as-code |
| Lint/security reports | US-03 | `terraform validate`, `tflint`, `tfsec`, `checkov`, etc. |
| Validation configuration in CI/CD + pre-commit | US-03 | Pipeline jobs, mandatory hooks |
| Allowlist/denylist of modules and sources | US-04 | Published and versioned policy |
| Registry of internal modules + documentation | US-04 | Versioned, with tests and review |
| Module SBOM/digest/attestation (when applicable) | US-04 | Evidence of provenance and integrity |
| `NAMING.md` + pre-commit hooks | US-05 | Naming conventions |
| Git history with a commit pattern + CHANGELOG | US-05 | Change control and audit |
| Semantic git tags and releases | US-05 | E.g.: `iac-prod-v2025.07.10` |
| PR with the `terraform plan` attached | US-06 | Human review before `apply` |
| Approval trail (roles) | US-06 | DevOps + AppSec (minimum) |
| Traceability dashboard/script | US-07 | File → resource → environment maps |
| Metadata in `locals` and tags per team/application | US-07 | Support for automatic traceability |
| Versioned OPA/Rego/Sentinel rules | US-08 | Policy-as-code enforcement |
| Block logs, metrics and exceptions | US-08 | Active exceptions, % compliance |
| Signatures + `attestation.json` | US-09 | Mandatory gate at L2/L3 |
| Provenance verification logs before `prod` | US-09 | Automatic rejection when invalid |
| OIDC/workload identity configuration | US-10 | Ephemeral tokens, short TTL |
| Drift and correction reports | US-11 | Periodic audits per environment |
| Snapshots and rollback logs | US-12 | Recovery after failure |
| Change calendar/windows + approvals | US-13 | Operational change management |
| Exception register with TTL and countermeasures | US-14 | Controlled debt, reviews |

---

## ⚖️ L1–L3 proportionality matrix {#️-matriz-de-proporcionalidade-l1l3}

Not all applications require the same rigour.  
Proportionality makes it possible to balance cost, risk and control.

| Practice | L1 (low) | L2 (medium) | L3 (high/critical) |
|---|---|---|---|
| Remote backend + locking | **Mandatory** | Mandatory | Mandatory + reinforced audit |
| Automatic validations | Warning | Blocking of severe failures | Full blocking + complete coverage |
| Module governance | Simple whitelist | Whitelist + automatic validation | Whitelist + validation + SBOM + reinforced review |
| Environment segregation + tagging | **Mandatory (minimum)** | Mandatory + complete tagging | Mandatory + tags + OPA validation |
| Traceability and naming | Recommended | Mandatory + formal conventions | Mandatory + pre-commit + CHANGELOG |
| Formal plan review | Recommended | Mandatory | Mandatory + dual approval + change window |
| File→resource traceability | Recommended | Mandatory + documentation | Mandatory + automatic dashboard |
| Policy enforcement | Recommended | Mandatory OPA/Rego | OPA + formal exceptions + metrics |
| Trusted origin of modules | Recommended | Mandatory + pinning | Mandatory + formal provenance |
| IaC secrets management | Recommended | Mandatory (OIDC/short TTL) | Mandatory + JIT + audit |
| Drift detection | Recommended | Mandatory (fortnightly) | Mandatory (weekly) + alerts |
| Rollback and guardrails | Recommended | Mandatory (snapshots) | Mandatory + automated rollback |
| Signing + provenance | Recommended | Mandatory (gate for critical environments) | Mandatory + automatic rejection |

---

## 🏁 Final recommendations {#-recomendações-finais}

IaC security must be understood as a **continuous discipline**.  
Applying isolated controls is not enough: it must be ensured that they all reinforce each other, forming a network of trust.

- **Standardise backends and providers** to reduce drift.  
- **Adopt policy-as-code** as a central practice, versioned and tested.  
- **Sign artefacts** and apply provenance as mandatory gates in critical environments.  
- **Automate the plan→review→apply cycle** in pipelines with formal approval.  
- **Measure compliance** with metrics (drift, blocks, exceptions) and report by L1–L3.  
- **Review exceptions periodically**, ensuring that they do not become permanent as hidden risks.

In summary, **IaC is software** - and must be treated with the same rigour, visibility and proportionality as any other critical piece of the lifecycle.

---

## 🆕 Additional User Stories (automated and assisted process) {#-user-stories-adicionais-processo-automatizado-e-assistido}

### US-15 - Segregation of duties (SoD) and control of `apply` execution {#us-15---separação-de-funções-sod-e-controlo-de-execução-de-apply}

**Context.**  
In IaC, `apply` is the action with the greatest impact: it creates, changes or destroys real resources. To reduce operational risk and prevent abuse (including by automated mechanisms), **segregation of duties** and explicit control over who may execute must be applied.

:::userstory
**Story.**  
As **GRC / Compliance** and **DevOps / SRE**, I want **to enforce segregation of duties and control of `apply` execution**, so that no change reaches critical environments without approval and traceability.

**Acceptance criteria (BDD).**
- **Given** an `apply` to the `prod` environment  
  **When** it is requested  
  **Then** it requires **explicit approval** from at least two roles (DevOps + AppSec/GRC) and execution within a **change window**.
- **Given** an `apply` to the `staging` environment  
  **When** it is requested  
  **Then** it requires approval from at least one independent second reviewer.  
- **Given** a user without execution permission  
  **When** they attempt to trigger `apply`  
  **Then** they are blocked by the pipeline (RBAC / environment protection).

**Checklist.**
- [ ] Environment protection configured (RBAC + approvals)  
- [ ] Approval required before `apply` in critical environments  
- [ ] SoD documented (whoever proposes ≠ whoever executes, when applicable)  
- [ ] Execution evidence associated with approvals  
:::

**🧾 Artefacts & evidence.**  
Environment protection policies, approval logs, execution records, RBAC audit.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Recommended | Simple approval |
| L2 | Yes | 2nd reviewer approval + RBAC |
| L3 | Yes | SoD + dual approval + change window + reinforced audit |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Deploy / Operation | `apply` requested for the `prod` environment | GRC / Compliance + DevOps / SRE | Approval from at least two roles and execution within a change window |
| Deploy / Operation | `apply` requested for the `staging` environment | GRC / Compliance + DevOps / SRE | Approval from an independent second reviewer |
| Operations | `apply` attempt by a user without permission | GRC / Compliance + DevOps / SRE | Blocked by the pipeline (RBAC / environment protection) |

---

### US-16 - Context minimisation and protection of sensitive information in IaC {#us-16---minimização-de-contexto-e-proteção-de-informação-sensível-em-iac}

**Context.**  
Plans, pipeline logs, outputs and diffs can reveal secrets and sensitive information (IDs, naming, topologies, permissions, endpoints). This risk increases when there is assisted automation, external integrations or export of artefacts.

:::userstory
**Story.**  
As **AppSec Engineers** and **DevOps / SRE**, I want **to enforce context minimisation and automatic redaction of sensitive information** in IaC artefacts and logs, so that the risk of exfiltration and involuntary exposure is reduced.

**Acceptance criteria (BDD).**
- **Given** a `plan` and pipeline logs  
  **When** they are published in a PR, storage or observability systems  
  **Then** secrets and sensitive fields are **masked** (redaction) and never remain in clear text.  
- **Given** a PR that includes sensitive outputs (e.g. access keys, tokens, private endpoints)  
  **When** it is analysed by the pipeline  
  **Then** it is blocked by **secret scanning** and minimum-exposure policies.  
- **Given** integration with external systems (tickets, chatops, assistants, etc.)  
  **When** logs/plan are exported  
  **Then** only the **minimum necessary** is sent, with neither detailed topology nor secrets.

**Checklist.**
- [ ] Redaction configured for logs and artefacts  
- [ ] Secret scanning before publishing artefacts  
- [ ] “Minimum necessary” policy for external integrations  
- [ ] Traceable and temporary exceptions  
:::

**🧾 Artefacts & evidence.**  
Redaction config, secret scanning reports, evidence of blocks, exception register.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Yes | Secret scanning + good practices |
| L2 | Yes | Automatic redaction + publication policies |
| L3 | Yes | Redaction + classification of outputs + reinforced controls on integrations |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| CI/CD | Publication of the `plan` and logs in a PR, storage or observability | AppSec Engineers + DevOps / SRE | Redaction of secrets and sensitive fields on publication |
| PR/MR | PR with sensitive outputs analysed by the pipeline | AppSec Engineers + DevOps / SRE | Blocked by secret scanning and minimum-exposure policy |
| Operations | Export of logs or the `plan` to external systems | AppSec Engineers + DevOps / SRE | Only the minimum necessary, with neither detailed topology nor secrets |

---

### US-17 - Determinism and reproducibility of the `plan` {#us-17---determinismo-e-reprodutibilidade-do-plan}

**Context.**  
Without determinism, the `plan` may vary depending on provider versions, modules, the runner environment or transitive dependencies, making audit and change control fragile. In critical environments, the organisation must be able to reproduce the `plan` and explain differences.

:::userstory
**Story.**  
As **DevOps / SRE** and **AppSec Engineers**, I want **to ensure determinism and reproducibility of the `plan`**, so that each change can be reproduced, audited and analysed retrospectively.

**Acceptance criteria (BDD).**
- **Given** an IaC repository  
  **When** `plan` is executed in CI  
  **Then** providers and modules are **pinned** (no ranges) and the execution environment is known and versioned.  
- **Given** an approved `plan`  
  **When** it is re-executed for validation  
  **Then** the result is functionally equivalent, or the differences are justified and recorded.  
- **Given** a change of provider/module version  
  **When** it is proposed  
  **Then** it is treated as a risk change (reinforced review and additional evidence).

**Checklist.**
- [ ] Version pinning (providers and modules)  
- [ ] Versioned and traceable runner environment  
- [ ] Record of the effective versions used in the `plan`  
- [ ] Re-execution/consistency verification when applicable  
:::

**🧾 Artefacts & evidence.**  
Lockfiles, version manifests, execution logs, record of justified diffs.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Yes | Basic pinning |
| L2 | Yes | Pinning + record of effective versions |
| L3 | Yes | Pinning + re-execution/verification + reinforced review of upgrades |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| CI/CD | Execution of the `plan` in CI | DevOps / SRE + AppSec Engineers | Providers and modules pinned; execution environment known and versioned |
| Development / Review | Re-execution of an approved `plan` for validation | DevOps / SRE + AppSec Engineers | Functionally equivalent result, or differences justified and recorded |
| PR/MR | Proposed change of provider or module version | DevOps / SRE + AppSec Engineers | Treated as a risk change: reinforced review and additional evidence |

---

### US-18 - Prohibition of manual/local `apply` outside the pipeline {#us-18---proibição-de-apply-manuallocal-fora-do-pipeline}

Only the authorised pipeline may touch real infrastructure; the workstation is not an execution plane.  

**Context.** An `apply` executed locally or outside the pipeline bypasses blocking validations, policy enforcement, artefact signing and the approval trail. Even with SoD and RBAC defined (US-15), the risk remains that someone with provider credentials runs `terraform apply` from their workstation, leaving the real state divergent from the approved baseline and without auditable evidence. The prescription is explicit in addon/01 ("Prohibit manual local executions outside a validated context"; "Never execute `terraform apply` locally") and in checklist item `IAC-007` ("no manual `apply` outside the pipeline").  

:::userstory
**Story.**   
As **DevOps / SRE** and **AppSec Engineers**, I want **to ensure that every `apply` takes place exclusively in the authorised pipeline, with technical blocking of local/manual execution**, so that no change reaches real environments without going through validations, enforcement and traceable approval.  

**Acceptance criteria (BDD).**  
- **Given** the provider execution credentials/identity  
  **When** they are issued  
  **Then** they can only be obtained by the pipeline runner (OIDC/workload identity), not by users on workstations  
- **Given** an `apply` attempt outside the authorised pipeline  
  **When** it is triggered  
  **Then** it is blocked by the absence of valid credentials and/or by environment protection, and the event is recorded  
- **Given** a legitimate `apply`  
  **When** it is executed  
  **Then** it runs in the pipeline on an approved `plan`, leaving an execution log associated with the PR/approval  

**Checklist.**  
- [ ] Provider credentials for `apply` unavailable to users outside the runner (OIDC/JIT)  
- [ ] Environment protection / branch protection prevents `apply` outside the pipeline  
- [ ] Organisational policy that explicitly prohibits manual/local `apply` in real environments  
- [ ] `apply` execution logs always traceable to the pipeline and the approval  

:::

**Artefacts & evidence.** OIDC/environment protection configuration, controlled execution policy, `apply` logs with origin (pipeline run ID), evidence of blocking of attempts outside the pipeline.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Documented policy + `apply` via pipeline in prod | Technical blocking (no local credentials) in staging/prod | Technical blocking in all environments + audit of attempts and recorded break-glass |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Deploy / Operation | `apply` request | DevOps / SRE | Execution only in the pipeline; immediate blocking outside it |
| Governance | Periodic audit | GRC / Compliance | Quarterly review of attempts and exceptions |

**Useful links.** [Planning and Control of the Application of IaC](/sbd-toe/sbd-manual/iac-infraestrutura/addon/planeamento-e-controle) · [Catalogue IAC-007](/sbd-toe/sbd-manual/iac-infraestrutura/addon/catalogo-requisitos-iac)

---

### US-19 - Reopening of the hardening review for baseline integrity {#us-19---reabertura-da-revisão-de-hardening-por-integridade-do-baseline}

Touching what defines the baseline reopens the review of the security posture before the next `apply`.  

**Context.** In IaC the object to protect is not only the final resource, but the **versioned baseline** that defines how that resource is born and may change. When a module, provider, blocking policy or template is changed — or when *drift detection* reveals divergence — the approved hardening posture may have been silently eroded without any per-resource validation detecting it. The prescription lives in the "Baseline integrity" principle (addon/04), in the Operational Note and in the lifecycle's own "Baseline integrity rule", and in the intro ("any material deviation must be blocked, reviewed or explicitly accepted"). What is missing is a US that makes reopening this review an operational event with a gate, an owner and a record.  

:::userstory
**Story.**   
As **AppSec Engineers** and **DevOps / SRE**, I want **to treat changes to modules, providers, policies or templates (and confirmed drift) as an event that mandatorily reopens the hardening review before the next `apply`**, so that silent erosion of the approved baseline is prevented.  

**Acceptance criteria (BDD).**  
- **Given** a PR that changes a module, provider, blocking policy or base template  
  **When** it is submitted  
  **Then** the pipeline flags it as a **baseline review event** and requires recorded confirmation that the hardening posture remains secure before allowing `apply`  
- **Given** a *drift detection* result that reveals divergence from the baseline  
  **When** it is confirmed  
  **Then** a review is opened with an assigned *owner*, and the reconciliation `apply` only proceeds after a recorded decision  
- **Given** a completed baseline review  
  **When** it is approved  
  **Then** traceability is maintained between the changed module/template, `plan`, validation evidence and applicable exceptions  

**Checklist.**  
- [ ] Pipeline detects changes to modules/providers/policies/templates and flags them as baseline events  
- [ ] Gate that requires a recorded hardening review before the `apply` in these events  
- [ ] *Owner* assigned and review decision recorded (incl. confirmed drift)  
- [ ] Module/template → `plan` → validation evidence → exceptions traceability  

:::

**Artefacts & evidence.** Baseline review record (date, *owner*, findings), associated `plan` output, post-change validation/policy reports, drift reports and the respective decisions, register of applicable exceptions.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Manual review recorded when a module/policy/template changes | Pipeline gate flags baseline events + mandatory review before `apply` | Formal review with an owner + periodic review of templates/modules + confirmed drift as a blocking security failure |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Development / Review | PR changes a module/provider/policy/template | AppSec Engineers | Review before the merge/`apply` |
| Operations | Confirmed drift | DevOps / SRE | Opening of a review and correction via PR |
| Governance | Periodic baseline review | GRC / Compliance | L3 cadence (weekly/quarterly according to criticality) |

**Useful links.** [SbD principles for IaC — Baseline integrity](/sbd-toe/sbd-manual/iac-infraestrutura/addon/principios-sbd-iac) · [Catalogue IAC-013](/sbd-toe/sbd-manual/iac-infraestrutura/addon/catalogo-requisitos-iac)
