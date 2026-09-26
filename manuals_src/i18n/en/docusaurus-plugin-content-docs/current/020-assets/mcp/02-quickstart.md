---
id: quickstart
title: Quickstart — 60 seconds
description: Connecting the SbD-ToE MCP to Claude Code or Cursor in under a minute.
sidebar_label: Quickstart
sidebar_position: 2
tags:
  - mcp
  - quickstart
translation:
  source_locale: pt
  source_path: 020-assets/mcp/02-quickstart.md
  source_sha256: 25d9240e27cfebae372b40d9770c2e221dce488d96e7bc47f60750171ee8e7ed
  source_commit: 058f86265e07bc86cb7f19162dd2c6b87fbcc0a7
  target_sha256: 35a1bd6c5db22f6bfa05fb45ff3319fe8b802670ef19af17dfb444d8119df7b8
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, mcp, papel_suporte, practitioner_manual, requirement_runtime, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: 6f084d11942de83468adb23339d4ce6bbae1f294f4bef16ba2dc3c157fdf761c
  translated_at: 2026-09-26T16:41:59Z
  stamped_at: 2026-09-26T18:36:34Z
  reviewed_by: null
---

# Quickstart — 60 seconds

The quickest way to evaluate the MCP is to try it for a minute and watch the AI client cite the Manual with IDs instead of paraphrasing it. There is nothing to clone and no credentials to configure — the server is published on npm and starts via `npx`.

## Prior requirement {#pré-requisito}

- **Node.js ≥ 20.9.0** ([nodejs.org](https://nodejs.org/))

## Option 1 — Claude Code (CLI) {#opção-1--claude-code-cli}

```bash
claude mcp add sbd-toe -- npx -y @shiftleftpt/sbd-toe-mcp
```

And that is it. In a new Claude Code session, it is enough to ask:

> *"List the chapters of the SbD-ToE Manual."*

The session should start with the tool `list_sbd_toe_chapters` returning the 15 chapters.

## Option 2 — Cursor / Claude Desktop / Windsurf {#opção-2--cursor--claude-desktop--windsurf}

Add to the client's MCP configuration file:

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

After restarting the client, the `sbd-toe.*` tools become available automatically.

## Option 3 — VS Code + GitHub Copilot {#opção-3--vs-code--github-copilot}

`.vscode/mcp.json` in the repository:

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

## Validating the connection {#validar-a-ligação}

To confirm that the session is really talking to the server (and not merely pretending to), it is enough to ask it for the identity of what it is serving:

```
read_sbd_toe_resource(uri="sbd://toe/version")
```

or, alternatively, `list_sbd_toe_chapters()`. A response with the package name, the version and the *provenance* (Manual, KG, ontology) — or with the chapter index, with real ids — confirms the connection. A vague response or one without ids indicates that the client is probably improvising; the configuration is worth reviewing before moving on.

In clients that expose MCP *prompts*, the *prompt* `setup_sbd_toe_agent(riskLevel, projectRole)` initialises the session: the response describes what each chapter demands at that level (for example, «predominantly mandatory at L2») and the rules of the role — no chapter is excluded. Clients without *prompt* support, such as Claude Desktop, do not expose it; for that reason it cannot serve as the only validation.

## The first real call {#a-primeira-chamada-real}

For a concrete task, the first call is the one the tool descriptions mark as *START HERE*: `select_sbd_toe_requirements`, with what the agent has read **declared** — `risk_level`, `concerns`, `exposure`, `data_sensitivity`, `technologies`, `changed_files`. `exposure: "local"` is valid but inert: declared on its own, it gives `needs_input`. The server does not guess from the task text: without a declaration, it returns `needs_input` with the accepted vocabulary (published in `sbd://toe/activation-vocabulary`). Details in the [tools reference](./05-tools-reference.md).

## What next {#e-a-seguir}

- Unsure which *risk level* to apply? See [Installation by client](./03-instalacao.md) → section "Determining the project's *risk level*".
- For the AI client to consult the Manual **automatically** without having to be asked: configure a [skill / agent file](./04-skills-agentes.md).
- Ready-made recipes (audit, *codegen*, *threat model*): [Use cases](./casos-uso/).
