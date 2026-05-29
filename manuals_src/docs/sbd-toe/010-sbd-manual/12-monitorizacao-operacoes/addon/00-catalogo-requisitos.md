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

Este catálogo cobre **requisitos do programa de monitorização e operações de segurança** - os controlos que garantem visibilidade contínua sobre o estado de segurança em produção, capacidade de deteção de eventos anómalos e integração com processos formais de resposta a incidentes.

É importante distinguir este catálogo do domínio `LOG-` do Cap. 02: o `LOG-` define as **propriedades do logging como requisito do software** (o que a aplicação deve registar, como proteger a integridade dos logs); o `OPS-` define os **controlos do programa operacional** que recebe, processa, correlaciona e actua sobre esses logs - SIEM, alertas, IRP, métricas. Ambos são necessários e complementares.

Para o mapeamento completo de todos os catálogos de requisitos do SbD-ToE por domínio técnico, prefixo canónico e responsável, consultar [Cap. 02 - Mapeamento de Catálogos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

O âmbito inclui: centralização e persistência de logs em produção, definição de eventos críticos de segurança, retenção conforme política e requisitos regulatórios, integração com SIEM, alertas automáticos com thresholds e SLA de resposta, correlação de eventos entre fontes, integração com processo de resposta a incidentes, deteção comportamental e medição de eficácia operacional.

> **Sobre a curadoria:** Consolidado a partir de NIST SP 800-137 (Continuous Monitoring), NIST SP 800-61 (Incident Response), CIS Controls v8 (Controls 8, 13, 17), MITRE ATT&CK (Detection coverage), DORA (Art. 10, monitorização operacional) e boas práticas de SOC moderno. Deve ser adaptado ao contexto de plataforma de monitorização em uso e revisto com cada ciclo de maturidade de segurança operacional.

Para instanciação em projecto e nomenclatura operacional (`SEC-Lx-OPS-CODIGO`), ver [Taxonomia e Rastreabilidade](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Convenções

| Símbolo | Significado |
|---------|-------------|
| ✔ | Requisito obrigatório para este nível |
| - | Não aplicável ou não obrigatório a este nível |

Os níveis são cumulativos: L3 inclui todos os requisitos de L1 e L2; L2 inclui todos os de L1.

---

## Catálogo OPS - Monitorização e Operações

Requisitos que garantem que a organização tem visibilidade operacional efectiva sobre os seus sistemas em produção, com capacidade de deteção, correlação e resposta proporcionais ao risco.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| OPS-001 | Logging estruturado e persistente para todos os componentes em produção | ✔ | ✔ | ✔ | Logs de todos os componentes em produção em formato estruturado (JSON, CEF ou equivalente); persistidos fora da instância (não apenas locais); acessíveis sem acesso directo ao host; cobertura verificável por inventário. |
| OPS-002 | Catálogo de eventos críticos de segurança definido e verificado | ✔ | ✔ | ✔ | Catálogo de eventos críticos definido por aplicação (autenticação, alteração de permissões, erros de autorização, acessos a dados sensíveis, etc.); evidência de que esses eventos são efectivamente gerados e retidos; revisto com cada release significativo. |
| OPS-003 | Retenção de logs conforme política e requisitos regulatórios | - | ✔ | ✔ | Política de retenção documentada por tipo de log e contexto regulatório aplicável; logs retidos pelo período mínimo obrigatório; processo de arquivo e purga documentado e auditável; evidência de cumprimento disponível. |
| OPS-004 | Centralização de logs em sistema SIEM ou equivalente | - | ✔ | ✔ | Logs enviados para sistema de monitorização centralizado com ingestion verificável; sem dependência exclusiva de logs locais para análise de segurança; evidência de logs recebidos por fonte; falhas de envio detectadas e alertadas. |
| OPS-005 | Alertas automáticos para eventos de segurança críticos | - | ✔ | ✔ | Alertas configurados para eventos críticos definidos no OPS-002; thresholds documentados e revistos periodicamente; canal de notificação testado; alertas não silenciados sem justificação. |
| OPS-006 | SLA de resposta a alertas definido e medido | - | ✔ | ✔ | SLA de resposta (time-to-acknowledge e time-to-resolve) definido por severidade de alerta; métricas de MTTD e MTTR recolhidas e reportadas periodicamente; desvios ao SLA documentados e tratados. |
| OPS-007 | Integração com processo formal de resposta a incidentes | - | ✔ | ✔ | Runbooks ou playbooks de resposta definidos para tipos de alerta críticos; integração entre sistema de alertas e sistema de gestão de incidentes; evidência de activação em incidente real ou exercício documentado no último ciclo. |
| OPS-008 | Correlação de eventos entre múltiplas fontes | - | - | ✔ | Regras de correlação activas no SIEM para eventos distribuídos (ex: acesso + alteração suspeita correlacionados por session ID, IP ou user ID); dashboards ou queries que agregam eventos correlacionados disponíveis; regras documentadas e mantidas. |
| OPS-009 | Deteção comportamental e baseline de actividade normal | - | - | ✔ | Mecanismos de deteção baseados em comportamento (UEBA, baselines de actividade) activos para fontes críticas; anomalias comportamentais geram alertas accionáveis; baseline documentada, actualizada periodicamente e com processo de aprovação de desvios. |
| OPS-010 | Métricas de eficácia da monitorização medidas e revistas | - | - | ✔ | MTTD e MTTR medidos, reportados e comparados com ciclos anteriores; cobertura de alertas por tipo de evento mapeada contra o catálogo de ameaças relevantes; revisão periódica de thresholds, regras e cobertura com evidência de melhoria contínua. |
| OPS-011 | Observabilidade dedicada a componentes AI/ML em produção | - | ✔ | ✔ | Sistemas com componentes AI/ML em produção (LLMs, modelos preditivos, RAG, agentes autónomos) têm telemetria dedicada: logging completo de inputs e outputs do modelo (com sanitização de PII); logging de tool invocations em agentes com agent identity, scope e contexto (`AML.M0024` AI Telemetry Logging); registo de drift de comportamento e degradação de precisão; alertas para anomalias de prompt input (potencial prompt injection); audit trail completo de model versions deployed e dataset versions usados em inferência. Os logs são integrados no SIEM/observability pipeline existente (OPS-004); a deteção de anomalias específicas a AI/ML (drift, prompt injection patterns, exfiltration via tool calls) é tratada em OPS-009 com baselines AI-aware. |
| OPS-012 | Audit completo por *tool invocation* de agente AI | - | ✔ | ✔ | Para cada agente AI em nível A1+ (ver [Cap. 02 — A0-A4](../../requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia)) em uso operacional, cada *tool call* gera *audit event* estruturado com `timestamp`, `agent_id`, `session_id`, `mandate_ref` (Policy 38), `autonomy_level`, `tool`, `tool_version`, `args` (PII redactada), `intent_event_ref` (`REQ-AGN-004` em A2+), `outcome`, `external_effect`. Eventos integrados no SIEM (OPS-004); divergência entre `intent` declarado e acção real gera alerta accionável; reúne-se a base para auditoria do `mandate_ref` e para reconstrução *post-mortem* de qualquer sessão. |
| OPS-013 | Budget e detecção de *runaway* em consumo de modelo (token spend) | - | ✔ | ✔ | Por agente e por mandate, define-se *budget* máximo de consumo por janela temporal (tokens, chamadas, custo); cada inferência conta para o orçamento; ao atingir threshold de aviso, alerta vai ao *owner*; ao atingir threshold máximo, sessão pausa ou *kill-switch* é accionado conforme nível de autonomia. Métricas de uso reportadas com cadência da revisão do *mandate*. Detecta *loops* descontrolados, abuso, regressões de eficiência do modelo após *upgrade*. |
| OPS-014 | Detecção de *jailbreak* / *off-policy actions* em produção | - | - | ✔ | Para agentes A2+, mecanismo activo de detecção de tentativas de *jailbreak* (LLM01-2025) e *off-policy actions* — acções fora do *scope* declarado no *mandate*. Sinais incluem: divergência entre `intent` declarado e acção real (cross-link OPS-012), padrões adversariais conhecidos no input, *tool call* com argumentos materialmente diferentes do esperado, recusas do modelo seguidas de tentativa diferente do utilizador. Eventos accionáveis alimentam IR (OPS-007) e a *eval suite* offline (Cap. 10 §C5). Para sistemas L3 com componente AI, deteção é obrigatória — para A4 com *mandate* assinado, é actualizada com cadência declarada no *mandate*. |

---

## Notas explicativas

- **OPS-001 vs LOG- (Cap. 02)**: LOG- define o que a aplicação deve registar e como proteger a integridade dos logs - são requisitos do software. OPS-001 define que esses logs devem ser persistidos e acessíveis na infraestrutura de monitorização - é um requisito do programa operacional. Ambos são necessários e complementares.
- **OPS-002**: O catálogo de eventos críticos deve ser definido em colaboração com as equipas de desenvolvimento e AppSec - são elas que sabem quais os eventos de negócio com implicações de segurança relevantes. Um SIEM a receber logs sem um catálogo de eventos críticos é observabilidade sem deteção.
- **OPS-004**: A falha de envio de logs para o SIEM deve ser detectada e alertada - um silêncio inesperado de uma fonte pode ser tão significativo como um alerta explícito.
- **OPS-006**: MTTD (Mean Time to Detect) e MTTR (Mean Time to Respond/Resolve) são as métricas operacionais mais directamente relevantes para a eficácia de segurança - e são as mais frequentemente ausentes em programas de monitorização maduros em tecnologia mas imaturos em processo.
- **OPS-007**: Um alerta sem playbook associado é uma notificação que cria ansiedade, não uma capacidade de resposta. A existência e o exercício periódico de playbooks é o que transforma a monitorização num controlo operacional efectivo.
- **OPS-009**: A deteção comportamental é necessariamente probabilística e contextual - não detecta ameaças conhecidas com signatures, mas anomalias que desviam de padrões estabelecidos. Exige manutenção activa das baselines e tolerância a falsos positivos contextualmente calibrada.
- **OPS-011**: A observabilidade de AI/ML difere de logging tradicional em três dimensões: (1) **dimensionalidade do input** — prompts são texto livre arbitrariamente complexo, exigindo logging com sanitização de PII e potencialmente decisões de retenção diferenciadas; (2) **observabilidade probabilística** — model outputs variam por design; o sinal de anomalia não é "output ≠ esperado" mas "output ≠ baseline estatística" (drift, degradação de precisão, distribuição de confidências); (3) **agentic action audit** — quando o modelo invoca tools backend (ex: via MCP, function calling), cada invocação é uma acção com impacto operacional que deve ser tratada como audit event de primeira ordem, não como sub-evento do model call. Para arquitectura AI/ML que origina estes eventos, ver [Cap. 04 — §AI/ML](../../arquitetura-segura/recomendacoes-avancadas#ai-ml).
### Nota detalhada — OPS-012 {#ops-012}

Especializa OPS-011 para o caso *agentic*. Cada *tool invocation* tem **três identidades em jogo** que importa registar: o agente (`agent_id`), a sessão (`session_id`) e o *mandate* sob o qual o agente opera (`mandate_ref`). Sem as três, o *audit trail* não permite reconstruir *quem*, *quando* e *com que autoridade*. Em sistemas A2+, o cruzamento entre `intent_event_ref` (declarado pelo agente antes da acção) e o resultado real (`outcome`/`external_effect`) é o que torna *off-policy actions* detectáveis em tempo útil — ver OPS-014.
### Nota detalhada — OPS-013 {#ops-013}

O risco operacional dos LLMs em produção tem duas faces: (a) *correctness* — coberta por OPS-011 (drift, precisão); (b) *consumo* — coberta aqui. Em agentes com tool-use e *loops* multi-passo, o consumo pode escalar exponencialmente em poucos segundos (e.g. um agente em *retry loop* a chamar 20 *tools* por iteração). Sem budget operacional, descobre-se o problema na factura mensal; com budget, alerta no momento e *kill-switch* dispara antes de impacto material.
### Nota detalhada — OPS-014 {#ops-014}

Esta é a contraparte operacional do controlo arquitectónico `ARC-015` (Cap. 04). O *intent declaration* (`REQ-AGN-004`) cria a *evidência*; OPS-014 cria a *deteção*. Em A4 obriga-se actualização periódica do corpus de detecção porque adversários adaptam-se às defesas — não é um *one-time setup*. O sinal aterra em IR (OPS-007) como qualquer outro incidente.

---

> Para domínios e taxonomia de monitorização, consultar [Domínios de Monitorização](./dominios-monitorizacao).
> Para logging centralizado, consultar [Controlos de Logging Centralizado](./controles-logging-centralizado).
> Para alertas e eventos críticos, consultar [Alertas e Eventos Críticos](./alertas-eventos-criticos).
> Para integração com SIEM, consultar [Integração com SIEM](./integracao-siem).
> Para correlação e anomalias, consultar [Correlação e Anomalias](./correlacao-anomalias).
> Para métricas e indicadores, consultar [Métricas e Indicadores](./metricas-indicadores).
> Para a matriz de controlos por nível de risco, consultar [Matriz de Controlos por Risco](./matriz-controles-por-risco).
