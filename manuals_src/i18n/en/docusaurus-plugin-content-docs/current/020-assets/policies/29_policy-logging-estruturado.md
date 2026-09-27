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
  source_sha256: 7d83c75529dbaa30904ffd8437e0574b63025a194fc1f13b10b701b713256a8e
  source_commit: ebf462b7f3a4272103adfe1b228ff31ae5fca3c8
  target_sha256: fc0bc1e60e3ef3c4f77e290902697dc942a819d8dc096a79054ab2a8a4224822
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [avaliacao, chapter_role, cra_pde, cra_support_period, dora_financial_entity, dora_ict_risk, eu_ai_high_risk_system, eu_ai_system, eu_placing_on_market, papel_suporte, practitioner_manual, requirement_runtime, sbdtoe_sbd]
  glossary_sha256: 13eead8e525138156b7211211b2b0691110ae1f044a37b8f2f4049cea01e2c3b
  translated_at: 2026-09-27T07:09:02Z
  stamped_at: 2026-09-27T07:14:37Z
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

| Log type | L1 | L2 | L3 |
|---|---|---|---|
| Operational logs (runtime, errors) | 30 days | 90 days | 1 year |
| Security logs (authentication, authorisation, changes) | 90 days | 1 year | 2 years |
| Audit logs (administrative operations, access to sensitive data) | 1 year | 1 year | 3 years |
| CI/CD pipeline logs | 30 days | 90 days | 1 year |
| Logs automatically generated by high-risk AI systems (OPS-011/012) | At least 6 months | 1 year | 2 years |

:::note
**Precedence.** The periods in this table are the **minimum recommended by the Manual** (the Manual's choice) and do not exhaust what is expected of the organisation. The most demanding of the following prevails:

- **(a) applicable EU law** — for example, logs automatically generated by high-risk AI systems are kept «for a period appropriate to the intended purpose of the high-risk AI system, of at least six months» (AI Act, Articles 19(1) and 26(6)), and the technical documentation of products with digital elements, including the SBOM, is kept available «for at least 10 years after the product with digital elements has been placed on the market or for the support period, whichever is longer» (CRA, Article 13(13)). Under DORA, it is the financial entity that establishes the retention period, taking into account, among other factors, the results of the ICT risk assessment (Delegated Regulation (EU) 2024/1774, Article 12(2)); entities covered by Implementing Regulation (EU) 2024/2690 maintain logs «for a predefined period» (Annex, point 3.2.5);
- **(b) national legislation**, including the transposition of NIS2 and sectoral regimes (for example, anti-money laundering, tax, employment, healthcare);
- **(c) supervisory guidance and expectations** (for example EBA, ESMA, EIOPA, Banco de Portugal, CMVM, ASF, ANACOM, CNCS), which are not law but are expected in audits;
- **(d) normal sector expectations**: standards and frameworks assumed by contract or expected by the market (for example PCI DSS for payment card data, ISO/IEC 27001 and SOC 2 in customer audits, customer and insurer requirements).

The Manual does not reproduce the periods of regimes (b) to (d): the organisation maps the applicable period in the version in force of each one. In any case, where logs contain personal data, they are kept for no longer than is necessary for the purpose (GDPR, Article 5(1), point (e)).
:::

**Organisation's retention map.** The organisation maintains a map that shows, for each record type, the regime that sets the period — EU law, national legislation, supervisor, sector or this Manual — and the value adopted, which is the most demanding of those applicable. It is the artefact an auditor asks for; it is reviewed whenever an applicable regime changes.

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
| DORA (Art. 9) — Delegated Regulation (EU) 2024/1774, Art. 12 (simplified framework: Art. 34, point (f)) | Logging requirements for financial entities |
| NIST SP 800-92 | Guide to Computer Security Log Management |
| ISO/IEC 27001 - A.12.4 | Logging and monitoring |
