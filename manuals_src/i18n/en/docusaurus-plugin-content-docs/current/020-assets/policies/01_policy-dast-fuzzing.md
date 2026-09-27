---
id: policy-dast-fuzzing
title: DAST and Fuzzing Policy
description: Organisational policy that defines the requirements, execution criteria, findings management and responsibilities for dynamic security testing (DAST) and fuzzing, proportional to the application's risk level.
tags: [policy, dast, fuzzing, testes dinâmicos, segurança, cap10, cap07, L2, L3, findings, pipeline]
grupo: testes
sidebar_position: 1
translation:
  source_locale: pt
  source_path: 020-assets/policies/01_policy-dast-fuzzing.md
  source_sha256: 510a592508c76597b018d117e07e2dd075f1b1cf7695be0c4277c671161ef0b4
  source_commit: 50f5914ebc90e4135e6678b2278709d5082dd237
  target_sha256: 6d5df6480904863cb55acc237dd17d0bce7d7e3ee1a06ea24af3cffcc09590d4
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, avaliacao, framework_source_corpus, practitioner_manual, requirement_runtime, risk_level, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: 2190616af45c704d0bdde9b6b05175705cda4e10018fb8b2c46ae504cde9f3e4
  translated_at: 2026-09-27T07:06:10Z
  stamped_at: 2026-09-27T07:06:10Z
  reviewed_by: null
---

# DAST and Fuzzing Policy

## 1. Objective {#1-objetivo}

This policy defines the minimum requirements for carrying out **dynamic security testing (DAST)** and **fuzzing** on applications classified as L2 or L3 in the SbD-ToE model.

The objective is to ensure that behavioural and input-handling vulnerabilities are detected before promotion to production, complementing static analysis mechanisms (SAST) with runtime validation.

DAST and fuzzing are complementary techniques:

- **DAST** - simulates the behaviour of an external user or attacker against the running application, identifying flaws that only manifest at runtime;
- **Fuzzing** - injects malformed, unexpected or random inputs into critical endpoints, revealing parsing flaws, crashes and anomalous behaviour not covered by planned tests.

---

## 2. Scope and proportionality {#2-âmbito-e-proporcionalidade}

| Technique | L1 | L2 | L3 |
|---|---|---|---|
| DAST | Manual/exploratory (optional) | Automated, authenticated | Automated + extended coverage |
| Fuzzing | Optional | Priority endpoints | Critical endpoints mandatory |
| IAST | Not applicable | Recommended | Mandatory |

This policy is **mandatory for L2 and L3**. For L1, the practices described here are recommended but not mandatory.

---

## 3. DAST - Dynamic Security Testing {#3-dast---testes-dinâmicos-de-segurança}

### 3.1 When to run {#31-quando-executar}

| Event | Mandatory status |
|---|:---:|
| Promotion of a build to staging | Mandatory |
| Before any release to production | Mandatory |
| After a change to the architecture or exposure surface | Mandatory |
| Periodic execution against the production version | Recommended (quarterly) |

### 3.2 Environment prior requirements {#32-pré-requisitos-de-ambiente}

- The execution environment must be **isolated** - DAST must never be run in production;
- Test environment data must be **fictitious or masked** - never real user data;
- The environment must be **equivalent to production** in terms of versions, configurations and dependencies;
- The environment must not be **shared** with other projects while the scan is running.

### 3.3 Mandatory configuration {#33-configuração-obrigatória}

**Authentication:**

- [ ] Login flow configured in the tool with a valid authenticated session
- [ ] Segregated test credentials - a dedicated account, never a real user account
- [ ] Credentials stored as secrets in the pipeline - never in plain text or in the repository
- [ ] Session with a short-lived token (TTL appropriate to the duration of the scan)

**Scope:**

- [ ] List of included URLs/endpoints defined and versioned
- [ ] Explicit and justified list of exclusions (e.g. logout endpoints, password reset, sending of external notifications, irreversible destructive operations)
- [ ] Scope configuration versioned in the repository alongside the pipeline definition

