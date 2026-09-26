---
id: policy-dependencias
title: Dependency Management Policy
description: Organisational policy that defines the criteria for approving, pinning, blocking, auditing and updating external dependencies in software projects, proportional to the application's criticality level (L1, L2, L3), with a focus on reducing supply chain risk and ensuring traceability.
tags: [policy, dependências, SCA, supply chain, CVE, licenças, pinning, SBOM, cap05, L1, L2, L3, governance]
grupo: supply-chain
sidebar_position: 10
translation:
  source_locale: pt
  source_path: 020-assets/policies/10_policy-dependencias.md
  source_sha256: 54f62e0b2e37e709afe8f857a9370f4ae2bf57baee8047f60da302f6e0407764
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 27d4af420b2ec346d06bf4caad08109c3a691b6aa3b9b58acf297e8548f39f76
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [framework_source_corpus, llm, mcp, mirror_osf, provenance, requirement_runtime, risk_level, role_tech_lead, sbdtoe_sbd, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 052afe4201bb7845b32e009aa3b254cfdb16b45b4b61f9aab43bcc31b8ab7ef9
  translated_at: 2026-09-26T14:10:48Z
  stamped_at: 2026-09-26T18:36:49Z
  reviewed_by: null
---

# Dependency Management Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for the **secure management of external dependencies** in software projects developed or operated by the organisation.

Every external dependency is an extension of the application's attack surface. Third-party components can introduce known vulnerabilities, incompatible licences, unverified origins or abandoned code. Without a formal management policy, dependencies accumulate without audit, CVEs spread silently and supply chain risk grows invisibly.

The objective of this policy is to ensure that:

- Every dependency introduced is approved, with a validated origin and a verified licence
- Dependencies with active CVEs are managed with severity criteria proportional to the risk level
- The dependency inventory is kept up to date and traceable per build
- Dependency updates are monitored and managed in a controlled way
- Local libraries (copied outside a package manager) are prohibited without a formal exception

---

## 2. Scope {#2-âmbito}

This policy applies to all projects with third-party code, regardless of language or runtime, including:

- Direct dependencies declared in manifest files (`package.json`, `requirements.txt`, `pom.xml`, `go.mod`, etc.)
- Transitive dependencies included through direct dependencies
- Libraries copied locally outside a package manager (`.js`, `.jar`, `.dll`, `.php` files, etc.)
- Container base images (also covered by the Secure Containers Policy)

---

## 3. Dependency approval criteria {#3-critérios-de-aprovação-de-dependências}

### 3.1 Mandatory validation per new dependency {#31-validação-obrigatória-por-dependência-nova}

Before any new dependency is included in an L2/L3 project, a formal validation must be carried out covering the following criteria:

| Criterion | Description |
|---|---|
| **Origin and provenance** | Public reference repository (PyPI, npm, Maven Central, etc.) or approved internal repository |
| **Active maintenance** | Project under active maintenance; no signs of abandonment in the last 12 months |
| **Compatible licence** | Licence compatible with the organisation's licence policy (`licenses-whitelist.yaml`) |
| **Known CVEs** | No critical or high CVEs without mitigation; medium CVEs assessed in context |
| **Popularity and reputation** | Signs of wide adoption and a track record of responding to vulnerabilities |
| **Minimal scope** | The dependency solves the problem without introducing excessive, unneeded functionality |

### 3.2 Approval record {#32-registo-de-aprovação}

The approval of each new dependency must be recorded in `dependencies-approval.md`, with:

- [ ] Name, version and source repository
- [ ] Technical justification of the need
- [ ] Result of the licence validation
- [ ] Result of the CVE verification at the date of approval
- [ ] Person responsible for the approval, and date

### 3.3 Proportionality {#33-proporcionalidade}

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Formal approval of new dependencies | Recommended | Mandatory | Mandatory |
| Licence validation | Recommended | Mandatory | Mandatory |
| Record in `dependencies-approval.md` | Optional | Mandatory | Mandatory |
| Validation by AppSec Engineer | Not applicable | Recommended | Mandatory |

---

## 4. Version pinning {#4-pinning-de-versões}

### 4.1 Applicability {#41-obrigatoriedade}

All dependencies must be fixed to specific versions (pinning) so as to ensure build reproducibility and avoid the unintended introduction of changes:

| Level | Pinning requirement |
|---|---|
| L1 | Recommended; at least a lock file generated and versioned |
| L2 | Mandatory; exact version in the manifest or lock file versioned in the repository |
| L3 | Mandatory; exact version and integrity hash whenever the ecosystem supports it |

### 4.2 Lock files {#42-lock-files}

- The lock file (`package-lock.json`, `poetry.lock`, `Pipfile.lock`, `go.sum`, etc.) must be versioned in the repository and never generated ad hoc in CI environments
- Changes to the lock file must be reviewed as part of code review

---

## 5. Prohibition of local libraries {#5-proibição-de-bibliotecas-locais}

Copying libraries directly into the repository (outside a package manager) is **prohibited** without an approved formal exception. This includes:

- `.js`, `.min.js` files copied into `vendor/`, `static/` or equivalent
- `.jar`, `.dll`, `.so`, `.dylib` archives included directly in the repository
- `.php` library files copied directly

:::warning
The presence of local libraries prevents automatic detection of CVEs by SCA, breaks provenance traceability and makes update management impossible. Detection of local libraries not declared in the package manager must be automated in the pipeline (`.audit-libs.json`/`.audit-libs.yaml`) and block the build at L2/L3.
:::

When local inclusion is technically unavoidable, it must be formalised as an exception under the terms of the Security Exception Management Policy, with:

- [ ] Technical justification
- [ ] Integrity hash of the included file
- [ ] CVEs verified manually
- [ ] Exception TTL and replacement plan

---

## 6. Blocking of direct external sources {#6-bloqueio-de-fontes-externas-diretas}

At L2/L3, dependencies must not be resolved directly from the internet at build time. The pipeline must:

- [ ] Use an internal repository (proxy/mirror) as the sole resolution source
- [ ] Block direct access to public repositories during the build (where technically feasible)
- [ ] Verify package integrity by hash before installation

The internal repository configuration must be recorded in `repo-config.yaml` and reviewed periodically.

---

## 7. SCA - Software composition analysis {#7-sca---análise-de-composição-de-software}

### 7.1 Integration into the pipeline {#71-integração-no-pipeline}

The CI/CD pipeline must include automatic SCA analysis in every build, covering direct and transitive dependencies:

| Level | SCA requirement |
|---|---|
| L1 | Alert; does not block |
| L2 | Blocks High and Critical findings without an approved exception |
| L3 | Blocks Medium, High and Critical findings without an approved exception |

### 7.2 Reference tools {#72-ferramentas-de-referência}

Accepted tools for SCA: OWASP Dependency-Check, Trivy, Grype, Snyk, or an equivalent with NVD/OSV support.

### 7.3 Evidence artefact {#73-artefacto-de-evidência}

The SCA report (`sca-report.html` or JSON) must be archived as a pipeline artefact with a reference to the commit, under the terms of the Traceability Policy.

---

## 8. Vulnerability alerts in production {#8-alertas-de-vulnerabilidades-em-produção}

For systems in production, there must be a mechanism for correlating the SBOM of the deployed version with CVEs published after the deploy:

- [ ] Inventory of deployed components per service and environment (`inventario-runtime-<servico>-<ambiente>.json`)
- [ ] Integration with a vulnerability feed (NVD, OSV, GitHub Advisory Database)
- [ ] Alert generated when a CVE affects a deployed version, with component, version, environment and severity
- [ ] Response SLA defined per severity (see CVE Exceptions Policy)

---

## 9. Periodic audit {#9-auditoria-periódica}

Regardless of the build gates, dependencies must be audited periodically:

| Level | Minimum cadence |
|---|---|
| L1 | Half-yearly or with each major release |
| L2 | Quarterly or with each major release |
| L3 | Monthly or with each release |

The audit must cover:
- [ ] Dependencies not in active use (may be removed)
- [ ] Versions significantly out of date compared with the latest stable version
- [ ] CVEs published since the last audit
- [ ] Licences that changed in the most recent versions
- [ ] Existing local libraries with exception status

---

## 10. Artefacts {#10-artefactos}

| Artefact | Description | Retention |
|---|---|---|
| `dependencies-approval.md` | Dependency approval record | While the dependency is in use |
| `sbom.json` / `sbom.xml` | Inventory per build (CycloneDX/SPDX) | See SBOM Policy |
| `sca-report.html` / JSON | Vulnerability report per build | 90 days (L2), 1 year (L3) |
| `inventario-runtime-*.json` | Deployed components per service/environment | While the deploy is active |
| `repo-config.yaml` | Internal repository configuration | Active version in the repository |
| `.audit-libs.json` | Audit results for local libs | Per release |
| `licenses-whitelist.yaml` | List of licences approved by the organisation | Active version in the repository |

---

## 11. Responsibilities {#11-responsabilidades}

| Role | Responsibility |
|---|---|
| Developer | Identify and submit new dependencies for approval; keep lock files up to date |
| Tech Lead | Validate the need for and scope of new dependencies; lead the periodic audit |
| AppSec Engineer | Approve dependencies at L3; configure and calibrate SCA; manage the licence policy |
| DevOps / SRE | Maintain the internal package repository; configure SCA gates in the pipeline; monitor alerts in production |
| GRC / Compliance | Verify SCA coverage; audit approval records; issue compliance reports |

---

## 12. Annex — AI providers as a supply dependency {#12-anexo--provedores-ai-como-dependência-de-fornecimento}

AI models consumed via an external *provider* (Anthropic, OpenAI, Google, Mistral, Cohere, etc.) or *self-hosted* (HuggingFace, vLLM, Ollama) are **supply dependencies** with particular characteristics — the version can change behaviour without changing a visible tag, the artefact is opaque, and the typical attack has a name of its own (`AML.T0109` Supply Chain Rug Pull). The following apply here:

- **Approval criteria** (section 3 extended): *data retention*, *training opt-out*, processing location (GDPR Art. 44–49 where applicable), AI Act Art. 53/55 (when GPAI), the SLA for notification of version changes and contractually agreed *audit rights* are additionally assessed.
- **Version pinning** (section 4 extended): `latest`/range/dynamic alias is prohibited for AI models; cross-link `DEP-013`.
- **Extended SCA** (section 7 extended): for AI components an AI BOM (CycloneDX 1.6 `ml-bom`) generated per *build* is used — see [Policy 11 §AI BOM](./policy-sbom) and [Policy 39 — AI BOM and Supply Chain](./policy-ai-bom-supply-chain).
- **Response to *upstream* incidents**: same triage as in section 8, extended with the classes `AML.T0010` / `AML.T0019` / `AML.T0109` / `AML.T0110` and LLM03-2025.

The detailed operationalisation of these points lives in [Policy 39 — AI BOM and Supply Chain](./policy-ai-bom-supply-chain). This policy remains the reference for the general case; Policy 39 specialises in the AI slice.

---

## 13. Review and audit of this policy {#13-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Incident originating in an undetected vulnerable dependency
- Significant change in the package manager ecosystem used
- Regulatory change with an impact on software supply chain management
- *Upstream* incident in the AI supply chain with operational impact (any class in section 12)

---

## 14. Normative and technical references {#14-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 05 - Dependencies, SBOM and SCA | Inventory, SCA, alerts, artefacts, user stories; **US-14 AI BOM**; `DEP-011..014` |
| SbD-ToE Ch. 07 - Secure CI/CD | SCA integration into the pipeline and gates |
| SbD-ToE Ch. 09 - Containers and Images | Dependencies in base images |
| SBOM Policy (`11_policy-sbom.md`) | Generation and retention of SBOM per build; **AI BOM annex** |
| AI BOM Policy (`39_policy-ai-bom-supply-chain.md`) | Specific handling of models, datasets, MCP, prompts |
| CVE Exceptions Policy (`12_policy-excecoes-cve.md`) | Management of CVEs with no fix available |
| OWASP Dependency-Check | Reference SCA tool |
| CycloneDX / SPDX | SBOM formats (including CycloneDX 1.6 `ml-bom` for AI) |
| MITRE ATLAS | Adversarial tactics/techniques for the AI supply chain |
| OWASP Top 10 for LLM Applications (2025) — LLM03 Supply Chain | Dedicated vector |
| NIST SP 800-161 | Cybersecurity Supply Chain Risk Management |
| NIST AI RMF 1.0 — MAP-4.x (third-party AI) | Risk mapping of third-party AI |
| SSDF PW.4 | Reuse of existing, well-secured software |
| SLSA (Supply chain Levels for Software Artifacts) | Supply chain integrity framework |
| EU AI Act (Reg. (EU) 2024/1689) — Art. 25, 53, 55 | When applicable to AI / GPAI providers |
