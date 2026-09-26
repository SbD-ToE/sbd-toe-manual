---
id: evidencia-reprodutibilidade
title: Evidence, Reproducibility and Auditability in Security Testing
description: Prescriptive rules to ensure that security test results are verifiable, reproducible and auditable, with protection of critical assets and separation between automated signal and human decision.
tags: [testes, evidência, reprodutibilidade, auditabilidade, validação, rastreabilidade, supply-chain, segredos, dados]
sidebar_position: 10
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/addon/10-evidencia-reprodutibilidade.md
  source_sha256: 12e7b5d87c1c0935a7637e18b5fcf54fe659381f203278daa9a09700fbbf0831
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: b57c17f0f3284da5dc286047e77a9ad0019ec5e5aeb48ca56f96c2c4d637b31a
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 2ffd43fd37c8802a693f5fa1e43a3d3a9df1ca9d5ea898c88f6f405bedc9d687
  glossary_keys: [cycle_iteration, framework_source_corpus, practitioner_manual, traceability, validation_evaluation]
  glossary_sha256: de4ffdc02c859536a2e803809627d4fa4d4e1f57ff7d07faae9665379c590da5
  translated_at: 2026-09-26T10:31:31Z
  reviewed_by: null
---

# Evidence, Reproducibility and Auditability in Security Testing

This annex defines **prescriptive** rules to ensure that security tests produce **verifiable evidence**, allow **independent reproduction** and support **audit** - even when execution is highly automated.

The aim is to avoid three recurring failures in modern testing processes:

1. **Confusing “signal” with “evidence”** (e.g. a report or a score replaces observable execution).
2. **Losing reproducibility** (e.g. the same commit produces incomparable results because of variation in rules, environment or data).
3. **Exposing critical assets** (e.g. credentials, data, telemetry or build artefacts leave the perimeter without explicit control).

> Master rule: **a test only “counts” as evidence when it can be verified and reproduced, with authorship and decision attributed to a human role.**

---

## 1. Separation between automated signal and human decision {#1-separação-entre-sinal-automático-e-decisão-humana}

Tools may:
- detect patterns;
- correlate results;
- prioritise findings;
- suggest fixes.

But they **may not**:
- declare “approved” or “compliant”;
- close findings without defined validation;
- authorise exceptions;
- accept residual risk.

### Prescription {#prescrição}
- Each security *gate* (pass/fail) must have an **explicit human owner** (e.g. Tech Lead, AppSec, QA Lead, Release Manager).
- “It passed the scanner” **is not** an accepted argument without:
  - evidence of execution (logs/artefacts),
  - execution conditions (config/versions),
  - and approval criteria (policy/rules).

---

## 2. Minimum evidence (what must exist for a result to be accepted) {#2-evidência-mínima-o-que-deve-existir-para-um-resultado-ser-aceite}

### 2.1 Evidence of execution (mandatory) {#21-evidência-de-execução-obrigatória}
For each relevant execution of security tests, there must exist, at a minimum:

- Identifier of the commit / build / artefact tested (hash, tag, digest).
- Timestamp and identified *runner* / executor.
- Effective configuration used (file, parameters, profile).
- Version of the test engine and dependent versions (e.g. images, rulepacks, signatures).
- Raw output preserved (full log, JSON/XML/HTML, artefacts).
- Summarised result (pass/fail, thresholds, severities) **derived from the raw output**.

> Dashboards and PDFs are merely “presentation”. The evidence is the **raw output + execution context**.

### 2.2 Evidence of validation (where applicable) {#22-evidência-de-validação-quando-aplicável}
Whenever there is triage, exception, suppression or “compensation”:

- Record of who validated and when (author/role).
- Objective justification (criterion + reference).
- Validity condition (TTL, next retest date, closure condition).
- Link to the backlog item / ticket / release decision.

---

## 3. Reproducibility: making results comparable over time {#3-reprodutibilidade-tornar-resultados-comparáveis-no-tempo}

### 3.1 Control of variables (mandatory) {#31-controlo-de-variáveis-obrigatório}
Test results are only comparable if the critical variables are controlled:

