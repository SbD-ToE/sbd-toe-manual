---
id: validacao-regressao
title: Security Regression Tests
description: Recurring validation of previously fixed vulnerabilities to prevent their reintroduction in future versions.
tags: [regressão, testes, segurança, validação contínua]
sidebar_position: 6
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/addon/05-validacao-regressao.md
  source_sha256: 8629147baa7e4bbf4c18fce3b8e5e3bb0fc8a01ed576501593f2f6e88a05c8ca
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: ea79468d3024ade66b45b84a4eec10f0624fb9a42319e6867fdd0346ac41efb4
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, cycle_iteration, maturity, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: f8a6d2aa8231c9ec11b9cc0c5b4f1fa5c40c71b064259100ef396164e06c0af8
  translated_at: 2026-09-26T10:31:28Z
  stamped_at: 2026-09-26T18:35:07Z
  reviewed_by: null
---


# Security Regression Validation

## 🌟 Objective {#-objetivo}

To ensure that **previously fixed vulnerabilities are not reintroduced** into the code as the application evolves, through systematic mechanisms of **security regression validation**, including:

- Automated re-execution of tests on resolved findings;
- Creation of security test cases from real flaws;
- Integration in the continuous quality cycle (functional + security regression);
- Traceability between historical findings and future builds.

> ⚠️ A security regression represents an **avoidable step backwards** - usually due to a lack of organisational memory or automation.

---

## 🔍 What regression validation is {#-o-que-é-validação-de-regressões}

Security regression validation consists of **detecting accidental reintroductions of known vulnerabilities**, previously fixed, that return to the code through refactoring, branch merges or repetition of mistakes.

Common forms:

- **Re-running SAST with a baseline of previous findings**;
- **Manual or automated test cases with payloads from previous exploits**;
- **Monitoring by hash/signature of reintroduced vulnerable code fragments**;
- **CI blocks dedicated to the validation of critical regressions**.

---

## ⚙️ How to apply {#️-como-aplicar}

1. **Keep a history of resolved findings**, with technical details and the associated commit;
2. **Automate verification of their absence** in future builds (e.g. via hash, SAST rule);
3. **Create specific security tests** for relevant flaws (e.g. previous bypass payloads);
4. **Integrate security regressions in the QA team's functional regression matrix**;
5. **Use tags or annotations on tests** to identify which are regression and security tests;
6. **Report whenever a flaw reappears - with an explicit alert to the module owner**.

> 💡 Suggestion: keep a `/tests/security-regression/` folder in the repository with versioned test cases.

---

## ✅ Good practices {#-boas-práticas}

- Retain all findings with status “Resolved” and the respective fix commit;
- Automate regressions as part of the PR pipeline;
- Create alerts for findings that reappear in later builds;
- Validate regressions especially in shared or legacy code;
- Include regression verification in the acceptance criteria of L2/L3 releases;
- Promote a culture of "zero known regressions" as a maturity practice.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                         | Strategic relevance                        |
|----------------------------------|------------------------------------------------|
| Chapter 02 - Requirements         | Validates requirements with a findings history    |
| `01-sast.md`                     | SAST findings can be the basis for regression |
| `08-gestao-findings.md`          | Keeps the history and status of vulnerabilities |
| `06-cobertura-e-priorizacao.md` | Helps prioritise areas with a higher risk of regression |
| Chapter 07 - Secure CI/CD       | Integration of regressions as pipeline jobs |

---

> 📉 Regression validation protects the investment made in fixing flaws - and prevents old vulnerabilities from coming back to haunt the security of new versions.
