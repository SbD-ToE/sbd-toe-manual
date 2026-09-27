---
id: catalogo-requisitos-containers
title: Containers and Images Requirements Catalogue
description: Canonical catalogue of security requirements for containers and images (CNT-001 to CNT-012), with applicability by risk level and acceptance criteria for the selection of base images, hardening, signing, scanning, runtime policies and access to registries.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:containers, CNT, imagens, hardening, runtime, rastreabilidade, L1, L2, L3, kubernetes, admission-control, supply-chain, auditoria]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/addon/00-catalogo-requisitos.md
  source_sha256: 98c24c2fdd7e43843bfc9e7a0cba781e227210fe3dc4b3df97ba85b397573b94
  source_commit: 036d74010f423f247be988e4a417375c74edb9d9
  target_sha256: 67797e57bf6a23ea7a956ece08107bf4988e7c449fe40bde19cea9f8e5acf5de
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [audit_trail, cycle_iteration, lifecycle_phase, mapping, provenance, requirement_runtime, risk_level, sbdtoe_sbd, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: bcb250f3a75280ac3f789b6ddd45cca571eb93db76926e8cc69e33e12d4a5730
  translated_at: 2026-09-27T07:53:46Z
  stamped_at: 2026-09-27T07:53:46Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Containers and Images Requirements Catalogue

## Scope: the container as a software artefact subject to governance {#âmbito-o-container-como-artefacto-de-software-sujeito-a-governação}

This catalogue covers **security requirements that apply to the lifecycle of containers and images** - from the selection of the base image, through hardening and scanning, to signing, provenance verification, runtime policies and access to registries.

Containers are complete software artefacts that encapsulate code, dependencies and runtime configuration. Their ubiquity in pipelines and in production introduces specific risk vectors: vulnerable base images, permissive configurations, lack of verifiable provenance and absence of execution policies. These requirements establish the minimum controls for containers to be **built, promoted and executed in a trustworthy and auditable way**.

For the complete mapping of all SbD-ToE requirements catalogues by technical domain, canonical prefix and owner, see [Ch. 02 - Catalogue Mapping](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **On curation:** Consolidated from the OWASP Top 10 (A06), CAPEC-310, CWE-1104, the CIS Benchmarks for Docker and Kubernetes, the NSA/CISA Kubernetes Hardening Guide, SLSA and established practices for Kubernetes, Docker and OCI registries. It must be adapted to the orchestration context in use and reviewed with each update of the container security policy.

For project instantiation and the operational nomenclature (`SEC-Lx-CNT-CODIGO`), see [Taxonomy and Traceability](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Conventions {#convenções}

| Symbol | Meaning |
|---------|-------------|
| ✔ | Mandatory requirement at this level |
| - | Not applicable or not mandatory at this level |

The levels are cumulative: L3 includes all L1 and L2 requirements; L2 includes all L1 requirements.

---

## CNT Catalogue - Containers and Images {#catálogo-cnt---containers-e-imagens}

Requirements that guarantee that containers are built, validated, promoted and executed with security controls proportional to the risk of the workloads they encapsulate.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| CNT-001 | Base images from a trusted and approved origin | ✔ | ✔ | ✔ | Base images sourced from a maintained list of approved origins; images from unapproved origins rejected in the pipeline or by admission control; selection decision documented with a technical justification. |
| CNT-002 | Vulnerability scanning of images in the CI/CD | ✔ | ✔ | ✔ | Container scanner active in the pipeline (e.g. Trivy, Grype); CVEs of critical severity block the promotion of the image; scan report available and linked to the build. |
| CNT-003 | Minimal images - absence of unnecessary components | ✔ | ✔ | ✔ | No unjustified interactive binaries (curl, bash, wget, ping); distroless, scratch or alpine image as the base whenever possible; verifiable by analysis of the artefact's layers. |
| CNT-004 | Execution as a non-root user | ✔ | ✔ | ✔ | `USER` directive with a non-root user in the Dockerfile or equivalent; admission policy that rejects containers running as root; evidence of active enforcement. |
| CNT-005 | Read-only file system at runtime | - | ✔ | ✔ | `readOnlyRootFilesystem: true` or equivalent configured; volumes with write permission limited to what is strictly necessary and explicitly declared; verifiable by inspection of the configuration. |
| CNT-006 | Restriction of kernel capabilities and syscall profiles | - | ✔ | ✔ | `drop: ALL` as the default, with capabilities added explicitly and justified; seccomp profile active (runtime default or custom); no unjustified `--privileged` or `hostPID`/`hostNetwork`. |
| CNT-007 | Signing and provenance verification of images | - | ✔ | ✔ | Images signed (e.g. Sigstore/Cosign, Notary v2) before publication in a registry; signature verification enforced by an admission controller before deploy; images without a valid signature rejected. |
| CNT-008 | SBOM per published image | - | ✔ | ✔ | SBOM generated and attached to each image published in the registry; CycloneDX or SPDX format; accessible for audit and incident response without the need for a rebuild. |
| CNT-009 | Active admission control policies | - | ✔ | ✔ | Admission controller active (OPA/Gatekeeper, Kyverno or equivalent); policies that block privileged containers, containers without a defined user, with host networking or with unauthorised sensitive volumes; admission and rejection logs available. |
| CNT-010 | Periodic renewal of base images | ✔ | ✔ | ✔ | Periodic rebuild or automatic trigger on update of the base image to incorporate security patches; images more than X days without a rebuild flagged; renewal policy defined, documented and complied with. |
| CNT-011 | Access to the registry with authentication and traceability | ✔ | ✔ | ✔ | Push and pull require authentication; access logs retained for the defined period; publication in public registries requires explicit approval; registry credentials with minimum scope and defined rotation. |
| CNT-012 | Namespace isolation and network policies in Kubernetes | - | - | ✔ | Network policies active per namespace; no inter-namespace access by default; critical workloads in dedicated namespaces with explicit network policies; evidence of active enforcement. |

---

## Explanatory notes {#notas-explicativas}

- **CNT-001**: The selection of the base image must be an **explicit and documented human decision** - not an implicit inheritance from a template or code generator. Images from bases such as `ubuntu:latest` or images without a verifiable maintainer are insufficient for L2/L3.
- **CNT-003**: The minimality of the image reduces the attack surface in the event of a runtime compromise. Tools such as `dive` or layer analysis make it possible to verify which binaries are present and to justify them.
- **CNT-006**: Restricting capabilities is a fundamental preventive control: a container with `CAP_SYS_ADMIN` or `--privileged` effectively has control of the host node in Kubernetes.
- **CNT-007**: The signing chain of trust must be verified downstream at the point of deploy - generating the signature without verifying it before execution does not constitute an effective control.
- **CNT-009**: The admission controller must be configured in `Enforce` mode, not only `Audit`, to be considered an effective control. Audit mode without enforcement is only observability, not protection.
- **CNT-010**: The renewal interval must be proportional to risk: for L3 workloads, a maximum cycle of 30 days; for L2, 60 days; for L1, 90 days. The relevant criterion is coverage of critical patches, not just the calendar.

---

> For the selection and validation of base images, see [Secure Base Images](./imagens-base).
> For hardening and execution restrictions, see [Container Hardening](./hardening-containers).
> For signing and the chain of trust, see [Signing and Chain of Trust](./assinatura-cadeia-trust).
> For runtime policies with OPA/Kyverno, see [Runtime Policies](./policies-runtime-opa).
> For vulnerability scanning of images, see [Image Vulnerabilities](./vulnerabilidades-imagens).
> For container SBOM, see [Container SBOM Inventory](./sbom-containers).
