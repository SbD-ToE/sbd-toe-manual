---
id: policy-ai-bom-supply-chain
title: AI BOM and Model Supply Chain Policy
description: Organisational policy that defines the treatment of AI models, datasets, MCP servers/tools, embedded prompts and AI providers as an auditable supply chain — AI BOM generation per build in a standardised format (CycloneDX 1.6 ml-bom), version pinning, a list of approved providers and response to upstream incidents, complementing Policy 10 (dependencies) and Policy 11 (SBOM), proportionate to the criticality level (L1, L2, L3).
tags: [policy, AI, BOM, AI-BOM, supply-chain, CycloneDX, ml-bom, providers, modelos, datasets, MCP, pinning, AML, L1, L2, L3, governance, cap05]
grupo: supply-chain
sidebar_position: 39
translation:
  source_locale: pt
  source_path: 020-assets/policies/39_policy-ai-bom-supply-chain.md
  source_sha256: 18030447820ce432ddf952f5afb5d22ca384a0f8610a4b2e77ff652e03e209a5
  source_commit: b8ce768a94df0281215156c8358b55b7d012b568
  target_sha256: 8167bcf21df4bbc4bd45c17aa1b854542819f898f5a23c055b7e23b0a18f24e0
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [ai_service_vendor, audit_trail, avaliacao, cycle_iteration, esquema_regime, lifecycle_phase, llm, mcp, plain_rag, requirement_runtime, risk_level, role_tech_lead, sbdtoe_sbd, schema]
  glossary_sha256: f807e448de3465bd2d9d97a90c9450cc28e528f2c1d2f571ec97146ddfd83565
  translated_at: 2026-09-27T09:05:47Z
  stamped_at: 2026-09-27T09:05:47Z
  reviewed_by: null
---

# AI BOM and Model Supply Chain Policy

## 1. Objective {#1-objetivo}

This policy defines how **AI models**, **datasets**, **MCP servers/tools** and **embedded prompts** are treated as an auditable supply chain — with a versioned inventory, a standardised format (preferably CycloneDX 1.6 `ml-bom`), a fixed version per *build*, a list of approved AI service vendors, and a process for responding to *upstream* incidents.

