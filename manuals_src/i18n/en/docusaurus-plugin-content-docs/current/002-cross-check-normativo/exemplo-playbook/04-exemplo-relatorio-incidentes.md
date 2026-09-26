---
id: exemplo-relatorio-incidentes
title: "Example: Incident Reporting"
description: Example incident reporting template aligned with the DORA RTS/ITS
tags: [exemplos, incidentes, reporte, dora, template]
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/exemplo-playbook/04-exemplo-relatorio-incidentes.md
  source_sha256: 580986b13def08feed58fd6abb06d7dd4c57cd5f3bcc59ed27616c145f3bc2bc
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 8b000beb4f071fc2ce9134b32df260450104fb1943fd6f89d272beb486e664af
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: da8c4621ee3f200794cd49e34ddc29239ba89f55effb1e5e578d388e50580b8d
  glossary_keys: [sbdtoe_sbd, validation_evaluation]
  glossary_sha256: 3a9b85df8a952c312898acf08c8c1475f977410b078c334d48a095fde978e4f9
  translated_at: 2026-09-26T17:57:34Z
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

The regulators (EBA, BCB, ESMA) will publish official ITS templates. This example:
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
DORA Art. 18 Threshold Analysis:
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
- [ ] Archive for 3+ years (audit trail)

---

## Log Retention {#retenção-de-logs}

**[Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) + DORA Art. 18 Compliance:**

```
Todos os incidentes + trilho auditoria devem ser retidos:
- Mínimo: 3 anos
- Recomendado: 5 anos
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

When the official DORA RTS/ITS are released:
1. Compare this template with the official one
2. Extend it with additional DORA fields
3. Integrate with the regulatory reporting system
4. Test audit trail integrity

---

**Version:** 1.0 (Example)  
**Date:** November 2025  
**Validation:** Await the official DORA templates
