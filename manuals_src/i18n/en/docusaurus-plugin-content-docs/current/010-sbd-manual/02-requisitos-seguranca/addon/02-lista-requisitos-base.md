---
id: lista-requisitos-base
title: Base Security Requirements Catalogue
description: Canonical catalogue of SbD-ToE application security requirements, organised by technical domain, with applicability by risk level (L1–L3) and minimum acceptance criteria for validation, audit and integration into backlogs.
requirement_class: aplicacional
tags: [tipo:catalogo, classe:aplicacional, requisitos, segurança-aplicacional, rastreabilidade, L1, L2, L3, aceitacao, auditoria, ASVS, NIST-SSDF]
sidebar_position: 2
translation:
  source_locale: pt
  source_path: 010-sbd-manual/02-requisitos-seguranca/addon/02-lista-requisitos-base.md
  source_sha256: 9be78c355bbd0770e892a0f0b25b367dd476848986b15c57dc06365f74d36e24
  source_commit: 550e045d15f912fcb68829e17082413a5d80bd97
  target_sha256: 4d774d9093f6a33445ddea329878c1177973748bbcd099146aa6d265b2ef05b0
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [audit_trail, avaliacao, capacitacao, chapter_role, cycle_iteration, esquema_regime, framework_source_corpus, lifecycle_phase, mapping, maturity, mcp_reading_programa, normative_empirical, practitioner_manual, programme_line, requirement_runtime, risk_level, role_tech_lead, sbdtoe_sbd, schema, threat, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: b5b719bdacb01d3e004a1446e0d542ec14541a3d0bda952c9470360d990c028a
  translated_at: 2026-09-27T16:11:04Z
  stamped_at: 2026-09-27T16:11:04Z
  reviewed_by: null
---

# Base Security Requirements Catalogue

This catalogue is the **canonical reference of application security requirements** of SbD-ToE. Each requirement is identified by a **stable canonical ID** (`CATEGORIA-NNN`), has its applicability defined by risk level (L1–L3) and carries a minimum acceptance criterion that allows objective validation and direct integration into backlogs, definitions of done and audit processes.

---

## Scope: application requirements {#âmbito-requisitos-aplicacionais}

This catalogue covers **security requirements intrinsic to the software** - the properties the system must guarantee at runtime, regardless of where it is deployed or how the infrastructure is defined. It includes: authentication and identity management, access control, logging and monitoring, session management, data validation, error handling, secure configuration of application parameters, security of APIs and integrations, and process requirements such as requirements management, artefact distribution and development tools.

## Mapping of catalogues by technical domain {#mapeamento-de-catalogos}

SbD-ToE organises security requirements into **canonical catalogues by technical domain**, distributed across the chapters of the manual. Each catalogue has its own prefix, typical owner and distinct reference artefact. This is the complete map:

| Ch. | Prefix(es) | Domain | Object | Typical owner |
|------|-----------|---------|---------|-------------------|
| 01 | `CLA` | Application classification | Formal criticality classification, reclassification, residual risk and proportionality of controls | Product Owner, Tech Lead, AppSec, GRC |
| 02 | `AUT` `ACC` `LOG` `SES` `VAL` `FIL` `ERR` `CFG` `ENC` `PRI` `API` `INT` `REQ` `DST` `IDE` | Application requirements | Security properties of the software at runtime | Development team |
| 03 | `THR` | Threat modelling | Threat identification, formal disposition, derivation of requirements and traceability | Technical architect, AppSec |
| 04 | `ARC` | Secure architecture | Design, structure and decisions of the system | Technical architect, AppSec |
| 05 | `DEP` | Dependencies, SBOM and SCA | Embedded third-party components | Development team, AppSec |
| 06 | `DEV` | Secure development | Development practices and processes | Development team, AppSec |
| 07 | `CIC` | Secure CI/CD | The pipeline as an engineering product | DevSecOps, platform |
| 08 | `IAC` | Infrastructure as Code | The IaC project as software | Platform engineering, DevSecOps |
| 09 | `CNT` | Containers and images | The container artefact and execution policies | DevSecOps, development |
| 10 | `TST` | Security testing | The security testing programme | AppSec, DevSecOps |
| 11 | `DPL` | Secure deployment | The process of promotion to production | DevSecOps, Release Management |
| 12 | `OPS` | Monitoring and operations | The operational monitoring programme | Operations, SOC, DevSecOps |
| 13 | `TRN` | Training and onboarding | Upskilling, verifiable onboarding, Security Champions and training effectiveness | AppSec, PeopleOps, technical leadership |
| 14 | `GOV` | Governance and contracting | Governance model, exceptions, contracting and organisational maturity | AppSec, GRC, CISO |

Each chapter holds its catalogue in `addon/00-catalogo-requisitos.md` (or equivalent), with applicability by risk level (L1–L3) and acceptance criteria in the same format as this catalogue. The distinction between catalogues is operationally relevant: owners, artefacts and review cycles differ by domain - a requirement of the `ARC-` kind is assessed in an architecture review, not in a code PR.

---

> **On curation:** This catalogue was consolidated from recognised sources - OWASP ASVS, NIST SSDF, IEC 62443, among others - and is meant to be **adapted by each organisation and instantiated by each project**. It is not immutable: it must be maintained as a living document, reviewed periodically and adjusted to the technical and risk context. When a project has no catalogue of its own, this one serves as a direct starting point.

For instantiation in a project and the operational traceability naming (`SEC-Lx-DOMINIO-CODIGO`), see [Taxonomy and Traceability](./taxonomia-rastreabilidade).

---

## Conventions {#convenções}

| Symbol | Meaning |
|---------|-------------|
| ✔ | Mandatory requirement at this level |
| - | Not applicable or not mandatory at this level |

Levels are cumulative: L3 includes all L1 and L2 requirements; L2 includes all L1 requirements.

---

## Index {#índice}

- [AUT - Authentication and Identity](#aut)
- [ACC - Access Control](#acc)
- [LOG - Logging and Monitoring](#log)
- [SES - Sessions and State](#ses)
- [VAL - Data Validation](#val)
- [FIL - File Handling](#fil)
- [ERR - Error Handling](#err)
- [CFG - Secure Configuration](#cfg)
- [ENC - Sensitive Data and Cryptography](#enc)
- [PRI - Personal Data (engineering)](#pri)
- [API - API Security](#api)
- [INT - Messaging and Integrations](#int)
- [REQ - Requirements Definition](#req)
- [DST - Artefact Distribution](#dst)
- [IDE - Development Tools](#ide)

---

## AUT - Authentication and Identity {#aut}

Requirements that ensure only legitimate entities access the system, with controls proportional to the sensitivity of the operations.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| AUT-001 | Mandatory MFA | - | ✔ | ✔ | Login without a second factor is rejected; evidence of the block in logs. |
| AUT-002 | Password policy | ✔ | ✔ | ✔ | The system rejects passwords that do not comply with the policy; the block is evidenced in testing. |
| AUT-003 | Brute-force protection | ✔ | ✔ | ✔ | Account locked or access delayed after N failed attempts; logs evidence the event. |
| AUT-004 | Active session revocation | ✔ | ✔ | ✔ | Logout invalidates the token/session immediately; reuse results in an authentication error. |
| AUT-005 | Automatic session expiry | ✔ | ✔ | ✔ | The session ends after the configured inactivity period; redirect to authentication. |
| AUT-006 | No credentials in clear text | ✔ | ✔ | ✔ | Audit confirms salted hashing; no clear-text credentials in storage or in transmission. |
| AUT-007 | Support for federated authentication | - | ✔ | ✔ | SAML/OIDC flow functional and tested; authentication log via external IdP available. |
| AUT-008 | Step-up for sensitive actions | - | ✔ | ✔ | Critical operations require an additional factor; testing evidences the block without step-up. |
| AUT-009 | Re-authentication for critical changes | ✔ | ✔ | ✔ | Changes to credentials or sensitive data require confirmation of the active identity. |
| AUT-010 | Alert on suspicious access | - | ✔ | ✔ | Anomalous access generates an alert or a notification to the user; log of the event available. |
| AUT-011 | No default credentials | ✔ | ✔ | ✔ | The application is not delivered or put into production with default accounts or credentials; initial credentials unique per installation and changed at first use; default accounts of components and platforms disabled or with their credential changed. |

---

## ACC - Access Control {#acc}

Requirements that ensure each entity accesses only the resources and operations explicitly permitted to it.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| ACC-001 | RBAC access control | ✔ | ✔ | ✔ | Profiles and permissions mapped; a role with reduced privilege does not access restricted resources. |
| ACC-002 | Principle of least privilege | ✔ | ✔ | ✔ | Accounts without unnecessary permissions; audit evidences effective restriction. |
| ACC-003 | Blocking and auditing of illegitimate access | ✔ | ✔ | ✔ | Unauthorised access attempts are blocked and logged with sufficient context. |
| ACC-004 | Separation of profiles | ✔ | ✔ | ✔ | User, administrator and service profiles are distinct; the actions of each profile are traceable. |
| ACC-005 | Access control for APIs and services | ✔ | ✔ | ✔ | Endpoints reject unauthenticated or unauthorised calls; logs record the rejections. |
| ACC-006 | Protection of sensitive resources | ✔ | ✔ | ✔ | Unauthorised access to critical data is prevented and logged; the bypass test fails. |
| ACC-007 | Validation of the access model | - | ✔ | ✔ | Permission model reviewed and documented; access-control threats mapped. |
| ACC-008 | Real-time revocation | ✔ | ✔ | ✔ | Removal of access takes effect immediately; the permission test fails after revocation. |
| ACC-009 | Attribute-based authorisation (ABAC) | - | - | ✔ | The access decision depends on dynamic attributes; logs evidence the policy evaluation. |
| ACC-010 | Periodic review of permissions | ✔ | ✔ | ✔ | Periodic audits remove obsolete permissions; review records kept and dated; minimum cadence (the Manual's choice): annual at L1, half-yearly at L2, quarterly at L3. |

---

## LOG - Logging and Monitoring {#log}

Requirements that guarantee auditable evidence of the system's operations, supporting incident detection and forensic response.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| LOG-001 | Logging of critical events | ✔ | ✔ | ✔ | Access, changes and critical security failures are logged; logs verified by sampling. |
| LOG-002 | Minimum attributes in logs | ✔ | ✔ | ✔ | Each entry includes: who, when, what and where; the absence of any attribute fails the audit. |
| LOG-003 | Protection of log integrity and access | ✔ | ✔ | ✔ | Logs cannot be altered by ordinary users; protection by permissions or verifiable signature. |
| LOG-004 | Periodic log analysis | - | ✔ | ✔ | Periodic analysis process documented and evidenced; frequency proportional to the risk. |
| LOG-005 | Minimum log retention | ✔ | ✔ | ✔ | Logs kept for the period defined in policy; effective retention verified. |
| LOG-006 | Forwarding to a centralised system | - | ✔ | ✔ | Critical events sent to and recorded in a central aggregator (SIEM or equivalent). |
| LOG-007 | Classification and anomaly detection | - | ✔ | ✔ | Severity policy defined; anomalies trigger alerts that are configured and tested. |
| LOG-008 | Alarm on failures of the logging mechanism | - | ✔ | ✔ | Failures of the logging system generate an alert; absence of logs is detected and notified. |
| LOG-009 | Logs support incident response | - | ✔ | ✔ | Logs with sufficient detail to reconstruct an incident; tested in an exercise or simulation. |
| LOG-010 | Logging of critical business events | - | - | ✔ | Events with business impact (transactions, critical authorisations) logged and traceable. |

---

## SES - Sessions and State {#ses}

Requirements that control the lifecycle of sessions and tokens, preventing reuse, fixation and improper persistence.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| SES-001 | Automatic expiry on inactivity | ✔ | ✔ | ✔ | The session ends after the configured inactivity period; redirect to authentication. |
| SES-002 | Manual logout and logout after credential change | ✔ | ✔ | ✔ | Logout ends all active sessions; a password change invalidates previous tokens. |
| SES-003 | Unpredictable session identifiers | ✔ | ✔ | ✔ | Tokens/sessions with adequate entropy; predictability analysis reveals no pattern. |
| SES-004 | Secure transmission of tokens | ✔ | ✔ | ✔ | Tokens transmitted only over TLS channels; cookies with the Secure and HttpOnly flags. |
| SES-005 | Binding of the session to the client context | - | ✔ | ✔ | A change of IP or user-agent ends the session or requires revalidation; testing evidences the behaviour. |
| SES-006 | Explicit session revocation | ✔ | ✔ | ✔ | The session can be ended at the request of the user or of the system; the token becomes invalid immediately. |
| SES-007 | Prevention of long-lived sessions | - | ✔ | ✔ | Maximum TTL configured and enforced; sessions of excessive duration are not possible. |
| SES-008 | Scope, TTL and revocation of JWT tokens | - | ✔ | ✔ | JWTs include scope and expiry claims; revocation mechanism implemented and tested. |

---

## VAL - Data Validation {#val}

Requirements that guarantee only well-formed and expected data is processed by the system, preventing injections and non-deterministic behaviour.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| VAL-001 | General validation of external inputs | ✔ | ✔ | ✔ | Invalid inputs are rejected with an appropriate error code; logs evidence the block. |
| VAL-002 | Use of whitelists instead of blacklists | ✔ | ✔ | ✔ | Only explicitly accepted values are allowed; unexpected values are rejected. |
| VAL-003 | Schema validators (JSON/XML schema) | - | ✔ | ✔ | Malformed payloads are rejected automatically; parsing logs available. |
| VAL-004 | Sanitisation against injections | ✔ | ✔ | ✔ | Potentially dangerous inputs are neutralised; injection attacks result in a controlled failure. |
| VAL-005 | Validation before internal use | ✔ | ✔ | ✔ | Data is validated before use in business logic or persistence; there are no unvalidated paths. |
| VAL-006 | Safe error messages in validation | ✔ | ✔ | ✔ | Validation errors expose neither internal logic nor sensitive data to the client. |
| VAL-007 | Automated tests against malicious inputs | - | ✔ | ✔ | Automated tests cover XSS, SQLi and other relevant injections; results recorded. |
| VAL-008 | Output encoding/escaping on rendering (anti-XSS) | ✔ | ✔ | ✔ | Output is encoded contextually to the rendering destination (HTML/attribute/JavaScript, queries via prepared statements, shell commands, anti-injection logs); no direct concatenation on sensitive surfaces. |

---

## FIL - File Handling {#fil}

A file is input — what differs is how it is validated: beyond the value, what counts is the real type of the content, the cost of processing it, and where it is stored and served from. The `VAL-*` requirements cover data validation; the `FIL-*` requirements cover what is specific to files — acceptance, content, compressed archives, quota, storage and serving — without duplicating the generic validation.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| FIL-001 | Processable size limit per upload | ✔ | ✔ | ✔ | Files above the limit defined per feature are rejected before any processing; the limit is documented. |
| FIL-002 | Type validation by content, not only by extension | ✔ | ✔ | ✔ | The extension matches the expected type and the content corresponds to the type (*magic bytes* check, image *re-writing* or a content-validation library); non-conforming files are rejected. |
| FIL-003 | Safe handling of compressed archives | - | ✔ | ✔ | Before decompressing: maximum decompressed size and maximum number of files checked; *symlinks* rejected unless explicitly allowlisted; decompression ignores user-supplied paths (*zip slip*). |
| FIL-004 | Storage quota per user | - | ✔ | ✔ | Space quota and maximum number of files per user active; an attempt to exceed them is rejected and logged. |
| FIL-005 | Storage outside the served tree, with generated names | ✔ | ✔ | ✔ | Files of untrusted origin are not executable as server code when accessed over HTTP; paths of file operations use internally generated names, or strict validation when the user-supplied name is unavoidable. |
| FIL-006 | Serving files in an inert context | - | ✔ | ✔ | Served file names are validated or sanitised and declared in `Content-Disposition` (RFC 6266); user content is served in a way that cannot be interpreted as HTML or script on the application's domain. |
| FIL-007 | Anti-malware scanning of files of untrusted origin | - | ✔ | ✔ | Files received from untrusted sources go through anti-malware scanning before being made available; a detection blocks availability and generates a log entry. |
| FIL-008 | Image dimension limit (pixel flood) | - | ✔ | ✔ | Images with pixel dimensions above the defined maximum are rejected wherever the application processes images. |

> **Proportionality of FIL-002 at L1** (from the derivation source, ASVS v5 `UNIT-V5.2.2`): "For L1, this can focus just on files which are used to make specific business or security decisions. For L2 and up, this must apply to all files being accepted." — at L1, content validation may be limited to the files that underpin business or security decisions; at L2+ it applies to all accepted files.

**Sources.** Derivation per line: FIL-001 — `UNIT-V5.2.1`, `UNIT-V5.1.1`; FIL-002 — `UNIT-V5.2.2`, `UNIT-V5.1.1`, CWE-434; FIL-003 — `UNIT-V5.2.3`, `UNIT-V5.2.5`, `UNIT-V5.3.3`; FIL-004 — `UNIT-V5.2.4`; FIL-005 — `UNIT-V5.3.1`, `UNIT-V5.3.2`, CWE-434; FIL-006 — `UNIT-V5.4.1`, `UNIT-V5.4.2` (the clause on content not interpretable on the application's domain is an editorial prescription of SbD-ToE); FIL-007 — `UNIT-V5.4.3` (the clause "and generates a log entry" is an editorial prescription); FIL-008 — `UNIT-V5.2.6`. The sources anchor the derivation; the prescription, the wording and the L1–L3 scaling are editorial choices of SbD-ToE.

---

## ERR - Error Handling {#err}

Requirements that ensure errors and exceptions are handled in a controlled way, without exposing sensitive information or internal logic.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| ERR-001 | Errors do not expose sensitive data | ✔ | ✔ | ✔ | Messages to the client are abstract; detailed internal logs are never exposed externally. |
| ERR-002 | Generic messages on the client | ✔ | ✔ | ✔ | The client always receives a generic message; stack traces and internal details are not transmitted. |
| ERR-003 | No disclosure of resource existence | ✔ | ✔ | ✔ | Error responses are identical for existing and non-existing resources (no enumeration). |
| ERR-004 | Localised and safe messages | ✔ | ✔ | ✔ | Translated messages without executable content or references to internal logic. |
| ERR-005 | Standardised and centralised handling | - | ✔ | ✔ | An error framework centralises handling and logging; no scattered ad-hoc handling. |
| ERR-006 | Automated tests for excessive errors | - | ✔ | ✔ | Tests guarantee that errors are handled and that no information leaks; coverage of edge cases. |
| ERR-007 | Error logs with pseudonymised context | - | ✔ | ✔ | Logs include contextual IDs; personal data or credentials are never recorded in error logs. |

---

## CFG - Secure Configuration {#cfg}

Requirements that guarantee the system is configured and operated in a way that minimises the attack surface and prevents accidental exposure.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| CFG-001 | Debug and flags disabled in production | ✔ | ✔ | ✔ | Debug, trace and dev_mode parameters switched off in production; automated check in the pipeline. |
| CFG-002 | Environment separation with automated validation | ✔ | ✔ | ✔ | Deployments and tests only in segregated environments; logs evidence effective segregation. |
| CFG-003 | No hardcoded parameters | ✔ | ✔ | ✔ | Source code contains no secrets or sensitive parameters in clear text; an automated scan confirms it. |
| CFG-004 | External configuration with controlled permissions | ✔ | ✔ | ✔ | Configuration is external to the code; access permissions to the configuration repository are restrictive. |
| CFG-005 | Configuration validation at start-up | - | ✔ | ✔ | The system fails to start when mandatory parameters are missing or incorrect; explicit error. |
| CFG-006 | Use of vaults and secure secrets management | - | ✔ | ✔ | Secrets exist only in secure vaults; audit evidences the absence of secrets in the repository. |
| CFG-007 | Configuration drift monitoring | - | - | ✔ | Unexpected changes to critical configuration trigger alerts; baseline documented. |

---

## ENC - Sensitive Data and Cryptography {#enc}

Requirements that guarantee the protection of sensitive data in transit and at rest, the use of robust cryptographic primitives, and the prevention of accidental exposure of secrets and personal data.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| ENC-001 | Encryption of all communications in transit | ✔ | ✔ | ✔ | All communication between client and server and between internal services uses TLS with a defined minimum version; insecure versions (TLS 1.0, 1.1, SSLv3) disabled and verifiable by configuration. |
| ENC-002 | Encryption of sensitive data at rest | - | ✔ | ✔ | Data classified as sensitive (PII, credentials, financial data) encrypted in persistent storage; encryption keys managed separately from the data; evidence of application to all relevant datastores. |
| ENC-003 | Robust cryptographic algorithms and configurations | - | ✔ | ✔ | Only approved algorithms and adequate key sizes in use (e.g. AES-256, RSA ≥ 2048, approved elliptic curves); weak or deprecated algorithms (MD5, SHA-1 for integrity, DES) absent; list of approved primitives documented. |
| ENC-004 | Adaptive password hashing | ✔ | ✔ | ✔ | Passwords stored with an adaptive, brute-force-resistant algorithm (bcrypt, Argon2, PBKDF2); cost factor configured and reviewed periodically; absence of static or reversible hashing confirmed. |
| ENC-005 | Masking of sensitive data in logs, outputs and API responses | ✔ | ✔ | ✔ | Passwords, tokens, card numbers and sensitive personal data do not appear in clear text in logs, error responses or debugging outputs; coverage verified by log analysis and testing. |
| ENC-006 | Detection and prevention of secrets exposed in repositories | ✔ | ✔ | ✔ | Secret-detection tool active in the pipeline (e.g. truffleHog, gitleaks, detect-secrets); commits with detected secrets blocked or alerted; no clear-text secrets in the repository history. |
| ENC-007 | Periodic rotation of keys and secrets | - | ✔ | ✔ | Rotation policy defined per type of secret; rotation carried out within the defined deadlines; auditable evidence of rotation; no keys without an expiry date for critical material. |
| ENC-008 | Prevention of client-side caching of sensitive data | - | ✔ | ✔ | Responses containing sensitive data include headers that inhibit caching (Cache-Control: no-store, etc.); configuration verifiable by header analysis in a test environment. |
| ENC-009 | Verifiable integrity of critical data | - | - | ✔ | Critical data with an integrity verification mechanism (MACs, signatures, checksums); tampering detected and logged; coverage applied to data with business or regulatory impact. |

---

## PRI - Personal Data (engineering) {#pri}

Engineering requirements on personal data: what is collected, how long it is kept, and what the system is able to do with that data. The legal side — legal bases, formal rights, regulatory obligations — does not live in this catalogue: it is a matter for the normative cross-check and the regulatory overlay.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| PRI-001 | Minimisation of the personal data collected | - | ✔ | ✔ | Each personal-data field collected is associated with a recorded purpose; fields without a purpose are removed from the collection flow. |
| PRI-002 | Retention of personal data with a deadline and effective deletion | - | ✔ | ✔ | Personal-data sets have a defined retention period; deletion at the end of the period is carried out and verifiable by sampling or automated evidence. |
| PRI-003 | Technical capability for deletion and export on request | - | ✔ | ✔ | A tested mechanism exists to delete and to export the personal data of an identified data subject, without manual intervention in the database. |
| PRI-004 | Record of purpose per personal-data set | - | ✔ | ✔ | An inventory associates each personal-data set with its purpose and the system that processes it; changes of purpose are recorded. |
| PRI-005 | Documented and applied concept for PII in logs | - | ✔ | ✔ | A documented concept for handling PII in logs exists (what is logged, masked how, for how long) and its application is verified. |

The existing neighbours keep their object: `ENC-005` forbids sensitive data in clear text in logs, outputs and API responses; `ERR-007` requires pseudonymised context in error logs (L2+); `LOG-005` sets the **minimum** retention of logs. `PRI-002` sets the **maximum** retention of business personal data, and `PRI-005` adds what none of them prescribes: the documented and verified concept — it does not repeat the prohibition, it requires the concept.

**Sources.** PRI-001…004 — [authorship] SbD-ToE (reference threat: CWE-359); PRI-005 — DSOMM activity "PII logging concept" (`UNIT-DSOMM-ACTIVITY-613A73DC4F6049DBA6CE4FB7BF8519F9`: "A concept how to log PII is documented and applied") and CWE-359. The sources anchor the derivation; the prescription is an editorial choice of SbD-ToE.

---

## API - API Security {#api}

Requirements specific to API surfaces, which are the most frequent exposure vector in modern applications.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| API-001 | Authentication and authorisation of API calls | ✔ | ✔ | ✔ | Endpoints reject calls without valid authentication/authorisation; anonymous calls fail. |
| API-002 | Unnecessary endpoints removed or hidden | ✔ | ✔ | ✔ | Debug or legacy endpoints not exposed in production; only in controlled test environments. |
| API-003 | Input validation in APIs | ✔ | ✔ | ✔ | Malformed inputs are rejected; logs record the attempt with minimum context. |
| API-004 | Rate limiting and abuse detection | - | ✔ | ✔ | Limit configured and active; excessive calls result in a 429 or a temporary block. |
| API-005 | Protection by TLS and up-to-date certificates | ✔ | ✔ | ✔ | TLS channel mandatory; valid certificates; security headers (HSTS, etc.) active. |
| API-006 | Verification of the SDKs and wrappers used | ✔ | ✔ | ✔ | Dependencies and versions documented in the SBOM; audit of licences and known vulnerabilities. |
| API-007 | Logging and auditing of external calls | - | ✔ | ✔ | External calls logged with the essential data (origin, destination, result, timestamp). |

---

## INT - Messaging and Integrations {#int}

Requirements that ensure security in communications between systems, preventing interception, forgery and injection in integration channels.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| INT-001 | Validation of messages between systems | ✔ | ✔ | ✔ | Malformed messages are rejected or handled in a controlled way; no blind processing. |
| INT-002 | Mutual authentication or secure tokens | ✔ | ✔ | ✔ | Integrations accepted only from authenticated sources; tokens verified and with a defined TTL. |
| INT-003 | Encrypted transmission with TLS | ✔ | ✔ | ✔ | All traffic between systems encrypted with TLS; insecure versions disabled. |
| INT-004 | Prohibition of insecure protocols | ✔ | ✔ | ✔ | Unencrypted protocols (HTTP, FTP, Telnet) rejected or redirected to the secure equivalent. |
| INT-005 | Message signing and integrity | - | ✔ | ✔ | Sensitive messages signed and verified; logs evidence the integrity verification. |
| INT-006 | Cross-validation of origin and destination | - | ✔ | ✔ | Only authorised origins and destinations accepted; rejection logs kept. |
| INT-007 | Monitoring and detection of anomalous patterns | - | - | ✔ | Anomalous behaviour in integration channels triggers alerts; logs analysed periodically. |
| INT-008 | Security and contract review in integrations | - | - | ✔ | Integrations documented with security clauses; review checklist carried out. |
| INT-009 | Idempotent consumers | - | ✔ | ✔ | Reprocessing the same message produces no duplicate effects; idempotence is tested. |
| INT-010 | Dead-letter queue with handling and alarm | - | ✔ | ✔ | Unprocessable messages go to a DLQ; the DLQ has defined handling and an active alarm — it never grows silently. |
| INT-011 | Protection against message replay | - | ✔ | ✔ | Messages carry a unique identifier and a validity window; re-injection outside the window, or duplicated, is rejected and logged. |
| INT-012 | Processing order where semantically required | - | - | ✔ | Where business semantics require ordering, processing guarantees it (partition key, sequencing) and a violation is detectable. |

**Sources (INT-009…012).** [authorship] SbD-ToE — message lifecycle (idempotence, DLQ, replay, ordering); no external anchor in the corpus to date. `INT-011` deals with **message** replay, an object distinct from token replay (`SES-008`).

---

## REQ - Requirements Definition {#req}

Requirements that ensure the systematic incorporation of security into the lifecycle's requirements definition and management process.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| REQ-001 | Inclusion of security requirements | ✔ | ✔ | ✔ | Explicit security requirements in the backlog/documentation; tagged and traceable. |
| REQ-002 | Formal security review of requirements | ✔ | ✔ | ✔ | Review process documented and evidenced; owner identified. |
| REQ-003 | Alignment with risk classification | ✔ | ✔ | ✔ | Mapping between requirements and criticality level available and up to date. |
| REQ-004 | Versioning and management of requirements | ✔ | ✔ | ✔ | Change history available; version control applied to the project's catalogue. |
| REQ-005 | Renewed threat analysis after a requirement change | - | ✔ | ✔ | Relevant changes trigger a threat modelling review; record of the decision available. |
| REQ-006 | Traceability requirement → threat → test | - | ✔ | ✔ | A matrix or tool demonstrates the link between requirements, identified threats and tests. |
| REQ-007 | Iterative review with the teams | - | ✔ | ✔ | Requirement changes discussed, reviewed and recorded in defined cycles. |

---

## DST - Artefact Distribution {#dst}

Requirements that guarantee the integrity and traceability of artefacts throughout the build, publication and distribution process.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| DST-001 | Authenticated and auditable repositories | ✔ | ✔ | ✔ | Mandatory authentication and active logs for access to artefact repositories. |
| DST-002 | Approval for public publication | - | ✔ | ✔ | Publication in a public registry requires approval and formal documentation of the process. |
| DST-003 | Digital signature or checksum | - | ✔ | ✔ | Artefacts signed or validated by hash before publication; automated verification; updates distributed to users or customers carry a published signature or hash, which the product or the installer verifies before installation. |
| DST-004 | Inclusion of an SBOM in the artefacts | - | ✔ | ✔ | SBOM generated and attached to each release; dependency traceability available. |
| DST-005 | Access segregated by role and environment | - | ✔ | ✔ | Only authorised users and automations access production artefacts. |
| DST-006 | Deploy only via a validated pipeline | - | ✔ | ✔ | Artefacts deployed only by a controlled and audited pipeline; no manual deploy to production. |
| DST-007 | Revocation and clean-up of compromised artefacts | ✔ | ✔ | ✔ | Compromised versions are removed promptly; users and dependants notified. |

---

## IDE - Development Tools {#ide}

Requirements that control the development environment as a risk surface, preventing the introduction of vulnerabilities through uncontrolled tools or extensions.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| IDE-001 | Authorised tools and IDEs | ✔ | ✔ | ✔ | Only approved tools are used; list maintained and kept up to date by the organisation. |
| IDE-002 | Updates and vulnerability management | ✔ | ✔ | ✔ | IDEs and tools kept up to date; update history available. |
| IDE-003 | Audit of tool-generated code | - | ✔ | ✔ | Code generated by tools or assistants is reviewed before integration into production. |
| IDE-004 | Extensions and plugins from trusted sources | ✔ | ✔ | ✔ | Only extensions from recognised and verified sources are installed; installation logs. |
| IDE-005 | Control of extension permissions | - | ✔ | ✔ | Extension permissions reviewed; only the necessary ones granted; sandboxed execution. |
| IDE-006 | Limitation of uncontrolled local environments | - | ✔ | ✔ | Use of local environments controlled; network or proxy logs available where applicable. |

---

> For detailed validation per requirement, test methods and expected evidence, see [Requirements Validation](./validacao-requisitos).
> For the traceability model and instantiation in a project, see [Taxonomy and Traceability](./taxonomia-rastreabilidade).
> For the applicability matrix by domain and risk level, see [Controls Matrix by Risk](./matriz-controlos-por-risco).
