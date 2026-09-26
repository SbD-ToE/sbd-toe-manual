---
id: policies-relevantes
title: Policies
description: Formal policies required to legitimise and operationalise the continuous validation of application security.
tags: [policy, organizacional, testes, segurança, validação, dsoom, ssdf, samm]
sidebar_position: 60
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/policies-relevantes.md
  source_sha256: ef090de3c6fd9e24d5db43578f9ecfa8b6fbcd2f728e0a96312ec2f96b5b162e
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 39e0c2433ccac74c3d257a2101943be4b5955496b85e778ed71594a5e5116561
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 2ffd43fd37c8802a693f5fa1e43a3d3a9df1ca9d5ea898c88f6f405bedc9d687
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, lifecycle_phase, maturity, practitioner_manual, traceability, validation_evaluation]
  glossary_sha256: ddf85f927c43aa6ec782c402dfcb880dfb5c34e6cbb1adafd6d5594817754d58
  translated_at: 2026-09-26T10:31:39Z
  reviewed_by: null
---


# Organisational Policies - Security Testing

The effective application of **Chapter 10 - Security Testing** requires the existence of **formal organisational policies** that define:

- **What to test**, **when to test** and **how to validate** application security;
- The **minimum required levels** of coverage and proportionality by criticality (L1–L2–L3);
- **Findings management**, **exceptions**, **revalidations** and **traceability mechanisms**;
- The **periodic execution of offensive testing (PenTesting)** as reinforcement and complementary validation of automated mechanisms.

---

## 📌 Fundamental note {#-nota-fundamental}

> ⚠️ Effective security validation does not depend on tools alone - it depends on **clear policies that establish criteria, responsibilities and continuous control**.

These policies:

- **Formalise the minimum validation requirements by application type** and risk;
- **Define security-based release approval and rejection criteria**;
- **Require traceability between findings, exceptions, decisions and releases**;
- **Establish the use of manual offensive validation (PenTesting) as complementary reinforcement where applicable**;
- **Facilitate external audits, regulatory compliance and continuous improvement**.

> 🧩 This chapter **executes and operationalises organisational policies** relating to continuous validation and security testing.

---

## 🧾 Recommended policies {#-políticas-recomendadas}

| Policy Name                                       | Mandatory? | Application                                 | Summary of required content |
|--------------------------------------------------------|--------------|--------------------------------------------|-------------------------------|
| [Application Security Validation Policy](/sbd-toe/assets/policies/policy-estrategia-testes)       | ✅ Yes       | All applications with continuous delivery   | Required test types (SAST, DAST, fuzzing), minimum levels by criticality, approved tools. |
| [Security Findings Management Policy](/sbd-toe/assets/policies/policy-estrategia-testes)            | ✅ Yes       | All products with an active scanner        | Process for triage, classification, prioritisation, tracking, ownership and reporting of findings. |
| [Policy on Exceptions to Identified Vulnerabilities](/sbd-toe/assets/policies/policy-excecoes-cve)  | ✅ Yes       | When a finding is not fixed          | Technical justification, validity period, periodic review, compensating mitigation. |
| [Offensive PenTesting Execution Policy](/sbd-toe/assets/policies/policy-pentesting)            | ⚠️ Optional  | L2/L3 applications, external APIs, critical products | Defined periodicity (e.g. half-yearly), scope, methodology, objectives (black-box/grey-box), reporting and mandatory follow-up. |
| [Security Test Coverage Policy](/sbd-toe/assets/policies/policy-estrategia-testes)           | ⚠️ Optional  | Critical applications (L2–L3)                | Definition of expected coverage metrics, targeted fuzzing, regression testing. |
| [Policy on Integrating Testing with the Lifecycle](/sbd-toe/assets/policies/policy-estrategia-testes)     | ⚠️ Optional  | Teams with DevSecOps integration           | Definition of BDD criteria, integration with pipelines, PRs and release processes. |
| [Test Revalidation and Observability Policy](/sbd-toe/assets/policies/policy-estrategia-testes)    | ⚠️ Optional  | Environments with audit requirements      | Revalidation of findings, logging of tests, analysis of execution failures. |
| [DAST and Fuzzing Policy](/sbd-toe/assets/policies/policy-dast-fuzzing) | ⚠️ Optional | L2/L3 applications, public APIs | Authenticated DAST, fuzzing on critical endpoints, management of dynamic findings. |
| [Secure Release Policy](/sbd-toe/assets/policies/policy-release-seguro) | ✅ Yes | All applications with continuous delivery | Release checklist, security-based go/no-go, documented risk acceptance. |

---

## 📋 Suggested structure of each policy {#-estrutura-sugerida-de-cada-política}

Each policy must include, at least:

- **Objective and scope** (e.g. security validation by application type or context);
- **Mandatory criteria by criticality level (L1–L3)**;
- **Technical requirements by test type** (e.g. permitted tools, formats, thresholds, scopes);
- **Roles and responsibilities** (e.g. QA, AppSec, product, Dev team, Red Team or external team);
- **Format of required evidence** (e.g. reports, logs, dashboards, issues, SBOM);
- **Exception, follow-up and periodic revalidation processes**;
- **Policy review and improvement cycle**.

---

## ✅ Final recommendations {#-recomendações-finais}

- These policies must be **approved jointly by the Security, Quality and Development areas**;
- They must be **documented, accessible and integrated into the software lifecycle**;
- Their application must be **auditable, based on objective evidence and aligned with automated pipelines and planned offensive testing**;
- The organisation's maturity in security validation depends **not only on the execution of tests, but on the existence of formal and consistent criteria**.

> 📌 Well-defined policies are the **guarantee that tests - automated or manual - have a real, visible and continuous impact on the organisation's security**.
