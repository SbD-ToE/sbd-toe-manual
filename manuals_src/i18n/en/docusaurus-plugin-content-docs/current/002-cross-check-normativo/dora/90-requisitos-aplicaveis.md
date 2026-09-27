---
id: requisitos-aplicaveis
title: "Applicable requirements — Financial entity (DORA)"
description: "Generated view: the Manual's requirements that apply under context CTX-DORA, by level and grade, with each floor that the regime elevates and its legal basis."
sidebar_position: 90
tags: [cross-check, dora, requisitos, overlay, gerado]
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
  - 002-cross-check-normativo/_matriz/dora.yaml
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/dora/90-requisitos-aplicaveis.md
  source_sha256: 2333270cd1b3d5ad4cd6ca2f8227bc022f2f8b5fe792c87c6a5e9047bfb6e006
  source_commit: null
  target_sha256: 9877fa4deb1fb013d05f2769f242f35990c05a76ad69f21d791f7d1d3c69b3ef
  engine: gen_reg_views
  prompt_sha256: null
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: []
  glossary_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
  translated_at: 2026-09-27T00:00:00Z
  stamped_at: 2026-09-27T00:00:00Z
  reviewed_by: null
---

# Applicable requirements: Financial entity (DORA)

> **Generated page**, produced by `scripts/gen_reg_views.py` from the requirement catalogues and from `002-cross-check-normativo/_contextos-regulatorios.yaml`. It is not edited by hand: each requirement's catalogue is the canonical source, and this page is a view of the regulatory overlay.

For context **CTX-DORA**, this page brings together the Manual's base selection per level and each **floor** that the regime elevates, with the obligation that grounds it. A context never lowers a minimum of the Manual.

## When it applies {#quando-se-aplica}

The organisation is one of the financial entities listed in Article 2(1) of Regulation (EU) 2022/2554. A floor without a grade applies to all the entity's applications; an FCI-grade floor only to those supporting a critical or important function. Declared per entity and inherited by all applications.

> Regulation (EU) 2022/2554, Article 2(1): “this Regulation applies to the following entities”

## Grades {#graus}

- **FCI** — Supports a critical or important function (cumulative with the context). The application supports a critical or important function in the financial entity's inventory of functions; declared per application, with a reference to that inventory.

## Context floor list {#pisos}

