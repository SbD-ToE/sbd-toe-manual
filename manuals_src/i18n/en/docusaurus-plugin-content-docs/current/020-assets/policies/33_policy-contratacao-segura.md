---
id: policy-contratacao-segura
title: Secure Contracting Policy
description: Organisational policy that defines the security requirements applicable to the contractual lifecycle with suppliers and contractors, including pre-contractual due diligence, minimum contractual clauses by risk level, technical onboarding, compliance monitoring, periodic reassessment and secure offboarding, proportional to the criticality level (L1, L2, L3).
tags: [policy, contratação, fornecedores, contractors, due diligence, cláusulas contratuais, onboarding, offboarding, conformidade, cap14, L1, L2, L3, governance, DORA, NIS2]
grupo: governacao
sidebar_position: 33
translation:
  source_locale: pt
  source_path: 020-assets/policies/33_policy-contratacao-segura.md
  source_sha256: 65a993cc1724436663e9bdb3124a5ef3122f90cecfdbe9fdc487804e96c59153
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 978834965c762c38c0183674157ca16a6bf44a71673c92d608a44c8270b775a0
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bc04ded428e40ee1c214f8535dfb1904655b64166d0aa82b5df521e4230b8cb0
  glossary_keys: [audit_trail, avaliacao, cycle_iteration, discipline, lifecycle_phase, practitioner_manual, risk_level, sbdtoe_sbd, traceability, trilho_formativo, validation_evaluation, verification_taxonomy]
  glossary_sha256: 6370929de8f5e7c319726dda381ef14d622808891aab3abbc1a383da6ef797e4
  translated_at: 2026-09-26T14:11:03Z
  reviewed_by: null
---

# Secure Contracting Policy

## 1. Objective {#1-objetivo}

This policy defines the **security requirements applicable to the contractual lifecycle with suppliers, partners and contractors** that access the organisation's systems, data or infrastructure.

Outsourcing technical competences and using third-party services are common operational practices. However, each supplier or contractor with technical access represents an additional risk vector: they may introduce vulnerabilities, have access to sensitive data without an adequate framework, or retain residual access after the end of the contract. Managing this risk cannot be relegated to a generic confidentiality clause - it requires a structured process that begins before the contract is signed and ends only with verified offboarding.

The objective of this policy is to ensure that:

- The security assessment of suppliers is carried out before any contract that involves access to systems or data
- Contracts include security clauses proportional to the risk level of the relationship
- The technical onboarding of contractors is conditional on completion of minimum mandatory training
- The compliance of active suppliers is monitored and reassessed periodically
- Offboarding is executed immediately, completely and in an auditable manner

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

This policy applies to all suppliers, partners and contractors that:

- Access the organisation's systems, platforms or infrastructure
- Develop, maintain or operate software components on behalf of the organisation
- Process, store or transmit data of the organisation or of its users
- Have access to regulated environments (production, health data, financial data, PII)

| Level | Applicability |
|---|---|
| L1 | Recommended; basic confidentiality and good-practice clauses; security contact defined |
| L2 | Mandatory; pre-contractual due diligence; SbD-ToE clauses; documented onboarding; annual reassessment |
| L3 | Mandatory; formal due diligence; technical audit; complete clauses; SBOM and test reports mandatory; half-yearly reassessment; formal right to audit |

---

## 3. Pre-contractual due diligence {#3-due-diligence-pré-contratual}

Before establishing any contractual relationship with technical access, a security assessment proportional to the risk level must be carried out:

### 3.1 Assessment criteria {#31-critérios-de-avaliação}

| Criterion | L2 | L3 |
|---|---|---|
| Documented information security policy | Verification | Mandatory + evidence |
| Vulnerability management process | Verification | Mandatory + defined SLA |
| Security incidents in the last 12 months | Declaration | Declaration + analysis |
| Certifications or compliance with standards (ISO 27001, SOC 2, etc.) | Recommended | Mandatory for access to regulated data |
| Capability to deliver SBOM | Not applicable | Mandatory for developed software |
| Recent security test reports | Recommended | Mandatory |
| Documented offboarding process | Recommended | Mandatory |

### 3.2 Due diligence outcome {#32-resultado-da-due-diligence}

