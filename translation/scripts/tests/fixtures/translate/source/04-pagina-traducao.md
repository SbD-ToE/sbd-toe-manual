---
id: pagina-traducao
title: Página de tradução com cobertura
sidebar_position: 4
description: Fixture para o translate.py — fatia ACO-TSV, requisito CIC-003.
tags: [fixture, traducao]
---

<!--template: sbdtoe-addon -->

# Página de tradução {#pagina-traducao}

Esta página exercita a **fatia** `ACO-TSV` do AppSec Core e o requisito `CIC-003` do SBOM.  
A segunda linha continua o parágrafo depois de uma quebra dura.

## Objectivo {#objectivo}

- Primeiro item com a fatia
- Segundo item
  - Sub-item aninhado com [ligação interna](./outra-pagina#seccao)
- Terceiro item sobre cobertura normativa

## Tabela {#tabela}

| ID | Descrição | Nível |
|:---|-----------|------:|
| CIC-003 | Inventário de componentes | L1 |
| CIC-004 | Cobertura de dependências | L2 |

:::userstory Como engenheiro
Como engenheiro, quero a fatia validada no pipeline.
:::

:::note
Nota sem título.
:::

```yaml
fatia: ACO-TSV
```

Ver a [secção da tabela](#tabela) e o [capítulo de CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro).

1. Passo um
2. Passo dois com cobertura

### Sub-secção sem id

Texto final em https://example.org/x.
