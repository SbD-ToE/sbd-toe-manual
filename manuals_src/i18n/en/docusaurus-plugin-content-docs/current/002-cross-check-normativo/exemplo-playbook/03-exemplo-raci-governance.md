---
id: exemplo-raci-governance
title: "Example: RACI and Governance"
description: Example RACI template (Responsible, Accountable, Consulted, Informed) for SbD implementation
tags: [exemplos, raci, governanca, responsabilidades, organizacao]
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/exemplo-playbook/03-exemplo-raci-governance.md
  source_sha256: 34812f2926b416c68ed0d0dbe99c97d60f18fa1109a83e607204b98501873148
  source_commit: 112711064196b71c545672fe3fb3ae412b36575e
  target_sha256: 78fd0df96c379e3000b30f3e7e722f8ad1cf2daa161dbc15a96f8bbe2eb8587c
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5f18169e44cb78faceac7d31df119020c508135f27e39f4105f054ecf5a72d33
  glossary_keys: [chapter_role, maturity, papel_suporte, role_tech_lead, sbdtoe_sbd]
  glossary_sha256: 3df7edba29d2791e2985ce72eb1907a60b6cfac5d858765719ae3865fb90e43c
  translated_at: 2026-09-26T18:12:00Z
  reviewed_by: null
---

# Example: Governance RACI

## Context {#enquadramento}

SbD-ToE prescribes ([Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)):
- ✓ Governance structure
- ✓ Clear RACI
- ✓ Formal approvals
- ✓ Segregation of responsibilities

SbD-ToE **does NOT prescribe** which organisation chart to use (it varies by sector, size and geography).

This document presents **RACI examples for different contexts**.

---

## Governance Model {#modelo-de-governo}

Security governance must have **three levels**:

```
┌──────────────────────────────────────────────────┐
│ NÍVEL EXECUTIVO: Board + Executive Committee    │
│ Função: Aprovação política, governance, risk    │
│ Frequência: Trimestral                          │
├──────────────────────────────────────────────────┤
│ NÍVEL TÁTICO: Segurança + Operações             │
│ Função: Execução, metriques, escalations        │
│ Frequência: Mensal                              │
├──────────────────────────────────────────────────┤
│ NÍVEL OPERACIONAL: Devs + SRE + Segurança      │
│ Função: Implementação diária, code review       │
│ Frequência: Contínua                            │
└──────────────────────────────────────────────────┘
```

---

## Example 1: Small Fintech (10-20 devs) {#exemplo-1-fintech-pequena-10-20-devs}

### Simplified Organisation Chart {#organigrama-simplificado}
```
CEO
├─ CTO (Chief Technology Officer)
│  ├─ Tech Lead (1 person)
│  │  └─ Developers (8-15)
│  ├─ SRE/DevOps (1-2)
│  └─ Security Champion (part-time, 0.5 FTE)
├─ Head of Compliance/GRC
│  └─ Compliance Officer
└─ CFO (Budget)
```

### RACI per Activity {#raci-por-atividade}

| Activity | CTO | Tech Lead | Security Champion | Compliance | CFO | Board |
|-----------|-----|-----------|------------------|-----------|-----|-------|
| **Governance** | | | | | | |
| Define the SbD policy | A | R | C | C | I | A |
| Approve the policy (board) | I | - | - | C | I | **A** |
| Define the RACI | R | A | C | - | - | I |
| **Planning** | | | | | | |
| Classify apps (L1-L3) | R | A | C | I | - | - |
| Allocate the security budget | I | I | I | C | **A** | I |
| **Development** | | | | | | |
| Code review (security gates) | I | R | C | - | - | - |
| Threat modelling | R | A | R | C | - | - |
| Security testing | R | A | R | - | - | - |
| **Operations** | | | | | | |
| Incident monitoring | I | I | R | - | - | - |
| Incident response | I | A | R | C | I | I |
| **Compliance** | | | | | | |
| Internal audit | I | C | I | R | - | A |
| DORA reporting | - | - | C | R | - | A |

