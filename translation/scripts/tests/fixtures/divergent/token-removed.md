---
id: pagina-exemplo
title: Example page
sidebar_position: 3
description: A page with varied structure (CIC-001 to CIC-002).
tags: [exemplo, ci-cd]
translation:
  source_locale: pt
  source_path: 03-pagina-exemplo.md
  source_sha256: 0000000000000000000000000000000000000000000000000000000000000000
  source_commit: 0000000
  target_sha256: 0000000000000000000000000000000000000000000000000000000000000000
  engine: fixture
  prompt_sha256: 0000000000000000000000000000000000000000000000000000000000000000
  terms_sha256: null
  translated_at: 2026-09-25T00:00:00Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Example page

Introductory text with **bold**, a reference to the first requirement, to the SBOM and to CI/CD.

## Objective {#objectivo}

- First item
- Second item
  - Nested sub-item
- Third item

## Requirements table {#tabela}

| ID | Description | Level |
|:---|-------------|------:|
| CIC-001 | Pipelines as code | L1 |
| CIC-002 | Secrets kept out of the repository | L2 |

:::userstory
As an engineer, I want SAST in the pipeline.
:::

:::note Note
The table above is illustrative.
:::

## Configuration example {#config}

```yaml
sast:
  enabled: true
```

See [the CI/CD chapter](/sbd-toe/sbd-manual/cicd-seguro/intro) and the [table section](#tabela).
External link: [OWASP](https://owasp.org/).

1. Step one
2. Step two

### Sub-section without id

Closing text.
