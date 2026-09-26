---
id: formacao-iac
title: Training Module - Secure Infrastructure as Code (IaC)
sidebar_position: 8
description: Practical upskilling for technical teams that develop, review or operate IaC projects securely
tags: [formacao, iac, terraform, tfsec, checkov, pipelines, devops, validacao, requisitos]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/addon/08-exemplo2-formacao-iac.md
  source_sha256: 0b076e64935a9e38b9a5172d0ef6e12a46ad48c25f4e97bfcb9786d8fe814dc9
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: ccb77e4c26e08414c3c0ab3f07133bcb88a9ad8043f8b5c1a35e504e9a698bdc
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [capacitacao, chapter_role, cycle_iteration, framework_source_corpus, lifecycle_phase, maturity, requirement_runtime, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: a9f4d3eb48a2d12612f68734439a16a2dc6ad36704528bc148aba928f5e150d8
  translated_at: 2026-09-26T12:49:00Z
  stamped_at: 2026-09-26T18:35:57Z
  reviewed_by: null
---


# Training Module - Secure Infrastructure as Code (IaC)
This example illustrates training in a context of high infrastructure automation, where human understanding of the mechanisms and limits remains essential.

## 🎯 Objective {#-objetivo}

To equip the technical teams to:

- Understand the main security risks in IaC projects;
- Apply requirements `IAC-001` to `IAC-013` defined in Chapter 08 of the SbD-ToE;
- Integrate security validations and good practices into the infrastructure development and operation lifecycle;
- Reduce the risk of exposure, misconfiguration and drift.

---

## 📋 Prerequisites {#-pré-requisitos}

- Familiarity with IaC languages (e.g. Terraform, Bicep, YAML/K8s)
- Previous experience with CI/CD pipelines (execution, review or configuration)
- Basic knowledge of environment segregation and credential management

---

## 🧪 Session format {#-formato-da-sessão}

| Block                     | Duration | Objective                                                              |
|--------------------------|---------|-----------------------------------------------------------------------|
| Introduction               | 10 min  | Context and importance of security in IaC                            |
| IaC requirements        | 20 min  | Presentation of the normative requirements and link to real bad practices|
| Review of an insecure PR   | 20 min  | Practical exercise with detection of flaws and group discussion         |
| Integration with CI/CD     | 15 min  | Demonstration of pipelines with automatic validations (tfsec, OPA, etc.) |
| Quiz + validation         | 10 min  | Questionnaire with immediate feedback                                    |

> 🔍 This module can be adapted to hands-on workshops with real labs or simulations per stack.

---

## 📦 Required materials {#-materiais-necessários}

- Repository with real and simulated examples (Terraform, Bicep, K8s)
- Cheatsheet of tools and commands (tfsec, checkov, driftctl, opa)
- PR templates with mandatory validation sections
- Quick reference for requirements `IAC-001` to `IAC-013`
- Flow diagram of validation and exception management

---

## ✅ Completion criteria {#-critérios-de-conclusão}

- Active participation in the session or assisted review of a PR
- Passing the final quiz (minimum 80%)
- Delivery of evidence of the integration of validations into the project pipeline (e.g. PR with tfsec/checkov config)

---

## 🔁 Integration into the lifecycle {#-integração-no-ciclo-de-vida}

- Inclusion of the module in the **mandatory DevOps onboarding training**
- Technical backlog tasks: `[SEC] Validar plano Terraform com tfsec` / `[SEC] Adicionar tagging obrigatório`
- Link to the **formal exceptions process** described in the chapter
- Create a card or story such as:  
  `Como DevOps quero validar todos os PRs de IaC com tfsec e driftctl, para garantir conformidade com os requisitos de IaC.`

---

## 🔗 Cross-references in the SbD-ToE {#-referências-cruzadas-no-sbd-toe}

| Chapter                       | Relevance                                                 |
|--------------------------------|------------------------------------------------------------|
| Chapter 08 - Secure IaC       | Main source of requirements and practices (`IAC-001` to `IAC-013`) |
| Chapter 07 - Secure CI/CD     | Integration with pipelines and isolated executions             |
| Chapter 04 - Architecture      | Structural impact of configurations and reusable modules|
| Chapter 02 - Requirements       | Correspondence with the Ch. 02 requirements related to secrets, permissions, segregation |

---

## 📊 Operational good practices {#-boas-práticas-operacionais}

- Include this module as a **prior requirement for access to cloud environments** or critical pipelines
- Hold quarterly sessions with analysis of the organisation's real IaC errors
- Reinforce the use of PR Clinics focused on infrastructure
- Maintain an internal repository of secure and insecure *IaC patterns*
- Keep track of changes in tools and continuously adapt the content

---

> 📌 This module is essential for any team that works on infrastructure as code - whether in the context of provisioning, pipelines or operations. Its application reduces systemic risks and increases the organisation's maturity in managing environments and permissions.
