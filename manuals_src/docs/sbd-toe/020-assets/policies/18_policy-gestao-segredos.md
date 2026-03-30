---
id: policy-gestao-segredos
title: Política de Gestão de Segredos
description: Política organizacional que define os requisitos para o armazenamento, injeção, rotação, auditoria e revogação de segredos (chaves, tokens, credenciais, certificados) em aplicações, pipelines CI/CD, containers e infraestrutura, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, segredos, secrets, vault, OIDC, rotação, pipeline, container, infraestrutura, cap07, cap09, cap11, L1, L2, L3, governance, credenciais]
grupo: pipeline-entrega
sidebar_position: 18
---

# Política de Gestão de Segredos

## 1. Objetivo

Esta política define os requisitos para a **gestão do ciclo de vida completo de segredos** - chaves de API, tokens de acesso, passwords, certificados, credenciais de base de dados e quaisquer outros valores que, se expostos, permitam acesso não autorizado a sistemas, dados ou infraestrutura.

Segredos são um dos vectores de comprometimento mais frequentes e impactantes: expostos em repositórios, logs, imagens de container ou pipelines, persistem muitas vezes durante meses sem serem rotacionados, transformando uma exposição temporária num risco permanente. A gestão eficaz de segredos não é apenas uma prática de higiene técnica - é um controlo de segurança fundamental cuja falha pode comprometer toda a postura de segurança da organização.

O objetivo desta política é garantir que:

- Nenhum segredo é armazenado em repositórios de código, logs, imagens ou artefactos de build
- Segredos são geridos centralmente em cofres de segredos com acesso controlado e auditado
- Segredos em pipelines são injetados de forma efémera, preferencialmente via OIDC/workload identity
- A rotação é automatizada ou agendada com TTL definidos por tipo e nível de criticidade
- A revogação em caso de exposição é imediata e verificável

---

## 2. Âmbito

Esta política cobre todos os segredos usados no contexto de desenvolvimento, pipeline, runtime e infraestrutura, independentemente do tipo:

- Credenciais de acesso a bases de dados, caches, filas e sistemas de mensagens
- Chaves de API de serviços externos
- Tokens de acesso a sistemas de cloud, registos de imagens, repositórios de artefactos
- Tokens de CI/CD (tokens de pipeline, deploy keys)
- Certificados TLS/mTLS e chaves privadas associadas
- Chaves de encriptação de dados em repouso ou em trânsito
- Passwords de contas de serviço

---

## 3. Proibições absolutas

As seguintes práticas são **proibidas** independentemente do nível de criticidade ou contexto:

| Prática proibida | Justificação |
|---|---|
| Hardcoding de segredos no código fonte | Propagação em histórico de versões; impossibilidade de rotação sem alteração de código |
| Segredos em ficheiros de configuração versionados (ex: `.env` commitado, `application.yml` com passwords) | Exposição a todos com acesso de leitura ao repositório |
| Segredos em variáveis de ambiente não mascaradas em logs de pipeline | Exposição em logs, frequentemente armazenados sem controlo de acesso adequado |
| Segredos embebidos em imagens de container | Impossibilidade de rotação sem rebuild; exposição em camadas da imagem |
| Segredos em artefactos de build (JARs, wheels, binários) | Distribuição incontrolada do segredo com o artefacto |
| Uso de "segredos globais" partilhados entre múltiplos pipelines ou ambientes | Violação do princípio de mínimo privilégio; comprometimento de um pipeline compromete todos |
| Segredos de produção acessíveis em ambientes de desenvolvimento | Exposição desnecessária; risco de fuga via ambiente menos controlado |

:::warning
A deteção de segredos hardcoded em código ou configuração deve ser automatizada no pipeline (secret detection). Qualquer finding bloqueia o merge em L2/L3, independentemente da severidade dos restantes gates.
:::

---

## 4. Armazenamento centralizado

Todos os segredos devem ser armazenados em cofre de segredos centralizado, com acesso controlado e auditado:

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Cofre de segredos centralizado em uso | Recomendado | Obrigatório | Obrigatório |
| Acesso ao cofre controlado por RBAC com mínimo privilégio | Recomendado | Obrigatório | Obrigatório |
| Acesso ao cofre auditado e log retido | Recomendado | Obrigatório | Obrigatório |
| Segredos de produção segregados dos restantes ambientes | Recomendado | Obrigatório | Obrigatório |
| Cofre com alta disponibilidade e backup | Recomendado | Obrigatório | Obrigatório |

Ferramentas de referência: HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager.

---

## 5. Injeção em runtime

Segredos devem ser injetados nas aplicações e pipelines exclusivamente em tempo de execução - nunca persistidos no sistema de ficheiros ou em variáveis de ambiente de forma permanente:

