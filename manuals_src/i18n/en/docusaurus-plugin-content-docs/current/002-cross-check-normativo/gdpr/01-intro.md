---
id: intro
title: GDPR - Normative cross-check
description: How SbD-ToE covers the technical requirements of the GDPR (EU 2016/679)
tags: [cross-check, gdpr, privacidade, protecao-dados, art32, privacy-by-design]
sidebar_position: 7
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/gdpr/01-intro.md
  source_sha256: 480a8909aeb3d3a6318484b91ebc0eb5fa559a29af59a9b12afd11f3f4819adc
  source_commit: 5bc57a2de453d4a50f78edcfb2b9546615b20690
  target_sha256: 61f991d2f86c162846b49ef43e9dccd6dc2096a9c2c9c96e9a38448c455a226b
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [avaliacao, cycle_iteration, gap_family, gdpr_controller, gdpr_dpbd, gdpr_dpo, gdpr_pseudonymisation, gdpr_security_of_processing, lifecycle_phase, mcp_reading_programa, normative_empirical, piso_limiar, piso_relacao, practitioner_manual, programme_line, requirement_runtime, role_juridico, sbdtoe_sbd, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: ff651986a8b37ea80ba32ae26ab24734d245212e64c51a5638f6149fa37c2a59
  translated_at: 2026-09-27T23:03:29Z
  stamped_at: 2026-09-27T23:03:29Z
  reviewed_by: null
---

# GDPR: Normative cross-check

> For practical implementation, see the [SbD-ToE 4 GDPR Playbook](/sbd-toe/cross-check-normativo/gdpr/playbook).
>
> For universal application patterns, see the SbD-ToE core chapters (01–14).

## Scope {#âmbito}

The **General Data Protection Regulation (GDPR)** - **Regulation (EU) 2016/679** (CELEX: [32016R0679](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679)) - establishes principles and obligations for the processing of personal data. This cross-check focuses on the **technical dimension** aligned with SbD-ToE (security and engineering), recognising that several obligations are **legal and organisational**: legal bases, information to the data subject, formal response to requests, DPIA methodology, the DPO and international transfers. These stay out of scope of the Manual. The technical capability to exercise data subjects' rights, on the other hand, is prescribed (PRI-003, PRI-006; CTX-RGPD-R01 to R05).

It is suggested that SbD-ToE be used as the technical core for the articles that require security measures, privacy-by-design and incident management, working with Legal/GRC for the rest.

## What this Manual covers and what stays out {#o-que-este-manual-cobre-e-o-que-fica-de-fora}

SbD-ToE is centred on the application: requirements, architecture, code, dependencies, pipeline, deploy and operation of the software. For each GDPR obligation, the Manual answers in one of three categories, and no obligation is left unanswered:

- **Covers**, and states how: catalogue requirement, policy, floor or requirement added by the regime, or engineering evidence for a duty that sits on another plane.
- **Declared gap**: what the Manual does not cover by default, with what is missing.
- **Out of scope**: what the Manual does not address, with the reason.

The complete list, obligation by obligation, is generated from the coverage matrix and is in [Applicable requirements — What this Manual covers and what stays out](./requisitos-aplicaveis#cobertura). Where this page and the list diverge, the list prevails.

**Out of scope, by programme decision:**
- Security of the entity as a whole (corporate network and administration channels, EDR, patching of operating systems and equipment, inventory and classification of all assets): the Manual is centred on the application.
- The legal side: legal bases, formal response to the data subject and deadlines, DPIA methodology, the data protection officer, international transfers. The Manual covers the technical part of the rights (PRI-001 to PRI-007).

---

## PART I: NORMATIVE ANALYSIS (GDPR → SbD-ToE) {#parte-i-análise-normativa-gdpr--sbd-toe}

### Principles (Art. 5) {#princípios-art-5}
They require: lawfulness, fairness and transparency; purpose limitation; data minimisation; accuracy; storage limitation; integrity and confidentiality; accountability.

SbD-ToE coverage:
- Ch. 01: Classification and identification of data by criticality (supports minimisation/retention)
- Ch. 02: Security requirements (confidentiality, integrity, availability)
- Ch. 04: Secure architecture (segregation, encryption, proportionate logging)
- Ch. 11: Validation before production (confirmation of requirements)
- Ch. 02 (PRI catalogue): minimisation (PRI-001), retention with effective erasure (PRI-002), accuracy and rectification (PRI-003), inventory of purposes and recipients (PRI-004), PII in logs (PRI-005)

**Out of scope:** lawfulness and legal bases (Article 5(1)(a) and Article 6). This is a legal matter, handled with Legal/the DPO.

---

### Consent and data subjects' rights (Articles 7, 8 and 12–22) {#direitos-dos-titulares-arts-7-22}
They require that the data subject can give and withdraw consent and exercise the rights of access, rectification, erasure, restriction, portability and objection, and that solely automated decisions have safeguards.

SbD-ToE coverage:
- Ch. 02 (PRI catalogue): access, rectification, erasure and export in a machine-readable format, through a tested mechanism, with propagation to the recorded recipients (PRI-003, PRI-004; Articles 15(3), 16, 17, 19 and 20(1)) and verification of the requester's identity (PRI-003, AUT-009; Article 12(6))
- Restriction of processing (CTX-RGPD-R01; Article 18) and erasure of data made public (CTX-RGPD-R02; Article 17(2))
- Consent and objection, including automated signals such as Global Privacy Control (PRI-006; CTX-RGPD-R04; Articles 7 and 21)
- Age verification and parental consent, where applicable (CTX-RGPD-R03; Article 8(2))
- Solely automated decisions with human intervention, the right to express a point of view and to contest (CTX-RGPD-R05; Article 22)

**Declared gaps:** direct transmission of data between controllers, where technically feasible (Article 20(2)); the request channel and the informative content of the response to the data subject (Articles 12(2) and 15(1)) are covered only in their technical part.

**Out of scope:** the formal response to the data subject, with deadlines, reasons and fees (Articles 11(2), 12(3) to (5) and 18(3)), and information to the data subject, including privacy notices (Articles 12(1), 13, 14 and 21(4)). These are legal and communication matters, handled with Legal/the DPO.

---

### Data protection by design and by default (Art. 25) {#privacy-by-designdefault-art-25}
It requires measures that implement the data-protection principles by design and that ensure that, by default, only personal data which are necessary for each specific purpose are processed (amount, extent, storage, accessibility).

SbD-ToE coverage:
- Ch. 04: Secure architectural patterns (pseudonymisation, segmentation)
- Ch. 06–07: Pipelines with gates to prevent exposures (secrets, excessive data)
- Ch. 11: Pre-deploy checklists (privacy parameters by default)
- Ch. 03: privacy threat analysis with LINDDUN at all levels when there is personal data, in a light form at L1 (THR-003)
- Ch. 02: privacy by default in user-facing settings (PRI-007) and minimisation (PRI-001)

---

### Records of Processing Activities (Art. 30) {#registos-de-atividades-art-30}
Requires a ROPA (Record of Processing Activities).

**Supports evidence:** the inventory of purposes and recipients per dataset (PRI-004, mandatory at any level: CTX-RGPD-P04) and the application inventory (CLA-008) feed the Article 30 record. The record itself, as a controller's document, is maintained by Legal/the DPO, with reference to the application IDs.

---

### Security of Processing (Art. 32) {#segurança-do-tratamento-art-32}
It requires technical and organisational measures appropriate to the risk, including, as appropriate: pseudonymisation and encryption, confidentiality/integrity/availability/resilience, restoring availability and regular testing of effectiveness.

SbD-ToE coverage:
- Ch. 02: Minimum requirements per level (includes encryption, IAM, hardening)
- Ch. 04: Architecture (segregation, key management)
- Ch. 05: Vulnerability and dependency management (SBOM/SCA)
- Ch. 10: Security testing and continuous assessment
- Ch. 12: Monitoring, continuity and exercises

Appropriateness to risk is achieved through classification (CLA-001, CLA-003) and the threat model, including the risk to data subjects (THR-001, THR-002). Backups with tested restoration include personal data (OPS-016; CTX-RGPD-P03).

---

### Personal Data Breach Notification (Art. 33/34) {#notificação-de-violação-art-3334}
It requires notifying the competent supervisory authority without undue delay and, where feasible, not later than 72 h after having become aware of the breach, unless it is unlikely to result in a risk (Art. 33); where there is a high risk, communicating it to the data subjects (Art. 34).

SbD-ToE coverage:
- Ch. 12: Incident detection, classification and response; runbooks
- Ch. 14: RACI for decisions and communications

**Coverage:** deadlines, criterion and minimum content of the notification to the supervisory authority (Policy 32 §6 and §6.1) and recording of all breaches, notified or not, with the reasons for the decision (CTX-RGPD-R06). **Declared gap:** the minimum content of the communication to data subjects (Article 34(2)). **Out of scope:** the forms and the relationship with the supervisory authority.

---

### DPIA - Data Protection Impact Assessment (Art. 35) {#dpia---avaliação-de-impacto-art-35}
Requires a DPIA where the processing is likely to result in a high risk.

SbD-ToE coverage (partial):
- Ch. 03: Threat Modelling (can serve as a technical basis)
- Ch. 04: Technical mitigation measures

**Supports evidence:** the threat model with LINDDUN (THR-003) and the systematic description of the processing (THR-002) serve as the technical annex to the DPIA. **Out of scope:** the DPIA methodology, the list of processing operations subject to it and prior consultation with the authority (Articles 35(3) and (9), and 36), which are legal matters. **Declared gap:** review by the DPO exists only at L3 and concerns the LINDDUN analysis, not the DPIA (Article 35(2)).

---

### Processors (Art. 28) and Contracts {#subcontratantes-art-28-e-contratos}
Requires contracts with processors containing data protection clauses.

SbD-ToE coverage:
- Ch. 14: Supplier/contractor lifecycle and security clauses
- Ch. 05: Component transparency (SBOM) and third-party risk

**Coverage:** the contract under Article 28(3) is mandatory at any level whenever a processor processes personal data (CTX-RGPD-P01; including those that receive personal data in AI prompts: Policy 18 §10.3, CTX-RGPD-P02), with security, support for rights and erasure or return at the end of the service (points (c), (e) and (g); PRI-002, PRI-003). **Out of scope:** the legal content of the clauses and the transfer mechanisms (SCC, BCR, derogations). **Declared gap:** a location and transfer rule for processors outside the EEA that are not AI suppliers (Articles 44 and 46).

---

## PART II: Convergences/Interactions {#parte-ii-convergênciasinterações}

- Incidents involving personal data may require dual notification: GDPR (72h) + sectoral regimes (e.g. NIS2/DORA). A single runbook with a reporting fork is suggested.
- Art. 32 measures complement NIS2/DORA controls (same technical basis; reusable evidence).

---

## Summary: out of scope and declared gaps {#lacunas-intencionais-resumo}

What the Manual covers is in the sections above; this table brings together what stays out of scope, with the reason, and the declared gaps.

| Area | Category | Reason / what is missing |
|---|---|---|
| Legal bases, information to the data subject (Articles 6, 13, 14) | Out of scope | Legal matter: Legal/DPO |
| Formal response to data subjects' requests (deadlines, reasons) | Out of scope | “Formal rights”; the technical capability is in PRI-003 and PRI-006 |
| DPIA methodology, prior consultation | Out of scope | Legal and organisational methodology; technical annexes in THR-002 and THR-003 |
| Status and designation of the DPO | Out of scope | Legal organisation |
| Joint controllers and representative in the EU (Articles 26, 27) | Out of scope | Legal relationship |
| Transfer regime (SCC, BCR, derogations) | Out of scope | Legal/DPO |
| Location and transfer of non-AI processors outside the EEA | Declared gap | Only the AI supplier slice has a rule (Articles 44 and 46) |
| Data protection policy | Declared gap | There is no dedicated policy among the 39 (Article 24(2)) |
| Content of the communication to data subjects | Declared gap | Article 34(2) |
| Involvement of the DPO in design, DPIA and processors | Declared gap | Article 38(1) |
| Direct transmission between controllers | Declared gap | Article 20(2) |

---

## Simple Metric (Self-Assessment) {#métrica-simples-autoavaliação}

Each “yes” scores one point:
1. Are the apps that process personal data classified, and do they have Article 32 requirements implemented?
2. Privacy by default configured (PRI-007; minimal logs, limited retention, encryption by default)?
3. Is there a DPIA process with technical annexes (TM with LINDDUN, controls) where applicable?
4. Incident runbook with an active 72h clock and the minimum content of Policy 32 §6.1?
5. Processors: contract under Article 28(3), with technical clauses and verified security?

≥4/5 → Good technical coverage. `<`3 → Prioritise Art. 32, PbD and 72h incidents.

---

## References {#referências}

- **GDPR**: Regulation (EU) 2016/679 (CELEX: [32016R0679](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679))
- ENISA - Guidelines on Security of Personal Data Processing
- EDPB - Guidelines (DPIA, Breach Notification)
- SbD-ToE Chapters 01–14

**Version:** 1.1  
**Date:** September 2026  
**Next review:** March 2027
