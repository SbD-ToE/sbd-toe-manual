---
id: validacao-requisitos
title: Security Requirements Validation
description: Complete model for validating the requirements of the SbD-ToE catalogue - principles, methods by requirement type, lifecycle moments and a detailed plan by domain with operational tag, recommended method and expected evidence.
tags: [validação, requisitos, segurança-aplicacional, evidência, SAST, DAST, auditoria, rastreabilidade, ciclo-de-vida, CI-CD]
sidebar_position: 7
translation:
  source_locale: pt
  source_path: 010-sbd-manual/02-requisitos-seguranca/addon/07-validacao-requisitos.md
  source_sha256: 29f6783bab28ef9a09a513b2c7b410be455ffa695c703023a6419a84597f6f92
  source_commit: 44d2d3451e163f3ad4ab710e3ee2ec8d02f9e02d
  target_sha256: 5e1f4cedc3a7933f15f35c8ee4891aed05f8c50a900e7f2d8ae30a1a7eece04d
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [audit_trail, avaliacao, cycle_iteration, eu_startups, gap_family, lifecycle_phase, mapping, practitioner_manual, requirement_runtime, risk_level, sbdtoe_sbd, threat, traceability, transversal, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 79f8c164a9afdb1bcb219b5345eb9b77b29a1359d519ca25de5ddce4e941390e
  translated_at: 2026-09-27T18:03:21Z
  stamped_at: 2026-09-27T18:03:21Z
  reviewed_by: null
---

# Security Requirements Validation

Validation is the mechanism that converts defined requirements into observable assurance. It is not enough for a requirement to exist in the catalogue - it is necessary to confirm that it has been implemented, that it works as expected and that auditable evidence of this exists. This document prescribes how to do so systematically, proportionally to risk and integrated into the development cycle.

---

## 1) Guiding principles {#1-princípios-orientadores}

Security requirements validation must be:

- **Systematic** - tied to well-defined moments of the lifecycle, not ad hoc;
- **Proportional to risk** - requirements of higher criticality demand deeper and more independent validation;
- **Traceable** - each validation produces an explicit link between requirement, method, result and evidence;
- **Repeatable** - automatable or documented in enough detail for replication;
- **Independent** - whenever possible, performed by someone outside the direct implementation line.

---

## 2) Validation methods {#2-métodos-de-validação}

The choice of method depends on the type of requirement and on the phase in which it is applied. The methods are not mutually exclusive - for critical requirements, combining two or more is the correct approach.

### Static Analysis (SAST) {#análise-estática-sast}

Applies to requirements that translate into code patterns, configurations or predictable structures. It must be run during development and in the build pipeline, and must verify:

- Presence of input validation;
- Use of approved cryptographic libraries and algorithms;
- Absence of hardcoded secrets;
- Control of the authentication and authorisation flow.

Results must be correlated with the project's requirement identifiers (`SEC-Lx-*`).

### Dynamic Analysis (DAST) {#análise-dinâmica-dast}

Applies to requirements that manifest in runtime behaviour. It must be used in a test or pre-production environment. It allows validation of:

- Exposure of endpoints and security headers;
- Behaviour when faced with malicious input;
- Absence of errors or improper disclosures;
- Response to authentication failures or misconfigured authorisation.

### Functional security tests {#testes-funcionais-de-segurança}

These complement dynamic analysis with explicit verification of each requirement's acceptance criteria. They must include:

- Verification of the expected behaviour (positive case);
- Attempt to bypass the control (negative case);
- Coverage of edge cases, restrictions and anticipated failures.

### Structured technical review {#revisão-técnica-estruturada}

Performed by analysts, architects or security staff. Suitable for requirements whose control is distributed or implicit - logical segregation, external dependencies, cross-cutting session control. It must take place after relevant milestones: release candidate, critical pull request, internal audit.

### Continuous validation in CI/CD {#validação-contínua-em-cicd}

Critical requirements must be tied to blocking mechanisms in the pipeline:

- Automated assessments of code and configuration;
- Rejection of builds that violate minimum criteria (absence of MFA, logging, exposed secrets);
- Revalidation with each change in risk (new functionality, new integration).

---

## 3) When to validate {#3-quando-validar}

| SDLC phase | Objective of the validation | Primary method |
|-----------|------------------------|-----------------|
| Planning and definition | Confirmation of the applicability of the requirements | Technical analysis + manual validation |
| Development | Early detection of non-compliance | SAST + code review |
| Testing | Verification of the expected behaviour | Functional tests + DAST |
| Pre-release / delivery | Validation of full compliance | Cross-validation + CI/CD gates |
| Production / operation | Continuous monitoring of active requirements | Revalidation, logging, alerts |

---

## 4) Validation plan by domain {#4-plano-de-validação-por-domínio}

For each requirement of the canonical catalogue the following are given: the reference operational tag, the minimum level of application, the recommended validation method and the expected evidence.

> **Note:** The operational tag uses `SEC-Lx-*` with `Lx` replaced by the project's effective level. Example: `SEC-Lx-AUT-MFA` → `SEC-L2-AUT-MFA` in an L2 project.

---

### AUT - Authentication and Identity {#aut---autenticação-e-identidade}

| ID | Operational tag | Level | Validation method | Expected evidence |
|----|-----------------|:-----:|---------------------|-------------------|
| AUT-001 | SEC-Lx-AUT-MFA | L2+ | Attempt login without a second factor. Confirm rejection and failure logs. | Log of failed authentication without MFA. Screenshot of the block. |
| AUT-002 | SEC-Lx-AUT-PWD | L1+ | Review the active policy. Attempt to set an invalid password. Confirm rejection. | Documented policy. Error or rejection log. |
| AUT-003 | SEC-Lx-AUT-BRUTE | L1+ | Simulate repeated failed attempts. Confirm lockout, CAPTCHA or progressive delay. | Log with failure count. Evidence of lockout or delay. |
| AUT-004 | SEC-Lx-AUT-LOGOUT | L1+ | Log out. Attempt to reuse the session or token. Confirm rejection. | Log of revoked session. Authentication error on reuse. |
| AUT-005 | SEC-Lx-AUT-IDLE | L1+ | Simulate inactivity for the configured period. Confirm expiry and redirect. | Timeout log. Screenshot of automatic expiry. |
| AUT-006 | SEC-Lx-AUT-CRED | L1+ | Validate salted hashing. Verify absence of clear-text credentials in storage and in transit. | Configuration output. Scan result. Absence in the repository. |
| AUT-007 | SEC-Lx-AUT-FED | L2+ | Simulate federated login via SAML/OIDC. Confirm the complete flow and logging. | Log of authentication via external IdP. Screenshot of successful login. |
| AUT-008 | SEC-Lx-AUT-STEPUP | L2+ | Simulate a sensitive action. Confirm that an additional factor is required. | Screenshot of step-up. Log associated with the critical action. |
| AUT-009 | SEC-Lx-AUT-CHANGE | L1+ | Attempt to change credentials without re-authentication. Confirm the block. | Log of the blocked attempt. Evidence of active session verification. |
| AUT-010 | SEC-Lx-AUT-ALERT | L2+ | Simulate an anomalous login. Confirm notification to the user and logging. | Example of the notification sent. Log of the critical event detected. |
| AUT-011 | SEC-Lx-AUT-DEFAULT | L1+ | Verify that no default accounts or credentials are active in the application and in the components in production. Confirm that the initial credential is changed at first use. | Inventory of accounts without default credentials. Evidence of the first-access flow. |

---

### ACC - Access Control {#acc---controlo-de-acesso}

| ID | Operational tag | Level | Validation method | Expected evidence |
|----|-----------------|:-----:|---------------------|-------------------|
| ACC-001 | SEC-Lx-ACC-RBAC | L1+ | Test access with a reduced-privilege role to a restricted resource. Confirm rejection. | Rejection log. Documented role mapping. |
| ACC-002 | SEC-Lx-ACC-PRIV | L1+ | Audit the permissions of user and service accounts. Confirm absence of unnecessary privileges. | Permissions audit report. |
| ACC-003 | SEC-Lx-ACC-BLOCK | L1+ | Attempt unauthorised access. Confirm the block and logging with sufficient context. | Rejection log with context data. |
| ACC-004 | SEC-Lx-ACC-SEP | L1+ | Verify effective separation of profiles. Confirm that each profile's actions are traceable. | Logs with the profile identified. Cross-profile test. |
| ACC-005 | SEC-Lx-ACC-API | L1+ | Test endpoints without authentication/authorisation. Confirm rejection with the appropriate code. | Rejection log. Automated endpoint tests. |
| ACC-006 | SEC-Lx-ACC-DATA | L1+ | Attempt access to critical data with an unauthorised role. Confirm the block and log. | Evidence of an effective control. Log of the event. |
| ACC-007 | SEC-Lx-ACC-MODEL | L2+ | Verify the existence of a reviewed and documented permissions model. | Documentation of the model. Dated review record. |
| ACC-008 | SEC-Lx-ACC-REVOKE | L1+ | Revoke access. Test immediately after revocation. Confirm failure. | Log of the failed attempt after revocation. Revocation timestamp. |
| ACC-009 | SEC-Lx-ACC-ABAC | L3 | Test the access decision with distinct attributes. Confirm enforcement of the dynamic policy. | Logs with attribute evaluation. Test with context variation. |
| ACC-010 | SEC-Lx-ACC-REVIEW | L1+ | Verify the existence of a periodic review process. Confirm removal of obsolete permissions. | Dated review records. Evidence of permissions clean-up. |

---

### LOG - Logging and Monitoring {#log---registo-e-monitorização}

| ID | Operational tag | Level | Validation method | Expected evidence |
|----|-----------------|:-----:|---------------------|-------------------|
| LOG-001 | SEC-Lx-LOG-EVENTS | L1+ | Review the logging configuration. Confirm coverage of accesses, changes and critical failures. | Auditable logs with events mapped by type and context. |
| LOG-002 | SEC-Lx-LOG-ATTRS | L1+ | Analyse the log structure. Confirm the presence of who, when, what and where in each entry. | Log samples with all mandatory attributes. |
| LOG-003 | SEC-Lx-LOG-INTEG | L1+ | Attempt to modify a log on disk. Verify protection mechanisms (hash, write-once, remote syslog). | Evidence of WORM, remote syslog or a tamper-detection mechanism. |
| LOG-004 | SEC-Lx-LOG-REVIEW | L2+ | Confirm the existence of a documented and executed periodic analysis process. | Dated analysis record. Documented procedure. |
| LOG-005 | SEC-Lx-LOG-RETAIN | L1+ | Verify the effective retention period against the defined policy. | Retention configuration. Evidence of logs within the required period. |
| LOG-006 | SEC-Lx-LOG-CENTRAL | L2+ | Confirm forwarding to the central aggregator. Verify the forwarding configuration. | Centralised view with logs per application. |
| LOG-007 | SEC-Lx-LOG-ALERT | L2+ | Generate an anomalous event. Confirm that the alert fires with the configured threshold and channel. | Log of the alert fired with timestamp and detail. |
| LOG-008 | SEC-Lx-LOG-FAIL | L2+ | Disable or block the logging system. Confirm that the failure is detected and alerted. | Logging failure alert. Log of the detection. |
| LOG-009 | SEC-Lx-LOG-IR | L2+ | Simulate an incident or forensic review. Confirm that the logs have enough detail for reconstruction. | Demonstrated ability to reconstruct the event timeline. |
| LOG-010 | SEC-Lx-LOG-BIZ | L3 | Verify logging of critical business events (transactions, high-impact authorisations). | Logs with business events identified and traceable. |

---

### SES - Sessions and State {#ses---sessões-e-estado}

| ID | Operational tag | Level | Validation method | Expected evidence |
|----|-----------------|:-----:|---------------------|-------------------|
| SES-001 | SEC-Lx-SES-IDLE | L1+ | Simulate inactivity for the configured period. Confirm expiry and redirect. | Timeout log. Screenshot of terminated session. |
| SES-002 | SEC-Lx-SES-LOGOUT | L1+ | Log out. Attempt to reuse the token. Change the password and attempt to use the previous token. | Authentication error on reuse. Invalidation log. |
| SES-003 | SEC-Lx-SES-ENTROPY | L1+ | Analyse the generated tokens. Confirm adequate entropy and absence of a predictable pattern. | Token analysis. Absence of predictability demonstrated. |
| SES-004 | SEC-Lx-SES-TLS | L1+ | Intercept traffic with a proxy. Confirm that tokens only travel over TLS. Verify cookie flags. | Response headers. Secure and HttpOnly flags confirmed. |
| SES-005 | SEC-Lx-SES-BIND | L2+ | Change IP or user-agent during an active session. Confirm termination or a revalidation requirement. | Log of session termination due to context change. |
| SES-006 | SEC-Lx-SES-REVOKE | L1+ | Revoke the session via the management interface. Test immediately after revocation. | Immediate authentication error. Explicit revocation log. |
| SES-007 | SEC-Lx-SES-TTL | L2+ | Verify the configured maximum TTL. Attempt to keep the session beyond the limit. | TTL configuration. Evidence of forced expiry. |
| SES-008 | SEC-Lx-SES-JWT | L2+ | Inspect JWTs. Confirm scope and expiry claims. Test the token after revocation. | Decoded JWT with correct claims. Failure after revocation. |

---

### VAL - Data Validation {#val---validação-de-dados}

| ID | Operational tag | Level | Validation method | Expected evidence |
|----|-----------------|:-----:|---------------------|-------------------|
| VAL-001 | SEC-Lx-VAL-INPUT | L1+ | Review the validation code. Send invalid inputs (type, size, format). Confirm rejection. | Invalid input tests. Code with validations. Rejection logs. |
| VAL-002 | SEC-Lx-VAL-WLIST | L1+ | Attempt to send values outside the allowed list. Confirm rejection and absence of implicit handling. | Code with an explicit whitelist. Tests with unexpected values. |
| VAL-003 | SEC-Lx-VAL-SCHEMA | L2+ | Send malformed payloads or payloads with missing fields. Confirm automatic rejection. | Consistent rejections. Contract tests. |
| VAL-004 | SEC-Lx-VAL-SQLI | L1+ | Review the use of prepared statements. Run SAST and SQL injection tests. | Scanner reports. Absence of concatenation in queries. |
| VAL-005 | SEC-Lx-VAL-PREUSE | L1+ | Trace the paths between the input layer and business logic/persistence. Confirm that validation precedes internal use; identify unvalidated paths. | Data-flow analysis with validation points evidenced. Code review confirms absence of unvalidated paths. |
| VAL-006 | SEC-Lx-VAL-SAFE | L1+ | Force a validation error. Confirm that the message to the client does not expose internal logic. | Generic error messages. Absence of technical detail on the client. |
| VAL-007 | SEC-Lx-VAL-AUTO | L2+ | Run automated tests with malicious payloads (XSS, SQLi, path traversal). | Execution reports. Documented case coverage. |
| VAL-008 | SEC-Lx-VAL-XSS | L1+ | Test output on rendered surfaces (HTML, attribute, JS, SQL via prepared statements, shell, logs). Confirm correct contextual encoding. | Tests with XSS/SQLi/log injection payloads. Encoding observable according to the rendering context. |

> Editorial note: VAL-005 covers **pre-use** validation of data (path input → logic/persistence; anchor ACO-IVF-004); VAL-008 covers **output encoding** at rendering (anchor ACO-IVF-008). The controls are complementary — input and output.

---

### ERR - Error Handling {#err---gestão-de-erros}

| ID | Operational tag | Level | Validation method | Expected evidence |
|----|-----------------|:-----:|---------------------|-------------------|
| ERR-001 | SEC-Lx-ERR-LEAK | L1+ | Provoke intentional errors. Confirm that the client receives an abstract message without internal data. | Generic response to the client. Separate detailed internal log. |
| ERR-002 | SEC-Lx-ERR-MSG | L1+ | Verify all error surfaces. Confirm absence of stack traces or technical information. | Screenshots of error messages in different scenarios. |
| ERR-003 | SEC-Lx-ERR-ENUM | L1+ | Test existing and non-existent resources. Confirm identical error responses (no enumeration). | Identical responses for existing and non-existent resources. |
| ERR-004 | SEC-Lx-ERR-I18N | L1+ | Verify messages in different locales. Confirm absence of executable content. | Translated messages without technical or executable references. |
| ERR-005 | SEC-Lx-ERR-CENTRAL | L2+ | Review the error-handling architecture. Confirm centralisation. | Code with a centralised handler. Absence of scattered ad hoc handling. |
| ERR-006 | SEC-Lx-ERR-TEST | L2+ | Run automated tests of error scenarios. Confirm that errors are handled without leakage. | Error test coverage. Execution report. |
| ERR-007 | SEC-Lx-ERR-LOG | L2+ | Review error logs. Confirm absence of personal data, tokens or credentials. | Logs without sensitive data. Pseudonymised contextual IDs. |

---

### CFG - Secure Configuration {#cfg---configuração-segura}

| ID | Operational tag | Level | Validation method | Expected evidence |
|----|-----------------|:-----:|---------------------|-------------------|
| CFG-001 | SEC-Lx-CFG-DEBUG | L1+ | Attempt to access debug or tracing endpoints or admin interfaces. Confirm that they are disabled or protected. | 403/404 response or authentication required. |
| CFG-002 | SEC-Lx-CFG-ENV | L1+ | Verify environment separation. Confirm that deploys and tests only take place in segregated environments. | Logs with the environment identified. Confirmation of segregation. |
| CFG-003 | SEC-Lx-CFG-HARD | L1+ | Run a secrets scan on the repository and the code. Confirm absence of hardcoded secrets. | Clean scan report. Absence of secrets in the history. |
| CFG-004 | SEC-Lx-CFG-EXT | L1+ | Verify that configuration is external to the code. Confirm restrictive permissions on the configuration repository. | External and versioned configuration. Audited permissions. |
| CFG-005 | SEC-Lx-CFG-START | L2+ | Remove a mandatory parameter. Confirm that start-up fails with an explicit error. | Start-up failure log with the cause identified. |
| CFG-006 | SEC-Lx-CFG-VAULT | L2+ | Review secrets management. Confirm use of a vault and absence of local secrets. | Vault configuration. Access policies. Absence of local secrets. |
| CFG-007 | SEC-Lx-CFG-DRIFT | L3 | Change a critical configuration outside the normal process. Confirm detection and alert. | Drift alert. Log of the unexpected change. |

---

### API - API Security {#api---segurança-de-apis}

| ID | Operational tag | Level | Validation method | Expected evidence |
|----|-----------------|:-----:|---------------------|-------------------|
| API-001 | SEC-Lx-API-AUTH | L1+ | Test endpoints without credentials. Confirm 401/403 rejection. | Rejection logs. Automated endpoint tests. |
| API-002 | SEC-Lx-API-EXPOSE | L1+ | Inventory the endpoints exposed in production. Confirm absence of debug or legacy endpoints. | Inventory of active endpoints. Absence of unintended endpoints. |
| API-003 | SEC-Lx-API-INPUT | L1+ | Send invalid payloads. Confirm rejection with the appropriate code. | Rejection logs. Tests with malformed payloads. |
| API-004 | SEC-Lx-API-RATE | L2+ | Execute a burst of calls. Confirm a 429 response or temporary block. | Evidence of rate limiting at runtime or in logs. |
| API-005 | SEC-Lx-API-TLS | L1+ | Verify certificates and TLS version. Confirm that security headers are active. | TLS scanner. Response headers. |
| API-006 | SEC-Lx-API-DEPS | L1+ | Verify the SBOM and documented dependencies. Confirm auditing of known vulnerabilities. | SBOM. Dependency audit report. |
| API-007 | SEC-Lx-API-LOG | L2+ | Verify logs of external calls. Confirm the presence of the essential data. | Logs with origin, destination, result and timestamp. |

---

### INT - Messaging and Integrations {#int---mensagens-e-integrações}

| ID | Operational tag | Level | Validation method | Expected evidence |
|----|-----------------|:-----:|---------------------|-------------------|
| INT-001 | SEC-Lx-INT-VAL | L1+ | Send a malformed message to the integration. Confirm rejection or controlled handling. | Evidence of rejection. No blind processing of invalid messages. |
| INT-002 | SEC-Lx-INT-AUTH | L1+ | Test the integration without a token or with an invalid token. Confirm rejection. | Rejection log. Expired token test. |
| INT-003 | SEC-Lx-INT-TLS | L1+ | Intercept traffic between systems. Confirm that TLS encryption is active. Verify supported versions. | TLS scanner. Encrypted connection logs. |
| INT-004 | SEC-Lx-INT-PROTO | L1+ | Attempt communication over an insecure protocol. Confirm rejection or redirect. | Error or redirect to the secure protocol. Rejection log. |
| INT-005 | SEC-Lx-INT-SIGN | L2+ | Send a message with an invalid or missing signature. Confirm rejection and log. | Evidence of integrity verification. Validation failure log. |
| INT-006 | SEC-Lx-INT-ORIGIN | L2+ | Send a message from an unauthorised origin. Confirm rejection. | Rejection log with the origin identified. List of authorised origins. |
| INT-007 | SEC-Lx-INT-ANOMALY | L3 | Simulate an anomalous communication pattern. Confirm the alert. | Alert fired. Log with the context of the detected pattern. |
| INT-008 | SEC-Lx-INT-REVIEW | L3 | Verify the integration documentation and the security clauses in the contracts. | Integration documentation. Contractual security clauses. |

---

### REQ - Requirements Definition {#req---definição-de-requisitos}

| ID | Operational tag | Level | Validation method | Expected evidence |
|----|-----------------|:-----:|---------------------|-------------------|
| REQ-001 | SEC-Lx-REQ-INC | L1+ | Verify the existence of security requirements in the backlog/documentation. | Requirements marked and traceable in the backlog. |
| REQ-002 | SEC-Lx-REQ-REV | L1+ | Verify the existence of an executed and documented review process. | Review record with the person responsible identified. |
| REQ-003 | SEC-Lx-REQ-RISK | L1+ | Confirm the mapping between requirements and criticality level. | Up-to-date applicability matrix. |
| REQ-004 | SEC-Lx-REQ-VER | L1+ | Verify the change history of the project's catalogue. | Active version control. History available. |
| REQ-005 | SEC-Lx-REQ-TM | L2+ | Confirm that relevant changes trigger a threat model review. | Decision record associated with the change. |
| REQ-006 | SEC-Lx-REQ-TRACE | L2+ | Verify traceability requirement → threat → test. | Matrix or tool with explicit links. |
| REQ-007 | SEC-Lx-REQ-ITER | L2+ | Confirm the existence of review cycles with the teams. | Dated iterative review records. |

---

### DST - Artefact Distribution {#dst---distribuição-de-artefactos}

| ID | Operational tag | Level | Validation method | Expected evidence |
|----|-----------------|:-----:|---------------------|-------------------|
| DST-001 | SEC-Lx-DST-REPO | L1+ | Test access to the repository without authentication. Confirm rejection and active logs. | Rejection of anonymous access. Access logs. |
| DST-002 | SEC-Lx-DST-PUB | L2+ | Verify the approval process for public publication. Confirm documentation. | Approval record. Process documentation. |
| DST-003 | SEC-Lx-DST-SIGN | L2+ | Verify the signature or checksum of the artefacts. Confirm automated verification. | Signed artefacts. Verification script or pipeline. |
| DST-004 | SEC-Lx-DST-SBOM | L2+ | Confirm generation and attachment of an SBOM per release. | SBOM available and traceable per version. |
| DST-005 | SEC-Lx-DST-ACCESS | L2+ | Verify that only authorised users and automation access production artefacts. | Access policies. Permissions audit. |
| DST-006 | SEC-Lx-DST-PIPE | L2+ | Attempt a manual deploy to production. Confirm the block. | Evidence of the pipeline as the only deploy path. |
| DST-007 | SEC-Lx-DST-REVOKE | L1+ | Verify the removal and notification process for compromised artefacts. | Revocation record. Evidence of notification. |

---

### IDE - Development Tools {#ide---ferramentas-de-desenvolvimento}

| ID | Operational tag | Level | Validation method | Expected evidence |
|----|-----------------|:-----:|---------------------|-------------------|
| IDE-001 | SEC-Lx-IDE-AUTH | L1+ | Verify the list of authorised tools and IDEs and whether it is up to date. | Maintained list. Evidence of approval of the tools in use. |
| IDE-002 | SEC-Lx-IDE-UPD | L1+ | Verify the versions of IDEs and tools in use. Confirm that updates have been applied. | Update history. Current versions documented. |
| IDE-003 | SEC-Lx-IDE-GEN | L2+ | Review samples of generated code. Confirm the existence of a review process before integration. | Evidence of review of generated code. Pull request with documented review. |
| IDE-004 | SEC-Lx-IDE-EXT | L1+ | Verify the list of installed extensions. Confirm that they come from recognised sources. | List of extensions with documented origin. |
| IDE-005 | SEC-Lx-IDE-PERM | L2+ | Verify the permissions granted to extensions. Confirm that only the necessary ones are active. | Reviewed permissions. Sandboxed execution confirmed. |
| IDE-006 | SEC-Lx-IDE-LOCAL | L2+ | Verify control over the use of local environments. Confirm the existence of logs or a proxy where applicable. | Policy on the use of local environments. Network or proxy logs. |

### PRI - Personal Data (engineering) {#pri---dados-pessoais-engenharia}

| ID | Operational tag | Level | Validation method | Expected evidence |
|----|-----------------|:-----:|---------------------|-------------------|
| PRI-001 | SEC-Lx-PRI-MIN | L1+ | Compare the personal-data fields collected with the register of purposes. Confirm there are no fields without a purpose. | List of fields with their associated purpose. |
| PRI-002 | SEC-Lx-PRI-RETAIN | L1+ | Check the defined periods and sample records beyond the period, including replicas and downstream systems. Confirm the declared period for backups. | Retention configuration. Evidence of deletion or anonymisation by sampling. |
| PRI-003 | SEC-Lx-PRI-RIGHTS | L1+ | Run export, rectification and deletion for a test data subject. Confirm the machine-readable format, downstream propagation and identity verification for requests outside the authenticated channel. | Exported file. Log of the executions. Evidence of propagation. |
| PRI-004 | SEC-Lx-PRI-INVENTORY | L2+ | Review the inventory. Confirm purpose, system and recipients per data set, and the record of changes. | Up-to-date inventory with change history. |
| PRI-005 | SEC-Lx-PRI-LOGPII | L2+ | Review the PII-in-logs concept and sample logs. In immutable logs, confirm pseudonyms and per-person keys. | Documented concept. Compliant log samples. |
| PRI-006 | SEC-Lx-PRI-CONSENT | L1+ | Give and withdraw consent (or object) with a test data subject. Confirm the auditable record, equivalent effort, effect on the dependent processing and persistence after synchronisation. | Consent record with the version of the text. Evidence of the effect of the withdrawal. |
| PRI-007 | SEC-Lx-PRI-DEFAULT | L1+ | Create a new account and check the initial sharing, visibility and optional-processing settings. | Screenshot or automated test of the default settings. |

---

## 5) Expected results of validation {#5-resultados-esperados-da-validação}

Each validated requirement must produce:

- **Evidence of execution** - report, log, validation artefact, screenshot;
- **Result** - compliant / non-compliant / partial, with enough context for a decision;
- **Link to the identifier** - the project's operational tag (`SEC-L2-AUT-MFA`) and canonical ID (`AUT-001`);
- **Corrective measure**, where applicable - action, person responsible, deadline.

---

## 6) Continuous improvement {#6-melhoria-contínua}

Validation must be incorporated into a continuous improvement cycle, with the methods:

- **Reviewed on the basis of real incidents or findings** - a recurring finding indicates a gap in the method, not only in the control;
- **Updated with new techniques** or changes to the catalogue;
- **Automated whenever possible**, to guarantee consistent and scalable coverage;
- **Monitored with indicators** - percentage of requirements validated per release, mean time to detect non-compliance.

---

## Cross-references {#referências-cruzadas}

| Document | Relationship |
|-----------|---------|
| [Base Requirements Catalogue](./lista-requisitos-base) | Defines the requirements and acceptance criteria to validate |
| [Taxonomy and Traceability](./taxonomia-rastreabilidade) | Defines the canonical IDs and operational tags used in this document |
| [Controls Matrix by Risk](./matriz-controlos-por-risco) | Indicates applicability by domain and risk level |
| [Traceability and Controls](./rastreabilidade-controlo) | Matrix model risk → requirement → control → evidence |
| [Exception Management](./gestao-excecoes) | Process for requirements that cannot be validated or met |
