---
id: processo-excecoes
title: Canonical Exception Management Process
sidebar_position: 12
description: Formal, cross-cutting and authoritative process for the management of exceptions to security requirements and controls in SbD-ToE
tags: [excecoes, governanca, risco, aprovacao, rastreabilidade, lifecycle]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/addon/12-processo-excecoes.md
  source_sha256: b7f1b832ddfb6662411cd7606322da7f3c76a92a2f9dfc24be9b766410392be4
  source_commit: 036d74010f423f247be988e4a417375c74edb9d9
  target_sha256: 52d2e9c245eeaf45d141d4c68650a88d5122be9e466dfc11ca7a418cc456ddb8
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [alcada, avaliacao, chapter_role, cycle_iteration, maturity, papel_suporte, practitioner_manual, requirement_runtime, risk_level, role_tech_lead, sbdtoe_sbd, transversal, validation_evaluation]
  glossary_sha256: e369fca5209e396286ce719b0c316a74a1c84e29f1844996e975804c90e4126e
  translated_at: 2026-09-27T07:54:01Z
  stamped_at: 2026-09-27T07:54:01Z
  reviewed_by: null
---

# Canonical Exception Management Process

This document defines the canonical exception management process in SbD-ToE.

It is the reference document for all the chapters of the manual. Each domain chapter specifies its own triggers, additional fields and integration with tools - but the process, the approval authorities and the lifecycle are invariant and are defined here.

An exception is a formal risk decision: it recognises that a control is not applied, documents why, defines what compensates for it and establishes when it is reviewed. What is not in this model is not an exception - it is a silent failure.

---

## Scope {#âmbito}

It applies to any situation in which a requirement or control prescribed in SbD-ToE is not applied in full. Typical causes:

- a demonstrable technical limitation (e.g. a legacy system, a SaaS without support for the control);
- an external dependency that cannot be controlled in the short term;
- an implementation cost disproportionate to the effective risk of the context;
- a phased migration with a known and bounded non-compliance window;
- a functional or contractual conflict with documented evidence.

The cause does not have to be exceptional - but the treatment has to be. Every non-application of a control activates this process, without exception.

---

## Process {#processo}

### 1. Identification {#1-identificação}

Define precisely what is at stake:

- the canonical ID of the requirement or control (e.g. `ARC-003`, `DEP-007`, `IAC-003`);
- the affected system, component or environment;
- the risk level of the context (`L1`, `L2` or `L3`).

Incomplete identification invalidates the record.

### 2. Technical justification {#2-justificação-técnica}

Answer three questions explicitly:

1. What is the objective reason that prevents the application of the control?
2. Is the exception temporary (with a deadline) or structural (with no foreseeable solution)?
3. Is there a viable technical alternative? If so, why is it not applied?

Vague or generic justifications are not accepted as grounds for approval.

### 3. Impact assessment {#3-avaliação-de-impacto}

Quantify the residual risk created:

- which threats cease to be mitigated?
- is the risk level of the context affected by the absence of this control?
- is the residual risk acceptable with the planned compensations?

### 4. Compensating measures {#4-medidas-compensatórias}

Identify the alternative controls that reduce the residual risk to an acceptable level. The compensation does not need to be equivalent to the missing control - it needs to be proportional to the residual risk and verifiable.

Exceptions without an identified compensation are approved only at L1, with a justification of negligible risk.

### 5. Formal approval {#5-aprovação-formal}

Approval is explicit, recorded and attributed by name to a role with formal authority, in accordance with the approval authorities defined below. Tacit or implicit approvals are invalid.

### 6. Registration and activation of the monitoring cycle {#6-registo-e-activação-do-ciclo-de-monitorização}

After approval, the exception is recorded with all the mandatory fields and integrated into the continuous validation cycle (see `addon/06-validacao-continuada.md`). From this moment on it is active, has a deadline and creates a review obligation.

---

## Mandatory fields {#campos-obrigatórios}

| Field | Mandatory | Notes |
|---|---|---|
| Exception ID | Yes | E.g. `IAC-EXC-003-2025-07-10`; the format may be adapted per domain |
| Affected requirement | Yes | Canonical ID (e.g. `ARC-003`) + the project's operational tag (e.g. `SEC-L2-ARC-003`) |
| System / component / environment | Yes | |
| Risk level (L1–L3) | Yes | |
| Technical justification | Yes | Objective reason; no vague generalities |
| Impact and residual risk | Yes | |
| Compensating measure | Yes | Alternative control applied or committed |
| **Who requested** | Yes | Author of the request - name, function, team |
| **Who created the risk assessment** | Yes | Person responsible for the impact and residual risk analysis - name and function |
| **Who approved** | Yes | Formal approver - name, function; in accordance with the approval authorities below |
| Approval date | Yes | |
| **Chain of authority** | Yes | See section below |
| **Technical evidence** | Yes | Artefacts that support the justification and the compensation - scanner reports, tickets, logs, ADRs, test evidence; reference by URL or traceable path |
| Expiry date | Yes | Ceiling of Policy 05 §7 (absolute maximum 90 days, at L1); an extension requires reassessment |
| Review trigger | Yes | Fixed date or condition (incident, architectural change, etc.) |

