---
id: pre-intro
title: Rationale
description: Why this chapter is exceptional, which sources support the IaC requirements catalogue and how to create/adapt the organisational catalogue
tags: [iac, rationale, requisitos, catálogo, segurança, pipelines, terraform, kubernetes, cloud]
sidebar_position: -1
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/pre-intro.md
  source_sha256: f2ebaf6b454a2878f371136cecab7bb8f2b09f1592fcd398e487030f1191f2cd
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 777a7b41d07c75554a4a0e130cf3ca2d92eed5ae844df988f73fab827e6f4a51
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, discipline, lifecycle_phase, mapping, prescriptive, provenance, requirement_runtime, sbdtoe_sbd, traceability, transversal]
  glossary_sha256: 4edc5cdb478d70dcb2a2a31eea0096704fa575a2b13ff01dfca74a5654b85804
  translated_at: 2026-09-26T09:25:44Z
  reviewed_by: null
---

# Rationale - IaC Requirements Catalogue

## 🧠 Why this chapter is **exceptional** {#-porque-este-capítulo-é-excecional}

This chapter is different from the others.  
While **Ch. 02 - Security Requirements** defines a common base applicable to any software, a **specialised technical catalogue (IaC requirements`)** is presented here, covering risks and controls specific to **Infrastructure as Code (IaC)**.  

This covers aspects such as:  
- state integrity,  
- automatic validations in *plan/apply*,  
- composition of environments,  
- file→resource→environment traceability,  
- enforcement in the pipeline.  

👉 Each IaC requirement gives rise to its **own user story**, allowing exhaustive and auditable coverage, without gaps or ambiguities.

---

## 🔑 Fundamental points of the exceptionality {#-pontos-fundamentais-da-excecionalidade}

### a) Different lifecycle and teams {#a-ciclo-de-vida-e-equipas-diferentes}

**IaC projects have a lifecycle distinct** from application projects.  
Normally:

- **Architecture/Infra/Platform** maintain the IaC, defining clusters, network, permissions, storage, etc.  
- **Application Development Teams** use that infrastructure to put software into production, but do not control its base configuration.

👉 This separation means that the readers of this chapter may differ from those of others: here the focus is on those who build and govern the infrastructure, not only on those who develop applications.

### b) IaC is also software {#b-iac-também-é-software}

Although peculiar, an IaC project **is, at heart, a software project**.  
It must therefore comply with the cross-cutting controls already defined in SbD-ToE:

- Risk classification (Ch. 01)  
- Threat modelling (Ch. 03)  
- Secure pipelines (Ch. 07)  
- Dependency and SBOM management (Ch. 05)  
- Automatic validations (linters, SAST for IaC)  
- Governance and audit (Ch. 14)

⚠️ The difference is that an error in IaC **does not affect just one application**, but all the applications that depend on that infrastructure.  
Hence the rigour: IaC must be treated with the same scientific discipline applied to the code it serves.

---

## 📚 Technical sources underpinning the catalogue {#-fontes-técnicas-que-fundamentam-o-catálogo}

The IaC requirements catalogue is not arbitrary: it results from the synthesis of **normative and market sources**.  
Among them:

- **CIS Benchmarks** (AWS, Azure, GCP, Kubernetes, Docker, Terraform)  
- **Kubernetes** (Pod Security Standards, Network Policies, Admission Control, Audit Logging)  
- **NIST SP 800-53** and **NIST SP 800-190**  
- **Cloud Security Alliance - CCM**  
- **ISO/IEC 27001** (Annex A: change control, least privilege, segregation of duties)  
- **SSDF (NIST 800-218)** and **SLSA** (supply chain)  
- **Market practices** (Terraform, Pulumi, OPA, Sentinel, Kyverno)

---

## 🧩 Relationship with Ch. 02 - Security Requirements {#-relação-com-o-cap-02---requisitos-de-segurança}

- The IaC requirements **complement** the security requirements of Ch. 02.  
- Wherever possible, direct traceability is established:  

| IaC Requirement | Objective | Ch. 02 Mapping | Note |
|---------------|----------|--------------------|------|
| IAC-001 Remote backend with locking | State integrity | SEC-CFG-STATE | Use of S3+DynamoDB+KMS |
| IAC-003 Automatic validations | Avoid bad practices | SEC-VAL-SHIFTLEFT | `tflint`, `tfsec`, `OPA` in PR |
| IAC-007 `plan` review | Formal change control | SEC-CRL-PR | `plan` attached to PR; approval gate |
| IAC-010 Signing/Provenance | Supply chain | SEC-SUPPLY-PROV | Signing + verified provenance |

---

## 🧱 How to adapt the organisational catalogue {#-como-adaptar-o-catálogo-organizacional}

The catalogue published here (`IAC-001` to `IAC-010`) is a **prescriptive baseline**.  
Each organisation must adapt it to its own reality, following a clear methodology:

1. Inventory the *stacks* and *providers* used  
2. Classify risks (L1–L3)  
3. Select applicable requirements  
4. Define thresholds/gates (High/Critical failures block at L2/L3)  
5. Specify expected evidence (logs, `plan`, SBOM, signatures)  
6. Automate validations (linters, policies, provenance)  
7. Govern exceptions (register, deadline, compensations, dual approval at L3)  
8. Audit and improve continuously (scorecards, drift metrics, blocked failures)  

---

## 🧾 Why user stories per requirement {#-porquê-user-stories-por-requisito}

Unlike other chapters, the work here is not limited to macro practices.  
Each IaC requirement becomes its **own user story**, because this:

- Guarantees that no requirement is forgotten  
- Allows direct integration into the backlog (reusable cards)  
- Ensures requirement → evidence → practice traceability  
- Facilitates L1–L3 proportionality requirement by requirement

---

## ⚖️ L1–L3 proportionality (principles applied to IaC) {#️-proporcionalidade-l1l3-princípios-aplicados-a-iac}

| Domain | L1 (low) | L2 (medium) | L3 (critical) |
|---------|------------|------------|--------------|
| Automatic validations | Warning | Block High/Critical | Block Medium+ |
| `plan` approval | Recommended | Mandatory | Mandatory + dual approval |
| Remote backend/state | Recommended | Remote with locking | Remote + monitoring and break-glass |
| Module origin | Pinning recommended | Pinning mandatory | Allowlist + formal review + SBOM |
| Signing/provenance | Recommended | Mandatory | Mandatory + automatic rejection |

---

## 📦 Expected evidence {#-evidências-esperadas}

- Repo structure per environment; `backend.tf`  
- Pipelines with lint/security/policies in PR and main  
- `terraform plan` attached to PR, approved before `apply`  
- Exception register with deadline and compensations  
- SBOM of modules/providers  
- Signatures + provenance (SLSA)  
- Correlated commit→pipeline→apply logs  
- Compliance and drift dashboards  

---

## 🚫 Frequent anti-patterns in IaC {#-anti-padrões-frequentes-em-iac}

Learning from recurring errors is essential.  
Among the most dangerous anti-patterns, the following stand out:

- **Terraform local state without locking** → concurrent corruption  
- **Direct apply to production without an approved plan** → untraceable changes  
- **External modules pinned to a branch (`main`)** → supply chain risk  
- **Absence of network policies/admission control** → expanded attack surfaces  
- **Secrets hardcoded in IaC variables** → accidental exposure  
- **Lack of SBOM/artefact signing** → untrustworthy builds and deploys  

---

## 🏛️ Governance and metrics {#️-governação-e-métricas}

A catalogue is only effective if it is governed and measured.  
The following is recommended:

- **Ownership**: Architecture/Platform + AppSec  
- **Periodic review**: quarterly, of the IaC requirements catalogue  
- **KPIs/KRIs**:  
  - % of PRs with `plan` approved before `apply`  
  - Scanner coverage in IaC  
  - % of pinned/validated modules  
  - No. and average age of active exceptions  
  - Drift detected and time to correction  

---

## 📌 How to read this chapter {#-como-ler-este-capítulo}

1. Read this **Rationale** to understand the exceptionality and methodology.  
2. Proceed to **intro.md** for the framing, roles and policies.  
3. Use **aplicacao-lifecycle.md** for practical integration into the SDLC.  
4. Consult **20-checklist-revisao.md** for operational control.  
5. Review examples and templates in the `addon/` directory.

👉 In summary: **Requirements → User Stories → Evidence → Proportionality → Audit.**  
It is this chain that ensures that IaC is treated with the same scientific rigour as any other critical software artefact.

---
