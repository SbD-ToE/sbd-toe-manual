---
id: catalogo-requisitos-operacoes
title: Catálogo de Requisitos de Monitorização e Operações
description: Catálogo canónico de requisitos do programa de monitorização e operações de segurança (OPS-001 a OPS-010), com aplicabilidade por nível de risco e critérios de aceitação para logging centralizado, eventos críticos, retenção, SIEM, alertas, SLA de resposta, correlação, integração com IRP, detecção comportamental e métricas de eficácia.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:operacoes, OPS, monitorizacao, SIEM, alertas, IRP, correlacao, MTTD, MTTR, rastreabilidade, L1, L2, L3, auditoria]
sidebar_position: 0
---

<!--template: sbdtoe-addon -->

# Catálogo de Requisitos de Monitorização e Operações

## Âmbito: o programa de monitorização como controlo operacional

Este catálogo cobre **requisitos do programa de monitorização e operações de segurança** — os controlos que garantem visibilidade contínua sobre o estado de segurança em produção, capacidade de deteção de eventos anómalos e integração com processos formais de resposta a incidentes.

É importante distinguir este catálogo do domínio `LOG-` do Cap. 02: o `LOG-` define as **propriedades do logging como requisito do software** (o que a aplicação deve registar, como proteger a integridade dos logs); o `OPS-` define os **controlos do programa operacional** que recebe, processa, correlaciona e actua sobre esses logs — SIEM, alertas, IRP, métricas. Ambos são necessários e complementares.

