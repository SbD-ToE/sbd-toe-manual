---
id: quickstart
title: Quickstart — 60 segundos
description: Ligar o SbD-ToE MCP ao Claude Code ou Cursor em menos de um minuto.
sidebar_label: Quickstart
sidebar_position: 2
tags:
  - mcp
  - quickstart
---

# Quickstart — 60 segundos

A forma mais rápida de avaliar o MCP é experimentá-lo durante um minuto e ver o cliente AI a citar o manual com IDs em vez de o parafrasear. Não é preciso clonar nada nem configurar credenciais — o servidor está publicado no npm e arranca via `npx`.

## Pré-requisito {#pré-requisito}

- **Node.js ≥ 20.9.0** ([nodejs.org](https://nodejs.org/))

## Opção 1 — Claude Code (CLI) {#opção-1--claude-code-cli}

```bash
claude mcp add sbd-toe -- npx -y @shiftleftpt/sbd-toe-mcp
```

E pronto. Numa nova sessão do Claude Code, basta perguntar:

> *"Lista os capítulos do manual SbD-ToE."*

A sessão deve arrancar com a tool `list_sbd_toe_chapters` a devolver os 15 capítulos.

## Opção 2 — Cursor / Claude Desktop / Windsurf {#opção-2--cursor--claude-desktop--windsurf}

Adicionar ao ficheiro de configuração MCP do cliente:

```json
{
  "mcpServers": {
    "sbd-toe": {
      "command": "npx",
      "args": ["-y", "@shiftleftpt/sbd-toe-mcp"]
    }
  }
}
```

Após reiniciar o cliente, as tools `sbd-toe.*` ficam disponíveis automaticamente.

## Opção 3 — VS Code + GitHub Copilot {#opção-3--vs-code--github-copilot}

`.vscode/mcp.json` no repositório:

```json
{
  "servers": {
    "sbdToe": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@shiftleftpt/sbd-toe-mcp"]
    }
  }
}
```

## Validar a ligação {#validar-a-ligação}

Para confirmar que a sessão está realmente a falar com o servidor (e não apenas a fingir que sim), basta pedir-lhe a identidade do que está a servir:

```
read_sbd_toe_resource(uri="sbd://toe/version")
```

ou, em alternativa, `list_sbd_toe_chapters()`. Uma resposta com o nome do pacote, a versão e a *provenance* (manual, KG, ontologia) — ou com o índice de capítulos, com ids reais — confirma a ligação. Uma resposta vaga ou sem ids indica que o cliente provavelmente está a improvisar; vale a pena rever a configuração antes de avançar.

Em clientes que expõem *prompts* MCP, o *prompt* `setup_sbd_toe_agent(riskLevel, projectRole)` inicializa a sessão: a resposta descreve a exigência de cada capítulo nesse nível (por exemplo, «dominantemente obrigatório em L2») e as regras do papel — nenhum capítulo fica excluído. Clientes sem suporte de *prompts*, como o Claude Desktop, não o expõem; por isso não serve como única validação.

## A primeira chamada real {#a-primeira-chamada-real}

Para uma tarefa concreta, a primeira chamada é a que as descrições das tools marcam como *START HERE*: `select_sbd_toe_requirements`, com aquilo que o agente leu **declarado** — `risk_level`, `concerns`, `exposure`, `data_sensitivity`, `technologies`, `changed_files`. O servidor não adivinha a partir do texto da tarefa: sem declaração, devolve `needs_input` com o vocabulário aceite (publicado em `sbd://toe/activation-vocabulary`). Detalhe na [referência de tools](./05-tools-reference.md).

## E a seguir {#e-a-seguir}

- Em dúvida sobre que *risk level* aplicar? Ver [Instalação por cliente](./03-instalacao.md) → secção "Determinar *risk level* do projecto".
- Para que o cliente AI consulte o manual **automaticamente** sem ter de pedir: configurar uma [skill / agent file](./04-skills-agentes.md).
- Receitas prontas (auditoria, *codegen*, *threat model*): [Casos de uso](./casos-uso/).
