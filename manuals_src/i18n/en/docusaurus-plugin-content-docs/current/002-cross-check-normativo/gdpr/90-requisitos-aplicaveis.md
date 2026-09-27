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
  source_sha256: 3b575d32b7fab4a48f014a4ca03e5d13744ed322c4d9a67f99b0fd97c8d9d47f
  source_commit: null
  target_sha256: b75f2f842243d22c3b809aa148ce4493bf1b495db6d20fc9fa5501f37ee3e54a
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
| CTX-RGPD-P04 | `PRI-004` | — | mandatory | Inventory of purposes and recipients at any level: without it, rectifications, erasures and restrictions do not reach the recipients. | Regulation (EU) 2016/679, Article 19: “to each recipient to whom the personal data have been disclosed” (RGPD-19) | not admitted |
| CTX-RGPD-P05 | `PRI-005` | — | mandatory | PII-in-logs concept at any level, with pseudonyms and a per-person key in immutable logs (Policy 29 §8.1). | Regulation (EU) 2016/679, Article 32(1), point (a): “the pseudonymisation and encryption of personal data” (RGPD-32-1-a) | not admitted |

## Requirements added by the regime {#acrescentos}

These requirements only make sense under the regime, so they do not live in the Manual's catalogues; they are defined here, each with its legal basis.

