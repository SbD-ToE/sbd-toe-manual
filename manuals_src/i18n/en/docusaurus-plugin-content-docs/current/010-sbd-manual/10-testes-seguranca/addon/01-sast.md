---
id: sast
title: Static Code Validation (SAST)
description: Application of static testing to source code for early detection of vulnerabilities and security flaws.
tags: [sast, validação, segurança, código, análise estática]
sidebar_position: 2
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/addon/01-sast.md
  source_sha256: 30f27f67b6c3971f37a7197f05627dc519b66598dd8c227f2b6206f230b3333f
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: 8a39ef1b682b3b367cc0db070174cfcfec57ae55db7cb68e3649c10030b3d022
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [chapter_role, cycle_iteration, framework_source_corpus, traceability, validation_evaluation]
  glossary_sha256: 6b8cdfef9b4ed0cbf3bc040622d75708c85c90ecc2cf94fb95dbf43082f9ab28
  translated_at: 2026-09-26T12:48:49Z
  reviewed_by: null
---

# Static Security Testing (SAST)

## 🌟 Objective {#-objetivo}

To detect security vulnerabilities in **source code** before the application runs, through **automated static analysis**, ensuring:

- Early and continuous feedback to development teams;
- Traceability between code, findings and security requirements;
- Automated integration with the development cycle and CI/CD;
- Risk reduction without impact on productivity.

> SAST is the foundation of shift-left validation - it detects flaws without the need to run the application.

---

## 🔍 What SAST is {#-o-que-é-sast}

SAST (Static Application Security Testing) analyses **source code or bytecode** to identify dangerous patterns, bad practices, logic flaws and potential vulnerabilities - without running the application.

It can be performed by:

- Language tooling (linters with security rules);
- Generic scanners (e.g. commercial tools);
- Configurable semantic engines (e.g. with custom rules).

> ⚠️ SAST is complementary to dynamic and manual testing - it does not replace runtime validation.

---

## ⚙️ How to apply {#️-como-aplicar}

1. **Select the appropriate tool** per stack (e.g. Node, Java, .NET, Python);
2. **Define minimum acceptance rules and thresholds** (e.g. critical flaws block the build);
3. **Run automatically on every pull request and build pipeline**;
4. **Emit findings with traceability by line of code and commit**;
5. **Maintain a baseline of accepted findings vs new findings**;
6. **Document exceptions and justify false positives**, with AppSec follow-up.

> 💡 Suggestion: use tags on findings to associate requirements (e.g. `EX-REQ-205` — illustrative identifier; it does not correspond to the Ch. 02 Requirements Catalogue) and mitigations.

---

## ✅ Good practices {#-boas-práticas}

- Run SAST locally (pre-commit) and in the pipeline (CI);
- Tune rules to reduce false positives and noise;
- Establish a clear policy of blocking findings by severity;
- Integrate with the backlog (e.g. Jira, Azure Boards) for triage and management;
- Validate the coverage of the analysis (e.g. ignored files, exclusions);
- Reassess configurations with each technological evolution.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                       | Relationship with SAST                            |
|--------------------------------|-----------------------------------------------|
| Chapter 02 - Requirements       | Validates `EX-REQ-203`, `EX-REQ-205`, `EX-REQ-303`        |
| Chapter 06 - Development  | Reinforces secure coding practices             |
| Chapter 07 - Secure CI/CD     | See `07-validacoes-seguranca-integradas.md`             |
| `06-cobertura-e-priorizacao.md`| Defines analysis targets and priorities       |
| `08-gestao-findings.md`        | Ensures effective handling of the results      |
| `09-feedback-equipa.md`        | Involvement of the teams in validation         |

*Illustrative identifiers (`EX-…`); they do not correspond to the Ch. 02 Requirements Catalogue.*

---

> 🔒 SAST reduces the cost of fixing vulnerabilities by acting before execution - but it is only effective when configured with judgement, kept up to date and managed together with the developers.
