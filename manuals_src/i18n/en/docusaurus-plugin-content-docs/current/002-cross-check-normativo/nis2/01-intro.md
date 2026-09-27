---
id: intro
title: NIS2 - Normative cross-check
description: What SbD-ToE covers, the gaps it declares and what it leaves out of scope against the NIS2 Directive (EU 2022/2555)
tags: [cross-check, nis2, diretiva, ciberseguranca, incident-reporting, governance]
sidebar_position: 3
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/nis2/01-intro.md
  source_sha256: 71dadf3eb2b5f498e996aa5670bc08d050a0f9d4c68596666e449660afd0bb6e
  source_commit: 5bc57a2de453d4a50f78edcfb2b9546615b20690
  target_sha256: 814b30da96eb1aeecb15aae71a8061ec7151e41137826a7d1413b555abe26e4a
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [alcada, avaliacao, chapter_role, cycle_iteration, eu_management_body, gap_family, layer, lifecycle_phase, mapping, mcp_reading_programa, nis2_crm_measures, nis2_early_warning, nis2_essential_entity, nis2_significant_incident, normative_empirical, piso_limiar, piso_relacao, practitioner_manual, programme_line, requirement_runtime, role_juridico, sbdtoe_sbd, verificacao_check, verification_taxonomy]
  glossary_sha256: af3f16e8472060a103f3bc5703e8533f1275a68bcbbd82c43f1eacb7fa5f5d73
  translated_at: 2026-09-27T23:03:33Z
  stamped_at: 2026-09-27T23:03:33Z
  reviewed_by: null
---

# Normative cross-check - NIS2

## Scope {#âmbito}

**Directive (EU) 2022/2555 (NIS2)** (CELEX: [32022L2555](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555)) updates the European cybersecurity framework for essential entities and important entities in 18 sectors, strengthening governance, cybersecurity risk-management measures and incident reporting obligations. Member States had until 17 October 2024 to transpose NIS2; NIS1 was repealed on 18 October 2024.

In the spirit of NIS2, "having controls" is not enough - operational capability and management accountability must be demonstrated. SbD-ToE, built top-down and attentive to multiple references, fits naturally into this ethos: it delivers reusable processes, policies and technical artefacts, while deliberately leaving some variables open to preserve the universality of the manual.

This document presents:

1. **PART I: NORMATIVE ANALYSIS** - article-by-article mapping of NIS2 requirements to SbD-ToE chapters, identifying what the Manual covers, the gaps it declares, what stays out of scope and the integration steps.
2. **PART II: SYNTHESIS AND REFERENCES** - a consolidated view of the NIS2/SbD-ToE relationship and normative references.

## What this Manual covers and what stays out {#o-que-este-manual-cobre-e-o-que-fica-de-fora}

SbD-ToE is centred on the application: requirements, architecture, code, dependencies, pipeline, deploy and operation of the software. For each NIS2 obligation, the Manual answers in one of three categories, and no obligation is left unanswered:

- **Covers**, and states how: catalogue requirement, policy, floor or requirement added by the regime, or engineering evidence for a duty that sits on another plane.
- **Declared gap**: what the Manual does not cover by default, with what is missing.
- **Out of scope**: what the Manual does not address, with the reason.

