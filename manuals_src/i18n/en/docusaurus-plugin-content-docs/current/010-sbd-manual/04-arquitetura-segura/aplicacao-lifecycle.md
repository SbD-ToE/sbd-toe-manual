---
id: aplicacao-lifecycle
title: How to Do It
description: Integration of Secure Architecture practices throughout the development cycle
tags: [tipo:aplicacao, ciclo-vida, arquitetura, requisitos, seguranca]
genia: us-format-normalization
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/aplicacao-lifecycle.md
  source_sha256: c3213c8e94382c853f45c3f0833608397023ee9fd4ac1ad30cd6c235871f22ef
  source_commit: 112711064196b71c545672fe3fb3ae412b36575e
  target_sha256: 65bd2ab7a554d0aad774f9019abd2bec3229d8fa5eac8676fb57a048d89bdb67
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, avaliacao, chapter_role, como_fazer, cycle_iteration, deterministic, discipline, layer, lifecycle_phase, llm, papel_suporte, plain_rag, provenance, requirement_runtime, risk_level, segregacao_de_funcoes, slug_threat_modeling, threat, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 75162a3183fc28d9e63e1cd304c05dc15abbcc8a7ef7d40154b281a5ca8323b7
  translated_at: 2026-09-26T17:23:46Z
  stamped_at: 2026-09-26T18:33:38Z
  reviewed_by: null
---

# Applying Secure Architecture in the Lifecycle

This annex prescribes **how to systematically apply the Secure Architecture practices defined in Chapter 4** throughout the development cycle, ensuring **traceability**, **proportionality to risk (L1–L3)** and integration with requirements and threats.

It includes **reusable user story templates**, actions per role, expected artefacts and application tables per criticality level.

---

## 🧭 When to apply Secure Architecture {#-quando-aplicar-arquitetura-segura}

| Phase / Event | Expected action | Who takes part | Main artefact |
|---|---|---|---|
| Project / epic start | Define principles and the initial baseline | Software Architects, AppSec Engineer, DevOps/SRE | `principios-arquitetura.md` |
| Solution design | Produce a solution sheet with controls and decisions | Software Architects, AppSec Engineer | `solution-architecture.md` |
| Grooming / Planning | Validate architectural requirements and control planning | Developer, Software Architects, AppSec Engineer | `design-review.md` |
| Relevant architectural decision | Record an ADR with alternatives, trade-offs and impact | Software Architects, AppSec Engineer | `adr/ADR-XXXX.md` |
| Integrations / trust boundaries | Review trust boundaries, integrations and data flows (incl. observability) | Software Architects, AppSec Engineer, Developer | `trust-boundaries.md` |
| Significant architectural change | Update the baseline and invalidate/update affected decisions | Developer, Software Architects, AppSec Engineer | `architecture-update.md` |
| Architectural exception | Request/assess/approve the exception with compensating controls and a *sunset* | Product Owner, AppSec Engineer, Software Architects | `excecao-arquitetura.md` |
| “Living architecture” triggers | Reassess docs/ADR/TM when defined events occur | Software Architects, DevOps/SRE, AppSec Engineer | `arquitetura-triggers.md` |
| Release / Go-live | Architectural gate: verify controls and exceptions | QA, AppSec Engineer, Software Architects | `checklist-arquitetura.md` |
| CI/CD pipeline | Automatically validate the architectural controls that can be automated (where applicable) | DevOps/SRE, AppSec Engineer | `ci-architecture-report.*` |

---

## 👥 Who does what {#-quem-faz-o-quê}

| Role / Function | Key responsibilities |
|---|---|
| Software Architects | Define principles, create solution sheets, maintain the baseline and ADRs, review designs and integrations |
| Developer | Implement architectural decisions and the specified controls, flag significant changes |
| QA | Ensure that architectural requirements and controls are reflected in tests and release evidence |
| AppSec Engineer | Define/review controls, validate decisions and exceptions, ensure the link to threats (Ch. 3) and requirements (Ch. 2) |
| Product Owner | Prioritise investment/mitigation, approve business trade-offs and exceptions with impact on scope/deadlines |
| DevOps/SRE | Integrate automatable validations into the pipeline, ensure reproducible evidence, support “living architecture” |

---

## 📝 Reusable User Stories {#-user-stories-reutilizáveis}

> **Editorial note:** each user story consistently includes **Story**, **BDD**, **Checklist**, **Artefacts & evidence**, **Proportionality (L1–L3)**, **Integration into the SDLC** and **Useful links**.

---

### US-01 - Defining secure architecture principles and baseline {#us-01---definição-de-princípios-e-baseline-de-arquitetura-segura}

**Context.**  
At the start of a project (or of a significant epic), it is mandatory to establish **principles** and an **initial baseline**, to guide decisions and prevent architectural drift.

:::userstory
**Story.**  
As **Software Architects**, I want to define and version secure architecture principles, so that all technical decisions are consistent, traceable and proportional to risk.

**Acceptance criteria (BDD).**
- **Given** that a project starts or a structural epic is created  
  **When** I document the principles and the initial baseline  
  **Then** the principles are versioned, approved and referenceable per release

