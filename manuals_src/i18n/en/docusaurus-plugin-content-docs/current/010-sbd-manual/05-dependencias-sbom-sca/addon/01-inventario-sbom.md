---
id: inventario-sbom
title: Dependency Inventory and SBOM
description: Generation and management of a Software Bill of Materials (SBOM) with traceability across the lifecycle
tags: [dependencias, sbom, sca, supply-chain]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/addon/01-inventario-sbom.md
  source_sha256: a64059f342fd8ba5b297c5dd8a3fd3ad3ba4bb17e0d4f4c24f4a8416d91f376b
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 5de402fff90792805a43de788293692cf8adf2dbe2b054bffb550f80c4600722
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [cycle_iteration, lifecycle_phase, mapping, normative_empirical, requirement_runtime, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: 5dadf32f80686776e144f0b9a113917971e2d7ee2a743961314ac413606c6db8
  translated_at: 2026-09-26T08:45:22Z
  stamped_at: 2026-09-26T18:33:45Z
  reviewed_by: null
---

# Dependency Inventory and SBOM

## 🌟 Objective {#-objetivo}

Guarantee that all applications have a **complete, traceable and versioned inventory** of the libraries and components used - known as an **SBOM (Software Bill of Materials)** - as a fundamental measure to:

- Mitigate third-party and supply chain risks;
- Accelerate the response to public vulnerabilities (e.g. CVE);
- Support compliance with standards and regulatory requirements (e.g. NIS2, CRA, EO 14028);
- Enable technical audits and impact analyses.

---

## 🧬 What an SBOM is {#-o-que-é-um-sbom}

An **SBOM** is a structured file that describes all the software components of a system, including:

- Package name and version
- Origin (repository, supplier)
- Licence
- Hashes/signatures
- Transitive dependencies
- Relationships (e.g. runtime, dev, optional)

> ⚠️ An SBOM **is not a lockfile** - it is a formal, standardised artefact that security tools can process.

---

## 📘 Supported formats {#-formatos-suportados}

| Format     | Description                                           | Compatible tools                   |
|-------------|-----------------------------------------------------|-------------------------------------------|
| **CycloneDX** | Lightweight, extensible and widely supported format    | Syft, Trivy, OWASP tools, GitHub, Snyk    |
| **SPDX**     | Normative format maintained by the Linux Foundation     | SPDX tools, FOSSology, Black Duck         |
| **SWID**     | Used in regulated environments (e.g. fed. gov.)        | Requires specialised tooling              |

> 🌟 Recommended by SbD-ToE: **CycloneDX**, in `JSON` or `XML` format, with support for multiple languages.

---

## 🛠️ How to generate SBOMs {#️-como-gerar-sboms}

| Stack / Language | Typical command                              | Notes                                       |
|-------------------|---------------------------------------------|---------------------------------------------|
| Node.js           | `syft . -o cyclonedx-json`                  | Includes `package.json` and transitive dependencies         |
| Java/Maven        | `cyclonedx-maven-plugin`                    | Output directly in the build (`target/`)          |
| Python            | `syft . -o cyclonedx-json`                  | Includes `requirements.txt`, `pipfile.lock`   |
| Docker/Containers | `syft docker:imagem:tag -o cyclonedx-json`  | Generates the SBOM of the complete image (base + app)   |
| C# (.NET)         | `cyclonedx-dotnet`                          | SBOM per `.csproj` project or `.sln`        |

> 💡 Suggestion: generate the SBOM **automatically on every build** as a versioned pipeline artefact.

---

## 📂 Where to store SBOMs {#-onde-armazenar-sboms}

- Dedicated directory in the repository: `/.sbom/`
- CI/CD artefact associated with the build (e.g. Azure Artifacts, GitHub Releases)
- SBOMs versioned in source control or external systems (Artifactory, Nexus, etc.)

---

## 🧬 Examples of fields in a CycloneDX SBOM {#-exemplos-de-campos-num-sbom-cyclonedx}

```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.5",
  "version": 1,
  "components": [
    {
      "type": "library",
      "name": "lodash",
      "version": "4.17.21",
      "purl": "pkg:npm/lodash@4.17.21",
      "hashes": [{ "alg": "SHA-256", "content": "..." }],
      "licenses": [{ "license": { "id": "MIT" } }]
    }
  ]
}
```

> Each component may be linked to CVEs, licence and metadata that support traceability and validation.

---

## ✅ Good practices {#-boas-práticas}

- Generate an SBOM **in every production build**
- Include **transitive** dependencies, not only direct ones
- Version and retain each SBOM alongside the corresponding artefact
- Automate the comparison of SBOMs between versions (detect the introduction of risk)
- Integrate the SBOM with SCA scanners and vulnerability management systems

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                   | Relationship with the SBOM                                 |
|-----------------------------|--------------------------------------------------|
| `02-analise-sca.md`         | Uses the SBOM as input for vulnerability analysis |
| `04-integracao-ci-cd.md`    | Integration of SBOM generation into the pipeline        |
| `08-rastreabilidade-vulnerabilidades.md` | Mapping between findings and SBOM components |

---

> 🔒 The SBOM is a **technical and documentary prerequisite** for effective risk detection, compliance with frameworks (SSDF, SLSA) and a swift response to security incidents.
