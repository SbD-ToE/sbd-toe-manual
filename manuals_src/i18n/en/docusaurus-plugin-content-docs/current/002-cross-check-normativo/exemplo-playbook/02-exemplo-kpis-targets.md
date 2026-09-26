---
id: exemplo-kpis-targets
title: "Example: KPIs and Targets"
description: Examples of KPIs and targets for different organisational profiles
tags: [exemplos, kpis, metricas, targets, monitoramento]
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/exemplo-playbook/02-exemplo-kpis-targets.md
  source_sha256: 9f80cb3d7a2fe4a01241ae1dd6dfad268094e2d609fc694a409d27c1287036a2
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: 7c88655ce275dfc6de202e408c9d90467fe47476d03c96322395d0b02b816770
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5f18169e44cb78faceac7d31df119020c508135f27e39f4105f054ecf5a72d33
  glossary_keys: [maturity, practitioner_manual, requirement_runtime, sbdtoe_sbd]
  glossary_sha256: 7181a06300a7579c8a732e591943ed35bfcce6287cd746781e9f14370a2c361c
  translated_at: 2026-09-26T18:11:59Z
  reviewed_by: null
---

# Example: KPIs and Targets

## Context {#enquadramento}

SbD-ToE prescribes ([Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)):
- ✓ Security metrics
- ✓ Continuous monitoring
- ✓ Data-driven improvement

SbD-ToE **does NOT prescribe** specific targets because contexts vary. This document presents **examples for different types of organisation**.

---

## KPI Dimensions (All Organisations) {#dimensões-de-kpis-todas-as-organizações}

The manual defines these dimensions ([Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)):

1. **Application Risk** - Threat coverage
2. **Development** - Code quality
3. **Operations** - Response time
4. **Supply Chain** - Supplier management
5. **Compliance** - Audit evidence

For each dimension, example targets are presented.

---

## Scenario 1: Payments Fintech (Startup, `<`50 devs) {#cenário-1-fintech-de-pagamentos-startup-50-devs}

### Context {#contexto}
- Critical service: Payment processing
- DORA deadline: January 2025 (short)
- Budget: Limited
- Risk appetite: Low (payments = PCI-DSS + DORA)

### KPIs and Targets {#kpis-e-targets}

| Category | Metric | Target | Period | Rationale |
|-----------|---------|--------|---------|---------------|
| **Application Risk** | % apps classified | 100% | M1 | Urgent: DORA requires classification |
| | Threat modelling (L3) | 100% | M3 | Before TLPT |
| | Unremediated critical vulns | 0 | Permanent | Payments: zero tolerance |
| | Unremediated high vulns | 0 (or `<`48h SLA) | Permanent | Direct PCI impact |
| **Development** | Test coverage | ≥80% | M6 | Progressive: start with critical functions |
| | High SAST findings | 0 | Permanent | CI/CD gate |
| | High SCA findings | 0 | Permanent | CI/CD gate |
| **Operations** | MTTR P0 (Critical) | `<`2h | Permanent | Payments: direct impact |
| | MTTR P1 (High) | `<`8h | Permanent | Business impact |
| | Incidents detected/month | `<`5 | M12 | Reduce with maturity |
| **Supply Chain** | Suppliers in the inventory | 100% | M2 | Required by DORA Art. 26 |
| | % with complete onboarding | 100% | M3 | Before access |
| | % with security training | 100% | M3 | Mandatory before access |
| **Compliance** | Policy signed by the board | ✓ | M1 | DORA Art. 5 |
| | Audit trail (logs) | 3 years | M0 | Prior requirement |
| | Staff SbD training | 100% devs | M4 | Rapid ramp-up |
| | Inspection readiness | 95% | M12 | Before the supervisor's inspection |

