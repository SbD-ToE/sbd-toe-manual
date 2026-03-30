---
id: policy-dast-fuzzing
title: Política de DAST e Fuzzing
description: Política organizacional que define os requisitos, critérios de execução, gestão de findings e responsabilidades para testes dinâmicos de segurança (DAST) e fuzzing, proporcional ao nível de risco da aplicação.
tags: [policy, dast, fuzzing, testes dinâmicos, segurança, cap10, cap07, L2, L3, findings, pipeline]
grupo: testes
sidebar_position: 1
---

# Política de DAST e Fuzzing

## 1. Objetivo

Esta política define os requisitos mínimos para a execução de **testes dinâmicos de segurança (DAST)** e **fuzzing** em aplicações classificadas como L2 ou L3 no modelo SbD-ToE.

O objetivo é garantir que vulnerabilidades comportamentais e de tratamento de input são detetadas antes da promoção a produção, complementando os mecanismos de análise estática (SAST) com validação em runtime.

DAST e fuzzing são técnicas complementares:

- **DAST** - simula o comportamento de um utilizador ou atacante externo sobre a aplicação em execução, identificando falhas que só se manifestam em runtime;
- **Fuzzing** - injeta inputs malformados, inesperados ou aleatórios em endpoints críticos, revelando falhas de parsing, crashes e comportamentos anómalos não cobertos por testes planeados.

---

## 2. Âmbito e proporcionalidade

| Técnica | L1 | L2 | L3 |
|---|---|---|---|
| DAST | Manual/exploratório (opcional) | Automático autenticado | Automático + cobertura ampliada |
| Fuzzing | Opcional | Endpoints prioritários | Endpoints críticos obrigatórios |
| IAST | Não aplicável | Recomendado | Obrigatório |

Esta política é **obrigatória para L2 e L3**. Para L1, as práticas aqui descritas são recomendadas mas não obrigatórias.

---

## 3. DAST - Testes Dinâmicos de Segurança

### 3.1 Quando executar

| Evento | Obrigatoriedade |
|---|:---:|
| Promoção de build para staging | Obrigatório |
| Antes de qualquer release para produção | Obrigatório |
| Após alteração de arquitetura ou superfície de exposição | Obrigatório |
| Execução periódica sobre versão em produção | Recomendado (trimestral) |

### 3.2 Pré-requisitos de ambiente

- O ambiente de execução deve ser **isolado** - DAST nunca deve ser executado em produção;
- Os dados do ambiente de teste devem ser **fictícios ou mascarados** - nunca dados reais de utilizadores;
- O ambiente deve ser **equivalente a produção** em termos de versões, configurações e dependências;
- O ambiente não deve ser **partilhado** com outros projetos durante a execução do scan.

### 3.3 Configuração obrigatória

**Autenticação:**

- [ ] Login flow configurado na ferramenta com sessão autenticada válida
- [ ] Credenciais de teste segregadas - conta dedicada, nunca conta de utilizador real
- [ ] Credenciais armazenadas como secrets no pipeline - nunca em texto simples ou repositório
- [ ] Sessão com token de curta duração (TTL adequado à duração do scan)

**Scope:**

- [ ] Lista de URLs/endpoints incluídos definida e versionada
- [ ] Lista de exclusões explícita e justificada (ex: endpoints de logout, reset de password, envio de notificações externas, operações destrutivas irreversíveis)
- [ ] Configuração de scope versionada no repositório junto à definição do pipeline

**Integração no pipeline:**

- [ ] Job DAST executado **após** deploy em staging e **antes** de promoção a produção
- [ ] Relatório correlacionado com commit SHA e release tag
- [ ] Relatório arquivado como artefacto do pipeline com retenção mínima de 90 dias
- [ ] Resultado do DAST rastreável no registo de release

### 3.4 Critérios de bloqueio e resposta

| Severidade | Ação |
|---|---|
| Critical | Bloqueia automaticamente; escala imediata para AppSec Engineer |
| High | Bloqueia automaticamente; requer correção validada ou exceção formal |
| Medium | Não bloqueia; registo obrigatório na plataforma centralizada; SLA de 30 dias |
| Low / Info | Não bloqueia; registo; revisão trimestral |

:::note Separação entre sinal automático e decisão humana
O pipeline reporta o resultado (sinal automático). A decisão de override ou exceção é sempre **humana e documentada** - nunca implícita ou por timeout. Todo o override requer aprovação explícita de AppSec Engineer com registo de rationale e prazo de validade máximo.
:::

### 3.5 Artefactos produzidos

| Artefacto | Retenção mínima |
|---|---|
| Relatório DAST (HTML/JSON/SARIF) | 90 dias |
| Evidência de gate (pass/fail) em log de pipeline | 90 dias |
| Findings abertos na plataforma centralizada | Até fecho ou aceitação formal |
| Registo de exceções | 1 ano |

---

## 4. Fuzzing - Testes de Inputs Inesperados

### 4.1 Quando executar

| Evento | Obrigatoriedade (L2) |
|---|:---:|
| Por release major | Obrigatório |
| Periodicidade regular | Obrigatório (trimestral) |
| Após adição de novo endpoint com parsing de input | Obrigatório |
| Após alteração de lógica de validação ou deserialização | Recomendado |

### 4.2 Seleção de targets

**Targets obrigatórios para L2:**

- Endpoints que recebem input externo não estruturado (formulários, JSON livre, query params)
- APIs com parsing de formatos de dados (JSON, XML, multipart, CSV, binário)
- Endpoints de upload de ficheiros
- Endpoints de pesquisa com parâmetros dinâmicos
- Endpoints com lógica de deserialização ou avaliação de expressões

