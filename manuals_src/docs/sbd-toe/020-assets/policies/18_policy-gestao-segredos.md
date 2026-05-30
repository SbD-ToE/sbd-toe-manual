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

## 9. Agentes AI como *principals* não-humanos

O capítulo anterior descreve segredos para identidades CI tradicionais (*runners*, *workloads*). Quando um agente AI passa a operar o pipeline ou recursos da organização — `Claude Code` a executar *tool calls*, `Copilot Workspace` a actuar em PRs, agentes próprios via SDK — esse agente é **mais um *principal* não-humano** sujeito aos mesmos princípios desta política, com três especializações.

### 9.1 Identidade dedicada por agente e por ambiente

- Cada agente AI tem **identidade *workload* efémera** (OIDC) distinta — sem reuso de credenciais humanas, sem reuso entre ambientes (dev / staging / prod) nem entre agentes.
- TTL ≤ 1h (mesma regra das outras *workload identities*).
- A identidade está declarada no *mandate* do agente (campo `identity_ref` — ver [Policy 38 — Mandates de Agentes AI](./policy-mandates-agentes)).

### 9.2 *Scoping* per-tool

A identidade do agente recebe **apenas os *scopes* necessários para as *tools* declaradas na `tools_allowlist`** do *mandate* — não os *scopes* máximos suportados pelo runtime. Exemplos práticos:

- Agente que abre PRs: `gh:pr:write`, `gh:repo:read`. **Não** `gh:repo:write` nem `gh:repo:delete`.
- Agente que aplica manifests Kubernetes em *staging*: `k8s:deploy:staging:apply`. **Não** `cluster-admin`.
- Agente que publica pacotes: `npm:publish:scoped-package`. **Não** `npm:publish:*`.

Alterar `tools_allowlist` ou *scopes* é uma alteração estruturalmente equivalente a alterar uma IAM policy — exige novo ciclo de aprovação do *mandate* (ver Policy 38 §5).

### 9.3 *Kill-switch* operacional

Para agentes em nível A2+, o procedimento de **revogação imediata** ([`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) tem de ser exercitado periodicamente:

| Nível de autonomia | Cadência mínima de exercício |
|---|---|
| A2 | Anual (em sandbox/staging) |
| A3 | Trimestral (em sandbox/staging) |
| A4 | Mensal (em sandbox/staging) |

O exercício mede tempo total entre accionamento e revogação efectiva (revogação OIDC + terminação de runtime + isolamento de namespace). Resultado registado; falha no exercício é tratada como degradação operacional e bloqueia novas activações de agentes A3/A4 até estar resolvido.

### 9.4 Proibições específicas

- ❌ **Reutilizar credenciais humanas** para autenticar o agente — viola o princípio fundamental desta política aplicado a *principals* AI.
- ❌ **Token *long-lived* (>1h)** em qualquer identidade de agente AI — mesma regra que se aplica a runners CI.
- ❌ **`scope` que excede a `tools_allowlist`** do *mandate* — *over-privilege* silencioso é incidente operacional.
- ❌ **Partilha de identidade** entre dois agentes ou entre agente e humano — quebra o *audit trail*.
- ❌ **Operação em A3/A4 sem *kill-switch* exercitado** dentro da cadência exigida — o *kill-switch* é decorativo se nunca foi medido.

> 📌 Tudo o resto desta política (proibições absolutas §3, armazenamento centralizado §4, injeção em runtime §5, TTL/rotação §6) aplica-se sem reformulação ao caso dos agentes AI.

---

## 10. PII e dados sensíveis em *prompts* (cross-link RGPD)

Os capítulos anteriores cobrem segredos clássicos — *tokens*, chaves, credenciais. Quando um agente AI recebe input de utilizador (chat, *document upload*, *form*), os **dados pessoais** entram no *prompt* e, por arrastamento, podem viajar até ao *provider* do modelo. A categoria do problema é parecida — informação sensível a fluir por canal não controlado — mas o regime jurídico aplicável é o do **RGPD**, não o desta política. Esta secção articula explicitamente os dois para que a coerência operacional não se perca na fronteira.

### 10.1 Princípio de minimização

- O *prompt* enviado ao modelo deve conter **apenas os dados pessoais estritamente necessários** para a tarefa. Aplica-se directamente o princípio da minimização do RGPD Art. 5.º, n.º 1, al. c).
- **Redacção / pseudonimização antes do envio** quando viável — substituir nomes, e-mails, IDs por *placeholders* (`<USER_X>`, `<EMAIL_REDACTED>`) e remapear no output.
- Quando a redacção não é viável (ex.: tarefas que exigem o conteúdo literal), a decisão é registada e revista com cadência do *mandate* (Policy 38).

### 10.2 Base legal explícita

Cada uso operacional em que o agente vê PII tem **base legal RGPD declarada** — Art. 6.º (consentimento, contrato, obrigação legal, interesse legítimo, etc.) e, quando categorias especiais (Art. 9.º), base legal reforçada. A base legal é parte do *mandate* do agente (Policy 38 — adicionar campo `legal_basis` quando aplicável) ou da ficha de tratamento do projecto, e é revisitada nas revisões periódicas.

### 10.3 Sub-processadores

O *provider* do modelo é um **sub-processador** quando trata dados pessoais em nome da organização (RGPD Art. 28.º). Aplica-se a cláusula contratual prevista em [Policy 33 §10](./policy-contratacao-segura):

- Contrato de sub-processador com cláusulas explícitas (retention, *training opt-out*, audit rights).
- Localização de processamento documentada; *Standard Contractual Clauses* (SCCs) ou outro mecanismo válido para transferências internacionais (RGPD Art. 44.º–49.º) quando o *provider* processa fora do EEA.
- **Sem PII para *providers* fora da lista aprovada** ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)).

### 10.4 *Training opt-out* obrigatório para PII

Quando o conteúdo do *prompt* inclui dados pessoais, é exigido contratualmente que o *provider* **não use esse conteúdo para treino futuro do modelo**. Preferência por **zero retention** para PII; quando o *provider* mantém logs operacionais, com retenção minimizada e propósito declarado.

### 10.5 Telemetria sob controlo do *deployer*

Os logs de inferência sob controlo da organização (Art. 19.º AI Act / RGPD Art. 5.º) cumprem [`OPS-003`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes) (retenção) e [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) (audit per *tool invocation*) com **redacção de PII nos `args`** — o *audit trail* preserva o suficiente para responder a auditoria sem replicar os dados pessoais.

### 10.6 Direitos do titular dos dados

Quando a interacção do utilizador com o agente gera dados pessoais, aplicam-se os direitos do RGPD (acesso Art. 15.º, rectificação Art. 16.º, apagamento Art. 17.º, oposição Art. 21.º). Em particular:

- **Apagamento dos *audit events*** sob controlo do *deployer* quando o titular exerce direito ao esquecimento (sujeito a obrigações legais de retenção concorrentes).
- **Não-retenção pelo *provider*** — verificado contratualmente. Quando a retenção pelo *provider* existe, o titular tem de poder accionar o direito também aí.

### 10.7 Proporcionalidade

| Requisito | L1 | L2 | L3 |
|---|:--:|:--:|:--:|
| Minimização / redacção antes do envio | Recomendado | Obrigatório quando viável | Obrigatório (categorias especiais sempre redactadas) |
| Base legal declarada | Recomendado | Obrigatório | Obrigatório (revisão GRC) |
| Sub-processador com cláusulas Art. 28.º | Obrigatório (sempre que há PII) | Obrigatório | Obrigatório + revisão Legal |
| *Training opt-out* contratualizado | Obrigatório (sempre que há PII) | Obrigatório | Obrigatório |
| Localização EEA / SCCs quando aplicável | Obrigatório (quando há PII e processamento fora EEA) | Obrigatório | Obrigatório (preferência por processamento EEA) |
| Redacção de PII nos `audit events` ([`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012)) | Recomendado | Obrigatório | Obrigatório |
| Procedimento para direitos do titular | Recomendado | Obrigatório | Obrigatório (incl. apagamento sob controlo do *deployer*) |

