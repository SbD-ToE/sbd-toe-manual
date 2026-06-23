---
id: policy-monitorizacao-seguranca
title: Política de Monitorização de Segurança
description: Política organizacional que define os requisitos de monitorização de segurança em produção, incluindo definição de eventos críticos, integração com SIEM, correlação comportamental, cobertura de domínios de monitorização e revisão periódica de regras de detecção, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, monitorização, segurança, SIEM, correlação, detecção, anomalias, eventos críticos, cap12, L1, L2, L3, governance, SOC]
grupo: operacoes
sidebar_position: 30
---

# Política de Monitorização de Segurança

## 1. Objetivo

Esta política define os requisitos para a **monitorização contínua de segurança em sistemas em produção**, cobrindo a definição de eventos críticos, a integração com SIEM, a correlação comportamental e a revisão periódica das regras de detecção.

A monitorização de segurança transforma logs em inteligência operacional. Sem monitorização activa, ataques em curso, compromissos de credenciais e exfiltrações de dados podem persistir durante semanas ou meses sem serem detectados. A monitorização de segurança não é uma funcionalidade opcional de compliance - é o mecanismo primário de detecção de incidentes que não foram prevenidos pelos controlos de segurança anteriores.

O objetivo desta política é garantir que:

- Os eventos de segurança críticos estão definidos, cobertos e a ser monitorizados em produção
- A integração com SIEM permite correlação entre eventos de múltiplas fontes
- Padrões comportamentais suspeitos são detectados e geram alertas de severidade adequada
- As regras de detecção são validadas e calibradas para minimizar falsos positivos
- A cobertura de monitorização é proporcional ao nível de criticidade da aplicação

---

## 2. Âmbito e obrigatoriedade

| Nível | Obrigatoriedade |
|---|---|
| L1 | Recomendado; monitorização básica de health e erros |
| L2 | Obrigatório; eventos de segurança definidos; alertas com SLA; integração com SIEM recomendada |
| L3 | Obrigatório; monitorização completa; SIEM obrigatório; correlação comportamental; revisão trimestral |

---

## 3. Definição de eventos críticos de segurança

A lista de eventos críticos de segurança a monitorizar deve ser definida formalmente, aprovada por AppSec Engineer e revisada periodicamente. Como mínimo, deve cobrir:

### 3.1 Autenticação e acesso

| Evento | Trigger de alerta |
|---|---|
| Múltiplas falhas de autenticação (mesmo utilizador ou mesmo IP) | > 5 falhas em 5 minutos |
| Login a partir de localização geográfica nova | Primeiro acesso de país/região não habitual |
| Login fora de horário normal | Acesso fora do padrão histórico do utilizador |
| Uso de conta de serviço em contexto não esperado | Acesso a recursos fora do scope da conta |
| Elevação de privilégios | Qualquer evento de alteração de role ou permissão |
| Acesso a recursos com permissão negada (403) em volume | > threshold definido por serviço |

### 3.2 Exfiltração e acesso a dados

| Evento | Trigger de alerta |
|---|---|
| Download de volume anómalo de dados | > threshold por utilizador/sessão |
| Acesso a dados classificados fora do perfil normal | Primeiro acesso ou volume acima do habitual |
| Exportação massiva de registos | Volume superior ao threshold definido por operação |

### 3.3 Pipeline e infraestrutura

| Evento | Trigger de alerta |
|---|---|
| Deploy em produção fora de janela de mudança | Qualquer deploy fora da janela definida |
| Alteração de configuração de segurança | WAF, CORS, TLS, grupos de segurança |
| Acesso ao cofre de segredos fora do padrão | Leitura de segredos de produção em contexto de desenvolvimento |
| Job de CI/CD com anomalia (falha sistemática, tempo anómalo) | Desvio > 3σ face à baseline |

---

## 4. Domínios de monitorização

A cobertura de monitorização deve abranger os seguintes domínios, de forma proporcional ao nível:

Quando o domínio técnico inclui sinais de saúde, heartbeat, readiness/liveness probes ou mecanismo equivalente de disponibilidade operacional para serviços críticos, a obrigação canónica aplicável é [`OPS-015`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-015). Esta política mantém o foco em monitorização de segurança e correlação operacional.

