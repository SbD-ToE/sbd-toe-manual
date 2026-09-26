---
id: policy-sbom
title: SBOM (Software Bill of Materials) Policy
description: Organisational policy that defines the requirements for the generation, format, signing, provenance, archiving and retention of SBOMs (Software Bill of Materials) in software, container and IaC builds, proportional to the application's criticality level (L1, L2, L3).
tags: [policy, SBOM, CycloneDX, SPDX, proveniência, assinatura, supply chain, cap05, cap07, cap09, L1, L2, L3, governance, rastreabilidade]
grupo: supply-chain
sidebar_position: 11
translation:
  source_locale: pt
  source_path: 020-assets/policies/11_policy-sbom.md
  source_sha256: 631f9813e06fc1271bbe81180e3cde02209e749da70151e4e903bda5141049fd
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 5df25a609f264685d56481b71a15a66d9e6ef3004106747aaad103aacb65853d
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bc04ded428e40ee1c214f8535dfb1904655b64166d0aa82b5df521e4230b8cb0
  glossary_keys: [discipline, framework_source_corpus, layer, mcp, practitioner_manual, provenance, requirement_runtime, sbdtoe_sbd, traceability, verification_taxonomy]
  glossary_sha256: 608fda23f09da0191c67baa652ce1bad59a11272de681623218ac821f4e239f2
  translated_at: 2026-09-26T14:10:48Z
  reviewed_by: null
---

# SBOM (Software Bill of Materials) Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for the **generation, signing, archiving and retention of Software Bills of Materials (SBOM)** in all software builds produced or operated by the organisation.

An SBOM is the complete and verifiable inventory of the components that make up a software artefact - direct and transitive dependencies, versions, licences and hashes. Without an SBOM, responding to a CVE requires manual research, supply chain auditing is speculative and demonstrating regulatory compliance becomes impossible.

The objective of this policy is to ensure that:

- Each build produces a complete SBOM, in a standardised format, signed and traceable
- The SBOM is associated with the artefact it inventories and is verifiable before the deploy
- The inventory of components in production can be correlated with build SBOMs
- SBOMs are retained according to the defined periods and are accessible for audit

---

## 2. Scope {#2-âmbito}

This policy applies to all builds that produce artefacts intended for test, pre-production or production environments, including:

- Software artefacts (binaries, packages, JARs, wheels, npm packages, etc.)
- Container images (Docker/OCI)
- IaC artefacts when they include third-party dependencies (Terraform modules, Helm charts, etc.)

---

## 3. Format and minimum content {#3-formato-e-conteúdo-mínimo}

### 3.1 Accepted formats {#31-formatos-aceites}

| Format | Minimum version | Notes |
|---|---|---|
| **CycloneDX** | 1.4 | Preferred format; native support in Trivy, Syft, cdxgen |
| **SPDX** | 2.3 | Accepted; interoperable with audit tools |

SBOMs must be produced in JSON or XML format. Proprietary formats are not accepted as substitutes.

### 3.2 Mandatory minimum content {#32-conteúdo-mínimo-obrigatório}

- [ ] Artefact metadata: name, version, build hash (SHA-256 or stronger)
- [ ] Reference to the commit SHA that gave rise to the build
- [ ] Complete list of direct and transitive components with name, version and hash
- [ ] Licence of each component (when available)
- [ ] Dependency relationships between components
- [ ] Generation timestamp and pipeline identifier

### 3.3 Additional mandatory content at L3 {#33-conteúdo-adicional-obrigatório-em-l3}

- [ ] Complete provenance: who built it, when, from which commit, in which pipeline
- [ ] Cryptographic signature of the SBOM (see section 5)
- [ ] Pipeline attestation (SLSA-like) associated with the SBOM

---

## 4. Mandatory generation {#4-obrigatoriedade-de-geração}

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| SBOM generated in every build | Mandatory (basic) | Mandatory (complete) | Mandatory (complete + signed) |
| SBOM includes transitive dependencies | Recommended | Mandatory | Mandatory |
| SBOM associated with the release artefact | Recommended | Mandatory | Mandatory |
| SBOM for container images | Recommended | Mandatory | Mandatory |
| SBOM archived as a pipeline artefact | Recommended | Mandatory | Mandatory |

