---
id: modelo-controle-execucao
title: Execution Control Model
description: Strategy for ensuring that all code executed in production has previously been validated and authorised.
tags: [tipo:anexo, grupo:execucao, tema:pipeline, segurança, deploy]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/addon/01-modelo-controle-execucao.md
  source_sha256: 277208569976541f71c4c052badaf0379f44c58f927ff04ef5abfadb1719dcf3
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: ea9d29381c1fa3485763cbb95e7b21033198c1a9dfabce5f1d6a46fda97c3323
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 112d795f9bd927f0d4c24114e389470217eb00c1d6b919ae2df2e4f7bdb4878d
  glossary_keys: [chapter_role, validation_evaluation, verification_taxonomy]
  glossary_sha256: 036d44fcbdf1437f2cc310c29424e19b7147cd1e0e68f9abb0425581977c74f6
  translated_at: 2026-09-26T11:00:47Z
  reviewed_by: null
---


# Runtime Execution Control Model

## 🌟 Objective {#-objetivo}

To ensure that the application, after deployment, **executes in a secure, controlled and reversible way**, through mechanisms that make it possible to limit impact, respond to failures, activate or deactivate functionality and prevent dangerous executions in production.

These controls operate **during the execution** of the application, complementing the pre-deployment tests and the CI/CD controls, and are fundamental to supporting:

- Reversibility and impact containment;
- Active monitoring and response capacity;
- Progressive deployment and real-time security.

---

## 🧬 What execution control is {#-o-que-é-controlo-de-execução}

Execution control refers to all the mechanisms applicable **at runtime** that make it possible to condition, block, adjust or switch off application functionality **without a new deployment**.

Typical examples are:

| Type                     | Description                                                                                   | Practical example                                       |
|--------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------|
| **Feature Toggle**       | Dynamic activation or deactivation of functionality                                         | Launching a new feature for 5% of users          |
| **Circuit Breaker**      | Automatic interruption of external calls in case of repeated failure                      | Stopping calls to an external API after 3 timeouts          |
| **Timeout / Quota**      | Limitation of time or resource usage                                                       | 2s timeout for internal calls                  |
| **Kill Switch**          | Switching off functionality in case of incident or risk                                     | Deactivating the sending of notifications after an anomaly         |
| **Runtime Guard**        | Verification of preconditions before executing sensitive logic                             | Checking that a token is signed before using it        |

---

## 🛠️ How to apply {#️-como-aplicar}

1. **Identify points of risk or dynamic control** in the code:
   - External calls, new functionality, critical operations;

2. **Apply conditional execution mechanisms**, with external control:
   - Environment variables, centralised configuration, toggle panels;

3. **Include active monitoring** of the effects of the control:
   - Metrics, alerts, activation/deactivation logs, failure tracking;

4. **Document the fallback behaviour** of each control:
   - What happens if it is activated/deactivated - expected impact;

5. **Test the control mechanisms periodically**:
   - Simulate failures, incidents, load, and rollback validations.

---

## ✅ Good practices {#-boas-práticas}

- Use **feature toggles with a time limit** (e.g. 30 days);
- Document the logic of each control and ensure reversibility;
- Include **runtime guards for critical data** (e.g. validation before executing);
- Treat *circuit breakers* as security measures, not only resilience measures;
- Ensure that toggles and switches are **auditable and versioned**;
- Prefer **centralised and secure configuration** (e.g. HashiCorp Consul, AWS AppConfig);
- Validate that the code executed matches the environment (e.g. staging ≠ production).

---

## 📎 Cross-references {#-referências-cruzadas}

| Document / Chapter               | Relation to this topic                              |
|------------------------------------|----------------------------------------------------|
| Ch. 07 - Secure CI/CD             | Validation of environments and execution by pipeline     |
| Ch. 10 - Security Testing      | Functional tests of toggles, guards and fallbacks    |
| Ch. 12 - Monitoring and Operations  | Runtime observability and response to failures     |
| SLSA L3/L4                         | Verified execution, controlled environments         |
| NIST SSDF PR.AC-3                  | Authorised execution control                    |

---

> 🔐 Runtime execution control is a **critical element of operational security**, making it possible to prevent, contain or mitigate the impact of changes without requiring a new deployment - essential for high-criticality and high-availability environments.
