---
id: intro
title: Introduction – Secure Development
description: Secure coding practices, curation and selection of guidelines, automated validation and governance during development
tags: [desenvolvimento, segurança, guidelines de código, linters, SAST, governação]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/06-desenvolvimento-seguro/intro.md
  source_sha256: b657a76581122881b85434934c49185e4ce2bcc84eba40b93c3fdf6a7d2ba877
  source_commit: 112711064196b71c545672fe3fb3ae412b36575e
  target_sha256: d646a0f84085e4f31c148acbbf0bef3a274379ae202b29a2702e4759dce8aaae
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 69aedbbdd11831f1cdc997bd1abfda3e2e4d3b411b1b43faf096628c510f395b
  glossary_keys: [audit_trail, basilar, chapter_role, cycle_iteration, discipline, lifecycle_phase, maturity, papel_suporte, practitioner_manual, risk_level, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: bb02b58678513c9fa89f46547780c3725497f0d139f39a88c2c85b679014df59
  translated_at: 2026-09-26T17:23:47Z
  reviewed_by: null
---

import ChapterTypeCallout from '@site/src/components/ChapterTypeCallout';

<ChapterTypeCallout kind="operacional" title="Capítulo Operacional">

This chapter is considered **operational** in the *Security by Design – Theory of Everything (SbD-ToE)* model.
Its function is to **apply, operationalise and validate** the practices defined in the foundational chapters, guaranteeing their continuous, consistent and measurable execution.

The operational chapters translate the foundational prescriptions of SbD-ToE into practices of **verifiable execution**, ensuring that security does not depend on individual intentions but on systematic mechanisms integrated into the software lifecycle.

</ChapterTypeCallout>

# Secure Development

Development is the **heart of the software lifecycle**.  
It is at this point that business value materialises in executable code - and it is also here that apparently minor technical decisions can introduce vulnerabilities with lasting impact.

For this reason, this chapter takes on a **structural** role in the manual: without consistent secure development practices, all later controls (CI/CD, testing, IaC, containers or operations) come to act only in a corrective or palliative way.

The empirical evidence is clear. Reports such as the **Verizon DBIR**, as well as multiple academic and industry studies, consistently show that a significant share of exploited flaws originates in **poor programming practices, insufficient validation or uncontrolled technical decisions** during development.

The good news is that these flaws are, to a large extent, **preventable**.  
Through systematic and auditable practices - such as clear guidelines, automated validations, formal reviews, governance of exceptions and the responsible use of development support tools - it is possible to drastically reduce the error surface introduced in this phase.

Within this scope, the chapter also covers the discipline of **secrets, sensitive parameters, cryptographic material and protected configuration** whenever these elements are introduced, reviewed or validated in code, PRs, pipelines and build artefacts. This authority remains **bounded to what is decided and evidenced in development** and does not replace the chapters on architecture, IaC, deploy, monitoring or governance.

In a context of growing use of advanced development support tools, this chapter explicitly assumes that **the origin of the code - human or automated - is irrelevant from the point of view of risk**, and adequate technical validation, verifiable evidence and clear accountability for incorporation decisions are always required.

The objective of this chapter is not to add bureaucracy but to **establish an environment where every development decision leaves objective evidence of applied security**, proportional to risk and traceable over time.

---

## 🧭 What it covers technically {#-o-que-cobre-tecnicamente}

This chapter covers all the practices that make development **secure, traceable and proportional to risk**, from the definition of rules to their continuous application:

- Curation and selection of code *guidelines* per stack, with explicit organisational governance  
- Writing secure code and systematically applying rules derived from linters and analysers  
- Automatic validations, locally and in pipelines (linters, SAST, quality profiles)  
- Management of external and internal dependencies with traceability (including SBOM)  
- Formal code reviews supported by security checklists  
- Recording, justification and governance of technical exceptions  
- Semantic annotations of security validations and decisions (`@sec:*`)  
- Responsible use of advanced development support tools, **under explicit technical constraints**, always subject to technical validation, human review and formal accountability

> ℹ️ **Controlled delegation to linters and analysers**  
> Guidelines may be **derived, codified and applied through automatic linters** (e.g. ESLint, Semgrep, Sonar, PSScriptAnalyzer), provided the rules are **versioned**, the *tailoring* is explicitly documented and there is **formal approval by Software Architects and AppSec Engineer**.  
> Automation reinforces consistency but does not replace responsibility.

---

## ⚙️ What must be done {#️-o-que-deve-ser-feito}

In practice, secure development requires teams to:

1. **Create or select (*curate*) guidelines per stack**, publishing them in a versioned, accessible and auditable form  
2. Use **organisational linters and *rulesets***, with controlled and approved *tailoring*  
3. **Integrate code validation tools** (e.g. SAST) into the continuous integration pipelines  
4. **Validate and record external dependencies**, ensuring traceability and formal justification  
5. **Manage technical exceptions** with defined mitigation, explicit approval and an expiry date  
6. **Trace security decisions** through standardised annotations in code and tests  
7. **Apply security checklists in pull requests**, ensuring objective validation  
8. **Use advanced development support tools only with technical review, licence validation and understanding of the incorporated code**

Whenever development support tools are used, teams must ensure that the code produced **respects the technical and security constraints defined for the project**, regardless of its origin.  
These constraints must be explicit, versioned and verifiable, forming an integral part of the secure development governance model.

These practices are not optional. They constitute the **foundation of trust** that supports the entire SDLC.

---

## 👥 Who is involved {#-quem-está-envolvido}

| Role / Function                  | Key responsibilities |
|--------------------------------|------------------------------|
| **Software Architects**     | Curate guidelines, approve *rulesets* and periodically review their adequacy |
| **AppSec Engineer**            | Define minimum criteria, co-approve guidelines, validate exceptions and map CWE/ASVS |
| **DevOps / SRE**               | Integrate validations into the pipeline, version configurations and apply *enforcement* |
| **Developer (technical reviewer)** | Apply security checklists in PRs and guarantee compliance |
| **Developer**                  | Apply guidelines, run local validations and propose improvements |

---

## ⏱️ When to apply {#️-quando-aplicar}

Secure development is neither a one-off activity nor confined to the end of the process.  
It applies continuously:

- During **planning** (selection of stack, guidelines and dependencies)  
- When **writing or refactoring code** (local validations and static analysis)  
- In every **pull request** (formal reviews, checklists and validation of exceptions)  
- In **continuous integration** (enforcement of rules and automated analysis)  
- Before a **go-live or release** (final validation and review of exceptions)  
- In **maintenance and operation** (patching, dependency updates and periodic review of guidelines)

---

## 🎯 What for {#-para-quê}

- Prevent vulnerabilities at the source  
- Drastically reduce the cost of remediation through early detection  
- Ensure traceability of technical decisions and exceptions  
- Demonstrate compliance in internal and external audits  
- Sustain application security maturity metrics and KPIs  

Ultimately, it is about turning **every line of code** into an opportunity to reinforce confidence in the product.

---

## ⚖️ Proportionality L1–L3 {#️-proporcionalidade-l1l3}

| Risk level | Minimum requirement |
|----------------|------------------|
| **L1 (low)** | Mandatory linters, PR checklist, justified dependencies |
| **L2 (medium)** | Curated guidelines per stack, mandatory SAST, recorded exceptions |
| **L3 (high)**  | Formal governance, dedicated reviewer, *policy-as-code* in CI/CD |

---

## 📜 Relevant Organisational Policies {#-políticas-organizacionais-relevantes}

| Policy                                   | Mandatory | Application             | Minimum content |
|-------------------------------------------|-------------|-----------------------|-----------------|
| [**Guidelines Curation Policy**](/sbd-toe/assets/policies/policy-guidelines-desenvolvimento)   | Yes         | All stacks       | Owners, selection process, *tailoring*, review cycles |
| [**Code Review Policy**](/sbd-toe/assets/policies/policy-revisao-codigo)         | Yes         | Relevant PRs        | Formal checklist, designated reviewer, recorded approval |
| [**Exception Management Policy**](/sbd-toe/assets/policies/policy-gestao-excecoes)        | Yes         | All projects     | Justification, mitigation, deadline and approval proportional to risk |
| [**Development Support Tools Usage Policy**](/sbd-toe/assets/policies/policy-uso-ferramentas-apoio) | Yes | Applicable projects | Usage rules, technical review, legal validation and responsibility |

In the printed version, the relevant policies include: **Guidelines Curation**, **Code Review**, **Exception Management** and **Controlled use of development support tools**.

---
