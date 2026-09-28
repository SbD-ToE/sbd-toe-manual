---
id: policy-excecoes-cve
title: CVE Exceptions Policy
description: Organisational policy that defines the criteria, the formal process, the approval authorities, the compensating controls and the reassessment deadlines applicable to exceptions to known vulnerabilities (CVEs) in software dependencies, proportional to the application's criticality level (L1, L2, L3).
tags: [policy, CVE, exceções, VEX, SCA, risco residual, compensação, reavaliação, cap05, L1, L2, L3, governance, supply chain]
grupo: risco
sidebar_position: 12
translation:
  source_locale: pt
  source_path: 020-assets/policies/12_policy-excecoes-cve.md
  source_sha256: 8669de5e51248839e96c83a2139bc38d9e987fd0cde1944893c000150fa35302
  source_commit: fae8897094a36c3dd4296383ae5b0d690cc5b9c1
  target_sha256: 0e5fc1760effe0f58be684d5f50011e244b1c5d16c650e49ee965b1251d41023
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [alcada, avaliacao, cra_pde, framework_source_corpus, layer, practitioner_manual, requirement_runtime, risk_level, role_tech_lead, sbdtoe_sbd, transversal]
  glossary_sha256: d08b98b471eb30727a46f86ffaccdaa8a76183dd5cfbcd23195832b870d197fc
  translated_at: 2026-09-28T09:12:28Z
  stamped_at: 2026-09-28T09:12:28Z
  reviewed_by: null
---

# CVE Exceptions Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for the **formalisation, approval, control and reassessment of exceptions to known vulnerabilities (CVEs)** detected in software dependencies.

The presence of a CVE in a component in use does not necessarily imply immediate exploitability - it may be a vulnerability with no attack vector reachable in the context of the application, a component that is not exposed, or a situation in which the available fix introduces regressions that make an immediate update unfeasible. However, the absence of direct exploitability does not waive formalisation: unrecorded exceptions are invisible risk.

The objective of this policy is to ensure that:

- Every exception to a CVE is formalised, approved by the appropriate approval authority and traceable
- The compensating control that justifies the acceptance is verifiable and monitored
- Reassessment deadlines are defined by severity and by the application's criticality level
- Expired or invalid exceptions are detected automatically and do not persist silently

---

## 2. Scope {#2-âmbito}

This policy applies to all known vulnerabilities (CVEs, GHSA, OSV, or equivalent) identified by SCA tools in software dependencies, including:

- Direct and transitive dependencies of applications
- Components present in container images
- Modules and providers in IaC artefacts when subject to SCA

It does not apply to vulnerabilities in the organisation's own code (SAST findings) - these are covered by the Security Exception Management Policy.

---

## 3. Definition of a CVE exception {#3-definição-de-exceção-a-cve}

A **CVE exception** is the formal record that documents the decision to keep a component with a known vulnerability in production for a limited period, on the basis of:

- An impact analysis demonstrating non-exploitability in the specific context of the application, or
- The absence of an available fix (upstream has not yet corrected it), or
- An available fix that introduces unacceptable regressions, with a defined, time-bound resolution plan

:::warning
The absence of a known public exploit is not, on its own, sufficient justification for an exception. It is necessary to demonstrate that the attack vector is not reachable in the context of the application, with verifiable technical evidence.
:::

An exception is not a permanent waiver. It is a temporary acceptance of residual risk, with a deadline and a compensating control.

---

## 4. Types of exception {#4-tipos-de-exceção}

| Type | Situation | Additional requirement |
|---|---|---|
| **Not affected** | The CVE exists but the vulnerable component is not used in the reachable code path | Technical evidence from code path analysis |
| **Fix not available** | Upstream has not released a patch; no alternative version | Monitoring plan and mandatory reassessment deadline |
| **Fix deferred** | Fix available but the update requires compatibility work | Update plan with a defined date and owner |
| **Risk accepted** | Exploitable CVE but risk mitigated by a compensating control | Verifiable and documented compensating control |