Generation of the SBOM must be automated in the pipeline - manual or ad hoc generation is not acceptable as a substitute for the build SBOM.

---

## 5. Signing and integrity verification {#5-assinatura-e-verificação-de-integridade}

### 5.1 Signing of the SBOM {#51-assinatura-do-sbom}

At L2 and L3, the SBOM must be signed with a centrally managed key:

- [ ] SBOM signed with a private key managed by DevOps/SRE (e.g. Cosign, GPG)
- [ ] Public verification key published and accessible
- [ ] Key rotation procedure documented and executed periodically
- [ ] Signature stored alongside the SBOM or in the artefact registry

### 5.2 Verification before the deploy {#52-verificação-antes-do-deploy}

At L2 and L3, the deploy pipeline must verify the signature of the SBOM and of the artefact before proceeding with promotion:

- [ ] Signature verification job executed before the deploy
- [ ] Deploy blocked if the signature is missing or invalid (L3: mandatory; L2: recommended)
- [ ] Verification result recorded in the pipeline log

---

## 6. Provenance {#6-proveniência}

The SBOM must be accompanied by provenance metadata that make it possible to answer:

- **Who built it**: identity of the CI system (not of an individual person)
- **When**: timestamp to the second, in UTC
- **From what**: commit SHA, repository, release branch/tag
- **How**: pipeline, job and version of the build tools used

At L3, provenance must be recorded in `attestation-<build>.json` in SLSA format or equivalent, signed and archived with the SBOM.

---

## 7. Inventory in production {#7-inventário-em-produção}

The build SBOM is not sufficient to ensure complete visibility in production. An **inventory of the components actually deployed** per service and environment must be maintained:

- [ ] `inventario-runtime-<servico>-<ambiente>.json` generated and updated with each deploy
- [ ] Correlation between the build SBOM and the runtime inventory for drift detection
- [ ] Alerts configured when a published CVE affects a component present in the runtime inventory

The runtime inventory is the basis for correlating post-deploy CVE alerts (see the Dependency Management Policy and the CVE Exceptions Policy).

---

## 8. Archiving and retention {#8-arquivamento-e-retenção}

### 8.1 Location {#81-localização}

SBOMs must be archived as CI/CD pipeline artefacts or in a dedicated evidence repository, with appropriate access control:

- They must not be stored only locally on the build machine
- They must be accessible for audit without depending on ephemeral environments

### 8.2 Minimum retention periods {#82-prazos-de-retenção-mínimos}

| Artefact | L1 | L2 | L3 |
|---|---|---|---|
| SBOM per build | Per release | 1 year | 2 years |
| SBOM of the version in production (active) | While in production | While in production | While in production |
| Provenance attestation | Per release | 1 year | 2 years |

:::note
In regulated contexts (DORA, NIS2, healthcare, finance), retention periods may be longer. The applicable regulatory requirements always prevail.
:::

---

## 9. Reference tools {#9-ferramentas-de-referência}

| Tool | Main use |
|---|---|
| **Syft** | SBOM generation from images, file systems, packages |
| **Trivy** | SBOM generation + integrated SCA |
| **cdxgen** | CycloneDX SBOM generation per ecosystem |
| **Cosign** | Signing and verification of images and SBOMs |
| **SLSA** | Build provenance and integrity framework |
| **Grype** | SCA analysis over an existing SBOM |

The organisation may adopt alternative tools provided they support the CycloneDX or SPDX formats and allow verifiable signing.

---

## 10. Responsibilities {#10-responsabilidades}

| Role | Responsibility |
|---|---|
| Developer | Ensure that the dependency manifest is up to date and complete before the build |
| DevOps / SRE | Integrate SBOM generation into the pipeline; manage signing keys; configure archiving and retention |
| AppSec Engineer | Define content and format requirements; verify completeness in audits; calibrate CVE alerts |
| GRC / Compliance | Verify compliance with retention periods; make SBOMs available in audits |

