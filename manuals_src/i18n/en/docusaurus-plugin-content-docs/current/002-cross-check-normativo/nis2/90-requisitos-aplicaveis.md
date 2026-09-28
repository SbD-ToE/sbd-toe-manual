---
id: requisitos-aplicaveis
title: "Applicable requirements — Essential entity or important entity (NIS2)"
description: "The Manual's requirements that apply under context CTX-NIS2, by level and grade, with each floor that the regime elevates and its legal basis."
sidebar_position: 90
tags: [cross-check, nis2, requisitos, overlay]
sbdtoe_generated: reg-requirements-view
generated_by: scripts/gen_reg_views.py  # não se edita à mão: editar os catálogos, o overlay e a matriz
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
  - 002-cross-check-normativo/_matriz/nis2.yaml
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/nis2/90-requisitos-aplicaveis.md
  source_sha256: a0eda58c2af29f44afdc39419803fc844a75f06366ccbdfa69b73deb70b15056
  source_commit: null
  target_sha256: 93a2c6d6cab93ce83007e3be8a2d7f0c564ed7c58b4614544c067df6389bda94
  engine: gen_reg_views
  prompt_sha256: null
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: []
  glossary_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
  translated_at: 2026-09-27T00:00:00Z
  stamped_at: 2026-09-27T00:00:00Z
  reviewed_by: null
---

# Applicable requirements: Essential entity or important entity (NIS2)

For context **CTX-NIS2**, this page brings together the Manual's base selection per level and each **floor** that the regime elevates, with the obligation that grounds it. A context never lowers a minimum of the Manual.

## When it applies {#quando-se-aplica}

The entity is essential or important under Article 3 of Directive (EU) 2022/2555, as transposed (in Portugal, the national cybersecurity legal framework). The context is declared per entity and inherited by all applications. Declared per entity and inherited by all applications.

> Directive (EU) 2022/2555, Article 3(1) and (2): “For the purposes of this Directive, the following entities shall be considered to be essential entities”

## Grades {#graus}

- **PERTINENTE** — Relevant entity under Implementing Regulation (EU) 2024/2690 (cumulative with the context). The entity is of one of the types listed in Article 1 of Implementing Regulation (EU) 2024/2690 (DNS service providers, TLD name registries, cloud computing, data centres, content delivery networks, managed and managed security services, online marketplaces, search engines, social networks, trust services).

## Context floor list {#pisos}