**Pipeline integration:**

- [ ] DAST job executed **after** deploy to staging and **before** promotion to production
- [ ] Report correlated with the commit SHA and release tag
- [ ] Report archived as a pipeline artefact with a minimum retention of 30 days (L1), 90 days (L2) or 1 year (L3)
- [ ] DAST result traceable in the release record

### 3.4 Blocking and response criteria {#34-critérios-de-bloqueio-e-resposta}

| Severity | Action |
|---|---|
| Critical | Blocks automatically; immediate escalation to AppSec Engineer |
| High | Blocks automatically; requires a validated fix or a formal exception |
| Medium | Does not block; mandatory recording in the centralised platform; 30-day SLA |
| Low / Info | Does not block; recording; quarterly review |

:::note Separation between automated signal and human decision
The pipeline reports the result (automated signal). The decision to override or grant an exception is always **human and documented** - never implicit or by timeout. Every override requires explicit approval by an AppSec Engineer, with the rationale recorded and a maximum validity period.
:::

### 3.5 Artefacts produced {#35-artefactos-produzidos}

| Artefact | Minimum retention |
|---|---|
| DAST report (HTML/JSON/SARIF) | 30 days (L1), 90 days (L2), 1 year (L3) |
| Gate evidence (pass/fail) in the pipeline log | 30 days (L1), 90 days (L2), 1 year (L3) |
| Open findings in the centralised platform | Until closure or formal acceptance |
| Exception register | 1 year (L1), 2 years (L2), 3 years (L3) after closure (Policy 06 §10) |

---

## 4. Fuzzing - Testing with Unexpected Inputs {#4-fuzzing---testes-de-inputs-inesperados}

### 4.1 When to run {#41-quando-executar}

| Event | Mandatory status (L2) |
|---|:---:|
| Per major release | Mandatory |
| Regular periodicity | Mandatory (quarterly) |
| After adding a new endpoint with input parsing | Mandatory |
| After a change to validation or deserialisation logic | Recommended |

### 4.2 Target selection {#42-seleção-de-targets}

**Mandatory targets for L2:**

- Endpoints that receive unstructured external input (forms, free-form JSON, query params)
- APIs that parse data formats (JSON, XML, multipart, CSV, binary)
- File upload endpoints
- Search endpoints with dynamic parameters
- Endpoints with deserialisation or expression evaluation logic

**Default exclusions** (inclusion requires explicit justification):

- Logout or session invalidation endpoints
- Endpoints that send external notifications (email, SMS, webhooks)
- Endpoints with aggressive rate limiting and no dedicated test instance

### 4.3 Mandatory configuration {#43-configuração-obrigatória}

**Environment:**

- [ ] Application instance **isolated** for fuzzing - with no connection to real external systems
- [ ] Active monitoring during execution: CPU, memory, crashes, error logs
- [ ] Mechanism for detecting crashes and anomalous responses configured

**Targets and profiles:**

- [ ] List of targets defined, versioned and approved by AppSec
- [ ] Fuzzing profiles (dictionaries, corpora, strategies) versioned in the repository
- [ ] Input corpora maintained and updated between executions

**Results:**

- [ ] Anomalies recorded with a minimal reproducible PoC (exact input, endpoint, application version)
- [ ] Report with reproducible cases archived

### 4.4 Severity criteria {#44-critérios-de-severidade}

| Result | Severity | Action |
|---|---|---|
| Application crash / Out-of-Memory | Critical | Blocks the release; escalates to AppSec |
| Exposure of internal data or stack trace | High | Blocks the release |
| Controlled anomalous behaviour | Medium | Recording and triage |
| Timeout or performance degradation | Low | Recording; later analysis |

### 4.5 Artefacts produced {#45-artefactos-produzidos}

