---
id: iast
title: Interactive Validation with Instrumentation (IAST)
description: Instrumentation of the application for real-time observation of vulnerabilities during execution.
tags: [iast, testes interativos, instrumentação, runtime]
sidebar_position: 4
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/addon/03-iast.md
  source_sha256: 81c88edca96b0a97ec85b9a018a0c789f20bee926cef4cb13d538bd476559ccf
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 562af006f9e4143f2ecb617ec0474617834a92b2fda165a9d025badeb2bf948a
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 2ffd43fd37c8802a693f5fa1e43a3d3a9df1ca9d5ea898c88f6f405bedc9d687
  glossary_keys: [chapter_role, validation_evaluation]
  glossary_sha256: 6e52253d91d1dd36374be7c5a3d7346a9b642a7abc5c2e7b51d25fca8120fb72
  translated_at: 2026-09-26T10:31:26Z
  reviewed_by: null
---


# Interactive Security Testing (IAST)

## 🌟 Objective {#-objetivo}

To leverage the normal execution of the application to perform security testing **with active instrumentation**, combining:

- The precision of SAST with the real context of DAST;
- Continuous monitoring of insecure calls, misuse of libraries, poorly validated variables and other risks;
- The generation of findings directly related to the application's behaviour at runtime;
- Improved coverage without duplicating manual or automated testing effort.

> IAST is ideal for validating security **without the additional effort of creating test cases or dedicated scanners**.

---

## 🔍 What IAST is {#-o-que-é-iast}

IAST (Interactive Application Security Testing) is a security testing approach that uses **instrumentation on the application server** to observe calls, flows and executions in real time - while the application is being used in functional, manual or automated tests.

It makes it possible to:

- Observe unsanitised data propagating to critical functions;
- Verify insecure use of libraries or native APIs;
- Detect vulnerable executions in real time with full visibility of the stack;
- Associate findings with concrete users, calls, routes and parameters.

> 💡 IAST requires integration with the application's runtime, which is easier in stacks such as Java, .NET, Python and Node.

---

## ⚙️ How to apply {#️-como-aplicar}

1. **Select an IAST tool compatible with the application's stack**;
2. **Instrument the staging server with IAST agents** (or configured containers);
3. **Run functional, manual or automated tests while IAST is active**;
4. **Analyse the findings generated in real context - by flow, route, user ID**;
5. **Triage the results and prioritise based on execution and impact**;
6. **Integrate results in continuous improvement cycles (e.g. security backlog)**.

> ⚠️ IAST does not replace DAST or SAST - it acts in a complementary way to maximise visibility.

---

## ✅ Good practices {#-boas-práticas}

- Use IAST in staging or integrated test environments;
- Validate coverage (e.g. endpoints exercised during the test);
- Prioritise findings based on real impact (executed vs potential);
- Review the permissions and the performance impact of the instrumentation;
- Use IAST as a passive observer in QA and integration tests.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                       | Strategic relevance                      |
|--------------------------------|---------------------------------------------|
| Chapter 02 - Requirements       | Validates `EX-REQ-203`, `EX-REQ-307`, `EX-REQ-404`      |
| Chapter 06 - Development  | Observes violations in real time             |
| `01-sast.md`                   | IAST observes flaws that SAST only detects statically |
| `02-dast.md`                   | Complements DAST with visibility into the backend |
| `06-cobertura-e-priorizacao.md`| Measures coverage by real execution            |
| `08-gestao-findings.md`        | IAST findings are highly traceable  |

*Illustrative identifiers (`EX-…`); they do not correspond to the Ch. 02 Requirements Catalogue.*

---

> 🧠 IAST combines code visibility with real execution - making security testing **more relevant, precise and contextualised**, without depending on false positives or assumptions.
