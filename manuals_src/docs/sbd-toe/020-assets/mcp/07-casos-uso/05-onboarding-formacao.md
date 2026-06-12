---
id: onboarding-formacao
title: Onboarding por role
description: get_guide_by_role para gerar guias de onboarding personalizados — práticas por fase do SDLC + user stories joined.
sidebar_label: Onboarding por role
sidebar_position: 5
tags:
  - mcp
  - casos-uso
  - onboarding
  - training
  - roles
---

# Caso de uso — Onboarding por role

Pedir a um *developer* recém-chegado para ler os 15 capítulos do manual antes de fazer o primeiro commit é, na prática, pedir que não os leia. Onboarding eficaz é o oposto: começa pequeno, no que esse papel faz nas próximas duas semanas, e cresce com o trabalho.

O `get_guide_by_role` foi pensado precisamente para isso. Recebe o *risk level* e o papel — `developer`, `appsec-engineer`, `devops-sre`, `qa`, qualquer um dos 13 canónicos — e devolve apenas as práticas que o manual atribui a essa pessoa, organizadas por fase do SDLC. O agente compõe um guia personalizado a partir daí: o que se espera deste papel em *requirements*, *design*, *implement*, *test*, *operate* — com *user stories* já ligadas, prontas a virar *acceptance criteria*.

## Pré-requisitos

- MCP instalado, skill carregada.
- *Risk level* do projecto conhecido.
- *Role* do novo membro definido (um dos 13 *roles* canónicos).

## Fluxo

### 1. Discovery — quantas atribuições existem?

Chamar sem `role`/`phase` para ver contagens:

```json
get_guide_by_role({"risk_level": "L2"})
```

Devolve `role_summary{}` + `phase_summary{}` — quantas *practice assignments* existem por *role* e por fase.

### 2. Detalhe — atribuições do *role* alvo

```json
get_guide_by_role({"risk_level": "L2", "role": "developer"})
```

**Output:** `assignments[]` (slim) + *user stories* joined.

Cada `assignment` tem:
- `practice_id`, `chapter_id`, `phase`
- *user stories* associadas (texto + *acceptance criteria*)

### 3. Detalhe por *fase*

Para um guia "primeira sprint", filtrar pela primeira fase relevante:

```json
get_guide_by_role({"risk_level": "L2", "role": "developer", "phase": "implement"})
```

→ apenas atribuições da fase `implement`.

### 4. Estruturar o guia

Modelo recomendado:

```markdown
# Onboarding — <Role> @ <Projecto>

> **Risk level:** L2
> **Role:** developer
> **Gerado a partir de:** SbD-ToE MCP v<versão>

## Como o teu role contribui em cada fase

### Fase: requirements
- Practice <ID>: <texto> (cap. <chapterId>)
  - User story: <texto>
  - Acceptance criteria: <texto>

### Fase: design
...

### Fase: implement
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

### 5. Customizar com o repo

Acrescentar:
- Link directo para os artefactos do repo (criados via [governance bootstrap](./governance-bootstrap))
- *Pointers* para `CLAUDE.md` / `AGENTS.md` do projecto
- *Checklist* operacional dos primeiros 30 dias

## Disciplina de output

- **Sempre passar `role` ou `phase`** — sem nenhum dos dois, o output é só contagens.
- Citar `practice_id` e `chapter_id` exactos.
- Se `assignments: []` para um `(role, phase)` → escrever *"Manual-grounded: este role não tem atribuições directas nesta fase"* — não inventar para "preencher".

## Skill / subagent — Claude Code

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
4. Estruturar guia por fase (requirements → operate).
5. Para cada assignment vazio: marcar "sem atribuições directas — não inventar".
6. Acrescentar pointers ao repo (governance/, CLAUDE.md, AGENTS.md) se existirem.
```

## Combinatória útil

Para um *role* que faz muitas fases (`developer`, `arquitetos-software`), iterar fase a fase para manter o output dentro do contexto:

```
get_guide_by_role(L2, "developer", "requirements")
get_guide_by_role(L2, "developer", "design")
get_guide_by_role(L2, "developer", "implement")
get_guide_by_role(L2, "developer", "test")
get_guide_by_role(L2, "developer", "operate")
```

Concatenar os outputs no guia.

## Anti-patterns

- ❌ Chamar `get_guide_by_role(L2)` sem `role`/`phase` e tentar extrair detalhe — só vem contagem.
- ❌ Aliasing manual de roles (ex.: "engineer" → "developer") em vez de deixar o servidor resolver — usar a forma canónica documentada.
- ❌ Inventar *acceptance criteria* para *user stories* não retornadas.

## Relacionado

- [Bootstrap de governança](./governance-bootstrap) — antes do onboarding, ter o scaffold.
- [`get_guide_by_role`](../05-tools-reference.md#get_guide_by_role) na referência.
