---
id: requisitos-aplicaveis
title: "Applicable requirements — Product with digital elements placed on the market (CRA)"
description: "The Manual's requirements that apply under context CTX-CRA, by level and grade, with each floor that the regime elevates and its legal basis."
sidebar_position: 90
tags: [cross-check, cra, requisitos, overlay]
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
  - 002-cross-check-normativo/_matriz/cra.yaml
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/cra/90-requisitos-aplicaveis.md
  source_sha256: 5c81208b0612b596bc9540dcaa74c10f3d63e00d707088872477b8ced1037e6b
  source_commit: null
  target_sha256: 959ed04467be70fc534be01a8fd77f935a30154463fff4f0e8643ecb11d3801f
  engine: gen_reg_views
  prompt_sha256: null
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: []
  glossary_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
  translated_at: 2026-09-27T00:00:00Z
  stamped_at: 2026-09-27T00:00:00Z
  reviewed_by: null
---

# Applicable requirements: Product with digital elements placed on the market (CRA)

For context **CTX-CRA**, this page brings together the Manual's base selection per level and each **floor** that the regime elevates, with the obligation that grounds it. A context never lowers a minimum of the Manual.

## When it applies {#quando-se-aplica}

The application is, or is part of, a product with digital elements that the organisation places on the market; declared per application or product. Declared per application.

> Regulation (EU) 2024/2847, Article 2(1): “This Regulation applies to products with digital elements made available on the market, the intended purpose or reasonably foreseeable use of which includes a direct or indirect logical or physical data connection to a device or network.”

## Context floor list {#pisos}

| Floor | Target | Grade | Required floor | Scope | Legal basis | Justification of non-applicability |
|---|---|---|---|---|---|---|
| CTX-CRA-P01 | `DEP-002` | — | mandatory | Blocking on a known exploitable vulnerability at any level, in addition to the severity criterion: no known exploitable vulnerability when placed on the market. | Regulation (EU) 2024/2847, Annex I, Part I, point 2(a): “be made available on the market without known exploitable vulnerabilities” (CRA-AnxI-P1-2a) | not admitted |
| CTX-CRA-P02 | [Policy 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção) | — | mandatory | The “fix deferred” and “risk accepted” exceptions do not apply to known exploitable vulnerabilities of a CRA product at the time it is placed on the market. | Regulation (EU) 2024/2847, Annex I, Part I, point 2(a): “be made available on the market without known exploitable vulnerabilities” (CRA-AnxI-P1-2a) | not admitted |
| CTX-CRA-P03 | `DEP-006` | — | mandatory | — | Regulation (EU) 2024/2847, Article 13(5): “manufacturers shall exercise due diligence when integrating components sourced from third parties” (CRA-13-5) | not admitted |
| CTX-CRA-P04 | `GOV-015` | — | mandatory | Single point of contact, easily identifiable and included in the information and instructions to the user (Annex II); contact address also for vulnerabilities in third-party components. | Regulation (EU) 2024/2847, Annex I, Part II, points 5 and 6; Article 13(17); Annex II, point 2: “put in place and enforce a policy on coordinated vulnerability disclosure” (CRA-AnxI-P2-5, CRA-AnxI-P2-6, CRA-13-17, CRA-AnxII-2) | not admitted |

## Requirements added by the regime {#acrescentos}

These requirements only make sense under the regime, so they do not live in the Manual's catalogues; they are defined here, each with its legal basis.

