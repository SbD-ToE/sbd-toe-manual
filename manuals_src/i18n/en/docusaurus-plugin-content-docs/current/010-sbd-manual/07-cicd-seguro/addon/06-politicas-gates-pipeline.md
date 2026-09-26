---
id: politicas-gates-pipeline
title: Policies and Gates by Application Level
sidebar_position: 6
description: Definition of automated policies in the pipeline with security gates that vary according to the risk level of the application.
tags: [cicd, gates, políticas, risco, segurança, validações]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/addon/06-politicas-gates-pipeline.md
  source_sha256: 7e96c77baf2cdaa4e22f9d51dd75393b44732c5604bbc5e32dfcad47e5230b3f
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 629b44eef5fe2b4e43e1e4bcd247ed7df3803b6d11612bfc06e01c8a52e17733
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, provenance, risk_level, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 75429002251f7e051589f83b2f184b39c69e6564fd5732033e10448f2a9d644d
  translated_at: 2026-09-26T09:09:15Z
  stamped_at: 2026-09-26T18:34:19Z
  reviewed_by: null
---


# Policies and gates by application level

Not all applications require the same level of security, but **all must comply with clear policies**, proportional to their risk. This practice defines the automated application of **policies, gates and controls by application level**, ensuring that:

- Criticality dictates the rigour of the control mechanisms;
- Bypass is only possible upon formal and auditable justification.

> The absence of a clear policy inevitably leads to inconsistent and permissive pipelines.

---

## 🎯 Objectives {#-objetivos}

- Prevent critical applications from advancing in the pipeline without mandatory validations;
- Ensure that security policies are applied consistently, automatically and auditably;
- Prevent informal bypass of critical stages in CI/CD.

---

## 🛠️ Practices {#️-práticas}

1. **Explicit classification of the application (L1–L3)**  
   - The risk level of the application must be defined (e.g. in a `.risk-level.yml` file, an environment variable, a repository tag);
   - That classification must determine the behaviour of the pipeline.

2. **Conditional application of policies and controls**  
   - L3 applications require signed provenance, formal review of findings, minimum coverage, etc.;
   - Policies must be coded directly into the pipeline (e.g. YAML templates, conditional workflows, policy-as-code).

3. **Automated, blocking security gates**  
   - Automated checks must prevent the pipeline from advancing if controls are not met;
   - They must be mandatory for levels L2 and L3 (e.g. SAST, coverage, SBOM, analysis of findings).

4. **Formal management of exceptions and bypass**  
   - Exceptions must be recorded, justified and formally approved (e.g. via `change request`);
   - Advancing with critical applications without explicit security validation is not permitted.

5. **Periodic review and update of policies**  
   - Policies must be maintained in versioned and auditable templates;
   - There must be a mechanism to verify the version of the policy applied (e.g. `policy-version.yml`).

---

## ⚖️ Proportional application by risk level {#️-aplicação-proporcional-por-nível-de-risco}

| Level | Policy requirements                                     | Blocking criteria                                   |
|-------|-------------------------------------------------------------|----------------------------------------------------------|
| **L1** | Basic rules (e.g. clean build, light SAST)                 | Build fails on a critical error                             |
| **L2** | Validated findings; minimum coverage; secrets checked | High-severity findings prevent promotion             |
| **L3** | Complete gates: SAST, DAST, IaC, SBOM, provenance        | Advances only with formal security approval              |

---

## 📌 Practical examples {#-exemplos-práticos}

- **GitHub Actions**  
  - Conditional workflows with `.risk-level.yml`;  
  - `required status checks` for specific gates (SAST passed, coverage OK).

- **GitLab CI**  
  - `rules:` with variables such as `APP_CRITICALITY=L3`;  
  - `when: manual` stages with security approval for L3.

- **Azure DevOps**  
  - `Environments` with `approval gates` and `branch protection`;  
  - YAML + branch policies for conditional enforcement.

- **Jenkins**  
  - Use of `when { expression { isCritical() } }` to activate enhanced stages;  
  - Integration with policy-as-code tools (e.g. Open Policy Agent - OPA).

---

## 📉 Mitigated risks {#-riscos-mitigados}

- Deploys of critical applications without mandatory validation (OSC&R: CI0006, CI0014);
- Divergence between organisational policy and what the pipeline applies;
- Informal or accidental bypass of security stages (OSC&R: CI0002).

---