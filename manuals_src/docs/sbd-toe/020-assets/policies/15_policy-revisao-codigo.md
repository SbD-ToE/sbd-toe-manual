---
id: policy-revisao-codigo
title: Política de Revisão de Código
description: Política organizacional que define os requisitos para a revisão de código como ponto de controlo de segurança, incluindo checklist obrigatória, critérios de aprovação, papéis de reviewer, cobertura mínima e integração com ferramentas automáticas, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, code review, revisão de código, checklist, PR, SAST, desenvolvimento seguro, cap06, L1, L2, L3, governance]
grupo: desenvolvimento
sidebar_position: 15
---

# Política de Revisão de Código

## 1. Objetivo

Esta política define os requisitos para a **revisão de código como ponto de controlo de segurança formal**, aplicável a todos os pull requests (PRs) que introduzam alterações em código de produção, configuração de segurança ou infraestrutura como código.

A revisão de código é, simultaneamente, um controlo de qualidade técnica e um mecanismo de deteção de vulnerabilidades. Quando sistematizada com checklist e critérios de aprovação claros, complementa as ferramentas automáticas (SAST, linters) com julgamento humano sobre lógica de negócio, fluxos de autorização e decisões de design que as ferramentas não conseguem avaliar de forma fiável.

O objetivo desta política é garantir que:

- Todo o PR relevante é revisto por pelo menos um reviewer com competência técnica adequada
- A revisão inclui verificação de segurança com base em checklist normalizada
- A aprovação é registada de forma rastreável e auditável
- A revisão humana é complementada - não substituída - por análise automática

---

## 2. Âmbito e obrigatoriedade

| Tipo de alteração | L1 | L2 | L3 |
|---|---|---|---|
| Código de lógica de negócio | Recomendado | Obrigatório (1 reviewer) | Obrigatório (2 reviewers) |
| Autenticação, autorização, sessões | Obrigatório | Obrigatório + AppSec | Obrigatório + AppSec |
| Tratamento de dados sensíveis ou PII | Obrigatório | Obrigatório + AppSec | Obrigatório + AppSec |
| Configuração de segurança (CORS, headers, TLS) | Obrigatório | Obrigatório + AppSec | Obrigatório + AppSec |
| IaC com impacto em segurança | Recomendado | Obrigatório + DevOps | Obrigatório + DevOps + AppSec |
| Integração externa nova | Recomendado | Obrigatório | Obrigatório + AppSec |
| Alteração de pipeline CI/CD | Recomendado | Obrigatório | Obrigatório + AppSec |
| **Prompts, *skill files*, *agent files* e *rules*** (`.claude/skills/*`, `.claude/agents/*`, `.cursorrules`, `.github/copilot-instructions.md`, `AGENTS.md`) | Recomendado | Obrigatório | Obrigatório + AppSec |
| **Alteração de `tools_allowlist` ou *scopes* de agente AI** | Obrigatório + AppSec | Obrigatório + AppSec | Obrigatório + AppSec + GRC |
| **Mandate de agente AI** (Policy 38) | Aprovação Tech Lead | Aprovação Tech Lead + AppSec | Aprovação Tech Lead + AppSec + GRC; A4 com `CISO` |