Each type has distinct approval requirements and a distinct maximum period (see sections 5 and 6).

---

## 5. Formal exception process {#5-processo-formal-de-exceção}

### 5.1 Mandatory steps {#51-etapas-obrigatórias}

| Step | Responsible | Artefact |
|---|---|---|
| Identification of the finding | SCA scanner (automated) | CVE + component + severity |
| Impact and exploitability analysis | Developer + AppSec Engineer | Documented technical justification |
| Definition of a compensating control | AppSec Engineer / Architect | Evidence of the alternative control |
| Formal approval | Approval authority as per section 5.2 | Record in `excecoes.yaml` or `vex.yaml` |
| Scheduling of the reassessment | AppSec Engineer | Review calendar with alerts |

### 5.2 Approval authorities {#52-alçadas-de-aprovação}

| Application level | CVE severity | Minimum approver |
|---|---|---|
| L1 | Low / Medium | Tech Lead |
| L1 | High / Critical | Tech Lead + AppSec Engineer |
| L2 | Low / Medium | AppSec Engineer |
| L2 | High | AppSec Engineer + application manager |
| L2 | Critical | AppSec Engineer + application manager + Security Officer |
| L3 | Any | AppSec Engineer + Security Officer + CISO (or delegate) |

### 5.3 Minimum content of the exception record {#53-conteúdo-mínimo-do-registo-de-exceção}

Each exception must be recorded in `excecoes.yaml` (or equivalent, e.g. `vex.yaml` in VEX format) with the following fields:

- [ ] CVE identifier (e.g. `CVE-2024-XXXXX`) or equivalent GHSA
- [ ] Affected component, version and ecosystem
- [ ] Type of exception (as per section 4)
- [ ] Technical justification (exploitability in the context of the application)
- [ ] Compensating control applied (if type "Risk accepted")
- [ ] Approver and approval date
- [ ] Expiry date of the exception
- [ ] Reference to the SCA finding that gave rise to the exception

---

## 6. Maximum periods and reassessment {#6-prazos-máximos-e-reavaliação}

**Triage.** Every CVE affecting a deployed component is triaged (affected / not affected / decision) within ≤ 24 h if Critical and ≤ 48 h if High, at any level; with an indication of active exploitation (for example, presence in the KEV), within ≤ 4 h. If the component is part of a product with digital elements that the organisation places on the market, confirmed active exploitation triggers the CRA Article 14 track (Policy 32 §6). These time limits are the Manual's choice.

### 6.1 TTL by severity and type {#61-ttl-por-severidade-e-tipo}

| CVE severity | Type | L1 | L2 | L3 |
|---|---|---|---|---|
| Critical | Fix deferred / Risk accepted | 7 days (remediation plan mandatory) | 7 days (CISO + remediation plan) | Not acceptable |
| High | Fix deferred / Risk accepted | 90 days | 30 days | 14 days |
| Medium | Any | 90 days | 60 days | 30 days |
| Low | Any | 90 days | 60 days | 30 days |
| Fix not available | Any | Ceiling of the severity (above) | Ceiling of the severity (above) | Ceiling of the severity (above) |
| Not affected | - | No TTL* | No TTL* | No TTL* |

The ceilings follow Policy 05 §7, which is the master for exception validity periods.

*Exceptions of the "Not affected" type must be reassessed whenever the component is updated or when new information about the CVE is published that changes the exploitability context.

### 6.2 Reassessment {#62-reavaliação}

Before each exception expires, a reassessment must be carried out to determine:

- **Maintained**: the situation has not changed; the compensating control remains effective; a new expiry date is set (requires new approval from the same approval authority)
- **Resolved**: the fix has been applied; the exception is closed
- **Escalated**: the situation has worsened (e.g. a public exploit has been published); the exception is reclassified and the approval authority rises

:::warning
An expired exception without a documented reassessment is treated as non-compliance. The pipeline must detect expired exceptions in `excecoes.yaml` and block the build at L2/L3 until the reassessment is completed.
:::

