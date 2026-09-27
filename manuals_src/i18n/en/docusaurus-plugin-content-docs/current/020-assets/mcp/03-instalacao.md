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
  source_sha256: b110ec9914a82bf656d17f4a36c980c33218ded1b3b578e167d74739cf6b8aaf
  source_commit: 5caf1bb9d128df1f7fb0b1e5b2a5603db3e6127f
  target_sha256: b02142fafb13977b4dc8634b744fade2dd6fc65f88c8728ceaffb1f2bc1da65a
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [mcp, practitioner_manual, requirement_runtime, sbdtoe_sbd, verificacao_check, verification_taxonomy]
  glossary_sha256: d97c66b968471198859e01f5c730c1ece105916803784396b352ad7392a492a4
  translated_at: 2026-09-27T08:34:23Z
  stamped_at: 2026-09-27T08:34:23Z
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

Without the correct `risk level`, the MCP returns a set of controls that is unnecessarily broad or dangerously narrow. To decide:

| Indicator | Suggests |
|---|---|
| **Internal** application, no sensitive data, no public APIs exposed | `L1` |
| **Public APIs** or processing of non-sensitive **user data** | `L2` |
| **PII** (GDPR), health, financial, **regulated** system (DORA, NIS2, AI Act — high-risk) | `L3` |

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
