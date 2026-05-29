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

A forma mais rápida de saber se o MCP é para ti é experimentá-lo durante um minuto e ver o teu cliente AI a citar o manual com IDs em vez de o parafrasear. Não precisas de clonar nada nem de configurar credenciais — o servidor está publicado no npm e arranca via `npx`.

## Pré-requisito

- **Node.js ≥ 20.9.0** ([nodejs.org](https://nodejs.org/))

## Opção 1 — Claude Code (CLI)

```bash
claude mcp add sbd-toe -- npx -y @shiftleftpt/sbd-toe-mcp
```

E pronto. Numa nova sessão do Claude Code, pergunta:

> *"Lista os capítulos do manual SbD-ToE."*

Deves ver a sessão arrancar com a tool `list_sbd_toe_chapters` a devolver os 15 capítulos.

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

Reinicia o cliente. Tools `sbd-toe.*` ficam disponíveis automaticamente.

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

Para confirmar que a sessão está realmente a falar com o servidor (e não apenas a fingir que sim), começa qualquer conversa com:

```
setup_sbd_toe_agent(riskLevel="L2", projectRole="appsec")
```

A resposta deve enumerar os capítulos activos para esse *risk level* e as regras específicas do papel. Se vires uma lista coerente — capítulos numerados, *concerns*, regras — está ligado. Se vires algo vago ou sem IDs, o cliente provavelmente está a improvisar; vale a pena rever a configuração antes de avançar.

## E a seguir

- Não sabes que *risk level* aplicar? Vê [Instalação por cliente](./03-instalacao.md) → secção "Determinar *risk level* do projecto".
- Queres que o cliente AI consulte o manual **automaticamente** sem ter de pedir? Configura uma [skill / agent file](./04-skills-agentes.md).
- Procuras receitas prontas (auditoria, *codegen*, *threat model*)? [Casos de uso](./casos-uso/).
