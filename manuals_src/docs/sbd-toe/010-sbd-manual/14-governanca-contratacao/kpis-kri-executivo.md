---
id: kpis-kri-executivo
title: Indicadores de Risco - Visão Executiva
sidebar_position: 88
description: Oito indicadores-chave de risco para reporte ao CISO, direcção e board. Foco em exposição a risco e capacidade de resposta, agregando os indicadores técnicos dos domínios SbD-ToE numa leitura executiva accionável.
tags: [kri, executivo, ciso, board, dashboard, risco, governacao]
---

<!--template: sbdtoe-addon -->

# Indicadores de Risco - Visão Executiva

## Para que serve este documento

O programa SbD-ToE produz dezenas de indicadores técnicos detalhados - um por domínio, por capítulo, por tipo de controlo. Esse detalhe é necessário para as equipas operacionais, mas não é a leitura certa para a direcção ou o board.

Este documento apresenta **oito indicadores de risco** que respondem às perguntas que a gestão precisa de ver respondidas: a organização sabe o que tem? as aplicações críticas estão protegidas? se algo correr mal, conseguimos detectar e reagir a tempo?

Os oito indicadores são um **subconjunto curado** dos indicadores técnicos - não criam nova medição, sintetizam o que os domínios já medem.

> **Nota de leitura:** Os objectivos variam consoante o nível de risco da aplicação - L1 (risco baixo), L2 (risco médio), L3 (risco alto ou crítico). Os sistemas mais críticos têm exigências mais altas.

---

## Os oito indicadores - visão rápida

| # | Pergunta | L1 | L2 | L3 | Revisto |
|---|----------|----|----|----|---------|
| 1 | Temos todas as aplicações catalogadas e classificadas por risco? | 100% | 100% | 100% | Trimestral |
| 2 | Cada aplicação tem um responsável de segurança identificado? | 100% | 100% | 100% | Trimestral |
| 3 | Quantas aplicações em produção estão sem falhas críticas conhecidas? | ≥ 70% | ≥ 90% | 100% | Mensal |
| 4 | Existem credenciais expostas ou autorizações de risco caducadas? | = 0 | = 0 | = 0 | Semanal |
| 5 | Quanto tempo demora a detectar um incidente de segurança? | ≤ 24h | ≤ 4h | ≤ 30 min | Mensal |
| 6 | Quanto tempo demora a reagir após detectar o incidente? | ≤ 48h | ≤ 4h | ≤ 1h | Mensal |
| 7 | As equipas têm formação em segurança actualizada? | ≥ 80% | ≥ 90% | 100% | Trimestral |
| 8 | As aplicações críticas foram testadas por uma entidade independente? | - | ≥ 80% | 100% | Semestral |

---

## Como ler o semáforo

| Cor | Significado |
|-----|-------------|
| **Verde** | Objectivo atingido para o nível de risco das aplicações em causa |
| **Amarelo** | Resultado entre 80% e 99% do objectivo - degradação detectada, ainda sem incumprimento |
| **Vermelho** | Resultado abaixo de 80% do objectivo - ou qualquer valor não-zero no indicador 4 |

Para os indicadores de tempo (5 e 6): amarelo = até ao dobro do objectivo; vermelho = acima do dobro.

---

## Cada indicador em detalhe

---

### 1 - Inventário e classificação do portfólio

**A pergunta:** sabemos quantas aplicações temos e qual o nível de risco de cada uma?

Sem um inventário completo e com níveis de risco atribuídos, todos os outros indicadores perdem validade - não existe denominador confiável para calcular percentagens, nem forma de saber se os controlos certos estão nos lugares certos. Este é o indicador de base de todo o programa.

**Objectivo:** 100% das aplicações classificadas, a todos os níveis de risco. Uma aplicação sem classificação é, por definição, um risco não gerido.

**Quando está vermelho, a pergunta a fazer:** existe um processo activo de inventário e classificação? Quem é responsável por o manter actualizado?

*Referência técnica: CLA-K01 (Cap. 01 - Classificação de Aplicações)*

---

### 2 - Responsabilidade por aplicação

**A pergunta:** para cada aplicação, existe um nome próprio responsável pela sua segurança?

Sem um responsável identificado, não existe ponto de escalada quando algo corre mal, não existe quem responda numa auditoria, e não existe quem garanta que os controlos são mantidos ao longo do tempo. A responsabilidade difusa é equivalente a ausência de responsabilidade.

