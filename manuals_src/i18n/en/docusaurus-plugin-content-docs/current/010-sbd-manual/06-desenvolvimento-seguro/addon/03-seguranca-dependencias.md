---
id: seguranca-dependencias
title: Dependency Security
sidebar_position: 3
description: Practices for managing and validating external dependencies to ensure integrity, currency and security in the code
tags: [dependências, segurança, sbom, gestão, validação]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/06-desenvolvimento-seguro/addon/03-seguranca-dependencias.md
  source_sha256: 6f0aca66af2380b30d8d8bb58ffb4c0e8a28e2c41b253ab61baf8a6cd8c50807
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: d24668a8bb37ae4cb4a7dced13f3e6f117b43e672cd14f1075e89641f84728e1
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [avaliacao, practitioner_manual, traceability, validation_evaluation]
  glossary_sha256: 2f3a2d80b5cdd837bb629b1c56c8ead6fb0084a5c6c874375f5aaf0032fc3fba
  translated_at: 2026-09-26T08:57:09Z
  reviewed_by: null
---

# Dependency Security

> 💡 **Practical note**:  
> Tools such as **Snyk**, **OWASP Dependency-Check**, **Sonatype**, **Xygeni**, among others, already make it possible to detect **known vulnerabilities (CVEs)** in libraries and packages used at build, run or test time.  
> These tools are useful for applying a policy of continuous validation and automated enforcement, but they **do not replace the technical team's critical analysis** of the legitimacy, necessity and currency of the dependencies used.

---

## 📌 Objectives {#-objetivos}

- Reduce the risk of exploitation through outdated or compromised libraries.
- Ensure that all dependencies have a technical justification and security validation.
- Establish a traceable process for approval and version control.
- Facilitate the automation of checks (SCA) and blocking in CI/CD.
- Support internal and external audits with evidence of technical control.

---

This document defines the minimum criteria for the secure use of external dependencies (and reused internal ones), ensuring that they are:

- **Validated for known vulnerabilities**
- **Technically legitimised by the team**
- **Up to date and traceable over time**

---

## 👥 Who should apply it {#-quem-deve-aplicar}

- **Developers**: when adding or updating packages.
- **Tech leads / technical reviewers**: when approving PRs with changes to `package.json`, `pom.xml`, `requirements.txt`, etc.
- **Security / AppSec team**: when defining allowlists or approval rules.

---

## ⏱️ When to apply it {#️-quando-aplicar}

- Whenever a dependency is introduced or updated.
- Periodically, by automated means (e.g. nightly scans).
- Before each release or delivery to production.
- During audits or security reviews.

---

## 🧱 Mandatory requirements {#-requisitos-obrigatórios}

1. **CVE validation through SCA (Software Composition Analysis)**
   - Automated scans with alerts and reports per PR or build.
   - Integration with CI/CD.

2. **Approved list (allowlist) and exclusion policy (denylist)**
   - Avoid unaudited, unmaintained or abandoned libraries.
   - Mandatory for projects classified L2/L3.

3. **Explicit technical validation in PRs**
   - Justification for the inclusion.
   - Assessment of the library's maintenance and origin.

4. **Regular package updates**
   - Require updates of obsolete, vulnerable or deprecated packages.
   - Automate alerts per dependency with a known, unmitigated CVE.

5. **Differentiated management of runtime vs. dev/test dependencies**
   - Apply validation proportionate to the risk of exploitation in production.

---

## 🚨 Risk signals {#-sinais-de-risco}

- Libraries without maintenance for more than 1 year.
- Packages with fewer than 10 stars and no official release.
- Scripts or binaries included without validation.
- Private forks without upstream updates.

---

## ✅ How to validate {#-como-validar}

- Automated scans on each commit/PR (`dependency-check`, `snyk test`, etc.).
- Manual approval of each new package.
- Blocking triggers in the pipeline for severe vulnerabilities.
- Review of the dependency's changelog and repository.

---

## 🧾 How to evidence it {#-como-evidenciar}

- Dependency scanner execution logs.
- Versioned `.approved-deps.yml` file or equivalent.
- PR comment with the validation and justification for the new dependency.
- Update history in the repository or package management system.

---

## 🔄 Link to other practices {#-ligação-a-outras-práticas}

| Theme                                    | Associated file               |
|-----------------------------------------|----------------------------------|
| Linters and validations in the pipeline        | `addon/02-linters-validacoes.md` |
| Justification of exceptions                | `addon/05-excecoes-e-justificacoes.md` |
| Validation integrated into code review| `addon/08-validacoes-codigo.md` |
| Traceability in code and PRs         | `addon/09-anotacoes-evidencia.md` |

---

> 📌 The inclusion of insecure dependencies is one of the most common causes of application compromise.  
> The validation process must be systematic, traceable and blocking in critical cases.