Para o mapeamento completo de todos os catálogos de requisitos do SbD-ToE por domínio técnico, prefixo canónico e responsável, consultar [Cap. 02 — Mapeamento de Catálogos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

O âmbito inclui: centralização e persistência de logs em produção, definição de eventos críticos de segurança, retenção conforme política e requisitos regulatórios, integração com SIEM, alertas automáticos com thresholds e SLA de resposta, correlação de eventos entre fontes, integração com processo de resposta a incidentes, deteção comportamental e medição de eficácia operacional.

> **Sobre a curadoria:** Consolidado a partir de NIST SP 800-137 (Continuous Monitoring), NIST SP 800-61 (Incident Response), CIS Controls v8 (Controls 8, 13, 17), MITRE ATT&CK (Detection coverage), DORA (Art. 10, monitorização operacional) e boas práticas de SOC moderno. Deve ser adaptado ao contexto de plataforma de monitorização em uso e revisto com cada ciclo de maturidade de segurança operacional.

Para instanciação em projecto e nomenclatura operacional (`SEC-Lx-OPS-CODIGO`), ver [Taxonomia e Rastreabilidade](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Convenções

| Símbolo | Significado |
|---------|-------------|
| ✔ | Requisito obrigatório para este nível |
| — | Não aplicável ou não obrigatório a este nível |

Os níveis são cumulativos: L3 inclui todos os requisitos de L1 e L2; L2 inclui todos os de L1.

---

## Catálogo OPS — Monitorização e Operações

Requisitos que garantem que a organização tem visibilidade operacional efectiva sobre os seus sistemas em produção, com capacidade de deteção, correlação e resposta proporcionais ao risco.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| OPS-001 | Logging estruturado e persistente para todos os componentes em produção | ✔ | ✔ | ✔ | Logs de todos os componentes em produção em formato estruturado (JSON, CEF ou equivalente); persistidos fora da instância (não apenas locais); acessíveis sem acesso directo ao host; cobertura verificável por inventário. |
| OPS-002 | Catálogo de eventos críticos de segurança definido e verificado | ✔ | ✔ | ✔ | Catálogo de eventos críticos definido por aplicação (autenticação, alteração de permissões, erros de autorização, acessos a dados sensíveis, etc.); evidência de que esses eventos são efectivamente gerados e retidos; revisto com cada release significativo. |
| OPS-003 | Retenção de logs conforme política e requisitos regulatórios | — | ✔ | ✔ | Política de retenção documentada por tipo de log e contexto regulatório aplicável; logs retidos pelo período mínimo obrigatório; processo de arquivo e purga documentado e auditável; evidência de cumprimento disponível. |
| OPS-004 | Centralização de logs em sistema SIEM ou equivalente | — | ✔ | ✔ | Logs enviados para sistema de monitorização centralizado com ingestion verificável; sem dependência exclusiva de logs locais para análise de segurança; evidência de logs recebidos por fonte; falhas de envio detectadas e alertadas. |
| OPS-005 | Alertas automáticos para eventos de segurança críticos | — | ✔ | ✔ | Alertas configurados para eventos críticos definidos no OPS-002; thresholds documentados e revistos periodicamente; canal de notificação testado; alertas não silenciados sem justificação. |
| OPS-006 | SLA de resposta a alertas definido e medido | — | ✔ | ✔ | SLA de resposta (time-to-acknowledge e time-to-resolve) definido por severidade de alerta; métricas de MTTD e MTTR recolhidas e reportadas periodicamente; desvios ao SLA documentados e tratados. |
| OPS-007 | Integração com processo formal de resposta a incidentes | — | ✔ | ✔ | Runbooks ou playbooks de resposta definidos para tipos de alerta críticos; integração entre sistema de alertas e sistema de gestão de incidentes; evidência de activação em incidente real ou exercício documentado no último ciclo. |
| OPS-008 | Correlação de eventos entre múltiplas fontes | — | — | ✔ | Regras de correlação activas no SIEM para eventos distribuídos (ex: acesso + alteração suspeita correlacionados por session ID, IP ou user ID); dashboards ou queries que agregam eventos correlacionados disponíveis; regras documentadas e mantidas. |
| OPS-009 | Deteção comportamental e baseline de actividade normal | — | — | ✔ | Mecanismos de deteção baseados em comportamento (UEBA, baselines de actividade) activos para fontes críticas; anomalias comportamentais geram alertas accionáveis; baseline documentada, actualizada periodicamente e com processo de aprovação de desvios. |
| OPS-010 | Métricas de eficácia da monitorização medidas e revistas | — | — | ✔ | MTTD e MTTR medidos, reportados e comparados com ciclos anteriores; cobertura de alertas por tipo de evento mapeada contra o catálogo de ameaças relevantes; revisão periódica de thresholds, regras e cobertura com evidência de melhoria contínua. |

---

## Notas explicativas

- **OPS-001 vs LOG- (Cap. 02)**: LOG- define o que a aplicação deve registar e como proteger a integridade dos logs — são requisitos do software. OPS-001 define que esses logs devem ser persistidos e acessíveis na infraestrutura de monitorização — é um requisito do programa operacional. Ambos são necessários e complementares.
- **OPS-002**: O catálogo de eventos críticos deve ser definido em colaboração com as equipas de desenvolvimento e AppSec — são elas que sabem quais os eventos de negócio com implicações de segurança relevantes. Um SIEM a receber logs sem um catálogo de eventos críticos é observabilidade sem deteção.
- **OPS-004**: A falha de envio de logs para o SIEM deve ser detectada e alertada — um silêncio inesperado de uma fonte pode ser tão significativo como um alerta explícito.
- **OPS-006**: MTTD (Mean Time to Detect) e MTTR (Mean Time to Respond/Resolve) são as métricas operacionais mais directamente relevantes para a eficácia de segurança — e são as mais frequentemente ausentes em programas de monitorização maduros em tecnologia mas imaturos em processo.
- **OPS-007**: Um alerta sem playbook associado é uma notificação que cria ansiedade, não uma capacidade de resposta. A existência e o exercício periódico de playbooks é o que transforma a monitorização num controlo operacional efectivo.
- **OPS-009**: A deteção comportamental é necessariamente probabilística e contextual — não detecta ameaças conhecidas com signatures, mas anomalias que desviam de padrões estabelecidos. Exige manutenção activa das baselines e tolerância a falsos positivos contextualmente calibrada.

---

> Para domínios e taxonomia de monitorização, consultar [Domínios de Monitorização](./dominios-monitorizacao).
> Para logging centralizado, consultar [Controlos de Logging Centralizado](./controles-logging-centralizado).
> Para alertas e eventos críticos, consultar [Alertas e Eventos Críticos](./alertas-eventos-criticos).
> Para integração com SIEM, consultar [Integração com SIEM](./integracao-siem).
> Para correlação e anomalias, consultar [Correlação e Anomalias](./correlacao-anomalias).
> Para métricas e indicadores, consultar [Métricas e Indicadores](./metricas-indicadores).
> Para a matriz de controlos por nível de risco, consultar [Matriz de Controlos por Risco](./matriz-controles-por-risco).
