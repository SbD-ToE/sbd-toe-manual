---
id: taxonomia-rastreabilidade
title: Taxonomia de Rastreabilidade de Requisitos
description: Dois sistemas de identificação complementares — o catálogo canónico SbD-ToE e as tags operacionais de projecto — e como articulá-los ao longo do ciclo de vida.
tags: [taxonomia, rastreabilidade, requisitos, domínios, ALM]
---

# 🏷️ Taxonomia e Rastreabilidade de Requisitos de Segurança

O SbD-ToE opera com **dois sistemas de identificação complementares**, cada um com propósito distinto. Compreender a diferença e a relação entre ambos é condição para implementar rastreabilidade efectiva — sem ela, o catálogo de requisitos fica desligado do trabalho real de desenvolvimento.

---

## 1) Dois sistemas, dois propósitos

### ID canónico (catálogo SbD-ToE)

O catálogo de requisitos do Cap. 02 atribui a cada requisito um **identificador canónico estável**:

```
CATEGORIA-NNN
```

| Componente | Descrição | Exemplo |
|------------|-----------|---------|
| `CATEGORIA` | 2–3 letras maiúsculas, identifica o domínio de segurança | `AUT`, `LOG`, `VAL` |
| `NNN` | Número sequencial de 3 dígitos | `001`, `003`, `012` |

**Exemplos:** `AUT-001` (MFA obrigatório), `LOG-003` (protecção de integridade de logs), `VAL-002` (validação de parâmetros de entrada)

Este ID é a **referência normativa permanente** — identifica o requisito no manual, nos cross-checks regulatórios, nas matrizes de controlo e em documentação de arquitectura. É independente de qualquer projecto específico.

---

### Tag operacional (instanciação por projecto)

Quando um requisito canónico é adoptado por um projecto concreto, é **instanciado** com o contexto desse projecto — nomeadamente o nível de risco — originando uma tag operacional rastreável:

```
SEC-Lx-DOMINIO-CODIGO
```

| Componente | Descrição | Exemplo |
|------------|-----------|---------|
| `SEC` | Prefixo fixo — indica requisito de segurança | `SEC` |
| `Lx` | Nível de risco da aplicação (L1, L2 ou L3) | `L2` |
| `DOMINIO` | Domínio técnico, alinhado com o catálogo | `AUT`, `LOG` |
| `CODIGO` | Código semântico abreviado do requisito | `MFA`, `BRUTE` |

**Exemplo completo:** `SEC-L2-AUT-MFA`

Esta tag é o identificador usado nos artefactos de ciclo de vida do projecto — backlog, código, testes, pipeline, evidência de auditoria.

---

## 2) A relação entre os dois sistemas

O ID canónico é a **fonte**; a tag operacional é a **instância contextualizada**. O fluxo é sempre descendente:

```
Catálogo SbD-ToE          Projecto concreto
─────────────────          ────────────────────────────────
AUT-001                →   SEC-L2-AUT-MFA   (aplicação pública, risco L2)
AUT-001                →   SEC-L1-AUT-MFA   (ferramenta interna, risco L1)
LOG-003                →   SEC-L2-LOG-INTEG
VAL-002                →   SEC-L3-VAL-SQLI  (app com dados regulados, risco L3)
```

O mesmo requisito canónico pode originar tags distintas em projectos diferentes, reflectindo contextos de risco diferentes. Isto é intencional: **a proporcionalidade é uma propriedade do projecto, não do requisito**.

---

## 3) Domínios técnicos suportados

| Domínio | Categoria canónica associada |
|---------|------------------------------|
| `AUT` | Autenticação e gestão de identidade |
| `ACC` | Controlo de acesso e autorização |
| `LOG` | Registo, auditoria e monitorização |
| `SES` | Sessões e gestão de estado |
| `VAL` | Validação e sanitização de dados |
| `ERR` | Gestão de erros e mensagens |
| `CFG` | Configuração segura e gestão de parâmetros |
| `API` | Segurança de APIs e serviços externos |
| `INT` | Integrações e trocas de mensagens |
| `REQ` | Definição e gestão de requisitos |
| `DST` | Distribuição de artefactos |
| `IDE` | Ferramentas e ambientes de desenvolvimento |
| `ENC` | Dados sensíveis e criptografia |

---

## 4) Onde aplicar cada sistema

| Contexto | Sistema a usar | Exemplo |
|----------|---------------|---------|
| Manual SbD-ToE, cross-checks normativos, arquitectura | ID canónico | `LOG-003` |
| Backlog (stories, épicos, tasks) | Tag operacional | `SEC-L2-LOG-INTEG` |
| Comentários no código-fonte | Tag operacional | `// SEC-L3-VAL-SQLI` |
| Gates de CI/CD e validações automáticas | Tag operacional | `SEC-L2-AUT-MFA` |
| Casos de teste e critérios de aceitação | Tag operacional + referência ao ID canónico | `SEC-L2-AUT-MFA` → `AUT-001` |
| Relatórios de auditoria e evidência | Ambos — rastreabilidade completa | `AUT-001` / `SEC-L2-AUT-MFA` |

A presença do ID canónico em relatórios e evidências é o que permite ligar o trabalho do projecto ao catálogo normativo — e, por extensão, a frameworks externos como ASVS, NIST ou requisitos regulatórios.

---

## 5) Verificação e manutenção

As tags operacionais devem ser **validadas periodicamente** contra:
- O [catálogo canónico](./catalogo-requisitos) — para garantir que os IDs referenciados existem e estão actualizados;
- A [matriz de controlos por risco](./matriz-controlos-por-risco) — para confirmar que o nível `Lx` da tag é coerente com a classificação actual da aplicação.

A organização deve manter um registo com:
- Requisitos adoptados e respectivos IDs canónicos;
- Tags operacionais activas por projecto/aplicação;
- Validações executadas e evidência gerada;
- [Excepções documentadas](./gestao-excecoes).

---

> 📌 A distinção entre ID canónico e tag operacional não é apenas formal — é o mecanismo que permite **governança centralizada do catálogo** com **implementação descentralizada, rastreável e auditável** em cada projecto.
