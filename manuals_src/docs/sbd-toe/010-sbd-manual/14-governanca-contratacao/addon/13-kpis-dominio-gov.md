---
id: kpis-dominio-governacao
title: KPIs de Domínio - Governação e Contratação
sidebar_position: 13
description: Indicadores técnicos e de processo específicos do domínio de governação organizacional de segurança (GOV), com thresholds por nível de risco e mapeamento para dimensões transversais de governação SbD-ToE.
tags: [kpi, metricas, GOV, governanca, excecoes, ownership, contratos, fornecedores, L1, L2, L3]
---

<!--template: sbdtoe-addon -->

# KPIs de Domínio - Governação e Contratação

## Âmbito e propósito

Os indicadores deste domínio avaliam a **saúde e eficácia da estrutura de governação organizacional de segurança**: a cobertura de ownership por aplicação, a qualidade e validade das excepções activas, a conformidade contratual com fornecedores, e a completude da rastreabilidade organizacional.

O domínio GOV é o único cujos indicadores medem o **processo de governação em si**, não os controlos técnicos que esse processo governa. Um indicador como "% excepções com cadeia de autoridade completa" não mede segurança técnica - mede a disciplina com que a organização gere os desvios à segurança que decidiu aceitar. Essa disciplina é, ela própria, um controlo.

Estes indicadores complementam os KPIs transversais definidos em `kpis-governanca.md` e alimentam directamente as dimensões **T-02 (Saúde de excepções)**, **T-04 (Ownership)** e **T-05 (Cadeia de fornecimento)**.

---

## Denominador e fundação de portfólio

Os indicadores deste domínio usam como denominador **F-02 - aplicações com classificação de risco formal** (Cap. 01, CLA-K01). As percentagens são interpretáveis apenas em relação ao conjunto de aplicações classificadas ao nível de risco relevante - não ao portfólio total ou a subconjuntos ad-hoc.

Ver `kpis-governanca.md` - secção "Fundação de portfólio" - para o funil de adoptabilidade SbD-ToE e a relação entre denominadores.

---

## Convenções

| Símbolo | Significado |
|---------|-------------|
| ✔ | Threshold obrigatório para este nível |
| - | Não aplicável ou não obrigatório a este nível |
| ↓ | Indicador inverso - valor menor indica melhor desempenho |

Os thresholds são cumulativos: L3 inclui todas as obrigações de L1 e L2.

**Tipos de indicador:**

| Código | Significado |
|--------|-------------|
| Q% | Quantitativo percentual |
| Q# | Quantitativo contagem |
| Bin | Binário - existência verificável com evidência obrigatória |

---

## Catálogo de indicadores

| ID | Indicador | Tipo | L1 | L2 | L3 | Dim. T | Período |
|----|-----------|:----:|:--:|:--:|:--:|:------:|---------|
| GOV-K01 | % aplicações com owner de segurança formalmente designado, registado e com formação válida (&lt; 12 meses) | Q% | 100% | 100% | 100% | T-04 | Trimestral |
| GOV-K02 | % excepções activas com cadeia de autoridade completa (quem pediu, quem avaliou, quem aprovou) | Q% | 100% | 100% | 100% | T-02 | Mensal |
| GOV-K03 | % excepções activas com prazo de expiração definido e data de reavaliação agendada | Q% | ≥ 80% | 100% | 100% | T-02 | Mensal |
| GOV-K04 | # excepções expiradas sem renovação formal (devem ser tratadas como não conformidade activa) | Q# ↓ | = 0 | = 0 | = 0 | T-02 | Semanal |
| GOV-K05 | % contratos com fornecedores de sistemas L2/L3 com cláusulas de segurança proporcionais ao risco, assinadas | Q% | ≥ 80% | 100% | 100% | T-05 | Semestral |
| GOV-K06 | % fornecedores L3 com validação de segurança anual concluída e documentada | Q% | - | - | 100% | T-05 | Anual |
| GOV-K07 | % aplicações com rastreabilidade organizacional completa e actualizada (risco → requisitos → excepções → owner) | Q% | - | ≥ 80% | 100% | T-04 | Trimestral |
| GOV-K08 | % desvios identificados em ciclos de validação contínua com acção correctiva atribuída a owner com prazo | Q% | ≥ 80% | 100% | 100% | T-02 | Por ciclo |

