---
id: gestao-excecoes
title: Excepções em IaC
sidebar_position: 9
description: Especificidades da gestão de excepções no contexto de Infraestrutura como Código - policy engines, enforcement e TTL
tags: [excecoes, governacao, iac, controlo, opa, enforcement]
---

# Excepções em IaC

> Processo base, alçadas, campos obrigatórios, cadeia de autoridade e lifecycle estão definidos em **Cap. 14 - `addon/12-processo-excecoes.md`**. Este ficheiro define apenas as especificidades deste domínio.

---

## Âmbito

Excepções a políticas e controlos de segurança aplicados por policy engines (OPA, Sentinel, Rego) sobre módulos, recursos e pipelines IaC - requisitos `IAC-001` a `IAC-013`.

---

## Triggers específicos deste domínio

- ferramenta de validação IaC indisponível com necessidade de deploy documentada como urgente;
- requisito tecnicamente impossível de aplicar ao módulo ou recurso em causa, com justificação de arquitectura;
- desvio intencional em ambiente de staging com controlo compensatório activo;
- módulo legado integrado sem suporte às políticas actuais, com plano de migração.

---

## Campos adicionais obrigatórios (IaC)

| Campo | Obrigatório | Notas |
|---|---|---|
| Ambiente afectado | Sim | `staging` / `production` / `shared` |
| Artefacto IaC afectado | Sim | Nome do módulo, recurso ou pipeline |
| Regra / policy violada | Sim | ID da regra OPA / Sentinel / Rego |

---

## Registo no repositório

**Ficheiro:** directório `exceptions/` no repositório IaC, ou repositório central dedicado com equivalência rastreável.

**Formato:** YAML ou JSON versionado. Formato `.md` apenas para excepções documentais sem integração com policy engine.

```yaml
id: IAC-EXC-003-2025-07-10
requisito: IAC-003
ambiente: staging
artefacto_afetado: pipeline-iac-staging
justificacao: "Deploy urgente para restauro de capacidade após incidente P1"
impacto: "Possível omissão temporária de detecção de má configuração"
mitigacao: "Execução manual de tfsec pós-deploy + revisão AppSec"
aprovado_por: "appsec@org"
validade: "2025-07-20"
```

**Ligação ao código:** comentário estruturado no recurso afectado:

```hcl
# iac-exception: IAC-EXC-003-2025-07-10
```

---

## Integração com policy engines

- Excepções são avaliadas **por regra e por contexto** - não desactivam regras globalmente;
- Policy engines (OPA/Sentinel/Rego) devem ser configurados para interpretar excepções activas como contexto de avaliação;
- Excepções expiradas resultam em **bloqueio automático** do pipeline - a expiração não é silenciosa nem passa para estado permissivo por omissão.

---

## Referências cruzadas

| Documento | Relação |
|---|---|
| `addon/06-controle-enforcement.md` | Tratamento técnico de excepções em policy-as-code |
| `addon/08-matriz-requisitos-iac.md` | Requisitos IAC-001..013 que podem ter excepções |
| Cap. 14 - `addon/12-processo-excecoes.md` | Processo canónico de gestão de excepções |
