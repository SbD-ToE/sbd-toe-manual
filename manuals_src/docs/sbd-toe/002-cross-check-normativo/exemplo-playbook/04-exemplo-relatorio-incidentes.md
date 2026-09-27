---
id: exemplo-relatorio-incidentes
title: "Exemplo: Reporte de Incidentes"
description: Template exemplar de reporte de incidentes alinhado com DORA RTS/ITS
tags: [exemplos, incidentes, reporte, dora, template]
---

# Exemplo: Relatório de Incidentes

## Enquadramento {#enquadramento}

O SbD-ToE prescreve ([Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)):
- ✓ Processos de deteção de incidentes
- ✓ Registre, classifique e documente
- ✓ Trilho auditoria completo

O SbD-ToE **NÃO prescreve** templates específicos DORA (ITS - Implementing Technical Standards).

Este documento apresenta um **template exemplar** de como estruturar reporte de incidentes.

---

## ⚠️ Aviso Importante {#️-aviso-importante}

**Este é um exemplo** - não é o template oficial DORA.

As normas técnicas (RTS/ITS) com os modelos oficiais são elaboradas pelas AES (EBA, EIOPA e ESMA), através do Comité Conjunto, nos termos do art. 20.º do DORA. Este exemplo:
- Ilustra **princípios** de estruturação
- Pode servir como **base interna**
- Deve ser **adaptado** aos templates regulatórios finais

---

## Estrutura de Incidente {#estrutura-de-incidente}

### 1. Identificação {#1-identificação}

```
Incident ID: INC-2025-001234
Detection Date: 2025-11-13 14:23 UTC
Detection Channel: SIEM alert (WAF)
Reporter: Security Team
```

### 2. Classificação Inicial {#2-classificação-inicial}

```
Severity (SbD-ToE):
├─ Critical (P1): Impacto imediato em produção / dados sensíveis
├─ High (P2): Comprometimento significativo
├─ Medium (P3): Impacto limitado / dados não-sensíveis
└─ Low (P4): Informativo
(A severidade não depende do nível L. Trilho regulatório: qualquer
 severidade, qualquer nível; sobe no mínimo a P2 - Política 32 §4.1)

Categorization:
├─ Malware/Ransomware
├─ Unauthorized Access
├─ Data Exfiltration
├─ Denial of Service
├─ Vulnerability Exploitation
├─ Configuration Issue
├─ Operational Issue
└─ Other
```

### 3. Timeline {#3-timeline}

```
Timeline (UTC):
- 14:23 - Alert triggered (WAF logs)
- 14:25 - Manual confirmation (analyst)
- 14:30 - Team notified (on-call)
- 14:35 - Response initiated
- 14:50 - Root cause identified
- 15:10 - Remediation started
- 15:40 - Services restored
- 16:00 - Incident closed (provisional)
```

### 4. Impacto {#4-impacto}

```
Impact:
├─ Affected Systems: Gateway API (L3), Auth Service (L3)
├─ Affected Users: ~500 (active sessions)
├─ Data Exposure: None detected
├─ Downtime: 15 minutes (partial degradation, not full)
├─ Business Impact: Transactions delayed (SLA met: `<`30min recovery)
└─ Regulatory Impact: DORA Art. 18 reportable? No (within thresholds)
```

### 5. Root Cause Analysis {#5-root-cause-analysis}

```
Root Cause:
- Missing rate limiting on auth endpoint
- Attacker: Automated bot (geo: RU IP)
- Attack type: Brute force authentication
- Volume: 50k attempts in 10 min
- Success: 0 (credentials not compromised)
```

### 6. Remediation {#6-remediation}

```
Immediate Actions (done):
- [ ] Rate limiting deployed (30 req/min per IP)
- [ ] IPs blocked (30-day)
- [ ] Alerts reconfigured

Follow-up Actions (planned):
- [ ] Implement CAPTCHA on auth (Sprint 12)
- [ ] Add behavioral analysis (WAF rule)
- [ ] Training: Secure coding (auth best practices)
- [ ] Retest: Penetration testing (within 30 days)
```

