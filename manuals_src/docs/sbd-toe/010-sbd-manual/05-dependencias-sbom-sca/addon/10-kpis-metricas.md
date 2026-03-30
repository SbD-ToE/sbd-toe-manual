---
id: kpis-metricas-dependencias
title: KPIs e Métricas - Dependências, SBOM e SCA
sidebar_position: 10
description: Indicadores técnicos e operacionais para avaliação da eficácia dos controlos de gestão de dependências, geração de SBOM e análise de composição de software, com thresholds por nível de risco e mapeamento para dimensões transversais de governação SbD-ToE.
tags: [kpi, metricas, DEP, sbom, sca, dependencias, cve, supply-chain, L1, L2, L3]
---

<!--template: sbdtoe-addon -->

# KPIs e Métricas - Dependências, SBOM e SCA

## Âmbito e propósito

Os indicadores deste domínio avaliam a **capacidade de uma organização conhecer, controlar e reagir ao risco introduzido pelas dependências de software**. A gestão de dependências é um domínio altamente quantificável: o SBOM é um artefacto estruturado, as CVEs têm pontuações CVSS normalizadas, e os prazos de remediação são rastreáveis com precisão temporal.

A ausência de visibilidade sobre dependências não é uma posição neutra - é a aceitação implícita de risco não quantificado. Estes indicadores transformam esse risco em dados accionáveis.

Os indicadores DEP alimentam as dimensões transversais **T-01 (Cobertura de controlos)**, **T-03 (Velocidade de resolução)** e **T-05 (Cadeia de fornecimento)**.

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
| DEP-K01 | % aplicações com SBOM gerado automaticamente e actualizado a cada release | Q% | ≥ 50% | ≥ 90% | 100% | T-01, T-05 | Por release |
| DEP-K02 | % CVEs críticos (CVSS ≥ 9.0) em dependências directas mitigados dentro de SLA | Q% | ≥ 70% (SLA: 30d) | ≥ 90% (SLA: 14d) | 100% (SLA: 5d) | T-03 | Contínuo |
| DEP-K03 | % CVEs altos (CVSS 7.0–8.9) em dependências directas mitigados dentro de SLA | Q% | ≥ 60% (SLA: 90d) | ≥ 80% (SLA: 30d) | ≥ 95% (SLA: 14d) | T-03 | Mensal |
| DEP-K04 | # dependências directas sem mantedor activo (EOL, abandonadas ≥ 24 meses) em produção | Q# ↓ | ≤ 5 | ≤ 2 | = 0 | T-05 | Trimestral |
| DEP-K05 | % pipelines com SCA automatizado integrado com gate de bloqueio para CVEs críticos | Q% | ≥ 60% | ≥ 90% | 100% | T-01 | Mensal |
| DEP-K06 | % dependências com licença incompatível com política organizacional activas em produção | Q% ↓ | - | = 0% | = 0% | T-05 | Trimestral |
| DEP-K07 | % aplicações L3 com SBOM entregue a stakeholders relevantes (GRC, procurement, cliente) | Q% | - | - | ≥ 80% | T-05 | Por release major |

---

## Definições complementares

**DEP-K02/K03 - SLA de mitigação:** o SLA conta a partir da data de publicação da CVE em NVD/OSV, ou da data de detecção pelo scanner SCA, consoante o que for mais tardio. Mitigação válida inclui: actualização da dependência, remoção da dependência, ou excepção formal documentada com compensação (que suspende o contador mas não fecha o indicador).

**DEP-K04 - Dependência abandonada:** uma dependência é considerada sem mantedor activo quando o repositório não tem commits relevantes há ≥ 24 meses E não existe versão de suporte de longo prazo activa. Dependências com fork interno activo são excluídas desta contagem se o fork tiver política de patch documentada.

**DEP-K05 - Gate de bloqueio:** o SCA apenas conta para este indicador se bloquear o pipeline em caso de CVE crítico sem excepção formal. SCA em modo report-only não satisfaz este critério.

**DEP-K06 - Licença incompatível:** definida pela política de licenciamento organizacional. Na ausência de política formal, usa-se como referência a incompatibilidade com licenças copyleft forte (GPL v3, AGPL) em contexto de software proprietário, ou licenças sem aprovação OSI em contexto open-source.

---

## Recolha e instrumentação

| Indicador | Fonte primária | Ferramentas de referência | Automação |
|-----------|---------------|--------------------------|-----------|
| DEP-K01 | Pipeline de build; registo de releases | Syft, CycloneDX, SPDX tools | Sim |
| DEP-K02/K03 | Scanner SCA + NVD/OSV feed | Grype, Trivy, Snyk, Dependabot | Sim |
| DEP-K04 | Scanner SCA + repos.github.com / deps.dev | OSS Insight, deps.dev API | Parcial |
| DEP-K05 | Configuração de pipeline (YAML audit) | Inspeção de pipeline + resultados SCA | Parcial |
| DEP-K06 | Scanner de licenças SCA | FOSSA, LicenseFinder, Snyk License | Sim |
| DEP-K07 | Registo de entregas GRC / contrato | Manual ou integração GRC | Não |

---

## Thresholds de SLA por nível - resumo

| Severidade (CVSS) | L1 | L2 | L3 |
|-------------------|:--:|:--:|:--:|
| Crítico (≥ 9.0) | 30 dias | 14 dias | 5 dias |
| Alto (7.0–8.9) | 90 dias | 30 dias | 14 dias |
| Médio (4.0–6.9) | - | 90 dias | 60 dias |
| Baixo (&lt; 4.0) | - | - | 180 dias |

Estes thresholds são referência de base. Regulamentação sectorial (DORA, NIS2) pode impor prazos mais curtos que prevalecem.

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| `addon/00-catalogo-requisitos.md` | Requisitos DEP-001..010 que fundamentam os indicadores |
| `addon/08-rastreabilidade-vulnerabilidades.md` | Modelo de rastreabilidade CVE → aplicação → resolução |
| `addon/09-excecoes-e-aceitacao-risco.md` | CVEs sem resolução dentro de SLA requerem excepção formal |
| Cap. 14 `addon/kpis-governanca.md` | Dimensões transversais T-01, T-03, T-05 |