Missing fields invalidate the record. An invalid record does not produce an approval.

---

## Chain of authority {#cadeia-de-autoridade}

The exception register is not the repository of the approval artefacts - it is the index that references them and ensures that the chain is complete and traceable. The artefacts themselves remain in the systems where they were produced (ticketing system, email, GRC, wiki).

What the register has to capture is the **decision sequence**: who identified the problem, who escalated, who assessed the risk, who gave the instruction to proceed and under what conditions.

Mandatory minimum structure:

| Step | Role | What has to be recorded | Reference |
|---|---|---|---|
| Exception request | Dev / PM / Architect | Description of the problem, reason for the technical impossibility and context | URL / ID |
| Escalation instruction | Tech Lead / BAO | Business context, indication of escalation and known conditions | URL / ID |
| Risk assessment | AppSec | Impact analysis, residual risk and opinion on the compensations | URL / ID |
| Formal approval | According to approval authorities (L1/L2/L3) | Explicit decision with conditions and validity | URL / ID |

The medium is not prescribed - a ticket, a comment on a PR, a note in a GRC system, a wiki entry, a decision in an ADR. What is prescribed is that **each step must have a recorded, dated action attributed to a role**, with a traceable reference in the corresponding field.

> A verbal approval without a record does not count. A chain with missing steps does not produce a valid approval.

---

## Approval authorities {#alçadas-de-aprovação}

| Level | Minimum approval |
|---|---|
| **L1** | Technical owner (Tech Lead or equivalent) |
| **L2** | AppSec + technical owner |
| **L3** | AppSec + GRC/CISO; compensating measure mandatory |

L3 exceptions without the approval of AppSec and GRC/CISO are non-compliant regardless of the content of the record.

---

## Validity, renewal and expiry {#validade-renovação-e-expiração}

The maximum time limit is that of [Policy 05 §7](/sbd-toe/assets/policies/policy-gestao-excecoes#7-prazos-máximos-de-validade-ttl), by level and severity; **90 days** is the absolute ceiling (L1). Extensions require a new full assessment - they are neither automatic nor granted by default.

Expired exceptions without active renewal constitute **non-compliance** from the expiry date onwards. They must be treated as such in the audit cycle.

Mandatory review triggers outside the normal period:

- a security incident directly related to the missing control;
- a change in the architecture, risk or classification of the affected system;
- a change of supplier, dependency or environment with an impact on the premise of the exception.

---

## Maturity indicators {#indicadores-de-maturidade}

The number and quality of the active exceptions in a project are direct signals of security maturity:

- many open exceptions at L3 indicate unmanaged security technical debt;
- exceptions with verifiable compensations and a met deadline indicate a functioning process;
- expired exceptions without renewal indicate the absence of effective governance.

See `kpis-governanca.md` for the associated organisational indicators.

---

## Specifics per domain {#especificidades-por-domínio}

Each domain chapter defines, in a file of its own, the characteristic triggers, additional fields, templates and integration with tools. The process in this section always applies, without substitution.

| Chapter | Specifics file |
|---|---|
| Ch. 02 - Application requirements | `addon/08-gestao-excecoes.md` |
| Ch. 04 - Secure Architecture | `addon/03-excecoes.md` |
| Ch. 05 - Dependencies and SBOM | `addon/09-excecoes-e-aceitacao-risco.md` |
| Ch. 06 - Secure Development | `addon/05-excecoes-e-justificacoes.md` |
| Ch. 07 - Secure CI/CD | `addon/09-controle-excecoes-visibilidade.md` |
| Ch. 08 - IaC | `addon/09-gestao-excecoes.md` |

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|---|---|
| `addon/01-modelo-governancao.md` | Roles, approval authorities and governance decision cycle |
| `addon/06-validacao-continuada.md` | Revalidation cycle and expiry management |
| `addon/05-exemplos-praticos.md` | Concrete examples of approved exceptions |
| `addon/08-diagramas-governanca.md` | Flowchart of the approval process |
| `kpis-governanca.md` | Indicators of active exceptions and maturity |
| SSDF GV.3 / RV.1 | Approval of exceptions and management of deviations |
| ISO/IEC 27001 A.18.1.4 | Formal acceptance of residual risks |
| OWASP SAMM Governance | Record and lifecycle of exceptional decisions |

---