| Requirement | Name | Acceptance criterion | Legal basis |
|---|---|---|---|
| `CTX-RGPD-R01` | Restriction of processing | Ability to flag a data subject's personal data as restricted; the flag is honoured on every processing path (application, integrations, exports, analytics), which then only store the data, save with the data subject's consent or under the exceptions of Article 18(2); the flag propagates to the recipients recorded in PRI-004, and lifting the restriction is logged. | Regulation (EU) 2016/679, Article 18(1) and (2): “such personal data shall, with the exception of storage, only be processed with the data subject's consent” (RGPD-18-1, RGPD-18-2) |
| `CTX-RGPD-R02` | Erasure of data made public | Where the application made personal data public and must later erase them: the reasonable technical steps to inform those processing them (e.g. removal requests to known search engines and aggregators, no-index headers and metadata, invalidation of public caches) are defined and carried out with the erasure, and logged. | Regulation (EU) 2016/679, Article 17(2): “shall take reasonable steps, including technical measures” (RGPD-17-2) |
| `CTX-RGPD-R03` | Age and parental consent verification | Where an information society service is offered directly to children on the basis of consent: age is verified against the applicable threshold (16, or the national threshold, not below 13), and consent from the holder of parental responsibility is obtained and verified by means appropriate to the available technology, recorded under PRI-006. | Regulation (EU) 2016/679, Article 8(2): “shall make reasonable efforts to verify in such cases that consent is given or authorised by the holder of parental responsibility over the child” (RGPD-8-2) |
| `CTX-RGPD-R04` | Objection by automated means | In information society services, automated objection signals sent by the browser or user agent (e.g. Global Privacy Control) are recognised and treated as a valid objection, with the same effect as an objection given through the interface (PRI-006). | Regulation (EU) 2016/679, Article 21(5): “the data subject may exercise his or her right to object by automated means using technical specifications” (RGPD-21-5) |
| `CTX-RGPD-R05` | Solely automated decisions | Decisions taken solely by automated processing, including profiling, with legal or similarly significant effects on the person are identified in the inventory; where permitted, the application allows the person to obtain human intervention, express their point of view and contest the decision, and each challenge is logged with its outcome; these decisions do not use special categories of data, save for the exceptions of Article 22(4). When the decision is supported by an Annex III high-risk AI system, CTX-AIA-RE-R03 also applies. | Regulation (EU) 2016/679, Article 22(1), (3) and (4): “at least the right to obtain human intervention on the part of the controller, to express his or her point of view and to contest the decision” (RGPD-22-1, RGPD-22-3, RGPD-22-4) |
| `CTX-RGPD-R06` | Register of personal data breaches | All personal data breaches are documented, whether notified or not: facts, effects, remedial action and the rationale for the decision to notify or not to notify, so that the supervisory authority can verify compliance. | Regulation (EU) 2016/679, Article 33(5): “The controller shall document any personal data breaches” (RGPD-33-5) |

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
| `AUT-011` | No default credentials | ✔ | ✔ | ✔ | — |
| `AUT-012` | Cryptographic authenticators and local biometrics | ✔ | ✔ | ✔ | — |
| `AUT-013` | Management and recovery of authentication factors | ✔ | ✔ | ✔ | — |
| `ACC-001` | RBAC access control | ✔ | ✔ | ✔ | — |
| `ACC-002` | Principle of least privilege | ✔ | ✔ | ✔ | — |
| `ACC-003` | Blocking and auditing of illegitimate access | ✔ | ✔ | ✔ | — |
| `ACC-004` | Separation of profiles | ✔ | ✔ | ✔ | — |
| `ACC-005` | Access control for APIs and services | ✔ | ✔ | ✔ | — |
| `ACC-006` | Protection of sensitive resources | ✔ | ✔ | ✔ | — |
| `ACC-007` | Validation of the access model | — | ✔ | ✔ | — |
| `ACC-008` | Real-time revocation | ✔ | ✔ | ✔ | — |
| `ACC-009` | Attribute-based authorisation (ABAC) | — | — | ✔ | — |
| `ACC-010` | Periodic review of permissions | ✔ | ✔ | ✔ | — |
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
| `ENC-007` | Lifecycle of keys, secrets and certificates | — | ✔ | ✔ | — |
| `ENC-008` | Prevention of client-side caching of sensitive data | — | ✔ | ✔ | — |
| `ENC-009` | Verifiable integrity of critical data | — | — | ✔ | — |
| `PRI-001` | Minimisation of the personal data collected | ✔ | ✔ | ✔ | — |
| `PRI-002` | Retention of personal data with a deadline and effective deletion | ✔ | ✔ | ✔ | — |
| `PRI-003` | Technical capability for access, rectification, deletion and export on request | ✔ | ✔ | ✔ | — |
| `PRI-004` | Record of purpose and recipients per personal-data set | ▲ | ▲ | ▲ | CTX-RGPD-P04 |
| `PRI-005` | Documented and applied concept for PII in logs | ▲ | ▲ | ▲ | CTX-RGPD-P05 |
| `PRI-006` | Technical management of consent and objection preferences | ✔ | ✔ | ✔ | — |
| `PRI-007` | Privacy by default in user-facing settings | ✔ | ✔ | ✔ | — |
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
| `THR-003` | Structured methodology applied with guaranteed minimum coverage | ✔ | ✔ | ✔ | — |
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
| `GOV-014` | Periodic review of access to supporting systems (least privilege) | ✔ | ✔ | ✔ | — |
| `GOV-015` | Coordinated vulnerability disclosure with a published reporting channel | ✔ | ✔ | ✔ | — |
| `GOV-016` | Privileged and administration accounts of supporting systems | ✔ | ✔ | ✔ | — |
| `GOV-017` | Lifecycle of identities with access to systems | ✔ | ✔ | ✔ | — |
| `CTX-RGPD-R01` | Restriction of processing | ▲ | ▲ | ▲ | — |
| `CTX-RGPD-R02` | Erasure of data made public | ▲ | ▲ | ▲ | — |
| `CTX-RGPD-R03` | Age and parental consent verification | ▲ | ▲ | ▲ | — |
| `CTX-RGPD-R04` | Objection by automated means | ▲ | ▲ | ▲ | — |
| `CTX-RGPD-R05` | Solely automated decisions | ▲ | ▲ | ▲ | — |
| `CTX-RGPD-R06` | Register of personal data breaches | ▲ | ▲ | ▲ | — |

## Obligations of the regime by coverage strength {#forca}

