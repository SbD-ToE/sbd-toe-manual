---
id: catalogo-requisitos-cicd
title: Secure CI/CD Requirements Catalogue
description: Canonical catalogue of security requirements for continuous integration and delivery pipelines (CIC-001 to CIC-010), with applicability by risk level and acceptance criteria for pipeline design, secrets management, runner isolation, artefact integrity and security gates.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:cicd, CIC, pipeline, rastreabilidade, L1, L2, L3, runners, segredos, proveniencia, gates, auditoria]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/addon/00-catalogo-requisitos.md
  source_sha256: 369d59cd0d332422e724191068132fe048a08380e332982de1e0303b46c2fd6d
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 0b597e9f14276f94a934cefe94691363a9da367518254d65e2bad86066b66dd2
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, framework_source_corpus, mapping, papel_suporte, practitioner_manual, provenance, requirement_runtime, risk_level, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: c4d217b90b5dd9c05539bbf81517a6d6632ba8595dc4e5f1b3e090488d282f67
  translated_at: 2026-09-26T09:09:11Z
  stamped_at: 2026-09-26T18:34:14Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Secure CI/CD Requirements Catalogue

## Scope: the pipeline as an engineering product with its own risk {#âmbito-o-pipeline-como-produto-de-engenharia-com-risco-próprio}

This catalogue covers **security requirements that apply to the design, operation and audit of CI/CD pipelines** - treating the pipeline as a critical engineering product that, if compromised, compromises all the software that passes through it.

Pipelines are today the frontier where code, credentials, artefacts and promotion decisions converge. An insecure pipeline is not merely a process risk: it is an attack vector against the whole delivery chain. These requirements establish the minimum controls for the pipeline to be **sound, traceable, auditable and resistant to tampering**.

