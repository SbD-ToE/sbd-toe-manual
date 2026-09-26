---
id: policy-logging-estruturado
title: Structured Logging Policy
description: Organisational policy that defines the requirements for the production, formatting, centralisation, retention and protection of application and security logs, including a minimum event schema, mandatory events, masking of sensitive data, immutability and SIEM integration, proportional to the criticality level (L1, L2, L3).
tags: [policy, logging, structured logging, JSON, ECS, SIEM, retenção, imutabilidade, eventos de segurança, cap12, L1, L2, L3, governance, observabilidade]
grupo: operacoes
sidebar_position: 29
translation:
  source_locale: pt
  source_path: 020-assets/policies/29_policy-logging-estruturado.md
  source_sha256: 0fb2a3b691d9b5d5be970772da6ad8e1cccb16e16725db17e38e0d6fe0c941ce
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 02bc03086c48a9b95f6f26788d7d76d628c1e734dcc7079ba8ea5b832cffef7e
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bc04ded428e40ee1c214f8535dfb1904655b64166d0aa82b5df521e4230b8cb0
  glossary_keys: [chapter_role, papel_suporte, requirement_runtime, sbdtoe_sbd]
  glossary_sha256: 1a60d9e8761f3f44655cb1913eb43e896d0421b057d78ef3c75bff005aa33db4
  translated_at: 2026-09-26T14:11:00Z
  reviewed_by: null
---

# Structured Logging Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for the **production, formatting, centralisation, retention and protection of logs** in the organisation's applications and systems.

Logs are the primary record of a system's behaviour - they are the basis of all incident investigation, compliance audit and detection of security anomalies. Decentralised, non-normalised logs, or logs without integrity guarantees, do not fulfil this role: they are noise, not evidence. The transition from ad-hoc logging to centralised structured logging is a paradigm shift - not a change of tool.

The objective of this policy is to ensure that:

- All systems produce logs in a structured and normalised format
- Mandatory security events are always recorded, regardless of level
- Sensitive data and PII never appear in logs without adequate masking
- Logs are centralised, immutable at L3, and retained for the defined periods
- Log correlation across systems is possible via trace ID and common fields

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

This policy applies to all running systems that produce events relevant to security, operations or audit. It includes web applications, APIs, workers, jobs, CI/CD pipelines, infrastructure and authentication systems.

| Level | Applicability |
|---|---|
| L1 | Basic logging; structured format recommended; centralisation recommended |
| L2 | Mandatory; structured JSON format; mandatory security events; centralisation; minimum retention |
| L3 | Mandatory; JSON/ECS; complete events; centralisation + SIEM; WORM; regulatory retention |

---

## 3. Logging format {#3-formato-de-logging}

### 3.1 Mandatory format {#31-formato-obrigatório}

At L2/L3, all logs must be produced in **JSON** format (or compatible with Elastic Common Schema - ECS), machine-readable and processable without custom parsing:

- No unstructured free-text logs in critical components
- No multiple log formats in the same system without normalisation at ingestion

### 3.2 Minimum event schema {#32-schema-mínimo-de-evento}

Each log event must contain, at a minimum, the following fields:

| Field | Example | Mandatory |
|---|---|---|
| `timestamp` | `2025-07-21T10:35:14.321Z` | Yes; ISO 8601 UTC |
| `level` | `INFO`, `WARN`, `ERROR`, `DEBUG` | Yes; standardised levels |
| `event.action` | `user.login`, `file.upload`, `api.call` | Yes at L2/L3; consistent taxonomy |
| `application` | `api-gateway`, `worker-payment` | Yes; logical component |
| `environment` | `production`, `staging` | Yes |
| `trace.id` | `xyz-9876-abcd` | Yes at L2/L3; correlation across systems |
| `user.id` | `usr-1234` (internal, never email or name) | When applicable |
| `src.ip` | `192.168.1.20` | In authentication and access events |
| `http.status_code` | `200`, `401`, `500` | In APIs and endpoints |
| `message` | Human-readable description of the event | Yes |

---

## 4. Mandatory security events {#4-eventos-de-segurança-obrigatórios}

The following security events must always be recorded, regardless of the application's criticality level:

