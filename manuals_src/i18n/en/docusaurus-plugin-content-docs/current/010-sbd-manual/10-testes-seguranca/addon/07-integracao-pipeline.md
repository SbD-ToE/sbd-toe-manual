---
id: integracao-pipeline
title: Integrating Tests into the Pipeline
description: Automated execution of security tests as part of CI/CD pipelines, with traceability and thresholds.
tags: [pipeline, integração contínua, testes, rastreabilidade, segurança]
sidebar_position: 8
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/addon/07-integracao-pipeline.md
  source_sha256: c0b060f58d78f53132d228e275f0a5f78c745e88670cf31f831637749f6de2d5
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 9847a4dfc2c7a28106f6f897c6b028db91965f0033eb0b9a0ecddd25859d8503
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 2ffd43fd37c8802a693f5fa1e43a3d3a9df1ca9d5ea898c88f6f405bedc9d687
  glossary_keys: [audit_trail, chapter_role, traceability, validation_evaluation]
  glossary_sha256: 4f7d762dc31caf92a79b7805a0ee8a8c7086fdf47b2ba4871f0a925da986c0d4
  translated_at: 2026-09-26T10:31:29Z
  reviewed_by: null
---


# Integrating Security Testing into the CI/CD Pipeline

## 🌟 Objective {#-objetivo}

To ensure that security tests are **executed automatically and with well-defined criteria** in all relevant CI/CD pipelines, guaranteeing:

- Early detection of flaws and blocking of builds when necessary;
- Traceability between results, artefacts and commits;
- Reinforcement of the security culture as part of the delivery process;
- Fulfilment of regulatory and internal requirements without depending on manual actions.

> Security that is not integrated into the pipeline is invisible - and therefore ineffective.

---

## 🔍 What “integrating tests into the pipeline” means {#-o-que-significa-integrar-testes-no-pipeline}

Integrating tests into the pipeline means **automating the execution of security tests as part of the build, validation, release or deploy process**. It may include:

- Execution of SAST, SCA, DAST, fuzzing, regressions and linters;
- Generation of SBOMs and security coverage analysis;
- Validation of findings, thresholds and gates by severity;
- Production of traceable artefacts with validation evidence.

---

## ⚙️ How to apply {#️-como-aplicar}

1. **Map the pipeline stages where each type of test must take place**:
   - Pre-build (linters, SBOM);
   - Build (SAST, SCA);
   - Staging (DAST, IAST, fuzzing);
   - Release (final validation and regressions);
2. **Create specific security jobs, with visible and versioned output**;
3. **Define gates and blocking criteria by severity, type of flaw or absence of validation**;
4. **Include metadata in the build artefacts** (e.g. commit, environment, tool version, hash);
5. **Ensure isolation of the test environments**, especially for fuzzing and DAST;
6. **Run security tests in parallel, without affecting total delivery time**.

> 💡 Tests such as SAST and regression may be blocking; tests such as DAST and fuzzing may be informative in asynchronous pipelines.

---

## ✅ Good practices {#-boas-práticas}

- Create pipelines dedicated to security, when possible (e.g. nightly or post-release);
- Keep a history of executions and results per commit, branch and release;
- Integrate findings with the backlog or triage system (Jira, Azure Boards);
- Ensure that tools are versioned and controlled as dependencies;
- Validate the real coverage and frequency of the tests in the pipeline (not just the presence of the jobs);
- Involve DevOps teams in orchestration and continuous maintenance.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                       | Strategic relevance                          |
|--------------------------------|--------------------------------------------------|
| Chapter 07 - Secure CI/CD     | Conditions for secure execution and segregation       |
| `01-sast.md`, `02-dast.md`     | Test types that must be automated       |
| `06-cobertura-e-priorizacao.md`| Defines what, when and how to test in the pipeline   |
| `08-gestao-findings.md`        | Ensures effective handling of the results         |
| Chapter 12 - Monitoring and Operations    | Tracking of security failures at runtime       |

---

> 📦 Integrating tests into the pipeline turns security into a **continuous, auditable and verifiable activity** - instead of a one-off checklist before delivery.
