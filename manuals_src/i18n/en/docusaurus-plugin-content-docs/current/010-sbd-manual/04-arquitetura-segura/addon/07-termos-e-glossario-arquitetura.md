---
id: termos-e-glossario-arquitetura
title: Operational Glossary
description: Terms used in Chapter 04 with operational definitions and associated artefacts
tags: [tipo:addon, tema:arquitetura, jargao, rastreabilidade, ADR, threat-modeling, trust-boundaries]
sidebar_position: 7
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/addon/07-termos-e-glossario-arquitetura.md
  source_sha256: 0531dae951ef77b5034fa792ef95b2c67e64475196a5538a62ba7501ae9d9389
  source_commit: 777d9e091c59c017d479b1ec53ba153c809a6d1f
  target_sha256: eed545638db182941124453db96cbe531773461fcba53bfbfe3e24ac3f6918ee
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [chapter_role, maturity, provenance, requirement_runtime, sbdtoe_sbd, slug_threat_modeling, threat, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: c0c17aed6075e176582da152e44c92de5e55d011c8e7ee64b6b92fb29aedb60a
  translated_at: 2026-09-27T15:08:32Z
  stamped_at: 2026-09-27T15:08:32Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

> This **operational glossary** normalises the vocabulary used in Ch. 04 and in its artefacts    
> **Objective:** to guarantee that critical terms have a single meaning, a clear application and a link to evidence.

---

## 🧭 Context: Architecture as a practice, not as a job title {#-contexto-arquitetura-como-prática-não-como-cargo}

Not every team that applies SbD-ToE has a formal *Architect* role.  
In many projects, **architecture “happens” naturally** - in the decisions taken during the design and implementation of the software.  
Chapter 4 starts from this principle: there is no need to institute a heavyweight process or a governance body; it is enough to **make explicit and traceable the technical decisions that already exist**.
To do so, a common taxonomy must be adopted, one that allows information and knowledge to be shared and thus applied in the activities embedded in this chapter.

- **Secure architecture is a collective practice.**  
  Any technical decision that affects security, scalability or dependencies is, in practice, an architectural decision - even when taken by a developer.

- **The objective is to capture reasoning, not to create bureaucracy.**  
  An *Architecture Decision Record* (ADR), an architecture sheet or a *trust boundary* are merely mechanisms for keeping the technical “why” of the choices made.

- **Formality grows with risk.**  
  SbD-ToE does not impose a format; it defines proportionality:  
  - *L1*: simple records in Markdown or tickets.  
  - *L2*: full traceability (decision ↔ requirement ↔ control).  
  - *L3*: formal process with independent review.

- **Designing with awareness is designing securely.**  
  The chapter does not create new documentation, but helps to turn implicit design into **verifiable security evidence**.

> 💬 In short: *Security by Design* is not about designing more - it is about designing consciously, and ensuring the production of evidence and a way of keeping the knowledge.

---


## 📘 General Conventions {#convencoes-gerais}
- **Architecture requirement**: identifier from the chapter's catalogue, in the form `ARC-001` to `ARC-015`.  
- **AuthN / AuthZ**: Authentication / Authorisation.  
- **L1–L3**: levels of **application criticality** (not organisational maturity).  
- **Artefact**: versioned document or evidence (Markdown, issue, ticket, CI/CD export).  
- **Traceability**: verifiable link between requirements, decisions, controls and evidence.

## 📚 Core Terms (Definition → Where to apply → Artefacts) {#termos-nucleo}

| Term | Operational Definition | Where to apply | Artefacts / Evidence |
|---|---|---|---|
| **ADR (Architecture Decision Record)** | Record of a relevant architectural decision, including context, alternatives, decision, security impact and traceability. | Whenever there is a decision with an impact on security, risk, cost of change or critical dependencies. | `adr/ADR-xxxx.md` (or the “Decisions” section in `solution-architecture.md`), AppSec *review*. |
| **Trust Boundary** | Explicit delimitation where the level of trust changes between components/services, teams or third parties. | Internal/external integrations, multitenancy, exposed interfaces. | `trust-boundaries.md`, `integration-review.md`, annotated C4/DFD diagrams. |
| **Living Architecture** | Set of *triggers* and routines that keep the documentation and controls synchronised with reality (avoiding *drift*). | After defined events (see “Triggers”). | `arquitetura-triggers.md`, update commits/PRs, *review* notes. |
| **Architectural Drift** | Divergence between the documented design and the actual implementation at runtime/in the pipeline. | Rapid changes, *hotfixes*, infrastructure changes, *feature flags*. | Misalignment issues, diffs in the diagrams, CI/CD validation *logs*. |
| **Architectural Exception** | Approved deviation from an architecture requirement, with a compensating control and a deadline. | When cost/time makes immediate compliance unfeasible without compromising baseline security. | `excecao-arquitetural.md`, decision and deadline, risk *owner*, periodic *review*. |
| **Compensating Control** | Alternative measure that reduces risk when the primary control is not possible. | In exceptions, *workarounds*, transitional phases. | Compensation plan, *evidence logs*, monitoring. |
| **TM ↔ Architecture Synchronisation** | Consistent updating between the **threat model** (Ch. 03) and the architecture decisions/diagrams. | Before significant *builds*, after a new ADR/integration. | `tm-sync-arquitetura.md`, threat → control → architecture requirement links. |
| **Architecture Sheet** | Solution document with decisions, *rationale* and the security controls applied. | In each project/epic/macro-feature with structural impact. | `solution-architecture.md`, annexes with controls, links to ADRs/diagrams. |
| **Architecture Checklist (Go-live)** | Final checklist of the controls and the approved exceptions. | Release *gate*. | `checklist-arquitetura.md`, QA/AppSec/Architect sign-offs. |
| ***Triggers** | Events that require an architectural review. | See the “Architecture review triggers” table. | `arquitetura-triggers.md`, update *tasks*, PRs. |
| **Provenance** | Ability to prove the origin/integrity of *artefacts* (code, *builds*), aligned with *supply chain* good practice. | Pipelines, dependencies, images. | CI/CD, SBOM records, signatures, logs. |

## 🗺️ Architecture review triggers  {#️-triggers-de-revisão-de-arquitetura}
| Trigger | Minimum action | Evidence |
|---|---|---|
| New integration (internal/third party) | Review *trust boundaries*, update the sheet and the threat model | `integration-review.md`, `tm-sync-arquitetura.md` |
| Change to sensitive data (type, volume, flow) | Review classification, encryption, retention | Update of `solution-architecture.md` and DFD/C4 |
| Infrastructure/pipeline change | Review dependencies and compensating control | Pipeline PR, validation *logs* |
| Relevant architectural decision | Create/update the ADR and the L1–L3 impacts | `adr/ADR-xxxx.md` |
| Incident or *near-miss* | Feed back into the controls, adjust the design | RCA, *post-mortem*, update of controls |
| Emerging threat (*threat intel*) | Review coverage and prioritisation | `tm-sync-arquitetura.md` |

## 🧩 Quick map: architecture requirement → Practice/Artefact {#-mapa-rápido-requisito-de-arquitectura--práticaartefacto}

| ARC-ID | Associated practice | Expected artefact |
|---|---|---|
| **ARC-004 - Architecture decisions documented** | ADR per structural decision with an impact on security or dependencies | `adr/ADR-xxxx.md`, decisions section in `solution-architecture.md` |
| **ARC-005 - Threat modelling in critical flows** | TM workshop; threat→control→ARC synchronisation | Annotated DFD, `tm-sync-arquitetura.md`, threat register |
| **ARC-006 - Isolation between sensitive domains** | Network policies; logical segmentation; ACLs; *admission control* | Annotated C4 diagram, network configuration, AppSec *review* |
| **ARC-008 - Data flows between zones protected** | DFD with explicit controls at each trust boundary | `trust-boundaries.md`, DFD versioned in the repository |

## 🔄 How to use this jargon in User Stories  {#-como-usar-este-jargão-nas-user-stories}
- **US-08 (ADR)**: accept as valid an ADR in Markdown, a *wiki* or an *issue*, provided there is context → decision → impact → traceability (architecture requirement).  
- **US-09 (Trust Boundaries)**: require an *integration inventory* and a trust matrix; point to AuthN/AuthZ/TLS/segregation.  
- **US-10 (TM ↔ Architecture)**: guarantee the threat → control → architecture requirement link in the artefacts.  
- **US-11 (Exceptions)**: include deadline, compensating control, *owner* and periodic *review*.  
- **US-12 (Living Architecture)**: publish the list of triggers and evidence their execution when they occur.

## 🧭 Proportionality L1–L3 (application of the jargon)  {#-proporcionalidade-l1l3-aplicação-do-jargão}
- **L1**: Simplified records (key decisions, critical integrations, lightweight *checklist*), with trust zones, flows between zones and the controls at each boundary in a versioned diagram.  
- **L2**: ADRs for significant decisions; complete *trust boundaries*; TM synchronisation; formal exceptions.  
- **L3**: Full coverage, independent *reviews*, validations in CI/CD, automation of triggers where possible.

## 🔗 Useful Internal Links  {#-ligações-internas-úteis}
- Ch. 01 - Risk Management: `/sbd-toe/sbd-manual/01-classificacao-aplicacoes/intro`  
- Ch. 02 - Security Requirements: `/sbd-toe/sbd-manual/02-requisitos-seguranca/intro`  
- Ch. 03 - Threat Modelling: `/sbd-toe/sbd-manual/03-threat-modeling/intro`  
- Ch. 04 - Secure Architecture (*lifecycle* file): `/sbd-toe/sbd-manual/04-arquitetura-segura/aplicacao-lifecycle`
