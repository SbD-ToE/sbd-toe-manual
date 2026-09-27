---
id: policy-requisitos-seguranca
title: Security Requirements Policy
description: Organisational policy that defines how security requirements must be selected, documented, traced, validated and maintained throughout the lifecycle of each application, proportionally to its classified risk level.
tags: [policy, requisitos, segurança, catálogo, backlog, rastreabilidade, validação, SDLC, cap02, L1, L2, L3, governance]
grupo: design-analise
sidebar_position: 7
translation:
  source_locale: pt
  source_path: 020-assets/policies/07_policy-requisitos-seguranca.md
  source_sha256: b371665d6512c151f72ffe640386bf5f982813429af39e3088f2768f1a06529f
  source_commit: 32978973a6e4e01d6abcfe36fb0e33a8192cb20d
  target_sha256: 51560c5ee9e1e93ab082723fb4e2b5fe043495a2480d2ae397ebb87ae9e0a489
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [alcada, cycle_iteration, eu_startups, gap_family, lifecycle_phase, mapping, requirement_runtime, risk_level, role_tech_lead, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: e4219dcb2318ea65d9efb4015721052fea5e12551c2287d96f1be46cc6cfa02d
  translated_at: 2026-09-27T15:08:13Z
  stamped_at: 2026-09-27T15:08:13Z
  reviewed_by: null
---

# Security Requirements Policy

## 1. Objective {#1-objetivo}

This policy defines how **security requirements** must be selected, documented, traced, validated and maintained throughout the entire lifecycle of each application developed or operated by the organisation.

Including security requirements in the development process is not optional - it is the foundation that ensures security is considered by design rather than corrected after the fact. Without formal requirements, the team develops without explicit security criteria, which makes validation impossible and compliance undemonstrable.

---

## 2. Scope {#2-âmbito}

This policy applies to all applications with an active risk classification (L1, L2 or L3), in every phase of the lifecycle: design, development, integration, testing, deploy and maintenance.

---

## 3. Requirements catalogue {#3-catálogo-de-requisitos}

### 3.1 Organisational baseline {#31-baseline-organizacional}

The organisation maintains a **baseline catalogue of security requirements**, organised by domain and applicability level (L1, L2, L3), aligned with the SbD-ToE Ch. 02 model.

The baseline catalogue is versioned, maintained by AppSec and reviewed at least annually.

### 3.2 Project catalogue {#32-catálogo-do-projeto}

At the start of each project (or when an existing application is brought into the SbD-ToE model), a **project requirements catalogue** must be created, derived from the organisational baseline and filtered by the application's criticality level.

**Requirements for the project catalogue:**

- [ ] Derived from the organisational baseline with an explicit filter by level L1/L2/L3
- [ ] Unique identifiers per requirement
- [ ] Owner defined and review frequency established
- [ ] Mapping to associated validation criteria
- [ ] Versioned in the project repository or requirements management platform
- [ ] Updated whenever the application's criticality level or scope changes

---

## 4. Proportional selection of requirements {#4-seleção-proporcional-de-requisitos}

The selection of requirements must be **proportional to the risk level** of the application:

| Practice | L1 | L2 | L3 |
|---|---|---|---|
| Essential subset of the catalogue | Mandatory | - | - |
| Full catalogue applicable to the level | - | Mandatory | Mandatory |
| Domain-specific requirements (auth, logging, API, etc.) | Recommended | Mandatory | Mandatory |
| Independent review of the selection | Not applicable | Recommended | Mandatory |
| Bidirectional traceability requirement → code | Recommended | Mandatory | Mandatory |

---

## 5. Integration into the development lifecycle {#5-integração-no-ciclo-de-desenvolvimento}

Security requirements must be applied at the following points of the SDLC:

| Phase / Event | Expected action | Main artefact |
|---|---|---|
| Project start | Select requirements proportional to the criticality level | `matriz-controlos-por-risco.md` |
| Grooming / Planning | Turn requirements into traceable cards in the backlog | Backlog with `SEC-Lx-*` tags |
| New feature or refactor | Revalidate the requirements applicable to the change | Updated story/technical task |
| New integration or external exposure | Review authentication, logging, access control and API requirements | Integration issue/checklist |
| Sprint review / Testing | Verify security acceptance criteria and collect evidence | Criteria + tests + evidence |
| Release | Confirm that all applicable requirements have validation evidence | Release checklist |
| Post-incident | Review whether the incident reveals a gap in the requirements; update the catalogue | Updated catalogue |

---

## 6. Taxonomy and tags {#6-taxonomia-e-tags}

Security requirements in the backlog must be identified with a traceable taxonomy. The reference format is:

```
SEC-Lx-Tyy-ZZZ
```

Where:
- `Lx` - criticality level (L1, L2, L3)
- `Tyy` - domain category (e.g. AUT, LOG, VAL, API, CFG, ENC, INT...)
- `ZZZ` - sequential number of the requirement

Automatic validation of the presence of `SEC-Lx-*` tags in relevant PRs must be configured in the CI/CD pipeline at L2 and L3.

---

## 7. Validation criteria {#7-critérios-de-validação}

Each selected requirement must have **explicit and verifiable acceptance criteria**, defined before development begins:

- [ ] Formal acceptance criteria defined in the card or requirement document
- [ ] Alignment with the project requirements catalogue
- [ ] Validation planned in automated tests and/or formal reviews
- [ ] Validation evidence recorded and traceable to the requirement

Requirements without defined validation criteria must not be considered implemented, regardless of the state of development.

---

## 8. Review upon relevant change {#8-revisão-por-alteração-relevante}

The applicable requirements must be reviewed whenever one of the following changes occurs:

| Trigger | Action |
|---|---|
| New external integration | Review authentication, integrity and logging requirements |
| New type of data processed | Review encryption, access control and logging requirements |
| Change in exposure | Review API, authentication and configuration requirements |
| Architecture change | Review secure architecture and threat modelling requirements |
| New user profile | Review access control and session requirements |
| Incident outcome | Update the catalogue with the requirements the incident revealed to be missing |

The review must be documented with reference to the trigger, the updated requirements and the approval.

---

## 9. Management of exceptions to requirements {#9-gestão-de-exceções-a-requisitos}

When a requirement mandatory for the level cannot be implemented, the process defined in the **Security Exception Management Policy** (`05_policy-gestao-excecoes`) applies:

- Mandatory technical justification
- Compensating mitigation defined
- TTL proportional to the level and severity
- Approval by the appropriate approval authority
- Formal record with reference to the requirement subject to the exception

---

## 10. Proportionality by level {#10-proporcionalidade-por-nível}

| Policy requirement | L1 | L2 | L3 |
|---|---|---|---|
| Project catalogue created and versioned | Mandatory | Mandatory | Mandatory |
| `SEC-Lx-*` tags in the backlog | Mandatory | Mandatory | Mandatory |
| Validation criteria per requirement | Mandatory | Mandatory | Mandatory |
| Automatic validation of tags in the pipeline | Not applicable | Recommended | Mandatory |
| Independent review of the selection | Not applicable | Recommended | Mandatory |
| Exportable traceability report | Optional | Recommended | Mandatory |
| Reassessment upon relevant change | On request | Mandatory | Mandatory |
| Formalised exceptions with TTL | Simplified | Mandatory | Mandatory (short TTL) |

---

## 11. Artefacts {#11-artefactos}

| Artefact | Suggested location | Retention |
|---|---|---|
| Project requirements catalogue | `docs/req/` or management platform | While the application is active |
| Matrix of controls by level | `docs/security/` | While the application is active |
| Backlog with `SEC-Lx-*` tags | Project management tool | History preserved |
| Validation evidence per requirement | Evidence repository / CI/CD | As per the Traceability Policy |
| Traceability report | GRC / periodic export | 2 years |

---

## 12. Responsibilities {#12-responsabilidades}

| Role | Responsibility |
|---|---|
| Product Owner | Ensure that security requirements enter the backlog with acceptance criteria |
| Tech Lead / Architect | Select requirements proportional to the level; review upon relevant change |
| Developer | Implement requirements with traceable evidence; report blockers |
| AppSec Engineer | Maintain the baseline catalogue; validate the selection at L2/L3; conduct independent reviews |
| QA | Verify acceptance criteria; collect and archive validation evidence |
| GRC / Compliance | Monitor requirements coverage; issue traceability reports |

---

## 13. Review and audit of this policy {#13-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Update of the SbD-ToE Ch. 02 baseline catalogue
- Incident revealing a gap in the requirements selection or validation process
- Regulatory change with an impact on the minimum security requirements

---

## 14. Normative and technical references {#14-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 02 - Security Requirements | Base catalogue, taxonomy, user stories for selection and traceability |
| SbD-ToE Ch. 01 - Application Classification | Criticality level that determines proportional selection |
| SbD-ToE Ch. 03 - Threat Modelling | Trigger for reviewing requirements after threats are identified |
| OWASP ASVS | Application Security Verification Standard - reference catalogue |
| NIST SP 800-160 | Systems Security Engineering |
| SSDF PW.1 | Definition of security requirements based on risk |
| ISO/IEC 27001 - Clause 8.1 | Operational planning and control |
