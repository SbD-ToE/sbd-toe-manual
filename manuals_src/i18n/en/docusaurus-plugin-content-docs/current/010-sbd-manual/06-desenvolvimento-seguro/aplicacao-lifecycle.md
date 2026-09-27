---
id: aplicacao-lifecycle
title: How to Do It
description: How to apply secure development practices in each phase of the SDLC, with reusable user stories, auditable artefacts and an L1–L3 proportionality matrix
tags: [tipo:aplicacao, ciclo-vida, desenvolvimento, codificacao-segura, validacao, user-stories]
genia: us-format-normalization
translation:
  source_locale: pt
  source_path: 010-sbd-manual/06-desenvolvimento-seguro/aplicacao-lifecycle.md
  source_sha256: d7985dd2a36d4523a448f2210c2f1b96db1af8c1e7ba5d1bde5e3559b9571576
  source_commit: a7cc396e338fab4654022c3d9077a3472e358da2
  target_sha256: 42df4f026e9ad1e50a35835d012b87a19d21d4df0d2e85df7b3b04f7ba84c064
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [audit_trail, chapter_role, como_fazer, cra_support_period, cycle_iteration, discipline, eu_placing_on_market, eu_startups, lifecycle_phase, mapping, practitioner_manual, provenance, requirement_runtime, risk_level, sbdtoe_sbd, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 3bb1fe7ab668390b69d928dc873c34bd5922f2ff88191aecd185bdaa9295916e
  translated_at: 2026-09-27T15:09:22Z
  stamped_at: 2026-09-27T15:09:22Z
  reviewed_by: null
---

# Applying in the Lifecycle - Secure Development

Secure development is neither a theoretical exercise nor a vague “good practice”: it requires consistent application in every phase of the software lifecycle.  
This document shows **how to turn the chapter's prescriptions into daily practice**, detailing when to apply them, who carries them out, which user stories must enter the backlog and which evidence enables audit and governance.  
The goal is simple but ambitious: to make secure development a measurable, traceable habit and an intrinsic part of product quality.

---

## 🧭 When to apply {#-quando-aplicar}

Security accompanies the project from the outset and cannot be relegated to the final phases.  
The following table shows **at which concrete moments of the SDLC** each practice must be applied and the action expected at each of them.

| SDLC Phase          | Specific moment                          | Expected action                                       |
|-----------------------|----------------------------------------------|-----------------------------------------------------|
| Planning           | Definition of stack, dependencies, guidelines | Create/adapt secure guidelines                    |
| Development       | When writing/refactoring code                 | Apply linters, local validations                  |
| Code Review     | On every PR / merge                           | Checklist and formal validation                        |
| Continuous Integration   | Pipeline execution                         | SAST, validation of dependencies and *rulesets*        |
| Pre-production          | Go-live / release                            | Validation of exceptions, final checklist              |
| Operation / Maintenance | Updates, patches, refactorings        | Review of guidelines, dependencies and exceptions      |

---

## 🧱 Secure development gates (proposed → reviewed → validated → accepted) {#-gates-de-desenvolvimento-seguro-proposto--revisto--validado--aceite}

To scale in delivery frequency and diversity of contributions, secure development cannot depend on “trust” in the origin of the code.  
SbD-ToE assumes that **all code is untrusted input** until there is sufficient validation and verifiable evidence.

For this reason, code acceptance must be treated as a process with explicit states:

- **Proposed**: change created, not yet understood or validated (maximum risk).  
- **Reviewed**: human technical understanding confirmed (reduced risk).  
- **Validated**: empirical validation completed (tests + relevant automated validations).  
- **Accepted**: explicit decision to incorporate, assigned to an identifiable role, with recorded evidence.

These states are not “bureaucracy”; they are practical mechanisms for reducing the risk introduced by the development process.

| Gate | Entry state | Mandatory action | Minimum evidence | Responsible role |
|-----|-------------------|------------------|------------------|------------------|
| G1 | Proposed | Structured human review with a checklist | Approval recorded in the PR + checklist | **Scrum Master / Team Lead** (with execution by **Developer** / **Quality Assurance (QA)**) |
| G2 | Reviewed | Automated technical validation | CI/CD reports + logs + tests | **DevOps / SRE** + **Developer** |
| G3 | Validated | Final acceptance decision | Final approval + reference to exceptions | **Scrum Master / Team Lead** (L1) · **AppSec Engineer** (L2/L3) · **Executive Management** (L3 when applicable) |

> Failing a gate implies correction or rejection.  
> A PR must not be “accepted” without passing through G1–G3 with evidence.

---

## 👥 Who carries out each action {#-quem-executa-cada-ação}

Security in development is a **collective effort**: different roles contribute in complementary ways, forming a chain of trust.  
The following table sets out these responsibilities, using **only the roles defined in SbD-ToE**.

| Role (SbD-ToE) | Key responsibilities |
|---|---|
| **Developer** | Apply guidelines, linters and local validations; record deviations and propose *tailoring* when necessary |
| **Quality Assurance (QA)** | Validate quality and security criteria in PRs; confirm criteria and exceptions; support evidence and traceability |
| **Scrum Master / Team Lead** | Ensure execution of G1/G3; confirm checklists; ensure integration into the agile cycle; block merges without evidence |
| **DevOps / SRE** | Automate linters/SAST; version and distribute organisational *rulesets*; apply enforcement and *quality gates* in pipelines |
| **AppSec Engineer** | Define minimum criteria; approve exceptions; validate critical dependencies; map requirements and findings to OWASP/ASVS/CWE; define L1–L3 profiles |
| **Software Architects** | Define standards per stack, structural decisions and baseline guidelines; approve the technical curation of guidelines/rulesets; ensure architectural consistency |
| **Product Owner (PO)** | Prioritise work (including debt and exceptions); ensure that security requirements enter the backlog and are accepted with objective criteria |

> Note: tools may support and automate, but **they do not assume responsibility**.  
> Responsibility for accepting code is always assigned to identifiable human roles.

---

## 📖 Reusable User Stories {#-user-stories-reutilizáveis}

### US-01 - Secure Development Guidelines {#us-01---guidelines-de-desenvolvimento-seguro}

**Context.**  
Clear guidelines, versioned per *stack*, avoid ad-hoc decisions and ensure consistency. More than a static document, they are a **living mechanism** of governance: updated, reviewed and applied daily. The existence of *rulesets* derived from linters and automated analysers, with documented *tailoring*, significantly reduces the risks of subjective interpretation.

:::userstory
**Story.**   
As a **Developer**, I want to apply the approved secure code guidelines, so that consistency is ensured and vulnerabilities are reduced from the start.

**Acceptance criteria (BDD).**
- **Given** that I start development on a defined *stack*  
  **When** I consult the approved guidelines  
  **Then** I apply the mandatory minimum rules and record any justified deviation

**Checklist.**
- [ ] `guidelines-stack.md` referenced in the project README  
- [ ] Linter/analyser configuration files present and versioned  
- [ ] Minimum rules applied  
- [ ] *Tailoring* documented (`rules/README.md`) and approved (by **Software Architects** / **AppSec Engineer** as applicable)  
- [ ] Deviations recorded in `excecoes-seguranca.md`  
- [ ] Evidence of PR review
:::

**Artefacts & evidence.**
- Artefacts: `guidelines-stack.md`, `rules/` directory  
- Evidence: commit IDs + PR history

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|-------|--------------|---------|
| L1    | Yes          | Upstream rules with minimal adjustments |
| L2    | Yes          | Curated organisational set |
| L3    | Yes          | Periodic audit and *policy-as-code* |

**Integration into the SDLC.**
| Phase        | Trigger            | Responsible                                   | SLA              |
|-------------|--------------------|-----------------------------------------------|------------------|
| Planning | Stack definition | **Software Architects** + **Developer**    | Before the 1st sprint |

**Useful links.**  
[Secure Development](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro)

---

### US-02 - Secure Code Review {#us-02---revisão-de-código-segura}

**Context.**  
Code reviews are not only a quality practice but a **security control point**. When systematised with a checklist, they prevent vulnerabilities, promote knowledge sharing and create a formal record of compliance.

:::userstory
**Story.**   
As a **Scrum Master / Team Lead**, I want to ensure that every PR is reviewed with a mandatory security checklist, so that vulnerabilities are prevented and a record of compliance is kept.

*(Carried out by: **Developer** / **Quality Assurance (QA)** under the governance of the **Scrum Master / Team Lead**)*

**Acceptance criteria (BDD).**
- **Given** that a PR is created  
  **When** it is submitted for review  
  **Then** the security checklist is filled in and the PR is only accepted after validation

**Checklist.**
- [ ] `checklist-pr.md` included in the **PR template**  
- [ ] Critical items validated (authentication, inputs, dependencies)  
- [ ] Security comments recorded when applicable  
- [ ] **PR automatically rejected if the checklist is not complete**  
- [ ] The PR only progresses when there is recorded human approval (“reviewed” state)
:::

**Artefacts & evidence.**  
`checklist-pr.md` (PR template), history and comments in the PR

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|-------|--------------|---------|
| L1    | Yes          | Basic checklist |
| L2    | Yes          | Complete checklist + dual review |
| L3    | Yes          | Dedicated security-focused review (includes **AppSec Engineer** when applicable) |

**Integration into the SDLC.**
| Phase              | Trigger  | Responsible                                                     | SLA          |
|-------------------|----------|------------------------------------------------------------------|--------------|
| Code Review | PR opened | **Developer** / **Quality Assurance (QA)** + **Scrum Master / Team Lead** | Before the merge |

---

### US-03 - Dependency Management in Code {#us-03---gestão-de-dependências-no-código}

**Context.**  
Every external dependency added to the project is a potential entry point for supply chain risks. Rigorous management of these dependencies ensures that obsolete, vulnerable or malicious software is not introduced.

:::userstory
**Story.**   
As an **AppSec Engineer**, I want to validate and justify external dependencies, so that supply chain risks are reduced and compliance is ensured.

**Acceptance criteria (BDD).**
- **Given** that a new dependency has been proposed  
  **When** I assess its licence, maintenance and associated CVEs  
  **Then** I approve or reject it with a recorded decision

**Checklist.**
- [ ] Dependency listed in `sbom-deps.json`  
- [ ] Licence compatible with the organisation's policy  
- [ ] No critical CVEs (or formal exception approved)  
- [ ] Decision documented in a ticket
:::

**Artefacts & evidence.**
- Artefact: `sbom-deps.json`  
- Evidence: approval ticket with justification

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|-------|--------------|---------|
| L1    | Yes          | Simplified approval |
| L2    | Yes          | Formal approval + recorded provenance |
| L3    | Yes          | Mandatory pinning/lockfile policy |

**Integration into the SDLC.**
| Phase            | Trigger              | Responsible                         | SLA            |
|-----------------|----------------------|-------------------------------------|----------------|
| Development | Dependency inclusion | **Developer** + **AppSec Engineer** | Before the merge |

**Note - intersects with other practices**  
This user story intersects with practices such as [Dependencies, SBOM and SCA](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) and, to some extent, enables *drift* monitoring as indicated in [Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro).

---

### US-04 - Automation in CI/CD (Linters & SAST) {#us-04---automatização-em-cicd-linters--sast}

**Context.**  
Automating validations in CI/CD pipelines ensures consistency, speeds up the detection of flaws and creates continuous evidence. Automating means **removing the human factor of distraction or forgetfulness** from repetitive controls.

:::userstory
**Story.**   
As **DevOps / SRE**, I want to integrate linters and SAST into the pipeline, so that flaws are detected early and continuous evidence is generated.

**Acceptance criteria (BDD).**
- **Given** that the pipeline is executed  
  **When** linters and SAST run  
  **Then** reports are archived and the build fails on critical findings

**Checklist.**
- [ ] Jobs configured in the pipeline  
- [ ] Severity limits (*thresholds*) defined  
- [ ] Reports archived immutably  
- [ ] Build fails on critical findings  
- [ ] The PR only progresses to “validated” when G2 is satisfied (CI/CD evidence)
:::

**Artefacts & evidence.**
- Artefact: `ci/pipeline.yml`  
- Evidence: archived SARIF/JSON reports

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|-------|--------------|---------|
| L1    | Yes          | Security linters + SAST blocking High/Critical findings |
| L2    | Yes          | Full SAST + severity *gating* |
| L3    | Yes          | SAST + additional validations (IaC/DAST) |

**Integration into the SDLC.**
| Phase | Trigger            | Responsible       | SLA        |
|------|--------------------|-------------------|------------|
| CI/CD| Pipeline execution  | **DevOps / SRE**  | Every build |

**Useful links.**  
[Secure CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro)

---

### US-05 - Management of Technical Exceptions {#us-05---gestão-de-exceções-técnicas}

**Context.**  
Not every control can always be applied in good time. Dealing with technical exceptions is inevitable - but if they are not **formally recorded, approved and temporary**, they become risk debt and create persistent vulnerabilities.

:::userstory
**Story.**   
As an **AppSec Engineer**, I want to record and approve technical exceptions, so that traceability, mitigation and future review are ensured.

**Acceptance criteria (BDD).**
- **Given** that an exception is requested  
  **When** I assess the proposed justification and mitigation  
  **Then** I approve or reject it and set an expiry date

**Checklist.**
- [ ] Exception recorded in `excecoes-seguranca.md`  
- [ ] Alternative mitigation defined  
- [ ] Expiry date assigned  
- [ ] Reassessment scheduled
:::

**Artefacts & evidence.**
- Artefact: `excecoes-seguranca.md`  
- Evidence: formal approval in an issue/PR

> **Reference:** This US implements [Ch. 14-US-01: Formal exceptions process]  
> in the context of secure development. All technical exceptions must be managed in accordance with the master exceptions policy in Ch. 14, including TTL and periodic revalidation.

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|-------|--------------|---------|
| L1    | Yes          | Simple and rare exceptions |
| L2    | Yes          | Revalidation per sprint |
| L3    | Yes          | Executive approval + compensating plan |

**Integration into the SDLC.**
| Phase    | Trigger            | Responsible                                  | SLA              |
|---------|--------------------|-----------------------------------------------|------------------|
| Release | Exception requested | **AppSec Engineer** + **Product Owner (PO)** | Before go-live |

**Useful links.**  
[Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro)

---

### US-06 - Validated Use of GenAI {#us-06---uso-validado-de-genia}

**Context.**  
Generative AI tools (GenAI) speed up code writing, but they can introduce **vulnerabilities, licence violations and misalignment with mandatory technical rules**.  
Their use must be traceable, validated and always subject to human technical review.

:::userstory
**Story.**   
As a **Developer**, I want to use generative AI with mandatory review and explicit technical constraints, so that productivity is accelerated without compromising security.

**Acceptance criteria (BDD).**
- **Given** that I generate code with GenAI  
  **When** I record the use and submit it for review  
  **Then** it is only accepted if it complies with the guidelines, the project's technical constraints and licensing
- And the PR does not progress without evidence of human review (G1) and validation (G2)

**Checklist.**
- [ ] Use recorded in `uso-genia.md`  
- [ ] Technical constraints versioned and applicable to the project (`constrangimentos-dev.md`)  
- [ ] Technical review applied (by **Developer** / **Quality Assurance (QA)**, with escalation to **AppSec Engineer** when applicable)  
- [ ] Licence compliance verified  
- [ ] Evidence attached to the PR (includes links to validations and to the relevant constraint)
:::

**Artefacts & evidence.**
- Artefacts: `uso-genia.md`, `constrangimentos-dev.md`  
- Evidence: review comments + validations in the PR

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|-------|--------------|---------|
| L1    | Optional     | Simple record |
| L2    | Yes          | Record + technical review + mandatory constraints |
| L3    | Yes          | Formal review + additional validations + reinforced evidence |

**Integration into the SDLC.**
| Phase            | Trigger   | Responsible                         | SLA           |
|-----------------|-----------|--------------------------------------|---------------|
| Development | GenAI use  | **Developer** + **Quality Assurance (QA)** | Before the merge |

**Useful links.**  
[Secure Development](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro)

---

### US-07 - Governance and Curation of Guidelines {#us-07---governação-e-curadoria-de-guidelines}

**Context.**  
Active governance of the guidelines ensures that they evolve with technologies and with emerging vulnerabilities.  
Formal publication and periodic review are mechanisms of control and compliance.

:::userstory
**Story.**  
As an **AppSec Engineer**, I want to review and publish curated guidelines quarterly, so that continuous updating and formal governance of secure development practices are ensured.

**Acceptance criteria (BDD).**
- **Given** that the review cycle is under way or a new *stack* emerges  
  **When** the *rulesets* are updated  
  **Then** a **release/tag** approved by **Software Architects** and **AppSec Engineer** is published (and, when applicable, operationalised by **DevOps / SRE**)

**Checklist.**
- [ ] *Rulesets* assessed and documented  
- [ ] *Tailoring* validated  
- [ ] Configurations versioned and published  
- [ ] Changelog included in the release  
- [ ] Periodic review recorded  
- [ ] Mapping updated for ASVS/CWE
:::

**Artefacts & evidence.**
- Artefact: `rules/` directory  
- Evidence: release/tag + changelog

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|-------|--------------|---------|
| L1    | Yes          | *Default* upstream rules, approved and reviewed within the validity period |
| L2    | Yes          | Mandatory organisational curation |
| L3    | Yes          | *Policy-as-code* + controlled distribution |

**Integration into the SDLC.**
| Phase       | Trigger               | Responsible                                                     | SLA       |
|------------|-----------------------|------------------------------------------------------------------|-----------|
| Governance | New stack or review | **Software Architects** + **AppSec Engineer** + **DevOps / SRE** | Within 2 wks. |

---

### US-08 - Traceability with Security Annotations {#us-08---rastreabilidade-com-anotações-de-segurança}

**Context.**  
Security validations must be traceable back to the original requirements. Standardised annotations (`@sec:*`) in code and tests make it possible to **link implementation, requirements and audit evidence** unambiguously.

:::userstory
**Story.**   
As a **Developer**, I want to annotate security validations with `@sec:*`, so that end-to-end traceability up to the backlog is ensured.

**Acceptance criteria (BDD).**
- **Given** that I implement a security requirement  
  **When** I add the `@sec:*` annotation  
  **Then** the requirement becomes traceable up to the backlog and the CI/CD reports

**Checklist.**
- [ ] Annotations included in code/tests  
- [ ] Cross-reference to requirements (`SEC-*`)  
- [ ] Reports export the annotations  
- [ ] Evidence archived
:::

**Artefacts & evidence.**
- Artefact: commented code, annotated tests  
- Evidence: CI/CD reports

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|-------|--------------|---------|
| L1    | Optional     | Only in critical modules |
| L2    | Yes          | All security validations |
| L3    | Yes          | Annotations + automated validation |

**Integration into the SDLC.**
| Phase            | Trigger                    | Responsible                         | SLA        |
|-----------------|----------------------------|--------------------------------------|------------|
| Development | Requirement implementation | **Developer** + **Quality Assurance (QA)** | By the merge |

---

### US-09 - Pre-release Security Gate {#us-09---gate-de-segurança-pré-release}

**Context.**  
Before each *release* there must be an objective control point that consolidates all the security evidence - SAST reports, SBOM, exceptions, checklists and approvals.

:::userstory
**Story.**  
As **DevOps / SRE**, I want to execute a **pre-release security gate** that aggregates all the validation evidence, so that only publications compliant with the security requirements are allowed.

**Acceptance criteria (BDD).**
- **Given** that there is a candidate *release*  
- And the L1–L3 risk level has been assigned  
  **When** the *security gate* is executed  
  **Then** the result is binary (Approved/Rejected) and is recorded as a release artefact

**Checklist.**
- [ ] `release-security-gate` *job* configured in the pipeline  
- [ ] Aggregated report attached to the *tag/release*  
- [ ] Links to SAST, SBOM, exceptions and PR checklist  
- [ ] Automatic blocking in the event of failure  
- [ ] Final approval by **AppSec Engineer** (and, at L3 when applicable, by **Executive Management**)
:::

**Artefacts & evidence.** `gate-relatorio.md`, CI/CD attachments, signed *tag/release*

**Proportionality.**
| Level | Mandatory? | Adjustments |
|-------|---------------|---------|
| L1 | Yes | Basic gate (SAST + SBOM + checklist) |
| L2 | Yes | Reinforced gate with exceptions policy |
| L3 | Yes | *Policy-as-code* and formal dual approval |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Pre-release | Execution of the *security gate* on a release candidate | **DevOps / SRE** | Binary result recorded as a release artefact, with automatic blocking on failure |

---

### US-10 - Validation Profiles by Risk Level (L1–L3) {#us-10---perfis-de-validação-por-nível-de-risco-l1l3}

**Context.**  
Proportional application of controls is essential to ensure efficiency and consistency.  
Each application must inherit a technical validation profile compatible with its risk classification.

:::userstory
**Story.**  
As an **AppSec Engineer**, I want to define and apply **L1–L3 validation profiles** that determine rules, limits and *quality gates* appropriate to the risk, so that execution and audit are standardised.

**Acceptance criteria (BDD).**
- **Given** that the application has an L1/L2/L3 classification  
  **When** the pipeline is executed  
  **Then** the rules and limits corresponding to the defined profile are applied

**Checklist.**
- [ ] L1–L3 profiles documented and approved  
- [ ] Corresponding *rulesets* in the pipeline  
- [ ] Severity and coverage metrics defined  
- [ ] Gates G1–G3 parameterised per profile (thresholds and exceptions)  
- [ ] Quarterly audit of profiles and thresholds
:::

**Artefacts & evidence.** `matriz-proporcionalidade-dev.md`, `ci/pipeline.yml`, audit reports

**Proportionality.**
| Level | Mandatory? | Adjustments |
|-------|---------------|---------|
| L1 | Yes | Profile with linters + light SAST + basic checklist |
| L2 | Yes | Profile with full SAST + thresholds + dual review when applicable |
| L3 | Yes | Profile with *policy-as-code* + reinforced gates + auditable retention |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| CI/CD | Pipeline execution on an application classified L1–L3 | **AppSec Engineer** | On every execution, with the rules and limits of the corresponding profile |

---

### US-11 - Central Archive of Validation Evidence {#us-11---arquivo-central-de-evidências-de-validação}

**Context.**  
Controlled retention of evidence is an audit and compliance requirement.  
Proof of the execution of controls must be exported and archived in a secure, immutable and auditable way.

:::userstory
**Story.**  
As **Quality Assurance (QA)** and **DevOps / SRE**, I want to **centrally archive all validation evidence** (SAST reports, SBOM, exceptions, `@sec:*`), so that traceability and compliance with audit requirements are ensured.

**Acceptance criteria (BDD).**
- **Given** that the pipeline executes validations  
  **When** it completes the execution  
  **Then** it exports and archives reports and evidence in a controlled and versioned repository

**Checklist.**
- [ ] Evidence repository defined (preferably WORM)  
- [ ] Automatic export per *build/release*  
- [ ] Evidence index per application and *commit*  
- [ ] Retention policy defined (1 year at L1, 2 years at L2, 3 years at L3; for products within the scope of the CRA, at least 10 years after placing on the market or the support period, whichever is longer)  
- [ ] Audited and controlled access
:::

**Artefacts & evidence.**  
`evidencias/` directory, `evidencias-index.json`, access logs

**Proportionality.**
| Level | Mandatory? | Adjustments |
|-------|---------------|---------|
| L1 | Yes | Minimum retention and basic export |
| L2 | Yes | Signed export + index per component |
| L3 | Yes | Immutable storage and periodic integrity verification |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| CI/CD | Completion of the execution of validations in the pipeline | **Quality Assurance (QA)** + **DevOps / SRE** | Export per *build*/*release*; retention of 1 year (L1), 2 years (L2), 3 years (L3); ≥ 10 years for products within the scope of the CRA |

---

### US-12 - Mandatory Local Validations (Pre-commit) {#us-12---validações-locais-obrigatórias-pre-commit}

**Context.**  
Validations executed locally before any push shorten feedback cycles, increase code consistency and reduce the load on the pipeline. Git hooks and local linters are the first line of defence.

:::userstory
**Story.**  
As a **Developer**, I want to run **linters and security validations locally** before committing, so that trivial errors and easily correctable vulnerabilities are detected without depending on the CI/CD pipeline.

**Acceptance criteria (BDD).**
- **Given** that I use an IDE or terminal in the project  
  **When** I run `make lint` or the pre-commit hook (automatic)  
  **Then** I receive immediate feedback on linting errors and locally detectable vulnerabilities  
- And critical failures block the commit

**Checklist.**
- [ ] Git hooks configured (`.husky/pre-commit` or `.git/hooks/`)  
- [ ] `make lint` and `make check-security` targets functional  
- [ ] Local minimum rules aligned with CI/CD  
- [ ] Critical failures block the commit; warnings allow a *bypass* with a flag  
- [ ] Documentation in `README.md` with setup and usage commands  
- [ ] Safe *bypass* (`SKIP_HOOKS=1`) available with traceability
:::

**Artefacts & evidence.**
- Artefacts: `.husky/pre-commit`, `Makefile` (targets `lint`, `check-security`), `.eslintrc.json` (or equivalent per stack)  
- Evidence: pre-commit execution logs in the commit history, output in the PR

**Proportionality.**
| Level | Mandatory? | Adjustments |
|-------|---------------|---------|
| L1 | Yes | Linter with security rules active locally (hook or IDE) |
| L2 | Yes | Mandatory linters + *secrets scanning* |
| L3 | Yes | Pre-commit + light local SAST + pattern validation |

**Integration into the SDLC.**
| Phase       | Trigger           | Responsible   | SLA |
|------------|-------------------|---------------|-----|
| Dev (Local)| Commit preparation | **Developer** | Immediate (local execution) |

**Useful links.**
- US-01 (Development Guidelines)
- US-04 (Automation in CI/CD)
- Ch. 06, addon 02 (Linters and Validations)

---

### US-13 - Validation of Dangerous Patterns and Anti-patterns {#us-13---validação-de-padrões-perigosos-e-anti-patterns}

**Context.**  
Insecure code patterns (eval, SQL concatenation, *hardcoded secrets*, XSS, etc.) must be detected automatically and blocked, with education on secure alternatives.

:::userstory
**Story.**  
As an **AppSec Engineer**, I want the pipeline to **automatically detect dangerous patterns** (eval, innerHTML without sanitisation, SQL concatenation, secrets, etc.) and block the build, with an educational message and a link to fix it.

**Acceptance criteria (BDD).**
- **Given** that a PR introduces a dangerous code pattern  
  **When** SAST/linters/semgrep run  
  **Then** the build fails with an explanatory message, a reference to CWE and a secure alternative  
- And the occurrence is recorded for trend measurement

**Checklist.**
- [ ] SAST/Semgrep rules configured for dangerous patterns per stack (Python, JS, Java, etc.)  
- [ ] Educational error messages with insecure vs. secure examples  
- [ ] Cross-reference with Ch. 06, addon 01 (Good Practices) and with OWASP/CWE  
- [ ] Clear severity scale: **critical** (eval, exec), **high** (SQL concat, XSS), **medium** (hardcoded secrets)  
- [ ] PR template with "How to fix this pattern" per category  
- [ ] Metrics of detections and resolutions reported on a dashboard
:::

**Artefacts & evidence.**
- Artefacts: `.semgrep.yml`, `sonar-project.properties`, SAST rules (SonarQube, Checkmarx, Snyk)  
- Evidence: PR reports with findings + education, history of resolutions

**Proportionality.**
| Level | Mandatory? | Adjustments |
|-------|---------------|---------|
| L1 | Yes | Detection of **critical** and **high** patterns (eval, exec, SQL, XSS) |
| L2 | Yes | Expanded detection (**critical** + **high**: SQL, XSS) |
| L3 | Yes | Complete detection + context and educational reinforcement |

**Integration into the SDLC.**
| Phase              | Trigger                  | Responsible                         | SLA |
|-------------------|--------------------------|--------------------------------------|-----|
| CI/CD (Analysis)  | PR opened or commit on dev | **DevOps / SRE** + **AppSec Engineer** | Every build (~5–10 min) |

**Useful links.**
- US-01, addon 01 (Code Good Practices)
- US-04 (Automation in CI/CD)
- US-08 (Annotations for Traceability)
- Ch. 06, addon 01 (Good Practices)

---

### US-14 - Compliance Monitoring and Security Metrics {#us-14---monitorização-de-conformidade-e-métricas-de-segurança}

**Context.**  
Continuous security metrics (linter coverage, active exceptions, resolved findings, L1–L3 compliance) enable informed governance and rapid identification of deviations.

:::userstory
**Story.**  
As a **Scrum Master / Team Lead** and an **AppSec Engineer**, I want to **view a dashboard of security metrics** (SAST coverage, active/expired exceptions, resolved findings, compliance per level L1–L3) for informed decision-making and rapid corrective action.

**Acceptance criteria (BDD).**
- **Given** that multiple releases and sprints are under way  
  **When** I access the compliance dashboard  
  **Then** I view: the compliance trend, pending exceptions, recommended actions  
- And I receive automatic alerts for critical deviations (e.g.: an expired exception without reassessment)

**Checklist.**
- [ ] Centralised dashboard (e.g.: Grafana, Kibana, internal panel) with Ch. 06 data  
- [ ] Key metrics: SAST coverage, active/expired exceptions, resolved findings, L1–L3 compliance  
- [ ] Aggregation by application, stack, risk level and sprint  
- [ ] Automatic alerts for deviations (e.g.: expired exception, drop in compliance)  
- [ ] Monthly/quarterly export for internal and regulatory audit  
- [ ] Link with US-11 (Evidence Archive) for complete traceability
:::

**Artefacts & evidence.**
- Artefacts: Dashboard configs (Grafana JSON, Elasticsearch queries), aggregation scripts  
- Evidence: monthly/quarterly dashboard captures, trend reports, generated alerts

**Proportionality.**
| Level | Mandatory? | Adjustments |
|-------|---------------|---------|
| L1 | Recommended | Basic metrics (SAST coverage, exceptions) |
| L2 | Yes | Dashboard with alerts for deviations |
| L3 | Yes | Continuous dashboard + automated audit + remediation SLA |

**Integration into the SDLC.**
| Phase                     | Trigger                     | Responsible                                              | SLA |
|--------------------------|-----------------------------|----------------------------------------------------------|-----|
| Governance (Quarterly +)| On demand / schedule   | **AppSec Engineer** + **DevOps / SRE** + **GRC / Compliance** (when applicable) | Monthly report |

**Useful links.**
- US-07 (Governance and Curation of Guidelines)
- US-09 (Pre-release Security Gate)
- US-11 (Central Evidence Archive)
- Ch. 12 (Monitoring and Operations)

---

### US-15 - GenAI Prompts and Outputs under Code Discipline {#us-15---prompts-e-outputs-de-genai-sob-disciplina-de-código}

The files that configure assistants and the outputs they return are treated as code: versioned, reviewed and validated.  

**Context.** The *system prompts*, *skill files* (`.claude/skills/*.md`), *agent files*, `.cursorrules` and `.github/copilot-instructions.md` decide what the assistant knows and which *tools* it may invoke; if they change without review, the operational behaviour changes without a trace. Symmetrically, when a model's structured output feeds a *tool call*, a record or an automated decision, its format and semantics have to be validated server-side before being consumed. Both artefacts frequently escape the discipline of *secure development*.  

:::userstory
**Story.**   
As an **AppSec Engineer**, I want the *prompts*, *skill files*, *agent files* and *rules* to be managed as code and the models' *structured outputs* to be validated server-side, so that silent operational change and the consumption of untrusted output are prevented.  

**Acceptance criteria (BDD).**  
- **Given** that there is a *skill file*, *agent file*, *prompt* or *rules* in the project  
  **When** it is changed or generated by a canonical tool  
  **Then** it goes through *code review*, *secret scanning* and *drift detection*, and is listed in a versioned inventory with an *owner*  
- **Given** that a model output feeds application logic  
  **When** it is received by the server  
  **Then** it is validated against a versioned *schema* (syntactically and semantically) before any action, and in case of failure the system does not consume the output and follows the declared *fallback*  

**Checklist.**  
- [ ] *Prompts*, *skill files*, *agent files* and *rules* versioned in VCS, with *code review*, extended *secret scanning* and *drift detection* configured  
- [ ] Versioned inventory of active *skill files*/*agent files*/*rules* per project, with an *owner* and a re-review cadence  
- [ ] *Schema* (JSON Schema/Pydantic/Zod) declared server-side, versioned and referenced in the log; syntactic and semantic validation mandatory before execution  
- [ ] The *provider*'s native *structured outputs* mechanisms adopted when feasible; no permissive *parsing* of raw text nor output feeding `eval()`  

:::

**Artefacts & evidence.** Inventory of *skill files*/*agent files*/*rules*; versioned *schemas* in the repository; *code review*, *secret scanning* and *drift detection* reports; logs with the *schema version* of failed validations.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Versioned *prompts*/*rules* + *code review*; *schema* declared and validated server-side | + extended *secret scanning*, inventory with an *owner*, per-action semantic validation | + automatic *drift detection*, canonical *tool definitions* and schema telemetry for *post-mortem* |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Code Review | Change to a *prompt*/*skill*/*agent*/*rules* or consumption of model output | **AppSec Engineer** + **Developer** | Before the merge |

**Useful links.** [Prompts and skill files as code](/sbd-toe/sbd-manual/desenvolvimento-seguro/addon/genia-e-seguranca#prompts-como-codigo) · [Structured outputs](/sbd-toe/sbd-manual/desenvolvimento-seguro/addon/genia-e-seguranca#structured-outputs)

---

### US-16 - Provenance and Quality Gate with an Approved Baseline {#us-16---proveniência-e-quality-gate-com-baseline-aprovada}

The provenance of all incorporated code is identified and integration is governed by a *quality gate* with an approved *baseline* and *thresholds*.  

**Context.** The risk of a contribution does not depend on its origin (human, reused or generated by GenAI), but on its understanding, validation and accountability. Code reused or adapted from an external, non-internal origin requires the same provenance identification and human review as code generated by GenAI. In parallel, the SAST gate can only be operationalised with a false-positive *baseline* approved by AppSec — without it, the noise of findings creates pressure to disable it — and integration must be governed by quality profiles with security *thresholds* versioned per risk level.  

:::userstory
**Story.**   
As an **AppSec Engineer**, I want the provenance of all incorporated code to be identified and integration to pass a *quality gate* with an approved false-positive *baseline* and *thresholds*, so that incorporation is accountable and the gate is operable and cannot be bypassed.  

**Acceptance criteria (BDD).**  
- **Given** that code of external origin (reused, adapted or generated by GenAI) is proposed  
  **When** it is incorporated  
  **Then** its provenance is identified before incorporation and there is evidence of human review per PR for non-internal provenance  
- **Given** that the SAST runs in the pipeline  
  **When** it produces findings  
  **Then** it applies the false-positive *baseline* approved by AppSec and the quality profiles with *thresholds* per risk level, blocking the pipeline or requiring documented approval in the event of a deviation  

**Checklist.**  
- [ ] Provenance of incorporated code (internal, reused, adapted or GenAI) identified before incorporation, with a documented provenance policy  
- [ ] Human review per PR recorded for code of non-internal provenance  
- [ ] SAST false-positive *baseline* versioned and approved by **AppSec Engineer**  
- [ ] Quality profiles with security *thresholds* per risk level versioned; deviations block the pipeline or require explicit documented approval  

:::

**Artefacts & evidence.** Provenance policy; provenance record per component; versioned false-positive *baseline*; versioned quality profiles (e.g.: *Quality Gates*); SAST reports and deviation approvals.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Provenance flagged; SAST with an AppSec-approved baseline and High/Critical blocking | Provenance identified + human review for non-internal origin; baseline approved by AppSec + thresholds per profile | + *policy-as-code* for the gate, periodic audit of the baseline and profiles, auditable retention of deviations |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| CI/CD | Incorporation of code of non-internal origin / execution of the SAST | **Developer** + **AppSec Engineer** | Before the merge |

**Useful links.** [Code Provenance](/sbd-toe/sbd-manual/desenvolvimento-seguro/addon/proveniencia-codigo) · [Requirements Catalogue (DEV-003/006/008)](/sbd-toe/sbd-manual/desenvolvimento-seguro/addon/catalogo-requisitos-desenvolvimento)

---

## 📦 Expected Artefacts {#-artefactos-esperados}

| Artefact                  | Auditable evidence                                      |
|---------------------------|----------------------------------------------------------|
| `guidelines-stack.md`     | Curated and approved guidelines, with a *changelog*          |
| `rules/`                  | Versioned and approved *rulesets*                       |
| `checklist-pr.md`         | Formal checklist integrated into PRs                        |
| `sbom-deps.json`          | SBOM validated and approved                                 |
| `gate-relatorio.md`       | Consolidated *security gate* report                 |
| `excecoes-seguranca.md`   | Record of exceptions and approvals                         |
| `uso-genia.md`            | Record and review of GenAI use                        |
| `constrangimentos-dev.md` | Versioned technical constraints (includes GenAI)     |
| `.husky/pre-commit`       | Git hooks configured and functional (US-12)              |
| `Makefile` (lint targets) | Local validations available (US-12)                    |
| `.semgrep.yml`            | Dangerous pattern detection rules (US-13)           |
| `sonar-rules.txt`         | Configuration of dangerous patterns in SAST (US-13)        |
| `evidencias/`             | Centralised and indexed evidence archive            |
| `dashboard-metrics.json`  | Compliance dashboard config (US-14)              |
| `compliance-report.md`    | Monthly/quarterly metrics report (US-14)          |

---

## ⚖️ L1–L3 Proportionality Matrix {#️-matriz-de-proporcionalidade-l1l3}

| Practice / Control | L1 (low) | L2 (medium) | L3 (critical) |
|--------------------|------------|-------------|--------------|
| Guidelines | Upstream rules | Curated per stack | Audited and *policy-as-code* |
| Code review | Basic checklist | Dual review | Dedicated review (includes AppSec when applicable) |
| Dependencies | Simple validation | Formal validation | Traceable SBOM |
| CI/CD | Security linters + SAST (High/Critical blocking) | Mandatory SAST | SAST + IaC/DAST + policies |
| Exceptions | Simple record | Revalidation per sprint | Dual approval |
| GenAI | Optional record | Review + mandatory constraints | Formal review, licences and reinforced evidence |
| Governance | Annual curation | Quarterly | Continuous and automated |
| Evidence | Manual export | Automatic export | Immutable and audited archive |
| Security Gate | Basic | Complete | Reinforced and automated |
| Local Validations (US-12) | Mandatory (local security linter) | Mandatory | Mandatory + light SAST |
| Dangerous Patterns (US-13) | Critical + High | Critical + High | Complete + education |
| Metrics & Compliance (US-14) | Recommended | With alerts | Continuous + SLA |

---

## 🏁 Final Recommendations {#-recomendações-finais}

Secure development must be treated as a **continuous and measurable process**.  
The *user stories* in this chapter operationalise the normative prescriptions, ensuring that each practice leaves a verifiable trail and that the degree of application is proportional to risk.  
Integrating these actions into the backlog and the pipeline turns software security into a daily, auditable discipline.

In summary: the chapter demonstrates that **secure development is the foundation on which the rest of the lifecycle rests**.  
Without it, no subsequent practice - whether CI/CD, IaC or runtime - can offer full confidence.
