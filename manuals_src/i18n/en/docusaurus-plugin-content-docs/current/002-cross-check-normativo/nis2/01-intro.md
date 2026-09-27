---
id: intro
title: NIS2 - Normative cross-check
description: How SbD-ToE covers, deliberately leaves open and can rapidly integrate the requirements of the NIS2 Directive (Directive (EU) 2022/2555)
tags: [cross-check, nis2, diretiva, ciberseguranca, incident-reporting, governance]
sidebar_position: 3
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/nis2/01-intro.md
  source_sha256: ed56bc3eeb54cdb5a364d502afae2e7a000d766503874a4402606b2c5228a6a0
  source_commit: 5c2b16d193f5e7fe0cc6b566c47e456677cca656
  target_sha256: e4632608d7607b1c4e7498601b7c87d0706c80156e86359c658c900aac323f8e
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [avaliacao, chapter_role, esquema_regime, eu_management_body, gap_family, layer, mapping, mcp_reading_programa, nis2_crm_measures, nis2_early_warning, nis2_essential_entity, nis2_significant_incident, normative_empirical, practitioner_manual, programme_line, requirement_runtime, sbdtoe_sbd, verificacao_check, verification_taxonomy]
  glossary_sha256: 2ae14a21f4f058c8b6407e4751c715b4136d395e7233f4a9c71e073837fabfdb
  translated_at: 2026-09-27T13:29:49Z
  stamped_at: 2026-09-27T13:29:49Z
  reviewed_by: null
---

# Normative cross-check - NIS2

## Scope {#âmbito}

**Directive (EU) 2022/2555 (NIS2)** (CELEX: [32022L2555](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555)) updates the European cybersecurity framework for essential entities and important entities in 18 sectors, strengthening governance, cybersecurity risk-management measures and incident reporting obligations. Member States had until 17 October 2024 to transpose NIS2; NIS1 was repealed on 18 October 2024.

In the spirit of NIS2, "having controls" is not enough - operational capability and management accountability must be demonstrated. SbD-ToE, built top-down and attentive to multiple references, fits naturally into this ethos: it delivers reusable processes, policies and technical artefacts, while deliberately leaving some variables open to preserve the universality of the manual.

This document presents:

1. **PART I: NORMATIVE ANALYSIS** - an article-by-article mapping of the NIS2 requirements to SbD-ToE chapters, identifying existing coverage, intentional gaps and integration steps.
2. **PART II: SYNTHESIS AND REFERENCES** - a consolidated view of the NIS2/SbD-ToE relationship and normative references.

---

## PART I: NORMATIVE ANALYSIS {#parte-i-análise-normativa}

### Article 20 - Governance and accountability {#artigo-20---governação-e-responsabilização}

**Normative content**

Art. 20 places the management body at the centre: it approves the cybersecurity risk-management measures, oversees their implementation and can be held liable for infringements. It also requires training for the members of the management body (and encourages regular training for employees).

**SbD-ToE coverage**

| NIS2 requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Approval of measures by the management body | Ch. 14, Ch. 02 | Governance, approval chain and supporting technical baseline |
| Oversight of implementation | Ch. 12, Ch. 14 | Metrics, operational evidence, monitoring and escalation |
| Regular training for management | Ch. 13 | Training and onboarding programme |

**What SbD-ToE covers**

- Defines the technical baseline of requirements and policies (Ch. 02) and the applicable governance/approval chain (Ch. 14).
- Establishes cycles of oversight, monitoring and operational evidence (Ch. 12), which can be linked to management accountability.
- Prescribes a training and onboarding programme (Ch. 13).

**Intentional gaps**

Who signs the policies: the manual requires formal approval, but does not fix ex ante the exact legal form of the approval chain. This is deliberate: in purely technical contexts, operational approval may suffice; for a NIS2 reading, the accountability of the management body has to be explicitly formalised.

**How to comply**

It is suggested to record, in Ch. 14, how the management's approval and oversight chain was formalised, using the Ch. 02 catalogue as the technical baseline and keeping evidence of periodic training for management (as per Article 20).

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
| Business continuity/crisis management (backups, DR) | Ch. 11, Ch. 12 | Partial: runbooks, response exercises and tested rollback; backups, restore tests and disaster recovery of the systems not yet prescribed |
| Supply chain security | Ch. 05, Ch. 14 | SBOM/SCA, dependencies, contractual requirements |
| Security in development | Ch. 06, Ch. 07, Ch. 08 | Secure development, CI/CD, IaC |
| Effectiveness assessment | Ch. 10, Ch. 12 | Security testing, continuous monitoring |
| Cyber hygiene/training | Ch. 13 | Training and onboarding |
| IAM, cryptography | Ch. 02, Ch. 04 | Security requirements, secure architecture |
| Vulnerability management/patching | Ch. 05, Ch. 10 | Dependencies, SCA, testing |
| Logging and monitoring | Ch. 12 | Observability, SIEM, alerts |

**What SbD-ToE covers**

- **Technical policies and controls** (Ch. 02 - Security Requirements).
- **Criticality classification** and proportional risk (Ch. 01 - Application Classification).
- **Threat modelling** (Ch. 03).
- **Supply chain**: SBOM/SCA, dependencies (Ch. 05).
- Secure **CI/CD & IaC** (Ch. 07, Ch. 08); containers/runtime (Ch. 09).
- **Testing** (Ch. 10) and secure deploy (Ch. 11).
- **Monitoring, logging, response and continuous improvement** (Ch. 12).
- **Governance & contracting** (Ch. 14), including third-party assessment.

