---
id: matriz-controlos-por-risco
title: Minimum Controls Matrix by Risk Level
sidebar_position: 5
tags: [tipo:matriz, risco, controlos, proporcionalidade]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/addon/05-matriz-controlos-por-risco.md
  source_sha256: ed33263e24c642988d8d77c25ecf97a2654628414aa81b3d1a81993d5674196f
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: c62015338be1305c24df677acdd80c30191ca40c7e6051589164a6b4c3c16648
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [avaliacao, chapter_role, cycle_iteration, deterministic, evidenciabilidade, instrument, lifecycle_phase, normative_empirical, practitioner_manual, provenance, risk_level, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: a89f91759b7403887019a12ce50c6416bd2077f3aaf4975e4751ac88c8a3709b
  translated_at: 2026-09-25T20:18:46Z
  stamped_at: 2026-09-26T18:32:46Z
  reviewed_by: null
---

<!--template: sbdtoe-core -->

# Minimum Controls Matrix by Risk Level

This matrix defines the **minimum floor of security controls expected**, by technical domain, according to the **application's risk level (L1–L3)**, as determined in Chapter 01.

The controls listed here are a **mandatory baseline** for each risk level and must be understood as **enforceable minimums**, not as an upper limit of application.

The matrix can be used:
- as an independent technical reference;
- as a basis for release criteria;
- as input for risk acceptance models;
- as an instrument for control, audit or organisational KPIs.

---

## 🧠 Normative framing {#-enquadramento-normativo}

In *Security by Design – Theory of Everything (SbD-ToE)*, the application's risk level determines **the minimum degree of rigour** expected in the application of security controls.

However:

- the **L1–L3** level results from a **simplified projection** of the risk (E/D/I model);
- the **attributes of the risk** (detectability, evidentiability, reproducibility, delegation, real impact) may require **additional reinforcement**;
- the absence of adequate evidence **invalidates the effective application of the control**, even if it is “planned”.

This matrix must therefore be applied **together** with:
- the risk classification model;
- the acceptance criteria;
- the residual risk analysis;
- and the risk lifecycle.

---

## 🛠️ Controls Matrix by Risk Level {#️-matriz-de-controlos-por-nível-de-risco}

| Domain                          | Low Risk (L1)                              | Medium Risk (L2)                                           | High Risk (L3)                                                      |
|----------------------------------|-----------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------------------|
| Requirements (Ch. 2)              | ASVS N1 (adapted)                            | ASVS N2 + formal criteria                                 | ASVS N2/N3 complete + validation by security                            |
| Threat Modelling (Ch. 3)         | Informal or omitted                           | Regular collaborative sessions                             | Formal with DFDs + STRIDE and recording                                       |
| Secure Architecture (Ch. 4)      | Minimum patterns                               | Technical review + trust zones                        | Formal review + mitigation documentation                               |
| Dependencies (Ch. 5)            | `npm audit` / `dotnet list`                   | SCA with severity policy                              | Automated SCA + SBOM + alerts                                        |
| Development (Ch. 6)         | Linters + basic review                      | Guides + specific PR rules                            | Mandatory review + reinforced secure review practices              |
| CI/CD (Ch. 7)                   | Protected credentials                        | Validation of environments and secrets                           | Provenance, SLSA + integrity controls                            |
| IaC (Ch. 8)                     | Manually reviewed scripts                  | Scanners (e.g. tfsec)                                       | Formal policies + mandatory enforcement in the pipeline                  |
| Containers (Ch. 9)              | Trusted images + updates                     | Hardening + image scanning                              | Signing, formal policy, runtime protection                          |
| Security Testing (Ch. 10)    | Manual checklists                            | Ad hoc SAST + DAST                                        | Fuzzing, regression, continuous DAST                                         |
| Secure Deployment (Ch. 11)          | Checklist + basic reversibility            | Dual approval + version control                       | Formal security validation process                                 |
| Operations (Ch. 12)              | Local logging                                 | Basic alerts + lightweight SIEM                                 | Integration with IRP + real-time detection                                |
| Training (Ch. 13)               | Brief onboarding session                    | Annual training + practical sessions                           | Formal training + periodic assessments                                    |
| Governance (Ch. 14)             | Simple security clauses                | Templates with compliance                                  | Requirements by risk + validation before onboarding                     |

---

## ⚠️ Mandatory control step-up rule {#️-regra-de-reforço-obrigatório-de-controlos}

> ⚠️ **Essential normative note**

Whenever the **attributes of the risk** indicate:
- low detectability;
- low evidentiability;
- non-deterministic behaviour;
- high delegation or automatic execution with real impact  
  (including advanced automation or decision support),

**controls equivalent to the next level up** must be applied,  
**regardless** of the L1–L3 classification initially assigned.

This rule applies to any technology or development practice and **does not depend on the explicit presence of AI**.

---

## 🔄 Updating and maintaining the matrix {#-atualização-e-manutenção-da-matriz}

This matrix must be:
- reviewed whenever relevant changes occur in the manual;
- adjusted to the regulatory and organisational context;
- kept consistent with internal security and risk policies.

Its use does not dispense with:
- contextual analysis;
- production of evidence;
- formal recording of the decisions taken.

---

## 📌 Final note {#-nota-final}

This matrix **does not define “the maximum to do”**,  
it defines **the acceptable minimum** for each risk level.

Effective security results from the **conscious, evidentiable and proportional application** of controls -  
not from mere compliance with a table.

---

## 🔗 Useful links {#-ligações-úteis}

- [Chapter 01 – Application Criticality Classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
- [Classification Model by Axes (E/D/I)](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/modelo-classificacao-eixos)
- [Risk Acceptance Criteria](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/criterios-aceitacao-risco)
- [Residual Risk Analysis](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/risco-residual)
