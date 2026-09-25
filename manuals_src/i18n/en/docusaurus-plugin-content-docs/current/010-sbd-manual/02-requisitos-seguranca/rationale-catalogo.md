---
id: rationale-catalogo
title: ℹ️ Rationale
description: Rationale and logical structure of the requirements themes used in the catalogue
tags: [estrutura, requisitos, temas, asvs, rastreabilidade, ia]
sidebar_position: 2
translation:
  source_locale: pt
  source_path: 010-sbd-manual/02-requisitos-seguranca/rationale-catalogo.md
  source_sha256: f8a134c4887e9cf6dcb74efc490aa6dc59894d48bf2dea6293a263d145f7f71e
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: adc04f4c88f203264771b140f111b0e9a688d77fd93cd79059b9f4784cdb3e0e
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [chapter_role, cycle_iteration, framework_source_corpus, lifecycle_phase, maturity, normative_empirical, practitioner_manual, risk_level, sbdtoe_sbd, traceability, transversal, validation_evaluation, verification_taxonomy]
  glossary_sha256: 2cb68c8b8c8cad959638c99821d5a7ba8526a15b0a41fa902aa611ee885923f8
  translated_at: 2026-09-25T20:20:20Z
  reviewed_by: null
---

## Rationale for the Structure of the Application Requirements {#rationale-para-a-estrutura-dos-requisitos-aplicacionais}

The definition of the application requirements in this manual follows a structure of **20 main themes**, created with the aim of offering a **comprehensive, practical and risk-proportional** approach, suited to applying the principles of *Security by Design* throughout the entire software lifecycle.

This structure seeks to balance **normative rigour**, **practical applicability** and **technological neutrality**, allowing its consistent use in traditional, cloud-native, highly automated or automatic-generation-assisted development contexts.

---

## 🧩 Origin and Foundation {#-origem-e-fundamento}

The structure adopted is based primarily on the **OWASP ASVS v5.0 (Application Security Verification Standard)** framework, recognised as a global reference for the definition and verification of application security requirements.

However, the version presented here:

- **Incorporates and cross-references requirements** inspired by other maturity and security frameworks, namely:
  - **NIST SP 800-53 Rev. 5**
  - **OWASP SAMM v2.1**
  - **BSIMM13** (by inference from public sources)
  - **SLSA v1.0**
  - **CIS Controls v8**
- **Groups and adapts ASVS domains** to better reflect the way systems are actually designed, developed, integrated and operated in modern environments.

In this way, the themes cover not only classic functional and technical security concerns (e.g. authentication, encryption, access control), but also domains related to **development practices**, **automation**, **auditing**, **supply chain** and **continuous integration**.

Notwithstanding this consolidation - which can and should be adapted to each organisation - the manual includes in other chapters **requirements specific to each technical domain**, such as Secure Architecture, CI/CD, Supply Chain, Infrastructure as Code or Containers.

This chapter deliberately addresses the requirements that can be classified as **cross-cutting application security requirements**, applicable to a concrete application and proportional to its risk level.

---

## 🧠 Motivations for Adjustments and Consolidation {#-motivações-para-ajustes-e-consolidação}

The structure of the 20 themes was developed on the basis of the following fundamental motivations:

- **Functional clarity**  
  The themes are named so that any technical team can quickly understand their scope and application.

- **Proportionality to risk**  
  All requirements can be classified by application risk level (L1, L2, L3), allowing a graduated and justifiable application.

- **Alignment with real engineering practices**  
  The groupings reflect the way organisations structure teams, processes, pipelines and technical responsibilities.

- **Coverage of gaps identified in base frameworks**  
  Domains such as *Threat Modelling*, *SBOM/SCA*, *Secure CI/CD*, *Security Testing* and *Governance* are traditionally little or poorly covered in exclusively application-oriented frameworks such as ASVS, yet they are critical in practice - which is why they appear as autonomous themes.

---

## 🤖 Note on Automation and the Use of AI in Development {#-nota-sobre-automação-e-uso-de-ia-no-desenvolvimento}

The theme-based structure **does not assume a manual development model**, nor does it ignore the growing adoption of **automation, advanced pipelines or AI-based assistants** in the software engineering process.

However, this pervasiveness **does not justify creating new application requirements themes**, since:

- automation **does not change the nature of application risks**;
- security requirements remain valid regardless of how the code is produced;
- the impact of automation manifests itself above all at the level of **governance**, **validation**, **traceability** and **evidence**.

For this reason, the manual opts to:
- keep the T01–T20 catalogue **stable and technologically neutral**;
- explicitly address the use of automation and AI through **cross-cutting prescriptions** and **application rules**, documented in annexes and in the lifecycle (e.g. governance of the use of automation, CI/CD gates, mandatory human review).

This decision preserves the longevity and coherence of the model, avoiding dependence on specific technologies.

---

## 🧷 Link to the Chapters of the Manual {#-ligação-aos-capítulos-do-manual}

The 20 requirements themes function as a **common basis** for the practical application of the following chapters of the manual, making it possible to:

- **Anchor architecture and development decisions in concrete and verifiable security requirements**;
- **Define the minimum security levels expected by application type**, on the basis of its risk classification;
- **Reinforce traceability between requirements, practices, tests and quality control**;
- **Support the threat modelling, onboarding, continuous verification and operational checklist models** presented in the following chapters.

Each theme can be directly associated with one or more technical chapters of the manual (for example, *Dependency Management* with Chapter 5, *Secure CI/CD* with Chapter 7, etc.).

> The theme-based structure is also reused in the **practical checklists**, in the **traceability matrices** and in the **coverage of normative frameworks** that accompany this manual.

---