**Objectivo:** 100% das aplicações com responsável nomeado, com papel e alçada formais. Aplicações sem responsável devem ser escaladas imediatamente.

**Quando está vermelho, a pergunta a fazer:** o processo de onboarding de aplicações inclui a nomeação de responsável? Existe revisão periódica quando há rotatividade de equipas?

*Referência técnica: GOV-K01 (Cap. 14 - Governação)*

---

### 3 - Exposição a falhas críticas em produção

**A pergunta:** quantas das nossas aplicações em produção têm falhas de segurança graves conhecidas que ainda não foram corrigidas?

Falhas críticas conhecidas - identificadas publicamente, com base de dados de vulnerabilidades publicada - são o vector mais explorado em ataques. Uma aplicação com uma falha crítica não corrigida está a operar com uma porta aberta cujo endereço é público. Este indicador agrega a exposição em dois vectores: as bibliotecas e componentes de software que as aplicações usam, e as imagens de sistema operativo e runtime em que correm.

**Objectivo:** L1 ≥ 70%, L2 ≥ 90%, L3 = 100% das aplicações sem falhas críticas não mitigadas. Excepções formais documentadas com compensação técnica são admissíveis - falhas sem qualquer registo de tratamento não são.

**Quando está vermelho, a pergunta a fazer:** os processos de actualização de dependências e imagens de base são automáticos ou manuais? Qual é o tempo médio entre a publicação de uma falha crítica e a sua correcção?

*Referência técnica: Dependências (Cap. 05) + Containers (Cap. 09)*

---

### 4 - Controlos que nunca podem falhar

**A pergunta:** existem credenciais de acesso expostas em código, ou autorizações de risco que já expiraram sem renovação?

Dois controlos cujo único valor aceitável é zero - não "poucos", não "em processo de resolução", mas zero:

- **Credenciais expostas não rotacionadas:** palavras-passe, tokens de acesso, chaves de cifra ou certificados encontrados em repositórios de código ou sistemas de automação, sem que o acesso tenha sido invalidado. O risco é imediato e o dano pode ser irrecuperável.
- **Autorizações de risco caducadas:** excepções a controlos de segurança que foram aprovadas com prazo definido e cujo prazo passou sem renovação ou encerramento. Representam controlos que a organização decidiu conscientemente não aplicar - e depois esqueceu.

**Objectivo:** zero em ambos, a todos os níveis de risco. Qualquer valor não-zero activa o semáforo vermelho e requer acção imediata.

**Quando está vermelho, a pergunta a fazer:** existem processos automáticos de detecção de credenciais expostas? Existe um inventário activo de todas as excepções aprovadas com data de expiração?

*Referência técnica: Desenvolvimento seguro (Cap. 06) + Governação (Cap. 14)*

---

### 5 - Velocidade de detecção

**A pergunta:** quando ocorre um incidente ou ataque, quanto tempo passa até sabermos?

O tempo que decorre entre um ataque e a sua detecção determina o tamanho do dano. Um ataque detectado em minutos pode ser contido; um ataque que passa semanas sem ser visto pode comprometer toda a infraestrutura. Este indicador mede a eficácia dos sistemas de monitorização e alerta - não a quantidade de alertas, mas a velocidade com que eventos reais são sinalizados.

**Objectivo:** L1 ≤ 24 horas, L2 ≤ 4 horas, L3 ≤ 30 minutos - para eventos de severidade alta ou crítica.

**Quando está vermelho, a pergunta a fazer:** os sistemas críticos têm monitorização centralizada activa? Os alertas estão calibrados para o contexto da organização ou são os valores por omissão das ferramentas?

*Referência técnica: OPS-K03 (Cap. 12 - Monitorização e Operações)*

---

### 6 - Velocidade de resposta

**A pergunta:** depois de detectado o incidente, quanto tempo passa até a organização agir?

Detectar um incidente não resolve o problema - a resposta é que limita o dano. Este indicador mede o tempo entre o alerta e a primeira acção concreta de contenção: isolamento de sistemas, bloqueio de acesso, activação de plano de resposta. Detectar depressa e reagir tarde é tão perigoso como não detectar.

