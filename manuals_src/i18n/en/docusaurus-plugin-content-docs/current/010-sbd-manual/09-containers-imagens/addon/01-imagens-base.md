---
id: imagens-base
title: Secure and Minimal Base Images
description: Selection, hardening and validation of secure base images for containers
tags: [containers, imagens base, hardening, runtime, supply chain]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/addon/01-imagens-base.md
  source_sha256: 220e636ba57eb7a75d05b9604cf043253dbe3afa1830fbe6ce81a8f3fa843b10
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: b04f538fc00a4e4ba06326f0d966300b2d5fe146ae8516e1df18416292554e58
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 6163399f3326e10bced3afe0b9ddfa197cae2c643b2beeb28c226f7164a47a99
  glossary_keys: [cycle_iteration, discipline, framework_source_corpus, harbor_registry, lifecycle_phase, provenance, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: 2278a334e0ff78288ba206e23a4b25ca4cd969ba6056b9e5498cbcf565ae6239
  translated_at: 2026-09-26T09:58:14Z
  reviewed_by: null
---

# Secure and Minimal Base Images

## 🌟 Objective {#-objetivo}

Ensure that all applications, pipelines and services that use containers **start from secure, controlled and minimised base images**, reducing the attack surface and establishing an **explicit point of trust** in the execution chain.

In a modern SSDLC context, base images are frequently **selected, inherited or reused automatically** by pipelines, templates or code generators.  
For that reason, their choice **cannot be implicit or tacit**: it must be an **initial human decision**, supported by technical validation and subject to periodic reassessment.

A secure base image makes it possible to:

- Significantly reduce exposure to known vulnerabilities (CVE);
- Minimise the number of binaries and libraries loaded;
- Apply integrity and provenance controls;
- Ensure consistency and predictability in execution environments;
- Support organisational policies for secure execution.

---

## 🧬 What a secure base image is {#-o-que-é-uma-imagem-base-segura}

A **secure base image** is one that:

- Is maintained and updated by a trusted source, internal or explicitly approved;
- Contains only what the application needs to function (e.g. distroless, alpine);
- Avoids interactive tools (`curl`, `wget`, `bash`, `ping`) that widen the attack surface;
- Uses a non-root user by default;
- Is subjected to **automatic technical validation** (SCA, container scanners);
- Is **assessed and approved by an explicit human decision** before its adoption;
- Is signed and traceable throughout the pipeline.

> ⚠️ Generic images such as `ubuntu`, `node`, `python` or `debian` may contain hundreds of unnecessary packages.  
> Their use in production **must not be implicit** and requires reinforced justification and validation.

---

## 📘 Examples of recommended images {#-exemplos-de-imagens-recomendadas}

| Type               | Example                                  | Notes                                                                 |
|--------------------|------------------------------------------|-----------------------------------------------------------------------|
| Distroless         | `gcr.io/distroless/static`               | No shell or package manager; drastically reduces the surface       |
| Minimal Alpine | `alpine:3.19`                            | Small image; requires compatibility validation                   |
| Builder + runtime  | Multi-stage `golang:alpine` → `distroless` | Compiles in one stage, runs in another                                    |
| In-house image     | `registry.corp.com/base/api`             | Controlled by the organisation, with a baseline and a maintenance SLA          |

These examples **do not constitute automatic authorisation**.  
Each image must be **assessed, approved and registered** as a valid base image.

---

## 🛠️ How to apply {#️-como-aplicar}

Correct application of secure base images requires discipline and traceability:

1. **Select the base image according to the language and the type of application**, assuming that the choice may be reused automatically;
2. **Assess the candidate image** (SCA scanner, composition, attack surface);
3. **Decide explicitly on its approval** as an organisational base image;
4. **Pin the version or digest**, avoiding floating references;
5. **Remove debug tools and interactive shells**;
6. **Run as a non-root user**, defined in the `Dockerfile`;
7. **Sign the image after validation** (see `03-assinatura-cadeia-trust.md`);
8. **Integrate validation and enforcement into the pipeline**, without replacing human decision (see `05-policies-runtime-opa.md`);
9. **Publish the image to a controlled registry**, with traceability and access control.

---

## 📂 Where to keep approved base images {#-onde-manter-imagens-base-aprovadas}

Approved base images must be treated as **organisational trust assets**:

- Internal or controlled registry (Artifactory, Harbor, ECR, GCR);
- Catalogue maintained by the platform/AppSec team;
- Fixed references (version or digest), never `latest`;
- Associated documentation with:
  - origin,
  - approval criteria,
  - review date,
  - owners.

The absence of this catalogue means **effective audit is impossible**.

---

## 🔁 Reassessment and lifecycle {#-reavaliação-e-ciclo-de-vida}

The approval of a base image **is not permanent**.

There must be:
- Periodic reassessment (e.g. by age, relevant CVEs, change of context);
- A deprecation and replacement process;
- Capacity for rapid revocation in the event of an incident.

Automatic reuse of images **does not exempt** this revalidation.

---

## ✅ Good practices {#-boas-práticas}

- Avoid `latest`: use auditable versions or digests;
- Prefer multi-stage builds;
- Reduce layers and dependencies;
- Reassess base images after critical CVEs;
- Associate an SBOM with the base image;
- Define a TTL for mandatory review of old images.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                         | Relation to base images                                  |
|----------------------------------|-----------------------------------------------------------|
| `03-assinatura-cadeia-trust.md`  | Signing and integrity verification                   |
| `05-policies-runtime-opa.md`    | Technical enforcement of approved images                  |
| `06-sbom-containers.md`         | Inventory and composition of images                       |
| `07-vulnerabilidades-imagens.md`| Continuous vulnerability analysis                      |
| `09-riscos-processo-imagens.md` | Separation between automatic validation and human decision     |

> 🧩 The base image is the **first point of conscious decision** in the container execution chain.  
> Without that explicit decision, all the remaining control loses its meaning.
