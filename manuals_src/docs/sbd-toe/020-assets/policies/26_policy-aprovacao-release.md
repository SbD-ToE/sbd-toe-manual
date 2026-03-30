---
id: policy-aprovacao-release
title: Política de Aprovação de Release
description: Política organizacional que define o processo formal de decisão go/no-go para releases de software, incluindo alçadas de aprovação por nível de criticidade, separação entre sinal automático e decisão humana, aceitação formal de risco residual e registo de evidências, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, release, aprovação, go/no-go, risco residual, sign-off, alçadas, cap10, cap11, L1, L2, L3, governance]
grupo: pipeline-entrega
sidebar_position: 26
---

# Política de Aprovação de Release

## 1. Objetivo

Esta política define o processo formal de **decisão de go/no-go para releases de software**, clarificando as alçadas de aprovação, os critérios de aceitação, a separação entre sinal automático e decisão humana, e o registo de evidências.

A aprovação de uma release é uma decisão de risco - não uma formalidade. O resultado dos gates automáticos (SAST, DAST, SCA) é um sinal que informa a decisão, mas não a substitui. A decisão requer um owner humano identificado, que aceita explicitamente o risco residual e o risco operacional de promover a versão, com base na evidência disponível.

O objetivo desta política é garantir que:

- A decisão de go/no-go é tomada por pessoa com alçada adequada ao nível de risco da aplicação
- A decisão é registada com evidência verificável (quem, quando, com base em quê)
- O risco residual é aceite explicitamente, nunca por omissão
- A distinção entre sinal automático e decisão humana é clara e auditável

---

## 2. Âmbito e obrigatoriedade

| Nível | Obrigatoriedade |
|---|---|
| L1 | Recomendado; aprovação informal do Tech Lead |
| L2 | Obrigatório; aprovação formal registada; aceitação explícita de risco residual se aplicável |
| L3 | Obrigatório; dupla aprovação; registo imutável; aceitação de risco residual com alçada CISO |

---

## 3. Distinção entre sinal automático e decisão humana

O pipeline produz **sinais** - resultados de gates automáticos que informam o estado de segurança da release. Estes sinais não são decisões:

| Sinal (automático) | O que indica | Não decide |
|---|---|---|
| Gate pré-release APROVADO | Critérios mínimos cumpridos | Que a release está pronta para produção |
| Gate pré-release REJEITADO | Critérios mínimos não cumpridos | Bloqueio automático mas a decisão de resolver/excecionar é humana |
| Score de qualidade (ex: SonarQube quality gate) | Nível de qualidade do código | Aprovação da release |

A promoção a produção requer sempre uma decisão humana nominalmente registada, mesmo quando o gate automático retorna APROVADO. Um "score verde" não é uma aprovação.

---

## 4. Alçadas de aprovação por nível

### 4.1 Aprovação de go

| Nível | Aprovador(es) mínimo(s) | Condição |
|---|---|---|
| L1 | Tech Lead | Gate automático APROVADO + revisão da checklist |
| L2 | Tech Lead + AppSec Engineer | Gate automático APROVADO + checklist verificada + risco residual avaliado |
| L3 | Tech Lead + AppSec Engineer + Security Officer (ou CISO delegado) - dupla aprovação | Gate automático APROVADO + checklist verificada + aceitação formal de risco residual |

### 4.2 Aprovação de no-go com exceção

Quando o gate automático retorna REJEITADO mas existe justificação de negócio para avançar (ex: fix de produção urgente, deadline regulatório), o no-go pode ser ultrapassado com:

| Nível | Alçada de override | Requisitos adicionais |
|---|---|---|
| L1 | Tech Lead | Justificação documentada; plano de correção com prazo |
| L2 | AppSec Engineer + Tech Lead | Justificação técnica; exceção formal aprovada; plano de correção |
| L3 | CISO (ou Security Officer delegado) + AppSec Engineer | Justificação técnica e de negócio; exceção formal; plano de correção com data; notificação ao GRC |