The outcome of the due diligence must be documented and approved before the contract is signed:

- **Approved without conditions**: contractual relationship established
- **Approved with conditions**: contract established with a remediation plan for the gaps identified and a defined deadline
- **Rejected**: supplier not eligible for a relationship with technical access until the non-conformities are resolved

---

## 4. Minimum contractual security clauses {#4-cláusulas-contratuais-mínimas-de-segurança}

All contracts that involve technical access must include security clauses proportional to the risk level:

### 4.1 Universal clauses (all levels) {#41-cláusulas-universais-todos-os-níveis}

| Clause | Description |
|---|---|
| Confidentiality | Obligation of confidentiality regarding data, credentials and architecture |
| Incident notification | Deadline for notifying security incidents to the organisation (recommended: ≤ 24 hours from awareness) |
| Acceptable use | Prohibition of access beyond what is strictly necessary for the contractual scope |
| Subcontracting | Prohibition or conditioning of subcontracting with access to data or systems |
| Termination for breach | Clause for immediate termination in the event of a serious security breach |

### 4.2 Additional clauses by risk level {#42-cláusulas-adicionais-por-nível-de-risco}

| Level | Additional clauses |
|---|---|
| **L1** | Generic commitment to good practices; incident notification policy |
| **L2** | Application of the SbD-ToE Catalogue; provision of technical evidence on request; SLA for resolution of critical vulnerabilities |
| **L3** | Mandatory periodic security testing (with report delivered); SBOM delivered per release; SLA for critical fixes (≤ 72 hours); formal right of technical audit by the organisation; security training requirements for personnel with access |

### 4.3 Reference contract template {#43-modelo-contratual-de-referência}

The organisation must maintain a standard contract template with legally validated security clauses, updated annually or after relevant regulatory changes. The template must be made available to Procurement and Legal as a negotiation reference - security clauses are minimum requirements, not negotiation points in L2/L3 contracts.

---

## 5. Technical onboarding of contractors {#5-onboarding-técnico-de-contractors}

Contractors who access the organisation's systems or repositories must complete a technical onboarding process before receiving permissions:

### 5.1 Onboarding process {#51-processo-de-onboarding}

| Step | Description | Applicability |
|---|---|---|
| Minimum training track | Training on security policies, credential management, data access, incident reporting | L2/L3 mandatory; L1 recommended |
| Validation of understanding | Quiz or test with a minimum pass mark of 80% | L2/L3 mandatory |
| Signing of specific terms | Individual statement of responsibility and confidentiality | All levels |
| Sandbox environment | Initial access to an isolated development environment before production | L3 mandatory |
| Assignment of minimum permissions | Access under the principle of least privilege; no production access without explicit approval | L2/L3 mandatory |

### 5.2 Access blocking {#52-bloqueio-de-acesso}

Access to the organisation's systems is **blocked until all mandatory onboarding steps have been completed**. Completion must be recorded (LMS, HR system or equivalent tool) and associated with the contractor's identity.

---

## 6. Compliance monitoring of active suppliers {#6-monitorização-de-conformidade-de-fornecedores-activos}

The contractual relationship does not end with the signature - active suppliers with technical access must be monitored continuously:

### 6.1 Compliance indicators to monitor {#61-indicadores-de-conformidade-a-monitorizar}

| Indicator | Description |
|---|---|
| Compliance with the vulnerability remediation SLA | Time between notification and confirmed remediation |
| Delivery of contractual artefacts | SBOM, test reports, audit reports (where applicable) |
| Incident notification within the deadline | Compliance with the contractual notification deadline |
| Absence of security incidents attributed to the supplier | Record of occurrences |

### 6.2 Periodic reassessment {#62-reavaliação-periódica}

| Level | Cadence | Scope |
|---|---|---|
| L1 | Annual | Review of clauses and basic compliance |
| L2 | Annual | Updated due diligence; verification of SLAs; analysis of incidents |
| L3 | Half-yearly | Complete technical due diligence; review of artefacts; verification of certifications; residual risk analysis |

The outcome of the reassessment must give rise to a documented decision:
- **Continuation without changes**: compliance maintained
- **Continuation with an improvement plan**: gaps identified with a resolution deadline
- **Contractual penalty**: SLA breach with financial impact (if provided for)
- **Replacement**: serious non-conformity or unacceptable risk

