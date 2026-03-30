---
id: kpis-metricas-iac
title: KPIs e Métricas - IaC e Infraestrutura
sidebar_position: 12
description: Indicadores técnicos e operacionais para avaliação da eficácia dos controlos de segurança em Infrastructure as Code, com thresholds por nível de risco e mapeamento para dimensões transversais de governação SbD-ToE.
tags: [kpi, metricas, IAC, infraestrutura, policy-as-code, drift, opa, sentinel, L1, L2, L3]
---

<!--template: sbdtoe-addon -->

# KPIs e Métricas - IaC e Infraestrutura

## Âmbito e propósito

Os indicadores deste domínio avaliam a **segurança da infraestrutura definida como código**: a cobertura de policy-as-code, a detecção e resolução de drift de configuração, a ausência de segredos em repositórios de IaC, e a proporção de infraestrutura gerida declarativamente vs provisionada manualmente.

IaC inverte o problema clássico de segurança de infraestrutura: em vez de auditar estados de sistemas em produção, audita-se o código que os define. Este deslocamento para a esquerda só tem valor se a policy enforcement for efectiva e o drift for detectado e resolvido rapidamente. Infraestrutura manual residual em sistemas críticos é uma lacuna de controlo, não uma excepção operacional.

Os indicadores IAC alimentam as dimensões transversais **T-01 (Cobertura de controlos)** e **T-02 (Saúde de excepções)**.

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
| IAC-K01 | % módulos/stacks IaC com policy-as-code activa e em modo de bloqueio no pipeline | Q% | ≥ 50% | ≥ 90% | 100% | T-01 | Mensal |
| IAC-K02 | # recursos de infraestrutura com drift detectado e não resolvido em mais de 7 dias | Q# ↓ | ≤ 10 | ≤ 3 | = 0 | T-01 | Semanal |
| IAC-K03 | % infraestrutura de produção de sistemas L2/L3 provisionada manualmente (não gerida por IaC) | Q% ↓ | - | ≤ 10% | = 0% | T-01 | Trimestral |
| IAC-K04 | % excepções de policy activas em IaC com registo formal, aprovador e data de expiração | Q% | ≥ 80% | 100% | 100% | T-02 | Mensal |
| IAC-K05 | # segredos detectados em repositórios IaC e não removidos e rotacionados em menos de 24h | Q# ↓ | = 0 | = 0 | = 0 | T-01 | Contínuo |
| IAC-K06 | % módulos IaC reutilizáveis (internos ou de registo privado) sem revisão de segurança activa | Q% ↓ | - | ≤ 15% | = 0% | T-01 | Semestral |
| IAC-K07 | % pipelines de IaC com plan + review obrigatório antes de apply em produção | Q% | ≥ 70% | ≥ 95% | 100% | T-01 | Mensal |

---

## Definições complementares

**IAC-K01 - Policy-as-code em modo bloqueio:** apenas contam módulos onde a falha de policy (OPA/Rego, Sentinel, Checkov, tfsec, kube-linter, cfn-guard) bloqueia o pipeline. Execuções em modo `plan-only` sem bloqueio não satisfazem este critério.

**IAC-K02 - Drift:** desvio entre o estado declarado no código IaC e o estado efectivo do recurso em cloud/on-premise. Ferramentas de detecção de drift: `terraform plan` com output analisado, AWS Config, Azure Policy, Driftctl. O prazo de 7 dias conta a partir do primeiro registo de drift detectado.

**IAC-K03 - Infraestrutura manual:** inclui recursos criados pela consola web, CLI sem IaC, ou scripts imperativos sem equivalência declarativa. Recursos de emergência criados manualmente com ticket associado e plano de migração para IaC têm prazo de 30 dias antes de entrarem nesta contagem.

**IAC-K04 - Excepção de policy:** uma excepção é considerada formal se incluir: ID da policy excepcionada, justificação técnica, owner, aprovador com autoridade proporcional ao nível de risco, e data de expiração. Comentários no código sem aprovação externa não satisfazem este critério.

**IAC-K05 - Secret em IaC:** inclui qualquer valor que satisfaça regras de detecção de secret scanners aplicados a repositórios de infraestrutura (Terraform, Helm, Ansible, CloudFormation). "Removido e rotacionado" requer: remoção do histórico git (rebase ou filter-repo) E rotação da credencial no sistema destino.

**IAC-K06 - Módulo com revisão activa:** um módulo é considerado com revisão activa se tiver sido sujeito a análise de segurança nos últimos 12 meses ou desde a última versão major, com evidência documentada.

---

## Recolha e instrumentação

| Indicador | Fonte primária | Ferramentas de referência | Automação |
|-----------|---------------|--------------------------|-----------|
| IAC-K01 | Configuração de pipeline + resultados de policy | Checkov, tfsec, OPA/Rego, Sentinel | Sim |
| IAC-K02 | Ferramenta de detecção de drift | Driftctl, `terraform plan`, AWS Config | Sim |
| IAC-K03 | Inventário de recursos cloud vs repositório IaC | Cloud asset inventory + IaC state | Parcial |
| IAC-K04 | Directório `exceptions/` + sistema de aprovação | Revisão de ficheiros + registo GRC | Parcial |
| IAC-K05 | Pre-commit hooks + CI scanner em repositórios IaC | GitLeaks, TruffleHog (config IaC) | Sim |
| IAC-K06 | Registo de módulos internos + histórico de revisões | Wiki/Confluence + git log | Não |
| IAC-K07 | Configuração de pipeline (workflow YAML) | Auditoria de pipeline de IaC | Parcial |

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| `addon/08-matriz-requisitos-iac.md` | Requisitos IAC-001..013 que fundamentam os indicadores |
| `addon/09-gestao-excecoes.md` | Processo de excepção de policy IaC (IAC-K04) |
| `addon/06-controle-enforcement.md` | Mecanismos de enforcement que alimentam IAC-K01/K07 |
| Cap. 14 `addon/kpis-governanca.md` | Dimensões transversais T-01, T-02 |
