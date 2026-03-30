---
id: policy-logging-estruturado
title: Política de Logging Estruturado
description: Política organizacional que define os requisitos para a produção, formatação, centralização, retenção e protecção de logs de aplicação e de segurança, incluindo schema mínimo de eventos, eventos obrigatórios, masking de dados sensíveis, imutabilidade e integração com SIEM, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, logging, structured logging, JSON, ECS, SIEM, retenção, imutabilidade, eventos de segurança, cap12, L1, L2, L3, governance, observabilidade]
grupo: operacoes
sidebar_position: 29
---

# Política de Logging Estruturado

## 1. Objetivo

Esta política define os requisitos para a **produção, formatação, centralização, retenção e protecção de logs** em aplicações e sistemas da organização.

Logs são o registo primário do comportamento de um sistema - são a base de toda a investigação de incidentes, auditoria de conformidade e detecção de anomalias de segurança. Logs descentralizados, não normalizados ou sem garantias de integridade não cumprem este papel: são ruído, não evidência. A transição de logging ad-hoc para logging estruturado centralizado é uma mudança de paradigma - não de ferramenta.

O objetivo desta política é garantir que:

- Todos os sistemas produzem logs em formato estruturado e normalizado
- Os eventos de segurança obrigatórios são sempre registados, independentemente do nível
- Dados sensíveis e PII nunca aparecem em logs sem masking adequado
- Logs são centralizados, imutáveis em L3, e retidos pelos prazos definidos
- A correlação de logs entre sistemas é possível via trace ID e campos comuns

---

## 2. Âmbito e obrigatoriedade

Esta política aplica-se a todos os sistemas em execução que produzam eventos relevantes para segurança, operação ou auditoria. Inclui aplicações web, APIs, workers, jobs, pipelines CI/CD, infraestrutura e sistemas de autenticação.

| Nível | Obrigatoriedade |
|---|---|
| L1 | Logging básico; formato estruturado recomendado; centralização recomendada |
| L2 | Obrigatório; formato JSON estruturado; eventos de segurança obrigatórios; centralização; retenção mínima |
| L3 | Obrigatório; JSON/ECS; eventos completos; centralização + SIEM; WORM; retenção regulatória |

---

## 3. Formato de logging

### 3.1 Formato obrigatório

Em L2/L3, todos os logs devem ser produzidos em formato **JSON** (ou compatível com Elastic Common Schema - ECS), legível por máquina e processável sem parsing personalizado:

- Sem logs em texto livre não estruturado em componentes críticos
- Sem múltiplos formatos de log no mesmo sistema sem normalização na ingestão

### 3.2 Schema mínimo de evento

Cada evento de log deve conter, no mínimo, os seguintes campos:

| Campo | Exemplo | Obrigatório |
|---|---|---|
| `timestamp` | `2025-07-21T10:35:14.321Z` | Sim; ISO 8601 UTC |
| `level` | `INFO`, `WARN`, `ERROR`, `DEBUG` | Sim; níveis padronizados |
| `event.action` | `user.login`, `file.upload`, `api.call` | Sim em L2/L3; taxonomia consistente |
| `application` | `api-gateway`, `worker-payment` | Sim; componente lógica |
| `environment` | `production`, `staging` | Sim |
| `trace.id` | `xyz-9876-abcd` | Sim em L2/L3; correlação entre sistemas |
| `user.id` | `usr-1234` (interno, nunca email ou nome) | Quando aplicável |
| `src.ip` | `192.168.1.20` | Em eventos de autenticação e acesso |
| `http.status_code` | `200`, `401`, `500` | Em APIs e endpoints |
| `message` | Descrição legível do evento | Sim |

---

## 4. Eventos de segurança obrigatórios

Os seguintes eventos de segurança devem ser sempre registados, independentemente do nível de criticidade da aplicação:

| Evento | Campos mínimos obrigatórios |
|---|---|
| Autenticação bem-sucedida | `user.id`, `src.ip`, `timestamp`, `method` (password/MFA/SSO) |
| Autenticação falhada | `user.id` (ou tentativa), `src.ip`, `timestamp`, `motivo` |
| Logout / expiração de sessão | `user.id`, `session.id`, `timestamp` |
| Acesso negado (403) | `user.id`, `resource`, `action`, `src.ip`, `timestamp` |
| Alteração de dados sensíveis | `user.id`, `resource`, `acção`, `valor anterior` (hash), `timestamp` |
| Alteração de permissões/papéis | `actor.id`, `target.id`, `permissão alterada`, `timestamp` |
| Operação administrativa | `actor.id`, `acção`, `target`, `timestamp` |
| Erro interno relevante | `error.type`, `error.message`, `stack trace resumido`, `trace.id` |
| Upload/download de ficheiros | `user.id`, `filename`, `size`, `method`, `timestamp` |
| Chamada a API externa | `endpoint`, `method`, `status`, `duration`, `trace.id` |

