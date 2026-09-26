---
id: intro
title: Infrastructure as Code (IaC)
description: Security practices for the definition, validation and management of infrastructure as code
tags: [infraestrutura, iac, terraform, segurança, automatização, DSOMM, SAMM, SLSA, SSDF]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/intro.md
  source_sha256: 8e2f2fa272af07c71d47879564c9a9ca61eb6e034bf04cc200fbc15cc1d0024e
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: ef3555a141406373fbf2cb3f1a1b41e10d244038e89440547f1d392930c6bf32
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, basilar, chapter_role, cycle_iteration, deterministic, discipline, layer, lifecycle_phase, mapping, papel_suporte, practitioner_manual, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: 39d2f41d098338673dd2c40e7be50d64df5b385edbe22b9984220f7145f6dfcd
  translated_at: 2026-09-26T09:25:43Z
  stamped_at: 2026-09-26T18:37:51Z
  reviewed_by: null
---

import ChapterTypeCallout from '@site/src/components/ChapterTypeCallout';

<ChapterTypeCallout kind="operacional" title="Capítulo Operacional">

This chapter is considered **operational** in the *Security by Design – Theory of Everything (SbD-ToE)* model.
Its function is to **apply, automate and validate** the practices defined in the foundational chapters, guaranteeing their continuous and measurable execution.

The operational chapters implement SbD-ToE in specific technical contexts, translating foundational prescriptions into practices of **verifiable execution**, with technical evidence, traceability and governance.

</ChapterTypeCallout>

---

## ⚠️ Canonical Note - Infrastructure as an Automated Process {#️-nota-canónica---infraestrutura-como-processo-automatizado}

Modern infrastructure is defined, validated and applied through **highly automated processes**, frequently supported by mechanisms for the **automatic generation, suggestion or normalisation of code and configuration**.

In the context of IaC, this reality introduces specific risks that must be explicitly controlled:

- **Suggestion does not equal decision**: automatic mechanisms may propose changes, but the impact decision (`plan` and above all `apply`) is always **human, traceable and formally approved**.
- **Plausibility does not equal evidence**: code that appears correct or is “well explained” does not replace **evidence of real execution**, namely the effective `plan`, auditable diffs and versioned artefacts.
- **Reproducibility is mandatory**: the security of IaC requires determinism - versions of providers, modules, policies and execution environments must allow faithful reconstruction and retrospective analysis.
- **The infrastructure context is a critical asset**: templates, topologies, permissions, naming and operational parameters constitute sensitive information; any dependency outside the organisation's direct control must be treated as a **supply chain dependency**, with a potential risk of exfiltration.

These premises are structural and apply **regardless of the tools used**.

---

# Security in Infrastructure as Code (IaC)

The definition of infrastructure through code (Terraform, Pulumi, CloudFormation, etc.) has become common practice.  
This approach has brought clear gains in speed, consistency and scalability. But, like any transformative technology, it has also brought **new risks**: configuration errors, excessive permissions, use of malicious modules or poorly segregated environments.

This chapter prescribes how to **treat IaC as critical software** - with requirements, tests, lifecycle and audit.  
The central idea is simple: if IaC defines the foundation on which software runs, then **its security determines the security of everything else**.

In this context, the chapter also works as the **operational centre for the secure configuration baseline and hardening**: infrastructure must start from an approved, versioned and validated posture, and any material deviation must be blocked, reviewed or explicitly accepted before it reaches real environments.

---

## 🧭 What it covers technically {#-o-que-cobre-tecnicamente}

In practice, speaking of IaC security means protecting every layer, from the first file to the last resource applied in production.  
The areas covered include:

- Provisioning templates and scripts (Terraform, Pulumi, CloudFormation, etc.)  
- Automation of environments via CI/CD pipelines  
- Validation and control of the configuration of cloud and on-prem resources  
- Detection of bad practices, excessive permissions or undue exposure  
- Trusted origin, integrity and versioning of modules and dependencies  
- Complete traceability of changes (file → resource → environment)  
- Automatic and blocking enforcement of security policies  
- Preservation of the integrity of the approved baseline over time, including review of templates, modules and exceptions  
- Context protection and minimisation of sensitive information in automated processes  

---

## 📌 What must be done {#-o-que-deve-ser-feito}

To turn recommendations into applicable engineering practices, the organisation must guarantee, at a minimum:

1. Use of declarative, deterministic and reproducible tools  
2. **Rigorous segregation and versioning** of environments  
3. **Automatic and blocking validations** (lint, security, policies) before any `apply`  
4. Strict control of the origin, integrity and version of the modules used  
5. **Formal, human review of the `plan`**, with clearly defined impact criteria  
6. Guarantee of **complete traceability** between code, resources and environments  
7. **Automatic enforcement** of security policies in the pipeline  
8. Versioning, retention and, where applicable, signing of all relevant artefacts (`plan`, reports, manifests)  
9. Periodic review of templates, modules, policies and exceptions to detect baseline erosion, *drift* or silent deviation from the intended hardening posture

---

## ⚙️ How it must be done {#️-como-deve-ser-feito}

Execution depends on practical tools and their disciplined integration into controlled pipelines.  
Relying on individual experience is not enough - it is necessary to **automate, restrict and audit**:

- Scanning tools: `tfsec`, `checkov`, `kics`, `terrascan`  
- Policy enforcement: `OPA`, `Sentinel`, `Conftest`  
- Mandatory CI/CD pipelines for validation before any effective change  
- Catalogue of certified internal modules, pinned by version and with auditable origin  
- Automated validation dashboards per environment  
- Centralised and traceable management of exceptions, with formal approval and time-bound validity  

---

## 📆 When to apply {#-quando-aplicar}

Controls must be applied throughout the entire IaC lifecycle.  
Ignoring a critical moment means allowing the silent accumulation of risk:

- Whenever there are changes to IaC templates or scripts  
- During code review and infrastructure pull/merge requests  
- Before the execution of pipelines that affect real environments  
- When integrating or updating external modules  
- In periodic compliance audits and *drift detection*  

---

## 👥 Who is involved {#-quem-está-envolvido}

The protection of IaC is a shared responsibility, requiring coordination between technical and governance functions:

| Role/Function      | Main contribution |
|-------------------|----------------------|
| **DevOps / SRE**  | Writing, review and maintenance of IaC templates; pipeline management |
| **AppSec Engineer** | Definition of policies, mandatory scanners and blocking criteria |
| **Software Architects** | Validation of technical standards and secure design of environments |
| **Product Owner** + **GRC / Compliance** | Approval of risks and exceptions, and validation of traceability |

---

## 🎯 What for {#-para-quê}

Investing in IaC security is investing in the **reliability of the foundation on which all applications rest**.  
The objectives are clear:

- Prevent insecure configurations or excessive permissions  
- Ensure consistency, reproducibility and traceability of infrastructure  
- Demonstrate technical compliance in audits  
- Reduce the risk of *drift*, human error and supply chain attacks  

---

## 📜 Relevant Organisational Policies {#-políticas-organizacionais-relevantes}

Formal policies ensure that practices do not depend solely on individual discipline, but on collective, clear and auditable rules.

| Organisational policy           | Mandatory | Application                     | Minimum content |
|----------------------------------|-------------|-------------------------------|-----------------|
| [Secure IaC Policy](/sbd-toe/assets/policies/policy-iac-seguro)            | Yes         | All IaC projects         | Technical standards, segregation of environments, mandatory pipelines, policy enforcement |
| [IaC Module Management Policy](/sbd-toe/assets/policies/policy-iac-seguro) | Recommended | DevOps / SRE, Software Architects     | Use of verified modules, version pinning, origin audit |
| [IaC Traceability Policy](/sbd-toe/assets/policies/policy-rastreabilidade)   | Yes         | DevOps / SRE, GRC / Compliance                   | File → resource → environment mapping, auditable history |
| [IaC `plan` Approval Policy](/sbd-toe/assets/policies/policy-aprovacao-plan-iac)   | Yes         | DevOps / SRE, AppSec Engineer                | Mandatory human review, impact criteria, rollback and SoD |
| [Secrets Management Policy](/sbd-toe/assets/policies/policy-gestao-segredos) | Yes | DevOps / SRE, AppSec Engineer | OIDC/short TTL, prohibition of secrets in IaC code, periodic rotation |
| [Rollback and Recovery Policy](/sbd-toe/assets/policies/policy-rollback) | ⚠️ Reinforced | Critical environments | Automated reversal, periodic tests of state restoration |

In the printed version, consult the **Manual's Organisational Policies Annex**, where these policies are consolidated across the board.
