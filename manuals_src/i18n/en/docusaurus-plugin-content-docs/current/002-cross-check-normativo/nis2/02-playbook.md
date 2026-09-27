---
id: playbook
title: "SbD-ToE 4 NIS2: Implementation Playbook"
description: A practical roadmap for using SbD-ToE as the basis for NIS2 implementation, with additional regulatory formalisation where applicable
tags: [playbook, nis2, implementacao, roadmap]
sidebar_position: 3
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/nis2/02-playbook.md
  source_sha256: f8363d7877269c51bee6eeb004118270a929688f6ab667e85d14865116ae4c97
  source_commit: 340729d3c6203de3d943929de2e7a3d81bcfc89f
  target_sha256: e907ce9dd3e32a604c024a726649c51efc5a38fafd41f51dce646bec8fb81488
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [avaliacao, chapter_role, cycle_iteration, entity_type, eu_management_body, eu_startups, lifecycle_phase, maturity, mcp_reading_programa, nis2_early_warning, nis2_significant_incident, practitioner_manual, programme_line, requirement_runtime, risk_level, role_tech_lead, sbdtoe_sbd, slug_threat_modeling, validation_evaluation]
  glossary_sha256: 8a1c34891c4a75132fe7d9d1a3f2804c5199e2e543230143312b7ff1851111f2
  translated_at: 2026-09-27T14:46:11Z
  stamped_at: 2026-09-27T14:46:11Z
  reviewed_by: null
---

# SbD-ToE 4 NIS2: Implementation Playbook

## Overview {#visão-geral}

This playbook maps **NIS2 requirements (Directive (EU) 2022/2555) to practical SbD-ToE actions**.

**Principle:** Implementing SbD-ToE creates a strong basis for meeting NIS2, but full compliance also requires regulatory formalisation, explicit management accountability and national or sectoral parameterisation where applicable.

**Structure:** Each section shows:
- NIS2 requirement (article)
- Applicable SbD-ToE chapter/add-on
- What to do (concrete action)
- Regulatory evidence

Where necessary, the text explicitly distinguishes:
- what the core manual already supports well
- and what must be formalised outside the manual for a complete regulatory reading

> 📚 **Supporting Resources:** For practical templates and implementation examples, see [Example Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-toolchain-options), with reusable toolchains, KPIs, RACI and incident reports for NIS2 and other frameworks.

---

## Quick Map: NIS2 Art. → SbD-ToE {#mapa-rápido-nis2-art--sbd-toe}

