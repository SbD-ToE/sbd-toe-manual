---
id: catalogo-requisitos-governanca
title: Governance and Contracting Requirements Catalogue
description: Canonical catalogue of organisational security governance requirements (GOV-001 to GOV-015), with applicability by risk level and acceptance criteria for ownership, exceptions, contracting, traceability, continuous validation, maturity, technical onboarding of third parties, access review and coordinated vulnerability disclosure.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:governanca, GOV, ownership, excecoes, contratacao, rastreabilidade, maturidade, divulgacao-vulnerabilidades, L1, L2, L3, auditoria]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/addon/00-catalogo-requisitos.md
  source_sha256: 6ec00fe7332a77c4adbc832f2a872396065f9b391c8b58c8bf4064da42357bb2
  source_commit: 62e6744cbd2001d8397d05f09a404fa2c18e3d61
  target_sha256: 51f8054c4c9b379e9db2b6e40d7204a4b4991a58ee3393ad15fa4c406a14ea65
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [alcada, audit_trail, avaliacao, cycle_iteration, gap_family, layer, mapping, maturity, practitioner_manual, requirement_runtime, risk_level, role_tech_lead, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: 53d793aa57da3ad735e7c493c668c3601da8730301a650b0ebed1de33980c0f8
  translated_at: 2026-09-27T14:30:47Z
  stamped_at: 2026-09-27T14:30:47Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Governance and Contracting Requirements Catalogue

## Scope: governance as a verifiable requirement {#âmbito-governação-como-requisito-verificável}

This catalogue covers the **organisational security governance requirements** - the controls that ensure that the practices prescribed in the technical chapters of the SbD-ToE are applied, traced, audited and evolved in a sustainable way.

Governance is not an administrative layer: it is the structure that gives authority, visibility and continuity to security. Without these requirements, the technical controls of the other chapters become dependent on individuals, invisible to management and untraceable in audit.

The GOV requirements are verifiable: the existence of an approved governance model, of an active exception process, of applied contractual clauses or of reported KPIs is factual and auditable. The absence of evidence is equivalent to the absence of control.

For the complete mapping of all SbD-ToE requirements catalogues by technical domain, canonical prefix and owner, see [Ch. 02 - Catalogue Mapping](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **On curation:** Consolidated from OWASP SAMM v2.1 (Governance, Policy & Compliance), NIST SSDF (PO.1, PO.3, RV.1, RV.2), ISO/IEC 27001 (A.5, A.15, A.18), OWASP DSOMM (Governance, Third-Party, Metrics), BSIMM13 (SM, CP) and DORA (governance of ICT risk). It must be adapted to the regulatory context and reviewed with each organisational maturity cycle.

For instantiation in a project and operational naming (`SEC-Lx-GOV-CODIGO`), see [Taxonomy and Traceability](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Conventions {#convenções}

| Symbol | Meaning |
|---------|-------------|
| ✔ | Requirement mandatory at this level |
| - | Not applicable or not mandatory at this level |

Levels are cumulative: L3 includes all L1 and L2 requirements; L2 includes all L1 requirements.

---

## GOV Catalogue - Governance and Contracting {#catálogo-gov---governação-e-contratação}

Requirements ensuring that security is applied with formal authority, complete traceability and a capacity for sustained organisational evolution.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| GOV-001 | Formal security governance model approved | ✔ | ✔ | ✔ | Model documented and formally approved by senior management, with roles, responsibilities and decision cycle defined; accessible and communicated to the relevant teams; reviewed at least annually or after significant organisational change. |
| GOV-002 | Security ownership assigned per application or project | ✔ | ✔ | ✔ | Each application or project has a formally designated and registered security owner; the owner has the competence and authority to take security decisions within the scope of the project; the designation is updated on changes of team or responsibility. |
| GOV-003 | Approval authorities defined and known per risk level | - | ✔ | ✔ | Approval authorities for risk decisions, exceptions and compensations are documented per level (L1/L2/L3); the chain of authority is known to decision-makers; decisions outside the approval authority are escalated in a defined and traceable way. |
| GOV-004 | Formal exception management process active | ✔ | ✔ | ✔ | A formal exception process exists, documented and in use; every non-application of a control is recorded with justification, compensation, approver and deadline; unrecorded exceptions are treated as active non-compliance; the process covers the complete chain of authority. |
| GOV-005 | Exceptions with validity, monitoring and mandatory revalidation | - | ✔ | ✔ | All active exceptions have a defined expiry date; an alert mechanism exists before expiry; expired exceptions without renewal are treated as non-compliance; the list of active exceptions is reviewed in each audit cycle. |
| GOV-006 | Security clauses proportional to risk in contracts with third parties | ✔ | ✔ | ✔ | Contracts with suppliers, outsourcing and contractors include security clauses proportional to the risk level; clauses reviewed at renewals; evidence of the clauses applied available per active contract. |
| GOV-007 | Formal supplier validation before onboarding | ✔ | ✔ | ✔ | Suppliers with access to data, code or pipelines are validated with a questionnaire or checklist before onboarding; validation proportional to risk (L3: SBOM, incident SLA, formal right to audit); validation record retained and traceable. |
| GOV-008 | Organisational traceability of security decisions per application | - | ✔ | ✔ | A consolidated record per application exists that links: risk classification → requirements applied → approved exceptions → validated suppliers → security owner; record updated at each relevant release or change of risk; available for audit. |
| GOV-009 | Evidence of decisions traceable, referenceable and retained | ✔ | ✔ | ✔ | Every risk decision or exception has referenceable evidence artefacts (ticket, note, GRC record, ADR or equivalent); the chain of authority - who requested, who assessed, who approved - is verifiable; evidence retained for the period defined in policy. |
| GOV-010 | Continuous validation cycle and periodic compliance review | - | ✔ | ✔ | Periodic review cycle defined by asset type (L3 applications: quarterly; L2: half-yearly; suppliers: annual, half-yearly at L3 and upon a critical event); reviews produce traceable evidence; identified deviations generate corrective actions with a defined owner and deadline. |
| GOV-011 | Governance KPIs defined, collected and reported | - | ✔ | ✔ | Governance KPIs are defined, collected periodically and reported to management; deviations from defined thresholds generate corrective action; KPIs include at least: active exceptions per domain, % of applications with an assigned owner, % of contracts with security clauses. |
| GOV-012 | Active maturity model with measured and planned evolution | - | - | ✔ | Active security maturity assessment (SAMM, DSOMM or equivalent); carried out at least annually; results documented with an evolution plan and defined targets; evolution compared with the previous cycle and reported to management. |
| GOV-013 | Technical onboarding and mandatory pre-access training of third parties | rec. | ✔ | ✔ | Contractors and third parties complete structured technical preparation **before real access** to systems: security training by profile (Dev, DevOps, QA, Architecture), comprehension quiz with a minimum score (typically 80%), sandbox environment for practice and NDA/confidentiality agreement signed; access is granted only after validated completion *sign-off* (Security Champion/AppSec + Tech Lead); the record is traceable (GRC/LMS) with dates, scores and validator, and kept according to the applicable regulatory retention (DORA, NIS2). At L1 it is recommended; at L2/L3 it is mandatory, with a validated quiz at L3. |
| GOV-014 | Periodic review of third-party access (least privilege) | ✔ | ✔ | ✔ | The access of active contractors to systems (repositories, CI/CD, databases, cloud IAM, VPN) is reviewed periodically — half-yearly at L1, quarterly at L2/L3 — validating, per third party, that each access remains necessary for the project; excessive or obsolete access is removed on the same day; the review is signed (Tech Lead + Security Champion), the changes are kept in an *audit trail* and a consolidated report (% kept / % removed) is delivered. Additional triggers: change of project, incident. |
| GOV-015 | Coordinated vulnerability disclosure with a published reporting channel | ✔ | ✔ | ✔ | Coordinated vulnerability disclosure policy published, with the scope of the systems covered and a channel for receiving external reports (e.g. `security.txt` under RFC 9116, or a dedicated address); receipt acknowledged and initial assessment made within defined time limits (the Manual's choice: acknowledgement within 5 working days, initial assessment within 15 days); confirmed reports handled as findings, with the SLAs of Policy 19 §4.3 (TST-003); affected users informed of the fix or mitigation; disclosure coordinated with the reporter. |

---

## Explanatory notes {#notas-explicativas}

- **GOV-001**: Formal approval by senior management is not formalism - it is the mechanism that gives the model its authority. A governance model not approved by senior management has no force to demand compliance or to sustain external audits.
- **GOV-002**: The security owner is the point of accountability for each application. Without a defined owner, exceptions have no approver, deviations have no recipient, and audits have no counterpart. Team turnover is the main trigger of outdated ownership.
- **GOV-003**: Approval authorities do not define who decides everything - they define who decides *what*, with what authority, and when to escalate. For L1 a technical owner is sufficient; for L3, the CISO or equivalent must be in the chain. The absence of formal approval authorities generates inconsistency and informal concentration of power.
- **GOV-004 and GOV-005**: The distinction is intentional. GOV-004 verifies whether the process exists and is used; GOV-005 verifies whether active exceptions are controlled over time. It is possible to have a formal process (GOV-004 met) with chronically expired exceptions (GOV-005 not met).
- **GOV-006**: Proportionality to risk is decisive: demanding the same level of clauses from an L1 supplier and from an L3 one is inefficient; not demanding adequate clauses from an L3 supplier is a control gap. The reference is the risk classification of the integrated application or service.
- **GOV-008**: Organisational traceability is not a static spreadsheet - it is a living record that reflects the security state of each application at a given moment. Its value for audit depends directly on how up to date it is.
- **GOV-011**: KPIs without thresholds and without corrective action are merely decorative metrics. The criterion does not demand a sophisticated dashboard - it demands that the numbers produce decisions.
- **GOV-012**: The maturity assessment only has value if compared with previous cycles and if it generates a plan with concrete targets. An assessment that changes nothing is not a control - it is an exercise.
- **GOV-013**: The risk of an unprepared third party is not bad faith - it is involuntary error: exposed credentials, unauthorised access to data, insecure practices through lack of knowledge. The *sign-off* before access is the point where preparation becomes a precondition and not a subsequent formality. It links Ch. 13 (Training) to Ch. 14 (Governance): training provides the content, governance provides the access *gate* and the traceability.
- **GOV-014**: *Access creep* is silent - permissions accumulate over time and nobody removes them without a cycle that forces it. Periodic review is the mechanism that keeps *least privilege* alive rather than declared. The difference from internal access review is the risk profile of the third party and the frequency: for an L3 contractor, the quarter is the acceptable limit between the end of a need and the removal of the corresponding access.
- **GOV-015**: Vulnerabilities that come from outside (researchers, customers, users) do not pass through the internal scanners: without a known channel and a process with time limits, they get lost, or become public before the fix. The policy does not require rewards (*bug bounty*): it requires that there is somewhere to report, someone who responds and a known next step. A confirmed report enters the same circuit as internal findings, and informing the affected users closes the cycle. The acknowledgement and initial-assessment time limits are the Manual's choice; an applicable regime may set others.

---

> For the governance model and decision cycle, see [Governance Model](./modelo-governancao).
> For the canonical exception process, see [Canonical Exception Management Process](./processo-excecoes).
> For contractual clauses, see [Security Contractual Clauses](./clausulas-contratuais).
> For supplier validation, see [Supplier Validation Model](./modelo-validacao-fornecedores).
> For organisational traceability, see [Organisational Traceability](./rastreabilidade-organizacional).
> For continuous validation, see [Continuous Validation](./validacao-continuada).
