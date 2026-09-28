---
id: playbook
title: "SbD-ToE 4 DORA: Implementation Playbook"
description: Practical roadmap for implementing SbD-ToE in line with DORA requirements - direct mapping of articles to actions
tags: [playbook, dora, implementacao, roadmap]
sidebar_position: 2
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/dora/02-playbook.md
  source_sha256: 63f95450da89cc2132f50c5244cacc2f0fc57d63bd655b21dff234687270c4e2
  source_commit: cd59ce0074d2e282eb290ceeaea128a60266b266
  target_sha256: 76ea7e6f70e9ba5e5f6fefb8957cca3e64b516c3a4003e2b8da982a6ea996f25
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [alcada, avaliacao, capacitacao, chapter_role, cycle_iteration, dora_ict_risk, dora_register_of_information, eu_management_body, eu_startups, framework_source_corpus, gap_family, layer, lifecycle_phase, mapping, maturity, mcp_reading_programa, normative_empirical, piso_limiar, practitioner_manual, programme_line, provenance, requirement_runtime, risk_level, role_procurement, sbdtoe_sbd, slug_threat_modeling, threat, traceability, validation_evaluation]
  glossary_sha256: c51c2f1a1ecc39532b3a2fe0f02b7ce3acac2e29e4e5c248aacf415764c4e9e3
  translated_at: 2026-09-28T09:11:48Z
  stamped_at: 2026-09-28T09:11:48Z
  reviewed_by: null
---

# SbD-ToE 4 DORA: Implementation Playbook

## Overview {#visão-geral}

This playbook maps **DORA requirements (Regulation (EU) 2022/2554) to practical SbD-ToE actions**.

**Principle:** Implementing SbD-ToE covers much of the **AppSec and operational baseline** required by DORA, but final compliance also depends on **additional regulatory formalisation** and on institutional artefacts that stay out of scope of the Manual.

