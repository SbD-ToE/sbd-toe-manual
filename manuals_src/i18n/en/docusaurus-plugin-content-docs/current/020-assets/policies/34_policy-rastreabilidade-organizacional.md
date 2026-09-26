---
id: policy-rastreabilidade-organizacional
title: Organisational Traceability Policy
description: Organisational policy that defines the requirements for the traceability of security practices throughout the application lifecycle, including a compliance repository per application, designation of security owners, periodic validations per SbD-ToE chapter, auditable evidence and an organisational dashboard, proportionate to the criticality level (L1, L2, L3).
tags: [policy, rastreabilidade, conformidade, owners, Security Champion, repositório conformidade, auditoria, dashboard, cap14, L1, L2, L3, governance, SSDF, ISO27001]
grupo: governacao
sidebar_position: 34
translation:
  source_locale: pt
  source_path: 020-assets/policies/34_policy-rastreabilidade-organizacional.md
  source_sha256: 4f57616ff35d84fe53fc8d8753d3c64d349031a7ce41fdbeae2511a39e7c03cd
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 23f07754282da347285e431c6e133538ef3fba9291f622466a3053b42cf0fc5f
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bc04ded428e40ee1c214f8535dfb1904655b64166d0aa82b5df521e4230b8cb0
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, framework_source_corpus, lifecycle_phase, maturity, requirement_runtime, risk_level, sbdtoe_sbd, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: 1c4417513720845aaf1c190a7d9645092b922fd09babf2a27e7c38664ba67294
  translated_at: 2026-09-26T14:11:04Z
  reviewed_by: null
---

# Organisational Traceability Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for the **traceability of security practices at organisational level** - the set of mechanisms that make it possible to demonstrate, at any moment, the compliance status of each application with the requirements of SbD-ToE, to identify those responsible for each security decision, and to present auditable evidence to internal auditors, external auditors or regulators.

Compliance without traceability is a statement of intent, not a verifiable security posture. Traceability turns scattered practices into structured evidence: it makes it possible to detect deviations before incidents, to support risk decisions with historical data, and to demonstrate maturity objectively. Without an organisational traceability mechanism, the real security status of applications remains invisible to management and to audit.

The objective of this policy is to ensure that:

- Each application has a compliance repository that reflects the real status of SbD-ToE practices
- Each application classified as L2/L3 has a formally designated security owner
- Periodic compliance validations are run with a cadence proportionate to the risk level
- All compliance evidence is auditable, versioned and linked to the decision that originated it
- The organisation has aggregated visibility of the security status of its portfolio

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

| Level | Applicability |
|---|---|
| L1 | Basic; classification record and technical owner; annual review |
| L2 | Mandatory; compliance repository per application; designated Security Champion; half-yearly validation; dashboard recommended |
| L3 | Mandatory; complete versioned repository; trained Security Champion; quarterly validation; dashboard mandatory; formal evidence for audit |

---

## 3. Compliance repository per application {#3-repositório-de-conformidade-por-aplicação}

Each application must have a compliance repository - a structured, versioned and auditable artefact that consolidates the compliance status with all applicable SbD-ToE chapters.

### 3.1 Format and minimum content {#31-formato-e-conteúdo-mínimo}

The repository may be implemented as a versioned YAML or Markdown file in a code repository, a GRC tool, or a compliance management system. The specific format is not prescribed - auditability and accessibility are the determining requirements.

| Field | Description | Applicability |
|---|---|---|
| `application.id` | Unique identifier of the application | Mandatory |
| `application.level` | Criticality level (L1/L2/L3) and date of last classification | Mandatory |
| `owner.security_champion` | Identity of the designated Security Champion | L2/L3 |
| `owner.tech_lead` | Identity of the responsible Tech Lead | Mandatory |
| `compliance.chapters[]` | Status per SbD-ToE chapter (Ch. 02–13): `Sim / Não / Exceção` | Mandatory |
| `compliance.evidence[]` | Links to evidence per chapter (reports, scans, reviews) | L2/L3 |
| `exceptions[]` | Active exceptions with a reference to the exception register | L2/L3 |
| `last_validated` | Date of and person responsible for the last validation | Mandatory |
| `next_validation` | Scheduled date for the next validation | Mandatory |

### 3.2 Updating {#32-atualização}

The repository must be updated:

- After each periodic compliance validation
- After each significant change of architecture, criticality level or owner
- After an exception is resolved or approved
- After a major release or a relevant security event

---

## 4. Formal designation of security owners {#4-designação-formal-de-owners-de-segurança}

For each application classified as L2 or L3, there must be a **formally designated Security Champion**, with documented and recorded security responsibilities.

### 4.1 Designation requirements {#41-requisitos-de-designação}

| Requirement | Description |
|---|---|
| Formal designation | In writing - official e-mail, HR system, or document signed by a manager |
| Documented responsibilities | Submission of exceptions, periodic validations, risk communication, maintenance of the compliance repository |
| Minimum training completed | The Security Champion must have completed the mandatory security training track for their function |
| Designated substitute | For continuity during prolonged absences (mandatory for L3) |

### 4.2 Centralised register {#42-registo-centralizado}

The organisation must maintain a centralised register of all active Security Champions, with identification of the application, identity, date of designation and training status. This register is the source of truth for escalation, risk communication and audit.

:::note
The designation of a Security Champion does not exempt the other team members from the security responsibilities that fall to them under the applicable policies. The Security Champion is the point of coordination and accountability - not the only person responsible for the security of the application.
:::

