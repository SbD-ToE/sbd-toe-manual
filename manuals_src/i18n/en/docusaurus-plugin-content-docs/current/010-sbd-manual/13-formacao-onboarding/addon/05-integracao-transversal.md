---
id: integracao-transversal
title: Integration of Training with the Technical Chapters
description: Strategies for linking continuous training to the other chapters of the SbD-ToE.
tags: [formacao, integracao, capitulos, cultura, aprendizagem continua]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/addon/05-integracao-transversal.md
  source_sha256: 8849e7724bbe884fb54c71d0110d7ea1fff59037451ada7d9b72b6adb9a4e82c
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: d6b74d7c7752de9b1d3c5c4e8e8f029a0cf1139c08092148eaac02087d90a69f
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [capacitacao, chapter_role, cycle_iteration, framework_source_corpus, lifecycle_phase, mapping, practitioner_manual, sbdtoe_sbd, transversal, validation_evaluation]
  glossary_sha256: bac0543c715418998a7f6db7b68d7e9daa67fe09d197a1e71b935beb2053710f
  translated_at: 2026-09-26T11:44:18Z
  stamped_at: 2026-09-26T18:35:54Z
  reviewed_by: null
---


# Cross-cutting Integration with the Technical Chapters

## 🌟 Objective {#-objetivo}

To describe how **continuous and applied training** can be integrated into the practical activities of each technical chapter of the SbD-ToE manual.  
The objective is to guarantee that learning **is not parallel to real execution**, but rather incorporated into the rituals, decisions and processes of the development cycle.

> Training becomes sustainable when it is **active, rotating, practical and visible**.

> The integration of training with other domains of the SbD-ToE does not presuppose delegating responsibility to automated mechanisms, but rather upskilling for their correct and conscious use.

---

## 🧬 Principles of cross-cutting learning {#-princípios-da-aprendizagem-transversal}

- Every security practice must be **teachable and replicable**
- Knowledge must circulate through **rotation of roles and leadership**
- Learning must be **linked to real rituals** (e.g. sprint, release, incident)
- Retention must be measured on the basis of **practical application**

---

## 📘 Examples of integration by chapter {#-exemplos-de-integração-por-capítulo}

### 1. Risk Management {#1-gestão-de-risco}

- **Periodic workshops** with the teams on classification and impact
- Sharing sessions between teams on risk decisions (e.g. exceptions, rationale)
- **Practical training** with risk mapping exercises per application

---

### 2. Security Requirements {#2-requisitos-de-segurança}

- Labs with examples of badly written user stories
- Monthly cross-review of requirements between teams
- Practical session: write and review 3 real requirements

---

### 3. Threat Modelling {#3-threat-modeling}

- **Rotation of leadership** among devs, QA and Champions
- Practical sessions based on real features
- Review of old models after bugs or incidents

---

### 4. Secure Architecture {#4-arquitetura-segura}

- Collective review of architecture decisions (monthly or per epic)
- Comparative workshops between approaches (e.g. API vs events)
- Repository of "before/after" architectures with annotations

---

### 5. Dependency Control {#5-controlo-de-dependências}

- Labs with real scenarios of vulnerable dependencies
- **PR Clinics** focused on SBOM, SCA, lockfiles and pinning
- Rotation of responsibility for triage and update decisions

---

### 6. Secure Development {#6-desenvolvimento-seguro}

- Public and educational PR reviews
- Peer sessions on recurring anti-patterns
- Use of historical PRs as the basis for training and discussion

---

### 7. Secure CI/CD {#7-cicd-seguro}

- Simulations of a compromised pipeline
- Rotation of ownership of critical stages (e.g. secrets, deploy)
- Workshops to build stages with security validators

---

### 8. Secure IaC {#8-iac-seguro}

- Labs with real Terraform code and tools such as Checkov or TFSec
- Collaborative refactors of insecure IaC
- Rotation in the review of infrastructure changes

---

### 9. *containers* and Images {#9-containers-e-imagens}

- Hardening workshops on real Dockerfiles
- Rotating vulnerability analysis with tools such as Trivy
- Practical demonstrations of security improvements on real images

---

### 10. Security Testing {#10-testes-de-segurança}

- Gamified activities with fuzzing and API exploration
- Collective review of SAST/DAST coverage
- Rotating participation in scanner tuning

---

### 11. Secure Deployment {#11-deploy-seguro}

- Rollout simulations with induced failures (e.g. wrong feature flag)
- Shadowing between teams during critical deploys
- Workshops on validation of configurations in production

---

### 12. Monitoring and Operations {#12-monitorização}

- Analysis of real alerts and false positives
- Mini war rooms with detections via logs or dashboards
- Rotating analyses and sharing of lessons learnt

---

### 13. Training and Onboarding {#13-formação-e-onboarding}

- Recurring use of PR Clinics, CTFs, shadowing between peers
- Champions as facilitators of practical integration
- Co-learning in sprint planning or technical onboarding

---

### 14. Governance and Contracting {#14-governança-e-contratação}

- Training sessions for contractors and suppliers
- Review of contractual clauses based on past incidents
- Case studies of contractual failures as part of internal training

---

## ✅ Good practices {#-boas-práticas}

- Plan **1 learning action per sprint or release**
- Promote **rotation and co-leadership** between roles
- Use **lightweight and reusable materials** (e.g. 1 slide, draw.io file, annotated PR)
- Link training to **real events** (bugs, incidents, releases)
- Record actions in the **backlog or internal repository**

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                         | Relevance                                         |
|-----------------------------------|----------------------------------------------------|
| `01-catalogo-formativo.md`        | Basis of the content by chapter and role           |
| `04-tecnicas-formativas.md`       | Practical techniques for cross-cutting application    |
| `03-programa-champions.md`        | Champions as local facilitators                |
| `15-aplicacao-lifecycle.md`       | Practical application in the development lifecycle |
| `90-indicadores-metricas.md`      | Measurement of the effectiveness of integrated training actions |

---

> 📚 Continuous training **is not parallel to the work - it is part of work done well**.  
>  
> The SbD-ToE manual works as a **structured source of living, practical and adaptable training**, covering the whole development cycle.