For the complete mapping of all SbD-ToE requirements catalogues by technical domain, canonical prefix and owner, see [Ch. 02 - Catalogue Mapping](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **On curation:** Consolidated from OSC&R (CI/CD Attack Framework), the CISA Top 10 CI/CD Security Risks, SLSA (Supply Chain Levels for Software Artefacts), NIST SSDF (PW.5, PW.6), the OWASP Top 10 CI/CD Security Risks and established practices for GitHub Actions, GitLab CI, Azure DevOps and Jenkins. It must be adapted to the CI/CD platform in use and reviewed with each pipeline architecture cycle.

For project instantiation and the operational nomenclature (`SEC-Lx-CIC-CODIGO`), see [Taxonomy and Traceability](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Conventions {#convenções}

| Symbol | Meaning |
|---------|-------------|
| ✔ | Mandatory requirement at this level |
| - | Not applicable or not mandatory at this level |

The levels are cumulative: L3 includes all L1 and L2 requirements; L2 includes all L1 requirements.

---

## CIC Catalogue - Secure CI/CD {#catálogo-cic---cicd-seguro}

Requirements that guarantee that the integration and delivery pipeline is designed, operated and audited with controls proportional to the risk of the software it processes.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| CIC-001 | Pipelines as code, versioned and subject to review | ✔ | ✔ | ✔ | Pipeline definition in versioned files in the repository (YAML, HCL, etc.); changes subject to a pull request with review; no pipelines managed manually outside version control. |
| CIC-002 | Triggers controlled and restricted to authorised sources | ✔ | ✔ | ✔ | Runs triggered only by events from authorised sources (protected branches, signed tags, approved merges); runs originating in external forks disabled or mediated by manual approval. |
| CIC-003 | Secure management of secrets in the pipeline | ✔ | ✔ | ✔ | Secrets injected via a vault or environment variables protected by the platform; no secrets in pipeline YAML, logs or versioned files; masking of sensitive values active in logs. |
| CIC-004 | Mandatory security gates before promotion between environments | ✔ | ✔ | ✔ | Security validation stages (SAST, SCA, lint, secrets scan) configured as blocking; promotion of artefacts between environments requires explicit human approval for irreversible actions; no automated bypass. |
| CIC-005 | Complete traceability of each pipeline run | ✔ | ✔ | ✔ | Each run identifiable by a unique ID; logs retained for the period defined in policy; possible to reconstruct what ran, when, with which inputs, with which result and who approved. |
| CIC-006 | Isolation of runners and execution environments | - | ✔ | ✔ | Runners without direct access to production data or credentials; execution in ephemeral or isolated environments; no sharing of persistent state between jobs from different repositories. |
| CIC-007 | Verifiable integrity and provenance of the artefacts produced | - | ✔ | ✔ | Artefacts digitally signed or with a verifiable hash generated at build time; provenance (commit SHA, pipeline run ID, build environment) associated with the artefact and verifiable before promotion. |
| CIC-008 | Separation of responsibilities between build, test and deploy | - | ✔ | ✔ | Distinct jobs for the build, test and deploy phases; no unnecessary cross-permissions between stages; identity and scope of credentials per stage documented and enforced. |
| CIC-009 | Pipeline credentials with minimum scope and defined rotation | - | ✔ | ✔ | Tokens and credentials used by the pipeline with the minimum necessary scope; periodic rotation defined and evidenced; no credentials shared between pipelines of different applications. |
| CIC-010 | Protection against execution of unauthorised code on runners | - | - | ✔ | Runners with strong isolation (ephemeral containers, disposable VMs); no access to the Docker socket by non-privileged jobs; no privilege escalation capabilities; logs of blocked attempts available. |
| CIC-011 | Promotion between environments attributable to an identified owner | - | ✔ | ✔ | Each promotion between environments is attributable to an identified person: whoever decided it or, when it promotes automatically, whoever approved the criteria under which it promotes. The record identifies the person (not merely a role or service account), the criterion applied and the evidence assessed. Automatic promotion requires **deterministic, versioned and pre-approved** criteria, and the level of autonomy declared when the promotion is executed by an agent; the output of a probabilistic model does not constitute a promotion criterion. |

---

## Explanatory notes {#notas-explicativas}

- **CIC-001**: Pipeline as code is a necessary condition for traceability and review - a pipeline that can only be edited in the platform UI is unauditable by definition.
- **CIC-002**: The risk of pipeline poisoning via forks (e.g. GitHub Actions pull_request_target) is an established vector; triggers from pull requests of external forks must be treated as untrusted by default.
- **CIC-003**: The confidentiality of secrets must be preserved even when the pipeline fails or aborts; secrets must never appear in debug outputs or in generated artefacts.
- **CIC-004**: "Human approval for irreversible actions" includes: promotion to production, deploy, publication to a public registry, and any operations that modify external state and cannot be reverted automatically.
- **CIC-007**: Reference tools: Sigstore/Cosign for signing, the SLSA Provenance Generator, GitHub Artifact Attestations, the in-toto framework. Provenance must be verified downstream, not merely generated.
- **CIC-010**: Access to the Docker socket by pipeline jobs is a frequently underestimated privilege escalation vector - a job with access to the socket has effective control of the host.
- **CIC-011**: does not require human presence at each promotion — it requires the promotion to be **attributable**. A pipeline that promotes on its own under deterministic, versioned and pre-approved criteria meets the requirement: it answers who approved the criteria, and the level of autonomy (A0–A4) declares the risk appetite. What the requirement excludes is promotion **with no one to whom it can be imputed** — and decision by probabilistic output, which is not a criterion. It complements `CIC-004`: `004` requires the gate and human approval for irreversible actions, `011` requires that it be recorded **to whom it is imputable**, and extends this to reversible promotions. This is what `DPL-001` already does for production. At L1, the run traceability of `CIC-005` is considered sufficient. When the promotion is executed by an agent, the A0–A4 scale and `REQ-AGN-002` additionally apply to it; a deterministic pipeline without an agent has no level of autonomy to declare and complies by way of the criteria.

---

> For secure pipeline design and trigger control, see [Secure Pipeline Design](./design-seguro-pipelines).
> For secure management and injection of secrets, see [Secrets Management in the Pipeline](./gestao-segredos-pipeline).
> For runner isolation, see [Runner Isolation](./isolamento-runners).
> For artefact integrity and provenance, see [Integrity and Provenance](./integridade-proveniencia).
> For pipeline policies and gates, see [Policies and Gates](./politicas-gates-pipeline).