| Floor | Target | Grade | Required floor | Scope | Legal basis | Justification of non-applicability |
|---|---|---|---|---|---|---|
| CTX-DORA-P01 | [Policy 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade) | — | mandatory | ICT-related incident management process defined, established and implemented at any level, including the recording of all incidents and the post-mortem of major incidents, with the review of the affected artefacts (§4.6). | Regulation (EU) 2022/2554, Article 17(1): “Financial entities shall define, establish and implement an ICT-related incident management process” (DORA-17-1) | not admitted |
| CTX-DORA-P02 | `OPS-007` | — | mandatory | — | Regulation (EU) 2022/2554, Article 17(1): “Financial entities shall define, establish and implement an ICT-related incident management process” (DORA-17-1) | not admitted |
| CTX-DORA-P03 | `TST-005` | — | mandatory | Dynamic testing (alongside static testing, already mandatory under DEV-003), with security testing of internet-exposed systems and applications. | Delegated Regulation (EU) 2024/1774, Article 16(3): “shall contain the performance of source code reviews covering both static and dynamic testing” (DORA-RTS1774-16-3) | not admitted |
| CTX-DORA-P04 | `LOG-008` | — | mandatory | — | Delegated Regulation (EU) 2024/1774, Article 12(2), point (e): “measures to detect a failure of logging systems” (DORA-RTS1774-12-2-e) | not admitted |
| CTX-DORA-P05 | `ACC-010` | — | mandatory; frequency of access-rights update ≥ annual (“at least once a year for all ICT systems, other than ICT systems supporting critical or important functions”) | — | Delegated Regulation (EU) 2024/1774, Article 21, point (e)(iv): “update of access rights where changes are necessary and at least once a year for all ICT systems” (DORA-RTS1774-21-e-iv) | not admitted |
| CTX-DORA-P06 | `ACC-010` | FCI | mandatory; frequency of access-rights update ≥ half-yearly (“at least every 6 months for ICT systems supporting critical or important functions”) | — | Delegated Regulation (EU) 2024/1774, Article 21, point (e)(iv): “at least every 6 months for ICT systems supporting critical or important functions” (DORA-RTS1774-21-e-iv) | not admitted |
| CTX-DORA-P07 | `AUT-001` | — | mandatory | Strong authentication of the application's users for access to ICT assets supporting critical or important functions and to ICT assets that are publicly accessible (remote and privileged access are in CTX-DORA-P13). | Delegated Regulation (EU) 2024/1774, Article 21, point (f)(ii); Article 33, point (d) (simplified framework): “the use of strong authentication methods in accordance with leading practices and techniques for remote access to the financial entity’s network, for privileged access, for access to ICT assets supporting critical or important functions or ICT assets that are publicly accessible” (DORA-RTS1774-21-f-ii, DORA-RTS1774-33-d) | admitted |
| CTX-DORA-P08 | [Policy 10 §9](/sbd-toe/assets/policies/policy-dependencias#9-auditoria-periódica) | FCI | mandatory; frequency of automated vulnerability scanning ≥ weekly (“on at least a weekly basis”) | Automated vulnerability scanning of the ICT assets supporting critical or important functions, not only of dependencies and images. | Delegated Regulation (EU) 2024/1774, Article 10(2), point (b), and second subparagraph: “financial entities shall perform the automated vulnerability scanning and assessments on ICT assets for the ICT assets supporting critical or important functions on at least a weekly basis” (DORA-RTS1774-10-2-b) | not admitted |
| CTX-DORA-P09 | `OPS-005` | FCI | mandatory | — | Delegated Regulation (EU) 2024/1774, Article 23(2), point (b): “tools generating alerts for anomalous activities and behaviour, at least for ICT assets and information assets supporting critical or important functions” (DORA-RTS1774-23-2-b) | not admitted |
| CTX-DORA-P10 | `GOV-015` | — | mandatory | Responsible disclosure to clients, counterparties and the public. | Delegated Regulation (EU) 2024/1774, Article 10(2), point (e): “establish procedures for the responsible disclosure of vulnerabilities to clients, counterparties, and to the public” (DORA-RTS1774-10-2-e) | not admitted |
| CTX-DORA-P11 | `OPS-016` | — | mandatory | Restoration on systems physically and logically segregated from the source system, protected against unauthorised access and corruption; periodic testing of backup and restoration. | Regulation (EU) 2022/2554, Article 12(1) to (3); Delegated Regulation (EU) 2024/1774, Article 8(2), point (b)(i), and Article 39(2), point (g): “financial entities shall use ICT systems that are physically and logically segregated from the source ICT system” (DORA-12-1-a, DORA-12-2, DORA-12-3, DORA-RTS1774-8-2-b-i, DORA-RTS1774-39-2-g) | not admitted |
| CTX-DORA-P12 | `OPS-017` | FCI | mandatory | Also at L1 for applications supporting critical or important functions: recovery levels and timeframes and dependencies on ICT third-party service providers. | Regulation (EU) 2022/2554, Article 12(6); Delegated Regulation (EU) 2024/1774, Article 39(2), point (d): “In determining the recovery time and recovery point objectives for each function” (DORA-12-6, DORA-RTS1774-39-2-d) | not admitted |
| CTX-DORA-P13 | `GOV-016` | — | mandatory | Strong authentication for remote access to the entity's network and for privileged access; dedicated accounts for administrative tasks and automated privileged access management (PAM) where feasible and appropriate, at any level. | Delegated Regulation (EU) 2024/1774, Article 21, points (e) and (f)(ii), and Article 33, points (c) and (d): “financial entities shall, where possible, use dedicated accounts for the performance of administrative tasks on ICT systems” (DORA-RTS1774-21-e, DORA-RTS1774-21-e-ii, DORA-RTS1774-21-f-ii, DORA-RTS1774-33-c, DORA-RTS1774-33-d) | not admitted |
| CTX-DORA-P14 | `GOV-017` | — | mandatory | Unique identification and authentication of persons and systems; lifecycle management process for identities and accounts, with automated solutions where possible and appropriate; generic and shared accounts limited, at any level. | Delegated Regulation (EU) 2024/1774, Article 20(1) and (2)(b), and Article 21, point (c): “a lifecycle management process for identities and accounts” (DORA-RTS1774-20-1, DORA-RTS1774-20-2-b, DORA-RTS1774-21-c) | not admitted |
| CTX-DORA-P15 | `ENC-007` | — | mandatory | Full cryptographic key lifecycle at any level. | Delegated Regulation (EU) 2024/1774, Article 7(1): “requirements for managing cryptographic keys through their whole lifecycle” (DORA-RTS1774-7-1) | admitted |
| CTX-DORA-P16 | `ENC-007` | FCI | mandatory | Register of all certificates and certificate-storing devices, kept up to date, with renewal before expiry, at any level. | Delegated Regulation (EU) 2024/1774, Article 7(4) and (5): “shall create and maintain a register for all certificates and certificate-storing devices” (DORA-RTS1774-7-4) | not admitted |
| CTX-DORA-P17 | `ENC-003` | — | mandatory | Cryptographic inventory and review at any level, with the cryptographic technology updated as cryptanalysis evolves or, where that is not possible, mitigating measures. | Delegated Regulation (EU) 2024/1774, Article 6(4): “on the basis of developments in cryptanalysis” (DORA-RTS1774-6-4) | admitted |
| CTX-DORA-P18 | `ARC-006` | FCI | mandatory | Review of the network filtering rules at least every six months, at any level, for the systems supporting critical or important functions. | Delegated Regulation (EU) 2024/1774, Article 13, point (h), and second subparagraph: “at least every 6 months” (DORA-RTS1774-13-h) | not admitted |

## Requirements added by the regime {#acrescentos}

These requirements only make sense under the regime, so they do not live in the Manual's catalogues; they are defined here, each with its legal basis.

| Requirement | Name | Acceptance criterion | Legal basis |
|---|---|---|---|
| `CTX-DORA-R01` | Redundant ICT capacities and switchover testing | Redundant ICT capacities, with resources, capabilities and functions adequate to business needs, for the systems the application depends on (microenterprises assess the need based on their risk profile); response and recovery plans tested at least yearly, including, for entities other than microenterprises, cyber-attack scenarios and switchover between the primary ICT infrastructure and the redundant capacity. | Regulation (EU) 2022/2554, Article 12(4), and Article 11(6), point (a): “shall maintain redundant ICT capacities equipped with resources, capabilities and functions that are adequate to ensure business needs” (DORA-12-4, DORA-11-6-a) |
| `CTX-DORA-R02` | Classification of ICT-related incidents and aggregation of recurring ones | ICT-related incidents are classified and their impact determined with the criteria of Article 18(1) (clients, counterparts and transactions affected; reputation; duration and downtime; geographical spread; data losses; criticality of the services; economic impact) and with the materiality thresholds of Delegated Regulation (EU) 2024/1772, from the impact data in the record (Policy 32 §4.3). Every month, the existence of recurring incidents is assessed: those that occurred at least twice within six months, with the same apparent root cause, and that collectively meet the criteria count as one major incident (except microenterprises and the entities of Article 16(1)). | Regulation (EU) 2022/2554, Articles 17(3), point (b), and 18(1); Delegated Regulation (EU) 2024/1772, Article 8(2): “assess the existence of recurring incidents on a monthly basis” (DORA-17-3-b, DORA-18-1, DORA-RTS1772-8-2, DORA-RTS1772-8-2-p2) |
| `CTX-DORA-R03` | Record of significant cyber threats | Besides incidents, the significant cyber threats that affect the application or its systems are recorded (description, source, systems targeted, assessment and measures), with the option of voluntary notification to the competent authority (Article 19(2)). | Regulation (EU) 2022/2554, Article 17(2): “Financial entities shall record all ICT-related incidents and significant cyber threats” (DORA-17-2) |

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
| `AUT-001` | Mandatory MFA | ▲ | ▲ | ▲ | CTX-DORA-P07 |
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
| `ACC-010` | Periodic review of permissions | ▲ | ▲ | ▲ | CTX-DORA-P05 |
| `LOG-001` | Logging of critical events | ✔ | ✔ | ✔ | — |
| `LOG-002` | Minimum attributes in logs | ✔ | ✔ | ✔ | — |
| `LOG-003` | Protection of log integrity and access | ✔ | ✔ | ✔ | — |
| `LOG-004` | Periodic log analysis | — | ✔ | ✔ | — |
| `LOG-005` | Minimum log retention | ✔ | ✔ | ✔ | — |
| `LOG-006` | Forwarding to a centralised system | — | ✔ | ✔ | — |
| `LOG-007` | Classification and anomaly detection | — | ✔ | ✔ | — |
| `LOG-008` | Alarm on failures of the logging mechanism | ▲ | ▲ | ▲ | CTX-DORA-P04 |
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
| `ENC-003` | Robust cryptographic algorithms and configurations | ▲ | ▲ | ▲ | CTX-DORA-P17 |
| `ENC-004` | Adaptive password hashing | ✔ | ✔ | ✔ | — |
| `ENC-005` | Masking of sensitive data in logs, outputs and API responses | ✔ | ✔ | ✔ | — |
| `ENC-006` | Detection and prevention of secrets exposed in repositories | ✔ | ✔ | ✔ | — |
| `ENC-007` | Lifecycle of keys, secrets and certificates | ▲ | ▲ | ▲ | CTX-DORA-P15 |
| `ENC-008` | Prevention of client-side caching of sensitive data | — | ✔ | ✔ | — |
| `ENC-009` | Verifiable integrity of critical data | — | — | ✔ | — |
| `PRI-001` | Minimisation of the personal data collected | ✔ | ✔ | ✔ | — |
| `PRI-002` | Retention of personal data with a deadline and effective deletion | ✔ | ✔ | ✔ | — |
| `PRI-003` | Technical capability for access, rectification, deletion and export on request | ✔ | ✔ | ✔ | — |
| `PRI-004` | Record of purpose and recipients per personal-data set | — | ✔ | ✔ | — |
| `PRI-005` | Documented and applied concept for PII in logs | — | ✔ | ✔ | — |
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
| `TST-005` | DAST integrated in a staging environment before promotion | ▲ | ▲ | ▲ | CTX-DORA-P03 |
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
| `OPS-007` | Integration with a formal incident response process | ▲ | ▲ | ▲ | CTX-DORA-P02 |
| `OPS-008` | Correlation of events across multiple sources | — | — | ✔ | — |
| `OPS-009` | Behavioural detection and baseline of normal activity | — | — | ✔ | — |
| `OPS-010` | Monitoring effectiveness metrics measured and reviewed | — | — | ✔ | — |
| `OPS-011` | Dedicated observability for AI/ML components in production | — | ✔ | ✔ | — |
| `OPS-012` | Complete audit per AI agent tool invocation | — | ✔ | ✔ | — |
| `OPS-013` | Budget and runaway detection in model consumption (token spend) | — | ✔ | ✔ | — |
| `OPS-014` | Detection of jailbreak / off-policy actions in production | — | — | ✔ | — |
| `OPS-015` | Continuous operational health and availability signals | — | ✔ | ✔ | — |
| `OPS-016` | Backups with tested restore | ▲ | ▲ | ▲ | CTX-DORA-P11 |
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
| `GOV-015` | Coordinated vulnerability disclosure with a published reporting channel | ▲ | ▲ | ▲ | CTX-DORA-P10 |
| `GOV-016` | Privileged and administration accounts of supporting systems | ▲ | ▲ | ▲ | CTX-DORA-P13 |
| `GOV-017` | Lifecycle of identities with access to systems | ▲ | ▲ | ▲ | CTX-DORA-P14 |
| `CTX-DORA-R01` | Redundant ICT capacities and switchover testing | ▲ | ▲ | ▲ | — |
| `CTX-DORA-R02` | Classification of ICT-related incidents and aggregation of recurring ones | ▲ | ▲ | ▲ | — |
| `CTX-DORA-R03` | Record of significant cyber threats | ▲ | ▲ | ▲ | — |

## Requirement list — FCI {#lista-fci}

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
| `AUT-001` | Mandatory MFA | ▲ | ▲ | ▲ | CTX-DORA-P07 |
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
| `ACC-010` | Periodic review of permissions | ▲ | ▲ | ▲ | CTX-DORA-P05, CTX-DORA-P06 |
| `LOG-001` | Logging of critical events | ✔ | ✔ | ✔ | — |
| `LOG-002` | Minimum attributes in logs | ✔ | ✔ | ✔ | — |
| `LOG-003` | Protection of log integrity and access | ✔ | ✔ | ✔ | — |
| `LOG-004` | Periodic log analysis | — | ✔ | ✔ | — |
| `LOG-005` | Minimum log retention | ✔ | ✔ | ✔ | — |
| `LOG-006` | Forwarding to a centralised system | — | ✔ | ✔ | — |
| `LOG-007` | Classification and anomaly detection | — | ✔ | ✔ | — |
| `LOG-008` | Alarm on failures of the logging mechanism | ▲ | ▲ | ▲ | CTX-DORA-P04 |
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
| `ENC-003` | Robust cryptographic algorithms and configurations | ▲ | ▲ | ▲ | CTX-DORA-P17 |
| `ENC-004` | Adaptive password hashing | ✔ | ✔ | ✔ | — |
| `ENC-005` | Masking of sensitive data in logs, outputs and API responses | ✔ | ✔ | ✔ | — |
| `ENC-006` | Detection and prevention of secrets exposed in repositories | ✔ | ✔ | ✔ | — |
| `ENC-007` | Lifecycle of keys, secrets and certificates | ▲ | ▲ | ▲ | CTX-DORA-P15, CTX-DORA-P16 |
| `ENC-008` | Prevention of client-side caching of sensitive data | — | ✔ | ✔ | — |
| `ENC-009` | Verifiable integrity of critical data | — | — | ✔ | — |
| `PRI-001` | Minimisation of the personal data collected | ✔ | ✔ | ✔ | — |
| `PRI-002` | Retention of personal data with a deadline and effective deletion | ✔ | ✔ | ✔ | — |
| `PRI-003` | Technical capability for access, rectification, deletion and export on request | ✔ | ✔ | ✔ | — |
| `PRI-004` | Record of purpose and recipients per personal-data set | — | ✔ | ✔ | — |
| `PRI-005` | Documented and applied concept for PII in logs | — | ✔ | ✔ | — |
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
| `ARC-006` | Technical isolation controls between sensitive domains | ▲ | ▲ | ▲ | CTX-DORA-P18 |
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
| `TST-005` | DAST integrated in a staging environment before promotion | ▲ | ▲ | ▲ | CTX-DORA-P03 |
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
| `OPS-005` | Automatic alerts for critical security events | ▲ | ▲ | ▲ | CTX-DORA-P09 |
| `OPS-006` | Alert response SLA defined and measured | — | ✔ | ✔ | — |
| `OPS-007` | Integration with a formal incident response process | ▲ | ▲ | ▲ | CTX-DORA-P02 |
| `OPS-008` | Correlation of events across multiple sources | — | — | ✔ | — |
| `OPS-009` | Behavioural detection and baseline of normal activity | — | — | ✔ | — |
| `OPS-010` | Monitoring effectiveness metrics measured and reviewed | — | — | ✔ | — |
| `OPS-011` | Dedicated observability for AI/ML components in production | — | ✔ | ✔ | — |
| `OPS-012` | Complete audit per AI agent tool invocation | — | ✔ | ✔ | — |
| `OPS-013` | Budget and runaway detection in model consumption (token spend) | — | ✔ | ✔ | — |
| `OPS-014` | Detection of jailbreak / off-policy actions in production | — | — | ✔ | — |
| `OPS-015` | Continuous operational health and availability signals | — | ✔ | ✔ | — |
| `OPS-016` | Backups with tested restore | ▲ | ▲ | ▲ | CTX-DORA-P11 |
| `OPS-017` | Recovery objectives and procedure for the application | ▲ | ▲ | ▲ | CTX-DORA-P12 |
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
| `GOV-015` | Coordinated vulnerability disclosure with a published reporting channel | ▲ | ▲ | ▲ | CTX-DORA-P10 |
| `GOV-016` | Privileged and administration accounts of supporting systems | ▲ | ▲ | ▲ | CTX-DORA-P13 |
| `GOV-017` | Lifecycle of identities with access to systems | ▲ | ▲ | ▲ | CTX-DORA-P14 |
| `CTX-DORA-R01` | Redundant ICT capacities and switchover testing | ▲ | ▲ | ▲ | — |
| `CTX-DORA-R02` | Classification of ICT-related incidents and aggregation of recurring ones | ▲ | ▲ | ▲ | — |
| `CTX-DORA-R03` | Record of significant cyber threats | ▲ | ▲ | ▲ | — |

## Obligations of the regime by coverage strength {#forca}

Count of the obligations in the matrix `_matriz/dora.yaml` (excluding those addressed to the authorities). The section [“What this Manual covers and what stays out”](#cobertura) lists them.

| Strength | Obligations |
|---|--:|
| Covers | 151 |
| Partial | 115 |
| Supports evidence | 123 |
| Gap | 3 |
| Out of scope | 234 |

## What this Manual covers and what stays out {#cobertura}

All the obligations of the matrix `_matriz/dora.yaml` in three categories: what the Manual **covers**, and in what form; the **declared gaps** (what it does not cover by omission); and what is **out of scope**, with the reason. Generated from the matrix; no obligation is left in silence. The 13 obligations addressed to the authorities create no duty for the organisation and are not listed.

### Covers (274) {#cobre}

Strength “covers” or “supports evidence”. The form is the Manual's response: catalogue requirement, policy, section, floor or requirement added by the regime.

| Obligation | Reference | Strength | Form |
|---|---|---|---|
| DORA-4-1 | Article 4(1) | Supports evidence | [Policy 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); `CLA-003` |
| DORA-4-2 | Article 4(2) | Supports evidence | [Policy 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); `CLA-003` |
| DORA-5-1 | Article 5(1) | Supports evidence | `GOV-001`; [Governance and ICT Risk Management (DORA Articles 5–6)](/sbd-toe/cross-check-normativo/dora/intro#governação-e-gestão-de-risco-tic-artigos-56-dora) |
| DORA-5-2 | Article 5(2), first subparagraph | Supports evidence | `GOV-001`; [Governance and ICT Risk Management (DORA Articles 5–6)](/sbd-toe/cross-check-normativo/dora/intro#governação-e-gestão-de-risco-tic-artigos-56-dora) |
| DORA-5-2-a | Article 5(2), point (a) | Supports evidence | `GOV-001` |
| DORA-5-2-b | Article 5(2), point (b) | Supports evidence | `GOV-001`; [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) |
| DORA-5-2-c | Article 5(2), point (c) | Supports evidence | `GOV-002`; `GOV-003` |
| DORA-5-2-d | Article 5(2), point (d) | Supports evidence | [Policy 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível) |
| DORA-5-2-e | Article 5(2), point (e) | Supports evidence | [Policy 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp) |
| DORA-5-2-h | Article 5(2), point (h) | Supports evidence | [Policy 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence); `GOV-006` |
| DORA-5-2-i | Article 5(2), point (i) | Supports evidence | [Policy 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte); [Policy 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente) |
| DORA-6-1 | Article 6(1) | Supports evidence | `GOV-001`; [Policy 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); [Policy 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível); [Policy 04 §3.1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#31-cadências-mínimas-obrigatórias) |
| DORA-6-5 | Article 6(5) | Supports evidence | `GOV-010` |
| DORA-6-6 | Article 6(6) | Supports evidence | [Policy 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte) |
| DORA-6-7 | Article 6(7) | Supports evidence | `GOV-010` |
| DORA-6-8 | Article 6(8), introductory wording | Supports evidence | `GOV-001`; [What this document is for](/sbd-toe/sbd-manual/governanca-contratacao/kpis-kri-executivo#para-que-serve-este-documento) |
| DORA-6-8-a | Article 6(8), point (a) | Supports evidence | `GOV-001` |
| DORA-6-8-b | Article 6(8), point (b) | Supports evidence | [Policy 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível); [Policy 03 §7](/sbd-toe/assets/policies/policy-aceitacao-risco#7-alçadas-de-aprovação) |
| DORA-6-8-f | Article 6(8), point (f) | Supports evidence | [Policy 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte) |
| DORA-6-8-h | Article 6(8), point (h) | Supports evidence | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-8-3 | Article 8(3) | Covers | [Policy 04 §4.1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#41-triggers-que-obrigam-a-revisão-imediata); `CLA-006`; `ARC-009`; `THR-006` |
| DORA-9-1 | Article 9(1) | Covers | [6️⃣ Essential Logging and Monitoring (Ch. 12)](/sbd-toe/sbd-manual/fundamentos/baseline#6️⃣-registo-e-monitorização-essencial-cap-12); `OPS-001`; `OPS-005` |
| DORA-9-3-a | Article 9(3), point (a) | Covers | `ENC-001`; `INT-003`; `INT-004` |
| DORA-9-4-a | Article 9(4), point (a) | Supports evidence | `GOV-001` |
| DORA-9-4-d | Article 9(4), point (d) | Covers | `ENC-007`; `AUT-001`; [🛡️ Security requirements per environment](/sbd-toe/sbd-manual/deploy-seguro/addon/08-segregacao-e-validacao-operacional#️-requisitos-de-segurança-por-ambiente); `CFG-006`; `ENC-007` |
| DORA-10-1-p2 | Article 10(1), second subparagraph | Covers | `OPS-007`; [Policy 30 §7](/sbd-toe/assets/policies/policy-monitorizacao-seguranca#7-validação-e-tuning-de-regras-de-detecção) |
| DORA-10-2 | Article 10(2) | Covers | `OPS-005`; `OPS-008`; [Policy 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp) |
| DORA-11-6-p3 | Article 11(6), third subparagraph | Supports evidence | [Policy 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp) |
| DORA-11-8 | Article 11(8) | Covers | [Policy 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); [Policy 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação); `LOG-009` |
| DORA-12-1-a | Article 12(1), point (a) | Covers | `OPS-016` |
| DORA-12-1-b | Article 12(1), point (b) | Covers | [Policy 27 §7](/sbd-toe/assets/policies/policy-rollback#7-teste-periódico-de-rollback); [Policy 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação); `OPS-017` |
| DORA-12-2 | Article 12(2) | Covers | `OPS-016`; `OPS-016` |
| DORA-12-3 | Article 12(3) | Covers | `OPS-016` |
| DORA-12-4 | Article 12(4) | Covers | `CTX-DORA-R01` |
| DORA-12-6 | Article 12(6) | Covers | [🔁 Practical mapping between DRP/BIA and security risk](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia#-mapeamento-prático-entre-drpbia-e-risco-de-segurança); [Policy 27 §6](/sbd-toe/assets/policies/policy-rollback#6-rto-de-rollback-por-nível); `OPS-017` |
| DORA-13-1 | Article 13(1) | Covers | [Policy 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção); [Ch. 12 US-16](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-16---cobertura-attck-e-priorização-epsskev); [Policy 11 §7](/sbd-toe/assets/policies/policy-sbom#7-inventário-em-produção) |
| DORA-13-2 | Article 13(2), first and third subparagraphs | Covers | [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); [Policy 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| DORA-13-3 | Article 13(3) | Covers | [Policy 04 §4.1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#41-triggers-que-obrigam-a-revisão-imediata); `CLA-006`; `TRN-006` |
| DORA-13-4 | Article 13(4) | Supports evidence | `GOV-011`; [Policy 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte) |
| DORA-13-5 | Article 13(5) | Supports evidence | [Policy 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte); [What this document is for](/sbd-toe/sbd-manual/governanca-contratacao/kpis-kri-executivo#para-que-serve-este-documento) |
| DORA-13-7 | Article 13(7) | Supports evidence | [Policy 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção); `TRN-006` |
| DORA-14-3 | Article 14(3) | Supports evidence | [Policy 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente) |
| DORA-16-1-a | Article 16(1), second subparagraph, point (a) | Supports evidence | `GOV-001`; [Policy 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); [Policy 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível) |
| DORA-16-1-b | Article 16(1), second subparagraph, point (b) | Covers | [6️⃣ Essential Logging and Monitoring (Ch. 12)](/sbd-toe/sbd-manual/fundamentos/baseline#6️⃣-registo-e-monitorização-essencial-cap-12); `OPS-001` |
| DORA-16-1-d | Article 16(1), second subparagraph, point (d) | Covers | `OPS-005`; [Policy 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp) |
| DORA-16-1-f | Article 16(1), second subparagraph, point (f) | Covers | [Policy 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação); [Policy 27 §7](/sbd-toe/assets/policies/policy-rollback#7-teste-periódico-de-rollback); `OPS-016`; `OPS-016` |
| DORA-16-2 | Article 16(2) | Supports evidence | `GOV-010` |
| DORA-17-1 | Article 17(1) | Covers | [Policy 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade); [Policy 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade); [Policy 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp); [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); `OPS-007` |
| DORA-17-2 | Article 17(2) | Covers | `CTX-DORA-R03`; [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); [Policy 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| DORA-17-3-a | Article 17(3), point (a) | Covers | `OPS-005`; `LOG-007` |
| DORA-17-3-b | Article 17(3), point (b) | Covers | `CTX-DORA-R02`; [Policy 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação); [Policy 31 §3](/sbd-toe/assets/policies/policy-gestao-alertas#3-classificação-de-alertas); [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); [Incidents, Classification and Reporting (DORA Articles 17–23)](/sbd-toe/cross-check-normativo/dora/intro#incidentes-classificação-e-reporte-artigos-1723-dora) |
| DORA-17-3-c | Article 17(3), point (c) | Covers | [Policy 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta); [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| DORA-17-3-d | Article 17(3), point (d) | Covers | [Policy 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente); [Policy 31 §5](/sbd-toe/assets/policies/policy-gestao-alertas#5-escalonamento-automático); [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-17-3-f | Article 17(3), point (f) | Covers | [Policy 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); [Policy 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação) |
| DORA-18-1 | Article 18(1), points (a) to (f) | Covers | `CTX-DORA-R02`; [Policy 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação); [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); [Incidents, Classification and Reporting (DORA Articles 17–23)](/sbd-toe/cross-check-normativo/dora/intro#incidentes-classificação-e-reporte-artigos-1723-dora) |
| DORA-18-2 | Article 18(2) | Supports evidence | [Ch. 12 US-16](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-16---cobertura-attck-e-priorização-epsskev) |
| DORA-19-1 | Article 19(1), first, third, fourth and fifth subparagraphs | Supports evidence | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| DORA-19-3 | Article 19(3), first subparagraph | Supports evidence | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-19-4-a | Article 19(4), point (a) | Supports evidence | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-19-4-b | Article 19(4), point (b) | Supports evidence | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-19-4-c | Article 19(4), point (c) | Supports evidence | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem) |
| DORA-24-1 | Article 24(1) and (2) | Covers | `TST-001`; [Policy 19 §2.1](/sbd-toe/assets/policies/policy-estrategia-testes#21-matriz-de-obrigatoriedade-por-nível) |
| DORA-24-3 | Article 24(3) | Covers | `TST-001`; `CLA-003` |
| DORA-24-5 | Article 24(5) | Covers | `TST-003`; [Policy 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); `TST-006` |
| DORA-24-6 | Article 24(6) | Covers | [Policy 36 §2](/sbd-toe/assets/policies/policy-pentesting#2-âmbito-e-obrigatoriedade); [Policy 36 §9](/sbd-toe/assets/policies/policy-pentesting#9-cadência-de-pentesting); `TST-008` |
| DORA-25-2 | Article 25(2) | Covers | `DPL-003`; `TST-005` |
| DORA-25-3 | Article 25(3) | Covers | `TST-001` |
| DORA-26-2 | Article 26(2) | Supports evidence | [6) Readiness checklist (binary)](/sbd-toe/sbd-manual/testes-seguranca/addon/tlpt-readiness#6-checklist-de-readiness-binário) |
| DORA-26-5 | Article 26(5) | Supports evidence | [Policy 36 §4.2](/sbd-toe/assets/policies/policy-pentesting#42-regras-de-engajamento) |
| DORA-28-1 | Article 28(1), points (a) and (b) | Supports evidence | `GOV-007`; [Policy 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence) |
| DORA-28-2 | Article 28(2) | Supports evidence | [Policy 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence); `GOV-006` |
| DORA-28-3 | Article 28(3), first subparagraph | Supports evidence | `GOV-008`; [Management of Critical Suppliers (DORA Articles 28–30)](/sbd-toe/cross-check-normativo/dora/intro#gestão-de-fornecedores-críticos-artigos-2830-dora) |
| DORA-28-4-a | Article 28(4), point (a) | Supports evidence | `GOV-007` |
| DORA-28-4-c | Article 28(4), point (c) | Supports evidence | [Policy 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação) |
| DORA-28-7 | Article 28(7), points (a) to (d) | Supports evidence | [Policy 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) |
| DORA-28-8 | Article 28(8), first subparagraph | Supports evidence | [Policy 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding) |
| DORA-30-1 | Article 30(1) | Supports evidence | [Policy 33 §4.3](/sbd-toe/assets/policies/policy-contratacao-segura#43-modelo-contratual-de-referência); [8️⃣ Minimum Security Clauses for Suppliers (Ch. 14)](/sbd-toe/sbd-manual/fundamentos/baseline#8️⃣-cláusulas-mínimas-de-segurança-em-fornecedores-cap-14) |
| DORA-30-2-a | Article 30(2), point (a) | Supports evidence | [Policy 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) |
| DORA-30-2-b | Article 30(2), point (b) | Supports evidence | [Policy 33 §10.2](/sbd-toe/assets/policies/policy-contratacao-segura#102-localização-de-processamento) |
| DORA-30-2-c | Article 30(2), point (c) | Supports evidence | [Policy 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) |
| DORA-30-2-d | Article 30(2), point (d) | Supports evidence | [Policy 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding) |
| DORA-30-2-e | Article 30(2), point (e) | Supports evidence | [🏷️ SaaS / Managed services](/sbd-toe/sbd-manual/governanca-contratacao/addon/clausulas-contratuais#️-saas--serviços-geridos) |
| DORA-30-2-f | Article 30(2), point (f) | Supports evidence | [Policy 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) |
| DORA-30-2-h | Article 30(2), point (h) | Supports evidence | [Policy 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) |
| DORA-30-2-i | Article 30(2), point (i) | Supports evidence | [Policy 33 §4.2](/sbd-toe/assets/policies/policy-contratacao-segura#42-cláusulas-adicionais-por-nível-de-risco); `GOV-013` |
| DORA-30-3-b | Article 30(3), point (b) | Supports evidence | [Policy 33 §10.4](/sbd-toe/assets/policies/policy-contratacao-segura#104-sla-de-notificação-prévia) |
| DORA-30-3-c | Article 30(3), point (c) | Supports evidence | [Policy 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação) |
| DORA-30-3-e | Article 30(3), point (e) | Supports evidence | [Policy 33 §4.2](/sbd-toe/assets/policies/policy-contratacao-segura#42-cláusulas-adicionais-por-nível-de-risco); [🏷️ SaaS / Managed services](/sbd-toe/sbd-manual/governanca-contratacao/addon/clausulas-contratuais#️-saas--serviços-geridos) |
| DORA-30-4 | Article 30(4) | Supports evidence | [Policy 33 §4.3](/sbd-toe/assets/policies/policy-contratacao-segura#43-modelo-contratual-de-referência) |
| DORA-RTS1773-1 | Article 1, points (a) to (j) | Supports evidence | [Policy 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence) |
| DORA-RTS1773-3-3 | Article 3(3) | Supports evidence | `GOV-002` |
| DORA-RTS1773-3-6 | Article 3(6), points (a) to (d) | Supports evidence | [🏷️ SaaS / Managed services](/sbd-toe/sbd-manual/governanca-contratacao/addon/clausulas-contratuais#️-saas--serviços-geridos); `GOV-006` |
| DORA-RTS1773-4 | Article 4, points (a) to (f) | Supports evidence | [Policy 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence); [Policy 33 §6.2](/sbd-toe/assets/policies/policy-contratacao-segura#62-reavaliação-periódica); [Policy 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding) |
| DORA-RTS1773-5-2 | Article 5(2), points (a) to (i) | Supports evidence | [Policy 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação) |
| DORA-RTS1773-6-1 | Article 6(1), points (a) to (f) | Supports evidence | [Policy 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence) |
| DORA-RTS1773-6-3 | Article 6(3), points (a) to (e) | Supports evidence | [Policy 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação) |
| DORA-RTS1773-6-4 | Article 6(4) | Supports evidence | [Policy 33 §6.1](/sbd-toe/assets/policies/policy-contratacao-segura#61-indicadores-de-conformidade-a-monitorizar) |
| DORA-RTS1773-8-1 | Article 8(1) | Supports evidence | [Policy 33 §4.3](/sbd-toe/assets/policies/policy-contratacao-segura#43-modelo-contratual-de-referência) |
| DORA-RTS1773-8-2 | Article 8(2), points (a) to (d) | Supports evidence | [Policy 33 §4.2](/sbd-toe/assets/policies/policy-contratacao-segura#42-cláusulas-adicionais-por-nível-de-risco); [🏷️ SaaS / Managed services](/sbd-toe/sbd-manual/governanca-contratacao/addon/clausulas-contratuais#️-saas--serviços-geridos) |
| DORA-RTS1773-8-3 | Article 8(3), points (a) to (h) | Supports evidence | [Policy 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação) |
| DORA-RTS1773-9-1 | Article 9(1) | Supports evidence | [Policy 33 §6.1](/sbd-toe/assets/policies/policy-contratacao-segura#61-indicadores-de-conformidade-a-monitorizar) |
| DORA-RTS1773-9-2 | Article 9(2), points (a) to (e) | Covers | [Policy 33 §6.1](/sbd-toe/assets/policies/policy-contratacao-segura#61-indicadores-de-conformidade-a-monitorizar); [Policy 33 §6.2](/sbd-toe/assets/policies/policy-contratacao-segura#62-reavaliação-periódica) |
| DORA-RTS1773-9-3 | Article 9(3) | Covers | [Policy 33 §6.2](/sbd-toe/assets/policies/policy-contratacao-segura#62-reavaliação-periódica) |
| DORA-RTS1773-9-4 | Article 9(4) | Covers | [Policy 33 §6.2](/sbd-toe/assets/policies/policy-contratacao-segura#62-reavaliação-periódica) |
| DORA-RTS532-3-1 | Article 3(1), first subparagraph and points (a) to (e) | Supports evidence | [Policy 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) |
| DORA-RTS532-3-2 | Article 3(2) | Supports evidence | [Policy 33 §6.2](/sbd-toe/assets/policies/policy-contratacao-segura#62-reavaliação-periódica) |
| DORA-RTS532-4-1-i | Article 4(1), point (i) | Supports evidence | [Policy 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis); `GOV-006` |
| DORA-RTS1774-1 | Article 1 | Supports evidence | [Policy 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); `CLA-003` |
| DORA-RTS1774-2-1 | Article 2(1) | Supports evidence | `GOV-001` |
| DORA-RTS1774-2-1-c | Article 2(1), point (c) | Covers | `ENC-001`; `ENC-002`; `ENC-003`; `ENC-009` |
| DORA-RTS1774-2-2-a | Article 2(2), point (a) | Supports evidence | `GOV-001` |
| DORA-RTS1774-2-2-b | Article 2(2), point (b) | Supports evidence | `GOV-001` |
| DORA-RTS1774-2-2-c | Article 2(2), point (c) | Covers | `GOV-004`; `GOV-011`; [Policy 05 §3](/sbd-toe/assets/policies/policy-gestao-excecoes#3-princípios-fundamentais) |
| DORA-RTS1774-2-2-d | Article 2(2), point (d) | Supports evidence | `GOV-002` |
| DORA-RTS1774-2-2-f | Article 2(2), point (f) | Supports evidence | [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) |
| DORA-RTS1774-2-2-h | Article 2(2), point (h) | Covers | [Mapping of catalogues by technical domain](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos) |
| DORA-RTS1774-2-2-i | Article 2(2), point (i) | Supports evidence | `GOV-001` |
| DORA-RTS1774-2-2-j | Article 2(2), point (j) | Supports evidence | `GOV-010` |
| DORA-RTS1774-2-2-k | Article 2(2), point (k) | Supports evidence | `GOV-010` |
| DORA-RTS1774-3 | Article 3, first subparagraph | Supports evidence | [Policy 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); [Policy 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível) |
| DORA-RTS1774-3-a | Article 3, point (a) | Supports evidence | [Policy 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível); [Policy 03 §7](/sbd-toe/assets/policies/policy-aceitacao-risco#7-alçadas-de-aprovação) |
| DORA-RTS1774-3-b | Article 3, point (b) | Covers | [Policy 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); `THR-003`; [Ch. 12 US-16](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-16---cobertura-attck-e-priorização-epsskev) |
| DORA-RTS1774-3-c | Article 3, point (c) | Covers | `THR-004`; [Policy 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível) |
| DORA-RTS1774-3-d | Article 3, point (d) | Covers | `CLA-007`; [Policy 03 §8](/sbd-toe/assets/policies/policy-aceitacao-risco#8-reavaliação-e-expiração); `GOV-004` |
| DORA-RTS1774-3-d-iv | Article 3, point (d)(iv) | Covers | [Policy 05 §7](/sbd-toe/assets/policies/policy-gestao-excecoes#7-prazos-máximos-de-validade-ttl); [Policy 03 §8](/sbd-toe/assets/policies/policy-aceitacao-risco#8-reavaliação-e-expiração) |
| DORA-RTS1774-3-e | Article 3, point (e) | Covers | [Policy 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção); [Ch. 12 US-16](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-16---cobertura-attck-e-priorização-epsskev); [Policy 11 §7](/sbd-toe/assets/policies/policy-sbom#7-inventário-em-produção) |
| DORA-RTS1774-3-f | Article 3, point (f) | Supports evidence | [Policy 04 §4.1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#41-triggers-que-obrigam-a-revisão-imediata) |
| DORA-RTS1774-5-2 | Article 5(2) | Covers | [Policy 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); `CLA-001` |
| DORA-RTS1774-6-1 | Article 6(1) | Covers | `ENC-001`; `ENC-002`; `ENC-003`; `ENC-007` |
| DORA-RTS1774-6-2 | Article 6(2), first subparagraph | Covers | `ENC-002`; `CLA-003` |
| DORA-RTS1774-6-2-a | Article 6(2), point (a) | Covers | `ENC-001`; `ENC-002` |
| DORA-RTS1774-6-2-c | Article 6(2), point (c) | Covers | `ENC-001`; `INT-003` |
| DORA-RTS1774-6-2-d | Article 6(2), point (d) | Covers | `ENC-007`; [Policy 18 §6.4](/sbd-toe/assets/policies/policy-gestao-segredos#64-ciclo-de-vida-das-chaves-e-inventário-de-certificados); `ENC-007`; `CFG-006`; `ENC-002` |
| DORA-RTS1774-6-3 | Article 6(3) | Covers | `ENC-003`; `GOV-004` |
| DORA-RTS1774-6-4 | Article 6(4) | Covers | `ENC-003` |
| DORA-RTS1774-6-5 | Article 6(5) | Covers | `GOV-004`; [Policy 05 §3](/sbd-toe/assets/policies/policy-gestao-excecoes#3-princípios-fundamentais) |
| DORA-RTS1774-7-1 | Article 7(1) | Covers | `ENC-007`; [Policy 18 §6.4](/sbd-toe/assets/policies/policy-gestao-segredos#64-ciclo-de-vida-das-chaves-e-inventário-de-certificados); `ENC-007`; [Policy 18 §6](/sbd-toe/assets/policies/policy-gestao-segredos#6-ttl-rotação-e-revogação); [Policy 18 §6.3](/sbd-toe/assets/policies/policy-gestao-segredos#63-revogação-por-exposição-suspeita) |
| DORA-RTS1774-7-2 | Article 7(2) | Covers | `CFG-006`; `ENC-002` |
| DORA-RTS1774-7-3 | Article 7(3) | Covers | [Policy 18 §6.3](/sbd-toe/assets/policies/policy-gestao-segredos#63-revogação-por-exposição-suspeita); `ENC-007` |
| DORA-RTS1774-7-4 | Article 7(4) | Covers | `ENC-007`; [Policy 18 §6.4](/sbd-toe/assets/policies/policy-gestao-segredos#64-ciclo-de-vida-das-chaves-e-inventário-de-certificados) |
| DORA-RTS1774-7-5 | Article 7(5) | Covers | [Policy 18 §6.4](/sbd-toe/assets/policies/policy-gestao-segredos#64-ciclo-de-vida-das-chaves-e-inventário-de-certificados); `API-005` |
| DORA-RTS1774-8-2-b-i | Article 8(2), point (b)(i) | Covers | `OPS-016`; `OPS-016` |
| DORA-RTS1774-8-2-b-iii | Article 8(2), point (b)(iii) | Covers | `LOG-001`; `LOG-002`; [Policy 29 §4](/sbd-toe/assets/policies/policy-logging-estruturado#4-eventos-de-segurança-obrigatórios) |
| DORA-RTS1774-8-2-b-iv | Article 8(2), point (b)(iv) | Covers | [Policy 36 §4.2](/sbd-toe/assets/policies/policy-pentesting#42-regras-de-engajamento); `TST-005` |
| DORA-RTS1774-8-2-b-v | Article 8(2), point (b)(v) and second subparagraph | Covers | `CFG-002`; `IAC-002`; [Policy 25 §6](/sbd-toe/assets/policies/policy-deploy-seguro#6-separação-de-ambientes-e-dados); `ARC-011` |
| DORA-RTS1774-8-2-b-vi | Article 8(2), point (b)(vi) | Covers | `CFG-002`; `IAC-002` |
| DORA-RTS1774-10-1 | Article 10(1) | Covers | [Policy 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção); [Policy 12 §6.1](/sbd-toe/assets/policies/policy-excecoes-cve#61-ttl-por-severidade-e-tipo); [Policy 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); `TST-003` |
| DORA-RTS1774-10-2-a | Article 10(2), point (a) | Covers | [Policy 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção) |
| DORA-RTS1774-10-2-d | Article 10(2), point (d), and fourth subparagraph | Covers | `DEP-001`; `DEP-007`; `DEP-008`; [Policy 11 §7](/sbd-toe/assets/policies/policy-sbom#7-inventário-em-produção) |
| DORA-RTS1774-10-2-e | Article 10(2), point (e) | Covers | `DST-007`; `GOV-015` |
| DORA-RTS1774-10-2-f | Article 10(2), point (f), and fifth subparagraph | Covers | [Policy 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); [Ch. 12 US-16](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-16---cobertura-attck-e-priorização-epsskev) |
| DORA-RTS1774-10-2-g | Article 10(2), point (g) | Covers | `TST-006`; `DEP-010` |
| DORA-RTS1774-10-2-h | Article 10(2), point (h) | Covers | `TST-003`; `DEP-010` |
| DORA-RTS1774-10-4-a | Article 10(4), point (a) | Covers | `DEP-008`; [Policy 13 §2](/sbd-toe/assets/policies/policy-atualizacao-automatica#2-âmbito-e-obrigatoriedade) |
| DORA-RTS1774-10-4-b | Article 10(4), point (b) | Covers | [Policy 26 §7](/sbd-toe/assets/policies/policy-aprovacao-release#7-releases-de-emergência); [Policy 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta) |
| DORA-RTS1774-10-4-c | Article 10(4), point (c) | Covers | `DPL-007`; `CFG-002` |
| DORA-RTS1774-10-4-d | Article 10(4), point (d) | Covers | [Policy 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); `DEP-007`; [Policy 05 §7](/sbd-toe/assets/policies/policy-gestao-excecoes#7-prazos-máximos-de-validade-ttl) |
| DORA-RTS1774-11-1 | Article 11(1) | Covers | `CLA-003` |
| DORA-RTS1774-11-2-a | Article 11(2), point (a) | Covers | `ACC-001`; `ACC-006`; `CLA-003` |
| DORA-RTS1774-12-1 | Article 12(1) | Covers | `OPS-001`; `LOG-001`; [Policy 29 §4](/sbd-toe/assets/policies/policy-logging-estruturado#4-eventos-de-segurança-obrigatórios) |
| DORA-RTS1774-12-2-a | Article 12(2), point (a) and second subparagraph | Covers | `OPS-002`; `OPS-003`; [Policy 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs) |
| DORA-RTS1774-12-2-b | Article 12(2), point (b) | Covers | `LOG-002`; `LOG-009` |
| DORA-RTS1774-13-a | Article 13, point (a) | Covers | `ARC-006`; `ARC-011`; `CNT-012` |
| DORA-RTS1774-13-e | Article 13, point (e) | Covers | `ENC-001`; `INT-004` |
| DORA-RTS1774-13-g | Article 13, point (g) | Covers | `ARC-002`; `ARC-008` |
| DORA-RTS1774-13-h | Article 13, point (h) and second subparagraph | Covers | `ARC-006` |
| DORA-RTS1774-13-j | Article 13, point (j) | Covers | [Policy 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); [Policy 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta) |
| DORA-RTS1774-13-m | Article 13, point (m) | Supports evidence | `GOV-006` |
| DORA-RTS1774-14-1 | Article 14(1) | Covers | `ENC-001`; `INT-003` |
| DORA-RTS1774-14-1-a | Article 14(1), point (a) | Covers | `ENC-001`; `INT-005` |
| DORA-RTS1774-14-1-c | Article 14(1), point (c) | Supports evidence | [Policy 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) |
| DORA-RTS1774-14-2 | Article 14(2) | Covers | `ENC-001`; `INT-005`; `CLA-003` |
| DORA-RTS1774-15-1 | Article 15(1) | Supports evidence | `REQ-001`; [Policy 09 §6.1](/sbd-toe/assets/policies/policy-arquitetura-segura#61-inventário-de-trust-boundaries) |
| DORA-RTS1774-15-2 | Article 15(2) | Supports evidence | `REQ-001` |
| DORA-RTS1774-15-3 | Article 15(3), points (a) to (f) | Supports evidence | `REQ-001`; `ARC-003` |
| DORA-RTS1774-15-3-g | Article 15(3), point (g) | Covers | `DPL-001`; `DPL-003`; `ARC-012` |
| DORA-RTS1774-15-4 | Article 15(4) | Supports evidence | `REQ-007` |
| DORA-RTS1774-16-1 | Article 16(1), first subparagraph | Covers | `DEV-001`; [Policy 15 §2](/sbd-toe/assets/policies/policy-revisao-codigo#2-âmbito-e-obrigatoriedade); [4️⃣ Basic Coding Guidelines and Automated Validation (Ch. 06)](/sbd-toe/sbd-manual/fundamentos/baseline#4️⃣-coding-guidelines-básicas-e-validação-automática-cap-06) |
| DORA-RTS1774-16-1-a | Article 16(1), point (a) | Covers | `DEV-001`; `DEV-002`; `DEV-003` |
| DORA-RTS1774-16-1-b | Article 16(1), point (b) | Covers | `REQ-001`; `REQ-002`; `REQ-003` |
| DORA-RTS1774-16-1-c | Article 16(1), point (c) | Covers | [🛠️ Practices](/sbd-toe/sbd-manual/cicd-seguro/addon/gestao-codigo-fonte#️-práticas); `CIC-007`; `DPL-002`; [Policy 20 §6](/sbd-toe/assets/policies/policy-release-seguro#6-imutabilidade-do-artefacto) |
| DORA-RTS1774-16-2 | Article 16(2), first subparagraph | Covers | `DPL-001`; `DPL-003`; `TST-001` |
| DORA-RTS1774-16-3-a | Article 16(3), point (a) | Covers | `DEV-003`; `TST-002` |
| DORA-RTS1774-16-3-b | Article 16(3), point (b) | Covers | `TST-003`; [Policy 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução) |
| DORA-RTS1774-16-3-c | Article 16(3), point (c) | Covers | `TST-003`; `GOV-011` |
| DORA-RTS1774-16-4 | Article 16(4) | Covers | `DEP-002`; [Policy 19 §2.1](/sbd-toe/assets/policies/policy-estrategia-testes#21-matriz-de-obrigatoriedade-por-nível) |
| DORA-RTS1774-16-5 | Article 16(5) | Covers | [Policy 25 §6](/sbd-toe/assets/policies/policy-deploy-seguro#6-separação-de-ambientes-e-dados); [🛡️ Security requirements per environment](/sbd-toe/sbd-manual/deploy-seguro/addon/08-segregacao-e-validacao-operacional#️-requisitos-de-segurança-por-ambiente); [4.1 Mandatory prescriptions](/sbd-toe/sbd-manual/testes-seguranca/addon/evidencia-reprodutibilidade#41-prescrições-obrigatórias) |
| DORA-RTS1774-16-7 | Article 16(7) | Covers | [🛠️ Practices](/sbd-toe/sbd-manual/cicd-seguro/addon/gestao-codigo-fonte#️-práticas); [🛠️ Practices](/sbd-toe/sbd-manual/cicd-seguro/addon/gestao-codigo-fonte#️-práticas); `CIC-001` |
| DORA-RTS1774-16-8 | Article 16(8) | Covers | `DEP-002`; `DEP-006`; [Policy 10 §3](/sbd-toe/assets/policies/policy-dependencias#3-critérios-de-aprovação-de-dependências) |
| DORA-RTS1774-17-1-a | Article 17(1), point (a) | Covers | `DPL-003`; `CIC-004` |
| DORA-RTS1774-17-1-b | Article 17(1), point (b) | Covers | [Policy 22 §5](/sbd-toe/assets/policies/policy-aprovacao-plan-iac#5-separação-de-funções-sod); `CIC-011`; `DPL-001` |
| DORA-RTS1774-17-1-c | Article 17(1), point (c) | Covers | `CIC-008`; `DPL-007` |
| DORA-RTS1774-17-1-e | Article 17(1), point (e) | Covers | `DPL-005`; [Policy 27 §7](/sbd-toe/assets/policies/policy-rollback#7-teste-periódico-de-rollback) |
| DORA-RTS1774-17-1-f | Article 17(1), point (f) | Covers | [Policy 26 §7](/sbd-toe/assets/policies/policy-aprovacao-release#7-releases-de-emergência); [Policy 22 §9](/sbd-toe/assets/policies/policy-aprovacao-plan-iac#9-apply-de-emergência) |
| DORA-RTS1774-17-1-g | Article 17(1), point (g) | Covers | [Policy 26 §7](/sbd-toe/assets/policies/policy-aprovacao-release#7-releases-de-emergência); [Policy 22 §9](/sbd-toe/assets/policies/policy-aprovacao-plan-iac#9-apply-de-emergência) |
| DORA-RTS1774-17-1-h | Article 17(1), point (h) | Covers | `ARC-009`; `REQ-005`; [Policy 04 §4.1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#41-triggers-que-obrigam-a-revisão-imediata) |
| DORA-RTS1774-19-a | Article 19, point (a) | Supports evidence | `TRN-002`; `GOV-002` |
| DORA-RTS1774-19-b-i | Article 19, point (b)(i) | Supports evidence | `TRN-002`; `TRN-007`; `GOV-013` |
| DORA-RTS1774-19-b-ii | Article 19, point (b)(ii) | Supports evidence | `TRN-002` |
| DORA-RTS1774-20-1 | Article 20(1) | Covers | `ACC-004`; `CIC-009`; [Ch. 07 US-20](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-20); `GOV-017` |
| DORA-RTS1774-20-2-b | Article 20(2), point (b) and third subparagraph | Covers | `ACC-008`; [Policy 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding); `GOV-014`; `GOV-017`; `GOV-017` |
| DORA-RTS1774-21-a | Article 21, point (a) | Covers | `ACC-001`; `ACC-002` |
| DORA-RTS1774-21-b | Article 21, point (b) | Covers | `CIC-008`; [Policy 22 §5](/sbd-toe/assets/policies/policy-aprovacao-plan-iac#5-separação-de-funções-sod); `ACC-004` |
| DORA-RTS1774-21-c | Article 21, point (c) | Covers | `ACC-004`; [Ch. 07 US-20](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-20); `GOV-017`; `GOV-017` |
| DORA-RTS1774-21-d | Article 21, point (d) | Covers | `ACC-003`; `ACC-005`; `ACC-006` |
| DORA-RTS1774-21-e | Article 21, point (e)(i) to (iii) | Covers | `ACC-008`; [Policy 33 §7.2](/sbd-toe/assets/policies/policy-contratacao-segura#72-prazos-de-offboarding); `GOV-016`; `GOV-016` |
| DORA-RTS1774-21-e-ii | Article 21, point (e)(ii), and the subparagraph 'For the purposes of point (e)(ii)' | Covers | `ACC-004`; `GOV-016`; `GOV-016` |
| DORA-RTS1774-21-e-iv | Article 21, point (e)(iv) | Covers | `ACC-010`; `GOV-014`; `ACC-010`; `GOV-014` |
| DORA-RTS1774-21-f-i | Article 21, point (f)(i) | Covers | `AUT-001`; `AUT-008`; `CLA-003` |
| DORA-RTS1774-21-f-ii | Article 21, point (f)(ii) | Covers | `AUT-001`; [🛡️ Security requirements per environment](/sbd-toe/sbd-manual/deploy-seguro/addon/08-segregacao-e-validacao-operacional#️-requisitos-de-segurança-por-ambiente); `GOV-016` |
| DORA-RTS1774-22-a | Article 22, point (a) | Covers | [Policy 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade); [Policy 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp) |
| DORA-RTS1774-22-c | Article 22, point (c) | Covers | `OPS-005`; `OPS-007` |
| DORA-RTS1774-22-d | Article 22, point (d) and second subparagraph | Covers | [Policy 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-RTS1774-22-e | Article 22, point (e) | Covers | [Policy 32 §4.7](/sbd-toe/assets/policies/policy-irp#47-análise-de-recorrência); [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `OPS-010` |
| DORA-RTS1774-23-1 | Article 23(1) | Covers | [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); `OPS-007` |
| DORA-RTS1774-23-2-c | Article 23(2), point (c) | Covers | [Policy 31 §3](/sbd-toe/assets/policies/policy-gestao-alertas#3-classificação-de-alertas); `OPS-006`; [Policy 31 §7](/sbd-toe/assets/policies/policy-gestao-alertas#7-alertas-p1-em-horas-não-laborais-on-call) |
| DORA-RTS1774-23-2-d | Article 23(2), point (d) | Covers | `LOG-004`; `OPS-009` |
| DORA-RTS1774-23-5 | Article 23(5) and (6) | Covers | [Policy 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp) |
| DORA-RTS1774-24-1-b | Article 24(1), point (b) | Supports evidence | [🔁 Practical mapping between DRP/BIA and security risk](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia#-mapeamento-prático-entre-drpbia-e-risco-de-segurança) |
| DORA-RTS1774-28-1 | Article 28(1) | Supports evidence | `GOV-001` |
| DORA-RTS1774-28-2-a | Article 28(2), point (a) | Supports evidence | `GOV-001` |
| DORA-RTS1774-28-2-b | Article 28(2), point (b) | Supports evidence | `GOV-002`; `GOV-003` |
| DORA-RTS1774-28-2-c | Article 28(2), point (c) | Supports evidence | `REQ-001` |
| DORA-RTS1774-28-2-d | Article 28(2), point (d) | Supports evidence | `CLA-002`; [🔁 Practical mapping between DRP/BIA and security risk](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia#-mapeamento-prático-entre-drpbia-e-risco-de-segurança) |
| DORA-RTS1774-28-2-f | Article 28(2), points (f) and (g) | Supports evidence | `GOV-001` |
| DORA-RTS1774-28-2-h | Article 28(2), point (h) | Supports evidence | `TRN-001` |
| DORA-RTS1774-28-2-i | Article 28(2), point (i) | Supports evidence | [Policy 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte) |
| DORA-RTS1774-28-5 | Article 28(5) | Supports evidence | [Policy 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte) |
| DORA-RTS1774-28-6 | Article 28(6) | Supports evidence | `GOV-010` |
| DORA-RTS1774-29-1 | Article 29(1) | Supports evidence | `GOV-001` |
| DORA-RTS1774-30-2 | Article 30(2) | Supports evidence | `GOV-007` |
| DORA-RTS1774-31-1 | Article 31(1) | Covers | [Policy 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível); [Policy 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); `THR-004`; [Policy 04 §4.1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#41-triggers-que-obrigam-a-revisão-imediata) |
| DORA-RTS1774-31-2 | Article 31(2) | Covers | [Policy 02 §5](/sbd-toe/assets/policies/policy-classificacao-risco#5-cadência-de-revisão-periódica); `CLA-005` |
| DORA-RTS1774-31-3 | Article 31(3) | Covers | [Policy 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção); [Policy 08 §4.2](/sbd-toe/assets/policies/policy-threat-modeling#42-cadência-periódica) |
| DORA-RTS1774-31-4 | Article 31(4) | Covers | `OPS-005`; [Policy 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp) |
| DORA-RTS1774-33-a | Article 33, point (a) | Covers | `ACC-002`; `ACC-001` |
| DORA-RTS1774-33-b | Article 33, point (b) | Covers | `ACC-004`; `LOG-002` |
| DORA-RTS1774-33-c | Article 33, point (c) and second subparagraph | Covers | `ACC-004`; [Policy 29 §4](/sbd-toe/assets/policies/policy-logging-estruturado#4-eventos-de-segurança-obrigatórios); `GOV-016` |
| DORA-RTS1774-33-d | Article 33, point (d) and third subparagraph | Covers | `AUT-001`; [🛡️ Security requirements per environment](/sbd-toe/sbd-manual/deploy-seguro/addon/08-segregacao-e-validacao-operacional#️-requisitos-de-segurança-por-ambiente); `GOV-016` |
| DORA-RTS1774-33-e | Article 33, point (e) | Covers | `ACC-010`; `ACC-008`; `ACC-010` |
| DORA-RTS1774-34-d | Article 34, point (d) | Covers | `DEP-002`; `CNT-002`; [Policy 10 §9](/sbd-toe/assets/policies/policy-dependencias#9-auditoria-periódica); [Policy 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução) |
| DORA-RTS1774-34-g | Article 34, point (g) | Covers | [6️⃣ Essential Logging and Monitoring (Ch. 12)](/sbd-toe/sbd-manual/fundamentos/baseline#6️⃣-registo-e-monitorização-essencial-cap-12); `OPS-005`; `OPS-009` |
| DORA-RTS1774-34-h | Article 34, point (h) | Covers | [Ch. 12 US-16](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-16---cobertura-attck-e-priorização-epsskev); [Policy 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção) |
| DORA-RTS1774-35-c | Article 35, point (c) | Covers | `ARC-002`; `ARC-006` |
| DORA-RTS1774-35-d | Article 35, point (d) | Covers | `ENC-001`; `INT-005` |
| DORA-RTS1774-36-1 | Article 36(1) | Covers | `TST-001` |
| DORA-RTS1774-36-2 | Article 36(2) | Covers | `TST-001`; `TST-007` |
| DORA-RTS1774-36-3 | Article 36(3) | Covers | `TST-003`; `TST-006` |
| DORA-RTS1774-37 | Article 37, first subparagraph | Covers | `DEV-001`; [4️⃣ Basic Coding Guidelines and Automated Validation (Ch. 06)](/sbd-toe/sbd-manual/fundamentos/baseline#4️⃣-coding-guidelines-básicas-e-validação-automática-cap-06) |
| DORA-RTS1774-37-a | Article 37, point (a) | Covers | `REQ-001`; `REQ-002` |
| DORA-RTS1774-37-b | Article 37, point (b) | Covers | `DPL-001`; `DPL-003` |
| DORA-RTS1774-37-c | Article 37, point (c) | Covers | [🛠️ Practices](/sbd-toe/sbd-manual/cicd-seguro/addon/gestao-codigo-fonte#️-práticas); `CIC-007` |
| DORA-RTS1774-38-1 | Article 38(1) | Supports evidence | `REQ-001` |
| DORA-RTS1774-39-2-d | Article 39(2), points (d) to (f) | Covers | [🔁 Practical mapping between DRP/BIA and security risk](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia#-mapeamento-prático-entre-drpbia-e-risco-de-segurança); [Policy 27 §6](/sbd-toe/assets/policies/policy-rollback#6-rto-de-rollback-por-nível); [Policy 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp); `OPS-017`; `OPS-017` |
| DORA-RTS1774-39-2-g | Article 39(2), point (g) | Covers | `OPS-016` |
| DORA-RTS1772-1-4 | Article 1(4) | Supports evidence | `LOG-010` |
| DORA-RTS1772-8-1 | Article 8(1); Article 9 | Supports evidence | [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); [Incidents, Classification and Reporting (DORA Articles 17–23)](/sbd-toe/cross-check-normativo/dora/intro#incidentes-classificação-e-reporte-artigos-1723-dora) |
| DORA-RTS1772-8-2 | Article 8(2), first subparagraph | Covers | `CTX-DORA-R02`; [Policy 32 §4.7](/sbd-toe/assets/policies/policy-irp#47-análise-de-recorrência); [Incidents, Classification and Reporting (DORA Articles 17–23)](/sbd-toe/cross-check-normativo/dora/intro#incidentes-classificação-e-reporte-artigos-1723-dora) |
| DORA-RTS1772-8-2-p2 | Article 8(2), second subparagraph | Covers | `CTX-DORA-R02` |
| DORA-RTS1772-10 | Article 10 | Supports evidence | [Ch. 12 US-16](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-16---cobertura-attck-e-priorização-epsskev) |
| DORA-RTS301-5-1-a | Article 5(1), point (a) | Supports evidence | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-RTS301-5-1-b | Article 5(1), point (b) | Supports evidence | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-RTS301-5-1-c | Article 5(1), point (c) | Supports evidence | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-RTS301-5-2 | Article 5(2) | Supports evidence | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| DORA-RTS1190-4-2-a | Article 4(2), point (a) | Supports evidence | [6) Readiness checklist (binary)](/sbd-toe/sbd-manual/testes-seguranca/addon/tlpt-readiness#6-checklist-de-readiness-binário) |
| DORA-RTS1190-4-2-c | Article 4(2), point (c) | Supports evidence | [Policy 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp) |
| DORA-RTS1190-5-1 | Article 5(1) | Supports evidence | [Policy 36 §4.2](/sbd-toe/assets/policies/policy-pentesting#42-regras-de-engajamento) |
| DORA-RTS1190-5-2 | Article 5(2) | Supports evidence | [Policy 36 §4.2](/sbd-toe/assets/policies/policy-pentesting#42-regras-de-engajamento) |
| DORA-RTS1190-6-1 | Article 6(1) | Supports evidence | [Policy 36 §4.2](/sbd-toe/assets/policies/policy-pentesting#42-regras-de-engajamento) |
| DORA-RTS1190-7-1-i | Article 7(1), point (i) | Supports evidence | [Policy 36 §4.2](/sbd-toe/assets/policies/policy-pentesting#42-regras-de-engajamento) |
| DORA-RTS1190-9-6 | Article 9(6), first sentence; Annex II | Supports evidence | [6) Readiness checklist (binary)](/sbd-toe/sbd-manual/testes-seguranca/addon/tlpt-readiness#6-checklist-de-readiness-binário) |
| DORA-RTS1190-9-7 | Article 9(7) | Supports evidence | [6) Readiness checklist (binary)](/sbd-toe/sbd-manual/testes-seguranca/addon/tlpt-readiness#6-checklist-de-readiness-binário) |
| DORA-RTS1190-10-1 | Article 10(1) | Supports evidence | [6) Readiness checklist (binary)](/sbd-toe/sbd-manual/testes-seguranca/addon/tlpt-readiness#6-checklist-de-readiness-binário); [Ch. 12 US-16](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-16---cobertura-attck-e-priorização-epsskev) |
| DORA-RTS1190-13-2 | Article 13(2) | Supports evidence | `TST-003`; [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem) |

### Declared gap (118) {#lacuna}

Strength “partial” or “gap”: the Manual does not cover, or covers only in part, and says what is missing. Gaps pending an AppSec Core round are marked with the name of the round.

| Obligation | Reference | Strength | How the Manual responds | What is missing |
|---|---|---|---|---|
| DORA-6-2 | Article 6(2) | Partial | `CLA-003`; `ARC-006`; `ACC-006` | Protection of hardware, physical servers, premises and data centres. |
| DORA-6-3 | Article 6(3), first sentence | Partial | `CLA-003`; [Policy 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta) | Impact minimisation measures at entity level (redundancy, continuity). |
| DORA-6-8-c | Article 6(8), point (c) | Partial | `GOV-011`; [What this document is for](/sbd-toe/sbd-manual/governanca-contratacao/kpis-kri-executivo#para-que-serve-este-documento) | The entity's information security objectives set out in the resilience strategy. |
| DORA-6-8-d | Article 6(8), point (d) | Partial | `ARC-007`; `ARC-010` | The entity's ICT reference architecture and changes needed to meet business objectives. |
| DORA-6-8-e | Article 6(8), point (e) | Partial | [6️⃣ Essential Logging and Monitoring (Ch. 12)](/sbd-toe/sbd-manual/fundamentos/baseline#6️⃣-registo-e-monitorização-essencial-cap-12); `OPS-005`; `OPS-007` | Inclusion of the mechanisms in the strategy (the strategy document is organisational). |
| DORA-6-8-g | Article 6(8), point (g) | Partial | `TST-001` | Operational resilience testing strategy (Chapter IV) — the Manual has an application security testing strategy; continuity, performance and scenario tests are missing. |
| DORA-7 | Article 7, points (a) to (d) | Partial | `OPS-015`; `DEP-007` | Capacity sizing (peaks) and technological resilience under conditions of market stress. |
| DORA-8-1 | Article 8(1) | Partial | `CLA-001`; `CLA-005`; `CLA-008`; `DEP-001` | Identification and classification of business functions and roles; the Manual classifies applications (E+D+I), not critical or important functions. |
| DORA-8-2 | Article 8(2) | Partial | `THR-001`; [Policy 08 §4.2](/sbd-toe/assets/policies/policy-threat-modeling#42-cadência-periódica); [Policy 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção) | Formal threat modelling only from L2 onwards; annual review of risk scenarios not prescribed for L1. |
| DORA-8-4 | Article 8(4) | Partial | `CLA-008`; `DEP-001`; `ARC-010`; `IAC-008` | Inventory of hardware, network resources and remote assets; mapping of configuration and interdependencies outside the application perimeter. |
| DORA-8-5 | Article 8(5) | Partial | `DEP-001`; `GOV-007` | Identification of business processes that depend on ICT third parties and of the interconnections with FCIs. |
| DORA-8-6 | Article 8(6) | Partial | `CLA-008`; [Policy 11 §7](/sbd-toe/assets/policies/policy-sbom#7-inventário-em-produção) | Inventories of functions and of third-party dependencies updated upon every major change. |
| DORA-8-7 | Article 8(7) | Partial | [🛠️ Proposed approach](/sbd-toe/sbd-manual/governanca-contratacao/addon/governanca-legada#️-abordagem-proposta); [Policy 04 §4.1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#41-triggers-que-obrigam-a-revisão-imediata) | Specific annual assessment of legacy systems and assessment before/after each connection. |
| DORA-9-2 | Article 9(2) | Partial | `ENC-001`; `ENC-002`; `ENC-009` | Data in use; availability/continuity of systems. |
| DORA-9-3-b | Article 9(3), point (b) | Partial | `ACC-006`; `ENC-009`; `INT-009` | Safeguarding against data loss (backups). |
| DORA-9-3-c | Article 9(3), point (c) | Partial | `ENC-009`; `ACC-006`; `OPS-015` | Prevention of unavailability and data loss (redundancy, backups). |
| DORA-9-3-d | Article 9(3), point (d) | Partial | `CFG-004`; `IAC-007`; [Policy 22 §5](/sbd-toe/assets/policies/policy-aprovacao-plan-iac#5-separação-de-funções-sod) | Controls against human error in the administration of production data (outside IaC/deploy). |
| DORA-9-4-b | Article 9(4), point (b), and second subparagraph | Partial | `ARC-006`; `ARC-011`; `CNT-012`; [Policy 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação) | Configuration of network interconnection for instant severance/segmentation at entity level. |
| DORA-9-4-c | Article 9(4), point (c) | Partial | `ACC-001`; `ACC-002`; `ACC-010` | Physical access. |
| DORA-9-4-e | Article 9(4), point (e), and third subparagraph | Partial | `DPL-001`; `DPL-004`; `CIC-004`; `IAC-007`; [Policy 26 §7](/sbd-toe/assets/policies/policy-aprovacao-release#7-releases-de-emergência) | Hardware/firmware and parameter changes outside pipelines. |
| DORA-9-4-f | Article 9(4), point (f) | Partial | `DEP-007`; [Policy 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); [Policy 13 §2](/sbd-toe/assets/policies/policy-atualizacao-automatica#2-âmbito-e-obrigatoriedade); [Policy 24 §6](/sbd-toe/assets/policies/policy-golden-base-images#6-sla-de-patching) | Patches for operating systems, firmware and hardware outside the base images. |
| DORA-10-1 | Article 10(1) | Partial | [6️⃣ Essential Logging and Monitoring (Ch. 12)](/sbd-toe/sbd-manual/fundamentos/baseline#6️⃣-registo-e-monitorização-essencial-cap-12); `OPS-005`; `OPS-009` | Identification of significant single points of failure; network performance. |
| DORA-10-3 | Article 10(3) | Partial | `OPS-006`; [Policy 31 §7](/sbd-toe/assets/policies/policy-gestao-alertas#7-alertas-p1-em-horas-não-laborais-on-call) | Allocation of human resources to monitoring (organisational decision). |
| DORA-11-2 | Article 11(2), points (a) to (e) | Partial | [Policy 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); [Policy 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação); [Policy 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente) | Continuity plans for critical functions and preliminary impact estimate; the Manual covers incident containment and response. |
| DORA-11-3 | Article 11(3) | Partial | [Policy 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta); [Policy 27 §7](/sbd-toe/assets/policies/policy-rollback#7-teste-periódico-de-rollback) | ICT recovery plans beyond playbooks/rollback; independent internal audit. |
| DORA-11-4 | Article 11(4) | Partial | [Policy 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp) | Testing of continuity plans (incl. outsourced functions); only the IRP and rollback are tested. |
| DORA-11-5 | Article 11(5) | Partial | [🔁 Practical mapping between DRP/BIA and security risk](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia#-mapeamento-prático-entre-drpbia-e-risco-de-segurança) | Performing the BIA and designing redundancy of critical components; the Manual only reuses an existing BIA as a classification input. |
| DORA-11-6-a | Article 11(6), point (a), and second subparagraph | Partial | [Policy 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp); [Policy 27 §7](/sbd-toe/assets/policies/policy-rollback#7-teste-periódico-de-rollback); `CTX-DORA-R01`; `OPS-017` | Tests of the entity's business continuity plans (outside the scope of the Manual); recovery of the application (OPS-016, OPS-017) and switchover to the redundant capacity (CTX-DORA-R01) are prescribed. |
| DORA-12-7 | Article 12(7) | Partial | [Policy 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação); `ENC-009` | Data reconciliation in recovery and in the reconstruction of data from external parties. |
| DORA-13-6 | Article 13(6) | Partial | `TRN-001`; [7️⃣ Initial Security Training (Ch. 13)](/sbd-toe/sbd-manual/fundamentos/baseline#7️⃣-formação-inicial-em-segurança-cap-13); [Policy 37 §2](/sbd-toe/assets/policies/policy-formacao-seguranca#2-âmbito-e-obrigatoriedade) | Mandatory modules for all (non-technical) staff and senior management; digital operational resilience content. |
| DORA-16-1-c | Article 16(1), second subparagraph, point (c) | Partial | `ENC-001`; `ENC-002`; `DEP-007` | Resilience of systems (redundancy). |
| DORA-16-1-e | Article 16(1), second subparagraph, point (e) | Partial | `DEP-001`; `GOV-007` | Dependencies on ICT service providers (not only components/suppliers with access). |
| DORA-16-1-g | Article 16(1), second subparagraph, point (g) | Partial | `TST-001`; [Policy 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp) | Testing of continuity plans. |
| DORA-16-1-h | Article 16(1), second subparagraph, point (h) | Partial | [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `TRN-001` | Training of the management. |
| DORA-17-3-e | Article 17(3), point (e) | Partial | [Policy 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente) | Reporting of major incidents to the management body (only “management” at P1). |
| DORA-24-4 | Article 24(4) | Partial | `THR-007`; `TST-008` | Assurance of testers' independence and management of conflicts of interest of internal testers. |
| DORA-25-1 | Article 25(1) | Partial | [Policy 19 §2.1](/sbd-toe/assets/policies/policy-estrategia-testes#21-matriz-de-obrigatoriedade-por-nível); `DEP-002`; `TST-008` | Network security, physical security, performance, compatibility, end-to-end and scenario-based tests. |
| DORA-26-1 | Article 26(1) | Partial | [Who is subject to TLPT](/sbd-toe/sbd-manual/testes-seguranca/addon/tlpt-readiness#quem-está-sujeito-a-tlpt); [4) What TLPT requires beyond SbD-ToE](/sbd-toe/sbd-manual/testes-seguranca/addon/tlpt-readiness#4-o-que-o-tlpt-exige-além-do-sbd-toe) | Execution of the TLPT under RTS 2025/1190 declared out of scope; the Manual covers readiness. |
| DORA-28-4-d | Article 28(4), point (d) | Partial | [Policy 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação); [Policy 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence); `GOV-007` | Due diligence criteria of RTS 2024/1773 (provider capability and continuity, location, good repute); the Manual's criteria apply only to L2/L3 and to suppliers with technical access. |
| DORA-28-5 | Article 28(5) | Partial | [Policy 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação); `GOV-007` | Prior verification of the “most up-to-date and highest quality” standards for FCIs; certifications mandatory only at L3 for regulated data. |
| DORA-28-6 | Article 28(6), first subparagraph | Partial | [Policy 33 §6.2](/sbd-toe/assets/policies/policy-contratacao-segura#62-reavaliação-periódica); [Policy 33 §4.2](/sbd-toe/assets/policies/policy-contratacao-segura#42-cláusulas-adicionais-por-nível-de-risco) | Programme of audits/inspections of providers with risk-based frequency (right to audit only at L3). |
| DORA-28-8-p4 | Article 28(8), fourth subparagraph | Partial | [Policy 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding) | Transition plans and secure and complete migration of data to another provider or in-house. |
| DORA-RTS1773-3-2 | Article 3(2) | Gap | [🔁 Practical mapping between DRP/BIA and security risk](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia#-mapeamento-prático-entre-drpbia-e-risco-de-segurança) | Methodology for determining which ICT services (and assets) support critical or important functions and when it is reviewed; the Manual does not have the notion of FCI. |
| DORA-RTS1774-2-1-a | Article 2(1), point (a) | Partial | `ARC-006`; `ARC-011` | Network security policy of the entity. |
| DORA-RTS1774-2-1-b | Article 2(1), point (b) | Partial | `ACC-003`; `ACC-006`; `OPS-009` | Network-level intrusion detection. |
| DORA-RTS1774-2-1-d | Article 2(1), point (d) | Partial | `INT-009`; `INT-010`; `INT-012` | Assurance of rapid transmission without undue delays (performance). |
| DORA-RTS1774-3-c-p2 | Article 3, second subparagraph, points (a) to (c) | Partial | `GOV-010`; `OPS-010` | Systematic verification of whether the tolerance was met after treatment. |
| DORA-RTS1774-4-1 | Article 4(1) | Partial | `CLA-008`; `DEP-001`; [Policy 11 §7](/sbd-toe/assets/policies/policy-sbom#7-inventário-em-produção) | ICT asset management policy covering hardware, network and licences. |
| DORA-RTS1774-4-2-a | Article 4(2), point (a) | Partial | [Policy 24 §6](/sbd-toe/assets/policies/policy-golden-base-images#6-sla-de-patching); `CLA-008` | Lifecycle management of all ICT assets. |
| DORA-RTS1774-4-2-b | Article 4(2), point (b) | Partial | `CLA-008`; `ARC-002`; `DEP-001` | Mandatory attributes: physical/logical location, functions supported, RTO/RPO, end-of-support dates. |
| DORA-RTS1774-4-2-c | Article 4(2), point (c) | Partial | [🛠️ Proposed approach](/sbd-toe/sbd-manual/governanca-contratacao/addon/governanca-legada#️-abordagem-proposta) | Specific records for the annual risk assessment of legacy systems. |
| DORA-RTS1774-5-1 | Article 5(1) | Partial | `CLA-008`; [Policy 11 §7](/sbd-toe/assets/policies/policy-sbom#7-inventário-em-produção) | ICT asset management procedure (not only applications and components). |
| DORA-RTS1774-6-2-b | Article 6(2), point (b) and second subparagraph | Gap | — | Rules for data in use or an equivalent separate environment. |
| DORA-RTS1774-8-1 | Article 8(1) | Partial | `OPS-001`; [Policy 31 §3](/sbd-toe/assets/policies/policy-gestao-alertas#3-classificação-de-alertas); [Policy 27 §7](/sbd-toe/assets/policies/policy-rollback#7-teste-periódico-de-rollback) | Operational documentation for the operation, control and restoration of ICT assets. |
| DORA-RTS1774-8-2-a | Article 8(2), point (a) | Partial | `IAC-003`; `CNT-003`; `CFG-001`; [🛠️ Proposed approach](/sbd-toe/sbd-manual/governanca-contratacao/addon/governanca-legada#️-abordagem-proposta) | Secure disposal and management of the information assets processed. |
| DORA-RTS1774-8-2-b-vii | Article 8(2), point (b)(vii) and third subparagraph | Partial | [Policy 36 §4.2](/sbd-toe/assets/policies/policy-pentesting#42-regras-de-engajamento) | Rules for development/testing in production: identification, justification, time limitation and approval. |
| DORA-RTS1774-8-2-c | Article 8(2), point (c) | Partial | [Policy 31 §5](/sbd-toe/assets/policies/policy-gestao-alertas#5-escalonamento-automático); [Policy 27 §7](/sbd-toe/assets/policies/policy-rollback#7-teste-periódico-de-rollback); [Policy 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação) | External support contacts and system restart/resumption procedures. |
| DORA-RTS1774-9-1 | Article 9(1) | Partial | `OPS-015` | Capacity and performance management (capacity requirements, optimisation, prevention of shortages). |
| DORA-RTS1774-10-2-b | Article 10(2), point (b) and second subparagraph | Partial | [Policy 10 §9](/sbd-toe/assets/policies/policy-dependencias#9-auditoria-periódica); [Ch. 05 US-09](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-09---auditoria-periódica-de-bibliotecas-copiadas-manualmente); [Policy 23 §4](/sbd-toe/assets/policies/policy-containers-seguros#4-scanning-de-imagens); [Policy 11 §7](/sbd-toe/assets/policies/policy-sbom#7-inventário-em-produção) | Automated vulnerability scanning at least weekly on all assets supporting FCI (incl. infrastructure, not only dependencies/images). |
| DORA-RTS1774-10-2-c | Article 10(2), point (c) and third subparagraph | Partial | [Policy 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação); [Policy 33 §6.1](/sbd-toe/assets/policies/policy-contratacao-segura#61-indicadores-de-conformidade-a-monitorizar); [💽 Licensing contracts (external software)](/sbd-toe/sbd-manual/governanca-contratacao/addon/clausulas-contratuais#-contratos-de-licenciamento-software-externo) | Request to the provider for investigation, cause analysis and mitigation; statistics and trends. |
| DORA-RTS1774-10-3 | Article 10(3) | Partial | `DEP-007`; [Policy 13 §2](/sbd-toe/assets/policies/policy-atualizacao-automatica#2-âmbito-e-obrigatoriedade); [Policy 24 §6](/sbd-toe/assets/policies/policy-golden-base-images#6-sla-de-patching) | OS/firmware/hardware patches outside the base images. |
| DORA-RTS1774-11-2-b | Article 11(2), point (b) and second subparagraph | Partial | `CNT-003`; `CNT-004`; `IAC-003`; `CFG-007`; [Policy 24 §6](/sbd-toe/assets/policies/policy-golden-base-images#6-sla-de-patching) | Hardening baselines for servers/OS and regular verification outside containers/IaC. |
| DORA-RTS1774-11-2-c | Article 11(2), point (c) | Partial | `IDE-001`; `CNT-001`; `DEP-005` | Control of authorised software on all systems and endpoints. |
| DORA-RTS1774-11-2-d | Article 11(2), point (d) | Partial | `FIL-007` | Anti-malware protection of servers and endpoints. |
| DORA-RTS1774-11-2-g | Article 11(2), point (g) | Partial | `PRI-002` | Secure erasure of non-personal data and of data at external sites. |
| DORA-RTS1774-11-2-i | Article 11(2), point (i) | Partial | [Policy 30 §3.2](/sbd-toe/assets/policies/policy-monitorizacao-seguranca#32-exfiltração-e-acesso-a-dados); `ENC-005` | Data loss and leakage prevention (DLP) measures on endpoints. |
| DORA-RTS1774-11-2-k | Article 11(2), point (k) and third subparagraph | Partial | `GOV-006`; `IAC-003` | Allocation of security responsibilities and vendor parameters for assets operated by third parties (cloud). |
| DORA-RTS1774-12-2-c | Article 12(2), point (c) | Partial | [Policy 29 §4](/sbd-toe/assets/policies/policy-logging-estruturado#4-eventos-de-segurança-obrigatórios); `DPL-004`; `CIC-005` | Physical access events, capacity management and network traffic/performance. |
| DORA-RTS1774-12-2-d | Article 12(2), point (d) | Partial | `LOG-003`; [Policy 29 §8](/sbd-toe/assets/policies/policy-logging-estruturado#8-integridade-e-imutabilidade) | Protection in transit and in use. |
| DORA-RTS1774-12-2-e | Article 12(2), point (e) | Partial | `LOG-008`; `OPS-004` | Detection of logging failures at L1. |
| DORA-RTS1774-12-2-f | Article 12(2), point (f) | Partial | [🛠️ Functional requirements of the integration](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/integracao-siem#️-requisitos-funcionais-da-integração) | Documented synchronisation of all ICT systems with a reliable time reference (the Manual only normalises timestamps in SIEM integration). |
| DORA-RTS1774-13 | Article 13, first subparagraph | Partial | `ARC-006`; [Policy 09 §6.1](/sbd-toe/assets/policies/policy-arquitetura-segura#61-inventário-de-trust-boundaries) | Network security management policy with elements (a) to (m). |
| DORA-RTS1774-13-b | Article 13, point (b) | Partial | `ARC-008`; `THR-002` | Documentation of all network connections (not only flows between the application's trust zones). |
| DORA-RTS1774-13-c | Article 13, point (c) | Gap | — | Separate and dedicated administration network/plane. |
| DORA-RTS1774-13-f | Article 13, point (f) | Partial | `ARC-001`; `ARC-006`; [Policy 09 §6.1](/sbd-toe/assets/policies/policy-arquitetura-segura#61-inventário-de-trust-boundaries) | Design of the entity's networks. |
| DORA-RTS1774-13-i | Article 13, point (i) | Partial | `ARC-010`; `ARC-003` | Annual review of network architecture and security design (the Manual reviews application diagrams annually). |
| DORA-RTS1774-13-l | Article 13, point (l) | Partial | `SES-001`; `AUT-005` | Termination of remote administration/system sessions after inactivity (the Manual covers application sessions). |
| DORA-RTS1774-14-1-b | Article 14(1), point (b) | Partial | [Policy 30 §3.2](/sbd-toe/assets/policies/policy-monitorizacao-seguranca#32-exfiltração-e-acesso-a-dados); `INT-002`; `INT-006` | Data leakage prevention (DLP) in transfers with external parties. |
| DORA-RTS1774-16-3 | Article 16(3) | Partial | [Policy 19 §2.1](/sbd-toe/assets/policies/policy-estrategia-testes#21-matriz-de-obrigatoriedade-por-nível); `DEV-003`; `TST-005`; [4️⃣ Basic Coding Guidelines and Automated Validation (Ch. 06)](/sbd-toe/sbd-manual/fundamentos/baseline#4️⃣-coding-guidelines-básicas-e-validação-automática-cap-06) | DAST mandatory at all levels (incl. internet-facing systems). |
| DORA-RTS1774-16-6 | Article 16(6) | Partial | [4.1 Mandatory prescriptions](/sbd-toe/sbd-manual/testes-seguranca/addon/evidencia-reprodutibilidade#41-prescrições-obrigatórias); [Ch. 10 US-19](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-19---proteção-dos-ativos-do-processo-de-teste) | Time limitation and communication to the ICT risk management function. |
| DORA-RTS1774-16-9 | Article 16(9) | Partial | [🎯 Scope and framing](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#-âmbito-e-enquadramento) | Application of the SDLC to end-user computing/shadow IT outside the ICT function. |
| DORA-RTS1774-17-1 | Article 17(1), first subparagraph | Partial | `DPL-001`; `DPL-004`; [Policy 26 §7](/sbd-toe/assets/policies/policy-aprovacao-release#7-releases-de-emergência); [Policy 22 §5](/sbd-toe/assets/policies/policy-aprovacao-plan-iac#5-separação-de-funções-sod) | Hardware/firmware changes. |
| DORA-RTS1774-17-1-d | Article 17(1), point (d) | Partial | `DPL-004`; `IAC-007` | Documentation of the objective and expected results of each change. |
| DORA-RTS1774-19-b-iii | Article 19, point (b)(iii) | Partial | [Policy 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding) | Return of assets by internal staff (the Manual covers contractors/suppliers). |
| DORA-RTS1774-20-2-a | Article 20(2), point (a) and second subparagraph | Partial | `ACC-004`; [Ch. 07 US-20](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-20) | Unique identity per staff member with the record retained after the end of the relationship. |
| DORA-RTS1774-22 | Article 22, first subparagraph | Partial | [Policy 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade); [Policy 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp); [Policy 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta) | Mandatory at L1 through floor CTX-DORA-P01, which rests on DORA Article 17 (see DORA-17-1); the RTS article is not in the floor base. |
| DORA-RTS1774-22-b | Article 22, point (b) | Partial | [Policy 31 §7](/sbd-toe/assets/policies/policy-gestao-alertas#7-alertas-p1-em-horas-não-laborais-on-call) | List of external contacts (authorities, CSIRT, providers). |
| DORA-RTS1774-23-2-a | Article 23(2), point (a) | Partial | `OPS-004`; [Ch. 12 US-16](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-16---cobertura-attck-e-priorização-epsskev); [Policy 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) | User reports as a mandatory source. |
| DORA-RTS1774-23-2-b | Article 23(2), point (b) and second subparagraph | Partial | `LOG-008`; `OPS-004`; `OPS-005` | Automatic alerts on integrity/completeness of collection for FCI assets classified L1. |
| DORA-RTS1774-23-3 | Article 23(3) | Partial | `LOG-003`; [Policy 29 §8](/sbd-toe/assets/policies/policy-logging-estruturado#8-integridade-e-imutabilidade) | Protection mandatory at L1 (see 12-2-d). |
| DORA-RTS1774-23-4 | Article 23(4) | Partial | [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); `LOG-002` | Separate recording of the date/time of occurrence and of detection. |
| DORA-RTS1774-25-1 | Article 25(1) | Partial | [Policy 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp); [🔁 Practical mapping between DRP/BIA and security risk](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia#-mapeamento-prático-entre-drpbia-e-risco-de-segurança) | Testing of continuity plans based on the BIA. |
| DORA-RTS1774-25-2 | Article 25(2) | Partial | [Policy 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp); [Policy 27 §7](/sbd-toe/assets/policies/policy-rollback#7-teste-periódico-de-rollback) | Third-party failure scenarios and failover scenarios for redundancy/backups. |
| DORA-RTS1774-25-5 | Article 25(5) | Partial | [Policy 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp) | Communication of deficiencies to the management body. |
| DORA-RTS1774-26-1 | Article 26(1) | Partial | [Policy 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta); [🔁 Practical mapping between DRP/BIA and security risk](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia#-mapeamento-prático-entre-drpbia-e-risco-de-segurança) | Recovery plans based on the BIA with activation/deactivation criteria and recovery objectives. |
| DORA-RTS1774-26-2 | Article 26(2) | Partial | [Policy 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta) | Non-cyber scenarios (premises, staff, climate, pandemic, energy, political instability). |
| DORA-RTS1774-26-4 | Article 26(4) | Partial | [Policy 33 §10.5](/sbd-toe/assets/policies/policy-contratacao-segura#105-sla-de-disponibilidade-e-fallback) | Continuity measures in the event of failures of FCI providers in general (the Manual only provides fallback for AI vendors). |
| DORA-RTS1774-29-2 | Article 29(2) | Partial | `CLA-003`; `GOV-006` | Mitigating measures applied by ICT providers. |
| DORA-RTS1774-30-1 | Article 30(1) | Partial | `CLA-001`; `CLA-008` | Identification of critical or important functions and interdependencies. |
| DORA-RTS1774-33 | Article 33, first subparagraph | Partial | `ACC-001`; `ACC-010` | Physical access control. |
| DORA-RTS1774-34-a | Article 34, point (a) | Partial | [Policy 24 §6](/sbd-toe/assets/policies/policy-golden-base-images#6-sla-de-patching); `CLA-008` | Lifecycle of all ICT assets. |
| DORA-RTS1774-34-b | Article 34, point (b) | Partial | [Policy 24 §6](/sbd-toe/assets/policies/policy-golden-base-images#6-sla-de-patching) | Verification of third-party support for all assets (EOL outside base images/dependencies). |
| DORA-RTS1774-34-c | Article 34, point (c) | Partial | `OPS-015` | Capacity planning. |
| DORA-RTS1774-34-e | Article 34, point (e) | Partial | [🛠️ Proposed approach](/sbd-toe/sbd-manual/governanca-contratacao/addon/governanca-legada#️-abordagem-proposta); [Policy 24 §6](/sbd-toe/assets/policies/policy-golden-base-images#6-sla-de-patching) | Management of risks from obsolete/unsupported hardware. |
| DORA-RTS1774-34-f | Article 34, point (f) and second subparagraph | Partial | [Policy 29 §4](/sbd-toe/assets/policies/policy-logging-estruturado#4-eventos-de-segurança-obrigatórios); `DPL-004` | Physical access and network traffic events. |
| DORA-RTS1774-34-i | Article 34, point (i) | Partial | [Policy 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção); `ENC-006`; `FIL-007` | Information leakage and hardware vulnerabilities. |
| DORA-RTS1774-35 | Article 35, first subparagraph | Partial | `ACC-003`; `ACC-006`; `ENC-001` | Safeguards against intrusion at network/endpoint level. |
| DORA-RTS1774-35-a | Article 35, point (a) | Partial | `ENC-001`; `ENC-002` | Data in use. |
| DORA-RTS1774-35-b | Article 35, point (b) | Partial | `IDE-001`; `CNT-001` | Storage media and endpoints. |
| DORA-RTS1774-35-e | Article 35, point (e) | Partial | `PRI-002` | Secure erasure of non-personal data. |
| DORA-RTS1774-38-2 | Article 38(2) | Partial | `DPL-001`; `DPL-004`; [Policy 26 §7](/sbd-toe/assets/policies/policy-aprovacao-release#7-releases-de-emergência) | Hardware/firmware changes. |
| DORA-RTS1774-39-1 | Article 39(1) | Partial | [Policy 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta) | Continuity plans (the Manual has incident playbooks, incl. ransomware). |
| DORA-RTS1774-40-1 | Article 40(1) and (2) | Partial | [Policy 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp); [Policy 27 §7](/sbd-toe/assets/policies/policy-rollback#7-teste-periódico-de-rollback); `OPS-016` | Tests of the entity's continuity plans with scenarios (outside the scope of the Manual); testing of backup and restoration is prescribed (OPS-016). |
| DORA-RTS1774-40-3 | Article 40(3) | Partial | [Policy 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp) | Reporting of deficiencies to the management body. |
| DORA-RTS1772-3-1 | Article 3(1) | Partial | [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); `LOG-002` | Measurement of duration from occurrence (using logs when prior to detection). |
| DORA-RTS1772-3-2 | Article 3(2) | Partial | `OPS-015`; `OPS-006` | Measurement of downtime until restoration of the previous service level. |
| DORA-RTS1772-5 | Article 5 | Partial | [Policy 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) | Structured assessment of the impact on availability, authenticity, integrity and confidentiality. |
| DORA-RTS1772-6 | Article 6 | Partial | [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); `CLA-008` | Criterion of services affected that support FCI or authorised financial services. |

### Out of scope (234) {#fora-de-ambito}

Obligations that the Manual declares out of scope, with the reason.

| Obligation | Reference | Reason |
|---|---|---|
| DORA-5-2-f | Article 5(2), point (f) | Duty of the management body / internal governance framework; the Manual does not set corporate bodies nor corporate approval authorities. Approval of internal audit plans. |
| DORA-5-2-g | Article 5(2), point (g) | Duty of the management body / internal governance framework; the Manual does not set corporate bodies nor corporate approval authorities. Budget. |
| DORA-5-3 | Article 5(3) | Duty of the management body / internal governance framework; the Manual does not set corporate bodies nor corporate approval authorities. Role for monitoring the arrangements with ICT third parties. |
| DORA-5-4 | Article 5(4) | Duty of the management body / internal governance framework; the Manual does not set corporate bodies nor corporate approval authorities. Policy 37 covers only staff with technical functions. |
| DORA-6-3-p2 | Article 6(3), second sentence | Reporting to/relationship with the competent authority — legal-regulatory level, not a software engineering prescription. |
| DORA-6-4 | Article 6(4) | Duty of the management body / internal governance framework; the Manual does not set corporate bodies nor corporate approval authorities. Independent control function and three lines of defence model. |
| DORA-6-10 | Article 6(10) | Principle of retained legal responsibility in outsourced verification. |
| DORA-10-4 | Article 10(4) | Specific sectoral obligation (CCP/CSD/trading venues/DRSP) — market operational parameter, outside a cross-cutting software engineering manual. |
| DORA-11-1 | Article 11(1) | Organisation-level business continuity/crisis management (BCM) — the Manual deals with cyber incident response and rollback, not general BCM. |
| DORA-11-6-b | Article 11(6), point (b) | Organisation-level business continuity/crisis management (BCM) — the Manual deals with cyber incident response and rollback, not general BCM. Crisis communication. |
| DORA-11-7 | Article 11(7) | Organisation-level business continuity/crisis management (BCM) — the Manual deals with cyber incident response and rollback, not general BCM. Crisis management function. |
| DORA-11-9 | Article 11(9) | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Obligation exclusive to CSDs. |
| DORA-11-10 | Article 11(10) | Reporting to/relationship with the competent authority — legal-regulatory level, not a software engineering prescription. |
| DORA-12-3-p2 | Article 12(3), second and third subparagraphs | Specific sectoral obligation (CCP/CSD/trading venues/DRSP) — market operational parameter, outside a cross-cutting software engineering manual. |
| DORA-12-5 | Article 12(5) | Specific sectoral obligation (CCP/CSD/trading venues/DRSP) — market operational parameter, outside a cross-cutting software engineering manual. |
| DORA-13-2-p2 | Article 13(2), second subparagraph | Reporting to/relationship with the competent authority — legal-regulatory level, not a software engineering prescription. |
| DORA-14-1 | Article 14(1) | Organisation-level business continuity/crisis management (BCM) — the Manual deals with cyber incident response and rollback, not general BCM. Crisis communication and disclosure. |
| DORA-14-2 | Article 14(2) | Organisation-level business continuity/crisis management (BCM) — the Manual deals with cyber incident response and rollback, not general BCM. Internal/external communication policies. |
| DORA-19-2 | Article 19(2) | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Voluntary notification of cyber threats. |
| DORA-19-3-p2 | Article 19(3), second subparagraph | Reporting to/relationship with the competent authority — legal-regulatory level, not a software engineering prescription. |
| DORA-19-5 | Article 19(5) | Legal responsibility retained when notification is outsourced. |
| DORA-23 | Article 23 | Application to operational or security payment-related incidents — sectoral legal scope. |
| DORA-26-3 | Article 26(3) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-26-4 | Article 26(4) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-26-6 | Article 26(6) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-26-7 | Article 26(7) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-26-8 | Article 26(8), first and second subparagraphs | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-27-1 | Article 27(1), points (a) to (e) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-27-2 | Article 27(2) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-27-3 | Article 27(3) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-28-1-a | Article 28(1), point (a) | Principle of legal responsibility retained by the financial entity. |
| DORA-28-2-orgao | Article 28(2), last sentence | Duty of the management body / internal governance structure; the Manual does not set corporate bodies or delegated authority levels. |
| DORA-28-3-p2 | Article 28(3), second subparagraph | Regulatory register of information (Article 28(3); ITS 2024/2956) — templates and reporting to the authority; intentional gap declared in the DORA cross-check. |
| DORA-28-3-p3 | Article 28(3), third subparagraph | Regulatory register of information (Article 28(3); ITS 2024/2956) — templates and reporting to the authority; intentional gap declared in the DORA cross-check. |
| DORA-28-3-p4 | Article 28(3), fourth subparagraph | Regulatory register of information (Article 28(3); ITS 2024/2956) — templates and reporting to the authority; intentional gap declared in the DORA cross-check. |
| DORA-28-3-p5 | Article 28(3), fifth subparagraph | Reporting to/relationship with the competent authority — legal-regulatory level, not a software engineering prescription. |
| DORA-28-4-b | Article 28(4), point (b) | Verification of supervisory conditions for subcontracting — legal-regulatory plane. |
| DORA-28-4-e | Article 28(4), point (e) | Conflicts of interest in the arrangement — legal/compliance plane. |
| DORA-28-6-p2 | Article 28(6), second subparagraph | Competence of auditors in complex contracts — audit/compliance plane. |
| DORA-28-8-p2 | Article 28(8), second subparagraph | Organisation-level business continuity/crisis management (BCM) — the Manual deals with cyber incident response and rollback, not general BCM. Provider exit planning. |
| DORA-28-8-p3 | Article 28(8), third subparagraph | Organisation-level business continuity/crisis management (BCM) — the Manual deals with cyber incident response and rollback, not general BCM. Documented and tested exit plans. |
| DORA-28-8-p5 | Article 28(8), fifth subparagraph | Organisation-level business continuity/crisis management (BCM) — the Manual deals with cyber incident response and rollback, not general BCM. |
| DORA-29-1 | Article 29(1), first subparagraph, points (a) and (b) | ICT third-party concentration risk — regulatory analysis; intentional gap (no concentration formulas). |
| DORA-29-1-p2 | Article 29(1), second subparagraph | Idem 29-1. |
| DORA-29-2 | Article 29(2), first subparagraph | Idem 29-1 (subcontracting in a third country). |
| DORA-29-2-p2 | Article 29(2), second subparagraph | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. |
| DORA-29-2-p3 | Article 29(2), third subparagraph | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. |
| DORA-29-2-p4 | Article 29(2), fourth subparagraph | Idem 29-1. |
| DORA-30-2-g | Article 30(2), point (g) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Cooperation with the authorities. |
| DORA-30-3-a | Article 30(3), point (a) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Complete SLAs with quantitative/qualitative targets. |
| DORA-30-3-d | Article 30(3), point (d) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Provider participation in TLPT. |
| DORA-30-3-f | Article 30(3), point (f) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Exit strategies with a transition period. |
| DORA-31-4 | Article 31(4) | Oversight framework for critical third-party providers (Articles 31–44) — provider/authority relationship, outside an engineering manual. |
| DORA-31-5-p2 | Article 31(5), second subparagraph | Oversight framework for critical third-party providers (Articles 31–44) — provider/authority relationship, outside an engineering manual. |
| DORA-31-12 | Article 31(12) | Oversight framework for critical third-party providers (Articles 31–44) — provider/authority relationship, outside an engineering manual. |
| DORA-31-13 | Article 31(13) | Oversight framework for critical third-party providers (Articles 31–44) — provider/authority relationship, outside an engineering manual. |
| DORA-35-1-d-iv | Article 35(1), point (d)(iv), last subparagraph | Oversight framework for critical third-party providers (Articles 31–44) — provider/authority relationship, outside an engineering manual. |
| DORA-35-5 | Article 35(5) | Oversight framework for critical third-party providers (Articles 31–44) — provider/authority relationship, outside an engineering manual. |
| DORA-37-4 | Article 37(4) | Oversight framework for critical third-party providers (Articles 31–44) — provider/authority relationship, outside an engineering manual. |
| DORA-38-4 | Article 38(4) | Oversight framework for critical third-party providers (Articles 31–44) — provider/authority relationship, outside an engineering manual. |
| DORA-39-6 | Article 39(6) | Oversight framework for critical third-party providers (Articles 31–44) — provider/authority relationship, outside an engineering manual. |
| DORA-42-1 | Article 42(1) | Oversight framework for critical third-party providers (Articles 31–44) — provider/authority relationship, outside an engineering manual. |
| DORA-42-3-p2 | Article 42(3), second subparagraph | Oversight framework for critical third-party providers (Articles 31–44) — provider/authority relationship, outside an engineering manual. |
| DORA-42-9-p2 | Article 42(9), second subparagraph | Oversight framework for critical third-party providers (Articles 31–44) — provider/authority relationship, outside an engineering manual. |
| DORA-45-1 | Article 45(1), points (a) to (c) | Institutional cyber threat information-sharing arrangements (conditional option); the cross-check declares an intentional gap. |
| DORA-45-2 | Article 45(2) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. |
| DORA-45-3 | Article 45(3) | Reporting to/relationship with the competent authority — legal-regulatory level, not a software engineering prescription. |
| DORA-59 | Article 59 (amends Regulation (EC) No 1060/2009, Annex I, Section A, point 4) | Amendments to sectoral acts (credit rating agencies, CCPs, APAs/CTPs/ARMs, benchmarks) — legal cross-reference. |
| DORA-60 | Article 60 (amends Regulation (EU) No 648/2012, Articles 26, 34, 56, 79...) | Amendments to sectoral acts (credit rating agencies, CCPs, APAs/CTPs/ARMs, benchmarks) — legal cross-reference. |
| DORA-61 | Article 61 (amends Regulation (EU) No 909/2014, Article 45) | Specific sectoral obligation (CCP/CSD/trading venues/DRSP) — market operational parameter, outside a cross-cutting software engineering manual. Amendment to the CSD regime (transaction recovery). |
| DORA-62 | Article 62 (amends Regulation (EU) No 600/2014, Articles 27g, 27h and 27i) | Amendments to sectoral acts (credit rating agencies, CCPs, APAs/CTPs/ARMs, benchmarks) — legal cross-reference. |
| DORA-63 | Article 63 (adita Article 6(6), ao Regulation (EU) 2016/1011) | Amendments to sectoral acts (credit rating agencies, CCPs, APAs/CTPs/ARMs, benchmarks) — legal cross-reference. |
| DORA-RTS1773-2 | Article 2 | Consistent application across the group — corporate organisation. |
| DORA-RTS1773-3-1 | Article 3(1) | Duty of the management body / internal governance structure; the Manual does not set corporate bodies or delegated authority levels. |
| DORA-RTS1773-3-4 | Article 3(4) | Assessment of the sufficiency of the provider's resources — contract management. |
| DORA-RTS1773-3-5 | Article 3(5) | Duty of the management body / internal governance structure; the Manual does not set corporate bodies or delegated authority levels. |
| DORA-RTS1773-3-7 | Article 3(7) | Duty of the management body / internal governance structure; the Manual does not set corporate bodies or delegated authority levels. Independent review/audit plan. |
| DORA-RTS1773-3-8 | Article 3(8), points (a) to (d) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. |
| DORA-RTS1773-5-1 | Article 5(1) | Definition of operational needs before contracting — procurement. |
| DORA-RTS1773-6-2 | Article 6(2) | Provider's assurance level and continuity — procurement assessment. |
| DORA-RTS1773-7-1 | Article 7(1) | Conflicts of interest — compliance. |
| DORA-RTS1773-7-2 | Article 7(2) | Intra-group services — corporate organisation. |
| DORA-RTS1773-8-4 | Article 8(4) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. |
| DORA-RTS1773-10 | Article 10 | Organisation-level business continuity/crisis management (BCM) — the Manual deals with cyber incident response and rollback, not general BCM. Exit plan per arrangement. |
| DORA-ITS2956-2 | Article 2 | Regulatory register of information (Article 28(3); ITS 2024/2956) — templates and reporting to the authority; intentional gap declared in the DORA cross-check. |
| DORA-ITS2956-3-1 | Article 3(1) | Regulatory register of information (Article 28(3); ITS 2024/2956) — templates and reporting to the authority; intentional gap declared in the DORA cross-check. |
| DORA-ITS2956-3-2 | Article 3(2), points (a) and (b) | Regulatory register of information (Article 28(3); ITS 2024/2956) — templates and reporting to the authority; intentional gap declared in the DORA cross-check. |
| DORA-ITS2956-3-3 | Article 3(3) | Regulatory register of information (Article 28(3); ITS 2024/2956) — templates and reporting to the authority; intentional gap declared in the DORA cross-check. |
| DORA-ITS2956-3-4 | Article 3(4), points (a) to (f) | Regulatory register of information (Article 28(3); ITS 2024/2956) — templates and reporting to the authority; intentional gap declared in the DORA cross-check. |
| DORA-ITS2956-3-5 | Article 3(5) | Regulatory register of information (Article 28(3); ITS 2024/2956) — templates and reporting to the authority; intentional gap declared in the DORA cross-check. |
| DORA-ITS2956-3-6 | Article 3(6) | Regulatory register of information (Article 28(3); ITS 2024/2956) — templates and reporting to the authority; intentional gap declared in the DORA cross-check. |
| DORA-ITS2956-4 | Article 4(2) and (3) | Regulatory register of information (Article 28(3); ITS 2024/2956) — templates and reporting to the authority; intentional gap declared in the DORA cross-check. |
| DORA-ITS2956-5-1 | Article 5(1), points (a) to (o); Annex I | Regulatory register of information (Article 28(3); ITS 2024/2956) — templates and reporting to the authority; intentional gap declared in the DORA cross-check. |
| DORA-ITS2956-6 | Article 6(1) and (2) | Regulatory register of information (Article 28(3); ITS 2024/2956) — templates and reporting to the authority; intentional gap declared in the DORA cross-check. |
| DORA-ITS2956-AnexoI | Annex I, Part 1 | Regulatory register of information (Article 28(3); ITS 2024/2956) — templates and reporting to the authority; intentional gap declared in the DORA cross-check. |
| DORA-RTS532-1 | Article 1, points (a) to (l) | Proportionality in the management of subcontracting — contractual plane. |
| DORA-RTS532-2 | Article 2 | Consistency across the group — corporate organisation. |
| DORA-RTS532-3-1-f | Article 3(1), point (f) | Risk assessment of subcontracting chains (capability, failure, location, concentration, audit) — contractual/regulatory analysis. |
| DORA-RTS532-3-1-g | Article 3(1), point (g) | Risk assessment of subcontracting chains (capability, failure, location, concentration, audit) — contractual/regulatory analysis. |
| DORA-RTS532-3-1-h | Article 3(1), point (h) | Risk assessment of subcontracting chains (capability, failure, location, concentration, audit) — contractual/regulatory analysis. |
| DORA-RTS532-3-1-i | Article 3(1), point (i) | Risk assessment of subcontracting chains (capability, failure, location, concentration, audit) — contractual/regulatory analysis. |
| DORA-RTS532-3-1-j | Article 3(1), point (j) | Risk assessment of subcontracting chains (capability, failure, location, concentration, audit) — contractual/regulatory analysis. |
| DORA-RTS532-4-1-a | Article 4(1), point (a) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Clauses on subcontractors. |
| DORA-RTS532-4-1-b | Article 4(1), point (b) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Clauses on subcontractors. |
| DORA-RTS532-4-1-c | Article 4(1), point (c) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Clauses on subcontractors. |
| DORA-RTS532-4-1-d | Article 4(1), point (d) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Clauses on subcontractors. |
| DORA-RTS532-4-1-e | Article 4(1), point (e) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Clauses on subcontractors. |
| DORA-RTS532-4-1-f | Article 4(1), point (f) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Clauses on subcontractors. |
| DORA-RTS532-4-1-g | Article 4(1), point (g) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Clauses on subcontractors. |
| DORA-RTS532-4-1-h | Article 4(1), point (h) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Clauses on subcontractors. |
| DORA-RTS532-4-1-j | Article 4(1), point (j) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Clauses on subcontractors. |
| DORA-RTS532-4-1-k | Article 4(1), point (k) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Clauses on subcontractors. |
| DORA-RTS532-4-1-l | Article 4(1), point (l) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Clauses on subcontractors. |
| DORA-RTS532-4-2 | Article 4(2) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Clauses on subcontractors. |
| DORA-RTS532-5-1 | Article 5(1) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Clauses on subcontractors. |
| DORA-RTS532-5-2 | Article 5(2) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Clauses on subcontractors. |
| DORA-RTS532-5-3 | Article 5(3) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Clauses on subcontractors. |
| DORA-RTS532-5-4 | Article 5(4) | DORA-specific contractual/legal content with no prescriptive counterpart in the Manual. Clauses on subcontractors. |
| DORA-RTS1774-2-2-e | Article 2(2), point (e) | Disciplinary consequences of non-compliance — HR/compliance regime. |
| DORA-RTS1774-2-2-g | Article 2(2), point (g) | Duty of the management body / internal governance structure; the Manual does not set corporate bodies or delegated authority levels. Segregation of duties between lines of defence. |
| DORA-RTS1774-8-2-b-ii | Article 8(2), point (b)(ii) | Processing scheduling with interdependencies — IT operations. |
| DORA-RTS1774-9-2 | Article 9(2) | Systems with long procurement lead times or that are resource-intensive — IT procurement planning. |
| DORA-RTS1774-11-2-e | Article 11(2), point (e) | Security of workstations/devices and physical media (corporate IT) — outside the secure development lifecycle. |
| DORA-RTS1774-11-2-f | Article 11(2), point (f) | Security of workstations/devices and physical media (corporate IT) — outside the secure development lifecycle. |
| DORA-RTS1774-11-2-h | Article 11(2), point (h) | Security of workstations/devices and physical media (corporate IT) — outside the secure development lifecycle. |
| DORA-RTS1774-11-2-j | Article 11(2), point (j) | Security of workstations/devices and physical media (corporate IT) — outside the secure development lifecycle. |
| DORA-RTS1774-13-d | Article 13, point (d) | Network access control (NAC) for devices — corporate network infrastructure. |
| DORA-RTS1774-13-k | Article 13, point (k) | Hardening of network equipment according to the vendor — network infrastructure. |
| DORA-RTS1774-15-5 | Article 15(5) | Duty of the management body / internal governance structure; the Manual does not set corporate bodies or delegated authority levels. |
| DORA-RTS1774-16-2-p2 | Article 16(2), segundo and third subparagraphs | Specific sectoral obligation (CCP/CSD/trading venues/DRSP) — market operational parameter, outside a cross-cutting software engineering manual. |
| DORA-RTS1774-17-2 | Article 17(2) | Specific sectoral obligation (CCP/CSD/trading venues/DRSP) — market operational parameter, outside a cross-cutting software engineering manual. |
| DORA-RTS1774-18-1 | Article 18(1) | Physical and environmental security of premises — outside the scope of a software engineering manual. |
| DORA-RTS1774-18-2 | Article 18(2), points (a) to (e), and following subparagraphs | Physical and environmental security of premises — outside the scope of a software engineering manual. |
| DORA-RTS1774-21-g | Article 21, point (g), and final subparagraphs | Physical and environmental security of premises — outside the scope of a software engineering manual. |
| DORA-RTS1774-24-1-a | Article 24(1), point (a) | Organisation-level business continuity/crisis management (BCM) — the Manual deals with cyber incident response and rollback, not general BCM. |
| DORA-RTS1774-24-2 | Article 24(2) | Specific sectoral obligation (CCP/CSD/trading venues/DRSP) — market operational parameter, outside a cross-cutting software engineering manual. |
| DORA-RTS1774-24-3 | Article 24(3) | Specific sectoral obligation (CCP/CSD/trading venues/DRSP) — market operational parameter, outside a cross-cutting software engineering manual. |
| DORA-RTS1774-24-4 | Article 24(4) | Specific sectoral obligation (CCP/CSD/trading venues/DRSP) — market operational parameter, outside a cross-cutting software engineering manual. |
| DORA-RTS1774-25-3 | Article 25(3) and (4) | Specific sectoral obligation (CCP/CSD/trading venues/DRSP) — market operational parameter, outside a cross-cutting software engineering manual. |
| DORA-RTS1774-26-3 | Article 26(3) | Organisation-level business continuity/crisis management (BCM) — the Manual deals with cyber incident response and rollback, not general BCM. Alternative recovery options. |
| DORA-RTS1774-27-1 | Article 27(1) | Reporting to/relationship with the competent authority — legal-regulatory level, not a software engineering prescription. |
| DORA-RTS1774-27-2 | Article 27(2) | Reporting to/relationship with the competent authority — legal-regulatory level, not a software engineering prescription. |
| DORA-RTS1774-28-2-e | Article 28(2), point (e) | Duty of the management body / internal governance framework; the Manual does not set corporate bodies nor corporate approval authorities. Budget. |
| DORA-RTS1774-28-3 | Article 28(3) | Legal responsibility retained when outsourcing verification. |
| DORA-RTS1774-28-4 | Article 28(4) | Duty of the management body / internal governance structure; the Manual does not set corporate bodies or corporate authority levels. Segregation between control and internal audit. |
| DORA-RTS1774-32 | Article 32(1) to (3) | Physical and environmental security of premises — outside the scope of a software engineering manual. |
| DORA-RTS1774-35-f | Article 35, point (f) | Security of workstations/devices and physical media (corporate IT) — outside the secure development lifecycle. |
| DORA-RTS1774-35-g | Article 35, point (g) | Security of workstations/devices and physical media (corporate IT) — outside the secure development lifecycle. |
| DORA-RTS1774-39-2-a | Article 39(2), points (a) to (c) | Organisation-level business continuity/crisis management (BCM) — the Manual deals with cyber incident response and rollback, not general BCM. |
| DORA-RTS1774-39-2-h | Article 39(2), points (h) to (j) | Organisation-level business continuity/crisis management (BCM) — the Manual deals with cyber incident response and rollback, not general BCM. |
| DORA-RTS1774-41-1 | Article 41(1) | Reporting to/relationship with the competent authority — legal-regulatory level, not a software engineering prescription. |
| DORA-RTS1774-41-2 | Article 41(2) | Reporting to/relationship with the competent authority — legal-regulatory level, not a software engineering prescription. |
| DORA-RTS1772-1-1 | Article 1(1) | Regulatory incident classification/impact criteria (RTS 2024/1772) — GRC plane; the DORA cross-check declares an intentional gap (the Manual uses an internal P1–P4 scale). |
| DORA-RTS1772-1-2 | Article 1(2) | Regulatory incident classification/impact criteria (RTS 2024/1772) — GRC plane; the DORA cross-check declares an intentional gap (the Manual uses an internal P1–P4 scale). |
| DORA-RTS1772-1-3 | Article 1(3) | Regulatory incident classification/impact criteria (RTS 2024/1772) — GRC plane; the DORA cross-check declares an intentional gap (the Manual uses an internal P1–P4 scale). |
| DORA-RTS1772-1-5 | Article 1(5); Article 9(1), second subparagraph | Regulatory incident classification/impact criteria (RTS 2024/1772) — GRC plane; the DORA cross-check declares an intentional gap (the Manual uses an internal P1–P4 scale). |
| DORA-RTS1772-2-1 | Article 2(1) | Regulatory incident classification/impact criteria (RTS 2024/1772) — GRC plane; the DORA cross-check declares an intentional gap (the Manual uses an internal P1–P4 scale). |
| DORA-RTS1772-2-2 | Article 2(2) | Regulatory incident classification/impact criteria (RTS 2024/1772) — GRC plane; the DORA cross-check declares an intentional gap (the Manual uses an internal P1–P4 scale). |
| DORA-RTS1772-4 | Article 4 | Regulatory incident classification/impact criteria (RTS 2024/1772) — GRC plane; the DORA cross-check declares an intentional gap (the Manual uses an internal P1–P4 scale). |
| DORA-RTS1772-7-1 | Article 7(1) and (2) | Regulatory incident classification/impact criteria (RTS 2024/1772) — GRC plane; the DORA cross-check declares an intentional gap (the Manual uses an internal P1–P4 scale). |
| DORA-RTS1772-7-3 | Article 7(3) and (4) | Regulatory incident classification/impact criteria (RTS 2024/1772) — GRC plane; the DORA cross-check declares an intentional gap (the Manual uses an internal P1–P4 scale). |
| DORA-RTS301-1 | Article 1 | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Content/templates of notifications. |
| DORA-RTS301-2 | Article 2 | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Content/templates of notifications. |
| DORA-RTS301-3 | Article 3 | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Content/templates of notifications. |
| DORA-RTS301-4 | Article 4 | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Content/templates of notifications. |
| DORA-RTS301-5-3 | Article 5(3) | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Content/templates of notifications. |
| DORA-RTS301-6 | Article 6 | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Content/templates of notifications. |
| DORA-ITS302-1-1 | Article 1(1), points (a) to (c); Annex I | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Templates, channels and procedures for communication (ITS 2025/302). |
| DORA-ITS302-1-2 | Article 1(2) | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Templates, channels and procedures for communication (ITS 2025/302). |
| DORA-ITS302-1-3 | Article 1(3) | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Templates, channels and procedures for communication (ITS 2025/302). |
| DORA-ITS302-1-4 | Article 1(4) | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Templates, channels and procedures for communication (ITS 2025/302). |
| DORA-ITS302-1-5 | Article 1(5); Annex II | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Templates, channels and procedures for communication (ITS 2025/302). |
| DORA-ITS302-3 | Article 3 | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Templates, channels and procedures for communication (ITS 2025/302). |
| DORA-ITS302-4-1 | Article 4(1) | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Templates, channels and procedures for communication (ITS 2025/302). |
| DORA-ITS302-4-2 | Article 4(2) | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Templates, channels and procedures for communication (ITS 2025/302). |
| DORA-ITS302-5 | Article 5 | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Templates, channels and procedures for communication (ITS 2025/302). |
| DORA-ITS302-6-1 | Article 6(1) | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Templates, channels and procedures for communication (ITS 2025/302). |
| DORA-ITS302-6-2 | Article 6(2) | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Templates, channels and procedures for communication (ITS 2025/302). |
| DORA-ITS302-6-3 | Article 6(3) | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Templates, channels and procedures for communication (ITS 2025/302). |
| DORA-ITS302-7-1 | Article 7(1) | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Templates, channels and procedures for communication (ITS 2025/302). |
| DORA-ITS302-7-2 | Article 7(2) | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Templates, channels and procedures for communication (ITS 2025/302). |
| DORA-ITS302-7-3 | Article 7(3) | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Templates, channels and procedures for communication (ITS 2025/302). |
| DORA-ITS302-8-1 | Article 8(1); Annexes III and IV | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Templates, channels and procedures for communication (ITS 2025/302). |
| DORA-ITS302-8-2 | Article 8(2) | Reporting to/relationship with the competent authority — legal-regulatory plane, not a software engineering prescription. Templates, channels and procedures for communication (ITS 2025/302). |
| DORA-RTS1190-4-1 | Article 4(1) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-4-2-b | Article 4(2), point (b) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-4-2-d | Article 4(2), point (d) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-4-2-e | Article 4(2), point (e) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-4-2-f | Article 4(2), point (f) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-6-2 | Article 6(2) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-7-1-a | Article 7(1), point (a) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-7-1-b | Article 7(1), point (b) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-7-1-cd | Article 7(1), points (c) and (d) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-7-1-e | Article 7(1), point (e) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-7-1-f | Article 7(1), point (f) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-7-1-g | Article 7(1), point (g) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-7-1-h | Article 7(1), point (h) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-7-2 | Article 7(2) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-8-1 | Article 8(1) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-9-1 | Article 9(1) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-9-2 | Article 9(2); Annex I | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-9-4 | Article 9(4) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-9-6-oa | Article 9(6), second sentence | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-9-8 | Article 9(8) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-9-9 | Article 9(9) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-9-10 | Article 9(10) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-9-11 | Article 9(11) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-10-2 | Article 10(2) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-10-3 | Article 10(3) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-10-4 | Article 10(4) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-10-5 | Article 10(5); Annex III | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-10-6 | Article 10(6) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-11-1 | Article 11(1); Annex IV | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-11-2 | Article 11(2) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-11-3 | Article 11(3) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-11-4 | Article 11(4) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-11-5 | Article 11(5) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-11-6 | Article 11(6) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-11-7 | Article 11(7) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-11-8 | Article 11(8) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-11-9 | Article 11(9) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-11-10 | Article 11(10) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-12-1 | Article 12(1) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-12-2 | Article 12(2); Annex V | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-12-3 | Article 12(3) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-12-4 | Article 12(4); Annex VI | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-12-5 | Article 12(5) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-12-6 | Article 12(6) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-12-7 | Article 12(7); Annex VII | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-13-1 | Article 13(1) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-15-1-a | Article 15(1), first subparagraph, point (a), and second subparagraph | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-15-1-b | Article 15(1), point (b) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-15-1-c | Article 15(1), point (c) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
| DORA-RTS1190-15-3 | Article 15(3) | Regulated TLPT process (Delegated Regulation (EU) 2025/1190) — addon 14 of Ch. 10 expressly declares it out of the Manual's scope (compliance/GRC/supervisor). |