---

## 5. Proibições absolutas nos logs

Os seguintes dados nunca devem aparecer em logs, independentemente do nível:

| Dado proibido | Alternativa |
|---|---|
| Passwords, PINs, respostas a perguntas secretas | Nunca registar - nem em hash |
| Tokens de sessão, JWT completos, API keys | Registar apenas o prefixo (ex: `Bearer eyJ...` → `Bearer eyJ[redacted]`) |
| Números de cartão de crédito, IBAN | Masking obrigatório: `****-****-****-1234` |
| Dados de saúde, dados biométricos | Nunca registar em logs operacionais |
| PII directamente identificável (nome completo + morada + NIF) | Usar `user.id` interno; masking de campos PII em logs de debug |
| Segredos, chaves privadas, certificados | Nunca |

:::warning
O registo de dados sensíveis em logs de debug ou de erro é uma das fontes mais comuns de exposição de PII em sistemas em produção. Os logs de nível DEBUG devem ser desactivados em produção ou filtrados antes da ingestão centralizada.
:::

---

## 6. Centralização de logs

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Logs centralizados em sistema de logging (ELK, Loki, Splunk, etc.) | Recomendado | Obrigatório | Obrigatório |
| Pipeline de ingestão com normalização de schema | Recomendado | Obrigatório | Obrigatório |
| Correlação possível por `trace.id` entre serviços | Recomendado | Obrigatório | Obrigatório |
| Integração com SIEM | Não aplicável | Recomendado | Obrigatório |
| Logs de pipeline CI/CD centralizados | Recomendado | Obrigatório | Obrigatório |

---

## 7. Retenção de logs

| Tipo de log | L2 | L3 |
|---|---|---|
| Logs operacionais (runtime, erros) | 90 dias | 1 ano |
| Logs de segurança (autenticação, autorização, alterações) | 1 ano | 2 anos (ou conforme regulação) |
| Logs de auditoria (operações administrativas, acesso a dados sensíveis) | 1 ano | 3 anos (DORA: 5 anos) |
| Logs de pipeline CI/CD | 90 dias | 1 ano |

:::note
Em contextos regulados (DORA, NIS2, RGPD, saúde, financeiro), os prazos regulatórios prevalecem sobre os mínimos desta política. O período mais longo é sempre o aplicável.
:::

---

## 8. Integridade e imutabilidade

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Logs protegidos de modificação | Recomendado | Obrigatório | Obrigatório |
| Armazenamento WORM (Write Once, Read Many) | Não aplicável | Recomendado | Obrigatório |
| Hash ou assinatura periódica de logs | Não aplicável | Recomendado | Obrigatório |
| Acesso a logs restrito e auditado | Recomendado | Obrigatório | Obrigatório |
| Alertas em caso de tentativa de alteração ou eliminação | Não aplicável | Recomendado | Obrigatório |

---

## 9. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer | Implementar logging estruturado conforme schema; não registar dados sensíveis; usar `trace.id` |
| DevOps / SRE | Configurar pipeline de centralização; garantir retenção e imutabilidade; gerir sistema de logging |
| AppSec Engineer | Definir eventos de segurança obrigatórios; auditar logs para PII; configurar integração com SIEM |
| GRC / Compliance | Verificar conformidade com prazos de retenção regulatórios; auditar acesso a logs; relatórios |

---

## 10. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente em que logs insuficientes ou ausentes dificultaram a investigação
- Exposição de PII ou dados sensíveis em logs
- Alteração regulatória que imponha novos requisitos de retenção

---

## 11. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 12 - Monitorização & Operações | US-01 (logging estruturado), US-07 (segurança e integridade de logs) |
| Elastic Common Schema (ECS) | Schema de referência para campos normalizados |
| OWASP Logging Cheat Sheet | Boas práticas de logging seguro |
| GDPR / RGPD - Art. 5(1)(e) | Limitação de conservação de dados pessoais |
| DORA - Art. 12 | Requisitos de logging para entidades financeiras |
| NIST SP 800-92 | Guide to Computer Security Log Management |
| ISO/IEC 27001 - A.12.4 | Logging and monitoring |
