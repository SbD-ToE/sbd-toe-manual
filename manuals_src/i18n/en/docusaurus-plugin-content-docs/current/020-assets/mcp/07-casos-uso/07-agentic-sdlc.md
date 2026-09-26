---
id: agentic-sdlc
title: Agentic SDLC via MCP
description: How to use the SbD-ToE MCP server to support the end-to-end agentic development process — the agent consults the manual via MCP at each stop of the flow, from mandate to kill-switch.
sidebar_label: Agentic SDLC via MCP
sidebar_position: 7
tags:
  - mcp
  - casos-uso
  - agentic
  - sdlc
  - mandate
  - eval-suite
translation:
  source_locale: pt
  source_path: 020-assets/mcp/07-casos-uso/07-agentic-sdlc.md
  source_sha256: 692e89c554f377d542b0dd6e4264c41bf406719e404fce606ea1ab1d7a9ebe79
  source_commit: 4e04c6c26f9325b8a3515d4ccd3b126f58be3b1e
  target_sha256: de59f43c1fe12da2730776403853f39af16fad5366f953a3430570b8f12aed33
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 211df96a27d713b5934d7534d61f1972d877902236e63b858563d206c67ccaa8
  glossary_keys: [chapter_role, cycle_iteration, discipline, framework_source_corpus, mcp, normative_empirical, oracle, practitioner_manual, sbdtoe_sbd, slug_threat_modeling, transversal]
  glossary_sha256: 84fb6866d90c1e8a320d71610fa747e8c1e124d7390bc668883049e09dc5e9d5
  translated_at: 2026-09-26T14:55:20Z
  reviewed_by: null
---

# Use case — Agentic SDLC via MCP

There is a useful symmetry in this use case: the MCP serves so that **the very agent that operates the agentic process** consults the manual before each decision. The agent that classifies another agent's A0–A4 level; the agent that produces another agent's *threat model*; the agent that records the *mandate*; the agent that generates the *eval suite*. At each stop of the [cross-cutting agentic process](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-agentic-sdlc), the MCP serves as the canonical source of what the manual says — so that the decision is *grounded*, not improvised.

The cross-check example (`exemplo-playbook/exemplo-agentic-sdlc`) describes **what** happens at each stop of the process; this use case describes **how** the MCP is invoked at each one. The two are deliberately coupled but separate — the regulatory view lives in the cross-check, the operational view via MCP lives here.

## Prior requirements {#pré-requisitos}

- MCP installed (see [Installation](../03-instalacao.md))
- Canonical skill in `.claude/skills/sbd-toe.md` (see [Skills](../04-skills-agentes.md))
- Familiarity with the [cross-cutting agentic process](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-agentic-sdlc) — this recipe assumes it is being followed

## MCP map by process stop {#mapa-mcp-por-paragem-do-processo}

The table shows, for each stop of the agentic flow, which MCP *tool* / *resource* / *prompt* to use and the expected result.

| Stop | MCP tool | Expected output |
|---|---|---|
| **1. Classify level A0–A4** | `setup_sbd_toe_agent(riskLevel, projectRole)` + `consult_security_requirements(risk_level, ["agents"])` | Active list of `REQ-AGN-*` requirements (the `agents` *concern* activates the AGN category); stringency by chapter at the level |
| **2. Agentic threat model** | `get_threat_landscape(risk_level, concerns=["auth","api","integrity","distribution"])` + `search_sbd_toe_manual("playbook agentic threat library")` | Applicable MITRE ATLAS threat library + citable mitigations (Ch. 03) |
| **3. Validate ARC-015 architecture** | `query_sbd_toe_entities(query="ARC-015")` + `consult_security_requirements(risk_level, ["architecture"])` | Complete acceptance criterion of `ARC-015` + complementary `ARC-001..014` architectural controls |
| **4. Record mandate** | `plan_sbd_toe_repo_governance()` filtering by chapters 02+14 + `get_sbd_toe_chapter_brief("02-requisitos-seguranca")` (for real `artifact_ids`) | Artefacts that the manual requires; mandate template anchored in Policy 38 |
| **5. Pipeline with main agent** | `map_sbd_toe_review_scope(changed_files=["pipeline/agent-runner.yaml"])` + `consult_security_requirements(risk_level, ["auth","logging","distribution"])` | Applicable CI/CD controls (Ch. 07); CI gates; US-04 pattern (secrets) inherited |
| **6. Prompts/skills as code** | `search_sbd_toe_manual("prompts como código revisão skill files")` + `consult_security_requirements(risk_level, ["validation","integrity"])` | Applicable code review controls; documented anti-patterns |
| **7. AI BOM + supply chain** | `search_sbd_toe_manual("AI BOM CycloneDX ml-bom providers")` + `query_sbd_toe_entities(query="DEP-012")` + `query_sbd_toe_entities(query="DEP-014")` | CycloneDX 1.6 format + list of approved providers; approval cycle |
| **8. Eval suite** | `get_guide_by_role(risk_level, role="appsec-engineer", phase="test")` + `search_sbd_toe_manual("C5 eval suites continuous")` | Applicable testing practices; minimum suite composition by level |
| **9. Release gates** | `consult_security_requirements(risk_level, ["distribution"])` + `get_guide_by_role(risk_level, role="devops-sre", phase="deploy")` | Release criteria for A2+; eval *gates* + model rollback |
| **10. Telemetry** | `query_sbd_toe_entities(query="OPS-011")` + `consult_security_requirements(risk_level, ["logging"])` | `OPS-011..014` with acceptance criterion; SIEM integration |
| **11. Mandate review** | `get_guide_by_role(risk_level, role="appsec-engineer")` + `inspect_sbd_toe_retrieval("revisão periódica mandate")` | Cadence by level; review checklist items |

