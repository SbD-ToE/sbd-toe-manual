---
id: case-study-inception-apply-sbd-to-cicd
title: Case Study - Applying SbD-ToE to the CI/CDx Pipeline Itself
sidebar_position: 9
description: Formal rules for allowing exceptions in the pipeline, with registration, approval, expiry date and visibility by function.
tags: [exceções, visibilidade, cicd, governação, auditoria, segurança]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/addon/11-case-study-inception-apply-sbd-to-cicd.md
  source_sha256: 978bb4027a5f2c24b544eecf6b2dddfbad2255b290b294bcc22a103c521ee0e4
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 55172fc30264a17f897904cda8c931b527eb8559e2d204bb73ea1d9a3904db5e
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [avaliacao, chapter_role, cycle_iteration, framework_source_corpus, lifecycle_phase, maturity, practitioner_manual, provenance, sbdtoe_sbd, traceability, transversal, validation_evaluation]
  glossary_sha256: 5a5425eaa90b6e44d2d592bbd5f9e25a451f6033de9dd7a5bddaa1dd38e53104
  translated_at: 2026-09-26T09:09:18Z
  reviewed_by: null
---


# Case Study - Applying SbD-ToE to the CI/CD Pipeline Itself

This case study describes the cross-cutting and rigorous application of the **Security by Design - Theory of Everything (SbD-ToE)** manual to an organisation's **own CI/CD pipeline system**. 

> The objective was to treat the pipelines as **critical assets (level L3)**, with a lifecycle, risks and controls comparable to those of any sensitive software product.

The approach followed all the lifecycle phases described in the manual - from risk to operation - with validations, traceability and automation as central pillars.

---

## 🧭 Context and decision {#-contexto-e-decisão}

The organisation operates multiple applications in regulated environments. Following an assessment based on Chapter 01 - Risk Management, it was identified that:

- The CI/CD pipeline has privileged access to code, artefacts, secrets and infrastructure;
- It is the entry point for the whole software lifecycle;
- Its integrity conditions the security of the whole SDLC.

> **Strategic decision:** Treat the pipelines as software of high criticality (level L3), and apply SbD-ToE as if they were a product.

---

## 📐 Architecture designed {#-arquitetura-desenhada}

A modular and secure architecture was adopted (Ch. 04):

- Pipelines as code (`.yaml`) in a dedicated repository with change control;
- Versioned central templates, with a formal approval policy;
- Segregated runners (build/test/deploy), with isolation and disposal;
- Dynamic secrets management via Vault (Ch. 03, 06);
- Internal mirrors for NPM, Maven, Docker (Ch. 05);
- Provenance and signing of the generated artefacts (Ch. 07);
- Complete logging with auditability of runs (Ch. 11).

---

## 🔍 Threat modelling {#-threat-modeling}

The threat modelling exercise (Ch. 03) identified risks such as:

- **Spoofing:** execution of pipelines on unauthorised runners → mitigated with restricted labels and dedicated workers.
- **Tampering:** silent alteration of templates → mitigated with mandatory PRs and reviews.
- **Information Disclosure:** improper access to secrets → mitigated with minimum scope and validated logs.
- **Elevation of Privilege:** inline tasks with excessive permissions → mitigated with manual review and a controlled catalogue.

---

## 🛠️ Secure development of the pipelines themselves {#️-desenvolvimento-seguro-dos-próprios-pipelines}

Applying Ch. 06:

- All pipeline code is versioned, with mandatory review;
- Linters and scanners analyse `.yaml`, embedded scripts and reused modules;
- Tasks, Actions and extensions are included in an **SBOM of its own**, with continuous validation (Ch. 05);
- Specific non-functional requirements were defined, e.g. `CI-CD-004`, `CI-CD-006`, `EX-REQ-014`, `EX-REQ-024` — illustrative identifiers; they do not correspond to the Requirements Catalogue of Ch. 02.

---

## 🧪 Tests applied to the pipeline {#-testes-aplicados-ao-pipeline}

Based on Ch. 10:

- SAST on auxiliary scripts and embedded tasks;
- Analysis of secrets and excessive permissions;
- Regression tests to ensure the enforcement of gates;
- Sandbox runs with traceability of inputs/outputs.

---

## 🔐 Management of dependencies, images and SBOM {#-gestão-de-dependências-imagens-e-sbom}

- SBOM of the pipeline generated with `syft` + `trivy`;
- External dependencies (e.g. Actions, plugins) audited and versioned;
- Runners based on verified, hardened containers, with signature validation (Ch. 09);
- Exception policy with validity and traceability (Ch. 05, 14).

---

## 📦 Deploy and execution {#-deploy-e-execução}

- The pipeline itself is deployed with full traceability;
- Logs are sent to a central system with anomaly alerts;
- With each relevant change, a new threat modelling review and functional validation are mandatory.

---

## 🎓 Training and onboarding {#-formação-e-onboarding}

- A training module was created (Ch. 13) for Dev and DevOps teams:
  - Good practices for changing pipelines;
  - Validation and traceability;
  - How to interpret security results.
- User stories and cards included in the technical backlog of the CI/CD team.

---

## 📊 Governance and visibility {#-governação-e-visibilidade}

- CI/CD compliance scorecard updated quarterly;
- Auditable exceptions approved by security (Ch. 14);
- Integration with internal audits and maturity monitoring.

---

## ✅ Conclusion {#-conclusão}

This case demonstrates the **cross-cutting and coherent application of the SbD-ToE manual to a critical CI/CD system**. 

> Treating the pipeline as a software product, with L3 risk, made it possible to:
> - Drastically reduce supply chain risks;
> - Gain end-to-end visibility and traceability;
> - Automate security decisions across the development and operations lifecycle.

The approach is scalable and replicable in other organisations.

> 💡 **This is a complete example of the application of SbD-ToE as an operational framework.**
