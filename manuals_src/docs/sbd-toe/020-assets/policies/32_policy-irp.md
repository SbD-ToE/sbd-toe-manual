---
id: policy-irp
title: Política de Integração com IRP (Incident Response Plan)
description: Política organizacional que define os requisitos de integração entre a monitorização de segurança e o processo de resposta a incidentes (IRP), incluindo critérios de activação, playbooks obrigatórios, fases de resposta, notificação regulatória, post-mortem e testes periódicos, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, IRP, incident response, playbook, SOAR, contenção, notificação, post-mortem, cap12, L1, L2, L3, governance, DORA]
grupo: operacoes
sidebar_position: 32
---

# Política de Integração com IRP

## 1. Objetivo

Esta política define os requisitos para a **integração entre os sistemas de monitorização de segurança e o processo formal de resposta a incidentes (IRP)** da organização.

A detecção de um incidente de segurança só tem valor operacional quando conduz a uma resposta estruturada. Alertas sem playbooks associados tornam-se decisões ad-hoc sob pressão - precisamente quando as decisões mais importantes precisam de ser as mais rápidas e correctas. O IRP transforma a detecção em resposta: define quem faz o quê, em que ordem, com que autoridade e com que evidência.

O objetivo desta política é garantir que:

- Cada categoria de alerta de segurança tem um playbook de resposta associado
- A activação do IRP é criteriosa, proporcional e auditável
- As fases de contenção, erradicação e recuperação são executadas de forma ordenada
- A notificação regulatória é feita dentro dos prazos aplicáveis
- O post-mortem é realizado após cada incidente significativo
- Os playbooks e o próprio IRP são testados periodicamente

---

## 2. Âmbito e obrigatoriedade

| Nível | Obrigatoriedade |
|---|---|
| L1 | Recomendado; processo de resposta documentado; contactos de escalonamento definidos |
| L2 | Obrigatório; playbooks definidos; integração com sistema de gestão de incidentes; post-mortem |
| L3 | Obrigatório; playbooks automatizados (SOAR); notificação regulatória; testes semestrais; war room |

---

## 3. Critérios de activação do IRP

O IRP é activado formalmente quando um alerta ou evento de segurança é confirmado como incidente. Os critérios de activação incluem:

| Categoria | Exemplos | Activação |
|---|---|---|
| Comprometimento de credenciais | Credencial de produção exposta, acesso não autorizado confirmado | Imediata |
| Exfiltração de dados | Download anómalo de dados confirmado, PII exposta | Imediata |
| Ransomware / malware | Ficheiros encriptados, binário suspeito em execução | Imediata |
| Disponibilidade | Indisponibilidade prolongada com suspeita de causa de segurança | Após 15 minutos de impacto |
| Anomalia de segurança de alta severidade | Padrão comportamental suspeito confirmado pelo SIEM | Após triagem positiva |
| Vulnerabilidade crítica em produção | CVE Critical com exploit activo em sistema exposto | Activação preventiva |

Um alerta não confirmado não activa o IRP formalmente - activa a fase de triagem. A activação formal ocorre após confirmação.

---

## 4. Fases de resposta a incidentes

### 4.1 Triagem (T0 - ≤ 15 minutos de detecção)

- [ ] Alerta classificado: verdadeiro positivo ou falso positivo
- [ ] Severidade atribuída (P1/P2/P3)
- [ ] Responsável pelo incidente designado (Incident Commander)
- [ ] Canal de comunicação do incidente aberto (war room se P1)

### 4.2 Contenção (T1 - início imediato após confirmação)

- [ ] Acções de contenção imediata executadas (isolamento de sistema, revogação de credencial, bloqueio de IP)
- [ ] Contenção documentada com timestamp e identidade do executor
- [ ] Sem destruição de evidências durante contenção (preserve first, contain second quando possível)
- [ ] Comunicação interna ao Tech Lead, AppSec Engineer e GRC

### 4.3 Investigação

- [ ] Recolha de logs, traces e evidências relevantes
- [ ] Timeline do incidente reconstruída
- [ ] Causa raiz identificada ou hipótese de trabalho documentada
- [ ] Âmbito do impacto determinado (sistemas, dados, utilizadores afectados)

### 4.4 Erradicação

- [ ] Causa raiz eliminada (patch, revogação de acesso, remoção de malware)
- [ ] Sistemas afectados reconstruídos de zero quando há suspeita de persistência
- [ ] Verificação de que o vector de entrada foi fechado

### 4.5 Recuperação

- [ ] Sistemas restaurados com versões limpas e verificadas
- [ ] Monitorização reforçada no período pós-recuperação
- [ ] Confirmação de estado normal de operação

