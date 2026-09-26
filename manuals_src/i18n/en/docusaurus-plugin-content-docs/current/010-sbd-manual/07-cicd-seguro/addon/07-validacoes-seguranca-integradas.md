---
id: validacoes-seguranca-integradas
title: Security Validations Integrated into the Pipeline
sidebar_position: 7
description: Integration of security validators (SAST, secrets, IaC, containers) directly into the pipeline, with mandatory execution.
tags: [cicd, validações, sast, segurança, scanner, automação]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/addon/07-validacoes-seguranca-integradas.md
  source_sha256: f4e44ca7c79e946cba1358972eca368e6e18327af7bb3b8083294d4475e480a0
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 6e9b61ee40b33b9727a3b5dde82230a92304299487f99adc08f006379b4ca4d3
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [cycle_iteration, framework_source_corpus, practitioner_manual, risk_level, validation_evaluation]
  glossary_sha256: 9f74f12fb1e48d3268e2d0ac10904fb90a2b73aca434dd6e263a06cbd24336c3
  translated_at: 2026-09-26T09:09:16Z
  reviewed_by: null
---


# Security validations integrated into the pipeline

Integrating security validations directly into pipelines makes it possible to **detect vulnerabilities early**, automate controls and ensure that continuous delivery respects the defined security requirements.

These validations must be proportional to the risk level of the application, but **systematic, objective and auditable** in all projects.

> The absence of integrated validations turns the pipeline into a vector for propagating risk.

---

## 🎯 Objectives {#-objetivos}

- Integrate security as a natural and automated part of the integration and delivery cycle;
- Ensure consistent coverage of tests and scanners, proportional to the type and criticality of the application;
- Automate decisions based on objective security criteria (e.g. severity of findings).

---

## 🛠️ Practices {#️-práticas}

1. **SAST - Static Application Security Testing**  
   - Analysis of source code to detect insecure patterns, poor practices or dangerous functions;
   - It must include application code and configuration code (e.g. YAML, JSON, Dockerfile).

2. **Secrets detection**  
   - Scanners for hardcoded secrets or exposed tokens;
   - They must be applied to all branches and commits.

3. **IaC scanning (Infrastructure as Code)**  
   - Validation of Terraform, CloudFormation, etc. files;
   - Detection of excessive permissions, dangerous configurations or insecure resources.

4. **Container security scanning**  
   - Analysis of the Docker images used or generated during the pipeline;
   - Identification of CVEs in base layers, binaries and libraries.

5. **DAST - Dynamic Application Security Testing**  
   - Dynamic testing of already-deployed applications (e.g. staging);
   - It should preferably be carried out in isolated environments.

6. **SBOM + Dependency Analysis**  
   - Generation of SBOMs (Software Bill of Materials);
   - Validation of vulnerable dependencies based on CVEs/NVD, OSS Index, etc.

7. **Enforcement of acceptance criteria**  
   - Application of an automated policy based on security findings:  
     - Maximum permitted severity;  
     - Findings accepted manually (with justification);  
     - Total number of findings by type.

---

## ⚖️ Proportional application by risk level {#️-aplicação-proporcional-por-nível-de-risco}

| Level | Mandatory validations             | Enhanced validations                                |
|-------|--------------------------------------|------------------------------------------------------|
| **L1** | SAST + secrets detection             | -                                                    |
| **L2** | IaC scanning, SBOM, CVE analysis     | Container scanning                                   |
| **L3** | DAST, enforcement of findings, automated policies | Fuzzing, semantic analysis, assisted manual review |

---

## 📌 Practical examples {#-exemplos-práticos}

- **GitHub Actions**  
  - Integration with `CodeQL`, `TruffleHog`, `checkov`, `grype`;  
  - SBOM with `cyclonedx-action`; enforcement with `scorecard-action`.

- **GitLab CI**  
  - Predefined templates: `security-sast`, `secret-detection`, `container-scanning`;  
  - Enforcement via the `Security Dashboard` and approval rules on the Merge Request.

- **Azure DevOps**  
  - Integration with tools such as SonarQube, Checkmarx, WhiteSource;  
  - Mandatory security tasks in the pipeline, with defined quality gates.

- **Jenkins**  
  - Scanners executed via stages (`semgrep`, `trivy`, `syft`);  
  - Enforcement blocks with `if (!pass) { error("blocked") }`.

---

## 📉 Mitigated risks {#-riscos-mitigados}

- Inclusion of vulnerable code or insecure libraries (OSC&R: CI0001, SC0007);
- Deploy of applications without minimum validations (OSC&R: CI0014);
- Concealment, underestimation or omission of critical findings in production.

---
