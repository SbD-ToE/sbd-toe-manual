---
id: intro
title: CRA - Normative cross-check
description: Analysis of how SbD-ToE supports the technical core of the Cyber Resilience Act in the context of products with digital elements, with explicit conformity boundaries
tags: [cross-check, cra, regulamentacao, produtos-digitais, sbom, vulnerabilidades]
sidebar_position: 5
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/cra/01-intro.md
  source_sha256: 91828b5c3a1fcc60f1b5829d6817325e6fe7862179ed69df716b2fae4a39c0bd
  source_commit: 036d74010f423f247be988e4a417375c74edb9d9
  target_sha256: d2bf6c42914cc503b072c12806fe636394b16d07724fc8344228e292412027d0
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [avaliacao, chapter_role, cra_actively_exploited_vulnerability, cra_economic_operator, cra_pde, cra_support_period, csa_certification_scheme, cycle_iteration, eu_ce_marking, eu_market_surveillance_authority, eu_notified_body, eu_placing_on_market, gap_family, lifecycle_phase, normative_empirical, papel_suporte, practitioner_manual, provenance, role_juridico, sbdtoe_sbd, verificacao_check, verification_taxonomy]
  glossary_sha256: 65e3761ca8f3fcf186a68a382295b6910c3a06b27e92e479ad1fc272b84f8f61
  translated_at: 2026-09-27T07:53:29Z
  stamped_at: 2026-09-27T07:53:29Z
  reviewed_by: null
---

# CRA: Normative cross-check

> For practical implementation, see the [SbD-ToE 4 CRA Playbook](/sbd-toe/cross-check-normativo/cra/playbook).
> 
> For universal application patterns, see the SbD-ToE core chapters (01–14).

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
> The CRA does not impose a single SBOM format, nor does it explicitly require the use of specific standards.  
> Nevertheless, standards such as **CycloneDX**, **SPDX**, **ISO/IEC 29147 (Vulnerability Disclosure)** and **ISO/IEC 30111 (Vulnerability Handling)** are widely recognised and provide a solid basis for meeting the technical and procedural requirements of the regulation.  
> SbD-ToE adopts these standards as **recommended good practices**, not as legal requirements in their own right.

SbD-ToE was designed for software applications and pipelines; a large part of its technical and procedural controls **aligns with the core of the CRA obligations**. This document identifies coverage, intentional gaps and adaptation actions, without pretending that product conformity is exhausted by the core manual.

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

| CRA Domain | Regulatory Reference (Summary) | SbD-ToE Coverage | Intentional Gap | Adaptation Action |
|-------------|----------------------------------|-------------------|--------------------|-------------------|
| Secure Lifecycle Management | Security requirements applicable throughout the entire cycle (design → development → distribution → maintenance) | Ch. 02 (requirements), Ch. 06 (development), Ch. 07 (CI/CD), Ch. 11 (pre-deploy) | Does not clearly distinguish manufacturer/importer/distributor roles, nor the formal determination of the support period | Map SbD-ToE roles → CRA roles and record a support period policy |
| Vulnerability Identification and Management | Processes to receive, assess, prioritise and remediate vulnerabilities | Ch. 05 (SBOM/SCA), Ch. 10 (testing), Ch. 12 (monitoring), exception addons | Formal mechanism for external receipt (coordinated disclosure portal) | Implement a public channel + a coordinated vulnerability disclosure policy (Annex I, Part II, point (5)) |
| SBOM / Transparency | Provision of information on critical components and dependencies | Ch. 05 (continuous SBOM) | Exact format for external provision (e.g. public CycloneDX export) | Create a sanitised SBOM export routine for stakeholders |
| Rapid Fixes and Patches | Apply security fixes without undue delay | Ch. 05 (CVE management), Ch. 07 (CI/CD automation), Ch. 12 (exploitation detection) | The CRA requires vulnerabilities to be addressed and remediated «without delay» (Annex I, Part II, point (2)), without setting a number of days | Apply the Manual's single internal remediation ladder ([Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle)) as the operationalisation of «without delay» — the Manual's choice, not a CRA time limit |
| Reporting of actively exploited vulnerabilities | Notify the CSIRT designated as coordinator and ENISA, via the single reporting platform, of actively exploited vulnerabilities and severe incidents: early warning ≤24 h, notification ≤72 h and final report (Art. 14; applicable since 11.9.2026) | Ch. 12 (detection, exploitation metrics), Ch. 14 (governance) | Does not sufficiently separate mandatory reporting, communication to users and the official platform/regime | Add a technical runbook + a formal notification and communication interface |
| Vulnerability Prevention Measures | Quality control and security testing before release | Ch. 10 (SAST/DAST/fuzzing), Ch. 11 (release gate) | Formal rejection/release criteria by criticality | Add a blocking criterion based on known exploitability, not only on criticality: the CRA requires products to be made available on the market «without known exploitable vulnerabilities» (Annex I, Part I, point (2)(a)) |
| Security Documentation | Security instructions and information for users/admins | Ch. 04 (architecture), Ch. 11 (secure deploy) | The manual does not on its own generate the entire `Annex II` surface (support period, contact point, end-of-support wording) | Create a "Product Security Guide" artefact + a support period and contact point table |
| Post-Market Monitoring | Continuous observation of exploitation and failures | Ch. 12 (monitoring, alerts) | Integration with a user feedback channel | Create a dedicated "Security Feedback" backlog + weekly triage |
| Exception Management | Justification of temporary deviations | Ch. 02 addon 08, Ch. 05 addon 09, Ch. 14 governance | Does not map CRA acceptability limits | Introduce a list of "non-exceptionable" vulnerabilities (e.g. critical RCE) |
| Supply Chain Security | Secure third-party components, integrity verification | Ch. 05 (SCA), Ch. 07 (pipeline), Ch. 09 (container runtime) | Firmware/hardware verification process and economic operator boundary still insufficiently explicit | Add a physical supply chain checklist (hash, secure boot if applicable) and a record per role |
| Conformity and CE Marking | Declaration and marking of conformity | (Not covered) | Formal technical/legal assessment | Establish a parallel GRC + Legal process |

