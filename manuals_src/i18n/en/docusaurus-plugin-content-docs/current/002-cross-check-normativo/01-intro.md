---
id: intro
title: Introduction - Normative cross-check
description: Framing of the normative analysis chapter, which shows how SbD-ToE intersects with different normative instruments and regulations
tags: [cross-check, normativos, compliance, dora, nis2, ai-act, cra, gdpr, enisa-csa]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/01-intro.md
  source_sha256: 2ae8e45aaf79de4abc690a67eff419c5facb25c27220ed1b75b9a350ee31a23f
  source_commit: 5bc57a2de453d4a50f78edcfb2b9546615b20690
  target_sha256: b25b602b877992fd4fb4cdbc877dfb12ce74166f5c8a0634bb0db3b55ee11222
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [appsec_core, avaliacao, chapter_role, cycle_iteration, discipline, dnt_fedramp_name, dnt_soc2_name, dora_financial_entity, dora_ict_risk, esquema_regime, eu_ce_marking, framework_source_corpus, gap_family, instrument, lifecycle_phase, maturity, normative_empirical, papel_suporte, piso_limiar, piso_relacao, practitioner_manual, prescriptive, requirement_runtime, role_juridico, sbdtoe_sbd, schema]
  glossary_sha256: 4483d8494d0ff6a4b761938050eaa6f3c5162de0175decf4517b376c1624c8e0
  translated_at: 2026-09-27T23:09:20Z
  stamped_at: 2026-09-27T23:09:20Z
  reviewed_by: null
---



# Introduction - Normative cross-check

Software security does not happen in a technical vacuum.  
Organisations in different sectors are subject to **regulations, standards and frameworks** that set explicit requirements to ensure adequate protection of systems, data and operations.  
In this context, **Security by Design - Theory of Everything (SbD-ToE)** is not only a prescriptive manual of good practice: it is also an **instrument of normative convergence**, making it possible to align secure development and operation practices with multiple external demands.

**Chapter 002 - Normative cross-check** plays precisely this role:  
- Demonstrate, in a clear and verifiable way, **how SbD-ToE responds to regulatory and normative requirements**.  
- Identify where the model covers requirements, where there are **declared gaps** and what is **out of scope**, with the reason; the gaps and what is left out call for complementary legal, organisational or contractual processes.  
- Support **GRC teams, auditors, technical teams and management teams** in the task of articulating operational security with formal compliance.
- For **organisations that own or contract software development**, offer **practical playbooks** to implement normative requirements consistently with the discipline of application security.

---

## Context and Rationale {#contexto-e-justificação}

Historically, the normative security landscape has evolved in a fragmented way:  
- **Two decades ago**, few standards existed, often limited to generic risk management requirements.  
- **With digitalisation**, an explosion of sectoral and regulatory normative instruments followed: **HIPAA** for healthcare, **PCI-DSS** for payments, **GDPR** for personal data protection, **NIS2** and **DORA** for European cyber resilience, among many others.  
- Today, the challenge is not a lack of normative instruments but the **excess of overlap** and the resulting difficulty of coherent practical application.

SbD-ToE was conceived as a response to this problem.  
Being built **top-down**, on the basis of multiple normative references, technical frameworks and maturity models (ISO, ENISA, NIST, OWASP SAMM, BSIMM, SSDF, DSOMM, SLSA, etc.), the manual ensures that:  

- **Normative requirements are incorporated from the root**, not treated as external or additive layers.  
- **Compliance is not an isolated goal**: applying secure practices throughout the lifecycle produces the technical evidence that regulations ask for, and the Manual declares what remains to be done.  
- **Each knowledge area** (requirements, architecture, CI/CD, containers, governance, etc.) contributes requirements and evidence to that answer.

---

## Objectives of this chapter {#objetivos-deste-capítulo}

1. **Show the correspondence** between SbD-ToE practices and the requirements of international and European normative instruments.  
2. **Show the areas covered**, where adopting the Manual provides the technical evidence the regulation asks for.  
3. **Declare the gaps and what is out of scope**, with no grey areas, helping organisations understand where they need additional measures (legal, procedural or technical).  
4. **Provide a comparative repository** that can be reused in audits, certifications or compliance reports.
5. **Offer implementation playbooks** for organisations that contract or develop software, ensuring that acquisition/development is consistent with specific normative requirements.

---

## Methodology adopted {#metodologia-adotada}

The analysis follows a systematic structure, common to all normative instruments:  

