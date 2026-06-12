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

## Pré-requisito

- **Node.js ≥ 20.9.0** ([nodejs.org](https://nodejs.org/))

## Opção 1 — Claude Code (CLI)

```bash
claude mcp add sbd-toe -- npx -y @shiftleftpt/sbd-toe-mcp
```

E pronto. Numa nova sessão do Claude Code, basta perguntar:

> *"Lista os capítulos do manual SbD-ToE."*

A sessão deve arrancar com a tool `list_sbd_toe_chapters` a devolver os 15 capítulos.

## Opção 2 — Cursor / Claude Desktop / Windsurf

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

## Opção 3 — VS Code + GitHub Copilot

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

## Validar a ligação

Para confirmar que a sessão está realmente a falar com o servidor (e não apenas a fingir que sim), basta começar qualquer conversa com:

```
setup_sbd_toe_agent(riskLevel="L2", projectRole="appsec-engineer")
```

A resposta deve enumerar os capítulos activos para esse *risk level* e as regras específicas do papel. Uma lista coerente — capítulos numerados, *concerns*, regras — confirma a ligação. Uma resposta vaga ou sem IDs indica que o cliente provavelmente está a improvisar; vale a pena rever a configuração antes de avançar.

## E a seguir

- Em dúvida sobre que *risk level* aplicar? Ver [Instalação por cliente](./03-instalacao.md) → secção "Determinar *risk level* do projecto".
- Para que o cliente AI consulte o manual **automaticamente** sem ter de pedir: configurar uma [skill / agent file](./04-skills-agentes.md).
- Receitas prontas (auditoria, *codegen*, *threat model*): [Casos de uso](./casos-uso/).