| Requirement | Name | Acceptance criterion | Legal basis |
|---|---|---|---|
| `CTX-CRA-R01` | Support period determined, communicated and honoured | Support period determined per product with the criteria of Article 13(8) (expected use time, reasonable user expectations, nature and purpose of the product) and of at least five years, unless the expected use is shorter; rationale recorded in the technical documentation; end date of support stated in the information to the user; users notified of the end of support where technically feasible; each security update kept available for at least 10 years after issue or for the remainder of the support period, whichever is longer; public archives of earlier versions with a clear warning of the risks of use outside the support period. | Regulation (EU) 2024/2847, Article 13(8), (9), (11) and (19); Annex II, point 7; Annex VII, point 4: “the support period shall be at least five years” (CRA-13-8-p2, CRA-13-8-p3, CRA-13-8-p5, CRA-13-9, CRA-13-11, CRA-13-19-p2, CRA-AnxII-7, CRA-AnxVII-4) |
| `CTX-CRA-R02` | Distribution and mechanism of security updates at the user | Automatic security updates enabled by default where applicable, with a clear opt-out mechanism, notification of available updates and the option to postpone them temporarily; security updates disseminated without delay and free of charge (unless otherwise agreed with a business user for a tailor-made product), separate from functionality updates where technically feasible and accompanied by advisory messages on the action to be taken; secure and verifiable distribution (DST-003); instructions for installing updates and for turning off automatic updates in the information to the user. | Regulation (EU) 2024/2847, Annex I, Part I, point 2(c), and Part II, points 2, 7 and 8; Annex II, point 8(c) and (e): “ensure that, where security updates are available to address identified security issues, they are disseminated without delay” (CRA-AnxI-P1-2c, CRA-AnxI-P2-2, CRA-AnxI-P2-7, CRA-AnxI-P2-8, CRA-AnxII-8c, CRA-AnxII-8e) |
| `CTX-CRA-R03` | Public security advisories on fixed vulnerabilities | Once the security update is available, a public advisory on the fixed vulnerabilities, with a description, information allowing the affected product to be identified, impacts, severity and clear and accessible remediation information; delay of the disclosure only in duly justified, recorded cases, until users have had the possibility to apply the fix. | Regulation (EU) 2024/2847, Annex I, Part II, point 4: “once a security update has been made available, share and publicly disclose information about fixed vulnerabilities” (CRA-AnxI-P2-4) |
| `CTX-CRA-R04` | Reporting of component vulnerabilities to the maintainer | A vulnerability identified in a component integrated in the product (including an open-source component) reported to the person or entity manufacturing or maintaining it; a fix developed by the organisation shared with the person responsible for the component, where appropriate in a machine-readable format; the vulnerability handled in accordance with Part II of Annex I (DEP-007, DEP-010). | Regulation (EU) 2024/2847, Article 13(6): “report the vulnerability to the person or entity manufacturing or maintaining the component” (CRA-13-6-a, CRA-13-6-b) |
| `CTX-CRA-R05` | Severe incident criterion | An incident with an impact on the security of the product is assessed as severe when it affects or is capable of affecting the product's ability to protect the availability, authenticity, integrity or confidentiality of sensitive or important data or functions, or when it leads or is capable of leading to the introduction or execution of malicious code in the product or in a user's systems; the assessment is recorded and, if severe, follows the time limits and content of Policy 32 §6 and §6.1. | Regulation (EU) 2024/2847, Article 14(3) and (5): “an incident having an impact on the security of the product with digital elements shall be considered to be severe” (CRA-14-3) |

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
| `DEP-002` | SCA integrated into the pipeline with blocking by severity policy | ▲ | ▲ | ▲ | CTX-CRA-P01 |
| `DEP-003` | Dependency versions pinned and auditable | ✔ | ✔ | ✔ | — |
| `DEP-004` | Prohibition of dependencies introduced by manual copying | ✔ | ✔ | ✔ | — |
| `DEP-005` | Controlled registries and source repositories | — | ✔ | ✔ | — |
| `DEP-006` | Formal approval for the introduction of new dependencies | ▲ | ▲ | ▲ | CTX-CRA-P03 |
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
| `GOV-015` | Coordinated vulnerability disclosure with a published reporting channel | ▲ | ▲ | ▲ | CTX-CRA-P04 |
| `GOV-016` | Privileged and administration accounts of supporting systems | ✔ | ✔ | ✔ | — |
| `GOV-017` | Lifecycle of identities with access to systems | ✔ | ✔ | ✔ | — |
| `CTX-CRA-R01` | Support period determined, communicated and honoured | ▲ | ▲ | ▲ | — |
| `CTX-CRA-R02` | Distribution and mechanism of security updates at the user | ▲ | ▲ | ▲ | — |
| `CTX-CRA-R03` | Public security advisories on fixed vulnerabilities | ▲ | ▲ | ▲ | — |
| `CTX-CRA-R04` | Reporting of component vulnerabilities to the maintainer | ▲ | ▲ | ▲ | — |
| `CTX-CRA-R05` | Severe incident criterion | ▲ | ▲ | ▲ | — |

## Evidence map for the technical documentation {#mapa-evidencia}

Documentary obligations of the regime (CRA Annex VII) linked to the Manual artefacts that feed them. “Supports evidence”: the Manual produces the engineering evidence and drafting the document is for whoever places the product on the market. Gaps and what stays out of scope appear with the reason. The list comes from the Manual's coverage matrix.

