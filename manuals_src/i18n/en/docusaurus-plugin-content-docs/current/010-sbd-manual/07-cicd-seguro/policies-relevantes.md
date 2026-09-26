---
id: policies-relevantes
title: Policies
description: Set of recommended policies to sustain and legitimise the CI/CD security practices described in the chapter
tags: [políticas, cicd, pipelines, governança, segurança organizacional]
sidebar_position: 60
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/policies-relevantes.md
  source_sha256: ce41b5b28adb482eb07a07789f6bd129ba0ea9a6ba074bb6bd4629c0f2fde8e6
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 8c71b8b058313554e54301fde93fa8a3e8671c976fb9abfede99fe44eb299906
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [chapter_role, cycle_iteration, mapping, maturity, practitioner_manual, provenance, risk_level, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: 3f02959428f1fed5f21e8fc2bece2ae5af785abdce8cdfcff8f5a7137e0339d8
  translated_at: 2026-09-26T09:09:23Z
  reviewed_by: null
---


# Organisational Policies - Security in CI/CD Pipelines

The effective adoption of Chapter 07 - Secure CI/CD - requires the existence of **formal organisational policies** that **regulate, legitimise and sustain the security practices applicable to the continuous integration and delivery chain**.

---

## 📌 Fundamental note {#-nota-fundamental}

> ⚠️ The technical practices prescribed in this chapter (e.g. execution control, secret injection, artefact validation, segregation of pipelines) **must be formally legitimised by approved and auditable organisational policies**.

These policies:

- Make **the proportional application of security controls by risk level mandatory**;
- Establish **clear rules for the secure execution of pipelines**, avoiding ad hoc decisions;
- Enable audit of the **provenance of artefacts and validation of the critical build and deploy stages**.

> 🧩 This chapter implements the practices; the policies provide **the normative and binding basis** to ensure that they are correctly applied.

> 📎 The existence of policies on CI/CD security is an **explicit requirement** or a **strong recommendation** in frameworks such as **SLSA**, **SSDF**, **OWASP DSOMM** and **ENISA** guides.

---

## 🧾 Recommended policies {#-políticas-recomendadas}

| Policy Name                              | Mandatory? | Application                                | Summary of the required content |
|-----------------------------------------------|--------------|-------------------------------------------|-------------------------------|
| [Secure Pipeline Execution Policy](/sbd-toe/assets/policies/policy-cicd-seguro)      | ✅ Yes       | All CI/CD pipelines               | Rules for authorised execution; permitted runners; control by branch/context; events that trigger builds. |
| [Environment and Runner Segregation Policy](/sbd-toe/assets/policies/policy-cicd-seguro) | ✅ Yes       | DevOps, Security, Cloud teams          | Isolation rules by project/trust; dedicated runners; prohibition of cross execution without approval. |
| [Secret Injection and Protection Policy](/sbd-toe/assets/policies/policy-gestao-segredos)    | ✅ Yes       | The whole organisation                        | Origin and management of secrets; prohibition of hardcoded secrets; masking in logs; integration with vaults. |
| [Artefact Validation and Provenance Policy](/sbd-toe/assets/policies/policy-cicd-seguro) | ✅ Yes   | Repositories, pipelines, staging/prod environments | Generation and verification of provenance; hash and signature; rules for promotion between environments. |
| [Pipeline Review Policy](/sbd-toe/assets/policies/policy-cicd-seguro)              | ⚠️ Optional | Organisations with shared pipelines    | Mandatory peer review; change control; technical approval of templates. |
| [Risk-Proportional Application Policy](/sbd-toe/assets/policies/policy-classificacao-risco)  | ⚠️ Optional | Organisations with formal classification     | Mapping between risk level and minimum controls required in the pipeline. |

---

## 📋 Suggested structure of each policy {#-estrutura-sugerida-de-cada-política}

Each organisational policy must contain, at a minimum:

- **Objective and scope** (application to pipelines, environments, teams, artefact types);
- **Mandatory criteria and explicit permissions** (e.g. authorised runners, sources of secrets, deploy rules);
- **Roles and responsibilities** (DevOps, Security, AppSec, product owners);
- **Mechanisms for recording, validation and traceability** (e.g. provenance, execution logs, approval of exceptions);
- **Rules for periodic review of the policy** (e.g. annual review, or after incidents).

---

## ✅ Final recommendations {#-recomendações-finais}

- The policies must be **officially approved by technical and security management**;
- They must be **accessible to all teams involved in the pipelines and deliveries**;
- Their existence is a **necessary condition to guarantee the maturity and auditability of the CI/CD cycle**;
- Their application must be visible in the practices defined in this chapter, with a **direct link to controls and validations in the pipeline**.

> 📌 Templates for these policies may be made available as `60-*.md` files in future versions of the manual.
