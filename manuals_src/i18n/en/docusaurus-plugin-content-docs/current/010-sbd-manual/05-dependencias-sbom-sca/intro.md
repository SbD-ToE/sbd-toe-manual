---
id: intro
title: Dependencies, SBOM and SCA
description: Principles, practices and controls to guarantee secure dependency management, SBOM generation and automated software composition analysis
tags: [dependencias, sbom, sca, supply-chain, oss, cicd, governance]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/intro.md
  source_sha256: bc10a8ff8316e7f972652f92e3dc7a14f5666e5045bbfc81c5f40c973185b898
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 14200dcf1e2ab340883ab077728b7e39160443a15b3fe6aa3f6e70b48a281fa0
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, avaliacao, basilar, chapter_role, cycle_iteration, framework_source_corpus, lifecycle_phase, papel_suporte, practitioner_manual, provenance, sbdtoe_sbd, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 749b12cdb247975ac61930961662081bfeff314cfe94bc90dda00fa5f06daf06
  translated_at: 2026-09-26T08:45:30Z
  stamped_at: 2026-09-26T18:33:56Z
  reviewed_by: null
---

import ChapterTypeCallout from '@site/src/components/ChapterTypeCallout';

<ChapterTypeCallout kind="operacional" title="Capítulo Operacional">

This chapter is considered **operational** in the *Security by Design - Theory of Everything (SbD-ToE)* model.
Its function is to **apply, automate and validate** the practices defined in the foundational chapters, guaranteeing their continuous and measurable execution.

The operational chapters implement SbD-ToE in specific technical contexts. These chapters translate the foundational prescriptions into practices of **verifiable execution**, promoting the **continuous integration of security** throughout the software lifecycle.

</ChapterTypeCallout>

# Dependencies, SBOM and SCA

The use of **Open Source Software (OSS)** and third-party libraries is common and recommended: it accelerates delivery and avoids reinventing the wheel.  
However, without governance, material risks arise: abandoned components, known CVEs, malicious packages and a lack of visibility over the **supply chain**.

This chapter establishes operational foundations for **secure, traceable and auditable** dependency management, including:
- SBOM updated per build,
- SCA integrated into CI/CD with *gates*,
- governance of exceptions,
- **prohibition of libraries copied manually into the repository**, and
- **update automation with impact assessment** (bots that open PRs when the change is safe and request human intervention when there is impact on the code).

The requirements described here apply to any stack/language.  
They focus on ensuring that:
- every dependency is known, approved and traceable,
- every build produces a complete SBOM,
- vulnerabilities are detected and triaged,
- **updates are automated with impact analysis** (semver, *release notes*, *changelogs*, tests and *static call graphs*),  
- no library enters “by manual copy” outside the *package manager*.

> ⚠️ **Normative note - Limits of the dependency inventory**  
> The SBOM represents the best possible approximation of a system's composition at a given moment, but **does not constitute an absolute truth**.  
> Dependencies may be introduced indirectly or emergently (e.g. tooling, pipelines, code generation, runtime loading).  
> This chapter prescribes explicit practices to **define inventory boundaries, detect deviations and govern unintended dependencies**, ensuring effective control of the software supply chain.

Links to other chapters:
- **Ch. 02 - Security Requirements** (REQ-DEP-xxx),
- **Ch. 07 - Secure CI/CD** (pipelines and gates),
- **Ch. 09 - Containers** (images as supply chain artefacts),
- **Ch. 14 - Governance** (requirements placed on suppliers).

---

## 🧭 What it covers technically {#-o-que-cobre-tecnicamente}