---

## 7. Secure offboarding {#7-offboarding-seguro}

The offboarding of a contractor or the termination of a contract with a supplier must be executed immediately and verifiably:

### 7.1 Offboarding checklist {#71-checklist-de-offboarding}

- [ ] Revocation of all access (systems, repositories, tools, VPN, service credentials)
- [ ] Removal of SSH keys, tokens, API keys and certificates issued in the name of the contractor/supplier
- [ ] Recovery of equipment or organisational assets provided to the contractor
- [ ] Confirmation of deletion or return of the organisation's data held by the supplier (where applicable)
- [ ] Deactivation of accounts in identity systems (IdP, Active Directory, etc.)
- [ ] Documented record of offboarding completion (timestamp, person responsible, status of each item)

### 7.2 Offboarding deadlines {#72-prazos-de-offboarding}

| Type of exit | Maximum deadline for access revocation |
|---|---|
| Planned exit (end of contract) | On the day of termination itself |
| Unplanned exit (immediate termination) | ≤ 2 hours after the decision |
| Termination for security reasons | Immediate - priority revocation before any other procedure |

:::warning
Keeping access active after the end of the contract is one of the most common causes of unauthorised residual access. The offboarding process must be automated as far as possible to avoid dependence on manual action under pressure or with information gaps.
:::

---

## 8. Record and traceability {#8-registo-e-rastreabilidade}

For each supplier and contractor, the organisation must maintain an up-to-date record that includes:

| Artefact | Content | Retention |
|---|---|---|
| Due diligence outcome | Pre-contractual assessment, decision, conditions | Contract duration + 3 years |
| Contract with security clauses | Signed version with applicable clauses | Contract duration + 5 years |
| Onboarding record | Training track, quiz, initial permissions | Contract duration + 1 year |
| Reassessment records | Results of each periodic assessment cycle | Contract duration + 3 years |
| Offboarding record | Completed checklist, timestamp, person responsible | 5 years |

---

## 9. Responsibilities {#9-responsabilidades}

| Role | Responsibility |
|---|---|
| Procurement / Legal | Ensure that contracts include minimum security clauses; conduct negotiation with the reference template |
| GRC / Compliance | Keep the contract template up to date; conduct due diligence; audit compliance; periodic reassessments |
| AppSec Engineer | Define the technical security requirements to be included in contracts; assess technical artefacts (SBOM, reports); support technical due diligence |
| Security Champion | Carry out the technical onboarding of contractors; verify completion of training before access is assigned |
| DevOps / SRE | Carry out the technical revocation of access at offboarding; manage identities and permissions |
| HR | Coordinate the onboarding/offboarding process with the Security Champion; record completion in HR systems |

---

## 10. Annex — Specific clauses for AI model providers {#anexo-ai-providers}

When the supplier is an **AI model provider** (Anthropic, OpenAI, Google, Mistral, Cohere, HuggingFace or an equivalent *self-hosted* option), the set of contractual clauses provided for in section 4 is extended with six specific clauses. They do not replace any of the preceding ones — they add discipline to the AI slice.

### 10.1 *Data retention* and *training opt-out* {#101-data-retention-e-training-opt-out}

- The *provider*'s retention policy made explicit: for how long submitted data is retained; in which systems; with what access controls.
- *Training opt-out* contractually agreed where applicable — preference for **zero retention** for sensitive data (PII, proprietary code, secrets potentially exposed in prompts).
- When the *provider* has *training* "opt-out by default", that guarantee is declared in the approval record (cross-link [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)).

### 10.2 Processing location {#102-localização-de-processamento}

- Document where data is processed (region, data centre, jurisdiction).
- Compliance with **GDPR Art. 44–49** when personal data is involved — *Standard Contractual Clauses* (SCCs), *Adequacy Decision*, or another valid mechanism.
- Specific clauses for *international transfers* when data leaves the EEA.

### 10.3 *Audit rights* {#103-audit-rights}

- Contractual right to access inference *logs* or equivalent when required (typical at L3 and in regulated systems — DORA Art. 28, AI Act Art. 26).
- Alternatively, periodic *audit reports* (SOC 2 Type II, ISO/IEC 42001 certification, AI Act Art. 47 declaration of conformity for GPAI).

