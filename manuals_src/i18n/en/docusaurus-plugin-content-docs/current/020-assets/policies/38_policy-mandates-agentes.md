---
id: policy-mandates-agentes
title: AI Agent Mandates Policy
description: Organisational policy that defines the lifecycle of the mandate of each AI agent in operational use — registration, ownership, autonomy levels A0-A4, tool scope, periodic review and revocation, in alignment with REQ-AGN-001..004 of Ch. 02 and ARC-015 of Ch. 04, proportionate to the criticality level (L1, L2, L3).
tags: [policy, agentic, AI, mandates, autonomy, governance, REQ-AGN, ARC-015, L1, L2, L3, cap02, cap04, cap14]
grupo: governacao
sidebar_position: 38
translation:
  source_locale: pt
  source_path: 020-assets/policies/38_policy-mandates-agentes.md
  source_sha256: 9974f1ca0f2e5e47a6de918e4b9cdc5528bc0d3412d84e833634ad4e3ccfde38
  source_commit: 5caf1bb9d128df1f7fb0b1e5b2a5603db3e6127f
  target_sha256: 8b439e39f94dd133b127699afc0155a194f023193bbd79324570e4f5cd662606
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [avaliacao, cycle_iteration, esquema_regime, eu_ai_deployer, eu_ai_high_risk_system, eu_ai_system, framework_source_corpus, lifecycle_phase, llm, mcp, requirement_runtime, risk_level, role_tech_lead, sbdtoe_sbd, schema]
  glossary_sha256: d36d9ddddd1d27e837c4e11ee08e63e70748ad0b1b905532ec5681e4546078de
  translated_at: 2026-09-27T08:34:28Z
  stamped_at: 2026-09-27T08:34:28Z
  reviewed_by: null
---

# AI Agent Mandates Policy

## 1. Objective {#1-objetivo}

This policy defines the **lifecycle of the *mandate*** of each AI agent in operational use in the organisation: how it is registered, who its *owner* is, what level of autonomy (A0–A4) is assigned to it, which *tools* it may invoke, in which environments it operates, and at what cadence it is reviewed.

It directly operationalises requirement [`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia) of Ch. 02 and supports the architectural requirement [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) of Ch. 04. [Policy 16 — Use of Development Support Tools](./policy-uso-ferramentas-apoio) (section 11) covers the operational rules for A2+ agents; this Policy 38 covers the *contract* under which the agent operates.

> 🧭 **In two sentences:** Policy 16 states *what* the agent may and may not do; this Policy 38 states *who decided*, *with what authority*, *for how long*, and *when the question is asked again*.

## 2. Scope {#2-âmbito}

This policy applies to **any AI agent** in operational use in the organisation that operates at **level A1 or above**, including (non-exhaustively):

- AI clients with tool-use capability that act on the organisation's resources (Claude Code, Cursor agent mode, Copilot Workspace, Devin, agents built on the Anthropic SDK or the OpenAI Assistants API)
- Agents integrated into CI/CD (auto-fix of SAST findings, generation and merge of PRs, assisted dependency updates)
- Operations agents (alert remediation, *moderation*, automated maintenance)
- Product agents that act on internal systems at the instruction of an end user

Out of scope:
- A0 use (consultation without execution), which remains covered by Policy 16 sections 1–10
- AI models that are part of the product without external tool-use capability (these fall under Ch. 04 ARC-014 and the AI Act cross-check)

## 3. Fundamental principle: the mandate is a formal act of authorisation {#3-princípio-fundamental-o-mandate-é-um-acto-formal-de-autorização}

A *mandate* is the way in which the organisation declares, in writing and under version control, that it **authorises this agent, with this level of autonomy, to act within this scope, for this period, under this *owner*, with this *kill-switch***. It is not metadata — it is an internal contract between whoever operates the agent and whoever answers for its effect.

:::warning
Operating an A1+ agent without a valid *mandate* is the equivalent of granting *production* access to a non-human identity without IAM review. This practice is prohibited at any criticality level.
:::

A4 additionally requires a **mandate signed by the `CISO`** (or equivalent); without that signature, the agent does not operate at A4.

## 4. Minimum content of a mandate {#4-conteúdo-mínimo-de-um-mandate}

Each *mandate* is a versioned document in VCS (Markdown or YAML format, at the organisation's choice — what matters is the content) with, at a minimum:

| Field | Content | Notes |
|---|---|---|
| `agent_id` | Unique identifier of the agent | Distinct per agent and per environment (e.g. `sbd-toe-pr-auditor@staging`) |
| `agent_runtime` | AI client and version; underlying model and pinned version | E.g. *Claude Code 1.x + claude-opus-4-7*; `latest` prohibited |
| `autonomy_level` | A0 / A1 / A2 / A3 / A4 | As per [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia) |
| `scope` | Repositories, *namespaces*, systems and data on which it operates | Positive list; no unnecessary wildcards |
| `tools_allowlist` | Permitted tools with maximum arguments and *destructiveness* | Each *tool* labelled as `read` / `write` / `destructive` / `external` |
| `environments` | Where it operates (`dev`, `staging`, `prod`, …) | Dedicated identity per environment (Ch. 04 `ARC-011` + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)) |
| `identity_ref` | Workload identity / *service account* / OIDC subject | No reuse of human credentials |
| `owner` | Human responsible for the operation | Necessarily human; with a named *backup* |
| `approver` | Who approved the mandate | `tech lead` (L1), `appsec + tech lead` (L2), `CISO + appsec + grc` (L3 or A4) |
| `kill_switch` | Procedure + responsible party + maximum time to effect | Documented and exercisable ([`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) |
| `intent_audit_sink` | Where the *intent events* land ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) | Observable system (Ch. 12) |
| `review_cadence` | When the question is asked again | A1: annual · A2: annual · A3: half-yearly · A4: quarterly |
| `effective_from` / `effective_until` | Validity window of the mandate | `effective_until` mandatory; no "forever" mandates |
| `risk_residual` | What this authorisation does not cover / accepts | Honest about limits |

