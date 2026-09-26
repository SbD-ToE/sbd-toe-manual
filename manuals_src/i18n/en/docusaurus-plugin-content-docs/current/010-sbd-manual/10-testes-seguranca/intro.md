---
id: intro
title: Security Testing
description: Strategies and practices for continuously validating application security through automated, manual and offensive testing
tags: [testes, segurança, validação contínua, SAST, DAST, fuzzing, pentesting, DSOMM, SAMM, SSDF, SLSA]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/intro.md
  source_sha256: 3c70246f642f4892c5b19e50e8ebb72f685a18009438225d38956564cfa3adc8
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: a3297ac8839e3d130000215f24025f2eb74c8ad9827fbed7dcfac416695e574f
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, basilar, chapter_role, como_fazer, cycle_iteration, lifecycle_phase, mapping, oracle, papel_suporte, practitioner_manual, sbdtoe_sbd, transversal, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 0524e8cdb6fa332dcbc8ea0acf69743cde60ec5a7f71cb59cc22f0c9bc19c09d
  translated_at: 2026-09-26T10:31:39Z
  stamped_at: 2026-09-26T18:35:19Z
  reviewed_by: null
---

import ChapterTypeCallout from '@site/src/components/ChapterTypeCallout';

<ChapterTypeCallout kind="operacional" title="Capítulo Operacional">

This chapter is considered **operational** in the *Security by Design – Theory of Everything (SbD-ToE)* model.
Its function is to **apply, automate and validate** the practices defined in the foundational chapters, ensuring their continuous and measurable execution.

The operational chapters implement the SbD-ToE in specific technical contexts, translating foundational prescriptions into practices of **verifiable execution**, with **objective, traceable and auditable evidence**.

</ChapterTypeCallout>

# Security Testing

Security testing is the **turning point between theory and practice**.  
Requirements may be well defined and controls well designed, but only through **continuous and verifiable testing** is it possible to demonstrate that they work when faced with real code, complex integrations and evolving threats.

This chapter stands out for providing **objective and auditable evidence**: it confirms whether the measures prescribed in the previous chapters are effective and whether they withstand the pressure of use in production.  
It includes automated techniques (SAST, DAST, fuzzing, IAST) and manual/offensive validations (PenTesting), creating a complementary network of assurances.

👉 In short, security testing is not an optional “phase” - it is the **continuous validation mechanism** that underpins *go/no-go* decisions at every commit, build and release.

---

## ⚖️ Canonical principles applicable to security testing {#️-princípios-canónicos-aplicáveis-a-testes-de-segurança}

In the context of security testing, the SbD-ToE explicitly assumes that:

- Tools **may detect, prioritise and correlate**,  
  but **do not take final decisions**.
- Automated results **do not constitute sufficient evidence on their own**.
- The *pass/fail* decision, the acceptance of exceptions or of residual risk is **always human**, assigned to an explicit role.
- A test only “counts” when it produces **verifiable, reproducible and auditable evidence**.
- The testing process itself introduces risks (e.g. exposure of data, credentials, telemetry) that must be **explicitly controlled**.

The prescriptive rules that operationalise these principles are defined in the file  
`addon/10-evidencia-reprodutibilidade.md`.

---

## 🧪 Practical prescription {#-prescrição-prática}

Practical application must be understood as a **continuous cycle**, not as an isolated list of tools:

- **What to do:**  
  Define a clear strategy, automate whatever is possible, test at different layers (code, runtime, integrations) and complete with offensive validation in critical applications.

- **How to do it (proportional to risk):**  
  - **L1**: essential tests (SAST + manual checklist).  
  - **L2**: integrated automated tests (DAST, regressions, *gates*).  
  - **L3**: advanced tests (systematic fuzzing, IAST, pre-production PenTesting).

- **When to apply:**  
  - Start of each project (formal strategy).  
  - Each commit/PR (SAST).  
  - CI/CD builds (SCA, IAST).  
  - Staging before *go-live* (DAST, fuzzing).  
  - Each release (*gates* + formal risk acceptance).  
  - Audit and independent validation cycles (PenTesting).

- **Why:**  
  Because validation is the only way to ensure that security is not a promise but **proven reality**.  
  Tests underpin critical decisions and reduce the time of exposure to vulnerabilities.

:::note[Testing and analysis — a distinction that decides where each control lives]
Not every security verification is a *test*. A test confronts observed behaviour with expected behaviour: it has a **behavioural oracle** — this is the case of SAST, DAST, IAST, fuzzing and PenTesting, which live in this chapter. *Composition analysis* (SCA, Ch. 05), the *scanning* of secrets, IaC and container images (Chs. 06 to 09) and the *functional validation of security requirements* (Ch. 02) operate on a **lookup or policy oracle**: they confront an inventory with a CVE database, with a rule or with an acceptance criterion. The distinction is not academic — it is what justifies SCA living in the dependencies chapter, and not here. This chapter covers the behavioural oracle; the complete verification of the system is distributed across the respective chapters and consolidated in the [cross-cutting verification matrix](./addon/matriz-verificacao-transversal).
:::

---

## 👥 Roles involved {#-papéis-envolvidos}

Responsibility for testing is **collective**, but each role has explicit responsibilities:

- **Developer** → fixes findings and creates verifiable automated regressions.  
- **QA** → runs DAST, fuzzing and validates acceptance criteria.  
- **AppSec Engineer** → defines the strategy, tunes rules and manages exceptions and evidence.  
- **DevOps / SRE** → integrates scanners, *gates* and artefact preservation in the CI/CD.  
- **Product Owner** → decides *go/no-go* and approves documented residual risk.  
- **AppSec Engineer** → conducts offensive validations and provides independent technical evidence.

👉 These responsibilities are operationalised through user stories in `aplicacao-lifecycle.md`.

---

## 📜 Relevant Organisational Policies {#-políticas-organizacionais-relevantes}

| Policy | Mandatory? | Application | Minimum content |
|--------|--------------|-----------|-----------------|
| [Test Strategy Policy](/sbd-toe/assets/policies/policy-estrategia-testes) | Yes | AppSec Engineer | Versioned document with Ch. 2 ⇄ tests mapping |
| [SAST in PR Policy](/sbd-toe/assets/policies/policy-estrategia-testes) | Yes | Developer + DevOps / SRE | Automatic execution in PRs, L1–L3 thresholds |
| [DAST and Fuzzing Policy](/sbd-toe/assets/policies/policy-dast-fuzzing) | Recommended | QA | Authenticated DAST, fuzzing on critical endpoints |
| [CI/CD Gates Policy](/sbd-toe/assets/policies/policy-cicd-seguro) | Yes | DevOps / SRE + AppSec Engineer | Formal criteria, preserved logs, recorded exceptions |
| [Secure Release Policy](/sbd-toe/assets/policies/policy-release-seguro) | Yes | Executive Management + AppSec Engineer | Release checklist and documented risk acceptance |
| [Offensive PenTesting Policy](/sbd-toe/assets/policies/policy-pentesting) | Recommended (L2), Mandatory (L3) | AppSec Engineer | Risk-based scope, technical reports and retests |

In the printed version, consult the **Manual's Organisational Policies Annex**.

---

## 🏁 Conclusion {#-conclusão}

Testing is what turns security intentions into **real evidence**.  
It is the mechanism that confirms whether requirements have been implemented, whether *gates* work and whether the application withstands credible attacks.

In the SbD-ToE, security testing is a **continuous process of auditable validation**, essential to maintaining technical trust, governance and accountability throughout the entire lifecycle.

---
