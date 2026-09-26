---
id: cobertura-e-priorizacao
title: Security Test Coverage and Prioritisation
description: Strategies for prioritising tests based on risk and ensuring effective coverage of the requirements.
tags: [cobertura, testes, segurança, priorização, risco]
sidebar_position: 7
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/addon/06-cobertura-e-priorizacao.md
  source_sha256: 33a559bab739050a63da9bd229f1e6eee1731c54da4dcfacc29a74b784e76b42
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: aee19ce4e5cb99c584a1fa462d65fa9bbc5bc6432b4231add9e0931d813e1c6f
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 2ffd43fd37c8802a693f5fa1e43a3d3a9df1ca9d5ea898c88f6f405bedc9d687
  glossary_keys: [chapter_role, framework_source_corpus, risk_level]
  glossary_sha256: d1b1a81ffcc5a6f5428ae7cdbc9447f5c6daf50d21ce00a3f20252d6d71fbfd6
  translated_at: 2026-09-26T10:31:28Z
  reviewed_by: null
---


# Coverage and Prioritisation of Security Testing

## 🌟 Objective {#-objetivo}

To define **which components, functionalities and interfaces must be tested**, **with what depth and frequency**, and **with what type of test**, based on:

- The application's risk level and criticality;
- Frequency of change and external exposure;
- History of previous flaws or findings;
- Security dependencies on other systems.

> Coverage without prioritisation leads to waste. Prioritisation without coverage leads to a false sense of security.

---

## 🔍 What coverage and prioritisation in security are {#-o-que-é-cobertura-e-priorização-em-segurança}

**Coverage** refers to the percentage of the system that is covered by security testing - including:

- Source code;
- APIs and endpoints;
- Functional flows;
- Integrations and dependencies.

**Prioritisation** defines **what to test first or more intensively**, based on:

- Likelihood of exploitation;
- Impact in the event of a flaw;
- Ease of testing;
- Regulatory or reputational risks.

> 💡 A risk x test-frequency matrix helps to operationalise the strategy.

---

## ⚙️ How to apply {#️-como-aplicar}

1. **Map attack surfaces and exposed interfaces** (e.g. public APIs, management panels);
2. **Classify areas by functional criticality and security impact**;
3. **Define a minimum test frequency per risk category** (e.g. monthly for L3, half-yearly for L1);
4. **Flag coverage gaps** (e.g. untested endpoints, uninstrumented code);
5. **Adjust test depth according to the type** (e.g. fuzzing for parsers, DAST for external interfaces);
6. **Review the coverage map periodically with the technical and security teams**.

---

## ✅ Good practices {#-boas-práticas}

- Include security coverage in the quality criteria;
- Track real coverage with metrics (e.g. % of APIs tested);
- Prioritise new, critical or recently changed functionalities;
- Use tagging by component and criticality in the tests;
- Assess the effective coverage of automated tests (not just their presence);
- Validate whether regressions and findings are being reviewed in the highest-risk areas.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                       | Strategic relevance                          |
|--------------------------------|--------------------------------------------------|
| Chapter 01 - Risk Management  | Defines classification and criticality criteria |
| Chapter 02 - Requirements       | Defines what must be validated and why         |
| `01-sast.md` to `04-fuzzing.md` | Test types applicable to prioritised areas   |
| `05-validacao-regressao.md`    | Helps define persistent targets            |
| `08-gestao-findings.md`        | Relates findings to tested or untested areas    |

---

> 🧩 Security test coverage is not binary - it must be **contextual, proportional and oriented to real risk**. Covering what matters is as vital as testing well.