| Event | Minimum mandatory fields |
|---|---|
| Successful authentication | `user.id`, `src.ip`, `timestamp`, `method` (password/MFA/SSO) |
| Failed authentication | `user.id` (or attempt), `src.ip`, `timestamp`, `motivo` |
| Logout / session expiry | `user.id`, `session.id`, `timestamp` |
| Access denied (403) | `user.id`, `resource`, `action`, `src.ip`, `timestamp` |
| Change to sensitive data | `user.id`, `resource`, `acção`, `valor anterior` (hash), `timestamp` |
| Change to permissions/roles | `actor.id`, `target.id`, `permissão alterada`, `timestamp` |
| Administrative operation | `actor.id`, `acção`, `target`, `timestamp` |
| Relevant internal error | `error.type`, `error.message`, `stack trace resumido`, `trace.id` |
| File upload/download | `user.id`, `filename`, `size`, `method`, `timestamp` |
| Call to an external API | `endpoint`, `method`, `status`, `duration`, `trace.id` |

---

## 5. Absolute prohibitions in logs {#5-proibições-absolutas-nos-logs}

The following data must never appear in logs, regardless of level:

| Prohibited data | Alternative |
|---|---|
| Passwords, PINs, answers to secret questions | Never record - not even as a hash |
| Session tokens, full JWTs, API keys | Record only the prefix (e.g. `Bearer eyJ...` → `Bearer eyJ[redacted]`) |
| Credit card numbers, IBAN | Mandatory masking: `****-****-****-1234` |
| Health data, biometric data | Never record in operational logs |
| Directly identifiable PII (full name + address + tax ID number) | Use internal `user.id`; masking of PII fields in debug logs |
| Secrets, private keys, certificates | Never |

:::warning
Recording sensitive data in debug or error logs is one of the most common sources of PII exposure in production systems. DEBUG-level logs must be disabled in production or filtered before centralised ingestion.
:::

---

## 6. Log centralisation {#6-centralização-de-logs}

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Logs centralised in a logging system (ELK, Loki, Splunk, etc.) | Recommended | Mandatory | Mandatory |
| Ingestion pipeline with schema normalisation | Recommended | Mandatory | Mandatory |
| Correlation possible by `trace.id` across services | Recommended | Mandatory | Mandatory |
| SIEM integration | Not applicable | Recommended | Mandatory |
| CI/CD pipeline logs centralised | Recommended | Mandatory | Mandatory |

---

## 7. Log retention {#7-retenção-de-logs}

| Log type | L2 | L3 |
|---|---|---|
| Operational logs (runtime, errors) | 90 days | 1 year |
| Security logs (authentication, authorisation, changes) | 1 year | 2 years (or as required by regulation) |
| Audit logs (administrative operations, access to sensitive data) | 1 year | 3 years (DORA: 5 years) |
| CI/CD pipeline logs | 90 days | 1 year |

:::note
In regulated contexts (DORA, NIS2, GDPR, healthcare, financial), regulatory periods prevail over the minimums of this policy. The longest period is always the applicable one.
:::

---

## 8. Integrity and immutability {#8-integridade-e-imutabilidade}

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Logs protected from modification | Recommended | Mandatory | Mandatory |
| WORM storage (Write Once, Read Many) | Not applicable | Recommended | Mandatory |
| Periodic hashing or signing of logs | Not applicable | Recommended | Mandatory |
| Access to logs restricted and audited | Recommended | Mandatory | Mandatory |
| Alerts upon any attempt at alteration or deletion | Not applicable | Recommended | Mandatory |

---

## 9. Responsibilities {#9-responsabilidades}

| Role | Responsibility |
|---|---|
| Developer | Implement structured logging according to the schema; do not record sensitive data; use `trace.id` |
| DevOps / SRE | Configure the centralisation pipeline; ensure retention and immutability; manage the logging system |
| AppSec Engineer | Define mandatory security events; audit logs for PII; configure SIEM integration |
| GRC / Compliance | Verify compliance with regulatory retention periods; audit access to logs; reports |

---

## 10. Review and audit of this policy {#10-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- An incident in which insufficient or missing logs hindered the investigation
- Exposure of PII or sensitive data in logs
- A regulatory change imposing new retention requirements

---

## 11. Normative and technical references {#11-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 12 - Monitoring and Operations | US-01 (structured logging), US-07 (log security and integrity) |
| Elastic Common Schema (ECS) | Reference schema for normalised fields |
| OWASP Logging Cheat Sheet | Good practices for secure logging |
| GDPR / RGPD - Art. 5(1)(e) | Storage limitation of personal data |
| DORA - Art. 12 | Logging requirements for financial entities |
| NIST SP 800-92 | Guide to Computer Security Log Management |
| ISO/IEC 27001 - A.12.4 | Logging and monitoring |
