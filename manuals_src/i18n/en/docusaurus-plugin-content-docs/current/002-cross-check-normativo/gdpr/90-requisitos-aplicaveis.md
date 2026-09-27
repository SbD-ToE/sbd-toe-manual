---
id: requisitos-aplicaveis
title: "Applicable requirements — Processing of personal data (GDPR)"
description: "Generated view: the Manual's requirements that apply under context CTX-RGPD, by level and grade, with each floor that the regime elevates and its legal basis."
sidebar_position: 90
tags: [cross-check, gdpr, requisitos, overlay, gerado]
sbdtoe_generated: reg-requirements-view
derived_from:
  - 010-sbd-manual/01-classificacao-aplicacoes/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/02-requisitos-seguranca/addon/02-lista-requisitos-base.md
  - 010-sbd-manual/02-requisitos-seguranca/addon/09-governaca-automatismos.md
  - 010-sbd-manual/03-threat-modeling/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/04-arquitetura-segura/addon/01-catalogo-requisitos.md
  - 010-sbd-manual/05-dependencias-sbom-sca/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/06-desenvolvimento-seguro/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/07-cicd-seguro/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/08-iac-infraestrutura/addon/08-matriz-requisitos-iac.md
  - 010-sbd-manual/09-containers-imagens/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/10-testes-seguranca/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/11-deploy-seguro/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/12-monitorizacao-operacoes/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/13-formacao-onboarding/addon/00-catalogo-requisitos.md
  - 010-sbd-manual/14-governanca-contratacao/addon/00-catalogo-requisitos.md
  - 002-cross-check-normativo/_contextos-regulatorios.yaml
  - 002-cross-check-normativo/_matriz/rgpd.yaml
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/gdpr/90-requisitos-aplicaveis.md
  source_sha256: bd2fbe7876f40de142d33cb3ad23e94b62b638b6b7c457913fba55c0eb30128c
  source_commit: null
  target_sha256: 6bdb16ac4f3f622444340cc048eecf25e4e55381dce43b0f9d60831e036be73c
  engine: gen_reg_views
  prompt_sha256: null
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: []
  glossary_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
  translated_at: 2026-09-27T00:00:00Z
  stamped_at: 2026-09-27T00:00:00Z
  reviewed_by: null
---

# Applicable requirements: Processing of personal data (GDPR)

> **Generated page**, produced by `scripts/gen_reg_views.py` from the requirement catalogues and from `002-cross-check-normativo/_contextos-regulatorios.yaml`. It is not edited by hand: each requirement's catalogue is the canonical source, and this page is a view of the regulatory overlay.

For context **CTX-RGPD**, this page brings together the Manual's base selection per level and each **floor** that the regime elevates, with the obligation that grounds it. A context never lowers a minimum of the Manual.

## When it applies {#quando-se-aplica}

The application processes personal data. The declaration is always explicit (yes or no) and is never inferred from the data sensitivity classification. Declared per application.

> Regulation (EU) 2016/679, Article 2(1): “This Regulation applies to the processing of personal data wholly or partly by automated means”

## Context floor list {#pisos}

