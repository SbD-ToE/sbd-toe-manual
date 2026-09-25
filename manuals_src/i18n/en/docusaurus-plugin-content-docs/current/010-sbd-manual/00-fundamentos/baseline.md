---
id: baseline
title: Minimum Cross-Cutting Obligations
sidebar_label: 🛡️ Mandatory Baseline
description: The hard core of practices that every application must meet, regardless of risk level
tags: [obrigacoes, baseline, minimo, must, nis2, dora, gdpr]
sidebar_position: 4
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/baseline.md
  source_sha256: c1f95a1fcd348b88604ecd5ffc0f9b132e3f1175715fa1137ba48dc931795473
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 5802edc4c4a33561cdceaa32b5e762f19cb4dd976982e3a6d659ef94e15fd046
  engine: claude-fable-5-1
  prompt_sha256: 13029ebd6497cb63207d12577bb94bbd3b20a5d9c8d3ebd2e4a450d20a45a251
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [avaliacao, chapter_role, cycle_iteration, layer, lifecycle_phase, mapping, maturity, piso_limiar, piso_relacao, risk_level, sbdtoe_sbd, traceability, transversal, validation_evaluation]
  glossary_sha256: 9cf7a95e7e92c29c8de85d2c5a3defe33cca28ae1f051d106f160b58afbd14b2
  translated_at: 2026-09-25T20:19:51Z
  reviewed_by: null
---

# Minimum Cross-Cutting Obligations

Software security cannot depend on the criticality of each application to guarantee a **common minimum foundation**.  
Without that foundation, the organisation fragments: some teams apply robust practices, others apply none, and the result is an inconsistent, vulnerable ecosystem that is hard to audit.

The **minimum cross-cutting obligations** are therefore the base of SbD-ToE.  
They do not aim to replace L1–L3 proportionality, but rather to create a uniform layer which guarantees that, whatever the application, an elementary set of controls is always in place.

These obligations do not apply only to the code or to the application itself. They apply equally to **processes, pipelines, environments, automations and external integrations** that take part in the software lifecycle.

Not applying any minimum obligation **is not a technical choice** but a **formal organisational decision**, which must be explicitly justified, approved and traceable in accordance with the SbD-ToE governance model (Ch. 14).

---

## 🎯 The Hard Core: 8 Cross-Cutting Obligations {#-o-núcleo-duro-8-obrigações-transversais}

Regardless of the risk level, **every application** must implement:

### 1️⃣ **Criticality Classification** (Ch. 01) {#1️⃣-classificação-da-criticidade-cap-01}
**What**: Before any development starts, classify the risk level of the application (L1, L2, L3).

**Why**: Without classification, it is impossible to determine which practices apply. The decision on security investment becomes arbitrary.

**Responsible**: Product Owner, Software Architect, CISO

**Regulations**: NIS2 (risk assessment), DORA (criticality classification)

---

### 2️⃣ **Minimum Security Requirements** (Ch. 02) {#2️⃣-requisitos-mínimos-de-segurança-cap-02}
**What**: Define and trace a minimum set of security requirements that the application must meet.

**Why**: Explicit requirements allow DevOps and QA to validate the implementation; without them, security remains vague.

**Responsible**: Product Owner, AppSec, QA

**Regulations**: NIS2 (technical measures), GDPR (data protection by design)

---

### 3️⃣ **Explicit Dependency Management** (Ch. 05) {#3️⃣-gestão-explícita-de-dependências-cap-05}
**What**: Maintain an up-to-date inventory of all critical dependencies (frameworks, libraries, systems). Include versions and vulnerability alerts.

**Why**: Most exploited vulnerabilities come from unmanaged or outdated dependencies. An inventory is fundamental for incident response.

**Responsible**: DevOps, Developers, AppSec

**Regulations**: NIS2 (supply chain risk), DORA (vendor management)

---

### 4️⃣ **Basic Coding Guidelines and Automated Validation** (Ch. 06) {#4️⃣-coding-guidelines-básicas-e-validação-automática-cap-06}
**What**: Apply a minimum set of secure coding guidelines (e.g. avoid injection, validate inputs, use secure hashing). Configure automated SAST (Static Application Security Testing) on every build.

**Why**: Guidelines and SAST combined eliminate most trivial vulnerabilities at almost no marginal cost.

**Responsible**: Developers, AppSec, DevOps

**Regulations**: GDPR (security by design), NIS2 (technical measures)

---

### 5️⃣ **CI/CD Pipelines with Minimum Checks** (Ch. 07) {#5️⃣-pipelines-cicd-com-verificações-mínimas-cap-07}
**What**: Run CI/CD pipelines with minimum security gates (SAST, dependency scanning, secret scanning). Never deploy without validations.

