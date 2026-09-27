---
id: catalogo-requisitos-arquitetura
title: Secure Architecture Requirements Catalogue
description: Canonical catalogue of structural and design security requirements (ARC-001 to ARC-013), organised by risk level, with acceptance criteria for architecture reviews, ADRs and technical audits.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:arquitetura, ARC, rastreabilidade, L1, L2, L3, threat-modeling, zonas-de-confianca, ADR, auditoria]
sidebar_position: 1
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/addon/01-catalogo-requisitos.md
  source_sha256: 7fc2256006fb79e90297efc50bdf1fb40f1ed847e9c908f845f0165ea082a980
  source_commit: 8eb6a0aba53db254727866b9715b6a7e56eb7490
  target_sha256: 326d3c01881be87312a357d8b1cbd02b1eab3ec5c5cc4a3a09cc857a45ce8085
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, eu_ai_human_oversight, instrument, llm, mapping, papel_suporte, plain_rag, practitioner_manual, provenance, requirement_runtime, risk_level, sbdtoe_sbd, slug_threat_modeling, traceability, validation_evaluation]
  glossary_sha256: cf00413e875023ffb096c766604e683c34342f175b5f0331219e6a1e1b75dc76
  translated_at: 2026-09-27T19:34:16Z
  stamped_at: 2026-09-27T19:34:16Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Secure Architecture Requirements Catalogue

## Scope: structural and design requirements {#âmbito-requisitos-estruturais-e-de-design}

This catalogue covers **security requirements that apply to the design, documentation and review of the system's architecture** - the structural properties that must be guaranteed before and independently of implementation. They include: definition of trust zones, minimisation of the exposure surface, documentation of design decisions, integration of threat modelling into the architecture process, approved reusable patterns and versioning of diagrams.

