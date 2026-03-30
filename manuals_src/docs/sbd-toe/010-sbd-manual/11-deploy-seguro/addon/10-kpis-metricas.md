---
id: kpis-metricas-deploy
title: KPIs e Métricas - Deploy Seguro
sidebar_position: 10
description: Indicadores técnicos e operacionais para avaliação da eficácia dos controlos de segurança no processo de deploy e gestão de releases, com thresholds por nível de risco e mapeamento para dimensões transversais de governação SbD-ToE.
tags: [kpi, metricas, DPL, deploy, release, break-glass, rollback, L1, L2, L3]
---

<!--template: sbdtoe-addon -->

# KPIs e Métricas - Deploy Seguro

## Âmbito e propósito

Os indicadores deste domínio avaliam a **segurança do processo de deploy e gestão de releases**: a cobertura das validações pré-deploy, o controlo e rastreabilidade de deploys de emergência (break-glass), a qualidade dos artefactos de evidência de deploy, e a separação efectiva de configuração entre ambientes.

O deploy é o momento em que os controlos implementados se tornam efectivos - ou falham. Os indicadores DPL focam-se na disciplina do processo: um deploy sem checklist de segurança validado não é necessariamente inseguro, mas é um deploy sem evidência de que a segurança foi verificada. Essa distinção é auditável e relevante.

Os indicadores DPL alimentam as dimensões transversais **T-01 (Cobertura de controlos)** e **T-02 (Saúde de excepções)**.

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
| Qt | Quantitativo temporal (horas/dias) |

---

## Catálogo de indicadores

| ID | Indicador | Tipo | L1 | L2 | L3 | Dim. T | Período |
|----|-----------|:----:|:--:|:--:|:--:|:------:|---------|
| DPL-K01 | % deploys de produção com checklist de segurança pré-deploy validado e registado | Q% | ≥ 70% | ≥ 95% | 100% | T-01 | Por release |
| DPL-K02 | % deploys de emergência (break-glass) com aprovação post-facto registada em menos de 24h | Q% | 100% | 100% | 100% | T-02 | Por evento |
| DPL-K03 | % deploys de emergência com notificação ao CISO (ou equivalente) realizada antes ou durante o deploy | Q% | - | 100% | 100% | T-02 | Por evento |
| DPL-K04 | # rollbacks de produção por motivo de segurança por trimestre | Q# | registo obrig. | ≤ 2 | ≤ 1 | T-03 | Trimestral |
| DPL-K05 | % ambientes de produção com separação verificada de segredos e configuração de não-produção | Q% | - | ≥ 90% | 100% | T-01 | Semestral |
| DPL-K06 | % releases com artefacto de evidência de deploy rastreável (ID de pipeline, hash de artefacto, timestamp) | Q% | ≥ 70% | ≥ 95% | 100% | T-01 | Por release |
| DPL-K07 | % deploys de emergência com post-mortem de segurança realizado em menos de 5 dias úteis | Q% | - | ≥ 80% | 100% | T-02 | Por evento |

---

## Definições complementares

**DPL-K01 - Checklist validado:** considera-se validado um checklist que: (a) foi preenchido pelo responsável técnico do deploy; (b) inclui verificação de security gates do pipeline; (c) está associado ao identificador do deploy (pipeline run ID, ticket, change record). Checklists genéricos sem associação ao deploy específico não satisfazem este critério.

**DPL-K02 - Deploy de emergência (break-glass):** qualquer deploy que bypassa um ou mais security gates obrigatórios, ou que é realizado fora do processo de change management definido para sistemas L2/L3. A aprovação post-facto é uma excepção ao processo normal - não é uma alternativa permanente. O prazo de 24h é absoluto; não existe extensão.

**DPL-K03 - Notificação ao CISO:** para sistemas L3, a notificação deve ser realizada em tempo real (durante o deploy) ou antes. Para sistemas L2, pode ser pós-evento mas dentro das 24h de DPL-K02. O canal de notificação (email, Slack, ticket) é livre; a evidência de notificação é obrigatória.

**DPL-K04 - Rollback por motivo de segurança:** inclui rollbacks iniciados por: descoberta de vulnerabilidade em produção, falha de controlo de segurança pós-deploy, configuração insegura detectada após deploy, ou instrução de CISO/AppSec. Rollbacks por outros motivos (performance, bugs funcionais) não entram neste indicador.

**DPL-K05 - Separação de configuração:** considera-se verificada a separação quando: (a) segredos de produção não estão acessíveis em ambientes de não-produção; (b) variáveis de ambiente específicas de produção não existem em staging/dev; (c) a verificação foi realizada por auditoria técnica (scan de configuração ou IaC review) com evidência registada.

**DPL-K07 - Post-mortem de segurança:** deve incluir: cronologia do evento, causa raiz, impacto de segurança (real e potencial), acções correctivas com owner e prazo, e revisão do processo que permitiu o deploy de emergência. Post-mortems sem análise de causa raiz de segurança não satisfazem este critério.

---

## Recolha e instrumentação

| Indicador | Fonte primária | Ferramentas de referência | Automação |
|-----------|---------------|--------------------------|-----------|
| DPL-K01 | Sistema de change management + pipeline logs | Jira, ServiceNow + pipeline (GitHub Actions, GitLab) | Parcial |
| DPL-K02 | Registo de deploys de emergência + sistema de aprovação | Change record + registo de excepções | Não |
| DPL-K03 | Log de notificações + registo de comunicação | Email/Slack com timestamp + registo GRC | Não |
| DPL-K04 | Sistema de change management + incident tracking | Jira, PagerDuty, ServiceNow | Parcial |
| DPL-K05 | Auditoria de configuração + IaC review | Auditoria de variáveis de ambiente + IaC scan | Parcial |
| DPL-K06 | Pipeline logs + registo de releases | CI/CD platform (run ID, artifact hash, timestamp) | Sim |
| DPL-K07 | Repositório de post-mortems | Confluence, GitHub (post-mortem templates) | Não |

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| `addon/00-catalogo-requisitos.md` | Requisitos DPL-001..009 que fundamentam os indicadores |
| `addon/09-excecoes-deploy.md` | Processo de break-glass e aprovação post-facto (DPL-K02/K03/K07) |
| `addon/04-validacoes-pre-deploy.md` | Checklist de segurança pré-deploy (DPL-K01) |
| Cap. 14 `addon/kpis-governanca.md` | Dimensões transversais T-01, T-02 |