| Domínio | L1 | L2 | L3 |
|---|---|---|---|
| Técnico (erros, latência, health) | Básico | Completo | Completo |
| Segurança (autenticação, autorização, anomalias) | Básico | Parcial | Completo |
| Negócio (transações críticas, fluxos de valor) | Não aplicável | Recomendado | Obrigatório |
| Conformidade (eventos auditáveis, acessos a dados regulados) | Não aplicável | Recomendado | Obrigatório |
| CI/CD e pipeline (deploys, gates, aprovações) | Recomendado | Obrigatório | Obrigatório |

---

## 5. Integração com SIEM

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Forwarder configurado (Filebeat, Fluentbit, Vector) | Não aplicável | Obrigatório | Obrigatório |
| Canal de envio seguro (TLS 1.2+, autenticação) | Não aplicável | Obrigatório | Obrigatório |
| Parsing e normalização (ECS ou schema comum) | Não aplicável | Obrigatório | Obrigatório |
| Enriquecimento com contexto (ambiente, aplicação, classificação) | Não aplicável | Recomendado | Obrigatório |
| Regras de correlação configuradas | Não aplicável | Básicas | Completas + revisão trimestral |
| Integração com SOAR (automação de resposta) | Não aplicável | Recomendado | Obrigatório |

---

## 6. Correlação comportamental

Em L3, o SIEM deve ser configurado com regras de correlação que detectem padrões comportamentais suspeitos impossíveis de detectar por evento isolado:

Exemplos de regras de correlação:

- Login bem-sucedido seguido de download massivo de dados nos 10 minutos seguintes
- Falhas de autenticação de múltiplos IPs para o mesmo utilizador (credential stuffing)
- Alteração de permissões seguida de acesso imediato a recurso anteriormente inacessível
- Deploy em produção seguido de acesso a dados sensíveis por conta de serviço nova
- Sequência de acessos 403 → tentativas com diferentes endpoints (scanning)

As regras de correlação devem ser:
- [ ] Documentadas com contexto técnico (o que detectam e porquê)
- [ ] Testadas em staging antes de ativação em produção
- [ ] Revistas trimestralmente para validade e calibração

---

## 7. Validação e tuning de regras de detecção

Alertas mal calibrados geram fadiga de alertas - que é o equivalente funcional a não ter alertas. A manutenção das regras de detecção é trabalho contínuo:

- [ ] Cada alerta tem um runbook associado que define o que fazer quando é activado
- [ ] Simulação periódica de eventos que devem activar o alerta (em staging)
- [ ] Métricas de qualidade de alertas: taxa de verdadeiros positivos, tempo de resposta, falsos positivos
- [ ] Thresholds ajustados com base em dados históricos e feedback do on-call
- [ ] Alertas não activados em 90 dias são revistos (podem ser removidos ou reformulados)

---

## 8. Revisão periódica de cobertura

| Nível | Cadência de revisão |
|---|---|
| L1 | Anual |
| L2 | Semestral |
| L3 | Trimestral |

A revisão deve cobrir:
- [ ] Eventos de segurança da lista estão todos a ser recolhidos e chegam ao SIEM
- [ ] Regras de correlação continuam válidas face a alterações de arquitectura ou comportamento
- [ ] Novos vectores de ataque relevantes para a aplicação estão cobertos
- [ ] Thresholds de alerta calibrados para o comportamento actual

---

## 9. Sinais agentic em produção {#sinais-agentic}

Quando o sistema inclui agentes AI a operar em nível A1 ou superior (Policy 38), três classes de sinais entram no escopo desta política — para além dos sinais clássicos descritos nas secções 3 e 6. Não substituem os existentes; complementam-nos para a fatia agentic.

### 9.1 *Audit events* de *tool invocation*

Cada invocação de *tool* por um agente AI emite *audit event* estruturado com:

