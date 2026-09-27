---
id: playbook
title: "SbD-ToE 4 GDPR: Implementation Playbook"
description: Practical roadmap for aligning SbD-ToE with the technical requirements of the GDPR
tags: [playbook, gdpr, implementacao, privacy-by-design, art32]
sidebar_position: 8
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/gdpr/02-playbook.md
  source_sha256: 3b16718e312836a54fdb5efe43d0d39d9cc8234c493e5dcfffd3cd706f2087a7
  source_commit: 5bc57a2de453d4a50f78edcfb2b9546615b20690
  target_sha256: be5d7d46899747b415a44e4342f6a374bae4e930d5e55bd3ea7d702ba6a427d7
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [chapter_role, eu_startups, gap_family, gdpr_controller, gdpr_security_of_processing, lifecycle_phase, mapping, papel_suporte, practitioner_manual, requirement_runtime, role_juridico, sbdtoe_sbd, slug_threat_modeling, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: cc8d41815bbb654fe89e5e8185a7d3f5d9ff5e28d868f752f514b64f6106a625
  translated_at: 2026-09-27T23:03:30Z
  stamped_at: 2026-09-27T23:03:30Z
  reviewed_by: null
---

# SbD-ToE 4 GDPR: Implementation Playbook

## Overview {#visão-geral}

Objective: operationalise GDPR Articles 15–22, 25, 30, 32, 33–34 and 35 on the basis of the technical capabilities of SbD-ToE and integrate with Legal/the DPO.

Structure: Requirements → Action → Evidence. Reuse NIS2/DORA controls wherever possible.

What the Manual covers, the gaps it declares and what stays out of scope, obligation by obligation, are in [Applicable requirements — What this Manual covers and what stays out](./requisitos-aplicaveis#cobertura).

> 📚 **Supporting Resources:** For practical templates and implementation examples, see the [Example Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-toolchain-options) with reusable encryption toolchains, privacy KPIs and incident response processes.

---

## Quick Map: GDPR Art. → SbD-ToE {#mapa-rápido-gdpr-art--sbd-toe}

| GDPR Article | Requirement | SbD-ToE Chapter | Main Action |
|-------------|-----------|------------------|----------------|
| 5 | Principles | [Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Ch. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Minimisation, retention, security |
| 15–22 | Data subjects' rights | [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro) | Tested technical mechanism (PRI-003, PRI-006); formal response with Legal/the DPO |
| 25 | Privacy by design/default | [Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Ch. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro)–[Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro), [Ch. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Secure default configurations |
| 30 | ROPA | [Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Apps/data inventory + GRC record |
| 32 | Security of processing | [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | Encryption, IAM, testing, resilience |
| 33/34 | Personal data breach | [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Runbook: supervisory authority ≤ 72h (Article 33); data subjects without undue delay where there is a high risk (Article 34) |
| 35 | DPIA | [Ch. 03](/sbd-toe/sbd-manual/threat-modeling/intro), [Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro) | TM + technical annexes in the DPIA |

---

## Implementation Phases (≈ 4–6 months) {#fases-de-implementação--46-meses}

### Phase 1 (M0–M1): Governance and Framing {#fase-1-m0m1-governação-e-enquadramento}
1. Appoint the DPO, if applicable (a legal matter, out of scope of the Manual; the Manual assumes the role where there is personal data) and align the RACI ([Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro))  
2. Data protection policy approved by the organisation (the Manual does not include it among its policies: a declared gap against Article 24(2))  
3. Define the classification of personal data per application  
**Evidence:** Approval minutes; RACI; data/applications matrix

### Phase 2 (M1–M2): Inventory & ROPA {#fase-2-m1m2-inventário--ropa}
1. Maintain the inventory of purposes and recipients per personal dataset (PRI-004, mandatory at any level)  
2. Record the ROPA in a GRC tool (Article 30 fields), fed by that inventory  
3. Link SbD-ToE app IDs to the ROPA  
**Evidence:** ROPA export; ID mapping

### Phase 3 (M2–M3): Privacy by Design/Default (Art. 25) {#fase-3-m2m3-privacy-by-designdefault-art-25}
1. Ch. 02 PRI requirements applied: minimisation (PRI-001), retention with effective erasure (PRI-002), PII in logs (PRI-005) and privacy by default (PRI-007)  
2. Default configs: minimal collection, encryption at rest/in transit  
3. Pipeline gate: block on excessive collection (schema linting, for example)  
**Evidence:** PbD catalogue; pipelines; blocking examples

### Phase 3-A (M2–M3): Data subjects' rights (Articles 15–22) {#fase-3-a-m2m3-direitos-dos-titulares-arts-1522}
1. Tested mechanism for access, rectification, erasure and export, reaching the recorded recipients (PRI-003, PRI-004)  
2. Restriction of processing (CTX-RGPD-R01) and erasure of data made public (CTX-RGPD-R02)  
3. Consent and objection, including automated signals such as GPC (PRI-006; CTX-RGPD-R04)  
4. Solely automated decisions with human intervention and the right to contest (CTX-RGPD-R05)  
5. Age verification and parental consent where applicable (CTX-RGPD-R03)  
**Out of scope:** the formal response to the data subject (deadlines, reasons), with Legal/the DPO.  
**Evidence:** tests of the mechanism; record of executions

### Phase 4 (M2–M3): Security of Processing (Art. 32) {#fase-4-m2m3-segurança-do-tratamento-art-32}
1. Encryption: TLS 1.2+; at rest with key management  
2. IAM: MFA, least privilege, periodic access review  
3. Testing: SAST/DAST/fuzzing; effectiveness validation  
4. Resilience: backups, tested DR, monitoring  
**Evidence:** Key records, test reports, DR logs

### Phase 5 (M3–M4): DPIA (Art. 35) {#fase-5-m3m4-dpia-art-35}
1. DPIA trigger criteria defined  
2. Reuse Threat Modelling ([Ch. 03](/sbd-toe/sbd-manual/threat-modeling/intro)) as a technical annex  
3. Attach the LINDDUN analysis, mandatory at all levels when there is personal data (THR-003)  
4. Opinion of the DPO and decision of the controller, recorded (outside the Manual; the Manual only provides for the DPO's review of the LINDDUN analysis at L3)  
**Evidence:** DPIA #1; TM annexes; DPO approval

### Phase 6 (M3–M4): Processors (Art. 28) {#fase-6-m3m4-processors-art-28}
1. Security checklist for processors  
2. Contract under Article 28(3) with each processor that processes personal data, at any level (CTX-RGPD-P01), with technical security clauses; the legal content belongs to Legal/the DPO  
3. The same contract with the processors that receive personal data in AI prompts, at any level (Policy 18 §10.3; CTX-RGPD-P02)  
4. Monitoring and annual review  
**Evidence:** Checklist; contracts; review reports

### Phase 7 (M4–M5): Incidents and 72h Notification (Art. 33/34) {#fase-7-m4m5-incidentes-e-notificação-72h-art-3334}
1. Runbook with a 72 h clock (Article 33) and the minimum content of Policy 32 §6.1: nature of the breach, categories and approximate number of data subjects and of records, DPO contact, likely consequences and measures. All breaches are recorded, notified or not, with the reasons (CTX-RGPD-R06); decision, without undue delay, on communicating to data subjects when there is a high risk (Article 34)  
2. High-risk criterion for communicating to data subjects; the content of that communication (Article 34(2)) is a declared gap of the Manual, to be prepared with the DPO  
3. Annual simulation exercise  
**Evidence:** Runbook; exercise records; post-action report

### Phase 8 (M5–M6): Retention & Secure Erasure {#fase-8-m5m6-retenção--eliminação-segura}
1. Retention periods per personal dataset, with effective erasure that reaches replicas, caches and copies (PRI-002); the legal grounds for the periods belong to Legal  
2. Scheduled deletion or anonymisation jobs  
3. In immutable logs and copies (WORM), pseudonyms and a key per data subject, and erasure by destroying the key (Policy 29 §8.1; PRI-005; CTX-RGPD-P05)  
4. Proof of execution (logs, reports)  
**Evidence:** Retention table; erasure logs; audits

---

## Checklists {#checklists}

### PbD/PbDf {#pbdpbdf}
- [ ] Requirements PRI-001 to PRI-007 applied and verified
- [ ] Secure defaults applied (minimal collection, encryption)
- [ ] Pipeline gate for schemas/data
- [ ] Periodic review of configurations

### Art. 32 {#art-32}
- [ ] TLS 1.2+/1.3 and at rest encryption
- [ ] Key management with rotation
- [ ] MFA and privilege review
- [ ] SAST/DAST/fuzzing integrated
- [ ] Backups tested; DR exercised

### DPIA {#dpia}
- [ ] Trigger criteria defined
- [ ] Threat Modelling attached
- [ ] LINDDUN analysis attached (THR-003)
- [ ] DPO approval

### 72h Incidents {#incidentes-72h}
- [ ] Runbook with the minimum content of Policy 32 §6.1 and recording of all breaches (CTX-RGPD-R06)
- [ ] 72h timer visible (Article 33, counted from awareness)
- [ ] High-risk criterion and communication to data subjects without undue delay (Article 34)
- [ ] Annual exercise completed
- [ ] Content of the communication to data subjects prepared with the DPO (a declared gap of the Manual, Article 34(2))

### Processors {#processors}
- [ ] Security checklist applied
- [ ] Contract under Article 28(3) in force with each processor
- [ ] Annual review and records

### Retention {#retenção}
- [ ] Table approved
- [ ] Automatic jobs configured
- [ ] Evidence of execution

---

## Key Metrics {#métricas-chave}
| Metric | Definition | Target |
|---------|-----------|---------|
| % apps with Art. 32 complete | Apps with encryption+IAM+testing | ≥95% |
| Notifications within the legal time limit | Awareness → submission to the authority | 100% ≤ 72h (legal deadline, Article 33); a shorter internal target, if any, belongs to the organisation |
| % DPIA on time | DPIAs completed within the SLA | ≥90% |
| Retention compliance | Job execution vs. plan | ≥95% |

---

## Artefacts to Maintain {#artefactos-a-manter}
- Data protection policy (the organisation's; a declared gap of the Manual, Article 24(2))
- ROPA export (GRC)
- Test and gate reports
- DPIAs with technical annexes
- 72h runbook + exercise records
- Retention tables + erasure logs
- Checklists/processors and contracts

---

## Notes {#notas}
- Incidents may also trigger NIS2/DORA. A single runbook with differentiated reporting channels is recommended.
- LINDDUN is part of threat modelling at all levels when there is personal data, in a light form at L1 (THR-003, [Ch. 03](/sbd-toe/sbd-manual/threat-modeling/intro)).

---

## Practical Implementation Resources {#recursos-práticos-de-implementação}

For concrete support in implementing this playbook, see the following reusable examples:

- 🛠️ **[Toolchain Options](../exemplo-playbook/exemplo-toolchain-options)** - Encryption, anonymisation and data minimisation tools
- 📊 **[KPIs and Targets](../exemplo-playbook/exemplo-kpis-targets)** - Privacy and data retention metrics adaptable to the GDPR
- 👥 **[RACI and Governance](../exemplo-playbook/exemplo-raci-governance)** - Technical/DPO interface and Art. 32 responsibilities
- 📝 **[Incident Report](../exemplo-playbook/exemplo-relatorio-incidentes)** - Adaptable template for personal data breaches (72h) Art. 33-34

These resources demonstrate practical implementations aligned with the GDPR.

---

## References {#referências}
- [GDPR normative analysis](intro)
- EDPB - Guidelines DPIA, Breach Notification
- ENISA - Security of Personal Data Processing
- SbD-ToE [Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)–[Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)

**Version:** 1.1  
**Date:** September 2026  
**Note:** This playbook complements the GDPR normative analysis with practical actions
