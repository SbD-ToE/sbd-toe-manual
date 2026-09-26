---
id: pen-testing
title: Offensive Testing (PenTesting)
description: Execution of controlled manual tests to identify vulnerabilities not detected by automated mechanisms.
tags: [pentesting, testes manuais, segurança ofensiva, grey-box, black-box]
sidebar_position: 12
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/addon/11-pen-testing.md
  source_sha256: e930c6bafda525d0ac6c44742b81708366d55095d34531823d29e15fcc012aa0
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 47cfaf720d351e795a18683572b0355d7b675e23821b2453f0b4ebe3836891e0
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, cycle_iteration, instrument, lifecycle_phase, maturity, practitioner_manual, sbdtoe_sbd, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: bcc9265d6da244347046958b28d591c4ebff239a296b8a8166bb0506881c28d7
  translated_at: 2026-09-26T10:31:31Z
  stamped_at: 2026-09-26T18:35:11Z
  reviewed_by: null
---


# PenTesting - Offensive Security Validation

This document establishes the technical and procedural framework for carrying out **penetration testing (PenTesting)**, as a practice complementary to the continuous validation described in Chapter 10.

---

## 🌟 Objective {#-objetivo}

To define:

- When PenTesting must be applied;
- How it must be planned and integrated into the lifecycle;
- Which types of approach are possible (black-box vs grey-box);
- How its results must be used to reinforce security;
- How Chapter 10 can serve as a basis for preparation and scope.

---

## 🔍 What PenTesting is {#-o-que-é-pentesting}

PenTesting is a **manual and exploratory offensive validation**, which simulates real attacks on a system with the objective of:

- Identifying vulnerabilities that escape automated validation;
- Assessing the effectiveness of implemented controls;
- Measuring the application's real exposure.

> 🎯 Unlike SAST/DAST, which test systematically, the PenTest simulates adversarial reasoning, logic abuse and contextualised exploitation.

---

## ⚙️ Possible approaches {#️-abordagens-possíveis}

There are two main ways of conducting a PenTest:

### ⚫ "Black Box" approach (*Black Box*) {#-abordagem-caixa-negra-black-box}

| Characteristic           | Description |
|--------------------------|-----------|
| Prior knowledge      | None. The pentester acts as an external attacker. |
| Data provided         | Only the URL or public entry point. |
| Focus                     | External exposure, functional abuse, visible misconfiguration. |
| Limitation                | May miss critical areas that are not directly exposed. |

**Relationship with Ch. 10:**
- Allows assessing whether the protection implemented (DAST, fuzzing) is effective;
- Helps validate scanner coverage in a real context;
- Useful as independent verification of the external posture.

---

### ⚪ "Grey Box" approach (*Grey Box*) {#-abordagem-caixa-cinzenta-grey-box}

| Characteristic           | Description |
|--------------------------|-----------|
| Prior knowledge      | Partial. The pentester receives technical context. |
| Data provided         | SAST/DAST/SCA findings, SBOM, endpoints, credentials, API docs. |
| Focus                     | Targeted exploitation, validation of fixes, real gaps. |
| Benefit                | Greater effectiveness with a risk-driven scope. |

**Relationship with Ch. 10:**
- Uses the findings from continuous validation as input;
- Allows confirming the effectiveness of applied fixes and controls;
- Supports targeted regression and verification of effective mitigation.

---

## 🔁 Integration with Chapter 10 {#-integração-com-o-capítulo-10}

The PenTest **does not replace** continuous testing - it is a **strategic complement** to:

- Validate the effectiveness of defences already applied;
- Confirm the coverage of automated tests;
- Identify abuses that escape systematic analysis.

### Suggested integration cycle: {#ciclo-de-integração-sugerido}

1. **Before the PenTest**
   - Consolidate findings from automated tests;
   - Map critical areas, recent changes, complex endpoints;
   - Share data with the PenTest team (grey-box preferred).

2. **During execution**
   - Follow a structured methodology (e.g. OWASP Testing Guide);
   - Document vectors, payloads, impact, bypasses and anomalies;
   - Respect the agreed rules of engagement (e.g. scope, limits, reporting).

3. **After the PenTest**
   - Record all findings as issues;
   - Associate each finding with a component, risk and real impact;
   - Apply the process of treatment, correction and continuous revalidation.

---

## 📋 Planning Checklist {#-checklist-de-planeamento}

| Item                                                       | Verified? |
|------------------------------------------------------------|-------------|
| Scope defined on the basis of risk classification         | ☐           |
| Endpoints, APIs and versions documented                     | ☐           |
| Secure and isolated test environment available             | ☐           |
| NDA and access agreements defined (if applicable)           | ☐           |
| Rules of engagement and reporting agreed                  | ☐           |
| Previous results of continuous validation analysed     | ☐           |
| PenTest findings recorded with full traceability| ☐           |
| Revalidation scheduled after fixes                        | ☐           |

---

## 📎 Difference between PenTest and other validations {#-diferença-entre-pentest-e-outras-validações}

| Type                   | Characteristics                               | Automated? | Performed by        |
|------------------------|-----------------------------------------------|---------------|------------------------|
| **PenTesting**         | Manual, offensive, simulative                  | ❌ No         | Internal/external offensive team |
| SAST/DAST/Fuzzing      | Continuous, rule-based                   | ✅ Yes         | CI/CD, QA, AppSec      |
| IAST                   | Runtime, execution-sensitive                  | ✅ Partial     | Dev/Test               |
| Red Team               | Persistent, objective-driven simulation  | ❌ No         | Internal/Consultants    |
| Bug Bounty             | Open, collaborative, reward per finding | ❌ Partial     | External community     |

---

## ✅ Conclusion {#-conclusão}

PenTesting is an **instrument of external and independent validation**. Its effectiveness depends directly on its **integration with internal security mechanisms**.

To be useful, it must:

- Rely on the data from continuous validation (Ch. 10);
- Be traceable, documented and comparable with previous findings;
- Feed improvements into the security lifecycle, architecture and requirements.

> 📌 The PenTest validates the application **and also the organisation's maturity** in managing, fixing and learning from detected failures - being a fundamental part of the continuous improvement cycle of the SbD-ToE model.
