---
id: requisitos-aplicaveis
title: "Applicable requirements — High-risk AI system (AI Act)"
description: "Generated view: the Manual's requirements that apply under context CTX-AIA-RE, by level and grade, with each floor that the regime elevates and its legal basis."
sidebar_position: 90
tags: [cross-check, ai-act, requisitos, overlay, gerado]
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
  - 002-cross-check-normativo/_matriz/aiact.yaml
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/ai-act/90-requisitos-aplicaveis.md
  source_sha256: dd588e99c9f7aca1d91678d3d67d46ebbeee4b479ded0c207a13f061ee1618e3
  source_commit: null
  target_sha256: d25785c20e4f9b34d4e915d8f2dd9a005de5d490060294b8e681b204c3652aa5
  engine: gen_reg_views
  prompt_sha256: null
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: []
  glossary_sha256: 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
  translated_at: 2026-09-27T00:00:00Z
  stamped_at: 2026-09-27T00:00:00Z
  reviewed_by: null
---

# Applicable requirements: High-risk AI system (AI Act)

> **Generated page**, produced by `scripts/gen_reg_views.py` from the requirement catalogues and from `002-cross-check-normativo/_contextos-regulatorios.yaml`. It is not edited by hand: each requirement's catalogue is the canonical source, and this page is a view of the regulatory overlay.

For context **CTX-AIA-RE**, this page brings together the Manual's base selection per level and each **floor** that the regime elevates, with the obligation that grounds it. A context never lowers a minimum of the Manual.

## When it applies {#quando-se-aplica}

The AI system is high-risk under Article 6 (with the legal qualification attached to the declaration). A floor without a grade applies to high-risk systems; the ART50 grade can also be declared on its own, for systems covered only by Article 50. Risk level L3 is not the same as high-risk. Declared per application.

> Regulation (EU) 2024/1689, Article 6(1) to (3): “AI systems referred to in Annex III shall be considered to be high-risk”

## Grades {#graus}

- **ART50** — Covered by Article 50 (transparency) (declarable on its own). AI system covered by the transparency obligations of Article 50 (direct interaction with natural persons, synthetic content, emotion recognition or biometric categorisation, deep fakes), whether or not it is high-risk.

## Context floor list {#pisos}

| Floor | Target | Grade | Required floor | Scope | Legal basis | Justification of non-applicability |
|---|---|---|---|---|---|---|
| CTX-AIA-RE-P01 | `OPS-011` | — | mandatory | — | Regulation (EU) 2024/1689, Article 12(1) and (2): “High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.” (AIA-12-1, AIA-12-2) | not admitted |
| CTX-AIA-RE-P02 | `OPS-012` | — | mandatory | When the system includes AI agents with tool invocation. | Regulation (EU) 2024/1689, Article 12(1) and (2): “High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.” (AIA-12-1, AIA-12-2) | admitted |
| CTX-AIA-RE-P03 | `OPS-003` | — | mandatory; retention of automatically generated logs ≥ 6 months (“of at least six months”) | No exception below the statutory floor; applies to the logs under the control of the provider or of the deployer. | Regulation (EU) 2024/1689, Article 19(1), and Article 26(6): “the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months” (AIA-19-1, AIA-26-6) | not admitted |
| CTX-AIA-RE-P04 | `THR-008` | — | mandatory | — | Regulation (EU) 2024/1689, Article 15(5): “High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities.” (AIA-15-5) | not admitted |
| CTX-AIA-RE-P05 | `ARC-014` | — | mandatory | — | Regulation (EU) 2024/1689, Article 15(5): “High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities.” (AIA-15-5) | not admitted |
| CTX-AIA-RE-P06 | `DEP-011` | — | mandatory | — | Regulation (EU) 2024/1689, Article 15(5): “High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities.” (AIA-15-5) | not admitted |
| CTX-AIA-RE-P07 | `DEP-012` | — | mandatory | — | Regulation (EU) 2024/1689, Article 15(5): “High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities.” (AIA-15-5) | not admitted |
| CTX-AIA-RE-P08 | `ARC-014` | — | mandatory | Human oversight at any level, with an interface that lets the overseer understand the system's capabilities and limitations, detect anomalies, interpret the output, decide not to use or to override it and stop the system; measures proportionate to the risks, autonomy and context; the overseer is made aware of automation bias. | Regulation (EU) 2024/1689, Article 14(1) to (4): “can be effectively overseen by natural persons during the period in which they are in use” (AIA-14-1, AIA-14-2, AIA-14-3, AIA-14-4) | not admitted |
| CTX-AIA-RE-P09 | `THR-008` | ART50 | mandatory | Systems that generate or manipulate realistic images, video or audio, at any level: the threat model covers the reasonably foreseeable misuse of the generated content, and the safeguards are assessed with red-teaming and content-safety tests. | Regulation (EU) 2024/1689, Article 5(1), points (ba) and (bb), and (1a) (Regulation (EU) 2026/1744): “reasonable and adequate technical safety measures and other safeguards to reliably prevent that generation or manipulation” (AIA-5-1-b-A, AIA-5-1-b-B, AIA-5-1A) | admitted |
| CTX-AIA-RE-P10 | `ARC-014` | ART50 | mandatory | Systems that generate or manipulate realistic images, video or audio, at any level: content-safety filters and classifiers on input and output, and correction of observed or reported misuse. | Regulation (EU) 2024/1689, Article 5(1), points (ba) and (bb), and (1a) (Regulation (EU) 2026/1744): “reasonable and adequate technical safety measures and other safeguards to reliably prevent that generation or manipulation” (AIA-5-1-b-A, AIA-5-1-b-B, AIA-5-1A) | admitted |
| CTX-AIA-RE-P11 | `ARC-009` | — | mandatory | At any level, the significant-change threshold distinguishes predetermined changes (declared beforehand in the technical documentation, e.g. continuous learning within limits) from substantial modifications; each change is classified and the classification recorded; a substantial modification is flagged for a new conformity assessment; the logs allow risk situations and substantial modifications to be identified. | Regulation (EU) 2024/1689, Article 43(4), Article 12(2), and Annex IV, point 2(f): “shall undergo a new conformity assessment procedure in the event of a substantial modification” (AIA-43-4, AIA-AnxIV-2-f, AIA-12-2) | not admitted |

> **ART50.** The ART50 grade carries the floor CTX-AIA-RE-P09 and the floor CTX-AIA-RE-P10 (content-safety safeguards in generators of realistic images, video or audio, Article 5(1a)) and the additions CTX-AIA-RE-R01 (informing) and R02 (marking synthetic content).

## Requirements added by the regime {#acrescentos}

These requirements only make sense under the regime, so they do not live in the Manual's catalogues; they are defined here, each with its legal basis.

