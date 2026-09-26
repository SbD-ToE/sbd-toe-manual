---
id: analise-sca
title: Vulnerability Analysis of Dependencies (SCA)
description: Software Composition Analysis practices to detect, prioritise and mitigate known vulnerabilities
tags: [dependencias, sbom, sca, supply-chain]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/addon/02-analise-sca.md
  source_sha256: 7242e429e3e38a9d30a64094f919516cb69c128fa01d238f3983cce3de5d83c4
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 735f4aa6791f3488861fde22d0a31138b09209abd3cdff0903e992cb938e0c51
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [cycle_iteration, framework_source_corpus, lifecycle_phase, sbdtoe_sbd, traceability, verificacao_check, verification_taxonomy]
  glossary_sha256: 4f783b58351228abe406e014b9135874758d03a9346fe70bd3fbdebcb8f4f27d
  translated_at: 2026-09-26T08:45:22Z
  stamped_at: 2026-09-26T18:33:46Z
  reviewed_by: null
---

# Vulnerability Analysis of Dependencies (SCA)

## 🌟 Objective {#-objetivo}

Ensure that all external dependencies (direct and transitive) are analysed automatically and on a recurring basis for **known vulnerabilities**, with traceability between:

- Component identified in the SBOM
- Associated vulnerability (CVE)
- Affected artefact and version
- Fix, exception or mitigation task

> The SCA process is essential to reduce the risk associated with reusing third-party libraries and packages.

---

## 🚀 How the SCA process works {#-como-funciona-o-processo-de-sca}

1. The generated SBOM is used as input for the scanner.
2. Each component is compared against vulnerability databases (NVD, GitHub Advisories, OSV, etc.).
3. For each CVE found, the following are identified:
   - Severity (CVSS base score or equivalent)
   - Exploitation vector (local, remote, etc.)
   - Patch / fix status
4. A **processable report** is generated (e.g. JSON, HTML, SARIF) and, where applicable, the pipeline is blocked.

---

## 🤖 Recommended open source tools {#-ferramentas-open-source-recomendadas}

| Tool     | Languages / Support           | Remarks                             |
|----------------|-------------------------------|--------------------------------------------|
| **Syft**       | Multi-stack (Node, Java, etc.) | Generates the SBOM + integrates with Grype              |
| **Grype**      | Multi-stack                    | Vulnerability scanner with OSV/NVD    |
| **Trivy**      | Apps, containers, IaC          | SCA + SAST + secret scanning               |
| **OWASP DC**   | Java/Maven/Gradle              | OWASP Dependency-Check, well supported      |
| **OSV-Scanner**| Node, Go, Rust, Python         | Uses the OSV.dev database, integrates with GitHub       |

> 💡 Syft + Grype is a particularly effective combination for modern pipelines.

---

## 💳 Commercial tools with broader coverage {#-ferramentas-comerciais-com-cobertura-alargada}

| Tool       | Highlights relevant to SbD-ToE                               |
|------------------|--------------------------------------------------------------------|
| **Snyk**          | SCA, IaC scanning, CI/CD integration, policy enforcement          |
| **GitHub Advanced Security** | CodeQL + SCA + Secret scanning integrated into the repository     |
| **Jfrog Xray**    | Repositories, SCA, container scanning, centralised SBOM           |
| **WhiteSource (Mend)** | Licences, risks, policies, centralised alerts                |
| **Checkmarx One** | SAST, SCA, IaC, API Security with integration per language and pipeline |

> These tools may be justified in regulated environments or where there are large volumes of projects.

---

## 🌐 Integration into the lifecycle {#-integração-no-ciclo-de-vida}

| Moment                          | Expected action                            | Result                           |
|----------------------------------|--------------------------------------|-------------------------------------|
| 📁 Build                  | SCA scanner run with the SBOM as input | Report + build status         |
| 📑 Pull Request           | Alerts visible and findings triaged        | Conditional approval or blocking |
| ✅ Release                     | Verification of pending findings         | Go/no-go                            |
| 🚨 Vuln. disclosed       | Notification, triage and associated fix   | Issue/ticket with traceability    |

---

## ⚠️ Prioritising findings {#️-priorizando-findings}

Findings must be triaged on the basis of:

- **Severity**: CVSS > 7.0 = Critical
- **Exposure**: Is the application public? Is the affected function reachable?
- **Impact**: Are sensitive data or critical actions involved?
- **Alternative mitigation**: Is there a documented compensating control?
- **Fix available?**: Does a fixed version exist?

> Findings with no plausible exploitation **must not be ignored**, but classified as "accepted" on the basis of justified risk.

---

## 🔗 Link to the backlog and traceability {#-ligação-com-backlog-e-rastreabilidade}

| Element                     | Recommended form                            |
|-----------------------------|-----------------------------------------------|
| Finding (e.g. CVE-2023-1234) | Create an issue with a reference to the SBOM/component |
| Status                      | "Pending", "Fixed", "Accepted w/ justification" |
| Tags                        | `sca`, `vuln`, `sbom`, `seguranca`, `cve`     |
| Evidence of the fix         | PR, commit, release, updated artefact     |

> 💡 A dashboard per project is suggested, with the status of active findings + a link to the associated task.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                   | Link with SCA                                |
|-----------------------------|-----------------------------------------------|
| `01-inventario-sbom.md`     | Source of the components to analyse               |
| `04-integracao-ci-cd.md`    | Automated execution in the pipeline              |
| `08-rastreabilidade-vulnerabilidades.md` | Mapping between finding, action and release |

---

> 🔎 SCA analysis must be **documented, automated and prioritised**, integrating with backlog tools, code repositories and release artefacts.