### 10.4 Prior notification SLA {#104-sla-de-notificação-prévia}

- Notification **before** changes that alter behaviour: major model version, data policy, discontinuation, change of location.
- Minimum expected SLA: ≥ 30 days for non-emergency changes; whatever is technically possible for emergencies.
- No adequate notification → triggers a proactive review and potential activation of the architectural *fallback* (Ch. 04 §AI/ML).

### 10.5 Availability SLA and *fallback* {#105-sla-de-disponibilidade-e-fallback}

- Declared availability SLA; communication mechanism in the event of an *outage*.
- The system architecture provides for a *fallback* for when the *provider* is unavailable or returns degraded *outputs* (cross-link [`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)/[`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)).

### 10.6 Declared regulatory compliance {#106-conformidade-regulatória-declarada}

- **AI Act Art. 53** (obligations of GPAI *providers*): technical documentation of the model, published *summary of training data*, *copyright compliance policy*.
- **AI Act Art. 55** (cybersecurity of GPAI with systemic risk): continuous *AI red teaming*, infrastructure hardening, *post-market monitoring*.
- **GDPR Art. 28** (sub-processors): contracts with sub-processors, prior notification of changes.
- **NIS2 Art. 21** and **DORA Art. 28–30**: applicable when the *provider* is treated as a critical *ICT third-party*.

### 10.7 Operationalisation {#107-operacionalização}

- The provider enters the **approved list [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)** only after validation of clauses 10.1 to 10.6 (proportional to the risk level).
- Critical clauses recorded in the provider's record; review scheduled according to the risk level (L1 annual; L2 half-yearly; L3 quarterly).
- Complete operational detail in [Policy 39 — AI BOM and Supply Chain](./policy-ai-bom-supply-chain) and in Ch. 14 US "AI provider contracting".

| Clause | L1 | L2 | L3 |
|---|:--:|:--:|:--:|
| 10.1 Retention + opt-out | Recommended | Mandatory | Mandatory (zero retention for PII) |
| 10.2 Location | Recommended | Mandatory | Mandatory + SCCs/Adequacy |
| 10.3 Audit rights | — | Recommended | Mandatory |
| 10.4 Notification SLA | Recommended | Mandatory | Mandatory (≥30d) |
| 10.5 Availability SLA + fallback | Recommended | Mandatory | Mandatory |
| 10.6 Declared regulatory compliance | — | Applicable when relevant | Mandatory when GPAI or personal data |

---

## 11. Review and audit of this policy {#11-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- A security incident involving a supplier or contractor
- A regulatory change that modifies due diligence or notification obligations (e.g. DORA, NIS2, GDPR)
- An audit result that identifies gaps in the contracting or offboarding process

---

## 12. Normative and technical references {#12-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 14 - Governance and Contracting | US-02: clauses; US-14: reassessment; US-15: contractor onboarding; US-17: offboarding; **US-21 — AI provider contracting** |
| Organisational Traceability Policy (`34_policy-rastreabilidade-organizacional.md`) | Record and evidence of compliance |
| Secrets Management Policy (`18_policy-gestao-segredos.md`) | Contractor credentials and revocation |
| AI BOM Policy (`39_policy-ai-bom-supply-chain.md`) | Operationalisation of the AI provider lifecycle |
| AI Agent Mandates Policy (`38_policy-mandates-agentes.md`) | When the provider supplies agents / runtimes |
| ISO/IEC 27001 - A.15 | Supplier relationships |
| ISO/IEC 27036 | Information security for supplier relationships |
| ISO/IEC 42001:2023 | AI Management System — relationships with AI suppliers |
| NIST SP 800-161 | Cybersecurity Supply Chain Risk Management |
| NIST AI RMF 1.0 — MAP-4.x | Third-party AI risk |
| GDPR - Art. 28, 44–49 | Sub-processors; international transfers |
| DORA - Art. 28-30 | ICT third-party risk management |
| NIS2 - Art. 21 | Supply chain security measures |
| EU AI Act (Reg. (EU) 2024/1689) - Art. 25, 26, 47, 53, 55 | AI supply chain; obligations of GPAI providers |