| NIS2 Article | Requirement | SbD-ToE Chapter | Main Action |
|----------|-----------|-----------------|----------------|
| **20** | Governance and Accountability | [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Ch. 13](/sbd-toe/sbd-manual/formacao-onboarding/intro), [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Formalise management approval, oversight and training; use the technical catalogue as the supporting basis |
| **21** | Cybersecurity Risk-Management Measures | [Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Ch. 03](/sbd-toe/sbd-manual/threat-modeling/intro), [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro), [Ch. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro), [Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Implement technical controls, evidence and continuous review |
| **23** | Incident Reporting | [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Detection, internal escalation and preparation of external reporting |
| **Supply Chain** | Supplier Security | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | SBOM, technical due diligence and complementary supplier governance (`Art. 21(2)(d)`, `21(3)`, `22`) |
| **Continuity** | Business Continuity and Crisis Management | [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | Runbooks and exercises; backups with tested restore (OPS-016) and recovery of the application (OPS-017) (`Art. 21(2)(c)`); broad corporate BCM remains out of scope |

---

## How to Implement (Logical Order) {#como-implementar-ordem-lógica}

### Phase 1: Governance (M0–M2) {#fase-1-governação-m0m2}
**NIS2 Art. 20** - Establish management accountability

1. **Set up a Cybersecurity Committee**
   - Members: management body sponsor, CISO, CTO, GRC Manager, General Counsel
   - Frequency: Quarterly (minimum)
   - **Evidence:** Meeting minutes and formal decisions of the management body

2. **Approve the Cybersecurity Risk-Management Policy**
   - Main reference: [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)
   - Supporting technical baseline: [Ch. 02 - Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
   - **Approval:** Management body or equivalent formal chain provided for in the applicable governance model
   - **Content:** L1–L3 requirements, lifecycle, responsibilities, Art. 21 measures and oversight model

3. **Define the RACI**
   - Who approves what (formal approvals and oversight)
   - Escalations (when to escalate)
   - Reference: [Ch. 07 - Roles](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

4. **Establish a Training Programme for Management**
   - Periodicity: Annual (minimum)
   - Content: Threats, NIS2 requirements, responsibilities
   - **Evidence:** Attendance, materials, assessments
   - Reference: [Ch. 13 - Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)

---

### Phase 2: Classification and Inventory (M2–M4) {#fase-2-classificação-e-inventário-m2m4}
**NIS2 Art. 21** - Know what is critical

1. **Inventory Applications and Systems**
   - Name, owner, data processed, services supported
   - Dependencies (who depends on it)
   - **Entity type:** Essential / Important (under NIS2 Art. 3, based on the sectors in Annexes I/II and on size)
   - Reference: [Ch. 01 - Application Classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)

2. **Classify by Risk (L1–L3)**
   - L3: Direct impact on critical (essential) services
   - L2: Supports important processes
   - L1: Support tools
   - Matrix signed by CTO + Product leads + CISO

3. **Define Minimum Requirements per Level**
   - L1: Basics (passwords, logs, code review)
   - L2: Essentials (+ threat modelling, SAST)
   - L3: Rigorous (+ DAST, 24x7 monitoring)
   - Reference: [Ch. 02 - Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro)

---

### Phase 3: Cybersecurity Risk-Management Measures (M4–M8) {#fase-3-medidas-de-gestão-de-risco-m4m8}
**NIS2 Art. 21** - Implement technical and organisational measures

#### 3.1 Policies on Risk Analysis {#31-políticas-de-análise-de-risco}
- **What:** Identify and assess cybersecurity risks
- **How:** Threat modelling (L2–L3); impact analysis
- **Trail:** Document risks, decisions, mitigations
- **Reference:** [Ch. 03 - Threat Modelling](/sbd-toe/sbd-manual/threat-modeling/intro)

#### 3.2 Vulnerability Management and Patching {#32-gestão-de-vulnerabilidades-e-patching}
- **What:** SBOM (Software Bill of Materials) + SCA
- **Why:** Art. 21 requires vulnerability management and system updates
- **How:** Generate the SBOM; continuous scanning; update dependencies
- **Trail:** Keep the SBOM up to date, vulnerabilities documented
- **Reference:** [Ch. 05 - Dependencies & SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)

#### 3.3 Security in Development and Maintenance {#33-segurança-em-desenvolvimento-e-manutenção}
- **What:** Security gates in the pipeline
- **How:** SAST/SCA before merge; secrets blocking; pre-deploy validation
- **Trail:** Audited logs of who did what, and when
- **Reference:** [Ch. 06 - Secure Development](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro), [Ch. 07 - Secure CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro)

#### 3.4 IAM and Access Control {#34-iam-e-controlo-de-acessos}
- **What:** Strong authentication, privilege management
- **How:** MFA, principle of least privilege, periodic review
- **Trail:** Access logs, approvals, revocations
- **Reference:** [Ch. 02 - Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Ch. 04 - Secure Architecture](/sbd-toe/sbd-manual/arquitetura-segura/intro)

#### 3.5 Cryptography {#35-criptografia}
- **What:** Protection of data in transit and at rest
- **How:** TLS 1.2+; encryption at rest; key management
- **Trail:** Certificate inventory, key rotation
- **Reference:** [Ch. 02 - Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Ch. 04 - Secure Architecture](/sbd-toe/sbd-manual/arquitetura-segura/intro)

#### 3.6 Cyber Hygiene and Training {#36-higiene-cibernética-e-formação}
- **What:** Staff training, threat awareness
- **How:** Continuous training programme, simulations
- **Trail:** Attendance, materials, assessments
- **Reference:** [Ch. 13 - Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)

---

### Phase 4: Supply Chain Security (M6–M10) {#fase-4-segurança-da-cadeia-de-fornecimento-m6m10}
**NIS2 Art. 21** - Management of suppliers and third parties

#### 4.1 Component Suppliers (SBOM) {#41-fornecedores-de-componentes-sbom}
**Already in Phase 3.2** - [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) covers this with SCA + SBOM

#### 4.2 Contractual Suppliers {#42-fornecedores-contratuais}
- **What:** Contracted people/companies (contractors, outsourcing)
- **Lifecycle:**
  - **Onboarding:** Validation, SbD training, sandbox
  - **Operation:** Controlled access, periodic review
  - **Offboarding:** Access revocation, audit of completion
- **Reference:** [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)

#### 4.3 Register of Critical Suppliers {#43-registo-de-fornecedores-críticos}
- **What:** Inventory of critical ICT suppliers
- **How:** Fields as required by the national authority (follow local guides/portals)
- **Trail:** Periodic updates, risk assessments
- **Reference:** [Ch. 05 - Dependencies & SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)

---

### Phase 5: Incident Detection and Response (M8–M12) {#fase-5-deteção-e-resposta-a-incidentes-m8m12}
**NIS2 Art. 23** - Reporting of significant incidents

#### 5.1 Centralised Monitoring {#51-monitorização-centralizada}
- **What:** Centralised logs of apps, infrastructure, access
- **Retention:** As per ENISA/national authority guidance
- **Protection:** Immutability (prevent alteration)
- **Reference:** [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

#### 5.2 Incident Detection and Classification {#52-deteção-e-classificação-de-incidentes}
- **What:** Identify anomalous events; classify by severity
- **Escalation:** According to the plan (criticality)
- **Documentation:** What, when, actions, impact
- **Reference:** [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

#### 5.3 Reporting of Significant Incidents {#53-reporte-de-incidentes-significativos}
- **What:** Submit significant incidents to the CSIRT or, where applicable, the competent authority (Article 23(4))
- **Deadlines:**
  - **Early warning:** ≤ 24h after becoming aware
  - **Incident notification:** ≤ 72h after becoming aware, with an initial assessment
  - **Intermediate report:** at the request of the CSIRT or the competent authority
  - **Final report:** ≤ 1 month after the incident notification (if the incident is ongoing: an intermediate report at that time and a final report ≤ 1 month after it has been handled)
- **Schema:** Parameterise fields according to Art. 23 and ENISA guides
- **How:** SIEM/ITSM exporters → files ready for submission
- **Reference:** [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### Phase 6: Business Continuity and Crisis Management (M8–M12) {#fase-6-continuidade-e-crise-m8m12}
**NIS2 Art. 21** - Ensure operational continuity

#### 6.1 Backups and Disaster Recovery {#61-backups-e-disaster-recovery}
- **What:** Regular, tested, off-site backups
- **How:** Automation, periodic restore tests
- **Trail:** Logs of backups, tests, results
- **State in the Manual:** backups with tested restore in OPS-016 and recovery objectives and procedure in OPS-017 (Ch. 12); redundancy is a requirement of the NIS2 context for the relevant entities.
- **Reference:** [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

#### 6.2 Crisis Management {#62-gestão-de-crise}
- **What:** Response plan for significant incidents
- **How:** Runbooks, exercises, defined roles
- **Trail:** Documented exercises, lessons learned
- **Reference:** [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### Phase 7: Validation and Testing (M12–M18) {#fase-7-validação-e-testes-m12m18}
**NIS2 Art. 21** - Assess the effectiveness of controls

#### 7.1 Continuous Testing {#71-testes-contínuos}
- **SAST:** Static code analysis (integrated into CI/CD)
- **DAST:** Dynamic application analysis in staging
- **Penetration:** Manual testing based on the threat model
- **Reference:** [Ch. 10 - Security Testing](/sbd-toe/sbd-manual/testes-seguranca/intro)

#### 7.2 Pre-Deploy Validation {#72-validação-pré-deploy}
- **What:** Security checklist before production
- **Confirmation:** All L1–L3 requirements covered
- **Approval:** Formal (AppSec + Management for L3)
- **Reference:** [Ch. 11 - Secure Deployment](/sbd-toe/sbd-manual/deploy-seguro/intro)

#### 7.3 Effectiveness Assessment {#73-avaliação-da-eficácia}
- **What:** Periodic review of the implemented controls
- **How:** Internal audits, security metrics, testing
- **Trail:** Audit reports, remediation plans
- **Reference:** [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

## Compliance Checklist {#checklist-de-conformidade}

The list below makes it possible to validate the alignment of the SbD-ToE programme with the NIS2 requirements. Periodic review of these points is suggested to ensure continuous compliance:

- [ ] **Governance:** Formal approval and oversight chain documented; RACI mapped; annual training for management
- [ ] **Classification:** All apps classified L1–L3; entity type (essential/important) defined
- [ ] **Risk Policies:** Threat modelling implemented (L2–L3)
- [ ] **Vulnerabilities:** SBOM generated and kept up to date; continuous SCA
- [ ] **CI/CD:** Security gates operational
- [ ] **IAM:** MFA implemented; principle of least privilege in force
- [ ] **Cryptography:** TLS 1.2+; encryption at rest; key management
- [ ] **Training:** Continuous training programme operational
- [ ] **Suppliers:** Inventory of critical suppliers; lifecycle operational
- [ ] **Monitoring:** Centralised logs, adequate retention
- [ ] **Incidents:** Detection, escalation and 24h/72h/1M reporting preparation process active
- [ ] **Continuity:** Backups tested; runbooks and operational recovery validated
- [ ] **Testing:** SAST/DAST integrated; periodic effectiveness assessment
- [ ] **Evidence:** Data room with documentation (policies, tests, logs, training)

---

## What Each SbD-ToE Chapter Covers (Quick Reference) {#o-que-cada-capítulo-sbd-toe-cobre-referência-rápida}

| Chapter | NIS2 Articles | What It Does |
|----------|-------------|----------|
| **[Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)** | Art. 21 | Classification of apps by risk (L1–L3) |
| **[Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro)** | Art. 21 (primary), Art. 20 (support) | Technical baseline of minimum security requirements per level |
| **[Ch. 03](/sbd-toe/sbd-manual/threat-modeling/intro)** | Art. 21 | Threat modelling to identify realistic threats |
| **[Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro)** | Art. 21 | Secure architecture, IAM, cryptography |
| **[Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)** | Art. 21 | SBOM, SCA, vulnerability management |
| **[Ch. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro)** | Art. 21 | Secure development |
| **[Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro)** | Art. 21 | Secure CI/CD, gates, audited trail |
| **[Ch. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro)** | Art. 21 | Secure IaC |
| **[Ch. 09](/sbd-toe/sbd-manual/containers-imagens/intro)** | Art. 21 | Secure containers/runtime |
| **[Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro)** | Art. 21 | Continuous testing (SAST/DAST/penetration) |
| **[Ch. 11](/sbd-toe/sbd-manual/deploy-seguro/intro)** | Art. 21 | Pre-deploy validation, requirements compliance |
| **[Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)** | Art. 20 (oversight), Art. 21, 23 | Monitoring, incidents, runbooks, operational continuity and evidence |
| **[Ch. 13](/sbd-toe/sbd-manual/formacao-onboarding/intro)** | Art. 20, 21 | Cybersecurity training for staff and management |
| **[Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)** | Art. 20 (primary), Art. 21, 23 | Governance, approval chain, escalation and supplier lifecycle |

---

## Simple Metric: Am I Compliant? {#métrica-simples-estou-compliant}

An organisation that can answer YES to the following has a strong basis for a defensible NIS2 reading:

1. **Governance:** Do I have a formal management approval and oversight chain? ✓
2. **Board Training:** Does management have annual cybersecurity training? ✓
3. **Risk Management:** Are all apps classified? ✓
4. **Policies:** Do I have policies on risk analysis and security? ✓
5. **Vulnerabilities:** Do I have SBOM and SCA active? ✓
6. **Development:** Secure CI/CD with operational gates? ✓
7. **IAM & Crypto:** MFA and cryptography implemented? ✓
8. **Training:** Continuous training programme active? ✓
9. **Supply Chain:** Inventory of critical suppliers and operational lifecycle? ✓
10. **Operations:** Centralised monitoring with adequate retention? ✓
11. **Incident Response:** Can I detect, escalate internally and prepare 24h/72h/1M reporting? ✓
12. **Continuity:** Backups tested, runbooks and operational recovery validated? ✓
13. **Testing:** Do I perform SAST/DAST and effectiveness assessment? ✓
14. **Evidence:** Can I demonstrate all of this in an audit? ✓

**If 12/14:** The organisation has a strong basis for a NIS2 audit, but should still confirm the applicable national and sectoral requirements.  
**If `<`7/14:** Prioritise governance + classification + monitoring + incidents.

---

## Critical Note: Exception Management in NIS2 {#nota-crítica-gestão-de-exceções-em-nis2}

NIS2 requires compliance with cybersecurity risk-management measures (Art. 21). Exceptions (deviations) must be formal and audited, with a documentary trail and appropriate approval.

What characterises an exception in SbD-ToE/NIS2:
- Formal deviation from a requirement
- Example: Deploy with a high vulnerability (vs. L3 requirement = zero criticals)
- Formal approval, justification, TTL (Time-To-Live), remediation plan

Who approves (SbD-ToE proposal, framed by the responsibility of the management body laid down in Article 20 of NIS2):
- L1 (low risk): Tech Lead / AppSec Engineer
- L2 (medium risk): CISO
- L3 (critical): Board / CRO / equivalent management body, according to the applicable governance model

Regulatory implication:
- Exceptions without formal approval may compromise oversight (Art. 20)
- Some exceptions must be considered unacceptable by internal policy (e.g. exploitable SQLi, absence of MFA where appropriate); NIS2 requires corrective measures without undue delay where there is non-compliance (Art. 21(4))
- An audited trail is mandatory to demonstrate control to the national authority

Suggested:
1. Clear policy on who approves per risk level
2. Audited trail: What, who, when, justification, TTL
3. Remediation SLAs from the Manual's internal ladder (Policy 19 §4.3; the Manual's choice — Article 21(2)(e) requires vulnerability handling without setting time limits)
4. List of unacceptable exceptions (policy)
5. Periodic review, escalation if expired

The absence of formalisation may compromise regulatory compliance and expose the organisation to unnecessary risks.

**Reference:** [Ch. 02 - Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro) as the technical baseline and [Ch. 14 - Governance](/sbd-toe/sbd-manual/governanca-contratacao/intro) for formalising exceptions

---

## Practical Implementation Resources {#recursos-práticos-de-implementação}

For concrete support in implementing this playbook, see the following reusable examples:

- 🛠️ **[Toolchain Options](../exemplo-playbook/exemplo-toolchain-options)** - Comparison of tools (IaC, logs, SCA, SAST, CI/CD) with configuration examples
- 📊 **[KPIs and Targets](../exemplo-playbook/exemplo-kpis-targets)** - Security metrics per organisational profile compatible with NIS2
- 👥 **[RACI and Governance](../exemplo-playbook/exemplo-raci-governance)** - Responsibility matrices aligned with Art. 20 (management accountability)
- 📝 **[Incident Report](../exemplo-playbook/exemplo-relatorio-incidentes)** - Formal reporting templates with NIS2 timelines (24h/72h/1M)

These resources are **reusable across multiple frameworks** (NIS2, DORA, ISO 27001, CRA) and show how to implement the deliberate abstentions of SbD-ToE (the manual does not prescribe specific tools; the examples show practical options).

---

## Next Steps {#próximos-passos}

The following approach is suggested to ensure continuous compliance and maturity:

1. Current compliance audit: Check [Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)–[Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) of SbD-ToE against the NIS2 requirements
2. Verify the entity's classification: Essential / Important (as per Annexes I/II)
3. Define the roadmap: Sequence the phases according to the organisational context
4. Implement: Iterate as planned
5. Register with the national authority: Follow local guides/portals (if applicable)
6. Validate: Demonstrate compliance in an audit

Complete documentation: See SbD-ToE chapters 01–14 for technical and operational detail.

---

## References {#referências}

- **SbD-ToE Manual:** Chapters 01–14 (technical detail per domain)
- **NIS2 Cross-Check:** [Full normative analysis](/sbd-toe/cross-check-normativo/nis2/intro)
- **NIS2 Directive:** (EU) 2022/2555
- **ENISA:** Technical guidance and practical mappings (2024/2025)
- **National Authorities:** Registration guides/portals and local requirements

---

**Version:** 1.0  
**Date:** January 2025  
**Note:** This playbook complements the [NIS2 normative analysis](intro) with practical implementation
