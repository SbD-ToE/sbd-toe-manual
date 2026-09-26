---
id: riscos-processo-cicd
title: Process Risks in Modern CI/CD
description: Risks introduced by pervasive automation in the CI/CD pipeline and the corresponding control, validation and evidence measures
tags: [cicd, processo, automacao, risco, evidencias]
genia: process-risk-normalization
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/addon/10-riscos-processo-cicd.md
  source_sha256: 1aa03164a176d5353299dab9a079595a3968c9f2ff36f205a613e63fea8af75e
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 351863572ea20abb056b796f6ee16f548868d7ed9e03fd0ae4b271a0a0eddbb9
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, deterministic, framework_source_corpus, instrument, lifecycle_phase, validation_evaluation]
  glossary_sha256: d86c73495fe7cdf17f03547ee8580128d27f22cc59ca6fe4a19683e7bff45a24
  translated_at: 2026-09-26T09:09:17Z
  reviewed_by: null
---

# Process Risks in Modern CI/CD

The CI/CD pipeline is today one of the **most critical assets** of any organisation that develops software continuously.  
Everything that reaches production - code, configuration, infrastructure, artefacts - inevitably passes through this mechanism.

For a long time, CI/CD was seen merely as an **automation tool**: compile, test, package, distribute.  
That view is no longer sufficient.

In the current context, CI/CD is an **operational decision system**, where it is determined, automatically or semi-automatically:

- what may move forward;
- what must be blocked;
- when a version is considered acceptable;
- who takes responsibility for a promotion.

The pervasive adoption of advanced automation - regardless of the concrete technology - **does not change this reality**, but it **accentuates the process risks** associated with the pipeline.

This document identifies those risks and establishes **clear prescriptions for mitigation, validation and evidence**, ensuring that CI/CD remains:

- deterministic,
- auditable,
- reproducible,
- governable,
- and with explicit human accountability.

---

## 🎯 Fundamental principle {#-princípio-fundamental}

CI/CD **may execute actions**,  
**may produce signals**,  
**may generate recommendations**.

But it **cannot take responsibility**.

The final decision on any irreversible action - promotion, deploy, rollback, exposure to users - is always human, assigned to an explicit role and supported by verifiable evidence.

---

## 🧭 CI/CD as a critical decision system {#-cicd-como-sistema-crítico-de-decisão}

Treating CI/CD as simple automation leads to systemic errors.

In practice, the pipeline:

- replaces the former release committees;
- encodes organisational policies;
- materialises security requirements;
- creates or destroys evidence of compliance.

Any conceptual failure at this point **propagates to the whole lifecycle**.

For this reason, the risks associated with automation in CI/CD must be treated **as process risks**, and not as isolated technical problems.

---

## ⚠️ Risk R1 - Non-determinism of the pipeline {#️-risco-r1---não-determinismo-do-pipeline}

### Description {#descrição}

A pipeline becomes non-deterministic when **identical runs do not produce equivalent results**, without any explicit change to the code or the versioned configuration.

In this scenario, the result no longer depends only on:

- source code;
- the pipeline definition;

and comes to depend on **implicit context**, often neither versioned nor controlled.

### How it arises {#como-surge}

- Configurations resolved dynamically at run time;
- Steps generated or altered without an explicit record;
- Volatile external dependencies;
- Environmental context not pinned.

### Impact {#impacto}

- Impossibility of reproducing historical builds;
- Inconclusive audits;
- Incidents that cannot be analysed retroactively;
- False confidence in previous results.

### Prescribed mitigations {#mitigações-prescritas}

- The pipeline must be treated as a **versioned artefact**;
- The pipeline definition must be **explicit and declarative**;
- Clear separation between:
  - the pipeline definition;
  - the pipeline run;
  - the results produced.

### Minimum evidence required {#evidência-mínima-exigida}

- Versioned pipeline definition (e.g. YAML/DSL);
- Unambiguous identification of the version run;
- Complete run logs;
- Clear association with a commit/hash.

**Relates to.** Violates `CIC-001`; materialises `MT-130`.

---

## ⚠️ Risk R2 - Confusion between automatic suggestion and effective decision {#️-risco-r2---confusão-entre-sugestão-automática-e-decisão-efetiva}

### Description {#descrição-1}

Results presented as *scores*, *ratings*, *priorities* or *recommendations* are often interpreted, in practice, as **final decisions**.

This confusion is subtle, but dangerous:  
a poorly defined *soft gate* turns into a *hard bypass*.

### How it arises {#como-surge-1}

- Ambiguous language in the outputs;
- Operational pressure for speed;
- Progressive automation without redefining responsibilities.

### Impact {#impacto-1}

- Improper promotions;
- Silent bypass of security controls;
- Difficulty in assigning responsibility after an incident.

