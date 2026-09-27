---
id: seguranca-codigo-pipeline
title: Code Security within the Pipeline
sidebar_position: 2
description: Validations of the pipeline's own code (YAML, scripts, linters), including control of logic, permissions and the use of external components.
tags: [cicd, pipeline, scripts, linters, validação, segurança]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/addon/02-seguranca-codigo-pipeline.md
  source_sha256: 8a628a60c9556fb4445dfa63e78ffb5d0eda89502581f64c41fd4034e9832ade
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 41880e046bb850e6e00a4b4ff44850516c6650a973c059ba45a53afb60399ccc
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, risk_level, traceability, validation_evaluation]
  glossary_sha256: bf1167c6ea7a7473584504ac16943df52d7b2e8a850b0af01b2f398f5d5d0438
  translated_at: 2026-09-26T09:09:13Z
  stamped_at: 2026-09-26T18:34:17Z
  reviewed_by: null
---


# Code security within the pipeline

The security of continuous delivery depends on the ability to **automatically detect insecure code, poor practices or known vulnerabilities** before the build or the deploy. This practice defines the **technical security validation controls to be applied directly within CI/CD pipelines**, in a traceable way and proportional to risk.

> Code must never be promoted without automated security validations that are visible in the pipeline.

---

## 🎯 Objectives {#-objetivos}

- Ensure that **all delivered code has passed automated and consistent security validations**;
- Integrate security testing as a mandatory part of the CI/CD flow;
- Prevent the inclusion of malicious or insecure code, or code with exposed secrets, in builds or releases.

---

## 🛠️ Practices {#️-práticas}

1. **Integration of security testing into the pipeline**  
   - Inclusion of SAST (static analysis) as a mandatory pipeline stage;
   - Regular execution of scanners for *secrets* and hardcoded credentials;
   - Application of security linters (e.g. IaC, containers, internal policies).

2. **Validation against the requirements defined in Chapter 02**  
   - The pipeline must verify whether the code meets the applicable security requirements;
   - L2 and L3 applications must have security *gates* defined as formal criteria.

3. **Automatic rejection of code that violates minimum criteria**  
   - The build must fail if insecure functions, outdated libraries or embedded secrets are detected;
   - There must be explicit approval/rejection criteria (e.g. minimum quality, blocking critical findings).

4. **Preservation and traceability of analysis results**  
   - Test results must be stored and associated with commits, branches or releases;
   - L3 applications must keep a formal history and mechanisms for reviewing findings.

5. **Coverage proportional to risk and to the type of application**  
   - Critical applications must include IaC and SBOM testing, and analysis of dependencies, containers and binaries;
   - Coverage must be documented and revisited regularly.

---

## ⚖️ Proportional application by risk level {#️-aplicação-proporcional-por-nível-de-risco}

| Level | Mandatory requirements                              | Enhanced requirements                                     |
|-------|--------------------------------------------------------|------------------------------------------------------------|
| **L1** | Basic SAST and secrets scanning integrated             | -                                                          |
| **L2** | Build fails if minimum criteria are violated     | IaC linters; analysis of containers and dependencies          |
| **L3** | Formal findings policy; traceability per commit| Full coverage; formal validation with security gates   |

---

## 📌 Practical examples {#-exemplos-práticos}

- **GitHub Actions**  
  - Integration with `CodeQL`, `TruffleHog`, IaC linters;
  - Automatic rejection with `continue-on-error: false`.

- **GitLab**  
  - Integrated security (`SAST`, `Secret Detection`, `Container Scanning`);
  - Export of findings to dashboards and artefacts.

- **Azure DevOps**  
  - SAST/DAST tasks as mandatory stages in `azure-pipelines.yml`;
  - Blocking `quality gates` via extensions (e.g. SonarQube).

- **Jenkins**  
  - Integration with scanners (e.g. SonarQube, Semgrep, detect-secrets);
  - Automatic failure via control policies in the pipeline.

---

## 📉 Mitigated risks {#-riscos-mitigados}

- Inclusion of malicious or insecure code (OSC&R: SC0001, SC0006);
- Builds with undetected known vulnerabilities (OSC&R: SC0008);
- Outdated or compromised dependencies (link with Ch. 05);
- Leakage of hardcoded secrets (OSC&R: CI0010).

---
