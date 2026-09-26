---
id: policies-relevantes
title: Policies
description: Organisational policies required to guarantee the security, traceability and governance of containers and images throughout the lifecycle.
tags: [políticas, containers, imagens, supply chain, kubernetes, devsecops, cloud]
sidebar_position: 60
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/policies-relevantes.md
  source_sha256: ca77b02bd3b5f8bd3b8d079dc8f8651c34b768ff4b8b59698f989e0f9c751fae
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 6dd6732a6df88d7d1cd705d16c76a5a295757cbaca3c124858a6f1b52f74ca84
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 6163399f3326e10bced3afe0b9ddfa197cae2c643b2beeb28c226f7164a47a99
  glossary_keys: [chapter_role, cycle_iteration, lifecycle_phase, maturity, practitioner_manual, provenance, segregacao_de_funcoes, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: d1e2ba8723e7eb46e1dea1321f3a4af9ef1f879ace6a31093768938d8e29b2ba
  translated_at: 2026-09-26T09:58:25Z
  reviewed_by: null
---

# Organisational Policies - Containers and Images

The effective application of **Chapter 09 - Containers and Images** requires the existence of **formal organisational policies** that frame and reinforce the practices of building, validation, signing, governance and execution of containers and images.

These policies ensure that:

- Images are built in a **secure, traceable and reproducible** way, with verifiable provenance;  
- The execution of containers takes place in **protected, auditable and controlled** environments;  
- There is **clear governance over the registries and pipelines** that handle containerisation artefacts.

---

## 📄 Relevant Organisational Policies {#-políticas-organizacionais-relevantes}

| Policy Name | Mandatory? | Application | Summary of the Required Content |
|------------------|--------------|------------|--------------------------------|
| [**Secure Image Building Policy**](/sbd-toe/assets/policies/policy-golden-base-images) | ✅ Yes | All build pipelines | Defines requirements for a secure base, _digest pinning_, fixed versions, _linting_ and automatic validation of Dockerfiles; mandates review and approval before publication. |
| [**Image Vulnerability Management Policy**](/sbd-toe/assets/policies/policy-containers-seguros) | ✅ Yes | CI/CD registries and pipelines | Mandates automated _scanning_ (SCA, CVE, licences); defines severity criteria and remediation deadlines; blocking on critical vulnerabilities. |
| [**Image Signing and Provenance Policy**](/sbd-toe/assets/policies/policy-containers-seguros) | ✅ Yes | Internal and external registries | Requires digital signing (Sigstore/Cosign), SLSA _attestations_ and integrity verification before execution. |
| [**Container Registry and Repository Governance Policy**](/sbd-toe/assets/policies/policy-containers-seguros) | ✅ Yes | All internal registries and repositories | Defines _ownership_, access control, _RBAC_, retention, periodic cleanup, audit and _access logs_. |
| [**Container Hardening and Secure Execution Policy**](/sbd-toe/assets/policies/policy-containers-seguros) | ⚠️ Reinforced | Execution environments (Docker, Kubernetes, etc.) | Defines minimum isolation parameters (seccomp, AppArmor, SELinux), _network policies_, _least privilege_ and _read-only rootfs_. |
| [**Obsolete Image Management and Cleanup Policy**](/sbd-toe/assets/policies/policy-containers-seguros) | ⚠️ Recommended | Repositories and pipelines | Establishes retention periods, _rebuild_ policies and the removal of vulnerable or unused images. |
| [**Deploy Manifest Validation and Approval Policy**](/sbd-toe/assets/policies/policy-containers-seguros) | ⚠️ Reinforced | Kubernetes, Compose, Helm | Mandates automated validation of manifests with _policy-as-code_ (OPA, Conftest) and security _admission controllers_. |
| [**Container Execution Observability and Audit Policy**](/sbd-toe/assets/policies/policy-containers-seguros) | ⚠️ Reinforced | Production environments | Determines the collection of metrics, _runtime logs_, commit-digest-deploy correlation and automatic alerts for _shadow containers_. |

---

## 📃 Minimum structure of each policy {#-estrutura-mínima-de-cada-política}

Each policy must contain:

- **Objective and scope** (artefacts, pipelines, environments covered);  
- **Roles and responsibilities** (DevOps, Cloud Ops, AppSec, Audit);  
- **Mandatory technical controls** (automatic validations, gates, segregation of duties);  
- **CI/CD integration** (control points and automatic blocks);  
- **Evidence and metrics** (_scan_ reports, logs, _attestations_, audits);  
- **Review frequency** and the policy update procedure.

---

## ✅ Final recommendations {#-recomendações-finais}

- All policies must be **published and approved by security and engineering management**, and integrated into *DevSecOps* processes.  
- Compliance must be **validated periodically** through _checklists_, technical audits and maturity metrics.  
- The policies must align with the practices of **Dependency Management** (Ch. 05) and **IaC** (Ch. 08) to guarantee the coherence of the supply chain.  
- Automating compliance verification via **_policy-as-code_** is recommended, integrating the rules into the build and deploy _pipelines_.  
- The application of these policies constitutes direct evidence of compliance with **SSDF, SLSA, CIS, ENISA and SAMM** in the context of **software supply chain security**.

> 📁 Templates and practical examples may be included in future versions of the manual as complementary `60-*.md` files.