> 💡 Example templates: see `020-assets/templates/mandate-agente.yaml` once it is published. Until then, the schema above is sufficient to get started.

## 5. Mandate lifecycle {#5-ciclo-de-vida-do-mandate}

```
[Proposta] → [Avaliação] → [Aprovação] → [Activação] → [Operação] → [Revisão / Renovação | Revogação]
```

### 5.1 Proposal {#51-proposta}

Whoever intends to operate an agent at A1+ submits a *mandate* proposal containing all the fields of section 4 and a justification of the chosen level of autonomy. The justification answers *"why A2 and not A1?"* — declaring is not enough; it must be substantiated.

### 5.2 Assessment {#52-avaliação}

| Criterion | Who assesses |
|---|---|
| Technical adequacy of the level to the actual work | `tech lead` + `appsec` |
| Adequacy of the *scope* and of the *tools_allowlist* (least privilege) | `appsec` |
| Adequacy of the *kill-switch* and of its time to effect | `appsec` + `devops` |
| Coverage of revert tests (A3+) | `qa` + `tech lead` |
| Regulatory compliance (AI Act, GDPR, etc., where applicable) | `grc` / `compliance` |

### 5.3 Approval {#53-aprovação}

| Level | Required approver |
|---|---|
| A1 | `tech lead` |
| A2 | `tech lead` + `appsec` |
| A3 | `tech lead` + `appsec` + `grc` |
| A4 | `CISO` (formal signature) + `appsec` + `grc` |

Approval is recorded in the *mandate* itself (`approver` field + signed commit in VCS).

### 5.4 Activation {#54-activação}

On activation, the following operational prior requirements are verified:

- [ ] Ephemeral agent identity created (`identity_ref` resolves to the real workload identity)
- [ ] *Scope* and *tools_allowlist* configured in the infrastructure (not merely declared in the document)
- [ ] *Kill-switch* tested in sandbox/staging with the timing recorded
- [ ] *Intent events* sink receiving test events
- [ ] Notification to the *owner* + *backup* configured

Without all the prior requirements, the agent remains at A1; it does not operate at the requested level.

### 5.5 Operation {#55-operação}

During operation the *mandate* is the source of truth for what the agent may do. Any change of *scope*, *tools_allowlist* or *autonomy_level* requires a **new Proposal → Approval cycle** — there are no informal *amendments*.

### 5.6 Review / Renewal {#56-revisão--renovação}

At the declared cadence (`review_cadence`), the *owner* + `appsec` review:

- [ ] *Intent events* in the window: any *intent-action divergence* observed?
- [ ] Any *off-policy actions* recorded?
- [ ] *Kill-switch* exercised at the required cadence (A3 quarterly, A4 monthly)?
- [ ] Did the model provider keep the pinned version?
- [ ] Is the *tools_allowlist* still proportionate to the actual work?

Outcome: renewal (with or without changes), downgrade of level, or revocation.

### 5.7 Revocation {#57-revogação}

Revocation is carried out **immediately** through the *kill-switch* in the following situations:

- *Off-policy action* with material effect
- Successful *prompt injection* resulting in an unauthorised tool call
- *Credential exposure* of the agent's identity
- *Kill-switch* failure (even without a material incident — a breach of operational trust)
- Silent change of provider/model (e.g. *AI supply chain "rug pull"*, `AML.T0109`)

Revocation is not synonymous with definitive termination — re-issue may follow after a *post-mortem* analysis and a new *mandate*.

## 6. Mandatory periodic review of the organisational register {#6-revisão-periódica-obrigatória-do-registo-organizacional}

Independently of the per-*mandate* reviews, the organisation reviews **the full set** of active *mandates* at the following cadence:

