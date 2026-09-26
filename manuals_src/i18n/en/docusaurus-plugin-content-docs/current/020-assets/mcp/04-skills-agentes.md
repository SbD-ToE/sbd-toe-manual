---
id: skills-agentes
title: Skills and agents
description: Configuring the AI client (Claude, Copilot, Cursor) to consult the SbD-ToE automatically — via skill files, agent files, persistent instructions.
sidebar_label: Skills and agents
sidebar_position: 4
tags:
  - mcp
  - skills
  - agentes
  - configuracao
translation:
  source_locale: pt
  source_path: 020-assets/mcp/04-skills-agentes.md
  source_sha256: 403c6085dbd070ff869d48f48b828b85276f524f870c19f7e340c79526676ce4
  source_commit: 4e04c6c26f9325b8a3515d4ccd3b126f58be3b1e
  target_sha256: d157b22379c61e57b3428b771b05a9f21310b524949ea032d63b24c9f88c9022
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 211df96a27d713b5934d7534d61f1972d877902236e63b858563d206c67ccaa8
  glossary_keys: [chapter_role, framework_source_corpus, mapping, maturity, mcp, papel_suporte, practitioner_manual, sbdtoe_sbd, slice]
  glossary_sha256: 4f7e4dc806c3e3544afbbca7658170ec11703d567af19b78c5bcfb2bab7f2565
  translated_at: 2026-09-26T14:55:15Z
  reviewed_by: null
---

# Skills and agents

There is a subtle effect in the daily use of the MCP: the tools become available as soon as the server connects, but the AI client does not start using them spontaneously. It lacks the *when*. For that reason, every modern client allows persistent instructions to be injected at the start of the conversation — *skill*, *agent file*, *rules* or *system prompt*, depending on the client. That is where the client is taught to look up the Manual before improvising.

Instead of those instructions having to be written from scratch (and becoming outdated the next day), the server publishes them via `generate_sbd_toe_skill`. They are generated once, saved in the client's canonical path, and regenerated only after an *upgrade* of the MCP. Short, and always aligned with the source.

## Canonical client → file mapping {#mapeamento-canónico-cliente--ficheiro}

| Client | File path | Scope |
|---|---|---|
| **Claude Code** | Role skill: `.claude/skills/sbd-<role>.md` · subagent: `.claude/agents/sbd-<role>.md` (the `suggested_path` returned by the tool). The *agent guide* without a role does not carry `suggested_path` — save it at a path of choice, for example `.claude/skills/sbd-toe.md` | Per project |
| **GitHub Copilot (VS Code)** | `.github/copilot-instructions.md` | Per repository |
| **Cursor** | `.cursorrules` | Per project |
| **Windsurf / Codeium** | `.codeium/instructions.md` (or equivalent skill) | Per project |
| **Generic** | `AGENTS.md` at the root | Per repository |

## Generating the skill {#gerar-a-skill}

Once the MCP is installed (see [Installation](./03-instalacao.md)), run it in the client. The tool has three forms:

| Call | Returns |
|---|---|
| `generate_sbd_toe_skill()` | the complete canonical *agent guide* (without role specialisation) |
| `generate_sbd_toe_skill(role="appsec-engineer", format="skill")` | a *skill* specialised in that role's *slice* |
| `generate_sbd_toe_skill(role="devops-sre", format="subagent", flavour="harnessed")` | an installable *subagent* definition |

**Parameters:**
- `role` — one of the 13 canonical personas (aliases resolve; unknown role → error with the list of the 13). Without `role`, it returns the *agent guide*.
- `format` — `skill` (guidance file) or `subagent` (agent definition, `.claude/agents/…`).
- `flavour` — `harnessed` (embeds the `mcp__sbd-toe__*` tools; consults the Manual live) or `skilled` (frozen *slice*, no live tools, offline).
- `risk_level` (default `L2`), `phase`, `include_detail`, `tool_prefix`, `clientType` — optional.

The tool returns `content` + `suggested_path` (in role skills and subagents) + `meta.coverage` (chapters, *user stories*, *checklist items* — **declared** coverage, nothing silently truncated). Save it **bytewise** at the `suggested_path` (or at the equivalent path in the client→file table above). The content starts with an identifying header:

```
---
name: sbd-appsec-engineer
description: SbD-ToE appsec-engineer (L2) — … Queries the SbD-ToE MCP live.
tools: …, mcp__sbd-toe__get_guide_by_role, mcp__sbd-toe__consult_security_requirements, …
---
```

:::tip Refreshing
A `skilled` skill (or the *agent guide* without `role`) is a **static** copy at generation time — regenerate it after each *upgrade* of the MCP. A `harnessed` skill/subagent consults the Manual **live**, so it always reflects the current version without regenerating.
:::

---

## Initialising the session {#inicializar-a-sessão}

Even with the skill loaded, the client needs to know the project's **risk level + role**. The canonical *prompt* is:

