---
id: governance-bootstrap
title: Governance bootstrap
description: Applying plan_sbd_toe_repo_governance to a new repository — list of artefacts by chapter and automatic scaffold.
sidebar_label: Governance bootstrap
sidebar_position: 4
tags:
  - mcp
  - casos-uso
  - governance
  - bootstrap
translation:
  source_locale: pt
  source_path: 020-assets/mcp/07-casos-uso/04-governance-bootstrap.md
  source_sha256: d79cfdfbcd47e6a5053517ad83aca5b399d40ab89105c2d363cc74cfda60d654
  source_commit: 058f86265e07bc86cb7f19162dd2c6b87fbcc0a7
  target_sha256: d181f9de4653f142c9a85c2bced858dfe1d75521971969642ea8e92323c12740
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 211df96a27d713b5934d7534d61f1972d877902236e63b858563d206c67ccaa8
  glossary_keys: [chapter_role, discipline, mcp, normative_empirical, practitioner_manual]
  glossary_sha256: 40b3a2ba6b88de2bfe0818246a8a78744644cb88e7a08299991ac065e54ccfc0
  translated_at: 2026-09-26T16:42:04Z
  reviewed_by: null
---

# Use case — Governance bootstrap

There is a short window at the start of a new repository in which everything is cheaper: creating folders, deciding conventions, leaving *placeholders* for artefacts that do not yet exist. Once that window has passed, retrofitting governance costs three times as much. This use case makes the most of it: the MCP knows which artefacts the manual identifies for each chapter (policies, templates, registers, *checklists*), and the agent uses that list to generate a coherent *scaffold* in minutes. The content of the artefacts is left open — filling it in is the team's work — but the skeleton makes visible, from day one, what is missing.

## Prior requirements {#pré-requisitos}

- MCP installed.
- Target *risk level* known (`L1` is typical at the outset; raise it as the system grows).

## Flow {#fluxo}

### 1. List the required artefacts {#1-listar-artefactos-requeridos}

```
plan_sbd_toe_repo_governance(riskLevel, offset, limit)
```

**Expected output** (fields): `byChapter[]` (the artefacts grouped by chapter, each one `{artefactId, chapterId, riskLevels[]}`), `totalArtefacts` (the number of chapter↔artefact rows), `artefact_totals` (`distinct_count`, the distinct artefacts, and `chapter_relation_count`, the rows — rows are never added up to count artefacts), `coverage` and `risk_level_effect`. Artefact ids have the form `ART-<slug>-<hash>`. The chapter↔artefact relation is a projection: it does not say who owns the artefact nor oblige anyone to produce it. The response is paginated (`offset` / `limit`): go through every page before treating the list as complete.

### 2. Pass the *risk level* {#2-filtrar-por-risk-level-opcional}

Pass `riskLevel` to `plan_sbd_toe_repo_governance`: the response declares the effect of the level in `risk_level_effect`. There are no artefacts to eliminate by level — no chapter is excluded; this is graded applicability, and what changes is the stringency (see [`sbd://toe/chapter-applicability/{riskLevel}`](../06-resources-prompts.md#sbdtoechapter-applicabilityrisklevel)).

### 3. Structure the repo {#3-estruturar-o-repo}

Recommended layout:

```
repo-root/
├── governance/
│   ├── 01-classificacao-aplicacoes/
│   │   ├── README.md                      # Refere ART-* + capítulo
│   │   └── classificacao.md                # Artefacto preenchido
│   ├── 02-requisitos-seguranca/
│   │   └── catalogo.md
│   ├── ...
├── policies/                              # (opcional) cópias adaptadas das policies do manual
├── AGENTS.md                              # Aponta ao SbD-ToE como guia
├── CLAUDE.md                              # Idem para Claude Code
└── .claude/skills/sbd-toe.md              # Skill canónica (de generate_sbd_toe_skill)
```

### 4. Automatic *scaffold* {#4-scaffold-automático}

For each artefact returned:

```markdown
<!-- governance/<chapter>/<artifact>.md -->

# <título>

> **Artefacto:** `ART-<slug>-<hash>`
> **Capítulo:** [<chapter>](https://www.securitybydesign.dev/sbd-toe/sbd-manual/<chapter>/intro)
> **Estado:** ⏳ pendente

## Propósito
<do que o MCP devolve para o artefacto>

## Conteúdo esperado
- ...

## Aprovação
- Owner: <role>
- Reviewers: <roles>
```

### 5. Initialise the team session {#5-inicializar-a-sessão-de-equipa}

In `AGENTS.md` / `CLAUDE.md`, include an initialisation block:

```markdown
## SbD-ToE

Este repositório segue o manual Security by Design — Theory of Everything.

- Risk level: L1
- Roles primários: developer, devops, appsec (rotativo)
- Skill: `.claude/skills/sbd-toe.md`
- Em qualquer sessão de design/implementação de segurança, inicializar:
  `setup_sbd_toe_agent(riskLevel="L1", projectRole="<role>")`
```

## Output discipline {#disciplina-de-output}

- The *bootstrap* generates **placeholders** — it does not fill in the artefacts. Each artefact requires team work.
- **Do not declare compliance** on the basis of the existence of placeholders. Compliance requires filled-in content + evidence.
- Document the **assumed *risk level*** explicitly in each artefact. Moving up from L1 to L2, chapter 03 starts listing its artefacts, and the per-chapter list grows, but no new artefacts appear. `risk_level_effect` declares that the level filters little, by design.

## Skill / subagent — Claude Code {#skill--subagent--claude-code}

`.claude/agents/sbd-toe-bootstrap.md`:

```markdown
---
name: sbd-toe-bootstrap
description: Bootstrap inicial de governança SbD-ToE num repo novo — gera scaffold de artefactos por capítulo.
tools: Read, Write, Edit, Bash, mcp__sbd-toe__*
---

# Workflow

1. Perguntar risk_level alvo se não estiver explícito.
2. Chamar plan_sbd_toe_repo_governance.
3. Passar riskLevel a plan_sbd_toe_repo_governance e ler risk_level_effect (nenhum capítulo é excluído; paginar até ao fim).
4. Criar layout governance/<chapter>/<artifact>.md com placeholders.
5. Criar AGENTS.md + CLAUDE.md com bloco de inicialização.
6. Guardar a skill canónica via generate_sbd_toe_skill em .claude/skills/sbd-toe.md.
7. Reportar lista do que ficou criado + lista do que falta preencher.
8. Não inventar conteúdo de artefactos — só scaffold.
```

## When to re-run {#quando-re-correr}

| Trigger | Action |
|---|---|
| *Risk level* rises (L1→L2 or L2→L3) | Re-run — the stringency changes; delete nothing. |
| Upgrade of the MCP server | Re-run `generate_sbd_toe_skill()` to refresh the skill. |
| Addition of a normative cross-check later than the MCP *snapshot* | Add it manually from the web manual until the next publication — confirm coverage in `sbd://toe/version` (see [content lag](../10-troubleshooting-faq.md#content-lag)). |

## Anti-patterns {#anti-patterns}

- ❌ Filling in the placeholders automatically with generic text — worse than empty.
- ❌ Deleting artefacts "that will not be used" — it hides the gap.
- ❌ Marking artefacts as "completed" without human review.

## Related {#relacionado}

- [Onboarding](./onboarding-formacao) — after the scaffold, train the team.
- [Skills and agents](../04-skills-agentes.md) — to configure persistence.