| Risk level | Organisational review cadence |
|---|---|
| L1 | Annual |
| L2 | Half-yearly |
| L3 | Quarterly |

The organisational review covers: *mandates* without an active *owner* (e.g. the person has left the company), *mandates* whose `effective_until` has passed, operational agents without a corresponding *mandate*, and *mandates* at levels that the work does not justify (under-use or *overprivilege*).

## 7. Responsibilities {#7-responsabilidades}

| Role | Responsibility |
|---|---|
| **Agent owner** | Submit the mandate proposal; operate within the scope; report incidents; take part in reviews; exercise the kill-switch at the required cadence |
| **AppSec Engineer** | Assess technical adequacy and least privilege; review intent events; approve A2+; audit active mandates |
| **Tech Lead** | Approve A1/A2; ensure that the team follows this policy; appoint the *owner* and the *backup* |
| **DevOps / SRE** | Provision the ephemeral workload identity, the operational kill-switch and the intent events sink; guarantee the kill-switch time to effect |
| **GRC / Compliance** | Assess regulatory compliance; approve A3/A4; conduct the periodic organisational review |
| **CISO** | Sign A4 mandates; approve the policy and its reviews; arbitrate scope conflicts |
| **Auditors** | Audit the mandate register + intent events against actual actions; flag divergences |

## 8. Proportionality by criticality level {#8-proporcionalidade-por-nível-de-criticidade}

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Mandate registered for A1+ | Mandatory | Mandatory | Mandatory |
| A2 permitted in production | No | Yes (with guardrails) | Yes (with reinforced guardrails) |
| A3 permitted in production | No | Yes (with demonstrated revert) | Yes (only with informal monthly audit) |
| A4 permitted | No | No (except by formal exception approved by the `CISO`) | Yes (with signed mandate) |
| Organisational review of the mandate register | Annual | Half-yearly | Quarterly |
| Mandate signed by the `CISO` | A4 only (rare) | A4 only | A4 always; A3 recommended |

## 9. Exception management {#9-gestão-de-exceções}

Exceptions to this policy follow the formal process defined in Ch. 14 and in [`Policy 05 — Gestão de Excepções`](./policy-gestao-excecoes):

- An exception has an explicit TTL (recommended ≤ 90 days).
- An exception at A3/A4 requires additional approval from the `CISO`.
- Accumulated exceptions (>2 on the same agent in 12 months) require a review of the *mandate*.

## 10. Review and audit of this policy {#10-revisão-e-auditoria-desta-política}

This policy must be **reviewed half-yearly** given the rapid evolution of AI agent capabilities, or after any of the following events:

- Incident involving an *off-policy action*, *intent-action divergence* or successful *prompt injection* in an A1+ agent
- Applicable regulatory change (AI Act, NIS2, DORA, GDPR) with an impact on agent autonomy
- Significant change in the capabilities of the supported AI *runtimes* (e.g. a new class of tool-use)
- Review of [Policy 16 — Use of Development Support Tools](./policy-uso-ferramentas-apoio) with an impact on the perimeter

## 11. Normative and technical references {#11-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 02 (addon `09-governaca-automatismos`) | A0–A4 model and `REQ-AGN-001..004` requirements |
| SbD-ToE Ch. 03 (agentic playbook) | Threat library for agents with tool-use |
| SbD-ToE Ch. 04 ([`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)) | Architectural patterns: the agent as an isolated *principal* |
| SbD-ToE Ch. 14 — Governance and Contracting | Exceptions, contracting, audit |
| [Policy 16 — Use of Development Support Tools](./policy-uso-ferramentas-apoio) | A2+ operational rules |
| [Policy 05 — Exception Management](./policy-gestao-excecoes) | Formal exception process |
| [Policy 18 — Secrets Management](./policy-gestao-segredos) | Ephemeral identity (OIDC) — inherited pattern |
| MITRE ATLAS | Catalogue of adversarial tactics/techniques (Threats `AML.T*` referenced in the Ch. 03 agentic playbook) |
| OWASP Top 10 for LLM Applications (2025) | LLM06-2025 Excessive Agency, LLM01-2025 Prompt Injection |
| OWASP MCP Top 10 (2025) | Applicable when the agent exposes or operates its own MCP server — *tool poisoning*, *excessive permissions*, authentication/authorisation, monitoring |
| NIST AI RMF 1.0 (2023) + Generative AI Profile (2024) | GOVERN-1.x (policies and ownership); MANAGE-4.x (review and revocation) |
| NIST SP 800-207 | Zero Trust — the agent as a non-human *principal* |
| NIST SP 800-218A | SSDF Profile for GenAI |
| ISO/IEC 42001:2023 | AI Management System — lifecycle, ownership, review |
| EU AI Act (Reg. (EU) 2024/1689) | Art. 14 (Human oversight); Art. 26 (Obligations of deployers of high-risk AI systems) — see [AI Act cross-check](/sbd-toe/cross-check-normativo/ai-act/intro) |