The complete list, obligation by obligation, is generated from the coverage matrix and is in [Applicable requirements — What this Manual covers and what stays out](./requisitos-aplicaveis#cobertura). Where this page and the list diverge, the list prevails.

**Out of scope, by programme decision:**
- Security of the entity as a whole (corporate network and administration channels, EDR, patching of operating systems and equipment, inventory and classification of all assets): the Manual is centred on the application.
- The entity's business continuity, crisis management and BIA. The Manual covers backups, tested restoration and recovery of the application (OPS-016, OPS-017).

---

## PART I: NORMATIVE ANALYSIS {#parte-i-análise-normativa}

### Article 20 - Governance and accountability {#artigo-20---governação-e-responsabilização}

**Normative content**

Art. 20 places the management body at the centre: it approves the cybersecurity risk-management measures, oversees their implementation and can be held liable for infringements. It also requires training for the members of the management body (and encourages regular training for employees).

**SbD-ToE coverage**

| NIS2 requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Approval of measures by the management body | Ch. 14, Ch. 02 | Formal approval of the governance model and the policies by senior management (GOV-001); approval of the Article 21 measures by the management body is a declared gap |
| Oversight of implementation | Ch. 12, Ch. 14 | Metrics, operational evidence, monitoring and escalation |
| Training of the management body | Ch. 13 | Partial: Policy 37 provides only “Executive awareness” at L1; mandatory training of the management body and regular training of non-technical staff remain a declared gap |

**What SbD-ToE covers**

- Defines the technical baseline of requirements and policies (Ch. 02) and the applicable governance/approval chain (Ch. 14).
- Establishes cycles of oversight, monitoring and operational evidence (Ch. 12), which can be linked to management accountability.
- Prescribes training and onboarding for technical roles and third parties with access (Ch. 13); training of the management body is a declared gap.

**Declared gaps**

The Manual requires formal approval, by senior management, of the governance model and the policies (GOV-001), but does not assign to the management body the approval of the Article 21 measures as a whole, oversight of their implementation or personal accountability. Nor does it require the designation of a person who reports directly to the management body, and acceptance of residual risk goes no higher than the CISO. The legal form of the approval chain is, by choice, left to the organisation.

**How to comply**

It is suggested to record, in Ch. 14, how the management's approval and oversight chain was formalised, using the Ch. 02 catalogue as the technical basis and keeping evidence of the periodic training of the management body, which the organisation provides beyond the Manual (Article 20).

---

### Article 21 - Cybersecurity risk-management measures {#artigo-21---medidas-de-gestão-de-risco-de-cibersegurança}

**Normative content**

Article 21(2) calls for measures that, based on an all-hazards approach, cover at least: policies on risk analysis and information system security; incident handling; business continuity (backup management, disaster recovery) and crisis management; supply chain security; security in systems acquisition, development and maintenance, including vulnerability handling and disclosure; assessment of the effectiveness of the measures; basic cyber hygiene practices and cybersecurity training; cryptography and encryption; human resources security, access control and asset management; multi-factor authentication and secured communications. For providers of DNS services, TLD name registries, cloud computing services, data centre services, CDN, managed services and managed security services, online marketplaces, online search engines, social networking services platforms and trust service providers, Implementing Regulation (EU) 2024/2690 specifies these measures, including monitoring and logging (Annex, point 3.2).

In 2024/2025, the Commission and ENISA published technical guidance and practical mappings with examples of evidence for implementing these measures - extremely useful for audit.

**SbD-ToE coverage**

| NIS2 requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Policies on risk analysis | Ch. 02, Ch. 03 | Security requirements, threat modelling |
| Incident handling | Ch. 12 | Detection, response, post-incident |
| Business continuity/crisis management (backups, DR) | Ch. 11, Ch. 12 | Response runbooks and exercises; backups with tested restore (OPS-016); recovery objectives and procedure for the application (OPS-017, L2/L3); the entity's BCM and crisis management outside the Manual |
| Supply chain security | Ch. 05, Ch. 14 | SBOM/SCA, dependencies, contractual requirements |
| Security in development | Ch. 06, Ch. 07, Ch. 08 | Secure development, CI/CD, IaC |
| Effectiveness assessment | Ch. 10, Ch. 12 | Security testing, continuous monitoring |
| Cyber hygiene/training | Ch. 13 | Training for technical roles and for third parties with access (TRN-002, TRN-007); cyber hygiene and awareness for all staff and the management body remain a declared gap |
| IAM, privileged accounts, cryptography | Ch. 02, Ch. 04, Ch. 14 | MFA (AUT-001); access review (ACC-010, GOV-014); privileged and administration accounts (GOV-016, GOV-017); key lifecycle and certificate inventory (ENC-007); cryptographic agility (ENC-003); for relevant entities, mandatory at any level (CTX-NIS2-P12, P13, P18 to P21) |
| Asset management and HR security | Ch. 01, Ch. 13 | Inventory of applications and components (CLA-008, DEP-001); the inventory of all assets is entity security, out of scope, and the asset handling policy is a declared gap; HR security stays out of scope (personnel management), except for onboarding and offboarding |
| Vulnerability handling and disclosure | Ch. 05, Ch. 10, Ch. 14 | Dependencies, SCA, testing; coordinated disclosure and handling of external reports (GOV-015; CTX-NIS2-P14, P15). Patching of operating systems, network equipment and off-the-shelf software is entity security, out of scope of the Manual |
| Logging and monitoring | Ch. 12 | Observability, SIEM, alerts; for relevant entities, regular analysis, threshold-based alarms and backup of logs are mandatory (LOG-004, LOG-007, OPS-005, LOG-005; CTX-NIS2-P03 to P06); network traffic and redundancy of monitoring remain a declared gap |

**What SbD-ToE covers**

- **Technical policies and controls** (Ch. 02 - Security Requirements).
- **Criticality classification** and proportional risk (Ch. 01 - Application Classification).
- **Threat modelling** (Ch. 03).
- **Supply chain**: SBOM/SCA, dependencies (Ch. 05).
- Secure **CI/CD & IaC** (Ch. 07, Ch. 08); containers/runtime (Ch. 09).
- **Testing** (Ch. 10) and secure deploy (Ch. 11).
- **Monitoring, logging, response and continuous improvement** (Ch. 12).
- **Governance & contracting** (Ch. 14), including third-party assessment.

**Declared gaps and out of scope**

The Manual is centred on the application. Out of scope, with the reason recorded, are physical and environmental security, workstations and removable media, human resources management, business continuity and crisis management, and the security of the entity as a whole (inventory of all assets, EDR, patching of operating systems). Among the declared gaps are cyber hygiene for all staff, the asset handling policy and European certification in procurement (Article 24). “Closed” formats, such as log fields and policy templates, remain deliberately generic. The detail, requirement by requirement, is in [Applicable requirements](./requisitos-aplicaveis#cobertura).

**How to comply**

It is suggested to use the Ch. 02 catalogue as the basis of a technical SoA, complemented by `01/03/05/10/12/14`, and to align the evidence with the ENISA technical guidance (evidence examples and mappings). The NIS2 context is declared per entity and inherited by all applications; for the relevant entities under Implementing Regulation (EU) 2024/2690, the PERTINENTE grade also applies. Levels L1–L3 still result from the classification of each application (Ch. 01) and do not correspond to the categories of essential entities and important entities.

---

### Article 23 - Incident reporting {#artigo-23---reporte-de-incidentes}

**Normative content**

NIS2 defines a reporting track for significant incidents:

- **Early warning**, to the CSIRT or, where applicable, the competent authority, without undue delay and within 24 h of becoming aware of the significant incident.
- **Incident notification**, with an initial assessment, within 72 h of becoming aware.
- **Final report** within 1 month of the incident notification (72h), with intermediate reports at the request of the CSIRT/authority.

**SbD-ToE coverage**

| NIS2 requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Detection and response | Ch. 12 | Detection, response and post-incident process |
| Escalation and responsibilities | Ch. 14 | Roles and responsibilities |
| Severity classification | Ch. 01, Ch. 12 | Impact criteria, incident classification |
| Mandatory response process | Ch. 12 | IRP mandatory at any level in the NIS2 context (CTX-NIS2-P01), with a post-mortem of significant incidents and review of the affected artefacts (Policy 32 §4.6) |

**What SbD-ToE covers**

- Detection and response process, with post-incident (Ch. 12).
- Escalation roles and responsibilities (Ch. 14).
- Impact criteria (Ch. 01) that support severity classification.

**Coverage and declared gaps**

The incident record collects the impact data (Policy 32 §4.3). The significant incident criterion (CTX-NIS2-R02) and, for relevant entities, the thresholds and the aggregation of recurring incidents under Implementing Regulation (EU) 2024/2690 (CTX-NIS2-R03) decide whether the incident is notifiable. The deadlines and minimum content of each stage are in Policy 32 §6 and §6.1. The P1–P4 scale is internal and does not replace these criteria. The Manual does not replace the CSIRT's forms or channels. Notification to the recipients of the service (Article 23(1)), communication of significant cyber threats to recipients (paragraph 2) and information to the public when the CSIRT requires it (paragraph 7) remain a declared gap.

**How to comply**

It is suggested to start from the impact data of Policy 32 §4.3 and the minimum content of §6.1 and to connect the SIEM/ITSM exporters to the national CSIRT's forms, within the 24 h, 72 h and 1 month deadlines.

---

### Supply chain and third-party security {#segurança-da-cadeia-de-fornecimento-e-terceiros}

**Normative content**

NIS2 emphasises supply chain security and security in acquisition/development/maintenance (Article 21), including verification of critical suppliers and verifiable technical measures.

**SbD-ToE coverage**

| NIS2 requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Inventory of dependencies and SBOM | Ch. 05 | SBOM, SCA, update policies |
| Technical contractual requirements | Ch. 14 | Governance and contracting, assessment practices (GOV-006, GOV-007); for relevant entities, supply chain policy at any level (Policy 33; CTX-NIS2-P07 to P09) |
| Supplier exit | Ch. 14 | Offboarding with revocation of access and deletion or return of data (Policy 33 §7.1) |

**What SbD-ToE covers**

- Inventory of dependencies and SBOM, SCA, update policies (Ch. 05).
- Technical contractual requirements (Ch. 14) and assessment practices.
- Supplier offboarding, with revocation of access and deletion or return of data (Policy 33 §7.1).

**Out of scope and declared gaps**

Registration with the authority, designation of a representative and the legal content of contracts belong to the legal and administrative plane and stay out of scope. The declared gaps are: requiring ICT products certified under the CSA where the Member State so imposes (Article 24(1)), the coordinated EU risk assessments in the selection criteria (Article 22), the overall quality of products and the supplier's secure development procedures as an explicit criterion, security updates throughout the whole lifetime, and background checks on the supplier's staff.

**How to comply**

It is suggested to extend the Ch. 05 supplier register with the fields required by the national authority (following local guides/portals and the ENISA notes).

---

### Continuity, crisis and operations {#continuidade-crise-e-operação}

**Normative content**

NIS2 calls for business continuity, crisis management, tested backups and DR, and effective monitoring/logging (Article 21).

**SbD-ToE coverage**

| NIS2 requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Response/recovery runbooks and exercises | Ch. 12 | Runbooks, exercises, tests |
| Backups with restore tests | Ch. 12 | Backups with tested restore ([`OPS-016`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#catálogo-ops---monitorização-e-operações)), with a cadence by level |
| Logging/observability "by design" | Ch. 12 | Logging, observability, retention |

**What SbD-ToE covers**

- Response/recovery runbooks and exercises (Ch. 12).
- Backups with tested restore (OPS-016) and recovery objectives and procedure for the application (OPS-017).
- Logging/observability "by design" (Ch. 12), with guidance on retention that can be aligned with standards.

**Coverage and out of scope**

The minimum log attributes (LOG-002), the event catalogue (OPS-002) and retention per log type (LOG-005; Policy 29 §7) are prescribed; for relevant entities, regular analysis, threshold-based alarms and backup of logs are mandatory (CTX-NIS2-P03 to P06). The periods in Policy 29 §7 are the Manual's choice: the most demanding among law, national legislation, supervisors and sector prevails. Business continuity, corporate BCM and the entity's crisis management stay out of scope of the Manual, which is centred on the application: the P1 war room of Policy 32 is incident response, not crisis management.

**Redundancy and continuity**

Backups with tested restore (OPS-016) and recovery of the application (OPS-017) are prescribed. At least partial redundancy of the systems (Implementing Regulation (EU) 2024/2690, Annex, point 4.2.4) applies only to the relevant entities, as a requirement of the NIS2 context (see [Applicable requirements](/sbd-toe/cross-check-normativo/nis2/requisitos-aplicaveis)). The entity's business continuity and crisis management remain outside the Manual.

**How to comply**

It is suggested to align with ENISA guidance the sources the Manual covers (application, IAM, cloud audit) and retention, gathering evidence examples for audit. The entity's sources, such as the network and EDR, come from entity security, out of scope of the Manual.

---

## PART II: SYNTHESIS AND REFERENCES {#parte-ii-síntese-e-referências}

### Synthesis of NIS2/SbD-ToE coverage {#síntese-da-cobertura-nis2sbd-toe}

NIS2 calls for accountable management, measures with substance and reporting with deadlines. SbD-ToE provides the technical-operational core: policies, processes, testing, inventories, automation and evidence.

The Manual's answer to NIS2 has three parts. It covers, in the form stated for each requirement, the technical and operational baseline. It declares gaps where it falls short, such as training of the management body, cyber hygiene for all staff or asset management beyond applications. And it leaves out of scope, with the reason, the security of the entity as a whole, business continuity and the administrative relationship with the authorities. Submission templates and the legal details of contracts remain deliberately configurable.

The result is stable:

- **Today**, SbD-ToE provides a strong technical-operational foundation for NIS2-compatible practices.
- **Then**, when the organisation wants to defend NIS2 compliance, the main incremental work is to formalise approval and oversight by the management body, close the declared gaps that matter to it, take care of what stays out of scope of the Manual and link the minimum content of Policy 32 §6.1 to the national forms, on top of that existing baseline.

In this way, SbD-ToE remains useful in day-to-day practice, and NIS2 adds the layer of regulatory formality and supervision. Together, they offer a more sustainable compliance path than a purely checklist-driven reading.

### Sector, scope and penalties {#setor-âmbito-e-sanções}

NIS2 extends the scope to 18 sectors (Annexes I/II) and reinforces the distinction between essential and important entities. In many countries, there are national registries and self-registration deadlines for entities in scope; following official trackers helps to implement the local specificities.

In terms of penalties, the Directive requires Member States to provide, for infringements of Articles 21 or 23, administrative fines of a maximum of at least €10 M or 2 % of the total worldwide annual turnover for essential entities, and of at least €7 M or 1.4 % for important entities (whichever is higher).

### References {#referências}

- **NIS2 Directive**: Directive (EU) 2022/2555 (CELEX: [32022L2555](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555))
- **Art. 20** - Accountability of the management body and training obligation.
- **Art. 21** - Minimum cybersecurity risk-management measures ("all-hazards" approach).
- **Art. 23** - Incident reporting deadlines (24h/72h/1 month) and intermediate reports.
- **Art. 34** - Maximum administrative fines (€10M or 2%; €7M or 1.4%).
- **ENISA & European Commission (2024/2025)** - Technical guidance and practical mappings with examples of evidence for Article 21.
- **ENISA** - *Technical implementation guidance for NIS2 risk-management measures* (examples of evidence and mappings).
- **National NIS2 authorities** - Registration guides/portals and local requirements (examples: national NCSCs).

---

:::note Exceptions and control evidence

NIS2, like DORA, benefits from a formal process for compliance exceptions. Cases where a requirement does not apply, or where a temporary risk is accepted, are documented and reviewed periodically (GOV-004; Policies 03 and 05). In the Manual, the approval authority goes no higher than the CISO. Acceptance of residual risk by the management body and the requirement-by-requirement justification of the per-level exemptions that Implementing Regulation (EU) 2024/2690 asks for (Article 2) are declared gaps.

Ch. 14 (Governance and Contracting) of SbD-ToE provides the artefacts: exception register, risk acceptance criteria, approval authorities and remediation plan. The existence of this process is not a sign of weakness - it is evidence of mature governance and of conscious control over the organisation's risk profile.

:::
