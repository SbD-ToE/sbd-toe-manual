---
id: excecoes-containers
title: Exceptions in Containers and Images
sidebar_position: 10
description: Specifics of exception management in the context of containers and images - admission control, image signing and vulnerability scanning
tags: [exceções, containers, imagens, admission-control, signing, scanning, opa, kyverno]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/addon/10-excecoes-containers.md
  source_sha256: 8f32d8463a3aa41202b519bef43941c0f30a0df846a84b21dc9b7ec660b29726
  source_commit: 036d74010f423f247be988e4a417375c74edb9d9
  target_sha256: 0cea052fc2460b23c8bb8a5df2f13693ac3df84608935324de408c3d0a3ae247
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [alcada, verificacao_check, verification_taxonomy]
  glossary_sha256: 28cd2e960d5f6da7fa653c83b87e274b2fd9220dce47c3421c49e90ed6b566c1
  translated_at: 2026-09-27T07:53:47Z
  stamped_at: 2026-09-27T07:53:47Z
  reviewed_by: null
---

# Exceptions in Containers and Images

> The base process, approval authorities, mandatory fields, chain of authority and lifecycle are defined in **Ch. 14 - `addon/12-processo-excecoes.md`**. This file defines only the specifics of this domain.

---

## Scope {#âmbito}

Exceptions to requirements of the containers and images catalogue: `CNT-001` to `CNT-012`.

---

## Triggers specific to this domain {#triggers-específicos-deste-domínio}

- a legacy base image with no immediate substitute that meets the approved-origin requirements (CNT-001);
- a critical CVE in a base image with no patch available for the version in use - distinct from the SCA exceptions of Ch. 05 because it acts at image level and is verified by an admission controller (CNT-002);
- image signing infrastructure (Cosign/Sigstore/Notary) not yet available - a migration exception with a defined deadline (CNT-007);
- a legacy workload incompatible with active admission controller policies - OPA/Gatekeeper, Kyverno - with a remediation plan (CNT-009);
- a kernel capability or syscall that is necessary and technically justified but conflicts with the required restrictive profile (CNT-006).

---

## Additional mandatory fields (containers) {#campos-adicionais-obrigatórios-containers}

| Field | Mandatory | Notes |
|---|---|---|
| Digest of the affected image | Yes | `sha256:...` - unambiguous identification of the artefact |
| Source registry | Yes | |
| Admission controller in use | Yes | OPA/Gatekeeper, Kyverno, or equivalent |
| Violated policy / rule | Yes | Name and version of the policy in the admission controller |
| Exception implemented in the admission controller? | Yes | If so, reference to the exception object (e.g. Kyverno `PolicyException`) |

---

## Exceptions in the admission controller {#excepções-no-admission-controller}

Exceptions to admission controller policies must be implemented as formal objects in the system itself (e.g. `PolicyException` in Kyverno, `constraint` with an exclusion in OPA/Gatekeeper), not as deactivation of the policy. The exception object in the admission controller is a mandatory evidence artefact and must be referenced in the chain of authority.

Exceptions implemented by globally deactivating a policy are always non-compliant, regardless of organisational approval.

---

## Image signing exceptions (migration) {#excepções-de-image-signing-migração}

Exceptions to CNT-007 because signing infrastructure is not yet available must include:

- an implementation plan with milestones and an owner;
- maximum time limit: ceilings of Policy 05 §7: L1 90 days; L2 60 days (Low/Medium) and 30 days (High); L3 30 days (Low/Medium) and 14 days (High); Critical 7 days with a remediation plan, not acceptable at L3; an extension requires GRC/CISO approval;
- compensating controls active during the exception window (e.g. digest verification, restriction of source registries).

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|---|---|
| `00-catalogo-requisitos.md` | Catalogue CNT-001..012 - requirements that may have exceptions |
| `03-assinatura-cadeia-trust.md` | Signing and verification infrastructure |
| `05-policies-runtime-opa.md` | Admission controller policies and exception mechanism |
| `07-vulnerabilidades-imagens.md` | Scanning and CVEs in images |
| Ch. 05 - `addon/09-excecoes-e-aceitacao-risco.md` | Package-level SCA exceptions - distinct from a CVE in an image |
| Ch. 14 - `addon/12-processo-excecoes.md` | Canonical exception management process |