**Exclusões por defeito** (inclusão requer justificação explícita):

- Endpoints de logout ou invalidação de sessão
- Endpoints com envio de notificações externas (email, SMS, webhooks)
- Endpoints com rate limiting agressivo sem instância de teste dedicada

### 4.3 Configuração obrigatória

**Ambiente:**

- [ ] Instância da aplicação **isolada** para fuzzing - sem ligação a sistemas externos reais
- [ ] Monitorização ativa durante execução: CPU, memória, crashes, logs de erro
- [ ] Mecanismo de deteção de crashes e respostas anómalas configurado

**Targets e perfis:**

- [ ] Lista de targets definida, versionada e aprovada por AppSec
- [ ] Perfis de fuzzing (dicionários, corpora, estratégias) versionados no repositório
- [ ] Corpora de inputs mantidos e atualizados entre execuções

**Resultados:**

- [ ] Anomalias registadas com PoC mínima reproduzível (input exato, endpoint, versão da aplicação)
- [ ] Relatório com casos reproduzíveis arquivado

### 4.4 Critérios de severidade

| Resultado | Severidade | Ação |
|---|---|---|
| Crash da aplicação / Out-of-Memory | Critical | Bloqueia release; escala AppSec |
| Exposição de dados internos ou stack trace | High | Bloqueia release |
| Comportamento anómalo controlado | Medium | Registo e triagem |
| Timeout ou degradação de performance | Low | Registo; análise posterior |

### 4.5 Artefactos produzidos

| Artefacto | Retenção mínima |
|---|---|
| Relatório de fuzzing | 90 dias |
| Corpora de inputs (versionados) | Permanente |
| Casos reproduzíveis (PoC) na plataforma de findings | Até fecho |
| Registo de exceções | 1 ano |

---

## 5. Gestão centralizada de findings

Todos os findings de DAST e fuzzing são consolidados na plataforma centralizada de gestão de segurança, em conjunto com os resultados de SAST, IAST e SCA.

**Metadados obrigatórios por finding:**

| Campo | Descrição |
|---|---|
| Ferramenta de origem | DAST / Fuzzing / SAST / IAST / SCA |
| Severidade | Critical / High / Medium / Low / Info |
| CWE e/ou CVE | Quando aplicável |
| Commit SHA e release tag | Rastreabilidade ao artefacto |
| Estado | Aberto / Em correção / Aceite / Suprimido |
| Owner de remediação | Responsável pela correção |
| SLA de resolução | Conforme tabela da secção 5.1 |

### 5.1 SLAs de resolução

| Severidade | SLA |
|---|---|
| Critical | 24 horas |
| High | 7 dias |
| Medium | 30 dias |
| Low | 90 dias |

---

## 6. Framework de decisão para findings (Checklist C1)

Quando um finding bloqueia o pipeline e a equipa avalia override ou exceção, a decisão deve ser documentada com os seguintes critérios:

- [ ] **Exploitabilidade** - o finding é exploitável no contexto atual? De que forma?
- [ ] **Mitigações existentes** - existem controlos compensatórios ativos?
- [ ] **Impacto de negócio** - qual o impacto real se o finding for explorado?
- [ ] **Remediação** - quando e como será corrigido?
- [ ] **Decisão** - CORRIGIR / ACEITAR COM PRAZO / SUPRIMIR (com justificação)
- [ ] **Aprovação** - AppSec Engineer (obrigatório para High e Critical)

:::warning
A decisão de suprimir um finding Critical requer aprovação adicional do responsável de segurança (CISO ou equivalente) e prazo máximo de 7 dias.
:::

---

## 7. Exceções a esta política

Toda exceção à presente política requer:

1. Justificação técnica documentada
2. Aprovação de AppSec Engineer
3. Mitigação compensatória definida e ativa
4. Prazo de validade máximo: **30 dias** (renovável com nova aprovação explícita)
5. Registo formal no repositório de exceções do projeto

Exceções a findings de severidade Critical têm prazo máximo de **7 dias** e requerem aprovação adicional do responsável de segurança.

---

## 8. Responsabilidades

| Role | Responsabilidade |
|---|---|
| AppSec Engineer | Definição de scope, aprovação de exceções, triagem de findings High e Critical |
| QA / Testes | Execução de DAST e fuzzing, definição e manutenção de targets e corpora |
| DevOps / SRE | Integração no pipeline, manutenção do ambiente de staging isolado |
| Developer | Correção de findings, participação na triagem e análise de contexto |
| Gestão de Produto | Aprovação de release, aceitação formal de risco residual |

---

## 9. Revisão e auditoria

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Alteração significativa de arquitetura ou superfície de exposição da aplicação
- Incidente de segurança relacionado com inputs ou comportamento em runtime
- Alteração do nível de risco classificado da aplicação
- Alteração regulatória ou normativa relevante

A evidência de execução desta política (relatórios, logs de gate, registos de exceção) deve ser **auditável** por funções de GRC e por auditores externos.

---

## 10. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 10 - Testes de Segurança | Requisitos de DAST, fuzzing, gestão de findings |
| SbD-ToE Cap. 07 - CI/CD Seguro | Integração de gates de segurança no pipeline |
| SbD-ToE Cap. 02 - Requisitos de Segurança | Rastreabilidade requisito → teste → evidência |
| OWASP Testing Guide (OTG) | Metodologia de testes dinâmicos |
| OWASP Web Security Testing Guide (WSTG) | Cobertura de categorias de vulnerabilidades |
| NIST SP 800-115 | Technical Guide to Information Security Testing |
| CWE Top 25 | Categorização de weaknesses |
| SSDF PW.8 | Práticas de testes de segurança no SDLC |