**Legend:**
- **R (Responsible):** Does the work
- **A (Accountable):** Approves, is answerable
- **C (Consulted):** Important opinion
- **I (Informed):** Informed of the outcome

### Governance Meetings {#reuniões-de-governo}

**Security Committee (Fortnightly, 1h)**
- Attendees: CTO, Tech Lead, Security Champion, Compliance Officer
- Agenda: Incidents, vulnerabilities, roadmap progress
- Output: Minutes, escalations, decisions

**Board Report (Quarterly, 30min)**
- Attendees: CEO, CTO, CFO, Compliance Officer, Board
- Agenda: KPIs, DORA compliance, risks, budget
- Output: Strategic decisions, approvals

---

## Example 2: Regional Bank (100-200 devs) {#exemplo-2-banco-regional-100-200-devs}

### Structured Organisation Chart {#organigrama-estruturado}
```
Conselho/Board
├─ Comissão de Risco
│  └─ Chief Risk Officer (CRO)
│
CEO
├─ CTO (Chief Technology Officer)
│  ├─ VP Development
│  │  ├─ Tech Leads (múltiplos)
│  │  └─ Development Squads (30-50 devs)
│  ├─ VP Operations/SRE
│  │  ├─ SRE Lead
│  │  ├─ SRE Team (3-5)
│  │  └─ Infrastructure
│  └─ CISO (Chief Information Security Officer)
│     ├─ Security Architect
│     ├─ Incident Response Manager
│     ├─ Security Engineers (2-3)
│     └─ Security Champions (embed em squads)
├─ Chief Compliance Officer (CCO)
│  ├─ Compliance Manager
│  ├─ GRC Team
│  └─ Internal Audit Lead
└─ CFO
```

### Expanded RACI {#raci-expandida}

| Activity | CTO | CISO | VP Dev | Tech Lead | Dev/SRE | Compliance | CRO | Board |
|-----------|-----|------|--------|-----------|---------|-----------|-----|-------|
| **Executive Governance** | | | | | | | | |
| Security strategy (3 years) | R | A | C | - | - | C | C | **A** |
| Application security policy | C | R | A | C | - | C | I | A |
| Board approval of policies | I | I | I | - | - | C | I | **A** |
| Security budget | I | A | C | - | - | I | C | **A** |
| **Classification & Risk** | | | | | | | | |
| Classify apps (L1-L3) | I | R | A | **R** | - | C | - | I |
| Threat modelling (L3 apps) | - | R | C | A | - | I | - | - |
| Risk assessment (suppliers) | I | C | - | - | - | R | I | I |
| **Development Lifecycle** | | | | | | | | |
| Code review (security gates) | I | C | I | A | **R** | - | - | - |
| SAST/SCA scanning | I | A | I | I | **R** | - | - | - |
| Pull request approval (sec) | I | C | - | A | **R** | - | - | - |
| **Operations & Monitoring** | | | | | | | | |
| Centralise logs (SIEM) | A | R | C | - | A | I | - | - |
| Security alerts | I | A | - | - | R | - | - | - |
| Incident detection | - | **R** | I | - | C | - | - | - |
| **Incidents & Response** | | | | | | | | |
| Incident classification | - | A | - | - | C | C | - | - |
| P0/P1 response | C | **A** | C | - | R | I | I | I |
| DORA incident reporting | - | C | - | - | - | **R** | A | A |
| **Compliance & Audit** | | | | | | | | |
| Internal audit (SbD) | I | C | I | - | - | **R** | I | A |
| DORA readiness | C | A | C | - | - | **R** | A | **A** |
| TLPT testing | C | **A** | C | - | - | I | I | I |

### Meeting Structure {#estrutura-de-reuniões}

**Steering Committee (Executive) - Monthly, 1.5h**
- Attendees: CTO, CISO, CCO, CFO, CRO
- Agenda: Risk dashboard, budget, compliance, escalations
- Output: Strategic decisions