- **Framing** → brief description of the normative instrument, its scope and objectives.  
- **Coverage matrix** → each obligation of the regulation, checked against the consolidated text, has one of three answers, and none is left unanswered:  
  - **Covers**, stating how: catalogue requirement, policy, floor or requirement added by the regime, or engineering evidence for a duty that sits on another plane (the latter never counts as coverage of the duty itself).  
  - **Declared gap**, stating what is missing; when the gap depends on a future round of the AppSec Core, the round is indicated.  
  - **Out of scope**, with the reason.  
  The “Applicable requirements” pages (and, for the CSA, “Coverage”) are generated from this matrix and take precedence over hand-written text.  
- **Regulatory contexts** → the core of the Manual is regulation-agnostic. When an application is subject to a regime, it declares the corresponding context (`CTX-<regime>`), which raises catalogue requirements to mandatory (floor) and adds requirements that only make sense under the regime. A context never removes or lowers a Manual minimum. Levels L1–L3 measure the application's risk and are not equivalent to any regulation's risk classes.  
- **Critical Notes** → observations on interpretation, overlap or complementarity.  
- **Conclusion** → what the SbD-ToE covers in that normative framework, what remains a declared gap and what is out of scope.
- **Practical Playbook** (where applicable) → implementation roadmap for organisations with a development/AppSec discipline, guiding how to integrate normative requirements into software acquisition or development.

The Manual is centred on the application: requirements, architecture, code, dependencies, pipeline, deployment and operation of the software. AI comes in like any other topic of the Manual; there is no separate AI manual. The obligation-by-obligation answer for each regulation is in:

