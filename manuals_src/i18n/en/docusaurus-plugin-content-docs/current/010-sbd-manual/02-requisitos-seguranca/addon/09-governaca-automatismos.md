---
id: governanca-automatismos
title: Governance of the Use of Automation and Assistants in the SSDLC
description: Prescription for the controlled use of automated generation tools (including AI) in development, without changing the application requirements
tags: [governanca, automatizacao, ia, sdlc, requisitos, validacao, rastreabilidade, agentic, mandates]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/02-requisitos-seguranca/addon/09-governaca-automatismos.md
  source_sha256: 2c98ddbab80b7ebba13764b4e2c51e6bd43b90b6e5426ca5db79fcd88ea53e48
  source_commit: e942cb6d9bc50586a82a25264f7bb2a016652246
  target_sha256: a58283fa5520e2968785beea3605d5b9f00deb76e31aebd8b33fd1a434b601d3
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [audit_trail, chapter_role, eu_ai_human_oversight, framework_source_corpus, layer, normative_empirical, practitioner_manual, requirement_runtime, risk_level, sbdtoe_sbd, traceability, transversal, validation_evaluation]
  glossary_sha256: 99bd217c01b2110ac5dc70d87c6809b50319bfca636ef6f08812cac3e128af17
  translated_at: 2026-09-27T18:45:48Z
  stamped_at: 2026-09-27T18:45:48Z
  reviewed_by: null
---

# Governance of the Use of Automation in Development

This annex defines **minimum principles, rules and obligations** for the use of **automation and assisted-generation tools** (including AI-based assistants, low-code/no-code and automatic code generation) in the context of the *Secure Software Development Lifecycle* (SSDLC).

Its objective is to **ensure that the adoption of these tools does not compromise**:
- the validity of the **security requirements** defined in Chapter 2;
- the **traceability** between risk, requirement, control and evidence;
- practical **verifiability** and human accountability.

> ⚠️ This annex **does not define new application requirements** nor does it change the T01–T20 catalogue.  
> It only defines **governance and validation conditions** for the correct application of the existing requirements when automation is used.

---

## 🎯 Scope and framing {#-âmbito-e-enquadramento}

This annex applies whenever the development process uses:

- AI-based code assistants (e.g. *code assistants*, *copilots*);
- *Low-code / no-code* platforms;
- Tools for automatic generation of code, configurations or tests;
- Automation that produces *executable artefacts* or logically relevant ones.