## PART II: Detailed Coverage {#parte-ii-cobertura-detalhada}

### 1. Secure Lifecycle {#1-ciclo-de-vida-seguro}
SbD-ToE defines security gates from classification through to deploy. This supports the CRA obligation to ensure security "by design" and during maintenance.

What still falls outside this technical basis is the explicit formalisation of:

- the economic operator role
- support period
- and communication of the end of support to the user

**Action:** Consolidate into a single document: "CRA Control Matrix" listing controls by phase (design, build, test, release, maintenance).

### 2. Vulnerability Handling & Coordinated Disclosure {#2-vulnerability-handling--coordinated-disclosure}
SbD-ToE already provides for internal triage (SCA, scans, tests). The CRA also requires an external channel for researchers or users to report flaws.

**Action:** Create a public page with the disclosure policy (Scope, PGP key, response time, no legal action against good-faith reporting).

### 3. SBOM and Transparency {#3-sbom-e-transparência}
Continuous SBOM (Ch. 05) is the basis for providing visibility. The CRA may require a standardised format (CycloneDX/SPDX).

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

**Action:** "no-critical-known" gate before release; exceptions only with board approval (maximum criticality).

### 7. Product Security Documentation {#7-documentação-de-segurança-do-produto}
Produce a guide for administrators/users: secure configurations, updating, security contact, logging policies.

For a `CRA` reading, this guide must also make explicit:

- security point of contact
- type and duration of the support period
- end-of-support date communicated to the user

**Action:** Template derived from Ch. 04 (architecture) + Ch. 11 (secure deploy).

### 8. Post-Market Monitoring {#8-monitorização-pós-comercialização}
Ch. 12 already defines monitoring; add specific panels: "Known vulnerabilities vs. patch status".

**Action:** Dashboard with: total open vulns, mean time to patch, percentage of SLA met.

### 9. Exceptions {#9-exceções}
Adapted exception policy: critical RCE vulnerabilities can never be an exception; others only with robust compensation and a short TTL.

**Action:** Add a "CRA Unacceptable Exceptions" table to the central policy.

### 10. Supply Chain {#10-cadeia-de-fornecimento}
Expand beyond software: firmware, cryptographic modules, integrated devices.

**Action:** Physical checklist: component origin, firmware hash, secure update channel.

### 11. Conformity and CE Marking {#11-conformidade-e-marcação-ce}
Outside the technical scope of SbD-ToE. Requires a legal documentary process.

**Action:** Create a separate GRC/Legal swimlane; keep the technical controls referenced as security evidence.

## Intentional Gaps {#lacunas-intencionais}

| Area | Reason for the Gap | Risk if Ignored | Proposed Mitigation |
|------|------------------|-------------------|--------------------|
| EU Declaration of Conformity | Requires a legal approach | Market failure / penalties | Involve the legal team early |
| Notified Body | Regulated process outside the manual | Certification delay | Define criteria for when to involve one |
| Official External SBOM Format | Evolution of standards | Incompatibility with buyer requirements | Implement a CycloneDX export plugin |
| External Disclosure Channel | Universality of the manual | Loss of responsible reporting | Publish the policy on the website /SECURITY.md |
| Firmware/Hardware Secure Boot | Focus on application software | Physical vector ignored | Add a physical supply chain checklist |

## Simple CRA Metric (Self-Assessment) {#métrica-simples-cra-autoavaliação}

Answer YES to the following points:
1. Is there a product security policy covering design→maintenance? ✓
2. Is a complete SBOM generated per release? ✓
3. Is there a public vulnerability disclosure channel? ✓
4. Is the patch SLA documented and monitored? ✓
5. Is there a gate that blocks releases with a known critical CVE? ✓
6. Is a post-market vulnerability dashboard active? ✓
7. Is a sanitised external SBOM export available to customers/regulators? ✓
8. Does the exception policy define unacceptable vulnerabilities? ✓
9. Is the Product Security Guide published? ✓
10. Is the active exploitation reporting process documented? ✓

≥8/10 → Good CRA technical basis. `<`6 → Prioritise SBOM, patching, disclosure, critical gating.

## Priority Actions (Initial Roadmap) {#ações-prioritárias-roadmap-inicial}

1. Formalise the secure lifecycle policy (integrate CRA requirements and support period) 
2. Implement an external disclosure channel (security.txt + page) 
3. Adjust the pipeline with a "no critical known" gate 
4. Define the CRA patch SLA and tracking metrics 
5. Generate SBOM and a CycloneDX export per release 
6. Create a product security guide + contact point + end of support 
7. Create an active exploitation reporting runbook 
8. Add a post-market dashboard 
9. Physical supply chain checklist (if applicable) 
10. CE Conformity swimlane (Legal + GRC)

## References {#referências}

- **Cyber Resilience Act**: Regulation (EU) 2024/2847 (CELEX: [32024R2847](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847))
- SbD-ToE Manual Chapters 01–14 
- ENISA Guidance on Product Security & Vulnerability Disclosure 
- ISO/IEC 29147 (Vulnerability Disclosure), ISO/IEC 30111 (Vulnerability Handling)
- CycloneDX / SPDX specifications

**Version:** 1.0  
**Date:** November 2025  
**Next review:** May 2026