| Requirement | Name | Acceptance criterion | Legal basis |
|---|---|---|---|
| `CTX-AIA-RE-R01` | Informing people that they are interacting with AI | People who interact directly with the system are informed that they are interacting with an AI system, unless this is obvious from the context; people exposed to emotion recognition or biometric categorisation are informed of that operation; image, audio or video content that constitutes a deep fake is disclosed as generated or manipulated. The information is clear and distinguishable, given at the latest at the first interaction or exposure, and meets the accessibility requirements; the presence of the notice is verified in testing. | Regulation (EU) 2024/1689, Article 50(1), (3), (4) (first subparagraph) and (5): “in a clear and distinguishable manner at the latest at the time of the first interaction or exposure” (AIA-50-1, AIA-50-3, AIA-50-4-a, AIA-50-5) |
| `CTX-AIA-RE-R02` | Marking of synthetic content | The audio, image, video or text outputs generated or manipulated by the system are marked in a machine-readable format and detectable as artificial (e.g. provenance metadata, content credentials, watermarking), with a solution that is effective, interoperable and robust as far as technically feasible; the marking is verified in testing and is not stripped by later pipeline steps; the exceptions of Article 50(2) (assistive function for standard editing, no substantial alteration of the input data) are recorded. | Regulation (EU) 2024/1689, Article 50(2), and Article 111(4): “are marked in a machine-readable format and detectable as artificially generated or manipulated” (AIA-50-2, AIA-111-4) |
| `CTX-AIA-RE-R03` | Informing and explaining to affected persons | When an Annex III high-risk AI system supports decisions about natural persons: the persons are informed that they are subject to its use; the application records, per decision, the system's output and the main elements that determined it (OPS-011), so that it can give the affected person clear and meaningful explanations of the role of the system and the main elements of the decision. When the decision is solely automated and personal data are involved, CTX-RGPD-R05 also applies. | Regulation (EU) 2024/1689, Article 26(11), and Article 86(1): “clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken” (AIA-26-11, AIA-86-1) |
| `CTX-AIA-RE-R04` | Post-market monitoring plan | When the organisation is the provider: a post-market monitoring plan per system, part of the technical documentation (Annex IV, point 9), naming the signals collected in production (OPS-011) and those provided by deployers, the performance criteria against which they are analysed, the cadence and owner of the analysis, and the triggers for corrective action (rollback, reclassification, threat model review, serious incident notification); the analysis is active and systematic over the lifetime and includes, where relevant, the interaction with other AI systems. Model drift metrics are pending the AppSec Core AISVS/SAIF round. | Regulation (EU) 2024/1689, Article 72(1) to (3), and Annex IV, point 9: “The post-market monitoring system shall be based on a post-market monitoring plan” (AIA-72-1, AIA-72-2, AIA-72-3, AIA-AnxIV-9) |

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
| `THR-008` | Threat modelling extended to systems with AI/ML components | ▲ | ▲ | ▲ | CTX-AIA-RE-P04 |
| `ARC-001` | Trust zones identified and documented | ✔ | ✔ | ✔ | — |
| `ARC-002` | External exposure minimised and justified | ✔ | ✔ | ✔ | — |
| `ARC-003` | Security-focused architecture review | — | ✔ | ✔ | — |
| `ARC-004` | Architecture decisions documented | — | ✔ | ✔ | — |
| `ARC-005` | Threat modelling integrated into critical flows | — | ✔ | ✔ | — |
| `ARC-006` | Technical isolation controls between sensitive domains | ✔ | ✔ | ✔ | — |
| `ARC-007` | Reusable and approved architecture patterns | — | ✔ | ✔ | — |
| `ARC-008` | Data flows between trust zones protected | ✔ | ✔ | ✔ | — |
| `ARC-009` | Significant changes trigger a new review | ▲ | ▲ | ▲ | CTX-AIA-RE-P11 |
| `ARC-010` | Architecture diagrams versioned and accessible | ✔ | ✔ | ✔ | — |
| `ARC-011` | Logical and physical segmentation between environments | — | — | ✔ | — |
| `ARC-012` | Formal approval criteria for high-risk applications | — | — | ✔ | — |
| `ARC-013` | Automatic topology validation in CI/CD or as code | — | — | ✔ | — |
| `ARC-014` | Architectural patterns specific to systems with AI/ML components | ▲ | ▲ | ▲ | CTX-AIA-RE-P05, CTX-AIA-RE-P08 |
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
| `DEP-011` | Inventory and provenance of AI/ML dependencies | ▲ | ▲ | ▲ | CTX-AIA-RE-P06 |
| `DEP-012` | AI BOM generated per build in a standardised format | ▲ | ▲ | ▲ | CTX-AIA-RE-P07 |
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
| `OPS-003` | Log retention in accordance with policy and regulatory requirements | ▲ | ▲ | ▲ | CTX-AIA-RE-P03 |
| `OPS-004` | Centralisation of logs in a SIEM system or equivalent | — | ✔ | ✔ | — |
| `OPS-005` | Automatic alerts for critical security events | — | ✔ | ✔ | — |
| `OPS-006` | Alert response SLA defined and measured | — | ✔ | ✔ | — |
| `OPS-007` | Integration with a formal incident response process | — | ✔ | ✔ | — |
| `OPS-008` | Correlation of events across multiple sources | — | — | ✔ | — |
| `OPS-009` | Behavioural detection and baseline of normal activity | — | — | ✔ | — |
| `OPS-010` | Monitoring effectiveness metrics measured and reviewed | — | — | ✔ | — |
| `OPS-011` | Dedicated observability for AI/ML components in production | ▲ | ▲ | ▲ | CTX-AIA-RE-P01 |
| `OPS-012` | Complete audit per AI agent tool invocation | ▲ | ▲ | ▲ | CTX-AIA-RE-P02 |
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
| `GOV-015` | Coordinated vulnerability disclosure with a published reporting channel | ✔ | ✔ | ✔ | — |
| `GOV-016` | Privileged and administration accounts of supporting systems | ✔ | ✔ | ✔ | — |
| `GOV-017` | Lifecycle of identities with access to systems | ✔ | ✔ | ✔ | — |
| `CTX-AIA-RE-R03` | Informing and explaining to affected persons | ▲ | ▲ | ▲ | — |
| `CTX-AIA-RE-R04` | Post-market monitoring plan | ▲ | ▲ | ▲ | — |

## Requirement list — ART50 {#lista-art50}

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
| `THR-008` | Threat modelling extended to systems with AI/ML components | ▲ | ▲ | ▲ | CTX-AIA-RE-P09 |
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
| `ARC-014` | Architectural patterns specific to systems with AI/ML components | ▲ | ▲ | ▲ | CTX-AIA-RE-P10 |
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
| `GOV-015` | Coordinated vulnerability disclosure with a published reporting channel | ✔ | ✔ | ✔ | — |
| `GOV-016` | Privileged and administration accounts of supporting systems | ✔ | ✔ | ✔ | — |
| `GOV-017` | Lifecycle of identities with access to systems | ✔ | ✔ | ✔ | — |
| `CTX-AIA-RE-R01` | Informing people that they are interacting with AI | ▲ | ▲ | ▲ | — |
| `CTX-AIA-RE-R02` | Marking of synthetic content | ▲ | ▲ | ▲ | — |

## Evidence map for the technical documentation {#mapa-evidencia}

Documentary obligations of the regime (AI Act Article 11, Annex IV and Article 13) linked to the Manual artefacts that feed them. “Supports evidence”: the Manual produces the engineering evidence and drafting the document is for whoever places the product on the market. Gaps and what stays out of scope appear with the reason. Generated from the matrix `_matriz/aiact.yaml`.