### Dashboard (Visual example) {#dashboard-exemplo-visual}

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'fontSize':'13px'}}}%%
graph TB
    subgraph FINTECH["📊 FINTECH SEGURANÇA - Novembro 2025"]
        subgraph RISCO["🎯 RISCO APLICACIONAL"]
            R1["Apps classificadas: 100%<br/>🟢 OK"]
            R2["Threat modeling L3: 95%<br/>target: 98% | ⚠️ DELAYED"]
            R3["Critical vulns: 0<br/>🟢 OK"]
            R4["High vulns: 2<br/>target: 0 | 🔴 CRITICAL"]
        end
        
        subgraph DEV["⚙️ DESENVOLVIMENTO"]
            D1["Cobertura testes: 72%<br/>target: 80% | ⚠️ DELAYED"]
            D2["SAST findings altos: 0<br/>🟢 OK"]
            D3["SCA findings altos: 0<br/>🟢 OK"]
        end
        
        subgraph OPS["OPERAÇÕES"]
            O1["MTTR P0: 1.5h<br/>🟢 OK"]
            O2["MTTR P1: 6h<br/>🟢 OK"]
            O3["Incidents/month: 3<br/>target: `<5` | 🟢 OK"]
        end
        
        subgraph SUPPLY["📦 SUPPLY CHAIN"]
            S1["Fornecedores inventariados: 100%<br/>🟢 OK"]
            S2["Com onboarding: 95%<br/>target: 100% | ⚠️ DELAYED"]
            S3["Com training: 95%<br/>target: 100% | ⚠️ DELAYED"]
        end
        
        subgraph CONF["📋 CONFORMIDADE"]
            C1["Política board: Assinada<br/>🟢 OK"]
            C2["Trilho auditoria: 3 anos<br/>🟢 OK"]
            C3["Staff training: 85%<br/>target: 100% | ⚠️ DELAYED"]
            C4["Readiness DORA: 92%<br/>target: 95% | ⚠️ DELAYED"]
        end
    end
    
    style R1 fill:#d4edda,stroke:#155724,stroke-width:2px
    style R2 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style R3 fill:#d4edda,stroke:#155724,stroke-width:2px
    style R4 fill:#f8d7da,stroke:#721c24,stroke-width:2px
    style D1 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style D2 fill:#d4edda,stroke:#155724,stroke-width:2px
    style D3 fill:#d4edda,stroke:#155724,stroke-width:2px
    style O1 fill:#d4edda,stroke:#155724,stroke-width:2px
    style O2 fill:#d4edda,stroke:#155724,stroke-width:2px
    style O3 fill:#d4edda,stroke:#155724,stroke-width:2px
    style S1 fill:#d4edda,stroke:#155724,stroke-width:2px
    style S2 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style S3 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style C1 fill:#d4edda,stroke:#155724,stroke-width:2px
    style C2 fill:#d4edda,stroke:#155724,stroke-width:2px
    style C3 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style C4 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style FINTECH fill:#f8f9fa,stroke:#343a40,stroke-width:3px
```

---

## Scenario 2: Traditional Bank (Regional, `>`200 devs) {#cenário-2-banco-tradicional-regional-200-devs}

### Context {#contexto-1}
- Critical apps: `>`30 (multiple business lines)
- DORA deadline: January 2025
- Budget: Adequate
- Risk appetite: Very low (historical compliance)
- Additional compliance: GDPR, NIS2, local regulation

### KPIs and Targets {#kpis-e-targets-1}

| Category | Metric | Target | Period | Rationale |
|-----------|---------|--------|---------|---------------|
| **Application Risk** | % apps classified | 100% | M1 | Mandatory under DORA |
| | Threat modelling (L3) | 100% | M4 | More apps = time |
| | Threat modelling (L2) | 80% | M6 | Progressive |
| | Unremediated critical vulns | 0 | Permanent | DORA + GDPR |
| | High vulns (remediation SLA) | `<`30 days | Permanent | As per [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) |
| | Medium vulns (remediation SLA) | `<`90 days | Permanent | As per [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) |
| **Development** | Test coverage | ≥85% | M12 | More rigorous: bank |
| | High SAST findings | 0 | Permanent | Zero tolerance |
| | High SCA findings | 0 | Permanent | Zero tolerance |
| | Code review rate | 100% | Permanent | Segregation of duties |
| **Operations** | MTTR P0 (Critical) | `<`1h | Permanent | Systemic impact |
| | MTTR P1 (High) | `<`4h | Permanent | Operational impact |
| | Core app availability | ≥99.95% | Permanent | Regulatory SLA |
| | P0 incidents resolved `<`24h | 100% | Permanent | Mandatory DORA reporting |
| **Supply Chain** | Suppliers in the inventory | 100% | M1 | DORA Art. 26 |
| | % audited (risk assessment) | 100% | M3 | Required by DORA |
| | % with an updated contract | 100% | M6 | Technical clauses |
| | % with access revoked `<`24h | 100% | Permanent | Rigorous offboarding |
| **Compliance** | Board policy + GDPR officer | ✓ | M0 | Prior requirement |
| | Audit trail (logs) | 5 years | M0 | GDPR + DORA |
| | Staff SbD training | 100% devs | M6 | Larger volume |
| | Staff GRC training | 100% architecture | M3 | Understand the regulations |
| | TLPT (L3 apps) | 100% | M12 | DORA Art. 19 |
| | TLPT attestation | ✓ | M13 | Board evidence |
| | Supervisory inspection readiness | 100% | M18 | Full preparation |

### New: A Different Timeline {#novidade-timeline-diferente}

```mermaid
gantt
    title Timeline de Implementação: Fintech vs Banco
    dateFormat YYYY-MM-DD
    axisFormat %b
    
    section Fintech (12 meses)
    Foundation rápida           :f1, 2025-01-01, 60d
    Automatização              :f2, after f1, 120d
    Operação + TLPT            :f3, after f2, 180d
    Conformidade               :milestone, f4, after f3, 0d
    
    section Banco (18 meses)
    Foundation (mais apps)      :b1, 2025-01-01, 90d
    Automatização (complexa)    :b2, after b1, 180d
    Operação + TLPT             :b3, after b2, 180d
    Auditoria interna          :b4, after b3, 90d
    Conformidade               :milestone, b5, after b4, 0d