It operationalises requirements [`DEP-011`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011), [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012), [`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013) and [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) of Ch. 05 and complements [Policy 10 — Dependencies](./policy-dependencias) (*AI service vendors* annex) and [Policy 11 — SBOM](./policy-sbom) (*AI BOM* annex). It exists as a standalone policy — rather than as a section of one of the former — because its lifecycle and risks are distinct enough to justify their own treatment, in the same way that NIST separates the AI RMF from the CSF.

## 2. Scope {#2-âmbito}

This policy applies to **any system** that uses AI components in development, *staging* or production, including:

- AI models consumed via an external AI service vendor (Anthropic, OpenAI, Google, Mistral, Cohere) or *self-hosted* (HuggingFace, vLLM, Ollama)
- Datasets used for *training*, *fine-tuning* or evaluation
- MCP servers / *tools* / *plugins* invoked by agents
- *Prompts* embedded in the product (system prompts, RAG templates, *skill files*)

Out of scope:
- AI models used in a purely exploratory mode, outside any release pipeline (these follow Policy 16)
- Traditional *machine learning* libraries without an embedded trained model (these fall under Policy 10 / Policy 11)

## 3. Fundamental principle: AI is supply chain {#3-princípio-fundamental-ai-é-supply-chain}

Everything learnt over the last fifteen years about the software supply chain applies to AI dependencies — with specialisation. *Pinned* version, auditable hash, approved AI service vendor, visible update mechanism, a plan for responding to *upstream* incidents. The difference is that the *attack vectors* have different names (`AML.T0019` Publish Poisoned Datasets, `AML.T0109` Supply Chain Rug Pull, `AML.T0110` AI Agent Tool Poisoning) and the artefacts are opaque (`npm audit` cannot be run against a model).

:::warning
Operating in production with an AI model referenced by `latest` (or by a range, or by a dynamic alias) is the equivalent of operating with `npm install` without a *lockfile* — only with a larger impact surface and a shorter detection window. This practice is prohibited at any criticality level.
:::

## 4. AI BOM — format and minimum content {#4-ai-bom--formato-e-conteúdo-mínimo}

| Field | Description | Notes |
|---|---|---|
| `format` | Serialisation format | CycloneDX 1.6 with the `ml-bom` extension (published in 2024) is preferred. Alternatives: SPDX 3.0 AI extension; proprietary AI service vendor formats when consumable by the governance *pipeline* |
| `components` | List of AI components | Each component with `type`, `name`, `version` (fixed), `hash`, `provider`, `license`, `provenance` |
| `models` | AI models subset | Includes `model_id` (e.g. `claude-opus-4-7`), `version` (e.g. `@2026-05-20`), `sha256`, `provider`, `capabilities` |
| `datasets` | Datasets subset | Includes `dataset_id`, `version`, `source`, `hash`, `curation_process` |
| `mcp_tools` | MCP servers/tools subset | Includes `server_id`, `version`, `scopes`, `source`, `audit_log_sink` |
| `prompts` | Embedded prompts subset | Includes `prompt_id`, `version` (commit SHA), `owner`, `system|rag|skill` |
| `providers` | AI service vendors used | Each one with `name`, `risk_classification` (L1/L2/L3), `contract_ref` |
| `build_ref` | Reference to the *build* | Link to the main SBOM and to the *release* |

## 5. Version *pinning* — operational rules {#5-version-pinning--regras-operacionais}

- **AI models**: an explicit fixed version with a hash when the AI service vendor exposes one — e.g. `claude-opus-4-7@2026-05-20#sha:…`. Semver ranges, dynamic *aliases* (`latest`, `stable`, `production`) and unversioned references are **prohibited** in any environment other than exploratory ([`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013)).
- **Datasets**: an immutable version, or a snapshot referenced by hash. Continuously evolving datasets require a snapshot per *release*.
- **MCP servers/tools**: a fixed version of the npm/pip/binary package. Tools discovered dynamically at runtime are only accepted at A0-A1 and outside production.
- **Prompts**: version = commit SHA of the repository where they live.

A major version change in any of these requires:
1. A new *eval suite* (Ch. 10 §C5)
2. A revised *threat model* (Ch. 03 US-11)
3. Approval by `appsec` (L2) or `appsec` + `grc` (L3) before the *cutover*

## 6. List of approved AI service vendors {#6-lista-de-providers-ai-aprovados}

The organisation maintains in VCS a **versioned list of approved AI service vendors** with, at a minimum:

- `name` · `service` · `model_families`
- `risk_classification` (L1/L2/L3 or its own criterion)
- `contract_ref` (reference to the contract in force; see Ch. 14)
- Declared critical clauses: *data retention*, *training opt-out*, *location*, *audit rights*, *notification of breaking changes*
- Declared compliance: AI Act Article 53 (and Article 55, if the model has systemic risk) when GPAI; GDPR Art. 28 + 44–49 (when personal data)
- `effective_until` — no "forever" approvals

Adding an AI service vendor requires: technical assessment (`appsec`) + contractual review (`grc` + Legal) + approval proportionate to the risk level. Removing an AI service vendor from the list requires a documented migration plan when the AI service vendor is in operational use.

## 7. Response to *upstream* incidents {#7-resposta-a-incidentes-upstream}

The same IR *runbooks* used for CVEs in dependencies apply to incidents in the AI supply chain — with adaptations per class:

| Incident class | Examples | Minimum action |
|---|---|---|
| **Compromised model / *rug pull*** (`AML.T0109`) | AI service vendor distributes a malicious version of the model; an unannounced *fine-tune* degrades security | Rollback to the previous *pinned* version; review of outputs from the affected period; communication to the *owner* of the affected systems |
| **Poisoned dataset** (`AML.T0019`) | Public dataset contaminated by *training-time poisoning* | Re-train / re-fine-tune without the affected dataset; full *eval* before a new *cutover* |
| **Compromised MCP server / tool** (`AML.T0110`) | A legitimate tool injects malicious context when invoked | Remove the *tool* from the `tools_allowlist` of the affected *mandates* (Policy 38); review of the *audit trail* of *tool invocations* (Ch. 12 OPS-012) for the suspect period; *kill-switch* for the agents that used it |
| ***Provider*** *outage / breaking change* | AI service vendor deprecates a version without notice; SLA breached | Activate the *fallback* declared in the architecture (Ch. 04 §AI/ML); assess a change of AI service vendor via a formal exception (Policy 05) |

## 8. Proportionality by criticality level {#8-proporcionalidade-por-nível-de-criticidade}

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| AI BOM generated per *build* (DEP-012) | Recommended | Mandatory | Mandatory |
| Explicit *pinned* version (DEP-013) | Mandatory | Mandatory | Mandatory |
| List of approved AI service vendors (DEP-014) | Recommended | Mandatory | Mandatory + GRC review |
| Detailed contractual clauses | Recommended | Mandatory | Mandatory + Legal review |
| *Eval suite* mandatory on a major version change | Recommended | Mandatory | Mandatory |
| Periodic review of the AI service vendor list | Annual | Half-yearly | Quarterly |

## 9. Responsibilities {#9-responsabilidades}

| Role | Responsibility |
|---|---|
| **AppSec Engineer** | Define the AI BOM schema; approve the inclusion of models/datasets/MCP servers; technical assessment of new AI service vendors |
| **DevOps / SRE** | Configure AI BOM generation in the *pipeline*; maintain the CI *gate* that validates *pinning*; archive BOMs per release |
| **GRC / Compliance / Legal** | Assess contractual clauses; approve the addition of L2/L3 AI service vendors; regulatory compliance (AI Act, GDPR) |
| **Tech Lead / Software Architect** | Identify which AI components are *load-bearing* in the system; declare AI dependencies in the design |
| **Auditors** | Verify the conformity of the AI service vendor list with the actual contractual clauses; trace *upstream* incidents in the published BOMs |

## 10. Anti-patterns {#10-anti-padrões}

- ❌ `model: latest` in any non-exploratory environment — violates DEP-013 and opens the door to `AML.T0109`.
- ❌ AI BOM in a proprietary format that the governance *pipeline* cannot read — the portability that is the value of the BOM is lost.
- ❌ AI service vendor in use without an entry in the approved list — *shadow AI*; operational incident.
- ❌ Major version change without a new *eval* or *threat review* — the evidence that supported the declared level of autonomy is lost.
- ❌ "Public" dataset used without a snapshot — typical `AML.T0019` attack (dataset altered between use and audit).
- ❌ AI service vendor list that grows but never shrinks — discontinued AI service vendors accumulate as contractual *cruft*.

## 11. Exception management {#11-gestão-de-excepções}

Exceptions to this policy follow the formal process of Ch. 14 and of [Policy 05 — Exception Management](./policy-gestao-excecoes):

- Use of a non-*pinned* version in a non-exploratory environment requires an exception with TTL ≤ 30 days.
- Use of an AI service vendor outside the approved list requires an exception with TTL ≤ 14 days and `appsec` + `grc` approval.
- Recurring exceptions (>2 on the same AI service vendor in 12 months) require the formal inclusion of the AI service vendor in the list or its replacement.

## 12. Review and audit of this policy {#12-revisão-e-auditoria-desta-política}

This policy must be **reviewed half-yearly** given the rapid evolution of the ecosystem of AI models and AI service vendors, or after any of the following events:

- Incident in the AI supply chain (any class in section 7)
- Publication of a new version of the CycloneDX `ml-bom` or SPDX AI specification
- Applicable regulatory change (AI Act, NIS2, DORA) with an impact on the AI supply chain
- Change in the contractual clauses of an AI service vendor in operational use

## 13. Normative and technical references {#13-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 05 (`DEP-011..014`) | Requirements for AI inventory + AI BOM + pinning + AI service vendors |
| SbD-ToE Ch. 05 — US-14 (AI BOM) | Operationalisation |
| SbD-ToE Ch. 03 §AI/ML | Threat library applicable to the AI supply chain (`AML.T0010`, `AML.T0019`, `AML.T0109`, `AML.T0110`) |
| SbD-ToE Ch. 04 ([`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)) | AI/ML architectural patterns (origin of the inventoried components) |
| SbD-ToE Ch. 14 — Contracting of AI providers | Detailed contractual clauses |
| Policy 10 — Dependencies (AI service vendors annex) | Operational coupling |
| Policy 11 — SBOM (AI BOM annex) | Format coherence |
| Policy 33 — Secure Contracting (AI service vendors annex) | Contractual clauses |
| Policy 38 — AI Agent Mandates | AI *tools* consumed by agents |
| CycloneDX 1.6 `ml-bom` (OWASP, 2024) | Preferred format |
| SPDX 3.0 AI Profile | Alternative format |
| MITRE ATLAS | Catalogue of adversarial tactics/techniques for the AI supply chain |
| OWASP Top 10 for LLM Applications (2025) — LLM03 Supply Chain | Dedicated vector |
| OWASP MCP Top 10 (2025) | Applicable when MCP servers/tools enter the AI BOM as a dependency — *tool poisoning* has a dedicated catalogue |
| NIST AI RMF 1.0 — MAP-4.x (third-party AI) | Third-party risk mapping |
| NIST SP 800-218A | SSDF Profile for GenAI |
| EU AI Act (Regulation (EU) 2024/1689) — Article 53 (GPAI; Article 55 if the model has systemic risk), Art. 25 (responsibilities along the AI value chain) | When applicable |