---

## 11. Annex — AI BOM (Bill of Materials for AI components) {#11-anexo--ai-bom-bill-of-materials-para-componentes-ai}

When the system includes AI components — models, datasets, MCP servers/tools, embedded prompts — an **AI BOM** is generated in a standardised format per *build*, linked to the main SBOM. It is not a separate inventory kept in parallel; it is an extension of the main SBOM with its own fields for the opaque components of the AI supply chain.

### 11.1 Preferred format {#111-formato-preferido}

**CycloneDX 1.6 with the `ml-bom` extension** (published in 2024 by OWASP). Recognised alternatives: SPDX 3.0 AI Profile; the *provider*'s proprietary formats when they can be consumed by the organisation's governance *pipeline*.

### 11.2 Minimum content {#112-conteúdo-mínimo}

In addition to the fields common to all components:

- **Models**: `model_id`, `version` (fixed), `sha256`, `provider`, `capabilities`, `license`, `provenance`
- **Datasets**: `dataset_id`, `version`, `source`, `hash`, `curation_process`
- **MCP servers/tools**: `server_id`, `version`, `scopes`, `source`, `audit_log_sink`
- **Embedded prompts**: `prompt_id`, `version` (commit SHA), `owner`, type (`system|rag|skill`)
- **Providers**: list with `name`, `risk_classification`, `contract_ref`, critical clauses

### 11.3 Applicability {#113-obrigatoriedade}

| Level | AI BOM generation | Notes |
|---|---|---|
| L1 | Recommended | Simple format acceptable |
| L2 | Mandatory | Standard format (CycloneDX 1.6 `ml-bom` preferred) |
| L3 | Mandatory + GRC review | Contractual clauses detailed in the `providers` field; cross-link with the AI Act cross-check where applicable |

### 11.4 Detailed operation {#114-operação-detalhada}

The complete operation of the AI BOM — generation, *pinning*, list of approved *providers*, response to *upstream* incidents — lives in [Policy 39 — AI BOM and Supply Chain](./policy-ai-bom-supply-chain). This policy remains the reference for the SBOM discipline in general; Policy 39 specialises in the AI slice.

> 📌 In short: the SBOM covers what comes from the *package manager*; the AI BOM covers what comes from *model registries*, *dataset hubs* and MCP servers. Equivalent discipline, compatible format, coherent process.

---

## 12. Review and audit of this policy {#12-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Publication of a new major version of the CycloneDX or SPDX format
- Publication of a new version of the CycloneDX `ml-bom` specification or the SPDX AI Profile
- Regulatory change imposing additional SBOM requirements (e.g. EU Cyber Resilience Act, EU AI Act Art. 25)
- Incident originating in a component that was not inventoried (SBOM or AI BOM)

---

## 13. Normative and technical references {#13-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 05 - Dependencies, SBOM and SCA | Generation, correlation with SCA, runtime inventory; **DEP-012 AI BOM**; **US-14** |
| SbD-ToE Ch. 07 - Secure CI/CD | SBOM integration into the build and release pipeline |
| SbD-ToE Ch. 09 - Containers and Images | SBOM per image layer |
| Dependency Management Policy (`10_policy-dependencias.md`) | Approval and traceability of components; AI Providers annex |
| AI BOM Policy (`39_policy-ai-bom-supply-chain.md`) | Specific handling of models, datasets, MCP, prompts |
| Traceability Policy (`06_policy-rastreabilidade.md`) | Archiving and retention of build artefacts |
| CycloneDX 1.6 `ml-bom` (OWASP, 2024) | Preferred format for AI BOM |
| SPDX 3.0 AI Profile | Alternative format for AI BOM |
| CycloneDX Specification | Preferred SBOM format |
| SPDX Specification (SPDX 2.3) | Accepted alternative SBOM format |
| SLSA Framework | Build provenance and integrity |
| NIST SP 800-161 | Supply Chain Risk Management |
| EU Cyber Resilience Act | SBOM requirements for products with digital elements |
| SSDF PW.8 | Archive and protect each software release |
