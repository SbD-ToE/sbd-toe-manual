---
id: policy-arquitetura-segura
title: Secure Architecture Policy
description: Organisational policy that defines the requirements for applying secure architecture principles throughout the lifecycle of applications classified L2 and L3, including baseline definition, management of architecture decisions (ADR), review of trust boundaries, integration with threat modelling and formal approval requirements.
tags: [policy, arquitetura, ADR, trust boundaries, solution-architecture, padrões, cap04, L2, L3, governance, design]
grupo: design-analise
sidebar_position: 9
translation:
  source_locale: pt
  source_path: 020-assets/policies/09_policy-arquitetura-segura.md
  source_sha256: 47a6a3f72cb7663d231bd7f953e283d4832e1da0e2b0f69059768c2d84f01c03
  source_commit: 32978973a6e4e01d6abcfe36fb0e33a8192cb20d
  target_sha256: b9b654e28f9ac37a33d9c4139e8d0a2bf4d1d7d52c2f8a4098324edf5c237370
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [cycle_iteration, lifecycle_phase, requirement_runtime, role_tech_lead, sbdtoe_sbd, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 78233c3946ccd27e8c8124db05e2c58f170d75b66e73da40e5de0359a56b532e
  translated_at: 2026-09-27T15:08:14Z
  stamped_at: 2026-09-27T15:08:14Z
  reviewed_by: null
---

# Secure Architecture Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for the systematic application of **secure architecture** throughout the lifecycle of applications classified as L2 or L3.

Secure architecture is not a document - it is a set of deliberate technical decisions, documented, approved and kept up to date. Without an explicit architectural baseline, the controls applied lack a structural foundation, design risks go unnoticed, and traceability between threats, requirements and implementation becomes impossible.

The objective of this policy is to ensure that:

- The secure architecture baseline is defined at kick-off and kept up to date throughout the lifecycle
- Relevant architecture decisions are recorded with alternatives, trade-offs and security impact (ADR)
- Trust boundaries and data flows are identified, documented and controlled
- The catalogue of secure architecture patterns is versioned, approved and reusable
- The architecture is synchronised with the threat model and with the applicable security requirements

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

| Level | Applicability |
|---|---|
| L1 | Optional; recommended for systems with external exposure or critical logic |
| L2 | Mandatory; baseline, ADRs and trust boundary review |
| L3 | Mandatory; with independent review, formal approval and a gate in the pipeline |

---

## 3. Secure architecture principles {#3-princípios-de-arquitetura-segura}

The organisational secure architecture baseline must incorporate the following fundamental principles:

| Principle | Description |
|---|---|
| **Isolation** | Components with different trust levels must be isolated; access between zones controlled and minimal |
| **Exposure minimisation** | No component, service or data item may have greater exposure than its function requires |
| **Explicit trust boundaries** | All trust boundaries must be identified, documented and associated with controls |
| **Defence in depth** | Security controls in multiple layers; the failure of one control does not compromise the system |
| **Fail secure** | In the event of failure, the default behaviour must be the most restrictive, not the most permissive |
| **Dependency management** | External dependencies must be inventoried, assessed and monitored as risk vectors |
| **Secure observability** | Logs, metrics and traces are architectural components - they must be planned, not added after the fact |
| **Artefact immutability** | Production artefacts must be immutable; changes imply a new build and a new promotion |

---

## 4. Baseline and mandatory documentation {#4-baseline-e-documentação-obrigatória}

### 4.1 Start of a project or significant epic {#41-arranque-de-projeto-ou-épico-significativo}

At the start of each L2/L3 project (or of a relevant structural epic), the following minimum set of artefacts must be produced and approved:

| Artefact | Minimum content | Applicability |
|---|---|---|
| `principios-arquitetura.md` | Applicable principles, justified deviations, version and approval | L2/L3 |
| `solution-architecture.md` | Trust boundaries, data flows, external exposure, architectural controls, link to requirements and threats | L2/L3 |
| `trust-boundaries.md` | Inventory of trust boundaries, flows between zones, controls per boundary | L2/L3 |

### 4.2 Minimum content of the solution sheet {#42-conteúdo-mínimo-da-ficha-de-solução}

- [ ] Trust boundaries and data flows (including telemetry, logs and metrics) identified
- [ ] External exposure justified and minimised
- [ ] Explicit architectural controls per component or zone
- [ ] Link to applicable security requirements (`REQ-*`)
- [ ] Link to the threat model (`threat-model-*`) when available
- [ ] Version, date and person responsible for preparing it
- [ ] Formal approval recorded

---

## 5. Management of architecture decisions (ADR) {#5-gestão-de-decisões-arquiteturais-adr}

### 5.1 When to record an ADR {#51-quando-registar-uma-adr}

An ADR must be created whenever an architecture decision has a security impact, including:

| Trigger | Examples |
|---|---|
| New technology or critical component | Choice of message broker, database, runtime |
| Change to the authentication or authorisation model | Migration to OAuth2, addition of MFA, change of session model |
| Surface exposure decision | Opening of a public endpoint, new external integration |
| Adoption or abandonment of an architecture pattern | Migration from monolith to microservices, adoption of a service mesh |
| Deliberate deviation from a baseline principle | Accepting additional exposure due to a technical constraint |

### 5.2 Minimum content of an ADR {#52-conteúdo-mínimo-de-uma-adr}

- [ ] Unique identifier (`ADR-XXXX`)
- [ ] Context and problem to be solved
- [ ] Alternatives considered, with trade-offs
- [ ] Decision taken and justification
- [ ] Security impact (explicit, even if none)
- [ ] Link to relevant threats in the threat model
- [ ] Link to affected security requirements
- [ ] Review by AppSec Engineer (L2/L3)
- [ ] Status: Proposed / Accepted / Superseded / Revoked

### 5.3 Proportionality {#53-proporcionalidade}

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| ADR for decisions with security impact | Optional | Mandatory | Mandatory |
| ADR review by AppSec | Recommended | Mandatory | Mandatory |
| ADR referenced in the commit or PR | Recommended | Mandatory | Mandatory |

---

## 6. Trust boundaries and integrations {#6-trust-boundaries-e-integrações}

### 6.1 Inventory of trust boundaries {#61-inventário-de-trust-boundaries}

Each L2/L3 application must maintain an up-to-date inventory of its trust boundaries, including:

- [ ] Identification of each trust boundary (e.g. user-to-app, app-to-db, app-to-external-api)
- [ ] Data flows that cross each boundary
- [ ] Control applied at each boundary (authentication, authorisation, validation, encryption)
- [ ] Trust level of each party involved
- [ ] Integration with the threat model (trust boundaries mapped in the DFD)

### 6.2 Review upon new integration {#62-revisão-por-nova-integração}

Whenever a new external integration or a new trust boundary is added, an `integration-review.md` must be produced with:

- [ ] Identification of the external system and the trust level assigned
- [ ] Data flows involved and classification of the data
- [ ] Controls applied to the integration
- [ ] Change to the threat model (if applicable)
- [ ] Formal approval before promotion to production

---

## 7. Update upon architectural change {#7-atualização-por-alteração-arquitetural}

The architecture document must be updated **before promotion to production** whenever a significant change occurs:

- [ ] Significant change identified and documented in `architecture-update.md`
- [ ] Affected artefacts (`solution-architecture.md`, `trust-boundaries.md`) updated
- [ ] ADR created if the decision warrants it
- [ ] Threat model updated if the change introduces new surfaces or flows
- [ ] New version formally approved
- [ ] Link to the commit or PR that gave rise to the change

:::warning
Architectural changes not reflected in the documentation and in the threat model are treated as a deviation from this policy. The CI/CD pipeline must check consistency between relevant code changes and the update of the architecture artefacts at L2/L3.
:::

---

## 8. Catalogue of secure architecture patterns {#8-catálogo-de-padrões-de-arquitetura-segura}

The organisation maintains a **versioned catalogue of secure architecture patterns** (`modelos-referencia.md` or equivalent), which serves as a reusable reference for new projects and design decisions.

Each pattern in the catalogue must include:

- [ ] Architecture diagram with trust boundaries
- [ ] Key decisions and justification
- [ ] Security requirements applicable to the pattern
- [ ] Threats mitigated by the pattern
- [ ] Verifiable implementation checklist
- [ ] Formal approval (Architecture + AppSec)
- [ ] Change history (changelog)

Reusing a pattern without verification of its suitability for the specific context does not relieve the team of the responsibility to validate the applicable controls.

---

## 9. Formal approval {#9-aprovação-formal}

| Artefact | Level | Minimum approval required |
|---|---|---|
| `principios-arquitetura.md` (initial) | L2 | Software Architect + AppSec Engineer |
| `principios-arquitetura.md` (initial) | L3 | Software Architect + AppSec Engineer + independent review |
| `solution-architecture.md` | L2 | Software Architect + AppSec Engineer |
| `solution-architecture.md` | L3 | Software Architect + AppSec Engineer + independent review |
| ADR with security impact | L2/L3 | AppSec Engineer |
| `integration-review.md` | L2/L3 | Software Architect + AppSec Engineer |

---

## 10. Integration with threat modelling {#10-integração-com-threat-modeling}

Secure architecture and threat modelling are synchronised bidirectionally:

- The architecture diagram (`solution-architecture.md`, `trust-boundaries.md`) is the basis for the DFD of the threat model
- Architectural changes must trigger an update of the threat model when they introduce new surfaces, flows or trust boundaries
- ADRs with security impact must reference the relevant threats in the model
- Threats identified in threat modelling must be reflected in architectural decisions and controls

---

## 11. Gate in the CI/CD pipeline {#11-gate-no-pipeline-cicd}

| Gate | L1 | L2 | L3 |
|---|---|---|---|
| Verification that `solution-architecture.md` exists | Not applicable | Recommended | Mandatory |
| Verification of ADR for PRs with architectural impact | Not applicable | Recommended | Mandatory |
| Block if the architecture is out of date without an approved justification | Not applicable | Recommended | Mandatory |

The gate must be configured by DevOps/SRE, in coordination with the AppSec Engineer, and calibrated so as not to block changes that have no relevant architectural impact.

---

## 12. Proportionality by level {#12-proporcionalidade-por-nível}

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Documented architecture baseline | Mandatory | Mandatory | Mandatory |
| `solution-architecture.md` approved | Recommended | Mandatory | Mandatory |
| ADR for decisions with security impact | Optional | Mandatory | Mandatory |
| Inventory of trust boundaries | Mandatory | Mandatory | Mandatory |
| `integration-review.md` per new integration | Recommended | Mandatory | Mandatory |
| Independent review | Not applicable | Recommended | Mandatory |
| Consistency gate in the CI/CD pipeline | Not applicable | Recommended | Mandatory |
| Reusable pattern catalogue | Optional | Mandatory | Mandatory |

---

## 13. Responsibilities {#13-responsabilidades}

| Role | Responsibility |
|---|---|
| Software Architect | Define and maintain the baseline; produce solution sheets and ADRs; update upon relevant change |
| AppSec Engineer | Review and approve architecture artefacts; verify alignment with the threat model and requirements |
| Tech Lead / Developer | Identify changes with architectural impact; reference ADRs in the relevant PRs |
| DevOps / SRE | Configure the consistency gate in the pipeline; ensure storage of and access control over the artefacts |
| GRC / Compliance | Verify that all L2/L3 applications have up-to-date and approved artefacts |

---

## 14. Review and audit of this policy {#14-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Incident originating in an undocumented or unapproved architecture decision
- Significant change to the organisation's reference principles
- Update of the adopted secure architecture methodologies or frameworks

---

## 15. Normative and technical references {#15-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 04 - Secure Architecture | Principles, user stories, artefacts, application across the lifecycle |
| SbD-ToE Ch. 03 - Threat Modelling | DFD ↔ trust boundaries ↔ threat model synchronisation |
| SbD-ToE Ch. 02 - Security Requirements | ADR and solution → requirements link (`REQ-*`) |
| SbD-ToE Ch. 07 - Secure CI/CD | Architectural consistency gate in the pipeline |
| NIST SP 800-160 | Systems Security Engineering - integration of security into design |
| NIST SP 800-207 | Zero Trust Architecture |
| TOGAF / SABSA | Enterprise architecture frameworks with a security dimension |
| OWASP Application Security Architecture Cheat Sheet | Secure architecture patterns for applications |
| ISO/IEC 27001 - Clause 8.1 | Operational security planning and control |
