---
id: rastreabilidade-arquitetural
title: Rastreabilidade Arquitetural
description: Modelo de rastreabilidade entre requisitos ARC, ameaças, decisões arquitecturais e evidência auditável, com template de matriz e critérios de actualização
tags: [tipo:addon, tema:arquitetura, ARC, rastreabilidade, ADR, evidencia, threat-modeling, L1, L2, L3]
sidebar_position: 6
---

<!--template: sbdtoe-addon -->

# Rastreabilidade Arquitetural

A rastreabilidade arquitectural é a capacidade de demonstrar, de forma verificável, que cada requisito de segurança relevante tem uma decisão de design associada, um controlo implementado e evidência auditável.

Sem rastreabilidade, uma arquitectura pode estar correcta mas não ser *demonstravelmente* segura - o que é insuficiente em contextos de auditoria, conformidade ou análise pós-incidente.

---

## Modelo de rastreabilidade

O modelo liga cinco elementos em cadeia:

```
Ameaça (Cap. 03)  →  Requisito ARC-XXX  →  Decisão (ADR)  →  Controlo implementado  →  Evidência
```

| Elemento | Descrição | Artefacto típico |
|----------|-----------|-----------------|
| **Ameaça** | Ameaça identificada no threat modeling (Cap. 03) - STRIDE, PASTA ou equivalente | Registo de TM, DFD anotado |
| **Requisito ARC-XXX** | Requisito canónico do catálogo deste capítulo que mitiga a ameaça | `01-catalogo-requisitos.md` |
| **Decisão (ADR)** | Architecture Decision Record que documenta como o requisito é satisfeito no contexto do projecto | `adr/ADR-xxxx.md`, secção de decisões em `solution-architecture.md` |
| **Controlo implementado** | A medida técnica ou processual em vigor que concretiza a decisão | Configuração de rede, política de admissão, processo de revisão |
| **Evidência** | Artefacto verificável que comprova o controlo - versionado, reproduzível e auditável | Diagrama versionado, log de CI/CD, ata de revisão, checklist preenchido |

---

## Template de matriz de rastreabilidade

A matriz pode ser mantida como tabela Markdown no repositório, backlog items com labels, ou secção na `solution-architecture.md`. O formato é secundário; a substância - ligação verificável entre requisito, decisão e evidência - é o critério determinante.

| Req. ARC | Nome | Ameaça associada (Cap. 03) | Decisão / ADR | Controlo implementado | Evidência | Estado |
|----------|------|---------------------------|---------------|-----------------------|-----------|--------|
| ARC-001 | Zonas de confiança identificadas | Spoofing, Information Disclosure | ADR-003 | Diagrama C4 com trust boundaries delimitados | `docs/arch/trust-zones-v3.drawio` (rev. 2024-11) | Conforme |
| ARC-005 | Threat modeling integrado | Elevation of Privilege, Tampering | ADR-007 | STRIDE aplicado em design session trimestral | `docs/tm/checkout-flow-2024-11.md` | Conforme |
| ARC-006 | Isolamento entre domínios sensíveis | Lateral movement, Info Disclosure | ADR-009 | Network policies Kubernetes + ACLs no API Gateway | CI log: `validate-isolation` (pipeline #247) | Conforme |
| ARC-011 | Segmentação entre ambientes | Tampering cross-env | ADR-012 | Namespaces isolados + credenciais separadas por ambiente | Auditoria IAM 2024-10, network policy review | Conforme |

*Para L1: colunas `Ameaça associada` e `Decisão / ADR` são recomendadas mas não obrigatórias. Para L2 e L3: todos os campos são obrigatórios.*

---

## Critérios de actualização

A matriz de rastreabilidade deve ser actualizada quando:

- um requisito ARC for instanciado ou revisto no projecto;
- um ADR for criado, actualizado ou invalidado;
- ocorrer um evento de revisão arquitectural (ver triggers em [Glossário Operacional](./termos-e-glossario-arquitetura));
- o nível de risco da aplicação for reclassificado;
- uma excepção for aprovada, renovada ou expirada.

Rastreabilidade desactualizada equivale a ausência de rastreabilidade para efeitos de auditoria.

---

## Instanciação operacional

Para instanciação em projecto, cada requisito ARC é identificado com a tag operacional `SEC-Lx-ARC-CODIGO` (ex: `SEC-L2-ARC-005`), conforme descrito em [Taxonomia e Rastreabilidade](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

A tag operacional é o elo entre a matriz de rastreabilidade arquitectural e o backlog ou sistema de gestão de conformidade do projecto.

---

> Para o catálogo de requisitos, consultar [Catálogo de Requisitos ARC](./catalogo-requisitos-arquitetura).
> Para critérios de validação por requisito, consultar [Plano de Validação Arquitetural](./validacao-arquitetural).
> Para o modelo de decisão e evidência, consultar [Decisão e Evidência Arquitetural](./decisao-evidencia-arquitetural).
> Para gestão de excepções à rastreabilidade, consultar [Gestão de Excepções](./excecoes).
