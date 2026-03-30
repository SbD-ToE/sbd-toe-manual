---
id: kpis-metricas-arquitetura
title: KPIs e Métricas - Arquitectura Segura
sidebar_position: 10
description: Indicadores técnicos e de processo para avaliação da eficácia dos controlos de arquitectura segura, com thresholds por nível de risco e mapeamento para dimensões transversais de governação SbD-ToE.
tags: [kpi, metricas, ARC, arquitectura, threat-model, L1, L2, L3]
---

<!--template: sbdtoe-addon -->

# KPIs e Métricas - Arquitectura Segura

## Âmbito e propósito

Os indicadores deste domínio avaliam a **aplicação efectiva de decisões e controlos de arquitectura de segurança** ao longo do ciclo de vida das aplicações. A arquitectura é um domínio predominantemente qualitativo - o que se mede não é o código produzido, mas a existência, actualidade e rastreabilidade das decisões estruturais de segurança.

Um sistema arquitecturalmente seguro não é apenas aquele que implementa os controlos correctos. É aquele que demonstra **por que** os implementa, **quem** os decidiu, e **o que acontece** quando as premissas mudam. Esses elementos são observáveis e auditáveis.

Os indicadores ARC alimentam as dimensões transversais **T-01 (Cobertura de controlos)**, **T-04 (Ownership)** e **T-06 (Maturidade SbD-ToE)**.

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
| Ord | Qualitativo ordinal (nível 1–3, alinhado com L1/L2/L3) |
| Bin | Binário - existência verificável com evidência obrigatória |

---

## Catálogo de indicadores

| ID | Indicador | Tipo | L1 | L2 | L3 | Dim. T | Período |
|----|-----------|:----:|:--:|:--:|:--:|:------:|---------|
| ARC-K01 | % aplicações com threat model documentado, revisto e actualizado no último ciclo de avaliação | Q% | - | ≥ 80% | 100% | T-01 | Semestral / por release major |
| ARC-K02 | % decisões de arquitectura de segurança com ADR registado e rastreável a requisito ARC canónico | Q% | - | ≥ 70% | ≥ 95% | T-01 | Por release |
| ARC-K03 | % fluxos de comunicação entre zonas de confiança distintas sem cifra em trânsito (deve tender a zero) | Q% ↓ | - | = 0% | = 0% | T-01 | Trimestral |
| ARC-K04 | % revisões de arquitectura com participação formal de AppSec antes de entrada em produção | Q% | - | ≥ 80% | 100% | T-01, T-04 | Por release |
| ARC-K05 | Nível de implementação de defence-in-depth por aplicação (múltiplas camadas de controlo independentes) | Ord | nível 1 | nível 2 | nível 3 | T-06 | Anual |
| ARC-K06 | % componentes críticos sem isolamento de blast radius documentado e verificado | Q% ↓ | - | ≤ 20% | = 0% | T-01 | Semestral |

---

## Definições complementares

**ARC-K01 - Threat model:** considera-se "revisto e actualizado" um threat model que reflecte a arquitectura actual e foi sujeito a revisão formal após a última mudança arquitectural significativa ou no prazo máximo definido pelo ciclo de avaliação do domínio (semestral para L2; por release major para L3). Ferramenta e formato são livres; a evidência é obrigatória.

**ARC-K02 - ADR rastreável:** um ADR (Architecture Decision Record) é considerado rastreável se identificar o requisito ARC a que responde, o responsável pela decisão, a data e o contexto que a motivou. ADRs sem requisito associado não contam para este indicador.

**ARC-K05 - Níveis de defence-in-depth:**
- Nível 1: controlo de acesso perimetral e logging básico
- Nível 2: segmentação de rede, autenticação por camada, detecção de anomalias
- Nível 3: controlos em cada camada com verificação independente, zero-trust por zona, auditabilidade de todas as travessias

**ARC-K06 - Blast radius:** documentação que demonstra que um compromisso de um componente não se propaga de forma irrestrita. Pode incluir: isolamento de rede, permissões mínimas, circuit breakers, ou análise formal de propagação de falhas.

---

## Recolha e instrumentação

| Indicador | Fonte primária | Automação possível |
|-----------|---------------|-------------------|
| ARC-K01 | Repositório de documentação (wiki, Git) | Parcial - presença do ficheiro; actualidade requer validação humana |
| ARC-K02 | Repositório de ADRs (Git, Confluence) | Parcial - contagem de ADRs com campo `requisito` preenchido |
| ARC-K03 | Scans de rede / IaC review / testes de penetração | Sim - ferramentas de análise de tráfego ou policy-as-code em IaC |
| ARC-K04 | Registos de revisão (tickets, actas, comentários de PR) | Parcial - presença de label/reviewer AppSec no PR |
| ARC-K05 | Avaliação qualitativa por AppSec ou arquitecto de segurança | Não - requer avaliação estruturada periódica |
| ARC-K06 | Documentação de arquitectura + revisão de IaC | Parcial - validação de políticas de rede e permissões em IaC |

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| `addon/01-catalogo-requisitos.md` | Requisitos ARC-001..013 que fundamentam os indicadores |
| `addon/06-rastreabilidade.md` | Modelo de rastreabilidade threat→requisito→ADR→controlo→evidência |
| `addon/03-excecoes.md` | Desvios aos controlos ARC requerem excepção formal |
| Cap. 14 `addon/kpis-governanca.md` | Dimensões transversais T-01, T-04, T-06 |