**Objectivo:** L1 ≤ 48 horas, L2 ≤ 4 horas, L3 ≤ 1 hora - para eventos de severidade alta ou crítica.

**Leitura conjunta com o indicador 5:** velocidade de detecção alta com velocidade de resposta baixa aponta para falta de capacidade operacional ou de processos de resposta; o problema não é a tecnologia de monitorização, é a organização de resposta a incidentes.

*Referência técnica: OPS-K04 (Cap. 12 - Monitorização e Operações)*

---

### 7 - Formação das equipas

**A pergunta:** as pessoas que desenvolvem e operam os sistemas têm conhecimentos de segurança actualizados?

A maioria dos incidentes de segurança tem origem em erro humano - uma configuração errada, um padrão de código inseguro, uma decisão tomada sem conhecimento das implicações. A formação em segurança é o investimento de menor custo e maior impacto na redução deste risco. "Actualizada" significa realizada ou renovada no último ano - formação de há três anos não cobre as ameaças actuais.

**Objectivo:** L1 ≥ 80%, L2 ≥ 90%, L3 = 100% das equipas com formação actualizada.

**Quando está vermelho, a pergunta a fazer:** existe um plano de formação com ciclo definido? A formação é obrigatória ou voluntária? Existe rastreamento de quem completou e quando?

*Referência técnica: TRN-K01 (Cap. 13 - Formação e Onboarding)*

---

### 8 - Validação independente

**A pergunta:** as aplicações mais críticas foram testadas por alguém de fora da organização?

Os processos internos de segurança validam que os controlos existem - mas não garantem que são eficazes contra um adversário real. Uma avaliação independente - teste de intrusão, revisão de arquitectura por entidade externa, exercício de red team - fornece a perspectiva que os processos internos não conseguem dar: a de quem tenta activamente comprometer o sistema. Para sistemas L2 e L3, esta validação é parte da garantia razoável que a direcção e o board precisam de ter.

**Objectivo:** não aplicável a L1; L2 ≥ 80%, L3 = 100% com avaliação independente nos últimos 12 meses.

**Quando está vermelho, a pergunta a fazer:** existe orçamento e processo para testes de segurança independentes? A calendarização é baseada no nível de risco ou é ad-hoc?

*Referência técnica: TST-K02 (Cap. 10 - Testes de Segurança)*

---

## Situações que requerem atenção imediata

As seguintes condições requerem atenção do CISO independentemente do período de revisão habitual:

| Situação | Acção mínima |
|----------|-------------|
| Credenciais expostas não invalidadas (indicador 4) | Notificação imediata ao CISO; invalidação forçada em menos de 24 horas |
| Autorizações de risco caducadas há mais de 7 dias (indicador 4) | Revisão do portfólio de excepções; renovação ou encerramento forçado |
| Tempo de resposta a incidente activo acima do dobro do objectivo (indicador 6) | Escalada de resposta; activação de plano de contingência |
| Menos de 95% das aplicações classificadas (indicador 1) | Suspender novos arranques sem classificação prévia; activar processo urgente |
| Aplicação L3 sem avaliação independente há mais de 18 meses (indicador 8) | Activar teste de segurança prioritário |

---

## Quando um indicador está vermelho - onde analisar

A visão executiva não inclui o detalhe de causa raiz - esse está nos indicadores técnicos de domínio. Quando um indicador está vermelho, a análise aprofundada faz-se aqui:

| Indicador | Onde encontrar o detalhe |
|-----------|--------------------------|
| 1 - Classificação | Cap. 01 - Classificação de Aplicações |
| 2 - Responsabilidade | Cap. 14 - Governação |
| 3 - Falhas críticas | Cap. 05 - Dependências e SBOM; Cap. 09 - Containers |
| 4 - Controlos absolutos | Cap. 06 - Desenvolvimento Seguro; Cap. 14 - Governação |
| 5 - Detecção; 6 - Resposta | Cap. 12 - Monitorização e Operações |
| 7 - Formação | Cap. 13 - Formação e Onboarding |
| 8 - Validação independente | Cap. 10 - Testes de Segurança |

Para a arquitectura completa da hierarquia de medição, ver [`kpis-arquitetura-visao-geral`](./kpis-arquitetura-visao-geral). Para o catálogo técnico completo de indicadores por domínio, ver [`kpis-governanca`](./kpis-governanca).
