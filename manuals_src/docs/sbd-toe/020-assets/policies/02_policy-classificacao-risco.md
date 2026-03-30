---
id: policy-classificacao-risco
title: Política de Classificação de Risco Aplicacional
description: Política organizacional que define o modelo obrigatório de classificação de risco por eixos (Exposição, Dados, Impacto), os momentos de aplicação, os critérios de revisão e os requisitos de registo formal, para todas as aplicações desenvolvidas ou operadas pela organização.
tags: [policy, classificação, risco, L1, L2, L3, cap01, eixos, exposição, dados, impacto, governance]
grupo: risco
sidebar_position: 2
---

# Política de Classificação de Risco Aplicacional

## 1. Objetivo

Esta política define o modelo obrigatório de classificação de risco aplicacional adotado pela organização, com base no modelo SbD-ToE.

A classificação de risco é o **ponto de entrada para a aplicação proporcional de controlos de segurança**. Sem uma classificação formal, validada e rastreável, não é possível garantir que os controlos aplicados são adequados ao contexto técnico e de negócio de cada aplicação.

A política estabelece:

- O modelo de classificação a utilizar e os seus eixos de avaliação;
- Os momentos obrigatórios de aplicação e reavaliação;
- Os critérios de escalão de risco (L1, L2, L3) e as suas implicações;
- Os requisitos de registo formal, aprovação e rastreabilidade.

---

## 2. Âmbito

Esta política aplica-se a **todas as aplicações desenvolvidas, operadas ou contratadas** pela organização, independentemente da sua natureza (interna, externa, pública, API, serviço de backend, produto), tecnologia ou modelo de entrega.

A classificação deve ser realizada **antes do início do desenvolvimento** ou, em aplicações existentes sem classificação prévia, no primeiro ciclo de revisão após adoção do modelo SbD-ToE.

---

## 3. Modelo de classificação - Eixos E+D+I

A classificação de risco baseia-se na avaliação de três eixos independentes:

| Eixo | Designação | O que avalia |
|:---:|---|---|
| **E** | Exposição | Superfície de ataque e acessibilidade da aplicação |
| **D** | Dados | Sensibilidade e volume dos dados tratados |
| **I** | Impacto | Consequência de um incidente de segurança para o negócio e para terceiros |

A pontuação combinada dos três eixos determina o nível de criticidade global da aplicação.

### 3.1 Escalões de risco

| Nível | Descrição geral | Exemplos típicos |
|---|---|---|
| **L1** | Baixo risco - aplicação interna, sem dados sensíveis, impacto limitado | Ferramentas internas, dashboards sem PII, utilitários |
| **L2** | Risco médio - exposição pública ou dados de utilizadores, impacto moderado | APIs públicas, aplicações com autenticação, portais de cliente |
| **L3** | Risco elevado - sistemas regulados, PII, dados críticos, impacto severo | Sistemas financeiros, saúde, infraestrutura crítica, dados regulados |

### 3.2 Critérios por eixo

**Eixo E - Exposição:**

| Valor | Critério |
|---|---|
| Baixo | Acesso restrito a rede interna, sem exposição externa |
| Médio | Acesso autenticado por utilizadores externos ou parceiros |
| Elevado | Acesso público sem autenticação, ou API exposta a terceiros |

**Eixo D - Dados:**

| Valor | Critério |
|---|---|
| Baixo | Sem dados pessoais, sem dados regulados, sem segredos de negócio |
| Médio | Dados pessoais de utilizadores, dados de negócio com confidencialidade |
| Elevado | PII sensível, dados regulados (RGPD, saúde, financeiro), segredos críticos |

**Eixo I - Impacto:**

| Valor | Critério |
|---|---|
| Baixo | Impacto operacional limitado; sem consequências para terceiros |
| Médio | Impacto operacional significativo; possível dano reputacional |
| Elevado | Impacto crítico no negócio; consequências regulatórias, legais ou para terceiros |

### 3.3 Contextos de automação e apoio à decisão

A utilização de mecanismos de automação ou apoio à decisão (incluindo sistemas de IA) **não cria novos eixos de risco**, mas deve ser considerada quando modifica atributos relevantes do risco existente, nomeadamente:

- Introdução de nova superfície de exposição ou integração externa;
- Tratamento adicional de dados pessoais, regulados, segredos ou informação confidencial;
- Aumento de delegação, alcance ou velocidade de decisões com impacto real.

Sempre que qualquer uma destas condições se verifique, a equipa deve ajustar os eixos afetados e registar explicitamente o racional da decisão.

---

## 4. Momentos obrigatórios de aplicação

