---
id: kpis-metricas-formacao
title: KPIs e Métricas - Formação e Onboarding
sidebar_position: 91
description: Indicadores técnicos e de processo para avaliação da eficácia, cobertura e impacto do programa de formação e onboarding em segurança, com thresholds por nível de risco e mapeamento para dimensões transversais de governação SbD-ToE.
tags: [kpi, metricas, TRN, formacao, onboarding, champions, L1, L2, L3]
---

<!--template: sbdtoe-addon -->

# KPIs e Métricas - Formação e Onboarding

## Âmbito e propósito

Os indicadores deste domínio avaliam a **eficácia, cobertura e impacto mensurável do programa de formação e onboarding em segurança**. A formação é um controlo organizacional, não um evento de compliance: o seu valor reside na mudança de comportamento observável, não na conclusão de módulos.

A medição de formação enfrenta um problema de causalidade - é difícil atribuir uma redução de incidentes exclusivamente à formação. Os indicadores TRN abordam este problema por dois ângulos: (a) indicadores de cobertura e processo que são directamente observáveis e controláveis; e (b) indicadores de impacto que estabelecem correlações observáveis entre formação e comportamento técnico, sem exigir causalidade exclusiva.

Os indicadores TRN alimentam a dimensão transversal **T-04 (Cobertura de ownership)**, que agrega a formação dos responsáveis por funções críticas de segurança.

> Este ficheiro define os indicadores no formato canónico SbD-ToE. O ficheiro `90-indicadores-metricas.md` contém uma síntese operacional mais leve para uso quotidiano das equipas.

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
| Misto | Combinação de componente quantitativa e avaliação contextual |

---

## Catálogo de indicadores

| ID | Indicador | Tipo | L1 | L2 | L3 | Dim. T | Período |
|----|-----------|:----:|:--:|:--:|:--:|:------:|---------|
| TRN-K01 | % novos colaboradores com onboarding de segurança concluído em ≤ 7 dias úteis após início | Q% | ≥ 90% | ≥ 95% | 100% | T-04 | Mensal |
| TRN-K02 | % owners de segurança e aprovadores de excepções com formação SbD válida (≤ 12 meses) | Q% | ≥ 80% | ≥ 95% | 100% | T-04 | Trimestral |
| TRN-K03 | % fornecedores com acesso a código, pipeline ou dados de sistemas L2/L3 com formação ou questionário de segurança concluído antes de onboarding | Q% | - | ≥ 90% | 100% | T-04 | Por onboarding |
| TRN-K04 | % conteúdos de formação actualizados após alteração significativa do catálogo de requisitos ou do modelo de ameaças | Q% | ≥ 80% | 100% | 100% | T-04 | Por alteração |
| TRN-K05 | # incidentes de segurança com causa raiz atribuída a lacuna de formação identificada e não endereçada | Q# ↓ | = 0 | = 0 | = 0 | T-04 | Por incidente |
| TRN-K06 | % PRs/commits em sistemas L2/L3 que repetem padrões de segurança identificados em formação (proxy de absorção) | Q% | - | ≥ 75% | ≥ 90% | T-04 | Trimestral |
| TRN-K07 | % equipas com pelo menos um Security Champion activo e com formação válida (≤ 12 meses) | Q% | - | ≥ 80% | 100% | T-04 | Trimestral |

---

## Definições complementares

**TRN-K01 - Onboarding concluído:** considera-se concluído quando o colaborador completou o módulo obrigatório de segurança (definido no catálogo formativo `addon/01-catalogo-formativo.md`) e existe registo rastreável de conclusão com data. Módulos parciais ou em progresso não satisfazem este critério.

**TRN-K02 - Formação SbD válida:** considera-se válida a formação concluída nos últimos 12 meses. Funções críticas incluem: owners de segurança, aprovadores de excepções, responsáveis por releases de produção, e revisores de arquitectura. A lista de funções críticas deve estar definida na política de formação organizacional.

**TRN-K03 - Fornecedor com formação:** para fornecedores de sistemas L3, o requisito é formação ou questionário de segurança específico ao contexto (não genérico). Para sistemas L2, um questionário de segurança documentado é suficiente. O critério de onboarding completo de fornecedores é definido em Cap. 14 `addon/03-modelo-validacao-fornecedores.md`.

**TRN-K04 - Conteúdo actualizado:** um conteúdo está desactualizado quando: (a) referencia requisitos revogados ou alterados; (b) não reflecte mudanças no catálogo de ameaças relevante para o domínio; ou (c) tem mais de 24 meses sem revisão. O prazo de actualização após alteração significativa do catálogo é de 90 dias.

**TRN-K05 - Incidente com causa raiz de formação:** um incidente tem causa raiz de formação quando a análise post-mortem identifica que: (a) o comportamento que originou o incidente era coberto por conteúdo de formação existente; e (b) o colaborador envolvido não tinha a formação concluída ou a tinha expirada. Este indicador deve tender a zero e qualquer valor não-zero é um sinal de alerta imediato.

**TRN-K06 - Absorção de padrões (proxy):** este indicador mede a proporção de PRs/commits que seguem os padrões de código seguro identificados como prioritários na formação (ex: não usar funções de criptografia deprecated, não construir queries com concatenação, não hardcode de segredos). A medição requer definição prévia dos padrões mensuráveis por scanner de código.

**TRN-K07 - Security Champion activo:** considera-se activo um champion que: (a) tem formação válida (≤ 12 meses); (b) participou em pelo menos uma actividade de security review ou awareness nos últimos 90 dias; (c) é o ponto de contacto conhecido pela equipa para questões de segurança. Designação formal sem actividade não satisfaz este critério.

---

## Recolha e instrumentação

| Indicador | Fonte primária | Suporte de instrumentação | Automação |
|-----------|---------------|--------------------------|-----------|
| TRN-K01 | Plataforma de formação + data de início (HRIS) | LMS (Moodle, Docebo, etc.) + HRIS | Sim |
| TRN-K02 | Registo de formação + lista de funções críticas | LMS + registo GRC de owners/aprovadores | Parcial |
| TRN-K03 | Registo de onboarding de fornecedores + plataforma de formação | GRC + registo de questionários | Não |
| TRN-K04 | Histórico de revisão de conteúdos (git log, LMS versioning) | LMS com controlo de versão de conteúdo | Parcial |
| TRN-K05 | Base de dados de incidentes + relatórios post-mortem | Sistema de IR + análise de causa raiz | Não |
| TRN-K06 | Scanner de código com regras de padrões prioritários | Semgrep (regras customizadas), SonarQube | Sim |
| TRN-K07 | Registo de champions + registo de actividade | Wiki/GRC + log de participação em reviews | Não |

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| `addon/01-catalogo-formativo.md` | Conteúdo obrigatório que define o baseline de TRN-K01/K02 |
| `addon/03-programa-champions.md` | Critérios de actividade de champion (TRN-K07) |
| `addon/90-indicadores-metricas.md` | Síntese operacional de métricas para uso quotidiano das equipas |
| Cap. 14 `addon/03-modelo-validacao-fornecedores.md` | Requisitos de formação de fornecedores (TRN-K03) |
| Cap. 14 `addon/kpis-governanca.md` | Dimensão transversal T-04 (ownership e formação) |
