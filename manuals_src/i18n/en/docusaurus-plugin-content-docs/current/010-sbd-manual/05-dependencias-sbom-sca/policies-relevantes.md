---
id: policies-relevantes
title: Policies
description: Organisational policies that support the practical application of this chapter
tags: [policy, organizacional, sbom, sca, dependencias]
sidebar_position: 60

translation:
  source_locale: pt
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/policies-relevantes.md
  source_sha256: fdfa6ef1ddc71a066c6f3af978e52b07922e4b49ab8e589e7adfcd901d042f5d
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: ab0524fa10d9ac60e65b55e7f8cb40cb9e19897e3b189108cf94552febc2bc80
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, avaliacao, chapter_role, cycle_iteration, mirror_osf, traceability]
  glossary_sha256: bb7758fb20669ca2c33644ed726014d9df0619ace1ac3aa55cb1bd6d8a9c59a3
  translated_at: 2026-09-26T08:45:31Z
  stamped_at: 2026-09-26T18:33:57Z
  reviewed_by: null
---

# Organisational Policies - Dependencies, SBOM and SCA

The effective adoption of Chapter 05 - Dependencies, SBOM and SCA - requires the existence of **formal organisational policies** that **regulate and support the secure management of third-party libraries, software composition analysis and the use of SBOMs**.

---

## 📌 Fundamental note {#-nota-fundamental}

> ⚠️ The technical practices described in this chapter (inventory, SCA analysis, SBOM integration, origin registries, exception management) **must be legitimised by approved organisational policies**.

These policies:

- Make the management of dependencies and external artefacts **mandatory and auditable**;
- Allow decisions on updating, blocking or accepting risks to **follow defined and consistent criteria**;
- Are a **mandatory reference** in build, CI/CD, vulnerability management and audit processes.

> 🧩 This chapter **operationalises the formal policies** on dependencies and external components. The policy defines, the chapter executes.

> 📎 The existence of these policies is **explicitly recommended** by frameworks such as **NIST SSDF**, **OWASP SAMM** and **SLSA** .

---

## 🧾 Recommended policies {#-políticas-recomendadas}

| Policy Name                                      | Mandatory? | Application                                   | Summary of the required content |
|-------------------------------------------------------|--------------|----------------------------------------------|-------------------------------|
| [Dependency and Library Management Policy](/sbd-toe/assets/policies/policy-dependencias)      | ✅ Yes       | All projects with third-party code    | Rules for the use, approval, versioning, updating and blocking of dependencies. |
| [SBOM Integration and Management Policy](/sbd-toe/assets/policies/policy-sbom)               | ✅ Yes       | Build, release and audit pipelines      | Required format (CycloneDX/SPDX), generation frequency, mandatory artefacts and retention. |
| [Policy on Vulnerability Assessment in Third-Party Components (SCA)](/sbd-toe/assets/policies/policy-excecoes-cve) | ✅ Yes       | Projects delivering to production           | Mandatory SCA analysis, severity criteria, response cycle and exception register. |
| [Repositories and Origin Registries Policy](/sbd-toe/assets/policies/policy-dependencias)         | ⚠️ Optional  | CI/CD, build agents, execution environments   | List of authorised registries, internal mirrors, fallback and caching policies. |
| [Policy on the Justification of Accepted Vulnerabilities](/sbd-toe/assets/policies/policy-gestao-excecoes)  | ✅ Yes       | When a CVE is accepted without an immediate patch     | Requirements for justifying exceptions, formal approval, periodic revalidation. |
| [Continuous Dependency Update Policy](/sbd-toe/assets/policies/policy-atualizacao-automatica)      | ⚠️ Optional  | Projects with short, continuous cycles       | Update frequency, use of automated tools, traceability of changes. |

---

## 📋 Suggested structure of each policy {#-estrutura-sugerida-de-cada-política}

Each organisational policy must contain, at a minimum:

- **Objective and scope** of the policy;
- **Scope of application**: who, where and when it applies;
- **Mandatory rules and criteria** (e.g. when to analyse, how to approve a dependency, SBOM format);
- **Roles and responsibilities** (security, product, dev, operations, CI/CD);
- **Requirement for documentation and traceability**;
- **Review frequency of the policy itself** (e.g. annual);
- **Requirement for traceability between policy, practice and technical evidence** (e.g. SBOM ↔ build ↔ release ↔ findings link).

---

## ✅ Final recommendations {#-recomendações-finais}

- These policies must be **approved by the security and development areas**;
- They must be **documented, disseminated and accessible** to all technical teams;
- Their existence is an essential condition for guaranteeing **formal control of the dependency chain and the integrity of builds**;
- Their application must be **automated** whenever possible, integrated into pipelines and release validations.

> 📌 Examples of policy templates may be included in complementary `60-*.md` files in future versions.
