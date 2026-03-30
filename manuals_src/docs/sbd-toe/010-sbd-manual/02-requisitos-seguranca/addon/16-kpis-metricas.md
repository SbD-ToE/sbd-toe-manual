---
id: kpis-metricas-requisitos
title: KPIs e Métricas - Requisitos de Segurança
sidebar_position: 16
description: Indicadores técnicos e de processo para avaliação da cobertura, rastreabilidade e validação efectiva dos requisitos de segurança aplicados por nível de risco, com mapeamento para dimensões transversais de governação SbD-ToE.
tags: [kpi, metricas, RQS, requisitos, rastreabilidade, cobertura, L1, L2, L3]
---

<!--template: sbdtoe-addon -->

# KPIs e Métricas - Requisitos de Segurança

## Âmbito e propósito

Os indicadores deste domínio avaliam a **aplicação efectiva, rastreabilidade e validação dos requisitos de segurança** definidos no catálogo SbD-ToE. O catálogo de requisitos é o elo entre a classificação de risco (Cap. 01) e os controlos técnicos implementados nos capítulos de domínio (Cap. 04–12). Sem este elo, os domínios técnicos funcionam sem referência normativa, e a governação não tem base para avaliar conformidade.

O risco específico deste domínio é a conformidade declarativa: uma aplicação pode listar os requisitos aplicados sem que estes estejam efectivamente implementados ou validados. Os indicadores RQS medem não apenas a declaração, mas a evidência de validação.

Os indicadores RQS alimentam as dimensões transversais **T-01 (Cobertura de controlos)** e **T-06 (Maturidade SbD-ToE)**.

---

## Denominador e fundação de portfólio

Os indicadores RQS usam como denominador **F-02 - aplicações com classificação de risco formal**, definido em Cap. 01 (`addon/12-kpis-metricas.md`, CLA-K01). RQS-K01 estabelece F-03 - aplicações com requisitos mapeados - que por sua vez é o denominador da camada seguinte do funil de adoptabilidade SbD-ToE.

A interpretação de qualquer percentagem RQS pressupõe que F-02 está completo para o nível de risco em questão. Ver `kpis-governanca.md` - secção "Fundação de portfólio".

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

---

## Catálogo de indicadores

| ID | Indicador | Tipo | L1 | L2 | L3 | Dim. T | Período |
|----|-----------|:----:|:--:|:--:|:--:|:------:|---------|
| RQS-K01 | % aplicações com requisitos de segurança formalmente mapeados ao nível de risco classificado | Q% | ≥ 80% | ≥ 95% | 100% | T-01 | Semestral |
| RQS-K02 | % requisitos obrigatórios por nível com evidência de implementação ou excepção formal documentada | Q% | ≥ 70% | ≥ 90% | ≥ 98% | T-01 | Por release |
| RQS-K03 | % requisitos aplicados com rastreabilidade completa (requisito → controlo implementado → evidência de teste) | Q% | - | ≥ 75% | ≥ 95% | T-01 | Semestral |
| RQS-K04 | % aplicações L2/L3 com validação formal de requisitos realizada no último ciclo de release | Q% | - | ≥ 85% | 100% | T-01 | Por release |
| RQS-K05 | % requisitos com critério de aceitação verificado (testado ou auditado) vs apenas declarado como aplicado | Q% | - | ≥ 70% | ≥ 90% | T-01 | Semestral |
| RQS-K06 | # requisitos obrigatórios para o nível de risco sem implementação e sem excepção formal (lacunas não governadas) | Q# ↓ | = 0 | = 0 | = 0 | T-01 | Por release |

---

## Definições complementares

**RQS-K01 - Mapeamento formal:** considera-se formal um mapeamento que identifica, por aplicação: (a) o nível de risco classificado; (b) os requisitos obrigatórios para esse nível em cada domínio relevante; (c) o estado de cada requisito (aplicado, excepcionado, não aplicável com justificação). Tabelas de requisitos sem estado actualizado não satisfazem este critério.

**RQS-K02 - Evidência de implementação:** a evidência pode ser técnica (resultado de scanner, log de validação, output de pipeline) ou processual (registo de revisão, checklist de release, resultado de auditoria). A evidência deve ser rastreável ao requisito específico, não genérica à aplicação.

**RQS-K03 - Rastreabilidade completa:** a cadeia requisito → controlo → evidência está completa quando é possível partir de um requisito canónico (ex: AUT-003) e chegar à evidência concreta de que está implementado na aplicação em questão. Rastreabilidade parcial (requisito declarado mas sem controlo identificado) não satisfaz este critério.

**RQS-K04 - Validação de ciclo:** a validação formal de requisitos deve ser um evento explícito no processo de release, com output documentado. Pode ser integrada em checklist de release, em revisão de AppSec, ou em pipeline automatizado com relatório. Validação implícita ("corre o CI, portanto está validado") não satisfaz este critério sem rastreabilidade explícita ao requisito.

**RQS-K05 - Critério verificado vs declarado:** um requisito está "verificado" quando o critério de aceitação definido no catálogo foi avaliado com evidência (teste, scan, auditoria). Está "declarado" quando o owner afirma que está aplicado sem evidência rastreável. RQS-K05 mede a proporção de requisitos no estado verificado vs o total de requisitos declarados como aplicados.

**RQS-K06 - Lacuna não governada:** um requisito é uma lacuna não governada quando é obrigatório para o nível de risco da aplicação, não está implementado, e não tem excepção formal activa. Esta situação equivale a uma não conformidade activa e deve ser tratada com o mesmo SLA de um finding crítico.

---

## Recolha e instrumentação

| Indicador | Fonte primária | Suporte de instrumentação | Automação |
|-----------|---------------|--------------------------|-----------|
| RQS-K01 | Registo de requisitos por aplicação (GRC, wiki, ALM) | Matriz de requisitos por aplicação | Parcial |
| RQS-K02 | Registo de requisitos + evidências + registo de excepções | GRC integrado com pipeline e gestão de findings | Parcial |
| RQS-K03 | Sistema de rastreabilidade (ALM, wiki estruturado) | Auditoria de completude de cadeia | Não |
| RQS-K04 | Registo de releases + checklists de validação | Release log + output de validação | Parcial |
| RQS-K05 | Registo de requisitos com campo de evidência | Auditoria de campo "evidência" vs "declarado" | Não |
| RQS-K06 | Registo de requisitos + registo de excepções activas | Cruzamento automático entre catálogo e estado por aplicação | Parcial |

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| `addon/02-lista-requisitos-base.md` | Catálogo canónico e mapeamento de prefixos por domínio |
| `addon/03-taxonomia-rastreabilidade.md` | Modelo de rastreabilidade que fundamenta RQS-K03 |
| `addon/07-validacao-requisitos.md` | Processo de validação de requisitos (RQS-K04/K05) |
| `addon/08-gestao-excecoes.md` | Requisitos excepcionados (RQS-K02, RQS-K06) |
| Cap. 14 `addon/kpis-governanca.md` | Dimensões transversais T-01, T-06 |
