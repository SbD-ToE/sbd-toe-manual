---
id: policy-monitorizacao-pos-deploy
title: Política de Monitorização Pós-Deploy
description: Política organizacional que define os requisitos de monitorização activa após cada deploy em produção, incluindo janela de observação obrigatória, métricas de saúde mínimas, thresholds de alerta, validação humana e critérios de activação de rollback, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, monitorização, pós-deploy, observabilidade, alertas, rollback, saúde, métricas, cap11, L1, L2, L3, governance]
sidebar_position: 28
---

# Política de Monitorização Pós-Deploy

## 1. Objetivo

Esta política define os requisitos de **monitorização activa após cada deploy em produção**, cobrindo a janela de observação obrigatória, as métricas e alertas mínimos, a validação humana e os critérios de activação automática de rollback.

Um deploy não termina com a promoção bem-sucedida do artefacto — termina quando a versão está estável em produção e o seu comportamento foi verificado. Sem monitorização activa pós-deploy, anomalias podem desenvolver-se silenciosamente durante horas antes de serem detectadas por utilizadores ou por sistemas externos. A janela pós-deploy é o período de maior risco de uma release: é quando comportamentos inesperados sob carga real de produção se manifestam.

O objetivo desta política é garantir que:

- Cada deploy em produção é seguido de uma janela de observação activa com métricas e alertas configurados
- Anomalias são detectadas e classificadas automaticamente, com encaminhamento para resposta
- A validação humana do estado de saúde é realizada antes de fechar a release
- Os critérios de activação de rollback estão pré-definidos e são aplicados de forma consistente

---

## 2. Âmbito e obrigatoriedade

| Nível | Obrigatoriedade |
|---|---|
| L1 | Recomendado; monitorização básica de health check |
| L2 | Obrigatório; janela de observação definida; alertas automáticos; validação humana |
| L3 | Obrigatório; monitorização completa; resposta automática a anomalias críticas; validação humana formal |

---

## 3. Janela de observação pós-deploy

Após cada deploy em produção, deve existir uma janela de observação activa durante a qual a equipa de operações monitoriza activamente o comportamento da nova versão:

| Nível | Janela mínima de observação | Actividade durante a janela |
|---|---|---|
| L1 | 15 minutos | Verificação manual de health checks |
| L2 | 30 minutos | Monitorização de dashboards; alertas configurados; on-call disponível |
| L3 | 60 minutos (ou até primeiro ciclo de rollout completo em deploys progressivos) | Monitorização activa; critérios de rollback automático activos; on-call disponível |

Durante deploys com rollout progressivo (canary, blue-green), a janela de observação aplica-se a cada etapa de promoção.

---

## 4. Métricas de saúde mínimas

As seguintes métricas devem estar configuradas e a ser monitorizadas durante a janela de observação pós-deploy:

| Métrica | Descrição | Threshold de alerta (referência) |
|---|---|---|
| Taxa de erros HTTP 5xx | Percentagem de respostas com erro de servidor | > 1% durante 5 minutos |
| Latência P99 | Percentil 99 do tempo de resposta | > 2x baseline dos últimos 7 dias |
| Taxa de crash/restart | Número de restarts de containers/processos por minuto | > threshold definido por serviço |
| Health check endpoint | Estado do endpoint `/health` ou equivalente | Falha em ≥ 2 instâncias consecutivas |
| Throughput | Número de requests por segundo vs baseline | Queda > 30% face ao baseline sem explicação |
| Erros de autenticação/autorização | Aumento anómalo de 401/403 | > 5x baseline durante 5 minutos |

Os thresholds específicos devem ser calibrados por serviço com base no comportamento histórico.

---

## 5. Alertas e encaminhamento

Os alertas de pós-deploy devem estar configurados antes de qualquer deploy em produção — não configurados após deteção de problema:

- [ ] Alertas associados ao deployment para o período de janela de observação
- [ ] Alertas encaminhados para canal de on-call activo (não apenas email)
- [ ] Alertas identificam claramente o deployment que os originou (versão, timestamp do deploy)
- [ ] Alertas classificados por severidade com SLA de resposta definido:
  - Critical: resposta em ≤ 5 minutos
  - High: resposta em ≤ 15 minutos
  - Medium: resposta em ≤ 60 minutos