### 7. Lições Aprendidas {#7-lições-aprendidas}

```
What went well:
- Detection fast (SIEM)
- Team response `<`10 min
- Communication clear
- No escalation to CEO

What could improve:
- Should have had rate limiting from start (code review gap)
- CAPTCHA should be standard (not opt-in)
- Post-incident review should happen faster (within 24h, well inside the 5 working days of Policy 32)

Action Items:
1. Add rate limiting to security checklist (Dev team)
2. Schedule code review training (Security)
3. Update threat model to include brute-force (Arch)
```

### 8. Conformidade DORA (Informativo) {#8-conformidade-dora-informativo}

```
DORA art. 18.º + Reg. Delegado (UE) 2024/1772, art. 8.º–9.º — análise de limiares: serviços críticos afetados? acesso malicioso bem-sucedido com possível perda de dados (art. 9.º, n.º 5, al. b))? clientes > 10 % ou > 100 000; transações > 10 %; duração > 24 h ou indisponibilidade > 2 h (funções críticas/importantes); ≥ 2 Estados-Membros; impacto económico > 100 000 EUR; impacto reputacional (art. 2.º)
- Availability Impact: `<`20% (low)
- Confidentiality Impact: None
- Integrity Impact: None
- Affected Customers: Not significantly
- Reputational Impact: Low
- Regulatory Notification: No (threshold not met)

Decision: Not reportable to supervisor
(But keep audit trail for demonstration)
```

---

## Template Genérico (Excel/Jira/ServiceNow) {#template-genérico-exceljiraservicenow}

Este template estrutura sistemas de tickets de incidentes:

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-----------|-----------|
| Incident ID | Auto-increment | Sim | ID único (INC-YYYY-NNNN) |
| Title | Text | Sim | Resumo (max 100 chars) |
| Description | Text | Sim | Descrição detalhada do incidente |
| Detection Date | DateTime | Sim | Data/hora UTC de detecção |
| Reporter | Dropdown (staff) | Sim | Quem reportou |
| Severity | Dropdown (P1-P4) | Sim | SbD-ToE classification |
| Category | Dropdown | Sim | Tipo de incidente |
| Affected Systems | Multi-select | Sim | Apps/infra impactados |
| Root Cause | Text | Condicional (pós-investigação) | Causa identificada |
| Remediation | Text | Condicional | Ações tomadas |
| Owner | Dropdown (team) | Sim | Equipa responsável |
| Status | Dropdown (Open/Investigating/Remediated/Closed) | Sim | Estado atual |
| Resolution Date | DateTime | Condicional (pós-resolução) | Quando foi resolvido |
| Retest Date | DateTime | Condicional | Quando será testado |
| Regulatory Track | Multi-select (RGPD/NIS2/DORA/CRA/AI Act/None/Under assessment) | Sim (na triagem; decisão ≤ 4 h) | Que notificações se aplicam e quando conta o prazo? |
| Related Incidents | Multi-link | Não | Incidentes relacionados |
| Attachments | Files | Não | Logs, screenshots, etc. |
| Audit Trail | Read-only log | Sim | Quem fez o quê, quando |

---

## Cronograma de Reporte {#cronograma-de-reporte}

### Imediato (< 1 hora) {#imediato--1-hora}
- [ ] Detectar e confirmar
- [ ] Criar ticket
- [ ] Notificar on-call
- [ ] Indício de trilho regulatório? Escalar para GRC/Compliance + EPD/DPO (≤ 1 h) e registar o momento do conhecimento

### Curto prazo (< 24 horas) {#curto-prazo--24-horas}
- [ ] Decisão de notificabilidade (≤ 4 h)
- [ ] Alerta rápido NIS2 / alerta precoce CRA (≤ 24 h após o conhecimento); notificação inicial DORA nos prazos do Reg. Delegado (UE) 2025/301
- [ ] Investigação completa
- [ ] Root cause identificado
- [ ] Remediation em progresso

