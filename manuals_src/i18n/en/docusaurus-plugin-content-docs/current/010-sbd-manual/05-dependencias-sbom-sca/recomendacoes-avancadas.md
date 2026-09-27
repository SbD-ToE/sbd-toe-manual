---
id: recomendacoes-avancadas
title: Advanced Practices - Dependency Management and Supply Chain
description: Reinforced recommendations for critical contexts or environments with high maturity
tags: [avancadas, maturidade, supply-chain, dependencias, sbom, sca]
sidebar_position: 30

translation:
  source_locale: pt
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/recomendacoes-avancadas.md
  source_sha256: 34f1d1a1702ab3e367e290c970fae105d7f5b5f9c03123427ba51b09f8e4cbe7
  source_commit: 036d74010f423f247be988e4a417375c74edb9d9
  target_sha256: 6a1a04b7a111639d6dc97ca46802f5c7f10a661904574cd740aa1479df78659b
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [audit_trail, avaliacao, deterministic, maturity, mirror_osf, provenance, traceability, transversal, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: f824039445774a69dc3aed2b27dc76e4a713573b2e2c47e0f4a409831ff84ea9
  translated_at: 2026-09-27T07:53:43Z
  stamped_at: 2026-09-27T07:53:43Z
  reviewed_by: null
---

# Advanced Practices - Dependency Management and Supply Chain

This annex presents reinforced security practices applicable to contexts with high maturity requirements, demanding regulatory compliance (e.g. NIS2, CRA, ISO 27001) or critical applications (e.g. finance, infrastructure, defence).

> 📌 These recommendations do not replace the main controls, but they significantly increase the visibility, reliability and resilience of the supply chain.

---

## 🔐 1. SBOM validation at runtime {#-1-validação-de-sbom-em-runtime}

- Integrate the SBOM as a verifiable artefact during execution (e.g. embedded as a container label, validation sidecar)
- Compare the runtime SBOM with the official image to detect drift
- Block execution if the binary contains unexpected libraries

> Tools: `tern`, `in-toto`, `Sigstore`, `Cosign`, `KubeClarity`

---

## 🧬 2. “Zero Unknowns” policy {#-2-política-zero-unknowns}

- **No transitive dependency may be unknown or uncatalogued**
- SBOMs must contain a `purl` or unique identifier per component
- Obsolete dependencies or those without a clear origin are blocked automatically

> Requires complete and up-to-date SBOMs + integration with internal repositories and CI policies

---

## 🧪 3. Deterministic sandboxing for build and SCA {#-3-sandboxing-determinístico-para-build-e-sca}

- Run the build and SCA analysis in a **sandboxed, immutable and auditable** environment
- Use a read-only file system and network isolation to prevent malicious scripts
- Control the hashes of the generated artefacts before deploy

> E.g. Docker containers with `--read-only`, `--no-new-privileges` and `seccomp`

---

## 🧰 4. Packaging and sealing of critical libraries {#-4-empacotamento-e-selagem-de-bibliotecas-críticas}

- Creation of internal bundles of libraries already verified and sealed
- Use of digital signatures (`cosign`, `gpg`) to guarantee integrity and origin
- Exposure via an internal private repository with a `promotion pipeline`

> Ideal for dependencies shared between teams or regulated projects

---

## 🧼 5. Systematic removal of unused code (dependency hygiene) {#-5-remoção-sistemática-de-código-não-utilizado-dependency-hygiene}

- Periodic checking for unused packages (e.g. `depcheck`, `pip-check`, `npm-prune`)
- Focus on reducing the attack surface associated with dead code
- Reverse approval process: everything that is not explicitly necessary is removed

> Critical practice in container images and serverless functions

---

## 📊 6. Maturity metrics for dependencies {#-6-métricas-de-maturidade-para-dependências}

- % of SCA findings resolved within the level SLA (Policy 19 §4.3)
- % of dependencies with a complete and versioned SBOM
- Average no. of dependencies per service / per image
- No. of active risk exceptions and associated expiry

> These metrics may be used for risk dashboards, internal SLAs and external audits

---
## 🧮 7. Analysis of the transitive dependency chain {#-7-análise-da-cadeia-transitiva-de-dependências}

- Assessment of the **complete behaviour of the dependency chain**, including post-install scripts, hooks and toolchains
- Use of scanners that assess `package.json`, `requirements.txt`, `setup.py`, `postinstall`, etc.
- Validation of packages that execute code on installation (e.g. `npm`, `pip`, `cargo`)

> Useful tools: `socket.dev`, `npm-lockfile-linter`, `PyUp`, `NodeSecure`, `Chain-bench`

---

## 🌐 8. Reputation and trusted origin of components {#-8-reputação-e-origem-confiável-de-componentes}

- Apply a **minimum reputation score** policy to public packages
- Only allow libraries with:
  - Multiple active maintainers
  - A public repository with signed releases
  - A history of regular updates
- Integration with scoring tools such as `OSSF Scorecard`, `deps.dev`, `libraries.io`

> Ideal for filtering out risks in little-used or unmaintained packages

---

## 🧱 9. Hardened fallback for external registries {#-9-fallback-hardened-para-registries-externos}

- Fallback to external repositories (e.g. `npmjs`, `PyPI`, `DockerHub`) **must be controlled and justified**
- Minimum requirements:
  - Signature or hash verification
  - Access only through an authenticated proxy
  - Justification of absence from the internal mirror

> This practice reduces the risk of *supply chain injection* during builds

---

## 🛰️ 10. Cross-validation of the SBOM with external threat intelligence {#️-10-validação-cruzada-de-sbom-com-threat-intelligence-externo}

- Enrich SBOMs with risk data from sources such as:
  - CISA KEV (Known Exploited Vulnerabilities)
  - OSV (Open Source Vulnerability)
  - VulnCheck, Risk Ledger, among others
- Automate blocking based on `exploit-in-the-wild` or `CVSS > threshold`
- Integrate enrichment into the CI/CD pipeline before build approval

> Increases the capacity for **proactive response to exploits in circulation**, complementing traditional SCA.

---

## 🧯 11. Blast radius analysis per critical dependency {#-11-análise-de-blast-radius-por-dependência-crítica}

- Identify libraries whose compromise would have a high organisational impact
- Calculate the blast radius on the basis of:
  - Cross-cutting use across services
  - Level of external exposure
  - Critical capabilities (e.g. auth, parsing, crypto)
- Apply reinforced measures:
  - Releases with staging + explicit approval
  - Multi-team verification
  - Forced priority update

> Makes it possible to manage risk not only by vulnerability, but by the **systemic impact of each dependency**.

## 🔗 Links to other reinforced practices {#-ligações-com-outras-práticas-reforçadas}

| Technical domain      | Related advanced recommendations                |
|----------------------|----------------------------------------------------|
| Containers           | Minimal images + embedded SBOM + isolated scanning |
| CI/CD                | Reproducible build + signature + provenance     |
| Requirements           | Bidirectional traceability + automated acceptance criteria |

---

> 🧭 These recommendations must be applied gradually and in proportion to the system's criticality. In L3 environments, at least 2 of these practices must be adopted as a high-maturity baseline.