**Checklist.**
- [ ] `principios-arquitetura.md` created and versioned
- [ ] Principles include: isolation, trust boundaries, exposure minimisation, dependency management, secure observability
- [ ] Approval recorded (AppSec + Architecture)
- [ ] Explicit link to the risk level (L1–L3)
:::

**Artefacts & evidence.**
- `principios-arquitetura.md`
- Approval record (PR/issue)

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Minimum principles and simplified baseline |
| L2 | Yes | Full principles and formal baseline |
| L3 | Yes | Full principles + independent review |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Start | New project / structural epic | Software Architects | Before detailed design |

**Useful links.**
- 🔗 Ch. 2 - Security Requirements: `/sbd-manual/requisitos-seguranca/intro`
- 🔗 Ch. 3 - Threat Modelling: `/sbd-manual/threat-modeling/intro`

---

### US-02 - Solution sheet with controls and architectural traceability {#us-02---ficha-de-solução-com-controlos-e-rastreabilidade-arquitetural}

**Context.**  
During design, the solution must be described with **explicit architectural controls**, exposure minimisation and a link to requirements/threats.

:::userstory
**Story.**  
As **Software Architects**, I want to produce an architecture sheet with security controls and traceability to architectural requirements, so that the solution is secure and verifiable before implementation.

**Acceptance criteria (BDD).**
- **Given** that the design is being defined  
  **When** I document the solution  
  **Then** the sheet includes trust boundaries, justified external exposure, architectural controls and references to the relevant requirements and threats

**Checklist.**
- [ ] `solution-architecture.md` created with the approved template
- [ ] Trust boundaries and flows (incl. logs/metrics/telemetry) identified
- [ ] External exposure minimised and justified
- [ ] Architectural controls specified (isolation, segmentation, quotas, *timeouts*, *fallbacks*, segregation)
- [ ] External dependencies identified and treated as architectural decisions
- [ ] Traceability recorded (architectural requirements ↔ decisions ↔ threats ↔ controls)
- [ ] Approval recorded (AppSec + Architecture)
:::

**Artefacts & evidence.**
- `solution-architecture.md`
- `controlos-arquitetura.md` (optional, if needed for detail)
- Approval record (PR/issue)

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Simplified sheet and essential controls |
| L2 | Yes | Detailed sheet + minimum traceability |
| L3 | Yes | Full sheet + independent review + reinforced evidence |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Design | Solution definition | Software Architects + AppSec Engineer | Before implementation |

**Useful links.**
- 🔗 Architectural requirements catalogue (ARC-*): `addon/01-catalogo-requisitos`
- 🔗 Reference diagrams/models: `addon/04-diagramas-referencia`

---

### US-03 - Formal review of the architectural design {#us-03---revisão-formal-do-design-arquitetural}

**Context.**  
Before implementation, the design must be reviewed for compliance with principles, requirements and threat mitigation.

:::userstory
**Story.**  
As an **AppSec Engineer**, I want to formally review the architectural design, so that the necessary controls are specified and the decisions are defensible and traceable.

**Acceptance criteria (BDD).**
- **Given** that a candidate solution sheet exists  
  **When** I carry out the review  
  **Then** the design is approved, or is returned with traceable corrective actions

**Checklist.**
- [ ] Review recorded (checklist + comments)
- [ ] Deviations and corrective actions recorded in the backlog
- [ ] Approval or rejection documented and versioned
:::

**Artefacts & evidence.**
- `design-review.md`
- Approval/rejection record (PR/issue)

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Simplified review |
| L2 | Yes | Formal review |
| L3 | Yes | Formal review + segregation of duties (independent review) |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Planning | Design ready for implementation | AppSec Engineer | Before implementation |

**Useful links.**
- 🔗 Ch. 3 - Threat Modelling: `/sbd-manual/threat-modeling/intro`

---

### US-04 - Managing architectural decisions (ADR) {#us-04---gestão-de-decisões-arquiteturais-adr}

**Context.**  
Critical architecture decisions must be documented with alternatives and trade-offs, to preserve traceability and allow review/invalidation.

:::userstory
**Story.**  
As **Software Architects**, I want to record architectural decisions (ADR) with alternatives and security impact, so that the baseline is auditable and can evolve.

**Acceptance criteria (BDD).**
- **Given** that a relevant architectural decision is taken  
  **When** I create an ADR with the approved template  
  **Then** the context, alternatives, decision, trade-offs, impact and AppSec review are recorded

**Checklist.**
- [ ] ADR created in `adr/ADR-XXXX.md`
- [ ] Alternatives considered and trade-offs documented
- [ ] Security and risk impact made explicit (incl. L1–L3 where applicable)
- [ ] Link to the relevant architectural requirements and threats
- [ ] Approval recorded
:::

**Artefacts & evidence.**
- `adr/ADR-XXXX.md`
- Approval record (PR/issue)

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | High-impact ADRs only |
| L2 | Yes | ADRs for significant decisions |
| L3 | Yes | ADRs for all relevant decisions + independent review |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Design | Relevant architectural decision | Software Architects | Before implementation |