**Security & Risk Committee - Weekly, 1h**
- Attendees: CISO, VP Operations, VP Dev Lead, Compliance Lead, Incident Response Manager
- Agenda: Incidents, vulnerabilities, roadmap, blockers
- Output: Decisions, task assignments

**Development Security Review - Bi-weekly, 1h**
- Attendees: Tech Leads, Security Engineers, SRE Lead
- Agenda: Code review findings, SAST/SCA results, threat modelling progress
- Output: Escalations, guidance, exemptions

**Squad Security Standup - Weekly (per squad), 15min**
- Attendees: Squad, Security Champion (embedded)
- Agenda: Security tasks, blockers, questions
- Output: Real-time support

**Board Governance - Quarterly, 1h**
- Attendees: Board, CTO, CISO, CCO, CFO, CRO
- Agenda: Strategic risk, compliance posture, DORA readiness, budget
- Output: Board decisions, strategic guidance

---

## Example 3: Distributed SME (30-50 devs, multiple locations) {#exemplo-3-pme-distribuída-30-50-devs-múltiplas-localizações}

### Challenge {#desafio}
- Multiple locations (Lisbon, Porto, remote)
- Limited resources
- Distributed expertise

### Solution: Hybrid Model {#solução-modelo-híbrido}

**Lean Structure:**
```
CEO (Lisboa)
├─ CTO/Tech Lead (Lisboa)
│  ├─ Security Champion (0.5 FTE, Lisboa)
│  ├─ SRE/DevOps (0.5 FTE, Porto)
│  └─ Developers (5-8 por squad, distribuído)
├─ CFO (remoto)
└─ Compliance Officer (Lisboa, part-time)
```

**Simplified RACI:**

| Activity | CTO | Sec Champion | SRE | Dev Lead | Compliance | CEO |
|-----------|-----|-------------|-----|----------|-----------|-----|
| Policy | R | C | - | - | C | A |
| Classify apps | R | A | - | C | - | I |
| Code review sec | I | A | - | R | - | - |
| SAST/SCA | I | R | I | I | - | - |
| Incidents | - | R | A | C | I | I |
| DORA audit | I | C | C | - | R | A |

**Meetings (Lean):**
- **Weekly, 30min:** CTO + Security Champion + SRE (remote standup)
- **Bi-weekly, 1h:** CTO + All Tech Leads (code review highlights)
- **Monthly, 1h:** CTO + Compliance + CEO (KPIs + DORA progress)

---

## Key Responsibilities by Role {#responsabilidades-chave-por-papel}

### CISO (Chief Information Security Officer) {#ciso-chief-information-security-officer}

**Accountable For:**
- ✓ Compliance with DORA and regulations
- ✓ Security policy
- ✓ Audit trail (logs)
- ✓ Incident response
- ✓ TLPT eligibility and execution
- ✓ Risk dashboard accuracy

**Reports to:** CRO or CEO (depends on governance)

**Typical escalations:**
- P0 incident (within 30 min)
- Unresolved critical vuln (within 48h)
- DORA compliance at risk (weekly)

---

### Tech Lead (Development Squads) {#tech-lead-development-squads}

**Responsible For:**
- ✓ Threat modelling (own apps)
- ✓ Code review (security gates)
- ✓ Security testing
- ✓ Requirements documentation

**Consulted:**
- Policy changes
- New tools / frameworks
- Security exceptions

**Reports to:** VP Development or CTO

---

### Security Champion (Embedded) {#security-champion-embedded}

**Role:** "Security voice" within the squad

**Responsible For:**
- ✓ Advocacy of secure practices
- ✓ Code review (security)
- ✓ Training & awareness
- ✓ Liaison with the CISO team

**Time:** 20-30% of the week

**Reports to:** CISO (dotted line), Squad Lead (solid line)

---

### Compliance Officer / GRC {#compliance-officer--grc}