Count of the obligations in the matrix `_matriz/rgpd.yaml` (excluding those addressed to the authorities). The section [“What this Manual covers and what stays out”](#cobertura) lists them.

| Strength | Obligations |
|---|--:|
| Covers | 38 |
| Partial | 10 |
| Supports evidence | 17 |
| Gap | 0 |
| Out of scope | 49 |

## What this Manual covers and what stays out {#cobertura}

All the obligations of the matrix `_matriz/rgpd.yaml` in three categories: what the Manual **covers**, and in what form; the **declared gaps** (what it does not cover by omission); and what is **out of scope**, with the reason. Generated from the matrix; no obligation is left in silence. The 6 obligations addressed to the authorities create no duty for the organisation and are not listed.

### Covers (55) {#cobre}

Strength “covers” or “supports evidence”. The form is the Manual's response: catalogue requirement, policy, section, floor or requirement added by the regime.

| Obligation | Reference | Strength | Form |
|---|---|---|---|
| RGPD-5-1-b | Article 5(1), point (b) | Supports evidence | `PRI-004`; `PRI-001` |
| RGPD-5-1-c | Article 5(1), point (c) | Covers | `PRI-001`; `PRI-005`; [Policy 29 §5](/sbd-toe/assets/policies/policy-logging-estruturado#5-proibições-absolutas-nos-logs); [Policy 29 §3.2](/sbd-toe/assets/policies/policy-logging-estruturado#32-schema-mínimo-de-evento); `ENC-005`; [Policy 18 §10.1](/sbd-toe/assets/policies/policy-gestao-segredos#101-princípio-de-minimização) |
| RGPD-5-1-d | Article 5(1), point (d) | Covers | `PRI-003` |
| RGPD-5-1-e | Article 5(1), point (e) | Covers | `PRI-002`; `PRI-002`; `PRI-002`; [Policy 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs); [Policy 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs); [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) |
| RGPD-5-1-f | Article 5(1), point (f) | Covers | `ENC-001`; `ENC-002`; `ACC-001`; `ACC-006`; `LOG-003`; `ENC-009` |
| RGPD-5-2 | Article 5(2) | Supports evidence | `GOV-009`; [Regulatory Framework](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/grc-compliance#enquadramento-regulatório); [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) |
| RGPD-6-4 | Article 6(4) | Supports evidence | `PRI-004` |
| RGPD-7-1 | Article 7(1) | Covers | `PRI-006` |
| RGPD-7-3 | Article 7(3) | Covers | `PRI-006` |
| RGPD-8-2 | Article 8(2) | Covers | `CTX-RGPD-R03`; [Policy 18 §10.8](/sbd-toe/assets/policies/policy-gestao-segredos#108-anti-padrões) |
| RGPD-9-1 | Article 9(1) and (2) | Supports evidence | [📑 Data Type (D)](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/modelo-classificacao-eixos#-tipo-de-dados-d); [Policy 29 §5](/sbd-toe/assets/policies/policy-logging-estruturado#5-proibições-absolutas-nos-logs); [Policy 18 §10.7](/sbd-toe/assets/policies/policy-gestao-segredos#107-proporcionalidade) |
| RGPD-12-6 | Article 12(6) | Covers | `AUT-009`; `PRI-003` |
| RGPD-15-3 | Article 15(3) | Covers | `PRI-003` |
| RGPD-16 | Article 16 | Covers | `PRI-003`; `PRI-003`; [Policy 18 §10.6](/sbd-toe/assets/policies/policy-gestao-segredos#106-direitos-do-titular-dos-dados) |
| RGPD-17-1 | Article 17(1) | Covers | `PRI-003`; `PRI-002`; [Policy 29 §8.1](/sbd-toe/assets/policies/policy-logging-estruturado#81-imutabilidade-e-apagamento-de-dados-pessoais); [Policy 18 §10.6](/sbd-toe/assets/policies/policy-gestao-segredos#106-direitos-do-titular-dos-dados) |
| RGPD-17-2 | Article 17(2) | Covers | `CTX-RGPD-R02` |
| RGPD-18-1 | Article 18(1) | Covers | `CTX-RGPD-R01` |
| RGPD-18-2 | Article 18(2) | Covers | `CTX-RGPD-R01` |
| RGPD-19 | Article 19 | Covers | `PRI-004`; `PRI-003` |
| RGPD-20-1 | Article 20(1) | Covers | `PRI-003` |
| RGPD-21-2-3 | Article 21(2) and (3) | Covers | `PRI-006`; [Policy 18 §10.6](/sbd-toe/assets/policies/policy-gestao-segredos#106-direitos-do-titular-dos-dados) |
| RGPD-21-5 | Article 21(5) | Covers | `CTX-RGPD-R04` |
| RGPD-22-1 | Article 22(1) and (2) | Covers | `CTX-RGPD-R05` |
| RGPD-22-3 | Article 22(3) | Covers | `CTX-RGPD-R05` |
| RGPD-22-4 | Article 22(4) | Covers | `CTX-RGPD-R05` |
| RGPD-24-1 | Article 24(1) | Supports evidence | `CLA-003`; `GOV-010`; [Policy 04 §1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#1-objetivo) |
| RGPD-25-1 | Article 25(1) | Covers | `THR-003`; [Ch. 03 US-08](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-08---aplicação-linddun-quando-existir-tratamento-de-dados-pessoais--novo); [The method](/sbd-toe/sbd-manual/threat-modeling/addon/linddun-privacidade#o-método); `PRI-001`; `ERR-007` |
| RGPD-25-2 | Article 25(2) | Covers | `PRI-007`; `PRI-007`; [Policy 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura); `PRI-001`; `PRI-002`; `ACC-002` |
| RGPD-28-1 | Article 28(1) | Supports evidence | [Policy 33 §3](/sbd-toe/assets/policies/policy-contratacao-segura#3-due-diligence-pré-contratual); `GOV-007` |
| RGPD-28-2 | Article 28(2) | Supports evidence | [Policy 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) |
| RGPD-28-3-b | Article 28(3), point (b) | Supports evidence | [Policy 33 §5.1](/sbd-toe/assets/policies/policy-contratacao-segura#51-processo-de-onboarding) |
| RGPD-28-3-c | Article 28(3), point (c) | Covers | `CLA-003`; [Policy 33 §4.2](/sbd-toe/assets/policies/policy-contratacao-segura#42-cláusulas-adicionais-por-nível-de-risco); `ENC-002`; `ACC-001` |
| RGPD-28-3-e | Article 28(3), point (e) | Covers | `PRI-003` |
| RGPD-28-3-f | Article 28(3), point (f) | Supports evidence | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) |
| RGPD-28-3-g | Article 28(3), point (g) | Covers | `PRI-002`; [Policy 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding) |
| RGPD-28-3-h | Article 28(3), point (h) | Supports evidence | [Policy 33 §4.2](/sbd-toe/assets/policies/policy-contratacao-segura#42-cláusulas-adicionais-por-nível-de-risco) |
| RGPD-30-1 | Article 30(1) | Supports evidence | `PRI-004`; `CLA-008`; `ARC-001` |
| RGPD-30-2 | Article 30(2) | Supports evidence | `PRI-004` |
| RGPD-32-1 | Article 32(1) | Covers | `CLA-001`; `CLA-003`; `THR-001` |
| RGPD-32-1-a | Article 32(1), point (a) | Covers | `ENC-002`; `ENC-001`; `ERR-007`; [Policy 18 §10.1](/sbd-toe/assets/policies/policy-gestao-segredos#101-princípio-de-minimização); `PRI-005` |
| RGPD-32-1-b | Article 32(1), point (b) | Covers | `ENC-001`; `ACC-001`; `ENC-009`; `OPS-015`; `ARC-006` |
| RGPD-32-1-c | Article 32(1), point (c) | Covers | `DPL-005`; [Policy 27 §3.3](/sbd-toe/assets/policies/policy-rollback#33-rollback-de-base-de-dados); [Policy 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação); [Policy 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta); `OPS-016`; `OPS-016` |
| RGPD-32-1-d | Article 32(1), point (d) | Covers | `TST-001`; `TST-008`; [Policy 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp); `GOV-010` |
| RGPD-32-2 | Article 32(2) | Covers | `THR-001`; `THR-002`; `CLA-001` |
| RGPD-32-4 | Article 32(4) | Supports evidence | `ACC-002`; `ACC-010`; [Policy 33 §5.1](/sbd-toe/assets/policies/policy-contratacao-segura#51-processo-de-onboarding); `TRN-001` |
| RGPD-33-1 | Article 33(1) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); [Policy 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade) |
| RGPD-33-2 | Article 33(2) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) |
| RGPD-33-3 | Article 33(3) | Covers | [Policy 32 §6.1](/sbd-toe/assets/policies/policy-irp#61-critério-e-conteúdo-mínimo-por-regime); [Policy 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| RGPD-33-4 | Article 33(4) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| RGPD-33-5 | Article 33(5) | Covers | `CTX-RGPD-R06`; [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) |
| RGPD-34-1 | Article 34(1) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente) |
| RGPD-35-1 | Article 35(1) | Supports evidence | [Scope and purpose](/sbd-toe/sbd-manual/threat-modeling/addon/linddun-privacidade#âmbito-e-propósito); [Ch. 03 US-08](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-08---aplicação-linddun-quando-existir-tratamento-de-dados-pessoais--novo); `THR-003`; [Scope and purpose](/sbd-toe/sbd-manual/threat-modeling/addon/linddun-privacidade#âmbito-e-propósito) |
| RGPD-35-7 | Article 35(7) | Supports evidence | [The method](/sbd-toe/sbd-manual/threat-modeling/addon/linddun-privacidade#o-método); `THR-002`; [The method](/sbd-toe/sbd-manual/threat-modeling/addon/linddun-privacidade#o-método) |
| RGPD-35-11 | Article 35(11) | Supports evidence | [Policy 08 §4.1](/sbd-toe/assets/policies/policy-threat-modeling#41-triggers-obrigatórios); `ARC-009`; `CLA-006` |
| RGPD-39-1 | Article 39(1) | Supports evidence | [The method](/sbd-toe/sbd-manual/threat-modeling/addon/linddun-privacidade#o-método); [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Key Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/legal#responsabilidades-principais) |

### Declared gap (10) {#lacuna}

Strength “partial” or “gap”: the Manual does not cover, or covers only in part, and says what is missing. Gaps pending an AppSec Core round are marked with the name of the round.

| Obligation | Reference | Strength | How the Manual responds | What is missing |
|---|---|---|---|---|
| RGPD-12-2 | Article 12(2) | Partial | `PRI-003`; `PRI-006`; `CTX-RGPD-R01`; [Policy 18 §10.7](/sbd-toe/assets/policies/policy-gestao-segredos#107-proporcionalidade); [Policy 18 §10.6](/sbd-toe/assets/policies/policy-gestao-segredos#106-direitos-do-titular-dos-dados) | The technical part of exercising the rights is prescribed (PRI-003, PRI-006; restriction in CTX-RGPD-R01). The request channel and the formal reply to the data subject are legal matters, to be declared out of scope. |
| RGPD-15-1 | Article 15(1) | Partial | `PRI-003`; `PRI-004` | The copy of the data and the inventory of purposes and recipients are prescribed (PRI-003, PRI-004). The informational content of the reply (purposes, recipients, period, source, rights) belongs to the formal reply, to be declared out of scope. |
| RGPD-20-2 | Article 20(2) | Partial | `PRI-003` | Export in a machine-readable format is prescribed (PRI-003); direct transmission between controllers, where technically feasible, is not. |
| RGPD-24-2 | Article 24(2) | Partial | [Policy 18 §10.1](/sbd-toe/assets/policies/policy-gestao-segredos#101-princípio-de-minimização); [Policy 29 §5](/sbd-toe/assets/policies/policy-logging-estruturado#5-proibições-absolutas-nos-logs) | There is no data protection policy among the 39 policies; there is only the section on personal data in AI prompts (Policy 18 §10) and the prohibitions in logs (Policy 29 §5). |
| RGPD-28-3 | Article 28(3) | Partial | [Policy 18 §10.3](/sbd-toe/assets/policies/policy-gestao-segredos#103-sub-processadores); [Policy 18 §10.7](/sbd-toe/assets/policies/policy-gestao-segredos#107-proporcionalidade); [Policy 33 §10.6](/sbd-toe/assets/policies/policy-contratacao-segura#106-conformidade-regulatória-declarada); [Policy 33 §10.7](/sbd-toe/assets/policies/policy-contratacao-segura#107-operacionalização); `GOV-006` | The Article 28(3) contract is prescribed only for AI service vendors; for other processors Policy 33 §4 requires only security clauses. |
| RGPD-34-2 | Article 34(2) | Partial | [Policy 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente) | Requires honest communication, but not the minimum content (nature of the breach in clear language, DPO contact, consequences, measures). |
| RGPD-35-2 | Article 35(2) | Partial | [Ch. 03 US-08](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-08---aplicação-linddun-quando-existir-tratamento-de-dados-pessoais--novo); [Key Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/legal#responsabilidades-principais) | Review by the DPO only at L3 and of the LINDDUN analysis, not of the DPIA. |
| RGPD-38-1 | Article 38(1) | Partial | [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Ch. 03 US-08](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-08---aplicação-linddun-quando-existir-tratamento-de-dados-pessoais--novo) | DPO involved in breaches (≤ 1 h) and in the L3 LINDDUN review; not involved in design, DPIA, choice of processors or exceptions. |
| RGPD-44 | Article 44 | Partial | [Policy 18 §10.3](/sbd-toe/assets/policies/policy-gestao-segredos#103-sub-processadores); [Policy 33 §10.2](/sbd-toe/assets/policies/policy-contratacao-segura#102-localização-de-processamento) | Only in the AI service vendors slice; hosting, SaaS and other processors outside the EEA have no location/transfer rule. |
| RGPD-46-1 | Article 46(1) to (3) | Partial | [Policy 18 §10.3](/sbd-toe/assets/policies/policy-gestao-segredos#103-sub-processadores) | Requires SCCs “or another valid mechanism” only for AI vendors; does not address transfer impact assessment nor supplementary technical measures. |

### Out of scope (49) {#fora-de-ambito}

Obligations that the Manual declares out of scope, with the reason.

| Obligation | Reference | Reason |
|---|---|---|
| RGPD-5-1-a | Article 5(1), point (a) | Legal duty (content/validity of the processing or legal relationship) — the Manual explicitly delimits it out of scope: “The legal side — legal bases, formal rights, regulatory obligations — does not live in this catalogue” (Ch. 02, PRI); the GDPR cross-check refers it to Legal/DPO. |
| RGPD-6-1 | Article 6(1) | Legal duty (content/validity of the processing or legal relationship) — the Manual explicitly delimits it out of scope: “The legal side — legal bases, formal rights, regulatory obligations — does not live in this catalogue” (Ch. 02, PRI); the GDPR cross-check refers it to Legal/DPO. |
| RGPD-7-2 | Article 7(2) | Content and form of the information to the data subject (privacy notices): legal-communication matter, referred by the Manual to Legal/DPO. |
| RGPD-8-1 | Article 8(1) | Legal duty (content/validity of the processing or legal relationship) — the Manual explicitly delimits it out of scope: “The legal side — legal bases, formal rights, regulatory obligations — does not live in this catalogue” (Ch. 02, PRI); the GDPR cross-check refers it to Legal/DPO. |
| RGPD-9-3 | Article 9(3) | Legal duty (content/validity of the processing or legal relationship) — the Manual explicitly delimits it out of scope: “The legal side — legal bases, formal rights, regulatory obligations — does not live in this catalogue” (Ch. 02, PRI); the GDPR cross-check refers it to Legal/DPO. |
| RGPD-10 | Article 10 | Legal duty (content/validity of the processing or legal relationship) — the Manual explicitly delimits it out of scope: “The legal side — legal bases, formal rights, regulatory obligations — does not live in this catalogue” (Ch. 02, PRI); the GDPR cross-check refers it to Legal/DPO. |
| RGPD-11-2 | Article 11(2) | Formal procedure for responding to the data subject (time limits, reasons, costs): “formal rights”, delimited by the Manual to the legal side; the corresponding technical capability is addressed in the engineering items. |
| RGPD-12-1 | Article 12(1) | Content and form of the information to the data subject (privacy notices): legal-communication matter, referred by the Manual to Legal/DPO. |
| RGPD-12-3 | Article 12(3) | Formal procedure for responding to the data subject (time limits, reasons, costs): “formal rights”, delimited by the Manual to the legal side; the corresponding technical capability is addressed in the engineering items. |
| RGPD-12-4 | Article 12(4) | Formal procedure for responding to the data subject (time limits, reasons, costs): “formal rights”, delimited by the Manual to the legal side; the corresponding technical capability is addressed in the engineering items. |
| RGPD-12-5 | Article 12(5) | Formal procedure for responding to the data subject (time limits, reasons, costs): “formal rights”, delimited by the Manual to the legal side; the corresponding technical capability is addressed in the engineering items. |
| RGPD-13-1 | Article 13(1) | Content and form of the information to the data subject (privacy notices): legal-communication matter, referred by the Manual to Legal/DPO. |
| RGPD-13-2 | Article 13(2) | Content and form of the information to the data subject (privacy notices): legal-communication matter, referred by the Manual to Legal/DPO. |
| RGPD-13-3 | Article 13(3) | Content and form of the information to the data subject (privacy notices): legal-communication matter, referred by the Manual to Legal/DPO. |
| RGPD-14-1-2 | Article 14(1) and (2) | Content and form of the information to the data subject (privacy notices): legal-communication matter, referred by the Manual to Legal/DPO. |
| RGPD-14-3 | Article 14(3) | Content and form of the information to the data subject (privacy notices): legal-communication matter, referred by the Manual to Legal/DPO. |
| RGPD-14-4 | Article 14(4) | Content and form of the information to the data subject (privacy notices): legal-communication matter, referred by the Manual to Legal/DPO. |
| RGPD-15-2 | Article 15(2) | Legal regime for international transfers (mechanisms, derogations, BCR): Legal/DPO. The Manual only touches on transfers in the AI vendors slice (Policies 18 §10.3 and 33 §10.2). |
| RGPD-18-3 | Article 18(3) | Formal procedure for responding to the data subject (time limits, reasons, costs): “formal rights”, delimited by the Manual to the legal side; the corresponding technical capability is addressed in the engineering items. |
| RGPD-21-1 | Article 21(1) | Legal duty (content/validity of the processing or legal relationship) — the Manual explicitly delimits it out of scope: “The legal side — legal bases, formal rights, regulatory obligations — does not live in this catalogue” (Ch. 02, PRI); the GDPR cross-check refers it to Legal/DPO. |
| RGPD-21-4 | Article 21(4) | Content and form of the information to the data subject (privacy notices): legal-communication matter, referred by the Manual to Legal/DPO. |
| RGPD-26-1 | Article 26(1) | Legal duty (content/validity of the processing or legal relationship) — the Manual explicitly delimits it out of scope: “The legal side — legal bases, formal rights, regulatory obligations — does not live in this catalogue” (Ch. 02, PRI); the GDPR cross-check refers it to Legal/DPO. |
| RGPD-26-2 | Article 26(2) | Legal duty (content/validity of the processing or legal relationship) — the Manual explicitly delimits it out of scope: “The legal side — legal bases, formal rights, regulatory obligations — does not live in this catalogue” (Ch. 02, PRI); the GDPR cross-check refers it to Legal/DPO. |
| RGPD-27-1 | Article 27(1) and (2) | Legal duty (content/validity of the processing or legal relationship) — the Manual explicitly delimits it out of scope: “The legal side — legal bases, formal rights, regulatory obligations — does not live in this catalogue” (Ch. 02, PRI); the GDPR cross-check refers it to Legal/DPO. |
| RGPD-28-3-a | Article 28(3), point (a) | Legal duty (content/validity of the processing or legal relationship) — the Manual explicitly delimits it out of scope: “The legal side — legal bases, formal rights, regulatory obligations — does not live in this catalogue” (Ch. 02, PRI); the GDPR cross-check refers it to Legal/DPO. |
| RGPD-28-3-2 | Article 28(3), second subparagraph | Legal duty (content/validity of the processing or legal relationship) — the Manual explicitly delimits it out of scope: “The legal side — legal bases, formal rights, regulatory obligations — does not live in this catalogue” (Ch. 02, PRI); the GDPR cross-check refers it to Legal/DPO. |
| RGPD-28-3-d | Article 28(3), point (d) | Legal duty (content/validity of the processing or legal relationship) — the Manual explicitly delimits it out of scope: “The legal side — legal bases, formal rights, regulatory obligations — does not live in this catalogue” (Ch. 02, PRI); the GDPR cross-check refers it to Legal/DPO. |
| RGPD-28-4 | Article 28(4) | Legal duty (content/validity of the processing or legal relationship) — the Manual explicitly delimits it out of scope: “The legal side — legal bases, formal rights, regulatory obligations — does not live in this catalogue” (Ch. 02, PRI); the GDPR cross-check refers it to Legal/DPO. |
| RGPD-28-10 | Article 28(10) | Legal duty (content/validity of the processing or legal relationship) — the Manual explicitly delimits it out of scope: “The legal side — legal bases, formal rights, regulatory obligations — does not live in this catalogue” (Ch. 02, PRI); the GDPR cross-check refers it to Legal/DPO. |
| RGPD-29 | Article 29 | Legal duty (content/validity of the processing or legal relationship) — the Manual explicitly delimits it out of scope: “The legal side — legal bases, formal rights, regulatory obligations — does not live in this catalogue” (Ch. 02, PRI); the GDPR cross-check refers it to Legal/DPO. |
| RGPD-30-3-4 | Article 30(3) and (4) | Relationship with the supervisory authority/supervisory bodies; legal plane, not engineering. |
| RGPD-31 | Article 31 | Relationship with the supervisory authority/supervisory bodies; legal plane, not engineering. |
| RGPD-35-3 | Article 35(3) | Legal duty (content/validity of the processing or legal relationship) — the Manual explicitly delimits it out of scope: “The legal side — legal bases, formal rights, regulatory obligations — does not live in this catalogue” (Ch. 02, PRI); the GDPR cross-check refers it to Legal/DPO. |
| RGPD-35-9 | Article 35(9) | Legal duty (content/validity of the processing or legal relationship) — the Manual explicitly delimits it out of scope: “The legal side — legal bases, formal rights, regulatory obligations — does not live in this catalogue” (Ch. 02, PRI); the GDPR cross-check refers it to Legal/DPO. |
| RGPD-36-1 | Article 36(1) | Relationship with the supervisory authority/supervisory bodies; legal plane, not engineering. |
| RGPD-36-3 | Article 36(3) | Relationship with the supervisory authority/supervisory bodies; legal plane, not engineering. |
| RGPD-37-1 | Article 37(1) | Status, designation and independence of the DPO: a matter of legal organisation; the Manual only assumes the DPO role where there is personal data (Roles — Legal). |
| RGPD-37-5 | Article 37(5) | Status, designation and independence of the DPO: a matter of legal organisation; the Manual only assumes the DPO role where there is personal data (Roles — Legal). |
| RGPD-37-7 | Article 37(7) | Status, designation and independence of the DPO: a matter of legal organisation; the Manual only assumes the DPO role where there is personal data (Roles — Legal). |
| RGPD-38-2 | Article 38(2) | Status, designation and independence of the DPO: a matter of legal organisation; the Manual only assumes the DPO role where there is personal data (Roles — Legal). |
| RGPD-38-3 | Article 38(3) | Status, designation and independence of the DPO: a matter of legal organisation; the Manual only assumes the DPO role where there is personal data (Roles — Legal). |
| RGPD-38-6 | Article 38(6) | Status, designation and independence of the DPO: a matter of legal organisation; the Manual only assumes the DPO role where there is personal data (Roles — Legal). |
| RGPD-40-4 | Article 40(4) | Relationship with the supervisory authority/supervisory bodies; legal plane, not engineering. |
| RGPD-42-6-7 | Article 42(6) and (7) | Relationship with the supervisory authority/supervisory bodies; legal plane, not engineering. |
| RGPD-47-2 | Article 47(2) | Legal regime for international transfers (mechanisms, derogations, BCR): Legal/DPO. The Manual only touches on transfers in the AI vendors slice (Policies 18 §10.3 and 33 §10.2). |
| RGPD-48 | Article 48 | Legal regime for international transfers (mechanisms, derogations, BCR): Legal/DPO. The Manual only touches on transfers in the AI vendors slice (Policies 18 §10.3 and 33 §10.2). |
| RGPD-49-1 | Article 49(1) | Legal regime for international transfers (mechanisms, derogations, BCR): Legal/DPO. The Manual only touches on transfers in the AI vendors slice (Policies 18 §10.3 and 33 §10.2). |
| RGPD-49-1-2 | Article 49(1), second subparagraph | Legal regime for international transfers (mechanisms, derogations, BCR): Legal/DPO. The Manual only touches on transfers in the AI vendors slice (Policies 18 §10.3 and 33 §10.2). |
| RGPD-49-6 | Article 49(6) | Legal regime for international transfers (mechanisms, derogations, BCR): Legal/DPO. The Manual only touches on transfers in the AI vendors slice (Policies 18 §10.3 and 33 §10.2). |