**Useful links.**
- 🔗 Architectural decision and evidence (addon): `addon/decisao-evidencia-arquitetural`

---

### US-05 - Reviewing trust boundaries and integrations {#us-05---revisão-de-fronteiras-de-confiança-e-integrações}

**Context.**  
Internal and third-party integrations require an explicit review of trust boundaries and data flows (including implicit flows).

:::userstory
**Story.**  
As **Software Architects + AppSec Engineer**, I want to review trust boundaries and integrations, so that authentication, authorisation, encryption, isolation and data exposure are validated.

**Acceptance criteria (BDD).**
- **Given** that a new or changed integration exists  
  **When** I assess trust boundaries and controls  
  **Then** I document decisions, residual risks and mitigating controls, with traceability

**Checklist.**
- [ ] Integration inventory updated
- [ ] Trust boundaries and flows (incl. logs/metrics/telemetry) documented
- [ ] Controls per integration defined (AuthN/AuthZ/TLS/segregation/minimisation)
- [ ] Residual risk and exceptions (if any) formalised
:::

**Artefacts & evidence.**
- `trust-boundaries.md`
- `integration-review.md`
- ADR (where applicable)

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Reduced scope (critical integrations) |
| L2 | Yes | Full scope |
| L3 | Yes | Full scope + reinforced validations (according to risk) |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Design / Change | New integration / change | Software Architects + AppSec Engineer | Before implementation |

**Useful links.**
- 🔗 Process risks in architecture (addon): `addon/riscos-processo-arquitetura`

---

### US-06 - Updating the baseline after a significant architectural change {#us-06---atualização-da-baseline-após-alteração-arquitetural-significativa}

**Context.**  
Significant architectural changes invalidate earlier decisions and require the baseline to be updated and (where applicable) threats/requirements to be reassessed.

:::userstory
**Story.**  
As a **Developer**, I want to update the architectural baseline when significant changes occur, so that the real system and the approved architectural evidence remain coherent.

**Acceptance criteria (BDD).**
- **Given** that a significant architectural change occurs  
  **When** I update the affected documentation and decisions  
  **Then** the baseline is consistent, and the necessary reviews are triggered

**Checklist.**
- [ ] Change classified as “significant” according to the chapter's criteria
- [ ] `architecture-update.md` updated and versioned
- [ ] Affected ADRs updated (or invalidated and replaced)
- [ ] AppSec review triggered where applicable
- [ ] (If applicable) associated review of threats and requirements
:::

**Artefacts & evidence.**
- `architecture-update.md`
- Updated ADRs
- Review record (PR/issue)

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Relevant structural changes only |
| L2 | Yes | All significant changes |
| L3 | Yes | All + independent review where applicable |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Development | Significant change | Developer + Software Architects | Within the same sprint |

**Useful links.**
- 🔗 Ch. 3 - Threat Modelling: `/sbd-manual/threat-modeling/intro`

---

### US-07 - Automatable architectural validation in CI/CD (where applicable) {#us-07---validação-arquitetural-automatizável-no-cicd-quando-aplicável}

**Context.**  
Certain architectural controls can be validated in an automated (or semi-automated) way. The goal is to **produce reproducible evidence**, not to “replace” human review.

:::userstory
**Story.**  
As **DevOps/SRE + AppSec Engineer**, I want to integrate automatable validations of architectural controls into the pipeline, so that non-conformities are detected early and auditable evidence is generated.

**Acceptance criteria (BDD).**
- **Given** that a change with impact on architecture, configuration or infrastructure occurs  
  **When** the pipeline runs  
  **Then** deterministic results (pass/fail where applicable) and versioned evidence artefacts are produced

**Checklist.**
- [ ] Criteria for when to run the validation defined (paths/labels/conditions)
- [ ] Automatable checks implemented (e.g. policies, configurations, architectural invariants, verifiable requirements)
- [ ] Evidence produced as an artefact (`ci-architecture-report.*`)
- [ ] Blocking rules by risk defined (e.g. L2 blocks critical failures; L3 blocks failures of high severity and above)
- [ ] Remediation SLA defined and traceable
:::

**Artefacts & evidence.**
- Pipeline configuration (`ci-pipeline.*`)
- `ci-architecture-report.*` (reports, logs, artefacts)
- Blocking and remediation records (PR/issue)

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Alerts and basic evidence |
| L2 | Yes | Formal evidence + blocking of critical non-conformities |
| L3 | Yes | Full evidence + reinforced blocking rules + centralised audit |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| CI/CD | Change with impact | DevOps/SRE + AppSec Engineer | On every relevant build |

**Useful links.**
- 🔗 Ch. 7 - Secure CI/CD: `/sbd-manual/cicd-seguro//intro`

---

### US-08 - Assessing business impact and prioritising trade-offs {#us-08---avaliação-de-impacto-no-negócio-e-priorização-de-trade-offs}

**Context.**  
Architectural decisions involve trade-offs with business impact. Prioritisation must be explicit and traceable.