---

## Definições complementares

**GOV-K01 - Owner com formação válida:** considera-se formação válida a conclusão de programa de formação em SbD-ToE (ou equivalente organizacional) nos últimos 12 meses. Owners com designação sem formação válida contam para o denominador mas não para o numerador. Rotatividade de equipa é o principal trigger de invalidade.

**GOV-K02 - Cadeia de autoridade completa:** uma excepção tem cadeia de autoridade completa quando o registo identifica explicitamente: (a) quem solicitou a excepção (nome e função); (b) quem realizou a avaliação de risco (nome e função); (c) quem aprovou (nome, função e alçada proporcional ao nível de risco). O suporte documental é livre (ticket, GRC, wiki, ADR) - a rastreabilidade é obrigatória.

**GOV-K03 - Excepção com reavaliação agendada:** a data de reavaliação deve estar registada no sistema de rastreabilidade e deve ser anterior ou igual à data de expiração. Excepções com data de expiração mas sem reavaliação agendada não satisfazem completamente este indicador.

**GOV-K04 - Excepção expirada:** uma excepção é considerada expirada no dia seguinte à sua data de expiração sem renovação formal. Excepções expiradas sem renovação equivalem a não conformidade activa e devem ser tratadas com o mesmo SLA de um finding crítico.

**GOV-K05 - Cláusulas proporcionais ao risco:** a proporcionalidade é avaliada pela correspondência entre o nível de risco da aplicação integrada e as cláusulas aplicadas, conforme definido em `addon/02-clausulas-contratuais.md`. Contratos com cláusulas genéricas sem especificidade de segurança não satisfazem este critério.

**GOV-K07 - Rastreabilidade completa:** considera-se completa quando o registo organizacional (por aplicação) reflecte o estado actual de: (a) classificação de risco; (b) requisitos aplicados por domínio; (c) excepções activas com referência; (d) owner designado e activo. Registos desactualizados há mais de um ciclo de revisão não satisfazem este critério.

**GOV-K08 - Desvio com acção correctiva:** um desvio identificado numa revisão de validação contínua tem acção correctiva atribuída quando existe: ticket ou registo com owner, prazo de resolução, e acompanhamento previsto no ciclo seguinte. Desvios registados sem owner ou prazo não satisfazem este critério.

---

## Recolha e instrumentação

| Indicador | Fonte primária | Suporte de instrumentação | Automação |
|-----------|---------------|--------------------------|-----------|
| GOV-K01 | Registo de owners + registo de formação | GRC, HRIS, plataforma de formação | Parcial |
| GOV-K02 | Sistema de gestão de excepções (GRC, Jira, wiki) | Auditoria de campos obrigatórios | Parcial |
| GOV-K03 | Sistema de gestão de excepções | Alertas automáticos por expiração iminente | Parcial |
| GOV-K04 | Sistema de gestão de excepções + calendário | Scan automático de datas de expiração | Sim |
| GOV-K05 | Repositório de contratos + GRC | Auditoria contratual + checklist de cláusulas | Não |
| GOV-K06 | Registo de validações de fornecedores | GRC + questionários de onboarding | Não |
| GOV-K07 | Registo de rastreabilidade organizacional | Auditoria de completude de campos | Parcial |
| GOV-K08 | Registos de validação contínua + backlog | Ciclos de revisão com tracking de acções | Parcial |

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| `addon/00-catalogo-requisitos.md` | Requisitos GOV-001..012 que fundamentam os indicadores |
| `addon/12-processo-excecoes.md` | Processo canónico de excepções (GOV-K02/K03/K04) |
| `addon/02-clausulas-contratuais.md` | Critérios de proporcionalidade contratual (GOV-K05) |
| `addon/03-modelo-validacao-fornecedores.md` | Validação anual de fornecedores (GOV-K06) |
| `addon/06-validacao-continuada.md` | Ciclos de revisão que produzem desvios (GOV-K08) |
| `addon/kpis-governanca.md` | Dimensões transversais T-02, T-04, T-05 |
