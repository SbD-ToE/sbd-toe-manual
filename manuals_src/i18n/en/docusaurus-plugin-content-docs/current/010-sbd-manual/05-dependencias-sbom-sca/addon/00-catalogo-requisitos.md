---
id: catalogo-requisitos-dependencias
title: Dependencies, SBOM and SCA Requirements Catalogue
description: Canonical catalogue of security requirements for the management of third-party dependencies (DEP-001 to DEP-010), with applicability by risk level and acceptance criteria for SBOM, SCA, library governance and update policies.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:dependencias, DEP, SBOM, SCA, supply-chain, rastreabilidade, L1, L2, L3, auditoria, CycloneDX, SPDX]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/addon/00-catalogo-requisitos.md
  source_sha256: aaea605a614c279b611a3da81fa95b39cf42eac0c406e1dff594015f382e5154
  source_commit: 62e6744cbd2001d8397d05f09a404fa2c18e3d61
  target_sha256: 0b6adba8b0412f6822a74cfc048187deb350ffd3fbe5aa6e73ca37407c2074d3
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [audit_trail, cycle_iteration, esquema_regime, framework_source_corpus, lifecycle_phase, mapping, mcp, plain_rag, practitioner_manual, provenance, requirement_runtime, risk_level, sbdtoe_sbd, traceability, verificacao_check, verification_taxonomy]
  glossary_sha256: e7ba97c1aa6ad5aceda3c6fc13a15a3a4be183c2b0fc6b9a8929cf71d8b88c14
  translated_at: 2026-09-27T14:19:07Z
  stamped_at: 2026-09-27T14:19:07Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Dependencies, SBOM and SCA Requirements Catalogue

## Scope: management of the software supply chain {#âmbito-gestão-da-cadeia-de-fornecimento-de-software}

This catalogue covers **security requirements that apply to the management of third-party dependencies** throughout the software lifecycle - from the selection and approval of libraries, through SBOM generation and vulnerability scanning, to update policies and the traceability of fixes.

Reliance on third-party libraries and components is one of the main risk surfaces in the software supply chain: vulnerable, abandoned or malicious components are established attack vectors (OWASP A06, Log4Shell, XZ Utils, etc.). These requirements establish the minimum controls so that this reliance is **known, governed and auditable**.