:::warning
O override de um gate rejeitado não elimina o risco - adia a sua resolução. Toda a aprovação com override deve ser tratada como aceitação de risco residual com TTL máximo igual ao prazo do plano de correção.
:::

---

## 5. Aceitação formal de risco residual

Quando uma release é aprovada com findings em aberto (com exceções formais), o aprovador deve registar explicitamente a aceitação de risco residual:

- [ ] Identificação dos findings em aberto e referência às exceções aprovadas
- [ ] Avaliação do impacto potencial se o risco for explorado
- [ ] Justificação de negócio para avançar com risco residual
- [ ] Controlos compensatórios activos que reduzem o risco de exploração
- [ ] Prazo de resolução com owner definido
- [ ] Identidade do aprovador e timestamp

A aceitação de risco residual é uma declaração formal - não um campo optativo da checklist.

---

## 6. Registo de aprovação

Cada decisão de go/no-go deve ser registada com os seguintes campos mínimos:

| Campo | Descrição |
|---|---|
| Release / versão | Tag semântica ou identificador da release |
| Ambiente alvo | staging / produção |
| Decisão | GO / NO-GO / GO com override / GO com risco residual |
| Aprovador(es) | Identidade(s) com timestamp individual |
| Referência ao gate report | Link ou identificador do relatório do gate pré-release |
| Referência ao artefacto | Digest SHA256 do artefacto aprovado |
| Risco residual aceite | Sim / Não; referência às exceções se sim |
| Notas | Qualquer contexto adicional relevante para a decisão |

Em L3, o registo deve ser imutável (WORM ou equivalente) e retido conforme a Política de Rastreabilidade.

---

## 7. Releases de emergência

Situações de incidente activo em produção podem requerer uma release de correcção urgente fora do processo normal. Nestes casos:

- [ ] Aprovação de emergência obtida antes do deploy (mesmo que em canais informais - deve ser formalizada a posteriori no prazo máximo de 24h)
- [ ] Gates de segurança executados mesmo em modo acelerado - sem bypass completo de SAST e secret detection
- [ ] A release de emergência é marcada como tal no registo com justificação
- [ ] Post-mortem realizado após a resolução com análise ao processo e medidas preventivas

---

## 8. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Tech Lead | Coordenar o processo de release; verificar checklist; aprovar em L1/L2 |
| AppSec Engineer | Verificar estado dos findings e exceções; aprovar em L2/L3; validar risco residual |
| Security Officer / CISO | Aprovar releases com risco residual significativo em L3; ser notificado de overrides |
| Product Manager | Apresentar justificação de negócio quando existe conflito entre prazo e segurança |
| DevOps / SRE | Executar o deploy após aprovação registada; não iniciar deploy sem aprovação |
| GRC / Compliance | Auditar registos de aprovação; verificar rastreabilidade; relatórios de conformidade |

---

## 9. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente com origem em release aprovada com risco residual não documentado
- Alteração das alçadas de governance da organização
- Alteração regulatória que imponha requisitos adicionais de aprovação formal

---

## 10. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 10 - Testes de Segurança | Critérios de go/no-go e aceitação de risco residual |
| SbD-ToE Cap. 11 - Deploy Seguro | Gates de aprovação de deploy |
| SbD-ToE Cap. 07 - CI/CD Seguro | Separação entre sinal automático e decisão humana |
| Política de Release Seguro (`20_policy-release-seguro.md`) | Gate pré-release e checklist de segurança |
| Política de Deploy Seguro (`25_policy-deploy-seguro.md`) | Execução do deploy após aprovação |
| Política de Gestão de Exceções (`05_policy-gestao-excecoes.md`) | Exceções activas referenciadas na aceitação de risco residual |
| ISO/IEC 27001 - A.12.5 | Control of operational software |
| ITIL Release Management | Framework de gestão de releases |