---

## 5. Periodic compliance validations {#5-validações-periódicas-de-conformidade}

Periodic compliance validations are intended to verify whether the requirements of SbD-ToE remain applied and effective, to detect deviations and to collect up-to-date evidence.

### 5.1 Validation cadence {#51-cadência-de-validação}

| Level | Cadence | Additional triggers |
|---|---|---|
| L1 | Annual | Significant architecture change |
| L2 | Half-yearly | Major release; security incident; change of level |
| L3 | Quarterly | Major release; incident; change of owner; external audit |

### 5.2 Validation process {#52-processo-de-validação}

Each validation cycle must cover:

- [ ] Verification of the status of each applicable SbD-ToE chapter (checklist per chapter)
- [ ] Collection of up-to-date evidence for chapters with status `Sim` (link to reports, scans, reviews)
- [ ] Review of active exceptions: validity, remediation progress, need for renewal
- [ ] Identification of new deviations or of chapters without up-to-date evidence
- [ ] Action plan for identified deviations (owner, deadline, priority)
- [ ] Update of the compliance repository with the validation result

### 5.3 Result and decision {#53-resultado-e-decisão}

The validation result must be documented with:

- Overall status: `Conforme / Conforme com desvios / Não conforme`
- List of identified deviations with severity
- Action plan with owners and deadlines
- Date of the next validation

---

## 6. Organisational dashboard {#6-dashboard-organizacional}

The organisation must maintain aggregated visibility of the compliance status of its application portfolio:

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Compliance status dashboard per application | Not applicable | Recommended | Mandatory |
| Adoption metrics per SbD-ToE chapter | Not applicable | Recommended | Mandatory |
| Visibility of active and expired exceptions | Not applicable | Recommended | Mandatory |
| Automatic alerts for critical deviations | Not applicable | Recommended | Mandatory |
| Periodic reports for executive management | Not applicable | Half-yearly | Quarterly |

The dashboard does not replace the compliance repository per application - it is an aggregated view for management and executive decision-making. The data must be derived from the individual compliance repositories to maintain consistency.

---

## 7. Auditable evidence {#7-evidência-auditável}

All compliance evidence must meet the following requirements to be considered auditable:

| Requirement | Description |
|---|---|
| Traceability | The evidence must be linkable to the practice, the chapter and the application it supports |
| Dating | Timestamp of production and of validation |
| Authorship | Identity of the person responsible for production or validation |
| Immutability | Evidence that cannot be altered after production (e.g. signed pipeline artefact, archived report) |
| Accessibility | Available to internal and external auditors without depending on access to production systems |

### 7.1 Accepted types of evidence {#71-tipos-de-evidência-aceite}

| Type | Examples |
|---|---|
| Tool reports | SAST, SCA, DAST, PenTest report - with tool version, date and scope |
| Pipeline logs | Evidence of execution of a security gate with result and timestamp |
| Review records | Pull request with documented approval and a reference to a security checklist |
| Exception decisions | Exception record with approval, justification and expiry date |
| Results of periodic tests | Reports of tabletop, war room or playbook simulation |

---

## 8. Retention of compliance artefacts {#8-retenção-de-artefactos-de-conformidade}

| Artefact | Minimum retention |
|---|---|
| Compliance repository (current status and history) | Lifetime of the application + 3 years |
| Validation evidence | 3 years |
| Security Champion designation records | Duration of the designation + 2 years |
| Periodic validation reports | 3 years |
| Exception records (including expired ones) | 5 years |

:::note
In regulated environments (DORA, NIS2, GDPR), regulatory time limits prevail over the minimums of this policy. The longer period is always the one that applies.
:::

---

## 9. Responsibilities {#9-responsabilidades}

| Role | Responsibility |
|---|---|
| Security Champion | Keep the application's compliance repository up to date; run or coordinate periodic validations; submit exceptions; communicate risk to GRC |
| AppSec Engineer | Define the structure and requirements of the compliance repository; support validations at L3; audit the quality of evidence; feed the organisational dashboard |
| Tech Lead | Ensure that the team maintains compliance practices; approve action plans for identified deviations |
| GRC / Compliance | Manage the centralised register of owners; run or audit periodic validations; produce reports for executive management; verify regulatory compliance |
| Management / CISO | Analyse portfolio status reports; take strategic risk decisions; ensure resources for the resolution of critical deviations |

---

## 10. Review and audit of this policy {#10-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- An audit that identifies gaps in the traceability status of one or more applications
- A change to the chapter structure of SbD-ToE that requires the compliance repositories to be updated
- A regulatory change that modifies the evidence or retention requirements

---

## 11. Normative and technical references {#11-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 14 - Governance and Contracting | US-04: organisational traceability; US-08: compliance repository; US-09: designation of owners; US-10: periodic validation; US-13: systematic control per chapter |
| Security Governance KPIs Policy (`35_policy-kpis-governacao.md`) | Metrics derived from the traceability data |
| Secure Contracting Policy (`33_policy-contratacao-segura.md`) | Traceability of suppliers and contractors |
| NIST SSDF - PO.3, PO.7 | Implementation of security practices and traceability |
| OWASP SAMM - PO2, PO3 | Organisational security maturity |
| ISO/IEC 27001 - A.18 | Compliance and information security reviews |
| DORA - Art. 17 | ICT risk management documentation and evidence |
| NIS2 - Art. 21 | Cybersecurity measures and accountability |
