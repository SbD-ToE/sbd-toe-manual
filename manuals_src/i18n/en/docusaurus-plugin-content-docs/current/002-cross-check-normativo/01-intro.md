---
id: intro
title: Introduction - Normative cross-check
description: Framing of the normative analysis chapter, which shows how SbD-ToE intersects with different normative instruments and regulations
tags: [cross-check, normativos, compliance, dora, nis2, ai-act, cra, hipaa, iso27001, pci-dss, gdpr, soc2]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/01-intro.md
  source_sha256: 27cc3ed9424ac44ef6fdf8e2c14f3a6f82030d869da014abf089719fedc50cb7
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 563123751d748f220fa1a9162b2f805e86cb886dfe64afed1b87f6e7cdcf150b
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: da8c4621ee3f200794cd49e34ddc29239ba89f55effb1e5e578d388e50580b8d
  glossary_keys: [chapter_role, cycle_iteration, discipline, dnt_fedramp_name, dnt_soc2_name, dora_financial_entity, dora_ict_risk, esquema_regime, framework_source_corpus, instrument, lifecycle_phase, maturity, normative_empirical, papel_suporte, practitioner_manual, prescriptive, sbdtoe_sbd, schema]
  glossary_sha256: 559597941762b85a55615caeb9632acdf8633166bcf0018a4b12186338c9a9ca
  translated_at: 2026-09-26T17:57:24Z
  reviewed_by: null
---



# Introduction - Normative cross-check

Software security does not happen in a technical vacuum.  
Organisations in different sectors are subject to **regulations, standards and frameworks** that set explicit requirements to ensure adequate protection of systems, data and operations.  
In this context, **Security by Design - Theory of Everything (SbD-ToE)** is not only a prescriptive manual of good practice: it is also an **instrument of normative convergence**, making it possible to align secure development and operation practices with multiple external demands.

**Chapter 002 - Normative cross-check** plays precisely this role:  
- Demonstrate, in a clear and verifiable way, **how SbD-ToE responds to regulatory and normative requirements**.  
- Identify where the model ensures **compliance "by construction"**, and where there are **gaps** that require complementary legal, organisational or contractual processes.  
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
- **Compliance is not an isolated objective**, but rather a **positive side effect** of applying secure practices across the whole lifecycle.  
- **Each knowledge area** (requirements, architecture, CI/CD, containers, governance, etc.) contributes to the model **building “compliance by design”**.

---

## Objectives of this chapter {#objetivos-deste-capítulo}

1. **Show the correspondence** between SbD-ToE practices and the requirements of international and European normative instruments.  
2. **Highlight the areas of full coverage**, where adopting the model leads to almost immediate compliance.  
3. **Reveal gaps and grey areas**, helping organisations understand where they need additional measures (legal, procedural or technical).  
4. **Provide a comparative repository** that can be reused in audits, certifications or compliance reports.
5. **Offer implementation playbooks** for organisations that contract or develop software, ensuring that acquisition/development is consistent with specific normative requirements.

---

## Methodology adopted {#metodologia-adotada}

The analysis follows a systematic structure, common to all normative instruments:  

- **Framing** → brief description of the normative instrument, its scope and objectives.  
- **Cross-Check Table** → main requirements of the normative instrument vs. SbD-ToE practices:  
  - If there is coverage, indicate the **chapter(s)** where it is addressed.  
  - If coverage is partial, detail the limitations.  
  - If there is no coverage, state the gap explicitly.  
- **Critical Notes** → observations on interpretation, overlap or complementarity.  
- **Conclusion** → the extent to which SbD-ToE ensures alignment with that normative instrument.
- **Practical Playbook** (where applicable) → implementation roadmap for organisations with a development/AppSec discipline, guiding how to integrate normative requirements into software acquisition or development.

---

## Philosophy of Integrated Compliance {#filosofia-de-conformidade-integrada}

**SbD-ToE is not a standard**, but it was designed to **engage in dialogue with all standards**.  
This is because:  