**Accountable For:**
- ✓ Regulatory compliance (DORA, GDPR, etc.)
- ✓ Reports to the supervisor
- ✓ Audit trail
- ✓ Policy approval coordination

**Reports to:** Chief Compliance Officer or CRO

---

## Formal Approvals (Decision Trail) {#aprovações-formais-trilho-de-decisão}

### Security Policy {#política-de-segurança}
```
Draft (CISO)
  ↓
Review (Security team + Compliance)
  ↓
Approval (CTO + CISO)
  ↓
Board vote
  ↓
Implementation + Communication
  ↓
Annual review
```

### Security Exception (e.g. deploy with a high vuln) {#exceção-de-segurança-ex-deploy-com-vuln-alta}
```
Request (Tech Lead)
  ↓
Justificação de risco (Squad + CISO)
  ↓
Approval (CISO + CTO)
    OR Escalate (Board decision)
  ↓
Approval + SLA remediação
  ↓
Log em audit trail + notify CRO
```

### Critical Supplier {#fornecedor-crítico}
```
Request (VP Procurement/Tech)
  ↓
Risk assessment (CISO team)
  ↓
Security requirements (CISO + Compliance)
  ↓
Contrato (Jurídico + CISO review)
  ↓
Approval (CTO + CISO + Compliance)
  ↓
Onboarding (Security Champion + SRE)
```

---

## Communication Matrix {#matriz-de-comunicação}

| Group | Frequency | Format | Owner |
|-------|-----------|---------|-------|
| **Board** | Quarterly | Formal report | CISO/Compliance |
| **Steering Committee** | Monthly | Meeting + slides | CTO/CISO |
| **Security Committee** | Weekly | Meeting | CISO |
| **Dev Leads** | Bi-weekly | Meeting | CISO |
| **All Staff** | Annual | All-hands | CEO/CISO |
| **Security Champions** | Fortnightly | Meeting + Slack | CISO |
| **On-call (incidents)** | On-demand | Pagerduty + Slack | DevOps / SRE (On-Call) |

---

## Essential Documentation {#documentação-essencial}

Each organisation must document:

```
📋 GOVERNANCE DOCUMENTATION

├─ Charter of Governance
│  ├─ Estrutura (organigrama)
│  ├─ Roles & responsibilities (RACI)
│  ├─ Escalation paths
│  └─ Approval workflows
│
├─ Security Policies
│  ├─ Policy de Segurança Aplicacional
│  ├─ Policy de Incidentes
│  ├─ Policy de Fornecedores
│  └─ Code of Conduct (security)
│
├─ Procedures
│  ├─ Code review procedure
│  ├─ Incident response playbook
│  ├─ Exception approval process
│  └─ Audit trail requirements
│
└─ Training Materials
   ├─ Role-based training (CISO, Tech Lead, Dev, QA)
   ├─ Onboarding security checklist
   ├─ Annual refresher modules
   └─ Incident response drills
```

---

## Implementation Checklist {#checklist-de-implementação}

- [ ] **Organisation chart defined** - Clear roles, reporting lines
- [ ] **RACI documented** - Approved and communicated
- [ ] **Meetings scheduled** - Calendar confirmed
- [ ] **Clear escalation paths** - Documented (e.g. P0 → CISO → CTO → CEO)
- [ ] **Approvals signed** - Board signature on policies
- [ ] **Training** - Everyone knows their role
- [ ] **Audit trail active** - Logs of who decided what, and when

---

## Important Notes {#notas-importantes}

1. **There is no one size fits all** - Adapt to the context
2. **Evolution:** The structure may change as maturity grows
3. **Simplicity:** Avoid excessive bureaucracy
4. **Clarity:** Ambiguous RACI = problems
5. **Documentation:** Everything in writing, nothing "implicit"
6. **Review:** Annually, after major changes

---

**Version:** 1.0  
**Date:** November 2025  
**Review:** Annual or after organisational change
