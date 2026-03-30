---
id: kpis-metricas-threat-modeling
title: KPIs e Métricas - Threat Modeling
sidebar_position: 11
description: Indicadores técnicos e de processo para avaliação da cobertura, qualidade e integração do threat modeling no ciclo de desenvolvimento, com thresholds por nível de risco e mapeamento para dimensões transversais de governação SbD-ToE.
tags: [kpi, metricas, THR, threat-modeling, ameacas, L1, L2, L3]
---

<!--template: sbdtoe-addon -->

# KPIs e Métricas - Threat Modeling

## Âmbito e propósito

Os indicadores deste domínio avaliam a **cobertura, actualidade e qualidade operacional do processo de threat modeling** no ciclo de desenvolvimento de software. O threat modeling é o mecanismo pelo qual as ameaças são identificadas antes de se tornarem vulnerabilidades exploráveis - é análise estruturada de risco aplicada à arquitectura, antes da implementação.

A medição de threat modeling enfrenta um desafio específico: a qualidade de um threat model não é directamente observável por métricas quantitativas simples. Um threat model extenso pode ser superficial; um threat model conciso pode ser exaustivo. Os indicadores THR combinam métricas de cobertura (quantitativas) com indicadores de qualidade de processo (ordinais e binários) que são observáveis sem requerer avaliação subjectiva linha a linha.

Os indicadores THR alimentam as dimensões transversais **T-01 (Cobertura de controlos)** e **T-06 (Maturidade SbD-ToE)**.

---

## Denominador e fundação de portfólio

Os indicadores THR usam como denominador **F-02 - aplicações com classificação de risco formal** (Cap. 01, CLA-K01). As percentagens deste capítulo são interpretáveis apenas em relação ao conjunto de aplicações classificadas ao nível de risco relevante - não em relação ao portfólio total ou a subconjuntos ad-hoc.

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
| Ord | Qualitativo ordinal (nível 1–3) |
| Bin | Binário - existência verificável com evidência obrigatória |

---

## Catálogo de indicadores

| ID | Indicador | Tipo | L1 | L2 | L3 | Dim. T | Período |
|----|-----------|:----:|:--:|:--:|:--:|:------:|---------|
| THR-K01 | % aplicações L2/L3 com threat model documentado, actualizado e acessível | Q% | - | ≥ 85% | 100% | T-01 | Semestral |
| THR-K02 | % ameaças identificadas no threat model com controlo associado ou risco aceite formalmente | Q% | - | ≥ 90% | 100% | T-01 | Por threat model |
| THR-K03 | % threat models de sistemas L2/L3 revistos por AppSec antes de entrada em produção | Q% | - | ≥ 80% | 100% | T-01 | Por release major |
| THR-K04 | % threat models actualizados em ≤ 30 dias após alteração arquitectural significativa | Q% | - | ≥ 85% | 100% | T-01 | Por evento |
| THR-K05 | % ameaças identificadas em threat model mapeadas a requisitos canónicos SbD-ToE | Q% | - | ≥ 70% | ≥ 90% | T-01 | Por threat model |
| THR-K06 | Nível de maturidade do processo de threat modeling (metodologia, integração, ferramentas) | Ord | nível 1 | nível 2 | nível 3 | T-06 | Anual |

---

## Definições complementares

**THR-K01 - Threat model actualizado:** considera-se actualizado um threat model que reflecte a arquitectura actual e foi revisto após a última mudança arquitectural significativa ou no prazo máximo do ciclo definido. A ferramenta é livre (STRIDE manual, IriusRisk, Threat Dragon, Microsoft Threat Modeling Tool); a evidência de revisão é obrigatória.

**THR-K02 - Controlo associado ou risco aceite:** cada ameaça deve ter uma disposição explícita - (a) controlo implementado com referência ao requisito; (b) mitigação em curso com prazo; ou (c) risco aceite formalmente com owner e registo. Ameaças sem disposição são lacunas de processo, não posições de risco consciente.

**THR-K03 - Revisão por AppSec:** a revisão pode ser realizada como parte de um security design review, de uma revisão de ADR, ou de um processo formal de threat model review. O critério é a existência de um revisor com competência de segurança independente do team que produziu o threat model.

**THR-K04 - Alteração arquitectural significativa:** inclui as mesmas categorias definidas em CLA-K03 (Cap. 01): novos tipos de dados, novas integrações externas, mudança de arquitectura com impacto na superfície de ataque, alteração regulatória. O prazo de 30 dias é para actualização do threat model, não para resolução das ameaças identificadas.

**THR-K05 - Mapeamento a requisitos canónicos:** uma ameaça está mapeada quando é possível traçar a linha entre a ameaça identificada e o requisito SbD-ToE que a mitiga (ex: ameaça de privilege escalation → AUT-003, AUT-007). O mapeamento pode ser automático (IriusRisk) ou manual documentado. Ameaças sem mapeamento indicam potencial lacuna de cobertura de requisitos.

**THR-K06 - Níveis de maturidade de threat modeling:**
- Nível 1: threat modeling realizado de forma ad-hoc, sem metodologia definida, sem integração no ciclo de desenvolvimento
- Nível 2: metodologia definida (STRIDE, PASTA, ou outra), realizado em novos sistemas e mudanças significativas, com output documentado e revisto por AppSec
- Nível 3: integrado no pipeline de desenvolvimento (idealmente contínuo ou por PR/release), com mapeamento automático a requisitos, rastreabilidade de ameaças ao longo do tempo, e evidência de evolução comparada com ciclos anteriores

---

## Recolha e instrumentação

| Indicador | Fonte primária | Ferramentas de referência | Automação |
|-----------|---------------|--------------------------|-----------|
| THR-K01 | Repositório de threat models (wiki, Git, ferramenta dedicada) | IriusRisk, Threat Dragon, Microsoft TMT | Parcial |
| THR-K02 | Threat model com coluna de disposição por ameaça | Qualquer ferramenta com tracking de ameaças + mitigações | Parcial |
| THR-K03 | Registo de revisões (tickets, comentários, actas) | Sistema de tickets + registo de revisão | Não |
| THR-K04 | Correlação entre log de mudanças e data de revisão do threat model | Auditoria de git log vs data de threat model | Não |
| THR-K05 | Threat model com campo de requisito por ameaça | IriusRisk (mapeamento automático), ou tabela manual | Parcial |
| THR-K06 | Avaliação qualitativa por AppSec ou arquitecto de segurança | Avaliação estruturada anual | Não |

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| `addon/01-metodologias-e-ferramentas.md` | Metodologias e ferramentas que fundamentam THR-K06 |
| `addon/03-validacao-evidencia-threat-modeling.md` | Processo de validação que alimenta THR-K03/K05 |
| `addon/07-mapeamento-threats-requisitos.md` | Mapeamento ameaça → requisito (THR-K05) |
| Cap. 04 `addon/10-kpis-metricas.md` | ARC-K01 (threat model por arquitectura) complementa THR-K01 |
| Cap. 14 `addon/kpis-governanca.md` | Dimensões transversais T-01, T-06 |
