---
id: policy-guidelines-desenvolvimento
title: Política de Curadoria de Guidelines de Desenvolvimento Seguro
description: Política organizacional que define os requisitos para a seleção, tailoring, publicação, versionamento e revisão periódica de guidelines de desenvolvimento seguro por stack tecnológica, incluindo a conversão de regras em configurações automáticas de linters e SAST, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, guidelines, desenvolvimento seguro, curadoria, linters, SAST, rulesets, tailoring, cap06, L1, L2, L3, governance]
grupo: desenvolvimento
sidebar_position: 14
---

# Política de Curadoria de Guidelines de Desenvolvimento Seguro

## 1. Objetivo

Esta política define os requisitos para a **seleção, curadoria, versionamento e revisão periódica de guidelines de desenvolvimento seguro** aplicáveis às stacks tecnológicas utilizadas pela organização.

Guidelines de desenvolvimento seguro não são documentos estáticos de boas práticas - são mecanismos vivos de governação técnica. Quando bem curadas e operacionalizadas como configurações de linters e rulesets SAST, reduzem a dependência de decisões ad-hoc, asseguram consistência entre equipas e tornam a conformidade verificável de forma automatizada.

O objetivo desta política é garantir que:

- Cada stack tecnológica em uso tem guidelines de desenvolvimento seguro aprovadas e publicadas
- As guidelines são derivadas de fontes reconhecidas e com tailoring documentado para o contexto da organização
- As regras são operacionalizadas como configurações de ferramentas (linters, SAST) sempre que tecnicamente viável
- A curadoria é realizada por ciclos regulares com aprovação formal

---

## 2. Âmbito

Esta política aplica-se a todas as stacks tecnológicas utilizadas no desenvolvimento de software na organização. Por "stack" entende-se o conjunto linguagem + runtime + frameworks principais (ex: Python/FastAPI, Java/Spring, TypeScript/Node, Go, Terraform/AWS).

---

## 3. Fontes de referência para guidelines

As guidelines organizacionais devem ser derivadas de fontes técnicas reconhecidas, que incluem (sem carácter exclusivo):

| Fonte | Domínio |
|---|---|
| OWASP Secure Coding Practices | Baseline transversal de desenvolvimento seguro |
| OWASP Cheat Sheet Series (por tecnologia) | Referências específicas por linguagem e framework |
| CWE Top 25 / SANS Top 25 | Fraquezas de implementação mais críticas |
| NIST SSDF (SP 800-218) | Framework de software seguro por fase do ciclo de vida |
| Rulesets upstream de ferramentas SAST | Semgrep, CodeQL, SonarQube, Bandit, ESLint Security, etc. |
| Benchmarks do fabricante | Guidelines de segurança da linguagem ou framework (ex: Go security, Python security model) |

O tailoring organizacional a partir destas fontes deve ser explicitamente documentado - indicando quais regras foram adotadas sem alteração, quais foram apertadas, quais foram desativadas e com que justificação.

---

## 4. Estrutura de uma guideline por stack

Cada guideline publicada deve ter, no mínimo:

- [ ] Identificação da stack coberta (linguagem, versão mínima, frameworks principais)
- [ ] Versão do documento e data de publicação
- [ ] Fontes utilizadas e versão referenciada
- [ ] Regras obrigatórias (não podem ser desativadas por projetos individuais)
- [ ] Regras recomendadas (podem ser desativadas com justificação registada)
- [ ] Configuração de ferramentas derivada das regras (ficheiros de configuração de linters/SAST)
- [ ] Tailoring documentado (regras upstream desativadas e justificação)
- [ ] Responsável pela curadoria e aprovação

---

## 5. Operacionalização como configurações de ferramentas

As guidelines devem ser convertidas em configurações de ferramentas sempre que o ecossistema o permita:

| Objetivo | Ferramentas de referência |
|---|---|
| Análise estática de segurança (SAST) | Semgrep, CodeQL, Bandit, Brakeman, SpotBugs, ESLint Security |
| Linters de qualidade e segurança | ESLint, Pylint, Flake8, golangci-lint, ktlint, Checkstyle |
| Verificação de padrões perigosos | Semgrep com rulesets customizados, grep-based rules |
| Secret detection | TruffleHog, Gitleaks, detect-secrets |

