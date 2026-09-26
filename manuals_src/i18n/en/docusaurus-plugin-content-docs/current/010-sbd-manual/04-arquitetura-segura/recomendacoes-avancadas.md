---
id: recomendacoes-avancadas
title: Advanced Recommendations - Secure Architecture
description: Advanced practices for contexts of high maturity in secure architecture
tags: [avancado, arquitetura, maturidade, zero-trust, sbomm]
sidebar_position: 30
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/recomendacoes-avancadas.md
  source_sha256: 06653bccc378030261c441cc94979a6809671337923b543ba1d603bbaa22a604
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 545f56afeeace79a0f6373efd11fcce4b9023cc0c9b17c7a033e477dd23f4fb2
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, framework_source_corpus, layer, llm, maturity, mcp, plain_rag, requirement_runtime, slug_threat_modeling, validation_evaluation]
  glossary_sha256: 6ce1ffc289f6d57706c2bcbbccf4e930b9f37b9365426dde1d1bbf19bacdbecb
  translated_at: 2026-09-26T08:32:13Z
  stamped_at: 2026-09-26T18:33:43Z
  reviewed_by: null
---

# Advanced Recommendations - Secure Architecture

This document complements the chapter's foundational practices with recommendations aimed at contexts of **high organisational maturity**, critical systems or regulated environments.

> The recommendations described here are optional, but highly desirable for teams that already apply the ARC requirements consistently.

---

## 🧱 Advanced Architectural Recommendations {#-recomendações-arquitetónicas-avançadas}

| Practice / Recommendation                             | Direct benefit                             | Reinforced requirements |
|------------------------------------------------------|------------------------------------------------|------------------------|
| Adopt the Zero Trust principle between microservices  | Reduces the risk of lateral movement                | ARC-002, ARC-006       |
| Apply OPA or rego for dynamic enforcement        | Governs the architecture's access policies       | ARC-001, ARC-008       |
| Use sidecars for security and inter-service communication | Creates network control and distributed logging   | ARC-002, ARC-003       |
| Apply segmentation in the CI/CD environment             | Ensures that execution reflects the architectural design | ARC-004, ARC-007 |
| Integrate threat modelling into stories and epics          | Detects flaws before detailed design       | ARC-005, ARC-010       |
| Formalise ADRs for all architecture decisions  | Improves auditability and future review        | ARC-004, ARC-011       |
| Validate consistency between architecture and SBOMs       | Ensures that the SBOM reflects the planned architecture | ARC-006, ARC-007       |

---

## 🧩 Recommended Models and Frameworks {#-modelos-e-frameworks-recomendados}

- **Context-Based Trust Model** (Context-Aware Trust Models)
- **Architecture Decision Records (ADRs)** with Git integration
- **Risk-Based Zoning Models**
- **Threat Modelling as part of the Definition of Done**
- **Frameworks**: SABSA, ISO/IEC 42010, NIST SP 800-160 Vol 1
- **SBOMM** (Security BOM Maturity Model) - integration between architecture and software composition

---

## ✅ When to apply these recommendations? {#-quando-aplicar-estas-recomendações}

- Regulated environments (finance, healthcare, defence)
- Highly complex distributed architectures (e.g. multicloud, event-driven)
- Platforms with a high volume of external integration
- Organisations with a dedicated architecture or security function

> 🧭 These recommendations align with the highest maturity levels in SAMM, SSDF and DSOMM.

---

## 🤖 Architectural patterns for AI/ML systems {#ai-ml}

