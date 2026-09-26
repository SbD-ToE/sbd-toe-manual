---
id: policy-uso-ferramentas-apoio
title: Development Support Tools Usage Policy
description: Organisational policy that defines the requirements for the controlled use of development support tools, including generative AI assistants (GenAI/Copilot) and autonomous agents with tool-use (A0–A4), with a focus on mandatory review of output, traceability, licence validation, autonomy mandates and the maintenance of human responsibility, proportional to the criticality level (L1, L2, L3).
tags: [policy, GenAI, Copilot, ferramentas, assistentes IA, revisão, licenças, rastreabilidade, desenvolvimento seguro, cap06, L1, L2, L3, governance, agentic, autonomy]
grupo: desenvolvimento
sidebar_position: 16
translation:
  source_locale: pt
  source_path: 020-assets/policies/16_policy-uso-ferramentas-apoio.md
  source_sha256: 3f3045d1cb240dcbc3905fd05c369f2ac27e8fe1432c3e80aa9d0f924dba51d3
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 33bb96a29f6d619a3ba325936c0d9b6ded4cd0cc50b6d77c6850e3c1b74c767b
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bc04ded428e40ee1c214f8535dfb1904655b64166d0aa82b5df521e4230b8cb0
  glossary_keys: [avaliacao, framework_source_corpus, github_copilot_trust_center, llm, requirement_runtime, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: bce7004dbaef07797cad1f1fc5fe70fd03ac9249c55b5c093b9ad05085ee7661
  translated_at: 2026-09-26T14:10:52Z
  reviewed_by: null
---

# Development Support Tools Usage Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for the **controlled use of development support tools**, with particular emphasis on generative artificial intelligence (GenAI) assistants, code generation tools, assisted autocompletion and automatic suggestion systems.

The adoption of GenAI tools in software development is a growing reality and, when well governed, can increase productivity without compromising security. The risk lies not in the tool itself, but in the absence of review and validation of the generated output - which may contain known vulnerabilities, licence violations, or misalignment with technical and security requirements of which the language model is unaware.

The objective of this policy is to ensure that:

- The use of development support tools is recorded and traceable
- All automatically generated output is subject to human technical review before being accepted
- The technical and security constraints applicable to the project are communicated to the tool and verified in the output
- Responsibility for the quality and security of the code remains human, regardless of the origin of the code

---

## 2. Scope {#2-âmbito}

This policy applies to any development support tool that generates, suggests or completes code, configuration, tests or technical documentation in an automated way, including (non-exclusively):

- GenAI assistants integrated into the IDE (GitHub Copilot, Amazon CodeWhisperer, Tabnine, Cursor, etc.)
- Conversational GenAI assistants used for code generation (ChatGPT, Claude, Gemini, etc.)
- AI-based automated test generation tools
- AI-based generators of IaC, configuration or scripts

The use of deterministic scaffolding tools or of internally curated templates (e.g. `cookiecutter`, approved project templates) is not within the scope of this policy.

---

## 3. Fundamental principle: responsibility is always human {#3-princípio-fundamental-a-responsabilidade-é-sempre-humana}

The use of GenAI tools neither transfers nor dilutes the developer's responsibility for the code produced. AI-generated code is treated as **unaudited third-party code** - it must be read, understood, validated and owned by the developer before being included in a codebase.

:::warning
Accepting automatic suggestions without reading and understanding the generated code is equivalent to copying code from an unknown source without review. This practice is prohibited at any criticality level.
:::

---

## 4. Rules of use by level {#4-regras-de-uso-por-nível}

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Recording of GenAI use in PRs | Optional | Mandatory | Mandatory |
| Human technical review of the output before submission | Mandatory | Mandatory | Mandatory |
| The project's technical constraints communicated to the tool | Recommended | Mandatory | Mandatory |
| Licence validation of the output | Recommended | Mandatory | Mandatory |
| Code review focused on GenAI output | Recommended | Mandatory | Mandatory + AppSec |
| Tools approved by the organisation | Recommended | Mandatory | Mandatory |
| Prohibition on sending confidential code to external tools | Mandatory | Mandatory | Mandatory |

---

## 5. Approval of tools {#5-aprovação-de-ferramentas}

Before a new development support tool is adopted, an assessment must be carried out covering:

- [ ] Data model: are the code or prompts sent used to train the model?
- [ ] Processing location: is the data processed on infrastructure that meets the applicable privacy requirements?
- [ ] Output licence: is there a risk of output with licences incompatible with the product (e.g. contaminating GPL)?
- [ ] Integration with the internal repository: does the tool access confidential code? With what controls?
- [ ] Compliance with applicable regulatory requirements (GDPR, DORA, NIS2, etc.)

The approval must be recorded and the list of approved tools published internally.

:::warning
The use of tools not approved by the organisation to generate production code is prohibited at L2/L3, regardless of whether it is personal use or integrated into the IDE.
:::

---

## 6. Technical constraints {#6-constrangimentos-técnicos}

Before using a GenAI tool to generate code related to a project, the developer must communicate the relevant technical constraints to the tool:

- Technology stack, versions and frameworks in use
- Prohibited or approved libraries
- Mandatory security patterns (e.g. "do not use SQL concatenation", "use ORM X", "follow guideline Y")
- Security requirements applicable to the context

These constraints must be versioned per project (`constrangimentos-genia.md` or equivalent) and referenced in the PRs that include GenAI output.

---

## 7. Traceability of GenAI output {#7-rastreabilidade-do-output-genai}

At L2/L3, PRs that include code generated or significantly assisted by GenAI tools must state this explicitly:

- [ ] Reference in the body of the PR to the tool used (e.g. "Sections X and Y generated with Copilot, reviewed manually")
- [ ] Constraints applied documented or referenced
- [ ] Record in `uso-genia.md` (or equivalent) when applicable to the project

The objective is not to create bureaucracy, but to ensure that reviewers know that the code was generated automatically and must pay heightened attention to its review.

---

## 8. Licence validation {#8-validação-de-licenças}

GenAI tools may suggest code that partially reproduces code under restrictive licences (copyleft). To mitigate this risk:

- [ ] Check whether the tool has a mode that filters suggestions matching public code under incompatible licences (e.g. GitHub Copilot "Duplication detection")
- [ ] Do not accept suggestions of extensive code blocks without checking whether they are derived from licensed code
- [ ] At L3, submit extensive output to licence analysis before inclusion

---

## 9. Prohibition on sending confidential information {#9-proibição-de-envio-de-informação-confidencial}

It is prohibited to send to external GenAI tools (not approved for processing confidential data):

- Code that contains secrets, keys, tokens or credentials
- Production data, PII or data classified as confidential
- Code from systems with information about undisclosed vulnerabilities
- Classified internal documentation

At L3, before any GenAI tool is used in the context of the project, it must be verified whether the service contract covers the applicable confidentiality requirements.

---

## 10. Responsibilities {#10-responsabilidades}

| Role | Responsibility |
|---|---|
| Developer | Use only approved tools; review all output before submitting; record use at L2/L3; not send confidential information |
| Tech Lead | Ensure that the team knows and follows this policy; review PRs with GenAI output with additional attention |
| AppSec Engineer | Define and publish the list of approved tools; review technical constraints per project; assess new tools |
| GRC / Legal | Assess the regulatory and licensing compliance of candidate tools |
| DevOps / SRE | Configure, where applicable, approved tools with controlled access to the repository |

---

## 11. Autonomous agents (A2+) with tool-use {#11-agentes-autónomos-a2-com-tool-use}

Sections 1–10 cover the general case: the tool **suggests** and the developer **decides**. When what the tool does becomes **executing actions with real effect** — opening PRs, reading secrets, performing deploys, writing to external systems — the territory is that of **autonomous agents**, with varying degrees of human supervision. The five-level autonomy model (A0–A4) is defined in [Ch. 02 — Autonomy level model](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia); it applies here without reformulation.

### 11.1 Where this policy applies vs. Policy 38 {#111-onde-esta-política-se-aplica-vs-policy-38}

| Scenario | Covered by |
|---|---|
| Assisted use (A0–A1) — the tool suggests, the developer decides | Sections 1–10 of this policy |
| Autonomous use (A2–A4) — the agent executes real actions | **This section 11** (operational rules) + [Policy 38 — AI Agent Mandates](./policy-mandates-agentes) (mandate, ownership, review) |

> 📌 **The separation matters.** Sections 1–10 are sufficient for Copilot/Cursor in *suggest* mode. From the moment the agent executes (`gh pr create`, `kubectl apply`, `terraform apply`, `npm publish`, any action outside the IDE), Policy 38 applies *in addition to this one*.

### 11.2 Operational rules for A2+ {#112-regras-operacionais-para-a2}

| Rule | A2 | A3 | A4 |
|---|:--:|:--:|:--:|
| **Mandate recorded and versioned in VCS** (Policy 38) | ✔ | ✔ | ✔ |
| **Dedicated identity** with ephemeral workload identity (OIDC, TTL ≤ 1h) — see [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) | ✔ | ✔ | ✔ |
| **Minimum scope per tool** declared in the mandate | ✔ | ✔ | ✔ |
| **Intent declaration** before a destructive tool call ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) | ✔ | ✔ | ✔ |
| **Out-of-band human approval** per destructive action | ✔ | (replaced by auto revert + notification) | (periodic audit only) |
| **Automatic revert** demonstrated in tests | — | ✔ | ✔ |
| **Kill-switch** documented and operational ([`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) | ✔ | ✔ | ✔ |
| **Kill-switch exercised** with a recorded cadence | Annual | Quarterly | Monthly |
| **Mandate signed by `CISO`** (not just recorded) | — | — | ✔ |
| **Periodic audit of the mandate** | Annual | Half-yearly | Quarterly |

### 11.3 Specific prohibitions at A2+ {#113-proibições-específicas-em-a2}

- ❌ **Reusing human credentials** to authenticate the agent. Each agent is a distinct *principal*.
- ❌ **Approving destructive actions within the agent's channel** (e.g. asking for confirmation in the chat where the agent operates) — this violates the out-of-band principle; a response to prompt injection becomes trivially approvable.
- ❌ **Raising the autonomy level (A1 → A2, A2 → A3, …) without review and update of the mandate.** Raising it requires operational evidence of the prior requirements.
- ❌ **Operating in production at A3/A4 without automatic revert demonstrated in a test environment.** If it has not been exercised, it is decorative.
- ❌ **A4 in any project without a mandate signed by the `CISO`.** No exceptions.

### 11.4 Reporting of agent-specific incidents {#114-reporte-de-incidentes-específicos-a-agentes}

The following constitute security incidents that must be reported through the IR process (Ch. 12):

- *Off-policy action*: the agent executed an action outside the scope declared in the mandate.
- *Intent-action divergence*: the real action differs materially from the declared `intent`.
- *Successful prompt injection* that resulted in an unauthorised tool call.
- *Kill-switch failed* or took longer than the agreed time to take effect.
- *Credential exposure*: the agent's identity reused or exposed outside its scope.

---

## 12. Review and audit of this policy {#12-revisão-e-auditoria-desta-política}

This policy must be **reviewed half-yearly** given the rapid evolution of GenAI tools, or after any of the following events:

- Identification of a vulnerability originating in unreviewed GenAI output
- Significant change in the capabilities or data model of an approved tool
- Regulatory change with an impact on the use of AI in software development

---

## 13. Normative and technical references {#13-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 06 - Secure Development | Controlled use of GenAI, traceability, constraints |
| SbD-ToE Ch. 02 - Security Requirements (add-on `09-governaca-automatismos`) | Autonomy level model A0–A4; `REQ-AGN-001..004` |
| SbD-ToE Ch. 04 - Secure Architecture ([`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)) | The agent as a *principal* with ephemeral workload identity and least privilege |
| SbD-ToE Ch. 03 - Threat Modelling (agentic playbook) | Threat library for agents with tool-use (MITRE ATLAS `AML.T*`, OWASP LLM Top 10) |
| Policy 38 — AI Agent Mandates (`38_policy-mandates-agentes.md`) | Operationalisation of [`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn): mandate, ownership, review |
| Code Review Policy (`15_policy-revisao-codigo.md`) | Review of PRs with GenAI output |
| Secure Development Guidelines Curation Policy (`14_policy-guidelines-desenvolvimento.md`) | Technical constraints derived from guidelines |
| MITRE ATLAS | Canonical catalogue of adversarial tactics/techniques for AI systems |
| OWASP Top 10 for LLM Applications (2025) | Security risks in LLM-based applications (LLM01–LLM10 2025) |
| NIST AI RMF 1.0 (2023) + Generative AI Profile (2024) | Risk Management Framework for AI: GOVERN / MAP / MEASURE / MANAGE |
| NIST SP 800-218A | Secure Software Development Framework Profile for GenAI |
| NIST SP 800-207 | Zero Trust Architecture — principles applicable to agents as non-human *principals* |
| ISO/IEC 42001:2023 | AI Management System (aligns with [`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) and periodic review) |
| EU AI Act (Reg. (EU) 2024/1689) | Regulatory requirements for AI systems — see [AI Act cross-check](/sbd-toe/cross-check-normativo/ai-act/intro) |
| ENISA - Cybersecurity of AI | Security guidance for the use of AI in development |
| GitHub Copilot Trust Center | Data model and privacy of a reference tool |