| Artefact | Minimum retention |
|---|---|
| Fuzzing report | 30 days (L1), 90 days (L2), 1 year (L3) |
| Input corpora (versioned) | Permanent |
| Reproducible cases (PoC) in the findings platform | Until closure |
| Exception register | 1 year (L1), 2 years (L2), 3 years (L3) after closure (Policy 06 §10) |

---

## 5. Centralised findings management {#5-gestão-centralizada-de-findings}

All DAST and fuzzing findings are consolidated in the centralised security management platform, together with the SAST, IAST and SCA results.

**Mandatory metadata per finding:**

| Field | Description |
|---|---|
| Source tool | DAST / Fuzzing / SAST / IAST / SCA |
| Severity | Critical / High / Medium / Low / Info |
| CWE and/or CVE | Where applicable |
| Commit SHA and release tag | Traceability to the artefact |
| Status | Open / Being fixed / Accepted / Suppressed |
| Remediation owner | Responsible for the fix |
| Resolution SLA | As per the table in section 5.1 |

### 5.1 Resolution SLAs {#51-slas-de-resolução}

| Severity | SLA |
|---|---|
| Critical | 24 hours |
| High | 7 days |
| Medium | 30 days |
| Low | 90 days |

---

## 6. Decision framework for findings (Checklist C1) {#6-framework-de-decisão-para-findings-checklist-c1}

When a finding blocks the pipeline and the team weighs an override or exception, the decision must be documented against the following criteria:

- [ ] **Exploitability** - is the finding exploitable in the current context? In what way?
- [ ] **Existing mitigations** - are there active compensating controls?
- [ ] **Business impact** - what is the real impact if the finding is exploited?
- [ ] **Remediation** - when and how will it be fixed?
- [ ] **Decision** - FIX / ACCEPT WITH DEADLINE / SUPPRESS (with justification)
- [ ] **Approval** - AppSec Engineer (mandatory for High and Critical)

:::warning
The decision to suppress a Critical finding requires additional approval from the security lead (CISO or equivalent) and a maximum deadline of 7 days.
:::

---

## 7. Exceptions to this policy {#7-exceções-a-esta-política}

Every exception to this policy requires:

1. Documented technical justification
2. Approval by an AppSec Engineer
3. A defined and active compensating mitigation
4. Maximum validity period: **30 days** (renewable with new explicit approval)
5. Formal recording in the project's exception repository

Exceptions to findings of Critical severity have a maximum period of **7 days** and require additional approval from the security lead.

---

## 8. Responsibilities {#8-responsabilidades}

| Role | Responsibility |
|---|---|
| AppSec Engineer | Scope definition, approval of exceptions, triage of High and Critical findings |
| QA / Testing | Execution of DAST and fuzzing, definition and maintenance of targets and corpora |
| DevOps / SRE | Pipeline integration, maintenance of the isolated staging environment |
| Developer | Fixing findings, taking part in triage and context analysis |
| Product Management | Release approval, formal acceptance of residual risk |

---

## 9. Review and audit {#9-revisão-e-auditoria}

This policy must be **reviewed annually** or after any of the following events:

- Significant change to the application's architecture or exposure surface
- Security incident related to inputs or runtime behaviour
- Change to the application's classified risk level
- Relevant regulatory or normative change

Evidence of the execution of this policy (reports, gate logs, exception records) must be **auditable** by GRC functions and by external auditors.

---

## 10. Normative and technical references {#10-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 10 - Security Testing | DAST requirements, fuzzing, findings management |
| SbD-ToE Ch. 07 - Secure CI/CD | Integration of security gates into the pipeline |
| SbD-ToE Ch. 02 - Security Requirements | Traceability requirement → test → evidence |
| OWASP Testing Guide (OTG) | Dynamic testing methodology |
| OWASP Web Security Testing Guide (WSTG) | Coverage of vulnerability categories |
| NIST SP 800-115 | Technical Guide to Information Security Testing |
| CWE Top 25 | Categorisation of weaknesses |
| SSDF PW.8 | Security testing practices in the SDLC |
