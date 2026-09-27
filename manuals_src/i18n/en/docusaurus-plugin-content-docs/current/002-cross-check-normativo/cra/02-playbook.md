---
id: playbook
title: "SbD-ToE 4 CRA: Implementation Playbook"
description: Practical roadmap for using SbD-ToE as the technical basis for the CRA in a product context, with complementary regulatory formalisation
tags: [playbook, cra, implementacao, roadmap, produtos-digitais]
sidebar_position: 6
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/cra/02-playbook.md
  source_sha256: e3647a8e7582e415ebec5d4502785e28dffcc0799786173d261291632161c18c
  source_commit: 50f5914ebc90e4135e6678b2278709d5082dd237
  target_sha256: ee332f74ba5496cff1d560e92c9d063b5e26c821a260f0a6e4462a60b0650704
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [avaliacao, chapter_role, cra_economic_operator, cra_pde, cra_support_period, cycle_iteration, eu_placing_on_market, lifecycle_phase, papel_suporte, practitioner_manual, requirement_runtime, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: add33d9a5f390ac71a175848cc9b05861423da22abdbf4138f3f3c577e2d1732
  translated_at: 2026-09-27T07:05:55Z
  stamped_at: 2026-09-27T07:14:34Z
  reviewed_by: null
---

# SbD-ToE 4 CRA: Implementation Playbook

## Overview {#visão-geral}

Objective: Turn CRA requirements into concrete actions using existing SbD-ToE controls.

Principle: Reuse > Invent. Many capabilities (SBOM, patching, testing) already exist, but `CRA` conformity also requires product context, an economic operator role, a support period, formal reporting and its own documentary route.

This playbook is most defensible when applied to:

- a manufacturer of a product with digital elements
- a supplier that needs to organise technical evidence for a `CRA` reading
- contexts with a versioned product, a security contact, a support period and economic operator responsibilities

Outside that context, SbD-ToE remains useful as a technical basis, but the reading is no longer a complete `CRA` reading.

> 📚 **Supporting Resources:** For practical templates and implementation examples, see the [Example Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-toolchain-options) with reusable toolchains, KPIs, RACI and vulnerability handling processes.

## Quick Map CRA → SbD-ToE {#mapa-rápido-cra--sbd-toe}

| CRA Area | SbD-ToE | Action | Evidence |
|----------|---------|------|----------|
| Secure Lifecycle | [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Ch. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro), [Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro), [Ch. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Lifecycle policy, support period and gates | Approved policy; pipeline YAML; support period record |
| Vulnerability Handling | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | Triage process + SLA | Triage records; SLA metrics |
| SBOM | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | Continuous generation + export | CycloneDX files per release |
| Rapid Patching | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | Automatic patch workflow | Patch pull requests + times |
| Exploitation Reporting | [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Technical runbook + regulatory notification interface | Runbook; communication matrix; example JSON |
| Security Documentation | [Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Ch. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Product security guide + contact point + end of support | Published PDF/Markdown guide; support table |
| Exceptions | [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro) addon 08, [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | CRA exception policy | Exception records + approvers |
| Supply Chain | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Ch. 09](/sbd-toe/sbd-manual/containers-imagens/intro), [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Physical supply chain checklist | Completed checklist |

---

## Implementation Phases (≈ 6–9 months) {#fases-de-implementação--69-meses}

### Phase 1 (M0–M1): Foundations, Scope Gate & Governance {#fase-1-m0m1-fundamentos-scope-gate--governance}
1. Designate a CRA Owner (GRC + AppSec)  
2. Create a "Product Security & CRA" Policy (approved by management)  
3. Map SbD-ToE roles → CRA roles (manufacturer, importer, distributor, substantial modification where applicable)  
4. Define a product criticality matrix (adapted L1–L3 basis)  
5. Record the support period and the end-of-support communication rule per product line  
**Evidence:** Approval minutes; criticality matrix; policy version 1.0; record of roles and support

### Phase 2 (M1–M2): SBOM & Inventory {#fase-2-m1m2-sbom--inventário}
1. Enable automatic SBOM generation (build pipeline)  
2. Validate coverage (≥95% of components listed)  
3. Create a sanitised CycloneDX export  
4. "SBOM Releases" repository (controlled, versioned)  
**Evidence:** SBOM v1; coverage report; export script

### Phase 3 (M2–M3): Vulnerability Handling & SLAs {#fase-3-m2m3-vulnerability-handling--slas}
1. Define severity (Critical/High/Medium/Low)  
2. Establish a patch SLA (Critical ≤15d, High ≤30d, Medium ≤90d)  
3. Automate issue creation for critical CVEs  
4. Patch compliance dashboard  
**Evidence:** SLA policy; initial dashboard; example issues

### Phase 4 (M3–M4): Testing & Release Gate {#fase-4-m3m4-testes--gate-release}
1. Integrate SAST/DAST/fuzzing into the pipeline  
2. Create a "no-critical-known" gate (release blocked)  
3. Critical exception process (board-level)  
4. Release quality report template  
**Evidence:** Pipeline logs; gate configuration; release report #1

### Phase 5 (M4–M5): Disclosure & External Communication {#fase-5-m4m5-disclosure--comunicação-externa}
1. Publish security.txt + PGP key  
2. "Vulnerability Disclosure Policy" page  
3. External report triage runbook  
4. Dedicated email/portal channel  
5. Identify a security point of contact for users and researchers  
**Evidence:** Public page; record of the first test report; published contact

### Phase 6 (M5–M6): Active Exploitation Reporting {#fase-6-m5m6-reporte-de-exploração-ativa}
1. Define criteria for "actively exploited" (IOC, confirmed telemetry)  
2. Create a script to export incident JSON + SBOM of the affected component  
3. Notification runbook for the CSIRT designated as coordinator and ENISA, via the single reporting platform (early warning ≤24 h, notification ≤72 h and final report (Art. 14; applicable since 11.9.2026)), and a communication matrix for users (Article 14(8))  
4. Internal exercise simulation  
**Evidence:** Script; runbook; exercise report; communication matrix

### Phase 7 (M6–M7): Product Security Documentation {#fase-7-m6m7-documentação-de-segurança-do-produto}
1. Write the Security Guide (secure installation, updating, contact, support period, end of support)  
2. Validate with AppSec + engineering  
3. Publish version 1.0 (Markdown/PDF)  
4. Per-release update process  
**Evidence:** Guide v1; diff v1→v2 (example)

### Phase 8 (M7–M8): Expanded Supply Chain {#fase-8-m7m8-cadeia-fornecimento-expandida}
1. Inventory firmware/hardware (if applicable)  
2. Integrity checklist (hash, signature, origin)  
3. Secure update process (secure channel)  
4. Supply chain coverage metric (≥90%)  
**Evidence:** Completed checklist; coverage metric

### Phase 9 (M8–M9): Metrics & Continuous Improvement {#fase-9-m8m9-métricas--melhoria-contínua}
1. Metrics: MTTP (Mean Time To Patch), % SLA met, open vulns by severity  
2. Quarterly retrospective meeting  
3. Improvement plan (top 3 blockers)  
4. Adjust policies following legal/regulatory review  
**Evidence:** Dashboard; retrospective minutes; improvement plan

---

## Checklists {#checklists}

### SBOM Checklist {#checklist-sbom}
- [ ] Pipeline generates SBOM automatically
- [ ] CycloneDX/SPDX format validated
- [ ] Sanitised export created
- [ ] SBOM version associated with the release
- [ ] Coverage ≥95% of components
- [ ] Update process documented

### Vulnerability Handling Checklist {#checklist-vulnerability-handling}
- [ ] Severity defined (Critical/High/Medium/Low)
- [ ] Patch SLA documented
- [ ] Automatic issues for critical findings
- [ ] Patch compliance dashboard active
- [ ] CRA exception policy published
- [ ] Critical exceptions approved by the board

### Release Gate Checklist {#checklist-release-gate}
- [ ] SAST integrated
- [ ] DAST integrated
- [ ] Fuzzing (if applicable)
- [ ] Gate blocks known critical CVEs
- [ ] Release quality report archived
- [ ] Formal exception override process

### Disclosure Checklist {#checklist-disclosure}
- [ ] security.txt published
- [ ] PGP key accessible
- [ ] Disclosure policy page published
- [ ] Reporting channel operational (email/portal)
- [ ] Internal triage runbook
- [ ] Security point of contact identified
- [ ] Average response time `<`5 business days for reports with no indication of exploitation; with an indication of active exploitation, triage ≤4 h and the Article 14 track (the Manual's choice)

### Exploitation Reporting Checklist {#checklist-reporte-exploração}
- [ ] "Actively exploited" criteria defined
- [ ] JSON export script ready
- [ ] Article 14 notification runbook (24 h / 72 h / final report)
- [ ] User communication matrix
- [ ] Simulation completed
- [ ] Test evidence archived

### Security Documentation Checklist {#checklist-documentação-segurança}
- [ ] Secure installation guide
- [ ] Update + rollback guide
- [ ] Security contact (security@)
- [ ] Support period documented
- [ ] End-of-support date communicable
- [ ] Hardened configuration recommendations
- [ ] Vulnerability management section
- [ ] Version and date
- [ ] Technical documentation (including the SBOM) and EU declaration of conformity kept for at least 10 years after placing on the market or for the support period, whichever is longer (Article 13(13))

### Physical Supply Chain Checklist (if applicable) {#checklist-supply-chain-física-se-aplicável}
- [ ] Firmware/hardware list
- [ ] Hashes/signatures verified
- [ ] Secure update channel
- [ ] Integrity validation process
- [ ] Auditable records

---

## Key Metrics {#métricas-chave}
| Metric | Definition | Initial Target |
|---------|-----------|------------------|
| Critical MTTP | Mean time to critical patch | ≤15 days |
| % SLA Met | (Vulns patched within SLA) / total | ≥90% |
| SBOM Coverage | % of components identified | ≥95% |
| Mean Disclosure Response Time | Receipt → first response | ≤5 business days with no indication of exploitation; triage ≤4 h with an indication of active exploitation (the Manual's choice) |
| Gate Effectiveness | Releases blocked due to critical CVE | 100% blocked |
| Active Critical Exceptions | No. of open critical exceptions | Downward trend |

---

## Artefacts to Maintain (Data Room) {#artefactos-a-manter-data-room}
| Artefact | Type | Update Frequency |
|-----------|------|------------------------|
| Product Security & CRA Policy | Document | Annual / when a requirement changes |
| CRA Roles & Support Period Record | Document | Per product line / release review |
| SBOM Releases | Files | Each major/minor release |
| Vulnerability Dashboard | Panel | Continuous (live) |
| Release Quality Reports | Document | Each release |
| Product Security Guide | Document | Each major release |
| Active Exploitation Runbook | Document | Annual / exercises |
| Disclosure Records | Tickets / Issues | Continuous |
| Supply Chain Checklist | Document | Quarterly |

---

## Exceptions (Summary Policy) {#exceções-política-resumida}
Categories:
- Unacceptable: critical RCE, authentication bypass, exposure of credentials in cleartext
- Acceptable (short TTL ≤30d): Critical with no patch available + robust compensation
- Acceptable (medium TTL ≤90d): High with partial mitigation

Records: ID | Vulnerability | Severity | Justification | Approver | TTL | Mitigation | Review Date

Escalation: Critical → Board; High → CISO/AppSec; Medium/Low → AppSec.

---

## Next Steps After Phase 9 {#próximos-passos-depois-da-fase-9}
1. Formal conformity assessment (legal + technical)  
2. Prepare documentation for a possible audit/regulator  
3. Integration with other frameworks (e.g. DORA, NIS2) - avoid duplication  
4. Refine metrics (MTTP per component, vulnerability density)  
5. Automate generation of the quarterly CRA report

---

## Practical Implementation Resources {#recursos-práticos-de-implementação}

For concrete support in implementing this playbook, see the following reusable examples:

- 🛠️ **[Toolchain Options](../exemplo-playbook/exemplo-toolchain-options)** - Comparison of SCA, SBOM and vulnerability management tools
- 📊 **[KPIs and Targets](../exemplo-playbook/exemplo-kpis-targets)** - Patching and SBOM coverage metrics adaptable to the CRA
- 👥 **[RACI and Governance](../exemplo-playbook/exemplo-raci-governance)** - Responsibility matrices for vulnerability handling
- 📝 **[Incident Report](../exemplo-playbook/exemplo-relatorio-incidentes)** - Adaptable template for active exploitation reporting (CRA)

These resources demonstrate practical implementations of the deliberate abstentions of SbD-ToE.

---

## References {#referências}
- [CRA normative analysis](intro)
- SbD-ToE Chapters 01–14
- ENISA: Vulnerability Disclosure Guidelines
- ISO/IEC 29147 & 30111
- CycloneDX, SPDX

**Version:** 1.0  
**Date:** November 2025  
**Note:** This playbook complements the CRA normative analysis with a practical sequential approach and does not replace the formal conformity route of the regulation.