**Why**: Automated pipelines guarantee that no vulnerable code reaches production through human oversight. These checks can be fully automated, provided the execution and blocking criteria are objective, deterministic and auditable.

**Responsible**: DevOps, AppSec

**Regulations**: NIS2 (change control), DORA (change management)

---

### 6️⃣ **Essential Logging and Monitoring** (Ch. 12) {#6️⃣-registo-e-monitorização-essencial-cap-12}
**What**: Enable minimum logging on every service (authentication events, critical changes, errors). Correlate logs at a central point and monitor for anomalies.

**Why**: Logs are the foundation of incident detection and of regulatory accountability.

**Responsible**: DevOps, Operations, CISO

**Regulations**: NIS2 (incident logging), DORA (monitoring), GDPR (audit trails)

---

### 7️⃣ **Initial Security Training** (Ch. 13) {#7️⃣-formação-inicial-em-segurança-cap-13}
**What**: Ensure that every team member (Developers, QA, DevOps, etc.) receives mandatory initial training in software security, aligned with their roles.

**Why**: Risk-aware teams avoid mistakes. Training is the security investment with the highest ROI.

**Responsible**: CISO, Security Champion, Executive Management

**Regulations**: NIS2 (competence), DORA (staff training)

---

### 8️⃣ **Minimum Security Clauses for Suppliers** (Ch. 14) {#8️⃣-cláusulas-mínimas-de-segurança-em-fornecedores-cap-14}
**What**: Include minimum security clauses in contracts with suppliers/third parties (commitment to data responsibility, right of audit, incident notification).

**Why**: The supply chain is one of the largest sources of risk. Without contractual clauses, there is no way to demand compliance.

**Responsible**: GRC, CISO, Legal

**Regulations**: NIS2 (supply chain), DORA (vendor management), GDPR (data processors)

---

## 📊 Coverage Map {#-mapa-de-cobertura}

| Obligation | Chapter | Responsible | Validation |
|-----------|----------|-------------|-----------|
| 1. Classification | 01 | Product Owner / Software Architect | CISO / GRC |
| 2. Requirements | 02 | AppSec / Product Owner | QA / GRC |
| 3. Dependencies | 05 | DevOps / Developers | SCA Tools / AppSec |
| 4. Coding Guidelines | 06 | Developers | SAST Tools / Code Review |
| 5. CI/CD Gates | 07 | DevOps | Automated Pipelines |
| 6. Logging | 12 | DevOps / Operations | Monitoring Tools / Auditors |
| 7. Training | 13 | CISO / Security Champion | Attendance Tracking |
| 8. Contracts | 14 | GRC / Legal | Contract Review / Auditors |

---

## 💡 Technical and Scientific Rationale {#-racional-técnico-científico}

The definition of these minimum obligations rests on:

### **Studies of Real Incidents** {#estudos-de-incidentes-reais}
- **Verizon DBIR** (Data Breach Investigations Report): Most breaches stem from basic failures - weak credentials, unapplied patches, lack of logging.
- **ENISA Threat Landscape**: Known vulnerabilities (e.g. CVEs) are routinely exploited because the basics are not in place.

### **OWASP Top 10** {#owasp-top-10}
The 10 most common vulnerabilities could be prevented by:
- **A01 Broken Access Control** → Clear requirements (2)
- **A02 Cryptographic Failures** → Coding guidelines (4)
- **A03 Injection** → SAST + validation (4, 6)
- **A04 Insecure Design** → Threat modelling (3)
- **A05 Security Misconfiguration** → IaC + guidelines (4, 8)
- **A06 Vulnerable Components** → Dependency management (5)
- **A07 Authentication Failures** → Requirements (2)
- **A08 Data Integrity Failures** → CI/CD gates (7)
- **A09 Logging & Monitoring Failures** → Mandatory logging (12)
- **A10 SSRF** → Threat modelling (3)

### **Maturity Models** {#modelos-de-maturidade}
Organisations assessed with OWASP SAMM show that **all the mature ones** share these 8 practices as their base.  
The absence of any one of them creates significant gaps.

---

## ⚖️ Baseline vs. Proportionality (L1–L3) {#️-baseline-vs-proporcionalidade-l1l3}

**Important**: The minimum obligations **do not replace** L1–L3 proportionality.

