---
id: intro
title: Secure CI/CD
description: Security practices for continuous integration and delivery pipelines, with a focus on automation, traceability and control proportional to risk
tags: [cicd, segurança, pipelines, automação, proveniência, devsecops, risco]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/intro.md
  source_sha256: f2448fe805d2081523864b43bd2658679398db2012f5363886c96dcdd3edd9bc
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 958941949ab0ea7b37d0bfc9b2e3ab5737653ce3d6d9df66504371621984a13a
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, basilar, chapter_role, cycle_iteration, deterministic, discipline, framework_source_corpus, lifecycle_phase, mapping, papel_suporte, practitioner_manual, prescriptive, provenance, risk_level, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: c483676ec2b90a6feec1768c15b0452a19247ea70a69564397a8610d3dc059bf
  translated_at: 2026-09-26T09:09:22Z
  stamped_at: 2026-09-26T18:34:28Z
  reviewed_by: null
---

import ChapterTypeCallout from '@site/src/components/ChapterTypeCallout';

<ChapterTypeCallout kind="operacional" title="Capítulo Operacional">

This chapter is considered **operational** in the *Security by Design - Theory of Everything (SbD-ToE)* model.
Its function is to **apply, automate and validate** the practices defined in the foundational chapters, guaranteeing their continuous and measurable execution.

The operational chapters implement SbD-ToE in specific technical contexts. These chapters translate the foundational prescriptions into practices of **verifiable execution**, promoting the **continuous integration of security** throughout the software lifecycle.

</ChapterTypeCallout>

# Secure CI/CD

**Continuous integration and delivery (CI/CD)** pipelines are today the **backbone of software engineering**.  
Through them code flows, artefacts are built, validations are applied and versions are finally promoted to production.  
If a pipeline is compromised, the impact is devastating: **all the applications and services that depend on it inherit that risk**.

This chapter starts from an unequivocal observation: **the security of the pipeline is the security of the product**.  
Protecting the source code or the application runtime is not enough - it is the pipeline that guarantees that everything else reaches production in an intact, auditable and trustworthy form.

For this reason, SbD-ToE establishes here a prescriptive body for pipelines: **how they must be designed, governed and audited to resist attacks, prevent failures and sustain organisational trust**.

> **Canonical note (modern process).**  
> A pipeline may automate execution and produce signals (results, scores, recommendations), but it **does not replace human decision** in irreversible actions (promotion, deploy, gate bypass).  
> Likewise, **plausible outputs do not replace empirical evidence**: evidence means observable execution (logs, *run ids*, *exit codes*, artefacts) and verifiable traceability.

---

## 🧭 What it covers technically {#-o-que-cobre-tecnicamente}

CI/CD security spans a broad set of technical and organisational domains:

- **Definition and versioning of pipelines** (YAML, scripts, templates)  
- **Execution environments**: runners, agents and build containers  
- **Management of secrets and credentials** used in jobs  
- **Integration of security scanners** (SAST, IaC, secrets, containers, SBOM)  
- **Artefact signing and provenance** to guarantee integrity  
- **Promotion policies and gates proportional to risk**  
- **End-to-end traceability** commit → pipeline → release  
- **Reproducibility and operational determinism** sufficient for audit and incident investigation (including recording of the effective configuration used in the execution, without exposing sensitive data)

---

## 📌 What must be done {#-o-que-deve-ser-feito}

For CI/CD pipelines to be trustworthy and auditable, the organisation must:

1. **Harden and isolate runners** per project, application or risk level.  
2. **Integrate automatic scanners** in phases proportional to the expected impact, ensuring that the results correspond to real and observable execution.  
3. **Prohibit static secrets** and replace them with OIDC, short-lived tokens and masked logs.  
4. **Sign and record provenance** of all artefacts and releases, with mandatory validation before promotion.  
5. **Enforce promotion gates** configured by risk classification (L1, L2, L3), keeping an explicit separation between *automatic signal* and *promotion decision*.  
6. **Record exceptions** in a formal, temporary and auditable way, with a defined owner, deadline and compensations.  
7. **Guarantee complete traceability** to support audits and incident response (commit → pipeline execution → artefact → release).  
8. **Minimise context exposure** in logs, intermediate artefacts and external integrations, treating any system outside the organisation's direct control as a dependency and a potential exfiltration channel.

