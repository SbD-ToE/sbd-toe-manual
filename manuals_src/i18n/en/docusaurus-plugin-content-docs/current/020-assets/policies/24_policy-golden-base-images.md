---
id: policy-golden-base-images
title: Golden Base Images Policy
description: Organisational policy that defines the requirements for the creation, approval, semantic versioning, patching, deprecation and revocation of container base images approved by the organisation (Golden Base Images), including patching SLAs by criticality and management of the internal catalogue, proportional to the criticality level (L1, L2, L3).
tags: [policy, golden base images, imagens base, container, catálogo, patching, digest, depreciação, revogação, cap09, L1, L2, L3, governance]
grupo: infraestrutura
sidebar_position: 24
translation:
  source_locale: pt
  source_path: 020-assets/policies/24_policy-golden-base-images.md
  source_sha256: 33200f8d2e966e4ad9543881a3479b4fe8de3b1920bcd0aa436e431af440b0b8
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 9d3a7be4aa98b8b81f52add453624a9a7ee9e5ea212a68e389ff163f55275363
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bc04ded428e40ee1c214f8535dfb1904655b64166d0aa82b5df521e4230b8cb0
  glossary_keys: [avaliacao, cycle_iteration, harbor_registry, lifecycle_phase, practitioner_manual, requirement_runtime, sbdtoe_sbd, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: 94087aa3603a142f51704b56e6ba0fb5f92c5fbda10d3bb0f43c91182b769e29
  translated_at: 2026-09-26T14:10:57Z
  reviewed_by: null
---

# Golden Base Images Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for **lifecycle management of container base images approved by the organisation** - the so-called Golden Base Images (GBI).

Every container image built by the organisation inherits the security characteristics of its base image. A base image that is unaudited, outdated or of unverified origin is a structural vulnerability that propagates to every service that uses it. The centralisation and governance of base images is therefore a multiplier control: a well-managed base update fixes vulnerabilities in all services simultaneously; a compromised base compromises them all.

The objective of this policy is to ensure that:

- The organisation maintains a controlled catalogue of approved base images
- No container image in production is built on bases outside the approved catalogue
- Golden Base Images are kept up to date with a patching SLA defined by criticality
- Deprecated or revoked base images are replaced in a controlled manner
- The integrity of each base image is verifiable by SHA256 digest

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

| Level | Applicability |
|---|---|
| L1 | Recommended; use of base images from official sources with a pinned version |
| L2 | Mandatory; GBI catalogue maintained; builds with bases outside the catalogue blocked |
| L3 | Mandatory; catalogue with formal approval, changelog, patching SLA and immediate revocation |

---

## 3. Golden Base Images catalogue {#3-catálogo-de-golden-base-images}

### 3.1 Catalogue structure {#31-estrutura-do-catálogo}

The GBI catalogue (`golden-base-images.yaml` or equivalent) is the official inventory of base images approved for use in the organisation's builds. Each entry must contain:

- [ ] Unique identifier of the GBI (e.g. `ubuntu-22.04-minimal-v1.3.2`)
- [ ] Upstream source image (e.g. `ubuntu:22.04`) and SHA256 digest of the referenced upstream version
- [ ] SHA256 digest of the internal GBI (in the organisation's internal registry)
- [ ] Semantic version of the GBI
- [ ] Approval date and person responsible for the approval
- [ ] Date of the last security review
- [ ] Status: `active` / `deprecated` / `revoked`
- [ ] Upstream End-of-Life (EOL) date (where applicable)
- [ ] Changelog of previous versions

### 3.2 Location {#32-localização}

GBIs are stored in the organisation's internal image registry (Artifactory, Harbor, ECR, GCR or equivalent), with:

- [ ] Access controlled by authentication - no anonymous pull
- [ ] Immutability of digests (once published, the digest cannot be changed)
- [ ] Semantic tags associated with immutable digests (no redefinition of existing tags)

---

## 4. Approval of new GBIs {#4-aprovação-de-novas-gbis}

Before a new base image is added to the catalogue, a formal assessment must be carried out:

| Assessment criterion | Description |
|---|---|
| Origin and maintenance | Image from an official repository or a trusted provider with a track record of responding to CVEs |
| Minimalism | Contains only what is necessary for the use case; no unnecessary diagnostic tools |
| Active CVEs | No active Critical or High CVEs in the candidate version |
| Upstream EOL | EOL date known and not imminent (minimum of 12 months of remaining support) |
| Licence | Licence compatible with the organisation's policy |
| Compatibility | Tested with the stacks and frameworks used by the organisation |

The result of the assessment must be recorded with:

- [ ] Decision (approved / rejected) with justification
- [ ] Responsible for approval: AppSec Engineer + senior DevOps/SRE
- [ ] Approval date and version assessed

---

## 5. Semantic versioning {#5-versionamento-semântico}

GBIs must follow semantic versioning (`MAJOR.MINOR.PATCH`):

| Version type | When to use |
|---|---|
| **PATCH** | Update of OS packages without a change to API or behaviour; security patches |
| **MINOR** | Addition of components; runtime upgrade (e.g. Python 3.11 → 3.12 while maintaining compatibility) |
| **MAJOR** | Change of base OS, breaking changes, replacement of a major runtime |

---

## 6. Patching SLA {#6-sla-de-patching}

When a CVE affecting an active GBI is published, the deadline for publishing a new fixed version is:

| CVE severity | L2 | L3 |
|---|---|---|
| Critical (CVSS ≥ 9.0) | 7 days | 3 days |
| High (CVSS 7.0–8.9) | 30 days | 15 days |
| Medium (CVSS 4.0–6.9) | 90 days | 45 days |
| Low | 180 days | 90 days |

Patching consists of:

1. Updating the GBI (new PATCH or MINOR version as appropriate)
2. Running the build and scanning pipeline for the new version
3. Publishing to the internal registry after automatic approval (green CI) + manual review where applicable
4. Notifying the teams with builds that reference the affected version
5. Deprecating the previous version (see section 7)

---

## 7. Deprecation {#7-depreciação}

A GBI must be marked as `deprecated` when:

- A new patched version is available and stable
- The upstream has reached EOL
- There is an approved replacement GBI that covers the same use case

A deprecated GBI:

- [ ] Remains accessible in the registry for existing builds in transition
- [ ] Must not be referenced in new Dockerfiles
- [ ] The pipeline issues a warning when a build uses a deprecated GBI
- [ ] Has a defined removal deadline (maximum of 60 days after deprecation at L2/L3)

---

## 8. Revocation {#8-revogação}

A GBI must be marked as `revoked` and removed immediately when:

- A critical vulnerability is discovered with no fix available and with an active exploitation vector
- The integrity of the image is compromised (supply chain attack, manipulated digest)
- The upstream has been compromised

A revoked GBI:

- [ ] Is removed from the registry (or made inaccessible for pull) immediately
- [ ] The pipeline blocks any build that attempts to use the revoked GBI
- [ ] Teams are notified immediately with replacement instructions
- [ ] Services in production that use the revoked GBI are identified via the runtime inventory and prioritised for replacement

:::warning
The revocation of a GBI is a security event that may require activation of the incident response process if services in production are exposed. Traceability of which services use each GBI (via SBOM and the runtime inventory) is a prior requirement for an effective response.
:::

---

## 9. Validation in the pipeline {#9-validação-em-pipeline}

The build pipeline of any service must verify the GBI used:

| Gate | L1 | L2 | L3 |
|---|---|---|---|
| GBI referenced by SHA256 digest (not by tag) | Recommended | Mandatory | Mandatory |
| GBI in the catalogue with status `active` | Recommended | Mandatory | Mandatory |
| Warning if GBI is `deprecated` | Warning | Blocking warning | Blocking |
| Block if GBI is `revoked` | Block | Block | Block |

---

## 10. Responsibilities {#10-responsabilidades}

| Role | Responsibility |
|---|---|
| DevOps / SRE (Platform) | Maintain the catalogue; build and publish GBIs; carry out patching within the SLA; manage the internal registry |
| AppSec Engineer | Approve new GBIs; define patching SLAs; coordinate revocations; monitor CVEs in active bases |
| Developer | Reference GBIs by digest; do not use images outside the catalogue; report compatibility problems |
| GRC / Compliance | Audit the catalogue; verify compliance with SLAs; validate the traceability of GBIs in production |

---

## 11. Review and audit of this policy {#11-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Incident originating in a compromised or outdated GBI
- Adoption of a new container platform (e.g. orchestrator migration)
- Change in the approval criteria for base images by the security community

---

## 12. Normative and technical references {#12-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 09 - Containers and Images | US-01, US-11, US-15: secure bases, patching, catalogue |
| Secure Containers Policy (`23_policy-containers-seguros.md`) | Use of GBIs in builds and runtime |
| SBOM Policy (`11_policy-sbom.md`) | SBOM per base image and traceability at runtime |
| CIS Docker Benchmark v1.6 | Security criteria for base images |
| NIST SP 800-190 | Application Container Security - base images |
| Cosign / Sigstore | Signing and verification of GBIs |
| Harbor / Artifactory | Reference internal registries for GBI management |
