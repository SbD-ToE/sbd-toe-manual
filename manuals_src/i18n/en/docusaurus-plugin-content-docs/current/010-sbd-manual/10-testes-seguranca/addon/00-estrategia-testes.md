---
id: estrategia-testes
title: Continuous Security Validation
description: Strategies and practices for continuously validating application security through automated, manual and offensive testing.
tags: [testes, segurança, validação contínua, SAST, DAST, fuzzing, pentesting, DSOMM, SAMM, SSDF, SLSA]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/addon/00-estrategia-testes.md
  source_sha256: dc6f642249ec1cfd1880abda011794892d3218355703d812aa2ed1fb889ba5a9
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: fe26962514366823724466b5c37ab33d73897551f1d14dfa4b99e56bae8d0e06
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 2ffd43fd37c8802a693f5fa1e43a3d3a9df1ca9d5ea898c88f6f405bedc9d687
  glossary_keys: [avaliacao, chapter_role, cycle_iteration, framework_source_corpus, lifecycle_phase, mapping, maturity, practitioner_manual, risk_level, validation_evaluation, verification_taxonomy]
  glossary_sha256: 0a627f186e4340eb669e88d8c7f744bc76e8f1e22a75a57a466df0d1606db496
  translated_at: 2026-09-26T10:31:25Z
  reviewed_by: null
---


# Security Testing Strategy across the Lifecycle

## 🌟 Objective {#-objetivo}

To establish an **integrated and proportional strategy** for applying security testing throughout the software development lifecycle (SDLC), ensuring that:

- The right tests are applied at the right time;
- The depth and frequency of testing are aligned with the application's risk;
- Teams understand the purpose and complementarity of each type of test;
- The strategy can evolve with the organisation's maturity.

> An effective strategy avoids both **false confidence** (an excess of tools without real coverage) and a **validation deficit** (untested assumptions).

---

## 🔍 What a security testing strategy is {#-o-que-é-uma-estratégia-de-testes-de-segurança}

A security testing strategy defines:

- **When** to test (e.g. by SDLC phase: coding, build, staging, production);
- **What** to test (e.g. source code, binaries, APIs, business flows);
- **How** to test (e.g. static, dynamic, interactive, fuzzing, manual);
- **Who** is responsible for interpreting results and responding;
- **How often** (e.g. continuously, per release, by risk);
- **Acceptance criteria** and minimum thresholds per type of test.

---

## 🧬 SDLC → Testing Mapping {#-mapeamento-sdlc--testes}

| SDLC phase        | Recommended test types                            | Main objective                    |
|---------------------|----------------------------------------------------------|----------------------------------------|
| Planning         | Threat modelling, requirements review                  | Prevention and coverage                  |
| Development     | Linters, SAST, IAST                                     | Early detection in code             |
| Build/CI            | SAST, SCA, regression tests, SBOM generation         | Continuous validation                     |
| Staging/Testing      | DAST, Fuzzing, IAST, manual validation                 | Assessment of real behaviour        |
| Production/Operation   | Monitoring, sample-based validation, pentest       | Post-deploy verification                 |

---

## 🛠️ How to apply in practice {#️-como-aplicar-na-prática}

1. **Classify the application's risk (L1–L2–L3)** according to Chapter 01;
2. **Select the appropriate test types** for the risk level:
   - L1: Linters + SAST + basic manual tests;
   - L2: Addition of DAST, security regression, IAST;
   - L3: Full pipeline with fuzzing, coverage per API type, differential tests;
3. **Integrate tests in the pipeline** with gates, thresholds and traceable artefacts;
4. **Document the testing strategy** in the repository/project (e.g. a `SECURITY-TESTS.md` file);
5. **Regularly assess the effectiveness of the tests** based on real findings and incidents.

---

## ✅ Good practices {#-boas-práticas}

- **Apply shift-left testing** whenever possible (e.g. SAST on the PR);
- Define **clear approval criteria** (e.g. minimum coverage, 0 critical findings);
- Adopt **risk vs test-type matrices** for each repository or product;
- Review the strategy periodically with the AppSec team;
- Include **feedback from the tests** in the backlog and in continuous improvement processes.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                       | Strategic relevance                         |
|----------------------------------|------------------------------------------------|
| `01-sast.md`                     | Essential part of the start of the strategy        |
| `02-dast.md`                     | Dynamic validation - depends on the context       |
| `06-cobertura-e-priorizacao.md` | Defines the targets and depth of the tests         |
| `07-integracao-pipeline.md`     | Where and how to connect the strategy to CI/CD        |
| Chapter 01 - Risk Management   | Defines the application's criticality level     |
| Chapter 02 - Requirements        | Defines what must be tested (REQs)           |
| Chapter 06 - Development   | Defines the secure practices to be validated              |
| Chapter 07 - Secure CI/CD      | Defines how the tests integrate into delivery   |
| Chapter 12 - Monitoring and Operations     | Post-deploy observation and runtime validation  |

---

> 🧠 A security testing strategy **is not a list of tools** - it is a decision about how, when and how deeply to validate the security of what is being built. It is the direct reflection of the risk the organisation accepts.
