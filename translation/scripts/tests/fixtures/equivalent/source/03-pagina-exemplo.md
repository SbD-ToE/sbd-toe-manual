---
id: pagina-exemplo
title: Página de exemplo
sidebar_position: 3
description: Uma página com estrutura variada (CIC-001 a CIC-002).
tags: [exemplo, ci-cd]
---

<!--template: sbdtoe-addon -->

# Página de exemplo

Texto introdutório com **negrito**, referência a `CIC-001`, ao SBOM e ao CI/CD.

## Objectivo {#objectivo}

- Primeiro item
- Segundo item
  - Sub-item aninhado
- Terceiro item

## Tabela de requisitos {#tabela}

| ID | Descrição | Nível |
|:---|-----------|------:|
| CIC-001 | Pipelines como código | L1 |
| CIC-002 | Segredos fora do repositório | L2 |

:::userstory
Como engenheiro, quero SAST no pipeline.
:::

:::note Nota
A tabela acima é ilustrativa.
:::

## Exemplo de configuração {#config}

```yaml
sast:
  enabled: true
```

Ver [o capítulo de CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro) e a [secção da tabela](#tabela).
Ligação externa: [OWASP](https://owasp.org/).

1. Passo um
2. Passo dois

### Sub-secção sem id

Texto final.