What the Manual covers, the gaps it declares and what stays out of scope, obligation by obligation, are in [Applicable requirements — What this Manual covers and what stays out](./requisitos-aplicaveis#cobertura).

**Structure:** Each section shows:
- The DORA requirement or normative block
- The applicable SbD-ToE chapter/addon
- What to do
- Which part falls within the Manual (including the floor entries and the requirements added by the DORA context, on the [Applicable requirements](./requisitos-aplicaveis) page) and which part is out of scope

> 📚 **Supporting Resources:** For practical templates and implementation examples, see the [Example Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-toolchain-options), with reusable toolchains, KPIs, RACI and incident reports for DORA and other frameworks.

---

## Quick Map: DORA Art. → SbD-ToE {#mapa-rápido-dora-art--sbd-toe}

| DORA Article | Requirement | SbD-ToE Chapter | Main Action |
|----------|-----------|-----------------|----------------|
| **5** | Governance and responsibility of the management body | [Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Approve policies, oversee risk, formalise the chain of authority |
| **6** | ICT risk management framework | [Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Inventory, classify, link risk to requirements, evidence and review |
| **8–15** | Protection, prevention, detection, response, recovery, learning and communication | [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Ch. 03](/sbd-toe/sbd-manual/threat-modeling/intro), [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro), [Ch. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro), [Ch. 11](/sbd-toe/sbd-manual/deploy-seguro/intro), [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Ch. 13](/sbd-toe/sbd-manual/formacao-onboarding/intro) | Implement technical and operational controls with evidence, monitoring and improvement |
| **17–23** | Management, classification and reporting of ICT-related incidents | [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Detection, triage, escalation and parameterisation of regulatory reporting |
| **24–27** | Digital resilience testing programme and TLPT | [Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Ch. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Continuous testing, pre-deploy validation and bounded TLPT readiness |
| **28–30** | ICT third-party risk management | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | SBOM, due diligence, contractual clauses, lifecycle and exit |

---

## How to Implement It (Logical Order) {#como-implementar-ordem-lógica}

### Phase 1: Governance (M0–M2) {#fase-1-governação-m0m2}
**DORA Art. 5** - Establish oversight by the management body

1. **Create a formal digital security governance forum**
   - Members: board sponsor, CISO, CTO, GRC, legal/procurement
   - Frequency: regular and with a formal record
   - **Evidence:** minutes, decisions, owners, follow-up

2. **Approve the policy and the chain of authority**
   - Reference: [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)
   - **Approval:** at the management level appropriate to the regulatory context
   - **Content:** responsibilities, escalation, exceptions, reporting

3. **Define RACI and escalation criteria**
   - Who approves what
   - When to escalate
   - How to preserve the documentary trail
   - 📄 **Template:** [RACI and Governance](../exemplo-playbook/exemplo-raci-governance)

---

### Phase 2: ICT risk framework (M2–M4) {#fase-2-framework-de-risco-tic-m2m4}
**DORA Art. 6** - Structure ICT risk management

1. **Inventory applications and services**
   - Name, owner, supported function, data, dependencies
   - Reference: [Ch. 01 - Application Classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)

2. **Classify by risk**
   - Level L1–L3 per application, according to the axes of exposure, data sensitivity and impact (CLA-001)
   - Mark, per application, whether it supports a critical or important function (FCI grade of the DORA context, with a reference to the entity's inventory of functions): it is an axis separate from the level and adds its own floor requirements; L3 is not equivalent to a critical or important function
   - Reference: [Ch. 01 - Application Classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)

3. **Define minimum requirements per level**
   - L1: basic
   - L2: essential, with formal validation
   - L3: reinforced rigour with greater evidence
   - Reference: [Ch. 02 - Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro)

4. **Formalise evidence, review and owners**
   - Record decisions, exceptions, owners and review cycles
   - Ensure periodic reporting to management and GRC
   - Reference: [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)

---

### Phase 3: Protection, prevention, detection and recovery (M4–M12) {#fase-3-proteção-prevenção-deteção-e-recuperação-m4m12}
**DORA Art. 8–15** - Implement technical and operational controls

#### 3.1 Threat modelling, requirements and architecture {#31-threat-modeling-requisitos-e-arquitetura}
- **What:** link risk, threats, requirements and architectural decisions
- **How:** proportional threat modelling; versioned requirements; secure architecture
- **Trail:** risk → threat → requirement → control → evidence
- **References:** [Ch. 02 - Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Ch. 03 - Threat Modelling](/sbd-toe/sbd-manual/threat-modeling/intro), [Ch. 04 - Secure Architecture](/sbd-toe/sbd-manual/arquitetura-segura/intro)

#### 3.2 Development, CI/CD, IaC and supply chain {#32-desenvolvimento-cicd-iac-e-supply-chain}
- **What:** harden the delivery chain and the composition of the software
- **How:** SAST/SCA; secret blocking; provenance; pre-deploy validation; SBOM; IaC scanning
- **Trail:** audited logs, up-to-date SBOM, findings, gates and formal exceptions
- **References:** [Ch. 05 - Dependencies & SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Ch. 07 - Secure CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro), [Ch. 08 - IaC](/sbd-toe/sbd-manual/iac-infraestrutura/intro), [Ch. 11 - Secure Deployment](/sbd-toe/sbd-manual/deploy-seguro/intro)
- 📄 **Template:** [Toolchain Options](../exemplo-playbook/exemplo-toolchain-options)

#### 3.3 Monitoring, response, recovery and learning {#33-monitorização-resposta-recuperação-e-aprendizagem}
- **What:** monitor, react, contain, recover and learn from events and deviations
- **How:** structured logging; alerts with SLAs; rollback; runbooks; metrics; continuous training
- **Trail:** operational evidence, post-incident reviews, KPIs and reporting
- **Recovery:** backups with tested restoration (OPS-016) and recovery objectives and procedure for the application (OPS-017); redundant capacities and switchover testing are a requirement added by the DORA context (CTX-DORA-R01). The entity's continuity plans (Article 11) stay outside the Manual.
- **DORA context floor:** IRP at any level (Policy 32 §2; CTX-DORA-P01); dynamic testing (TST-005; P03); annual access review, and half-yearly for critical or important functions (ACC-010; P05, P06); strong authentication (AUT-001; P07); weekly vulnerability scanning of the assets supporting critical or important functions (Policy 10 §9; P08); responsible disclosure (GOV-015; P10); privileged accounts and identity lifecycle (GOV-016, GOV-017; P13, P14); key lifecycle and certificate register (ENC-007; P15, P16); cryptographic agility (ENC-003; P17); half-yearly review of network filtering rules (ARC-006; P18). See [Applicable requirements](./requisitos-aplicaveis#cobertura).
- **References:** [Ch. 11 - Secure Deployment](/sbd-toe/sbd-manual/deploy-seguro/intro), [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Ch. 13 - Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)

---

### Phase 4: Incidents and regulatory reporting (M8–M12) {#fase-4-incidentes-e-reporte-regulatório-m8m12}
**DORA Art. 17–23** - Manage, classify and report ICT-related incidents

#### 4.1 Centralised monitoring {#41-monitorização-centralizada}
- **What:** centralised logs of applications, infrastructure and access
- **Retention:** in line with internal policy and the applicable regulatory framework
- **Protection:** immutability, integrity and traceability
- **Reference:** [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

#### 4.2 Detection, triage and response {#42-deteção-triagem-e-resposta}
- **What:** identify events, classify them by impact and respond
- **Escalation:** according to criticality and the governance model
- **Documentation:** what, when, actions, learning
- **References:** [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)
- 📄 **Template:** [Incident Report](../exemplo-playbook/exemplo-relatorio-incidentes)

#### 4.3 Parameterisation of external reporting {#43-parametrização-de-reporte-externo}
- **What:** translate the internal process into `initial`, `intermediate` and `final report`, within the time limits set by the RTS (Delegated Regulation (EU) 2025/301, Art. 5: initial notification ≤ 4 h after classification as major and ≤ 24 h after becoming aware; intermediate report ≤ 72 h after the initial notification; final report ≤ 1 month after the latest intermediate report) and inform the affected clients without undue delay (Article 19(3))
- **How:** start from the impact data (Policy 32 §4.3), classify using the criteria of Article 18 and the thresholds of Delegated Regulation (EU) 2024/1772, with a monthly assessment of recurring incidents (CTX-DORA-R02), and use the content of Policy 32 §6.1 (templates of Implementing Regulation (EU) 2025/302)
- **Boundary:** submission, channels and the relationship with the competent authority stay out of scope of the Manual
- **References:** [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)

---

### Phase 5: Resilience testing (M12–M18) {#fase-5-testes-de-resiliência-m12m18}
**DORA Art. 24–27** - Validate the defensive posture and prepare for TLPT

#### 5.1 Continuous testing {#51-testes-contínuos}
- **SAST:** integrated static analysis
- **DAST:** dynamic analysis in staging, mandatory at any level in the DORA context, with testing of Internet-facing systems and applications (TST-005; CTX-DORA-P03)
- **PenTesting:** manual testing guided by the threat model
- **Reference:** [Ch. 10 - Security Testing](/sbd-toe/sbd-manual/testes-seguranca/intro)

#### 5.2 Pre-deploy validation {#52-validação-pré-deploy}
- **What:** security checklist before production
- **Confirmation:** requirements and evidence consistent with the risk level
- **Approval:** formal where applicable
- **Reference:** [Ch. 11 - Secure Deployment](/sbd-toe/sbd-manual/deploy-seguro/intro)

#### 5.3 TLPT readiness and regulatory boundary {#53-tlpt-readiness-e-boundary-regulatório}
- **What:** prepare the technical foundation for TLPT exercises in eligible entities
- **Basis:** threat model scenarios, scope, remediation and evidence
- **Boundary:** eligibility, formal qualification of testers and attestation belong to the regulatory/compliance layer
- **References:** [Ch. 10 - Security Testing](/sbd-toe/sbd-manual/testes-seguranca/intro), [Ch. 11 - Secure Deployment](/sbd-toe/sbd-manual/deploy-seguro/intro)

---

### Phase 6: ICT third parties and critical suppliers (M12–M18) {#fase-6-terceiros-tic-e-fornecedores-críticos-m12m18}
**DORA Art. 28–30** - Manage ICT third-party risk

#### 6.1 Component suppliers and software supply chain {#61-fornecedores-de-componentes-e-supply-chain-de-software}
- **What:** SBOM + SCA
- **How:** generate the SBOM; continuous scanning; update dependencies
- **Trail:** inventory, findings, fixes and exceptions
- **Reference:** [Ch. 05 - Dependencies & SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)

#### 6.2 Contractual suppliers {#62-fornecedores-contratuais}
- **What:** contractors, outsourcing and partners with access or technical responsibility
- **Lifecycle:**
  - **Onboarding:** validation, SbD training, sandbox
  - **Operation:** controlled access, periodic review
  - **Offboarding:** access revocation, closure audit
- **Reference:** [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)

#### 6.3 Concentration and exit {#63-concentração-e-saída}
- **What:** assess concentration, critical dependencies and exit strategy
- **How:** inventory, periodic revalidation, contractual clauses and transition plans
- **Boundary:** the register of information (Implementing Regulation (EU) 2024/2956), concentration analysis and the entity's exit strategies stay out of scope of the Manual (relationship with the supervisor and business continuity); the transition and full data migration plans are a declared gap.
- **References:** [Ch. 05 - Dependencies & SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)

---

## DORA Reading Checklist {#checklist-de-leitura-dora}

The list below makes it possible to validate the maturity of the **AppSec and operational foundation** for a defensible DORA reading. Final compliance still depends on regulatory parameterisation and additional institutional evidence:

- [ ] **Governance:** Policy approved; clear chain of authority; periodic reporting
- [ ] **Risk framework:** All apps classified and linked to requirements by level
- [ ] **Requirements:** Versioned and traceable catalogue
- [ ] **Technical supply chain:** SBOM generated and continuous SCA
- [ ] **Pipeline:** Operational security gates
- [ ] **Monitoring:** Centralised logs, adequate protection and retention
- [ ] **Incidents:** IRP at any level (CTX-DORA-P01); DORA classification (CTX-DORA-R02) and the content of Policy 32 §6.1
- [ ] **Suppliers:** Inventory, due diligence and operational lifecycle
- [ ] **Testing:** SAST/DAST integrated; readiness for TLPT where applicable
- [ ] **Evidence:** Data room with policies, tests, logs, contracts and reporting

---

## What Each SbD-ToE Chapter Covers (Quick Reference) {#o-que-cada-capítulo-sbd-toe-cobre-referência-rápida}

| Chapter | DORA Articles | What It Does |
|----------|-------------|----------|
| **[Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)** | Art. 5, 6 | Classification of apps by risk and proportionality |
| **[Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro)** | Art. 6, 8–15 | Minimum requirements, traceability and validation |
| **[Ch. 03](/sbd-toe/sbd-manual/threat-modeling/intro)** | Art. 8–15, 24–27 | Threat modelling for realistic scenarios |
| **[Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)** | Art. 8–15, 28–30 | SBOM, SCA, software supply chain |
| **[Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro)** | Art. 8–15 | Secure CI/CD, gates, audited trail |
| **[Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro)** | Art. 24–27 | Continuous testing, readiness and evidence |
| **[Ch. 11](/sbd-toe/sbd-manual/deploy-seguro/intro)** | Art. 8–15, 24–27 | Pre-deploy validation, rollback and containment |
| **[Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)** | Art. 8–15, 17–23 | Monitoring, incidents, response and internal reporting |
| **[Ch. 13](/sbd-toe/sbd-manual/formacao-onboarding/intro)** | Art. 8–15 | Continuous training and upskilling |
| **[Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)** | Art. 5, 6, 17–23, 28–30 | Governance, RACI, reporting and supplier lifecycle |

The column shows where each chapter contributes, not that the article is covered. In Articles 28–30, the Manual covers parts of due diligence and of the clauses and supports evidence; the register of information and concentration analysis stay out of scope. In Article 19, Policy 32 §6 supports evidence, and the relationship with the authority stays out of scope. The detail is in [Applicable requirements](./requisitos-aplicaveis#cobertura).

---

## Simple Metric: Am I Well Prepared? {#métrica-simples-estou-bem-preparado}

Each affirmative answer scores one point and indicates the maturity of the AppSec baseline for a defensible DORA implementation:

1. **Governance:** Do I have an approved policy and a clear chain of authority?
2. **Risk Management:** Are all apps classified and linked to requirements?
3. **Security by Design:** Are my requirements and controls traceable?
4. **Software Supply:** Do I have SBOM and SCA in place?
5. **Operations:** Do I have centralised monitoring with adequate retention and protection?
6. **Incident Response:** Can I detect and classify incidents and configure their reporting?
7. **Vendor Management:** Do I have a formal lifecycle for contractors and critical third parties?
8. **Testing:** Do I run SAST/DAST and am I ready for TLPT where applicable?
9. **Evidence:** Can I demonstrate all of this in an audit and in regulatory reporting?

**Practical reading:** the more positive answers, the more mature the AppSec baseline. Moving to full DORA compliance still requires what the Manual leaves out of scope, with the reason (business continuity and crisis management, physical and workstation security, register of information, regulated TLPT, reporting channels), formalisation by the management body and the closing of the gaps declared in [Applicable requirements](./requisitos-aplicaveis#cobertura).

---

## Critical Note: Exception Management under DORA {#nota-crítica-gestão-de-exceções-em-dora}

The DORA framework requires exceptions to the implementation of the ICT security policies to be recorded and resilience to be ensured in those cases (Delegated Regulation (EU) 2024/1774, Article 2(2), point (c)); the acceptance of residual risks above the tolerance requires assigned roles, a justified inventory and annual review (Article 3, point (d)). The concrete approval level is defined by the entity.

What characterises an exception in SbD-ToE/DORA:
- a formal deviation from a requirement;
- technical and business justification;
- a validity period (`TTL`);
- a remediation plan and an owner;
- an auditable documentary trail.

Who approves depends on criticality, the governance model and the applicable regulatory framework. In the Manual, the approval authority for exceptions goes no higher than the CISO (Policy 05 §6), and Critical is not acceptable as an exception at L3. In critical contexts, a DORA reading tends to require escalating the decision to the management body: that is the entity's decision, out of scope of the Manual.

Practical reading:
- exceptions without formal approval undermine oversight;
- some exceptions may be unacceptable in a defensible regulatory reading;
- the Manual covers the process well, but final admissibility still depends on the regulatory context.

**References:** [Ch. 02 - Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro) and [Ch. 14 - Governance](/sbd-toe/sbd-manual/governanca-contratacao/intro)

---

## Practical Implementation Resources {#recursos-práticos-de-implementação}

For concrete support in implementing this playbook, see the following reusable examples:

- 🛠️ **[Toolchain Options](../exemplo-playbook/exemplo-toolchain-options)** - Comparison of tools (IaC, logs, SCA, SAST, CI/CD) with configuration examples
- 📊 **[KPIs and Targets](../exemplo-playbook/exemplo-kpis-targets)** - Security metrics by organisational profile
- 👥 **[RACI and Governance](../exemplo-playbook/exemplo-raci-governance)** - DORA-compatible responsibility and approval matrices
- 📝 **[Incident Report](../exemplo-playbook/exemplo-relatorio-incidentes)** - Formal reporting templates with DORA fields

These resources are reusable across multiple frameworks and show how to operationalise, outside the base Manual, the details that depend on the regulatory context, the supervisor and tooling.

---

## Next Steps {#próximos-passos}

1. Carry out an audit of current compliance against the matrix above
2. Sequence the roadmap by criticality, gap and dependency
3. Implement in phases, with versioned evidence
4. Link the content of Policy 32 §6.1 to the authority's channels and take care of what stays out of scope (register of information, concentration, continuity)
5. Periodically validate documentary and operational readiness

Full documentation: see SbD-ToE chapters 01–14 for technical and operational detail.

---

## References {#referências}

- **SbD-ToE Manual:** Chapters 01–14
- **DORA Cross-Check:** [Full normative analysis](/sbd-toe/cross-check-normativo/dora/intro)
- **DORA Regulation:** Regulation (EU) 2022/2554

---

**Version:** 1.3 (aligned with the coverage matrix and the DORA context)  
**Date:** September 2026  
**Note:** This playbook complements the [DORA normative analysis](intro) with bounded, evidence-oriented practical implementation.
