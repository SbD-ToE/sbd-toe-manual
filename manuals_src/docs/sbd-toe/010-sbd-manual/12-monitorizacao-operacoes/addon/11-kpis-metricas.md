---
id: kpis-metricas-operacoes
title: KPIs e Métricas - Monitorização e Operações
sidebar_position: 11
description: Indicadores técnicos e operacionais para avaliação da eficácia do programa de monitorização de segurança, com thresholds por nível de risco e mapeamento para dimensões transversais de governação SbD-ToE.
tags: [kpi, metricas, OPS, monitorizacao, SIEM, alertas, MTTD, MTTR, logging, L1, L2, L3]
---

<!--template: sbdtoe-addon -->

# KPIs e Métricas - Monitorização e Operações

## Âmbito e propósito

Os indicadores deste domínio avaliam a **eficácia operacional do programa de monitorização de segurança**: a cobertura de logging centralizado, a qualidade dos alertas, a velocidade de detecção e resposta, e a capacidade de correlação entre fontes. Este domínio opera sobre dados produzidos por todos os outros capítulos - os logs gerados pelo código (Cap. 06), pelo pipeline (Cap. 07), pelos containers (Cap. 09) e pela infraestrutura (Cap. 08) convergem aqui e são avaliados pela sua utilidade operacional.

> Este ficheiro é o **catálogo canónico** de `OPS-Kxx`. O ficheiro [`07-metricas-indicadores.md`](./07-metricas-indicadores.md) é uma síntese operacional mais leve para uso quotidiano.

A distinção central deste domínio: os requisitos `LOG-` (Cap. 02) definem o que o software deve registar; os indicadores `OPS-K` medem se esses registos são centralizados, analisados e accionados com eficácia. Um sistema com logging perfeito mas sem correlação, alertas ou resposta tem visibilidade zero do ponto de vista operacional.

Os indicadores OPS alimentam a dimensão transversal **T-03 (Velocidade de resolução)** - especificamente MTTD e MTTR operacionais.

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
| Qt | Quantitativo temporal (horas/minutos) |

---

## Catálogo de indicadores

| ID | Indicador | Tipo | L1 | L2 | L3 | Dim. T | Período |
|----|-----------|:----:|:--:|:--:|:--:|:------:|---------|
| OPS-K01 | % aplicações de produção com logging de eventos de segurança centralizado em SIEM ou equivalente | Q% | ≥ 60% | ≥ 90% | 100% | T-03 | Mensal |
| OPS-K02 | % alertas de segurança com threshold definido, testado e documentado (sem alertas por omissão ou não calibrados) | Q% | ≥ 50% | ≥ 80% | ≥ 95% | T-03 | Trimestral |
| OPS-K03 | MTTD - tempo médio desde ocorrência de evento de segurança até geração de alerta | Qt | ≤ 24h | ≤ 4h | ≤ 30min | T-03 | Mensal |
| OPS-K04 | MTTR - tempo médio desde geração de alerta até início de acção de mitigação | Qt | ≤ 48h | ≤ 4h | ≤ 1h | T-03 | Mensal |
| OPS-K05 | % alertas disparados que resultam em falso positivo (taxa de ruído) | Q% ↓ | ≤ 50% | ≤ 30% | ≤ 15% | T-03 | Mensal |
| OPS-K06 | % eventos de segurança críticos com cobertura de correlação entre pelo menos duas fontes distintas | Q% | - | ≥ 70% | ≥ 95% | T-03 | Trimestral |
| OPS-K07 | % incidentes de segurança com processo formal de resposta (IRP) activado e rastreável | Q% | ≥ 80% | 100% | 100% | T-03 | Por incidente |
| OPS-K08 | % logs de sistemas L2/L3 retidos dentro do período mínimo obrigatório por política e regulação aplicável | Q% | ≥ 80% | 100% | 100% | T-03 | Semestral |

---

## Definições complementares

**OPS-K01 - Logging centralizado:** considera-se centralizado o envio de eventos de segurança para um sistema de recolha central (SIEM, plataforma de log aggregation) com retenção, indexação e capacidade de consulta. Logging local sem forwarding não satisfaz este critério.

**OPS-K02 - Alerta testado:** um alerta está testado quando existe evidência de que o seu threshold foi validado em ambiente real ou simulado, e produz o comportamento esperado (alerta verdadeiro positivo com contexto suficiente para triagem). Alertas gerados por defaults de ferramenta sem revisão e calibração não satisfazem este critério.