### 4.6 Post-mortem

- [ ] Realizado no prazo máximo de 5 dias úteis após resolução
- [ ] Participação de todas as funções envolvidas
- [ ] Análise de causa raiz (5 Whys ou equivalente)
- [ ] Plano de acções correctivas com owner e prazo
- [ ] Documento arquivado e lições aprendidas partilhadas internamente

---

## 5. Playbooks de resposta

Cada categoria de incidente deve ter um playbook que detalha as acções específicas por fase:

| Categoria de incidente | Playbook obrigatório |
|---|---|
| Credencial comprometida | Revogação, rotação, auditoria de acessos no período de exposição |
| Exfiltração de dados / PII | Contenção, análise de âmbito, notificação regulatória |
| Ransomware | Isolamento, forensics, recuperação de backup |
| Vulnerabilidade crítica em produção | Patching de emergência, contenção temporária, comunicação |
| Deploy de código malicioso | Rollback, análise da pipeline, revogação de credenciais de CI |
| Comprometimento de dependência (supply chain) | Identificação do âmbito, remoção, rebuild |

Em L3, os playbooks devem estar integrados com SOAR para automação das acções de contenção imediata (ex: bloqueio de IP, revogação de token, isolamento de pod).

---

## 6. Notificação regulatória

Alguns incidentes requerem notificação a autoridades regulatórias dentro de prazos definidos:

| Regulação | Tipo de incidente | Prazo |
|---|---|---|
| RGPD - Art. 33 | Violação de dados pessoais | ≤ 72 horas após conhecimento |
| DORA - Art. 17/19 | Incidente TIC significativo (entidade financeira) | ≤ 4 horas (relatório inicial) + 72 horas (intermédio) |
| NIS2 - Art. 23 | Incidente significativo em entidade essencial/importante | ≤ 24 horas (alerta) + 72 horas (notificação) |

:::warning
A determinação de se um incidente é notificável deve ser feita pelo GRC/Compliance com o apoio do Encarregado de Proteção de Dados (EPD/DPO) quando aplicável. O prazo começa a contar a partir do momento em que a organização tem conhecimento do incidente - não quando a causa raiz é identificada.
:::

---

## 7. Comunicação durante o incidente

- [ ] Canal dedicado ao incidente (sem ruído de outros canais)
- [ ] Incident Commander responsável pela comunicação interna e externa
- [ ] Actualizações regulares ao management em incidentes P1 (ex: a cada 30 minutos)
- [ ] Comunicação a utilizadores afectados quando aplicável - honesta e sem comprometer a investigação
- [ ] Sem comunicação pública não autorizada por membros da equipa técnica

---

## 8. Testes periódicos do IRP

| Nível | Cadência | Tipo de teste |
|---|---|---|
| L1 | Anual | Revisão tabletop (discussão de cenário) |
| L2 | Semestral | Tabletop + simulação de playbook |
| L3 | Semestral | War room com simulação activa; validação de escalonamento e notificação |

Os resultados dos testes devem ser documentados e as lacunas identificadas devem resultar em acções correctivas com prazo definido.

---

## 9. Responsabilidades

| Role | Responsabilidade |
|---|---|
| AppSec Engineer | Manter playbooks; coordenar resposta técnica; garantir preservação de evidências |
| Incident Commander (on-call sénior) | Coordenar o incidente; gerir comunicação; tomar decisões de contenção |
| DevOps / SRE | Executar acções técnicas de contenção e recuperação |
| GRC / Compliance | Determinar obrigações de notificação; contactar autoridades regulatórias; gerir post-mortem |
| Management / CISO | Ser notificado em P1; autorizar comunicações externas; aprovar declarações públicas |

---

## 10. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente real que revelou lacunas no IRP
- Alteração regulatória que modifique os prazos ou requisitos de notificação
- Resultado de teste que identifique falhas no processo de resposta

---

## 11. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 12 - Monitorização & Operações | US-04: integração com IRP; playbooks; automação |
| Política de Monitorização de Segurança (`30_policy-monitorizacao-seguranca.md`) | Detecção de incidentes |
| Política de Gestão de Alertas (`31_policy-gestao-alertas.md`) | Activação de IRP por alerta |
| NIST SP 800-61 rev.2 | Computer Security Incident Handling Guide |
| ISO/IEC 27035 | Information Security Incident Management |
| RGPD - Art. 33-34 | Notificação de violação de dados pessoais |
| DORA - Art. 17-20 | ICT incident management e reporting |
| NIS2 - Art. 23 | Incident notification obligations |
| MITRE ATT&CK | Táticas e técnicas para investigação de incidentes |
