---
id: policy-iac-seguro
title: Secure IaC Policy
description: Organisational policy that defines the security requirements for the definition, validation, execution and maintenance of Infrastructure as Code (IaC), including configuration scanning, policy-as-code, environment separation, drift control, approved modules and plan signing, proportional to the criticality level (L1, L2, L3).
tags: [policy, IaC, Terraform, Pulumi, tfsec, checkov, OPA, policy-as-code, drift, módulos, assinatura, cap08, L1, L2, L3, governance, infraestrutura]
grupo: infraestrutura
sidebar_position: 21
translation:
  source_locale: pt
  source_path: 020-assets/policies/21_policy-iac-seguro.md
  source_sha256: 08af210a8367bd5a9a9293d0fcfcebb3fa7afd699b2320c07ccb1e231d16ddfc
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 7e0901ef7ef47d548fa366fee6b95a4f46dd538c8a064341be7bebf7fe7ee367
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [avaliacao, cycle_iteration, framework_source_corpus, lifecycle_phase, practitioner_manual, requirement_runtime, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: ecd53498f823c203ba2d1f1bbc6d567b9d66ef95eca0b82734cae6f66172431d
  translated_at: 2026-09-26T14:10:55Z
  stamped_at: 2026-09-26T18:36:56Z
  reviewed_by: null
---

# Secure IaC Policy

## 1. Objective {#1-objetivo}

This policy defines the security requirements applicable to the **design, validation, execution and maintenance of Infrastructure as Code (IaC)** in all environments managed by the organisation.

IaC defines the foundation on which software runs - a configuration error in IaC is not an application bug: it is an infrastructure vulnerability with potential impact on every system that shares it. Permissive security groups, IAM roles with excessive access, public buckets, disabled encryption - all of these errors recur in unreviewed IaC and have proportionally more serious consequences than most code vulnerabilities.

The objective of this policy is to ensure that:

- IaC is treated as critical software: reviewed, tested, signed and audited
- Insecure configurations are detected automatically before any apply
- Policy-as-code enforces guardrails that do not depend on individual human review
- Manual changes to the real state of the infrastructure (drift) are detected and corrected
- External IaC modules are assessed, versioned and approved before adoption

---

## 2. Scope {#2-âmbito}

This policy applies to all infrastructure defined as code, regardless of the tool used (Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, Ansible, etc.) and of the environment (public, private or hybrid cloud, Kubernetes, etc.).

---

## 3. Principles of secure IaC {#3-princípios-de-iac-seguro}

| Principle | Practical application |
|---|---|
| **IaC as code** | Versioned, reviewed, tested and audited with the same rigour as application code |
| **Principle of least privilege** | IAM roles and policies with the minimum permissions for the function; no wildcards in prod |
| **Environment separation** | Segregated environments with separate state and distinct credentials; no cross-references between backends |
| **Infrastructure immutability** | Changes via pipeline - not manual; manual changes are drift and must be reverted |
| **Fail secure** | Default configurations are the most restrictive; explicit permissions for what is needed |
| **No hardcodes** | Secrets, IPs and sensitive references never hardcoded; passed as variables or via a vault |

---

## 4. Mandatory automated validation {#4-validação-automática-obrigatória}

### 4.1 Linting and syntax validation {#41-linting-e-validação-de-sintaxe}

Run on every PR with IaC changes, before any plan or apply:

- [ ] Formatting checked (`terraform fmt`, or the equivalent for each tool)
- [ ] Syntax validated (`terraform validate`, or equivalent)
- [ ] Best-practice linter (`tflint`, or equivalent)

### 4.2 Security scanning {#42-scanning-de-segurança}

| Gate | L1 | L2 | L3 |
|---|---|---|---|
| IaC configuration scanner (tfsec, checkov, kics, terrascan) | Alert | Blocks High/Critical | Blocks Medium+ |
| Policy-as-code (OPA/Rego, Sentinel, Conftest) | Recommended | Mandatory | Mandatory |
| Validation of minimum IAM permissions | Recommended | Mandatory | Mandatory |
| Detection of hardcoded secrets | Mandatory | Mandatory | Mandatory |

### 4.3 Policy-as-code {#43-policy-as-code}

At L2/L3, infrastructure security policies must be codified as automatically verifiable rules:

- [ ] Policies covered include (examples): no public buckets, mandatory encryption at rest, security groups without unrestricted 0.0.0.0/0 access, mandatory tags on all resources
- [ ] Policies versioned and approved by an AppSec Engineer
- [ ] A policy failure blocks the apply regardless of human review
- [ ] Compliance reports exported per environment

---

## 5. Environment separation {#5-separação-de-ambientes}

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Environments in separate directories/workspaces | Recommended | Mandatory | Mandatory |
| Separate remote state per environment (no state shared between dev/prod) | Recommended | Mandatory | Mandatory |
| Distinct credentials per environment | Recommended | Mandatory | Mandatory |
| No cross-references between backends of different environments | Recommended | Mandatory | Mandatory |
| State encrypted at rest | Recommended | Mandatory | Mandatory |
| State locking for concurrent operations | Recommended | Mandatory | Mandatory |

---

## 6. External modules and internal catalogue {#6-módulos-externos-e-catálogo-interno}

### 6.1 Assessment of external modules {#61-avaliação-de-módulos-externos}

IaC modules from external sources (e.g. Terraform Registry, public GitHub) must be assessed before adoption:

- [ ] Origin verified (recognised maintainer, active repository)
- [ ] No known vulnerabilities in the version to be adopted
- [ ] Compatible licence
- [ ] Version fixed (pinning) - no use of `latest` or ranges in prod

### 6.2 Internal catalogue of approved modules {#62-catálogo-interno-de-módulos-aprovados}

At L2/L3, the organisation must maintain a catalogue of approved internal IaC modules:

- [ ] Modules versioned with a changelog
- [ ] Modules with documented and typed outputs
- [ ] Formal approval before publication (AppSec Engineer + DevOps/SRE)
- [ ] New or changed modules subject to review and scanning before publication
- [ ] Projects reference modules from the internal catalogue - not local copies

---

## 7. Plan review and approval {#7-revisão-e-aprovação-de-plan}

Before any apply in staging or production environments:

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Plan generated in the pipeline (not locally) | Recommended | Mandatory | Mandatory |
| Readable plan output attached to the PR | Recommended | Mandatory | Mandatory |
| Plan reviewed by DevOps/SRE before apply | Recommended | Mandatory | Mandatory |
| Plan reviewed by an AppSec Engineer (security impact) | Not applicable | Recommended | Mandatory |
| Plan signed before apply (L3) | Not applicable | Not applicable | Mandatory |
| Apply blocked without explicit approval in staging/prod | Recommended | Mandatory | Mandatory (dual approval) |

The plan review must validate:
- [ ] No resources being unexpectedly destroyed
- [ ] No unplanned changes to security groups, IAM roles or policies
- [ ] Changes confined to the scope of the PR

---

## 8. Drift detection and correction {#8-deteção-e-correção-de-drift}

Manual changes to the real infrastructure create a divergence (drift) from the state defined in IaC. This state is unacceptable at L2/L3:

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Scheduled drift detection job | Recommended | Mandatory (monthly) | Mandatory (fortnightly) |
| Drift report per environment generated and archived | Recommended | Mandatory | Mandatory |
| Critical drift in production triggers an immediate alert | Recommended | Mandatory | Mandatory |
| Drift correction via PR with approval (never manual) | Recommended | Mandatory | Mandatory |

:::warning
Direct manual changes to production infrastructure, outside the IaC pipeline, are treated as non-compliance at L2/L3 and must be recorded as an incident. The resulting drift must be corrected by the pipeline, not legitimised retroactively.
:::

---

## 9. Mandatory resource tagging {#9-tagging-obrigatório-de-recursos}

All resources created by IaC must carry mandatory tags that enable traceability:

| Tag | Description |
|---|---|
| `Environment` | dev / staging / prod |
| `Owner` | Responsible team or product |
| `Application` | Application identifier |
| `Criticality` | L1 / L2 / L3 |
| `ManagedBy` | terraform / pulumi / etc. |

Tagging compliance must be verified automatically by policy-as-code at L2/L3.

---

## 10. Expected artefacts {#10-artefactos-esperados}

| Artefact | Description | Retention |
|---|---|---|
| `backend.tf` + locking logs | Remote state configuration and locking evidence | While active |
| Lint and scanning reports | Output of tfsec, checkov, etc., per PR | 90 days (L2), 1 year (L3) |
| Policy-as-code reports | Policy compliance per environment | 90 days (L2), 1 year (L3) |
| Plan history with metadata | Timestamp, author, PR/MR ID | 1 year (L2/L3) |
| Drift reports | Per environment, per audit cycle | 1 year (L2/L3) |
| Catalogue of approved modules | Active version + changelog | History |

---

## 11. Responsibilities {#11-responsabilidades}

| Role | Responsibility |
|---|---|
| Developer / DevOps | Write IaC and submit it for review; fix scanning findings; reference modules from the catalogue |
| DevOps / SRE | Manage state backends; configure the IaC pipeline; run drift detection; manage the module catalogue |
| AppSec Engineer | Define policy-as-code policies; approve modules; review plans with security impact; manage exceptions |
| GRC / Compliance | Audit compliance reports; verify drift; validate artefact retention |

---

## 12. Review and audit of this policy {#12-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- An incident originating from an insecure IaC configuration or undetected drift
- Adoption of a new IaC tool or a new cloud provider
- A change to the scanning or policy-as-code tools

---

## 13. Normative and technical references {#13-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 08 - IaC and Infrastructure | Principles, user stories, artefacts, lifecycle |
| IaC Plan Approval Policy (`22_policy-aprovacao-plan-iac.md`) | Detailed plan review and approval process |
| Secure CI/CD Policy (`17_policy-cicd-seguro.md`) | IaC validation pipeline |
| Secrets Management Policy (`18_policy-gestao-segredos.md`) | Secrets in IaC and providers |
| tfsec / checkov / kics | IaC scanning tools |
| OPA / Rego / Sentinel / Conftest | Policy-as-code tools |
| CIS Benchmarks (AWS, Azure, GCP) | Reference controls for cloud infrastructure |
| NIST SP 800-190 | Application Container Security Guide (applicable to container IaC) |
| SLSA Framework | Build integrity - applicable to IaC artefacts |
