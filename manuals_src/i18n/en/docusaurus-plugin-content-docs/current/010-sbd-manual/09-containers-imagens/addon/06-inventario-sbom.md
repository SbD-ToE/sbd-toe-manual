---
id: sbom-containers
title: Container SBOM and Runtime Traceability
description: Generation, versioning and use of SBOMs as evidence of composition, not as proof of security
tags: [sbom, containers, rastreabilidade, supply-chain, assinatura]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/addon/06-inventario-sbom.md
  source_sha256: cbdcf98f30a57182d551fb4e1442b5b31e5b42894c2f894ec7891346f112b1f4
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: fb327a5f5ee107cab8240acfd723eb407913b9f53a967c9ada6308d2a6be4ed1
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 6163399f3326e10bced3afe0b9ddfa197cae2c643b2beeb28c226f7164a47a99
  glossary_keys: [audit_trail, cycle_iteration, lifecycle_phase, provenance, sbdtoe_sbd, traceability]
  glossary_sha256: b026e53d99524a8b07169f6d15aa6ebed33ee22cb357f261c0acfae35cefb328
  translated_at: 2026-09-26T09:58:17Z
  reviewed_by: null
---

# Container SBOM and Runtime Traceability

## 🌟 Objective {#-objetivo}

Ensure that all **container images used in pipelines or production** have an **SBOM (Software Bill of Materials)** generated from the real artefact, versioned and traceable, enabling:

- Objective visibility of components, libraries and layers;
- Vulnerability analysis based on the actual content of the image;
- Comparison between versions and detection of unexpected changes;
- Support for regulatory requirements (e.g. SLSA, SSDF, EO 14028).

In the SbD-ToE model, the SBOM is treated as **evidence of composition**, not as a guarantee of security nor as a substitute for risk analysis.

---

## 🧬 What a container SBOM is {#-o-que-é-um-sbom-de-container}

A **container SBOM** represents the **effective state of the image after the build**, including:

- Installed packages (e.g. `apk`, `apt`, `npm`, `pip`);
- Transitive dependencies;
- Origin and licensing information;
- Hashes, locations and metadata;
- Known links to CVEs.

> 🧱 An SBOM **is not equivalent** to a `Dockerfile`, lockfile or declarative manifest.  
> It describes **what is actually present**, including side effects of the build process.

---

## ⚠️ Complete SBOM ≠ absence of risk {#️-sbom-completo--ausência-de-risco}

In automated environments, it is essential to avoid incorrect interpretations:

- ✔️ Existing SBOM → visible composition  
- ❌ Existing SBOM ≠ secure image  
- ❌ SBOM without CVEs ≠ non-existent risk

Typical limitations include:
- undetected dependencies;
- static binaries;
- manually embedded components;
- differences between build environments.

For that reason, the SBOM must be used as a **technical input for analysis**, not as a conclusion.

---

## 📘 Recommended formats and tools {#-formatos-e-ferramentas-recomendadas}

| Format         | Supported tools                    | Technical observations                   |
|-----------------|--------------------------------------------|----------------------------------------|
| **CycloneDX**   | Syft, Trivy, Docker SBOM, GitHub          | Lightweight, extensible, suited to pipelines |
| **SPDX**        | SPDX tools, FOSSology                      | Common in formal audits        |
| **Syft JSON**   | Syft (`syft image:tag -o json`)            | Useful for custom validations      |

> 🌟 SbD-ToE recommendation: **CycloneDX JSON** as the base format for container image SBOMs.

---

## 🛠️ How to generate container SBOMs {#️-como-gerar-sboms-de-containers}

| Stage                | Technical example                                   | Operational notes                     |
|----------------------|--------------------------------------------------|----------------------------------------|
| Post-build generation    | `syft docker:app:tag -o cyclonedx-json`          | Must reflect the final image           |
| Alternative generation  | `trivy image --format cyclonedx image:tag`       | May enrich with CVEs               |
| CI/CD integration     | Mandatory step after build                      | Automatic execution                    |
| Versioning        | Artefact associated with the image digest          | Unambiguous correlation                  |

Automatic generation **does not eliminate** the need for human interpretation of the results.

---

## 📂 Storage, versioning and correlation {#-armazenamento-versionamento-e-correlação}

To ensure real traceability:

- Store the SBOM as a versioned artefact;
- Explicitly associate:
  - image (digest),
  - build,
  - pipeline;
- Reference the SBOM via labels or OCI metadata;
- Optionally sign the SBOM or link it to the image signature.

The absence of this correlation reduces the SBOM to an informational file with no auditable value.

---

## 🔍 Correct use of the SBOM {#-utilização-correta-do-sbom}

In SbD-ToE, the SBOM must be used to:

- Feed SCA scanners and analysis processes;
- Detect unexpected changes between builds;
- Support incident response;
- Justify acceptance or mitigation decisions.

It must not be used as:
- a seal of approval;
- a substitute for contextual analysis;
- proof of the absence of vulnerabilities.

---

## ✅ Good practices {#-boas-práticas}

- Generate the SBOM automatically after each build;
- Treat the SBOM as a versioned artefact;
- Review the SBOM after base image changes;
- Correlate the SBOM with signature and provenance;
- Use the SBOM as input to documented human decision;
- Review analysis criteria after relevant incidents.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                         | Relation to container SBOM              |
|----------------------------------|---------------------------------------------|
| `01-imagens-base.md`             | Approved images must have an associated SBOM  |
| `03-assinatura-cadeia-trust.md` | Link between integrity and composition      |
| `07-vulnerabilidades-imagens.md`| SCA analysis based on the SBOM                 |
| `09-riscos-processo-imagens.md` | SBOM as evidence, not decision            |
| `15-aplicacao-lifecycle.md`     | Operational integration into the lifecycle     |

> 🔍 The SBOM answers the question **“what is here?”**.  
> The question **“is this acceptable?”** still requires human analysis and decision.
