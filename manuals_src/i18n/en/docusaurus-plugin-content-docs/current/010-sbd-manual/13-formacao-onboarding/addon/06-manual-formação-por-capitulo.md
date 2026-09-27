---
id: manual-formacao-capitulos
title: SbD-ToE Training Manual by Chapter
description: Technical guide to continuous training with a direct link to each chapter of the manual.
tags: [formacao, manual, por capitulo, sbdtoe, referencia cruzada]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/addon/06-manual-formação-por-capitulo.md
  source_sha256: 714543f19a008770d4071e73ad3e6e6deb4241d156fcbbd827e6c8921edaf846
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: f4499779008eaa88e9b12c457368cd8f59be2253cf3eea9cee4726c3665b7468
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, mapping, maturity, practitioner_manual, risk_level, sbdtoe_sbd, traceability, trilho_formativo, validation_evaluation]
  glossary_sha256: bf4c48591608eff3589229e47913654a7df6688238b8fdc48ef7ed77805984be
  translated_at: 2026-09-26T11:44:19Z
  stamped_at: 2026-09-26T18:35:55Z
  reviewed_by: null
---


# Training Manual by Profile

## 🌟 Objective {#-objetivo}

To organise the training content suggested by the SbD-ToE manual by **technical functional profile**.  
This document serves as the basis for:

- Building **practical tracks by role**
- **Structured technical onboarding**
- Plans for **knowledge retention and rotation**

> 📌 Aligned with Chapter 01 - Risk Management, proportional application by risk level must modulate the depth of the content.

---

## 🧬 Suggested content by role {#-conteúdos-sugeridos-por-função}

### 👤 Dev (Developers) {#-dev-desenvolvedores}

| Topic                                    | Recommended format                   |
|-------------------------------------------|----------------------------------------|
| Secure coding                             | Labs with real flaws (e.g. Juice Shop) |
| Secure Pull Requests                     | Templates + fortnightly Code Clinics    |
| Threat Modelling per feature               | Peer-led sessions                       |
| Dependency management                    | Labs with lockfiles, SCA, SBOM          |
| Pipelines with scanners                    | Integration workshop                  |
| Token control                        | Abuse simulation + scope review  |
| Secure use of Docker images              | Practical hardening                      |

---

### 👤 QA (Testers / Quality Assurance) {#-qa-testers--quality-assurance}

| Topic                                    | Recommended format                   |
|-------------------------------------------|----------------------------------------|
| Acceptance criteria that include security      | Cross-review + real examples       |
| Security testing (SAST, DAST, fuzzing) | Guided labs + simulation             |
| Participation in Threat Modelling           | Sessions per epic                      |
| Validation of requirements                   | Checklist + functional labs            |
| Analysis of alerts and false positives     | War Room + detection tuning           |
| Review of bugs with a security cause    | Internal case study                 |

---

### 👤 PO (Product Owners) {#-po-product-owners}

| Topic                                    | Recommended format                   |
|-------------------------------------------|----------------------------------------|
| Risk classification                    | Workshop + guided exercise            |
| Prioritisation of security requirements    | Practical session + historical examples   |
| Management of justified exceptions           | Rotating review + impact analysis  |
| Legal implications (NIS2, DORA)           | Executive training                     |
| Storytelling of real failures              | Internal repository + sharing in the retro|

---

### 👤 DevOps / Platform Engineering {#-devops--engenharia-de-plataforma}

| Topic                                    | Recommended format                   |
|-------------------------------------------|----------------------------------------|
| Security in CI/CD pipelines             | Workshop on stages with scanners         |
| Secrets management                        | Lab with Vault and scopes                |
| Image hardening                      | PR review + analysis with Trivy          |
| IaC scanners and validation               | Hands-on with Checkov/TFSec             |
| Deploy with rollback and feature flags       | Rollout simulation                   |
| Alerts and tuning                          | War Room + operational dashboards     |

---

### 👤 AppSec (Application Security) {#-appsec-segurança-aplicacional}

| Topic                                    | Recommended format                   |
|-------------------------------------------|----------------------------------------|
| Facilitation of Threat Modelling            | Training + real sessions               |
| Creation of training tracks             | Alignment with Ch. 13 and Ch. 1       |
| Analysis of dependencies and vulnerabilities| Practical cases with SBOM + SCA          |
| PR review + pairing                  | Regular sessions with the teams          |
| Running CTFs, quizzes, war rooms      | Plan of rotating activities          |
| Metrics governance                    | Dashboard + follow-up                  |

---

### 👤 Management (Team Leads, Executives, Organisational Security) {#-gestão-team-leads-executivos-segurança-organizacional}

| Topic                                    | Recommended format                   |
|-------------------------------------------|----------------------------------------|
| Training governance and traceability  | Reports + track audits      |
| Contractual requirements (third parties)        | Legal sessions + standard clauses   |
| Maturity metrics                    | Analysis of security/training KPIs  |
| Promotion of Champions                     | Internal visibility plan          |
| Participation in post-mortems              | Corrective actions with cultural reinforcement  |

---

## ✅ Good practices {#-boas-práticas}

- Define **tracks by profile + risk (L1–L3)** based on this mapping
- Include actions in the **backlog, LMS or onboarding plans**
- Measure **retention and effectiveness** with quizzes, labs, shadowing or real PRs
- Involve **Champions** in the curation and facilitation of continuous training

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                          | Direct relation                        |
|------------------------------------|----------------------------------------|
| `02-trilho-formativo.md`           | Formal matrix by profile and risk       |
| `01-catalogo-formativo.md`         | Mapping by chapter and format      |
| `03-programa-champions.md`         | Multipliers in dissemination        |
| `90-indicadores-metricas.md`       | KPIs by profile and by content         |

---

> 🎯 Training by profile is the practical basis of the proportional application of the SbD-ToE.  
> Its effectiveness depends on **contextual relevance, practical repetition and peer validation**.