:::userstory
**Story.**  
As a **Product Owner**, I want to assess the business impact of architectural requirements and decisions, so that mitigation is prioritised and trade-offs are accepted consciously and auditably.

**Acceptance criteria (BDD).**
- **Given** that there are requirements/decisions with impact on cost/schedule/UX  
  **When** I assess the impact and prioritise  
  **Then** the decision is documented and linked to the backlog and to the technical decisions

**Checklist.**
- [ ] Impact assessed and recorded (cost/schedule/risk)
- [ ] Prioritisation reflected in the backlog
- [ ] Trade-off documented and approved where necessary
:::

**Artefacts & evidence.**
- `impacto-arquitetura.md` (or an equivalent record)
- Backlog/epics linked to ADRs/requirements

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Critical impacts only |
| L2 | Yes | Formal assessment |
| L3 | Yes | Formal assessment + executive validation where applicable |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Planning | Requirements/decisions defined | Product Owner | Before sprint prioritisation |

**Useful links.**
- 🔗 Ch. 1 - Classification / risk: `/sbd-manual/classificacao-aplicacoes/intro`

---

### US-09 - Threat Modelling ↔ Architecture synchronisation {#us-09---sincronização-threat-modeling--arquitetura}

**Context.**  
Architecture decisions must reflect the prioritised threats and, in the opposite direction, architectural changes require the threat model to be updated where applicable.

:::userstory
**Story.**  
As **Software Architects + AppSec Engineer**, I want to synchronise architecture and threat modelling, so that architectural controls cover the prioritised threats and traceability remains valid.

**Acceptance criteria (BDD).**
- **Given** that a significant architectural decision or change exists  
  **When** I check the impact on the threat model  
  **Then** I update the necessary artefacts and keep the decision ↔ threat ↔ control ↔ requirement traceability

**Checklist.**
- [ ] Impact of the change assessed
- [ ] Threat model updated where applicable
- [ ] Solution sheet and ADRs aligned
- [ ] Coverage evidence updated
:::

**Artefacts & evidence.**
- `solution-architecture.md`
- Threat model artefact (as per Ch. 3)
- Update record (PR/issue)

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Simplified model where applicable |
| L2 | Yes | Full model |
| L3 | Yes | Detailed model + independent review where applicable |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Design / Change | Significant decision/change | Software Architects + AppSec Engineer | Before the release |

**Useful links.**
- 🔗 Ch. 3 - Threat Modelling: `/sbd-manual/threat-modeling/intro`

---

### US-10 - Managing architectural exceptions with compensating controls {#us-10---gestão-de-exceções-arquiteturais-com-controlos-compensatórios}

**Context.**  
When an architectural requirement/control cannot be applied, a formal exception is required, with compensating controls, an *owner* and a *sunset*.

:::userstory
**Story.**  
As **Product Owner + AppSec Engineer**, I want to manage architectural exceptions with approval and compensating controls, so that risk and delivery are balanced while auditability is maintained.

**Acceptance criteria (BDD).**
- **Given** that an architectural exception is requested  
  **When** I assess the impact, compensations and deadline  
  **Then** the exception is approved/rejected, with evidence, an *owner* and a review date (*sunset*)

**Checklist.**
- [ ] Exception request documented
- [ ] Impact and residual risk assessed
- [ ] Compensating controls defined and verifiable
- [ ] Risk *owner* defined
- [ ] *Sunset* and review scheduled
- [ ] Approval recorded and versioned
:::

**Artefacts & evidence.**
- `excecao-arquitetura.md`
- Approval record (PR/issue)
- Evidence of compensations (tests/configs)

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Simplified process |
| L2 | Yes | Formal process |
| L3 | Yes | Reinforced governance + audit |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Design / Release | Inability to meet a control | Product Owner + AppSec Engineer | Before go-live |

**Useful links.**
- 🔗 Ch. 14 - Governance: `/cap14/intro`

---

### US-11 - “Living architecture” triggers and review discipline {#us-11---triggers-de-arquitetura-viva-e-disciplina-de-revisão}

**Context.**  
The architecture must be treated as a living baseline. There are events that require evidence to be reviewed and synchronised.

:::userstory
**Story.**  
As **Software Architects + DevOps/SRE**, I want to maintain a list of triggers that set off an architecture review, so that the baseline, ADRs and evidence remain valid over time.

**Acceptance criteria (BDD).**
- **Given** that a defined trigger occurs (e.g. new integration, change to sensitive data, change of trust boundary, structural change to infrastructure/pipeline)  
  **When** I carry out the associated review  
  **Then** I update the baseline, the affected ADRs and the necessary evidence, with a verifiable record

**Checklist.**
- [ ] `arquitetura-triggers.md` published and versioned
- [ ] Triggers defined with minimum actions per trigger
- [ ] Trigger execution generates evidence (PR/issue/minutes)
- [ ] Traceability maintained (decision ↔ evidence)
:::

