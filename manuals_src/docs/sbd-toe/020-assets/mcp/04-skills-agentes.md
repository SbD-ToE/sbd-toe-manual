---
id: skills-agentes
title: Skills e agentes
description: Configurar o cliente AI (Claude, Copilot, Cursor) para consultar o SbD-ToE automaticamente — via skill files, agent files, instruções persistentes.
sidebar_label: Skills e agentes
sidebar_position: 4
tags:
  - mcp
  - skills
  - agentes
  - configuracao
---

# Skills e agentes

Há um efeito subtil no uso diário do MCP: as tools ficam disponíveis assim que o servidor liga, mas o cliente AI não as começa a usar espontaneamente. Falta-lhe o *quando*. Por isso, cada cliente moderno permite injectar instruções persistentes no início da conversa — chamem-lhe *skill*, *agent file*, *rules* ou *system prompt*. É aí que se ensina o cliente a procurar o manual antes de improvisar.

Em vez de te pedir para escreveres essas instruções do zero (e ficarem desactualizadas no dia seguinte), o servidor publica-as via `generate_sbd_toe_skill`. Geras uma vez, guardas no caminho canónico do cliente, e re-geras só depois de um *upgrade* do MCP. Curto, e sempre alinhado com a fonte.

## Mapeamento canónico cliente → ficheiro

| Cliente | Caminho do ficheiro | Escopo |
|---|---|---|
| **Claude Code** | `.claude/skills/sbd-toe.md` | Por projecto |
| **GitHub Copilot (VS Code)** | `.github/copilot-instructions.md` | Por repositório |
| **Cursor** | `.cursorrules` | Por projecto |
| **Windsurf / Codeium** | `.codeium/instructions.md` (ou skill equivalente) | Por projecto |
| **Genérico** | `AGENTS.md` na raiz | Por repositório |

## Gerar a skill

Após instalado o MCP (ver [Instalação](./03-instalacao.md)), executar no cliente:

```
generate_sbd_toe_skill()
```

A tool devolve o conteúdo a guardar — começa com um cabeçalho identificador:

```
<!-- SbD-ToE skill content — source: sbd://toe/agent-guide (@shiftleftpt/sbd-toe-mcp) -->
<!-- Re-run generate_sbd_toe_skill to refresh. -->

# SbD-ToE — Agent Guide
...
```

Guardar **bytewise** no caminho da tabela acima. A skill cobre:

- Identidade (SbD-ToE = Security by Design — Theory of Everything)
- Modos operacionais (CONSULT / GUIDE / SETUP)
- Roteamento por fase do SDLC e por domínio
- Padrões epistémicos (`manual-grounded` / `observed` / `inferred` / `not verified`)
- Vocabulário controlado (*concerns*, *roles*, *risk levels*)
- Mapa dos 15 capítulos

:::tip Refrescar
A skill é uma cópia estática do *agent guide* na altura da geração. Re-correr `generate_sbd_toe_skill()` após cada *upgrade* do MCP para sincronizar.
:::

---

## Inicializar a sessão

Mesmo com a skill carregada, o cliente precisa de saber **risk level + role** do projecto. O *prompt* canónico é:

```
setup_sbd_toe_agent(riskLevel="<L1|L2|L3>", projectRole="<role>")
```

O resultado é o **estado inicial** da sessão:

- Capítulos activos para o `riskLevel`
- Capítulos excluídos / condicionais
- *Domains* activos da ontologia
- Regras específicas do *role* (ex.: para `appsec`, ênfase em capítulos 03/06/10)

Sugestão: cravar este *prompt* como **primeira mensagem** de qualquer sessão em que o tema seja segurança no projecto.

### Roles canónicos

Aceitam *aliases* — o servidor resolve automaticamente.

`developer` · `appsec` · `devops` · `grc` · `qa` · `security_champion` · `software_architect` · `product_owner` · `scrum_master` · `team_lead` · `ciso` · `executive_management` · `ops` · `pentester` · `compliance` · `auditor` · `ir` · `sre`

---

## Padrões por cliente

### Claude Code

Para além do `.claude/skills/sbd-toe.md`, podes criar um *subagent* dedicado:

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

Ver receita completa em [Caso de uso — auditoria de PR](./casos-uso/auditoria-pr).

### GitHub Copilot

`.github/copilot-instructions.md` é carregado automaticamente em *Agent mode*. Adicionar uma secção dedicada após o conteúdo canónico:

```markdown
## Quando aplicar SbD-ToE

Sempre que a tarefa toque em segurança (autenticação, validação, logging,
gestão de segredos, IaC, containers, deploy, monitorização) — começar por
chamar `consult_security_requirements` antes de propor código.
```

### Cursor

`.cursorrules` é único — o conteúdo do MCP cohabita com regras de projecto. Manter um **separador** explícito:

```markdown
# Regras do projecto
... regras existentes ...

# SbD-ToE (security guidance — não anula regras do projecto)
<!-- conteúdo do generate_sbd_toe_skill -->
```

---

## Skill *vs* agent file *vs* prompt directo

Três níveis de integração — escolher consoante a maturidade da equipa:

| Nível | Quando | Como |
|---|---|---|
| **Prompt directo** | Adoção experimental, sessões pontuais | Chamar tools manualmente: "Usa `consult_security_requirements(L2)` antes de propor código." |
| **Skill estática** | Adopção em projecto fixo | Guardar a skill no caminho canónico — auto-carregada |
| **Subagent / persona** | Workflows recorrentes (auditoria de PR, *codegen*, *threat model*) | Subagent dedicado com tools restritas e *prompt* especializado |

A receita completa para cada nível está em [Casos de uso](./casos-uso/) — 6 cenários com exemplos *runnable*.

---

## A seguir

- Consultar a [referência completa de tools](./05-tools-reference.md) para saber o que cada uma faz e como combinar.
- Os [casos de uso](./casos-uso/) mostram fluxos completos (input → tool calls → output → resultado final).