Systems that integrate artificial intelligence components — LLMs in a conversational interface, predictive models, retrieval-augmented generation (RAG) systems, autonomous agents with tool invocation — introduce architectural patterns with attack surfaces qualitatively distinct from those of traditional applications. The recommendations in this section complement (they do not replace) ARC-001..ARC-013 and operationalise requirement [ARC-014](./addon/catalogo-requisitos-arquitetura#arc-014).

### Trust zones in AI/ML architectures {#trust-zones-em-arquitecturas-aiml}

AI/ML components introduce three classes of trust boundary that must be explicitly marked in DFDs:

| Boundary | Description | Canonical threats | Typical architectural controls |
|---|---|---|---|
| **Training-time** | Between external datasets and the training pipeline | Training data poisoning (`AML.T0020`); Publish Poisoned Datasets (`AML.T0019`); ML02-2023 Data Poisoning | Source curation; dataset checksum/signature; isolation of the training pipeline; human review before retraining |
| **Inference-time** | Between external input (user, RAG retrieval, file ingestion) and the model context | Direct and indirect prompt injection (LLM01-2025; `AML.T0051.001`); `AML.T0093` Prompt Infiltration via Public-Facing App | Input sanitisation specific to the prompt context; clear separation between system prompt and user input; output filtering against system-prompt extraction |
| **Agentic** | Between the model output and the tool invocations executed (functions, MCP servers, APIs) | Exfiltration via AI Agent Tool Invocation (`AML.T0086`); AI Agent Tool Poisoning (`AML.T0110`); Data Destruction via AI Agent (`AML.T0101`); LLM06-2025 Excessive Agency | Human approval for write/mutating actions; rate limiting per tool; allowlist of tool scopes; full logging of tool calls (see Ch. 12 — AI observability) |

### Boundary controls for prompt injection {#boundary-controls-para-prompt-injection}

Prompt injection is the most common architectural vulnerability in LLM applications. Relevant architectural controls:

- **Separate by channel** the system prompt (application configuration) from user input (untrusted data) — use structured messages (e.g. `system`/`user`/`assistant` roles) instead of string concatenation
- **Treat all retrieval-augmented content as user-level untrusted** — in RAG systems, returned documents are external data; apply the same controls as to direct user input (`AML.T0051.001` Indirect Prompt Injection)
- **Output filtering** against system-prompt extraction (`AML.T0069.002`); detect instruction exfiltration patterns
- **Confidentiality of system prompts** — do not assume the content is secret; architect it as if it were public

### LLM ↔ backend tool invocation security {#llm--backend-tool-invocation-security}

AI agents capable of invoking backend tools (APIs, file systems, databases via MCP, function calls) require architectural isolation analogous to privilege control in traditional systems:

- **Principle of least privilege applied to agents** — each tool exposed to an AI agent must have the minimum necessary scope; agents must not operate with real user credentials (LLM06-2025 Excessive Agency)
- **Out-of-band human approval** for tool calls with critical impact (delete, transfer, send) — particularly relevant in workflows where the agent is autonomous
- **Full audit of tool invocations** — each call with timestamp, context, agent identity, scope; integrate with the Ch. 12 observability pipeline (`AML.M0024` AI Telemetry Logging)
- **Validation of MCP servers and tools** as supply chain dependencies — see Ch. 5 §AI/ML for the supply chain framing (`AML.T0110` AI Agent Tool Poisoning)

### Design considerations {#considerações-de-design}

- **AI components are NOT opaque libraries** — they must appear as distinct participants in architecture DFDs, with inputs, outputs, dependencies (models, datasets, prompts) and trust boundaries explicitly modelled
- **Cross-zone propagation** — outputs of AI models may propagate to high-trust zones (e.g. model output used to take automatic decisions in critical systems); apply the same propagation analysis that would be applied to untrusted external inputs
- **Resilience to model degradation** — the design considers a fallback for when the model is unavailable, returns degraded outputs, or has been compromised (`AML.T0031` Erode AI Model Integrity)

> Threat modelling analysis for AI/ML architectures uses MITRE ATLAS as a complement to STRIDE — see [Ch. 03 — AI/ML Methodologies](../threat-modeling/addon/metodologias-e-ferramentas#ai-ml).

### Patterns for AI agents as *principals* (ARC-015) {#agentes-principals}

The patterns above cover *AI/ML components* in general. When the system has **autonomous agents** that execute actions with real effect — invoking tools, creating PRs, reading secrets, deploying, writing to external systems — a different architectural posture is adopted: the agent is treated as **one more non-human *principal***, subject to the same principles applied to traditional *workload identities*, specialised for the case in which the one deciding the next action is a model.

This section operationalises requirement [ARC-015](./addon/catalogo-requisitos-arquitetura#arc-015) and cross-references the `REQ-AGN-001..004` requirements defined in [Ch. 02 — Autonomy levels model](../requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia).

#### Agent identity — ephemeral workload identity {#identidade-do-agente--workload-identity-efémera}

- **Dedicated identity per agent** (and per environment). The agent receives credentials via **OIDC / workload identity**, with TTL ≤ 1h, without reuse of a human identity. The same principle as US-04 of Ch. 07 and US-10 of Ch. 08 — applied to a new type of *principal*.
- **Minimum scope per tool** (and per environment, see `ARC-011`). An agent that needs to open PRs **does not receive** *scope* to delete the repository; an agent operating in *staging* **does not see** *production* credentials. No tacit exceptions.
- **Revocation by *kill-switch*** (see [`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) must be architecturally possible within seconds — i.e. credential revocation cannot depend on a redeploy or on eventual propagation.

> The rule that applies to human *workload identity* — *"if the credential has to be shared, the design is wrong"* — holds literally for agents. If two agents share the same identity, the *audit trail* ceases to be useful.

#### Intent declaration before destructive tool calls {#intent-declaration-antes-de-tool-calls-destrutivos}

At levels A2+, before each *tool call* with a destructive effect, a *side-effectful* one or one on critical external systems, the agent declares to the infrastructure **what it is going to do and why**. The *intent* is a structured event, recorded in audit, with (at a minimum): agent identity, *tool* to be invoked, material arguments, human-readable *intent*, *expected outcome*, *residual risk* from the agent's perspective. The operational *gate* validates declared *intent* vs *action actually executed* a posteriori — divergence is a signal of an incident.

| *Intent event* field | Purpose |
|---|---|
| `agent_id` | Identity of the *principal* (ARC-015) |
| `mandate_ref` | Version of the *mandate* under which the agent operates ([`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) |
| `tool` + `args` | What is going to be invoked and with which material arguments |
| `intent` | Human-readable sentence: "I am going to do X to resolve Y" |
| `expected_outcome` | Expected post-action state |
| `risk_self_assessment` | What the agent considers the residual risk of the action |

This design does not ask the agent to *ask permission* at every step — it asks it to **leave a trail** of what it intended to do before doing it. The difference is operational: it makes it possible to compare intention and action, and to detect off-policy behaviour even when the isolated action seems legitimate.

#### Out-of-band human approval {#aprovação-humana-out-of-band}

For actions with a critical effect (delete, transfer, send, deploy, rotate-secrets, contacting sensitive external systems), approval **outside the agent's channel** is required — Slack approval, GitHub review with 2FA, signed webhook, *push notification* to an on-call human. The reason is simple: if the approval channel is the same one in which the agent acts, the approval is subject to the same set of adversaries as the main channel (prompt injection included). Out-of-band forces a *real human, in an independent channel*, to confirm.

#### Operational kill-switch {#kill-switch-operacional}

The *kill-switch* ([`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) is an architectural mechanism, not a symbolic button. It is composed of:

- **Immediate credential revocation** (revocation of the OIDC token; *workload identity* binding invalidated within seconds).
- **Termination of the agent's *runtime*** (MCP session closed; *worker* terminated).
- **Isolation of the *namespace*** in which the agent operated (preventing reanimation until diagnosis).
- **Operational signal** (on-call alert) to ensure that a human knows it was triggered.

At A3/A4 the *kill-switch* is exercised in sandbox/staging with a recorded cadence (≥ 1×/quarter for A3, ≥ 1×/month for A4). Without this exercise, the *kill-switch* is decorative.

#### Full audit per tool invocation {#audit-completo-por-tool-invocation}

Each *tool call* generates a structured *audit event* — logging "agent did something" is not enough. The suggested minimum:

- `timestamp`, `agent_id`, `session_id`, `mandate_ref`, `autonomy_level` (A0–A4)
- `tool`, `tool_version`, `args` (with redaction of PII and secrets)
- `intent_event_ref` (reference to the declared *intent*, if A2+)
- `outcome`: success / failure / timeout / rejected_by_gate; return payload (summarised)
- `external_effect`: if the tool affected an external system, which one and how (URL, resource, state change)

These events feed directly into the Ch. 12 observability (landing in v1.6.0 — `REQ-MON-AI-*`) and the evidence for periodic operational audit (Ch. 14).

> 🧭 Everything described in this section is a specialisation of what is already practised for traditional non-human identities. If the team already has maturity in OIDC + minimum scope + audit per invocation, all it lacks is to recognise the agent as one more *principal* passing through the same sieve — and to add *intent declaration* and an exercised *kill-switch*, which are the two genuinely new pieces.

### Patterns for RAG systems (*Retrieval-Augmented Generation*) {#rag-patterns}

RAG is today the dominant architecture in production LLM applications — the model receives, in addition to the user's *prompt*, content retrieved from an external source (document base, vector DB, corporate *knowledge base*) that enriches the context. The operational advantage is clear: answers based on the organisation's current information without retraining the model. The price is that **the `inference-time` boundary ceases to be a single one** — there are now two distinct entries into the model context, with very different degrees of trust, and both deserve treatment as *user-untrusted*.

This section complements what has already been said about [trust zones in AI/ML architectures](#ai-ml) and [boundary controls for prompt injection](#boundary-controls-para-prompt-injection), with the operational specialisation for RAG.

#### What changes in RAG {#o-que-muda-em-rag}

| New component | What it introduces | Why it matters for security |
|---|---|---|
| **Vector DB / *index store*** | Stores *embeddings* + document chunks | New supply chain asset; dedicated access control and integrity |
| ***Embedding model*** | Converts query and documents into vectors | Additional dependency in the chain (model registry); mandatory *pinning* |
| ***Retriever*** | Selects top-k chunks by vector similarity | Determines what enters the LLM context; new *attack surface* |
| ***Re-ranker*** (optional) | Re-orders retrieved chunks | Additional manipulation point if model-based |
| ***Document corpus*** | Source of content to be ingested | Primary vector of *indirect prompt injection* (`AML.T0051.001`) |

#### Architectural patterns for secure RAG {#padrões-arquitectónicos-para-rag-seguro}

- **Treat *retrieved content* as *user-untrusted* by design** — in RAG, the retrieved document enters the model context as if it were user text. The control from the [boundary controls for prompt injection](#boundary-controls-para-prompt-injection) section applies literally: canonical `system` / `user` / `retrieved_context` separation when the model supports it (Anthropic *documents* parameter, OpenAI *tool messages*) — no *string concatenation*. Where the model does not distinguish structurally, isolate with *delimiters* + *prompt hardening* in the *system prompt*.
- **Ingestion curation** — documents ingested into the corpus go through a curation *pipeline*: origin validation, *content scanning* for known adversarial patterns (LLM01-2025 *indirect prompt injection* patterns), sensitivity classification. Do not treat ingestion as *trusted by default*.
- **Vector DB as a critical asset** — access control (authentication + per-namespace authorisation), *audit log* of reads and writes, encryption *at-rest* and *in-transit*, integrity of the *embeddings* (hash over the original content that originated each *embedding*).
- ***Embedding model* pinned** — explicit fixed version (cross-link [`DEP-013`](../dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013)). A major version change of the *embedding model* requires re-indexing the entire corpus and re-running the RAG *eval suite* (see below) — *embedding spaces* are not compatible across major versions.
- ***Retriever* with authorisation filters** — top-k retrieval respects the *row-level security* / *namespace boundary* of the user making the query. A classic failure in corporate RAG: user A can see chunks belonging to user B's perimeter because the retriever does not filter. It is treated as normal *access control*.
- ***Output filtering* against corpus extraction** — detect patterns in which the model is regurgitating corpus content without processing it (potential *membership inference* about which documents are in the index, or targeted *exfiltration*).
- ***Provenance* in the output** — when the model cites corpus documents, expose *provenance* (which document, which chunk) to the user. It has a dual function: auditability and making silent exfiltration harder.

#### RAG-specific threats {#threats-específicas-a-rag}

The following RAG-specific vectors are added to the [agentic threat library of Ch. 03](../threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic):

| Threat | ID | Target boundary | Primary mitigation |
|---|---|---|---|
| ***Indirect prompt injection* via ingested document** | `AML.T0051.001` · LLM01-2025 | Inference (via retrieval) | Ingestion curation; treat *retrieved content* as *user-untrusted*; *output filtering* |
| ***Embedding poisoning*** (training-time of the *embedding model* or ingestion-time of the corpus) | `AML.T0020` (adapted) | Training-time / Ingestion-time | *Embedding model* from an approved source ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)); ingestion validation |
| ***Vector DB exfiltration*** | `AML.T0086` (adapted) | Vector DB | Access control + audit; *row-level security* in the retriever |
| ***Membership inference* on the corpus** | LLM02-2025 (*sensitive info disclosure*) | Inference | *Output filtering*; rate-limiting; detection of *probing queries* |
| ***Cross-namespace contamination*** | LLM06-2025 (*excessive agency*, in a RAG variant) | Retriever | Authorisation filter in top-k retrieval |

#### Eval suite for RAG {#eval-suite-para-rag}

The *eval suite* (Ch. 10 §C5) gains a layer of its own in RAG:

- ***Retrieval relevance*** — does the top-k contain chunks relevant to the query?
- ***Citation faithfulness*** — does the output cite the retrieved chunks correctly, without inventing content?
- ***Adversarial documents corpus*** — documents with known *indirect prompt injection* attempts must be detected or neutralised without altering the model's behaviour.
- ***Cross-namespace isolation*** — a query by user A never returns chunks from B's namespace.

For A2+ systems that invoke *tools* from a RAG context, this layer of the *eval suite* is mandatory — because the most common attack vector in production is precisely *"poisoned document leads the agent to invoke a destructive tool"*.

> 🧭 RAG is often seen as "just adding context to the prompt". Technically it is more than that: it introduces a new trust boundary (`retrieved_context`) that has the same power to manipulate the model as user input, but arrives through a channel that seems internal. It is this asymmetry that makes secure RAG a distinct architectural problem.

### Note on multi-agent systems {#nota-sobre-sistemas-multi-agente}

Multi-agent orchestration *frameworks* (*LangGraph*, *CrewAI*, *AutoGen*, *orchestrator → executor → reviewer* built on their own SDKs) became common during 2024–2025 and continue to evolve rapidly. No dedicated section is written because the solution space **has not yet stabilised** — conventions for *agent-to-agent communication*, *trust delegation* between agents and hierarchical supervision vary significantly between *frameworks*. The operational principle is, however, stable:

- **Each agent in the system is a distinct *principal*** ([`ARC-015`](./addon/catalogo-requisitos-arquitetura#arc-015)) with its own identity, *mandate* (Policy 38) and A0–A4 level. An orchestrator does not "lend" its credentials to a sub-agent.
- **Explicit *trust delegation*** — when one agent invokes another, the call is treated as a *tool call* (audited by [`OPS-012`](../monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012)), with `intent` declared when destructive.
- ***Out-of-band approval* at the executing agent**, not at the orchestrator — human approval is required at the point where the destructive action happens, not at the point where it was decided.

When multi-agent patterns stabilise (probably 2026–2027), this will be revisited to extract a dedicated section based on accumulated operational practice.

---

## 📌 Final Consideration {#-consideração-final}

These practices do not replace the normative requirements (ARC), but represent **natural next steps for teams that already apply secure architecture in a structured and consistent way**.

> Applying these recommendations selectively can accelerate maturity and prepares the organisation for governance models based on evidence and distributed control.