> 📌 When a stop addresses a topic outside the MCP's **canon 00-14** (e.g. detailed contractual clauses with AI providers — it falls outside because legal-specific content lives in the web manual, in Ch. 14 US-21 and Policy 33), the agent must use `WebFetch` on the web manual instead of inventing — see [Use case: Normative cross-check](./06-cross-check-conformidade.md) and [troubleshooting / content lag](../10-troubleshooting-faq.md#content-lag).

## Output discipline {#disciplina-de-output}

At each stop of the process, the agent executing via MCP must:

1. **Cite the exact ID** returned by the tool (`REQ-AGN-001`, `ARC-015`, `DEP-012`, `OPS-014`) — never improvise.
2. **Mark the epistemic label** (see [Epistemics & anti-patterns](../09-epistemica-anti-patterns.md)):
   - `manual-grounded` — retrieved via MCP, with `Document path` recorded
   - `observed` — verified directly in the repository / system (e.g. `tools_allowlist` in the IaC)
   - `inferred` — combination of `manual-grounded` + `observed`
   - `not verified` — when in doubt, prefer this to presenting something as fact
3. **Preserve `mandate_ref`** in any artefact it generates — pipeline manifests, *audit events*, eval reports — so that the audit can reconstruct "which agent, under which mandate, with what authority".
4. **Distinguish three classes of artefact** (cross-link [Use cases — Grounded codegen §discipline](./codegen-grounded)): code, tests, evidence. *Tests* are evidence; code is not.

## Typical sequence in a session {#sequência-típica-numa-sessão}

For a concrete decision — for example, "can this agent move up from A2 to A3?" — the MCP sequence is:

1. `setup_sbd_toe_agent("L2", "appsec")` — loads the stringency by chapter + role rules
2. Read `sbd://toe/agent-guide` (once per session)
3. `consult_security_requirements("L2", ["agents"])` — confirms whether `REQ-AGN-002` is active (yes, at L1+)
4. `search_sbd_toe_manual("A0 A4 níveis de autonomia subir nível critérios")` — extracts the promotion rule
5. `get_guide_by_role("L2", "appsec", "operate")` — applicable review practices
6. Combine with what is in VCS: read the current *mandate*; check whether the *kill-switch* has been exercised according to cadence; check whether the *eval suite* confirms the intended level
7. Decide — `manual-grounded` (manual rule) + `observed` (actual repo state) → final recommendation to the human

Step 7 is where the agent returns the answer to the human who asked — citing real IDs (`REQ-AGN-002`, rule X), stating what it verified (`observed`: kill-switch exercised 2026-04-15), and indicating whether the move up can proceed (`inferred`: conditions satisfied) or whether there is a blocker (`not verified`: evidence of Y missing).

## Skill / subagent — Claude Code {#skill--subagent--claude-code}

`.claude/agents/sbd-toe-agentic-sdlc.md`:

```markdown
---
name: sbd-toe-agentic-sdlc
description: Suporta o processo agentic SDLC ponta-a-ponta consultando o MCP em cada paragem. Não inventa decisões; recolhe evidência grounded e propõe ao humano.
tools: Read, Glob, Grep, mcp__sbd-toe__*
---

# Workflow

1. Ler sbd://toe/agent-guide (1x por sessão).
2. Identificar a paragem do processo agentic em causa (usar o exemplo
   cross-check /sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-agentic-sdlc
   como referência).
3. Para essa paragem, invocar a(s) tool(s) MCP indicada(s) na tabela
   "Mapa MCP por paragem".
4. Combinar com leitura do repositório (mandates em VCS, eval reports,
   audit logs) — distinguir manual-grounded vs observed.
5. Devolver ao humano:
   - IDs do manual citados (manual-grounded)
   - Estado observado (observed)
   - Inferência sustentada (inferred)
   - Itens em falta (not verified)
   - Recomendação final, sem omitir as dúvidas

# Hard rules

- citations (quando `prepare_sbd_toe_codegen_context` é usado) é
  mundo fechado de ids válidos — não inventar.
- Em dúvida, marcar `not verified` em vez de assumir.
- Em decisões A3/A4, propor mas nunca decidir; escalação ao CISO via
  Policy 38 §5.3 é obrigatória.
- mandate_ref preservado em qualquer artefacto produzido.
```

## Anti-patterns {#anti-patterns}

- ❌ **"Claude consulted the MCP and said yes"** without citing concrete IDs — it wastes the advantage of the MCP, which is citable grounding.
- ❌ **Not distinguishing `manual-grounded` from `observed`** — the manual says X, the repo is in state Y; these are two different facts and combining them is an inference.
- ❌ **Skipping stops "because it is already covered"** — each stop has its own acceptance criterion; "implicit" does not count as evidence.
- ❌ **Promoting the A level based on loose interactions in chat without an audit `mandate_ref`** — violates Policy 38 §5.5 (no informal *amendments*).
- ❌ **Treating the MCP as an oracle** — the MCP returns what the manual says; the interpretation for the concrete case remains with whoever operates it (human + agent as assistant).

## Related {#relacionado}

- **Regulatory view of the same process**: [Cross-check — End-to-end agentic SDLC](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-agentic-sdlc) — describes **what** and maps to AI Act/NIS2/DORA/CRA
- [Use case — Grounded codegen](./codegen-grounded) — `citations` discipline applied to *codegen*
- [Use case — Threat modelling](./threat-modeling) — stop 2 in detail
- [Use case — Governance bootstrap](./governance-bootstrap) — stop 4 in detail (mandate scaffolding)
- [Use case — PR audit](./auditoria-pr) — realistic operational case of an A2 agent
- [Epistemics & anti-patterns](../09-epistemica-anti-patterns.md) — labels `manual-grounded` / `observed` / `inferred` / `not verified`
