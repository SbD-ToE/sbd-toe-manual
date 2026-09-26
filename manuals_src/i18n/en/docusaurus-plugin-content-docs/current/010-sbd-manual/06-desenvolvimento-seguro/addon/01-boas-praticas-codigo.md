---
id: boas-praticas-codigo
title: Good Practices for Writing Secure Code
sidebar_position: 1
description: Recommendations for writing secure code by language and stack, including prohibited patterns and validated good practices
tags: [desenvolvimento, boas práticas, secure coding, requisitos, segurança]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/06-desenvolvimento-seguro/addon/01-boas-praticas-codigo.md
  source_sha256: ad3f31cb43830f20ba32733b34cebc6f8bad7a0846e55d0d283329ced1743abe
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 4b023b4644a34c8fd109a32f38c3d216f9ab6bce456f20265df30ca9cfcc2315
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [framework_source_corpus, layer, traceability, transversal, validation_evaluation, verification_taxonomy]
  glossary_sha256: 5e41ecdf73c1783b0866398ae987479214d8db09fbd58da058e434482b30181b
  translated_at: 2026-09-26T08:57:08Z
  reviewed_by: null
---


# Good Practices for Writing Secure Code

> 💡 **Practical note**:  
> Many modern static analysis tools and linters - such as ESLint, Pylint, SonarQube, Checkmarx, Semgrep, among others - already include **essential security rules** by default that cover several of the practices described here.  
> These rules can (and should) be **customised, audited and aligned with the organisation's technical context**.  
> Adopting these tools does not remove the need to define these good practices, but it **significantly facilitates their verification and operationalisation.**

---

This document establishes the minimum set of good practices for writing secure code, which must be followed by all development teams and **validated during the development, review and release process**.

These practices must be integrated into the organisation's technical guidelines and code review routines.

---

## 📌 Objectives {#-objetivos}

- Reduce the introduction of common vulnerabilities (e.g. CWE Top 25)
- Increase the readability, maintainability and security of code
- Standardise behaviour across teams
- Integrate security from the very first commit

---

## 👥 Who should apply it {#-quem-deve-aplicar}

- **Developers**: while writing and refactoring code.
- **Technical reviewers** (peer reviewers, tech leads): while analysing PRs.
- **Security / AppSec teams**: as a cross-cutting validation criterion.

---

## ⏱️ When to apply it {#️-quando-aplicar}

- Whenever production source code is started or changed.
- During technical reviews of PRs.
- In internal audits or security reviews.
- During the technical onboarding of new developers.

---

## 🧱 Essential practices {#-práticas-essenciais}

1. **Avoid copying code from the internet without validation**
   - Justify and review copied snippets (StackOverflow, GitHub, etc.)
   - Validate security and licensing

2. **Separate business logic from presentation logic**
   - Minimises the risk of injection (e.g. XSS)
   - Improves testability and security per layer

3. **Avoid code duplication (DRY)**
   - Increases traceability
   - Reduces security inconsistencies

4. **Avoid using dangerous or deprecated functions**
   - E.g. `eval`, `exec`, `system`, `strcpy`, `innerHTML` without sanitisation
   - Replace them with secure alternatives

5. **Use meaningful and expressive names**
   - Increases comprehensibility and reduces logic errors

6. **Keep comments useful and up to date**
   - Outdated comments lead to critical errors

7. **Remove dead or commented-out code before final commits**
   - Obsolete code is a frequent source of security flaws

---

## 🚨 Prohibited practices {#-práticas-proibidas}

- Use of hardcoded *secrets* (e.g. tokens, passwords)
- Inclusion of *debug code* or *console logging* in production
- Direct access to `request` without validation/sanitisation
- Query strings built by concatenation
- Commit of altered dependencies without formal review

---

## ✅ How to validate {#-como-validar}

These practices must be validated through:

- Code review checklists (see `addon/08-validacoes-codigo.md`)
- Automated linters with mandatory minimum rules (see `addon/02-linters-validacoes.md`)
- PRs with mandatory reviewers and semantic annotation (see `addon/09-anotacoes-evidencia.md`)

---

## 🧾 How to evidence it {#-como-evidenciar}

Evidence of the application of these practices may be:

- Presence of an annotation in the code (`@sec:checked`, `@sec:input-validated`)
- Explicit validation in the PR template
- Linter execution logs in the CI/CD
- Inclusion in the technical review report

---

## 🔄 Link to other practices {#-ligação-a-outras-práticas}

| Theme                                 | Associated file         |
|--------------------------------------|----------------------------|
| Linters and automated validations     | `addon/02-linters-validacoes.md` |
| Secure dependency management       | `addon/03-seguranca-dependencias.md` |
| Code reviews with a checklist     | `addon/08-validacoes-codigo.md` |
| Traceability in code            | `addon/09-anotacoes-evidencia.md` |
| Justification of exceptions             | `addon/05-excecoes-e-justificacoes.md` |

---

> 📌 This practice is cross-cutting and must be applied across all of the organisation's technical stacks and languages.
> Its absence undermines the effectiveness of automated validations and leaves the codebase vulnerable to trivial flaws.