- **Standards and regulations are, by definition, subset requirements**: they focus on specific dimensions (governance, risk, reporting, data protection, etc.).  
- SbD-ToE, by contrast, prescribes **comprehensive and integrated** practices that **by construction already meet many of those requirements**.  
- The SbD-ToE approach is **“compliance built-in”**: compliance is the natural consequence of the practical application of the measures, not a parallel or bureaucratic effort.  

This view **mitigates regulatory fragmentation** and offers organisations a **unified model of practical application**, where security, risk and compliance converge.

---

## Important Note: Normative Instruments and Application Development {#nota-importante-normativos-e-desenvolvimento-aplicacional}

Many normative instruments (e.g. **DORA**, **NIS2**, **ISO 27001**) **are not specific to software development**, but cover the **comprehensive management of ICT risk** in organisations.

However, when an organisation **owns or contracts software development**, the discipline of **application security (AppSec)** becomes a **critical component** for demonstrating compliance with those normative instruments.

**Practical consequence:**  
- The normative instrument requires "ICT risk management" (broad scope)
- The organisation implements this through multiple controls (architecture, operations, contracts, etc.)
- If there is software development/acquisition, the playbooks in this chapter guide **how to integrate AppSec practices** in a **consistent and proportionate** way with the regulation

**Example:** **DORA** is financial regulation, but if a financial entity develops software in-house, it must apply the principles of SbD-ToE to demonstrate that its **cyber-resilience posture** (DORA Art. 5) includes **development security practices**.

---

## Chapter Structure {#estrutura-do-capítulo}

This chapter is organised by **framework/normative instrument**, each in a dedicated folder with an introduction and an implementation playbook:

### Frameworks Currently Covered {#frameworks-atualmente-cobertos}

#### **[DORA](dora/intro)** (Digital Operational Resilience Act) {#dora-digital-operational-resilience-act}
- 📂 `dora/`
  - [Framing of the regulation](dora/intro)
  - [Practical implementation playbook](dora/playbook)
  - [Convergence analysis with NIS2](dora/convergencia-dora)

#### **[NIS2](nis2/intro)** (Network and Information Security Directive) {#nis2-network-and-information-security-directive}
- 📂 `nis2/`
  - [Framing of the directive](nis2/intro)
  - [Practical implementation playbook](nis2/playbook)
  - [Convergence analysis with DORA](nis2/convergencia-dora)

#### **[CRA](cra/intro)** (Cyber Resilience Act) {#cra-cyber-resilience-act}
- 📂 `cra/`
  - [Framing of the regulation](cra/intro)
  - [Practical implementation playbook](cra/playbook)

#### **[GDPR](gdpr/intro)** (General Data Protection Regulation) {#gdpr-general-data-protection-regulation}
- 📂 `gdpr/`
  - [Framing of the regulation](gdpr/intro)
  - [Practical implementation playbook](gdpr/playbook)

#### **[AI Act](ai-act/intro)** (Artificial Intelligence Regulation) {#ai-act-regulamento-de-inteligência-artificial}
- 📂 `ai-act/`
  - [Framing of the regulation](ai-act/intro)
  - [Practical implementation playbook](ai-act/playbook)
  - [Convergence analysis with the CRA](ai-act/convergencia-cra)

#### **[ENISA CSA](enisa-csa/intro)** (Cloud Security Alliance Certification) {#enisa-csa-cloud-security-alliance-certification}
- 📂 `enisa-csa/`
  - [Framing of the certification scheme](enisa-csa/intro)

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

---

## Recommended reading {#leitura-recomendada}

- This chapter should be read **in conjunction with [Chapter 00 - Theory of Everything](/sbd-toe/teory-of-everything/intro)**, which explains the overall philosophy of the manual.  
- For organisations **with software development/acquisition**, it is recommended to start with the playbooks (e.g. [DORA](dora/playbook), [NIS2](nis2/playbook)), which guide coherent implementation.
- It may also be used as a **stand-alone document**, serving as a quick reference guide for anyone seeking to verify the alignment of SbD-ToE with specific requirements.  

---
