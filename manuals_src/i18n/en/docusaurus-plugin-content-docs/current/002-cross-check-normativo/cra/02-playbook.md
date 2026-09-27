---
id: playbook
title: "SbD-ToE 4 CRA: Implementation Playbook"
description: Practical roadmap for using SbD-ToE as the technical basis for the CRA in a product context, with complementary regulatory formalisation
tags: [playbook, cra, implementacao, roadmap, produtos-digitais]
sidebar_position: 6
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/cra/02-playbook.md
  source_sha256: 90358c5934b3b5700b78766cab1e031297903e9783ebf60804c8c157306e728f
  source_commit: 5bc57a2de453d4a50f78edcfb2b9546615b20690
  target_sha256: 64e9fcff6f9f4281e0d5d84d690ef09a3ef42c3910ead4d804905c6380233c8b
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [alcada, avaliacao, chapter_role, cra_economic_operator, cra_pde, cra_support_period, cycle_iteration, eu_placing_on_market, eu_startups, gap_family, lifecycle_phase, papel_suporte, piso_limiar, piso_relacao, practitioner_manual, requirement_runtime, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: a1f9af9de4bc92e74688b1aee15ab57b1ee6df8e5b977123d0ec564f93e24fe4
  translated_at: 2026-09-27T23:03:31Z
  stamped_at: 2026-09-27T23:03:31Z
  reviewed_by: null
---

# SbD-ToE 4 CRA: Implementation Playbook

## Overview {#visão-geral}

Objective: Turn CRA requirements into concrete actions using existing SbD-ToE controls.

Principle: Reuse > Invent. Many capabilities (SBOM, patching, testing) already exist, but `CRA` compliance also requires product context (the `CTX-CRA` context, with its floor and additions), a support period (`CTX-CRA-R01`), formal reporting and a documentation route of its own. The economic operator role is a legal qualification, outside the scope of the Manual.

What the Manual covers, what is a declared gap and what is out of scope is set out in the [normative analysis](./intro#o-que-este-manual-cobre-e-o-que-fica-de-fora) and, obligation by obligation, in [Applicable requirements](./requisitos-aplicaveis#cobertura).

This playbook is most defensible when applied to:

- a manufacturer of a product with digital elements
- a supplier that needs to organise technical evidence for a `CRA` reading
- contexts with a versioned product, a security contact, a support period and economic operator responsibilities

Outside that context, SbD-ToE remains useful as a technical basis, but the reading is no longer a complete `CRA` reading.

> 📚 **Supporting Resources:** For practical templates and implementation examples, see the [Example Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-toolchain-options) with reusable toolchains, KPIs, RACI and vulnerability handling processes.

## Quick Map CRA → SbD-ToE {#mapa-rápido-cra--sbd-toe}

| CRA Area | SbD-ToE | Action | Evidence |
|----------|---------|------|----------|
| Secure Lifecycle | [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Ch. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro), [Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro), [Ch. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Lifecycle policy, support period (`CTX-CRA-R01`) and gates | Approved policy; pipeline YAML; support period record |
| Vulnerability Handling | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | Triage process + SLA | Triage records; SLA metrics |
| SBOM | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | Continuous generation + export | CycloneDX files per release |
| Rapid Patching | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Ch. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | Automatic patch workflow | Patch pull requests + times |
| Exploitation Reporting | [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro), [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória), `CTX-CRA-R05` | Technical runbook + regulatory notification interface | Runbook; communication matrix; example JSON |
| Security Documentation | [Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Ch. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Product security guide + point of contact (`GOV-015`, floor `CTX-CRA-P04`) + end of support (`CTX-CRA-R01`) | Published PDF/Markdown guide; support table |
| Exceptions | [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro) addon 08, [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | [Policy 12 §4](/sbd-toe/assets/policies/policy-excecoes-cve#4-tipos-de-exceção) with floor `CTX-CRA-P02` (no exception for a known exploitable vulnerability at placing on the market) | Exception records + approvers |
| Supply Chain | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Ch. 09](/sbd-toe/sbd-manual/containers-imagens/intro), [Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | `DEP-006` with floor `CTX-CRA-P03`; reporting to the maintainer (`CTX-CRA-R04`) | Dependency approval record |

---

## Implementation Phases (≈ 6–9 months) {#fases-de-implementação--69-meses}

### Phase 1 (M0–M1): Foundations, Scope Gate & Governance {#fase-1-m0m1-fundamentos-scope-gate--governance}
1. Designate a CRA Owner (GRC + AppSec)  
2. Create a "Product Security & CRA" Policy (approved by management)  
3. Map SbD-ToE roles → CRA roles (manufacturer, importer, distributor, substantial modification where applicable); the qualification is legal and is outside the scope of the Manual  
4. Declare the `CTX-CRA` context per application or product and classify the risk as L1–L3 (Ch. 01). The product category under Annexes III and IV is a different classification, which L1–L3 does not replace (declared gap: the Manual does not identify it)  
5. Determine the support period in line with `CTX-CRA-R01` (criteria of Article 13(8), at least five years unless the expected use is shorter, recorded justification, notification of the end of support)  
**Evidence:** Approval minutes; L1–L3 classification and context declaration; policy version 1.0; record of roles and of the support period

### Phase 2 (M1–M2): SBOM & Inventory {#fase-2-m1m2-sbom--inventário}
1. Enable automatic SBOM generation (build pipeline)  
2. Validate coverage (≥95% of components listed; indicative target, the Manual's choice)  
3. Create a sanitised CycloneDX export  
4. "SBOM Releases" repository (controlled, versioned)  
**Evidence:** SBOM v1; coverage report; export script

### Phase 3 (M2–M3): Vulnerability Handling & SLAs {#fase-3-m2m3-vulnerability-handling--slas}
1. Define severity (Critical/High/Medium/Low)  
2. Adopt the internal remediation ladder of Policy 19 §4.3 (the Manual's choice, not a CRA time limit)  
3. Automate issue creation for critical CVEs  
4. Patch compliance dashboard  
**Evidence:** SLA policy; initial dashboard; example issues

### Phase 4 (M3–M4): Testing & Release Gate {#fase-4-m3m4-testes--gate-release}
1. Integrate SAST/DAST/fuzzing into the pipeline  
2. A gate that blocks any known exploitable vulnerability, at any level (`DEP-002`, floor `CTX-CRA-P01`)  
3. Exceptions for known exploitable vulnerabilities: not admitted at placing on the market (floor `CTX-CRA-P02`)  
4. Release quality report template  
**Evidence:** Pipeline logs; gate configuration; release report #1

### Phase 5 (M4–M5): Disclosure & External Communication {#fase-5-m4m5-disclosure--comunicação-externa}
The Manual prescribes the coordinated disclosure policy and the receiving channel (`GOV-015`); in the CRA context they are mandatory at any level, with a single point of contact (floor `CTX-CRA-P04`). The steps below implement that requirement.

1. Publish security.txt + PGP key  
2. "Vulnerability Disclosure Policy" page  
3. External report triage runbook  
4. Dedicated email/portal channel  
5. Identify a security point of contact for users and researchers  
**Evidence:** Public page; record of the first test report; published contact

### Phase 6 (M5–M6): Active Exploitation Reporting {#fase-6-m5m6-reporte-de-exploração-ativa}
1. Define criteria for "actively exploited" (IOC, confirmed telemetry)  
2. Create a script to export incident JSON + SBOM of the affected component  
3. Runbook for notification to the CSIRT designated as coordinator and to ENISA, through the single reporting platform (early warning ≤24 h, notification ≤72 h and final report (Article 14; applicable from 11.9.2026)), and a communication matrix for users (Article 14(8)). Basis in the Manual: [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) and the severe incident criterion `CTX-CRA-R05`; the minimum content of each notification and the intermediate report are a declared gap  
4. Internal exercise simulation  
**Evidence:** Script; runbook; exercise report; communication matrix

### Phase 7 (M6–M7): Product Security Documentation {#fase-7-m6m7-documentação-de-segurança-do-produto}
1. Write the Security Guide (secure installation, updating, contact, support period and its end date in line with `CTX-CRA-R01`). Secure installation and use, the effect of changes on the security of data, and decommissioning and data removal are a declared gap of the Manual (Annex II, point 8)  
2. Validate with AppSec + engineering  
3. Publish version 1.0 (Markdown/PDF)  
4. Per-release update process  
**Evidence:** Guide v1; diff v1→v2 (example)

### Phase 8 (M7–M8): Expanded Supply Chain {#fase-8-m7m8-cadeia-fornecimento-expandida}
Firmware and hardware are outside the scope of the Manual, which is centred on the application; this phase only applies if the organisation has a process of its own. The integrity of third-party software components is `DEP-006` (floor `CTX-CRA-P03`).

1. Inventory firmware/hardware (if applicable)  
2. Integrity checklist (hash, signature, origin)  
3. Secure update process (secure channel)  
4. Supply chain coverage metric (≥90%; indicative target, the Manual's choice)  
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
- [ ] CRA exceptions policy published, with floor `CTX-CRA-P02`
- [ ] No exception for a known exploitable vulnerability in a release to the market (floor `CTX-CRA-P02`)

### Release Gate Checklist {#checklist-release-gate}
- [ ] SAST integrated
- [ ] DAST integrated
- [ ] Fuzzing (if applicable)
- [ ] Gate blocks known exploitable vulnerabilities (Annex I, Part I, point (2)(a)), not only critical CVEs
- [ ] Release quality report archived
- [ ] Formal exception process restricted to vulnerabilities with a documented analysis of non-exploitability in the product (floor `CTX-CRA-P02`)

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
- [ ] Minimum content of each notification (Member States, nature, measures, sensitivity of the information) — declared gap in the Manual
- [ ] Intermediate report at the CSIRT's request — declared gap in the Manual
- [ ] Fast track: triage ≤ 4 h where there is an indication of active exploitation (the Manual's choice); early warning notification ≤ 24 h after becoming aware
- [ ] User communication matrix
- [ ] Simulation completed
- [ ] Test evidence archived

### Security Documentation Checklist {#checklist-documentação-segurança}
- [ ] Secure installation guide
- [ ] Update + rollback guide
- [ ] Security contact (security@)
- [ ] Support period determined and justified (`CTX-CRA-R01`)
- [ ] End-of-support date communicable
- [ ] Hardened configuration recommendations
- [ ] Vulnerability management section
- [ ] Version and date
- [ ] Technical documentation (including the SBOM) and EU declaration of conformity retained for at least 10 years after placing on the market or for the support period, whichever is longer (Article 13(13)). Declared gap: the Manual applies the 10 years to the SBOM and the evidence pack, but not yet to threat model versions or approval records; the EU declaration is the manufacturer's and is outside the scope of the Manual

### Physical Supply Chain Checklist (if applicable) {#checklist-supply-chain-física-se-aplicável}
Outside the scope of the Manual; include only if the organisation has a process of its own.

- [ ] Firmware/hardware list
- [ ] Hashes/signatures verified
- [ ] Secure update channel
- [ ] Integrity validation process
- [ ] Auditable records

---

## Key Metrics {#métricas-chave}
| Metric | Definition | Initial Target |
|---------|-----------|------------------|
| Critical MTTP | Mean time to critical patch | ≤ the level SLA (Policy 19 §4.3; 3 days at L3) |
| % SLA Met | (Vulns patched within SLA) / total | ≥90% (the Manual's choice) |
| SBOM Coverage | % of components identified | ≥95% |
| Mean Disclosure Response Time | Receipt → first response | ≤5 business days with no indication of exploitation; triage ≤4 h with an indication of active exploitation (the Manual's choice) |
| Gate Effectiveness | Releases with a known exploitable vulnerability blocked | 100% (floor `CTX-CRA-P01`) |
| Exceptions on Known Exploitables | No. of active exceptions on known exploitable vulnerabilities in a release to the market | 0 (floor `CTX-CRA-P02`) |

---

## Artefacts to Maintain (Data Room) {#artefactos-a-manter-data-room}
| Artefact | Type | Update Frequency |
|-----------|------|------------------------|
| Product Security & CRA Policy | Document | Annual / when a requirement changes |
| CRA Roles & Support Period Record (`CTX-CRA-R01`) | Document | Per product line / release review |
| SBOM Releases | Files | Each major/minor release |
| Vulnerability Dashboard | Panel | Continuous (live) |
| Release Quality Reports | Document | Each release |
| Product Security Guide | Document | Each major release |
| Active Exploitation Runbook | Document | Annual / exercises |
| Disclosure Records | Tickets / Issues | Continuous |
| Supply Chain Checklist | Document | Quarterly |

---

## Exceptions (Summary Policy) {#exceções-política-resumida}
**CRA rule:** a known exploitable vulnerability cannot be made an exception at placing on the market, whatever its severity (floor `CTX-CRA-P02`). The floor admits no justification and no approval at any level. The categories below apply only to vulnerabilities with no known exploitation and to products already on the market, within handling without delay.

Categories:
- Unacceptable: critical RCE, authentication bypass, exposure of credentials in cleartext
- Acceptable (TTL from Policy 05 §7: Critical 7 days with a remediation plan; not acceptable at L3): Critical with no patch available, with robust compensation and a documented analysis that the vulnerability is not exploitable in the product (e.g. component not used or not reachable). A known exploitable vulnerability is never acceptable at placing on the market (floor CTX-CRA-P01/P02; the legal criterion is exploitability, not active exploitation)
- Acceptable (TTL from Policy 05 §7: High 90 / 30 / 14 days at L1 / L2 / L3): High with partial mitigation and a documented analysis that it is not exploitable in the product

Records: ID | Vulnerability | Severity | Justification | Approver | TTL | Mitigation | Review Date

Escalation (only for vulnerabilities not exploitable in the product; approval authorities from Policy 05 §6): Critical → CISO (L2; not acceptable at L3); High → AppSec or CISO, depending on the level; Medium/Low → AppSec.

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

**Version:** 1.1  
**Date:** September 2026 (aligned with the coverage matrix and the `CTX-CRA` context)  
**Note:** This playbook complements the CRA normative analysis with a practical sequential approach and does not replace the regulation's formal conformity route.