- **Engine and rules version**: rulepacks, signatures, policies.
- **Execution environment**: runner image, operating system, dependencies.
- **Target tested**: immutable build/digest/artefact.
- **Configuration**: profiles, exclusion lists, limits, thresholds.
- **Test data and credentials**: dataset and permissions (see Section 4).

### 3.2 Practical prescriptions {#32-prescrições-práticas}
- Use version *pinning* (engine + rules) per pipeline and per project.
- Version test profiles and policies (in the repo).
- Preserve raw outputs with a defined minimum retention (e.g. per release).
- Ensure that each execution can be re-run with the “same input” (replay).

### 3.3 Intrinsically non-deterministic tests {#33-testes-intrinsecamente-não-determinísticos}
Some tests may produce variation (e.g. fuzzing, DAST with timing, distributed targets).

**In those cases:**
- Preserve the *seed* and execution parameters when they exist.
- Repeat the execution (minimum N) to reduce false negatives.
- Treat the absence of a finding as a **weak signal** without additional coverage evidence.

---

## 4. Protection of critical assets in the testing process {#4-proteção-de-ativos-críticos-no-processo-de-teste}

Security tests frequently involve:
- credentials and tokens for authenticated tests;
- representative (or accidentally real) data;
- telemetry, logs and traffic containing secrets;
- build artefacts and code.

### 4.1 Mandatory prescriptions {#41-prescrições-obrigatórias}
- **Real data**: prohibited by default in tests (except with explicit approval and compensating controls).
- **Test credentials**:
  - must be segregated by environment,
  - minimal (least privilege),
  - with rotation and expiry.
- **Egress and telemetry**:
  - any sending of outputs outside the perimeter must be treated as a supply chain dependency;
  - require explicit approval, data classification and contractual/technical control.
- **Logs**:
  - apply masking rules;
  - ensure that preserved outputs do not expose secrets.

### 4.2 Test environments and targets {#42-ambientes-e-alvos-de-teste}
- DAST/IAST/fuzzing must use environments with:
  - network isolation,
  - impact limitation (rate limiting, quotas),
  - monitoring of changes and traffic.
- Offensive and intrusive tests must have:
  - an approved window,
  - an operational “kill switch”,
  - stop criteria.

---

## 5. Minimum evidence by type of test (operational table) {#5-evidência-mínima-por-tipo-de-teste-tabela-operativa}

| Type of test | Minimum evidence of execution | Minimum reproducibility | Critical note |
|---|---|---|---|
| SAST | commit + config + engine/rules version + raw output | rule pinning + comparable baseline | “0 findings” without a baseline is a weak signal |
| DAST | target + window + auth profile + output + execution logs | versioned config + scope policy | high risk of exfiltration and false negatives |
| IAST | build + instrumentation + config + logs + findings | instrumentation version + controlled environment | outputs may contain sensitive data |
| Fuzzing | target + parameters + seed (if applicable) + crashes + logs | seed + execution time + versioned corpus | absence of a crash ≠ absence of a bug |
| Pentesting / manual | scope + methodology + evidence (PoC) + report | execution artefacts and notes preserved | requires tracking of decision and fix |

---

## 6. Exceptions, suppressions and risk acceptance (closing the cycle) {#6-exceções-supressões-e-aceitação-de-risco-fecho-de-ciclo}

Suppressions, “false positives”, exceptions and risk acceptance are **governance facts**, not technical “opinions”.

### Prescription {#prescrição-1}
- No exception is valid without:
  - a human owner,
  - an objective justification,
  - a deadline (TTL),
  - a retest plan,
  - a link to the affected release/artefact.

---

## 7. Acceptance criteria for this annex {#7-critérios-de-aceitação-deste-anexo}

This annex is considered applied when, in the project:

1. Raw evidence is preserved for relevant executions.
2. Test profiles and policies are versioned and controlled.
3. Replay of an execution is possible (or the variation is controlled by repetition).
4. Credentials/data/telemetry are treated as critical assets with explicit controls.
5. Exception and “pass/fail” decisions have a human owner and traceability.

---
