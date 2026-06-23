---
id: checklist-revisao
title: Checklist - Monitorização e Operações
sidebar_label: Checklist de Revisão
sidebar_position: 20
description: Checklist de controlo binário da adoção das práticas de monitorização, alerta, resposta a incidentes e sinais contínuos de saúde operacional.
tags: [checklist, controlo, validacao, monitorizacao, deteccao, resposta, health, readiness, disponibilidade]
---


# Checklist de Revisão - Capítulo 12: Monitorização e Operações

Este checklist aplica-se a todas as aplicações que requeiram capacidade de **logging estruturado, alertas automáticos, correlação de eventos, sinais de saúde operacional e resposta a incidentes**.
Serve como instrumento de verificação binária e auditável da **adoção prática das prescrições do Capítulo 12** (`OPS-001` a `OPS-015`), permitindo:

- Controlo contínuo da aplicação proporcional das práticas de monitorização;
- Verificação sistemática por projeto ou aplicação;
- Geração de indicadores operacionais e de maturidade organizacional.

> 🗓️ **Recomenda-se a sua execução por release, por alteração de domínios monitorizados ou após incidentes relevantes.**

---

## 📋 Itens de Verificação

| Item                                                                                                            | Verificado? |
|-----------------------------------------------------------------------------------------------------------------|-------------|
| Todos os componentes em produção emitem logs estruturados (JSON/CEF/ECS) persistidos fora da instância, com os campos mínimos normalizados e sem dados sensíveis em claro? (`OPS-001`) | ☐           |
| Existe catálogo de eventos críticos de segurança por aplicação, com evidência de que são gerados e retidos, e os domínios de monitorização mapeados? (`OPS-002`) | ☐           |
| A integridade dos logs está protegida (retenção WORM, acesso restrito e auditado, assinatura/hash, função de logging isolada)? | ☐           |
| Existe política de retenção de logs por tipo e contexto regulatório, com retenção mínima cumprida e arquivo/purga auditável? (`OPS-003`) | ☐           |
| Os logs são centralizados num SIEM com ingestão verificável, transporte TLS+autenticação, buffering no forwarder e deteção/alerta de falhas de ingestão? (`OPS-004`) | ☐           |
| Os eventos são normalizados para esquema comum com tagging por aplicação/ambiente e timestamps UTC sincronizados por NTP? | ☐           |
| Existem regras de alerta automáticas para os eventos críticos, com thresholds documentados e testadas antes de ativação? (`OPS-005`) | ☐           |
| Os falsos positivos são documentados com causa e as condições revistas periodicamente, e cada alerta crítico tem runbook associado? | ☐           |
| Existe SLA de resposta a alertas (time-to-acknowledge e time-to-resolve) definido por severidade? (`OPS-006`) | ☐           |
| Existe integração com o processo de gestão de incidentes (IRP/SOAR), com evidência de ativação de playbooks num incidente ou exercício? (`OPS-007`) | ☐           |
| Os alertas são correlacionados entre múltiplas fontes por regras ativas no SIEM, com deteção comportamental e baseline para as fontes críticas? (`OPS-008`/`OPS-009`) | ☐           |
| As regras de deteção declaram as técnicas MITRE ATT&CK que cobrem, com a versão ATT&CK em uso registada? | ☐           |
| As métricas de MTTD e MTTR são medidas e reportadas, com dashboards atualizados e evidência de melhoria contínua? (`OPS-010`) | ☐           |
| A priorização de remediação aplica EPSS e KEV sobre os SLAs por severidade, mantendo o SLA por severidade como piso? | ☐           |
| Os controlos estão ajustados ao nível de risco (L1–L3) com rastreabilidade, e as exceções à monitorização têm justificação, data de fim e controlo compensatório de visibilidade? | ☐           |
| As ações irreversíveis (purga de logs, desativação de alertas, alteração de baselines) exigem aprovação humana, e o kill-switch de alertas tem limite temporal, notificação obrigatória e RCA antes de reativar? | ☐           |
| Para serviços críticos L2/L3, existe inventário de serviços com sinal monitorizado de saúde/prontidão/disponibilidade (endpoint de saúde, heartbeat, readiness/liveness probe ou equivalente), alerta accionável e integração com incidente ou rollback quando aplicável? (`OPS-015`) | ☐           |
| Os sistemas com componentes AI/ML registam inputs/outputs do modelo (com sanitização de PII), drift, anomalias de prompt input e versões de modelo/dataset; cada tool invocation de agente (A1+) gera audit event estruturado no SIEM; existe budget de token spend com kill-switch; e existe deteção de jailbreak/off-policy para A2+? (`OPS-011` a `OPS-014`) | ☐           |
| As práticas estão integradas no ciclo de vida (pipeline, PR, release)? | ☐           |

---

## 🔄 Integração Operacional

- Este checklist pode ser usado em **auditorias técnicas, gates de release ou revisões de segurança**;
- Cada resposta afirmativa deve ser suportada por **evidência objetiva**: regras, dashboards, tickets, configs, capturas de teste;
- A proporcionalidade deve seguir a [matriz de controlo por risco](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/matriz-controles-por-risco).

> ⚠️ **Respostas negativas exigem exceção formal aprovada e justificada.**

---

## 📊 Conformidade e Governação

- Este instrumento valida a **conformidade com o Capítulo 12 - Monitorização e Operações**;
- Pode ser integrado em **ciclos de revisão regulares ou como KPI organizacional**;
- A evolução das métricas (ex: % com alertas testados, cobertura de logs, MTTD médio) reflete a **maturidade da equipa**.

> 📅 Este checklist é parte integrante do modelo canónico de controlo SbD-ToE, e suporta a governança por evidência.