- Secure management of dependencies (OSS, commercial, internal).
- Generation and maintenance of **SBOM** (CycloneDX/SPDX).
- Integration of automated **SCA** into CI/CD.
- Formal process for **exceptions** and risk acceptance.
- **Internal repositories** as the single source of trust.
- **Prohibition of locally copied dependencies** (JS, PHP, DLLs, JARs, etc.).
- **Update automation with impact assessment** (Renovate/Dependabot/similar):
  - automatic PRs when the impact is nil/low (compatible semver *patch*/*minor*, green tests),
  - *handoff* to human intervention when there is impact (major/breaking, changed APIs).

---

## 🧪 Governance pillars {#pilares-de-governação}

1. **Approved internal repositories** as the single source.  
2. **Dependency policy** with approval criteria and *pinning*.  
3. **SBOM per build**, versioned and accessible.  
4. **Automatic SCA with gates** by severity and criticality (L1–L3).  
5. **Formal exceptions** with a deadline and compensating mitigation.  
6. **Periodic audits** to prevent manually copied libraries.  
7. **Update automation with impact assessment** and integration into tests/gates.

---

## ⚙️ How it must be done {#️-como-deve-ser-feito}

- Configure *package managers* to use **only** internal repositories.  
- Generate an **SBOM** on every build (CycloneDX/SPDX); archive it.  
- Integrate **SCA** with automatic blocking for critical CVEs (thresholds per Lx).  
- Formalise **exceptions** (e.g. `excecoes.yaml`) and review them periodically.  
- Enable **update bots** with:
  - analysis of *semver*, *release notes* and *diffs*,
  - execution of tests and validations (CI),
  - **“auto-merge” PRs conditioned** on proven *no-impact*,
  - a “requires-human” label when there is impact on the code (*breaking*).  
- Remove manually copied libraries and replace them with declared dependencies.

---

## 📆 When to apply {#-quando-aplicar}

- **Start**: policy and configuration of internal repositories.  
- **New dependency**: review of origin/licence/maintenance/CVEs.  
- **Build**: generate SBOM + run SCA.  
- **Release**: validate findings and exceptions.  
- **Regular cycle**: update dependencies (bots) and review findings.  
- **Critical CVE**: assess impact and remediate affected versions.

---

## 👥 Who is involved {#-quem-está-envolvido}

| Role/Function       | Main contribution |
|--------------------|----------------------|
| **Developer / Lead** | Adding dependencies, initial triage, *pinning*, fixes |
| **AppSec Engineer**           | Policies, *tuning*, *gates*, exceptions and risk review |
| **DevOps / CI/CD**   | SBOM, SCA, internal repositories, update bots |
| **QA** | Evidence, regression tests, validation of bot PRs |
| **Product Owner**    | *Go/no-go* decision in the face of findings/residual risk |
| **GRC / Management**     | Audit, compliance, evidence retention |

---

## 🎯 What for {#-para-quê}

- Reduce the risk of vulnerable/abandoned components.  
- Guarantee traceability and a rapid response to CVEs.  
- **Accelerate *time‑to‑fix*** with bots that **assess impact**, automate safe PRs and request human intervention when necessary.  
- Avoid hidden risks (manually copied libraries).  
- Comply with SSDF, SLSA, NIS2 and good market practice.

---

## 🧮 Proportional application L1–L3 {#-aplicação-proporcional-l1l3}

| Practice                       | L1 (low)                 | L2 (medium)                                 | L3 (high/crit.)                                  |
|-------------------------------|----------------------------|--------------------------------------------|--------------------------------------------------|
| SBOM                          | Basic per build           | Complete per release                        | Signed + integrity verification            |
| SCA                           | Warning                      | Blocking High/Critical                      | Blocking Medium+                                 |
| Pinning                       | Recommended                | Mandatory                                 | Mandatory + verified provenance            |
| Exceptions                      | Simple                    | Formal + periodic review                 | Formal + executive validation                    |
| Internal repository           | Recommended                | Mandatory                                 | Mandatory + signature/verification              |
| Locally copied libraries   | Prohibited (policy)       | Periodic audit                         | Enforcement in CI/CD                              |
| **Update bots**       | Optional                   | Active with auto‑PR and *no‑impact merge*      | Active + *impact analysis* + *canary* + *gates*  |

---

## 📜 Relevant Organisational Policies {#-políticas-organizacionais-relevantes}

| Policy                          | Mandatory | Application              | Minimum expected content                                  |
|----------------------------------|-------------|------------------------|-----------------------------------------------------------|
| [Dependency Policy](/sbd-toe/assets/policies/policy-dependencias)         | Yes         | All projects      | Approval criteria, *pinning*, external blocking       |
| [SBOM Policy](/sbd-toe/assets/policies/policy-sbom)                 | Yes         | All builds        | CycloneDX/SPDX, versioning, retention                   |
| [CVE Exceptions Policy](/sbd-toe/assets/policies/policy-excecoes-cve)      | Yes         | Critical projects      | Justification, deadline, compensating mitigation              |
| [Dependency Policy — Local Libraries](/sbd-toe/assets/policies/policy-dependencias)   | Yes         | All repositories  | Prohibition of local JS/PHP/DLL/JAR outside a *package manager* |
| [Automatic Dependency Update Policy](/sbd-toe/assets/policies/policy-atualizacao-automatica) | Yes   | L2–L3                   | Active bots, *impact analysis*, *auto‑merge* criteria, human *handoff* |
| [Exception Management Policy](/sbd-toe/assets/policies/policy-gestao-excecoes) | ⚠️ Optional | All projects | Formal process for exceptions to supply chain requirements: justification, deadline and approval |

In the printed version, consult the **Manual's Policies Annex**, where these policies are consolidated across the board.
