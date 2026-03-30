---
id: policy-gestao-alertas
title: Política de Gestão de Alertas
description: Política organizacional que define os requisitos para a configuração, classificação, SLAs de resposta, escalonamento, runbooks e calibração de alertas de segurança e operacionais, incluindo prevenção de fadiga de alertas e métricas de qualidade, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, alertas, SLA, on-call, runbook, escalamento, fadiga de alertas, SIEM, cap12, L1, L2, L3, governance, operações]
grupo: operacoes
sidebar_position: 31
---

# Política de Gestão de Alertas

## 1. Objetivo

Esta política define os requisitos para a **gestão do ciclo de vida completo de alertas** - desde a configuração e classificação, passando pelo SLA de resposta e escalonamento, até à calibração e eliminação de alertas que não cumprem o seu propósito.

Um alerta sem prazo de resposta é apenas ruído. Um sistema com centenas de alertas activos que ninguém responde está pior do que um sistema sem alertas - criou a ilusão de monitorização sem a substância. A fadiga de alertas (alert fatigue) é uma das causas mais documentadas de incidentes não detectados: quando tudo alerta, nada alerta. A gestão eficaz de alertas é uma prática disciplinada de signal/noise ratio, não de acumulação de regras.

O objetivo desta política é garantir que:

- Cada alerta tem um SLA de resposta definido e testado
- Cada alerta tem um runbook associado que guia a resposta
- O escalonamento automático actua quando o SLA é excedido
- Métricas de qualidade de alertas são acompanhadas e usadas para calibração
- A fadiga de alertas é monitorizada e corrigida activamente

---

## 2. Âmbito

Esta política aplica-se a todos os alertas de segurança e operacionais configurados nos sistemas de monitorização, SIEM, APM e plataformas de on-call da organização.

---

## 3. Classificação de alertas

Todos os alertas devem ser classificados por severidade, que determina o SLA de resposta e o canal de notificação:

| Severidade | Critério | SLA de primeira resposta | Canal |
|---|---|---|---|
| **P1 - Critical** | Impacto imediato em produção ou comprometimento de segurança confirmado | ≤ 5 minutos | PagerDuty/OpsGenie (ligação) + Slack |
| **P2 - High** | Impacto significativo em produção ou anomalia de segurança de alta severidade | ≤ 15 minutos | PagerDuty/OpsGenie + Slack |
| **P3 - Medium** | Degradação de serviço ou anomalia que requer atenção mas não causa impacto imediato | ≤ 60 minutos | Slack + ticket |
| **P4 - Low** | Evento informativo com potencial de degradação se ignorado | ≤ 4 horas (horário laboral) | Ticket |

---

## 4. Runbooks obrigatórios

Cada alerta configurado deve ter um **runbook** associado que guia a resposta:

| Conteúdo mínimo do runbook | Descrição |
|---|---|
| O que este alerta detecta | Descrição clara do evento ou condição |
| Como verificar (diagnóstico) | Passos concretos para confirmar se é verdadeiro positivo |
| Contexto normal vs anómalo | O que é comportamento normal para distinguir do anómalo |
| Acções imediatas | O que fazer nos primeiros 5 minutos |
| Escalonamento | Para quem escalar e em que condições |
| Links relevantes | Dashboard, logs, playbook de incidente se aplicável |

Runbooks sem os campos mínimos ou com mais de 6 meses sem revisão são tratados como desactualizados e o alerta é candidato a revisão.

---

## 5. Escalonamento automático

Quando o SLA de primeira resposta é excedido sem acção registada, o alerta deve ser escalado automaticamente:

| Nível | L1 | L2 | L3 |
|---|---|---|---|
| Escalonamento automático por SLA excedido | Não aplicável | Obrigatório (para Tech Lead) | Obrigatório (para Tech Lead + AppSec/GRC) |
| Notificação a gestor quando P1 persiste > 30 minutos | Não aplicável | Recomendado | Obrigatório |

