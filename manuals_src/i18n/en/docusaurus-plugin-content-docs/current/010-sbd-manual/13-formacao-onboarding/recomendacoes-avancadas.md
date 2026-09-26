---
id: recomendacoes-avancadas
title: Advanced Recommendations - Training and Secure Onboarding
description: Recommendations for organisations with greater maturity in continuous training, automation and behavioural security.
tags: [formacao, maturidade, lms, cicd, feedback, gamificacao, terceiros]
sidebar_position: 30
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/recomendacoes-avancadas.md
  source_sha256: 942db59e021a0aa7b6f78c2eb852cbb635cea1cb3276a3882f479e5f41cc32e7
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 36b2160a76cbde0a3cec0ed06d5c98efee0f500f350fc46c3fbac56b1b691ac6
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: d743dfcba33f930c34618b93d1eaaa34f697328d45aaf3bb657c33b8b3c59c9a
  glossary_keys: [chapter_role, cycle_iteration, lifecycle_phase, maturity, practitioner_manual, sbdtoe_sbd, trilho_formativo, validation_evaluation]
  glossary_sha256: 99143e7907217564a528bb86a6d04e294a023daf08c1bf48eb2a277f29a4bdbd
  translated_at: 2026-09-26T11:44:31Z
  reviewed_by: null
---


# Advanced Recommendations - Training and Secure Onboarding

This document presents advanced recommendations that **complement the minimum practices described in Chapter 13**, applicable to organisations with greater security maturity, a consolidated DevSecOps culture and a focus on the **scale, automation and continuous improvement** of technical security training.

> 🔍 These practices make it possible to reach the high maturity levels defined by **SAMM EDU.3**, **SSDF PO.4** and **DSOMM Training & Awareness L4**.

---

## 🚀 Recommendations for organisations with greater maturity {#-recomendações-para-organizações-com-maior-maturidade}

### 🧠 1. Integration with an LMS platform {#-1-integração-com-plataforma-lms}

- Automate **personalised training tracks** per technical profile (Dev, QA, DevOps, AppSec).
- Integrate quizzes, videos, practical tests and automated recording per chapter (e.g. Ch. 05 - SBOM).
- Generate **real-time dashboards per team, project or functional domain**.
- Version the content per SbD-ToE chapter and associate completion metrics.

### 🤖 2. Automatic validation via CI/CD {#-2-validação-automática-via-cicd}

- Automatically validate that **training and validation have been completed** before authorising:
  - Access to repositories
  - Execution of pipelines
  - Submission of PRs
- Block critical operations if the user's status is "not enabled".
- Integrate with identity sources (e.g. GitHub, GitLab, Azure AD) to reflect onboarding status.

### 🔄 3. Continuous and adaptive feedback {#-3-feedback-contínuo-e-adaptativo}

- Use **adaptive quizzes with reinforcement in weak areas**, based on profile and history.
- Correlate **real errors in PRs or incidents** with automatic reinforcement (e.g. microlearning).
- Apply **spaced repetition** techniques, effectiveness metrics and optional gamification.

### 🔐 4. Assisted technical onboarding {#-4-onboarding-técnico-assistido}

- Create **secure sandbox environments** to validate knowledge (e.g. PR review, fault detection).
- Include **real cases and internal lessons learned** in the training paths.
- Monitor time, performance and drop-off points during onboarding.

### 🌍 5. Extension to suppliers and partners {#-5-expansão-para-fornecedores-e-parceiros}

- Make **public or NDA-covered training tracks** available to strategic partners.
- Require **training compliance** with completion metrics before technical permissions.
- Integrate training requirements into **supplier qualification** processes.

---

## 🧭 Integration with maturity frameworks {#-integração-com-frameworks-de-maturidade}

### 📘 OWASP DSOMM - `Training & Awareness` {#-owasp-dsomm---training--awareness}

| Level | Expected practice in DSOMM                                                                             | Covered by the recommendations |
|-------|--------------------------------------------------------------------------------------------------------|------------------------------|
| L1    | Basic initial training (e.g. OWASP Top 10)                                                             | ✅                            |
| L2    | Continuous training per technical profile                                                                 | ✅                            |
| L3    | Integration with technical processes (CI/CD, permissions, deploys)                                         | ✅                            |
| L4    | Adaptive training, use of real data, effectiveness metrics, continuous feedback                       | ✅                            |

> ✅ The recommendations described here make it possible to reach **DSOMM level 4** in the `Training & Awareness` domain.

### 📘 SAMM v2.1 - `Education & Guidance` {#-samm-v21---education--guidance}

- **EDU.3 - Automated, role-specific training**: The tracks per profile, gating via CI/CD and dashboards fully support this level.
- The integration with technical onboarding, content per chapter and metrics are examples of **continuous application of EDU.3**.

### 📘 NIST SSDF v1.1 - `PO.4` {#-nist-ssdf-v11---po4}

- **PO.4.1 / PO.4.2**: Establish that training must be updated on the basis of incidents and centred on roles.
- **PO.4.3 / PO.4.4**: Support continuous measurement and review - as recommended with the dashboards and KPIs.

---

## 🧩 Progressive adoption {#-adoção-progressiva}

| Maturity Level | Applicable recommendations                                                             |
|---------------------|----------------------------------------------------------------------------------------|
| Initial             | Manual training, minimum validation, checklists in onboarding                          |
| Intermediate          | Defined tracks, centralised quizzes, basic indicators                         |
| High             | LMS integration, continuous feedback, validation via CI/CD, assisted onboarding, extension to third parties |

---

## ✅ Conclusion {#-conclusão}

These advanced practices make training:

- **More effective, continuous and measurable**
- **Integrated into the lifecycle and into technical permissions**
- **Based on evidence, feedback and personalisation**

> 📈 True security maturity is reflected in the ability to **train, retain and upskill teams continuously and in a way adapted to risk and role.**
