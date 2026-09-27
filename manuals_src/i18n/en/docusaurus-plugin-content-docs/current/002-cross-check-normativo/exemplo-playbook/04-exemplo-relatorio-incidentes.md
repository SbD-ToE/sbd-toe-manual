---
id: exemplo-relatorio-incidentes
title: "Example: Incident Reporting"
description: Example incident reporting template aligned with the DORA RTS/ITS
tags: [exemplos, incidentes, reporte, dora, template]
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/exemplo-playbook/04-exemplo-relatorio-incidentes.md
  source_sha256: e4db47cdcc511e16d451f07e67b5e4c74d5a3add8a1ffbe8aa18a24bfd8e8fb7
  source_commit: 50f5914ebc90e4135e6678b2278709d5082dd237
  target_sha256: fb7bec3ed45d8ba6da062848c24b9709227d0c4999992656182cabbe6a773799
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [cra_actively_exploited_vulnerability, cra_pde, practitioner_manual, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: 8beef8d4e289efc0b7ab05a8003354655d7164bea81529fd7f6bda7fc261f24b
  translated_at: 2026-09-27T07:05:57Z
  stamped_at: 2026-09-27T07:05:57Z
  reviewed_by: null
---

# Example: Incident Report

## Context {#enquadramento}

SbD-ToE prescribes ([Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)):
- ✓ Incident detection processes
- ✓ Record, classify and document
- ✓ Complete audit trail

SbD-ToE **does NOT prescribe** specific DORA templates (ITS - Implementing Technical Standards).

This document presents an **example template** of how to structure incident reporting.

---

## ⚠️ Important Warning {#️-aviso-importante}

**This is an example** - it is not the official DORA template.

The technical standards (RTS/ITS) with the official templates are developed by the ESAs (EBA, EIOPA and ESMA), through the Joint Committee, in accordance with Article 20 of DORA. This example:
- Illustrates structuring **principles**
- May serve as an **internal baseline**
- Must be **adapted** to the final regulatory templates

---

## Incident Structure {#estrutura-de-incidente}

### 1. Identification {#1-identificação}

```
Incident ID: INC-2025-001234
Detection Date: 2025-11-13 14:23 UTC
Detection Channel: SIEM alert (WAF)
Reporter: Security Team
```

### 2. Initial Classification {#2-classificação-inicial}

```
Severity (SbD-ToE):
├─ Critical (P0): Impacto imediato em apps L3 / dados sensíveis
├─ High (P1): Impacto em apps L2 / comprometimento significativo
├─ Medium (P2): Impacto limitado / dados não-sensíveis
└─ Low (P3): Informativo

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

### 4. Impact {#4-impacto}

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

### 7. Lessons Learned {#7-lições-aprendidas}

```
What went well:
- Detection fast (SIEM)
- Team response `<`10 min
- Communication clear
- No escalation to CEO

What could improve:
- Should have had rate limiting from start (code review gap)
- CAPTCHA should be standard (not opt-in)
- Post-incident review should happen faster (within 24h)

Action Items:
1. Add rate limiting to security checklist (Dev team)
2. Schedule code review training (Security)
3. Update threat model to include brute-force (Arch)
```

### 8. DORA Compliance (Informative) {#8-conformidade-dora-informativo}

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

## Generic Template (Excel/Jira/ServiceNow) {#template-genérico-exceljiraservicenow}

This template structures incident ticketing systems:

| Field | Type | Mandatory | Description |
|-------|------|-----------|-----------|
| Incident ID | Auto-increment | Yes | Unique ID (INC-YYYY-NNNN) |
| Title | Text | Yes | Summary (max 100 chars) |
| Description | Text | Yes | Detailed description of the incident |
| Detection Date | DateTime | Yes | UTC date/time of detection |
| Reporter | Dropdown (staff) | Yes | Who reported it |
| Severity | Dropdown (P0-P3) | Yes | SbD-ToE classification |
| Category | Dropdown | Yes | Incident type |
| Affected Systems | Multi-select | Yes | Impacted apps/infra |
| Root Cause | Text | Conditional (post-investigation) | Identified cause |
| Remediation | Text | Conditional | Actions taken |
| Owner | Dropdown (team) | Yes | Responsible team |
| Status | Dropdown (Open/Investigating/Remediated/Closed) | Yes | Current status |
| Resolution Date | DateTime | Conditional (post-resolution) | When it was resolved |
| Retest Date | DateTime | Conditional | When it will be tested |
| DORA Reportable | Dropdown (Yes/No/Unknown) | Conditional (post-investigation) | Notification required? |
| Related Incidents | Multi-link | No | Related incidents |
| Attachments | Files | No | Logs, screenshots, etc. |
| Audit Trail | Read-only log | Yes | Who did what, and when |

---

## Reporting Schedule {#cronograma-de-reporte}

### Immediate (< 1 hour) {#imediato--1-hora}
- [ ] Detect and confirm
- [ ] Create a ticket
- [ ] Notify on-call

### Short term (< 24 hours) {#curto-prazo--24-horas}
- [ ] Investigation complete
- [ ] Root cause identified
- [ ] Remediation in progress

### Medium term (< 7 days) {#médio-prazo--7-dias}
- [ ] Remediation complete
- [ ] Tests validated the fix
- [ ] Lessons learned documented

### Compliance (as per DORA) {#compliance-conforme-dora}
- [ ] DORA analysis (reportable?)
- [ ] Notification to the competent authority (if applicable)
- [ ] Archived in line with Policy 06 §10 (1 year at L1/L2, 3 years at L3; audit trail)

---

> 📌 **CRA in parallel.** If the incident involves an actively exploited vulnerability, or a severe incident, in a product with digital elements that the organisation places on the market, the CRA also applies, Article 14 (since 11 September 2026): early warning notification ≤24 h, notification ≤72 h and final report, to the CSIRT designated as coordinator and to ENISA, via the single reporting platform.

## Log Retention {#retenção-de-logs}

**Compliance [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) (DORA: Delegated Regulation (EU) 2024/1774, Art. 22, point (d) — period defined by the entity, commensurate with criticality and no longer than necessary). The values below are the Manual's choice, in line with [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) and [Policy 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs):**

```
Registos de incidentes (timeline, post-mortem, notificações):
- L1 / L2: 1 ano
- L3: 3 anos
Trilho de auditoria: 1 ano (L1/L2), 3 anos (L3)
- Acesso: Immutable (WORM - Write Once Read Many)
- Verificação: Integridade criptográfica (hash)
```

---

## Integration with the SIEM {#integração-com-siem}

Example of automatically sending incidents from the SIEM to the ticketing system:

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

## Next Steps {#próximos-passos}

Based on the reporting technical standards already adopted under Articles 18 and 20 of DORA (Delegated Regulation (EU) 2024/1772 — classification; Delegated Regulation (EU) 2025/301 — content and time limits; Implementing Regulation (EU) 2025/302 — forms and templates):
1. Compare this template with the official one
2. Extend it with additional DORA fields
3. Integrate with the regulatory reporting system
4. Test audit trail integrity

---

**Version:** 1.0 (Example)  
**Date:** November 2025  
**Validation:** Await the official DORA templates