- `timestamp` · `agent_id` · `session_id` · `mandate_ref` (Policy 38) · `autonomy_level`
- `tool` · `tool_version` · `args` (PII redactada)
- `intent_event_ref` (obrigatório em A2+; declarado pelo agente antes da acção — [`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn))
- `outcome` (success / failure / timeout / rejected_by_gate)
- `external_effect` (URL, recurso, mudança de estado em sistema externo)

Estes eventos integram-se no SIEM como qualquer outro *audit log* — não vivem num *silo* separado. Cobertura operacional: ver [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012).

### 9.2 *Token spend* / *runaway* detection

Por agente e por *mandate*, define-se *budget* de consumo do modelo (tokens, chamadas, custo) por janela temporal. Cada inferência conta para o orçamento:

- **Threshold de aviso** → alerta ao *owner*
- **Threshold máximo** → sessão pausa ou *kill-switch* dispara, conforme nível de autonomia

Detecta *loops* descontrolados, abuso, regressões de eficiência do modelo após *upgrade*. Cobertura operacional: ver [`OPS-013`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013).

### 9.3 Detecção de *jailbreak* / *off-policy actions*

Para agentes A2+, mecanismo activo que cruza sinais para detectar comportamento adversarial ou fora do *mandate*:

- **Divergência `intent` ↔ acção real** (cruzando 9.1) — o agente declarou ir fazer X, fez Y
- **Padrões adversariais conhecidos** no input do utilizador (LLM01-2025 prompt injection patterns)
- **Argumentos materialmente diferentes do esperado** na *tool call*
- **Recusas seguidas de re-tentativa diferente** — sinal de pressão multi-turn

Sinais accionáveis alimentam IR (secção 4 desta política + Cap. 12 US-04) e a *eval suite* offline (Cap. 10 §C5). Cobertura operacional: ver [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014).

### 9.4 Proporcionalidade

| Nível de risco | Sinais 9.1 | Sinais 9.2 | Sinais 9.3 |
|---|:--:|:--:|:--:|
| L1 | Recomendado para A1+ | Recomendado | — |
| L2 | Obrigatório para A1+ | Obrigatório | Recomendado |
| L3 | Obrigatório para A1+ | Obrigatório | Obrigatório (corpus actualizado conforme cadência do *mandate*) |

### 9.5 Anti-padrões

- ❌ *Tool invocation log* genérico (sem `agent_id`/`session_id`/`mandate_ref`) — perde-se a capacidade de auditar o *mandate*.
- ❌ *Budget* sem *kill-switch* operacional — alerta sem acção é teatro.
- ❌ Detector de *jailbreak* não actualizado — adversários adaptam-se; corpus tem de evoluir.
- ❌ Sinais 9.3 que ficam apenas em dashboards sem aterrar em IR — incidente não é dashboard.

---

## 10. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer | Garantir que a aplicação emite os eventos de segurança obrigatórios no formato correcto |
| DevOps / SRE | Configurar e manter forwarders; gerir integração com SIEM; monitorizar saúde do pipeline de eventos |
| AppSec Engineer | Definir eventos críticos e regras de correlação; validar cobertura; rever e calibrar alertas |
| SOC / On-Call | Responder a alertas dentro dos SLAs; escalar quando necessário; fornecer feedback para calibração |
| GRC / Compliance | Auditar cobertura de monitorização; verificar retenção; relatórios de conformidade |

---

## 11. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente em que a monitorização não detectou a actividade maliciosa em tempo útil
- Alteração significativa da arquitectura que introduza novos componentes ou fluxos
- Alteração das fontes de ameaça relevantes para a organização

---

## 12. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 12 - Monitorização & Operações | US-02, US-08, US-09, US-10: eventos, SIEM, correlação, tuning; **US-13 — telemetria agentic** |
| SbD-ToE Cap. 12 — Catálogo ([`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012), [`OPS-013`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013), [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014)) | Requisitos operacionais agentic |
| SbD-ToE Cap. 12 — [`OPS-015`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-015) | Sinais contínuos de saúde/prontidão/disponibilidade para serviços críticos |
| SbD-ToE Cap. 04 — Arquitetura Segura ([`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)) | Audit completo por *tool invocation* — origem dos sinais agentic |
| SbD-ToE Cap. 02 — Requisitos ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) | *Intent declaration* — origem do sinal 9.3 |
| Política de Logging Estruturado (`29_policy-logging-estruturado.md`) | Base de eventos para monitorização |
| Policy 38 — Mandates de Agentes AI | `mandate_ref` em audit events |
| MITRE ATLAS | `AML.M0024` AI Telemetry Logging |
| OWASP Top 10 for LLM Applications (2025) | LLM01 Prompt Injection — corpus de detecção 9.3 |
| NIST AI RMF 1.0 — MANAGE-4.x | Revisão e revogação operacional |
| Política de Gestão de Alertas (`31_policy-gestao-alertas.md`) | SLAs e processo de resposta a alertas |
| Política de IRP (`32_policy-irp.md`) | Integração da monitorização com resposta a incidentes |
| MITRE ATT&CK | Framework de táticas e técnicas para definição de regras de detecção |
| NIST SP 800-92 | Guide to Computer Security Log Management |
| NIST SP 800-137 | Information Security Continuous Monitoring |
| ISO/IEC 27001 - A.12.4 | Logging and monitoring |
| DORA - Art. 17 | ICT-related incident detection and reporting |