| Floor | Target | Grade | Required floor | Scope | Legal basis | Justification of non-applicability |
|---|---|---|---|---|---|---|
| CTX-NIS2-P01 | [Policy 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade) | — | mandatory | Incident response process (IRP) mandatory at any level, including the recording of incidents and the post-mortem of significant incidents, with the review of the affected artefacts (§4.6). | Directive (EU) 2022/2555, Article 21(2), point (b); Implementing Regulation (EU) 2024/2690, Annex, point 3.1.1: “incident handling” (NIS2-21-2-b, NIS2-IR2690-3.1.1) | not admitted |
| CTX-NIS2-P02 | `OPS-007` | — | mandatory | — | Directive (EU) 2022/2555, Article 21(2), point (b); Implementing Regulation (EU) 2024/2690, Annex, point 3.1.1: “incident handling” (NIS2-21-2-b, NIS2-IR2690-3.1.1) | not admitted |
| CTX-NIS2-P03 | `LOG-004` | PERTINENTE | mandatory | — | Implementing Regulation (EU) 2024/2690, Annex, point 3.2.4: “The logs shall be regularly reviewed for any unusual or unwanted trends.” (NIS2-IR2690-3.2.4) | not admitted |
| CTX-NIS2-P04 | `LOG-007` | PERTINENTE | mandatory | — | Implementing Regulation (EU) 2024/2690, Annex, point 3.2.4: “If the laid down values for alarm threshold are exceeded, an alarm shall be triggered, where appropriate, automatically.” (NIS2-IR2690-3.2.4) | not admitted |
| CTX-NIS2-P05 | `OPS-005` | PERTINENTE | mandatory | — | Implementing Regulation (EU) 2024/2690, Annex, point 3.2.4: “The relevant entities shall ensure that, in case of an alarm, a qualified and appropriate response is initiated in a timely manner.” (NIS2-IR2690-3.2.4) | not admitted |
| CTX-NIS2-P06 | `LOG-005` | PERTINENTE | mandatory | Includes backups of the logs, protected from unauthorised access or changes. | Implementing Regulation (EU) 2024/2690, Annex, point 3.2.5: “The relevant entities shall maintain and back up logs for a predefined period and shall protect them from unauthorised access or changes.” (NIS2-IR2690-3.2.5) | not admitted |
| CTX-NIS2-P07 | [Policy 33 §2](/sbd-toe/assets/policies/policy-contratacao-segura#2-âmbito-e-obrigatoriedade) | PERTINENTE | mandatory | Supply chain security policy governing the relations with direct suppliers and service providers, at any level. | Implementing Regulation (EU) 2024/2690, Annex, point 5.1.1: “the relevant entities shall establish, implement and apply a supply chain security policy which governs the relations with their direct suppliers and service providers” (NIS2-IR2690-5.1.1) | not admitted |
| CTX-NIS2-P08 | `GOV-006` | PERTINENTE | mandatory | — | Implementing Regulation (EU) 2024/2690, Annex, point 5.1.1: “the relevant entities shall establish, implement and apply a supply chain security policy which governs the relations with their direct suppliers and service providers” (NIS2-IR2690-5.1.1) | not admitted |
| CTX-NIS2-P09 | `GOV-007` | PERTINENTE | mandatory | — | Implementing Regulation (EU) 2024/2690, Annex, point 5.1.1: “the relevant entities shall establish, implement and apply a supply chain security policy which governs the relations with their direct suppliers and service providers” (NIS2-IR2690-5.1.1) | not admitted |
| CTX-NIS2-P10 | `DPL-007` | PERTINENTE | mandatory | Changes tested and assessed before being implemented, including emergency and configuration changes. | Implementing Regulation (EU) 2024/2690, Annex, point 6.4.2: “The procedures shall ensure that those changes are documented and, based on the risk assessment carried out pursuant to point 2.1, tested and assessed in view of the potential impact before being implemented.” (NIS2-IR2690-6.4.2) | not admitted |
| CTX-NIS2-P11 | `IAC-007` | PERTINENTE | mandatory | — | Implementing Regulation (EU) 2024/2690, Annex, point 6.4.2: “The procedures shall ensure that those changes are documented and, based on the risk assessment carried out pursuant to point 2.1, tested and assessed in view of the potential impact before being implemented.” (NIS2-IR2690-6.4.2) | admitted |
| CTX-NIS2-P12 | `ACC-010` | PERTINENTE | mandatory | Includes the access rights of privileged and system administration accounts, at planned intervals, with the results documented. | Implementing Regulation (EU) 2024/2690, Annex, point 11.2.3: “The relevant entities shall review access rights at planned intervals and shall modify them based on organisational changes.” (NIS2-IR2690-11.2.3) | not admitted |
| CTX-NIS2-P13 | `GOV-016` | PERTINENTE | mandatory | Privileged accounts and system administration accounts. | Implementing Regulation (EU) 2024/2690, Annex, points 11.3.1, 11.3.2(a) and 11.4.1: “establish strong identification, authentication such as multi-factor authentication, and authorisation procedures for privileged accounts and system administration accounts” (NIS2-IR2690-11.3.1, NIS2-IR2690-11.3.2, NIS2-IR2690-11.4.1) | not admitted |
| CTX-NIS2-P14 | `GOV-015` | — | mandatory | Vulnerability handling and disclosure, including vulnerabilities reported by external sources. | Directive (EU) 2022/2555, Article 21(2), point (e): “including vulnerability handling and disclosure” (NIS2-21-2-e) | not admitted |
| CTX-NIS2-P15 | `GOV-015` | PERTINENTE | mandatory | The disclosure procedure follows the national coordinated vulnerability disclosure policy. | Implementing Regulation (EU) 2024/2690, Annex, point 6.10.2(e): “lay down a procedure for disclosing vulnerabilities in accordance with the applicable national coordinated vulnerability disclosure policy” (NIS2-IR2690-6.10.2) | not admitted |
| CTX-NIS2-P16 | `OPS-016` | PERTINENTE | mandatory | Complete and accurate backups, including configuration data and data in cloud environments, stored in a safe location outside the system's network; integrity verified and recovery tested, at any level. | Implementing Regulation (EU) 2024/2690, Annex, points 4.2.1 to 4.2.3 and 4.2.6: “the relevant entities shall lay down backup plans” (NIS2-IR2690-4.2.1, NIS2-IR2690-4.2.2, NIS2-IR2690-4.2.3, NIS2-IR2690-4.2.6) | not admitted |
| CTX-NIS2-P17 | `OPS-017` | PERTINENTE | mandatory | Recovery plan with activation and deactivation conditions and recovery order, also at L1. | Implementing Regulation (EU) 2024/2690, Annex, points 4.1.1 and 4.1.2: “The relevant entities’ operations shall be restored according to the business continuity and disaster recovery plan.” (NIS2-IR2690-4.1.1, NIS2-IR2690-4.1.2) | not admitted |
| CTX-NIS2-P18 | `GOV-014` | PERTINENTE | mandatory | Review at planned intervals of identities and of privileged and administration accounts on the supporting systems, with documented results. | Implementing Regulation (EU) 2024/2690, Annex, points 11.2.3, 11.3.3 and 11.5.4: “The relevant entities shall review access rights at planned intervals and shall modify them based on organisational changes.” (NIS2-IR2690-11.2.3, NIS2-IR2690-11.3.3, NIS2-IR2690-11.5.4) | not admitted |
| CTX-NIS2-P19 | `GOV-017` | PERTINENTE | mandatory | Granting, change, removal and documentation of access rights; unique identities, linked to a person and overseen; logging of identity management. | Implementing Regulation (EU) 2024/2690, Annex, points 11.2.1 and 11.5.1 to 11.5.3: “The relevant entities shall provide, modify, remove and document access rights to network and information systems in accordance with the access control policy referred to in point 11.1.” (NIS2-IR2690-11.2.1, NIS2-IR2690-11.5.1, NIS2-IR2690-11.5.2, NIS2-IR2690-11.5.3) | not admitted |
| CTX-NIS2-P20 | `ENC-007` | PERTINENTE | mandatory | Key and certificate management at any level, with the methods of point 9.2(c). | Implementing Regulation (EU) 2024/2690, Annex, point 9.2: “approach to key management” (NIS2-IR2690-9.2) | admitted |
| CTX-NIS2-P21 | `ENC-003` | PERTINENTE | mandatory | Approved primitives and protocols, with cryptographic agility where appropriate, reviewed at planned intervals in light of technical progress, at any level. | Implementing Regulation (EU) 2024/2690, Annex, points 9.2 and 9.3: “following, where appropriate, a cryptographic agility approach” (NIS2-IR2690-9.2, NIS2-IR2690-9.3) | admitted |

## Requirements added by the regime {#acrescentos}

These requirements only make sense under the regime, so they do not live in the Manual's catalogues; they are defined here, each with its legal basis.

| Requirement | Name | Acceptance criterion | Legal basis |
|---|---|---|---|
| `CTX-NIS2-R01` | At least partial redundancy | Based on the risk assessment and the continuity plan, sufficient availability of resources through at least partial redundancy of the network and information systems and of the communication channels the application depends on; resources monitored and adjusted according to the backup and redundancy requirements. | Implementing Regulation (EU) 2024/2690, Annex, points 4.2.4 and 4.2.5: “shall ensure sufficient availability of resources by at least partial redundancy of the following” (NIS2-IR2690-4.2.4, NIS2-IR2690-4.2.5) |
| `CTX-NIS2-R02` | Significant incident criterion | An incident is assessed as significant, from the impact data in the record (Policy 32 §4.3), when it has caused or is capable of causing severe operational disruption of the services or financial loss to the entity, or considerable material or non-material damage to other persons; the assessment and the decision are recorded. | Directive (EU) 2022/2555, Article 23(3): “An incident shall be considered to be significant if” (NIS2-23-3) |
| `CTX-NIS2-R03` | Significant incident thresholds and aggregation of recurring incidents | For relevant entities, the criteria of Article 3 of Implementing Regulation (EU) 2024/2690 apply (direct financial losses above EUR 500 000 or 5 % of turnover, whichever is lower; exfiltration of trade secrets; death or considerable damage to health; malicious access capable of causing severe disruption; and the criteria specific to each entity type). Every quarter, the existence of recurring incidents is assessed: those that occurred at least twice within six months, with the same apparent root cause, and that collectively meet the financial criterion count as one significant incident. | Implementing Regulation (EU) 2024/2690, Articles 3 and 4 and Annex, point 3.4.2: “have occurred at least twice within six months” (NIS2-IR2690-art3, NIS2-IR2690-art4, NIS2-IR2690-3.4.2) |

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
| `OPS-007` | Integration with a formal incident response process | ▲ | ▲ | ▲ | CTX-NIS2-P02 |
| `OPS-008` | Correlation of events across multiple sources | — | — | ✔ | — |
| `OPS-009` | Behavioural detection and baseline of normal activity | — | — | ✔ | — |
| `OPS-010` | Monitoring effectiveness metrics measured and reviewed | — | — | ✔ | — |
| `OPS-011` | Dedicated observability for AI/ML components in production | — | ✔ | ✔ | — |
| `OPS-012` | Complete audit per AI agent tool invocation | — | ✔ | ✔ | — |
| `OPS-013` | Budget and runaway detection in model consumption (token spend) | — | ✔ | ✔ | — |
| `OPS-014` | Detection of jailbreak / off-policy actions in production | — | — | ✔ | — |
| `OPS-015` | Continuous operational health and availability signals | — | ✔ | ✔ | — |
| `OPS-016` | Backups with tested restore | ✔ | ✔ | ✔ | — |
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
| `GOV-015` | Coordinated vulnerability disclosure with a published reporting channel | ▲ | ▲ | ▲ | CTX-NIS2-P14 |
| `GOV-016` | Privileged and administration accounts of supporting systems | ✔ | ✔ | ✔ | — |
| `GOV-017` | Lifecycle of identities with access to systems | ✔ | ✔ | ✔ | — |
| `CTX-NIS2-R02` | Significant incident criterion | ▲ | ▲ | ▲ | — |

## Requirement list — PERTINENTE {#lista-pertinente}

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
| `ACC-010` | Periodic review of permissions | ▲ | ▲ | ▲ | CTX-NIS2-P12 |
| `LOG-001` | Logging of critical events | ✔ | ✔ | ✔ | — |
| `LOG-002` | Minimum attributes in logs | ✔ | ✔ | ✔ | — |
| `LOG-003` | Protection of log integrity and access | ✔ | ✔ | ✔ | — |
| `LOG-004` | Periodic log analysis | ▲ | ▲ | ▲ | CTX-NIS2-P03 |
| `LOG-005` | Minimum log retention | ▲ | ▲ | ▲ | CTX-NIS2-P06 |
| `LOG-006` | Forwarding to a centralised system | — | ✔ | ✔ | — |
| `LOG-007` | Classification and anomaly detection | ▲ | ▲ | ▲ | CTX-NIS2-P04 |
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
| `ENC-003` | Robust cryptographic algorithms and configurations | ▲ | ▲ | ▲ | CTX-NIS2-P21 |
| `ENC-004` | Adaptive password hashing | ✔ | ✔ | ✔ | — |
| `ENC-005` | Masking of sensitive data in logs, outputs and API responses | ✔ | ✔ | ✔ | — |
| `ENC-006` | Detection and prevention of secrets exposed in repositories | ✔ | ✔ | ✔ | — |
| `ENC-007` | Lifecycle of keys, secrets and certificates | ▲ | ▲ | ▲ | CTX-NIS2-P20 |
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
| `IAC-007` | Traceable and approved plan before any apply | ▲ | ▲ | ▲ | CTX-NIS2-P11 |
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
| `DPL-007` | Validation in staging before promotion to production | ▲ | ▲ | ▲ | CTX-NIS2-P10 |
| `DPL-008` | Active monitoring during and after deployment | — | ✔ | ✔ | — |
| `DPL-009` | Progressive deployment with impact containment for critical applications | — | — | ✔ | — |
| `DPL-010` | Release gates for systems with AI agents | — | ✔ | ✔ | — |
| `DPL-011` | Canary and autonomy demotion in model releases | — | — | ✔ | — |
| `OPS-001` | Structured and persistent logging for all components in production | ✔ | ✔ | ✔ | — |
| `OPS-002` | Catalogue of critical security events defined and verified | ✔ | ✔ | ✔ | — |
| `OPS-003` | Log retention in accordance with policy and regulatory requirements | — | ✔ | ✔ | — |
| `OPS-004` | Centralisation of logs in a SIEM system or equivalent | — | ✔ | ✔ | — |
| `OPS-005` | Automatic alerts for critical security events | ▲ | ▲ | ▲ | CTX-NIS2-P05 |
| `OPS-006` | Alert response SLA defined and measured | — | ✔ | ✔ | — |
| `OPS-007` | Integration with a formal incident response process | ▲ | ▲ | ▲ | CTX-NIS2-P02 |
| `OPS-008` | Correlation of events across multiple sources | — | — | ✔ | — |
| `OPS-009` | Behavioural detection and baseline of normal activity | — | — | ✔ | — |
| `OPS-010` | Monitoring effectiveness metrics measured and reviewed | — | — | ✔ | — |
| `OPS-011` | Dedicated observability for AI/ML components in production | — | ✔ | ✔ | — |
| `OPS-012` | Complete audit per AI agent tool invocation | — | ✔ | ✔ | — |
| `OPS-013` | Budget and runaway detection in model consumption (token spend) | — | ✔ | ✔ | — |
| `OPS-014` | Detection of jailbreak / off-policy actions in production | — | — | ✔ | — |
| `OPS-015` | Continuous operational health and availability signals | — | ✔ | ✔ | — |
| `OPS-016` | Backups with tested restore | ▲ | ▲ | ▲ | CTX-NIS2-P16 |
| `OPS-017` | Recovery objectives and procedure for the application | ▲ | ▲ | ▲ | CTX-NIS2-P17 |
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
| `GOV-006` | Security clauses proportional to risk in contracts with third parties | ▲ | ▲ | ▲ | CTX-NIS2-P08 |
| `GOV-007` | Formal supplier validation before onboarding | ▲ | ▲ | ▲ | CTX-NIS2-P09 |
| `GOV-008` | Organisational traceability of security decisions per application | — | ✔ | ✔ | — |
| `GOV-009` | Evidence of decisions traceable, referenceable and retained | ✔ | ✔ | ✔ | — |
| `GOV-010` | Continuous validation cycle and periodic compliance review | — | ✔ | ✔ | — |
| `GOV-011` | Governance KPIs defined, collected and reported | — | ✔ | ✔ | — |
| `GOV-012` | Active maturity model with measured and planned evolution | — | — | ✔ | — |
| `GOV-013` | Technical onboarding and mandatory pre-access training of third parties | — | ✔ | ✔ | — |
| `GOV-014` | Periodic review of access to supporting systems (least privilege) | ▲ | ▲ | ▲ | CTX-NIS2-P18 |
| `GOV-015` | Coordinated vulnerability disclosure with a published reporting channel | ▲ | ▲ | ▲ | CTX-NIS2-P14, CTX-NIS2-P15 |
| `GOV-016` | Privileged and administration accounts of supporting systems | ▲ | ▲ | ▲ | CTX-NIS2-P13 |
| `GOV-017` | Lifecycle of identities with access to systems | ▲ | ▲ | ▲ | CTX-NIS2-P19 |
| `CTX-NIS2-R01` | At least partial redundancy | ▲ | ▲ | ▲ | — |
| `CTX-NIS2-R02` | Significant incident criterion | ▲ | ▲ | ▲ | — |
| `CTX-NIS2-R03` | Significant incident thresholds and aggregation of recurring incidents | ▲ | ▲ | ▲ | — |

## Obligations of the regime by coverage strength {#forca}

Count of the regime's obligations in the coverage matrix (excluding those addressed to the authorities). The section [“What this Manual covers and what stays out”](#cobertura) lists them.

| Strength | Obligations |
|---|--:|
| Covers | 98 |
| Partial | 57 |
| Supports evidence | 12 |
| Gap | 10 |
| Out of scope | 43 |

## What this Manual covers and what stays out {#cobertura}

All the obligations of the regime, in the Manual's coverage matrix, in three categories: what the Manual **covers**, and in what form; the **declared gaps** (what it does not cover by omission); and what is **out of scope**, with the reason. No obligation is left in silence. The 8 obligations addressed to the authorities create no duty for the organisation and are not listed.

### Covers (110) {#cobre}

Strength “covers” or “supports evidence”. The form is the Manual's response: catalogue requirement, policy, section, floor or requirement added by the regime.

| Obligation | Reference | Strength | Form |
|---|---|---|---|
| NIS2-21-2-a | Article 21(2), point (a) | Covers | `CLA-001`; [Policy 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); `THR-001`; [Policy 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível) |
| NIS2-21-2-b | Article 21(2), point (b) | Covers | [Policy 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade); [Policy 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade); [Policy 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp); [Policy 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta); `OPS-007` |
| NIS2-21-2-d | Article 21(2), point (d) | Covers | `GOV-006`; `GOV-007`; [Policy 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence); `DEP-006`; `DEP-001` |
| NIS2-21-2-e | Article 21(2), point (e) | Covers | `REQ-001`; `DEV-001`; `TST-001`; `DEP-002`; [Policy 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); `GOV-015` |
| NIS2-21-2-f | Article 21(2), point (f) | Covers | [Policy 35 §7](/sbd-toe/assets/policies/policy-kpis-governacao#7-avaliação-de-maturidade); `OPS-010`; `GOV-011`; [Policy 34 §5.2](/sbd-toe/assets/policies/policy-rastreabilidade-organizacional#52-processo-de-validação) |
| NIS2-21-2-h | Article 21(2), point (h) | Covers | `ENC-001`; `ENC-003`; [Policy 18 §4](/sbd-toe/assets/policies/policy-gestao-segredos#4-armazenamento-centralizado); [Policy 18 §6.1](/sbd-toe/assets/policies/policy-gestao-segredos#61-ttl-por-tipo-de-segredo) |
| NIS2-21-4 | Article 21(4) | Covers | `GOV-010`; [Policy 34 §5.2](/sbd-toe/assets/policies/policy-rastreabilidade-organizacional#52-processo-de-validação); `GOV-004` |
| NIS2-23-1-1 | Article 23(1), first subparagraph (first sentence) | Covers | [Policy 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade); [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-23-1-3 | Article 23(1), first subparagraph (third sentence) | Covers | [Policy 32 §6.1](/sbd-toe/assets/policies/policy-irp#61-critério-e-conteúdo-mínimo-por-regime) |
| NIS2-23-3 | Article 23(3) | Covers | `CTX-NIS2-R02`; [Policy 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação); [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-23-4-a | Article 23(4), point (a) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 32 §6.1](/sbd-toe/assets/policies/policy-irp#61-critério-e-conteúdo-mínimo-por-regime) |
| NIS2-23-4-b | Article 23(4), point (b) | Covers | [Policy 32 §6.1](/sbd-toe/assets/policies/policy-irp#61-critério-e-conteúdo-mínimo-por-regime); [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| NIS2-23-4-c | Article 23(4), point (c) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| NIS2-23-4-d | Article 23(4), point (d) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação); [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); [Policy 32 §6.1](/sbd-toe/assets/policies/policy-irp#61-critério-e-conteúdo-mínimo-por-regime) |
| NIS2-23-4-e | Article 23(4), point (e) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| NIS2-23-4-2par | Article 23(4), second subparagraph | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| NIS2-32-2-eg | Article 32(2), points (e) to (g); Article 33(2), points (d) to (f) | Supports evidence | [Policy 34 §7](/sbd-toe/assets/policies/policy-rastreabilidade-organizacional#7-evidência-auditável); `GOV-009`; [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) |
| NIS2-32-4-d | Article 32(4), points (b), (d) and (f); Article 33(4), points (b), (d) and (f) | Supports evidence | `GOV-010`; [Policy 34 §5.2](/sbd-toe/assets/policies/policy-rastreabilidade-organizacional#52-processo-de-validação) |
| NIS2-IR2690-art3 | Implementing Regulation (EU) 2024/2690, Article 3 | Covers | `CTX-NIS2-R03`; [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art4 | Implementing Regulation (EU) 2024/2690, Article 4 | Covers | `CTX-NIS2-R03` |
| NIS2-IR2690-art5 | Implementing Regulation (EU) 2024/2690, Article 5 | Supports evidence | `OPS-015`; [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art6 | Implementing Regulation (EU) 2024/2690, Article 6 | Supports evidence | `OPS-015`; [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art7 | Implementing Regulation (EU) 2024/2690, Article 7 | Supports evidence | `OPS-015`; [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art8 | Implementing Regulation (EU) 2024/2690, Article 8 | Supports evidence | `OPS-015`; [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art9 | Implementing Regulation (EU) 2024/2690, Article 9 | Supports evidence | `OPS-015`; [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art10 | Implementing Regulation (EU) 2024/2690, Article 10 | Supports evidence | `OPS-015`; [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art11 | Implementing Regulation (EU) 2024/2690, Article 11 | Supports evidence | `OPS-015`; [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art12 | Implementing Regulation (EU) 2024/2690, Article 12 | Supports evidence | `OPS-015`; [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art13 | Implementing Regulation (EU) 2024/2690, Article 13 | Supports evidence | `OPS-015`; [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-art14 | Implementing Regulation (EU) 2024/2690, Article 14 | Supports evidence | `OPS-015`; [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-1.2.1 | Implementing Regulation (EU) 2024/2690, Annex, point 1.2.1 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Covers | `GOV-001`; `GOV-002` |
| NIS2-IR2690-1.2.2 | Implementing Regulation (EU) 2024/2690, Annex, point 1.2.2 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Covers | `TRN-002`; `GOV-006`; `TRN-007` |
| NIS2-IR2690-1.2.4 | Implementing Regulation (EU) 2024/2690, Annex, point 1.2.4 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Covers | `GOV-002`; `TRN-008` |
| NIS2-IR2690-1.2.6 | Implementing Regulation (EU) 2024/2690, Annex, point 1.2.6 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Covers | [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `GOV-001` |
| NIS2-IR2690-2.1.4 | Implementing Regulation (EU) 2024/2690, Annex, point 2.1.4 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Covers | [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `CLA-005`; [Policy 04 §3.1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#31-cadências-mínimas-obrigatórias); [Policy 04 §4.1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#41-triggers-que-obrigam-a-revisão-imediata); `THR-006` |
| NIS2-IR2690-2.2.1 | Implementing Regulation (EU) 2024/2690, Annex, point 2.2.1 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Covers | [Policy 34 §5.2](/sbd-toe/assets/policies/policy-rastreabilidade-organizacional#52-processo-de-validação); `GOV-011`; [Policy 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte) |
| NIS2-IR2690-2.2.2 | Implementing Regulation (EU) 2024/2690, Annex, point 2.2.2 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Covers | [Policy 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte); `GOV-011` |
| NIS2-IR2690-2.2.3 | Implementing Regulation (EU) 2024/2690, Annex, point 2.2.3 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Covers | [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); [Policy 34 §5.1](/sbd-toe/assets/policies/policy-rastreabilidade-organizacional#51-cadência-de-validação) |
| NIS2-IR2690-3.1.1 | Implementing Regulation (EU) 2024/2690, Annex, point 3.1.1 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Covers | [Policy 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade); [Policy 32 §2](/sbd-toe/assets/policies/policy-irp#2-âmbito-e-obrigatoriedade); [Policy 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp); [Policy 32 §9](/sbd-toe/assets/policies/policy-irp#9-responsabilidades) |
| NIS2-IR2690-3.1.3 | Implementing Regulation (EU) 2024/2690, Annex, point 3.1.3 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Covers | [Policy 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp); [Policy 32 §10](/sbd-toe/assets/policies/policy-irp#10-revisão-e-auditoria-desta-política) |
| NIS2-IR2690-3.2.1 | Implementing Regulation (EU) 2024/2690, Annex, point 3.2.1 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Covers | `LOG-001`; `OPS-001`; `OPS-002`; [Policy 29 §4](/sbd-toe/assets/policies/policy-logging-estruturado#4-eventos-de-segurança-obrigatórios) |
| NIS2-IR2690-3.2.2 | Implementing Regulation (EU) 2024/2690, Annex, point 3.2.2 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Covers | `OPS-005`; [Policy 30 §7](/sbd-toe/assets/policies/policy-monitorizacao-seguranca#7-validação-e-tuning-de-regras-de-detecção) |
| NIS2-IR2690-3.2.7 | Implementing Regulation (EU) 2024/2690, Annex, point 3.2.7 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Covers | [Policy 29 §10](/sbd-toe/assets/policies/policy-logging-estruturado#10-revisão-e-auditoria-desta-política); `OPS-002`; [Policy 30 §8](/sbd-toe/assets/policies/policy-monitorizacao-seguranca#8-revisão-periódica-de-cobertura) |
| NIS2-IR2690-3.4.1 | Implementing Regulation (EU) 2024/2690, Annex, point 3.4.1 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Covers | [Policy 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp); [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| NIS2-IR2690-3.4.2 | Implementing Regulation (EU) 2024/2690, Annex, point 3.4.2 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Covers | `CTX-NIS2-R03`; [Policy 31 §3](/sbd-toe/assets/policies/policy-gestao-alertas#3-classificação-de-alertas); [Policy 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação); `OPS-008` |
| NIS2-IR2690-3.5.1 | Implementing Regulation (EU) 2024/2690, Annex, point 3.5.1 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Covers | [Policy 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta); `OPS-006` |
| NIS2-IR2690-3.5.2 | Implementing Regulation (EU) 2024/2690, Annex, point 3.5.2 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Covers | [Policy 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); [Policy 32 §4.4](/sbd-toe/assets/policies/policy-irp#44-erradicação); [Policy 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação) |
| NIS2-IR2690-3.5.3 | Implementing Regulation (EU) 2024/2690, Annex, point 3.5.3 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente); [Policy 32 §9](/sbd-toe/assets/policies/policy-irp#9-responsabilidades) |
| NIS2-IR2690-3.5.4 | Implementing Regulation (EU) 2024/2690, Annex, point 3.5.4 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Covers | [Policy 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); [Policy 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); `DPL-004` |
| NIS2-IR2690-3.5.5 | Implementing Regulation (EU) 2024/2690, Annex, point 3.5.5 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Covers | [Policy 32 §8](/sbd-toe/assets/policies/policy-irp#8-testes-periódicos-do-irp); `OPS-007`; [Ch. 12 US-17](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-17---exercícios-de-resposta-a-incidentes-end-to-end) |
| NIS2-IR2690-3.6.1 | Implementing Regulation (EU) 2024/2690, Annex, point 3.6.1 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Covers | [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); [Policy 32 §4.3](/sbd-toe/assets/policies/policy-irp#43-investigação) |
| NIS2-IR2690-3.6.2 | Implementing Regulation (EU) 2024/2690, Annex, point 3.6.2 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Covers | [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `CLA-006`; `TRN-006`; [Policy 32 §10](/sbd-toe/assets/policies/policy-irp#10-revisão-e-auditoria-desta-política) |
| NIS2-IR2690-3.6.3 | Implementing Regulation (EU) 2024/2690, Annex, point 3.6.3 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Covers | [Policy 35 §3.3](/sbd-toe/assets/policies/policy-kpis-governacao#33-operações-e-resposta-a-incidentes) |
| NIS2-IR2690-4.1.2 | Implementing Regulation (EU) 2024/2690, Annex, point 4.1.2 (Article 21(2), point (c), of Directive (EU) 2022/2555) | Covers | `OPS-017` |
| NIS2-IR2690-4.2.1 | Implementing Regulation (EU) 2024/2690, Annex, point 4.2.1 (Article 21(2), point (c), of Directive (EU) 2022/2555) | Covers | `OPS-016`; `CTX-NIS2-R01` |
| NIS2-IR2690-4.2.2 | Implementing Regulation (EU) 2024/2690, Annex, point 4.2.2 (Article 21(2), point (c), of Directive (EU) 2022/2555) | Covers | `OPS-016` |
| NIS2-IR2690-4.2.3 | Implementing Regulation (EU) 2024/2690, Annex, point 4.2.3 (Article 21(2), point (c), of Directive (EU) 2022/2555) | Covers | `OPS-016` |
| NIS2-IR2690-4.2.4 | Implementing Regulation (EU) 2024/2690, Annex, point 4.2.4 (Article 21(2), point (c), of Directive (EU) 2022/2555) | Covers | `CTX-NIS2-R01` |
| NIS2-IR2690-4.2.5 | Implementing Regulation (EU) 2024/2690, Annex, point 4.2.5 (Article 21(2), point (c), of Directive (EU) 2022/2555) | Covers | `CTX-NIS2-R01` |
| NIS2-IR2690-4.2.6 | Implementing Regulation (EU) 2024/2690, Annex, point 4.2.6 (Article 21(2), point (c), of Directive (EU) 2022/2555) | Covers | `OPS-016` |
| NIS2-IR2690-5.1.5 | Implementing Regulation (EU) 2024/2690, Annex, point 5.1.5 (Article 21(2), point (d), of Directive (EU) 2022/2555) | Covers | [Policy 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence) |
| NIS2-IR2690-5.1.6 | Implementing Regulation (EU) 2024/2690, Annex, point 5.1.6 (Article 21(2), point (d), of Directive (EU) 2022/2555) | Covers | [Policy 33 §6.2](/sbd-toe/assets/policies/policy-contratacao-segura#62-reavaliação-periódica); `GOV-010` |
| NIS2-IR2690-5.1.7 | Implementing Regulation (EU) 2024/2690, Annex, point 5.1.7 (Article 21(2), point (d), of Directive (EU) 2022/2555) | Covers | [Policy 33 §6.1](/sbd-toe/assets/policies/policy-contratacao-segura#61-indicadores-de-conformidade-a-monitorizar); [Policy 33 §6.1](/sbd-toe/assets/policies/policy-contratacao-segura#61-indicadores-de-conformidade-a-monitorizar); `GOV-010`; [Policy 33 §10.4](/sbd-toe/assets/policies/policy-contratacao-segura#104-sla-de-notificação-prévia) |
| NIS2-IR2690-6.1.3 | Implementing Regulation (EU) 2024/2690, Annex, point 6.1.3 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); [Policy 33 §4.3](/sbd-toe/assets/policies/policy-contratacao-segura#43-modelo-contratual-de-referência) |
| NIS2-IR2690-6.2.1 | Implementing Regulation (EU) 2024/2690, Annex, point 6.2.1 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | `REQ-001`; `DEV-001`; `TST-001`; `CIC-001` |
| NIS2-IR2690-6.2.2 | Implementing Regulation (EU) 2024/2690, Annex, point 6.2.2 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | `REQ-002`; [Policy 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura); `DEV-001`; `IDE-006`; `CIC-006`; `TST-001`; [Policy 25 §6](/sbd-toe/assets/policies/policy-deploy-seguro#6-separação-de-ambientes-e-dados); [Ch. 10 US-19](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-19---proteção-dos-ativos-do-processo-de-teste) |
| NIS2-IR2690-6.2.4 | Implementing Regulation (EU) 2024/2690, Annex, point 6.2.4 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | `DEV-001` |
| NIS2-IR2690-6.3.1 | Implementing Regulation (EU) 2024/2690, Annex, point 6.3.1 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | `CFG-001`; `IAC-003`; `CNT-009`; [Policy 21 §3](/sbd-toe/assets/policies/policy-iac-seguro#3-princípios-de-iac-seguro) |
| NIS2-IR2690-6.4.1 | Implementing Regulation (EU) 2024/2690, Annex, point 6.4.1 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | `DPL-001`; `IAC-007`; `CIC-001` |
| NIS2-IR2690-6.4.3 | Implementing Regulation (EU) 2024/2690, Annex, point 6.4.3 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | [Emergency deploy - break glass](/sbd-toe/sbd-manual/deploy-seguro/addon/excecoes-deploy#emergency-deploy---break-glass); [Policy 26 §7](/sbd-toe/assets/policies/policy-aprovacao-release#7-releases-de-emergência) |
| NIS2-IR2690-6.4.4 | Implementing Regulation (EU) 2024/2690, Annex, point 6.4.4 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | [Policy 26 §9](/sbd-toe/assets/policies/policy-aprovacao-release#9-revisão-e-auditoria-desta-política) |
| NIS2-IR2690-6.5.1 | Implementing Regulation (EU) 2024/2690, Annex, point 6.5.1 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | `TST-001` |
| NIS2-IR2690-6.5.2 | Implementing Regulation (EU) 2024/2690, Annex, point 6.5.2 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | `TST-001`; `TST-004`; `TST-003`; `TST-008` |
| NIS2-IR2690-6.5.3 | Implementing Regulation (EU) 2024/2690, Annex, point 6.5.3 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | `TST-001` |
| NIS2-IR2690-6.6.2 | Implementing Regulation (EU) 2024/2690, Annex, point 6.6.2 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | [Policy 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção); `GOV-004` |
| NIS2-IR2690-6.7.1 | Implementing Regulation (EU) 2024/2690, Annex, point 6.7.1 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | `ARC-006`; `ACC-005`; `ENC-001`; `CLA-003` |
| NIS2-IR2690-6.7.3 | Implementing Regulation (EU) 2024/2690, Annex, point 6.7.3 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `ARC-009`; `ARC-010` |
| NIS2-IR2690-6.8.1 | Implementing Regulation (EU) 2024/2690, Annex, point 6.8.1 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | `ARC-001`; `ARC-006`; [Policy 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura) |
| NIS2-IR2690-6.8.3 | Implementing Regulation (EU) 2024/2690, Annex, point 6.8.3 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `ARC-009`; `ARC-010` |
| NIS2-IR2690-6.10.1 | Implementing Regulation (EU) 2024/2690, Annex, point 6.10.1 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | `DEP-002`; `CNT-002`; [Policy 11 §7](/sbd-toe/assets/policies/policy-sbom#7-inventário-em-produção); [Policy 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção) |
| NIS2-IR2690-6.10.2 | Implementing Regulation (EU) 2024/2690, Annex, point 6.10.2 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | [Policy 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção); [KEV — confirmed exploitation](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/epss-kev-priorizacao#kev--exploração-confirmada); [Policy 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); `DEP-010`; `GOV-015`; `DEP-010` |
| NIS2-IR2690-6.10.3 | Implementing Regulation (EU) 2024/2690, Annex, point 6.10.3 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Covers | [Policy 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção); `DEP-010`; `GOV-004` |
| NIS2-IR2690-7.1 | Implementing Regulation (EU) 2024/2690, Annex, point 7.1 (Article 21(2), point (f), of Directive (EU) 2022/2555) | Covers | [Policy 35 §7](/sbd-toe/assets/policies/policy-kpis-governacao#7-avaliação-de-maturidade); `OPS-010`; `GOV-011` |
| NIS2-IR2690-7.2 | Implementing Regulation (EU) 2024/2690, Annex, point 7.2 (Article 21(2), point (f), of Directive (EU) 2022/2555) | Covers | [Policy 35 §4](/sbd-toe/assets/policies/policy-kpis-governacao#4-fontes-de-dados-e-recolha); [Policy 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte) |
| NIS2-IR2690-7.3 | Implementing Regulation (EU) 2024/2690, Annex, point 7.3 (Article 21(2), point (f), of Directive (EU) 2022/2555) | Covers | [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); [Policy 35 §10](/sbd-toe/assets/policies/policy-kpis-governacao#10-revisão-e-auditoria-desta-política) |
| NIS2-IR2690-8.1.3 | Implementing Regulation (EU) 2024/2690, Annex, point 8.1.3 (Article 21(2), point (g), of Directive (EU) 2022/2555) | Covers | `TRN-003`; `TRN-009`; [Policy 37 §7](/sbd-toe/assets/policies/policy-formacao-seguranca#7-actualização-de-conteúdos-formativos) |
| NIS2-IR2690-8.2.1 | Implementing Regulation (EU) 2024/2690, Annex, point 8.2.1 (Article 21(2), point (g), of Directive (EU) 2022/2555) | Covers | `TRN-001`; `TRN-001`; `TRN-005` |
| NIS2-IR2690-8.2.2 | Implementing Regulation (EU) 2024/2690, Annex, point 8.2.2 (Article 21(2), point (g), of Directive (EU) 2022/2555) | Covers | `TRN-001` |
| NIS2-IR2690-8.2.3 | Implementing Regulation (EU) 2024/2690, Annex, point 8.2.3 (Article 21(2), point (g), of Directive (EU) 2022/2555) | Covers | `TRN-003`; [Policy 37 §3.1](/sbd-toe/assets/policies/policy-formacao-seguranca#31-conteúdos-mínimos-de-onboarding); [Policy 37 §8](/sbd-toe/assets/policies/policy-formacao-seguranca#8-kpis-de-eficácia-formativa) |
| NIS2-IR2690-8.2.5 | Implementing Regulation (EU) 2024/2690, Annex, point 8.2.5 (Article 21(2), point (g), of Directive (EU) 2022/2555) | Covers | `TRN-006`; [Policy 37 §7](/sbd-toe/assets/policies/policy-formacao-seguranca#7-actualização-de-conteúdos-formativos) |
| NIS2-IR2690-9.1 | Implementing Regulation (EU) 2024/2690, Annex, point 9.1 (Article 21(2), point (h), of Directive (EU) 2022/2555) | Covers | `ENC-001`; `ENC-003`; `ENC-009`; [Policy 18 §4](/sbd-toe/assets/policies/policy-gestao-segredos#4-armazenamento-centralizado) |
| NIS2-IR2690-9.2 | Implementing Regulation (EU) 2024/2690, Annex, point 9.2 (Article 21(2), point (h), of Directive (EU) 2022/2555) | Covers | `ENC-007`; `ENC-003`; `ENC-003`; `ENC-002`; `ENC-007`; [Policy 18 §6.1](/sbd-toe/assets/policies/policy-gestao-segredos#61-ttl-por-tipo-de-segredo); [Policy 18 §6.3](/sbd-toe/assets/policies/policy-gestao-segredos#63-revogação-por-exposição-suspeita) |
| NIS2-IR2690-9.3 | Implementing Regulation (EU) 2024/2690, Annex, point 9.3 (Article 21(2), point (h), of Directive (EU) 2022/2555) | Covers | `ENC-003`; [Policy 18 §11](/sbd-toe/assets/policies/policy-gestao-segredos#11-revisão-e-auditoria-desta-política) |
| NIS2-IR2690-11.1.2 | Implementing Regulation (EU) 2024/2690, Annex, point 11.1.2 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Covers | `ACC-005`; `INT-002`; `ARC-015` |
| NIS2-IR2690-11.2.1 | Implementing Regulation (EU) 2024/2690, Annex, point 11.2.1 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Covers | `ACC-008`; `GOV-014`; [Policy 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding); `GOV-017` |
| NIS2-IR2690-11.2.2 | Implementing Regulation (EU) 2024/2690, Annex, point 11.2.2 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Covers | `ACC-002`; `ACC-004`; `GOV-014`; [Policy 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding); `ACC-003` |
| NIS2-IR2690-11.2.3 | Implementing Regulation (EU) 2024/2690, Annex, point 11.2.3 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Covers | `ACC-010`; `GOV-014`; `ACC-010`; `GOV-014` |
| NIS2-IR2690-11.3.1 | Implementing Regulation (EU) 2024/2690, Annex, point 11.3.1 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Covers | `GOV-016` |
| NIS2-IR2690-11.3.2 | Implementing Regulation (EU) 2024/2690, Annex, point 11.3.2 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Covers | `ACC-004`; `AUT-001`; [🛡️ Security requirements per environment](/sbd-toe/sbd-manual/deploy-seguro/addon/08-segregacao-e-validacao-operacional#️-requisitos-de-segurança-por-ambiente); `GOV-016` |
| NIS2-IR2690-11.3.3 | Implementing Regulation (EU) 2024/2690, Annex, point 11.3.3 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Covers | `ACC-010`; `GOV-014` |
| NIS2-IR2690-11.4.1 | Implementing Regulation (EU) 2024/2690, Annex, point 11.4.1 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Covers | `GOV-016`; `GOV-016` |
| NIS2-IR2690-11.5.1 | Implementing Regulation (EU) 2024/2690, Annex, point 11.5.1 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Covers | `ACC-008`; [Policy 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding); `ARC-015`; `GOV-017`; `GOV-017` |
| NIS2-IR2690-11.5.2 | Implementing Regulation (EU) 2024/2690, Annex, point 11.5.2 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Covers | `LOG-002`; `CIC-011`; [Ch. 07 US-20](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-20); `ARC-015`; `GOV-017` |
| NIS2-IR2690-11.5.3 | Implementing Regulation (EU) 2024/2690, Annex, point 11.5.3 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Covers | [Ch. 07 US-20](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-20); `GOV-017` |
| NIS2-IR2690-11.5.4 | Implementing Regulation (EU) 2024/2690, Annex, point 11.5.4 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Covers | `GOV-014`; `ACC-010`; [Policy 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding); `GOV-014`; `GOV-017` |
| NIS2-IR2690-11.6.1 | Implementing Regulation (EU) 2024/2690, Annex, point 11.6.1 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Covers | `AUT-002`; `AUT-003`; `AUT-006`; `ACC-005` |
| NIS2-IR2690-11.6.2 | Implementing Regulation (EU) 2024/2690, Annex, point 11.6.2 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Covers | `AUT-002`; `AUT-003`; `AUT-005`; `AUT-006`; `SES-002`; [Policy 18 §6.3](/sbd-toe/assets/policies/policy-gestao-segredos#63-revogação-por-exposição-suspeita); `ACC-004`; `AUT-011` |
| NIS2-IR2690-11.7.1 | Implementing Regulation (EU) 2024/2690, Annex, point 11.7.1 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Covers | `AUT-001`; `AUT-008`; `CLA-003` |
| NIS2-IR2690-11.7.2 | Implementing Regulation (EU) 2024/2690, Annex, point 11.7.2 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Covers | `AUT-001`; `AUT-008`; `CLA-003` |
| NIS2-IR2690-12.1.3 | Implementing Regulation (EU) 2024/2690, Annex, point 12.1.3 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Covers | `CLA-005`; `CLA-006` |

### Declared gap (67) {#lacuna}

Strength “partial” or “gap”: the Manual does not cover, or covers only in part, and says what is missing. Gaps pending an AppSec Core round are marked with the name of the round.

| Obligation | Reference | Strength | How the Manual responds | What is missing |
|---|---|---|---|---|
| NIS2-20-1 | Article 20(1) | Partial | `GOV-001`; [Ch. 14 US-22](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-22); `GOV-011`; [Policy 35 §5](/sbd-toe/assets/policies/policy-kpis-governacao#5-cadência-de-recolha-e-reporte) | The Manual requires approval “by senior management” of the governance model and the policies, and reporting of KPIs to management, but does not assign to the management body the approval of the Article 21 measures as a whole, oversight of their implementation, or personal liability; the cross-check acknowledges that it “does not fix ex ante the exact legal form of the approval chain”. |
| NIS2-20-2 | Article 20(2) | Partial | [Policy 37 §4.1](/sbd-toe/assets/policies/policy-formacao-seguranca#41-matriz-de-trilhos-por-perfil-e-nível-de-risco); `TRN-001` | There is no mandatory training of members of the management body in cybersecurity risk management: Policy 37 covers “staff with technical functions” and for “Management / Tech Lead” provides only “Executive awareness” at L1; regular training of the remaining (non-technical) employees is not prescribed. |
| NIS2-21-1 | Article 21(1) | Partial | `CLA-003`; [Policy 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); `REQ-001` | The Manual's proportionality is per application (L1–L3) and covers the software lifecycle; it does not cover the entity's network and information systems as a whole (corporate network, workstations, premises, continuity). |
| NIS2-21-2 | Article 21(2), introductory wording | Partial | `CLA-003`; [Policy 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura); `OPS-016`; `OPS-017` | All-hazards approach: the application backups and recovery are covered (OPS-016, OPS-017); the physical environment and the entity's business continuity are out of scope; general cyber hygiene is partial. |
| NIS2-21-2-c | Article 21(2), point (c) | Partial | `OPS-016`; `OPS-017` | The entity's business continuity and crisis management fall outside the scope of the Manual; recovery of the application is prescribed (OPS-016, OPS-017). |
| NIS2-21-2-g | Article 21(2), point (g) | Partial | [Policy 37 §2](/sbd-toe/assets/policies/policy-formacao-seguranca#2-âmbito-e-obrigatoriedade); `TRN-002`; `TRN-007` | Security training prescribed for technical roles and third parties with access; cyber hygiene practices and awareness for all (non-technical) staff and for the management bodies are missing. |
| NIS2-21-2-i | Article 21(2), point (i) | Partial | `ACC-001`; `ACC-002`; `CLA-008`; `TRN-002` | Access control covered; asset management limited to the inventory of applications and components (no inventory of all assets nor asset handling policy); human resources security out of scope except onboarding/offboarding. |
| NIS2-21-2-j | Article 21(2), point (j) | Partial | `AUT-001`; `AUT-008`; [🛡️ Security requirements per environment](/sbd-toe/sbd-manual/deploy-seguro/addon/08-segregacao-e-validacao-operacional#️-requisitos-de-segurança-por-ambiente); `GOV-016` | Secured voice, video and text communications and secured emergency communication systems are not addressed (entity security, outside the scope of the Manual); MFA is prescribed for the application (AUT-001) and for privileged access to the supporting systems (GOV-016). |
| NIS2-21-3 | Article 21(3) | Partial | [Policy 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação); [Policy 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação); `DEP-006`; `GOV-007` | Due diligence assesses the supplier's vulnerability management process and test reports (L2/L3), but not the overall quality of products nor secure development procedures as an explicit criterion, and ignores the Union-level coordinated risk assessments (Article 22). |
| NIS2-23-1-2 | Article 23(1), first subparagraph (second sentence) | Partial | [Policy 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente) | There is a generic communication “to affected users where applicable”, but the NIS2 line of Policy 32 §6 does not include notification of the recipients of the services (unlike the DORA and CRA lines), with no deadline and no “likely to adversely affect the provision” criterion. |
| NIS2-23-2 | Article 23(2) | Gap | — | There is no duty to communicate to the recipients of the service significant cyber threats or the measures they can take; Policy 32 deals only with incidents. |
| NIS2-23-7 | Article 23(7) | Partial | [Policy 32 §9](/sbd-toe/assets/policies/policy-irp#9-responsabilidades); [Policy 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente) | There is control over who authorises public communications, but not the procedure for informing the public when the CSIRT/authority requires it. |
| NIS2-24-1 | Article 24(1) | Gap | — | The procurement and due diligence criteria (Policy 33 §3.1) do not provide for the requirement of ICT products, services or processes certified under European cybersecurity certification schemes (CSA) where the Member State imposes it. |
| NIS2-IR2690-art2 | Implementing Regulation (EU) 2024/2690, Article 2 | Partial | `GOV-004`; [Policy 05 §3](/sbd-toe/assets/policies/policy-gestao-excecoes#3-princípios-fundamentais); `CLA-003` | Non-application of controls goes through a documented formal exception, but exemptions by level (requirements marked “-” or “Recommended” at L1/L2) are not exceptions and do not generate the documented justification, requirement by requirement, that Article 2(2) requires when a modulated requirement is considered not applicable. |
| NIS2-IR2690-1.1.1 | Implementing Regulation (EU) 2024/2690, Annex, point 1.1.1 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Partial | `GOV-001`; [Ch. 14 US-22](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-22); `GOV-012` | There is no policy on the security of network and information systems with the minimum content of point 1.1.1 (approach, objectives, commitment of resources, documentation to be kept, list of topic-specific policies, maturity indicators); there is a governance model and a body of policies approved by management, with maturity only at L3 (GOV-012). |
| NIS2-IR2690-1.1.2 | Implementing Regulation (EU) 2024/2690, Annex, point 1.1.2 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Partial | [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `GOV-001`; [Ch. 14 US-22](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-22) | Yearly review and review after a significant incident prescribed; review after significant changes to operations or risks and documentation of the result by management are missing. |
| NIS2-IR2690-1.2.3 | Implementing Regulation (EU) 2024/2690, Annex, point 1.2.3 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Gap | — | The Manual refers to the CISO as a decision authority, but does not require designating a person who reports directly to the management bodies on matters of the security of network and information systems. |
| NIS2-IR2690-1.2.5 | Implementing Regulation (EU) 2024/2690, Annex, point 1.2.5 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Partial | `CIC-008`; [Policy 22 §5](/sbd-toe/assets/policies/policy-aprovacao-plan-iac#5-separação-de-funções-sod) | Technical segregation of duties in pipelines and IaC apply (L2/L3); there is no organisational rule for segregating conflicting areas of responsibility. |
| NIS2-IR2690-2.1.1 | Implementing Regulation (EU) 2024/2690, Annex, point 2.1.1 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Partial | `CLA-001`; `CLA-007`; [Policy 03 §7](/sbd-toe/assets/policies/policy-aceitacao-risco#7-alçadas-de-aprovação) | Per-application risk framework with documented residual risk; acceptance of residual risk goes up at most to the CISO — not to the management bodies — and there is no risk treatment plan for the entity. |
| NIS2-IR2690-2.1.2 | Implementing Regulation (EU) 2024/2690, Annex, point 2.1.2 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Partial | [Policy 02 §3](/sbd-toe/assets/policies/policy-classificacao-risco#3-modelo-de-classificação---eixos-edi); `THR-001`; `THR-004`; [Policy 03 §5](/sbd-toe/assets/policies/policy-aceitacao-risco#5-limiares-de-aceitação-por-nível) | Methodology (E/D/I axes, STRIDE) and threat disposition exist, but the process is per application: entity risk tolerance, identification of third-party risks and single points of failure, and threat modelling at L1 are missing. |
| NIS2-IR2690-2.1.3 | Implementing Regulation (EU) 2024/2690, Annex, point 2.1.3 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Partial | [Policy 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); [KEV — confirmed exploitation](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/epss-kev-priorizacao#kev--exploração-confirmada); `CLA-003` | Prioritisation by severity, exploitation (KEV/EPSS) and level; no cost-benefit and no link to business impact analysis. |
| NIS2-IR2690-2.3.1 | Implementing Regulation (EU) 2024/2690, Annex, point 2.3.1 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Partial | [Ch. 12 US-12](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-12---rastreabilidade-e-conformidade-com-regulações-ssdf-nis2-iso-27001); [Ch. 14 US-22](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-22); `THR-007` | Internal and adherence audits provided for; an independent review of the approach to security management as a whole (people, processes, technologies) is not required. |
| NIS2-IR2690-2.3.2 | Implementing Regulation (EU) 2024/2690, Annex, point 2.3.2 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Gap | — | There is no requirement for audit competences or for hierarchical independence of reviewers from the area reviewed (independence appears only in the threat model — THR-007 — and in testing). |
| NIS2-IR2690-2.3.3 | Implementing Regulation (EU) 2024/2690, Annex, point 2.3.3 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Partial | [Ch. 14 US-22](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-22); `GOV-010` | Deviations generate corrective action; communicating the results to the management bodies, or the formal alternative of acceptance of residual risk by them, is not required. |
| NIS2-IR2690-2.3.4 | Implementing Regulation (EU) 2024/2690, Annex, point 2.3.4 (Article 21(2), point (a), of Directive (EU) 2022/2555) | Partial | [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); [Ch. 12 US-12](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-12---rastreabilidade-e-conformidade-com-regulações-ssdf-nis2-iso-27001) | Yearly internal audit and review after a significant incident; no trigger after significant changes. |
| NIS2-IR2690-3.1.2 | Implementing Regulation (EU) 2024/2690, Annex, point 3.1.2 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Partial | [Policy 32 §6.1](/sbd-toe/assets/policies/policy-irp#61-critério-e-conteúdo-mínimo-por-regime); [Policy 32 §3](/sbd-toe/assets/policies/policy-irp#3-critérios-de-activação-do-irp); [Policy 31 §3](/sbd-toe/assets/policies/policy-gestao-alertas#3-classificação-de-alertas); [Policy 32 §5](/sbd-toe/assets/policies/policy-irp#5-playbooks-de-resposta); [Policy 31 §5](/sbd-toe/assets/policies/policy-gestao-alertas#5-escalonamento-automático); [Policy 32 §9](/sbd-toe/assets/policies/policy-irp#9-responsabilidades) | Categorisation, playbooks, escalation, roles, contacts and the minimum content of notifications exist; consistency with the entity's business continuity plan is out of scope. |
| NIS2-IR2690-3.2.3 | Implementing Regulation (EU) 2024/2690, Annex, point 3.2.3 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Partial | `OPS-001`; `OPS-002`; [Policy 29 §4](/sbd-toe/assets/policies/policy-logging-estruturado#4-eventos-de-segurança-obrigatórios); `LOG-002` | An event catalogue and coverage by inventory exist; the required content does not include incoming and outgoing network traffic, execution of system utilities or access to network systems (the Manual is application-centred). |
| NIS2-IR2690-3.2.4 | Implementing Regulation (EU) 2024/2690, Annex, point 3.2.4 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Partial | `LOG-004`; `LOG-007`; `OPS-005`; [6️⃣ Essential Logging and Monitoring (Ch. 12)](/sbd-toe/sbd-manual/fundamentos/baseline#6️⃣-registo-e-monitorização-essencial-cap-12) | Regular analysis of logs and automatic alarms with thresholds mandatory only at L2/L3. |
| NIS2-IR2690-3.2.5 | Implementing Regulation (EU) 2024/2690, Annex, point 3.2.5 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Partial | `LOG-005`; `LOG-003`; [Policy 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs); [Policy 29 §8](/sbd-toe/assets/policies/policy-logging-estruturado#8-integridade-e-imutabilidade) | Retention for a defined period and protection against alteration are in the catalogue; backup of logs is not prescribed. |
| NIS2-IR2690-3.2.6 | Implementing Regulation (EU) 2024/2690, Annex, point 3.2.6 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Partial | [🛠️ Functional requirements of the integration](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/integracao-siem#️-requisitos-funcionais-da-integração); `OPS-001` | NTP synchronisation referred to in the SIEM integration (addon, L2+) and coverage inventory; redundancy of the monitoring and logging systems is not required. |
| NIS2-IR2690-3.3.1 | Implementing Regulation (EU) 2024/2690, Annex, point 3.3.1 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Partial | [Policy 37 §3.1](/sbd-toe/assets/policies/policy-formacao-seguranca#31-conteúdos-mínimos-de-onboarding); [Policy 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) | Reporting channel for technical staff and contractual notification by suppliers; there is no mechanism for customers or for non-technical employees. |
| NIS2-IR2690-3.3.2 | Implementing Regulation (EU) 2024/2690, Annex, point 3.3.2 (Article 21(2), point (b), of Directive (EU) 2022/2555) | Partial | [Policy 37 §3.1](/sbd-toe/assets/policies/policy-formacao-seguranca#31-conteúdos-mínimos-de-onboarding) | Training of technical staff in the reporting channel; making the mechanism known to suppliers and customers is not provided for. |
| NIS2-IR2690-4.1.1 | Implementing Regulation (EU) 2024/2690, Annex, point 4.1.1 (Article 21(2), point (c), of Directive (EU) 2022/2555) | Partial | `OPS-017`; `OPS-017` | The entity's business continuity and crisis management fall outside the scope of the Manual; recovery of the application is prescribed (OPS-016, OPS-017). |
| NIS2-IR2690-4.1.3 | Implementing Regulation (EU) 2024/2690, Annex, point 4.1.3 (Article 21(2), point (c), of Directive (EU) 2022/2555) | Partial | `CLA-001`; [🎯 Objective](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia#-objetivo) | The impact axis of the classification and the reuse of existing DRP/BIA support impact analysis, but the Manual does not require a BIA nor derive continuity requirements from it. |
| NIS2-IR2690-4.1.4 | Implementing Regulation (EU) 2024/2690, Annex, point 4.1.4 (Article 21(2), point (c), of Directive (EU) 2022/2555) | Partial | `OPS-017` | Exercising the recovery procedure is mandatory only at L3 (OPS-017); updating the entity's continuity plan is out of scope. |
| NIS2-IR2690-4.3.3 | Implementing Regulation (EU) 2024/2690, Annex, point 4.3.3 (Article 21(2), point (c), of Directive (EU) 2022/2555) | Partial | [Policy 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção); [KEV — confirmed exploitation](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/epss-kev-priorizacao#kev--exploração-confirmada) | Consumes vulnerability feeds (NVD/OSV/GitHub) and KEV; there is no process for managing and using information received from CSIRTs or authorities on incidents, threats and mitigation measures. |
| NIS2-IR2690-5.1.1 | Implementing Regulation (EU) 2024/2690, Annex, point 5.1.1 (Article 21(2), point (d), of Directive (EU) 2022/2555) | Partial | [Policy 33 §2](/sbd-toe/assets/policies/policy-contratacao-segura#2-âmbito-e-obrigatoriedade); `GOV-006`; `GOV-007` | The secure procurement policy (Policy 33) is mandatory at all levels, but it does not define the entity's role in the supply chain nor communicate it to suppliers. |
| NIS2-IR2690-5.1.2 | Implementing Regulation (EU) 2024/2690, Annex, point 5.1.2 (Article 21(2), point (d), of Directive (EU) 2022/2555) | Partial | [Policy 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação); [Policy 33 §3.1](/sbd-toe/assets/policies/policy-contratacao-segura#31-critérios-de-avaliação); `GOV-007` | Due diligence criteria (L2/L3) cover security practices and vulnerability management; capacity to meet specifications, quality and resilience of products, and diversification of sources are missing. |
| NIS2-IR2690-5.1.3 | Implementing Regulation (EU) 2024/2690, Annex, point 5.1.3 (Article 21(2), point (d), of Directive (EU) 2022/2555) | Gap | — | EU coordinated risk assessments (Article 22(1)) are not part of the selection criteria. |
| NIS2-IR2690-5.1.4 | Implementing Regulation (EU) 2024/2690, Annex, point 5.1.4 (Article 21(2), point (d), of Directive (EU) 2022/2555) | Partial | [Policy 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis); [Policy 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis); [Policy 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis); [Policy 33 §4.2](/sbd-toe/assets/policies/policy-contratacao-segura#42-cláusulas-adicionais-por-nível-de-risco); [Policy 33 §4.2](/sbd-toe/assets/policies/policy-contratacao-segura#42-cláusulas-adicionais-por-nível-de-risco); [Policy 33 §4.2](/sbd-toe/assets/policies/policy-contratacao-segura#42-cláusulas-adicionais-por-nível-de-risco); [Policy 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding) | Universal clauses (confidentiality, notification ≤ 24 h, subcontracting, termination) and per-level clauses; background checks on supplier staff and, at L1/L2, right of audit and (L1) vulnerability handling are missing — even though the baseline always asks for “right of audit”. |
| NIS2-IR2690-6.1.1 | Implementing Regulation (EU) 2024/2690, Annex, point 6.1.1 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Partial | `DEP-006`; [Policy 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence); `GOV-007` | Acquisition of libraries and contracting of suppliers with access are managed by risk; there is no process for the acquisition of ICT products and services (hardware, off-the-shelf software, services) for critical components throughout the lifecycle. |
| NIS2-IR2690-6.1.2 | Implementing Regulation (EU) 2024/2690, Annex, point 6.1.2 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Partial | [Policy 33 §4.2](/sbd-toe/assets/policies/policy-contratacao-segura#42-cláusulas-adicionais-por-nível-de-risco); [💽 Licensing contracts (external software)](/sbd-toe/sbd-manual/governanca-contratacao/addon/clausulas-contratuais#-contratos-de-licenciamento-software-externo); `DEP-001` | Requires vulnerability remediation and SBOM (L3) from suppliers; requirements for security updates throughout the entire lifetime, information on hardware components, secure configuration by default and assurance of compliance are missing. |
| NIS2-IR2690-6.2.3 | Implementing Regulation (EU) 2024/2690, Annex, point 6.2.3 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Partial | [Policy 33 §2](/sbd-toe/assets/policies/policy-contratacao-segura#2-âmbito-e-obrigatoriedade); [Policy 33 §3.2](/sbd-toe/assets/policies/policy-contratacao-segura#32-resultado-da-due-diligence) | Outsourced development falls within the scope of Policy 33, but it inherits the acquisition gaps (6.1). |
| NIS2-IR2690-6.3.2 | Implementing Regulation (EU) 2024/2690, Annex, point 6.3.2 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Partial | `IAC-003`; [Policy 21 §3](/sbd-toe/assets/policies/policy-iac-seguro#3-princípios-de-iac-seguro); `IAC-012`; `CFG-007` | Secure configurations enforced on new systems via the pipeline; on systems in operation, drift detection is mandatory only at L2/L3 (IaC) and L3 (application). |
| NIS2-IR2690-6.3.3 | Implementing Regulation (EU) 2024/2690, Annex, point 6.3.3 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Partial | [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `IAC-013`; `CNT-010` | Review of configurations after a significant incident prescribed; the formal review of modules remains L3 only. |
| NIS2-IR2690-6.4.2 | Implementing Regulation (EU) 2024/2690, Annex, point 6.4.2 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Partial | `DPL-001`; `DPL-003`; `DPL-007`; `IAC-007`; [Policy 26 §2](/sbd-toe/assets/policies/policy-aprovacao-release#2-âmbito-e-obrigatoriedade) | Approval and gates before production at all levels (DPL-001/003); validation in staging and approved plan only at L2/L3; impact assessment not explicit. |
| NIS2-IR2690-6.6.1 | Implementing Regulation (EU) 2024/2690, Annex, point 6.6.1 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Partial | `DEP-007`; `DEP-003`; `DEP-005`; `CNT-010`; [Policy 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção); [Policy 24 §6](/sbd-toe/assets/policies/policy-golden-base-images#6-sla-de-patching) | Patching of dependencies and images with SLA, verified integrity and compensating controls is prescribed; patch management of the entity's operating systems and equipment is out of scope of the Manual (entity-wide security). |
| NIS2-IR2690-6.7.2 | Implementing Regulation (EU) 2024/2690, Annex, point 6.7.2 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Partial | `ARC-001`; `ARC-002`; `ARC-006`; `ARC-008`; `INT-004`; `INT-006` | Zones, exposure, isolation and secure protocols covered; missing: only authorised devices on the network, provider connections authorised and time-limited, restriction of security management systems, transition plans for next-generation protocols, email security standards, and DNS and routing good practices. |
| NIS2-IR2690-6.8.2 | Implementing Regulation (EU) 2024/2690, Annex, point 6.8.2 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Partial | `ARC-006`; `CFG-002`; `IAC-002`; `ARC-011`; `CNT-012`; [📝 Description](/sbd-toe/sbd-manual/arquitetura-segura/addon/diagramas-referencia#-descrição-2) | Separation of production/development and domain isolation exist; DMZ only in an L3 reference diagram; network segregation between environments only at L3 (ARC-011); separating the administration network and channels from operational traffic, and production backups, is missing. |
| NIS2-IR2690-6.9.1 | Implementing Regulation (EU) 2024/2690, Annex, point 6.9.1 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Partial | `FIL-007`; `IDE-001`; `CNT-001`; `CNT-009`; `DEP-005` | Controls unauthorised software in the chain (images, libraries, tools) and file scanning (L2/L3); does not cover anti-malware protection of systems in operation. |
| NIS2-IR2690-6.9.2 | Implementing Regulation (EU) 2024/2690, Annex, point 6.9.2 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Partial | `FIL-007` | No detection and response software (EDR) on systems; malware detection is limited to uploaded files (L2/L3). |
| NIS2-IR2690-6.10.4 | Implementing Regulation (EU) 2024/2690, Annex, point 6.10.4 (Article 21(2), point (e), of Directive (EU) 2022/2555) | Partial | `DEP-010` | Periodic review of the sources of vulnerability information is mandatory at L2/L3 (DEP-010); not at L1. |
| NIS2-IR2690-8.1.1 | Implementing Regulation (EU) 2024/2690, Annex, point 8.1.1 (Article 21(2), point (g), of Directive (EU) 2022/2555) | Partial | [Policy 37 §2](/sbd-toe/assets/policies/policy-formacao-seguranca#2-âmbito-e-obrigatoriedade); `TRN-007`; [Policy 37 §4.1](/sbd-toe/assets/policies/policy-formacao-seguranca#41-matriz-de-trilhos-por-perfil-e-nível-de-risco) | Awareness for technical staff and third parties with access; non-technical employees, management bodies (only “Executive awareness”) and explicit cyber hygiene practices are missing. |
| NIS2-IR2690-8.1.2 | Implementing Regulation (EU) 2024/2690, Annex, point 8.1.2 (Article 21(2), point (g), of Directive (EU) 2022/2555) | Partial | `TRN-002`; `TRN-001` | Onboarding and renewal for technical roles; there is no scheduled awareness programme for all staff. |
| NIS2-IR2690-8.2.4 | Implementing Regulation (EU) 2024/2690, Annex, point 8.2.4 (Article 21(2), point (g), of Directive (EU) 2022/2555) | Partial | `TRN-002` | Onboarding before autonomous work; there is no explicit training trigger on moving to a new role with security requirements. |
| NIS2-IR2690-10.1.1 | Implementing Regulation (EU) 2024/2690, Annex, point 10.1.1 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Partial | `TRN-002`; [Policy 33 §5.1](/sbd-toe/assets/policies/policy-contratacao-segura#51-processo-de-onboarding); `TRN-007` | Responsibilities communicated at onboarding and individual undertaking for contractors; no statement of responsibilities for employees in general. |
| NIS2-IR2690-10.1.2 | Implementing Regulation (EU) 2024/2690, Annex, point 10.1.2 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Partial | `TRN-002`; `ACC-004` | General cyber hygiene and hiring of qualified staff not addressed. |
| NIS2-IR2690-10.3.1 | Implementing Regulation (EU) 2024/2690, Annex, point 10.3.1 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Partial | [Policy 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis); [Policy 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding) | Confidentiality and offboarding for suppliers/contractors; post-termination duties of employees are an employment-law matter out of scope. |
| NIS2-IR2690-10.3.2 | Implementing Regulation (EU) 2024/2690, Annex, point 10.3.2 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Partial | [Policy 33 §5.1](/sbd-toe/assets/policies/policy-contratacao-segura#51-processo-de-onboarding); [Policy 33 §4.1](/sbd-toe/assets/policies/policy-contratacao-segura#41-cláusulas-universais-todos-os-níveis) | Confidentiality terms for contractors; employment contracts out of scope. |
| NIS2-IR2690-11.1.1 | Implementing Regulation (EU) 2024/2690, Annex, point 11.1.1 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Partial | `ACC-001`; `ACC-005` | Logical access control prescribed; physical access is out of scope. |
| NIS2-IR2690-11.1.3 | Implementing Regulation (EU) 2024/2690, Annex, point 11.1.3 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Partial | [Policy 32 §4.6](/sbd-toe/assets/policies/policy-irp#46-post-mortem); `ACC-007` | Review of the access model after a significant incident prescribed; the periodic review of the permission model (ACC-007) remains L2/L3 only. |
| NIS2-IR2690-11.4.2 | Implementing Regulation (EU) 2024/2690, Annex, point 11.4.2 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Gap | — | Exclusive use of administration systems, logical separation from application software and dedicated protection of access to them are not required. |
| NIS2-IR2690-11.6.3 | Implementing Regulation (EU) 2024/2690, Annex, point 11.6.3 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Partial | `AUT-007`; `AUT-001`; `AUT-012`; `AUT-013` | Passwordless and FIDO2 methods are prescribed (AUT-001, AUT-012); federation and MFA remain L2/L3 only in the core. |
| NIS2-IR2690-11.6.4 | Implementing Regulation (EU) 2024/2690, Annex, point 11.6.4 (Article 21(2), points (i) and (j), of Directive (EU) 2022/2555) | Gap | — | There is no periodic review of authentication procedures and technologies. |
| NIS2-IR2690-12.2.1 | Implementing Regulation (EU) 2024/2690, Annex, point 12.2.1 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Gap | `PRI-002` | There is no asset handling policy (use, storage, transport, secure disposal); only retention/erasure of personal data (PRI-002, L2/L3). |
| NIS2-IR2690-12.2.2 | Implementing Regulation (EU) 2024/2690, Annex, point 12.2.2 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Gap | [Policy 33 §7.1](/sbd-toe/assets/policies/policy-contratacao-segura#71-checklist-de-offboarding) | No rules for the asset lifecycle, transport and secure destruction; data disposal appears only in supplier offboarding. |
| NIS2-IR2690-12.2.3 | Implementing Regulation (EU) 2024/2690, Annex, point 12.2.3 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Gap | — | No policy to review. |

### Out of scope (43) {#fora-de-ambito}

Obligations that the Manual declares out of scope, with the reason.

| Obligation | Reference | Reason |
|---|---|---|
| NIS2-3-4-a_d | Article 3(4), first subparagraph, points (a) to (d) | Administrative relationship with the competent authority/ENISA (registration, notification of identification data, supervision or penalty regime); legal-administrative plane, not security engineering. |
| NIS2-3-4-2par | Article 3(4), second subparagraph | Administrative relationship with the competent authority/ENISA (registration, notification of identification data, supervision or penalty regime); legal-administrative plane, not security engineering. |
| NIS2-26-3 | Article 26(3) | Designation of a representative in the Union: a legal obligation of establishment, not of engineering. |
| NIS2-27-2 | Article 27(2) | Administrative relationship with the competent authority/ENISA (registration, notification of identification data, supervision or penalty regime); legal-administrative plane, not security engineering. |
| NIS2-27-3 | Article 27(3) | Administrative relationship with the competent authority/ENISA (registration, notification of identification data, supervision or penalty regime); legal-administrative plane, not security engineering. |
| NIS2-28-1 | Article 28(1) | Specific functional duty of TLD name registries and entities providing domain name registration services (content of and access to the registration database); it is a business requirement of the service, not a security engineering practice that a generic SbD manual should prescribe. |
| NIS2-28-2 | Article 28(2) | Specific functional duty of TLD name registries and entities providing domain name registration services (content of and access to the registration database); it is a business requirement of the service, not a security engineering practice that a generic SbD manual should prescribe. |
| NIS2-28-3 | Article 28(3) | Specific functional duty of TLD name registries and entities providing domain name registration services (content of and access to the registration database); it is a business requirement of the service, not a security engineering practice that a generic SbD manual should prescribe. |
| NIS2-28-4 | Article 28(4) | Specific functional duty of TLD name registries and entities providing domain name registration services (content of and access to the registration database); it is a business requirement of the service, not a security engineering practice that a generic SbD manual should prescribe. |
| NIS2-28-5 | Article 28(5) | Specific functional duty of TLD name registries and entities providing domain name registration services (content of and access to the registration database); it is a business requirement of the service, not a security engineering practice that a generic SbD manual should prescribe. |
| NIS2-28-6 | Article 28(6) | Specific functional duty of TLD name registries and entities providing domain name registration services (content of and access to the registration database); it is a business requirement of the service, not a security engineering practice that a generic SbD manual should prescribe. |
| NIS2-29-4 | Article 29(4) | Administrative relationship with the competent authority/ENISA (registration, notification of identification data, supervision or penalty regime); legal-administrative plane, not security engineering. |
| NIS2-30-1 | Article 30(1), point (a) | An option (voluntary notification), not a duty; Policy 32 does not prevent it. |
| NIS2-32-2-2par | Article 32(2), third subparagraph; Article 33(2), third subparagraph | Administrative relationship with the competent authority/ENISA (registration, notification of identification data, supervision or penalty regime); legal-administrative plane, not security engineering. |
| NIS2-32-6 | Article 32(6) | Administrative relationship with the competent authority/ENISA (registration, notification of identification data, supervision or penalty regime); legal-administrative plane, not security engineering. |
| NIS2-34-4_5 | Article 34(4) and (5) | Administrative relationship with the competent authority/ENISA (registration, notification of identification data, supervision or penalty regime); legal-administrative plane, not security engineering. |
| NIS2-IR2690-art1 | Implementing Regulation (EU) 2024/2690, Article 1 | Provision on personal scope; it does not create an engineering duty. |
| NIS2-IR2690-4.3.1 | Implementing Regulation (EU) 2024/2690, Annex, point 4.3.1 (Article 21(2), point (c), of Directive (EU) 2022/2555) | Institutional crisis management (corporate BCM beyond software); the Manual's own NIS2 cross-check declares it outside (“institutional crisis management … outside the core manual”). The P1 war room of Policy 32 is incident response, not crisis management. |
| NIS2-IR2690-4.3.2 | Implementing Regulation (EU) 2024/2690, Annex, point 4.3.2 (Article 21(2), point (c), of Directive (EU) 2022/2555) | Institutional crisis management (corporate BCM beyond software); the Manual's own NIS2 cross-check declares it outside (“institutional crisis management … outside the core manual”). The P1 war room of Policy 32 is incident response, not crisis management. |
| NIS2-IR2690-4.3.4 | Implementing Regulation (EU) 2024/2690, Annex, point 4.3.4 (Article 21(2), point (c), of Directive (EU) 2022/2555) | Institutional crisis management (corporate BCM beyond software); the Manual's own NIS2 cross-check declares it outside (“institutional crisis management … outside the core manual”). The P1 war room of Policy 32 is incident response, not crisis management. |
| NIS2-IR2690-10.1.3 | Implementing Regulation (EU) 2024/2690, Annex, point 10.1.3 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Human resources management (background checks, disciplinary regime, staff assignment); outside the scope of a software security engineering manual. |
| NIS2-IR2690-10.2.1 | Implementing Regulation (EU) 2024/2690, Annex, point 10.2.1 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Human resources management (background checks, disciplinary regime, staff assignment); outside the scope of a software security engineering manual. |
| NIS2-IR2690-10.2.2 | Implementing Regulation (EU) 2024/2690, Annex, point 10.2.2 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Human resources management (background checks, disciplinary regime, staff assignment); outside the scope of a software security engineering manual. |
| NIS2-IR2690-10.2.3 | Implementing Regulation (EU) 2024/2690, Annex, point 10.2.3 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Human resources management (background checks, disciplinary regime, staff assignment); outside the scope of a software security engineering manual. |
| NIS2-IR2690-10.4.1 | Implementing Regulation (EU) 2024/2690, Annex, point 10.4.1 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Human resources management (background checks, disciplinary regime, staff assignment); outside the scope of a software security engineering manual. |
| NIS2-IR2690-10.4.2 | Implementing Regulation (EU) 2024/2690, Annex, point 10.4.2 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Human resources management (background checks, disciplinary regime, staff assignment); outside the scope of a software security engineering manual. |
| NIS2-IR2690-12.1.1 | Implementing Regulation (EU) 2024/2690, Annex, point 12.1.1 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Asset management for the entity as a whole (inventory and classification of all assets, infrastructure, equipment, licences) is out of scope: the Manual is application-centric. The inventory and classification of the application and its components (CLA-001, SBOM) give evidence for the part that concerns it. |
| NIS2-IR2690-12.1.2 | Implementing Regulation (EU) 2024/2690, Annex, point 12.1.2 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Asset management for the entity as a whole (inventory and classification of all assets, infrastructure, equipment, licences) is out of scope: the Manual is application-centric. The inventory and classification of the application and its components (CLA-001, SBOM) give evidence for the part that concerns it. |
| NIS2-IR2690-12.3.1 | Implementing Regulation (EU) 2024/2690, Annex, point 12.3.1 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Endpoint/workstation control (removable media, autorun, portable devices); IT operations outside the scope of a software security engineering manual. |
| NIS2-IR2690-12.3.2 | Implementing Regulation (EU) 2024/2690, Annex, point 12.3.2 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Endpoint/workstation control (removable media, autorun, portable devices); IT operations outside the scope of a software security engineering manual. |
| NIS2-IR2690-12.3.3 | Implementing Regulation (EU) 2024/2690, Annex, point 12.3.3 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Endpoint/workstation control (removable media, autorun, portable devices); IT operations outside the scope of a software security engineering manual. |
| NIS2-IR2690-12.4.1 | Implementing Regulation (EU) 2024/2690, Annex, point 12.4.1 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Asset management for the entity as a whole (inventory and classification of all assets, infrastructure, equipment, licences) is out of scope: the Manual is application-centric. The inventory and classification of the application and its components (CLA-001, SBOM) give evidence for the part that concerns it. |
| NIS2-IR2690-12.4.2 | Implementing Regulation (EU) 2024/2690, Annex, point 12.4.2 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Asset management for the entity as a whole (inventory and classification of all assets, infrastructure, equipment, licences) is out of scope: the Manual is application-centric. The inventory and classification of the application and its components (CLA-001, SBOM) give evidence for the part that concerns it. |
| NIS2-IR2690-12.4.3 | Implementing Regulation (EU) 2024/2690, Annex, point 12.4.3 (Article 21(2), point (i), of Directive (EU) 2022/2555) | Asset management for the entity as a whole (inventory and classification of all assets, infrastructure, equipment, licences) is out of scope: the Manual is application-centric. The inventory and classification of the application and its components (CLA-001, SBOM) give evidence for the part that concerns it. |
| NIS2-IR2690-13.1.1 | Implementing Regulation (EU) 2024/2690, Annex, point 13.1.1 (Article 21(2), points (c), (e) and (i), of Directive (EU) 2022/2555) | Physical and environmental security of premises (perimeters, power, air conditioning, physical access); outside the scope of a software security engineering manual. |
| NIS2-IR2690-13.1.2 | Implementing Regulation (EU) 2024/2690, Annex, point 13.1.2 (Article 21(2), points (c), (e) and (i), of Directive (EU) 2022/2555) | Physical and environmental security of premises (perimeters, power, air conditioning, physical access); outside the scope of a software security engineering manual. |
| NIS2-IR2690-13.1.3 | Implementing Regulation (EU) 2024/2690, Annex, point 13.1.3 (Article 21(2), points (c), (e) and (i), of Directive (EU) 2022/2555) | Physical and environmental security of premises (perimeters, power, air conditioning, physical access); outside the scope of a software security engineering manual. |
| NIS2-IR2690-13.2.1 | Implementing Regulation (EU) 2024/2690, Annex, point 13.2.1 (Article 21(2), points (c), (e) and (i), of Directive (EU) 2022/2555) | Physical and environmental security of premises (perimeters, power, air conditioning, physical access); outside the scope of a software security engineering manual. |
| NIS2-IR2690-13.2.2 | Implementing Regulation (EU) 2024/2690, Annex, point 13.2.2 (Article 21(2), points (c), (e) and (i), of Directive (EU) 2022/2555) | Physical and environmental security of premises (perimeters, power, air conditioning, physical access); outside the scope of a software security engineering manual. |
| NIS2-IR2690-13.2.3 | Implementing Regulation (EU) 2024/2690, Annex, point 13.2.3 (Article 21(2), points (c), (e) and (i), of Directive (EU) 2022/2555) | Physical and environmental security of premises (perimeters, power, air conditioning, physical access); outside the scope of a software security engineering manual. |
| NIS2-IR2690-13.3.1 | Implementing Regulation (EU) 2024/2690, Annex, point 13.3.1 (Article 21(2), points (c), (e) and (i), of Directive (EU) 2022/2555) | Physical and environmental security of premises (perimeters, power, air conditioning, physical access); outside the scope of a software security engineering manual. |
| NIS2-IR2690-13.3.2 | Implementing Regulation (EU) 2024/2690, Annex, point 13.3.2 (Article 21(2), points (c), (e) and (i), of Directive (EU) 2022/2555) | Physical and environmental security of premises (perimeters, power, air conditioning, physical access); outside the scope of a software security engineering manual. |
| NIS2-IR2690-13.3.3 | Implementing Regulation (EU) 2024/2690, Annex, point 13.3.3 (Article 21(2), points (c), (e) and (i), of Directive (EU) 2022/2555) | Physical and environmental security of premises (perimeters, power, air conditioning, physical access); outside the scope of a software security engineering manual. |
