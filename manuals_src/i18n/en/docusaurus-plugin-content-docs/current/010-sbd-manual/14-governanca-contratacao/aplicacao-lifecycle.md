---
id: aplicacao-lifecycle
title: How to Do It
description: Practical integration of governance, exception and contracting practices into the SbD-ToE lifecycle
tags: [tipo:aplicacao, ciclo-vida, governanca, contratacao, excecoes, rastreabilidade]
genia: us-format-normalization
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/aplicacao-lifecycle.md
  source_sha256: bf8690e7dd796d27b3927c614d16413f014f32ab8137faf3c3c24a359a8b6ff4
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: a2d05f0ce22e062155b7de2f9a3c23d895985c62ee27438f19e068cd5f3ad2aa
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [alcada, audit_trail, avaliacao, chapter_role, como_fazer, cycle_iteration, lifecycle_phase, maturity, papel_suporte, programme_line, provenance, risk_level, sbdtoe_sbd, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: 360b3fa67cb2f7995801f408ffc6f670cbe002abb8e2ea13970bac89b89bf8ac
  translated_at: 2026-09-26T12:00:21Z
  reviewed_by: null
---

# Applying Governance and Contracting Throughout the Lifecycle

## 🧭 When to apply {#-quando-aplicar}

| Phase / Event | Expected action | Evidence |
|---------------|--------------|-----------|
| Planning | Define contractual clauses and metrics | Approved documents |
| Execution | Record exceptions, apply clauses to suppliers | GRC record |
| Validation | Supplier audits, exception reviews | Audit reports |
| Operations | Continuous KPI reporting | Dashboards |
| Audit | Organisational review | Consolidated report |

---

## 👥 Who carries out each action {#-quem-executa-cada-ação}

| Role | Responsibility |
|-------|------------------|
| **Developer** | Record exceptions and comply with policies |
| **AppSec Engineer** | Validate exceptions, oversee traceability |
| **DevOps / SRE** | Ensure technical execution in line with the clauses |
| **Executive Management** | Approve residual risk |
| **GRC / Compliance (Procurement + Legal)** | Integrate security clauses into contracts |
| **GRC / Compliance** | Consolidate metrics and audit suppliers |

---

## 📖 Normalised User Stories {#-user-stories-normalizadas}

### US-01 - Formal exception process with approval authorities by risk level {#us-01---processo-formal-de-exceções-com-alçadas-por-nível-de-risco}
**Context.** Without formal exceptions, practices are ignored without transparency. Without clear approval authorities by risk level, decisions are inconsistent and responsibility is dispersed.  

:::userstory
**Story.**   
As **Developer + AppSec Engineer**, I want **to submit security exceptions through a formal flow with automatic routing by risk level (L1→app manager, L2→AppSec+manager, L3→CISO+AppSec+senior management)**, so that **transparency, risk-proportionate approval and periodic revalidation are ensured**.  

**Acceptance criteria (BDD).**  
- **Given** that a control cannot be met in an application classified as L1, L2 or L3  
  **When** I submit an exception with technical justification and compensation  
  **Then** it is routed to the appropriate approval authority, assessed, and approved or rejected  
- And a revalidation schedule is automatically created (L3: 3 months, L2: 6 months, L1: annual)  

**Acceptance criteria (DoD).**  
- [ ] Exception recorded in a GRC tool with mandatory fields: application, risk (L1–L3), missing control, justification, compensation, owner  
- [ ] Approval authority determined automatically by risk level  
- [ ] Formal approval received (digital signature or timestamp record)  
- [ ] Revalidation schedule created and owner notified (30 days before expiry)  
- [ ] Mitigation issue created in the security backlog for the next release  
- [ ] Automatic notification sent to the owner if the exception is approaching expiry  

:::

**Artefacts & evidence.** Versioned exception register, Formalised decision with approval authority, Revalidation schedule, Backlog issue, Automatic notifications  

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Optional | Recommended | Mandatory |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Execution | Whenever there is a deviation | Developer (submission) + AppSec Engineer (validation) + Executive Management / CISO (approval according to level) | Approval within 5 days (L1–L2), 3 days (L3); Revalidation notification 30 days before expiry |

---

### US-02 - Security contractual clauses {#us-02---cláusulas-contratuais-de-segurança}
**Context.** Suppliers without clauses can compromise the entire chain.  

:::userstory
**Story.**   
As **GRC / Compliance (Legal + Procurement)**, I want **to include SbD-ToE clauses in contracts**, so that **supplier compliance is guaranteed**.  

**Acceptance criteria (BDD).**  
- **Given** a new contract  
  **When** clauses are applied  
  **Then** the supplier commits to complying with security practices  

**Acceptance criteria (DoD).**  
- [ ] Clauses published in a contract template  
- [ ] Contracts legally validated  
- [ ] Compliance monitoring  

:::

**Artefacts & evidence.** Contracts, clauses  

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Recommended | Mandatory | Mandatory + audits |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Planning | New contract | GRC / Compliance (Legal + Procurement) | According to the US cycle |

---

### US-03 - Continuous supplier validation {#us-03---validação-contínua-de-fornecedores}
**Context.** Compromised suppliers propagate risk.  

:::userstory
**Story.**   
As **GRC / Compliance**, I want **to validate suppliers continuously**, so that **compliance and contractual security are ensured**.  

**Acceptance criteria (BDD).**  
- **Given** an active supplier  
  **When** an audit takes place  
  **Then** the report documents compliance  

**Acceptance criteria (DoD).**  
- [ ] Annual audit  
- [ ] Report published  
- [ ] Findings recorded  

:::

**Artefacts & evidence.** Audit reports  

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Optional | Recommended | Mandatory |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Validation | Audit of an active supplier | GRC / Compliance | Annual audit |

---

### US-04 - Organisational traceability {#us-04---rastreabilidade-organizacional}
**Context.** Without traceability, management has no real visibility.  

:::userstory
**Story.**   
As an **AppSec Engineer**, I want **to aggregate security practices by project into an organisational dashboard**, so that **visibility is provided and adoption is measured**.  

**Acceptance criteria (BDD).**  
- **Given** active projects  
  **When** metrics are collected  
  **Then** the dashboard shows the overall status  

**Acceptance criteria (DoD).**  
- [ ] Dashboard configured  
- [ ] Metrics per chapter collected  
- [ ] Reports delivered to senior management  

:::

**Artefacts & evidence.** Dashboard, reports  

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic | Recommended | Mandatory |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Operation | Collection of metrics from active projects | AppSec Engineer + GRC / Compliance | According to the US cycle |

---

## 📊 Global Traceability Matrix {#-matriz-de-rastreabilidade-global}

The following table consolidates the traceability practices applied in each chapter, showing the focal point for audit and governance:

| Chapter | US | Context | Main artefact | Responsible |
|----------|----|---------|--------------------|-------------|
| **Ch. 02** | US-07 | Requirements with `SEC-Lx-*` tags | Backlog with traceability | QA / Product Owner |
| **Ch. 07** | US-03 | Logs and commit-build-release correlation | CI/CD reports + audit trail | DevOps / SRE |
| **Ch. 08** | US-02 | Versioned and traceable modules | IaC module history | DevOps / SRE |
| **Ch. 09** | US-06 | SBOM with provenance per image | `sbom.json` + metadata | DevOps / SRE |
| **Ch. 11** | US-02 | End-to-end traceability (build → deploy → runtime) | Attestations + deploy logs | DevOps / SRE |
| **Ch. 12** | US-01 | Correlated security events | Events + SIEM logs | Operations (Ops) / AppSec Engineer |
| **Ch. 14** | US-04 | Organisational metrics dashboard | Dashboard + quarterly reports | AppSec Engineer + GRC / Compliance |

**Notes:**
- Each chapter has **a traceability focal point** that is integrated into the organisational matrix
- **Ch. 14 - US-04** aggregates data from all chapters for executive visibility
- All artefacts must be **versioned** and **auditable** according to level L1–L3
- **Minimum SLA:** Monthly (L1), fortnightly (L2), continuous (L3) reports

---

### US-05 - Governance KPIs {#us-05---kpis-de-governação}
**Context.** Without metrics, there is no continuous improvement.  

:::userstory
**Story.**   
As **Executive Management**, I want **to define and monitor governance KPIs**, so that **the effectiveness of the SbD-ToE programme is assessed**.  

**Acceptance criteria (BDD).**  
- **Given** a quarterly cycle  
  **When** KPIs are measured  
  **Then** a report is shared with senior management  

**Acceptance criteria (DoD).**  
- [ ] KPIs defined (e.g. exceptions, audited suppliers)  
- [ ] Metrics collected  
- [ ] Report shared  

:::

**Artefacts & evidence.** KPI reports  

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic | Recommended | Mandatory |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Audit | Quarterly KPI measurement cycle | Executive Management + GRC / Compliance | According to the US cycle |

---

### US-06 - Execution of a formal supplier validation flow {#us-06---execução-de-fluxo-formal-de-validação-de-fornecedores}
**Context.** Unvalidated suppliers introduce untraceable risk into the supply chain.  

:::userstory
**Story.**   
As **GRC / Compliance (Procurement Officer)**, I want **to execute the formal supplier validation flow (questionnaire → AppSec analysis → approval)**, so that **new suppliers are guaranteed to meet minimum requirements before onboarding**.  

**Acceptance criteria (BDD).**  
- **Given** a new supplier classified as L2 or L3  
  **When** the validation flow is initiated  
  **Then** the questionnaire is sent, analysed by AppSec, and the approval/exception is recorded  

**Acceptance criteria (DoD).**  
- [ ] Validation checklist completed (questionnaire, clauses, evidence)  
- [ ] Technical analysis by the AppSec Engineer documented  
- [ ] Formalised decision (Approval / Rejection / Exception) recorded in GRC  
- [ ] Supplier Owner designated and notified  

:::

**Artefacts & evidence.** Questionnaire form, AppSec analysis report, GRC record  

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Optional | Recommended | Mandatory |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Planning | New L2/L3 supplier; start of the validation flow | AppSec Engineer + GRC / Compliance (Procurement Officer) | 2 weeks (L2), 1 week (L3) |

**Useful links.**  
- [Supplier Validation Model](./addon/modelo-validacao-fornecedores)
- [Practical Examples](./addon/exemplos-aplicacao-governanca)

---

### US-07 - Continuous cycle of exception review and reassessment {#us-07---ciclo-contínuo-de-revisão-e-reavaliação-de-exceções}
**Context.** Forgotten exceptions become permanent unmitigated risk.  

:::userstory
**Story.**   
As an **AppSec Engineer**, I want **to review and reassess exceptions and compensations periodically**, so that **residual risk is guaranteed to remain mitigated and compensations remain effective**.  

**Acceptance criteria (BDD).**  
- **Given** an active exception or compensation with a review deadline  
  **When** the scheduled review date arrives (or a critical event occurs)  
  **Then** it is reassessed, revalidated, extended or closed  

**Acceptance criteria (DoD).**  
- [ ] Review schedule defined by criticality (L3 quarterly, L2 half-yearly)  
- [ ] Exception register updated with the new review date  
- [ ] Reassessment documented (maintained, extended, closed)  
- [ ] Security Owner notified and decision approved  

:::

**Artefacts & evidence.** Exception table with deadlines, Reassessment report, Notification to owner  

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic | Recommended | Mandatory |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Operation | Schedule (quarterly/half-yearly), Critical incident, Architecture change | AppSec Engineer + GRC / Compliance | Reassessment within 5 working days |
| Validation | Schedule (quarterly/half-yearly), Critical incident, Architecture change | AppSec Engineer + GRC / Compliance | Reassessment within 5 working days |

**Useful links.**  
- [Continuous Validation](./addon/validacao-continuada)

---

### US-08 - Compliance repository per application (systematic control) {#us-08---repositório-de-conformidade-por-aplicação-controlo-sistemático}
**Context.** Without a centralised repository, the security status remains invisible to auditors and management.  

:::userstory
**Story.**   
As **AppSec Engineer + Scrum Master / Team Lead**, I want **to maintain a structured compliance repository for each application**, so that **the status of all SbD-ToE practices is consolidated and internal and external audits are facilitated**.  

**Acceptance criteria (BDD).**  
- **Given** an application classified as L1, L2 or L3  
  **When** the repository is created or updated  
  **Then** it reflects the status of all chapters (2–13) in a structured checklist  

**Acceptance criteria (DoD).**  
- [ ] Repository created (YAML file, versioned MD or GRC dashboard)  
- [ ] Checklist per chapter (02–13) included with binary status (Yes/No/Exception)  
- [ ] Validation evidence linked (links to reports, tests, scans, audits)  
- [ ] Change history maintained and auditable  
- [ ] Updated per relevant release or critical event  

:::

**Artefacts & evidence.** Compliance file (YAML/MD), Links to validation reports, Version history  

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic | Recommended | Mandatory |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Planning | Creation or update of the repository; relevant release or critical event | AppSec Engineer + Scrum Master / Team Lead + GRC / Compliance | Update per release or 5 days after a critical event |
| Execution | Creation or update of the repository; relevant release or critical event | AppSec Engineer + Scrum Master / Team Lead + GRC / Compliance | Update per release or 5 days after a critical event |
| Validation | Creation or update of the repository; relevant release or critical event | AppSec Engineer + Scrum Master / Team Lead + GRC / Compliance | Update per release or 5 days after a critical event |

**Useful links.**  
- [Systematic Control of SbD-ToE Practices](./addon/controlos-praticas-sbd)
- [Organisational Traceability](./addon/rastreabilidade-organizacional)

---

### US-09 - Formal designation of security owners per application {#us-09---designação-formal-de-owners-de-segurança-por-aplicação}
**Context.** Without a clear owner, dispersed responsibility results in neglect of exceptions and validations.  

:::userstory
**Story.**   
As **Executive Management**, I want **to formally designate a security owner (Security Champion) for each critical application**, so that **clear accountability, continuity of security decisions and risk communication are guaranteed**.  

**Acceptance criteria (BDD).**  
- **Given** an application classified as L2 or L3  
  **When** a Security Champion is designated  
  **Then** they are responsible for submitting exceptions, validations, risk communication and policy compliance  

**Acceptance criteria (DoD).**  
- [ ] Security Champion designated in writing (official e-mail, document, HR system)  
- [ ] Responsibilities documented (exceptions, validation, communication, traceability)  
- [ ] Mandatory SbD-ToE training completed (Ch. 13 - Training and Onboarding)  
- [ ] Centralised register maintained (Git, Confluence, SharePoint)  
- [ ] Formal notification to the previous owner (if there is rotation)  

:::

**Artefacts & evidence.** Designation document, Proof of training, Centralised register of owners  

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Recommended | Mandatory | Mandatory |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Planning | L2/L3 application; project kick-off or owner rotation | Executive Management + Security Champion + AppSec Engineer | Designation at project kick-off or change of owner |

**Useful links.**  
- [Governance Model](./addon/modelo-governancao)
- [Training and Onboarding (Ch. 13)](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle)  

---

### US-10 - Periodic validation of applications (compliance cycle) {#us-10---validação-periódica-de-aplicações-ciclo-de-conformidade}
**Context.** Without recurring validations, deviations are not detected until an audit or incident.  

:::userstory
**Story.**   
As **AppSec Engineer + GRC / Compliance**, I want **to execute periodic compliance validations against SbD-ToE on each application**, so that **requirements are ensured to remain applied and effective, deviations are detected early, and evidence is kept up to date**.  

**Acceptance criteria (BDD).**  
- **Given** a review schedule defined by criticality (L3 quarterly, L2 half-yearly)  
  **When** the review cycle arrives  
  **Then** the application is reassessed, evidence collected, and status updated in the repository  

**Acceptance criteria (DoD).**  
- [ ] Review schedule defined and communicated to the Scrum Master / Team Lead  
- [ ] Validation checklist per chapter executed  
- [ ] Evidence collected (tests, scans, reviews, external audits)  
- [ ] Compliance report generated with clear status  
- [ ] Findings and deviations recorded in a tracking system (Jira, etc.)  
- [ ] Action plan created for critical non-conformities  

:::

**Artefacts & evidence.** Validation report per cycle, Completed checklist, Action plan for findings, Cycle history  

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Annual | Half-yearly | Quarterly |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Validation | Cyclical schedule, Relevant release, Critical incident | AppSec Engineer + GRC / Compliance + Scrum Master / Team Lead | Cycle completed within 2 weeks of the trigger |
| Audit | Cyclical schedule, Relevant release, Critical incident | AppSec Engineer + GRC / Compliance + Scrum Master / Team Lead | Cycle completed within 2 weeks of the trigger |

**Useful links.**  
- [Continuous Validation](./addon/validacao-continuada)
- [Systematic Control of Practices](./addon/controlos-praticas-sbd)

---

### US-11 - Consolidation of governance and maturity KPIs {#us-11---consolidação-de-kpis-de-governação-e-maturidade}
**Context.** Without consolidated metrics, executive decisions on the effectiveness of SbD-ToE lack an empirical basis.  

:::userstory
**Story.**   
As **CISO + Executive Management**, I want **to consolidate and report governance KPIs (exceptions, audited suppliers, compliance per chapter, maturity)**, so that **the organisation's security maturity is assessed objectively and strategic decisions are taken**.  

**Acceptance criteria (BDD).**  
- **Given** compliance and exception data per application  
  **When** the reporting cycle arrives (quarterly/half-yearly)  
  **Then** KPIs are calculated, visualised and reported to senior management  

**Acceptance criteria (DoD).**  
- [ ] KPIs defined (e.g. % applications with traceability, % exceptions resolved, % suppliers audited, SAMM/SSDF maturity level)  
- [ ] Dashboard configured with metrics per chapter and per application  
- [ ] Data aggregated from all projects, teams and suppliers  
- [ ] Consolidated report delivered to Executive Management, CISO and GRC  
- [ ] Trends identified and recommendations included  
- [ ] History maintained for trend analysis  

:::

**Artefacts & evidence.** KPI dashboard, Quarterly/half-yearly consolidated report, Trend history, Executive analysis  

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic | Recommended | Mandatory |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Audit | Quarterly (minimum), Half-yearly (recommended) | GRC / Compliance + AppSec Engineer + CISO | Report published 5 days after the end of the period |
| Operation | Quarterly (minimum), Half-yearly (recommended) | GRC / Compliance + AppSec Engineer + CISO | Report published 5 days after the end of the period |

**Useful links.**  
- [Governance and Maturity](./addon/governancao-maturidade)
- [Organisational Traceability](./addon/rastreabilidade-organizacional)

---

### US-12 - Formalisation of a governance model by risk level {#us-12---formalização-de-modelo-de-governação-por-nível-de-risco}
**Context.** Without a documented formal model, security decisions are scattered across AppSec, Management and Legal. The lack of explicit criteria for approval by level results in inconsistency, untraceable risk, and stakeholder mistrust.

:::userstory
**Story.**   
As **CISO + AppSec Engineer**, I want **to formalise and document the governance model with explicit approval authority levels and clear roles and responsibilities**, so that **security decisions are guaranteed to be taken with appropriate authority, consistency, and full traceability**.

**Acceptance criteria (BDD).**  
- **Given** that the organisation adopts SbD-ToE  
  **When** a new governance model is defined or revised  
  **Then** it is documented with approval authorities per L1–L3, approved by senior management, and communicated to all stakeholders  

**Acceptance criteria (DoD).**  
- [ ] Formal "SbD-ToE Security Governance Policy" document approved by senior management  
- [ ] Approval authority levels explicitly defined: L1 (Application Manager), L2 (AppSec + Manager), L3 (CISO + AppSec + Senior Management)  
- [ ] Roles and responsibilities mapped by function (Dev, AppSec, Management, Legal, GRC, CISO)  
- [ ] Decision record template created (Jira / SharePoint / Git) with mandatory fields  
- [ ] Escalation flow documented with SLAs per level  
- [ ] Training delivered to all approvers (Ch. 13 - Governance Training Track)  
- [ ] Official communication published on corporate channels  

:::

**Artefacts & evidence.** Policy document, Decision template, Repository of recorded decisions, Proof of approver training, Communication e-mail  

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic | Recommended | Mandatory |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Planning | SbD-ToE kick-off, annual review, organisational change | CISO + AppSec Engineer + GRC / Compliance (Legal) | Publication within 2 weeks |
| Execution | SbD-ToE kick-off, annual review, organisational change | CISO + AppSec Engineer + GRC / Compliance (Legal) | Publication within 2 weeks |

**Useful links.**  
- [Governance Model](./addon/modelo-governancao)
- [Decision Examples](./addon/exemplos-aplicacao-governanca)
- [Governance Training (Ch. 13)](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle)  

---

### US-13 - Systematic and periodic control per SbD-ToE chapter {#us-13---controlo-sistemático-e-periódico-por-capítulo-sbd-toe}
**Context.** Without a centralised compliance checklist, an application's compliance status with Ch. 2–13 remains invisible. Deviations are not detected until an audit or critical incident. Management has no visibility of progress.

:::userstory
**Story.**   
As **AppSec Engineer + Scrum Master / Team Lead**, I want **to maintain a centralised, versioned and auditable checklist of compliance with all SbD-ToE chapters (2–13), with periodic verification per release or critical event**, so that **the real status of all practices is consolidated and audits, risk decisions, and demonstration of regulatory compliance are facilitated**.

**Acceptance criteria (BDD).**  
- **Given** an application classified as L1, L2 or L3  
  **When** a validation cycle is triggered (per release, quarterly for L3, half-yearly for L2, or critical event)  
  **Then** the checklist is completed with status, evidence is linked, and a report is generated  

**Acceptance criteria (DoD).**  
- [ ] Versioned checklist file created in a repository (YAML, MD or GRC dashboard) with the structure: Chapter | Practice | Status (Yes/No/Exception/N/A) | Evidence (link/reference) | Owner | Validation date  
- [ ] Integration with the version control system (Git) or GRC with auditable history  
- [ ] Triggers defined and automated: relevant release, critical event (incident, CVE), scheduled cycle (L3 quarterly, L2 half-yearly, L1 annual)  
- [ ] History maintained with dated changes and those responsible (audit trail)  
- [ ] Consolidated report generated per cycle with % compliance, critical findings, and action plan  
- [ ] Evidence artefacts linked or referenced in the checklist (links to tests, scans, reports, audits)  
- [ ] Automatic notification sent to the Scrum Master / Team Lead and AppSec Engineer when a cycle is triggered  

:::

**Artefacts & evidence.** Versioned checklist file (YAML/MD), Git history or GRC dashboard, Reports per cycle, Links to validation artefacts, Action plan for non-conformities, Version history  

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic | Recommended | Mandatory |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Planning | Relevant release, critical event, scheduled cycle (quarterly/half-yearly/annual) | AppSec Engineer (validation) + Scrum Master / Team Lead (completion) + GRC / Compliance (consolidation) | Update within 5 working days of the trigger |
| Execution | Relevant release, critical event, scheduled cycle (quarterly/half-yearly/annual) | AppSec Engineer (validation) + Scrum Master / Team Lead (completion) + GRC / Compliance (consolidation) | Update within 5 working days of the trigger |
| Validation | Relevant release, critical event, scheduled cycle (quarterly/half-yearly/annual) | AppSec Engineer (validation) + Scrum Master / Team Lead (completion) + GRC / Compliance (consolidation) | Update within 5 working days of the trigger |
| Audit | Relevant release, critical event, scheduled cycle (quarterly/half-yearly/annual) | AppSec Engineer (validation) + Scrum Master / Team Lead (completion) + GRC / Compliance (consolidation) | Update within 5 working days of the trigger |

**Useful links.**  
- [Systematic Control of SbD-ToE Practices](./addon/controlos-praticas-sbd)
- [Organisational Traceability](./addon/rastreabilidade-organizacional)
- [Periodic Validation](./addon/validacao-continuada)

---

### US-14 - Continuous reassessment and rotation of suppliers post-onboarding {#us-14---reavaliação-contínua-e-rotação-de-fornecedores-pós-onboarding}
**Context.** Suppliers are validated at onboarding, but without periodic review, deviations emerge over time (new unmitigated CVEs, SLA not met, changes of ownership, evolution of risk). Residual risk accumulates invisibly. Contracts expire without renewal of validation.

:::userstory
**Story.**   
As **AppSec Engineer + GRC / Compliance (Procurement Officer)**, I want **to reassess and re-approve suppliers periodically (annual by default, half-yearly for L2, quarterly for L3), with updated technical validation, SLA compliance analysis, and escalation for a penalty or replacement decision if necessary**, so that **they are ensured to continue meeting requirements and SLAs, risk is mitigated, and continuity decisions are based on evidence**.

**Acceptance criteria (BDD).**  
- **Given** an active supplier with a contract in force  
  **When** the scheduled review date arrives (calendar) or a critical event occurs (incident, critical CVE, SLA change)  
  **Then** the supplier is reassessed with an updated questionnaire, validated technical evidence (SBOM, SLA compliance, changes) and the decision is formalised  

**Acceptance criteria (DoD).**  
- [ ] Supplier review schedule defined and communicated (annual minimum, 6 months for L2, quarterly for L3, or per critical event)  
- [ ] Updated questionnaire with security and SLA questions sent to the supplier  
- [ ] Technical analysis documented (AppSec): SBOM validated, CVEs analysed, SLA compliance verified, organisational/technical changes identified  
- [ ] Decision formalised and recorded in GRC: Approved / Exception created / Penalty proposed / Termination initiated  
- [ ] Owner formally notified by e-mail with the decision and next review date  
- [ ] Mitigation plan created if gaps are identified (deadline, AppSec owner, expected validation)  
- [ ] Register updated in the supplier repository with date, decision-maker, and history  

:::

**Artefacts & evidence.** Review schedule, Updated questionnaire + answers, Documented technical analysis, Decision recorded in GRC, Formal communication to the supplier, Mitigation plan if applicable, Decision history  

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Annual | Half-yearly | Quarterly / critical event |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Validation | Scheduled calendar (annual/half-yearly), Critical incident, Unmitigated critical CVE, Change of contract/ownership/SLA | AppSec Engineer (technical analysis) + GRC / Compliance (Procurement Officer — coordination; decision and record) | Reassessment completed within 2 weeks of the trigger |
| Operation | Scheduled calendar (annual/half-yearly), Critical incident, Unmitigated critical CVE, Change of contract/ownership/SLA | AppSec Engineer (technical analysis) + GRC / Compliance (Procurement Officer — coordination; decision and record) | Reassessment completed within 2 weeks of the trigger |

**Useful links.**  
- [Supplier Validation Model](./addon/modelo-validacao-fornecedores)
- [Continuous Validation](./addon/validacao-continuada)
- [Application Examples](./addon/exemplos-aplicacao-governanca)

---

### US-15 - Technical Preparation and Validation of Contractors Before Access {#us-15---preparação-técnica-e-validação-de-contractors-pré-acesso}
**Context.** Contractors gain access without understanding security policies, mandatory tools, or procedures. Risk of involuntary error (exposed credentials, unauthorised data access, insecure practices).

:::userstory
**Story.**   
As a **Security Champion (HR/Recruiter)**, I want **to execute a structured technical preparation process for contractors (screening, mandatory training, comprehension test, sandbox environment) before they gain access to systems**, so that **they are guaranteed to be prepared, to have understood fundamental policies, and to be able to work securely**.

**Acceptance criteria (BDD).**  
- **Given** a new contractor approved by Procurement (US-06) and a signed contract  
  **When** the project start date arrives  
  **Then** the preparation track is triggered: mandatory training, quiz, sandbox setup, NDA confirmation  

**Acceptance criteria (DoD).**  
- [ ] Preparation checklist completed (skills screening, expected security level, required training defined)  
- [ ] Profile-based training track (Dev, DevOps, QA, etc.) started in the LMS or training platform  
- [ ] Security policy comprehension quiz completed (minimum score 80%)  
- [ ] Access to a sandbox environment provided for practice (e.g. private Git repository, demo application, security tools)  
- [ ] NDA and confidentiality agreement digitally signed with timestamp  
- [ ] Technical onboarding checklist completed and validated by the team (Security Champion + Scrum Master / Team Lead)  
- [ ] Real access to systems granted only after all approval steps  
- [ ] "Ready for access" record documented in GRC with date, validator, and reference to all validations  

:::

**Artefacts & evidence.** Completed preparation checklist, Confirmed LMS enrolment, Validated quiz score, Sandbox access credentials, Digitally signed agreements, Onboarding checklist, GRC "ready for access" record

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic | Recommended | Mandatory + validated quiz |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Planning | Contract signed, project start date | Security Champion (HR coordination) + AppSec Engineer (validation) + Scrum Master / Team Lead (sandbox setup) | Completion 2–3 working days before the start date; Notification: Contractor informed by e-mail about the track |

**Useful links.**  
- [Ch. 13 - Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle)  
- [Supplier Validation - US-06](#us-06---execução-de-fluxo-formal-de-validação-de-fornecedores)  
- [Contractor Validation Template](/sbd-toe/sbd-manual/governanca-contratacao/addon/template-validacao-contractors)
- [Sandbox Preparation Guide](/sbd-toe/sbd-manual/formacao-onboarding/addon/guia-preparacao-sandbox)  
- Canonical grounding: [`GOV-013`](./addon/catalogo-requisitos-governanca)  

---

### US-16 - Mandatory Training Track Before Access (Contractors) {#us-16---trilho-de-formação-obrigatória-pré-acesso-contractors}
**Context.** Contractors started without completing mandatory security training. Lack of clear integration between Ch. 13 (Training) and Ch. 14 (Governance): who approves, what the SLA is, how it is tracked.

:::userstory
**Story.**   
As **CISO + Security Champion (Training Manager)**, I want **to define and execute a mandatory training track per contractor profile, with an explicit completion SLA before technical access**, so that **minimum security awareness, regulatory compliance (DORA, NIS2), and traceability of preparation are guaranteed**.

**Acceptance criteria (BDD).**  
- **Given** a newly hired contractor  
  **When** a training track is assigned in the LMS  
  **Then** they must complete mandatory courses, pass a quiz, and have a consolidated record before real access  

**Acceptance criteria (DoD).**  
- [ ] Training track defined per profile (Developer, DevOps, QA, Architecture, etc.) with estimated duration  
- [ ] Mandatory courses listed and mapped to SbD-ToE chapters:  
    - **[O1] General Security Awareness** (2h) → Ch. 00 + 02 + 14  
    - **[O2] SbD-ToE Overview** (1h) → Ch. 01–03 (risk, requirements, threat modelling)  
    - **[O3] Secure Coding & SAST** (2h) → Ch. 06 (if developer)  
    - **[O4] CI/CD Security & Artefacts** (1h) → Ch. 07 (if DevOps)  
    - **[O5] Incident Response Basics** (1h) → Ch. 12  
    - **[O6] Supply Chain & Dependencies** (1h) → Ch. 05 (if involved with builds)  
- [ ] Assessment quiz per course (minimum score 80%) completed  
- [ ] Centralised register updated (LMS or Confluence) with dates, scores, validator  
- [ ] Completion SLA communicated to the contractor: Maximum **5 working days before the start date**  
- [ ] Automatic notification sent if the SLA is at risk (e.g. 2 days before the deadline)  
- [ ] "Training complete" sign-off provided to the AppSec Engineer (releases technical access)  
- [ ] History kept for 3 years (DORA, NIS2 requirement)  

:::

**Artefacts & evidence.** Training track defined per profile, LMS enrolment, Quiz completion records, Completion sign-off, SLA compliance checklist, Notifications sent

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic | Mandatory | Mandatory + 80% score required |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Planning | Contractor approved (end of US-06/US-15) | AppSec Engineer (completion validation) + Security Champion (Training Manager — track coordination; HR traceability) | Training completed before real access; Notification: weekly if at risk, daily if `<`3 days |
| Execution | Contractor approved (end of US-06/US-15) | AppSec Engineer (completion validation) + Security Champion (Training Manager — track coordination; HR traceability) | Training completed before real access; Notification: weekly if at risk, daily if `<`3 days |

**Useful links.**  
- [Ch. 13 - Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle)  
- [Designation of Security Owners - US-09](#us-09---designação-formal-de-owners-de-segurança-por-aplicação)  
- [Technical Preparation - US-15](#us-15---preparação-técnica-e-validação-de-contractors-pré-acesso)  
- Canonical grounding: [`GOV-013`](./addon/catalogo-requisitos-governanca)  

---

### US-17 - Secure Offboarding of Contractors and Supplier Termination {#us-17---offboarding-seguro-de-contractors-e-rescisão-de-fornecedores}
**Context.** Contractors finish a project or contract without a formal process: access remains active, assets (code, credentials, documents) are not recovered. Risk of post-termination leakage, residual access, breach of confidentiality.

:::userstory
**Story.**   
As **Security Champion (HR) + DevOps / SRE**, I want **to execute a formal and automatic secure offboarding process when a contractor finishes or a supplier is terminated**, so that **access is guaranteed to be fully revoked, assets recovered, confidentiality maintained, and legal compliance ensured**.

**Acceptance criteria (BDD).**  
- **Given** a contractor whose end date is known (or a supplier terminated with notice)  
  **When** the offboarding date arrives  
  **Then** access is revoked, assets recovered, and completion documented  

**Acceptance criteria (DoD).**  
- [ ] Offboarding checklist prepared 2 weeks in advance (DevOps / SRE, Security Champion, AppSec Engineer, Scrum Master / Team Lead)  
- [ ] Formal notification sent to the contractor/supplier with the exact deactivation date  
- [ ] Access to systems revoked (at most 24h after the end date):  
    - User accounts deactivated in Git, Jira, CI/CD  
    - SSH keys and API tokens removed  
    - VPN, cloud IAM access revoked  
    - MFA removed  
    - Corporate e-mail accounts deactivated (if applicable)  
- [ ] Assets recovered:  
    - Code/repositories transferred or archived (if the contractor developed them)  
    - Documentation delivered and versioned  
    - Laptop/hardware returned, wiped, and certified clean  
    - Secrets (API keys, passwords) rotated  
- [ ] Last backup of the contractor's work performed (e.g. clone of private repos)  
- [ ] Formal "offboarding complete" sign-off recorded in GRC with timestamp  
- [ ] Legal reminder sent to the contractor: Confidentiality obligations continue after termination (duration, consequences)  
- [ ] Offboarding report archived for 7 years (DORA requirement)  

:::

**Artefacts & evidence.** Completed offboarding checklist, Confirmation of access deactivation, Backup certificate, Recovered assets (inventory), GRC sign-off, Legal notice, Archived report

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic | Mandatory | Mandatory + audit trail |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Operation | Known end date (scheduled), Immediate termination (unscheduled) | DevOps / SRE (technical access) + AppSec Engineer (validation) + Security Champion (HR timeline coordination; checkpoints) | Offboarding completed within **`<`24h** of the end date; Notification: HR sends notice 2 weeks in advance |
| Validation | Known end date (scheduled), Immediate termination (unscheduled) | DevOps / SRE (technical access) + AppSec Engineer (validation) + Security Champion (HR timeline coordination; checkpoints) | Offboarding completed within **`<`24h** of the end date; Notification: HR sends notice 2 weeks in advance |

**Useful links.**  
- [Supplier Reassessment - US-14](#us-14---reavaliação-contínua-e-rotação-de-fornecedores-pós-onboarding)  
- [Technical Preparation - US-15](#us-15---preparação-técnica-e-validação-de-contractors-pré-acesso)  
- [Offboarding Checklist](/sbd-toe/sbd-manual/governanca-contratacao/addon/checklist-offboarding)  

---

### US-18 - Continuous Monitoring of Supplier Compliance (Alerts and Escalation) {#us-18---monitorização-contínua-de-conformidade-de-fornecedores-alertas-e-escalação}
**Context.** Suppliers are assessed periodically (US-14), but risk between cycles is not detected. CVEs, critical incidents, SLA changes, or breaches are not monitored in real time.

:::userstory
**Story.**   
As **AppSec Engineer + Operations (Ops)**, I want **to continuously monitor the compliance of critical suppliers (incidents, CVEs, SLA, organisational changes) and escalate automatically if gaps emerge**, so that **residual risk between formal assessment cycles is reduced and critical events are detected in real time**.

**Acceptance criteria (BDD).**  
- **Given** a critical supplier (L2–L3) with a contract in force  
  **When** an incident, critical CVE, SLA breach, or organisational change is reported  
  **Then** an automatic alert is generated and escalated to AppSec and Procurement  

**Acceptance criteria (DoD).**  
- [ ] Integration with the supplier's incident feed (status page, e-mail alerts, API)  
- [ ] Continuous monitoring of CVEs in the supplier's technical stack (via SBOM/SCA tool)  
- [ ] Automatic alert triggered if:  
    - Critical CVE in a supplier dependency not mitigated within 72h (L3) or 7 days (L2)  
    - Security incident reported by the supplier  
    - SLA not met (e.g. uptime `<`99.5% for L3, `<`99% for L2)  
    - Change of ownership, location, or subcontracting  
- [ ] Automatic escalation with priority:  
    - **P0 (exploited critical CVE):** Immediate → AppSec Engineer + GRC / Compliance (Procurement Officer) + CISO  
    - **P1 (critical CVE, serious incident):** 1h → AppSec Engineer + GRC / Compliance (Procurement Officer)  
    - **P2 (high CVE, moderate incident):** 4h → AppSec Engineer  
- [ ] Automatic trigger of a special out-of-cycle review (US-14) if there is a critical gap  
- [ ] Record of alert, escalation, and action documented in GRC (audit trail)  
- [ ] Real-time dashboard with the status of critical suppliers and active alerts (visible to the board)  

:::

**Artefacts & evidence.** Incident feed configured, Active CVE monitoring, Alerts documented with timestamps, Escalation records, Dashboard, GRC audit trail

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| No | Recommended | Mandatory |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Operation | Incident, critical CVE, SLA breach, contractual change | AppSec Engineer (initial setup) + Operations (Ops) (24x7 operation) | Alert within **`<`1h** of detection, escalation within `<`15 min |

**Useful links.**  
- [Supplier Reassessment - US-14](#us-14---reavaliação-contínua-e-rotação-de-fornecedores-pós-onboarding)  
- [Monitoring and Operations - Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle)  
- [Dependencies and SCA - Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle)  

---

### US-19 - Quarterly Review of Contractor Access (Least Privilege) {#us-19---revisão-trimestral-de-acesso-de-contractors-least-privilege}
**Context.** Contractors gain initial access, but permissions accumulate over time ("access creep"). Without periodic review, the principle of least privilege is violated.

:::userstory
**Story.**   
As **Security Champion + DevOps / SRE + Scrum Master / Team Lead**, I want **to review the access of active contractors quarterly, validating that they only have the access needed for the project**, so that **the principle of least privilege is maintained, the risk of excessive access is reduced, and obsolete access is removed**.

**Acceptance criteria (BDD).**  
- **Given** active contractors with access to systems (repos, CI/CD, databases, cloud)  
  **When** the quarterly review cycle arrives  
  **Then** access is validated with the Scrum Master / Team Lead, and excessive access is removed on the same day  

**Acceptance criteria (DoD).**  
- [ ] List of active contractors extracted from systems (Git orgs, Jira, VPN, Cloud IAM, databases)  
- [ ] For each contractor:  
    - Access listed in detail (repositories, CI/CD pipelines, databases, cloud resources, etc.)  
    - Scrum Master / Team Lead validates each access: **Needed for the current project?** (Yes/No/Modify)  
    - If **Not needed:** access removed on the same day  
    - If **Modify:** new scope configured, old one revoked  
    - If **Yes:** maintained with dated confirmation  
- [ ] Review checklist completed and digitally signed by the Scrum Master / Team Lead + Security Champion  
- [ ] Notification sent to each contractor informing them of the review outcome  
- [ ] If access is removed: clear notification indicating the reason and completion date  
- [ ] Record of changes documented in the audit trail (Git logs, IAM change log, etc.)  
- [ ] Consolidated report (% of access maintained, % removed) delivered to the AppSec Engineer  

:::

**Artefacts & evidence.** List of contractors and access, Signed checklist, Notifications sent, Git/IAM change logs, Consolidated report, Sign-off

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Half-yearly | Quarterly | Quarterly |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Validation | Schedule (quarterly), Project change, Incident | Security Champion (coordination) + Scrum Master / Team Lead (validation of need) + DevOps / SRE (technical changes) | Review started and completed within **1 week** |

**Useful links.**  
- [Technical Preparation - US-15](#us-15---preparação-técnica-e-validação-de-contractors-pré-acesso)  
- [Offboarding - US-17](#us-17---offboarding-seguro-de-contractors-e-rescisão-de-fornecedores)  
- [Authentication and Access Requirements - Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle)  
- Canonical grounding: [`GOV-014`](./addon/catalogo-requisitos-governanca)  

---

### US-20 - Post-Project Feedback and Contractor Rating {#us-20---feedback-pós-projeto-e-rating-de-contractors}
**Context.** Contractors finish a project without feedback on their security performance. Without assessment data, it is impossible to take an informed decision on re-hire or referral.

:::userstory
**Story.**   
As **Security Champion + Scrum Master / Team Lead**, I want **to collect structured post-project feedback on contractors covering security understanding, incidents, and recommendations**, so that **re-hire decisions are informed, the preparation programme is improved, and an assessment database is created**.

**Acceptance criteria (BDD).**  
- **Given** a contractor whose project is ending  
  **When** offboarding is initiated (US-17)  
  **Then** a feedback form is sent for the Scrum Master / Team Lead + AppSec Engineer to complete  

**Acceptance criteria (DoD).**  
- [ ] Feedback form created with structured questions:  
    - **Security:** Understanding of policies (scale 1–5), Best practices applied (Yes/No), Incidents during the project (Yes/No + desc)  
    - **Performance:** Code quality (1–5), Testing (1–5), Documentation (1–5)  
    - **Compliance:** Contractor followed mandatory procedures (Yes/No), Violations (Yes/No + desc)  
    - **Recommendations:** Areas for improvement in training/preparation, Overall security rating (1–5 stars)  
    - **Decision:** Re-hire recommended? (Yes/No/Maybe + justification)  
- [ ] Feedback collected from the Scrum Master / Team Lead + AppSec Engineer + Security Champion (consensus)  
- [ ] Result recorded in a centralised system (HR, Procurement, GRC) with date and reviewers  
- [ ] Rating (positive/neutral/negative) stored as a reference for future hiring  
- [ ] If there are multiple contractors from the same supplier: aggregated insights for supplier review (US-14)  
- [ ] Consolidated results published in a quarterly report of the contractor programme  

:::

**Artefacts & evidence.** Completed feedback form, Ratings recorded (HR/GRC system), Aggregation per supplier, Quarterly report, History of assessments

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Optional | Recommended | Mandatory |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Operation | Offboarding initiated (US-17) | Security Champion (coordination) + Scrum Master / Team Lead + AppSec Engineer (completion) | Feedback completed within **3 working days** after the end of the contract |

**Useful links.**  
- [Offboarding - US-17](#us-17---offboarding-seguro-de-contractors-e-rescisão-de-fornecedores)  
- [Supplier Reassessment - US-14](#us-14---reavaliação-contínua-e-rotação-de-fornecedores-pós-onboarding)  
- [Designation of Owners - US-09](#us-09---designação-formal-de-owners-de-segurança-por-aplicação)  

---

### US-21 - Contracting AI model providers {#us-21}

**Context.**
US-14 covers continuous reassessment of suppliers in general. When the supplier is an **AI model provider** (Anthropic, OpenAI, Google, Mistral, Cohere, HuggingFace, in-house *self-hosted* providers), clauses arise that traditional contracts did not cover: *data retention*, *training opt-out*, processing location (GDPR), audit rights over inference logs, SLA for notification of version changes, declared compliance with AI Act Art. 53/55 when the provider supplies GPAI. This US operationalises those contractual requirements before the provider enters the approved list (cross-link [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)).

:::userstory
**Story.**
As **GRC / Compliance (Procurement + Legal)**, I want each contract with an AI model provider to include minimum clauses covering data handling, location, *audit rights*, change notification and applicable regulatory compliance, so that operational use of the provider is legally and technically sustainable.

**Acceptance criteria (BDD).**
- **Given** that a new AI provider is intended to be adopted for operational use
  **When** contractual due diligence begins
  **Then** the *due diligence* (cross-link Policy 33 §3) is extended with the AI-specific criteria: data retention, training opt-out, location (GDPR Art. 44–49), audit rights, notification SLA, AI Act Art. 53/55 when GPAI
- **Given** that the contract is finalised
  **When** the provider is added to the approved list ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014))
  **Then** the `contract_ref` references the contract in force and records critical clauses
- **Given** that the provider changes its data model (e.g. a new training policy) or the model's major version
  **When** it is notified according to the contractual SLA
  **Then** a review runs (`appsec` + `grc`) before the *cutover*; without adequate notification, a proactive review is triggered

**Checklist.**
- [ ] *Data retention*: declared (preference for zero retention for sensitive data); compatible with the classification of the data the system sends
- [ ] *Training opt-out*: contracted when applicable; declared when "opt-out by default"
- [ ] **Processing location**: documented; compliant with GDPR Art. 44–49 when there is personal data; clauses for *international transfers* when applicable
- [ ] **Audit rights**: contracted access to inference logs or equivalent when required (typical at L3)
- [ ] **Prior notification SLA** for changes that alter behaviour (major model version, data policy, discontinuation)
- [ ] **Availability SLA** declared; architectural *fallback* in case of *outage* (cross-link Ch. 04 §AI/ML)
- [ ] **Declared compliance with AI Act Art. 53/55** when the provider supplies GPAI
- [ ] **Declared compliance with GDPR Art. 28** (sub-processors) when there is personal data
- [ ] Provider included in the approved list ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)) with `risk_classification`
- [ ] Critical clauses recorded in the provider's record sheet; review scheduled

:::

**🧾 Artefacts & evidence.**
- Contract signed with explicit clauses (referenced in `contract_ref` of the approved list)
- Provider record sheet in the governance repository (`governance/ai-providers/<provider>.md`) with critical clauses
- Record of notifications received from the provider + actions taken
- Periodic review documented according to the risk level

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Recommended | Minimum clauses: location + zero retention for sensitive data |
| L2 | Yes | Detailed clauses: retention, opt-out, location, SLA, basic audit rights |
| L3 | Yes | Detailed clauses + operational audit rights + AI Act Art. 53/55 when GPAI; Legal review mandatory |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Pre-onboarding | Adoption of a new AI provider | GRC / Compliance (Procurement + Legal) | Before operational use |
| Operation | Change notification by the provider | AppSec Engineer + GRC / Compliance | According to the contractual SLA; pre-*cutover* |
| Periodic review | Cadence by risk level | GRC / Compliance | L1 annual / L2 half-yearly / L3 quarterly |
| Discontinuation | Provider removed from the list | GRC / Compliance + DevOps / SRE | Migration plan before operational removal |

**Useful links.**
- 🔗 [`DEP-014` — List of approved AI providers](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)
- 🔗 [US-14 of Ch. 05 — AI BOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle)
- 🔗 [Policy 33 — Secure Contracting (AI providers annex)](/sbd-toe/assets/policies/policy-contratacao-segura)
- 🔗 [Policy 39 — AI BOM and Supply Chain](/sbd-toe/assets/policies/policy-ai-bom-supply-chain)
- 🔗 [Cross-check AI Act](/sbd-toe/cross-check-normativo/ai-act/intro)
- 🔗 [Cross-check GDPR](/sbd-toe/cross-check-normativo/gdpr/intro)

---

### US-22 - Formal approval and periodic audit of organisational policies {#us-22}

A policy not approved by senior management has no authority; a policy that is not audited loses adherence over time.  

**Context.** The chapter prescribes a set of relevant organisational policies (exception management, secure contracting, organisational traceability, supplier audit, governance KPIs — see intro §Relevant Organisational Policies) and the canonical checklist requires them to be *formally approved and audited*. US-12 formalises the policy for the **governance model**, but the rest of the body of policies is left without a user story that operationalises its cycle of approval by senior management and periodic audit. Without this cycle, the policies exist as a document but not as a living control: no one confirms that they remain approved, up to date and complied with.  

:::userstory
**Story.**   
As **GRC / Compliance** with the support of **CISO + Executive Management**, I want **to keep each organisational policy of the chapter in a formal cycle of approval by senior management and periodic adherence audit**, so that **the body of policies is guaranteed to have authority, be up to date and be effectively complied with and auditable**.  

**Acceptance criteria (BDD).**  
- **Given** a relevant organisational policy (exceptions, secure contracting, traceability, supplier audit, governance KPIs)  
  **When** it is created or revised  
  **Then** it is submitted for formal approval by senior management, with version, date and approver recorded before it comes into force  
- **Given** a policy in force  
  **When** the defined audit cycle arrives (at most annual)  
  **Then** practical adherence is audited, deviations are recorded and corrective action is generated with an owner and deadline  

**Checklist.**  
- [ ] Inventory of the chapter's relevant organisational policies maintained and versioned, with status (Mandatory/Recommended), owner and date of last approval  
- [ ] Each policy has formal senior-management approval recorded (version, date, approver) before it comes into force; review at least annually or after significant organisational change  
- [ ] Periodic adherence audit executed per defined cycle, with deviations recorded and corrective actions (owner + deadline) tracked through to closure  

:::

**Artefacts & evidence.** Versioned inventory of policies with status and owner; record of formal approval by senior management (version/date/approver); adherence audit report per cycle; corrective action plan for deviations.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Mandatory policies approved; informal annual audit | Full set approved; formal annual audit with deviations recorded | Full set approved; formal audit ≤ annual + review upon organisational change; corrective actions tracked through to closure |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Planning | Creation or revision of a policy | GRC / Compliance + CISO + Executive Management (approval) | Approval before coming into force |
| Audit | Periodic cycle (≤ annual) or organisational change | GRC / Compliance + AppSec Engineer | Audit completed within the cycle; corrective actions with a defined deadline |

**Useful links.**  
- [Periodic Review Checklist — Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/canon/checklist-revisao)
- [Formal governance model — US-12](#us-12---formalização-de-modelo-de-governação-por-nível-de-risco)
- [Canonical exception management process](./addon/processo-excecoes)
- [Security Exception Management Policy](/sbd-toe/assets/policies/policy-gestao-excecoes)
- [Secure Contracting Policy](/sbd-toe/assets/policies/policy-contratacao-segura)
- [Organisational Traceability Policy](/sbd-toe/assets/policies/policy-rastreabilidade-organizacional)
- [Security Governance KPIs Policy](/sbd-toe/assets/policies/policy-kpis-governacao)

---

## 📦 Expected artefacts {#-artefactos-esperados}

| Artefact | Evidence |
|-----------|-----------|
| Exception register with approval authorities | Versioned GRC tool, auditable decisions |
| Contracts with clauses | Legally validated documents |
| Supplier reports | Audits and findings, technical analysis |
| Organisational dashboard | Metrics per project and application |
| KPI reports | Quarterly/half-yearly consolidation |
| Supplier validation form | Completed questionnaire, AppSec analysis, GRC record |
| Exception table with revalidation schedule | Traceability with expiry dates |
| Compliance repository per app | Versioned YAML/MD file, Auditable history |
| Owner designation document | Centralised register with validated training |
| Periodic validation reports | Checklist + Action plan, cycle history |
| KPI and maturity dashboard | Metrics per chapter, Historical trends |
| SbD-ToE Governance Policy | Approved document, Approval authority levels, Decision template |
| Centralised compliance checklist | Versioned file per app (YAML/MD), Git history |
| Supplier reassessment schedule | Quarterly/half-yearly/annual planning, Automatic notifications |

---

## ⚖️ L1–L3 proportionality matrix {#️-matriz-de-proporcionalidade-l1l3}

| Practice | L1 | L2 | L3 |
|---------|----|----|----|
| Formal exceptions with approval authorities | Optional | Recommended | Mandatory |
| Contractual clauses | Recommended | Mandatory | Mandatory + audits |
| Supplier validation (initial) | Optional | Recommended | Mandatory |
| Organisational traceability | Basic | Recommended | Mandatory |
| Governance KPIs | Basic | Recommended | Mandatory |
| Formal supplier validation flow | Optional | Recommended | Mandatory |
| Continuous review of exceptions | Basic | Recommended | Mandatory |
| Compliance repository per app | Basic | Recommended | Mandatory |
| Formal designation of security owners | Recommended | Mandatory | Mandatory |
| Periodic compliance validation | Annual | Half-yearly | Quarterly |
| Maturity KPIs and executive reporting | Basic | Recommended | Mandatory |
| Formal governance model | Basic | Recommended | Mandatory |
| Centralised checklist per chapter | Basic | Recommended | Mandatory |
| Post-onboarding supplier reassessment | Annual | Half-yearly | Quarterly / critical event |
| **Technical preparation of contractors** | Basic | Recommended | Mandatory + validated quiz |
| **Pre-access training track** | Basic | Mandatory | Mandatory + 80% score |
| **Secure offboarding** | Basic | Mandatory | Mandatory + audit trail |
| **Continuous supplier monitoring** | No | Recommended | Mandatory |
| **Quarterly access review (contractors)** | Half-yearly | Quarterly | Quarterly |
| **Post-project feedback** | Optional | Recommended | Mandatory |

---

## 🏁 Final recommendations {#-recomendações-finais}

- **Unrecorded exceptions = invisible risk.** US-01 (with clear approval authorities) and US-07 should be operationalised to guarantee continuous traceability and automatic revalidation.  
- **The formal model is the foundation.** US-12 documents governance with explicit criteria, approval authorities per L1–L3, and mandatory training for approvers (Ch. 13).  
- **Suppliers must be part of the SbD-ToE model.** US-02, US-06, US-14 and US-18 serve contractual integration, initial validation, periodic reassessment, and continuous monitoring.  
- **Contractors deserve a dedicated lifecycle.** US-15 (technical preparation), US-16 (mandatory training), US-17 (offboarding) and US-19 (access review) ensure that contractors are prepared, maintain least privilege, and leave securely.  
- **Clear designation of owners eliminates dispersed responsibility.** US-09 guarantees continuity of security decisions with validated training.  
- **A centralised compliance repository gives full visibility.** US-08 and US-13 consolidate the status of all practices per application, chapter and cycle.  
- **Periodic validations detect deviations early.** US-10 integrates continuous review into the lifecycle; US-13 validates per chapter; US-14 reassesses suppliers; US-19 validates contractor access.  
- **Governance KPIs are the objective measure of maturity.** US-05 and US-11 enable evidence-based strategic decisions (% compliance, % exceptions resolved, % suppliers audited).  
- **Organisational traceability gives transparency to management.** US-04 aggregated with US-08, US-10, US-13, US-14 and US-20 creates visibility of risk at all levels.  
- **Continuous preparation and feedback improve contractor quality.** US-15, US-16 and US-20 create a continuous improvement cycle and an assessment database for re-hire.  
- **This chapter is the "cement" that binds the remaining chapters 2–13:** it makes practices visible, auditable, traceable and sustainable over time. Without formal governance (US-12), systematic control (US-13), a contractor lifecycle (US-15–17, 19–20), and continuous reassessment (US-01, US-07, US-14, US-18), SbD-ToE is limited to one-off technical practice.