For the complete mapping of all SbD-ToE requirements catalogues by technical domain, canonical prefix and owner, see [Ch. 02 - Catalogue Mapping](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

The requirements defined here are assessed in **architecture reviews**, in the approval of structural decisions and in technical audits - not in runtime tests nor in CI/CD pipelines.

> **On curation:** This catalogue was consolidated from recognised practices - NIST SSDF, OWASP SAMM, ISO/IEC 27001, threat modelling frameworks (STRIDE, PASTA) and secure architecture practices. It must be adapted to the organisational context and reviewed with each significant architecture cycle.

For project instantiation and the operational traceability nomenclature (`SEC-Lx-ARC-CODIGO`), see [Taxonomy and Traceability](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Conventions {#convenções}

| Symbol | Meaning |
|---------|-------------|
| ✔ | Mandatory requirement at this level |
| - | Not applicable or not mandatory at this level |

The levels are cumulative: L3 includes all L1 and L2 requirements; L2 includes all L1 requirements.

---

## ARC Catalogue - Secure Architecture {#catálogo-arc---arquitectura-segura}

Requirements that guarantee that the system is designed, documented and reviewed with structural controls proportional to its risk level.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| ARC-001 | Trust zones identified and documented | ✔ | ✔ | ✔ | Diagram with trust zones delimited, identified and justified; versioned in a repository; reviewed in the last architecture review. |
| ARC-002 | External exposure minimised and justified | ✔ | ✔ | ✔ | Inventory of externally exposed components; each exposure accompanied by a technical justification and an associated control (gateway, proxy, WAF, ACL). |
| ARC-003 | Security-focused architecture review | - | ✔ | ✔ | Formal review record (minutes, checklist or AppSec report) with date, participants and decisions; proportional to the application's risk level. |
| ARC-004 | Architecture decisions documented | - | ✔ | ✔ | ADR (Architecture Decision Record) or equivalent for each significant structural decision; fields: owner, date, alternatives considered and justification. |
| ARC-005 | Threat modelling integrated into critical flows | - | ✔ | ✔ | Threat modelling output available with identified threats, critical data flows covered and mitigations recorded; linked to the architecture diagram. |
| ARC-006 | Technical isolation controls between sensitive domains | ✔ | ✔ | ✔ | Evidence of active isolation between sensitive domains: network policies, logical firewalls or API segmentation; testable and auditable. The network filtering rules that protect the application (*security groups*, *network policies*, firewall and WAF rules) are defined as code, each justified, with an owner and approved; creation, change and removal are recorded; the rules are reviewed yearly at L1 and L2 and half-yearly at L3, and obsolete ones removed (cadence: the Manual's choice). The organisation's network firewall is out of scope. |
| ARC-007 | Reusable and approved architecture patterns | - | ✔ | ✔ | Repository of approved patterns with the date of last review; evidence of use of an approved pattern recorded in an architecture review. |
| ARC-008 | Data flows between trust zones protected | ✔ | ✔ | ✔ | Data flow diagram (DFD) with explicit controls at each trust boundary; updated and versioned. |
| ARC-009 | Significant changes trigger a new review | - | ✔ | ✔ | Documented process that defines the threshold of "significant change"; evidence of a review carried out after the last change that reached that threshold. |
| ARC-010 | Architecture diagrams versioned and accessible | ✔ | ✔ | ✔ | Diagram in the repository with version history; accessible to the relevant teams; reviewed at least annually or per significant release. |
| ARC-011 | Logical and physical segmentation between environments | - | - | ✔ | Evidence of network, permission and identity segregation between dev, staging and prod; documented and verifiable. |
| ARC-012 | Formal approval criteria for high-risk applications | - | - | ✔ | Formal approval checklist completed and signed by the security owner; approval record prior to deployment to production. |
| ARC-013 | Automatic topology validation in CI/CD or as code | - | - | ✔ | CI job with topology validation output (e.g. Cartography, diagrams-as-code, checkov for topology); execution logs available. |
| ARC-014 | Architectural patterns specific to systems with AI/ML components | - | ✔ | ✔ | Systems that integrate AI/ML components (LLMs, predictive models, RAG, autonomous agents) have dedicated architectural patterns: explicit trust boundaries between training data / model artefacts / inference endpoints / agentic tool invocations; input sanitisation and output filtering controls specific to direct and indirect prompt injection (LLM01-2025, `AML.T0051.001`); rate limiting and isolation of LLM calls; approval of agentic tool invocations with limited scope (`AML.T0086`); provenance of models and datasets documented (`AML.T0010`, LLM03-2025); the architecture considers model theft (ML05-2023) and training data poisoning (`AML.T0020`) scenarios; trust zones include AI components as distinct participants (not as opaque libraries). Minimum human oversight, proportionate to autonomy: the overseer can ignore or override the component's *output*, stop the component in a safe state or switch to a *fallback* without AI, and receives anomaly signals (degradation, *drift*, unexpected responses). In systems that generate or manipulate realistic images, video or audio: content-safety filters and classifiers on input and output, which block the generation of non-consensual intimate images of identifiable people and of child sexual abuse material; detected misuse is blocked, logged and corrected. |
| ARC-015 | AI agents operate as isolated *principals* with a mandate and least privilege | - | ✔ | ✔ | When the system includes autonomous agents that invoke *tools* (create a PR, read secrets, deploy, write to external systems), each agent is treated as a **distinct non-human principal**, with its own identity (ephemeral workload identity via OIDC), the minimum necessary *scope* per *tool* and per environment, and never reuses human credentials. At autonomy levels A2+ (see Ch. 02 — [autonomy levels](../../requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia)), the architecture additionally includes: (1) a structured **intent declaration** before each destructive *tool call*, recorded for audit ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)); (2) **out-of-band human approval** for actions with a destructive effect or on critical external systems (LLM06-2025 — Excessive Agency); (3) an **operational kill-switch** that revokes credentials and terminates sessions within seconds ([`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)); (4) a **complete audit per tool invocation** (timestamp, agent identity, scope, declared intent, actual action, outcome) integrated with the observability of Ch. 12 (`AML.M0024` AI Telemetry Logging). |

---

## Explanatory notes {#notas-explicativas}

- **ARC-003**: The review may be carried out with a structured checklist, an architecture peer review or an AppSec workshop; the format is proportional to the application's complexity.
- **ARC-005**: Threat modelling in this context is applied as an architecture review instrument - complementary to the autonomous threat modelling process described in Ch. 03.
- **ARC-009**: A "significant change" is defined as any change that affects trust boundaries, critical data flows, external exposure or documented isolation decisions.
- **ARC-011**: Applies both to network isolation (VLANs, namespaces, peering policies) and to identity isolation (IAM policies, distinct service accounts, no cross-env credentials).
- **ARC-013**: Example tools: validation of `.drawio` diagrams as code, Cartography for infrastructure graph analysis, or topology checks in Terraform/Pulumi pipelines.
- **Operational health in architecture**: For L2/L3 services, the architecture review must verify that critical runtime components have an observable health/readiness signal, or a native platform equivalent, represented in the operational monitoring model (`OPS-015`). The architectural concern is designability and exposure control; the operational obligation remains in `OPS-015`.

### Detailed note — ARC-014 {#arc-014}

AI/ML components introduce three classes of trust boundaries that do not exist in traditional architectures — (1) a **training-time boundary** between external datasets and the training pipeline (target of data poisoning); (2) an **inference-time boundary** between user input and the model's context (target of direct and indirect prompt injection); (3) an **agentic boundary** between the model's output and the tool invocations executed (target of exfiltration via AI agent tools, `AML.T0086`). The architecture must mark these boundaries explicitly in DFDs and define boundary controls proportional to risk. The associated threat modelling analysis uses MITRE ATLAS as a catalogue complementary to STRIDE (see Ch. 03 — [AI/ML Methodologies](../../threat-modeling/addon/metodologias-e-ferramentas#ai-ml)).
### Detailed note — ARC-015 {#arc-015}

ARC-014 covers *AI/ML components in general*; ARC-015 specialises in the case where those components **execute actions** with an effect on external systems via *tool invocation*. The difference matters because the attack surface is no longer just the model and comes to include the closed set of *tools* the agent can invoke, the identity with which it operates and the `agentic → tool` boundary (see Ch. 03 — [Agentic playbook](../../threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic)). The alignment with Zero Trust (NIST SP 800-207) is direct: the agent is one more non-human *principal* subject to the same principles of ephemeral identity, minimum *scope* and continuous audit applied to traditional *workload identities*. At A2+ an *intent declaration* and a *kill-switch* are additionally required — not as cosmetic controls, but as mechanisms that make visible and reversible what the agent has done in the real world.

---

> For validation criteria per requirement, method and responsible role, see the [Architectural Validation Plan](./validacao-arquitetural).
> For traceability between requirements, decisions and evidence, see [Architectural Traceability](./rastreabilidade-arquitetural).
> For the management of exceptions to these requirements, see [Exception Management](./excecoes).
