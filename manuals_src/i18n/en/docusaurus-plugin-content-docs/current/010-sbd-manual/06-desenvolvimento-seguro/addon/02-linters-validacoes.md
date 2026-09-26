---
id: linters-validacoes
title: Linters and Local Security Validations
sidebar_position: 2
description: Rules and tools for security validation directly in the development environment (pre-commit, IDE, CLI)
tags: [linters, validação, IDE, pre-commit, segurança, automação]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/06-desenvolvimento-seguro/addon/02-linters-validacoes.md
  source_sha256: 3c0e9f5a416c32639a5507c16e125d8791d17d21684da83c6595695b6b9e262d
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 71a7e049ad2bbf095370c54e927266a73a0fe2c34b1baf344dc36d2a18ef5805
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [audit_trail, maturity, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: 4f29de95dbfe1e549a551e5b4292088a48df22f524be090131d6baa0b6585056
  translated_at: 2026-09-26T08:57:09Z
  reviewed_by: null
---

# Linters and Local Security Validations

> 💡 **Practical note**:  
> Most modern languages and frameworks already have **configurable linters and validators** (such as ESLint, Pylint, RuboCop, etc.), many of which include **basic security rules by default**.  
> Tools such as **Semgrep**, **SonarLint** or IDEs such as VSCode and IntelliJ also allow custom policies to be applied.  
> Adopting them reinforces security even before the commit and prevents bad practices from spreading to the main repository.

---

## 📌 Objectives {#-objetivos}

- Ensure that common errors and bad practices are detected before code is submitted.
- Increase the consistency and technical quality of the code produced.
- Automate security validations, reducing exclusive reliance on human review.
- Establish auditable minimum validation criteria before changes are integrated into the repository.

---

This document defines the minimum requirements for **local validation and security linting** that must be present in any active project.

Consistent application of these validations **significantly reduces the introduction of trivial security errors** and improves the traceability of fixes.

---

## 👥 Who should apply it {#-quem-deve-aplicar}

- **All developers** while writing code.
- **Technical leads** when configuring the repository and pipelines.
- **PR reviewers**, ensuring that the linters have been run and passed.

---

## ⏱️ When to apply it {#️-quando-aplicar}

- Before any commit or push.
- When the PR is created (via hook or pipeline).
- During technical reviews.
- Periodically, as part of maintenance tasks.

---

## 🧱 Minimum requirements {#-requisitos-mínimos}

1. **Mandatory local execution of linters with minimum security rules**
   - Must be part of the development flow
   - E.g. ESLint with the `eslint-plugin-security` plugin, Bandit for Python

2. **Validation integrated into the PR via CI/CD**
   - The pipeline must block merges in the event of critical failures
   - Rules must be visible and justifiable

3. **Rules aligned with the internal secure coding guidelines**
   - Linters must reinforce what is defined in `addon/01-boas-praticas-codigo.md`

4. **Versioned and auditable configuration**
   - The `.eslintrc`, `.pylintrc`, `.semgrep.yml` files, etc., must be in the repository
   - Updates must be tracked and justified

---

## 🚨 Common flaws detectable with linters {#-falhas-comuns-detetáveis-com-linters}

- Use of `eval`, `exec`, `innerHTML` without escaping
- Missing verification of mandatory parameters
- Inclusion of dead code, sensitive comments or debugging
- Instances of known vulnerabilities (by CWE) with autofix

---

## ✅ How to validate {#-como-validar}

- Local execution before the commit (`pre-commit`, `make lint`, etc.)
- Automatic execution in build or PR pipelines
- Presence of reports or logs in the PR
- Integration with the IDE and visible alerts during development

---

## 🧾 How to evidence it {#-como-evidenciar}

- Pipeline logs showing the linters being run
- Screenshot or output integrated into the PR
- Versioned linter configuration files
- Validation mark in the PR template (`[x] Linter executado e sem falhas`)

---

## 🔄 Link to other practices {#-ligação-a-outras-práticas}

| Theme                                | Associated file               |
|-------------------------------------|----------------------------------|
| Secure development guidelines | `addon/01-boas-praticas-codigo.md` |
| Validations in the CI/CD pipeline        | `addon/08-validacoes-codigo.md` |
| Justification of exceptions            | `addon/05-excecoes-e-justificacoes.md` |
| Annotation of validations              | `addon/09-anotacoes-evidencia.md` |

---

> 📌 The absence of linting, or running it only optionally, is one of the clearest signs of low technical maturity and latent risk.  
> These practices must be **mandatory, verified and auditable per project**.
