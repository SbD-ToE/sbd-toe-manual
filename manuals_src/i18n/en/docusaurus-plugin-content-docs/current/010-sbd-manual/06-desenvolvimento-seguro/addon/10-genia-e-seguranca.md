---
id: genia-e-seguranca
title: Use of GenAI in Secure Development
sidebar_position: 10
description: Good practices and controls for the secure use of generative AI tools in code writing and automated review
tags: [genia, ai, código gerado, validação, segurança, revisão]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/06-desenvolvimento-seguro/addon/10-genia-e-seguranca.md
  source_sha256: 02caf89e39c048b5e0b752fef74fb4bf759ea255fccf046ea6b9dec1231c70b7
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 7e8df415030d7f08929364b289ed5fb07bbe2101e1c4be58c84b946c67b051cd
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, discipline, framework_source_corpus, lifecycle_phase, maturity, mcp, practitioner_manual, sbdtoe_sbd, schema, threat, transversal, validation_evaluation, verification_taxonomy]
  glossary_sha256: a4f0e9ead71bab57184406fc1a3c2292d7c575bbcaf7802a7f8e21290b838039
  translated_at: 2026-09-26T08:57:13Z
  reviewed_by: null
---


# Use of GenAI in Secure Development

The integration of generative artificial intelligence (GenAI) tools such as **GitHub Copilot**, **ChatGPT**, **Claude**, **CodeWhisperer**, among others, has become an everyday reality in development - regardless of whether formal policies exist.

These tools have come to act as **continuous assistants**, not only for productivity but also for quality and security. Even without explicit instructions, their presence **influences the way code is written, structured and commented**.

---

## ✅ Why it is relevant in the context of SbD-ToE {#-porque-é-relevante-no-contexto-do-sbd-toe}

- GenAI **automatically suggests secure practices**: input escaping, separation of layers, meaningful names, modularity.
- It works as an **intelligent and adaptive linter**, especially useful for less experienced profiles.
- It makes it possible to **speed up reviews**, generate explanatory comments and detect common failure patterns.
- It can be used to **prototype improvements**, refactor insecure code or generate tests from real code.

> 💡 In many cases, the quality of code generated with the support of GenAI is **higher than the average of the existing legacy code** - not because it is perfect, but because it applies good practices by default.

---

## 🔄 Where it reinforces the chapter's practices {#-onde-reforça-práticas-do-capítulo}

| SbD-ToE practice                     | How GenAI contributes                                                  |
|-------------------------------------|------------------------------------------------------------------------|
| `addon/01` - Code good practices | Suggests secure structures, expressive names, separation of logic     |
| `addon/02` - Linters and validations    | Proposes code that avoids common bad practices (eval, concat, hardcode)  |
| `addon/07` - Team guidelines    | Facilitates the documentation of patterns and refactorings                       |
| `addon/08` - Code validation     | Helps to spot obvious flaws and propose fixes                   |
| `addon/09` - Annotations and evidence   | Generates explanatory comments and `TODO` markers, and can be adapted to `@sec:`   |

---

## 🔍 Points to watch with a critical eye {#-pontos-a-observar-com-atenção-crítica}

Without being a threat, the use of GenAI raises points that must be followed with technical discernment:

- **Not all suggestions are correct or secure** - they require human validation.
- **It may reinforce bad habits** if used passively (e.g. copying without thinking).
- **The origin of suggestions is not always clear** - context and licensing must be taken into account.
- **It promotes technical acceleration** that needs to be accompanied by control and review.

---

## 📌 Organisational considerations {#-considerações-organizacionais}

- The use of GenAI can be beneficial **even without a formal policy**, but it must be **observed with technical maturity**.
- Some organisations choose to define lightweight guidelines: e.g. marking assisted code, not using it in sensitive modules, requiring reinforced review.
- Others may evolve towards more structured policies (e.g. prompt logging, lists of authorised tools), which may be addressed in other chapters.

> 🎯 Most importantly: **ignoring the use of GenAI is no longer realistic**. What the SbD-ToE model proposes is that it be regarded **as part of the modern development flow**, with a critical spirit and responsible integration.

---

## 🌐 Beyond development: the role of AI in Security by Design {#-para-além-do-desenvolvimento-o-papel-da-ia-no-security-by-design}

Although this file focuses on the use of GenAI during the writing and validation of code, there are **multiple emerging applications of AI across the whole Security by Design lifecycle**, including:

- **Secure architecture**: assisted generation of STRIDE models or ATT&CK mappings.
- **Requirements management**: checking for ambiguity, inconsistency or missing controls.
- **Security testing**: generation of fuzzing cases, suggestions of DAST scenarios, exploitation simulation.
- **Prioritisation of findings**: contextual classification of flaws based on stack, criticality and history.
- **Training and technical culture**: personalised microlearning based on the team's real errors.

