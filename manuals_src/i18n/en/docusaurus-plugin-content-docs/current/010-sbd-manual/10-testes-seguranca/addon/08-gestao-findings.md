---
id: gestao-findings
title: Security Findings Management
description: Process for triaging, prioritising, tracking and resolving vulnerabilities detected in security testing.
tags: [findings, gestão, vulnerabilidades, segurança, rastreabilidade]
sidebar_position: 9
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/addon/08-gestao-findings.md
  source_sha256: 74f92604877f1468dfb998c8a68730c72a49dfb308539540df5df41a47cc2962
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 250884f6a44d644bd73136af672cf3463b90462b81e2807bb25828b6169aa0e8
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 2ffd43fd37c8802a693f5fa1e43a3d3a9df1ca9d5ea898c88f6f405bedc9d687
  glossary_keys: [chapter_role, requirement_runtime, traceability, validation_evaluation]
  glossary_sha256: 6af212a305387ad1d5f9cdb9d61c526df762cfb0aee255e5376f0156048a9835
  translated_at: 2026-09-26T10:31:29Z
  reviewed_by: null
---


# Security Findings Management

## 🌟 Objective {#-objetivo}

To establish an effective and continuous process for managing security findings - that is, **test results that indicate potential vulnerabilities or bad practices**, ensuring:

- Triage by criticality, context and reproducibility;
- Integration with the backlog and development tools;
- Centralised consolidation for prioritisation and traceability;
- Validated handling by owners with organisational memory;
- Reduction of noise and redundancy between validation tools.

> ⚠️ Ignored or scattered findings weaken security. Centralised and tracked findings strengthen it.

---

## 🔍 What security findings are {#-o-que-são-findings-de-segurança}

Findings can result from:

- SAST, DAST, IAST, fuzzing;
- Manual tests or reviews;
- SBOM/SCA tools or organisational policies;
- Runtime monitoring or production alerts.

Each finding represents a **risk observation** that requires a decision:

- Is it true? Is it a false positive?
- Has it been accepted, mitigated or resolved?
- Is it associated with a requirement, release, commit?
- Has it been validated or merely hidden?

> 💡 Findings ≠ CVEs: they are *concrete occurrences* in the context of the application and must be treated as such.

---

## ⚙️ How to apply {#️-como-aplicar}

1. **Centralise all findings in a consolidated system** (e.g. DefectDojo, Jira with plugins, Vulcan, Security Hub);
2. **Create objective triage criteria** (e.g. CWE, OWASP Top 10, organisational risk);
3. **Associate each finding with traceable metadata**: commit, version, module, requirement;
4. **Integrate findings in the team's backlog with a defined status and SLA**;
5. **Establish a formal flow: triaged → accepted → fixed → validated**;
6. **Consolidate data from multiple tools with correlation of duplicates and false positives**.

> 🔐 Centralisation makes it possible to prioritise resources, ensure a response proportional to risk and generate executive visibility.

---

## ✅ Good practices {#-boas-práticas}

- Use platforms such as **DefectDojo**, **Vulcan**, **Security Hub** or integrated solutions for centralisation;
- Classify findings by risk (L1–L3) and adjust the process:
  - **L1**: findings may be triaged directly in the backlog;
  - **L2–L3**: must be centralised, auditable and followed up by AppSec;
- Avoid duplication between tools - establish correlation pipelines;
- Automate the export of findings to triage boards and KPIs;
- Review accepted findings every quarter;
- Integrate dashboards by release, module, team or type of flaw.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                       | Strategic relevance                        |
|--------------------------------|------------------------------------------------|
| Chapter 02 - Requirements       | Validates requirements and enables traceability to the requirement |
| Chapter 06 - Development  | Findings evidence recurring flaws or violation of secure patterns |
| Chapter 07 - Secure CI/CD     | Findings originating in continuous validation jobs |
| `01-sast.md`, `02-dast.md`     | Produce findings that must be triaged       |
| `09-feedback-equipa.md`        | Defines communication mechanisms and ownership   |
| Ch. 14 - `addon/12-processo-excecoes.md` | Findings not resolved within the TST-003 SLA require a formal exception through this process |

---

> 📊 Findings management is a continuous process, not an export file. Its centralisation and rationalisation by risk are the foundation for informed and effective security decisions.