**Intentional gaps**

"Closed" taxonomies/formats: NIS2 sets out topics, but the detail (e.g. the exact list of log fields or policy templates) may vary between jurisdictions and sectors. SbD-ToE keeps generic models, so that they can be "plugged" into national/sectoral requirements.

**How to comply**

It is suggested to use the Ch. 02 catalogue as the basis of a technical SoA, complemented by `01/03/05/10/12/14`, and to align the evidence with the ENISA technical guidance (examples of evidence and mappings). Declare, in Ch. 01, that proportionality follows the NIS2 classes (essential/important) and the impact on services.

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

**What SbD-ToE covers**

- Detection and response process, with post-incident (Ch. 12).
- Escalation roles and responsibilities (Ch. 14).
- Impact criteria (Ch. 01) that support severity classification.

**Intentional gaps**

SbD-ToE does not set a canonical data model for incidents, nor an "official" severity taxonomy (the P1–P4 scale of Policy 31 is internal), nor the submission templates. This is intentional: DORA, NIS2 and HIPAA ask for different sets of fields and formats. The manual says "record the incident with mandatory fields", and the final set of fields comes from the applicable normative framework (in the case of NIS2, from national guidance and Article 23).

**How to comply**

It is suggested, in Ch. 12, to adopt a minimum schema (`incident.json/csv`) and to parameterise the fields according to NIS2 (e.g. probable cause, severity, consequences, IOCs, measures; cf. ENISA guides). Configure SIEM/ITSM exporters → files ready for submission within the deadlines (24h/72h/1 month).

---

### Supply chain and third-party security {#segurança-da-cadeia-de-fornecimento-e-terceiros}

**Normative content**

NIS2 emphasises supply chain security and security in acquisition/development/maintenance (Article 21), including verification of critical suppliers and verifiable technical measures.

**SbD-ToE coverage**

| NIS2 requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Inventory of dependencies and SBOM | Ch. 05 | SBOM, SCA, update policies |
| Technical contractual requirements | Ch. 14 | Governance and contracting, assessment practices |
| Portable architectures and exit plans | Ch. 04, Ch. 08 | Secure architecture, IaC |

**What SbD-ToE covers**

- Inventory of dependencies and SBOM, SCA, update policies (Ch. 05).
- Technical contractual requirements (Ch. 14) and assessment practices.
- Portable architectures and (technical) exit plans.

**Intentional gaps**

National lists of entities to be registered, designation procedures and legal contract requirements (these vary between Member States). Specific normative fields of national registries.

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
| Backups with restore tests | — | Not yet prescribed: only the pre-deploy snapshot (Policy 27 §3) and the backup of the secrets vault (Policy 18 §4) exist |
| Logging/observability "by design" | Ch. 12 | Logging, observability, retention |

**What SbD-ToE covers**

- Response/recovery runbooks and exercises (Ch. 12).
- Logging/observability "by design" (Ch. 12), with guidance on retention that can be aligned with standards.

**Intentional gaps**

Retention periods and exact log fields: these vary between NIS2, DORA and sectoral regimes; the manual defines "logs with mandatory fields" and leaves the final fields to be plugged in according to the applicable normative framework (NIS2 here). Broad business continuity, corporate BCM and institutional crisis management may also require artefacts outside the core manual.

**Gap to cover**

Backups, restore tests and disaster recovery of the systems that the Manual governs (Article 21(2), point (c); Implementing Regulation (EU) 2024/2690, Annex, points 4.1 and 4.2) are not yet prescribed. Rollback ([`DPL-005`](/sbd-toe/sbd-manual/deploy-seguro/addon/catalogo-requisitos-deploy#catálogo-dpl---deploy-seguro)) reverts a deployment; it does not recover data or systems.

**How to comply**

It is suggested to align the source matrix (app, IAM, network, cloud audit, EDR) and retention with the ENISA guidance, collecting examples of evidence for audit.

---

## PART II: SYNTHESIS AND REFERENCES {#parte-ii-síntese-e-referências}

### Synthesis of NIS2/SbD-ToE coverage {#síntese-da-cobertura-nis2sbd-toe}

NIS2 calls for accountable management, measures with substance and reporting with deadlines. SbD-ToE provides the technical-operational core: policies, processes, testing, inventories, automation and evidence.

The apparent gaps in the manual - who approves policies, rigid log/incident fields, submission templates and formats, legal details of contracts - are deliberate gaps: specific details that change between standards and countries and which SbD-ToE therefore leaves configurable.

The result is stable:

- **Today**, SbD-ToE provides a strong technical-operational foundation for NIS2-compatible practices.
- **Later**, when the organisation wishes to defend NIS2 compliance, the main incremental work consists of formalising management approval and oversight, external reporting schemes and national or sectoral requirements on top of that existing foundation.

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

NIS2, like DORA, benefits from a formal process for compliance exceptions. Cases where a specific requirement is not applicable or where a temporary risk is accepted must be documented, approved by the management body and reviewed periodically.

Ch. 14 (Governance and Contracting) of SbD-ToE provides the necessary artefacts: exception register, risk acceptance criteria, approval chain and remediation plan. The existence of this process is not a sign of fragility - it is evidence of mature governance and of conscious control over the organisation's risk profile.

:::