> 💡 These cases reinforce the idea that **AI can and should be explored as an ally of the SbD-ToE model**, not only in development but across the whole security lifecycle.

### 🧭 Suggested next steps {#-próximos-passos-sugeridos}

The topic “AI applied to Security by Design” will be explored in a more structured way in a **future cross-cutting annex** or dedicated chapter, covering:

- Categories of use by phase (architecture, requirements, testing, validation, training)
- Practical examples
- Integration with existing tools
- Ethical and operational considerations

---

> 📌 GenAI is not a linter, but it **complements one** - with context, natural language and adaptive capability. When used with awareness, it **raises the level of quality and security of the code** produced by any team.

---

## ✍️ Prompts and *skill files* as code {#prompts-como-codigo}

There is a class of artefacts that tends to escape the discipline of *secure development*: the files that *configure* the behaviour of assistants and agents — *system prompts*, *skill files* (`.claude/skills/*.md`), *agent files* (`.claude/agents/*.md`), `.cursorrules`, `.github/copilot-instructions.md`, `AGENTS.md`. These files are treated as **code**, with the same guarantees.

The practical reason is simple: these files decide **what the assistant knows**, **which tools it may invoke**, **how it should interact with the user and with the organisation's resources**. If they change silently — through a *commit* without review, through outdated automatic generation, through a suggestion accepted without being read — they change operational behaviour without a trace. That is exactly the kind of change the *code review* process was designed to prevent in other contexts; the same discipline applies here.

### 🧭 Principles {#-princípios}

1. **Versioning in VCS.** Prompts, *skill files*, *agent files* and *rules* live in the same repository as the code they apply to (or in a dedicated repository, with equivalent integration). Copies in personal *clouds* as the only source of truth are not tolerated.
2. **Review as code.** Every change goes through the same *code review* as application code (see [Policy 15 — Code Review](/sbd-toe/assets/policies/policy-revisao-codigo) §extended scope). Reviewers look for: instructions that escalate privileges, newly added *tools*, wording *escapes*, ambiguities that leave room for *prompt injection*.
3. **Secrets do not go into prompts.** The same rule applies here as to any file in the repo — *secret scanning* runs over these files as over the others (internal URLs, *tenant IDs*, client IDs and *connection strings* count as sensitive).
4. **Auditable origin when generated.** When the content comes from a canonical tool (e.g. `generate_sbd_toe_skill` from the SbD-ToE MCP server — see [MCP mini-site](/sbd-toe/assets/mcp/intro)), the header identifying the source is preserved so that *drift* is detectable.
5. **Regenerate after a source *upgrade*.** A static skill is a *point-in-time* copy. When the *upstream* changes (upgrade of the MCP server, a new version of the *agent guide*, a change in the *runtime*), it is regenerated and re-reviewed; implicit alignment is not relied upon.

### 🛡️ Practical controls {#️-controlos-práticos}

| Control | What it checks | Where it runs |
|---|---|---|
| **Mandatory code review** | *Diff* read by a human reviewer, with attention to privilege escalation and the *tool surface* | PR/MR before the merge |
| Extended **secret scanning** | Patterns of internal URLs, *tokens*, *connection strings*, client IDs — over `.claude/`, `.cursorrules`, `.github/copilot-instructions.md`, `AGENTS.md` | CI/CD; see [Ch. 07 — Gates](/sbd-toe/sbd-manual/cicd-seguro/addon/politicas-gates-pipeline) |
| **Specific diff review** | Changes to `tools_allowlist`, *scopes* and *system prompts* treated as seriously as changes to IAM policies | PR/MR before the merge |
| **Drift detection** | Generated skills vs the current version of the canonical source; alert when the divergence exceeds N days or after a *bump* of the source | Periodic job in CI |
| **Versioned inventory** | List of active *skill files* + *agent files* + *rules* per project, with an *owner* and a re-review cadence | Governance repository |

### ⚠️ Observed anti-patterns {#️-anti-padrões-observados}

- ❌ *Skill file* with the instruction "*always accept the suggestion without asking*" — nullifies [`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) (Ch. 02) at the source.
- ❌ Silent addition of *tools* to the *allowlist* in an agent file via a *commit* without review — equivalent to changing an IAM policy without approval.
- ❌ Prompts referencing `latest` instead of a *pinned* version of the model (cross-reference with `REQ-DEP-AI-002` once it comes into force) — opens the door to an *AI supply chain "rug pull"* (`AML.T0109`).
- ❌ *System prompt* with embedded credentials or *tokens* — the *system prompt* is treated as public content (see [Ch. 04 — boundary controls](/sbd-toe/sbd-manual/arquitetura-segura/recomendacoes-avancadas#ai-ml)); never embed secrets.
- ❌ Static skill never regenerated after an upgrade of the MCP server — reading of outdated canon masquerading as current.

### 📍 Where it lands in the rest of the Manual {#-onde-aterra-no-resto-do-manual}

- **Ch. 02** — [`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) requires a *mandate* versioned in VCS; the *mandate* explicitly references the applicable *skill file(s)* / *agent file(s)* / *system prompt(s)*.
- **Ch. 07** — *secret scanning* and *diff review* of these files are pipeline *gates*.
- **Ch. 12** — *drift detection* feeds an observable signal when the skill diverges from the canonical source beyond the agreed limit.
- **Policy 15** — scope extended to prompts/skills.