It does not apply:
- to the AI components of the **product itself**: these are governed by `THR-008`, by `ARC-014` (US-18 of Ch. 04), by `ARC-015` (US-16 of Ch. 04, which applies `REQ-AGN-003` and `REQ-AGN-004` to the product's agents), by `DEP-011` to `DEP-014` and by `OPS-011` to `OPS-014`; when the system is regulated by the AI Act, also by the regulatory overlay (context CTX-AIA-RE);
- to purely informational tools with no impact on code, configuration or logic.

---

## 🧠 Fundamental principles (normative) {#-princípios-fundamentais-normativos}

The following rules are **invariants** in the SbD-ToE model:

1. **Accountability is always human**  
   No technical or security decision may be attributed to a tool.

2. **Automated output is not evidence**  
   Automatically generated code, tests or configurations **do not constitute evidence of compliance** with requirements.

3. **Generated code is treated as third-party code**  
   It is subject to the same validations, reviews and controls.

4. **Validation is mandatory and explicit**  
   All relevant output must be validated by human and/or automated mechanisms.

5. **Traceability is not optional**  
   The use of automation **neither breaks nor simplifies** the traceability requirements.

---

## 🔗 Impact on the existing requirement themes {#-impacto-nos-temas-de-requisitos-existentes}

The use of automation **reinforces** (does not replace) the obligations in the following catalogue themes:

| Theme | Specific impact |
|---|---|
| **T11 – Code and Build Security** | Mandatory human review of generated code |
| **T12 – Dependencies and SBOM** | Identification of implicit dependencies introduced |
| **T13 – Secure CI/CD** | Automated gates become critical |
| **T17 – Security Testing** | Tests cannot assume implicit trust |
| **T20 – Governance and Compliance** | Use must be known, authorised and auditable |

> These impacts are operationalised in the file `aplicacao-lifecycle.md` through specific user stories and gates.

---

## ⚙️ Minimum governance rules {#️-regras-mínimas-de-governação}

### 1. Authorised and known use {#1-uso-autorizado-e-conhecido}
- The organisation **must know** which tools are used;
- Use must be covered by internal policy (see Ch. 14).

### 2. Information protection {#2-proteção-de-informação}
- It is **forbidden** to enter secrets, keys, sensitive data or confidential information into prompts;
- A violation constitutes a security incident.

### 3. Mandatory human review {#3-revisão-humana-obrigatória}
- All generated code/configuration must be:
  - reviewed by a qualified developer;
  - subject to the same *code review* criteria.

### 4. Independent technical validation {#4-validação-técnica-independente}
- SAST, SCA, tests and validations **cannot be disabled** on grounds of “trust in the tool”.

### 5. Exception management {#5-gestão-de-exceções}
- Any shortcut or non-application of a control follows the **formal exception process** of Chapter 14, with a TTL.

---

---

## 🤖 Autonomy level model for AI agents {#niveis-autonomia}

Up to this point the subject has been **assisted automation** — tools that suggest, but where decision and execution are human. A different class of tool has emerged: **agents** that receive an objective, decide which steps to take, invoke real *tools* (create a PR, run tests, read secrets, deploy), and can do so with varying degrees of human oversight. *Copilot Workspace*, *Claude Code*, *Cursor agent mode*, *Devin*, agents built on proprietary SDKs — all fit here.

When moving from a "tool that suggests" to an "agent that executes", the question is no longer *"was it reviewed?"* but *"was it authorised to do this, in this context, with this reach?"*. A **five-level autonomy model (A0–A4)** is therefore adopted, which makes that authorisation explicit, classifiable and auditable.

> 📌 The A0–A4 levels **do not replace** the fundamental principles (human accountability, output is not evidence, generated code is third-party code). They specialise them for the case in which the agent *executes* rather than merely *suggests*.

### Levels A0–A4 {#níveis-a0a4}

| Level | Designation | What the agent may do | Human approval required | Where it typically applies |
|---|---|---|---|---|
| **A0** | *Read-only / consultation* | Reads code, docs, logs; answers questions; suggests in a chat window | Not required; output is not acted upon | Exploratory sessions, assisted debugging, questions about the manual |
| **A1** | *Proposes changes* | Generates *patches*, opens PRs in *draft* state, writes tests, proposes configurations | Yes, **at merge / apply time**; classic human review of the output | Everyday use of *Copilot* / *Claude Code* in "propose-only" mode |
| **A2** | *Executes with confirmation per destructive action* | Executes idempotent/lightweight actions without confirmation (running tests, listing resources, reading config); requests explicit confirmation before each destructive or *side-effectful* action (deleting, writing to external systems, rotating secrets, *commit/push*, opening a PR outside *draft*) | Yes, **per** destructive or impactful action | Automated workflows with a human on call (PR auditing, *grounded codegen*, assisted *threat modelling*) |
| **A3** | *Executes autonomously with automatic revert* | Executes complete chains without intermediate confirmation, within a previously agreed *scope*, with an automatic *revert* mechanism on detected failure (tests, *health checks*, *anomaly detection*) | **Post-facto**: mandatory notification to the responsible human; mandatory periodic review of the session log | Maintenance automation (AI-driven *dependabot*, *autofix* of low-criticality SAST *findings*, generation and merge of regression tests) |
| **A4** | *Fully autonomous in production* | Operates continuously in production, within a registered mandate, without per-action approval; operational *kill-switch* available 24/7 | Mandatory periodic audit (cadence ≤ quarterly); *kill-switch* exercised at least once per quarter | Assisted *SRE*, alert remediation agents, automated *moderation* — only with a formal *mandate* and multi-layer *guardrails* |

> 🧭 **How to read the table.** Classification is done **per agent and per context** (not per organisation). The same agent may be A1 in an internal L1 project and A2 in a public L2 one; never A4 in any project without a formal *mandate* (see [`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)).

### Criteria for choosing the right level {#critérios-para-escolher-o-nível-certo}

Moving up a level **adds** obligations, never removes them. The practical rule is the most conservative level compatible with the actual work:

1. The starting point is **A1** whenever the agent is still new to the project or the team.
2. **A2** is reached when there is reliable operational auditing of *tool invocations* and per-tool *guardrails*.
3. **A3** requires *automatic revert* demonstrated in a test environment and test coverage that detects the kind of failure the agent may introduce.
4. **A4** requires a *mandate* signed by the `CISO` (or equivalent), an exercised *kill-switch*, and a scheduled periodic audit.

Moving down a level (e.g. A2 → A1) is always legitimate and requires no formal justification. Moving up requires a *mandate* (see [`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) and operational evidence of the prerequisites.

---

## 📋 REQ-AGN requirements — AI agents in the SDLC {#req-agn}

These requirements are **cross-cutting** across chapters 03 (Threat Modelling), 04 (Architecture), 06 (Development), 07 (CI/CD), 10 (Testing), 12 (Monitoring) and 14 (Governance). They do not replace existing requirements — they add the specific agentic layer.

| ID | Requirement | L1 | L2 | L3 | Description |
|---|---|:--:|:--:|:--:|---|
| **REQ-AGN-001** | *Registered and versioned mandate* | ✔ | ✔ | ✔ | Each agent in operational use (A1+) has a *mandate* documented and versioned in VCS containing: identity, autonomy level, scope of permitted *tools*, environments in which it operates, human *owner*, review periodicity. Without a valid *mandate* the agent does not operate beyond A0. Operationalised by [Policy 38 — AI agent mandates](/sbd-toe/assets/policies/policy-mandates-agentes). |
| **REQ-AGN-002** | *Autonomy level classified by context* | ✔ | ✔ | ✔ | Each use of an agent declares the A0–A4 level applicable to the specific context (project × environment × task). A change of context re-assesses the level. A4 only with a *mandate* signed by the `CISO` and a scheduled audit. |
| **REQ-AGN-003** | *Documented and tested operational kill-switch* | — | ✔ | ✔ | For A2+ agents, a documented mechanism exists to halt operation immediately (revoke credentials, terminate the session, isolate the runtime). The *kill-switch* is exercised in sandbox/staging at least once per quarter (A3) or per month (A4); the result is recorded. |
| **REQ-AGN-004** | *Intent declaration before a destructive tool-call* | — | ✔ | ✔ | In A2+ agents, before each *tool call* with a destructive or *side-effectful* effect (deleting, writing externally, rotating secrets, *commit/push*, *deploy*), the agent declares to the infrastructure (structured log, *audit event*) **what it is going to do and why**, before doing it. The gate audits *intent* against *actual action* after the fact. |

> 💡 **Where these requirements land.** [`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) is instrumented by Policy 38 and referenced in Ch. 14. [`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) is declared in the *mandate* (Policy 38) and validated by *guardrails* in Ch. 04 ([`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)). [`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) lands in Ch. 04 (*kill-switch* architecture) and Ch. 12 (the telemetry that triggers it). [`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) lands in Ch. 04 (mechanism) and Ch. 12 (audit signal).

### Proportionality by criticality {#proporcionalidade-por-criticidade}

| Risk level | Minimum requirements | Operational notes |
|---|---|---|
| **L1** | [`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn), [`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) | A2+ permitted only in non-production environments; in production, limit to A0/A1 |
| **L2** | [`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn), [`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn), [`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn), [`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) | A3 in production only for tasks with demonstrated *revert*; A4 outside the typical scope |
| **L3** | All + quarterly audit of the *mandate* register | A4 only with a *mandate* signed by the `CISO` and GRC review; preference for A2 even in mature automation |

### How to classify a concrete use — decision flow {#como-classificar-um-uso-concreto--fluxo-decisório}

1. **Identify the use**: which agent, in which project/environment, for which task.
2. **Map the *tools* invoked** and mark the destructive/*side-effectful* ones.
3. **Map the effect of the worst action** the agent can take within that scope.
4. **Choose the lowest level** compatible with the actual work.
5. **Record the *mandate*** (Policy 38) with level, *tools*, *owner*, review.
6. **Operationalise `REQ-AGN-003/004`** if A2+, before the agent operates.

> 🛑 When in doubt between two levels, the lower one is always chosen. Moving up is always easier than repairing the consequences of having moved up too early.

---

## 🧪 Evidence and audit {#-evidência-e-auditoria}

The evidence **is not the use of the tool**, but rather:

- Test results;
- CI/CD pipeline logs;
- Documented human approvals;
- Traceability between:
  - risk → requirement → control → validation.

Where relevant, there must be an explicit reference that **automation was used**, without any need to detail prompts or models.

---

## 📚 Normative alignment and references {#-alinhamento-normativo-e-referências}

This annex is aligned with the following references:

- **NIST SP 800-218A** - Secure Software Development Framework Profile for GenAI  
- **NIST AI Risk Management Framework 1.0**  
- **ISO/IEC 42001:2023** - AI Management System  
- **OpenSSF – Secure Use of AI Code Assistants**

These references **do not create new application requirements**, but reinforce governance, accountability and validation principles already present in the SbD-ToE.

---

## 🧭 Relationship with other chapters {#-relação-com-outros-capítulos}

- Chapter 1 - Risk classification: the use of automation **does not change L1–L3**;
- Chapter 2 - Security Requirements: requirements remain unchanged;
- Chapter 7 - Secure CI/CD: automated gates become critical;
- Chapter 14 - Governance and Exceptions: policies, training and formal control.

---

## ✅ Conclusion {#-conclusão}

The SbD-ToE **understands and accepts AI as a powerful tool**, but rejects any model in which:
- trust replaces validation;
- automation replaces accountability;
- convenience compromises evidence.

This annex ensures that the adoption of automation **reinforces** - and never weakens - the rigorous application of the security requirements defined in this manual.

