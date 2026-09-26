---
id: quiz-onboarding
title: Quiz Template for Onboarding Validation
description: Example of a technical quiz used for knowledge validation in the onboarding process.
tags: [onboarding, quiz, validacao, conhecimento, rastreabilidade]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/addon/11-template-quiz-onboarding.md
  source_sha256: 1af5b766197dc70a18c7bd58ab42b13e89a71356639f40f29b458c4cfcae5361
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 1f64f437aab22ceda69dfeeac72abc801ecb80282275863adb337b42089e9318
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, framework_source_corpus, practitioner_manual, risk_level, sbdtoe_sbd, traceability, trilho_formativo, validation_evaluation]
  glossary_sha256: 364cafcf4bcc67fc2319f72a0aa809f33a59b288d819979b751a3d50571448a8
  translated_at: 2026-09-26T11:44:22Z
  stamped_at: 2026-09-26T18:35:59Z
  reviewed_by: null
---


# Quiz Template - Technical Onboarding

This document presents a reusable example of a **technical quiz** for knowledge validation in the context of **initial training** (onboarding) in security.  
It may be adapted by profile, risk level or chapter of the SbD-ToE Manual, and is especially useful in **training tracks for developers**.

---

## 🎯 Objective {#-objetivo}

- Objective validation of the assimilation of essential security content
- Provision of an auditable record of the completion of technical onboarding
- Reinforcement of key concepts through realistic examples

---

## 📦 Context of use {#-contexto-de-uso}

| Situation                         | Recommended application                                 |
|----------------------------------|--------------------------------------------------------|
| Onboarding of a new Dev           | Use after completion of the initial training track        |
| Change of stack or project      | Validation of the knowledge specific to the new context     |
| Reinforcement of continuous training     | Integrate as an annual revalidation (e.g. access review)|
| Checkpoint for technical access   | Associate with the unlocking of permissions (e.g. Git, CI/CD) |

> It may be used in an LMS, a Google Form, a GitHub Issue with markdown, or integrated into the onboarding flow via pipelines/scripts.

---

## 🧪 Example quiz: Dev on an L2 application {#-exemplo-de-quiz-dev-em-aplicação-l2}

1. **Which of these practices is mandatory when merging a PR?**  
   - a) Resolve all conflicts automatically  
   - b) Validate the security requirements applicable to the application  
   - c) Run only `npm install`  
   - d) Ignore unused dependencies  
   ✅ **Correct answer:** b)

2. **What is the risk of leaving a secret in the source code?**  
   - a) None, if it is a temporary token  
   - b) It may lead to unauthorised access and compromise the environment  
   - c) It only makes the build slower  
   - d) It is acceptable if it is on a private branch  
   ✅ **Correct answer:** b)

3. **Which of these tools is used to check for insecure dependencies?**  
   - a) ESLint  
   - b) Git  
   - c) SCA (e.g. Xygeni, OWASP Dependency-Check)  
   - d) Jenkins  
   ✅ **Correct answer:** c)

---

## 📌 Good practices for use {#-boas-práticas-de-utilização}

- Adapt the questions to the content actually taught in the track
- Include immediate feedback with an explanation of the answers
- Ensure a record of completion (minimum score, evidence of submission)
- Reuse questions in clinics, internal quizzes or training games

---

## 🔗 Useful links {#-ligações-úteis}

| Document                     | Relevance                                      |
|-------------------------------|-------------------------------------------------|
| `03-checklist-onboarding.md`  | Checklist in which this quiz may be referenced |
| `trilho-formativo.md`         | Indicates when and for whom to apply the quiz       |
| `90-catalogo-formativo.md`    | Lists the topics that must be covered         |

---

> 🎯 This template may be duplicated and adapted by chapter, role or criticality - ensuring traceability and alignment with the SbD-ToE Manual.