```
┌──────────────────────────────────────┐
│   8 Obrigações Mínimas (SEMPRE)      │
├──────────────────────────────────────┤
│  L1 (Baixo Risco)                    │
│  - Mínimos acima + validações básicas│
├──────────────────────────────────────┤
│  L2 (Risco Moderado)                 │
│  - Mínimos + práticas robustas       │
│  - Threat modeling, security reviews │
├──────────────────────────────────────┤
│  L3 (Risco Crítico)                  │
│  - Mínimos + aplicação integral      │
│  - Red teaming, auditorias rigorosas │
└──────────────────────────────────────┘
```

What changes between levels is the **intensity, depth and formalisation**.  
But the baseline is cross-cutting and **is never negotiable**.

---

## 🔄 Pragmatism and Universal Application {#-pragmatismo-e-aplicação-universal}

One essential aspect is efficiency: in many cases, applying **certain practices to every application** is more practical than case-by-case discussions.

### Practical Examples {#exemplos-práticos}

**SAST in every repository**  
→ Even at zero cost (open-source tools), it eliminates the trivial ones.  
→ Fewer false positives than disconnected SCA.

**Automated dependency scanning in pipelines**  
→ A standard job in every project simplifies policy.  
→ Avoids debates over "is this lib critical?"

**Logging and monitoring by default**  
→ Enabling collectors on every service makes audits easier.  
→ Detects incidents faster.

**Minimum contract templates**  
→ Applying the same clauses to every supplier reduces negotiation.  
→ Legal stays consistent.

---

## 📋 Implementation Checklist {#-checklist-de-implementação}

For each application, validate:

- [ ] **Classification (L1/L2/L3)** documented and approved
- [ ] **Minimum security requirements** defined and traced
- [ ] **SBOM/dependency inventory** up to date
- [ ] **SAST configured** and integrated into CI/CD
- [ ] **Dependency scanning active** with alerts
- [ ] **Coding guidelines** distributed to the team
- [ ] **CI/CD gates** implemented (SAST, deps, secrets)
- [ ] **Minimum logging** implemented and centralised
- [ ] **Essential monitoring** active (critical alerts)
- [ ] **Security training** completed by everyone
- [ ] **Contractual clauses** in place with suppliers

---

## 🔗 Regulatory Alignment {#-alinhamento-regulatório}

### **NIS2 (Directive on Network and Information Security)** {#nis2-directive-on-network-and-information-security}
- ✅ Covers: Technical measures, logging, monitoring, risk assessment
- ✅ All 8 obligations contribute to NIS2 compliance

### **DORA (Digital Operational Resilience Act)** {#dora-digital-operational-resilience-act}
- ✅ Covers: Periodic testing, supplier management, resilience
- ✅ Obligations 5, 6, 7, 8 are essential for DORA

### **GDPR (General Data Protection Regulation)** {#gdpr-general-data-protection-regulation}
- ✅ Covers: Privacy by design, security by design, logging
- ✅ Obligations 2, 4, 6 are critical for GDPR

### **PCI-DSS (Payment Card Industry)** {#pci-dss-payment-card-industry}
- ✅ All 8 obligations cover the PCI-DSS minimums

### **ISO/IEC 27001** {#isoiec-27001}
- ✅ Direct mapping: each obligation corresponds to ISO controls

---

## 📈 Expected Impact {#-impacto-esperado}

With the 8 obligations implemented:

| Metric | Impact |
|---------|---------|
| **Trivial Vulnerabilities** | ↓ 70-80% (SAST + guidelines) |
| **Dependency-Related Incidents** | ↓ 60% (SCA + inventory) |
| **Time to Detect (MTTD)** | ↓ 50% (logging + monitoring) |
| **Time to Respond (MTTR)** | ↓ 40% (centralised logs) |
| **Compliance Readiness** | ↑ 80%+ (traceability) |
| **Remediation Cost** | ↓ 30% (early detection) |

---

## 🎯 Next Steps {#-próximos-passos}

1. **Audit the current state**: Which of these 8 obligations are already implemented?
2. **Prioritise the gaps**: Which is the most urgent? (Recommendation: start with 1, 2, 5, 7)
3. **Allocate resources**: Each obligation has an "owner" - define the responsibilities
4. **Set a timeline**: What is the deadline for 100% compliance?
5. **Measure**: Establish KPIs for each obligation

---

**Related Reading**:
- [Roles and Responsibilities](./roles-responsabilidades/intro) - Who implements each obligation
- [Ch. 01 - Classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro) - How to classify applications
- [Ch. 02 - Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro) - How to define requirements

---

**Final Note**: The baseline is non-negotiable, but its implementation is flexible.  
A small start-up can apply all 8 with open-source tools and minimal effort.  
An enterprise will apply them with frameworks, regulatory compliance and formalised processes.  
But the essence is always the same: **nothing is left without basic security**.
