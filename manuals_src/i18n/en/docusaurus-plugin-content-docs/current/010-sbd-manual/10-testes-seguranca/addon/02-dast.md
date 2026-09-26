---
id: dast
title: Dynamic Application Validation (DAST)
description: Dynamic testing at runtime to detect vulnerabilities by simulating external interactions.
tags: [dast, testes dinâmicos, runtime, segurança]
sidebar_position: 3
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/addon/02-dast.md
  source_sha256: 43d4682bf9d11f0d50123993fd14b0e8bcfc197028a839343099aff02573e168
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: dec3b25086c3bf00ce6aedd820b95c3ec818f5aa7952a7a722e7168ebc4519ca
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 2ffd43fd37c8802a693f5fa1e43a3d3a9df1ca9d5ea898c88f6f405bedc9d687
  glossary_keys: [chapter_role, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: 6368d04ebe07c9227ce26c3b1aef3b28a1b6e58d5b952ecaa88c19810b0091e4
  translated_at: 2026-09-26T10:31:26Z
  reviewed_by: null
---


# Dynamic Security Testing (DAST)

## 🌟 Objective {#-objetivo}

To detect vulnerabilities in applications **while they are running**, simulating the behaviour of a user or an attacker, with the aim of:

- Identifying flaws that are not visible in the code (e.g. injections, authentication bypass);
- Validating the real configuration of the environment (e.g. headers, permissions, exposure of services);
- Testing complete flows and interactions with the running application;
- Complementing static testing (SAST) with runtime visibility.

> DAST is essential for testing what is only revealed when the application is actually running.

---

## 🔍 What DAST is {#-o-que-é-dast}

DAST (Dynamic Application Security Testing) consists of running automated security tests **against a running application** (usually in staging or in controlled environments), simulating malicious or erroneous external behaviour.

It may include:

- Injection attacks (SQLi, XSS, command injection);
- Manipulation of sessions, cookies and authentication;
- Exploitation of public endpoints or APIs;
- Verification of security headers (e.g. CSP, HSTS, CORS);
- Tests of multi-step workflows.

> ⚠️ DAST requires a runnable environment and configured authentication to simulate real users.

---

## ⚙️ How to apply {#️-como-aplicar}

1. **Prepare an isolated staging or pre-production environment**, with controlled data;
2. **Select a DAST scanner suited to the application type** (web, API, mobile);
3. **Configure authentication, scope and appropriate crawling**;
4. **Run regular scans per version or per release**;
5. **Review findings manually before triggering remediation actions**;
6. **Integrate results in the backlog, with traceability by artefact or release**.

> 💡 Suggestion: define distinct scan profiles per application type (e.g. portal vs REST API).

---

## ✅ Good practices {#-boas-práticas}

- Automate DAST execution in the pipeline, but outside the critical path (e.g. a validation environment);
- Use fictitious or masked data;
- Avoid destructive tests in shared environments;
- Configure timeouts, multi-user authentication and session fallback;
- Review scan scopes after changes to the architecture or routes;
- Include APIs and external integration points.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                       | Strategic relevance                     |
|--------------------------------|--------------------------------------------|
| Chapter 02 - Requirements       | Validates `EX-REQ-208`, `EX-REQ-310`, `EX-REQ-405`     |
| Chapter 07 - Secure CI/CD     | Integration with parallel pipelines         |
| `04-fuzzing.md`                | Complements dynamic validation with randomness |
| `06-cobertura-e-priorizacao.md`| Defines the criticality of the endpoints to be tested   |
| `08-gestao-findings.md`        | Management of results and follow-up          |
| `09-feedback-equipa.md`        | Involvement of the QA and DevOps teams    |

*Illustrative identifiers (`EX-…`); they do not correspond to the Ch. 02 Requirements Catalogue.*

---

> 🔍 DAST sees what the code hides: integration flaws, unexpected responses and risks arising from the real execution environment. It is the external lens on application security.