> 🧭 In short: prompts are treated as code is treated — versioned, reviewed, *scanned* and regenerated when the source changes. Without discipline they are one more silent vector of operational change; with discipline, they are an auditable artefact like any other in the SDLC.

---

## 🧱 *Structured outputs* — validation of what the model returns {#structured-outputs}

When the model's output feeds application logic — a *tool call* with arguments, a record in a DB, an automated decision — its *format* matters as much as its *content*. In 2026 the main *providers* expose native mechanisms to force the model to return output that adheres to a declared *schema* (Anthropic *tool use* + *structured outputs*, OpenAI *Structured Outputs* / *function calling*, Google *constrained generation*). These mechanisms are adopted wherever feasible and, in any case, **the output is validated on the server before it is consumed**.

### 🧭 Principles {#-princípios-1}

1. **Schema declared server-side.** The model is not trusted to "remember" the format; the *schema* (JSON Schema, *Pydantic*, *Zod*, or equivalent) is declared on the server that makes the call. The *schema* is part of the reviewed code — versioned, tested, *type-checked*.
2. **The *provider's* native mechanisms where they exist.** Anthropic *tool use* + *structured outputs* and OpenAI *Structured Outputs* guarantee (with restrictions) syntactic adherence to the declared *schema*. This is preferred to permissive *parsing* of the raw text.
3. **Double validation — syntactic and semantic.** Adhering to the *schema* is not enough. Correct types, *ranges* within what is expected, IDs that exist in the database, *side effects* within the *scope* of the *mandate* (Policy 38). The model may obey the *schema* and still return `{"action": "delete_database"}` in a context where that is prohibited.
4. **Fail open, with a declared *fallback*.** When the output does not validate, the system **does not consume the output** and follows the declared *fallback* (ask the user, escalate to a human, return a handled error). Never *"try to parse anyway"*.

### 🛡️ Patterns {#️-padrões}

| Pattern | Detail |
|---|---|
| **Schema versioned in the repository** | JSON Schema / Pydantic / Zod defined in code; version referenced in the log for *post-mortem* reconstruction |
| **Canonical *tool definitions*** | When the *providers'* *tool use* is used, the definitions of the *tools* live in the same repository as the code that implements them — not in an embedded prompt |
| **Mandatory pre-execution schema validation** | Output passes through a validator before any action; a failure blocks execution |
| **Per-action semantic validation** | For destructive actions, additional validation that checks `args` against the *scope* declared in the *mandate* — cross-link [`REQ-AGN-004`](../../requisitos-seguranca/addon/governanca-automatismos#req-agn) |
| ***Tool call replay protection*** | Unique identifier per *tool call* + idempotency verification where applicable; prevents accidental re-execution |
| **Schema telemetry** | When the output fails validation, `eval_run_id` + *schema version* + *redacted raw output* go into [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) for diagnosis |

### ⚠️ Anti-patterns {#️-anti-padrões}

- ❌ **Permissive *parsing* of the raw text** — `re.search(r'\{.*\}', output)` is a notorious *anti-pattern*; models with native *tool use* eliminate it.
- ❌ **Validating only the *schema*, without semantic validation** — `{"action": "transfer_all_funds"}` is no less dangerous for adhering to the *schema*.
- ❌ **Relying on the *system prompt* to force the format** ("*always return JSON*") instead of the *provider's* native mechanisms — it works most of the time, and fails exactly when it matters.
- ❌ **Model output feeding `eval()` or equivalent** — if the model's output becomes executed code, any compromise of the model becomes RCE. Treat it literally as *user-untrusted* input.

### 📍 Where it lands in the rest of the Manual {#-onde-aterra-no-resto-do-manual-1}

- **Ch. 02** — [`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) (*intent declaration*) is the semantic counterpart of the *structured output* — declaring the *intent* before the action and validating the *output* before execution are two sides of the same principle.
- **Ch. 04** — [boundary controls for prompt injection](../../arquitetura-segura/recomendacoes-avancadas#boundary-controls-para-prompt-injection) reinforces that the model's output is *user-untrusted*; *structured outputs* give that attitude its operational form.
- **Ch. 10 §C5** — the *eval suite* includes the *adherence rate* to the *schema* as an observable metric.
- **Ch. 12 — [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014)** — semantic validation failures (action outside the *scope*) fall under *off-policy actions*.