### Médio prazo (< 7 dias) {#médio-prazo--7-dias}
- [ ] Remediation completa
- [ ] Testes validaram fix
- [ ] Lições aprendidas documentadas

### Compliance (relógios regulatórios) {#compliance-conforme-dora}
- [ ] RGPD: autoridade de controlo ≤ 72 h após o conhecimento (art. 33.º); titulares sem demora injustificada se houver elevado risco (art. 34.º)
- [ ] NIS2: notificação de incidente ≤ 72 h; relatório final ≤ 1 mês após a notificação
- [ ] DORA: relatório intercalar e final nos prazos do Reg. Delegado (UE) 2025/301, art. 5.º
- [ ] CRA: notificação ≤ 72 h; relatório final ≤ 14 dias após a medida corretiva (vulnerabilidade) ou ≤ 1 mês após a notificação (incidente grave)
- [ ] AI Act: incidente grave ≤ 15 dias (10 em caso de morte; 2 em caso de infração generalizada) - art. 73.º
- [ ] Post-mortem ≤ 5 dias úteis após a resolução (Política 32 §4.6)
- [ ] Arquivo conforme a Política 06 §10 (1 ano em L1/L2, 3 anos em L3; audit trail)

---

> 📌 **CRA em paralelo.** Se o incidente envolver uma vulnerabilidade ativamente explorada, ou um incidente grave, num produto com elementos digitais que a organização coloca no mercado, aplica-se também o CRA, art. 14.º (desde 11 de setembro de 2026): notificação de alerta precoce ≤24 h, notificação ≤72 h e relatório final, à CSIRT designada como coordenadora e à ENISA, através da plataforma única de comunicação de informações.

## Retenção de Logs {#retenção-de-logs}

**Conformidade [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) (DORA: Reg. Delegado (UE) 2024/1774, art. 22.º, al. d) — período definido pela entidade, proporcional à criticalidade e não superior ao necessário). Os valores abaixo são escolha do Manual, conforme a [Política 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) e a [Política 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs):**

```
Registos de incidentes (timeline, post-mortem, notificações):
- L1 / L2: 1 ano
- L3: 3 anos
Trilho de auditoria: 1 ano (L1/L2), 3 anos (L3)
- Acesso: Immutable (WORM - Write Once Read Many)
- Verificação: Integridade criptográfica (hash)
```

---

## Integração com SIEM {#integração-com-siem}

Exemplo de envio automático de incidentes do SIEM para sistema de tickets:

```json
{
  "incident_id": "INC-2025-001234",
  "timestamp": "2025-11-13T14:23:00Z",
  "title": "Potential brute-force attack on Auth endpoint",
  "source": "SIEM (Splunk)",
  "severity": "high",
  "details": {
    "endpoint": "/api/auth/login",
    "attempts": 50000,
    "unique_ips": 1,
    "geo": "RU",
    "detection_rule": "Authentication_Brute_Force"
  },
  "affected_systems": ["gateway-api", "auth-service"],
  "action_required": true,
  "assignee": "on-call-security-engineer"
}
```

---

## Próximos Passos {#próximos-passos}

Com base nas normas técnicas de reporte já adotadas ao abrigo dos art. 18.º e 20.º do DORA (Reg. Delegado (UE) 2024/1772 — classificação; Reg. Delegado (UE) 2025/301 — conteúdo e prazos; Reg. de Execução (UE) 2025/302 — formulários e modelos):
1. Comparar este template com oficial
2. Estender com campos adicionais DORA
3. Integrar com sistema de reporting regulatório
4. Testar integridade de audit trail

---

**Versão:** 1.0 (Exemplar)  
**Data:** Novembro 2025  
**Validação:** Aguardar templates DORA oficiais
