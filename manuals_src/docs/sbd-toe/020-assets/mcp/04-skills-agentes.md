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

Há um efeito subtil no uso diário do MCP: as tools ficam disponíveis assim que o servidor liga, mas o cliente AI não as começa a usar espontaneamente. Falta-lhe o *quando*. Por isso, cada cliente moderno permite injectar instruções persistentes no início da conversa — *skill*, *agent file*, *rules* ou *system prompt*, conforme o cliente. É aí que se ensina o cliente a procurar o manual antes de improvisar.

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

Após instalado o MCP (ver [Instalação](./03-instalacao.md)), executar no cliente. A tool tem três formas:

| Chamada | Devolve |
|---|---|
| `generate_sbd_toe_skill()` | o *agent guide* canónico completo (sem especialização de papel) |
| `generate_sbd_toe_skill(role="appsec-engineer", format="skill")` | uma *skill* especializada no *slice* desse papel |
| `generate_sbd_toe_skill(role="devops-sre", format="subagent", flavour="harnessed")` | uma definição de *subagent* instalável |

**Parâmetros:**
- `role` — uma das 13 personas canónicas (aliases resolvem; papel desconhecido → erro com a lista das 13). Sem `role`, devolve o *agent guide*.
- `format` — `skill` (ficheiro de orientação) ou `subagent` (definição de agente, `.claude/agents/…`).
- `flavour` — `harnessed` (embebe as tools `mcp__sbd-toe__*`; consulta o manual ao vivo) ou `skilled` (*slice* congelado, sem tools live, offline).
- `risk_level` (default `L2`), `phase`, `include_detail` — opcionais.

A tool devolve `content` + `suggested_path` + `meta.coverage` (capítulos, *user stories*, *checklist items* — cobertura **declarada**, nada truncado em silêncio). Guardar **bytewise** no `suggested_path` (ou no caminho equivalente da tabela cliente→ficheiro acima). O conteúdo começa com um cabeçalho identificador:

```
---
name: sbd-appsec-engineer
description: SbD-ToE appsec-engineer (L2) — … Queries the SbD-ToE MCP live.
tools: …, mcp__sbd-toe__get_guide_by_role, mcp__sbd-toe__consult_security_requirements, …
---
```

:::tip Refrescar
Uma skill `skilled` (ou o *agent guide* sem `role`) é uma cópia **estática** na altura da geração — re-gerar após cada *upgrade* do MCP. Uma skill/subagent `harnessed` consulta o manual **ao vivo**, por isso reflecte sempre a versão corrente sem re-gerar.
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
- Regras específicas do *role* (ex.: para `appsec-engineer`, ênfase em capítulos 03/06/10)

Sugestão: cravar este *prompt* como **primeira mensagem** de qualquer sessão em que o tema seja segurança no projecto.

### Roles canónicos

Aceitam *aliases* — o servidor resolve automaticamente.

`developer` · `appsec-engineer` · `arquitetos-software` · `devops-sre` · `qa` · `security-champion` · `product-owner` · `scrum-master` · `operacoes` · `grc-compliance` · `gestao-executiva` · `auditores` · `fornecedores-terceiros`

> São os **13 papéis canónicos** do manual ([Papéis e Responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)). O servidor aceita *aliases* comuns (ex.: `appsec`→`appsec-engineer`, `devops`/`sre`→`devops-sre`, `ciso`→`gestao-executiva`, `compliance`→`grc-compliance`) e resolve-os sempre para um destes 13.

---

## Padrões por cliente

### Claude Code

Para além do `.claude/skills/sbd-toe.md`, é possível criar um *subagent* dedicado — gerável directamente com `generate_sbd_toe_skill(role="auditores", format="subagent")`, ou escrito à mão:

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
| **Skill estática** | Adopção em projecto fixo | `generate_sbd_toe_skill(role, format="skill")` → guardar no caminho canónico (auto-carregada) |
| **Subagent / persona** | Workflows recorrentes (auditoria de PR, *codegen*, *threat model*) | `generate_sbd_toe_skill(role, format="subagent", flavour="harnessed")` → `.claude/agents/sbd-<role>.md` |

A receita completa para cada nível está em [Casos de uso](./casos-uso/) — 6 cenários com exemplos *runnable*.

---

## A seguir

- Consultar a [referência completa de tools](./05-tools-reference.md) para saber o que cada uma faz e como combinar.
- Os [casos de uso](./casos-uso/) mostram fluxos completos (input → tool calls → output → resultado final).
