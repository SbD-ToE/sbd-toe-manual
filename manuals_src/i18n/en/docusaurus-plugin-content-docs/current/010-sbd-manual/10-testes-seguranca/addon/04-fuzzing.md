---
id: fuzzing
title: Directed and Random Fuzzing
description: Testing with unexpected or malformed data to discover flaws in parsers, APIs and internal logic.
tags: [fuzzing, testes aleatórios, fuzzers, cobertura, validação]
sidebar_position: 5
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/addon/04-fuzzing.md
  source_sha256: 000fe7676307165a70fd390d38efeedbdc120b3a07eeea6bfde84055c2b2b906
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 20c86911480112f594de3dd76319574915c0232222a67bb1e52eb14e42319927
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 2ffd43fd37c8802a693f5fa1e43a3d3a9df1ca9d5ea898c88f6f405bedc9d687
  glossary_keys: [chapter_role, maturity, validation_evaluation]
  glossary_sha256: 30d34650b8be5c4934ff9df91b0e5cc816877b45b42cd7eacd3d30e4f4079315
  translated_at: 2026-09-26T10:31:27Z
  reviewed_by: null
---


# Security Fuzzing

## 🌟 Objective {#-objetivo}

To discover vulnerabilities and robustness flaws through the **automated, large-scale generation of malformed, unexpected or random inputs**, with the aim of:

- Testing the limits of the application;
- Detecting unhandled exceptions, parsing failures, crashes;
- Reproducing anomalous behaviour or edge cases;
- Validating the application's resilience to inputs outside what is expected.

> Fuzzing is essential for testing “the unexpected” - what planned tests do not cover.

---

## 🔍 What fuzzing is {#-o-que-é-fuzzing}

Fuzzing is a security technique that consists of feeding the application with **randomly or systematically generated inputs**, with the intent of provoking errors, failures or crashes.

Common types:

- **REST API fuzzing** (inputs in JSON, headers, parameters);
- **Fuzzing of binary protocols or structured messages**;
- **File or parser fuzzing** (e.g. XML, PDF, image);
- **Coverage-guided fuzzing** (instrumentation to maximise the paths explored);
- **Mutation-based fuzzing** (variations on known real inputs).

> ⚠️ Fuzzing does not directly identify vulnerabilities - rather, error conditions that **may indicate exploitable weaknesses**.

---

## ⚙️ How to apply {#️-como-aplicar}

1. **Select the target and test context** (e.g. REST endpoint, file, API flow);
2. **Configure the fuzzer with the relevant input types** (structure, types, encoding);
3. **Run fuzzing in an isolated or controlled environment**, with observability (logging, crash dump);
4. **Instrument the application with coverage or exception detection** (optional);
5. **Analyse anomalous or inconsistent behaviour**: unexpected responses, silent failures, crashes;
6. **Report occurrences as robustness findings, with evidence and reproducibility**.

---

## ✅ Good practices {#-boas-práticas}

- Use fuzzing on critical endpoints and external APIs;
- Prioritise rich formats (JSON, XML, JWT) and less validated fields;
- Repeat fuzzing after changes to parsing or input libraries;
- Use tools with coverage feedback for better exploration;
- Integrate fuzzing as a separate stage in the pipeline or in the nightly build;
- Combine with logs, tracing and crash reports for effective analysis.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                       | Strategic relevance                       |
|--------------------------------|----------------------------------------------|
| Chapter 02 - Requirements       | Related to `EX-REQ-309`, `EX-REQ-406`         |
| `02-dast.md`                   | Complements with more unpredictable inputs  |
| `06-cobertura-e-priorizacao.md`| Used in areas with fewer manual tests      |
| Chapter 07 - Secure CI/CD     | Applied in dedicated jobs or parallel environments |
| `08-gestao-findings.md`        | Fuzzing findings may require specialised triage |

*Illustrative identifiers (`EX-…`); they do not correspond to the Ch. 02 Requirements Catalogue.*

---

> 🎲 Fuzzing does not replace planned tests - but it **increases invisible coverage**, detecting flaws that only emerge with out-of-the-ordinary inputs. It is a sign of maturity in the security validation strategy.