| Floor | Target | Grade | Required floor | Scope | Legal basis | Justification of non-applicability |
|---|---|---|---|---|---|---|
| CTX-RGPD-P01 | [Policy 33 §10.7](/sbd-toe/assets/policies/policy-contratacao-segura#107-operacionalização) | — | mandatory | Article 28(3) contract mandatory at any level whenever a processor processes personal data. | Regulation (EU) 2016/679, Article 28(3): “Processing by a processor shall be governed by a contract” (RGPD-28-3) | admitted |
| CTX-RGPD-P02 | [Policy 18 §10.3](/sbd-toe/assets/policies/policy-gestao-segredos#103-sub-processadores) | — | mandatory | Article 28(3) contract with the processors that receive personal data in prompts, at any level. | Regulation (EU) 2016/679, Article 28(3): “Processing by a processor shall be governed by a contract” (RGPD-28-3) | admitted |
| CTX-RGPD-P03 | `OPS-016` | — | mandatory | Personal data included in the backups, with tested restore. | Regulation (EU) 2016/679, Article 32(1), point (c): “the ability to restore the availability and access to personal data in a timely manner in the event of a physical or technical incident” (RGPD-32-1-c) | not admitted |

## How to read the list {#como-se-le}

Key: ✔ base selection for the level; ▲ elevated or added by the regime (applies by the regime; if the component does not exist, a documented justification of non-applicability is required); — not selected.

**Activation rule.** Effective requirements = technical selection ∪ elevated ∪ added. Ids with origin “base” enter only if the technical selection (the application's technical context) activates them. An elevated or added id without technical activation is not dropped silently: it enters flagged “applies by the regime; if the component does not exist, a documented justification of non-applicability is required” (model of Implementing Regulation (EU) 2024/2690, Article 2).

## Requirement list — context (no grade) {#lista-contexto}

| Requirement | Name | L1 | L2 | L3 | Floor ids |
|---|---|:--:|:--:|:--:|---|
| `CLA-001` | Formal classification according to the risk axes model | ✔ | ✔ | ✔ | — |
| `CLA-002` | Approval proportional to the assigned risk level | ✔ | ✔ | ✔ | — |
| `CLA-003` | Activation of baseline controls determined by the classification | ✔ | ✔ | ✔ | — |
| `CLA-004` | Reclassification criteria documented and monitored | ✔ | ✔ | ✔ | — |
| `CLA-005` | Periodic classification review cycle differentiated by level | ✔ | ✔ | ✔ | — |
| `CLA-006` | Classification reassessment after a significant change event | ✔ | ✔ | ✔ | — |
| `CLA-007` | Residual risk with formalised compensation, owner and TTL | — | ✔ | ✔ | — |
| `CLA-008` | Application inventory kept up to date and accessible for audit | ✔ | ✔ | ✔ | — |
| `AUT-001` | Mandatory MFA | — | ✔ | ✔ | — |
| `AUT-002` | Password policy | ✔ | ✔ | ✔ | — |
| `AUT-003` | Brute-force protection | ✔ | ✔ | ✔ | — |
| `AUT-004` | Active session revocation | ✔ | ✔ | ✔ | — |
| `AUT-005` | Automatic session expiry | ✔ | ✔ | ✔ | — |
| `AUT-006` | No credentials in clear text | ✔ | ✔ | ✔ | — |
| `AUT-007` | Support for federated authentication | — | ✔ | ✔ | — |
| `AUT-008` | Step-up for sensitive actions | — | ✔ | ✔ | — |
| `AUT-009` | Re-authentication for critical changes | ✔ | ✔ | ✔ | — |
| `AUT-010` | Alert on suspicious access | — | ✔ | ✔ | — |
| `ACC-001` | RBAC access control | ✔ | ✔ | ✔ | — |
| `ACC-002` | Principle of least privilege | ✔ | ✔ | ✔ | — |
| `ACC-003` | Blocking and auditing of illegitimate access | ✔ | ✔ | ✔ | — |
| `ACC-004` | Separation of profiles | ✔ | ✔ | ✔ | — |
| `ACC-005` | Access control for APIs and services | ✔ | ✔ | ✔ | — |
| `ACC-006` | Protection of sensitive resources | ✔ | ✔ | ✔ | — |
| `ACC-007` | Validation of the access model | — | ✔ | ✔ | — |
| `ACC-008` | Real-time revocation | ✔ | ✔ | ✔ | — |
| `ACC-009` | Attribute-based authorisation (ABAC) | — | — | ✔ | — |
| `ACC-010` | Periodic review of permissions | — | ✔ | ✔ | — |
| `LOG-001` | Logging of critical events | ✔ | ✔ | ✔ | — |
| `LOG-002` | Minimum attributes in logs | ✔ | ✔ | ✔ | — |
| `LOG-003` | Protection of log integrity and access | ✔ | ✔ | ✔ | — |
| `LOG-004` | Periodic log analysis | — | ✔ | ✔ | — |
| `LOG-005` | Minimum log retention | ✔ | ✔ | ✔ | — |
| `LOG-006` | Forwarding to a centralised system | — | ✔ | ✔ | — |
| `LOG-007` | Classification and anomaly detection | — | ✔ | ✔ | — |
| `LOG-008` | Alarm on failures of the logging mechanism | — | ✔ | ✔ | — |
| `LOG-009` | Logs support incident response | — | ✔ | ✔ | — |
| `LOG-010` | Logging of critical business events | — | — | ✔ | — |
| `SES-001` | Automatic expiry on inactivity | ✔ | ✔ | ✔ | — |
| `SES-002` | Manual logout and logout after credential change | ✔ | ✔ | ✔ | — |
| `SES-003` | Unpredictable session identifiers | ✔ | ✔ | ✔ | — |
| `SES-004` | Secure transmission of tokens | ✔ | ✔ | ✔ | — |
| `SES-005` | Binding of the session to the client context | — | ✔ | ✔ | — |
| `SES-006` | Explicit session revocation | ✔ | ✔ | ✔ | — |
| `SES-007` | Prevention of long-lived sessions | — | ✔ | ✔ | — |
| `SES-008` | Scope, TTL and revocation of JWT tokens | — | ✔ | ✔ | — |
| `VAL-001` | General validation of external inputs | ✔ | ✔ | ✔ | — |
| `VAL-002` | Use of whitelists instead of blacklists | ✔ | ✔ | ✔ | — |
| `VAL-003` | Schema validators (JSON/XML schema) | — | ✔ | ✔ | — |
| `VAL-004` | Sanitisation against injections | ✔ | ✔ | ✔ | — |
| `VAL-005` | Validation before internal use | ✔ | ✔ | ✔ | — |
| `VAL-006` | Safe error messages in validation | ✔ | ✔ | ✔ | — |
| `VAL-007` | Automated tests against malicious inputs | — | ✔ | ✔ | — |
| `VAL-008` | Output encoding/escaping on rendering (anti-XSS) | ✔ | ✔ | ✔ | — |
| `FIL-001` | Processable size limit per upload | ✔ | ✔ | ✔ | — |
| `FIL-002` | Type validation by content, not only by extension | ✔ | ✔ | ✔ | — |
| `FIL-003` | Safe handling of compressed archives | — | ✔ | ✔ | — |
| `FIL-004` | Storage quota per user | — | ✔ | ✔ | — |
| `FIL-005` | Storage outside the served tree, with generated names | ✔ | ✔ | ✔ | — |
| `FIL-006` | Serving files in an inert context | — | ✔ | ✔ | — |
| `FIL-007` | Anti-malware scanning of files of untrusted origin | — | ✔ | ✔ | — |
| `FIL-008` | Image dimension limit (pixel flood) | — | ✔ | ✔ | — |
| `ERR-001` | Errors do not expose sensitive data | ✔ | ✔ | ✔ | — |
| `ERR-002` | Generic messages on the client | ✔ | ✔ | ✔ | — |
| `ERR-003` | No disclosure of resource existence | ✔ | ✔ | ✔ | — |
| `ERR-004` | Localised and safe messages | ✔ | ✔ | ✔ | — |
| `ERR-005` | Standardised and centralised handling | — | ✔ | ✔ | — |
| `ERR-006` | Automated tests for excessive errors | — | ✔ | ✔ | — |
| `ERR-007` | Error logs with pseudonymised context | — | ✔ | ✔ | — |
| `CFG-001` | Debug and flags disabled in production | ✔ | ✔ | ✔ | — |
| `CFG-002` | Environment separation with automated validation | ✔ | ✔ | ✔ | — |
| `CFG-003` | No hardcoded parameters | ✔ | ✔ | ✔ | — |
| `CFG-004` | External configuration with controlled permissions | ✔ | ✔ | ✔ | — |
| `CFG-005` | Configuration validation at start-up | — | ✔ | ✔ | — |
| `CFG-006` | Use of vaults and secure secrets management | — | ✔ | ✔ | — |
| `CFG-007` | Configuration drift monitoring | — | — | ✔ | — |
| `ENC-001` | Encryption of all communications in transit | ✔ | ✔ | ✔ | — |
| `ENC-002` | Encryption of sensitive data at rest | — | ✔ | ✔ | — |
| `ENC-003` | Robust cryptographic algorithms and configurations | — | ✔ | ✔ | — |
| `ENC-004` | Adaptive password hashing | ✔ | ✔ | ✔ | — |
| `ENC-005` | Masking of sensitive data in logs, outputs and API responses | ✔ | ✔ | ✔ | — |
| `ENC-006` | Detection and prevention of secrets exposed in repositories | ✔ | ✔ | ✔ | — |
| `ENC-007` | Periodic rotation of keys and secrets | — | ✔ | ✔ | — |
| `ENC-008` | Prevention of client-side caching of sensitive data | — | ✔ | ✔ | — |
| `ENC-009` | Verifiable integrity of critical data | — | — | ✔ | — |
| `PRI-001` | Minimisation of the personal data collected | — | ✔ | ✔ | — |
| `PRI-002` | Retention of personal data with a deadline and effective deletion | — | ✔ | ✔ | — |
| `PRI-003` | Technical capability for deletion and export on request | — | ✔ | ✔ | — |
| `PRI-004` | Record of purpose per personal-data set | — | ✔ | ✔ | — |
| `PRI-005` | Documented and applied concept for PII in logs | — | ✔ | ✔ | — |
| `API-001` | Authentication and authorisation of API calls | ✔ | ✔ | ✔ | — |
| `API-002` | Unnecessary endpoints removed or hidden | ✔ | ✔ | ✔ | — |
| `API-003` | Input validation in APIs | ✔ | ✔ | ✔ | — |
| `API-004` | Rate limiting and abuse detection | — | ✔ | ✔ | — |
| `API-005` | Protection by TLS and up-to-date certificates | ✔ | ✔ | ✔ | — |
| `API-006` | Verification of the SDKs and wrappers used | ✔ | ✔ | ✔ | — |
| `API-007` | Logging and auditing of external calls | — | ✔ | ✔ | — |
| `INT-001` | Validation of messages between systems | ✔ | ✔ | ✔ | — |
| `INT-002` | Mutual authentication or secure tokens | ✔ | ✔ | ✔ | — |
| `INT-003` | Encrypted transmission with TLS | ✔ | ✔ | ✔ | — |
| `INT-004` | Prohibition of insecure protocols | ✔ | ✔ | ✔ | — |
| `INT-005` | Message signing and integrity | — | ✔ | ✔ | — |
| `INT-006` | Cross-validation of origin and destination | — | ✔ | ✔ | — |
| `INT-007` | Monitoring and detection of anomalous patterns | — | — | ✔ | — |
| `INT-008` | Security and contract review in integrations | — | — | ✔ | — |
| `INT-009` | Idempotent consumers | — | ✔ | ✔ | — |
| `INT-010` | Dead-letter queue with handling and alarm | — | ✔ | ✔ | — |
| `INT-011` | Protection against message replay | — | ✔ | ✔ | — |
| `INT-012` | Processing order where semantically required | — | — | ✔ | — |
| `REQ-001` | Inclusion of security requirements | ✔ | ✔ | ✔ | — |
| `REQ-002` | Formal security review of requirements | ✔ | ✔ | ✔ | — |
| `REQ-003` | Alignment with risk classification | ✔ | ✔ | ✔ | — |
| `REQ-004` | Versioning and management of requirements | ✔ | ✔ | ✔ | — |
| `REQ-005` | Renewed threat analysis after a requirement change | — | ✔ | ✔ | — |
| `REQ-006` | Traceability requirement → threat → test | — | ✔ | ✔ | — |
| `REQ-007` | Iterative review with the teams | — | ✔ | ✔ | — |
| `DST-001` | Authenticated and auditable repositories | ✔ | ✔ | ✔ | — |
| `DST-002` | Approval for public publication | — | ✔ | ✔ | — |
| `DST-003` | Digital signature or checksum | — | ✔ | ✔ | — |
| `DST-004` | Inclusion of an SBOM in the artefacts | — | ✔ | ✔ | — |
| `DST-005` | Access segregated by role and environment | — | ✔ | ✔ | — |
| `DST-006` | Deploy only via a validated pipeline | — | ✔ | ✔ | — |
| `DST-007` | Revocation and clean-up of compromised artefacts | ✔ | ✔ | ✔ | — |
| `IDE-001` | Authorised tools and IDEs | ✔ | ✔ | ✔ | — |
| `IDE-002` | Updates and vulnerability management | ✔ | ✔ | ✔ | — |
| `IDE-003` | Audit of tool-generated code | — | ✔ | ✔ | — |
| `IDE-004` | Extensions and plugins from trusted sources | ✔ | ✔ | ✔ | — |
| `IDE-005` | Control of extension permissions | — | ✔ | ✔ | — |
| `IDE-006` | Limitation of uncontrolled local environments | — | ✔ | ✔ | — |
| `REQ-AGN-001` | Registered and versioned mandate | ✔ | ✔ | ✔ | — |
| `REQ-AGN-002` | Autonomy level classified by context | ✔ | ✔ | ✔ | — |
| `REQ-AGN-003` | Documented and tested operational kill-switch | — | ✔ | ✔ | — |
| `REQ-AGN-004` | Intent declaration before a destructive tool-call | — | ✔ | ✔ | — |
| `THR-001` | Formal threat modelling in L2+ applications and significant architectural changes | — | ✔ | ✔ | — |
| `THR-002` | Current architecture represented with explicit DFDs and trust boundaries | — | ✔ | ✔ | — |
| `THR-003` | Structured methodology applied with guaranteed minimum coverage | — | ✔ | ✔ | — |
| `THR-004` | Formal disposition of each identified threat, with an owner | — | ✔ | ✔ | — |
| `THR-005` | Traceability threat → requirement → backlog → validation | — | ✔ | ✔ | — |
| `THR-006` | Threat model versioned and updated within the cycle or after a trigger | — | ✔ | ✔ | — |
| `THR-007` | Independent review by AppSec before go-live in L2 and L3 | — | ✔ | ✔ | — |
| `THR-008` | Threat modelling extended to systems with AI/ML components | — | ✔ | ✔ | — |
| `ARC-001` | Trust zones identified and documented | ✔ | ✔ | ✔ | — |
| `ARC-002` | External exposure minimised and justified | ✔ | ✔ | ✔ | — |
| `ARC-003` | Security-focused architecture review | — | ✔ | ✔ | — |
| `ARC-004` | Architecture decisions documented | — | ✔ | ✔ | — |
| `ARC-005` | Threat modelling integrated into critical flows | — | ✔ | ✔ | — |
| `ARC-006` | Technical isolation controls between sensitive domains | ✔ | ✔ | ✔ | — |
| `ARC-007` | Reusable and approved architecture patterns | — | ✔ | ✔ | — |
| `ARC-008` | Data flows between trust zones protected | ✔ | ✔ | ✔ | — |
| `ARC-009` | Significant changes trigger a new review | — | ✔ | ✔ | — |
| `ARC-010` | Architecture diagrams versioned and accessible | ✔ | ✔ | ✔ | — |
| `ARC-011` | Logical and physical segmentation between environments | — | — | ✔ | — |
| `ARC-012` | Formal approval criteria for high-risk applications | — | — | ✔ | — |
| `ARC-013` | Automatic topology validation in CI/CD or as code | — | — | ✔ | — |
| `ARC-014` | Architectural patterns specific to systems with AI/ML components | — | ✔ | ✔ | — |
| `ARC-015` | AI agents operate as isolated principals with a mandate and least privilege | — | ✔ | ✔ | — |
| `DEP-001` | SBOM generated per build, in a standardised format | ✔ | ✔ | ✔ | — |
| `DEP-002` | SCA integrated into the pipeline with blocking by severity policy | ✔ | ✔ | ✔ | — |
| `DEP-003` | Dependency versions pinned and auditable | ✔ | ✔ | ✔ | — |
| `DEP-004` | Prohibition of dependencies introduced by manual copying | ✔ | ✔ | ✔ | — |
| `DEP-005` | Controlled registries and source repositories | — | ✔ | ✔ | — |
| `DEP-006` | Formal approval for the introduction of new dependencies | — | ✔ | ✔ | — |
| `DEP-007` | Update policy with an SLA defined by severity | ✔ | ✔ | ✔ | — |
| `DEP-008` | Automated updates with impact analysis | — | ✔ | ✔ | — |
| `DEP-009` | Detection of unintended or emergent dependencies | — | — | ✔ | — |
| `DEP-010` | SBOM → vulnerability → fix traceability | — | ✔ | ✔ | — |
| `DEP-011` | Inventory and provenance of AI/ML dependencies | — | ✔ | ✔ | — |
| `DEP-012` | AI BOM generated per build in a standardised format | — | ✔ | ✔ | — |
| `DEP-013` | Explicit pinned version for AI models and providers | — | ✔ | ✔ | — |
| `DEP-014` | List of approved AI providers with risk classification | — | ✔ | ✔ | — |
| `DEV-001` | Secure code guidelines versioned and approved per stack | ✔ | ✔ | ✔ | — |
| `DEV-002` | Security linters and rulesets configured and enforced | ✔ | ✔ | ✔ | — |
| `DEV-003` | Static analysis (SAST) integrated as an integration gate | ✔ | ✔ | ✔ | — |
| `DEV-004` | Code review with a security checklist for critical components | ✔ | ✔ | ✔ | — |
| `DEV-005` | Formal management of technical exceptions and deviations from guidelines | — | ✔ | ✔ | — |
| `DEV-006` | Provenance of incorporated code identified and controlled | — | ✔ | ✔ | — |
| `DEV-007` | Explicit technical constraints for AI-generated code | — | ✔ | ✔ | — |
| `DEV-008` | Quality profiles with minimum security thresholds by risk level | — | ✔ | ✔ | — |
| `DEV-009` | Traceable security annotations in code and tests | — | — | ✔ | — |
| `CIC-001` | Pipelines as code, versioned and subject to review | ✔ | ✔ | ✔ | — |
| `CIC-002` | Triggers controlled and restricted to authorised sources | ✔ | ✔ | ✔ | — |
| `CIC-003` | Secure management of secrets in the pipeline | ✔ | ✔ | ✔ | — |
| `CIC-004` | Mandatory security gates before promotion between environments | ✔ | ✔ | ✔ | — |
| `CIC-005` | Complete traceability of each pipeline run | ✔ | ✔ | ✔ | — |
| `CIC-006` | Isolation of runners and execution environments | — | ✔ | ✔ | — |
| `CIC-007` | Verifiable integrity and provenance of the artefacts produced | — | ✔ | ✔ | — |
| `CIC-008` | Separation of responsibilities between build, test and deploy | — | ✔ | ✔ | — |
| `CIC-009` | Pipeline credentials with minimum scope and defined rotation | — | ✔ | ✔ | — |
| `CIC-010` | Protection against execution of unauthorised code on runners | — | — | ✔ | — |
| `CIC-011` | Promotion between environments attributable to an identified owner | — | ✔ | ✔ | — |
| `IAC-001` | Authenticated remote backend with active locking | — | ✔ | ✔ | — |
| `IAC-002` | Segregated and versioned environments | ✔ | ✔ | ✔ | — |
| `IAC-003` | Mandatory automated validations in the pipeline | ✔ | ✔ | ✔ | — |
| `IAC-004` | Reused modules with a trusted origin and an immutable version | — | ✔ | ✔ | — |
| `IAC-005` | Complete history with versioning, tags and releases | ✔ | ✔ | ✔ | — |
| `IAC-006` | Formal naming, tagging and layout conventions | — | ✔ | ✔ | — |
| `IAC-007` | Traceable and approved plan before any apply | — | ✔ | ✔ | — |
| `IAC-008` | Traceability file → resource → environment | — | ✔ | ✔ | — |
| `IAC-009` | Automated enforcement of policies in the pipeline | — | — | ✔ | — |
| `IAC-010` | Plan artefacts and manifests versioned and hashed | — | ✔ | ✔ | — |
| `IAC-011` | Secure management of secrets - prohibition of hardcoding | ✔ | ✔ | ✔ | — |
| `IAC-012` | Automated detection of drift between IaC and actual state | — | ✔ | ✔ | — |
| `IAC-013` | Formal periodic review of modules and templates | — | — | ✔ | — |
| `CNT-001` | Base images from a trusted and approved origin | ✔ | ✔ | ✔ | — |
| `CNT-002` | Vulnerability scanning of images in the CI/CD | ✔ | ✔ | ✔ | — |
| `CNT-003` | Minimal images - absence of unnecessary components | ✔ | ✔ | ✔ | — |
| `CNT-004` | Execution as a non-root user | ✔ | ✔ | ✔ | — |
| `CNT-005` | Read-only file system at runtime | — | ✔ | ✔ | — |
| `CNT-006` | Restriction of kernel capabilities and syscall profiles | — | ✔ | ✔ | — |
| `CNT-007` | Signing and provenance verification of images | — | ✔ | ✔ | — |
| `CNT-008` | SBOM per published image | — | ✔ | ✔ | — |
| `CNT-009` | Active admission control policies | — | ✔ | ✔ | — |
| `CNT-010` | Periodic renewal of base images | ✔ | ✔ | ✔ | — |
| `CNT-011` | Access to the registry with authentication and traceability | ✔ | ✔ | ✔ | — |
| `CNT-012` | Namespace isolation and network policies in Kubernetes | — | — | ✔ | — |
| `TST-001` | Formal security testing strategy by risk level | ✔ | ✔ | ✔ | — |
| `TST-002` | SAST with a managed coverage profile and false-positive baseline | ✔ | ✔ | ✔ | — |
| `TST-003` | Formal findings management with remediation SLA by severity | ✔ | ✔ | ✔ | — |
| `TST-004` | Reproducible, auditable test evidence linked to the build | ✔ | ✔ | ✔ | — |
| `TST-005` | DAST integrated in a staging environment before promotion | — | ✔ | ✔ | — |
| `TST-006` | Security regression tests for fixed vulnerabilities | — | ✔ | ✔ | — |
| `TST-007` | Minimum security test coverage thresholds by risk | — | ✔ | ✔ | — |
| `TST-008` | Periodic penetration tests with defined scope and methodology | — | ✔ | ✔ | — |
| `TST-009` | Systematic fuzzing of components processing complex input | — | — | ✔ | — |
| `TST-010` | IAST in a staging environment for behavioural validation at runtime | — | — | ✔ | — |
| `DPL-001` | Mandatory formal approval before deployment to production | ✔ | ✔ | ✔ | — |
| `DPL-002` | Promotion only of artefacts with verified provenance | ✔ | ✔ | ✔ | — |
| `DPL-003` | Automated security gates as a condition of promotion | ✔ | ✔ | ✔ | — |
| `DPL-004` | End-to-end traceability of each deployment | ✔ | ✔ | ✔ | — |
| `DPL-005` | Rollback configured, tested and with a defined SLA | ✔ | ✔ | ✔ | — |
| `DPL-006` | Deployment credentials with minimum scope and a short life | ✔ | ✔ | ✔ | — |
| `DPL-007` | Validation in staging before promotion to production | — | ✔ | ✔ | — |
| `DPL-008` | Active monitoring during and after deployment | — | ✔ | ✔ | — |
| `DPL-009` | Progressive deployment with impact containment for critical applications | — | — | ✔ | — |
| `DPL-010` | Release gates for systems with AI agents | — | ✔ | ✔ | — |
| `DPL-011` | Canary and autonomy demotion in model releases | — | — | ✔ | — |
| `OPS-001` | Structured and persistent logging for all components in production | ✔ | ✔ | ✔ | — |
| `OPS-002` | Catalogue of critical security events defined and verified | ✔ | ✔ | ✔ | — |
| `OPS-003` | Log retention in accordance with policy and regulatory requirements | — | ✔ | ✔ | — |
| `OPS-004` | Centralisation of logs in a SIEM system or equivalent | — | ✔ | ✔ | — |
| `OPS-005` | Automatic alerts for critical security events | — | ✔ | ✔ | — |
| `OPS-006` | Alert response SLA defined and measured | — | ✔ | ✔ | — |
| `OPS-007` | Integration with a formal incident response process | — | ✔ | ✔ | — |
| `OPS-008` | Correlation of events across multiple sources | — | — | ✔ | — |
| `OPS-009` | Behavioural detection and baseline of normal activity | — | — | ✔ | — |
| `OPS-010` | Monitoring effectiveness metrics measured and reviewed | — | — | ✔ | — |
| `OPS-011` | Dedicated observability for AI/ML components in production | — | ✔ | ✔ | — |
| `OPS-012` | Complete audit per AI agent tool invocation | — | ✔ | ✔ | — |
| `OPS-013` | Budget and runaway detection in model consumption (token spend) | — | ✔ | ✔ | — |
| `OPS-014` | Detection of jailbreak / off-policy actions in production | — | — | ✔ | — |
| `OPS-015` | Continuous operational health and availability signals | — | ✔ | ✔ | — |
| `OPS-016` | Backups with tested restore | ▲ | ▲ | ▲ | CTX-RGPD-P03 |
| `OPS-017` | Recovery objectives and procedure for the application | — | ✔ | ✔ | — |
| `TRN-001` | Security training tracks defined by profile and criticality level | ✔ | ✔ | ✔ | — |
| `TRN-002` | Mandatory security onboarding before autonomous work | ✔ | ✔ | ✔ | — |
| `TRN-003` | Objective validation of onboarding with a defined acceptance criterion | ✔ | ✔ | ✔ | — |
| `TRN-004` | Access to critical environments conditional on validated onboarding | ✔ | ✔ | ✔ | — |
| `TRN-005` | Continuous security training for teams on L2 and L3 projects | — | ✔ | ✔ | — |
| `TRN-006` | Training content versioned and updated after defined triggers | — | ✔ | ✔ | — |
| `TRN-007` | Equivalent security onboarding for third parties and contractors | ✔ | ✔ | ✔ | — |
| `TRN-008` | Formal Security Champions programme in L3 teams | — | — | ✔ | — |
| `TRN-009` | Training KPIs defined, collected and acted upon | — | ✔ | ✔ | — |
| `GOV-001` | Formal security governance model approved | ✔ | ✔ | ✔ | — |
| `GOV-002` | Security ownership assigned per application or project | ✔ | ✔ | ✔ | — |
| `GOV-003` | Approval authorities defined and known per risk level | — | ✔ | ✔ | — |
| `GOV-004` | Formal exception management process active | ✔ | ✔ | ✔ | — |
| `GOV-005` | Exceptions with validity, monitoring and mandatory revalidation | — | ✔ | ✔ | — |
| `GOV-006` | Security clauses proportional to risk in contracts with third parties | ✔ | ✔ | ✔ | — |
| `GOV-007` | Formal supplier validation before onboarding | ✔ | ✔ | ✔ | — |
| `GOV-008` | Organisational traceability of security decisions per application | — | ✔ | ✔ | — |
| `GOV-009` | Evidence of decisions traceable, referenceable and retained | ✔ | ✔ | ✔ | — |
| `GOV-010` | Continuous validation cycle and periodic compliance review | — | ✔ | ✔ | — |
| `GOV-011` | Governance KPIs defined, collected and reported | — | ✔ | ✔ | — |
| `GOV-012` | Active maturity model with measured and planned evolution | — | — | ✔ | — |
| `GOV-013` | Technical onboarding and mandatory pre-access training of third parties | — | ✔ | ✔ | — |
| `GOV-014` | Periodic review of third-party access (least privilege) | ✔ | ✔ | ✔ | — |
| `GOV-015` | Coordinated vulnerability disclosure with a published reporting channel | ✔ | ✔ | ✔ | — |

## Obligations of the regime by coverage strength {#forca}

Count of the obligations in the matrix `_matriz/rgpd.yaml` (excluding those addressed to the authorities). The section “What this Manual covers and what stays out” of the cross-check page details them.

| Strength | Obligations |
|---|--:|
| Covers | 12 |
| Partial | 21 |
| Supports evidence | 17 |
| Gap | 15 |
| Out of scope | 49 |
