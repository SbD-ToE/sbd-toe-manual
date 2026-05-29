---
id: governance-bootstrap
title: Bootstrap de governança
description: Aplicar plan_sbd_toe_repo_governance num repositório novo — lista de artefactos por capítulo e scaffold automático.
sidebar_label: Governance bootstrap
sidebar_position: 4
tags:
  - mcp
  - casos-uso
  - governance
  - bootstrap
---

# Caso de uso — Bootstrap de governança

Há uma janela curta no início de um repositório novo em que tudo é mais barato: criar pastas, decidir convenções, deixar *placeholders* para artefactos que ainda não existem. Passada essa janela, retrofitar governança custa o triplo. Este caso de uso aproveita-a: o MCP sabe que artefactos o manual identifica para cada capítulo (políticas, templates, registos, *checklists*), e o agente usa essa lista para gerar um *scaffold* coerente em minutos. O conteúdo dos artefactos fica em aberto — preencher é trabalho da equipa — mas o esqueleto deixa visível, desde o primeiro dia, o que falta.

## Pré-requisitos

- MCP instalado.
- *Risk level* alvo conhecido (`L1` é típico no arranque; subir conforme o sistema cresce).

## Fluxo

### 1. Listar artefactos requeridos

```json
plan_sbd_toe_repo_governance()
```

**Output esperado** (forma):

```json
{
  "artifacts": [
    {
      "artifact_id": "ART-01-classificacao-aplicacoes-form",
      "chapter": "01-classificacao-aplicacoes",
      "description": "Formulário de classificação de risco",
      "required_at": "project_init"
    },
    {
      "artifact_id": "ART-02-requisitos-seguranca-catalog",
      "chapter": "02-requisitos-seguranca",
      "description": "Catálogo de requisitos de segurança",
      "required_at": "project_init"
    },
    ...
  ]
}
```

### 2. Filtrar por *risk level* (opcional)

Cruzar com [`sbd://toe/chapter-applicability/L1`](../06-resources-prompts.md#sbdtoechapter-applicabilityrisklevel) — eliminar artefactos de capítulos excluídos para o *risk level*.

### 3. Estruturar o repo

Layout recomendado:

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

### 4. *Scaffold* automático

Para cada `artifact_id`:

```markdown
<!-- governance/<chapter>/<artifact>.md -->

# <título>

> **Artefacto:** `ART-<chapter>-<name>`
> **Capítulo:** [<chapter>](https://www.securitybydesign.dev/sbd-toe/sbd-manual/<chapter>/intro)
> **Estado:** ⏳ pendente

## Propósito
<do `description` do MCP>

## Conteúdo esperado
- ...

## Aprovação
- Owner: <role>
- Reviewers: <roles>
```

### 5. Inicializar a sessão de equipa

Em `AGENTS.md` / `CLAUDE.md`, incluir bloco de inicialização:

```markdown
## SbD-ToE

Este repositório segue o manual Security by Design — Theory of Everything.

- Risk level: L1
- Roles primários: developer, devops, appsec (rotativo)
- Skill: `.claude/skills/sbd-toe.md`
- Em qualquer sessão de design/implementação de segurança, inicializar:
  `setup_sbd_toe_agent(riskLevel="L1", projectRole="<role>")`
```

## Disciplina de output

- O *bootstrap* gera **placeholders** — não preenche os artefactos. Cada artefacto requer trabalho de equipa.
- **Não declarar conformidade** com base na existência de placeholders. Conformidade requer conteúdo preenchido + evidência.
- Documentar o ***risk level* assumido** explicitamente em cada artefacto — se subir, alguns artefactos extra ficam a faltar.

## Skill / subagent — Claude Code

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
3. Filtrar artefactos por chapter applicable ao risk_level (via sbd://toe/chapter-applicability/{riskLevel}).
4. Criar layout governance/<chapter>/<artifact>.md com placeholders.
5. Criar AGENTS.md + CLAUDE.md com bloco de inicialização.
6. Guardar a skill canónica via generate_sbd_toe_skill em .claude/skills/sbd-toe.md.
7. Reportar lista do que ficou criado + lista do que falta preencher.
8. Não inventar conteúdo de artefactos — só scaffold.
```

## Quando re-correr

| Trigger | Acção |
|---|---|
| *Risk level* sobe (L1→L2 ou L2→L3) | Re-correr — adiciona artefactos dos capítulos novos. Não apagar nada. |
| Upgrade do MCP server | Re-correr `generate_sbd_toe_skill()` para refrescar a skill. |
| Adição de cross-check normativo posterior ao *snapshot* do MCP (ex.: AI Act em v1.3.0) | Adicionar manualmente — o MCP `0.9.0` só indexa CRA, DORA, NIS2, GDPR, ENISA/CSA (ver [content lag](../10-troubleshooting-faq.md)). |

## Anti-patterns

- ❌ Preencher os placeholders automaticamente com texto genérico — pior que vazio.
- ❌ Apagar artefactos "que não vão ser usados" — esconde o gap.
- ❌ Marcar artefactos como "concluídos" sem revisão humana.

## Relacionado

- [Onboarding](./onboarding-formacao) — depois do scaffold, treinar a equipa.
- [Skills e agentes](../04-skills-agentes.md) — para configurar persistência.
