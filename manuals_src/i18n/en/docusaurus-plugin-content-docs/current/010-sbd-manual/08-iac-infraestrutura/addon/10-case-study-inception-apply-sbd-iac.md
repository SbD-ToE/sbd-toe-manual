---
id: case-study-inception-apply-sbd-iac
title: Case Study – Applying SbD-ToE to an IaC Project
sidebar_position: 10
description: A case study demonstrating the integrated, authorship-independent application of Security in Infrastructure as Code practices throughout the whole lifecycle.
tags: [caso-de-estudo, iac, sbd-toe, aplicacao-pratica, seguranca]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/addon/10-case-study-inception-apply-sbd-iac.md
  source_sha256: c7b998a6a823cfe6ccf0a733d7284339d57ae04d1f82a623fdb82218fa1adfe6
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: fdfbb07dae8ace1a7ee0b20a91e10689f0eaedbe4277ea3ec56bd67330298e26
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [capacitacao, chapter_role, cycle_iteration, lifecycle_phase, mcp_reading_programa, practitioner_manual, programme_line, requirement_runtime, sbdtoe_sbd, threat, traceability, transversal, validation_evaluation]
  glossary_sha256: 513b30381f481a91c0922f722d5e0006cb125329fd8511c706fcb8452156d0dc
  translated_at: 2026-09-26T09:25:39Z
  stamped_at: 2026-09-26T18:34:38Z
  reviewed_by: null
---

# Case Study – Applying SbD-ToE to an Infrastructure as Code Project (IaC)

This case study describes the **practical, integrated and traceable application** of the **Security by Design – Theory of Everything (SbD-ToE)** manual to a real **Infrastructure as Code (IaC)** project.

The objective is not to illustrate tools, authoring styles or creative processes, but to demonstrate **how the prescriptions of Chapter 08 are applied in an objective and verifiable way**, from the *inception* phase through to continuous operation in production.

> **Fundamental note:**  
> This study explicitly assumes that **any IaC code may have been produced wholly or partly with the support of automated tools**, including code generation systems.  
> For that reason, **no trust is placed in the authorship or origin of the code**.  
> All artefacts are treated as **untrusted input until complete technical validation**, in accordance with the SbD-ToE model.

The project analysed defines `dev`, `staging` and `prod` environments for a Kubernetes cluster and its network, identity and observability services. It was classified as **L3 criticality (high)**.

---

## 🧭 Risk classification {#-classificação-de-risco}

The classification was carried out according to **Chapter 01 - Risk Management**, and resulted in **L3**, based on the following factors:

* Ability to directly impact production environments;
* Control of critical resources (network, identity, certificates, logging);
* Cross-cutting effect on multiple applications and teams;
* High potential for operational and reputational impact.

This classification determined the **full application of the requirements, validations and acceptance gates** foreseen for L3 in Chapter 08, regardless of the origin of the code.

---

## 📐 Architecture and repository model {#-arquitetura-e-modelo-de-repositório}

The technical design of the project followed principles of decoupling, segregation and explicit control:

* Terraform as the main declarative tool;
* Modular structure by technical domain;
* Physical separation of repositories:

  * `iac-core` (common modules and policies);
  * `iac-nonprod` (non-production environments);
  * `iac-prod` (production, with reinforced controls);
* Distinct CI/CD pipelines per environment;
* Remote backend with *locking* and encryption (`S3 + DynamoDB + KMS`).

This structure ensures that **no change can be applied without passing through the formal mechanisms of validation, approval and evidence**, regardless of who or what produced the code.

---

## 🔍 Threat Modelling applied to IaC {#-threat-modeling-aplicado-a-iac}

The *threat modelling* was conducted in accordance with **Chapter 03 - Threat Modelling**, treating the IaC project as a **critical asset**.

The main flows and attack surfaces were analysed, explicitly considering scenarios of:

* changes introduced by automation;
* reuse of external modules;
* code generation from templates or suggestions.

The threats identified included:

* **Tampering**: malicious or inadvertent modification of modules or *plans*;
* **Information Disclosure**: exposure of topology, permissions or sensitive *tags*;
* **Repudiation**: changes without evidence or clear accountability;
* **Elevation of Privilege**: excessive IAM permissions introduced by human error or automation.

Each threat was mapped to IaC requirements and the corresponding technical controls in the pipeline.

---

## 🧱 Application of the security requirements {#-aplicação-dos-requisitos-de-segurança}

All the requirements **IAC-001 to IAC-013** were assessed and applied according to the L3 proportionality matrix:

* Remote backend with mandatory *locking*;
* Complete automated validations (`tflint`, `tfsec`, `Checkov`, OPA/Conftest);
* Active *drift detection* (`terraform plan`, `driftctl`, alerts);
* Formal governance of internal and external modules;
* Secrets management via Vault and *workload identity*;
* Full traceability between code, *plan*, *apply* and environment;
* Blocking enforcement of policies in all *pipelines*.

At no point did the acceptance of changes depend on the authorship of the code, but **exclusively on the technical evidence produced**.

---

## 📊 Validation, evidence and audit {#-validação-evidência-e-auditoria}

The validation strategy followed the model defined in **Chapter 10 - Validation**:

* All *Pull Requests* require automated validation and human review;
* Validation reports are archived per environment and *build*;
* Continuous comparison between the approved `plan` and the executed `apply`;
* Exceptions formalised, temporary and approved by AppSec, in accordance with **Chapter 14**.

This model guarantees that **any contribution - human or automated - is subject to the same technical scrutiny**.

---

## 🔐 Integration with CI/CD pipelines {#-integração-com-pipelines-cicd}

The CI/CD pipelines were designed as **control and decision mechanisms**, not merely automation:

* Restrictive *branch protection* and *merge* rules;
* Mandatory execution of `terraform plan` on PRs;
* *Apply* permitted only after explicit approval and validation of artefacts;
* Dedicated and isolated *runners*;
* Signing and hashing of artefacts (`plan`, reports, manifests).

---

## 🎓 Training and upskilling of the team {#-formação-e-capacitação-da-equipa}

Recognising that secure IaC requires specific competences, a **dedicated training programme** was created, covering:

* Requirements of Ch. 02 and of IaC;
* Interpretation of *findings* and real impacts;
* Validation of changes regardless of authorship;
* Management of secrets and identity;
* The complete cycle of validation, evidence and exceptions.

Training became a **prerequisite for write permissions**, reinforcing that **final responsibility is always human**, even when automated support tools exist.

---

## ✅ Conclusion {#-conclusão}

This case study demonstrates that **SbD-ToE applies uniformly and robustly to IaC projects**, assuming by default that **code is not trusted until proven otherwise**.

The approach makes it possible to:

* Neutralise risks introduced by automation or reuse;
* Keep acceptance criteria stable over time;
* Scale secure IaC without relying on implicit trust in people or tools.

> 💡 This study constitutes the **canonical model for applying SbD-ToE to IaC**, valid regardless of the evolution of authoring tools.
