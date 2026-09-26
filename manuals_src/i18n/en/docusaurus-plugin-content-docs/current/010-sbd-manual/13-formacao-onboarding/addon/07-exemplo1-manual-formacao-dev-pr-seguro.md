---
id: exemplo-manual-dev-pr
title: Example Training Manual - Secure Pull Request
description: Concrete example of a training manual for developers on secure practices in PRs.
tags: [exemplo, formacao, pull request, dev, aplicacao]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/addon/07-exemplo1-manual-formacao-dev-pr-seguro.md
  source_sha256: 0fa08a095ecc631da232a0fe31ca7388531adb9c60d777e2d2ac4708b23b6930
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: da1f9248b9bb0e6144ea516000e1d327feba9e5fb850a40faaa44cae06918c72
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: d743dfcba33f930c34618b93d1eaaa34f697328d45aaf3bb657c33b8b3c59c9a
  glossary_keys: [chapter_role, cycle_iteration, maturity, practitioner_manual, sbdtoe_sbd, trilho_formativo, validation_evaluation]
  glossary_sha256: 73b66bd4477b469540030383bdb7cf336f28fbf542172b86038ff82ea5bf69b1
  translated_at: 2026-09-26T11:44:20Z
  reviewed_by: null
---


# Training Module - Secure Pull Request
This example assumes a development environment strongly supported by automated tools, while keeping final responsibility for decisions and practices with the teams involved.

## 🎯 Objective {#-objetivo}

To equip developers to:

- Write Pull Requests with minimum security criteria applied
- Identify bad practices in code submitted by colleagues
- Justify security decisions directly in the PR

---

## 📋 Prerequisites {#-pré-requisitos}

- Basic experience with Git and the Pull Request flow
- Previous participation in at least 1 active sprint
- Knowledge of the internal code standards (naming, logging, validations)

---

## 🧪 Session format {#-formato-da-sessão}

| Block              | Duration | Objective                                                                 |
|-------------------|---------|--------------------------------------------------------------------------|
| Introduction         | 5 min   | Frame the importance of the secure PR for the development cycle    |
| Positive example   | 10 min  | Review a real or simulated PR with good practices                          |
| Example with flaws | 15 min  | Identify bad practices, omissions and validation failures                 |
| Guided review     | 10 min  | Apply the checklist and write improvement comments                      |
| Quiz or validation  | 10 min  | 5 questions or a quick consolidation challenge                            |

> 💡 The session may be synchronous (training, group peer review) or asynchronous (exercise done at one's own pace with later review).

---

## 📦 Required materials {#-materiais-necessários}

- Two real or simulated PRs (one exemplary, one with flaws)
- Internal secure review guide (e.g. `checklist-pr-seguro.md`)
- Quiz platform (Kahoot, LMS, Markdown with manual validation)
- Internal channel for sharing and discussion (e.g. Confluence, GitHub Discussions)

---

## ✅ Completion criteria {#-critérios-de-conclusão}

- Active participation in the session or delivery of the exercise
- Passing the quiz (minimum 80%)
- Submission of a real PR with explicit security justifications (e.g. input validation, logging, permission control)

---

## 🔗 Cross-references in the SbD-ToE {#-referências-cruzadas-no-sbd-toe}

| Chapter                    | Relevance                                   |
|-----------------------------|----------------------------------------------|
| Chapter 6 - Secure Development | Direct application of requirements EX-REQ-114, EX-REQ-115 and EX-REQ-118 |
| Chapter 2 - Security Requirements | Integration with user stories that carry security criteria     |
| Chapter 13 - Training and Onboarding | May be part of the training track for the Developer profile         |

*Illustrative identifiers (`EX-…`); they do not correspond to the Ch. 02 Requirements Catalogue.*

---

## 🧭 Operational recommendations {#-recomendações-operacionais}

- Repeat this session fortnightly with new examples
- Share the “PR of the week” internally as an educational model
- Create a repository of exemplary PRs (good and bad) for consultation and discussion
- Link the module to permissions: e.g. devs may only approve after completing this module

---

> ✅ Consolidated learning about secure code review significantly reduces the introduction of vulnerabilities and accelerates the maturity of the technical teams.
