---
id: intro
title: CRA - Normative cross-check
description: Analysis of how SbD-ToE supports the technical core of the Cyber Resilience Act in the context of products with digital elements, with explicit conformity boundaries
tags: [cross-check, cra, regulamentacao, produtos-digitais, sbom, vulnerabilidades]
sidebar_position: 5
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/cra/01-intro.md
  source_sha256: 3dd7f6772b7f13bb039ca484d86ad8636905dc9461a1b335e08f4982be8864d7
  source_commit: 5bc57a2de453d4a50f78edcfb2b9546615b20690
  target_sha256: 20cec387114634ea25d4434c1a90b8ce196e7c59f5b0c479fdaed57a16a662ed
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [avaliacao, chapter_role, cra_actively_exploited_vulnerability, cra_economic_operator, cra_pde, cra_support_period, csa_certification_scheme, cycle_iteration, eu_ce_marking, eu_market_surveillance_authority, eu_notified_body, eu_placing_on_market, eu_startups, gap_family, lifecycle_phase, mcp_reading_programa, normative_empirical, papel_suporte, piso_limiar, piso_relacao, practitioner_manual, programme_line, provenance, requirement_runtime, role_juridico, sbdtoe_sbd, verificacao_check, verification_taxonomy]
  glossary_sha256: a81fc8db6f3473de0dd4156bb3e0588fbb2b6d2e9720fa68a5f78261e41e2c49
  translated_at: 2026-09-27T23:03:31Z
  stamped_at: 2026-09-27T23:03:31Z
  reviewed_by: null
---

# CRA: Normative cross-check

> For practical implementation, see the [SbD-ToE 4 CRA Playbook](/sbd-toe/cross-check-normativo/cra/playbook).
> 
> For universal application patterns, see the core chapters of the SbD-ToE (01–14).
>
> For the obligation-by-obligation answer (what the Manual covers, the declared gaps and what is out of scope) and for the requirements that apply under the `CTX-CRA` context, see [Applicable requirements](/sbd-toe/cross-check-normativo/cra/requisitos-aplicaveis).

## Scope {#âmbito}

### 🧩 CRA - Cyber Resilience Act {#-cra---cyber-resilience-act}

The **Cyber Resilience Act (CRA)** is **Regulation (EU) 2024/2847** (CELEX: [32024R2847](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847)), which lays down horizontal requirements for the design, development, production and support of products with digital elements.

In this reading, `CRA` should be understood first and foremost as a framework of:

- product with digital elements
- manufacturer and other economic operators
- technical obligations supported by evidence
- and a separate formal conformity route

The CRA imposes obligations on manufacturers, importers and distributors, including:

- essential requirements for **security by design and by default** throughout the entire lifecycle;
- **vulnerability handling** processes, including receipt, analysis, remediation and responsible disclosure;
- **vulnerability handling during the support period** (Annex I, Part II) and remediation without delay;
- requirements for **technical documentation**, instructions and information to the user — the technical documentation and the EU declaration of conformity are kept at the disposal of the market surveillance authorities «for at least 10 years after the product with digital elements has been placed on the market or for the support period, whichever is longer» (Article 13(13));
- obligations to **notify actively exploited vulnerabilities and severe incidents**.

### Scope gate {#gate-de-âmbito}

This local `CRA` reading is most defensible when applied to:

- manufacturers of software or products with digital elements
- suppliers that need technical evidence for a product conformity surface
- contexts where there is a product, a version, a support period and a chain of economic operator responsibilities

Outside that context, SbD-ToE remains useful as a technical basis, but the reading ceases to be a full `CRA` reading and becomes partial support only.

In the SbD-ToE context, the CRA is operationalised through:

- secure engineering practices (requirements, architecture, development, IaC, pipelines and testing chapters);
- management of SBOM, provenance and supply chain (dependencies, containers, images, CI/CD);
- structured _vulnerability handling_ and _incident handling_ processes;
- governance and contracts (including subcontractors and software/service suppliers).