A cadeia de escalonamento deve ser documentada e testada periodicamente (pelo menos uma vez por semestre).

---

## 6. Prevenção de fadiga de alertas

A fadiga de alertas é um risco operacional que deve ser monitorizado e gerido activamente:

### 6.1 Métricas de qualidade de alertas

As seguintes métricas devem ser acompanhadas mensalmente:

| Métrica | Descrição | Target |
|---|---|---|
| Taxa de verdadeiros positivos (TVP) | % de alertas P1/P2 que correspondem a incidentes reais | > 70% |
| Taxa de falsos positivos (TFP) | % de alertas P1/P2 que são ruído | &lt; 30% |
| Tempo médio de resposta | Tempo médio entre alerta e primeira acção registada | ≤ SLA por severidade |
| Alertas sem acção em 24h | Número de alertas P3/P4 sem acção em 24h | &lt; 10% |
| Volume total de alertas por dia | Indicador de ruído sistémico | Trend descendente ou estável |

### 6.2 Critérios de intervenção

Se as métricas de qualidade piorarem sistematicamente:

- [ ] Revisão de thresholds dos alertas com maior taxa de falsos positivos
- [ ] Suspensão de alertas com TVP < 30% até recalibração
- [ ] Aggregation de alertas correlacionados num único evento
- [ ] Remoção de alertas que nunca originaram acção em 90 dias

---

## 7. Alertas P1 em horas não laborais (on-call)

Para sistemas L2/L3, deve existir rotação de on-call que garante disponibilidade de resposta 24/7 para alertas P1:

- [ ] Rotação de on-call documentada e conhecida pela equipa
- [ ] Primeiro on-call e segundo on-call (backup) definidos para cada período
- [ ] Ferramenta de on-call configurada com a cadeia de escalonamento
- [ ] Compensação e limites de on-call estabelecidos de acordo com política de RH

---

## 8. Revisão periódica do inventário de alertas

| Nível | Cadência | Âmbito |
|---|---|---|
| L1 | Anual | Alertas existentes; remoção de alertas obsoletos |
| L2 | Semestral | Alertas existentes + métricas de qualidade + runbooks |
| L3 | Trimestral | Alertas + métricas + runbooks + simulação de escalonamento |

A revisão deve resultar em:
- Remoção ou reformulação de alertas com TVP < 30%
- Actualização de runbooks desactualizados
- Adição de alertas para novos riscos identificados

---

## 9. Responsabilidades

| Role | Responsabilidade |
|---|---|
| DevOps / SRE | Configurar e manter alertas; gerir on-call; acompanhar métricas de qualidade |
| AppSec Engineer | Definir alertas de segurança; validar runbooks de segurança; calibrar thresholds |
| On-Call | Responder dentro do SLA; registar acção tomada; escalar quando necessário; fornecer feedback |
| Tech Lead | Garantir que a equipa tem runbooks actualizados; gerir escalamentos recebidos |
| GRC / Compliance | Auditar conformidade de SLAs; verificar cadeia de escalonamento; relatórios |

---

## 10. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente em que o alerta não foi respondido dentro do SLA
- Período com fadiga de alertas documentada (TVP < 50% durante > 30 dias)
- Alteração da ferramenta de on-call ou SIEM

---

## 11. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 12 - Monitorização & Operações | US-03, US-10: alertas com SLA, validação e tuning |
| Política de Monitorização de Segurança (`30_policy-monitorizacao-seguranca.md`) | Definição de eventos críticos a alertar |
| Política de IRP (`32_policy-irp.md`) | Integração de alertas com resposta a incidentes |
| PagerDuty / OpsGenie | Ferramentas de on-call e gestão de alertas de referência |
| Site Reliability Engineering (Google SRE Book) | Alert Philosophy, SLO-based alerting |
| NIST SP 800-61 | Computer Security Incident Handling - detecção e análise |