For the complete mapping of all SbD-ToE requirements catalogues by technical domain, canonical prefix and owner, see [Ch. 02 - Catalogue Mapping](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **On curation:** Consolidated from the OWASP Top 10 (A06 - Vulnerable Components), NIST SSDF (PS.3, PW.4), the SLSA Supply Chain Framework, the CISA SBOM Guidelines, Executive Order 14028 and good dependency management practices per stack. It must be adapted to the technological context and reviewed with each security policy update cycle.

For project instantiation and the operational nomenclature (`SEC-Lx-DEP-CODIGO`), see [Taxonomy and Traceability](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Conventions {#convenções}

| Symbol | Meaning |
|---------|-------------|
| ✔ | Mandatory requirement at this level |
| - | Not applicable or not mandatory at this level |

The levels are cumulative: L3 includes all L1 and L2 requirements; L2 includes all L1 requirements.

---

## DEP Catalogue - Dependencies, SBOM and SCA {#catálogo-dep---dependências-sbom-e-sca}

Requirements that guarantee that all third-party dependencies are known, analysed, governed and updated in proportion to risk.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| DEP-001 | SBOM generated per build, in a standardised format | ✔ | ✔ | ✔ | SBOM present and accessible for each build, in CycloneDX or SPDX format; includes direct and transitive dependencies; versioned artefact linked to the build that generated it. |
| DEP-002 | SCA integrated into the pipeline with blocking by severity policy | ✔ | ✔ | ✔ | SCA scanner active in CI/CD; documented severity policy; CVEs of critical or high severity block promotion; scan report available per run. |
| DEP-003 | Dependency versions pinned and auditable | ✔ | ✔ | ✔ | Lockfile present, versioned and up to date; no unversioned references (`*`, `latest`, unbounded ranges); integrity verifiable by hash (e.g. the `integrity` field in npm, `--hash` in pip). |
| DEP-004 | Prohibition of dependencies introduced by manual copying | ✔ | ✔ | ✔ | No third-party libraries copied directly into the repository outside the package manager; verifiable by a structure scan; documented process that explicitly prohibits it. |
| DEP-005 | Controlled registries and source repositories | - | ✔ | ✔ | List of permitted registries and repositories defined and enforced; downloads from unapproved sources blocked in the pipeline or by network policy; evidence of active enforcement. |
| DEP-006 | Formal approval for the introduction of new dependencies | - | ✔ | ✔ | Documented approval process for new libraries with minimum criteria: maintenance activity, compatible licence, no active CVEs, verified popularity; approval record available per dependency. |
| DEP-007 | Update policy with an SLA defined by severity | ✔ | ✔ | ✔ | Update SLA defined by CVE severity level (in line with Policy 19 §4.3: e.g. critical 30 / 7 / 3 days and high 90 / 30 / 15 days at L1 / L2 / L3; with an indication of active exploitation, the time limit is brought forward); evidence of compliance in the most recent cycles; exceptions formalised where applicable. |
| DEP-008 | Automated updates with impact analysis | - | ✔ | ✔ | Update bot active (e.g. Dependabot, Renovate); PRs generated automatically with semver impact information, changelogs and tests; human intervention mandatory for breaking changes; PRs not merged automatically without review. |
| DEP-009 | Detection of unintended or emergent dependencies | - | - | ✔ | Defined process to detect dependencies introduced via tooling, code generation, pipelines or runtime loading; inventory boundaries documented; deviations detected and handled. |
| DEP-010 | SBOM → vulnerability → fix traceability | - | ✔ | ✔ | Traceable evidence from the component identified in the SBOM to the associated CVE and to the action taken (fix PR, version update or formalised exception with justification and review date); sources of vulnerability information defined (public databases, supplier advisories, CSIRTs) and reviewed at planned intervals. |
| DEP-011 | Inventory and provenance of AI/ML dependencies | - | ✔ | ✔ | Systems with AI/ML components have a dedicated inventory of AI dependencies: (1) base models with version, artefact hash and source (model registry, fine-tuning provenance); (2) training and fine-tuning datasets with version, source and curation process; (3) MCP servers and tools exposed to agents with identifier, version and scope (`AML.T0110` AI Agent Tool Poisoning); (4) embedded prompts relevant to behaviour (system prompts, RAG templates) with version and owner. The inventory is generated per build and integrated into the main SBOM (DEP-001); upstream incidents in models, datasets or MCP servers (LLM03-2025 Supply Chain, `AML.T0010` AI Supply Chain Compromise) trigger the same triage process as DEP-002/DEP-007. |
| DEP-012 | AI BOM generated per *build* in a standardised format | - | ✔ | ✔ | The AI/ML inventory (DEP-011) is materialised as an **AI BOM** in a standardised format per *build* — CycloneDX 1.6 with the `ml-bom` extension (published in 2024) is preferred, or a recognised equivalent (`ML-BOM`, `AIBOM`). The AI BOM is a *build* artefact (not a separate analysis), versioned, and linked to the main SBOM. It includes models, datasets, MCP servers/tools and embedded prompts with *pinned* version, hash, *provider* and licence. |
| DEP-013 | Explicit *pinned* version for AI models and providers | - | ✔ | ✔ | AI models used in production or in a pipeline have an **explicit fixed version** — e.g. `claude-opus-4-7@sha:…` instead of `claude-latest`. Semver ranges, dynamic *aliases* (`latest`, `stable`) and unversioned references are **prohibited** in any environment that is not exploratory. A major version change by the provider requires a new *eval suite* (Ch. 10 §C5) and a review of the *threat model* (Ch. 03 US-11). Mitigates *AI Supply Chain Rug Pull* (`AML.T0109`). |
| DEP-014 | List of approved AI *providers* with risk classification | - | ✔ | ✔ | Providers of AI models (Anthropic, OpenAI, HuggingFace, the organisation's own self-hosted providers) used by the organisation are on an **approved list** with a risk classification and applicable contractual clauses (cross-link Ch. 14 — contracting of AI providers). Minimum approval criteria: zero retention for sensitive data where applicable; processing location compliant with GDPR Art. 44–49; contractually agreed audit; SLA for prior notification of version changes; declared compliance with AI Act Article 53 (and Article 55, if the model has systemic risk) if it supplies GPAI. The list is reviewed periodically according to the level of criticality. |

---

## Explanatory notes {#notas-explicativas}

- **DEP-001**: The SBOM must be generated as an artefact of the build process itself, not as a separate analysis. Reference tools: Syft, Trivy, CycloneDX Maven Plugin, OWASP Dependency Track.
- **DEP-002**: The severity policy must be explicit about what blocks vs. what only alerts. For L1, the minimum acceptable is blocking at critical severity; for L2/L3, high severity or above.
- **DEP-004**: This prohibition extends to Git submodules with third-party code, vendor directories without version control, and third-party binaries versioned directly.
- **DEP-006**: The approval criteria must include verification of the project's last update, the number of active maintainers and presence in databases of supply chain incidents (e.g. OpenSSF Scorecard, Socket.dev).
- **DEP-008**: Update automation must be configured with caution in high-risk environments: automatic updates of transitive dependencies or of critical security components must always require human review.
### Detailed note — DEP-011 {#dep-011}

AI/ML dependencies are not limited to packages via a package manager — they include **opaque artefacts** with a distinct attack surface. Three regimes of model consumption are distinguished, with different risk implications in the chain:

- **Base model via an external *provider*** (Anthropic, OpenAI, Google) — the most common case in 2026. The organisation has no copy of the weights; the risk is concentrated in the contract (Policy 33 §10) and in the detection of unannounced changes (`AML.T0109` *Supply Chain Rug Pull*).
- **Self-hosted *model*** (HuggingFace, vLLM, Ollama, *llama.cpp*) — the organisation holds the weights on its own infrastructure. A different risk: weights as a critical asset ([Ch. 09 §12 — *Self-hosted inference*](../../containers-imagens/addon/self-hosted-inference)); hash verification at *startup*; SCA over the *runtime*.
- **Internally *fine-tuned* model** — the organisation starts from a base model and adapts it with its own *dataset*. The resulting artefact is **simultaneously** an *upstream* dependency (base model) and an *internal artefact*. Implications: the *fine-tuned* model inherits the risks of the base (`DEP-013/014` apply), but also inherits the risks of the *fine-tuning dataset* (`AML.T0019` *poisoned datasets*); the *fine-tuned artefact* must enter the AI BOM ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012)) and be protected as an asset of the organisation (Ch. 09 §12). (1) **Models**: include the SHA-256 hash of the artefact, the model registry source (HuggingFace, Anthropic, OpenAI) and the version (e.g. `claude-sonnet-4-6@sha:…`); a typical attack is AI Supply Chain Rug Pull (`AML.T0109`) — a legitimate model replaced by a malicious variant via an update. (2) **Datasets**: track source, date obtained and hash; a typical attack is Publish Poisoned Datasets (`AML.T0019`) — contaminated public datasets. (3) **MCP servers and tools**: a typical attack is AI Agent Tool Poisoning (`AML.T0110`) — a legitimate MCP tool compromised to inject malicious context when invoked by the agent. (4) **Embedded prompts**: system prompts and RAG templates are operational code — changes require PR review like any other behavioural dependency. For the associated threat modelling analysis, see Ch. 03 §AI/ML; architectural controls for the isolation of agentic tool invocation are defined in Ch. 04 [ARC-014](../../arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014).
### Detailed note — DEP-012 {#dep-012}

The AI BOM is the materialisation of DEP-011 in a **standardised and portable format**. CycloneDX 1.6 with the `ml-bom` extension (published in 2024) is preferred because it preserves the structure of the main SBOM (DEP-001) and adds fields specific to AI components (models, datasets, considerations). Alternative schemas (the provider's proprietary format, an in-house `ML-BOM`) are acceptable provided that they cover the same fields and can be consumed by the organisation's governance *pipeline*.
### Detailed note — DEP-013 {#dep-013}

The "no `latest`" rule applies literally — *semver* ranges (`^4.x`, `>=4.0`), dynamic *aliases* and *channels* that update silently are a direct source of the `AML.T0109` class of incident (AI Supply Chain Rug Pull). The operational policy is symmetrical to the one that applies to code dependencies (DEP-003): a fixed and auditable version. The difference is that with AI models the *same version* may behave differently depending on incremental *fine-tunes* the provider may apply — hence the need for cross-checking against the eval suite (Ch. 10 §C5) whenever the version changes.
### Detailed note — DEP-014 {#dep-014}

Approving an AI provider is not merely a technical decision — it involves contractual clauses that `grc` / `compliance` validates (data retention, training opt-out, location, audit rights, AI Act Art. 53/55 where applicable). The approved list lives in VCS in the organisation's governance repository, alongside the list of DEP-005 registries. Operational cross-link: Policy 33 (Secure Contracting) §Annex AI Providers; Ch. 14 US "Contracting of AI providers".

---

> For inventory and SBOM generation, see [Dependency Inventory and SBOM](./inventario-sbom).
> For vulnerability analysis and the SCA process, see [SCA Analysis](./analise-sca).
> For the governance of third-party libraries and the approval process, see [Library Governance](./governanca-libs-terceiros).
> For update policies and SLAs, see [Update Policy](./politica-atualizacoes).
> For exception management and risk acceptance, see [Exceptions and Risk Acceptance](./excecoes-e-aceitacao-risco).