> ⚖️ **Note on technical references.**  
> The CRA requires the SBOM “in a commonly used and machine-readable format covering at the very least the top-level dependencies of the products” (Annex I, Part II, point 1), without imposing a specific format; the Commission may specify it by implementing acts (Article 13(24)).  
> Standards such as **CycloneDX**, **SPDX**, **ISO/IEC 29147 (Vulnerability Disclosure)** and **ISO/IEC 30111 (Vulnerability Handling)** are widely recognised and provide a solid basis for meeting the regulation's technical and procedural requirements.  
> The SbD-ToE treats these standards as **recommended good practice**, not as legal requirements in themselves.

The SbD-ToE was designed for software applications and pipelines; much of its technical and procedural controls **align with the core of CRA obligations**. This document answers each obligation in one of three categories (covers, declared gap, out of scope) and indicates the adaptation actions, without pretending that product compliance is exhausted by the core manual.

## What this Manual covers and what stays out {#o-que-este-manual-cobre-e-o-que-fica-de-fora}

The SbD-ToE is centred on the application: requirements, architecture, code, dependencies, pipeline, deployment and operation of the software. For each CRA obligation, the Manual answers in one of three categories, and no obligation is left in silence:

- **Covers**, and states how: catalogue requirement, policy, floor or requirement added by the regime, or engineering evidence for a duty that sits on another plane.
- **Declared gap**: what the Manual does not cover by default, stating what is missing.
- **Out of scope**: what the Manual does not deal with, with the reason.

