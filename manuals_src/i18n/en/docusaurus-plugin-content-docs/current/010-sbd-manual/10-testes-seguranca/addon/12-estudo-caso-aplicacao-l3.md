---
id: estudo-caso
title: Case Study - Continuous Security Validation in a Critical Application
description: Practical example of applying security testing practices to an application classified as L3, with full pipeline integration and findings management.
tags: [estudo de caso, testes, segurança, integração, devsecops, aplicação crítica]
sidebar_position: 12
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/addon/12-estudo-caso-aplicacao-l3.md
  source_sha256: c58bfa62415d55326b6e996e953ce985bb7f1c257d6b25e118bdba312b54d035
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 64342e1d5512c79e07d659cfcfb1d878983652a41c60e60d077f46d13a39de9b
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 2ffd43fd37c8802a693f5fa1e43a3d3a9df1ca9d5ea898c88f6f405bedc9d687
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, practitioner_manual, risk_level, sbdtoe_sbd, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: 0c4c5b21baa128815fece4a376c77da20a4c6317a70ae259acf37dfb65f98507
  translated_at: 2026-09-26T10:31:32Z
  reviewed_by: null
---

# Practical Application of the SbD-ToE Prescriptions in an L3 Application

The example refers to an online payment system for retail and public services. 
The application was classified as **level L3** in Chapter 01 - Risk Management, due to its functional criticality and exposure to financial and personal data. The development and delivery process fully follows the model prescribed in the SbD-ToE manual, and the focus here is on how the testing processes in particular, and other areas of the SbD-ToE, are orchestrated.

---

## 👨‍💻 Development with built-in quality (Ch. 06) {#-desenvolvimento-com-qualidade-embutida-cap-06}

During development, the developers used:

* **GenAI copilots with customised security rules**;
* **Linters and local SAST (e.g. customised Semgrep)** directly integrated into the IDE;
* **Story templates and acceptance criteria with built-in security** (see Ch. 02 - Security Requirements);
* **Isolated environment with DevContainers and preventive scanners** (see Ch. 09 - *Containers* and Isolated Execution).

Result: when submitting a Pull Request, most trivial problems had already been eliminated.

---

## 🔍 Automatic validations in the Pull Request (Ch. 10, Ch. 07) {#-validações-automáticas-no-pull-request-cap-10-cap-07}

At PR time, the following are activated:

* **Full SAST via Checkmarx**;
* **Compliance linters (YAML, JSON, infra)**;
* **Dependency verification with Xygeni and generated SBOMs** (see Ch. 05 - SBOM and SCA);
* **Integration of automatic feedback into the PR** (via GitHub + inline comments).

Blocking criteria configured (Ch. 10 `addon/01`, `addon/02`, `addon/04`):

* No critical finding may be "open";
* Any high finding requires **triage or a justified exception** (Ch. 10 `addon/08`);
* The risk-based test plan (Ch. 10 `addon/00`) validates whether the L3 matrix is being met.

---

## 🗒️ Findings Management (Ch. 10, Ch. 05) {#️-gestão-de-findings-cap-10-cap-05}

Findings are automatically recorded in **DefectDojo**, with:

* Commit, PR and branch metadata;
* Classification by severity, origin (SAST/DAST/Fuzzing), CVSS;
* Recurrence or regression analysis (Ch. 10 `addon/08`);
* Integration with the backlog (Jira), with assigned ownership (Ch. 06).

Exceptions are submitted with:

* Technical justification;
* Compensating mitigation;
* Mandatory reassessment date (Ch. 10 `addon/08` + `20-checklist`).

---

## ⚠️ Staging environment and offensive testing (Ch. 10, Ch. 11) {#️-ambiente-de-staging-e-testes-ofensivos-cap-10-cap-11}

After merge:

1. The code is deployed to **isolated staging**, with secure variables (Ch. 07 and Ch. 09);

2. Combined tests are executed:

   * **DAST with authentication + spidering** (Burp Enterprise);
   * **Coverage-guided fuzzing** (RESTler + ZAP add-ons);
   * **IAST via passive instrumentation** (Contrast).

3. In parallel, a **Grey-box PenTest** is scheduled by an internal team, with access to documentation and sensitive endpoints. The vectors explored include:

   * Session manipulation;
   * Privilege escalation;
   * Bypass of client-side validations;
   * Abuse testing on transactional APIs.

PenTest results are integrated into the same findings process (Ch. 10 `addon/11-pen-testing.md`), with a treatment cycle identical to that of the other tests.

---

## 🛡️ Continuous monitoring and response (Ch. 12 + Ch. 05) {#️-monitorização-e-resposta-contínua-cap-12--cap-05}

In production:

* The application is instrumented with **security telemetry**, covering authentication failures, suspicious behaviour, anomalous HTTP errors;
* Production artefacts include complete signed SBOMs (see Ch. 05);
* The **Xygeni tool continuously monitors the SBOM and the supply chain** (SSCS):

  * Identifies **malware in libraries**;
  * Detects **new CVEs with direct impact**;
  * For packages with a **safe update**, **automatically opens PRs** with the fix;
  * For packages with functional impact, **creates a critical issue** with automated risk analysis and the dependency blocked until manual review.

This process closes the cycle, since:

* Findings are associated with specific versions and SBOMs;
* Teams are notified by channel (Slack + Jira + e-mail);
* All actions are **documented for future audit** (Ch. 10 `addon/08` + `addon/09`).

---

## 📦 Final validation before release (Ch. 11) {#-validação-final-antes-do-release-cap-11}

Before going into production:

* A **security checklist (Ch. 10 `20-checklist`)** is generated with full traceability;
* All **exceptions must be approved and documented**;
* The **PenTest results must be resolved or formally accepted**;
* The release is only permitted if all mandatory tests have positive coverage.

---

## 📈 Conclusion {#-conclusão}

This narrative demonstrates the **practical application of the SbD-ToE model in an integrated and realistic way**, with:

* Proportional application by risk level (L3);
* Continuous, offensive and regression validations;
* Integration of leading tools (Checkmarx, Xygeni, DefectDojo);
* A security culture sustained by processes, policies and automation.

> 📌 Each step of the story corresponds to one or more explicit prescriptions of the manual, validating that the SbD-ToE is feasible, auditable and effective - even in highly demanding contexts.
