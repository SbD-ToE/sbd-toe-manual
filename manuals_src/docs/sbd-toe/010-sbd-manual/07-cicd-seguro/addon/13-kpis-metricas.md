---
id: kpis-metricas-cicd
title: KPIs e Métricas - CI/CD Seguro
sidebar_position: 13
description: Indicadores técnicos e operacionais para avaliação da eficácia dos controlos de segurança em pipelines de integração e entrega contínua, com thresholds por nível de risco e mapeamento para dimensões transversais de governação SbD-ToE.
tags: [kpi, metricas, CIC, cicd, pipeline, gates, artefactos, secrets, L1, L2, L3]
---

<!--template: sbdtoe-addon -->

# KPIs e Métricas - CI/CD Seguro

## Âmbito e propósito

Os indicadores deste domínio avaliam a **segurança estrutural dos pipelines de CI/CD**: a presença e eficácia dos security gates, a integridade e proveniência dos artefactos, a gestão de segredos em contexto de automação, e a visibilidade sobre bypasses e desvios ao processo definido.

O pipeline é simultaneamente um mecanismo de controlo e um vector de ataque. A sua segurança não é binária - é mensurável através da cobertura dos gates, da rastreabilidade dos artefactos e da velocidade com que vulnerabilidades detectadas são resolvidas. Um pipeline onde todos os gates existem mas podem ser bypassados sem registo não é um controlo: é uma ilusão de controlo.

Os indicadores CIC alimentam as dimensões transversais **T-01 (Cobertura de controlos)**, **T-02 (Saúde de excepções)** e **T-03 (Velocidade de resolução)**.

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
| CIC-K01 | % pipelines de produção com security gates activos e em modo de bloqueio (não apenas report) | Q% | ≥ 60% | ≥ 90% | 100% | T-01 | Mensal |
| CIC-K02 | % bypasses de security gate com aprovação formal registada e rastreável (vs total de bypasses) | Q% | ≥ 80% | 100% | 100% | T-02 | Por evento |
| CIC-K03 | % artefactos de build assinados digitalmente e com verificação de assinatura antes de deploy | Q% | - | ≥ 70% | 100% | T-01 | Por release |
| CIC-K04 | % segredos de pipeline injectados via cofre centralizado (Vault, KMS, secret store) vs hardcoded ou env vars não geridos | Q% | ≥ 60% | ≥ 90% | 100% | T-01 | Trimestral |
| CIC-K05 | MTTR - tempo desde detecção de vulnerabilidade crítica em pipeline até mitigação confirmada | Qt | ≤ 14d | ≤ 7d | ≤ 3d | T-03 | Por evento |
| CIC-K06 | % runners/agentes de CI/CD com isolamento efectivo entre jobs de diferentes contextos de confiança | Q% | - | ≥ 80% | 100% | T-01 | Trimestral |
| CIC-K07 | # pipelines sem registo de última revisão de segurança em mais de 12 meses | Q# ↓ | - | ≤ 5 | = 0 | T-01 | Semestral |

---

## Definições complementares

**CIC-K01 - Security gate em modo bloqueio:** um gate conta para este indicador apenas se a sua falha impedir o avanço do pipeline para o ambiente seguinte sem intervenção explícita e registada. Gates configurados como `continue-on-error: true` ou equivalente não satisfazem este critério.

**CIC-K02 - Bypass com aprovação formal:** um bypass é qualquer execução do pipeline que contorna ou ignora um security gate activo. A aprovação formal requer: identificação do responsável, justificação técnica, referência ao ticket ou excepção correspondente, e timestamp. Aprovações genéricas sem contexto não são válidas.

**CIC-K03 - Assinatura de artefactos:** inclui imagens de container (Cosign/Notary), binários (GPG, Sigstore), e pacotes de release. A verificação da assinatura antes do deploy é obrigatória - a existência da assinatura sem verificação não satisfaz este indicador.

**CIC-K04 - Secret de pipeline:** os segredos injectados via variável de ambiente definida manualmente no SCM (sem rotação automática, sem auditoria de acesso) não contam como "geridos via cofre". Apenas integração com sistemas de secret management com auditoria (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager) satisfaz o critério.

**CIC-K05 - MTTR de pipeline:** conta desde a data/hora de detecção pelo scanner (log do job) até à data/hora em que a correcção é confirmada num build limpo. Excepções formais que suspendem a remediação devem ser excluídas do cálculo de MTTR mas registadas separadamente.

**CIC-K06 - Isolamento de runners:** considera-se isolado um runner que: (a) é efémero (destruído após cada job); ou (b) tem política de limpeza de workspace e contexto entre jobs de diferentes repositórios/organizações; ou (c) está em rede segregada sem acesso a credenciais de outros projectos.

---

## Recolha e instrumentação

| Indicador | Fonte primária | Ferramentas de referência | Automação |
|-----------|---------------|--------------------------|-----------|
| CIC-K01 | Configuração de pipeline (YAML) + resultados de jobs | GitHub Actions, GitLab CI, Azure DevOps (auditoria de config) | Parcial |
| CIC-K02 | Logs de pipeline + registos de aprovação | SCM audit log + registo de excepções | Parcial |
| CIC-K03 | Registos de assinatura + policy de admission | Cosign, Sigstore, Notary + verificação no deploy | Sim |
| CIC-K04 | Inventário de variáveis de pipeline vs integrações de secret store | Auditoria de configuração de pipeline | Parcial |
| CIC-K05 | Plataforma de findings + logs de pipeline | DefectDojo + timestamps de pipeline | Parcial |
| CIC-K06 | Configuração de runners + topologia de rede | Auditoria de configuração + IaC review | Parcial |
| CIC-K07 | Registo de revisões de pipeline (git log, tickets) | Auditoria manual ou tagged reviews | Não |

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| `addon/00-catalogo-requisitos.md` | Requisitos CIC-001..010 que fundamentam os indicadores |
| `addon/09-controle-excecoes-visibilidade.md` | Processo de excepção de pipeline (CIC-K02) |
| `addon/06-politicas-gates-pipeline.md` | Definição dos gates que alimentam CIC-K01 |
| Cap. 14 `addon/kpis-governanca.md` | Dimensões transversais T-01, T-02, T-03 |
