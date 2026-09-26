---
id: policy-containers-seguros
title: Secure Containers Policy
description: Organisational policy that defines the security requirements for the building, scanning, signing, runtime configuration and management of container images, including securityContext hardening, admission policies in Kubernetes, network isolation and runtime monitoring, proportional to the criticality level (L1, L2, L3).
tags: [policy, containers, Docker, Kubernetes, imagens, scanning, runtime, securityContext, OPA, Kyverno, assinatura, cap09, L1, L2, L3, governance]
grupo: infraestrutura
sidebar_position: 23
translation:
  source_locale: pt
  source_path: 020-assets/policies/23_policy-containers-seguros.md
  source_sha256: f459d88df873a67188cbd668b840453dc61d5870c7be47f3f56d85670b0f14b8
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 9cd0b4ca2d0efd6a5efd0232e597a40448034f11b295cfd54e690c47a71988cc
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [cycle_iteration, framework_source_corpus, lifecycle_phase, provenance, requirement_runtime, sbdtoe_sbd, verificacao_check, verification_taxonomy]
  glossary_sha256: f04fb69f8e9c35a5ac329866aae65eafd920a0a3fc072fcb6d13d877d05d3547
  translated_at: 2026-09-26T14:10:56Z
  stamped_at: 2026-09-26T18:36:57Z
  reviewed_by: null
---

# Secure Containers Policy

## 1. Objective {#1-objetivo}

This policy defines the security requirements for the **full lifecycle of containers**: from the choice of base image, through building, scanning and signing, to runtime configuration and monitoring in production.

Containers offer logical isolation - not security isolation by default. A container without execution restrictions (running as root, with excessive capabilities, without a read-only filesystem, without a NetworkPolicy) has a potential impact on the host node and on other workloads that undermines the isolation advantages the technology could offer. Security in containers is not automatic - it is the result of deliberate configuration and systematic verification.

The objective of this policy is to ensure that:

- Images are built from trusted, minimal bases with the version pinned by digest
- Vulnerabilities in images are detected and blocked before production
- Images in production are signed and their integrity is verified before deploy
- Runtime configurations follow the principle of least privilege and are enforced by policy
- Secrets are never embedded in images

---

## 2. Scope {#2-âmbito}

This policy applies to all containers used in development, integration, staging and production environments, including application containers, sidecar containers and infrastructure containers (e.g. proxies, service mesh).

---

## 3. Image building {#3-construção-de-imagens}

### 3.1 Base image {#31-imagem-base}

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Base image from a verified origin (official repository or internal catalogue) | Mandatory | Mandatory | Mandatory |
| Version pinned by SHA256 digest (not by floating tag) | Recommended | Mandatory | Mandatory |
| Minimal base image (distroless, alpine, slim) | Recommended | Mandatory | Mandatory |
| No unnecessary debug tools in the final image (curl, bash, wget) | Recommended | Mandatory | Mandatory |

### 3.2 Secure Dockerfile {#32-dockerfile-seguro}

The Dockerfile must follow these mandatory practices:

- [ ] Multi-stage build where applicable: separation between build environment and runtime image
- [ ] `USER` set to a non-root user in the final instruction before `CMD`/`ENTRYPOINT`
- [ ] No `ADD` with remote URLs (use `COPY` from the local context)
- [ ] No `--privileged` or `--cap-add` in build instructions
- [ ] No secrets in `ARG`, `ENV` or `RUN` (including exported variables)
- [ ] Dockerfile linter (`hadolint` or equivalent) with no blocking findings

### 3.3 Image registries {#33-registos-de-imagens}

At L2/L3, images must be produced and stored in controlled internal registries:

- [ ] Internal registry as the source of images in production (no direct pulls from Docker Hub)
- [ ] Allowlist of authorised external registries (for base images)
- [ ] Access to the registry controlled by authentication - no anonymous access

---

## 4. Image scanning {#4-scanning-de-imagens}

The pipeline must include vulnerability scanning of the image produced:

| Gate | L1 | L2 | L3 |
|---|---|---|---|
| Image scanner (Trivy, Grype, Clair) | Alert | Blocks High/Critical | Blocks Medium+ |
| SBOM generated per image | Recommended | Mandatory | Mandatory |
| Scan of Dockerfile configurations (hadolint) | Recommended | Mandatory | Mandatory |
| Scan for secrets embedded in layers | Mandatory | Mandatory | Mandatory |

The scanning report must be archived as a pipeline artefact, associated with the image digest.

---

## 5. Signing and provenance {#5-assinatura-e-proveniência}

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Image signed after build (Cosign or equivalent) | Optional | Recommended | Mandatory |
| Signature verified before deploy | Optional | Recommended | Mandatory |
| Provenance attestation (SLSA-like) | Not applicable | Recommended | Mandatory |
| Deploy blocked if the signature is missing or invalid | Not applicable | Recommended | Mandatory |

At L3, only images signed by the organisation's pipeline must be admitted to production. Unsigned images or images with a signature of unknown origin must be rejected by the admission controller.

---

