---
id: playbook
title: "SbD-ToE 4 NIS2: Implementation Playbook"
description: A practical roadmap for using SbD-ToE as the basis for NIS2 implementation, with additional regulatory formalisation where applicable
tags: [playbook, nis2, implementacao, roadmap]
sidebar_position: 3
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/nis2/02-playbook.md
  source_sha256: 1778d9b11573fd90b52ec54566739d7bb6f7888c551c3214e4d7c02fdac3d667
  source_commit: f2e7be9ecdd9179e9770d80bc6363f7da7f1d9aa
  target_sha256: 149287e29ca19a086db229d62c21b6cafc7fe8bef4d8cece74490fd056357bde
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [alcada, avaliacao, chapter_role, cycle_iteration, entity_type, eu_management_body, eu_startups, gap_family, lifecycle_phase, maturity, mcp_reading_programa, nis2_early_warning, nis2_significant_incident, piso_limiar, practitioner_manual, programme_line, requirement_runtime, risk_level, role_tech_lead, sbdtoe_sbd, slug_threat_modeling, validation_evaluation]
  glossary_sha256: 423e41a2c5ce34e44ebbfdc6855ce1cb1368a23fbd4f5c7cab8b3c5e45253913
  translated_at: 2026-09-28T09:11:50Z
  stamped_at: 2026-09-28T09:11:50Z
  reviewed_by: null
---

# SbD-ToE 4 NIS2: Implementation Playbook

## Overview {#visão-geral}

This playbook maps **NIS2 requirements (Directive (EU) 2022/2555) to practical SbD-ToE actions**.

**Principle:** Implementing SbD-ToE creates a strong basis for meeting NIS2, but full compliance also requires regulatory formalisation, explicit management accountability and national or sectoral parameterisation where applicable.

