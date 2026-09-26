---
id: playbook
title: "SbD-ToE 4 GDPR: Implementation Playbook"
description: Practical roadmap for aligning SbD-ToE with the technical requirements of the GDPR
tags: [playbook, gdpr, implementacao, privacy-by-design, art32]
sidebar_position: 8
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/gdpr/02-playbook.md
  source_sha256: d310619cd99c1979155f22c0531888feef73eee3e6bf0dd3247cb76f167bf2d6
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 2c5ecf24556fb94b679234a72ccef2c5cd847b398ebf4fc686d1debb67f0e98e
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: da8c4621ee3f200794cd49e34ddc29239ba89f55effb1e5e578d388e50580b8d
  glossary_keys: [chapter_role, gdpr_pseudonymisation, gdpr_security_of_processing, lifecycle_phase, mapping, requirement_runtime, role_juridico, sbdtoe_sbd, slug_threat_modeling, validation_evaluation]
  glossary_sha256: 276135a67b957a418116e4abf230b968903515a116df23d296c421b1d1b82515
  translated_at: 2026-09-26T17:57:37Z
  reviewed_by: null
---

# SbD-ToE 4 GDPR: Implementation Playbook

## Overview {#visão-geral}

Objective: operationalise GDPR Art. 25/30/32/33–34/35 based on the technical capabilities of SbD-ToE and integrate with Legal/DPO.

Structure: Requirements → Action → Evidence. Reuse NIS2/DORA controls wherever possible.

> 📚 **Supporting Resources:** For practical templates and implementation examples, see the [Example Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-toolchain-options) with reusable encryption toolchains, privacy KPIs and incident response processes.

---

## Quick Map: GDPR Art. → SbD-ToE {#mapa-rápido-gdpr-art--sbd-toe}

| GDPR Article | Requirement | SbD-ToE Chapter | Main Action |
|-------------|-----------|------------------|----------------|
| 5 | Principles | [Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Ch. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Minimisation, retention, security |
| 25 | Privacy by design/default | [Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Ch. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro)–[Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro), [Ch. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Secure default configurations |
| 30 | ROPA | [Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Apps/data inventory + GRC record |
| 32 | Security of processing | [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | Encryption, IAM, testing, resilience |
| 33/34 | Personal data breach | [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | 72h runbook + communication |
| 35 | DPIA | [Ch. 03](/sbd-toe/sbd-manual/threat-modeling/intro), [Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro) | TM + technical annexes in the DPIA |

---

## Implementation Phases (≈ 4–6 months) {#fases-de-implementação--46-meses}

### Phase 1 (M0–M1): Governance and Framing {#fase-1-m0m1-governação-e-enquadramento}
1. Appoint a DPO (if applicable) and align the RACI ([Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro))  
2. "Privacy by Design & by Default" policy approved  
3. Define the classification of personal data per application  
**Evidence:** Approval minutes; RACI; data/applications matrix

### Phase 2 (M1–M2): Inventory & ROPA {#fase-2-m1m2-inventário--ropa}
1. Update the SbD-ToE inventory (apps, data, high-level purposes)  
2. Record the ROPA in a GRC tool (Art. 30 fields)  
3. Link SbD-ToE app IDs to the ROPA  
**Evidence:** ROPA export; ID mapping

### Phase 3 (M2–M3): Privacy by Design/Default (Art. 25) {#fase-3-m2m3-privacy-by-designdefault-art-25}
1. Pattern catalogue: pseudonymisation, data minimisation, retention, proportionate logging  
2. Default configs: minimal collection, encryption at rest/in transit  
3. Pipeline gate: block on excessive collection (schema linting, for example)  
**Evidence:** PbD catalogue; pipelines; blocking examples

### Phase 4 (M2–M3): Security of Processing (Art. 32) {#fase-4-m2m3-segurança-do-tratamento-art-32}
1. Encryption: TLS 1.2+; at rest with key management  
2. IAM: MFA, least privilege, periodic access review  
3. Testing: SAST/DAST/fuzzing; effectiveness validation  
4. Resilience: backups, tested DR, monitoring  
**Evidence:** Key records, test reports, DR logs

### Phase 5 (M3–M4): DPIA (Art. 35) {#fase-5-m3m4-dpia-art-35}
1. DPIA trigger criteria defined  
2. Reuse Threat Modelling ([Ch. 03](/sbd-toe/sbd-manual/threat-modeling/intro)) as a technical annex  
3. Add Privacy TM (LINDDUN) when high risk  
4. DPO approval and record  
**Evidence:** DPIA #1; TM annexes; DPO approval

### Phase 6 (M3–M4): Processors (Art. 28) {#fase-6-m3m4-processors-art-28}
1. Security checklist for processors  
2. Standard technical clauses (encryption, logs, sub-processors)  
3. Monitoring and annual review  
**Evidence:** Checklist; contracts; review reports

### Phase 7 (M4–M5): Incidents and 72h Notification (Art. 33/34) {#fase-7-m4m5-incidentes-e-notificação-72h-art-3334}
1. Runbook with a 72h timer and minimum fields (what, when, data, measures)  
2. Risk criteria for communication to data subjects  
3. Annual simulation exercise  
**Evidence:** Runbook; exercise records; post-action report

### Phase 8 (M5–M6): Retention & Secure Erasure {#fase-8-m5m6-retenção--eliminação-segura}
1. Formalised retention tables (with Legal)  
2. Scheduled erasure/pseudonymisation jobs  
3. Proof of execution (logs, reports)  
**Evidence:** Retention table; erasure logs; audits

---

## Checklists {#checklists}

### PbD/PbDf {#pbdpbdf}
- [ ] Privacy pattern catalogue published
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
- [ ] Privacy TM (if high risk)
- [ ] DPO approval

### 72h Incidents {#incidentes-72h}
- [ ] Runbook with GDPR fields
- [ ] 72h timer visible
- [ ] Annual exercise completed
- [ ] Communication templates ready

### Processors {#processors}
- [ ] Security checklist applied
- [ ] Standard technical clauses
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
| Mean time to notification | Event → submission to the authority | ≤60h |
| % DPIA on time | DPIAs completed within the SLA | ≥90% |
| Retention compliance | Job execution vs. plan | ≥95% |

---

## Artefacts to Maintain {#artefactos-a-manter}
- PbD/PbDf policy
- ROPA export (GRC)
- Test and gate reports
- DPIAs with technical annexes
- 72h runbook + exercise records
- Retention tables + erasure logs
- Checklists/processors and contracts

---

## Notes {#notas}
- Incidents may also trigger NIS2/DORA. A single runbook with differentiated reporting channels is recommended.
- LINDDUN is recommended for Privacy TM; keep it as an add-on to [Ch. 03](/sbd-toe/sbd-manual/threat-modeling/intro).

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

**Version:** 1.0  
**Date:** November 2025  
**Note:** This playbook complements the GDPR normative analysis with practical actions