## 6. Runtime configuration (hardening) {#6-configuração-de-runtime-hardening}

### 6.1 Mandatory securityContext {#61-securitycontext-obrigatório}

All running containers must have the following `securityContext` configured (Kubernetes) or equivalent:

| Configuration | L1 | L2 | L3 |
|---|---|---|---|
| `runAsNonRoot: true` | Mandatory | Mandatory | Mandatory |
| `allowPrivilegeEscalation: false` | Mandatory | Mandatory | Mandatory |
| `readOnlyRootFilesystem: true` | Recommended | Mandatory | Mandatory |
| `capabilities: drop: ["ALL"]` | Recommended | Mandatory | Mandatory |
| `privileged: false` | Mandatory | Mandatory | Mandatory |
| `seccompProfile: RuntimeDefault` (or more restrictive) | Recommended | Mandatory | Mandatory |

### 6.2 Volumes and mounts {#62-volumes-e-montagens}

- [ ] No mounting of `/var/run/docker.sock` (container access to the Docker socket)
- [ ] Volumes mounted in read-only mode whenever possible
- [ ] No sharing of host namespaces (`hostNetwork`, `hostPID`, `hostIPC`) without formal justification

### 6.3 Admission policies (Kubernetes) {#63-policies-de-admissão-kubernetes}

At L2/L3 with Kubernetes, admission policies must be enforced by an admission controller (OPA/Gatekeeper, Kyverno, or PSA):

- [ ] Policies that enforce a minimum `securityContext` in all production namespaces
- [ ] Violations blocked and audited with timestamp, actor and pod details
- [ ] Policies versioned and approved by the AppSec Engineer

---

## 7. Network isolation {#7-isolamento-de-rede}

- [ ] NetworkPolicy defined for each namespace/workload (deny-all by default, explicit permit)
- [ ] No unrestricted communication between namespaces or between pods without an explicit policy
- [ ] Egress controlled to the necessary external services (allowlist of destinations)

---

## 8. Secrets management in containers {#8-gestão-de-segredos-em-containers}

Secrets must not be included in container images under any circumstances:

- [ ] No secrets in `ENV` variables in the Dockerfile
- [ ] No secrets in build `ARG` (they persist in the image layers)
- [ ] Secrets injected at runtime via Kubernetes Secrets (with encryption at rest) or an external vault (Vault, AWS Secrets Manager, etc.)
- [ ] Preferred alternative at L3: workload identity (IRSA, GKE Workload Identity, Vault Agent) - no persisted secrets

---

## 9. Runtime monitoring {#9-monitorização-de-runtime}

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Logging of runtime events (start, stop, errors) | Basic | Mandatory | Mandatory |
| Runtime anomaly detection (Falco, eBPF-based) | Not applicable | Recommended | Mandatory |
| Alerts in the event of a runtime policy violation | Not applicable | Mandatory | Mandatory |
| Automatic response to critical anomalies (kill container) | Not applicable | Recommended | Recommended |

---

## 10. Expected artefacts {#10-artefactos-esperados}

| Artefact | Description | Retention |
|---|---|---|
| Image scan report (Trivy/Grype) | Vulnerabilities per build | 90 days (L2), 1 year (L3) |
| Image SBOM | Inventory per build | See SBOM Policy |
| Image signature | Per build, in the image registry | While the image is in use |
| Provenance attestation | Per build | 1 year (L2), 2 years (L3) |
| Admission logs | Policy violations in the cluster | 90 days (L2), 1 year (L3) |

---

## 11. Responsibilities {#11-responsabilidades}

| Role | Responsibility |
|---|---|
| Developer | Write secure Dockerfiles; do not include secrets; use approved base images |
| DevOps / SRE | Configure the build and scanning pipeline; manage the image registry; configure runtime policies |
| AppSec Engineer | Define scanning thresholds; approve admission policies; review securityContext configurations |
| GRC / Compliance | Audit scanning reports; verify the compliance of runtime policies; validate retention |

---

## 12. Review and audit of this policy {#12-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Incident originating in an image vulnerability or a runtime misconfiguration
- Change of the container orchestrator or of the admission controller
- Publication of a new version of the CIS Docker or Kubernetes benchmarks

---

## 13. Normative and technical references {#13-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 09 - Containers and Images | Building, scanning, runtime, SBOM, signing |
| Golden Base Images Policy (`24_policy-golden-base-images.md`) | Catalogue of approved base images |
| SBOM Policy (`11_policy-sbom.md`) | SBOM per image |
| Secrets Management Policy (`18_policy-gestao-segredos.md`) | Secrets in containers |
| CIS Docker Benchmark v1.6 | Reference controls for Docker |
| CIS Kubernetes Benchmark | Reference controls for Kubernetes |
| NIST SP 800-190 | Application Container Security Guide |
| ENISA Cloud Baseline | Security in containers - European baseline |
| Cosign / Sigstore | Image signing and verification |
| Falco | Runtime security for containers |
| OPA Gatekeeper / Kyverno | Admission controllers for Kubernetes |