---

## 7. Compensating controls {#7-controlos-compensatórios}

When the type of exception is "Risk accepted", a compensating control that reduces the likelihood or the impact of exploitation must be defined and verified. Examples of accepted compensating controls:

| Control | Description |
|---|---|
| WAF / filtering | Filtering of payloads associated with the exploitation vector at the network or application layer |
| Network isolation | Vulnerable component with no direct external access; traffic controlled by a firewall or service mesh |
| Feature deactivation | Vulnerable functionality deactivated in the application's configuration |
| Runtime protection | RASP or eBPF-based monitoring with detection of exploitation attempts |
| Restricted access | Component accessible only to authenticated and authorised users, with MFA enabled |

Compensating controls must be verifiable - their effectiveness must be demonstrable in an audit.

---

## 8. Integration into the pipeline {#8-integração-no-pipeline}

The CI/CD pipeline must check the status of active exceptions in every build:

| Gate | L1 | L2 | L3 |
|---|---|---|---|
| Block the build if there is a Critical/High CVE without an approved exception | Yes | Yes | Yes |
| Block the build if an exception has expired without reassessment | No | Yes | Yes |
| Alert 15 days before expiry (or at the midpoint of the TTL, if shorter than 30 days — Policy 05 §7) | Mandatory | Mandatory | Mandatory |
| Generate a report of active exceptions per build | Recommended | Mandatory | Mandatory |

---

## 9. Artefacts {#9-artefactos}

| Artefact | Description | Retention |
|---|---|---|
| `excecoes.yaml` / `vex.yaml` | Register of active exceptions with approvals and deadlines | While the exception is active + 1 year (L1), 2 years (L2), 3 years (L3) |
| `sca-report.*` | SCA report with findings and the status of exceptions | 90 days (L2), 1 year (L3) |
| Reassessment history | Records of previous reassessments with decisions | 2 years (L2), 3 years (L3) after the exception is closed |

---

## 10. Responsibilities {#10-responsabilidades}

| Role | Responsibility |
|---|---|
| Developer | Identify and report CVEs with no immediate fix; propose the justification and the type of exception |
| AppSec Engineer | Analyse impact and exploitability; validate compensating controls; approve/reject exceptions; manage the reassessment calendar |
| Tech Lead | Define the update plan for "Fix deferred"; ensure reassessment within the deadline |
| Security Officer / CISO | Approve Critical exceptions at L2/L3; be notified of expired exceptions without resolution |
| DevOps / SRE | Configure the exceptions gate in the pipeline; integrate expiry alerts |
| GRC / Compliance | Audit the exception register; verify compliance with deadlines; report persistent exceptions |

---

## 11. Review and audit of this policy {#11-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Incident originating in a CVE with an active exception (regardless of expiry)
- Regulatory change that imposes more restrictive deadlines
- Change to the SCA tools that affects how exceptions are managed (e.g. VEX support)

---

## 12. Normative and technical references {#12-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 05 - Dependencies, SBOM and SCA | SCA process, gates, formal exceptions |
| SbD-ToE Ch. 14 - Governance and Contracting | Exception approval authorities by risk level |
| Dependency Management Policy (`10_policy-dependencias.md`) | SCA gates and blocking by severity |
| SBOM Policy (`11_policy-sbom.md`) | Component inventory and CVE-runtime correlation |
| Security Exception Management Policy (`05_policy-gestao-excecoes.md`) | Cross-cutting framework for security exceptions |
| CycloneDX VEX | Exploitability declaration format |
| CVSS v3.1 / v4.0 | Vulnerability severity scoring system |
| EPSS (Exploit Prediction Scoring System) | Complement to CVSS for the assessment of the likelihood of exploitation |
| NIST NVD | Reference database for CVEs |
| OSV (Open Source Vulnerabilities) | Alternative database for vulnerabilities in OSS |
| SSDF PW.4.2 | Review software for vulnerabilities and remediate |