---

## 6. Critérios de activação de rollback pós-deploy

Os critérios de rollback automático devem estar pré-definidos e configurados para a janela de observação:

| Critério | Acção |
|---|---|
| Taxa de erros 5xx > threshold durante janela definida | Rollback automático (L2/L3) ou alerta para decisão humana (L1) |
| Latência P99 > 2x baseline durante janela definida | Alerta imediato; rollback se persistir após 10 minutos |
| Health check com falha persistente | Rollback automático |
| Crash loop em instâncias/pods | Rollback automático |
| Alerta de segurança activo (anomalia de runtime) | Alerta imediato; decisão humana de rollback |

O rollback automático deve ser acompanhado de notificação imediata ao on-call e registo da decisão automatizada.

---

## 7. Validação humana pós-deploy

Em L2/L3, o deploy só é considerado concluído após validação humana explícita do estado de saúde:

- [ ] Responsável pelo on-call verifica dashboards e confirma estado normal
- [ ] Verificação documentada (timestamp, identidade, estado observado)
- [ ] Se anomalias são detectadas mas não atingem thresholds de rollback automático, a decisão de manter ou reverter é humana e registada
- [ ] Release marcada como "concluída" apenas após validação positiva

---

## 8. Dashboards de monitorização pós-deploy

Os dashboards de monitorização devem estar configurados e actualizados antes de cada deploy:

- [ ] Dashboard específico de pós-deploy com métricas em tempo real e comparação com versão anterior
- [ ] Filtro por versão/deployment activo
- [ ] Visualização da janela de rollout progressivo (se aplicável)
- [ ] Histórico de deploys anteriores para comparação

---

## 9. Extensão da janela de observação

Se durante a janela de observação forem detectadas anomalias que não atingem o threshold de rollback mas causam incerteza, a janela deve ser estendida:

- [ ] Decisão de extensão registada com justificação
- [ ] Nova duração da janela definida
- [ ] On-call mantido disponível durante a extensão

---

## 10. Rastreabilidade

Cada evento relevante durante a janela de observação deve ser registado:

| Evento | Registo |
|---|---|
| Início da janela de observação | Timestamp + versão deployed + on-call responsável |
| Alerta gerado | Tipo, severidade, timestamp, métrica afectada |
| Decisão de rollback (automático ou manual) | Critério activado, timestamp, versão alvo |
| Validação humana concluída | Identidade, timestamp, estado observado |
| Fecho da janela | Timestamp + estado final (concluído, rollback, em observação estendida) |

---

## 11. Responsabilidades

| Role | Responsabilidade |
|---|---|
| DevOps / SRE | Configurar dashboards e alertas antes do deploy; monitorizar durante a janela; executar rollback se necessário |
| On-Call | Responder a alertas dentro dos SLAs; tomar decisão de rollback quando necessário; validar estado pós-deploy |
| Tech Lead | Coordenar resposta a anomalias; decidir rollback quando o on-call escalona |
| AppSec Engineer | Definir métricas de segurança a monitorizar pós-deploy; rever alertas de anomalia de segurança |
| GRC / Compliance | Auditar registos de observação pós-deploy; verificar cumprimento de janelas e SLAs |

---

## 12. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente em que uma anomalia pós-deploy não foi detectada dentro da janela de observação
- Alteração da plataforma de monitorização que afecte os dashboards ou alertas
- Alteração dos SLAs de resposta a incidentes

---

## 13. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 11 — Deploy Seguro | US-06 (monitorização pós-deploy), US-13 (validação humana) |
| Política de Deploy Seguro (`25_policy-deploy-seguro.md`) | Estratégias de rollout e critérios de promoção |
| Política de Rollback (`27_policy-rollback.md`) | Processo de rollback activado pela monitorização |
| Política de Monitorização de Segurança (`30_policy-monitorizacao-seguranca.md`) | Monitorização de segurança em produção |
| Política de Gestão de Alertas (`31_policy-gestao-alertas.md`) | SLAs de resposta a alertas |
| Site Reliability Engineering (Google SRE Book) | Práticas de monitorização e SLO/SLA |
| NIST SP 800-61 | Computer Security Incident Handling Guide |