| Momento | Obrigatoriedade |
|---|:---:|
| Início de novo projeto ou produto | Obrigatório |
| Antes do primeiro deployment em produção (go-live) | Obrigatório |
| Após alteração significativa de arquitetura | Obrigatório |
| Após nova integração externa ou exposição adicional | Obrigatório |
| Após alteração do tipo ou volume de dados tratados | Obrigatório |
| Revisão periódica com cadência definida | Obrigatório |
| Após incidente de segurança relevante | Obrigatório |

---

## 5. Cadência de revisão periódica

A classificação deve ser reavaliada com cadência mínima definida por nível:

| Nível | Cadência mínima |
|---|---|
| L1 | Anual (12 meses) |
| L2 | Semestral (6 meses) |
| L3 | Trimestral (3 meses) |

Cada reavaliação deve documentar:

- [ ] Reavaliação dos três eixos E, D e I com base no estado atual da aplicação
- [ ] Decisão: manter nível / alterar nível (com justificação técnica)
- [ ] Data da próxima revisão agendada
- [ ] Aprovação pelo AppSec Engineer responsável

---

## 6. Processo de classificação

### 6.1 Passos obrigatórios

1. **Aplicar o modelo E+D+I** - avaliar cada eixo com base nos critérios definidos na secção 3
2. **Determinar o nível global** - L1, L2 ou L3, com base na pontuação combinada
3. **Documentar o racional** - registar os critérios que determinaram cada eixo e o nível final
4. **Obter validação** - revisão e aprovação por AppSec Engineer
5. **Registar formalmente** - documento de classificação versionado, com data e responsável
6. **Comunicar às equipas** - o nível determina os controlos obrigatórios a aplicar em todos os capítulos SbD-ToE

### 6.2 Aprovações por nível

| Nível | Aprovação mínima requerida |
|---|---|
| L1 | Tech Lead ou AppSec Engineer |
| L2 | AppSec Engineer |
| L3 | AppSec Engineer + CISO ou equivalente |

---

## 7. Registo formal e rastreabilidade

Toda a classificação e respetiva reavaliação deve ser:

- Registada em documento versionado, identificado por aplicação
- Associada à data de classificação e ao responsável pela aprovação
- Acessível para consulta por AppSec, GRC e auditores
- Atualizada sempre que o nível for alterado, com histórico preservado

**Artefacto principal:** `risk-classification.md` (ou equivalente no repositório do projeto ou plataforma GRC da organização)

---

## 8. Implicações da classificação

O nível de risco atribuído determina diretamente:

- Os **capítulos SbD-ToE ativos** e os controlos obrigatórios a aplicar
- As **políticas organizacionais aplicáveis** e o seu grau de obrigatoriedade
- Os **artefactos de segurança** que devem ser produzidos e mantidos
- As **cadências de revisão e testes de segurança** exigidas
- As **alçadas de aprovação** para exceções, deploys e alterações de risco

:::warning
Uma classificação incorreta ou desatualizada invalida a proporcionalidade de todos os controlos aplicados. A manutenção ativa da classificação é uma responsabilidade contínua da equipa, não um ato pontual de onboarding.
:::

---

## 9. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Tech Lead / Team Lead | Iniciar o processo de classificação no arranque do projeto |
| AppSec Engineer | Validar e aprovar a classificação; conduzir reavaliações periódicas |
| Developer | Notificar alterações técnicas com impacto potencial nos eixos E, D ou I |
| GRC / Compliance | Garantir que todas as aplicações têm classificação registada e atualizada |
| CISO | Aprovação de classificações L3; supervisão do programa de classificação |
| Gestão de Produto | Informar sobre alterações de negócio com impacto nos eixos |

---

## 10. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Alteração do modelo de classificação SbD-ToE
- Alteração regulatória que introduza novos critérios de risco
- Incidente que evidencie lacuna no modelo de classificação

A evidência de aplicação desta política (documentos de classificação, histórico de reavaliações, aprovações) deve ser auditável por funções de GRC e por auditores externos.

---

## 11. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 01 - Classificação de Aplicações | Modelo E+D+I, critérios de nível, user stories de classificação |
| SbD-ToE Cap. 14 - Governança e Contratação | Alçadas de aprovação, rastreabilidade organizacional |
| ISO/IEC 27001 - Cláusula 6.1 | Avaliação e tratamento de risco |
| NIST SP 800-30 | Guide for Conducting Risk Assessments |
| OWASP Risk Rating Methodology | Critérios de avaliação de risco aplicacional |
| SSDF PW.1 | Definição de requisitos de segurança baseada em risco |