---

## ⚙️ How it must be done {#️-como-deve-ser-feito}

The technical mechanisms that make it possible to implement these practices include:

- Versioning of pipelines in Git repositories with review through PR  
- Use of **ephemeral, unprivileged and segregated** runners  
- Integration of tools such as `semgrep`, `trivy`, `cosign`, `scorecard` and IaC/container scanners  
- Configuration of **OIDC and short TTL** for secrets, eliminating *long-lived* keys  
- Automatic signing of artefacts and provenance in accordance with **SLSA**  
- Structured retention of logs, metadata and commit→pipeline→release correlations  
- Controlled recording of the **effective execution configuration** (without sensitive data), supporting reproducibility and audit  
- Control of logging and *debug* (temporary and auditable activation), preventing exposure of secrets, sensitive data or intellectual property

---

## 📆 When to apply {#-quando-aplicar}

The discipline of Secure CI/CD is not switched on occasionally: it accompanies the whole life of the project.  
It must be applied:

- **From the start of a new pipeline**, even in MVPs  
- **Whenever releases are promoted** to higher environments (in particular when the action is irreversible)  
- **When runners, tooling, gates or secrets are changed**  
- **When any external dependency is integrated** into the pipeline (scanners, services, repos, registries, etc.)  
- **In regular audits**, to ensure traceability, reproducibility and compliance  

---

## 👥 Who is involved {#-quem-está-envolvido}

CI/CD security depends on distinct but complementary roles:

| Role/Function              | Main contribution |
|---------------------------|----------------------|
| **Developer**             | Develop pipelines, react to findings and maintain code quality |
| **DevOps / SRE**          | Harden runners, manage automation and apply operational controls |
| **AppSec Engineer**       | Define policies, scanner thresholds and gates by risk |
| **GRC / Compliance** + **Auditors** | Verify traceability, exceptions and organisational compliance |

---

## 🎯 What for {#-para-quê}

- **Prevent supply chain attacks** exploiting insecure pipelines or runners  
- **Protect critical artefacts**, ensuring that only trustworthy code is promoted  
- **Provide organisational trust**, demonstrating traceability to managers, auditors and regulators  
- **Enable fast and secure releases**, without compromising integrity or compliance  

---

## 📜 Relevant Organisational Policies {#-políticas-organizacionais-relevantes}

| Organisational policy         | Mandatory | Application | Minimum content |
|---------------------------------|-------------|-----------|-----------------|
| [Secure CI/CD Policy](/sbd-toe/assets/policies/policy-cicd-seguro)        | Yes         | All projects | Review through PR, secure runners, mandatory scanners, secrets management, signing/provenance |
| [Secrets Management Policy](/sbd-toe/assets/policies/policy-gestao-segredos)  | Yes         | DevOps / SRE, AppSec Engineer | OIDC/short TTL, prohibition of static secrets, periodic rotation |
| [Traceability Policy](/sbd-toe/assets/policies/policy-rastreabilidade)     | Recommended | GRC / Compliance, Auditors | Correlated commit→pipeline→release logs, minimum retention, immutable export |
| [CI/CD Exception Management Policy](/sbd-toe/assets/policies/policy-gestao-excecoes)      | Yes         | AppSec Engineer, GRC / Compliance | Formal record, approvals, deadline and compensations |
| [Risk-Proportional Application Policy](/sbd-toe/assets/policies/policy-classificacao-risco) | ⚠️ Optional | Organisations with formal classification | Mapping between risk level and minimum controls required in the pipeline |

The relevant organisational policies are described in the **Manual's Policies Annex**, including: Secure CI/CD, Secrets Management, Traceability and Exceptions.

---
