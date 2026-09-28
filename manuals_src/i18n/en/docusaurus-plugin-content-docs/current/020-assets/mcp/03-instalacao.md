---
id: instalacao
title: Installation by client
description: Detailed installation instructions for the SbD-ToE MCP in every supported MCP client.
sidebar_label: Installation
sidebar_position: 3
tags:
  - mcp
  - instalacao
  - claude-code
  - cursor
  - copilot
  - windsurf
translation:
  source_locale: pt
  source_path: 020-assets/mcp/03-instalacao.md
  source_sha256: 6e5b8ab1c1145a1de89db9d34210c6f19e6292bd5ba65ccaa51ef888205a65e6
  source_commit: d394b0928bbec912dd0391bedb6cc4f403b46015
  target_sha256: 5eba1b6e4359f1e7ee283b977fdb96e38cc85e95c8f7589fbdda5e4544b9d1aa
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [mcp, practitioner_manual, requirement_runtime, sbdtoe_sbd, verificacao_check, verification_taxonomy]
  glossary_sha256: d97c66b968471198859e01f5c730c1ece105916803784396b352ad7392a492a4
  translated_at: 2026-09-28T09:12:27Z
  stamped_at: 2026-09-28T09:12:27Z
  reviewed_by: null
---

# Installation by client

The `@shiftleftpt/sbd-toe-mcp` server is distributed **exclusively via npm** (plus an alternative GitHub Release bundle) and runs as a `stdio` process — compatible with **any standard MCP client**.

## Prior requirements {#pré-requisitos}

| Requirement | Detail |
|---|---|
| **Node.js** | ≥ 20.9.0 |
| **Access to the npm registry** | Public — no token needed |
| **Disk space** | A few tens of MB (*snapshot* of the Manual, KG and ontology) |
| **Network** | Only on first start (`npx` does the *fetch*) or on *upgrades* |

:::tip Offline / *air-gapped* mode
For environments without npm access, download the bundle from the [GitHub Release](https://github.com/SbD-ToE/sbd-toe-mcp/releases), verify the `.sha256` and reference the extracted `dist/index.js` via `command: "node"` (see the section [GitHub Release Bundle](#github-release-bundle)).
:::

---

## Claude Code (CLI) {#claude-code-cli}

The simplest form — one command, *zero* file editing:

```bash
claude mcp add sbd-toe -- npx -y @shiftleftpt/sbd-toe-mcp
```

To verify:

```bash
claude mcp list
```

To remove:

```bash
claude mcp remove sbd-toe
```

The configuration is stored in `~/.claude.json` (global scope) or in `.mcp.json` (project scope, with `--scope project`).

---

## Claude Desktop (macOS / Windows) {#claude-desktop-macos--windows}

Edit the file `claude_desktop_config.json`:

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

Restart Claude Desktop. The `sbd-toe.*` tools appear in the conversation's tools panel.

---

## Cursor {#cursor}

Edit `~/.cursor/mcp.json` (global) or `.cursor/mcp.json` in the repository (per project):

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

Under **Settings → Features → MCP**, confirm that `sbd-toe` appears as *running* (green badge).

---

## VS Code + GitHub Copilot {#vs-code--github-copilot}

Add `.vscode/mcp.json` to the repository (auto-detected by Copilot Chat in *Agent* mode):

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

Alternatively, global user configuration via *Settings UI* → *Extensions → GitHub Copilot → MCP*.

---

## Windsurf (Codeium) {#windsurf-codeium}

Edit `~/.codeium/windsurf/mcp_config.json`:

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

Edit `~/.config/zed/settings.json`, section `context_servers`:

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

## Other MCP clients {#outros-clientes-mcp}

Any client that supports the `stdio` transport of MCP uses the same pattern: `command: "npx"` + `args: ["-y", "@shiftleftpt/sbd-toe-mcp"]`. The client's documentation gives the location of the configuration file.

---

## GitHub Release Bundle {#github-release-bundle}

For environments without access to `npm` (*air-gapped*, *self-hosted*) or for *pinning* to a specific version:

1. Download the bundle from [github.com/SbD-ToE/sbd-toe-mcp/releases](https://github.com/SbD-ToE/sbd-toe-mcp/releases) — `sbd-toe-mcp-v<versão>-bundle.tar.gz` (or `.zip`) — and its `.sha256`, and verify the *checksum* before extracting.
2. Extract to a known path — `/opt/sbd-toe-mcp/` for example.
3. Reference `dist/index.js` instead of `npx`:

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

## Determining the project's *risk level* {#determinar-o-risk-level-do-projecto}

Without the correct `risk level`, MCP returns a set of controls that is needlessly broad or dangerously narrow. The level is computed with the Ch. 01 method (exposure, data and impact axes, E+D+I). The indicators below are illustrative hints, neither necessary nor sufficient, and the regulatory context is declared separately: a regime does not imply `L3`.

| Indicator (illustrative) | Typically |
|---|---|
| **Internal** application with low impact (even with personal data, if E+D+I ≤ 4) | `L1` |
| **Public APIs** or processing of **user data** | `L2` |
| **Public exposure** with sensitive data and **high impact** | `L3` |

The level decision follows the method of Ch. 01 — no tool takes it on the project's behalf. The tool `map_sbd_toe_applicability` requires `riskLevel` and accepts `technologies`, `hasPersonalData`, `isPublicFacing` and `projectRole`: it does not decide the level, but it shows the effect of each level on the project, which helps compare the alternatives when in doubt.

---

## Final verification {#verificação-final}

Whatever the client, validate with:

```
list_sbd_toe_chapters()
```

It should return **15 chapters** (`00-fundamentos` to `14-governanca-contratacao`). If so — it is operational.

## Next {#a-seguir}

Configure a [skill / agent file](./04-skills-agentes.md) so that the AI client consults the Manual **automatically** instead of requiring the user to ask explicitly.