**Artefacts & evidence.**
- `arquitetura-triggers.md`
- Execution records (PR/issue)
- ADRs/baseline updated where applicable

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Minimum subset of triggers |
| L2 | Yes | Full set |
| L3 | Yes | Full set + detection/alerts where feasible |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Continuous | Architectural trigger | Software Architects + DevOps/SRE | Within the current sprint (or the defined SLA) |

---

### US-12 - Architectural gate before Go-live {#us-12---gate-arquitetural-antes-do-go-live}

**Context.**  
Before production, there must be an **architectural gate** that confirms: controls implemented, decisions valid and exceptions handled.

:::userstory
**Story.**  
As **QA + AppSec Engineer + Software Architects**, I want to run an architectural gate before go-live, so that the implemented architecture matches the approved baseline and controls/exceptions are verified.

**Acceptance criteria (BDD).**
- **Given** that the application is ready for release  
  **When** I run the architectural validation checklist  
  **Then** I confirm compliance, or I block the go-live with traceable deviations

**Checklist.**
- [ ] `checklist-arquitetura.md` completed and versioned
- [ ] Critical controls verified with evidence
- [ ] Exceptions confirmed with compensations and a *sunset*
- [ ] Deviations recorded and formally accepted where applicable
- [ ] Final approval recorded
:::

**Artefacts & evidence.**
- `checklist-arquitetura.md`
- Verification evidence (tests/configs/logs)
- Approval record (PR/issue)

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Simplified checklist |
| L2 | Yes | Formal checklist |
| L3 | Yes | Full checklist + independent review where applicable |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Release / Go-live | Release preparation | QA + AppSec + Architecture | Before entry into production |

**Useful links.**
- 🔗 Architectural criteria and evidence (addon): `addon/decisao-evidencia-arquitetural`

---

### US-13 - Secure architecture pattern catalogue (governed reuse) {#us-13---catálogo-de-padrões-de-arquitetura-segura-reutilização-governada}

**Context.**  
Approved patterns reduce variation and the risk of omission. Reuse must be governed and versioned.

:::userstory
**Story.**  
As **Software Architects**, I want to maintain a versioned catalogue of secure architecture patterns, so that new projects reuse approved designs with requirements, mitigated threats and an implementation checklist.

**Acceptance criteria (BDD).**
- **Given** that a new project starts  
  **When** I select a pattern from the catalogue  
  **Then** the pattern provides a baseline, applicable requirements, covered threats and a verifiable checklist

**Checklist.**
- [ ] Catalogue published and versioned
- [ ] Patterns have: diagram, key decisions, applicable requirements, mitigated threats, checklist
- [ ] Formal approval (Architecture + AppSec)
- [ ] Change history (changelog)
:::

**Artefacts & evidence.**
- `modelos-referencia.md`
- `padroes-checklist.md` (if needed)
- Approval records

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Reduced catalogue |
| L2 | Yes | Formal catalogue with the main patterns |
| L3 | Yes | Full catalogue and continuous evolution |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Design | New project / structural change | Software Architects + AppSec Engineer | Before the solution sheet |

**Useful links.**
- 🔗 Diagrams/models: `addon/04-diagramas-referencia`

---

### US-14 - Formal architecture review for L3 (reinforced governance) {#us-14---revisão-formal-de-arquitetura-para-l3-governação-reforçada}

**Context.**  
L3 applications require reinforced formal validation (including segregation of duties and an auditable decision).

:::userstory
**Story.**  
As **Executive Management/CISO + Software Architects**, I want to establish a formal architecture approval process for L3, so that structural risks are identified, mitigated and accepted auditably before go-live.

**Acceptance criteria (BDD).**
- **Given** that an L3 application is ready for approval  
  **When** it is submitted to the reinforced formal review  
  **Then** a recorded opinion exists (approve, approve with exceptions, reject) with actions and deadlines

**Checklist.**
- [ ] Process and participants defined (explicit responsibilities)
- [ ] Documentation submitted (baseline, ADRs, integrations, exceptions, evidence)
- [ ] Review concluded with a formal opinion
- [ ] Deviations generate a remediation plan or an exception with compensations
- [ ] Decision archived and referenceable per release
:::

**Artefacts & evidence.**
- `governance-checklist-l3.md` (or equivalent)
- Formal opinion recorded
- Remediation plan / approved exceptions

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | No | - |
| L2 | Recommended | Reinforced *peer* review |
| L3 | Yes | Formal and auditable process |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Release / Go-live | L3 release | Management/CISO + designated reviewers | Internal SLA (e.g. ≥ 2 weeks before) |

**Useful links.**
- 🔗 Ch. 14 - Governance: `/cap14/intro`

---

### US-15 - Identifying and governing non-deterministic components {#us-15---identificação-e-governação-de-componentes-não-determinísticos}

**Context.**  
Modern architectures may include components whose behaviour **is not strictly deterministic** (e.g. probabilistic decision engines, heuristic scoring, statistical models or inference components). These components introduce specific challenges in terms of security, audit, explainability and operational control, which must be explicitly addressed at the architecture level.

