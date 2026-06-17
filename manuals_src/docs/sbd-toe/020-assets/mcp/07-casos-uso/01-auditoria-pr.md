---
id: auditoria-pr
title: Auditoria de PR
description: Review automatizada de Pull Requests contra os controlos activos do risk_level — findings citáveis por CTRL-*.
sidebar_label: Auditoria de PR
sidebar_position: 1
tags:
  - mcp
  - casos-uso
  - review
  - audit
---

# Caso de uso — Auditoria de PR

Considere-se um PR aberto a meio da tarde de sexta. Toca autenticação, logging e um ficheiro de configuração — exactamente o tipo de mistura que o reviewer humano tem dificuldade em rever em profundidade quando há outras seis revisões na fila. O objectivo deste caso de uso é dar ao agente uma rotina disciplinada para essa revisão: que examine o diff *contra os controlos activos do projecto*, devolva *findings* com `CTRL-*` reais do manual, e nunca declare conformidade só por o código existir.

## Pré-requisitos

- MCP instalado (ver [Instalação](../03-instalacao.md))
- Skill canónica em `.claude/skills/sbd-toe.md` (ver [Skills](../04-skills-agentes.md))
- *Risk level* do projecto conhecido — assumir `L2` no exemplo

## Fluxo

### 1. Identificar o escopo do PR

```
git diff --name-only origin/main...HEAD
```

→ ex.: `src/auth/login.ts`, `src/middleware/audit.ts`, `config/prod.yaml`

### 2. Mapear ficheiros → capítulos

```
map_sbd_toe_review_scope({"changed_files": [
  "src/auth/login.ts",
  "src/middleware/audit.ts",
  "config/prod.yaml"
]})
```

**Output esperado** (forma):
```json
{
  "bundles": [
    {"chapter": "06-desenvolvimento-seguro", "reason": "..."},
    {"chapter": "12-monitorizacao-operacoes", "reason": "..."},
    {"chapter": "08-iac-infraestrutura", "reason": "..."}
  ]
}
```

### 3. Listar controlos activos por *concern*

```
consult_security_requirements({"risk_level": "L2", "concerns": ["auth", "logging", "config"]})
```

Devolve `controls[]` filtrados — usar **apenas estes IDs** no relatório.

### 4. Cruzar diff ↔ controlos

Para cada *hunk* relevante, identificar:

- **`CTRL-*` cobertos** — explicitamente endereçados pelo código
- **`CTRL-*` em risco** — não-cobertos, mas no escopo
- **`CTRL-*` neutros** — não aplicáveis a este *hunk*

### 5. Gerar relatório

Estrutura obrigatória:

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

## Disciplina de output

- **Citar `CTRL-*` exactos**, nunca aproximações textuais.
- Marcar cada *finding* como `manual-grounded` ou `inferred` — nunca `verified` sem leitura humana.
- Para *controlos ausentes do `controls[]`* devolvido, escrever: *"Sem cobertura normativa neste escopo — flag para human review."*
- **Não declarar conformidade regulatória** com base em código.

## Skill / subagent — Claude Code

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

## Anti-patterns

- ❌ Inventar `CTRL-00-99` porque o controlo "encaixa".
- ❌ "PR compliant with NIS2" baseado só em código.
- ❌ Misturar `CTRL-*` de capítulos não devolvidos por `map_sbd_toe_review_scope`.
- ❌ Saltar `consult_security_requirements` e ir directo a `search_sbd_toe_manual` (perde-se o filtro estrutural).

## Relacionado

- [Codegen grounded](./codegen-grounded) — o reverso: gerar código já cumprindo controlos.
- [`map_sbd_toe_review_scope`](../05-tools-reference.md) na referência.