As configurações resultantes devem ser:

- [ ] Versionadas no repositório central de configurações da organização
- [ ] Reutilizáveis por projetos (por referência, não por cópia)
- [ ] Aplicadas automaticamente pelo pipeline CI - não dependentes de configuração local do developer

### 5.1 Proporcionalidade

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Guidelines documentadas por stack | Regras upstream sem tailoring | Curadas com tailoring documentado | Curadas + policy-as-code |
| Operacionalização como configuração de ferramenta | Recomendado | Obrigatório | Obrigatório |
| Configuração centralizada e reutilizável | Recomendado | Obrigatório | Obrigatório |
| Desvios à guideline registados por projeto | Opcional | Obrigatório | Obrigatório |

---

## 6. Cadência de revisão e publicação

| Nível | Cadência de revisão mínima |
|---|---|
| L1 | Anual ou por alteração major de stack |
| L2 | Trimestral ou por alteração major de stack |
| L3 | Contínua; revisão formal trimestral; alertas automáticos para novas regras upstream |

### 6.1 Triggers de revisão extraordinária

Para além da cadência regular, a guideline de uma stack deve ser revista sempre que:

- É publicada uma vulnerabilidade crítica com origem em padrão de código coberto pela guideline
- É adotada uma nova versão major da linguagem ou framework com alterações de segurança relevantes
- Uma ferramenta SAST utilizada publica rulesets com alterações materiais
- É identificado um padrão de vulnerabilidade recorrente em code reviews que não estava coberto

### 6.2 Processo de publicação

Cada nova versão de uma guideline deve seguir o processo:

1. Atualização do documento e configurações de ferramentas pelo curador designado
2. Revisão por AppSec Engineer (obrigatório L2/L3)
3. Revisão por Arquitetos de Software (obrigatório L2/L3)
4. Publicação de release/tag versionada no repositório central
5. Comunicação às equipas com registo de alterações (changelog)

---

## 7. Desvios a nível de projeto

Projetos individuais podem desativar regras recomendadas, mas não regras obrigatórias. Todo o desvio deve ser registado:

- [ ] Regra desativada identificada (ex: `semgrep-rule-id`)
- [ ] Justificação técnica documentada (ex: falso positivo sistemático no contexto do projeto)
- [ ] Aprovação por AppSec Engineer em L2/L3
- [ ] Registo em ficheiro de configuração do projeto com comentário explícito (não apenas supressão inline)

:::warning
Supressões inline sem referência a registo de desvio aprovado (ex: `# noqa`, `// nosec`, `// nolint` sem contexto) são tratadas como não-conformidade em L2/L3 e devem ser detetadas e reportadas pelo pipeline.
:::

---

## 8. Responsabilidades

| Role | Responsabilidade |
|---|---|
| AppSec Engineer | Curar e manter guidelines por stack; aprovar versões e desvios; selecionar e configurar ferramentas SAST |
| Arquiteto de Software | Rever guidelines quanto à adequação técnica e impacto arquitetural; aprovar versões |
| Developer | Aplicar guidelines da stack; registar desvios justificados; não suprimir regras sem registo formal |
| Tech Lead | Assegurar que o projeto referencia a versão correta das guidelines; rever desvios da equipa |
| DevOps / SRE | Integrar configurações de linters/SAST no pipeline; garantir que o pipeline referencia configurações centrais |

---

## 9. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente com origem em padrão de código não coberto por guidelines existentes
- Adoção de nova stack tecnológica pela organização
- Alteração significativa nas ferramentas SAST utilizadas

---

## 10. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 06 - Desenvolvimento Seguro | Curadoria de guidelines, operacionalização, proporcionalidade L1-L3 |
| OWASP Secure Coding Practices | Baseline de desenvolvimento seguro |
| OWASP Cheat Sheet Series | Referências por linguagem e framework |
| CWE Top 25 | Fraquezas de implementação mais críticas |
| NIST SP 800-218 (SSDF) | Framework de software seguro por fase |
| Semgrep Registry | Rulesets de referência para SAST |
| Política de Revisão de Código (`15_policy-revisao-codigo.md`) | Aplicação de guidelines em code review |
| Política de CI/CD Seguro (`17_policy-cicd-seguro.md`) | Integração de linters/SAST no pipeline |
