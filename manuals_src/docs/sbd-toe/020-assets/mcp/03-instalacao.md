---
id: instalacao
title: Instalação por cliente
description: Instruções detalhadas de instalação do SbD-ToE MCP em todos os clientes MCP suportados.
sidebar_label: Instalação
sidebar_position: 3
tags:
  - mcp
  - instalacao
  - claude-code
  - cursor
  - copilot
  - windsurf
---

# Instalação por cliente

O servidor `@shiftleftpt/sbd-toe-mcp` é distribuído **exclusivamente via npm** (mais bundle GitHub Release alternativo) e corre como processo `stdio` — compatível com **qualquer cliente MCP padrão**.

## Pré-requisitos {#pré-requisitos}

| Requisito | Detalhe |
|---|---|
| **Node.js** | ≥ 20.9.0 |
| **Acesso ao registo npm** | Pública — sem token necessário |
| **Espaço em disco** | Algumas dezenas de MB (*snapshot* do manual, KG e ontologia) |
| **Rede** | Apenas no primeiro arranque (`npx` faz *fetch*) ou em *upgrades* |

:::tip Modo offline / *air-gapped*
Para ambientes sem acesso npm, descarregar o bundle do [GitHub Release](https://github.com/SbD-ToE/sbd-toe-mcp/releases), verificar o `.sha256` e referir o `dist/index.js` extraído via `command: "node"` (ver secção [GitHub Release Bundle](#github-release-bundle)).
:::

---

## Claude Code (CLI) {#claude-code-cli}

Forma mais simples — um comando, *zero* edição de ficheiros:

```bash
claude mcp add sbd-toe -- npx -y @shiftleftpt/sbd-toe-mcp
```

Para verificar:

```bash
claude mcp list
```

Para remover:

```bash
claude mcp remove sbd-toe
```

A configuração fica guardada em `~/.claude.json` (escopo global) ou em `.mcp.json` (escopo projecto, com `--scope project`).

---

## Claude Desktop (macOS / Windows) {#claude-desktop-macos--windows}

Editar o ficheiro `claude_desktop_config.json`:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

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

Reiniciar o Claude Desktop. As tools `sbd-toe.*` aparecem no painel de ferramentas da conversa.

---

## Cursor {#cursor}

Editar `~/.cursor/mcp.json` (global) ou `.cursor/mcp.json` no repositório (por projecto):

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

Em **Settings → Features → MCP**, confirmar que `sbd-toe` aparece como *running* (badge verde).

---

## VS Code + GitHub Copilot {#vs-code--github-copilot}

Adicionar `.vscode/mcp.json` no repositório (auto-detectado pelo Copilot Chat em modo *Agent*):

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

Em alternativa, configuração global do utilizador via *Settings UI* → *Extensions → GitHub Copilot → MCP*.

---

## Windsurf (Codeium) {#windsurf-codeium}

Editar `~/.codeium/windsurf/mcp_config.json`:

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

---

## Zed {#zed}

Editar `~/.config/zed/settings.json`, secção `context_servers`:

```json
{
  "context_servers": {
    "sbd-toe": {
      "command": {
        "path": "npx",
        "args": ["-y", "@shiftleftpt/sbd-toe-mcp"]
      }
    }
  }
}
```

---

## Outros clientes MCP {#outros-clientes-mcp}

Qualquer cliente que suporte o transporte `stdio` do MCP usa o mesmo padrão: `command: "npx"` + `args: ["-y", "@shiftleftpt/sbd-toe-mcp"]`. Consultar a documentação do cliente para localização do ficheiro de configuração.

---

## GitHub Release Bundle {#github-release-bundle}

Para ambientes sem acesso a `npm` (*air-gapped*, *self-hosted*) ou para *pinning* a uma versão específica:

1. Descarregar o bundle de [github.com/SbD-ToE/sbd-toe-mcp/releases](https://github.com/SbD-ToE/sbd-toe-mcp/releases) — `sbd-toe-mcp-v<versão>-bundle.tar.gz` (ou `.zip`) — e o respetivo `.sha256`, e verificar o *checksum* antes de extrair.
2. Extrair para um caminho conhecido — `/opt/sbd-toe-mcp/` por exemplo.
3. Referir o `dist/index.js` em vez de `npx`:

```json
{
  "mcpServers": {
    "sbd-toe": {
      "command": "node",
      "args": ["/opt/sbd-toe-mcp/dist/index.js"]
    }
  }
}
```

---

## Determinar o *risk level* do projecto {#determinar-o-risk-level-do-projecto}

Sem `risk level` correcto, o MCP devolve um conjunto de controlos desnecessariamente amplo ou perigosamente reduzido. O nível calcula-se pelo método do cap. 01 (eixos exposição, dados e impacto, E+D+I). Os indicadores abaixo são pistas ilustrativas, nem necessárias nem suficientes, e o contexto regulatório declara-se à parte: um regime não implica `L3`.

| Indicador (ilustrativo) | Tipicamente |
|---|---|
| Aplicação **interna** de impacto baixo (mesmo com dados pessoais, se E+D+I ≤ 4) | `L1` |
| **APIs públicas** ou tratamento de **dados de utilizador** | `L2` |
| **Exposição pública** com dados sensíveis e **impacto elevado** | `L3` |

A decisão do nível segue o método do cap. 01 — nenhuma tool a toma pelo projeto. A tool `map_sbd_toe_applicability` exige `riskLevel` e aceita `technologies`, `hasPersonalData`, `isPublicFacing` e `projectRole`: não decide o nível, mas mostra o efeito de cada nível no projeto, o que ajuda a comparar as alternativas quando há dúvida.

---

## Verificação final {#verificação-final}

Independentemente do cliente, validar com:

```
list_sbd_toe_chapters()
```

Deve devolver **15 capítulos** (`00-fundamentos` a `14-governanca-contratacao`). Se sim — está operacional.

## A seguir {#a-seguir}

Configurar uma [skill / agent file](./04-skills-agentes.md) para que o cliente AI consulte o manual **automaticamente** em vez de exigir que o utilizador peça explicitamente.
