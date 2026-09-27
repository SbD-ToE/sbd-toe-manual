---
id: policies-relevantes
title: Policies
description: Organisational policies needed to frame and reinforce governance and security in the use of Infrastructure as Code (IaC)
tags: [políticas, infraestrutura como código, cloud, devsecops, pipelines, configuração segura]
sidebar_position: 60
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/policies-relevantes.md
  source_sha256: 322a40e34d7b24637abd458364e668869f10b3f9ac4df2d67f1a368c194afefb
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 3a8341f7d49fc4e3e6f4e790919bebfc3a16f0e0046ab31d1c1b2dd3e9a2d5c7
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, framework_source_corpus, lifecycle_phase, maturity, practitioner_manual, segregacao_de_funcoes, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 6df7fb0a4e085b125dfd850eb05b7c1b6f8e430caed4bd5c5fa941b6ae034a91
  translated_at: 2026-09-26T09:25:44Z
  stamped_at: 2026-09-26T18:34:44Z
  reviewed_by: null
---

# Organisational Policies - IaC and Infrastructure as Code

The effective application of **Chapter 08 - IaC and Infrastructure as Code** requires the existence of **formal organisational policies** that frame, reinforce and legitimise the practices of technical governance, security and validation associated with the automation of infrastructure.

These policies ensure that:

- Infrastructure is treated as a **software artefact**, subject to the same rules of control, quality and traceability as source code;
- The management of environments and resources is **deterministic, auditable and reversible**;
- Security and compliance are **validated before the application** of any infrastructure change.

---

## 📄 Relevant Organisational Policies {#-políticas-organizacionais-relevantes}

| Policy Name | Mandatory? | Application | Summary of the Required Content |
|------------------|--------------|------------|--------------------------------|
| [**IaC Governance Policy**](/sbd-toe/assets/policies/policy-iac-seguro) | ✅ Yes | All repositories and pipelines that define or apply infrastructure | Defines principles, roles and responsibilities; requires *code review*, segregation of environments, access control and formal approval before *apply*. |
| [**Secrets and Credentials Management Policy in IaC**](/sbd-toe/assets/policies/policy-gestao-segredos) | ✅ Yes | IaC repositories, pipelines and orchestration tools | Prohibits the inclusion of secrets in code; mandates the use of *secret managers*; establishes a *rotation policy*, minimum *scopes* and monitoring of access. |
| [**IaC Security Validation and Testing Policy**](/sbd-toe/assets/policies/policy-iac-seguro) | ✅ Yes | CI/CD pipelines and shared modules | Requires the execution of *IaC scanning* and *policy-as-code* (tfsec, Checkov, KICS, OPA); mandatory validations before *merge* and *deploy*. |
| [**Cloud Resource Hardening and Secure Configuration Policy**](/sbd-toe/assets/policies/policy-iac-seguro) | ✅ Yes | Automated cloud, hybrid and on-premises environments | Defines minimum controls (IAM, network, storage, logging); imposes baselines (CIS, ENISA Cloud); mandates the detection and mitigation of *drift*. |
| [**IaC Module Management and Reuse Policy**](/sbd-toe/assets/policies/policy-iac-seguro) | ⚠️ Recommended | Internal registries of modules and templates | Establishes approval criteria, semantic versioning, security review and the lifecycle of reusable modules. |
| [**Automated Rollback and Recovery Policy**](/sbd-toe/assets/policies/policy-rollback) | ⚠️ Reinforced | Critical and production environments | Defines mechanisms for automated reversal and periodic tests of configuration and state restoration; establishes consistency requirements. |
| [**Infrastructure Change Observability and Audit Policy**](/sbd-toe/assets/policies/policy-iac-seguro) | ⚠️ Reinforced | All environments managed via IaC | Determines that all changes (automatic or manual) are recorded with *commit ID*, *pipeline run* and evidence of approval. |
| [**IaC Plan Approval Policy**](/sbd-toe/assets/policies/policy-aprovacao-plan-iac) | ✅ Yes | DevOps, AppSec | Mandatory human review before *apply*; impact criteria; segregation of duties and SoD |

---

## 📃 Minimum structure of each policy {#-estrutura-mínima-de-cada-política}

Each policy must contain, at a minimum:

- **Objective and scope** (technologies, environments, teams covered);  
- **Roles and responsibilities** (DevOps, Cloud Engineer, AppSec, Audit);  
- **Mandatory criteria and technical controls** (automatic validations, *gates*, segregation);  
- **CI/CD integration** (verification points, *policy-as-code*, approval);  
- **Traceable evidence** (logs, reports, *pull requests*);  
- **Frequency of review and compliance audit.**

---

## ✅ Final recommendations {#-recomendações-finais}

- The policies must be **published and managed centrally** in the organisation's technical policy repository.  
- They must be **integrated into the CI/CD pipelines** as automatic compliance mechanisms (*policy enforcement*).  
- Their application must be **assessed in the chapter's per-project review checklists** and in security audits.  
- Continuous alignment with **CIS/ENISA benchmarks** and with the practices of the *cloud providers* is recommended.  
- Compliance with these policies is a **formal maturity criterion** in infrastructure security and DevSecOps.

> 📁 Templates or detailed examples of these policies may be included in future versions as complementary `60-*.md` files of the manual.
