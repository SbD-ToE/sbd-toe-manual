---
id: catalogo-requisitos-iac
title: Infrastructure as Code Requirements Catalogue
description: Canonical catalogue of security requirements for IaC projects (IAC-001 to IAC-013), organised by risk level, with acceptance criteria for the governance of repositories, pipelines, state, modules and configuration drift.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:iac, IAC, rastreabilidade, L1, L2, L3, terraform, state-management, drift, supply-chain, auditoria]
sidebar_position: 8
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/addon/08-matriz-requisitos-iac.md
  source_sha256: 529eb896daf93e5f9079e46d65a6d7d162594b15db76374111c9897d635a824e
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 34262990197d76aa79d6a90d3f43effa2da5c40c481d1005c906748da34bf801
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [audit_trail, cycle_iteration, mapping, practitioner_manual, provenance, requirement_runtime, risk_level, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: 7323d93645f9374ac6819d9058a14cd18282054a1f3f5677750113f95ef70f7a
  translated_at: 2026-09-26T09:25:38Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Infrastructure as Code Requirements Catalogue

## Scope: the IaC project as a software product {#âmbito-o-projecto-iac-como-produto-de-software}

This catalogue defines **security requirements that apply to the IaC project itself** - treating infrastructure code as a software product with its own risks, which must be governed, validated and audited with the same rigour as any application.

The requirements cover: remote state management, segregation of environments, automated validations in the pipeline, traceability of modules and their provenance, versioning of artefacts, secure management of secrets, drift detection and periodic review of templates.

For the complete mapping of all SbD-ToE requirements catalogues by technical domain, canonical prefix and owner, see [Ch. 02 - Catalogue Mapping](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **Note:** These requirements govern **how infrastructure is defined and managed as code** - not the security properties of the provisioned infrastructure itself (network configurations, IAM permissions, bucket encryption, etc.), which result from what the IaC code defines and are subject to each organisation's policies.

> **On curation:** Consolidated from NIST SSDF, SLSA (Supply Chain Levels for Software Artefacts), the CIS Benchmarks for IaC, OWASP SAMM and established practices for Terraform, Pulumi and cloud platforms. It must be adapted to the context and to the IaC tools used by the organisation.

For project instantiation and the operational nomenclature (`SEC-Lx-IAC-CODIGO`), see [Taxonomy and Traceability](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Conventions {#convenções}

| Symbol | Meaning |
|---------|-------------|
| ✔ | Mandatory requirement at this level |
| - | Not applicable or not mandatory at this level |

The levels are cumulative: L3 includes all L1 and L2 requirements; L2 includes all L1 requirements.

---

## IAC Catalogue - Infrastructure as Code {#catálogo-iac---infraestrutura-como-código}

Requirements that guarantee that the IaC project is developed, versioned, validated and operated with security controls proportional to the risk of the infrastructure it manages.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| IAC-001 | Authenticated remote backend with active locking | - | ✔ | ✔ | `backend` configured with authentication and locking; an attempted concurrent `apply` results in blocking; lock logs available. |
| IAC-002 | Segregated and versioned environments | ✔ | ✔ | ✔ | Distinct `dev`, `staging` and `prod` configurations, versioned in separate directories or workspaces; a deploy cannot cross environments without explicit approval. |
| IAC-003 | Mandatory automated validations in the pipeline | ✔ | ✔ | ✔ | Pipeline with lint, security analysis (e.g. tfsec, checkov) and policy validation stages; failure at any stage blocks the `apply`. |
| IAC-004 | Reused modules with a trusted origin and an immutable version | - | ✔ | ✔ | Module references with a pinned semantic version or hash; no unversioned references (`latest`, `master`, `HEAD`); origin documented. |
| IAC-005 | Complete history with versioning, tags and releases | ✔ | ✔ | ✔ | Git repository with intact history, semantic tags per release and release notes; no mandatory squash on main branches. |
| IAC-006 | Formal naming, tagging and layout conventions | - | ✔ | ✔ | Linter or automated policy that validates naming conventions and mandatory tags; resources without mandatory identification tags are rejected. |
| IAC-007 | Traceable and approved plan before any apply | - | ✔ | ✔ | PR with the `plan` output attached and reviewable; approval recorded before `apply`; evidence that the `apply` took place after approval and on the same `plan`. |
| IAC-008 | Traceability file → resource → environment | - | ✔ | ✔ | Possible to identify, for any provisioned resource, the source IaC file, the environment and the pipeline that created it; evidence available at audit. |
| IAC-009 | Automated enforcement of policies in the pipeline | - | - | ✔ | Policy rules (e.g. OPA/Rego, Sentinel) active in the pipeline; logs of blocking due to policy violations available; policy versioned with the code. |
| IAC-010 | Plan artefacts and manifests versioned and hashed | - | ✔ | ✔ | Plans and manifests stored with a verifiable hash; integrity confirmed before the `apply`; artefacts not reusable across distinct environments. |
| IAC-011 | Secure management of secrets - prohibition of hardcoding | ✔ | ✔ | ✔ | No secrets in code, unprotected environment variables or versioned files; integration with a secrets vault (Vault, KMS, OIDC) verifiable; automated secrets scan in the pipeline. |
| IAC-012 | Automated detection of drift between IaC and actual state | - | ✔ | ✔ | Periodic drift reports available; active alerts for divergence between the state defined in IaC and the actual state of the infrastructure. |
| IAC-013 | Formal periodic review of modules and templates | - | - | ✔ | Review records with date, owner and findings; review cycle defined and evidence of compliance; obsolete modules or modules with known vulnerabilities withdrawn from service. |

---

## Explanatory notes {#notas-explicativas}

- **IAC-001**: Applies whenever there is collaboration between multiple engineers, shared pipelines or more than one environment managed by the same state. In single-operator contexts with an isolated pipeline, locking may be waived with a documented justification.
- **IAC-004**: Any dependency on an external module must be treated as code untrusted by origin until explicitly validated. Shared internal modules are also subject to this requirement.
- **IAC-007**: Embodies the principle of technical *change control* in IaC: no `apply` should take place without direct traceability to a human approval of a verifiable `plan`.
- **IAC-009**: A structural requirement for high-risk environments (L3), where reliance on manual review is insufficient to guarantee continuous policy coverage.
- **IAC-011**: The secrets scan must cover code, Git history and pipeline variables; reference tools: TruffleHog, GitLeaks, detect-secrets.
- **IAC-012**: Drift is treated as a security failure, not as an operational exception - infrastructure that diverges from the state defined in IaC represents unauditable risk.

---

> For Security by Design principles applied specifically to IaC projects, see [SbD Principles for IaC](./principios-sbd-iac).
> For recommended automated validations and checks, see [Validations and Checks](./validacoes-e-checks).
> For management of exceptions to these requirements, see [Exception Management](./gestao-excecoes).
> For traceability and tagging of resources, see [Traceability and Tags](./rastreabilidade-e-tags).