:::userstory
**Story.**  
As **Software Architects + AppSec Engineer**, I want to identify and govern non-deterministic architectural components, documenting their impact on security, audit and control, so that the architecture remains traceable, governable and proportional to risk.

**Acceptance criteria (BDD).**
- **Given** that the solution includes a component whose behaviour is not fully deterministic  
  **When** I design or review the architecture  
  **Then** the component is explicitly identified and classified  
- **And** the impact on security, audit and control is documented  
- **And** adequate architectural controls are defined (isolation, supervision, *fallback*, logging)  
- **And** traceability exists between the component, the relevant threats and the applicable architecture requirements

**Checklist.**
- [ ] Non-deterministic components identified in the architecture sheet
- [ ] Type of non-determinism classified (e.g. probabilistic, heuristic, inferential)
- [ ] Impact analysed on:
  - [ ] Security (abuse, *bypass*, unexpected behaviour)
  - [ ] Audit and explainability
  - [ ] Operational control and *fallback* mechanisms
- [ ] Trust boundaries and isolation reviewed (where applicable)
- [ ] Logging and evidence defined for relevant decisions
- [ ] Traceability documented (component ↔ threat ↔ control ↔ architecture requirement)
- [ ] Evidence archived in the architecture repository
:::

**Artefacts & evidence.**
- Update of `solution-architecture.md`
- Architectural decision/evidence documentation (e.g. `decision-evidence.md`)
- Threat model update (where applicable)

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Simple identification and impact note |
| L2 | Yes | Formal identification and defined controls |
| L3 | Yes | Full governance, explicit isolation and independent validation |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Design / Review | Introduction or change of a non-deterministic component | Software Architects + AppSec Engineer | Before design approval |

**Useful links.**
- 🔗 Ch. 3 - Threat Modelling  
- 🔗 Architecture requirements applicable to the architecture

---

### US-16 - Architecture review for an AI agent at A2+ {#us-16}