| Obligation | Reference | Strength | How the Manual responds | Note |
|---|---|---|---|---|
| CRA-AnxVII-7 | Annex VII, point 7 | Out of scope | — | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-AnxVII-1 | Annex VII, point 1 | Supports evidence | [Policy 09 §4.1](/sbd-toe/assets/policies/policy-arquitetura-segura#41-arranque-de-projeto-ou-épico-significativo); [Ch. 11 US-09](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico) | — |
| CRA-AnxVII-2a | Annex VII, point 2(a) | Covers | `ARC-010`; `ARC-004`; [Policy 09 §4.1](/sbd-toe/assets/policies/policy-arquitetura-segura#41-arranque-de-projeto-ou-épico-significativo) | — |
| CRA-AnxVII-2b | Annex VII, point 2(b) | Covers | `DEP-001`; [Policy 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção); `DST-003`; `GOV-015`; `CTX-CRA-R02` | — |
| CRA-AnxVII-2c | Annex VII, point 2(c) | Covers | `CIC-001`; `CIC-005`; [Policy 20 §7](/sbd-toe/assets/policies/policy-release-seguro#7-rastreabilidade-ponta-a-ponta) | — |
| CRA-AnxVII-3 | Annex VII, point 3 | Supports evidence | `THR-001`; `THR-006` | The link to Annex I is drafted by the manufacturer in the technical documentation; the Manual provides the evidence (see the evidence map). |
| CRA-AnxVII-4 | Annex VII, point 4 | Covers | `CTX-CRA-R01` | — |
| CRA-AnxVII-5 | Annex VII, point 5 | Out of scope | — | List of harmonised standards/common specifications applied: conformity level. |
| CRA-AnxVII-6 | Annex VII, point 6 | Supports evidence | `TST-004`; [Policy 19 §5](/sbd-toe/assets/policies/policy-estrategia-testes#5-rastreabilidade-e-evidência-por-release) | The link to Annex I is drafted by the manufacturer in the technical documentation; the Manual provides the evidence (see the evidence map). |
| CRA-AnxVII-8 | Annex VII, point 8 | Covers | [Policy 11 §8.2](/sbd-toe/assets/policies/policy-sbom#82-prazos-de-retenção-mínimos); [Policy 11 §10](/sbd-toe/assets/policies/policy-sbom#10-responsabilidades) | — |

## Obligations of the regime by coverage strength {#forca}

Count of the regime's obligations in the coverage matrix (excluding those addressed to the authorities). The section [“What this Manual covers and what stays out”](#cobertura) lists them.

| Strength | Obligations |
|---|--:|
| Covers | 47 |
| Partial | 20 |
| Supports evidence | 20 |
| Gap | 7 |
| Out of scope | 97 |

## What this Manual covers and what stays out {#cobertura}

All the obligations of the regime, in the Manual's coverage matrix, in three categories: what the Manual **covers**, and in what form; the **declared gaps** (what it does not cover by omission); and what is **out of scope**, with the reason. No obligation is left in silence. The 46 obligations addressed to the authorities create no duty for the organisation and are not listed.

### Covers (67) {#cobre}

Strength “covers” or “supports evidence”. The form is the Manual's response: catalogue requirement, policy, section, floor or requirement added by the regime.

| Obligation | Reference | Strength | Form |
|---|---|---|---|
| CRA-12-1 | Article 12(1) | Supports evidence | `ARC-014`; `THR-008` |
| CRA-13-2 | Article 13(2) | Covers | `CLA-001`; `THR-001`; [Policy 08 §4.1](/sbd-toe/assets/policies/policy-threat-modeling#41-triggers-obrigatórios); [Policy 04 §1](/sbd-toe/assets/policies/policy-revisao-periodica-risco#1-objetivo) |
| CRA-13-5 | Article 13(5) | Covers | `DEP-006`; [Policy 10 §3.1](/sbd-toe/assets/policies/policy-dependencias#31-validação-obrigatória-por-dependência-nova); `GOV-007`; `DEP-002` |
| CRA-13-6-a | Article 13(6), first sentence | Covers | `CTX-CRA-R04` |
| CRA-13-6-b | Article 13(6), second sentence | Covers | `CTX-CRA-R04` |
| CRA-13-7 | Article 13(7) | Covers | `DEP-010`; `TST-003`; `GOV-009`; [Policy 10 §8](/sbd-toe/assets/policies/policy-dependencias#8-alertas-de-vulnerabilidades-em-produção) |
| CRA-13-8-p1 | Article 13(8), first subparagraph | Covers | [Policy 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); `DEP-007`; [Policy 12 §6](/sbd-toe/assets/policies/policy-excecoes-cve#6-prazos-máximos-e-reavaliação); `GOV-015`; `CTX-CRA-R01`; `CTX-CRA-R02`; `CTX-CRA-R03` |
| CRA-13-8-p2 | Article 13(8), second subparagraph | Covers | `CTX-CRA-R01` |
| CRA-13-8-p3 | Article 13(8), third subparagraph | Covers | `CTX-CRA-R01` |
| CRA-13-8-p5 | Article 13(8), fifth subparagraph | Covers | `CTX-CRA-R01` |
| CRA-13-8-p6 | Article 13(8), sixth subparagraph | Covers | [Policy 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção); [Policy 19 §4.2](/sbd-toe/assets/policies/policy-estrategia-testes#42-triagem-formal); `DEP-007`; `GOV-015`; `GOV-015` |
| CRA-13-9 | Article 13(9) | Covers | `CTX-CRA-R01` |
| CRA-13-11 | Article 13(11) | Covers | `CTX-CRA-R01` |
| CRA-13-12-p1 | Article 13(12), first subparagraph | Supports evidence | [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos); [Policy 11 §8.2](/sbd-toe/assets/policies/policy-sbom#82-prazos-de-retenção-mínimos) |
| CRA-13-12-p2 | Article 13(12), second subparagraph | Supports evidence | [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos); `TST-004` |
| CRA-13-15 | Article 13(15) | Supports evidence | [Ch. 11 US-09](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico); [Policy 20 §8](/sbd-toe/assets/policies/policy-release-seguro#8-registo-histórico-de-releases) |
| CRA-13-17 | Article 13(17) | Covers | `GOV-015` |
| CRA-13-19-p2 | Article 13(19), second subparagraph | Covers | `CTX-CRA-R01` |
| CRA-13-21 | Article 13(21) | Supports evidence | `DST-007`; `DPL-005` |
| CRA-14-1 | Article 14(1) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 12 §6](/sbd-toe/assets/policies/policy-excecoes-cve#6-prazos-máximos-e-reavaliação); [Ch. 05 US-11](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-11---alertas-sobre-vulnerabilidades-em-componentes-usados) |
| CRA-14-3 | Article 14(3) and (5) | Covers | `CTX-CRA-R05`; [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| CRA-14-4-c | Article 14(4), point (c) | Covers | [Policy 32 §6.1](/sbd-toe/assets/policies/policy-irp#61-critério-e-conteúdo-mínimo-por-regime); [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| CRA-14-8 | Article 14(8) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 32 §7](/sbd-toe/assets/policies/policy-irp#7-comunicação-durante-o-incidente); `DST-007` |
| CRA-17-2 | Article 17(2) | Supports evidence | [Policy 32 §9](/sbd-toe/assets/policies/policy-irp#9-responsabilidades) |
| CRA-23 | Article 23 | Supports evidence | [Policy 33 §8](/sbd-toe/assets/policies/policy-contratacao-segura#8-registo-e-rastreabilidade); [Policy 10 §3.2](/sbd-toe/assets/policies/policy-dependencias#32-registo-de-aprovação) |
| CRA-31-1 | Article 31(1) | Supports evidence | [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos); [Policy 09 §4.1](/sbd-toe/assets/policies/policy-arquitetura-segura#41-arranque-de-projeto-ou-épico-significativo); [Policy 11 §8.2](/sbd-toe/assets/policies/policy-sbom#82-prazos-de-retenção-mínimos) |
| CRA-31-2 | Article 31(2) | Supports evidence | `THR-006`; `ARC-010` |
| CRA-69-3 | Article 69(3) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| CRA-AnxI-P1-1 | Annex I, Part I, point 1 | Covers | `CLA-003`; `CLA-001`; `THR-001` |
| CRA-AnxI-P1-2a | Annex I, Part I, point 2(a) | Covers | `DEP-002`; [Policy 20 §5.1](/sbd-toe/assets/policies/policy-release-seguro#51-critérios-de-bloqueio-automático-no-go); `TST-005`; `TST-008`; [Policy 12 §8](/sbd-toe/assets/policies/policy-excecoes-cve#8-integração-no-pipeline) |
| CRA-AnxI-P1-2c | Annex I, Part I, point 2(c) | Covers | `CTX-CRA-R02` |
| CRA-AnxI-P1-2d | Annex I, Part I, point 2(d) | Covers | `ACC-001`; `ACC-003`; `AUT-001`; `AUT-010` |
| CRA-AnxI-P1-2e | Annex I, Part I, point 2(e) | Covers | `ENC-001`; `ENC-002`; `ENC-003` |
| CRA-AnxI-P1-2h | Annex I, Part I, point 2(h) | Covers | `API-004`; `FIL-001`; `OPS-015`; `DPL-005`; [Policy 32 §4.5](/sbd-toe/assets/policies/policy-irp#45-recuperação) |
| CRA-AnxI-P1-2j | Annex I, Part I, point 2(j) | Covers | `ARC-002`; `API-002`; `CNT-003`; [Policy 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura) |
| CRA-AnxI-P1-2k | Annex I, Part I, point 2(k) | Covers | `ARC-006`; `ACC-002`; `CNT-004`; `CNT-006` |
| CRA-AnxI-P2-1 | Annex I, Part II, point 1 | Covers | `DEP-001`; [Policy 11 §3.2](/sbd-toe/assets/policies/policy-sbom#32-conteúdo-mínimo-obrigatório); `DEP-010` |
| CRA-AnxI-P2-2 | Annex I, Part II, point 2 | Covers | [Policy 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); `DEP-007`; `TST-003`; `CTX-CRA-R02` |
| CRA-AnxI-P2-3 | Annex I, Part II, point 3 | Covers | `TST-001`; `TST-008`; [Policy 19 §5](/sbd-toe/assets/policies/policy-estrategia-testes#5-rastreabilidade-e-evidência-por-release) |
| CRA-AnxI-P2-4 | Annex I, Part II, point 4 | Covers | [Ch. 11 US-09](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico); `CTX-CRA-R03`; `GOV-015` |
| CRA-AnxI-P2-5 | Annex I, Part II, point 5 | Covers | `GOV-015` |
| CRA-AnxI-P2-6 | Annex I, Part II, point 6 | Covers | `GOV-015` |
| CRA-AnxI-P2-7 | Annex I, Part II, point 7 | Covers | `DST-003`; `CIC-007`; `DPL-002`; `CTX-CRA-R02`; `DST-003` |
| CRA-AnxI-P2-8 | Annex I, Part II, point 8 | Covers | `CTX-CRA-R02` |
| CRA-AnxII-2 | Annex II, point 2 | Covers | `GOV-015` |
| CRA-AnxII-3 | Annex II, point 3 | Supports evidence | [Ch. 11 US-09](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico) |
| CRA-AnxII-4 | Annex II, point 4 | Supports evidence | [Policy 09 §4.1](/sbd-toe/assets/policies/policy-arquitetura-segura#41-arranque-de-projeto-ou-épico-significativo); `ARC-001` |
| CRA-AnxII-5 | Annex II, point 5 | Supports evidence | [Ch. 03 US-13](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-13---derivação-de-abusemisuse-cases-para-o-backlog); `THR-001` |
| CRA-AnxII-7 | Annex II, point 7 | Covers | `CTX-CRA-R01` |
| CRA-AnxII-8c | Annex II, point 8(c) | Covers | `CTX-CRA-R02` |
| CRA-AnxII-8e | Annex II, point 8(e) | Covers | `CTX-CRA-R02` |
| CRA-AnxII-8f | Annex II, point 8(f) | Supports evidence | `DST-004`; `DEP-001` |
| CRA-AnxVII-1 | Annex VII, point 1 | Supports evidence | [Policy 09 §4.1](/sbd-toe/assets/policies/policy-arquitetura-segura#41-arranque-de-projeto-ou-épico-significativo); [Ch. 11 US-09](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico) |
| CRA-AnxVII-2a | Annex VII, point 2(a) | Covers | `ARC-010`; `ARC-004`; [Policy 09 §4.1](/sbd-toe/assets/policies/policy-arquitetura-segura#41-arranque-de-projeto-ou-épico-significativo) |
| CRA-AnxVII-2b | Annex VII, point 2(b) | Covers | `DEP-001`; [Policy 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção); `DST-003`; `GOV-015`; `CTX-CRA-R02` |
| CRA-AnxVII-2c | Annex VII, point 2(c) | Covers | `CIC-001`; `CIC-005`; [Policy 20 §7](/sbd-toe/assets/policies/policy-release-seguro#7-rastreabilidade-ponta-a-ponta) |
| CRA-AnxVII-3 | Annex VII, point 3 | Supports evidence | `THR-001`; `THR-006` |
| CRA-AnxVII-4 | Annex VII, point 4 | Covers | `CTX-CRA-R01` |
| CRA-AnxVII-6 | Annex VII, point 6 | Supports evidence | `TST-004`; [Policy 19 §5](/sbd-toe/assets/policies/policy-estrategia-testes#5-rastreabilidade-e-evidência-por-release) |
| CRA-AnxVII-8 | Annex VII, point 8 | Covers | [Policy 11 §8.2](/sbd-toe/assets/policies/policy-sbom#82-prazos-de-retenção-mínimos); [Policy 11 §10](/sbd-toe/assets/policies/policy-sbom#10-responsabilidades) |
| CRA-AnxVIII-PI-2 | Annex VIII, Part I (module A), point 2 | Supports evidence | [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) |
| CRA-AnxVIII-PI-3 | Annex VIII, Part I (module A), point 3 | Covers | [Policy 20 §5.1](/sbd-toe/assets/policies/policy-release-seguro#51-critérios-de-bloqueio-automático-no-go); [Policy 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); `CIC-001`; `GOV-015`; `CTX-CRA-R01`; `CTX-CRA-R02`; `CTX-CRA-R03` |
| CRA-AnxVIII-PII-7 | Annex VIII, Part II (module B), point 7, second subparagraph | Supports evidence | `ARC-009`; `CLA-006` |
| CRA-AnxVIII-PIII-2 | Annex VIII, Part III (module C), point 2 | Covers | [Policy 20 §6](/sbd-toe/assets/policies/policy-release-seguro#6-imutabilidade-do-artefacto); `DPL-002` |
| CRA-AnxVIII-PIV-2 | Annex VIII, Part IV (module H), point 2 | Supports evidence | `GOV-001`; `GOV-010` |
| CRA-AnxVIII-PIV-3.2 | Annex VIII, Part IV (module H), point 3.2 | Covers | `GOV-001`; `TST-001`; `TRN-001`; `GOV-011`; `GOV-015`; `CTX-CRA-R01`; `CTX-CRA-R02` |
| CRA-AnxVIII-PIV-3.4a3.5 | Annex VIII, Part IV (module H), points 3.4 and 3.5 | Supports evidence | `GOV-010` |

### Declared gap (27) {#lacuna}

Strength “partial” or “gap”: the Manual does not cover, or covers only in part, and says what is missing. Gaps pending an AppSec Core round are marked with the name of the round.

| Obligation | Reference | Strength | How the Manual responds | What is missing |
|---|---|---|---|---|
| CRA-4-3 | Article 4(3) and (4) | Gap | — | There is no rule for beta/pre-release channels of unfinished software: period limited to testing, visible indication of non-conformity and use exclusively for testing. |
| CRA-6 | Article 6 | Partial | [Policy 20 §5.1](/sbd-toe/assets/policies/policy-release-seguro#51-critérios-de-bloqueio-automático-no-go); `DEP-001`; `TST-001`; `GOV-015`; `CTX-CRA-R01`; `CTX-CRA-R02`; `CTX-CRA-R03` | Aggregate coverage of Parts I and II of Annex I is partial: the Manual does not prescribe reset to the original state (P1-2b) nor secure removal/transfer of data (P1-2m). Coordinated disclosure and contact (GOV-015), advisories (CTX-CRA-R03), the update mechanism and distribution (CTX-CRA-R02) and the support period (CTX-CRA-R01) are prescribed. |
| CRA-7-1 | Article 7(1) and (2) | Gap | — | The Manual's classification model (E/D/I axes → L1–L3, CLA-001) does not identify whether the product belongs to the categories of Annex III (classes I/II) or Annex IV, which determine the conformity assessment route. |
| CRA-13-1 | Article 13(1) | Partial | `REQ-001`; `CLA-003`; [Policy 20 §5.1](/sbd-toe/assets/policies/policy-release-seguro#51-critérios-de-bloqueio-automático-no-go); `CTX-CRA-R02` | Design/development in conformity with the whole of Part I of Annex I: missing are reset to the original state, secure removal and transfer of all data, minimisation of non-personal data and notification of corruptions/access to the user at L1. The product update mechanism is in CTX-CRA-R02. |
| CRA-13-3 | Article 13(3) | Partial | `THR-006`; [Policy 08 §4.2](/sbd-toe/assets/policies/policy-threat-modeling#42-cadência-periódica) | The Manual's risk assessment does not indicate, requirement by requirement, whether and how the points of Annex I, Part I, point (2) apply, nor how point (1) and Part II apply; it is not structured by intended purpose, reasonably foreseeable use, operational environment and period of use; the update is not anchored to the support period. |
| CRA-13-4 | Article 13(4) | Partial | [Policy 07 §9](/sbd-toe/assets/policies/policy-requisitos-seguranca#9-gestão-de-exceções-a-requisitos); `GOV-009` | There is formal justification of non-implemented requirements (exceptions), but not the integration of the risk assessment into the technical documentation (Annex VII) nor the justification per CRA essential requirement deemed not applicable. |
| CRA-13-10 | Article 13(10) | Gap | — | No supported-versions policy: does not provide for the option of fixing only the latest version nor the condition of free access to it. |
| CRA-13-13 | Article 13(13) | Partial | [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos); [Policy 11 §8.2](/sbd-toe/assets/policies/policy-sbom#82-prazos-de-retenção-mínimos); [Policy 08 §9.3](/sbd-toe/assets/policies/policy-threat-modeling#93-retenção) | The 10-year rule covers the SBOM and the evidence package; other elements of the technical documentation (historical versions of the threat model: 3 years; approval records: 1–3 years) are not covered; the EU declaration is out of scope. |
| CRA-13-14 | Article 13(14) | Partial | `ARC-009`; `CLA-006`; `REQ-005`; `THR-006` | Design/process changes trigger review, but tracking changes to the harmonised standards/common specifications that serve as reference for the declaration of conformity is missing. |
| CRA-13-18 | Article 13(18) | Partial | [Policy 20 §4.1](/sbd-toe/assets/policies/policy-release-seguro#41-critérios-obrigatórios) | Only the generic criterion “Security documentation updated” exists (recommended at L2, mandatory at L3); prescribing the content of Annex II, the recipient (user), the language and retention for 10 years/support period is missing. |
| CRA-14-2-a | Article 14(2), point (a) | Partial | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) | The 24 h deadline and the recording of the moment of awareness are prescribed; the minimum content is missing (indication of the Member States where the product has been made available). |
| CRA-14-2-b | Article 14(2), point (b) | Partial | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) | 72 h deadline prescribed; the minimum content is missing (general information about the product, nature of the exploit and of the vulnerability, corrective measures taken and to be taken by users, sensitivity of the information). |
| CRA-14-2-c | Article 14(2), point (c) | Partial | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) | Deadline of 14 days after the corrective measure prescribed (and the counting rule is correct in the note to Policy 32 §6); the content of the final report is missing (severity and impact, malicious actor, details of the update). |
| CRA-14-4-a | Article 14(4), point (a) | Partial | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) | 24 h deadline prescribed; indicating the suspicion of an unlawful/malicious act and the Member States is missing. |
| CRA-14-4-b | Article 14(4), point (b) | Partial | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) | 72 h deadline prescribed; the content is missing (nature, initial assessment, measures, sensitivity). |
| CRA-14-6 | Article 14(6) | Gap | — | The CRA row of Policy 32 §6 does not provide for the intermediate report at the request of the CSIRT (it exists only in the NIS2 row). |
| CRA-14-7 | Article 14(7) | Partial | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) | Names the CSIRT designated as coordinator and the single reporting platform, but not the determination rule (Member State of the main establishment and fallback rule for manufacturers outside the EU). |
| CRA-AnxI-P1-2b | Annex I, Part I, point 2(b) | Partial | `CFG-001`; [Policy 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura); `CNT-003` | Hardened configuration of the production environment and “fail secure” exist, but not a secure by default configuration of the product delivered to the user nor the possibility of resetting to the original state. |
| CRA-AnxI-P1-2f | Annex I, Part I, point 2(f) | Partial | `ENC-009`; `INT-005`; `CIC-007`; `DST-003`; `CFG-007`; `LOG-003` | Integrity of software (signing) and of messages covered at L2/L3; integrity of critical data and of configuration only at L3; reporting corruptions to the user is missing. |
| CRA-AnxI-P1-2g | Annex I, Part I, point 2(g) | Partial | `PRI-001` | Minimisation covers personal data only (PRI-001, from L1); the CRA covers «personal or other» data. |
| CRA-AnxI-P1-2i | Annex I, Part I, point 2(i) | Partial | `CNT-012`; `ARC-006` | Isolation and network policies contain lateral impact, but there is no requirement that the product's own functions do not degrade other devices/networks (e.g. limiting outbound traffic, retry storms). |
| CRA-AnxI-P1-2l | Annex I, Part I, point 2(l) | Partial | `LOG-001`; `OPS-001`; `OPS-002` | Logging and monitoring of internal activity prescribed; the opt-out option for the user and the guidance to make that security information available to the user are missing. |
| CRA-AnxI-P1-2m | Annex I, Part I, point 2(m) | Partial | `PRI-003` | Erasure and export on request cover only the personal data of a data subject (PRI-003, from L1); removal by the user of all data and settings, securely and permanently, and secure transfer to other products are missing. |
| CRA-AnxII-8a | Annex II, point 8(a) | Gap | — | Does not prescribe a guide for commissioning and secure use for the user (hardening guide); the criterion “Security documentation updated” of Policy 20 §4.1 does not define content. |
| CRA-AnxII-8b | Annex II, point 8(b) | Gap | — | There is no instruction to the user on how changes to the product affect the security of data. |
| CRA-AnxII-8d | Annex II, point 8(d) | Gap | — | There are no instructions for secure decommissioning and removal of data by the user (capability also missing, CRA-AnxI-P1-2m). |
| CRA-AnxII-9 | Annex II, point 9 | Partial | `DST-004` | The SBOM is attached to each release (L2/L3), but indicating to the user where to access it, when the manufacturer chooses to make it available, is not prescribed. |

### Out of scope (97) {#fora-de-ambito}

Obligations that the Manual declares out of scope, with the reason.

| Obligation | Reference | Reason |
|---|---|---|
| CRA-2-1 | Article 2(1) | Provision delimiting the scope/legal qualification of the product; creates no engineering duty. |
| CRA-2-2a7 | Article 2(2) to (8) | Provision delimiting the scope/legal qualification of the product; creates no engineering duty. |
| CRA-4-2 | Article 4(2) | Display of prototypes at trade fairs/demonstrations: market logistics, not engineering. |
| CRA-8-1 | Article 8(1) | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-11 | Article 11 | Interplay between legislative acts (GPSR); legal level. |
| CRA-12-2a4 | Article 12(2) to (4) | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-13-12-p3 | Article 13(12), third subparagraph | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-13-16 | Article 13(16) | Identification of the manufacturer on the product/packaging: labelling duty. |
| CRA-13-19-p1 | Article 13(19), first subparagraph | Commercial indication of the end-of-support date at the time of purchase; market level. |
| CRA-13-20 | Article 13(20) | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-13-22 | Article 13(22) | Relationship with market surveillance authorities/penalties regime; legal level, not engineering. |
| CRA-13-23 | Article 13(23) | Relationship with market surveillance authorities/penalties regime; legal level, not engineering. |
| CRA-15-1a2 | Article 15(1) and (2) | Option (voluntary notification), not duty; its absence is not a gap, although it is recommendable PSIRT practice. |
| CRA-18-1a2 | Article 18(1) and (2) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-18-3 | Article 18(3), introductory wording | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-18-3-a | Article 18(3), point (a) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-18-3-b | Article 18(3), point (b) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-18-3-c | Article 18(3), point (c) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-19-1 | Article 19(1) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-19-2-a | Article 19(2), point (a) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-19-2-b | Article 19(2), point (b) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-19-2-c | Article 19(2), point (c) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-19-2-d | Article 19(2), point (d) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-19-2-p2 | Article 19(2), second subparagraph | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-19-3-p1 | Article 19(3), first subparagraph | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-19-3-p2 | Article 19(3), second subparagraph | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-19-4 | Article 19(4) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-19-5-p1 | Article 19(5), first subparagraph | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-19-6 | Article 19(6) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-19-7 | Article 19(7) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-19-8 | Article 19(8) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-20-1 | Article 20(1) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-20-2-a | Article 20(2), point (a) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-20-2-b | Article 20(2), point (b) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-20-3 | Article 20(3) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-20-4-p1 | Article 20(4), first subparagraph | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-20-5 | Article 20(5) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-20-6 | Article 20(6) | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-19-5-p2 | Article 19(5), second subparagraph | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-20-4-p2 | Article 20(4), second subparagraph | Duty of another economic operator (importer/distributor/authorised representative), not of the manufacturer's engineering process. |
| CRA-21 | Article 21 | Legal requalification as manufacturer. |
| CRA-22 | Article 22 | Legal requalification as manufacturer. |
| CRA-24-1 | Article 24(1) | Duty of the open-source software steward; the Manual does not model that role. |
| CRA-24-2 | Article 24(2) | Duty of the open-source software steward; the Manual does not model that role. |
| CRA-52-3 | Article 52(3) | Duty of the open-source software steward; the Manual does not model that role. |
| CRA-24-3 | Article 24(3) | Duty of the open-source software steward; the Manual does not model that role. |
| CRA-28-1a2 | Article 28(1) and (2) | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-28-3 | Article 28(3) | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-28-4 | Article 28(4) | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-30-1 | Article 30(1) and (2) (and Article 29) | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-30-3a4 | Article 30(3) and (4) | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-31-3a4 | Article 31(3) and (4) | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-32-1 | Article 32(1) | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-32-2 | Article 32(2) | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-32-3 | Article 32(3) | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-32-4 | Article 32(4) | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-32-5 | Article 32(5) | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-33-5 | Article 33(5) | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-58 | Article 58 | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-AnxV | Annex V | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-AnxVI | Annex VI | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-AnxVII-7 | Annex VII, point 7 | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-AnxVIII-PI-4 | Annex VIII, Part I (module A), points 4.1 and 4.2 | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-AnxVIII-PI-5 | Annex VIII, Part I (module A), point 5 | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-AnxVIII-PII-3 | Annex VIII, Part II (module B), point 3 | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-AnxVIII-PII-10 | Annex VIII, Part II (module B), point 10 | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-AnxVIII-PII-11 | Annex VIII, Part II (module B), point 11 | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-AnxVIII-PIII-3 | Annex VIII, Part III (module C), points 3.1 and 3.2 | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-AnxVIII-PIII-4 | Annex VIII, Part III (module C), point 4 | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-AnxVIII-PIV-3.1 | Annex VIII, Part IV (module H), point 3.1 | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-AnxVIII-PIV-4.2 | Annex VIII, Part IV (module H), point 4.2 | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-AnxVIII-PIV-5 | Annex VIII, Part IV (module H), points 5.1 and 5.2 | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-AnxVIII-PIV-6 | Annex VIII, Part IV (module H), point 6 | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-AnxVIII-PIV-8 | Annex VIII, Part IV (module H), point 8 | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-AnxII-6 | Annex II, point 6 | Obligation at the formal conformity/market level (EU declaration, CE marking, notified bodies, authorities); outside the scope of a software security engineering manual — the Manual itself declares it out of scope (“does not replace”). |
| CRA-53 | Article 53 | Relationship with market surveillance authorities/penalties regime; legal level, not engineering. |
| CRA-54-1-4 | Article 54(1) (first subparagraph, second sentence) and (4) | Relationship with market surveillance authorities/penalties regime; legal level, not engineering. |
| CRA-56-3 | Article 56(3) (last sentence) | Relationship with market surveillance authorities/penalties regime; legal level, not engineering. |
| CRA-57-2-7 | Article 57(2) and (7) (last sentence) | Relationship with market surveillance authorities/penalties regime; legal level, not engineering. |
| CRA-64-2 | Article 64(2) | Relationship with market surveillance authorities/penalties regime; legal level, not engineering. |
| CRA-64-3 | Article 64(3) | Relationship with market surveillance authorities/penalties regime; legal level, not engineering. |
| CRA-64-4 | Article 64(4) | Relationship with market surveillance authorities/penalties regime; legal level, not engineering. |
| CRA-64-10 | Article 64(10) | Relationship with market surveillance authorities/penalties regime; legal level, not engineering. |
| CRA-65 | Article 65 | Relationship with market surveillance authorities/penalties regime; legal level, not engineering. |
| CRA-69-1 | Article 69(1) | Relationship with market surveillance authorities/penalties regime; legal level, not engineering. |
| CRA-69-2 | Article 69(2) | Transitional regime (application to earlier products only upon substantial modification); legal level. |
| CRA-71-2 | Article 71(2) | Dates of application; the Manual records them correctly (Article 14 since 11.9.2026) in Policy 32 §6. |
| CRA-AnxII-1 | Annex II, point 1 | Identification and contact details of the manufacturer: labelling. |
| CRA-AnxIII-I | Annex III, classe I | Lists/technical descriptions of the regulatory product categories (they determine the conformity route). |
| CRA-AnxIII-II | Annex III, classe II | Lists/technical descriptions of the regulatory product categories (they determine the conformity route). |
| CRA-AnxIV | Annex IV | Lists/technical descriptions of the regulatory product categories (they determine the conformity route). |
| CRA-R2025-2392-2 | Implementing Regulation (EU) 2025/2392, Articles 1 and 2 | Lists/technical descriptions of the regulatory product categories (they determine the conformity route). |
| CRA-R2025-2392-AnxI-CI | Implementing Regulation (EU) 2025/2392, Annex I, classe I | Lists/technical descriptions of the regulatory product categories (they determine the conformity route). |
| CRA-R2025-2392-AnxI-CII | Implementing Regulation (EU) 2025/2392, Annex I, classe II | Lists/technical descriptions of the regulatory product categories (they determine the conformity route). |
| CRA-R2025-2392-AnxII | Implementing Regulation (EU) 2025/2392, Annex II | Lists/technical descriptions of the regulatory product categories (they determine the conformity route). |
| CRA-R2025-1535-1 | Delegated Regulation (EU) 2025/1535, Article 1 | Provision delimiting the scope/legal qualification of the product; creates no engineering duty. |
| CRA-AnxVII-5 | Annex VII, point 5 | List of harmonised standards/common specifications applied: conformity level. |
