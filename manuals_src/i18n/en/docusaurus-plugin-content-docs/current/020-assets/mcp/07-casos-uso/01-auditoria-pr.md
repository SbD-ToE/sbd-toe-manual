---
id: auditoria-pr
title: PR audit
description: Automated review of Pull Requests against the active controls of the risk_level — findings citable by CTRL-*.
sidebar_label: PR audit
sidebar_position: 1
tags:
  - mcp
  - casos-uso
  - review
  - audit
translation:
  source_locale: pt
  source_path: 020-assets/mcp/07-casos-uso/01-auditoria-pr.md
  source_sha256: b85ee92695f93f62d38a53a8a35f55fdd076faef8a3cab0089b2c7051e9485ff
  source_commit: 4e04c6c26f9325b8a3515d4ccd3b126f58be3b1e
  target_sha256: 49be31981503383bf06383d292a6f61b8492d2c70b2ef87311054b6c5acfc679
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: da8c4621ee3f200794cd49e34ddc29239ba89f55effb1e5e578d388e50580b8d
  glossary_keys: [discipline, mcp, practitioner_manual, validation_evaluation]
  glossary_sha256: a72f13f664ae812032811b0182c964155ebe19c826837f3b2932f35745641a66
  translated_at: 2026-09-26T17:58:49Z
  reviewed_by: null
---

# Use case — PR audit

Consider a PR opened in the middle of a Friday afternoon. It touches authentication, logging and a configuration file — exactly the kind of mix that the human reviewer struggles to review in depth when there are six other reviews in the queue. The aim of this use case is to give the agent a disciplined routine for that review: to examine the diff *against the project's active controls*, return *findings* with real `CTRL-*` from the manual, and never declare compliance merely because the code exists.

## Prior requirements {#pré-requisitos}

- MCP installed (see [Installation](../03-instalacao.md))
- Canonical skill in `.claude/skills/sbd-toe.md` (see [Skills](../04-skills-agentes.md))
- Project *risk level* known — assume `L2` in the example

## Flow {#fluxo}

### 1. Identify the scope of the PR {#1-identificar-o-escopo-do-pr}

```
git diff --name-only origin/main...HEAD
```

→ e.g.: `src/auth/login.ts`, `src/middleware/audit.ts`, `config/prod.yaml`

### 2. Map files → chapters {#2-mapear-ficheiros--capítulos}

```
map_sbd_toe_review_scope({"changed_files": [
  "src/auth/login.ts",
  "src/middleware/audit.ts",
  "config/prod.yaml"
]})
```

**Expected output** (shape):
```json
{
  "bundles": [
    {"chapter": "06-desenvolvimento-seguro", "reason": "..."},
    {"chapter": "12-monitorizacao-operacoes", "reason": "..."},
    {"chapter": "08-iac-infraestrutura", "reason": "..."}
  ]
}
```

### 3. List active controls by *concern* {#3-listar-controlos-activos-por-concern}

```
consult_security_requirements({"risk_level": "L2", "concerns": ["auth", "logging", "config"]})
```

Returns filtered `controls[]` — use **only these IDs** in the report.

:::tip Declarative alternative
Instead of inferring the *concerns* by hand, the list of changed files can be declared directly in `changed_files` of [`select_sbd_toe_requirements`](../05-tools-reference.md), which activates the chapters through the published table. To close the audit with the expected evidence, `get_sbd_toe_verification_matrix(requirement_ids)` returns, for the selected requirements, the validation method and the expected evidence.
:::

### 4. Cross-reference diff ↔ controls {#4-cruzar-diff--controlos}

For each relevant *hunk*, identify:

- **`CTRL-*` covered** — explicitly addressed by the code
- **`CTRL-*` at risk** — not covered, but in scope
- **`CTRL-*` neutral** — not applicable to this *hunk*

### 5. Generate the report {#5-gerar-relatório}

Mandatory structure:

```markdown
## Findings (manual-grounded)

### `<requisito ou CTRL-…>` — <título>
- **Capítulo:** 06-desenvolvimento-seguro
- **Ficheiro:hunk:** src/auth/login.ts:42-58
- **Status:** ⚠️ partial / ❌ missing / ✅ covered
- **Observação:** <objectiva, refere o controlo>
- **Evidência esperada:** <test path, log shape, scan report — código sozinho NÃO é evidência>

### ...
```

## Output discipline {#disciplina-de-output}

- **Cite exact `CTRL-*`**, never textual approximations.
- Mark each *finding* as `manual-grounded` or `inferred` — never `verified` without human reading.
- For *controls absent from the returned `controls[]`*, write: *"No normative coverage in this scope — flag for human review."*
- **Do not declare regulatory compliance** on the basis of code.

## Skill / subagent — Claude Code {#skill--subagent--claude-code}

`.claude/agents/sbd-toe-pr-auditor.md`:

```markdown
---
name: sbd-toe-pr-auditor
description: Audita um Pull Request contra os controlos activos do SbD-ToE para o risk_level do projecto.
tools: Bash, Read, Grep, Glob, mcp__sbd-toe__*
---

# Workflow

1. Identifica risk_level (procura em CLAUDE.md, AGENTS.md ou pergunta).
2. Lista ficheiros alterados: `git diff --name-only origin/main...HEAD`.
3. Chama map_sbd_toe_review_scope com a lista.
4. Para cada chapter devolvido, infere os concerns aplicáveis (ex.: cap. 06 → desenvolvimento; auth/logging se o código toca login/audit).
5. Chama consult_security_requirements(risk_level, concerns).
6. Para cada CTRL-* devolvido, examina os hunks relevantes (Read + Grep).
7. Produz relatório em Markdown com a estrutura da página de caso de uso.
8. Não inventa IDs. Não declara conformidade. Não trata o próprio código como evidência.
```

## Anti-patterns {#anti-patterns}

- ❌ Inventing `CTRL-00-99` because the control "fits".
- ❌ "PR compliant with NIS2" based on code alone.
- ❌ Mixing `CTRL-*` from chapters not returned by `map_sbd_toe_review_scope`.
- ❌ Skipping `consult_security_requirements` and going straight to `search_sbd_toe_manual` (the structural filter is lost).

## Related {#relacionado}

- [Grounded codegen](./codegen-grounded) — the reverse: generating code that already meets the controls.
- [`map_sbd_toe_review_scope`](../05-tools-reference.md) in the reference.
