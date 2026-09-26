---
id: aplicacao-lifecycle
title: How to Do It
description: Integration of requirements practices throughout the phases of the development lifecycle
tags: [tipo:aplicacao, ciclo-vida, requisitos, validacao, rastreabilidade, excecoes]
genia: us-format-normalization
translation:
  source_locale: pt
  source_path: 010-sbd-manual/02-requisitos-seguranca/aplicacao-lifecycle.md
  source_sha256: 40e5a02ac36f1761c0df8e75208e2a419c94dd9323fefa9e7428d52f13374a86
  source_commit: 112711064196b71c545672fe3fb3ae412b36575e
  target_sha256: c75f0e88cb5ec3294ef9a382da280957fd85ffbbcbf9fccc271804930ecc0a69
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: da8c4621ee3f200794cd49e34ddc29239ba89f55effb1e5e578d388e50580b8d
  glossary_keys: [alcada, audit_trail, avaliacao, chapter_role, como_fazer, cycle_iteration, discipline, esquema_regime, framework_source_corpus, lifecycle_phase, mapping, maturity, papel_suporte, provenance, requirement_runtime, risk_level, role_tech_lead, schema, threat, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: a137adfde19217cfcc327ddf6dfc0092750e7fc52087370a1c253aff8002cc80
  translated_at: 2026-09-26T17:58:13Z
  reviewed_by: null
---

# Applying Security Requirements in the Lifecycle

This document prescribes **how to apply systematically the requirements defined in Chapter 2** throughout the development lifecycle, ensuring **traceability**, **proportionality to risk**, **continuous validation** and an **explicit discipline of review/versioning**.

It includes reusable *user story* templates, actions per role, expected artefacts and application tables per criticality level (L1–L3).

> **Framing note:** L1–L3 classify the **application's risk** (impact and exposure).  
> Process characteristics (e.g. a high degree of automation, artefact generation, third-party dependency) **do not change the classification**, but may demand greater rigour in validation, evidence and operational control.

> **Requirement governance principle:** a security requirement must not be treated as a static declaration. Whenever material changes occur in the risk, the data processed, the exposed surface, the architecture or the integrations, the team must reassess the set of applicable requirements, record the review decision and update the traceability chain to *Threat Modelling*, validation and exceptions, where they exist.

---

## 📅 When to apply security requirements {#-quando-aplicar-os-requisitos-de-segurança}

| Phase / Event                    | Expected action                                                                 | Main artefact                      |
| -------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------- |
| Project start                | Proportional selection of requirements based on criticality                    | `matriz-controlos-por-risco.md`          |
| Grooming / Planning           | Turn requirements into traceable cards                                 | Backlog (cards + `SEC-...` tags)         |
| New feature / refactor   | Revalidate applicable requirements, record the review decision and update links to risk, threat and validation | Story/technical task + review record |
| Integration or external exposure  | Review authentication, logging, access control and API requirements, updating the baseline and operational tags where applicable | Integration issue/checklist + updated baseline |
| Sprint review / Testing           | Verify security acceptance criteria and collect evidence            | Criteria + tests + evidence          |
| Preparation for go-live / release| Validate applied requirements, approved exceptions, coverage and evidence       | Release checklist + attached evidence |

---

## 🔁 Re-trigger and versioning rule {#-regra-de-re-trigger-e-versionamento}

The set of applicable security requirements must be **explicitly reviewed** whenever there is a material change in at least one of the following axes:

- classification or exposure of the application;
- architecture, trust boundaries or external integrations;
- data processed, sensitivity or specific obligations;
- technical mechanism for implementing or validating a control;
- approved exceptions that change how the requirement is satisfied or verified.

When the review takes place, the expected outcome is not merely to “verbally confirm” that the requirement still holds. There must be at least:

- an update or confirmation of the baseline of applicable requirements;
- a record of the review decision and of its *owner*;
- maintenance of the link to *Threat Modelling*, when the requirement stems from a specific risk or threat;
- maintenance of the link to validation and to the expected evidence;
- an update of exceptions and of their revalidation deadline, where they exist.

---

## 👥 Who does what {#-quem-faz-o-quê}

| Role / Function                      | Key responsibilities                                                                 |
| ----------------------------------- | ---------------------------------------------------------------------------------------- |
| Product Owner                  | Ensure integration into the backlog; ensure that relevant requirements exist as traceable work |
| Developer                           | Implement controls; apply tags; link changes to `SEC-Lx-*` and/or to the catalogue requirement; propose exceptions when necessary |
| QA                                  | Define acceptance and validation criteria; ensure test coverage and evidence     |
| Software Architects / Tech Lead / DevOps / SRE | Review requirements in critical changes; ensure technical coherence and impact on risk  |
| AppSec Engineer                     | Validate application; approve exceptions; ensure overall alignment and consistency          |
| GRC / Compliance (where applicable) | Record exceptions and decisions; support auditing and organisational traceability          |

> ✅ Traceability and verifiability are shared responsibilities;  
> **final responsibility for risk decisions and exceptions must always be explicit.**

---

## 📝 Reusable User Stories and Cards {#-user-stories-e-cartões-reutilizáveis}

### US-01 - Selection of requirements by criticality {#us-01---seleção-de-requisitos-por-criticidade}

**Context.**  
The initial selection of requirements must be proportional to the application's risk (L1–L3).

:::userstory
**Story.**  
As a **Product Owner**, I want to select the requirements applicable to the project, so that security is proportional to the risk level.

**Acceptance criteria (BDD).**
- **Given** that the application has an assigned criticality level  
  **When** I consult the appropriate requirements application matrix  
  **Then** I mark in the backlog the requirements applicable to the defined level and record the evidence of the decision

**Checklist.**
- [ ] Criticality classification (L1–L3) assigned  
- [ ] Application matrix used (`SEC-Lx-...`)  
- [ ] Requirements marked in the backlog  
- [ ] Evidence documented in the project repository

:::

**Artefacts & evidence.**
- Artefact: `matriz-controlos-por-risco.md`  
- Evidence: backlog with `SEC-Lx-*` tags and a reference to the project's Lx level

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Recommended | Essential subset |
| L2 | Yes | Full catalogue applicable to L2 |
| L3 | Yes | Full catalogue applicable to L3 + reinforcements |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Start | Project kick-off | Product Owner | Before the initial backlog |

---

### US-02 - Review upon relevant change {#us-02---revisão-por-alteração-relevante}

**Context.**  
Applicable requirements must be reviewed whenever there is a material change in the technical context, exposure surface, data processed or architecture.

:::userstory
**Story.**  
As **Software Architects / Tech Lead** and **Scrum Master / Team Lead**, I want to review applicable requirements whenever a critical integration or relevant change occurs, so that the selected controls and requirements are updated, traced and validated.

**Acceptance criteria (BDD).**
- **Given** that a significant change occurs (external integration, change of data, exposure, architecture)
  **When** the team analyses the technical and risk impact
  **Then** the team updates the selection of requirements, creates/updates work in the backlog with `SEC-Lx-*` tags and, if applicable, triggers a new Threat Modelling

**Acceptance criteria (DoD).**
- [ ] Selection/matrix updated and recorded (including new applicable requirements)
- [ ] If the change affects risk: Threat Modelling trigger recorded
- [ ] Backlog cards marked with `SEC-Lx-*` and owner defined
- [ ] Evidence: PR/issue with the relevant links (e.g. requirement ↔ change ↔ risk)
- [ ] Notification to AppSec for validation (L2/L3 or critical changes)

:::

**Artefacts & evidence.**
- `matriz-controlos-por-risco.md` updated; PR/issue; wiki/architecture diagram; decision record and notification

**Proportionality.**
- L1: ad-hoc review; L2: mandatory review; L3: mandatory review + AppSec validation

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Design/Refactor | Change of architecture, data or exposure | Software Architects + Tech Lead | Before the release |

**Useful links.**
- 🔗 [Requirements validation and review](./addon/validacao-requisitos)
- 🔗 [Traceability taxonomy](./addon/rastreabilidade-controlo)

---

### US-03 - Exception Management with TTL and Mandatory Revalidation {#us-03---gestão-de-exceções-com-ttl-e-revalidação-obrigatória}

**Context.**  
Not all requirements are applicable. Exceptions must be documented, justified, approved and subject to revalidation, avoiding permanent exceptions.

:::userstory
**Story.**  
As a **Developer** (proposer) and **GRC/Compliance** (recorder), I want to record exceptions with a TTL and an approval flow by **AppSec** (technical) and **Executive Management/CISO** (where applicable), so that all exceptions are time-bound, traceable and revalidated.

**Acceptance criteria (BDD).**
- **Given** that a requirement cannot be applied
  **When** the team records an exception (unique ID) with justification and TTL
  **Then** the exception has a defined owner, an alert configured before expiry and re-approval required for renewal

**Acceptance criteria (DoD).**
- [ ] Exception with ID and link to the requirement (`SEC-Lx-...` and/or requirement ID) recorded
- [ ] TTL defined in accordance with the master exceptions policy ([Canonical Exception Management Process](/sbd-toe/sbd-manual/governanca-contratacao/addon/processo-excecoes), Ch. 14): default maximum period, extension only with reassessment
- [ ] Owner designated and alert recipients defined
- [ ] Technical approval by AppSec documented; executive approval where applicable at L3
- [ ] Automatic alerts configured (e.g. 15 days before expiry)
- [ ] Evidence of revalidation, mitigation or closure attached

:::

**Artefacts & evidence.**
- `excecoes/EXC-YYYY-N.md` (or GRC ticket); alert logs; history of decisions and approvers

> **Reference:** This user story specialises the organisational exception process (Ch. 14) for the requirements context. TTL, approval authorities and revalidation must follow the master policy defined in that chapter.

**Proportionality.**
- L1: simplified process; L2: mandatory formalisation; L3: formal + mitigation required

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Planning/Release | Identification of the exception | Developer + AppSec Engineer + GRC / Compliance | Before the release |

**Useful links.**
- 🔗 [Exception management](./addon/gestao-excecoes)

---

### US-04 - Requirements traceability {#us-04---rastreabilidade-de-requisitos}

**Context.**  
All applied requirements must be traceable in the backlog and auditable.

:::userstory
**Story.**  
As a **QA role**, I want to ensure that all applied requirements have traceability in the backlog, so that auditing and verification are supported.

**Acceptance criteria (BDD).**
- **Given** that the applicable requirements have been selected  
  **When** I review the backlog and PRs  
  **Then** I find associated work with `SEC-Lx-*` tags and traceable references to the validations/evidence

**Checklist.**
- [ ] All relevant cards have a `SEC-Lx-Tyy-ZZZ` tag (or as per the taxonomy)
- [ ] Cross-reference with the catalogue of applicable requirements
- [ ] Exportable reports (audit)
- [ ] Traceability evidence archived

:::

**Artefacts & evidence.**
- Artefact: development board  
- Evidence: traceability report/export and links to validations

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Recommended | Critical requirements only |
| L2 | Yes | Full coverage of the selected requirements |
| L3 | Yes | Full coverage + reinforced traceability |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Grooming | Backlog review | QA | Per sprint |

**Useful links.**
- 🔗 [Traceability taxonomy](./addon/rastreabilidade-controlo)

---

### US-05 - Definition of validation criteria {#us-05---definição-de-critérios-de-validação}

**Context.**  
Each selected requirement must have explicit and verifiable acceptance/validation criteria.

:::userstory
**Story.**  
As a **Product Owner/QA role**, I want to ensure that each requirement selected in the backlog contains clear security acceptance criteria, so that they can be validated and tested consistently.

**Acceptance criteria (BDD).**
- **Given** that a requirement is selected  
  **When** I place it in the backlog  
  **Then** I add formal and verifiable acceptance/validation criteria

**Checklist.**
- [ ] Criteria defined on the card  
- [ ] Alignment with the applicable catalogue
- [ ] Validation planned in tests and/or reviews
- [ ] Evidence recorded and traceable

:::

**Artefacts & evidence.**
- Artefact: backlog  
- Evidence: cards/documents with criteria and links to validations

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Recommended | For critical requirements |
| L2 | Yes | For all selected requirements |
| L3 | Yes | For all + reinforced validation |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Planning | Creation of cards | Product Owner + QA | Before the sprint |

**Useful links.**
- 🔗 [Requirements validation](./addon/validacao-requisitos)

---

### US-06 - Validation of test coverage {#us-06---validação-de-cobertura-de-testes}

**Context.**  
Requirements must have associated validation to prevent regressions and ensure effectiveness.

:::userstory
**Story.**  
As a **QA role**, I want to ensure that the applicable requirements have associated validation, so that absence of control is prevented and auditable evidence is supported.

**Acceptance criteria (BDD).**
- **Given** that requirements have been applied  
  **When** I run the validation tests/reviews  
  **Then** I obtain documented and traceable evidence of the result

**Checklist.**
- [ ] Automated or manual tests documented  
- [ ] Acceptance criteria defined  
- [ ] Evidence of execution per sprint/release  
- [ ] Logs/reports archived in CI/CD where applicable

:::

**Artefacts & evidence.**
- Artefact: test/validation plans  
- Evidence: logs, reports, screenshots, reviews, results

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Recommended | Basic validation of critical requirements |
| L2 | Yes | Full coverage of the selected requirements |
| L3 | Yes | Full coverage + independent review |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Sprint review | Execution of validations | QA | Per sprint |

**Useful links.**
- 🔗 [Requirements validation](./addon/validacao-requisitos)

---

### US-07 - Final validation and approval {#us-07---validação-e-aprovação-final}

**Context.**  
The Security Team must validate the application of the requirements and approve exceptions, formally controlling risk decisions.

:::userstory
**Story.**  
As the **Security Team / AppSec**, I want to validate the application of the requirements and approve exceptions, so that risk decisions are controlled and documented.

**Acceptance criteria (BDD).**
- **Given** that the release is ready  
  **When** I review the applied requirements and exceptions  
  **Then** I approve or reject based on the risk and the available evidence

**Checklist.**
- [ ] Applicable requirements verified (evidence available)
- [ ] Exceptions approved/rejected and recorded
- [ ] Evidence of the decision documented
- [ ] Feedback recorded in the backlog/board

:::

**Artefacts & evidence.**
- Artefact: register of requirements and exceptions  
- Evidence: decision recorded in PR/issue and/or GRC tool

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Recommended | Simplified review |
| L2 | Yes | Formal review |
| L3 | Yes | Formal review + mitigation required |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Release | Final approval | AppSec Engineer | Before go-live |

**Useful links.**
- 🔗 [Exception management](./addon/gestao-excecoes)

---

### US-08 - Project requirements catalogue (creation and maintenance) {#us-08---catálogo-de-requisitos-do-projeto-criação-e-manutenção}

**Context.**  
At project start and whenever there are changes of scope, there must be a **versioned catalogue of project requirements**, derived from the organisational baseline and filtered by criticality.

:::userstory
**Story.**  
As **AppSec/PO/TL**, I want to establish and maintain a catalogue of the project's security requirements, so that consistent, versioned and auditable application is ensured throughout the SDLC.

**Acceptance criteria (BDD).**
- **Given** that the application has a defined L1–L3 criticality  
  **When** I derive the project catalogue from the baseline and filter by level  
  **Then** the catalogue is versioned, with a defined owner and a link to validation criteria

**Checklist.**
- [ ] Project requirements catalogue created/updated and versioned  
- [ ] Owner and review periodicity defined  
- [ ] Mapping to validation criteria and backlog tags  
- [ ] Persistent location and link in the repository

:::

**Artefacts & evidence.**
- Artefact: `catalogo-requisitos.md` (or `catalogo/` folder) + changelog  
- Evidence: MR/PR of creation/update and approval by AppSec

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Pre-approved essential subset |
| L2 | Yes | Full catalogue applicable to L2 |
| L3 | Yes | Catalogue applicable to L3 + relevant reinforcements |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Start | Kick-off / major release | AppSec Engineer + Product Owner + Tech Lead | Before the initial backlog / before the release |

**Useful links.**
- 🔗 [Requirements catalogue](./addon/catalogo-requisitos)  
- 🔗 [Acceptance criteria](./addon/criterios-aceitacao)

---

### US-09 - Validation per requirement/domain (REQ-XXX → evidence) {#us-09---validação-por-requisitodomínio-req-xxx--evidência}

**Context.**  
Each active requirement must have associated validation and evidence.

:::userstory
**Story.**  
As **QA/AppSec/TL**, I want to validate each requirement of the catalogue according to the defined criteria, so that objective and traceable evidence of its fulfilment is ensured.

**Acceptance criteria (BDD).**
- **Given** a catalogue requirement with defined criteria  
  **When** I run the associated validation  
  **Then** I record the result and attach evidence to the requirement

**Checklist.**
- [ ] Validation method defined per requirement  
- [ ] Execution recorded per sprint/release  
- [ ] Result and evidence linked to the requirement  
- [ ] Review and approval by AppSec where applicable

:::

**Artefacts & evidence.**
- Artefact: `validacoes/REQ-XXX.md` (or equivalent)  
- Evidence: CI/CD logs, reports (SAST/DAST/IAST), reviews, screenshots

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Minimum coverage of critical requirements |
| L2 | Yes | Full coverage of the selected requirements |
| L3 | Yes | Full coverage + independent review and automatic gates |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Testing/Review | Pipelines and checkpoints | QA + AppSec Engineer + Tech Lead | Per sprint and before release |

**Useful links.**
- 🔗 [Requirements validation](./addon/validacao-requisitos)  
- 🔗 [Controls per requirement](./addon/validacao-requisitos)

---

### US-10 - Automatic CI/CD gates for security requirements {#us-10---gates-automáticos-em-cicd-para-requisitos-de-segurança}

**Context.**  
Pipelines must enforce automatic checks aligned with the applicable requirements, blocking merge/release when they fail.

:::userstory
**Story.**  
As a **DevOps/SRE** and **Developer**, I want the CI/CD pipeline to run security checks and enforce *gates*, so that merges and releases only happen when the security requirements are satisfied.

**Acceptance criteria (BDD).**
- **Given** a PR/MR to the main branch
  **When** the pipeline runs the security jobs
  **Then** the merge is blocked if any critical gate fails, and the reports are attached to the PR

**Acceptance criteria (DoD).**
- [ ] SAST run with configured baseline and thresholds
- [ ] SCA run; vulnerabilities above the threshold cause a failure or a blocking issue
- [ ] DAST in staging where applicable (L2/L3 and exposure changes)
- [ ] SBOM generation (CycloneDX or SPDX) attached to the artefact
- [ ] Artefact signing and storage of signature/provenance
- [ ] `policy-check` validates `SEC-Lx-*` tags and links to the requirement in the PR
- [ ] Gate summary linked to the PR/issue

:::

**Artefacts & evidence.**
- CI logs, SAST/SCA/DAST reports, SBOM (`sbom.cdx.json`), signature (`artifact.sig`), gate report

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Recommended | Basic SAST; SCA recommended |
| L2 | Yes | SAST + SCA mandatory; thresholds configured |
| L3 | Yes | SAST + SCA + DAST; strict gates; SBOM + signing mandatory |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Merge/Release | PR/MR targeting main/release | DevOps / SRE + AppSec Engineer | Automatic block until resolved |

**Useful links.**
- 🔗 [Security gates in CI/CD](/sbd-toe/sbd-manual/cicd-seguro/addon/politicas-gates-pipeline)  
- 🔗 [SBOM and provenance](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)

---

### US-11 - SBOM generation and signing of build artefacts {#us-11---geração-de-sbom-e-assinatura-de-artefactos-de-build}

**Context.**  
SBOMs and signatures support provenance and auditing.

:::userstory
**Story.**  
As a **Developer** and **DevOps/SRE**, I want the pipeline to generate an SBOM and sign the final artefact, so that origin, dependencies and integrity can be verified at deployment.

**Acceptance criteria (BDD).**
- **Given** that a release artefact is built
  **When** the build job completes successfully
  **Then** an SBOM is generated and the artefact is signed; both are stored with provenance metadata

**Acceptance criteria (DoD).**
- [ ] SBOM generated (CycloneDX/SPDX) and attached to the build
- [ ] Artefact signed and signature stored in the registry
- [ ] Provenance metadata (who/when/how) recorded
- [ ] Signature verification job available for deploy
- [ ] Key procedures and rotation documented in an internal policy

:::

**Artefacts & evidence.**
- `sbom.cyclonedx.json`, `artifact.sig`, attestations, build metadata

> **Reference:** Specialises the SBOM and provenance process described in Ch. 05 for the requirements context.

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Build | Release build | Developer + DevOps / SRE | Always in the release pipeline |

---

### US-12 - Validation of `SEC-Lx-*` tags and requirements in the pipeline {#us-12---validação-de-tags-sec-lx--e-requisitos-no-pipeline}

**Context.**  
Tags and references must be present to ensure traceability.

:::userstory
**Story.**  
As a **Developer** and **QA role**, I want the pipeline to validate the presence and conformity of `SEC-Lx-*` tags and references to the catalogue requirement, so that traceability and the correct triggering of automatic checks are ensured.

**Acceptance criteria (BDD).**
- **Given** a PR with a functional change
  **When** the `tag-check` job runs
  **Then** the PR fails if there is not at least one valid tag and one traceable reference to the applicable requirement; the automatic comment explains what is missing

**Acceptance criteria (DoD).**
- [ ] `tag-check` job present and executable
- [ ] Format validation in accordance with the chapter's taxonomy
- [ ] Check of the reference/link to the requirement where applicable
- [ ] Automatic comment on the PR with instructions on failure

:::

**Artefacts & evidence.**
- `tag-check` logs, PR templates, examples of conformant PRs

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| PR/MR | PR creation | Developer + DevOps / SRE | Before merge |

---

### US-13 - Policy, Training and Operational Procedures {#us-13---política-formação-e-procedimentos-operacionais}

**Context.**  
For consistency, the organisation must publish policies, responsibilities and training.

:::userstory
**Story.**  
As **Executive Management/CISO** and **GRC/Compliance**, I want to publish the requirements application policy and provide training, so that teams know the procedures, SLAs and operation of the controls.

**Acceptance criteria (BDD).**
- **Given** that pipeline and exception management practices exist
  **When** the policy and the operational guides are published
  **Then** teams receive training and an operational checklist, and compliance is assessed within a defined period (e.g. 3 months)

**Acceptance criteria (DoD).**
- [ ] Policy published and versioned
- [ ] Operational playbooks documented
- [ ] Training sessions held and recorded
- [ ] Feedback/FAQ mechanism available
- [ ] Internal assessment/audit after the defined period

:::

**Artefacts & evidence.**
- Published policy; training materials; records; compliance checklist

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Governance | Policy publication/change of practices | CISO + GRC / Compliance | Policy and training within a defined period |

---

### US-14 - Controlled use of automated assistants (including AI) in development {#us-14---uso-controlado-de-assistentes-automatizados-incluindo-ia-no-desenvolvimento}

**Context.**  
The use of automated assistants and AI-based tools can speed up development, but **neither changes nor replaces** the application security requirements. All generated output must be treated as third-party code and subject to explicit governance, validation and traceability.

:::userstory
**Story.**  
As a **Developer**, **Tech Lead** and **AppSec Engineer**, I want to ensure that any code, configuration or test generated with the help of automated assistants (including AI) is explicitly reviewed, validated and traceable, so that fulfilment of the security requirements is verifiable and responsibility remains human.

**Acceptance criteria (BDD).**
- **Given** that an automated assistant is used to generate code, configuration or tests  
  **When** the output is integrated into the repository  
  **Then** the artefact is subject to human review, automatic validation in CI/CD and linked to the applicable catalogue requirements

**Acceptance criteria (DoD).**
- [ ] Generated code/configuration identified in the PR/MR (note or PR template)
- [ ] Human review carried out and approved (formal code review)
- [ ] Security gates in CI/CD run (SAST, SCA and others as applicable)
- [ ] Catalogue requirements and `SEC-Lx-*` tags referenced in the PR/MR
- [ ] Validation evidence archived (pipeline logs, reports, approvals)
- [ ] No secret, credential or sensitive data included in prompts or generated artefacts

:::

**Artefacts & evidence.**
- PR/MR with a reference to the requirement and `SEC-Lx-*` tags
- CI/CD logs (SAST, SCA, tests)
- Code review approval
- Security gates report

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Recommended | Human review and basic SAST |
| L2 | Yes | Review + SAST/SCA mandatory |
| L3 | Yes | Review + SAST/SCA + reinforced validations and AppSec review |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| PR/MR | Introduction of generated code/configuration | Developer + Tech Lead | Before the merge |
| Release | Final security gate | AppSec Engineer | Before go-live |

**Useful links.**
- 🔗 [Governance of the use of automation](./addon/governanca-automatismos)
- 🔗 [Automatic gates in CI/CD](/sbd-toe/sbd-manual/cicd-seguro/addon/politicas-gates-pipeline)
- 🔗 [Requirements validation](./addon/validacao-requisitos)

---

### US-15 - Classification and recording of the AI agent *mandate* {#us-15}

**Context.**
When moving from **assistants that suggest** to **agents that execute** (creating PRs, reading secrets, *deploy*, writing to external systems), it is no longer enough to know *"was it reviewed?"* — it is necessary to know *"was it authorised to do this, in this context, with this reach?"*. That authorisation is operationalised through the five-level autonomy model (A0–A4) and the *mandate* — a versioned document in VCS that records who decided, with what authority, for how long, and with what *kill-switch*.

:::userstory
**Story.**
As an **AppSec Engineer** and **Tech Lead**, I want to classify the autonomy level (A0–A4) of each AI agent in operational use and record its *mandate* versioned in VCS, so that each agent operates under explicit, auditable authorisation proportional to the risk of the context.

**Acceptance criteria (BDD).**
- **Given** that an AI agent is going to operate in the project at A1 or above
  **When** its operational activation is proposed
  **Then** there is a *mandate* recorded in VCS with `agent_id`, *runtime* + *pinned* model, `autonomy_level`, `scope`, `tools_allowlist`, `identity_ref`, `owner`, `approver`, `kill_switch`, `intent_audit_sink`, `review_cadence`, `effective_window` and `risk_residual`
- **Given** that the autonomy level, the *scope* or the `tools_allowlist` changes
  **When** operation is to continue
  **Then** a new Proposal → Approval cycle is run; informal *amendments* are prohibited

**Acceptance criteria (DoD).**
- [ ] *Mandate* present in VCS, validated against the minimum schema (mandatory fields) and referenced by `mandate_ref` in audit
- [ ] `autonomy_level` classified according to [levels A0–A4](./addon/governanca-automatismos#niveis-autonomia) and justified in writing
- [ ] *Approver* appropriate to the level (A1: Tech Lead; A2: Tech Lead + AppSec Engineer; A3: Tech Lead + AppSec Engineer + GRC / Compliance; A4: `CISO` with formal sign-off)
- [ ] Ephemeral *identity* configured (no reuse of human credentials)
- [ ] *Kill-switch* exercised in sandbox/staging with the timing recorded before activation
- [ ] `effective_until` defined — no *mandates* without a validity window
- [ ] *Mandate* indexed in the organisational register of active *mandates*

:::

**Artefacts & evidence.**
- *Mandate* file in VCS (Markdown or YAML) with version history
- Approval record (signed commit + identification of the *approver*)
- *Log* of the *kill-switch* exercise (initial entry + cadence)
- Organisational inventory of active *mandates*
- Audit *trail* with `mandate_ref` on each *tool invocation*

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | A1+ | Simple *mandate*; approval by Tech Lead; A2+ allowed only outside production |
| L2 | A1+ | Full *mandate*; *kill-switch* exercised quarterly at A3 |
| L3 | A1+ | Full *mandate* + quarterly organisational review; A4 requires formal sign-off by the `CISO` |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Activation | Request to operate an agent at A1+ | *Owner* + AppSec Engineer | Before the first *tool call* |
| Review | `review_cadence` or material change | *Owner* + AppSec Engineer | As per the declared cadence |
| Revocation | *Off-policy action*, *credential exposure*, *kill-switch* failure | *Owner* + AppSec Engineer | Immediate via *kill-switch* |

**Useful links.**
- 🔗 [Autonomy levels A0–A4](./addon/governanca-automatismos#niveis-autonomia)
- 🔗 [`REQ-AGN-*` catalogue](./addon/governanca-automatismos#req-agn)
- 🔗 [Policy 38 — AI Agent Mandates](/sbd-toe/assets/policies/policy-mandates-agentes)
- 🔗 [Policy 16 — Use of Support Tools (section 11)](/sbd-toe/assets/policies/policy-uso-ferramentas-apoio)

---

### US-16 - Classification of the control type in the traceability matrix {#us-16---classificação-do-tipo-de-controlo-na-matriz-de-rastreabilidade}

Each traced requirement must declare the nature of the control — Preventive, Detective or Corrective.  

**Context.** The traceability matrix links risk → requirement → control → validation → evidence, but without classifying the **control type** the coverage is blind to the defensive balance: an application may accumulate preventive controls and have no detection or correction capability at all. Making the type explicit allows that balance to be audited per row of the matrix.  

:::userstory
**Story.**   
As **Software Architects / DevOps / SRE**, I want to classify each control in the traceability matrix as Preventive, Detective or Corrective, so that balanced and auditable defensive coverage per requirement is ensured.  

**Acceptance criteria (BDD).**  
- **Given** a row of the matrix linking a risk to a requirement  
  **When** the associated control is recorded  
  **Then** the `Tipo de Controlo` field takes one of `Preventivo`/`Detetivo`/`Corretivo` and is filled in on all active rows  

**Checklist.**  
- [ ] `Tipo de Controlo` column present and filled in on all rows of the matrix  
- [ ] Value restricted to the vocabulary `Preventivo`/`Detetivo`/`Corretivo`  
- [ ] Defensive balance review recorded (absence of detection/correction flagged)  

:::

**Artefacts & evidence.** Versioned traceability matrix with the `Tipo de Controlo` column filled in; defensive balance review note.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Type declared for critical controls | Type declared for all selected requirements | Type declared + formal review of the Prev/Det/Corr balance per release |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Design/Grooming | Recording of the control in the matrix | Software Architects / DevOps / SRE | Before validation of the requirement |

**Useful links.** [Traceability model between risks, requirements and controls](./addon/rastreabilidade-controlo)

---

### US-17 - Incorporation of legal, regulatory and contractual constraints {#us-17---incorporação-de-restrições-legais-normativas-e-contratuais}

The selection of requirements must absorb the legal, regulatory and contractual obligations applicable to the context.  

**Context.** Proportionality to risk determines what is essential, but does not capture external obligations: legislation (e.g. data protection), sector standards and contractual clauses with clients or third parties may impose additional requirements or stricter acceptance criteria. Without an explicit incorporation step, these obligations remain unmapped until they are discovered late, in an audit.  

:::userstory
**Story.**   
As **GRC/Compliance** and **Architecture**, I want to incorporate the applicable legal, regulatory and contractual constraints into the selection of requirements, so that the project catalogue reflects external obligations and not only technical risk.  

**Acceptance criteria (BDD).**  
- **Given** that the project has identified legal, regulatory or contractual obligations  
  **When** the project requirements catalogue is established or reviewed  
  **Then** each applicable obligation is mapped to a requirement (or a recorded exception) and linked to its normative source  

**Checklist.**  
- [ ] Survey of the applicable legal/regulatory/contractual obligations documented  
- [ ] Each obligation mapped to a catalogue requirement or to a formal exception  
- [ ] Normative source referenced and compliance owner defined  

:::

**Artefacts & evidence.** Register of applicable obligations with requirement↔source mapping; updated project requirements catalogue; GRC approval.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Essential legal obligations identified | Survey documented and mapped | Formal survey + GRC validation and review upon change of contractual context |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Start/Review | Kick-off or new legal/contractual obligation | GRC / Compliance + Software Architects | Before closing the project catalogue |

**Useful links.** [Requirements catalogue](./addon/catalogo-requisitos)

---

### US-18 - Intent declaration per destructive tool-call of an AI agent {#us-18---intent-declaration-por-tool-call-destrutivo-de-agente-ai}

Before each destructive action or action with external effect, the AI agent declares an auditable intent.  

**Context.** The *mandate* (US-15) authorises the agent and configures the *intent_audit_sink*, but does not impose per-action verification: what is missing is a Definition of Done confirming, per destructive *tool-call* (delete, write to an external system, rotate secrets, *commit/push*, *deploy*), that the A2+ agent declares **what it is going to do and why** before doing it, and that the gate audits *intent* vs. actual action after the fact. Without this per-action control, the global authorisation does not translate into a verifiable trail of each risky operation. Operationalises `REQ-AGN-004`.  

:::userstory
**Story.**   
As an **AppSec Engineer** and **Tech Lead**, I want each A2+ AI agent to declare its intent as an *audit event* before each destructive *tool-call*, so that each risky action is preceded by an auditable declaration that can be reconciled with the actual action.  

**Acceptance criteria (BDD).**  
- **Given** an A2+ AI agent operating under an active *mandate*  
  **When** it is about to invoke a destructive *tool-call* or one with external effect  
  **Then** it emits a structured *audit event* (what + why + `mandate_ref`) before execution, and the gate reconciles the declared *intent* vs. the actual action after the fact  

**Checklist.**  
- [ ] *Intent audit event* emitted before each destructive *tool-call* (delete/external write/rotate secrets/commit-push/deploy)  
- [ ] Structured event contains the intended action, the justification and `mandate_ref`  
- [ ] Reconciliation of *intent* vs. actual action executed and divergences flagged  

:::

**Artefacts & evidence.** *Audit trail* with *intent events* per *tool-call*; reconciliation report of *intent* vs. actual action; link to the agent's *mandate_ref*.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Not mandatory (A2+ only outside production) | Intent declaration mandatory at A2+ | Intent declaration mandatory + reconciliation audited per release |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Runtime | Destructive *tool-call* of an A2+ agent | Owner + AppSec Engineer | Before each execution; reconciliation after the fact |

**Useful links.** [`REQ-AGN-*` catalogue (REQ-AGN-004)](./addon/governanca-automatismos#req-agn)

---

### US-19 - Collection and thresholds of the RQS indicators {#us-19---recolha-e-thresholds-dos-indicadores-rqs}

The RQS indicators of coverage, traceability and validation are collected and compared against the level's thresholds.  

**Context.** The RQS catalogue defines indicators that measure not the declaration but the evidence of effective application of the requirements. Without an explicit step of collection and comparison against the thresholds per level, the risk of declarative compliance remains: an application may list applied requirements without these being validated. Operationalising the collection makes RQS maturity visible and actionable.  

:::userstory
**Story.**   
As **GRC/Compliance** and **AppSec**, I want to collect the RQS indicators and compare them against the thresholds of the risk level, so that the coverage, traceability and effective validation of the requirements become visible and ungoverned gaps are acted upon.  

**Acceptance criteria (BDD).**  
- **Given** an application with mapped requirements and a defined risk level  
  **When** the RQS collection cycle is run (per release/half-yearly, depending on the indicator)  
  **Then** each RQS indicator is calculated, compared against the level's threshold, and the deviations (incl. RQS-K06 = 0) are recorded and acted upon  

**Checklist.**  
- [ ] Indicators RQS-K01..K06 calculated at the defined periodicity  
- [ ] Comparison against the level's threshold (L1/L2/L3) recorded  
- [ ] Ungoverned gaps (RQS-K06) handled with the SLA of a critical finding  

:::

**Artefacts & evidence.** RQS report per application with values vs. thresholds; register of deviations and remediation plan; evidence of handling of RQS-K06.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| RQS-K01/K02/K06 at the L1 thresholds | RQS-K01–K06 at the L2 thresholds | RQS-K01–K06 at the L3 thresholds + formal review of deviations |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Governance/Release | Collection cycle (per release/half-yearly) | GRC / Compliance + AppSec Engineer | As per the indicator's period |

**Useful links.** [KPIs and metrics — RQS indicators](./addon/kpis-metricas-requisitos)

---

## ⚖️ Proportional application by risk level (L1–L2–L3) {#️-aplicação-proporcional-por-nível-de-risco-l1l2l3}

| Practice                    | L1 (low risk)               | L2 (medium risk)                          | L3 (high risk)                                      |
| -------------------------- | ------------------------------ | ----------------------------------------- | ---------------------------------------------------- |
| Requirements catalogue     | Essential subset          | Full catalogue applicable to L2          | Full catalogue applicable to L3 + relevant reinforcements |
| Traceability (tags)     | Recommended                    | Mandatory on security cards      | Mandatory on technical and functional cards          |
| Exceptions                   | Simplified                   | Documented and approved                  | Formalised with a short TTL and mitigation                |
| Requirements validation    | Basic review/validation        | Associated tests and evidence             | Tests + evidence + independent review             |
| Reassessment upon changes | On request                        | On every critical change                   | Whenever there is a change of exposure/architecture/control |

---

## 📄 Templates and expected artefacts {#-templates-e-artefactos-esperados}

| Artefact                       | Suggested format           | Where to store / reference            |
| ------------------------------- | -------------------------- | ------------------------------------- |
| Requirements matrix by risk  | Markdown / table          | `docs/` or product Wiki            |
| Cards with `SEC-*` tags        | Board / GitHub / Jira      | Team backlog                     |
| Project requirements catalogue | Markdown / files       | `docs/req/` (or equivalent)          |
| Justification of exceptions        | Markdown / issue template  | `excecoes/` or GRC tool         |
| Traceability reports   | Board export / CSV      | Audit archive                  |
| Test plans and evidence    | YAML / Markdown / CI logs  | QA repository and/or CI/CD             |
