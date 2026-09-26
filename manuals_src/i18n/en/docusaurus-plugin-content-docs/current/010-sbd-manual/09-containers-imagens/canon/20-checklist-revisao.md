---
id: checklist-revisao
title: Checklist - Containers and Images
sidebar_label: Review Checklist
description: Binary and auditable checklist to assess the practical adoption of the practices prescribed in Chapter 09 - Containers and Images
tags: [checklist, containers, imagens, supply chain, kubernetes, auditoria]
sidebar_position: 20
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/canon/20-checklist-revisao.md
  source_sha256: f043a287886c11c82226df0bb96ef1512b60b2ebcf970481938ad9df91ae13e8
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 3853689369efd9ddb1892a2932932f9c6fd14df89aa9fda78592d55711d786a3
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, avaliacao, chapter_role, cycle_iteration, instrument, lifecycle_phase, maturity, provenance, sbdtoe_sbd, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 7baa0e6e972e3388da665e6d26207b442590a76521787868ed0ef5640a407993
  translated_at: 2026-09-26T09:58:22Z
  stamped_at: 2026-09-26T18:34:57Z
  reviewed_by: null
---

# Periodic Review Checklist - Containers and Images

This checklist applies to all projects and pipelines that **build, distribute or run containers and images** within the scope of Chapter 09 - Containers and Images (`CNT-001` to `CNT-012`).
It serves as an instrument of binary and auditable verification of the **practical adoption of the prescriptions of this chapter**, enabling:

- Systematic control of security in the container build and execution chain;
- Verification per project at key moments of the lifecycle (build, deploy, operation);
- Generation of indicators of technical compliance and *supply chain security* maturity.

> 🗓️ **Its application is recommended at each significant release**, or whenever there are changes to base images, pipelines, registries or *runtime* configurations.

---

## 📋 Verification Items {#-itens-de-verificação}

| Item                                                                                                           | Verified? |
|----------------------------------------------------------------------------------------------------------------|-------------|
| Do base images come from an approved and maintained list of origins, and are images from non-approved origins rejected? (`CNT-001`) | ☐           |
| Is each image referenced by an immutable SHA digest, with no floating tags? (`CNT-001`)                          | ☐           |
| Are the images minimalist (without unjustified interactive binaries), with periodic rebuild according to a patching SLA? (`CNT-003`/`CNT-010`) | ☐           |
| Is there a versioned catalogue of Golden Base Images with approval, deprecation and revocation states?           | ☐           |
| Is there a registry allowlist with blocking by origin, authenticated access with retained logs and approval for publication to public registries? (`CNT-011`) | ☐           |
| Is there an active vulnerability scanner in CI/CD, and do vulnerabilities with severity equal to or above the threshold block the build or deploy? (`CNT-002`) | ☐           |
| Is an SBOM (CycloneDX or SPDX) generated and attached to each published image, accessible for audit? (`CNT-008`)    | ☐           |
| Do the containers run as a non-root user? (`CNT-004`)                                                  | ☐           |
| Are kernel capabilities restricted (`drop: ALL` + justified additions), and is there an active seccomp/AppArmor profile? (`CNT-006`) | ☐           |
| Is the root file system configured as read-only at runtime? (`CNT-005`)                          | ☐           |
| Are privileged execution and access to the Docker socket / hostPID / hostNetwork blocked, and is the effective hardening state verified against the declared one (drift)? (`CNT-006`) | ☐           |
| Are images signed (with a transparency log), and is the signature/provenance verified by an admission controller before deploy? (`CNT-007`) | ☐           |
| Is the admission controller in enforce mode, validating manifests against versioned policies (OPA/Kyverno), with admission and rejection logs? (`CNT-009`) | ☐           |
| Do workloads use a dedicated ServiceAccount with minimal RBAC and a NetworkPolicy with default deny-all and controlled egress, with critical workloads in dedicated namespaces? (`CNT-012`) | ☐           |
| Are images free of embedded credentials (verified by secret scanning at build), and do containers obtain credentials via ephemeral identity? | ☐           |
| For L3 critical workloads, is advanced sandboxing used (gVisor/Kata/Firecracker via RuntimeClass), and are runners/builders ephemeral, signed and resource-limited? | ☐           |
| Is there commit → pipeline → image → decision → execution traceability, with a record of the human promotion decision, retention/cleanup of obsolete images, and exceptions with a TTL and a formal object in the admission controller? | ☐           |
| Do self-hosted AI inference runtimes protect the model weights (at-rest encryption with keys in the vault, integrity verification by hash, audited access), with GPU isolation and separation of sensitive workloads? | ☐           |
| Do AI inference APIs require authentication, consumption-based rate limiting and `max_tokens`/prompt/timeout limits, with auditing per principal, a restrictive network policy and a pinned runtime with SCA? | ☐           |

---

## 🔄 Practical application notes {#-notas-de-aplicação-prática}

- This checklist may be converted into an **automated CI/CD step**, a digital validation form or a container compliance dashboard.
- Each item must be treated as a **binary indicator (yes/no)**, enabling the calculation of adoption KPIs per project, pipeline or team.
- Complete validation of this checklist confirms **technical compliance with Chapter 09**, supporting security audits and SbD-ToE maturity assessments.
- The results may be correlated with **Chapter 05 - Dependencies and SBOM**, ensuring full traceability of the supply chain.

> ❗ This chapter is **essential to the integrity and security of the software build and delivery chain**.
> The absence of these practices compromises trust in the distributed artefacts and compliance with the *supply chain security* requirements set out in NIS 2 and DORA.