### Prescribed mitigations {#mitigações-prescritas-1}

- Gates must be **explicit, binary and unambiguous**;
- The final decision must require **named human approval**;
- There must be a formal distinction between:
  - automatic signal;
  - promotion decision.

### Minimum evidence required {#evidência-mínima-exigida-1}

- Record of the decision;
- Identity of the owner;
- Timestamp and context of the approval;
- Reference to the evidence considered.

**Relates to.** Violates `CIC-004`; materialises `MT-126`.

---

## ⚠️ Risk R3 - Plausible evidence without empirical execution {#️-risco-r3---evidência-plausível-sem-execução-empírica}

### Description {#descrição-2}

Well-structured, convincing or complete outputs **do not constitute evidence** if they are not associated with real, observable execution.

In modern CI/CD, the appearance of rigour can mask the absence of effective validation.

### How it arises {#como-surge-2}

- Aggregated reports with no link to concrete execution;
- Synthesised or derived outputs;
- Excessive abstraction over tests or scans.

### Impact {#impacto-2}

- Failed audits;
- False perception of coverage;
- Decisions based on appearance, not on facts.

### Prescribed mitigations {#mitigações-prescritas-2}

- Evidence must always derive from **observable execution**;
- Each relevant result must be traceable to:
  - a test;
  - a scan;
  - a validation actually executed;
- Non-verifiable outputs must not be accepted as evidence.

### Minimum evidence required {#evidência-mínima-exigida-2}

- Execution logs;
- Artefacts produced;
- Return codes;
- Explicit reference to the action executed.

**Relates to.** Violates `CIC-005`; materialises `MT-129`.

---

## ⚠️ Risk R4 - Exfiltration of secrets and sensitive context {#️-risco-r4---exfiltração-de-segredos-e-contexto-sensível}

### Description {#descrição-3}

The pipeline handles highly sensitive information:

- proprietary code;
- secrets;
- configuration;
- intermediate artefacts;
- context-rich logs.

Any external dependency or implicit export mechanism constitutes a potential leakage vector.

### How it arises {#como-surge-3}

- Excessive logging;
- Debug active in production;
- Implicit upload of context;
- Lack of data segregation.

### Impact {#impacto-3}

- Exposure of secrets;
- Leakage of intellectual property;
- Legal or contractual non-compliance.

### Prescribed mitigations {#mitigações-prescritas-3}

- Principle of minimum necessary context;
- Systematic reduction of sensitive logging;
- Explicit policies for the use of external systems;
- Regular review of configuration and outputs.

### Minimum evidence required {#evidência-mínima-exigida-3}

- Applicable policies;
- Validated configuration;
- Documented reviews;
- Evidence of log control.

**Relates to.** Violates `CIC-003`; materialises `MT-120`, `MT-131`.

---

## ⚠️ Risk R5 - Dilution of operational accountability {#️-risco-r5---diluição-de-responsabilidade-operacional}

### Description {#descrição-4}

When the pipeline “decides”, no one decides.

The absence of an explicit human owner destroys the notion of non-repudiation and compromises the governance of the process.

### How it arises {#como-surge-4}

- Automation without redefinition of roles;
- Lack of clear ownership per environment;
- Organisational ambiguity.

### Impact {#impacto-4}

- Incidents without an owner;
- Ineffective escalations;
- Governance and audit failures.

### Prescribed mitigations {#mitigações-prescritas-4}

- Each promotion must have an **explicit human owner**;
- Responsibilities must be associated with clear roles;
- Irreversible actions require a named decision.

### Minimum evidence required {#evidência-mínima-exigida-4}

- Role → action mapping;
- Promotion records;
- Complete history of decisions.

**Relates to.** Violates `CIC-011`; materialises `MT-128`.

---

## 📊 Operational summary of the risks {#-síntese-operacional-dos-riscos}

| Risk | Where it occurs | Key mitigation | Evidence required |
|-----|------------|----------------|------------------|
| R1 | Pipeline definition | Explicit versioning | YAML + logs |
| R2 | Decision gates | Human approval | Named record |
| R3 | Outputs | Observable execution | Artefacts |
| R4 | Execution | Context containment | Policies |
| R5 | Promotion | Clear accountability | Audit trail |

---

## 🧩 Conclusion {#-conclusão}

Automation in CI/CD **is not the problem**.  
The problem arises when automation **implicitly replaces decision, accountability or evidence**.

A well-designed pipeline:

- speeds up the process;
- reinforces security;
- improves quality;
- and **increases**, rather than reduces, the capacity for governance.

This document establishes the invariants needed for CI/CD to remain a **reliable control instrument**, even in a context of pervasive automation and growing complexity.

