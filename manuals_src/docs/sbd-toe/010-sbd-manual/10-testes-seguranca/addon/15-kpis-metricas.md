---
id: kpis-metricas-testes
title: KPIs e Métricas - Testes de Segurança
sidebar_position: 15
description: Indicadores técnicos e operacionais para avaliação da eficácia do programa de testes de segurança, com thresholds por nível de risco e mapeamento para dimensões transversais de governação SbD-ToE.
tags: [kpi, metricas, TST, testes, sast, dast, pentest, findings, regressao, L1, L2, L3]
---

<!--template: sbdtoe-addon -->

# KPIs e Métricas - Testes de Segurança

## Âmbito e propósito

Os indicadores deste domínio avaliam a **eficácia, cobertura e maturidade do programa de testes de segurança**: a cobertura por tipo de teste (SAST, DAST, pentest), a velocidade de resolução de findings dentro dos SLAs definidos, a centralização da gestão de findings, e a taxa de regressão como proxy de qualidade do processo de remediação.

Os testes de segurança não produzem segurança - produzem visibilidade. O valor dos indicadores deste domínio reside na sua capacidade de revelar lacunas no que é testado, na forma como os resultados são tratados, e na consistência da resposta ao longo do tempo. Um programa de testes com boa cobertura mas com taxa de regressão elevada indica um processo de remediação estruturalmente deficiente.

Os indicadores TST alimentam as dimensões transversais **T-01 (Cobertura de controlos)** e **T-03 (Velocidade de resolução)**.

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
| Qt | Quantitativo temporal (dias) |

---

## Catálogo de indicadores

| ID | Indicador | Tipo | L1 | L2 | L3 | Dim. T | Período |
|----|-----------|:----:|:--:|:--:|:--:|:------:|---------|
| TST-K01 | % aplicações com SAST activo e executado em cada build/PR | Q% | ≥ 70% | ≥ 95% | 100% | T-01 | Mensal |
| TST-K02 | % aplicações L2/L3 com DAST executado por release (ou equivalente de cobertura dinâmica) | Q% | - | ≥ 80% | 100% | T-01 | Por release |
| TST-K03 | % findings críticos resolvidos dentro de SLA TST-003 (por severidade e nível) | Q% | ≥ 70% | ≥ 85% | ≥ 98% | T-03 | Por release |
| TST-K04 | % findings críticos/altos em regressão - vulnerabilidade declarada resolvida que reaparece em 90 dias | Q% ↓ | - | ≤ 5% | ≤ 2% | T-03 | Trimestral |
| TST-K05 | % findings reportados centralizados em plataforma de gestão (vs dispersos em ferramentas individuais) | Q% | ≥ 60% | ≥ 90% | 100% | T-01 | Mensal |
| TST-K06 | % aplicações L3 com pentest externo realizado no último ano (ou por release major) | Q% | - | - | 100% | T-01 | Anual |
| TST-K07 | # falsos positivos confirmados por triagem formal vs total de findings reportados (taxa de ruído) | Q% ↓ | - | ≤ 30% | ≤ 15% | T-01 | Trimestral |

---

## Definições complementares

**TST-K03 - SLA por severidade e nível (referência TST-003):**

| Severidade | L1 | L2 | L3 |
|------------|:--:|:--:|:--:|
| Crítico (CVSS ≥ 9.0) | 30 dias | 14 dias | 7 dias |
| Alto (CVSS 7.0–8.9) | 90 dias | 30 dias | 14 dias |
| Médio (CVSS 4.0–6.9) | - | 90 dias | 60 dias |

Findings com excepção formal activa são excluídos do cálculo de TST-K03 mas registados separadamente.

**TST-K04 - Regressão:** um finding é classificado como regressão se: (a) foi marcado como resolvido no sistema de gestão de findings; (b) reaparece na mesma localização (ficheiro + linha ± 10 linhas) ou no mesmo endpoint/parâmetro; (c) dentro de 90 dias após resolução declarada. A taxa de regressão é um indicador da qualidade do processo de remediação, não da qualidade do scanner.

**TST-K05 - Centralização:** considera-se centralizado um finding que está registado, com estado actualizado, numa plataforma de gestão (DefectDojo, Vulcan Cyber, Security Hub, ou equivalente) e associado à aplicação, versão e responsável. Findings apenas em relatórios PDF, emails ou backlog não estruturado não satisfazem este critério.

**TST-K06 - Pentest externo:** deve ser realizado por entidade externa à organização (não apenas por equipa interna), com âmbito documentado, metodologia formal (PTES, OWASP Testing Guide, TIBER-EU para sectores regulados), e relatório com findings rastreáveis. TLPT (Threat-Led Penetration Testing) satisfaz este critério para sectores com obrigação DORA.

**TST-K07 - Taxa de ruído:** um falso positivo é confirmado quando o processo formal de triagem (com analista de segurança) classifica o finding como irrelevante para o contexto da aplicação. Falsos positivos não triados não entram neste cálculo. Uma taxa de ruído elevada indica necessidade de ajuste nas regras de detecção, não ausência de vulnerabilidades.

---

## Recolha e instrumentação

| Indicador | Fonte primária | Ferramentas de referência | Automação |
|-----------|---------------|--------------------------|-----------|
| TST-K01 | Configuração de pipeline + resultados SAST | SonarQube, Semgrep, CodeQL | Sim |
| TST-K02 | Logs de pipeline + resultados DAST | OWASP ZAP, Burp Suite Enterprise, Nuclei | Parcial |
| TST-K03 | Plataforma de gestão de findings + timestamps | DefectDojo (SLA tracking) | Sim |
| TST-K04 | Histórico de findings na plataforma de gestão | DefectDojo (re-open tracking) | Sim |
| TST-K05 | Auditoria de plataformas de findings vs relatórios de ferramentas | Contagem de findings por fonte vs plataforma central | Parcial |
| TST-K06 | Registo de pentests (contrato, relatório, data) | Manual - registo GRC ou repositório de relatórios | Não |
| TST-K07 | Plataforma de gestão com campo de triagem | DefectDojo (false positive flag + triagem documentada) | Parcial |

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| `addon/00-catalogo-requisitos.md` | Requisitos TST-001..010 que fundamentam os indicadores |
| `addon/08-gestao-findings.md` | Processo de centralização (TST-K05) e triagem (TST-K07) |
| `addon/05-validacao-regressao.md` | Metodologia de detecção de regressões (TST-K04) |
| Cap. 14 `addon/kpis-governanca.md` | Dimensões transversais T-01, T-03 |