| Obligation | Reference | Strength | How the Manual responds | Note |
|---|---|---|---|---|
| AIA-11-1-a | Article 11(1), first subparagraph | Supports evidence | `ARC-004`; `ARC-010`; `THR-006`; `DEP-012`; `TST-004` | Drafting the document is for the provider; the Manual provides the evidence (see the evidence map on the “Applicable requirements” page). |
| AIA-11-1-b | Article 11(1), second subparagraph | Supports evidence | `ARC-004`; `ARC-010`; `THR-006`; `DEP-012`; `TST-004` | The Annex IV points without an artefact are declared gaps in the evidence map. |
| AIA-AnxIV-1 | Annex IV, point 1 | Supports evidence | `ARC-001`; `ARC-010`; `ARC-014`; `DEP-011`; `DEP-012`; `DEP-013` | Declared gap: intended purpose (point (a)), forms of placing on the market (point (d)), hardware outside self-hosted inference (point (e)) and description of the interface for the deployer (point (g)). Out of scope: photographs and markings (point (f)). |
| AIA-AnxIV-2-a | Annex IV, point 2(a) | Supports evidence | `DEP-011`; `DEP-012`; `DEP-014`; `CIC-001` | The training methodology is out of scope (data governance, Article 10). |
| AIA-AnxIV-2-b | Annex IV, point 2(b) | Supports evidence | `ARC-004` | Declared gap: general logic, algorithms and what the system optimises. Assumptions about groups of persons are out of scope (bias). |
| AIA-AnxIV-2-c | Annex IV, point 2(c) | Supports evidence | `ARC-001`; `ARC-010`; `ARC-014` | Declared gap: computational resources for development, training, testing and validation. |
| AIA-AnxIV-2-d | Annex IV, point 2(d) | Out of scope | — | Governance of training data (Article 10) is out of scope by the lead's decision; DEP-011 and Policy 39 §4 give only incidental evidence. |
| AIA-AnxIV-2-e | Annex IV, point 2(e) | Supports evidence | `ARC-014`; `REQ-AGN-003` | Assessment of the oversight measures supported by the minimum oversight of ARC-014 (floor CTX-AIA-RE-P08). |
| AIA-AnxIV-2-f | Annex IV, point 2(f) | Covers | `ARC-009`; `DEP-013` | — |
| AIA-AnxIV-2-g | Annex IV, point 2(g) | Supports evidence | `TST-004`; `DPL-010`; `CIC-007` | **AppSec Core AISVS/SAIF round.** Accuracy and robustness metrics for non-agentic systems pending the AppSec Core AISVS/SAIF round; discriminatory impacts out of scope (bias). |
| AIA-AnxIV-2-h | Annex IV, point 2(h) | Covers | `REQ-001`; `THR-008`; `ARC-014` | — |
| AIA-AnxIV-3 | Annex IV, point 3 | Supports evidence | `OPS-011`; `ARC-014`; `THR-008` | Declared gap: performance capabilities and limitations and input data specifications. Accuracy by groups of persons is out of scope (bias). |
| AIA-AnxIV-4 | Annex IV, point 4 | Gap | — | **AppSec Core AISVS/SAIF round.** Declared gap: appropriateness of the performance metrics, pending the AppSec Core AISVS/SAIF round. |
| AIA-AnxIV-5 | Annex IV, point 5 | Out of scope | — | The risk management system of Article 9 is out of scope by the lead's decision. |
| AIA-AnxIV-6 | Annex IV, point 6 | Covers | `THR-006`; `ARC-010`; `CIC-005` | — |
| AIA-AnxIV-7 | Annex IV, point 7 | Out of scope | — | List of harmonised standards/common specifications applied: conformity level. |
| AIA-AnxIV-8 | Annex IV, point 8 | Out of scope | — | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-AnxIV-9 | Annex IV, point 9 | Covers | `CTX-AIA-RE-R04`; `OPS-011` | — |
| AIA-13-1 | Article 13(1) | Supports evidence | `ARC-014`; `OPS-011` | Interpretation of the output is supported by the minimum oversight of ARC-014 (floor CTX-AIA-RE-P08). |
| AIA-13-2 | Article 13(2) | Supports evidence | `DEP-013`; `DEP-014`; `ARC-014`; `OPS-011` | **AppSec Core AISVS/SAIF round.** Drafting the instructions is for the provider. Declared gap: intended purpose and interface description; the accuracy and robustness levels are pending the AppSec Core AISVS/SAIF round. |
| AIA-13-3 | Article 13(3) | Supports evidence | `DEP-013`; `DEP-014`; `ARC-014`; `OPS-011` | **AppSec Core AISVS/SAIF round.** Drafting the instructions is for the provider. Declared gap: intended purpose and interface description; the accuracy and robustness levels are pending the AppSec Core AISVS/SAIF round. |
| AIA-13-3-b-ii | Article 13(3), point (b)(ii) | Gap | — | **AppSec Core AISVS/SAIF round.** Declaration of the accuracy and robustness levels pending the AppSec Core AISVS/SAIF round. |
| AIA-13-3-e | Article 13(3), point (e) | Supports evidence | `DEP-013` | — |
| AIA-13-3-f | Article 13(3), point (f) | Supports evidence | `OPS-011` | — |

## Obligations of the regime by coverage strength {#forca}