The full list, obligation by obligation, is generated from the coverage matrix and is in [Applicable requirements — What this Manual covers and what stays out](./requisitos-aplicaveis#cobertura). Where this page and the list diverge, the list prevails.

When the application is, or is part of, a product with digital elements placed on the market, the `CTX-CRA` context is declared. The context raises four requirements to mandatory at any level (floor `CTX-CRA-P01` to `P04`: blocking on a known exploitable vulnerability, no exception at placing on the market, due diligence on third-party components, coordinated disclosure with a single point of contact) and adds five requirements specific to the regime (`CTX-CRA-R01` to `R05`: support period, security update mechanism, public advisories on fixed vulnerabilities, reporting to the component maintainer, severe incident criterion).

**Out of scope, by programme decision:**
- Security of the entity as a whole (corporate network and administration channels, EDR, patching of operating systems and equipment, inventory and classification of all assets): the Manual is centred on the application.
- Conformity assessment, CE marking and EU declaration of conformity. The technical documentation (Annex VII) has an evidence map on the [generated page](./requisitos-aplicaveis#mapa-evidencia).

## Regulatory Notice {#aviso-regulatório}

The CRA introduces obligations concerning: classification as an important product (classes I/II, Annex III) or a critical product (Annex IV), CE marking, declaration of conformity, conformity assessment (including modules involving notified bodies for certain categories), post-market obligations (vulnerability handling), and notification of actively exploited vulnerabilities, simultaneously, to the CSIRT designated as coordinator and to ENISA, via the single reporting platform (Art. 14 and 16): an early warning notification within 24 hours of becoming aware, a vulnerability notification within 72 hours and a final report no later than 14 days after a corrective or mitigating measure is available; severe incidents having an impact on the security of the product follow the same channel (24 hours, 72 hours and a final report within one month). Article 14 applies from 11 September 2026 (Article 71(2)).

It is also worth fixing two operational dates of the regulation:

- `Article 14` applies from `11 September 2026`
- the general application of the regulation starts on `11 December 2027`

SbD-ToE covers the technical "how", but **does not replace**:
- Formal conformity assessment procedures (module A; modules B + C; module H; or a European cybersecurity certification scheme, Article 32)
- Interactions with notified bodies
- Issuing the EU declaration of conformity / CE marking
- Legal process of manufacturer/importer/distributor liability

## PART I: CRA Obligations vs. SbD-ToE {#parte-i-obrigações-cra-vs-sbd-toe}

| CRA Domain | Regulatory Reference (Summary) | SbD-ToE Coverage | Declared gap or out of scope | Adaptation Action |
|-------------|----------------------------------|-------------------|------------------------------------|-------------------|
| Secure Lifecycle Management | Security requirements applicable throughout the entire cycle (design → development → distribution → maintenance) | Ch. 02 (requirements), Ch. 06 (development), Ch. 07 (CI/CD), Ch. 11 (pre-deploy); support period: `CTX-CRA-R01` | Declared gap: supported versions policy (Article 13(10)), beta or pre-release channels (Article 4(3)), classification of the product in the categories of Annexes III and IV (Article 7(1)). Out of scope: the economic operator role, as it is a legal qualification | Declare the `CTX-CRA` context per application or product and determine the support period in line with `CTX-CRA-R01` |
| Vulnerability Identification and Management | Processes to receive, assess, prioritise and remediate vulnerabilities | Ch. 05 (SBOM/SCA), Ch. 10 (testing), Ch. 12 (monitoring), exception addons; `GOV-015` (coordinated disclosure policy and channel for receiving external reports; floor `CTX-CRA-P04`) | — | Publish the coordinated disclosure policy and the single point of contact in line with `GOV-015` and floor `CTX-CRA-P04` (Annex I, Part II, points 5 and 6) |
| SBOM / Transparency | Provision of information on critical components and dependencies | Ch. 05 (continuous SBOM in CycloneDX or SPDX, `DEP-001`) | Declared gap: telling the user where to access the SBOM, when the manufacturer makes it available (Annex II, point 9) | Create a sanitised SBOM export routine for stakeholders |
| Rapid Fixes and Patches | Apply security fixes without undue delay | Ch. 05 (CVE management), Ch. 07 (CI/CD automation), Ch. 12 (exploitation detection); distribution of updates: `CTX-CRA-R02` | — (the CRA asks for vulnerabilities to be addressed and remediated “without delay” (Annex I, Part II, point 2), without setting a number of days) | Apply the Manual's single internal remediation ladder ([Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle)) as the operationalisation of «without delay» — the Manual's choice, not a CRA time limit |
| Reporting of actively exploited vulnerabilities | Notify the CSIRT designated as coordinator and ENISA, via the single reporting platform, of actively exploited vulnerabilities and severe incidents: early warning ≤24 h, notification ≤72 h and final report (Art. 14; applicable since 11.9.2026) | Ch. 12 (detection, exploitation metrics), Ch. 14 (governance); [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) (deadlines, recipients and information to affected users); severe incident criterion: `CTX-CRA-R05` | Declared gap: minimum content of each notification (Article 14(2) and (4)), intermediate report at the CSIRT's request (paragraph 6) and rule for determining the coordinating CSIRT (paragraph 7) | Complete the notification runbook with the minimum content of each notification and the intermediate report |
| Vulnerability Prevention Measures | Quality control and security testing before release | Ch. 10 (SAST/DAST/fuzzing), Ch. 11 (release gate); `DEP-002` with floor `CTX-CRA-P01` | — | Block any known exploitable vulnerability, at any level and beyond the severity criterion (floor `CTX-CRA-P01`): the CRA requires products to be made available “without known exploitable vulnerabilities” (Annex I, Part I, point 2(a)) |
| Security Documentation | Security instructions and information for users/admins | Ch. 04 (architecture), Ch. 11 (secure deployment); point of contact: `GOV-015` (floor `CTX-CRA-P04`); support period and end of support: `CTX-CRA-R01`; update instructions: `CTX-CRA-R02` | Declared gap: guidance on secure commissioning and use, effect of changes to the product on the security of data, secure decommissioning and data removal (Annex II, point 8(a), (b) and (d)); content, language and retention of the instructions (Article 13(18)) | Create the "Product Security Guide" artefact for the parts under a gap |
| Post-Market Monitoring | Continuous observation of exploitation and failures | Ch. 12 (monitoring, alerts) | — | Create a dedicated "Security Feedback" backlog + weekly triage |
| Exception Management | Justification of temporary deviations | Ch. 02 addon 08, Ch. 05 addon 09, Ch. 14 governance; [Policy 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção) with floor `CTX-CRA-P02` | — | Apply floor `CTX-CRA-P02`: the “fix deferred” and “risk accepted” exceptions do not apply to known exploitable vulnerabilities at placing on the market, and the floor admits no justification |
| Supply Chain Security | Secure third-party components, integrity verification | Ch. 05 (SCA), Ch. 07 (pipeline), Ch. 09 (container runtime); `DEP-006` with floor `CTX-CRA-P03`; reporting to the component maintainer: `CTX-CRA-R04` | Out of scope: firmware, hardware and secure boot, because the Manual is centred on the application | Apply `DEP-006` with floor `CTX-CRA-P03` and the addition `CTX-CRA-R04` |
| Conformity and CE Marking | Declaration and marking of conformity | — | Out of scope: the plane of formal conformity and the market (EU declaration, CE marking, notified bodies), outside the scope of a software security engineering manual | Establish a parallel GRC + legal process; the Manual provides the technical evidence |

## PART II: Detailed Coverage {#parte-ii-cobertura-detalhada}

### 1. Secure Lifecycle {#1-ciclo-de-vida-seguro}
SbD-ToE defines security gates from classification through to deploy. This supports the CRA obligation to ensure security "by design" and during maintenance.

The role of economic operator (manufacturer, importer, distributor) is a legal qualification and is out of scope. The support period and informing the user of the end of support are prescribed in the `CTX-CRA` context (`CTX-CRA-R01`).

**Action:** Consolidate into a single document: "CRA Control Matrix" listing controls by phase (design, build, test, release, maintenance).

### 2. Vulnerability Handling & Coordinated Disclosure {#2-vulnerability-handling--coordinated-disclosure}
The SbD-ToE already provides for internal triage (SCA, scans, testing). The CRA also requires a coordinated disclosure policy and an external channel for researchers or users to report flaws (Annex I, Part II, points 5 and 6). The Manual prescribes the coordinated disclosure policy and the channel for receiving external reports (`GOV-015`), which the `CTX-CRA` context makes mandatory at any level, with a single point of contact (floor `CTX-CRA-P04`).

**Action:** Publish the policy and the point of contact in line with `GOV-015` and floor `CTX-CRA-P04`.

### 3. SBOM and Transparency {#3-sbom-e-transparência}
Continuous SBOM (Ch. 05) is the basis for providing visibility. The CRA requires the SBOM in a commonly used and machine-readable format (Annex I, Part II, point 1); Ch. 05 meets this with CycloneDX or SPDX (`DEP-001`).

**Action:** Generate a sanitised export (without sensitive internal paths) and keep one version per major release.

### 4. Rapid Patching {#4-patching-rápido}
Apply the Manual's internal remediation ladder ([Policy 19 §4.3](/sbd-toe/assets/policies/policy-estrategia-testes#43-slas-de-triagem-e-resolução); the Manual's choice) as the operationalisation of the CRA's «without delay» (Annex I, Part II, point (2)); with an indication of active exploitation, the time limit is brought forward. Integrate into the pipeline: if critical CVE → automatic task + CISO alert.

**Action:** Automation: a CI workflow that opens an issue + "CRA-Patch" label.

### 5. Exploited Vulnerability Reporting {#5-reporte-de-vulnerabilidade-explorada}
When exploitation is confirmed (telemetry, IOC, proof), generate a minimum report: vulnerability ID, component, affected version, impact, temporary mitigation, patch deadline.

Time limits of Article 14 (applicable since 11.9.2026), to the CSIRT designated as coordinator and to ENISA, via the single reporting platform: early warning notification ≤ 24 h and vulnerability notification ≤ 72 h after becoming aware; final report ≤ 14 days after the corrective or mitigating measure is available. For severe incidents: 24 h, 72 h and final report ≤ 1 month after the notification. The manufacturer also informs the impacted users (Article 14(8)).

This must be read as a technical basis for meeting the reporting obligation, not as a substitute for the full regulatory surface of `Articles 14-16`, which includes formal notification, institutional coordination and communication to users where applicable.

**Action:** Extraction script (e.g. SIEM + SBOM export) → ready-made JSON.

### 6. Quality and Security Testing {#6-qualidade-e-testes-de-segurança}
SbD-ToE covers a variety of tests. Align with the CRA requirement to make the product available on the market without known exploitable vulnerabilities (Annex I, Part I, point (2)(a), on the basis of the risk assessment).

**Action:** A gate that blocks any known exploitable vulnerability before release, at any level (`DEP-002`, floor `CTX-CRA-P01`). These vulnerabilities admit no exception at placing on the market (floor `CTX-CRA-P02`).

### 7. Product Security Documentation {#7-documentação-de-segurança-do-produto}
Produce a guide for administrators/users: secure configurations, updating, security contact, logging policies.

For `CRA` reading, the security point of contact (`GOV-015`, floor `CTX-CRA-P04`), the support period and its end date (`CTX-CRA-R01`) and the instructions for installing updates (`CTX-CRA-R02`) are prescribed. The following remain a declared gap: guidance on secure commissioning and use, instructions on the effect of changes on the security of data and on decommissioning and data removal, and telling the user where to access the SBOM (Annex II, points 8 and 9).

**Action:** Template derived from Ch. 04 (architecture) + Ch. 11 (secure deploy).

### 8. Post-Market Monitoring {#8-monitorização-pós-comercialização}
Ch. 12 already defines monitoring; add specific panels: "Known vulnerabilities vs. patch status".

**Action:** Dashboard with: total open vulns, mean time to patch, percentage of SLA met.

### 9. Exceptions {#9-exceções}
In the CRA context, the “fix deferred” and “risk accepted” exceptions do not apply to known exploitable vulnerabilities at the time of placing on the market, whatever their type or severity (floor `CTX-CRA-P02`, [Policy 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção)). All others follow the general exceptions policy.

**Action:** Apply floor `CTX-CRA-P02` in the applications that declare the `CTX-CRA` context.

### 10. Supply Chain {#10-cadeia-de-fornecimento}
Due diligence on third-party components is `DEP-006`, mandatory at any level in the CRA context (floor `CTX-CRA-P03`); reporting a vulnerability in a component to its maintainer is `CTX-CRA-R04`.

**Out of scope:** firmware, hardware, physical cryptographic modules and secure boot. The Manual is centred on the application; an organisation with these elements in its product needs a process of its own.

### 11. Conformity and CE Marking {#11-conformidade-e-marcação-ce}
Out of scope: this is the plane of formal conformity and the market (EU declaration, CE marking, notified bodies), outside the scope of a software security engineering manual. It requires a legal documentation process.

**Action:** Create a separate GRC/Legal swimlane; keep the technical controls referenced as security evidence.

## Declared gaps and out of scope {#lacunas-intencionais}

The coordinated disclosure channel (`GOV-015`, floor `CTX-CRA-P04`) and the format of the SBOM (`DEP-001`, CycloneDX or SPDX) are covered and no longer appear in this section. The full list, obligation by obligation, is in [Applicable requirements](./requisitos-aplicaveis#cobertura); the tables below group it.

**Declared gaps** (the Manual does not cover, or covers only in part):

| Group | Obligations | What is missing |
|-------|------------|-------------|
| Product and lifecycle | Article 4(3); Article 7(1); Article 13(10) and (14) | Rule for beta or pre-release channels; classification of the product in the categories of Annexes III and IV, which determine the conformity route; supported versions policy; tracking of harmonised standards and common specifications |
| Risk assessment | Article 13(3) and (4) | Structured risk assessment, essential requirement by essential requirement, integrated into the technical documentation |
| Requirements for the delivered product | Annex I, Part I, point 2(b), (f), (g), (i), (l) and (m) | Secure-by-default configuration of the delivered product and reset to the original state; reporting corruption to the user; minimisation of non-personal data; not degrading other devices or networks; user opt-out of reporting; secure removal and transfer of all data |
| Information to the user | Annex II, points 8 ((a), (b), (d)) and 9; Article 13(18) | Guidance on secure commissioning and use; effect of changes on the security of data; secure decommissioning and data removal; where to access the SBOM; content, language and retention of the instructions |
| Retention of documentation | Article 13(13) | The Manual applies the 10 years to the SBOM and the evidence pack, but not yet to threat model versions or approval records |
| Article 14 notifications | Article 14(2), (4), (6) and (7) | Minimum content of each notification; intermediate report at the CSIRT's request; rule for determining the coordinating CSIRT |

**Out of scope** (the Manual does not deal with it, with the reason):

| Area | Reason |
|------|-------|
| EU declaration of conformity, CE marking, notified bodies, relations with authorities and penalties regime | Legal plane, and plane of formal conformity and the market, outside the scope of a software security engineering manual |
| Duties of importers, distributors and authorised representatives; requalification as manufacturer (Articles 21 and 22) | Duty of another economic operator, or a legal qualification |
| Open-source software steward (Article 24) | The Manual does not model this role |
| Identification of the manufacturer on the product and contact details on the packaging (Article 13(16); Annex II, point 1); commercial indication of the end-of-support date at the time of purchase | Labelling and market plane |
| Voluntary notification (Article 15) | An option, not a duty |
| Transitional regime and product category lists (Annexes III and IV) | Legal plane; the lists determine the conformity route |
| Firmware, hardware and secure boot | The Manual is centred on the application |

## Simple CRA Metric (Self-Assessment) {#métrica-simples-cra-autoavaliação}

Answer YES or NO to the following points:
1. Is there a product security policy covering design→maintenance?
2. Is a complete SBOM generated per release?
3. Is there a public vulnerability disclosure channel (`GOV-015`)?
4. Is the patch SLA documented and monitored?
5. Is there a gate that blocks any known exploitable vulnerability (floor `CTX-CRA-P01`)?
6. Is a post-market vulnerability dashboard active?
7. Is a sanitised external SBOM export available for customers/regulators?
8. Does the exceptions policy allow no exception for known exploitable vulnerabilities at placing on the market (floor `CTX-CRA-P02`)?
9. Is the Product Security Guide published?
10. Is the active exploitation reporting process documented?

≥8/10 → Good CRA technical baseline. `<`6 → Prioritise SBOM, patching, disclosure, gating by exploitability. The thresholds are the Manual's choice, not a CRA criterion.

## Priority Actions (Initial Roadmap) {#ações-prioritárias-roadmap-inicial}

1. Declare the `CTX-CRA` context in the applications in scope and apply its floor (`CTX-CRA-P01` to `P04`) and additions (`CTX-CRA-R01` to `R05`), including the support period 
2. Publish the coordinated disclosure policy and the single point of contact (`GOV-015`, floor `CTX-CRA-P04`) 
3. Adjust the pipeline with the gate on known exploitable vulnerabilities (`DEP-002`, floor `CTX-CRA-P01`) 
4. Define the CRA patch SLA and tracking metrics 
5. Generate SBOM and a CycloneDX export per release 
6. Close the declared gaps in information to the user (secure use guidance, effect of changes, decommissioning and data removal, access to the SBOM) 
7. Complete the Article 14 reporting runbook with the minimum content of each notification and the intermediate report 
8. Add a post-market dashboard 
9. Define the supported versions policy 
10. CE Conformity swimlane (legal + GRC), outside the scope of the Manual

## References {#referências}

- **Cyber Resilience Act**: Regulation (EU) 2024/2847 (CELEX: [32024R2847](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847))
- SbD-ToE Manual Chapters 01–14 
- ENISA Guidance on Product Security & Vulnerability Disclosure 
- ISO/IEC 29147 (Vulnerability Disclosure), ISO/IEC 30111 (Vulnerability Handling)
- CycloneDX / SPDX specifications

**Version:** 1.1  
**Date:** September 2026 (aligned with the coverage matrix and the `CTX-CRA` context)
