---
id: onboarding-formacao
title: Onboarding by role
description: get_guide_by_role to generate personalised onboarding guides — practices by SDLC phase + user stories joined.
sidebar_label: Onboarding by role
sidebar_position: 5
tags:
  - mcp
  - casos-uso
  - onboarding
  - training
  - roles
translation:
  source_locale: pt
  source_path: 020-assets/mcp/07-casos-uso/05-onboarding-formacao.md
  source_sha256: b41e912f1ac1fe5e6ca67b92611cb40b40f21ee5aba34009cab83c8bf8f9ffe2
  source_commit: 4e04c6c26f9325b8a3515d4ccd3b126f58be3b1e
  target_sha256: 5721366cea116e24693ce43da82fceb80ff9f60cdacf346336e1702865bde960
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, discipline, lifecycle_phase, mcp, papel_suporte, practitioner_manual]
  glossary_sha256: 28c3e93ae4d5394f3b4776f1395f8b2598f3d639e9edc8505f7756d1e4c8ae82
  translated_at: 2026-09-26T14:55:19Z
  stamped_at: 2026-09-26T18:36:39Z
  reviewed_by: null
---

# Use case — Onboarding by role

Asking a newly arrived *developer* to read the manual's 15 chapters before making the first commit is, in practice, asking them not to read them. Effective onboarding is the opposite: it starts small, with what that role does in the next two weeks, and grows with the work.

The `get_guide_by_role` was designed precisely for this. It receives the *risk level* and the role — `developer`, `appsec-engineer`, `devops-sre`, `qa`, any of the 13 canonical ones — and returns only the practices that the manual assigns to that person, organised by SDLC phase. The agent composes a personalised guide from there: what is expected of this role in each phase — `plan`, `design`, `develop`, `test`, `operate`, … — with *user stories* already linked, ready to become *acceptance criteria*.

The canonical phases are `plan`, `design`, `develop`, `build`, `test`, `deploy`, `operate` and `govern`. The old names still resolve as *aliases* (`requirements`→`plan`, `implement`→`develop`, `governance`→`govern`), but the examples on this page use the canonical form.

## Prior requirements {#pré-requisitos}

- MCP installed, skill loaded.
- Project *risk level* known.
- *Role* of the new member defined (one of the 13 canonical *roles*).

## Flow {#fluxo}

### 1. Discovery — how many assignments exist? {#1-discovery--quantas-atribuições-existem}

Call without `role`/`phase` to see counts:

```json
get_guide_by_role({"risk_level": "L2"})
```

Returns `role_summary{}` + `phase_summary{}` — how many *practice assignments* exist per *role* and per phase.

### 2. Detail — assignments of the target *role* {#2-detalhe--atribuições-do-role-alvo}

```json
get_guide_by_role({"risk_level": "L2", "role": "developer"})
```

**Output:** `assignments[]` (slim) + joined *user stories*.

Each `assignment` has:
- `practice_id`, `chapter_id`, `phase`
- associated *user stories* (text + *acceptance criteria*)

### 3. Detail by *phase* {#3-detalhe-por-fase}

For a "first sprint" guide, filter by the first relevant phase:

```json
get_guide_by_role({"risk_level": "L2", "role": "developer", "phase": "develop"})
```

→ only assignments in the `develop` phase.

### 4. Structure the guide {#4-estruturar-o-guia}

Recommended model:

```markdown
# Onboarding — <Role> @ <Projecto>

> **Risk level:** L2
> **Role:** developer
> **Gerado a partir de:** SbD-ToE MCP v<versão>

## Como o role contribui em cada fase

### Fase: plan
- Practice <ID>: <texto> (cap. <chapterId>)
  - User story: <texto>
  - Acceptance criteria: <texto>

### Fase: design
...

### Fase: develop
...

### Fase: test
...

### Fase: deploy
...

### Fase: operate
...

## Roles com quem mais interages
<inferir do output — ex.: developer interage com appsec em design/test, devops em deploy>

## Próximos passos
- Ler capítulos: <chapters_ids do output, ordenados por número de practice_assignments>
- Setup do ambiente: `setup_sbd_toe_agent(riskLevel="L2", projectRole="<role>")` em cada sessão
- Skill no cliente AI: ver [Skills e agentes](../04-skills-agentes.md)
```

### 5. Customise with the repo {#5-customizar-com-o-repo}

Add:
- Direct link to the repo's artefacts (created via [governance bootstrap](./governance-bootstrap))
- *Pointers* to the project's `CLAUDE.md` / `AGENTS.md`
- Operational *checklist* for the first 30 days

## Output discipline {#disciplina-de-output}

- **Always pass `role` or `phase`** — without either of them, the output is only counts.
- Cite exact `practice_id` and `chapter_id`.
- If `assignments: []` for a `(role, phase)` → write *"Manual-grounded: this role has no direct assignments in this phase"* — do not invent to "fill in".

## Skill / subagent — Claude Code {#skill--subagent--claude-code}

`.claude/agents/sbd-toe-onboarding.md`:

```markdown
---
name: sbd-toe-onboarding
description: Gera guia de onboarding SbD-ToE personalizado por role + risk_level.
tools: Read, Write, mcp__sbd-toe__*
---

# Workflow

1. Perguntar role + risk_level se não explícitos.
2. Chamar get_guide_by_role(risk_level) sem role para ver contagens.
3. Chamar get_guide_by_role(risk_level, role) para detalhe.
4. Estruturar guia por fase (plan → govern).
5. Para cada assignment vazio: marcar "sem atribuições directas — não inventar".
6. Acrescentar pointers ao repo (governance/, CLAUDE.md, AGENTS.md) se existirem.
```

## Useful combinations {#combinatória-útil}

For a *role* that spans many phases (`developer`, `arquitetos-software`), iterate phase by phase to keep the output within the context:

```
get_guide_by_role(L2, "developer", "plan")
get_guide_by_role(L2, "developer", "design")
get_guide_by_role(L2, "developer", "develop")
get_guide_by_role(L2, "developer", "test")
get_guide_by_role(L2, "developer", "operate")
```

Concatenate the outputs into the guide.

## Anti-patterns {#anti-patterns}

- ❌ Calling `get_guide_by_role(L2)` without `role`/`phase` and trying to extract detail — only counts come back.
- ❌ Manual aliasing of roles (e.g.: "engineer" → "developer") instead of letting the server resolve them — use the documented canonical form.
- ❌ Inventing *acceptance criteria* for *user stories* that were not returned.

## Related {#relacionado}

- [Governance bootstrap](./governance-bootstrap) — before onboarding, have the scaffold in place.
- [`get_guide_by_role`](../05-tools-reference.md#get_guide_by_role) in the reference.