Count of the obligations in the matrix `_matriz/aiact.yaml` (excluding those addressed to the authorities). The section [“What this Manual covers and what stays out”](#cobertura) lists them.

| Strength | Obligations |
|---|--:|
| Covers | 38 |
| Partial | 22 |
| Supports evidence | 49 |
| Gap | 4 |
| Out of scope | 132 |

## What this Manual covers and what stays out {#cobertura}

All the obligations of the matrix `_matriz/aiact.yaml` in three categories: what the Manual **covers**, and in what form; the **declared gaps** (what it does not cover by omission); and what is **out of scope**, with the reason. Generated from the matrix; no obligation is left in silence. The 15 obligations addressed to the authorities create no duty for the organisation and are not listed.

### Covers (87) {#cobre}

Strength “covers” or “supports evidence”. The form is the Manual's response: catalogue requirement, policy, section, floor or requirement added by the regime.

| Obligation | Reference | Strength | Form |
|---|---|---|---|
| AIA-4a-2 | Article 4a(2) | Supports evidence | `PRI-002`; `ACC-001` |
| AIA-5-1-a | Article 5(1), first subparagraph, point (a) | Supports evidence | [Ch. 02 US-17](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-17---incorporação-de-restrições-legais-normativas-e-contratuais) |
| AIA-5-1-b | Article 5(1), first subparagraph, point (b) | Supports evidence | [Ch. 02 US-17](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-17---incorporação-de-restrições-legais-normativas-e-contratuais) |
| AIA-5-1-b-A | Article 5(1), first subparagraph, point (b-A) | Covers | `THR-008`; `ARC-014` |
| AIA-5-1-b-B | Article 5(1), first subparagraph, point (b-B) | Covers | `THR-008`; `ARC-014` |
| AIA-5-1-e | Article 5(1), first subparagraph, point (e) | Supports evidence | [Ch. 02 US-17](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-17---incorporação-de-restrições-legais-normativas-e-contratuais); `DEP-011` |
| AIA-5-1A | Article 5(1a) | Covers | `THR-008`; `ARC-014`; [C5 - Continuous eval suites for agents in development and production](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites) |
| AIA-6-1 | Article 6(1), (1a), (1b) and (1c) | Covers | [When it applies (CTX-AIA-RE)](/sbd-toe/cross-check-normativo/ai-act/requisitos-aplicaveis#quando-se-aplica) |
| AIA-6-2-3 | Article 6(2) and (3) | Covers | [When it applies (CTX-AIA-RE)](/sbd-toe/cross-check-normativo/ai-act/requisitos-aplicaveis#quando-se-aplica) |
| AIA-6-4 | Article 6(4) | Supports evidence | `CLA-001`; `GOV-009` |
| AIA-11-1-a | Article 11(1), first subparagraph | Supports evidence | `ARC-004`; `ARC-010`; `THR-006`; `DEP-012`; `TST-004` |
| AIA-11-1-b | Article 11(1), second subparagraph | Supports evidence | `ARC-004`; `ARC-010`; `THR-006`; `DEP-012`; `TST-004` |
| AIA-AnxIV-1 | Annex IV, point 1 | Supports evidence | `ARC-001`; `ARC-010`; `ARC-014`; `DEP-011`; `DEP-012`; `DEP-013` |
| AIA-AnxIV-2-a | Annex IV, point 2(a) | Supports evidence | `DEP-011`; `DEP-012`; `DEP-014`; `CIC-001` |
| AIA-AnxIV-2-b | Annex IV, point 2(b) | Supports evidence | `ARC-004` |
| AIA-AnxIV-2-c | Annex IV, point 2(c) | Supports evidence | `ARC-001`; `ARC-010`; `ARC-014` |
| AIA-AnxIV-2-e | Annex IV, point 2(e) | Supports evidence | `ARC-014`; `REQ-AGN-003` |
| AIA-AnxIV-2-f | Annex IV, point 2(f) | Covers | `ARC-009`; `DEP-013` |
| AIA-AnxIV-2-g | Annex IV, point 2(g) | Supports evidence | `TST-004`; `DPL-010`; `CIC-007` |
| AIA-AnxIV-2-h | Annex IV, point 2(h) | Covers | `REQ-001`; `THR-008`; `ARC-014` |
| AIA-AnxIV-3 | Annex IV, point 3 | Supports evidence | `OPS-011`; `ARC-014`; `THR-008` |
| AIA-AnxIV-6 | Annex IV, point 6 | Covers | `THR-006`; `ARC-010`; `CIC-005` |
| AIA-AnxIV-9 | Annex IV, point 9 | Covers | `CTX-AIA-RE-R04`; `OPS-011` |
| AIA-12-1 | Article 12(1) | Covers | `LOG-001`; `OPS-011`; [Policy 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs) |
| AIA-12-2 | Article 12(2) | Covers | `ARC-009`; `OPS-011` |
| AIA-13-1 | Article 13(1) | Supports evidence | `ARC-014`; `OPS-011` |
| AIA-13-2 | Article 13(2) | Supports evidence | `DEP-013`; `DEP-014`; `ARC-014`; `OPS-011` |
| AIA-13-3 | Article 13(3) | Supports evidence | `DEP-013`; `DEP-014`; `ARC-014`; `OPS-011` |
| AIA-13-3-e | Article 13(3), point (e) | Supports evidence | `DEP-013` |
| AIA-13-3-f | Article 13(3), point (f) | Supports evidence | `OPS-011` |
| AIA-14-1 | Article 14(1) | Covers | `ARC-014`; `ARC-015`; [Ch. 04 US-15](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-15---identificação-e-governação-de-componentes-não-determinísticos) |
| AIA-14-2 | Article 14(2) | Covers | `ARC-014`; `ARC-015`; `REQ-AGN-004` |
| AIA-14-3 | Article 14(3) | Covers | `ARC-014`; `REQ-AGN-002`; [Policy 38 §2](/sbd-toe/assets/policies/policy-mandates-agentes#2-âmbito) |
| AIA-14-4 | Article 14(4) | Covers | `ARC-014`; `REQ-AGN-003`; `ARC-015`; [🎯 Scope and framing](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#-âmbito-e-enquadramento) |
| AIA-15-5 | Article 15(5) | Covers | `THR-008`; `ARC-014`; `DEP-011`; `OPS-014`; [1. The model weights are a critical asset](/sbd-toe/sbd-manual/containers-imagens/addon/self-hosted-inference#1-os-pesos-do-modelo-são-activo-crítico) |
| AIA-17-1-b | Article 17(1), point (b) | Supports evidence | `ARC-004`; `THR-006`; `REQ-005` |
| AIA-17-1-c | Article 17(1), point (c) | Supports evidence | `DEV-001`; `DEV-004`; `CIC-005` |
| AIA-17-1-i | Article 17(1), point (i) | Supports evidence | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| AIA-17-1-k | Article 17(1), point (k) | Supports evidence | `GOV-009`; [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) |
| AIA-17-1-m | Article 17(1), point (m) | Supports evidence | `GOV-001`; `GOV-002` |
| AIA-17-2 | Article 17(2) | Supports evidence | `CLA-001` |
| AIA-18-1 | Article 18(1) | Supports evidence | [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) |
| AIA-18-3 | Article 18(3) | Supports evidence | [Policy 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs) |
| AIA-19-1 | Article 19(1) | Covers | [Policy 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs); `OPS-003`; `LOG-005` |
| AIA-19-2 | Article 19(2) | Supports evidence | [Policy 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs) |
| AIA-21-2 | Article 21(2) | Supports evidence | `LOG-003`; `OPS-003` |
| AIA-25-2 | Article 25(2) | Supports evidence | `DEP-012`; [Policy 33 §10.6](/sbd-toe/assets/policies/policy-contratacao-segura#106-conformidade-regulatória-declarada) |
| AIA-26-6 | Article 26(6) | Covers | [Policy 18 §10.5](/sbd-toe/assets/policies/policy-gestao-segredos#105-telemetria-sob-controlo-do-deployer); [Policy 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs); `OPS-003` |
| AIA-26-9 | Article 26(9) | Supports evidence | [Ch. 03 US-08](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-08---aplicação-linddun-quando-existir-tratamento-de-dados-pessoais--novo) |
| AIA-26-11 | Article 26(11) | Covers | `CTX-AIA-RE-R03` |
| AIA-27-1 | Article 27(1) | Supports evidence | `THR-008`; [Ch. 03 US-08](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-08---aplicação-linddun-quando-existir-tratamento-de-dados-pessoais--novo) |
| AIA-27-2 | Article 27(2) | Supports evidence | `THR-006` |
| AIA-27-4 | Article 27(4) | Supports evidence | [Ch. 03 US-08](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-08---aplicação-linddun-quando-existir-tratamento-de-dados-pessoais--novo) |
| AIA-42-3 | Article 42(3) | Supports evidence | `THR-008`; `ARC-014` |
| AIA-43-4 | Article 43(4) | Covers | `ARC-009`; `CLA-006`; `DEP-013` |
| AIA-AnxVI | Annex VI | Supports evidence | `GOV-010`; `GOV-009` |
| AIA-AnxVII-4 | Annex VII, points 4.1-4.5, 4.7 | Supports evidence | `DEP-011`; `DEP-012` |
| AIA-50-1 | Article 50(1) | Covers | `CTX-AIA-RE-R01` |
| AIA-50-2 | Article 50(2) | Covers | `CTX-AIA-RE-R02` |
| AIA-50-3 | Article 50(3) | Covers | `CTX-AIA-RE-R01` |
| AIA-50-4-a | Article 50(4), first subparagraph | Covers | `CTX-AIA-RE-R01` |
| AIA-50-5 | Article 50(5) | Covers | `CTX-AIA-RE-R01` |
| AIA-53-1-a | Article 53(1), point (a) | Supports evidence | `DEP-012`; [Ch. 10 US-21](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-21---governação-do-uso-de-ia-em-testes-e-eval-suites-para-agentes) |
| AIA-53-1-b | Article 53(1), point (b) | Supports evidence | [Policy 33 §10.6](/sbd-toe/assets/policies/policy-contratacao-segura#106-conformidade-regulatória-declarada); `DEP-014` |
| AIA-55-1-b | Article 55(1), point (b) | Supports evidence | `THR-008` |
| AIA-55-1-c | Article 55(1), point (c) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção); [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| AIA-55-1-d | Article 55(1), point (d) | Covers | [1. The model weights are a critical asset](/sbd-toe/sbd-manual/containers-imagens/addon/self-hosted-inference#1-os-pesos-do-modelo-são-activo-crítico); `ARC-014`; `DEP-011` |
| AIA-AnxXI-1 | Annex XI, Section 1 | Supports evidence | `DEP-012`; [Policy 39 §4](/sbd-toe/assets/policies/policy-ai-bom-supply-chain#4-ai-bom--formato-e-conteúdo-mínimo) |
| AIA-AnxXI-2 | Annex XI, Section 2 | Supports evidence | [Ch. 10 US-21](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-21---governação-do-uso-de-ia-em-testes-e-eval-suites-para-agentes) |
| AIA-AnxXII | Annex XII | Supports evidence | [Policy 33 §10.6](/sbd-toe/assets/policies/policy-contratacao-segura#106-conformidade-regulatória-declarada) |
| AIA-59-1 | Article 59(1) | Supports evidence | `ENC-002`; `ACC-002`; `PRI-002` |
| AIA-60-7 | Article 60(7) to (8) | Supports evidence | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); `DPL-005` |
| AIA-72-1 | Article 72(1) | Covers | `CTX-AIA-RE-R04`; `OPS-011` |
| AIA-72-2 | Article 72(2) | Covers | `CTX-AIA-RE-R04`; `OPS-011` |
| AIA-72-3 | Article 72(3) | Covers | `CTX-AIA-RE-R04`; `OPS-011` |
| AIA-73-1 | Article 73(1) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) |
| AIA-73-2 | Article 73(2) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| AIA-73-3 | Article 73(3) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| AIA-73-4 | Article 73(4) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| AIA-73-5 | Article 73(5) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| AIA-74-12 | Article 74(12) | Supports evidence | `DEP-011`; [Policy 39 §4](/sbd-toe/assets/policies/policy-ai-bom-supply-chain#4-ai-bom--formato-e-conteúdo-mínimo) |
| AIA-74-13 | Article 74(13) | Supports evidence | `CIC-005` |
| AIA-75-1A | Article 75(1a) | Covers | [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória); [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) |
| AIA-79-4 | Article 79(2) and (4) | Supports evidence | `DPL-005`; `GOV-010` |
| AIA-82-2 | Article 82(2) | Supports evidence | `DPL-005`; `GOV-010` |
| AIA-86-1 | Article 86(1) | Covers | `CTX-AIA-RE-R03`; [Ch. 04 US-15](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-15---identificação-e-governação-de-componentes-não-determinísticos); `OPS-011` |
| AIA-111-4 | Article 111(4) | Covers | `CTX-AIA-RE-R02` |

### Declared gap (26) {#lacuna}

Strength “partial” or “gap”: the Manual does not cover, or covers only in part, and says what is missing. Gaps pending an AppSec Core round are marked with the name of the round.

| Obligation | Reference | Strength | How the Manual responds | What is missing |
|---|---|---|---|---|
| AIA-4-1 | Article 4(1) (replaced) | Partial | [Policy 37 §11](/sbd-toe/assets/policies/policy-formacao-seguranca#11-formação-em-agentes-ai-e-tooling-pervasivo-módulo-obrigatório); [Ch. 13 US-19](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-19---formação-em-uso-seguro-de-ia-e-tooling); `TRN-001` | Covers technical SDLC roles (developer, AppSec, DevOps, GRC, PO, CISO) and the use of AI as a tool/agents; missing are the business staff who operate or use product AI systems on behalf of the organisation and the weighing of the context of use and of the persons targeted. |
| AIA-4a-1-b | Article 4a(1), point (b) | Partial | `ENC-002`; `PRI-001`; `ACC-002` | Encryption at rest (L2+) and minimisation exist; missing are technical limitations on re-use and the pseudonymisation required for these datasets (pseudonymisation in the Manual applies only to logs, ERR-007). |
| AIA-4a-1-c | Article 4a(1), point (c) | Partial | `ACC-001`; `ACC-003`; `LOG-001` | RBAC access control and access logging (L1+) cover the core; missing are careful documentation of each access to these datasets and the confidentiality duty of those who access them. |
| AIA-4a-1-d | Article 4a(1), point (d) | Partial | [Policy 18 §10.4](/sbd-toe/assets/policies/policy-gestao-segredos#104-training-opt-out-obrigatório-para-pii); `DEP-014` | There is only a prohibition on use for training/retention by the AI service vendor; there is no general prohibition on transmission of, or access to, these data by third parties. |
| AIA-4a-1-e | Article 4a(1), point (e) | Partial | `PRI-002` | PRI-002 imposes a deadline and verifiable deletion, but not the legal trigger “once the bias has been corrected”. |
| AIA-4a-1-f | Article 4a(1), point (f) | Partial | `PRI-004` | The inventory records the purpose; it does not record the reasons for strict necessity nor the impossibility of using other data. |
| AIA-8-1 | Article 8(1) | Partial | `THR-008`; `ARC-014`; `OPS-011` | **AppSec Core AISVS/SAIF round.** Cybersecurity (THR-008, ARC-014, DEP-011 to DEP-014), human oversight (ARC-014 with floor P08) and transparency (CTX-AIA-RE-R01/R02) covered; accuracy and robustness pending the AISVS/SAIF round; data governance out of scope. |
| AIA-AnxIV-4 | Annex IV, point 4 | Gap | — | **AppSec Core AISVS/SAIF round.** Declared gap: appropriateness of the performance metrics, pending the AppSec Core AISVS/SAIF round. |
| AIA-13-3-b-ii | Article 13(3), point (b)(ii) | Gap | — | **AppSec Core AISVS/SAIF round.** Declaration of the accuracy and robustness levels pending the AppSec Core AISVS/SAIF round. |
| AIA-15-1 | Article 15(1) | Partial | `ARC-014`; `OPS-011` | **AppSec Core AISVS/SAIF round.** Cybersecurity covered (THR-008, ARC-014, DEP-011 to DEP-014, OPS-011 to OPS-014, DPL-010/011); accuracy and robustness pending the AppSec Core AISVS/SAIF round. |
| AIA-15-3 | Article 15(3) | Gap | — | **AppSec Core AISVS/SAIF round.** Declaration of the accuracy levels and parameters pending the AppSec Core AISVS/SAIF round. |
| AIA-15-4 | Article 15(4) | Partial | [Design considerations](/sbd-toe/sbd-manual/arquitetura-segura/recomendacoes-avancadas#considerações-de-design); [Policy 09 §3](/sbd-toe/assets/policies/policy-arquitetura-segura#3-princípios-de-arquitetura-segura); [🧱 Structured outputs — validation of what the model returns](/sbd-toe/sbd-manual/desenvolvimento-seguro/addon/genia-e-seguranca#structured-outputs) | Fallback, fail-secure and fail-closed output validation exist; missing are redundancy/safety plans for performance and bias mitigation in feedback loops of systems that continue to learn. |
| AIA-16-a | Article 16, point (a) | Partial | `THR-008`; `ARC-014`; `OPS-011` | **AppSec Core AISVS/SAIF round.** Cybersecurity (THR-008, ARC-014, DEP-011 to DEP-014), human oversight (ARC-014 with floor P08) and transparency (CTX-AIA-RE-R01/R02) covered; accuracy and robustness pending the AISVS/SAIF round; data governance out of scope. |
| AIA-16-c | Article 16, point (c) | Partial | `GOV-001`; `TST-001` | See AIA-17-1-*: operational components of a QMS exist; missing is the formal QMS structure of Article 17. |
| AIA-16-d | Article 16, point (d) | Partial | [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos); [Policy 06 §10](/sbd-toe/assets/policies/policy-rastreabilidade#10-prazos-de-retenção-mínimos) | See AIA-18-1: no 10-year period for the documentation of high-risk AI systems. |
| AIA-16-e | Article 16, point (e) | Partial | [Policy 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs); `OPS-003` | See AIA-19-1. |
| AIA-16-j | Article 16, point (j) | Partial | `DPL-005`; [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) | See AIA-20-1/20-2. |
| AIA-20-1 | Article 20(1) | Partial | `DPL-005`; [Policy 27 §3](/sbd-toe/assets/policies/policy-rollback#3-tipos-de-rollback-e-requisitos-específicos) | Tested rollback allows restoring/disabling; missing are withdrawal/recall of the system and informing distributors, deployers, the authorised representative and importers. |
| AIA-20-2 | Article 20(2) | Partial | [Policy 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); [Policy 32 §4.1](/sbd-toe/assets/policies/policy-irp#41-triagem-t0----15-minutos-de-detecção) | Incident investigation exists; missing are joint investigation with the deployer and informing the market surveillance authority of the non-compliance (not only of serious incidents). |
| AIA-25-4 | Article 25(4), first subparagraph | Partial | [Policy 33 §10.3](/sbd-toe/assets/policies/policy-contratacao-segura#103-audit-rights); [Policy 33 §10.6](/sbd-toe/assets/policies/policy-contratacao-segura#106-conformidade-regulatória-declarada); `DEP-014`; [Ch. 14 US-21](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-21) | Specific contractual clauses for AI service vendors (retention, audit, notification, declared compliance); they do not specify the information, capabilities, technical access and assistance needed for the provider to comply with the regulation. |
| AIA-26-1 | Article 26(1) | Partial | [Policy 38 §4](/sbd-toe/assets/policies/policy-mandates-agentes#4-conteúdo-mínimo-de-um-mandate); [Ch. 14 US-21](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-21) | For agents, the mandate defines how the system is used; for acquired AI systems there is no procedure for operating in accordance with the provider's instructions for use. |
| AIA-26-2 | Article 26(2) | Partial | [Policy 38 §4](/sbd-toe/assets/policies/policy-mandates-agentes#4-conteúdo-mínimo-de-um-mandate); [Policy 37 §11](/sbd-toe/assets/policies/policy-formacao-seguranca#11-formação-em-agentes-ai-e-tooling-pervasivo-módulo-obrigatório) | Named human owner and mandatory training for agents; nothing for overseers of non-agentic high-risk AI systems (competence, authority, support). |
| AIA-26-4 | Article 26(4) | Gap | `VAL-001` | VAL-001 validates inputs for security; there is no duty to ensure that input data is relevant and representative for the purpose. |
| AIA-26-5 | Article 26(5) | Partial | `OPS-011`; `REQ-AGN-003`; [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) | Monitoring (L2+), agent kill-switch and notification to the authority exist; missing are informing the provider/distributor and suspending non-agentic systems when there is a risk. |
| AIA-55-1-a | Article 55(1), point (a) | Partial | [Policy 19 §7.1](/sbd-toe/assets/policies/policy-estrategia-testes#71-composição-mínima); [C5 - Continuous eval suites for agents in development and production](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites) | Red-team corpus and eval suites (agents A2+/A3+); missing are standardised model evaluation protocols and documented adversarial testing at model level. |
| AIA-73-6 | Article 73(6) | Partial | [Policy 32 §4.2](/sbd-toe/assets/policies/policy-irp#42-contenção-t1---início-imediato-após-confirmação); `LOG-009` | Evidence preservation and investigation exist; the prohibition on altering the system in a way that affects the analysis of causes without informing the authorities beforehand is missing (the IRP prioritises containment “when possible”). |

### Out of scope (132) {#fora-de-ambito}

Obligations that the Manual declares out of scope, with the reason.

| Obligation | Reference | Reason |
|---|---|---|
| AIA-2-1 | Article 2(1) | Provision delimiting scope, a definition or a legal qualification; it does not create an engineering duty. |
| AIA-2-12 | Article 2(12) | Provision delimiting scope, a definition or a legal qualification; it does not create an engineering duty. |
| AIA-2-13 | Article 2(13) | Provision delimiting scope, a definition or a legal qualification; it does not create an engineering duty. |
| AIA-4a-1-a | Article 4a(1), point (a) | Necessity judgement (effectiveness of synthetic/anonymised data for correcting bias) — a data science and data protection decision, not a security engineering one. |
| AIA-5-1-c | Article 5(1), first subparagraph, point (c) | Judgement on the admissibility of the purpose (prohibited practice) — legal and product qualification; the Manual declares it out of scope. Generic hook: Ch. 02 US-17 (legal obligations mapped to requirements). |
| AIA-5-1-d | Article 5(1), first subparagraph, point (d) | Judgement on the admissibility of the purpose (prohibited practice) — legal and product qualification; the Manual declares it out of scope. Generic hook: Ch. 02 US-17 (legal obligations mapped to requirements). |
| AIA-5-1-f | Article 5(1), first subparagraph, point (f) | Judgement on the admissibility of the purpose (prohibited practice) — legal and product qualification; the Manual declares it out of scope. Generic hook: Ch. 02 US-17 (legal obligations mapped to requirements). |
| AIA-5-1-g | Article 5(1), first subparagraph, point (g) | Judgement on the admissibility of the purpose (prohibited practice) — legal and product qualification; the Manual declares it out of scope. Generic hook: Ch. 02 US-17 (legal obligations mapped to requirements). |
| AIA-5-1-h | Article 5(1), first subparagraph, point (h) | Judgement on the admissibility of the purpose (prohibited practice) — legal and product qualification; the Manual declares it out of scope. Generic hook: Ch. 02 US-17 (legal obligations mapped to requirements). |
| AIA-5-1B | Article 5(1b) | Provision delimiting scope, a definition or a legal qualification; it does not create an engineering duty. |
| AIA-8-2 | Article 8(2) | Integrated conformity with the Annex I sectoral legislation; product-conformity plane. |
| AIA-9-1 | Article 9(1) | Article 9 (risk management system) is out of scope by the lead's decision; the Manual's classification and threat model give only incidental evidence. |
| AIA-9-2 | Article 9(2) | Article 9 (risk management system) is out of scope by the lead's decision; the Manual's classification and threat model give only incidental evidence. |
| AIA-9-4 | Article 9(4) | Article 9 (risk management system) is out of scope by the lead's decision; the Manual's classification and threat model give only incidental evidence. |
| AIA-9-5 | Article 9(5) | Article 9 (risk management system) is out of scope by the lead's decision; the Manual's classification and threat model give only incidental evidence. |
| AIA-9-6 | Article 9(6) to (7) | Article 9 (risk management system) is out of scope by the lead's decision. |
| AIA-9-8 | Article 9(8) | Article 9 (risk management system) is out of scope by the lead's decision. |
| AIA-9-9 | Article 9(9) | Article 9 (risk management system) is out of scope by the lead's decision; the Manual's classification and threat model give only incidental evidence. |
| AIA-9-10 | Article 9(10) | Option/presumption (does not create an autonomous duty); compliance-strategy plane. |
| AIA-10-1 | Article 10(1) | Training-data governance and statistical bias assessment (Article 10) are out of scope by the lead's decision; the provenance and integrity of datasets (DEP-011) give only incidental evidence. |
| AIA-10-2 | Article 10(2) | Training-data governance and statistical bias assessment (Article 10) are out of scope by the lead's decision; the provenance and integrity of datasets (DEP-011) give only incidental evidence. |
| AIA-10-3 | Article 10(3) | Training-data governance and statistical bias assessment (Article 10) are out of scope by the lead's decision; the provenance and integrity of datasets (DEP-011) give only incidental evidence. |
| AIA-10-4 | Article 10(4) | Training-data governance and statistical bias assessment (Article 10) are out of scope by the lead's decision; the provenance and integrity of datasets (DEP-011) give only incidental evidence. |
| AIA-10-6 | Article 10(6) | Training-data governance and statistical bias assessment (Article 10) are out of scope by the lead's decision; the provenance and integrity of datasets (DEP-011) give only incidental evidence. |
| AIA-11-2 | Article 11(2) | Single technical documentation with the Annex I sectoral legislation; documentary organisation of compliance. |
| AIA-AnxIV-2-d | Annex IV, point 2(d) | Governance of training data (Article 10) is out of scope by the lead's decision; DEP-011 and Policy 39 §4 give only incidental evidence. |
| AIA-AnxIV-5 | Annex IV, point 5 | The risk management system of Article 9 is out of scope by the lead's decision. |
| AIA-AnxIV-7 | Annex IV, point 7 | List of harmonised standards/common specifications applied: conformity level. |
| AIA-AnxIV-8 | Annex IV, point 8 | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-12-3 | Article 12(3) | The specifics of biometric identification systems (Annex III, point 1: logs of Article 12(3) and two-person verification of Article 14(5)) are out of scope by the lead's decision; developing such an application follows the Manual like any other. Biometrics as an authentication factor belongs to the authentication requirements (AUT-*). |
| AIA-14-5 | Article 14(5) | The specifics of biometric identification systems (Annex III, point 1: logs of Article 12(3) and two-person verification of Article 14(5)) are out of scope by the lead's decision; developing such an application follows the Manual like any other. Biometrics as an authentication factor belongs to the authentication requirements (AUT-*). |
| AIA-16-b | Article 16, point (b) | Identification of the provider on the system/packaging: product labelling, compliance plane. |
| AIA-16-f | Article 16, point (f) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-16-g | Article 16, point (g) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-16-h | Article 16, point (h) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-16-i | Article 16, point (i) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-16-k | Article 16, point (k) | Relationship with authorities / penalty regime; legal plane, not engineering. |
| AIA-16-l | Article 16, point (l) | Accessibility requirements (Directives 2016/2102 and 2019/882): product quality, outside a security engineering manual. |
| AIA-17-1-a | Article 17(1), point (a) | Article 17 (quality management system) is out of scope by the lead's decision. |
| AIA-17-1-d | Article 17(1), point (d) | Article 17 (quality management system) is out of scope by the lead's decision. |
| AIA-17-1-e | Article 17(1), point (e) | Article 17 (quality management system) is out of scope by the lead's decision. |
| AIA-17-1-f | Article 17(1), point (f) | Article 17 (quality management system) is out of scope by the lead's decision. |
| AIA-17-1-g | Article 17(1), point (g) | Article 17 (quality management system) is out of scope by the lead's decision. |
| AIA-17-1-h | Article 17(1), point (h) | Article 17 (quality management system) is out of scope by the lead's decision. The Article 72 plan is in CTX-AIA-RE-R04. |
| AIA-17-1-j | Article 17(1), point (j) | Article 17 (quality management system) is out of scope by the lead's decision. |
| AIA-17-1-l | Article 17(1), point (l) | Article 17 (quality management system) is out of scope by the lead's decision. |
| AIA-17-3-4 | Article 17(3) and (4) | Option/presumption (does not create an autonomous duty); compliance-strategy plane. |
| AIA-21-1 | Article 21(1) | Relationship with authorities / penalty regime; legal plane, not engineering. |
| AIA-22-1 | Article 22(1) to (2) | Duty of another economic operator (importer/distributor/authorised representative), not of the engineering process of the provider or the deployer. |
| AIA-22-3 | Article 22(3) | Duty of another economic operator (importer/distributor/authorised representative), not of the engineering process of the provider or the deployer. |
| AIA-22-4 | Article 22(4) | Duty of another economic operator (importer/distributor/authorised representative), not of the engineering process of the provider or the deployer. |
| AIA-23-1 | Article 23(1) | Duty of another economic operator (importer/distributor/authorised representative), not of the engineering process of the provider or the deployer. |
| AIA-23-2 | Article 23(2) | Duty of another economic operator (importer/distributor/authorised representative), not of the engineering process of the provider or the deployer. |
| AIA-23-3 | Article 23(3) | Duty of another economic operator (importer/distributor/authorised representative), not of the engineering process of the provider or the deployer. |
| AIA-23-4 | Article 23(4) | Duty of another economic operator (importer/distributor/authorised representative), not of the engineering process of the provider or the deployer. |
| AIA-23-5 | Article 23(5) | Duty of another economic operator (importer/distributor/authorised representative), not of the engineering process of the provider or the deployer. |
| AIA-23-6 | Article 23(6) | Duty of another economic operator (importer/distributor/authorised representative), not of the engineering process of the provider or the deployer. |
| AIA-23-7 | Article 23(7) | Duty of another economic operator (importer/distributor/authorised representative), not of the engineering process of the provider or the deployer. |
| AIA-24-1 | Article 24(1) | Duty of another economic operator (importer/distributor/authorised representative), not of the engineering process of the provider or the deployer. |
| AIA-24-2 | Article 24(2) | Duty of another economic operator (importer/distributor/authorised representative), not of the engineering process of the provider or the deployer. |
| AIA-24-3 | Article 24(3) | Duty of another economic operator (importer/distributor/authorised representative), not of the engineering process of the provider or the deployer. |
| AIA-24-4 | Article 24(4) | Duty of another economic operator (importer/distributor/authorised representative), not of the engineering process of the provider or the deployer. |
| AIA-24-5 | Article 24(5) | Duty of another economic operator (importer/distributor/authorised representative), not of the engineering process of the provider or the deployer. |
| AIA-24-6 | Article 24(6) | Duty of another economic operator (importer/distributor/authorised representative), not of the engineering process of the provider or the deployer. |
| AIA-25-1 | Article 25(1) | Legal qualification of who becomes a provider. |
| AIA-25-3 | Article 25(3) | Provision delimiting scope, a definition or a legal qualification; it does not create an engineering duty. |
| AIA-25-5 | Article 25(5) | Provision delimiting scope, a definition or a legal qualification; it does not create an engineering duty. |
| AIA-26-7 | Article 26(7) | Information and consultation of workers: labour law/HR. |
| AIA-26-8 | Article 26(8) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-26-10 | Article 26(10) | Judicial/administrative authorisation for post-remote biometrics for law enforcement; legal plane. |
| AIA-26-12 | Article 26(12) | Relationship with authorities / penalty regime; legal plane, not engineering. |
| AIA-27-3 | Article 27(3) | Relationship with authorities / penalty regime; legal plane, not engineering. |
| AIA-41-5 | Article 41(5) | Justification of alternative solutions to common specifications: compliance plane. |
| AIA-42-1 | Article 42(1) | Option/presumption (does not create an autonomous duty); compliance-strategy plane. |
| AIA-42-2 | Article 42(2) | Option/presumption (does not create an autonomous duty); compliance-strategy plane. |
| AIA-43-1 | Article 43(1) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-43-2 | Article 43(2) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-43-3 | Article 43(3) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-47-1 | Article 47(1) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-47-2 | Article 47(2) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-47-3 | Article 47(3) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-47-4 | Article 47(4) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-AnxV | Annex V | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-48-2 | Article 48(2) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). The technical implementation of digital CE marking is trivial compared with the duty. |
| AIA-48-3 | Article 48(3) to (5) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-49-1 | Article 49(1) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-49-2 | Article 49(2) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-49-3 | Article 49(3) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-49-4 | Article 49(4) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-49-5 | Article 49(5) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-AnxVIII-A | Annex VIII, Section A | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-AnxVIII-B | Annex VIII, Section B | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-AnxVIII-C | Annex VIII, Section C | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-AnxVII-3 | Annex VII, points 3.1, 3.3, 3.4 | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-AnxVII-5 | Annex VII, point 5.2 | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-AnxIII-1 | Annex III, point 1 | Definition of the high-risk use cases; the operative duty is in AIA-6-2-3 (gap: the Manual does not link the legal status to the classification). |
| AIA-AnxIII-2 | Annex III, point 2 | Definition of the high-risk use cases; the operative duty is in AIA-6-2-3 (gap: the Manual does not link the legal status to the classification). |
| AIA-AnxIII-3 | Annex III, point 3 | Definition of the high-risk use cases; the operative duty is in AIA-6-2-3 (gap: the Manual does not link the legal status to the classification). |
| AIA-AnxIII-4 | Annex III, point 4 | Definition of the high-risk use cases; the operative duty is in AIA-6-2-3 (gap: the Manual does not link the legal status to the classification). |
| AIA-AnxIII-5 | Annex III, point 5 | Definition of the high-risk use cases; the operative duty is in AIA-6-2-3 (gap: the Manual does not link the legal status to the classification). |
| AIA-AnxIII-6 | Annex III, point 6 | Definition of the high-risk use cases; the operative duty is in AIA-6-2-3 (gap: the Manual does not link the legal status to the classification). |
| AIA-AnxIII-7 | Annex III, point 7 | Definition of the high-risk use cases; the operative duty is in AIA-6-2-3 (gap: the Manual does not link the legal status to the classification). |
| AIA-AnxIII-8 | Annex III, point 8 | Definition of the high-risk use cases; the operative duty is in AIA-6-2-3 (gap: the Manual does not link the legal status to the classification). |
| AIA-50-4-b | Article 50(4), second subparagraph | Disclosure of AI-generated text published on matters of public interest, with the editorial-control exception: editorial process of the deployer. |
| AIA-52-1 | Article 52(1) to (2) | Obligation of the GPAI model provider towards the Commission/AI Office; legal and AI-domain plane. The Manual deals with the GPAI consumer side (DEP-014, Policy 33 §10.6). |
| AIA-53-1-c | Article 53(1), point (c) | Copyright/TDM opt-out policy: legal plane. |
| AIA-53-1-d | Article 53(1), point (d) | Public summary of the training content according to the AI Office template: legal/AI-domain plane. |
| AIA-53-3 | Article 53(3) | Relationship with authorities / penalty regime; legal plane, not engineering. |
| AIA-53-4 | Article 53(4) | Option/presumption (does not create an autonomous duty); compliance-strategy plane. |
| AIA-54-1 | Article 54(1) to (2) | Duty of another economic operator (importer/distributor/authorised representative), not of the engineering process of the provider or the deployer. |
| AIA-54-3 | Article 54(3) to (5) | Duty of another economic operator (importer/distributor/authorised representative), not of the engineering process of the provider or the deployer. |
| AIA-55-2 | Article 55(2) | Option/presumption (does not create an autonomous duty); compliance-strategy plane. |
| AIA-91-5 | Article 91(5) | Relationship with authorities / penalty regime; legal plane, not engineering. |
| AIA-92-5 | Article 92(3) and (5) | Relationship with authorities / penalty regime; legal plane, not engineering. |
| AIA-57-12 | Article 57(12) | Relationship with authorities / penalty regime; legal plane, not engineering. |
| AIA-60-4 | Article 60(4) | Regulatory conditions for testing in real-world conditions (approved plan, registration, consent): legal plane. |
| AIA-60-9 | Article 60(9) | Relationship with authorities / penalty regime; legal plane, not engineering. |
| AIA-61-1 | Article 61 | Informed consent of participants: legal/ethical plane. |
| AIA-72-4 | Article 72(4) | Option/presumption (does not create an autonomous duty); compliance-strategy plane. |
| AIA-73-9-10 | Article 73(9) to (10) | Provision delimiting scope, a definition or a legal qualification; it does not create an engineering duty. |
| AIA-75-1E | Article 75(1e), second subparagraph | Relationship with authorities / penalty regime; legal plane, not engineering. |
| AIA-75c-3 | Article 75c(3) | Relationship with authorities / penalty regime; legal plane, not engineering. |
| AIA-80-4 | Article 80(4), (5) and (7) | Reclassification by the authority and penalty for incorrect classification: legal plane. |
| AIA-83-1 | Article 83(1) | Conformity assessment/market plane (EU declaration, CE marking, notified bodies, registration in the EU database); outside a security engineering manual — the Manual's own cross-check declares it out of scope (“does not replace”). |
| AIA-87 | Article 87 | Whistleblowing channels (Directive 2019/1937): HR/legal. |
| AIA-99-3 | Article 99(3) | Relationship with authorities / penalty regime; legal plane, not engineering. |
| AIA-99-4 | Article 99(4) | Relationship with authorities / penalty regime; legal plane, not engineering. |
| AIA-99-5 | Article 99(5) | Relationship with authorities / penalty regime; legal plane, not engineering. |
| AIA-101-1 | Article 101(1) | Relationship with authorities / penalty regime; legal plane, not engineering. |
| AIA-111-2 | Article 111(2) | Provision delimiting scope, a definition or a legal qualification; it does not create an engineering duty. |
| AIA-111-3 | Article 111(3) | Provision delimiting scope, a definition or a legal qualification; it does not create an engineering duty. |
| AIA-113-3 | Article 113, third subparagraph | Provision delimiting scope, a definition or a legal qualification; it does not create an engineering duty. |