```
setup_sbd_toe_agent(riskLevel="<L1|L2|L3>", projectRole="<role>")
```

The result is the session's **initial state**:

- What each chapter demands at the `riskLevel` — applicability is graded: every chapter applies, none is excluded
- Active ontology *domains*
- *Role*-specific rules (e.g. for `appsec-engineer`, emphasis on chapters 03/06/10)

Suggestion: pin this *prompt* as the **first message** of any session whose subject is security in the project. It is best not to depend on it alone: it is an MCP *prompt*, and clients without *prompt* support (such as Claude Desktop) do not expose it.

### The declarative contract {#o-contrato-declarativo}

For a concrete task, what the skill should teach the client is the entry point `select_sbd_toe_requirements`: the agent **declares** what it has read — `risk_level`, `concerns`, `exposure`, `data_sensitivity`, `technologies`, `changed_files` — and the server selects the requirements deterministically. The `task` is recorded, not interpreted; without a declaration, the response is `needs_input`, with the accepted vocabulary (`sbd://toe/activation-vocabulary`). To generate code next, `prepare_sbd_toe_codegen_context`. The `consult_security_requirements` remains useful, but for a different question: it returns the level's catalogue, not the selection for a task.

### Canonical roles {#roles-canónicos}

*Aliases* are accepted — the server resolves them automatically.

`developer` · `appsec-engineer` · `arquitetos-software` · `devops-sre` · `qa` · `security-champion` · `product-owner` · `scrum-master` · `operacoes` · `grc-compliance` · `gestao-executiva` · `auditores` · `fornecedores-terceiros`

> These are the Manual's **13 canonical roles** ([Roles and Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)). The server accepts common *aliases* (e.g. `appsec`→`appsec-engineer`, `devops`/`sre`→`devops-sre`, `ciso`→`gestao-executiva`, `compliance`→`grc-compliance`) and always resolves them to one of these 13.

---

## Patterns by client {#padrões-por-cliente}

### Claude Code {#claude-code}

Besides `.claude/skills/sbd-toe.md`, a dedicated *subagent* can be created — generated directly with `generate_sbd_toe_skill(role="auditores", format="subagent")`, or written by hand:

```markdown
---
name: sbd-toe-auditor
description: Auditor de PR contra o manual SbD-ToE — usa o MCP para verificar controlos activos.
tools: Bash, Read, Grep, Glob, mcp__sbd-toe__*
---

Quando recebes um PR para auditar:
1. Identifica o risk_level do projecto (procura em CLAUDE.md ou pergunta ao utilizador).
2. Chama `map_sbd_toe_review_scope` com a lista de ficheiros alterados.
3. Para cada chapter devolvido, chama `consult_security_requirements(risk_level, concerns)`.
4. Compara controlos activos ↔ código alterado; produz relatório com IDs `CTRL-*` citados.
5. Marca cada finding como `manual-grounded` ou `inferred` — nunca como `verified` sem leitura humana.
```

See the complete recipe in [Use case — PR audit](./casos-uso/auditoria-pr).

### GitHub Copilot {#github-copilot}

`.github/copilot-instructions.md` is loaded automatically in *Agent mode*. Add a dedicated section after the canonical content:

```markdown
## Quando aplicar SbD-ToE

Sempre que a tarefa toque em segurança (autenticação, validação, logging,
gestão de segredos, IaC, containers, deploy, monitorização) — antes de propor
código, chamar `select_sbd_toe_requirements` declarando o que se leu
(risk_level, concerns, exposure, data_sensitivity, technologies,
changed_files), ou `prepare_sbd_toe_codegen_context` para gerar o código.
```

### Cursor {#cursor}

`.cursorrules` is a single file — the MCP content coexists with project rules. Keep an explicit **separator**:

```markdown
# Regras do projecto
... regras existentes ...

# SbD-ToE (security guidance — não anula regras do projecto)
<!-- conteúdo do generate_sbd_toe_skill -->
```

---

## Skill *vs* agent file *vs* direct prompt {#skill-vs-agent-file-vs-prompt-directo}

Three levels of integration — choose according to the team's maturity:

| Level | When | How |
|---|---|---|
| **Direct prompt** | Experimental adoption, one-off sessions | Call tools manually: "Use `select_sbd_toe_requirements`, with the declaration of what was read, before proposing code." |
| **Static skill** | Adoption in a fixed project | `generate_sbd_toe_skill(role, format="skill")` → save at the canonical path (auto-loaded) |
| **Subagent / persona** | Recurring workflows (PR audit, *codegen*, *threat model*) | `generate_sbd_toe_skill(role, format="subagent", flavour="harnessed")` → `.claude/agents/sbd-<role>.md` |

The complete recipe for each level is in [Use cases](./casos-uso/) — scenarios with *runnable* examples.

---

## Next {#a-seguir}

- Consult the [complete tools reference](./05-tools-reference.md) to learn what each one does and how to combine them.
- The [use cases](./casos-uso/) show complete flows (input → tool calls → output → final result).
