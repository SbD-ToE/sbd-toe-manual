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
  source_sha256: 3ceb49376d696d779378a376a8c53043127fa2308c193676bd342197c28d1026
  source_commit: 1b21e5fa08d7a0f483eec3516d87de20ee99574c
  target_sha256: 186d9a64e986c25f8e3d561cff0791931d5d35ebe782310221ff73c5e063e973
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [avaliacao, chapter_role, cycle_iteration, gdpr_security_of_processing, layer, lifecycle_phase, mapping, maturity, normative_empirical, piso_limiar, piso_relacao, practitioner_manual, requirement_runtime, risk_level, role_juridico, sbdtoe_sbd, traceability, transversal, validation_evaluation]
  glossary_sha256: a88b23ade7602938e9966077c7e1f1bcc847c5796489f78a7be29953917aceb8
  translated_at: 2026-09-28T09:13:16Z
  stamped_at: 2026-09-28T09:13:16Z
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

**Why**: Automated pipelines guarantee that no vulnerable code reaches production through human oversight. These checks can be fully automated, provided the execution and blocking criteria are objective, deterministic and auditable. Automated validation replaces human approval when the owner of that approval has accepted it as sufficient and deterministic; whatever deviates from it goes back to that owner as an exception.

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
Published incident reports, such as the Verizon DBIR and the ENISA Threat Landscape, repeatedly describe incidents that stem from basic failures: compromised credentials, known vulnerabilities left unpatched, missing logging. They are context for the choice of these obligations, not proof of their effectiveness; each edition's figures apply to the population and period that edition studies.

### **OWASP Top 10** {#owasp-top-10}
The minimum obligations address the categories of the OWASP Top 10 (2021 edition), without guaranteeing that they prevent them:
- **A01 Broken Access Control** → Clear requirements (obligation 2)
- **A02 Cryptographic Failures** → Requirements and coding guidelines (2, 4)
- **A03 Injection** → Coding guidelines and SAST in the pipeline (4, 5)
- **A04 Insecure Design** → Requirements and risk classification (1, 2); threat modelling (Ch. 03) goes deeper
- **A05 Security Misconfiguration** → Guidelines and pipeline checks (4, 5)
- **A06 Vulnerable and Outdated Components** → Dependency management (3)
- **A07 Identification and Authentication Failures** → Requirements (2)
- **A08 Software and Data Integrity Failures** → Pipeline checks (5)
- **A09 Security Logging and Monitoring Failures** → Logging and monitoring (6)
- **A10 SSRF** → Requirements and guidelines (2, 4); threat modelling (Ch. 03) goes deeper

### **Maturity Models** {#modelos-de-maturidade}
The practices in these obligations correspond to baseline practices of the maturity models used as reference (OWASP SAMM, BSIMM). This is a correspondence of content, not a measurement: the Manual does not claim that all mature organisations share them.

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
→ There are open-source tools with no licence cost; the operational cost (configuration, triage of results, maintenance) is always there.  
→ Catches part of the trivial defects early; the false-positive rate depends on the tool, the configuration and the code.

**Automated dependency scanning in pipelines**  
→ A standard job in every project simplifies policy.  
→ Avoids debates over "is this lib critical?"

**Logging and monitoring by default**  
→ Enabling collectors on all services makes audits easier.  
→ Provides the basis for detecting incidents; how fast they are detected depends on monitoring and response.

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

The 8 obligations **contribute** to several regimes; they are not equivalent to compliance with any of them. Obligation-by-obligation coverage, with what the Manual covers, the declared gaps and what is out of scope, is on the [normative cross-check](/sbd-toe/cross-check-normativo/intro) pages.

### **NIS2 (Directive on Network and Information Security)** {#nis2-directive-on-network-and-information-security}
- They contribute to the technical measures of Art. 21 (logging, monitoring, vulnerability management, risk assessment). See the [NIS2 cross-check](/sbd-toe/cross-check-normativo/nis2/intro).

### **DORA (Digital Operational Resilience Act)** {#dora-digital-operational-resilience-act}
- Obligations 5 to 8 contribute most (pipeline, logging, training, suppliers). See the [DORA cross-check](/sbd-toe/cross-check-normativo/dora/intro).

### **GDPR (General Data Protection Regulation)** {#gdpr-general-data-protection-regulation}
- Obligations 2, 4 and 6 contribute most, to data protection by design and security of processing. See the [GDPR cross-check](/sbd-toe/cross-check-normativo/gdpr/intro).

### **PCI-DSS (Payment Card Industry)** {#pci-dss-payment-card-industry}
- Used as a reference, with no published cross-check and no requirement-by-requirement mapping. There is thematic overlap with several of the standard's requirements; that is not compliance.

### **ISO/IEC 27001** {#isoiec-27001}
- Used as a reference, with no published cross-check. Several obligations correspond to Annex A controls; the correspondence is not mapped control by control.

---

## 📈 Expected Impact {#-impacto-esperado}

With the 8 obligations implemented, effects in this direction are expected. They are **hypotheses**, with no effectiveness demonstrated by the Manual: they depend on the context, the starting point and the quality of implementation, and each organisation measures them with the chapters' KPIs.

| Area | Expected effect (hypothesis) |
|---------|---------|
| **Trivial vulnerabilities** | Fewer, through guidelines and SAST |
| **Dependency-related incidents** | Fewer, through SCA and inventory |
| **Time to detect (MTTD)** | Shorter, through logging and monitoring |
| **Time to respond (MTTR)** | Shorter, through centralised logs |
| **Audit readiness** | Greater, through traceability |
| **Remediation cost** | Lower, through earlier detection |

---

## 🎯 Next Steps {#-próximos-passos}

1. **Audit the current state**: Which of these 8 obligations are already implemented?
2. **Prioritise the gaps**: Which is the most urgent? (Recommendation: start with 1, 2, 5, 7)
3. **Allocate resources**: Each obligation has an "owner" - define the responsibilities
4. **Set a timeline**: What is the deadline for implementing the 8 obligations?
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