```

**Key differences:**
- **Fintech:** 12 months, fast foundation (M0-M2), focus on speed
- **Bank:** 18 months, longer foundation (M0-M3), more apps and complexity


---

## Scenario 3: Digital Insurer (SME, 20-50 devs) {#cenário-3-segurador-digital-pme-20-50-devs}

### Context {#contexto-2}
- Apps: Critical subsystems (10-15 L3)
- DORA deadline: January 2025
- Budget: Moderate
- Risk appetite: Low (insurance = sensitive data + GDPR)
- Additional compliance: GDPR, local insurance regulation

### KPIs and Targets {#kpis-e-targets-2}

| Category | Metric | Target | Period | Rationale |
|-----------|---------|--------|---------|---------------|
| **Application Risk** | % apps classified | 100% | M1 | Mandatory under DORA |
| | Threat modelling (L3) | 100% | M3 | Fewer apps = fast |
| | Unremediated critical vulns | 0 | Permanent | GDPR + data |
| | High vulns (SLA) | `<`15 days | Permanent | Sensitive data |
| **Development** | Test coverage | ≥75% | M6 | Pragmatic for an SME |
| | High SAST findings | 0 | Permanent | CI/CD gate |
| | High SCA findings | 0 | Permanent | CI/CD gate |
| **Operations** | MTTR P0 | `<`4h | Permanent | Insurance: operational impact |
| | MTTR P1 | `<`24h | Permanent | Less critical than a bank |
| | Availability | ≥99.5% | Permanent | Commercial SLA |
| **Supply Chain** | Suppliers in the inventory | 100% | M2 | Required by DORA |
| | % with onboarding | 100% | M3 | Before access |
| | % with training | 100% | M3 | Mandatory |
| **Compliance** | Board policy | ✓ | M1 | DORA Art. 5 |
| | Audit trail | 3 years (GDPR) | M0 | |
| | Staff training | 100% | M4 | SME: everyone is aware |
| | TLPT readiness | Critical L3 pilot | M10 | Fewer apps = feasible |
| | Inspection readiness | 90% | M12 | Before the DORA deadline |

---

## Scenario 4: Outsourcing/Financial Services Company {#cenário-4-empresa-de-outsourcingserviços-financeiros}

### Context {#contexto-3}
- Apps: Multiple SaaS/On-prem solutions
- Clients: Different risk profiles
- DORA deadline: Depends on the client
- Budget: Variable (per client)
- Challenge: Different maturity levels per client

### Approach: Targets per Tier {#approach-targets-por-tier}

| Tier | Client | RTO | High Vulns SLA | TLPT | Training |
|------|---------|-----|-----------------|------|----------|
| **Essential** | Small bank | `<`4h | `<`30d | Yes | 100% |
| **Standard** | Financial SME | `<`8h | `<`45d | Yes | 80% |
| **Basic** | Fintech startup | `<`24h | `<`60d | Pilot | 60% |

### Client Management {#gestão-de-clientes}

**👤 Each client has:**
- App classification (L1-L3)
- Its own policy (signed)
- Customised SLA
- Specific DORA timeline
- KPIs tracked on a dashboard
- Quarterly report

**📊 Internal consolidation:**
- Aggregate KPI: % compliant clients
- Aggregate risk: Clients at risk
- Training: Coverage per region/client
- Alerts: Clients that will miss the deadline

---

## Components of Any Dashboard {#componentes-de-qualquer-dashboard}

Regardless of the scenario, the dashboard must have:

### 📊 Unified Dashboard {#-dashboard-unificado}

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'fontSize':'14px'}}}%%
graph TB
    subgraph DASH["📊 DASHBOARD - Período: Trimestral | Status: 92% on-track"]
        subgraph RISK["🎯 RISCO"]
            R1["Critical: 0 / target: 0<br/>🟢 OK"]
            R2["High: 3 / target: `<5`<br/>🟢 OK"]
            R3["Medium: 12 / target: `<20`<br/>🟡 WATCH"]
        end
        
        subgraph COMP["📋 CONFORMIDADE"]
            C1["Apps classificadas: 95%<br/>target: 100% | 🟡 DELAYED"]
            C2["Policy signed: YES<br/>🟢 OK"]
            C3["Trilho logs: 3 years<br/>🟢 OK"]
            C4["Staff trained: 80%<br/>target: 100% | 🟡 DELAYED"]
        end
        
        subgraph TREND["📈 TREND últimos 6 meses"]
            T1["Critical vulns: ↓<br/>🟢 melhorando"]
            T2["High vulns: →<br/>➡️ estável"]
            T3["Training: ↑<br/>🟢 melhorando"]
        end
        
        subgraph ALERT["⚠️ ALERTAS CRÍTICOS"]
            A1["🚨 2 fornecedores sem training<br/>Deadline: M3"]
            A2["🚨 1 app L3 sem threat modeling<br/>Status: atrasado"]
        end
    end
    
    style R1 fill:#d4edda,stroke:#155724,stroke-width:2px
    style R2 fill:#d4edda,stroke:#155724,stroke-width:2px
    style R3 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style C1 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style C2 fill:#d4edda,stroke:#155724,stroke-width:2px
    style C3 fill:#d4edda,stroke:#155724,stroke-width:2px
    style C4 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style T1 fill:#d4edda,stroke:#155724,stroke-width:2px
    style T2 fill:#e2e3e5,stroke:#6c757d,stroke-width:2px
    style T3 fill:#d4edda,stroke:#155724,stroke-width:2px
    style A1 fill:#f8d7da,stroke:#721c24,stroke-width:2px
    style A2 fill:#f8d7da,stroke:#721c24,stroke-width:2px
    style DASH fill:#f8f9fa,stroke:#343a40,stroke-width:3px
```