What the Manual covers, the gaps it declares and what stays out of scope, obligation by obligation, are in [Applicable requirements — What this Manual covers and what stays out](./requisitos-aplicaveis#cobertura).

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
   - Reference: [Foundations - Roles and responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

4. **Establish a Training Programme for Management**
   - Periodicity: Annual (minimum)
   - Content: Threats, NIS2 requirements, responsibilities
   - **Evidence:** Attendance, materials, assessments
   - Reference: [Ch. 13 - Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
   - **Status in the Manual:** Policy 37 provides only “Executive awareness” at L1; the programme for the management body is a declared gap, and it is for the organisation to formalise it.

---

### Phase 2: Classification and Inventory (M2–M4) {#fase-2-classificação-e-inventário-m2m4}
**NIS2 Art. 21** - Know what is critical

1. **Inventory Applications and Systems**
   - Name, owner, data processed, services supported
   - Dependencies (who depends on it)
   - **Entity type:** Essential / Important (under NIS2 Art. 3, based on the sectors in Annexes I/II and on size)
   - Reference: [Ch. 01 - Application Classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)

2. **Classify by Risk (L1–L3)**
   - Level L1–L3 per application, according to the axes of exposure, data sensitivity and impact (CLA-001); the level does not correspond to the NIS2 categories of essential entities and important entities
   - The NIS2 context is declared per entity and applies its floor to all applications; for the relevant entities under Implementing Regulation (EU) 2024/2690, the PERTINENTE-grade floor also applies
   - Matrix signed by CTO + Product leads + CISO

3. **Define Minimum Requirements per Level**
   - L1: baseline (authentication, logs, code review, SAST as a gate — DEV-003 —, SCA blocking Critical and High — DEP-002)
   - L2: adds formal threat modelling (THR-001), DAST (TST-005), log centralisation and automatic alerts (OPS-004, OPS-005)
   - L3: reinforced rigour and evidence; the exact selection per level is in the catalogue
   - Reference: [Ch. 02 - Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro)

---

### Phase 3: Cybersecurity Risk-Management Measures (M4–M8) {#fase-3-medidas-de-gestão-de-risco-m4m8}
**NIS2 Art. 21** - Implement technical and organisational measures

#### 3.1 Policies on Risk Analysis {#31-políticas-de-análise-de-risco}
- **What:** Identify and assess cybersecurity risks
- **How:** threat modelling at L2 and L3 (THR-001); at L1, only the light LINDDUN strand when there is personal data (THR-003). The entity's risk tolerance and business impact analysis (BIA) are not prescribed by the Manual: they are declared gaps.
- **Trail:** Document risks, decisions, mitigations
- **Reference:** [Ch. 03 - Threat Modelling](/sbd-toe/sbd-manual/threat-modeling/intro)

#### 3.2 Vulnerability handling and disclosure {#32-gestão-de-vulnerabilidades-e-patching}
- **What:** SBOM and SCA, and a coordinated disclosure process that receives and handles external reports (GOV-015, mandatory at any level in the NIS2 context: CTX-NIS2-P14; for relevant entities, in line with the national coordinated disclosure policy: CTX-NIS2-P15)
- **Why:** Article 21(2)(e) calls for vulnerability handling and disclosure
- **How:** Generate SBOM; continuous scanning; update dependencies; publish the channel for receiving external reports
- **Trail:** Keep the SBOM up to date, vulnerabilities documented
- **Out of scope:** patching of operating systems, network equipment and off-the-shelf software (entity security).
- **Reference:** [Ch. 05 - Dependencies & SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)

#### 3.3 Security in Development and Maintenance {#33-segurança-em-desenvolvimento-e-manutenção}
- **What:** Security gates in the pipeline
- **How:** SAST/SCA before merge; secrets blocking; pre-deploy validation
- **Trail:** Audited logs of who did what, and when
- **Reference:** [Ch. 06 - Secure Development](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro), [Ch. 07 - Secure CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro)

#### 3.4 IAM and Access Control {#34-iam-e-controlo-de-acessos}
- **What:** Strong authentication, privilege management
- **How:** MFA (AUT-001); least privilege; access review at planned intervals (ACC-010, GOV-014); privileged and administration accounts with strong authentication and a documented lifecycle (GOV-016, GOV-017), mandatory for relevant entities (CTX-NIS2-P12, P13, P18, P19).
- **Declared gaps:** exclusive use and separation of administration systems (point 11.4.2) and periodic review of authentication technologies (point 11.6.4).
- **Trail:** Access logs, approvals, revocations
- **Reference:** [Ch. 02 - Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Ch. 04 - Secure Architecture](/sbd-toe/sbd-manual/arquitetura-segura/intro)

#### 3.5 Cryptography {#35-criptografia}
- **What:** Protection of data in transit and at rest
- **How:** TLS 1.2+; encryption at rest; key management
- **Trail:** Certificate inventory, key rotation
- **Reference:** [Ch. 02 - Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Ch. 04 - Secure Architecture](/sbd-toe/sbd-manual/arquitetura-segura/intro)

#### 3.6 Cyber Hygiene and Training {#36-higiene-cibernética-e-formação}
- **What:** training for technical roles and for third parties with access (TRN-001, TRN-002, TRN-007)
- **How:** Continuous training programme, simulations
- **Declared gap:** scheduled awareness and cyber hygiene practices for all non-technical staff and for the management body.
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
- **Status in the Manual:** secure contracting policy (Policy 33), security clauses (GOV-006) and supplier validation (GOV-007); for relevant entities, at any level (CTX-NIS2-P07 to P09). The register fields the national authority asks for belong to the organisation.
- **Trail:** Periodic updates, risk assessments
- **Reference:** [Ch. 05 - Dependencies & SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)

---

### Phase 5: Incident Detection and Response (M8–M12) {#fase-5-deteção-e-resposta-a-incidentes-m8m12}
**NIS2 Art. 23** - Reporting of significant incidents

#### 5.1 Centralised Monitoring {#51-monitorização-centralizada}
- **What:** centralised application and access logs (LOG-001, OPS-001); for relevant entities, regular analysis, threshold-based alarms and backup of logs (CTX-NIS2-P03 to P06). Network traffic and the execution of system utilities are entity security, outside the Manual.
- **Retention:** period defined per log type (LOG-005; Policy 29 §7, the Manual's choice); the most demanding period of the law, national transposition or the supervisor prevails
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
- **Content:** impact data from the record (Policy 32 §4.3); significant incident criterion (CTX-NIS2-R02) and, for relevant entities, thresholds and aggregation of recurring incidents (CTX-NIS2-R03; Policy 32 §4.7); minimum content of each stage (Policy 32 §6.1)
- **How:** SIEM/ITSM exporters to the national CSIRT's forms; the forms and channels belong to the authority
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

#### 6.2 Response to serious incidents (crisis management stays outside) {#62-gestão-de-crise}
- **What:** IRP with playbooks, P1 war room and post-mortem with review of the affected artefacts (Policy 32 §4.6; mandatory at any level in the NIS2 context: CTX-NIS2-P01)
- **How:** Runbooks, exercises, defined roles
- **Trail:** Documented exercises, lessons learned
- **Out of scope:** the entity's crisis management (Implementing Regulation (EU) 2024/2690, point 4.3) and the business continuity plan.
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
- **Declared gap:** independent review of the approach to security as a whole and hierarchical independence of reviewers (points 2.3.1 and 2.3.2).
- **Reference:** [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

## Compliance Checklist {#checklist-de-conformidade}

The list below makes it possible to validate the alignment of the SbD-ToE programme with NIS2 requirements. Periodic review of these points is suggested to keep the alignment:

- [ ] **Governance:** Formal approval and oversight chain documented; RACI mapped; annual training of the management body (provided by the organisation: a declared gap of the Manual)
- [ ] **Classification:** All apps classified L1–L3; entity type (essential/important) defined
- [ ] **Risk Policies:** Formal threat modelling (L2–L3) and light LINDDUN at L1 when there is personal data (THR-003)
- [ ] **Vulnerabilities:** SBOM generated and kept up to date; continuous SCA
- [ ] **CI/CD:** Security gates operational
- [ ] **IAM:** MFA implemented; principle of least privilege in force
- [ ] **Cryptography:** TLS 1.2+; encryption at rest; key management
- [ ] **Training:** Continuous training programme operational
- [ ] **Suppliers:** Inventory of critical suppliers; lifecycle operational
- [ ] **Monitoring:** Centralised logs, adequate retention
- [ ] **Incidents:** IRP at any level (CTX-NIS2-P01); detection, escalation and the minimum content of Policy 32 §6.1 for 24h/72h/1M reporting
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
| **[Ch. 13](/sbd-toe/sbd-manual/formacao-onboarding/intro)** | Art. 20, 21 | Training for technical roles and for third parties with access; training of the management body is a declared gap |
| **[Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)** | Art. 20 (primary), Art. 21, 23 | Governance, approval chain, escalation and supplier lifecycle |

---

## Simple metric: self-assessment of the baseline {#métrica-simples-estou-compliant}

Each affirmative answer scores one point; how to read the result follows the list.

1. **Governance:** Do I have a formal chain of approval and oversight by management?
2. **Board Training:** Does management receive annual cybersecurity training?
3. **Risk Management:** Are all apps classified?
4. **Policies:** Do I have risk analysis and security policies?
5. **Vulnerabilities:** Do I have SBOM and SCA in place?
6. **Development:** Secure CI/CD with operational gates?
7. **IAM & Crypto:** MFA and cryptography implemented?
8. **Training:** Continuous training programme in place?
9. **Supply Chain:** Inventory of critical suppliers and operational lifecycle?
10. **Operations:** Centralised monitoring with adequate retention?
11. **Incident Response:** Can I detect, escalate internally and prepare 24h/72h/1M reporting?
12. **Continuity:** Tested backups, runbooks and operational recovery validated?
13. **Testing:** Do I run SAST/DAST and assess effectiveness?
14. **Evidence:** Can I demonstrate all of this in an audit?

**With 12 or more out of 14:** the application-side baseline is strong. For a NIS2 audit, what is still missing are the entity's measures that the Manual leaves out of scope (physical security, workstations, HR, continuity and crisis, inventory of all assets), the gaps declared in [Applicable requirements](./requisitos-aplicaveis#cobertura) and national and sectoral requirements.  
**With fewer than 7 out of 14:** the priority is governance, classification, monitoring and incidents.

---

## Critical Note: Exception Management in NIS2 {#nota-crítica-gestão-de-exceções-em-nis2}

NIS2 requires compliance with cybersecurity risk-management measures (Art. 21). Exceptions (deviations) must be formal and audited, with a documentary trail and appropriate approval.

What characterises an exception in SbD-ToE/NIS2:
- Formal deviation from a requirement
- Example: a deploy with an unfixed High vulnerability, when SCA blocks Critical and High at any level (DEP-002)
- Formal approval, justification, TTL (Time-To-Live), remediation plan

Who approves, in the Manual (Policy 05 §6):
- L1: Tech Lead or AppSec Engineer
- L2: AppSec Engineer, with Product Management for High, and the CISO for Critical
- L3: AppSec Engineer with GRC for Medium and the CISO for High; Critical is not acceptable as an exception

Escalating the decision to the management body, as a reading of Article 20 suggests, is formalisation by the organisation: the Manual does not prescribe it (a declared gap against Implementing Regulation (EU) 2024/2690, point 2.3.3).

Regulatory implication:
- Exceptions without formal approval may compromise oversight (Art. 20)
- The limits on exceptions are those of Policy 05 (approval authorities and deadlines by severity and level; Critical not acceptable in L3); NIS2 does not list inadmissible exceptions, but it requires corrective measures without undue delay when there is non-compliance (Art. 21(4))
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

These resources are **reusable across multiple frameworks** (NIS2, DORA, ISO 27001, CRA) and show practical options for what SbD-ToE leaves deliberately configurable (the manual does not prescribe specific tools).

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

**Version:** 1.1  
**Date:** September 2026  
**Note:** This playbook complements the [NIS2 normative analysis](intro) with practical implementation