### 5.1 Aplicações

- [ ] Segredos injetados via variável de ambiente em runtime (não em tempo de build)
- [ ] Variáveis de ambiente com segredos não expostas em endpoints de diagnóstico ou health checks
- [ ] Alternativa preferida em L2/L3: acesso direto ao cofre via SDK em runtime, com identidade do workload

### 5.2 Pipelines CI/CD

- [ ] Segredos referenciados via mecanismo nativo do sistema de CI (`secrets.*`, `CI/CD Variables masked`, `Variable Groups`)
- [ ] Output de comandos que acedam a segredos mascarado nos logs
- [ ] Credenciais de cloud via OIDC/workload identity (token efémero, TTL ≤ 1h) - elimina chaves estáticas de longa duração

### 5.3 Containers

- [ ] Segredos montados como volumes de segredo do orquestrador (ex: Kubernetes Secrets, com encriptação em repouso)
- [ ] Alternativa preferida em L3: acesso via cofre com workload identity (ex: Vault Agent, AWS IRSA, GCP Workload Identity)
- [ ] Segredos nunca passados como ARG de Docker durante o build

---

## 6. TTL, rotação e revogação

### 6.1 TTL por tipo de segredo

| Tipo de segredo | TTL máximo recomendado | L3 (TTL máximo obrigatório) |
|---|---|---|
| Tokens de pipeline (OIDC efémeros) | ≤ 1 hora | ≤ 1 hora |
| Tokens de acesso a APIs (short-lived) | ≤ 24 horas | ≤ 8 horas |
| Credenciais de base de dados (rotação automática) | 30 dias | 15 dias |
| Chaves de API de serviços externos | 90 dias | 30 dias |
| Certificados TLS (aplicação) | 1 ano | 90 dias |
| Chaves de encriptação de dados | 1 ano (com rotação de envelope) | 90 dias |

### 6.2 Rotação

- [ ] Rotação automatizada sempre que o sistema de emissão o suporte (ex: Vault dynamic secrets, AWS IAM roles, OIDC)
- [ ] Rotação manual agendada para segredos sem suporte a rotação automática, com alertas antes da expiração
- [ ] Rotação verificável sem alteração de código ou rebuild de imagens
- [ ] Histórico de rotações auditável

### 6.3 Revogação por exposição suspeita

Em caso de suspeita ou confirmação de exposição de um segredo:

1. Revogar o segredo imediatamente (não aguardar o TTL)
2. Emitir novo segredo e distribuir para os sistemas que dele dependem
3. Rever os logs de acesso do cofre para avaliar uso indevido do período de exposição
4. Registar o incidente e notificar conforme Política de Rastreabilidade e processo de IRP

---

## 7. Segredos de terceiros e integrações

Segredos recebidos de terceiros (ex: chaves de API de fornecedores) devem ser:

- [ ] Armazenados no cofre centralizado, não em ficheiros partilhados ou sistemas de ticketing
- [ ] Com âmbito e permissões mínimas negociadas com o fornecedor
- [ ] Com prazo de validade conhecido e alerta de renovação
- [ ] Revogados imediatamente quando a integração é terminada

---

## 8. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer | Nunca hardcodar segredos; usar mecanismos de injeção aprovados; reportar segredos acidentalmente expostos |
| DevOps / SRE | Gerir cofre de segredos; configurar rotação; implementar OIDC/workload identity; monitorizar acessos |
| AppSec Engineer | Definir TTLs e política de rotação; configurar secret detection no pipeline; auditar acessos ao cofre |
| Tech Lead | Garantir que a equipa conhece e segue esta política; não aprovar PRs com segredos hardcoded |
| GRC / Compliance | Auditar conformidade; verificar que segredos de produção estão segregados; verificar logs de acesso |

---

## 9. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente com origem em segredo exposto ou não rotacionado
- Adoção de novo cofre de segredos ou plataforma de cloud
- Alteração de fornecedor com impacto em chaves de integração

---

## 10. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 07 - CI/CD Seguro | Gestão e injeção de segredos em pipeline |
| SbD-ToE Cap. 09 - Containers e Imagens | Segredos fora de imagens; workload identity |
| SbD-ToE Cap. 11 - Deploy Seguro | Segredos em runtime de deploy |
| Política de CI/CD Seguro (`17_policy-cicd-seguro.md`) | Secret detection no pipeline; masking de logs |
| OWASP Secrets Management Cheat Sheet | Referência de boas práticas de gestão de segredos |
| HashiCorp Vault Documentation | Cofre de referência; dynamic secrets; OIDC |
| NIST SP 800-57 | Key Management Guidelines |
| CIS Benchmark - Secrets Management | Controlos de referência |
| SSDF PO.5.2 | Implement and maintain secure environments for software development |