**Context.**
US-15 covers *non-deterministic components* in general (predictive models, RAG, LLMs in the interface). When the component is an **autonomous agent** that performs actions with real effect on external systems via *tool-use* — and operates at level A2 or higher — an additional layer of architectural validation is required: confirming that the architecture meets [`ARC-015`](./addon/catalogo-requisitos-arquitetura#arc-015) before activation, so that structural failures are not only detected at the incident.

:::userstory
**Story.**
As a **Software Architect** and **AppSec Engineer**, I want to validate that the system architecture fully meets [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (dedicated identity, per-tool *least privilege*, *intent declaration*, *out-of-band* human approval, exercised *kill-switch*, full audit per *tool invocation*) **before** approving the operation of an AI agent at A2 or higher, so that structural problems are not discovered only once they have already had an effect in production.

**Acceptance criteria (BDD).**
- **Given** that an AI agent is going to operate at A2+
  **When** the architecture review prior to the activation of the *mandate* is carried out
  **Then** a completed [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) checklist exists, with evidence for each item, linked to the `mandate_ref`
- **Given** that a checklist item fails
  **When** the review is concluded
  **Then** the agent does **not** operate at the requested level; it operates at a lower level until the item is resolved (stepping down is always legitimate; stepping up requires a new review)
- **Given** that the *kill-switch* has never been exercised in this architecture
  **When** activation of A3 or A4 is intended
  **Then** the exercise is run in sandbox/staging, timed and with the *log* archived before activation

**Acceptance criteria (DoD).**
- [ ] **Dedicated identity** — the agent has an ephemeral *workload identity* (OIDC) per environment; no reuse of human credentials; TTL ≤ 1h
- [ ] **Minimum per-tool scope** — each *tool* on the *allowlist* with arguments limited to what is necessary; labelled `read`/`write`/`destructive`/`external`
- [ ] **Intent declaration** — mechanism ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) emits a structured *intent event* before each destructive *tool call*, with the minimum schema: `agent_id`, `mandate_ref`, `tool`, `args`, `intent`, `expected_outcome`, `risk_self_assessment`
- [ ] **Out-of-band approval** — channel independent of the agent's channel (Slack approval with 2FA, GitHub review, signed webhook, *push notification*); *prompt injection* attacks on the main channel cannot approve
- [ ] **Operational kill-switch** — credential revocation + *runtime* termination + *namespace* isolation + on-call alert; exercised in sandbox/staging with a recorded cadence (quarterly A3; monthly A4)
- [ ] **Full per-tool audit** — structured *event* with `timestamp`, `agent_id`, `session_id`, `mandate_ref`, `autonomy_level`, `tool`, `tool_version`, `args` (PII and secrets redacted), `intent_event_ref`, `outcome`, `external_effect`; integrated with the observability of Ch. 12
- [ ] The agent's *threat model* (US-11 of Ch. 03) referenced and *mitigations* mapped to this checklist

:::

**Artefacts & evidence.**
- `arc-015-review.md` — completed checklist with reference to `mandate_ref` and `threat_model_ref`
- *Log* of the *kill-switch* exercise (initial date + recorded cadence)
- Versioned agentic architecture diagram (DFD with five participants — human · client · model · *tool runtime* · external system — and four boundaries)
- *Workload identity* configuration (IaC reference) and evidence of TTL ≤ 1h
- Redacted example of an *intent event* + *tool invocation audit event* (one real session)

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | A2+ typically outside production; simplified review where applicable | Essential [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) checklist; *kill-switch* exercised annually |
| L2 | Mandatory for A2+ | Full [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) checklist; *kill-switch* exercised quarterly (A3) |
| L3 | Mandatory for A2+; A3/A4 with independent `appsec` review | Full [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) checklist + independent review; A4 with formal signature of the `CISO` on the *mandate*; *kill-switch* exercised monthly (A4) |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Design / Review | Activation of an agent at A2+ | Software Architects + AppSec Engineer | Before activation of the *mandate* |
| Level increase | Promotion A2→A3 or A3→A4 | `appsec` (+ `grc` at A3; + `CISO` at A4) | Before the new activation |
| Periodic review | `review_cadence` of the *mandate* | `appsec` | According to cadence (annual A2; half-yearly A3; quarterly A4) |

**Useful links.**
- 🔗 [`ARC-015` — agent as an isolated *principal*](./addon/catalogo-requisitos-arquitetura#arc-015)
- 🔗 [Architectural patterns for agents (advanced recommendations)](./recomendacoes-avancadas#agentes-principals)
- 🔗 [`REQ-AGN-*` catalogue (Ch. 02)](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)
- 🔗 [Agentic Threat Modelling playbook (Ch. 03)](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic)
- 🔗 [Policy 38 — AI Agent Mandates](/sbd-toe/assets/policies/policy-mandates-agentes)

---

### US-17 - Environment segmentation and topology-as-code validation (L3) {#us-17---segmentação-de-ambientes-e-validação-de-topologia-como-código-l3}

At L3 the separation between `dev`, `staging` and `prod` ceases to be a convention and becomes an invariant verifiable in the pipeline.  

**Context.** `ARC-011` requires segregation of network, permissions and identity between environments; `ARC-013` requires the topology to be validated automatically in CI/CD, with promotion blocked on failure. Without operationalisation, segmentation remains an intention in a diagram — with no guarantee that the real state of the environments respects it, nor detection of *drift* when someone reuses credentials or opens undue *peering* between `staging` and `prod`. US-07 covers generic automatable validation; this US prescribes the specific verification of segmentation and topology as code for high-risk applications.  

:::userstory
**Story.**   
As **DevOps/SRE** and **AppSec Engineer**, I want to validate automatically, in CI/CD, the segregation of network, permissions and identity between `dev`/`staging`/`prod` and the conformity of the topology with the approved baseline, so that a promotion that violates segmentation is blocked before it reaches production.  

**Acceptance criteria (BDD).**  
- **Given** that an L3 application has `dev`, `staging` and `prod` environments  
  **When** the pipeline runs the topology validation  
  **Then** a verifiable output is produced that confirms segregation of network, permissions and identity between environments (no *cross-env* credentials), with execution logs archived  
- **Given** that a change introduces *peering*, identity sharing or exposure between environments not foreseen in the baseline  
  **When** the validation runs at promotion  
  **Then** the promotion is blocked and the deviation is recorded for remediation or a formal exception  

**Checklist.**  
- [ ] Network segregation between `dev`/`staging`/`prod` evidenced (VLANs, *namespaces*, *peering policies*)  
- [ ] Identity and permission segregation evidenced (distinct IAM/*service accounts*, no *cross-env* credentials)  
- [ ] CI job validates topology as code (e.g. diagrams-as-code, Cartography, `checkov`/Terraform checks) with logs available  
- [ ] Validation failure blocks the promotion; a deviation generates a remediation record or an approved exception  

:::

**Artefacts & evidence.** Topology validation job configuration (`ci-pipeline.*`); `ci-architecture-report.*` with segregation and topology output; IaC evidence of network/identity segregation; blocking/remediation record (PR/issue).  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Not mandatory | Recommended: documented segregation of environments | Mandatory: verifiable segregation of network/permissions/identity + topology-as-code validation in CI/CD with promotion blocking (`ARC-011`, `ARC-013`) |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| CI/CD | Promotion between environments (L3) | DevOps/SRE + AppSec Engineer | On every promotion; immediate blocking on failure |

**Useful links.** [Architectural requirements catalogue (ARC-011, ARC-013)](./addon/catalogo-requisitos-arquitetura) · [Ch. 7 - Secure CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro)

---

### US-18 - Architectural patterns for non-agentic AI/ML systems {#us-18---padrões-arquitetónicos-para-sistemas-aiml-não-agentic}

Systems that integrate LLMs, predictive models or RAG without *tool-use* require trust boundaries and controls of their own, distinct from the agentic case.  

**Context.** US-15 addresses non-deterministic components in general and US-16 covers the autonomous agent with *tool-use* (`ARC-015`). What remains is to operationalise `ARC-014` for the **non-agentic** case — LLMs in a conversational interface, predictive models and RAG that produce *output* but do not perform actions on external systems. Here the attack surface is the model itself and its data: direct and indirect prompt injection (LLM01-2025, `AML.T0051.001`), *training data poisoning* (`AML.T0020`), *model theft* (ML05-2023) and the absence of provenance for models/datasets (LLM03-2025). The architecture has to mark the *training-time* and *inference-time* trust boundaries explicitly and treat the AI as a distinct participant in the DFD, not as an opaque library.  

:::userstory
**Story.**   
As **Software Architects** and **AppSec Engineer**, I want to apply architectural patterns dedicated to non-agentic AI/ML systems, with explicit trust boundaries, anti-prompt-injection controls and provenance of models/datasets, so that the AI-specific risk is contained and auditable at the architecture level.  

**Acceptance criteria (BDD).**  
- **Given** that the solution integrates an AI/ML component that produces *output* without invoking *tools* (conversational LLM, predictive model, RAG)  
  **When** I design or review the architecture  
  **Then** the DFD marks the *training-time* and *inference-time* trust boundaries, with the AI as a distinct participant, and the boundary controls are documented  
- **Given** that there is user input or external content in the model's context  
  **When** I specify the architectural controls  
  **Then** there is *input sanitisation* and *output filtering* against direct and indirect prompt injection, *rate limiting* and isolation of the calls to the model  
- **Given** that the system uses models and datasets  
  **When** I record the provenance  
  **Then** the origin and version of models and datasets are documented, with explicit consideration of *model theft* and *training data poisoning*  

**Checklist.**  
- [ ] *Training-time* and *inference-time* trust boundaries marked in the DFD, with the AI as a distinct participant  
- [ ] Anti-prompt-injection controls (input/output) for direct and indirect injection (LLM01-2025, `AML.T0051.001`)  
- [ ] *Rate limiting* and isolation of the calls to the inference model  
- [ ] Provenance of models and datasets documented (`AML.T0010`, LLM03-2025); *model theft* (ML05-2023) and *data poisoning* (`AML.T0020`) scenarios considered  

:::

**Artefacts & evidence.** Update of `solution-architecture.md` with AI/ML trust boundaries; versioned DFD with the AI as a distinct participant; provenance record for models/datasets; link to the AI/ML threat model (Ch. 3).  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Simple identification of the AI/ML component and impact note | Mandatory: trust boundaries, anti-prompt-injection controls and provenance documented (`ARC-014`) | Mandatory + reinforced isolation of the calls to the model and independent review of the AI/ML architecture |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Design / Review | Introduction or change of a non-agentic AI/ML component | Software Architects + AppSec Engineer | Before design approval |

**Useful links.** [`ARC-014` — AI/ML architectural patterns](./addon/catalogo-requisitos-arquitetura#arc-014) · [Advanced Recommendations — §AI/ML](./recomendacoes-avancadas#ai-ml) · [Ch. 3 - AI/ML Methodologies](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#ai-ml)

---

## 📑 Expected artefacts {#-artefactos-esperados}

| Artefact | Origin / US | Associated evidence |
|---|---|---|
| `principios-arquitetura.md` | US-01 | Commit + approval |
| `solution-architecture.md` | US-02 | PR/issue + approval |
| `design-review.md` | US-03 | Review record + backlog |
| `adr/ADR-XXXX.md` | US-04 | ADR + approval |
| `trust-boundaries.md` | US-05 | Inventory + controls |
| `integration-review.md` | US-05 | Review per integration |
| `architecture-update.md` | US-06 | Update + review |
| `ci-architecture-report.*` | US-07 | Pipeline artefacts |
| `impacto-arquitetura.md` | US-08 | Record + backlog |
| `excecao-arquitetura.md` | US-10 | Exception + *sunset* + compensations |
| `arquitetura-triggers.md` | US-11 | List + execution evidence |
| `checklist-arquitetura.md` | US-12 | Gate + approvals |
| `modelos-referencia.md` | US-13 | Catalogue + changelog |
| `governance-checklist-l3.md` | US-14 | Formal opinion |

---

## ⚖️ Proportionality matrix (L1–L3) {#️-matriz-de-proporcionalidade-l1l3}

| Level | Application of Secure Architecture practices |
|---|---|
| L1 | Minimum principles; decisions (ADR) for high impact only; critical integrations; simplified gate where applicable; minimum triggers |
| L2 | Full principles; detailed sheet; formal review; ADRs for significant decisions; formal exceptions; automatable validations where applicable; synchronisation with threat modelling |
| L3 | Full coverage; segregation of duties; reinforced evidence; formal governance; rigorous gates; independent review where applicable; “living architecture” discipline |

---

## 📌 Final recommendations {#-recomendações-finais}

- Centralise artefacts in a versioned repository referenceable per release (baseline, ADRs, integrations, exceptions).
- Treat **external dependencies** and **implicit flows** (observability) as part of the architecture, with decision and evidence.
- Integrate automatable validations into the pipeline **as evidence generation**, not as a substitute for human review.
- Use a *sunset* and periodic review for architectural exceptions, avoiding permanent structural debt.