### 10.8 Anti-padrões

- ❌ Enviar PII a *provider* fora da lista aprovada — *shadow AI* com risco RGPD.
- ❌ Logar *prompts* com PII sem redacção em [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) — `audit trail` torna-se ele próprio repositório de dados pessoais sem base legal específica.
- ❌ Confiar que o *provider* "não usa para treino" sem cláusula contratual — declarações operacionais não substituem o Art. 28.º.
- ❌ Ignorar categorias especiais (Art. 9.º RGPD) no prompt — saúde, biometria, dados de menores, etc. exigem base legal reforçada que muitos casos de uso de chatbots não satisfazem.
- ❌ Tratar redacção como ofuscação suficiente — *pseudonimização* (RGPD) não é anonimização; PII pseudonimizada continua a ser dado pessoal.

### 10.9 Cruzamento com cross-check RGPD

Para alinhamento detalhado com o regulamento, ver o [cross-check RGPD](/sbd-toe/cross-check-normativo/gdpr/intro). Esta secção mantém a coerência operacional na fronteira AppSec ↔ RGPD; o cross-check trata as obrigações jurídicas em detalhe.

---

## 11. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente com origem em segredo exposto ou não rotacionado
- Adoção de novo cofre de segredos ou plataforma de cloud
- Alteração de fornecedor com impacto em chaves de integração

---

## 12. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 07 - CI/CD Seguro | Gestão e injeção de segredos em pipeline; **US-19 — Agentes AI como principals na pipeline** |
| SbD-ToE Cap. 09 - Containers e Imagens | Segredos fora de imagens; workload identity |
| SbD-ToE Cap. 11 - Deploy Seguro | Segredos em runtime de deploy |
| SbD-ToE Cap. 04 — Arquitetura Segura ([`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)) | Agente como *principal* isolado; least privilege per-tool |
| Política de CI/CD Seguro (`17_policy-cicd-seguro.md`) | Secret detection no pipeline; masking de logs |
| Policy 38 — Mandates de Agentes AI | Operacionaliza [`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn): mandate, ownership, kill-switch |
| Policy 16 — Uso de Ferramentas de Apoio | Regras operacionais A2+ para agentes |
| NIST SP 800-207 — Zero Trust Architecture | Princípios aplicados a *principals* não-humanos (incluindo agentes AI) |
| OWASP Secrets Management Cheat Sheet | Referência de boas práticas de gestão de segredos |
| HashiCorp Vault Documentation | Cofre de referência; dynamic secrets; OIDC |
| NIST SP 800-57 | Key Management Guidelines |
| CIS Benchmark - Secrets Management | Controlos de referência |
| SSDF PO.5.2 | Implement and maintain secure environments for software development |