> 📌 **Sobre prompts e *skill files* como código.** Estes artefactos decidem o que o assistente sabe, que *tools* pode invocar e como interage com a organização. Tratamo-los com a mesma disciplina de revisão que aplica-se a código — incluindo *secret scanning* e atenção redobrada a mudanças em `tools_allowlist`/*scopes*. Ver detalhe operacional em [Cap. 06 — Prompts como código](/sbd-toe/sbd-manual/desenvolvimento-seguro/addon/genia-e-seguranca#prompts-como-codigo) e em [Policy 38 — Mandates de Agentes AI](./policy-mandates-agentes).

---

## 3. Checklist de segurança mínima

Cada PR deve ser avaliado com base nos seguintes pontos de controlo. A checklist deve estar incluída no template de PR do repositório e preenchida pelo reviewer antes da aprovação:

### 3.1 Autenticação e autorização
- [ ] Endpoints protegidos com autenticação adequada ao contexto
- [ ] Lógica de autorização verificada - não apenas autenticação
- [ ] Ausência de escalada de privilégios horizontal ou vertical
- [ ] Tokens, sessões ou credenciais não expostos em logs ou respostas

### 3.2 Validação de input e output
- [ ] Inputs validados e sanitizados antes de processamento
- [ ] Ausência de concatenação direta de input em queries, comandos ou templates (SQLi, CMDi, SSTI)
- [ ] Output codificado adequadamente para o contexto (HTML, JSON, SQL) para prevenir XSS

### 3.3 Gestão de segredos e dados sensíveis
- [ ] Nenhum segredo, password, chave ou token hardcoded no código ou configuração
- [ ] Dados sensíveis ou PII não expostos em logs, traces ou respostas de erro
- [ ] Dados classificados tratados conforme a classificação atribuída

### 3.4 Dependências e imports
- [ ] Novas dependências aprovadas conforme Política de Dependências
- [ ] Imports de bibliotecas validados - sem copiagem de código externo sem proveniência

### 3.5 Tratamento de erros e logging
- [ ] Erros tratados sem exposição de informação técnica ao utilizador (stack traces, paths, versões)
- [ ] Eventos relevantes de segurança registados (tentativas de acesso, erros de autorização)
- [ ] Logging sem exposição de dados sensíveis

### 3.6 Criptografia e comunicações
- [ ] Algoritmos criptográficos aprovados pela organização (sem MD5, SHA-1, DES, RC4)
- [ ] Comunicações externas sobre TLS; sem validação de certificado desativada

### 3.7 Padrões e anti-patterns
- [ ] Ausência de padrões perigosos detetados por SAST/linters
- [ ] Sem supressões inline não justificadas (`# noqa`, `// nosec`, `// nolint`)
- [ ] Lógica de concorrência ou estado partilhado sem race conditions óbvios

---

## 4. Critérios de aprovação

Um PR só pode ser aprovado e fundido quando:

- [ ] Todos os itens críticos da checklist foram verificados
- [ ] Findings bloqueantes de SAST/linters estão resolvidos ou têm exceção formal aprovada
- [ ] O número mínimo de reviewers aprovados foi atingido (conforme tabela da secção 2)
- [ ] Nenhum reviewer aprovou o seu próprio código (self-approval proibida)

:::warning
A aprovação de um PR não é a confirmação de que o código está isento de vulnerabilidades - é a confirmação de que foi sujeito a revisão competente e sistemática. A responsabilidade de segurança é partilhada entre o autor e os reviewers.
:::

---

## 5. Reviewers e competência

### 5.1 Requisitos de reviewer

| Nível | Reviewer mínimo | Reviewer adicional quando aplicável |
|---|---|---|
| L1 | Developer com competência na stack | - |
| L2 | Developer sénior ou Tech Lead | AppSec Engineer para alterações de segurança |
| L3 | Tech Lead | AppSec Engineer obrigatório para alterações de segurança |

### 5.2 Self-review

A self-review (aprovação do próprio autor) é proibida independentemente do nível. Em equipas de uma só pessoa, deve ser seguido o processo de peer review com um elemento externo ou com o AppSec Engineer.

### 5.3 Reviewer rotation

Em L3, recomenda-se rotação de reviewers para evitar pontos cegos sistemáticos. A mesma combinação autor/reviewer não deve ser a única válida para o mesmo módulo de forma continuada.

---

## 6. Integração com ferramentas automáticas

A revisão humana complementa - não substitui - a análise automática. O pipeline deve executar, antes ou durante o PR, as seguintes verificações automáticas:

| Verificação | Quando executa | Bloqueia merge em L2/L3? |
|---|---|---|
| Linters de segurança (ESLint Security, Bandit, etc.) | A cada push no PR | Sim, para findings críticos |
| SAST (Semgrep, CodeQL, SonarQube) | A cada push no PR | Sim, para findings High/Critical |
| Secret detection (TruffleHog, Gitleaks) | A cada push no PR | Sim, para qualquer finding |
| SCA (dependências novas) | Quando manifesto é alterado | Sim, conforme Política de Dependências |

Os resultados das verificações automáticas devem ser visíveis no PR (comentário ou status check) antes de o reviewer iniciar a revisão humana.

---

## 7. Rastreabilidade e evidência

Cada revisão deve produzir evidência rastreável:

- [ ] Aprovação registada na plataforma de controlo de versão (PR aprovado, não apenas comentado)
- [ ] Checklist preenchida e visível no PR (template ou comentário estruturado)
- [ ] Comentários de revisão com ações corretivas registados e resolvidos antes do merge
- [ ] Histórico de revisões retido conforme Política de Rastreabilidade

---

## 8. Dimensão educativa

A revisão de código é também um mecanismo de transferência de conhecimento. Os reviewers devem:

- Explicar os problemas encontrados com referência à guideline ou CWE correspondente
- Sugerir a alternativa segura, não apenas apontar o problema
- Evitar aprovações sem comentário quando existem pontos de melhoria identificados

Padrões recorrentes de vulnerabilidades identificados em PRs devem ser reportados ao AppSec Engineer para atualização das guidelines e das configurações de SAST.

---

## 9. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer (autor) | Submeter PR com checklist preenchida; resolver findings antes de solicitar revisão |
| Developer / Tech Lead (reviewer) | Rever com checklist; registar comentários; aprovar apenas quando critérios cumpridos |
| AppSec Engineer | Rever PRs com alterações de segurança em L2/L3; atualizar checklist com padrões emergentes |
| Scrum Master / Tech Lead | Garantir que o processo é seguido; gerir PRs sem reviewer disponível |
| DevOps / SRE | Configurar branch protection rules que imponham o número mínimo de aprovações |

---

## 10. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Vulnerabilidade introduzida em produção que deveria ter sido detetada em code review
- Alteração das guidelines de desenvolvimento que introduza novos itens de checklist
- Alteração das ferramentas SAST com impacto nos gates do pipeline

---

## 11. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 06 - Desenvolvimento Seguro | Revisão de código como controlo de segurança, proporcionalidade L1-L3 |
| Política de Guidelines de Desenvolvimento (`14_policy-guidelines-desenvolvimento.md`) | Checklist derivada das guidelines por stack |
| Política de CI/CD Seguro (`17_policy-cicd-seguro.md`) | Integração de SAST/linters no pipeline de PR |
| OWASP Code Review Guide | Referência de boas práticas de revisão de código segura |
| CWE Top 25 | Fraquezas de implementação a verificar em revisão |
| NIST SP 800-218 (SSDF) PW.2 | Review the software design to address security requirements |
| SAFECode Fundamental Practices | Peer code review como prática de segurança fundamental |