**OPS-K03 - MTTD (Mean Time to Detect):** medido como `timestamp_alerta − timestamp_evento`. Para eventos que não geram alerta imediato (detecção por correlação ou análise periódica), o timestamp de detecção é o momento em que um analista toma conhecimento do evento. Eventos sem registo de timestamp de ocorrência não podem ser incluídos no cálculo - a sua ausência é em si um indicador de gap de logging.

**OPS-K04 - MTTR (Mean Time to Respond):** medido como `timestamp_primeira_acção − timestamp_alerta`. A primeira acção inclui: isolamento, bloqueio, escalonamento formal, ou activação de runbook. Tempo de análise antes da primeira acção conta para o MTTR.

**OPS-K05 - Taxa de ruído:** um falso positivo é um alerta que, após triagem formal por analista, é classificado como irrelevante para o contexto de segurança. A taxa de ruído elevada tem dois efeitos: (a) consome capacidade de resposta; (b) cria dessensibilização aos alertas, aumentando o risco de ignorar verdadeiros positivos. A calibração de alertas é o mecanismo de controlo.

**OPS-K06 - Correlação entre fontes:** eventos críticos (autenticação anómala, exfiltração de dados, escalada de privilégios) ganham contexto e reduzem falsos positivos quando correlacionados entre, por exemplo: logs de autenticação + logs de rede + logs de aplicação. A cobertura mínima para L3 deve incluir correlação entre endpoint, rede e aplicação.

**OPS-K07 - IRP activado:** o processo formal de resposta a incidentes (Incident Response Plan) está activado quando existe um ticket ou registo com: classificação do incidente, owner de resposta, timeline de acções, e estado de resolução. Incidentes resolvidos informalmente sem registo não satisfazem este critério.

**OPS-K08 - Retenção conforme regulação:** o período mínimo aplicável depende da regulação sectorial. Referência base: DORA exige 2 anos para logs de ICT; NIS2 não define período mas exige disponibilidade para auditoria. Sistemas sem classificação regulatória aplicam a política interna - mínimo 90 dias para L1, 1 ano para L2, 2 anos para L3.

---

## Thresholds de MTTD/MTTR por nível - resumo

| Métrica | L1 | L2 | L3 |
|---------|:--:|:--:|:--:|
| MTTD (detecção) | ≤ 24h | ≤ 4h | ≤ 30min |
| MTTR (resposta) | ≤ 48h | ≤ 4h | ≤ 1h |

Estes thresholds aplicam a eventos de segurança de severidade alta/crítica. Para eventos de severidade média, os thresholds podem ser 3× superiores. Sectores regulados (financeiro, saúde, infraestruturas críticas) podem ter requisitos mais exigentes por norma sectorial.

---

## Recolha e instrumentação

| Indicador | Fonte primária | Ferramentas de referência | Automação |
|-----------|---------------|--------------------------|-----------|
| OPS-K01 | Inventário de aplicações + configuração de SIEM | SIEM (Splunk, Elastic, Sentinel, QRadar) | Parcial |
| OPS-K02 | Registo de alertas com metadata de calibração | SIEM + documentação de alertas | Não |
| OPS-K03 | Log de eventos + log de alertas com timestamps | SIEM (cálculo automático de MTTD) | Sim |
| OPS-K04 | Log de alertas + log de acções de resposta | SIEM + sistema de IR (PagerDuty, JIRA) | Sim |
| OPS-K05 | Plataforma de IR com classificação de triagem | SIEM + triagem documentada por analista | Parcial |
| OPS-K06 | Configuração de regras de correlação no SIEM | SIEM (contagem de regras com múltiplas fontes) | Parcial |
| OPS-K07 | Base de dados de incidentes | Sistema de IR (ServiceNow, Jira, PagerDuty) | Sim |
| OPS-K08 | Configuração de retenção + inventário de sistemas | Auditoria de política de retenção por fonte | Parcial |

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| `addon/00-catalogo-requisitos.md` | Requisitos OPS-001..010 que fundamentam os indicadores |
| `addon/07-metricas-indicadores.md` | Síntese operacional de MTTD/MTTR para uso quotidiano das equipas |
| `addon/10-excecoes-operacoes.md` | Excepções a alertas e retenção (OPS-K02, OPS-K08) |
| Cap. 14 `addon/kpis-governanca.md` | Dimensão transversal T-03 (velocidade de resolução) |