---

## Review Cadence {#cadência-de-revisão}

### Monthly (Quick-check) {#mensal-quick-check}
- Critical/High vulns
- Open incidents
- Suppliers without onboarding

### Quarterly (Formal Review) {#trimestral-formal-review}
- KPIs against targets
- Trends over the last 3 months
- Target adjustments if needed
- Board reporting

### Annual (Strategic) {#anual-strategic}
- Review of targets in line with DORA's evolution
- Lessons learned vs. targets
- Projection for the next year

---

## Target-Setting Process (To Do) {#processo-de-definição-de-targets-por-fazer}

1. **Baseline:** Audit the current state
2. **Benchmarking:** Compare with the industry (caution: contexts vary)
3. **Risk Assessment:** Define the risk appetite
4. **Proposal:** Present to management
5. **Approval:** Board sign-off
6. **Communication:** Publish targets, communicate the timeline
7. **Monitoring:** Track progress
8. **Review:** Quarterly + annual

---

## Important {#importante}

**There are no "right targets"** - each organisation must:

- Start conservatively (better to exceed than to fail)
- Iterate according to capacity
- Align with DORA requirements
- Communicate trade-offs
- Document decisions

Targets serve a **practical purpose**, not a theoretical one - they exist to guide action, not to look good in an audit.

---

**Version:** 1.0  
**Date:** November 2025  
**Review:** Quarterly in line with DORA's evolution
