---
id: kpis-metricas-classificacao
title: KPIs e Métricas - Classificação de Aplicações
sidebar_position: 12
description: Indicadores técnicos e de processo para avaliação da qualidade, cobertura e actualidade da classificação de risco de aplicações, com thresholds por nível de risco e mapeamento para dimensões transversais de governação SbD-ToE.
tags: [kpi, metricas, CLA, classificacao, risco, L1, L2, L3]
---

<!--template: sbdtoe-addon -->

# KPIs e Métricas - Classificação de Aplicações

## Âmbito e propósito

Os indicadores deste domínio avaliam a **qualidade, cobertura e actualidade do processo de classificação de risco de aplicações**. A classificação é o ponto de partida de todo o modelo SbD-ToE: sem uma classificação correcta, os requisitos aplicados são os errados, as excepções têm alçadas inadequadas, e os controlos não são proporcionais ao risco real.

A classificação não é um evento único - é um processo contínuo que deve reflectir alterações arquitecturais, regulatórias ou funcionais. Um sistema classificado como L1 que evoluiu para processar dados pessoais de grande escala e nunca foi reclassificado não é um sistema L1: é um sistema L3 com controlos de L1.

Os indicadores CLA alimentam as dimensões transversais **T-01 (Cobertura de controlos)** e **T-06 (Maturidade SbD-ToE)**.

---

## Denominador e fundação de portfólio

Os indicadores CLA são a **origem do denominador** de todos os KPIs de domínio do programa SbD-ToE. CLA-K01 estabelece F-02 - o inventário de aplicações classificadas por nível de risco que serve de denominador partilhado a todos os capítulos. Sem CLA-K01 completo e actualizado, as percentagens dos outros capítulos não têm base interpretável.

A relação é directa: F-01 (inventário total) e F-02 (classificadas por nível) são métricas absolutas que precedem qualquer percentagem de domínio. Ver `kpis-governanca.md` - secção "Fundação de portfólio".

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
| Qt | Quantitativo temporal (dias) |
| Bin | Binário - existência verificável com evidência obrigatória |

---

## Catálogo de indicadores

| ID | Indicador | Tipo | L1 | L2 | L3 | Dim. T | Período |
|----|-----------|:----:|:--:|:--:|:--:|:------:|---------|
| CLA-K01 | % aplicações do portfólio com classificação de risco formal documentada e acessível | Q% | 100% | 100% | 100% | T-01 | Trimestral |
| CLA-K02 | % classificações revistas dentro do ciclo definido por nível (L3: trimestral; L2: semestral; L1: anual) | Q% | ≥ 90% | ≥ 95% | 100% | T-01 | Por ciclo |
| CLA-K03 | % aplicações com alteração significativa (arquitectura, dados, regulação) cuja classificação foi actualizada em ≤ 30 dias | Q% | ≥ 80% | ≥ 95% | 100% | T-01 | Por evento |
| CLA-K04 | % classificações de sistemas L2/L3 validadas por AppSec ou GRC (não apenas auto-avaliação do owner) | Q% | - | ≥ 90% | 100% | T-01 | Semestral |
| CLA-K05 | % aplicações com risco residual formalmente documentado e aceite pelo owner com autoridade proporcional | Q% | - | ≥ 85% | 100% | T-01 | Semestral |
| CLA-K06 | # aplicações classificadas como L1 sem revisão nos últimos 12 meses e com mudança funcional significativa registada | Q# ↓ | = 0 | = 0 | = 0 | T-01 | Semestral |

---

## Definições complementares

**CLA-K01 - Classificação documentada:** considera-se documentada uma classificação que inclui: (a) nível de risco atribuído (L1/L2/L3); (b) critérios que determinaram o nível (tipo de dados, exposição, criticidade); (c) owner responsável pela classificação; (d) data de última revisão. Classificações informais ou verbais não satisfazem este critério.

**CLA-K02 - Ciclos de revisão por nível:**
- L3: revisão trimestral ou por cada release major, o que ocorrer primeiro
- L2: revisão semestral ou por cada release major que altere a superfície de ataque
- L1: revisão anual ou após qualquer alteração funcional significativa

**CLA-K03 - Alteração significativa:** inclui qualquer das seguintes: (a) introdução de novos tipos de dados pessoais ou sensíveis; (b) integração com novos sistemas externos ou de terceiros; (c) mudança de arquitectura com impacto na superfície de ataque; (d) alteração do contexto regulatório aplicável; (e) incidente de segurança que revele subestimação de risco.

**CLA-K04 - Validação por AppSec/GRC:** a validação pode ser realizada em revisão formal, em processo de onboarding de aplicação, ou em ciclo de auditoria. O critério é a existência de um segundo par de olhos com competência e independência relativamente ao owner da aplicação.

**CLA-K05 - Risco residual aceite:** o risco residual é o risco remanescente após aplicação dos controlos. A sua aceitação formal requer: identificação dos requisitos não aplicados ou parcialmente aplicados, justificação, compensações, e aprovação pelo owner com alçada proporcional ao nível de risco (ver Cap. 14 `addon/12-processo-excecoes.md`).

**CLA-K06 - Subclassificação não detectada:** este indicador destina-se a detectar situações em que uma aplicação L1 evoluiu funcionalmente sem reclassificação. A detecção pode ser baseada em: auditoria de changelog, revisão de tickets de produto, ou análise de integração com novos sistemas.

---

## Recolha e instrumentação

| Indicador | Fonte primária | Suporte de instrumentação | Automação |
|-----------|---------------|--------------------------|-----------|
| CLA-K01 | Inventário de aplicações / CMDB / GRC | Registo centralizado de aplicações | Parcial |
| CLA-K02 | Registo de classificações + datas de revisão | GRC com alertas de expiração de revisão | Parcial |
| CLA-K03 | Sistema de change management + registo de classificações | Correlação entre tickets de mudança e data de reclassificação | Não |
| CLA-K04 | Registo de revisões com identificação de validador | GRC + registo de aprovação | Não |
| CLA-K05 | Registo de risco residual por aplicação | GRC / repositório de decisões de risco | Não |
| CLA-K06 | Inventário de aplicações L1 + log de mudanças funcionais | Auditoria cruzada entre CMDB e changelog | Não |

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| `addon/01-modelo-classificacao-eixos.md` | Modelo e critérios de classificação que fundamentam CLA-K01/K03 |
| `addon/04-risco-residual.md` | Processo de documentação de risco residual (CLA-K05) |
| `addon/02-ciclo-vida-risco.md` | Ciclos de revisão que definem os thresholds de CLA-K02 |
| Cap. 14 `addon/12-processo-excecoes.md` | Aceitação de risco residual (CLA-K05) |
| Cap. 14 `addon/kpis-governanca.md` | Dimensões transversais T-01, T-06 |