- [DORA — Applicable requirements](dora/requisitos-aplicaveis#cobertura)
- [NIS2 — Applicable requirements](nis2/requisitos-aplicaveis#cobertura)
- [CRA — Applicable requirements](cra/requisitos-aplicaveis#cobertura)
- [GDPR — Applicable requirements](gdpr/requisitos-aplicaveis#cobertura)
- [AI Act — Applicable requirements](ai-act/requisitos-aplicaveis#cobertura)
- [ENISA/CSA — Coverage](enisa-csa/cobertura#cobertura)

---

## Philosophy of Integrated Compliance {#filosofia-de-conformidade-integrada}

**SbD-ToE is not a standard**, but it was designed to **engage in dialogue with all standards**.  
This is because:  

- **Standards and regulations are, by definition, subset requirements**: they focus on specific dimensions (governance, risk, reporting, data protection, etc.).  
- The SbD-ToE, by contrast, prescribes **comprehensive and integrated** practices that answer many of these requirements.  
- Compliance remains the organisation's judgement. The Manual provides the technical evidence and states clearly what remains to be done and what does not fall to it, without a parallel or bureaucratic effort for each regulation.  

This view **mitigates regulatory fragmentation** and offers organisations a **unified model of practical application**, where security, risk and compliance converge.

---

## Important Note: Normative Instruments and Application Development {#nota-importante-normativos-e-desenvolvimento-aplicacional}

Many normative instruments (e.g. **DORA**, **NIS2**, **ISO 27001**) **are not specific to software development**, but cover the **comprehensive management of ICT risk** in organisations.

However, when an organisation **owns or contracts software development**, the discipline of **application security (AppSec)** becomes a **critical component** for demonstrating compliance with those normative instruments.

**Practical consequence:**  
- The normative instrument requires "ICT risk management" (broad scope)
- The organisation implements this through multiple controls (architecture, operations, contracts, etc.)
- If there is software development/acquisition, the playbooks in this chapter guide **how to integrate AppSec practices** in a **consistent and proportionate** way with the regulation

**The Manual's perimeter.** The Manual is centred on the application. The following are out of scope, with the reason recorded in each regulation's matrix: the security of the entity as a whole (corporate network and administration channels, EDR, patching of operating systems and equipment, inventory and classification of all assets), business continuity, crisis management and the entity's BIA, conformity assessment, CE marking and declarations of conformity, and the legal side of the GDPR (legal bases, formal response to the data subject and deadlines). AI is treated like any other topic of the Manual, with no separate manual.

**Example:** **DORA** is financial regulation, but if a financial entity develops software in-house, it must apply the principles of SbD-ToE to demonstrate that its **cyber-resilience posture** (DORA Art. 5) includes **development security practices**.

---

## Chapter Structure {#estrutura-do-capítulo}

This chapter is organised by **framework/normative instrument**, each in a dedicated folder with an introduction, an implementation playbook and the coverage page generated from the matrix:

### Frameworks Currently Covered {#frameworks-atualmente-cobertos}

#### **[DORA](dora/intro)** (Digital Operational Resilience Act) {#dora-digital-operational-resilience-act}
- 📂 `dora/`
  - [Framing of the regulation](dora/intro)
  - [Practical implementation playbook](dora/playbook)
  - [Convergence analysis with NIS2](dora/convergencia-dora)
  - [Applicable requirements (generated from the matrix)](dora/requisitos-aplicaveis)

#### **[NIS2](nis2/intro)** (Network and Information Security Directive) {#nis2-network-and-information-security-directive}
- 📂 `nis2/`
  - [Framing of the directive](nis2/intro)
  - [Practical implementation playbook](nis2/playbook)
  - [Convergence analysis with DORA](nis2/convergencia-dora)
  - [Applicable requirements (generated from the matrix)](nis2/requisitos-aplicaveis)

#### **[CRA](cra/intro)** (Cyber Resilience Act) {#cra-cyber-resilience-act}
- 📂 `cra/`
  - [Framing of the regulation](cra/intro)
  - [Practical implementation playbook](cra/playbook)
  - [Applicable requirements (generated from the matrix)](cra/requisitos-aplicaveis)

#### **[GDPR](gdpr/intro)** (General Data Protection Regulation) {#gdpr-general-data-protection-regulation}
- 📂 `gdpr/`
  - [Framing of the regulation](gdpr/intro)
  - [Practical implementation playbook](gdpr/playbook)
  - [Applicable requirements (generated from the matrix)](gdpr/requisitos-aplicaveis)

#### **[AI Act](ai-act/intro)** (Artificial Intelligence Regulation) {#ai-act-regulamento-de-inteligência-artificial}
- 📂 `ai-act/`
  - [Framing of the regulation](ai-act/intro)
  - [Practical implementation playbook](ai-act/playbook)
  - [Convergence analysis with the CRA](ai-act/convergencia-cra)
  - [Applicable requirements (generated from the matrix)](ai-act/requisitos-aplicaveis)

#### **[ENISA / CSA](enisa-csa/intro)** (Cybersecurity Act — European cybersecurity certification) {#enisa-csa-cloud-security-alliance-certification}
- 📂 `enisa-csa/`
  - [Framing of the certification scheme](enisa-csa/intro)
  - [Obligation-by-obligation coverage (generated from the matrix)](enisa-csa/cobertura)

### Supporting Examples and Templates {#exemplos-e-templates-de-suporte}

#### **[Example Playbook](exemplo-playbook/exemplo-toolchain-options)** {#exemplo-playbook}
- 📂 [`exemplo-playbook/`](exemplo-playbook/exemplo-toolchain-options)
  - Reusable templates and examples for implementing any framework
  - Tools, KPIs, governance, reports, policies, contracts
  - [See the full index](exemplo-playbook/exemplo-toolchain-options) for details

---

### Frameworks to Include (Roadmap) {#frameworks-a-incluir-roadmap}

The following frameworks are on the roadmap for future addition:

- **ISO 27001** → Information Security Management Standard
- **HIPAA** → Health Insurance Portability and Accountability Act
- **PCI-DSS** → Payment Card Industry Data Security Standard
- **SOC2** → Service Organization Control 2
- **FedRAMP** → Federal Risk and Authorization Management Program
- **CSA STAR** → Cloud Security Alliance Security Trust Assurance and Risk

---

### Common Structure of Each Framework {#estrutura-comum-de-cada-framework}

Each framework folder follows this consistent structure:

1. **Introduction**
   - Legal/regulatory framing
   - Scope of application
   - Main objectives

2. **Implementation Playbook**
   - Cross-check: Requirements vs. SbD-ToE
   - Implementation roadmap
   - Phases and milestones
   - Practical checklists

3. **Convergence Analyses** (where applicable)
   - Overlap between frameworks
   - *Lex specialis* principle
   - Harmonised implementation strategies

4. **Applicable requirements / Coverage** (generated from the matrix)
   - Obligation by obligation: covered, declared gap or out of scope
   - Floor and requirements added by the regulatory context, where one exists

---

## Recommended reading {#leitura-recomendada}

- This chapter should be read **in conjunction with [Chapter 00 - Theory of Everything](/sbd-toe/teory-of-everything/intro)**, which explains the overall philosophy of the manual.  
- For organisations **with software development/acquisition**, it is recommended to start with the playbooks (e.g. [DORA](dora/playbook), [NIS2](nis2/playbook)), which guide coherent implementation.
- It may also be used as a **stand-alone document**, serving as a quick reference guide for anyone seeking to verify the alignment of SbD-ToE with specific requirements.  

---
