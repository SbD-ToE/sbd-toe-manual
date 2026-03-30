---
id: kpis-metricas-desenvolvimento
title: KPIs e Métricas - Desenvolvimento Seguro
sidebar_position: 11
description: Indicadores técnicos e de processo para avaliação da eficácia dos controlos de desenvolvimento seguro, com thresholds por nível de risco e mapeamento para dimensões transversais de governação SbD-ToE.
tags: [kpi, metricas, DEV, desenvolvimento, sast, secrets, code-review, L1, L2, L3]
---

<!--template: sbdtoe-addon -->

# KPIs e Métricas - Desenvolvimento Seguro

## Âmbito e propósito

Os indicadores deste domínio avaliam a **integração de práticas de segurança no processo de desenvolvimento de software**: desde a qualidade das revisões de código até à velocidade de resolução de findings estáticos, passando pelo controlo de secrets e pela rastreabilidade das excepções declaradas no código.

O desenvolvimento seguro é medido não apenas pelo que é bloqueado, mas pelo que é aprendido: a taxa de regressão - vulnerabilidades que reaparecem após resolução - é um indicador de qualidade do processo de remediação, não apenas da ferramenta de detecção.

Os indicadores DEV alimentam as dimensões transversais **T-01 (Cobertura de controlos)**, **T-02 (Saúde de excepções)** e **T-03 (Velocidade de resolução)**.

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
| DEV-K01 | % findings SAST de severidade crítica/alta resolvidos dentro de SLA | Q% | ≥ 70% (SLA: 30d) | ≥ 85% (SLA: 14d) | ≥ 98% (SLA: 7d) | T-03 | Por release |
| DEV-K02 | # secrets detectados em commits e não removidos/rotacionados em menos de 24h | Q# ↓ | ≤ 2/mês | = 0 | = 0 | T-01 | Contínuo |
| DEV-K03 | % PRs em aplicações L2/L3 com verificação explícita de critério de segurança na code review | Q% | - | ≥ 80% | 100% | T-01, T-04 | Mensal |
| DEV-K04 | % excepções de SAST (mutes/waives) com aprovação formal registada e rastreável | Q% | ≥ 80% | 100% | 100% | T-02 | Mensal |
| DEV-K05 | % findings de severidade alta/crítica que reaparecem após resolução declarada (taxa de regressão) | Q% ↓ | - | ≤ 10% | ≤ 5% | T-03 | Trimestral |
| DEV-K06 | % repositórios com SAST activo e configurado para o stack tecnológico em uso | Q% | ≥ 60% | ≥ 90% | 100% | T-01 | Mensal |

---

## Definições complementares

**DEV-K01 - SLA de resolução SAST:** conta a partir da data de detecção pelo scanner no pipeline. Um finding é considerado resolvido quando: (a) o código é corrigido e o scanner confirma ausência; ou (b) uma excepção formal com compensação é registada (suspende o contador, mas não fecha o indicador - ver DEV-K04). Falsos positivos confirmados pelo processo de triagem formal não contam.

**DEV-K02 - Secret exposto:** inclui credenciais, tokens de API, chaves privadas, passwords, e qualquer valor que satisfaça regras de detecção de secret scanners (GitLeaks, TruffleHog, detect-secrets). O prazo de 24h conta a partir da detecção, não do commit. "Removido" exige remoção do histórico git E rotação da credencial no sistema destino - a remoção do ficheiro sem rotação não fecha o indicador.

**DEV-K03 - Critério de segurança em code review:** considera-se verificado quando existe evidência de que pelo menos um reviewer avaliou explicitamente: validação de inputs, gestão de erros, uso de APIs sensíveis, e ausência de padrões proibidos. A evidência pode ser um comentário de review, um checklist de PR, ou label de revisão de segurança.

**DEV-K04 - Excepção de SAST rastreável:** uma excepção é considerada rastreável se incluir: ID do finding, justificação técnica, responsável pela aprovação, e prazo de validade. Anotações sem aprovador registado não satisfazem este critério.

**DEV-K05 - Regressão:** um finding é classificado como regressão se tiver sido marcado como resolvido e reaparecer na mesma localização (ficheiro + linha ± 10 linhas) dentro de 90 dias. Ferramentas como DefectDojo suportam rastreamento automático de regressões.

---

## Recolha e instrumentação

| Indicador | Fonte primária | Ferramentas de referência | Automação |
|-----------|---------------|--------------------------|-----------|
| DEV-K01 | Pipeline SAST + sistema de gestão de findings | SonarQube, Semgrep, CodeQL + DefectDojo | Sim |
| DEV-K02 | Pre-commit hooks + CI scanner | GitLeaks, TruffleHog, detect-secrets | Sim |
| DEV-K03 | Pull request reviews (SCM) | GitHub/GitLab API (labels, reviewers) | Parcial |
| DEV-K04 | Ficheiro `excecoes-aprovadas.yml` + sistema de aprovação | Revisão de PR + registo GRC | Parcial |
| DEV-K05 | Plataforma de gestão de findings com histórico | DefectDojo, Vulcan Cyber | Sim |
| DEV-K06 | Configuração de pipeline + inventário de repositórios | Auditoria de YAML de pipeline | Parcial |

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| `addon/00-catalogo-requisitos.md` | Requisitos DEV-001..009 que fundamentam os indicadores |
| `addon/05-excecoes-e-justificacoes.md` | Processo de excepção de SAST (DEV-K04) |
| Cap. 10 `addon/08-gestao-findings.md` | Centralização e triagem de findings que alimentam DEV-K01/K05 |
| Cap. 14 `addon/kpis-governanca.md` | Dimensões transversais T-01, T-02, T-03 |
