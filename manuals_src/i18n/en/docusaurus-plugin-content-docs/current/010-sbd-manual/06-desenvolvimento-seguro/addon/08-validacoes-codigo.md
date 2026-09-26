---
id: validacoes-codigo
title: Security Validations in Code
sidebar_position: 8
description: Techniques and tools to ensure the presence of security controls directly in source code
tags: [validação, código, segurança, automação, integração contínua]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/06-desenvolvimento-seguro/addon/08-validacoes-codigo.md
  source_sha256: c3b100cef6e2c56a908fa332ae846419e0b803a6ddfc1d1d1b524717d876bf5d
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 46fce18ad4172ee0eb324b439c10ea68bb9fa007148d245d222de4aeece3edc8
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [framework_source_corpus, maturity, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: 3628362336fe534e6e124d25b020cbb9cd94f46487bf13e409501a49dacc0343
  translated_at: 2026-09-26T08:57:12Z
  reviewed_by: null
---


# Security Validations in Code

> 💡 **Practical note**:  
> Tools such as **SonarQube**, **Checkmarx**, **Kiuwan**, **Semgrep**, **Xygeni**, **Fortify** and others make it possible to run security validations directly on the code, during development, in PRs or in CI/CD pipelines.  
> These automated validations complement human review and must be **configured with mandatory minimum criteria per project**.  
> Their effectiveness depends on **integration with review practices, technical onboarding and exception control**.

---

## 📌 Objectives {#-objetivos}

- Identify vulnerabilities in source code before delivery.
- Automate repetitive verifications and detect trivial flaws consistently.
- Support the review process with objective and traceable criteria.
- Increase the team's maturity in detecting and responding to security problems.

---

## 👥 Who should apply it {#-quem-deve-aplicar}

- **Developers**: when writing and validating code locally.
- **Technical reviewers**: when approving code and releases.
- **Security team**: when defining rules, metrics and severity.

---

## ⏱️ When to apply it {#️-quando-aplicar}

- During development (locally or via the IDE)
- When submitting a pull request
- Before each release (via CI/CD)
- In internal audits or certified deliveries

---

## 🧱 Mandatory requirements {#-requisitos-obrigatórios}

1. **Mandatory automated validations with SAST tools**
   - Must run on each PR or commit.
   - The result must be visible and traceable.

2. **Blocking on critical or unjustified failures**
   - High-severity CWE must prevent a merge without an approved exception.

3. **Integration with PR templates**
   - Indicate whether validation was run, which tool was used, and whether there are pending findings.

4. **Definition of minimum criteria by severity**
   - E.g. reject code with "High" findings, allow "Low" with an annotation.

5. **Traceability of fixed, accepted or justified findings**
   - Findings must have a justification or a clear status (accepted, false positive, mitigated).

---

## ✅ How to validate {#-como-validar}

- Reports generated automatically in the CI/CD or in PRs.
- Review checklists with reference to findings and their resolution.
- Explicit marking in affected files or comments in the PR.
- Links to scan evidence (e.g. Semgrep output, Kiuwan report, SonarQube dashboard).

---

## 🧾 How to evidence it {#-como-evidenciar}

- Archived logs from SAST/SCA tools.
- PR annotation with findings + resolution.
- Per-release report with metrics on critical findings resolved vs. justified.
- Verification scripts used in the versioned pipelines.

---

## 🔄 Link to other practices {#-ligação-a-outras-práticas}

| Theme                                | Associated file               |
|-------------------------------------|----------------------------------|
| Linters and local validations         | `addon/02-linters-validacoes.md` |
| Justification of exceptions            | `addon/05-excecoes-e-justificacoes.md` |
| Traceability and evidence         | `addon/09-anotacoes-evidencia.md` |
| Team guidelines                | `addon/07-guidelines-equipa.md` |

---

> 📌 Automated code validation is one of the pillars of technical maturity in secure development.  
> It must be treated as a mandatory stage of the SDLC, with clear criteria, objective evidence and integration with review processes.
