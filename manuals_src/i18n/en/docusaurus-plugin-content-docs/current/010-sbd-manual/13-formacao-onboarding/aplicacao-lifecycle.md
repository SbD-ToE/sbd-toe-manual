---
id: aplicacao-lifecycle
title: How to Do It
description: Practical integration of upskilling and onboarding practices into the development lifecycle
tags: [tipo:aplicacao, ciclo-vida, formacao, capacitacao, onboarding, seguranca]
genia: us-format-normalization
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/aplicacao-lifecycle.md
  source_sha256: 16f4c0326acc73e438d193bf66c16f248b7d7639bcd6d893f3e10f66e0acf809
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: a654d24e54f013dd354548f6bdd8c8d583af06dd96a2f8cf053d9abbc1d95531
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [audit_trail, avaliacao, capacitacao, chapter_role, como_fazer, cycle_iteration, lifecycle_phase, mapping, papel_suporte, practitioner_manual, programme_line, risk_level, slug_threat_modeling, threat, traceability, transversal, trilho_formativo, v1_entity_tmr_peer_review, validation_evaluation, verification_taxonomy]
  glossary_sha256: 7ee8c94398c5d4969cb0a6b905467ad31eab8a74a84cabf0332528f36f053d59
  translated_at: 2026-09-26T12:49:02Z
  reviewed_by: null
---

# Applying Training and Upskilling Throughout the Lifecycle

## 🧭 When to apply {#-quando-aplicar}

| Phase | Action | Evidence |
|------|------|-----------|
| Onboarding | Initial training in SbD and secure practices | LMS certification |
| Continuous development | Courses, labs and quarterly reviews | Training reports |
| Release/Operations | Practical exercises and simulations | Exercise logs |
| Audit | Verification of upskilling KPIs | GRC reports |

---

## 👥 Who carries out each action {#-quem-executa-cada-ação}

| Role | Responsibility |
|-------|------------------|
| **Developer** | Take part in practical training, apply it in code |
| **Quality Assurance (QA)** | Training in validation and regressions |
| **AppSec Engineer** | Produce content, deliver training, facilitate sessions |
| **DevOps / SRE** | Upskilling in CI/CD and monitoring |
| **Security Champion** | Mentor teams, facilitate peer learning |
| **Executive Management** | Support adoption, validate regulatory compliance |
| **GRC / Compliance** | Manage traceability, audits, KPIs |
| **Security Champion (HR)** | Operate the LMS, manage onboarding, integrate into the individual development plan |
| **Software Architects** | Contribute to threat modelling and secure patterns |
| **Operations (Ops)** | Take part in simulations, communication during incidents |
| **Suppliers / Third Parties** | Receive mandatory minimum training |

---

## 📖 Normalised User Stories {#-user-stories-normalizadas}

### US-01 - Mandatory secure onboarding {#us-01---onboarding-seguro-obrigatório}
**Context.** New members without training introduce basic risks.  

:::userstory
**Story.**   
As a **Security Champion (HR)**, I want **to ensure mandatory onboarding training in SbD**, so that **everyone starts out aligned with the practices**.  

**Acceptance criteria (BDD).**  
- **Given** a new staff member  
  **When** they take up their duties  
  **Then** they only have full access after completing training  

**Checklist.**  
- [ ] Course completed in the LMS  
- [ ] Certification issued  
- [ ] Record archived  
- [ ] Technical access blocked until completion  
- [ ] Automatic block in Git/Azure DevOps/CI/CD pipelines  
- [ ] Exceptions documented with AppSec/Management approval  
- [ ] Biennial re-authentication or on a new-risk trigger  

:::

**Artefacts & evidence.** LMS certificates, block records in Git/Azure DevOps, exceptions document.

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic | Mandatory | Mandatory + practical assessment |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Onboarding | Arrival of a new staff member | Security Champion (HR) + AppSec Engineer | Before technical access |

**Useful links.**  
[Technical Onboarding Checklist](./addon/checklist-onboarding)  
[Roles and Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)  

---

### US-02 - Continuous training by profile {#us-02---formação-contínua-por-perfil}
**Context.** Without continuous updating, practices become obsolete.  

:::userstory
**Story.**   
As an **AppSec Engineer**, I want **to provide continuous training by profile (Dev, QA, DevOps, Management)**, so that **staying up to date with the latest practices is ensured**.  

**Acceptance criteria (BDD).**  
- **Given** a quarterly (L3), half-yearly (L2) or annual (L1) cycle  
  **When** the LMS makes courses available  
  **Then** each profile completes its specific track  

**Checklist.**  
- [ ] Courses defined by profile  
- [ ] Record in the LMS  
- [ ] Cycle defined: quarterly for L3, half-yearly for L2, annual for L1 (TRN-005)  
- [ ] Additional triggers: new technical chapter, new risk, incident  
- [ ] Communication to teams (announcement, deadline, completion criterion)  
- [ ] Integration into individual OKRs or performance assessments  
- [ ] Quarterly effectiveness review  

:::

**Artefacts & evidence.** LMS reports, communications to teams, completion records, OKRs that include training.

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Recommended annually | Mandatory half-yearly | Mandatory quarterly |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Continuous cycle | Quarterly (L3) / Half-yearly (L2) / Annual (L1) | AppSec Engineer + Security Champion (HR) | Deadline communicated 2 weeks in advance |

**Useful links.**  
[Training Catalogue by Technical Profile](./addon/catalogo-formativo)  
[Training Tracks by Role and Risk](./addon/trilho-formativo)  
[Roles and Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)  

---

### US-03 - Security Champions Programme {#us-03---programa-de-security-champions}
**Context.** Without champions, teams lack internal leadership.  

:::userstory
**Story.**   
As a **Champion**, I want **to mentor and evangelise the team**, so that **the continuous application of SbD practices is ensured**.  

**Acceptance criteria (BDD).**  
- **Given** a sprint in progress  
  **When** questions arise  
  **Then** the champion supports and guides the team  

**Checklist.**  
- [ ] Champion appointed per team  
- [ ] Monthly meetings recorded  
- [ ] Feedback collected  
- [ ] Formal Champions community (monthly meeting, Teams/Slack channel)  
- [ ] Collective documentation of practices and anti-patterns (wiki)  
- [ ] Badges or institutional recognition (email, board, salary)  
- [ ] Budget for security events or conferences (optional depending on maturity)  

:::

**Artefacts & evidence.** Meeting records, practices wiki, community channel, list of recognitions.

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Optional | Recommended | Mandatory |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Continuous cycle | Monthly | Security Champion + AppSec Engineer | Monthly meeting confirmed |

**Useful links.**  
[Security Champions Programme](./addon/programa-champions)  
[Roles and Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)  

---

### US-04 - Practical exercises and simulations {#us-04---exercícios-práticos-e-simulações}
**Context.** Theoretical training without practice has low retention.  

:::userstory
**Story.**   
As a **QA** role, I want **to carry out practical exercises (labs, CTFs, simulations)**, so that **it is ensured that the knowledge is applicable**.  

**Acceptance criteria (BDD).**  
- **Given** a training plan  
  **When** I run an exercise  
  **Then** I record the result and performance metrics  

**Acceptance criteria (DoD).**  
- [ ] Labs run  
- [ ] Results recorded  
- [ ] Metrics analysed  

:::

**Artefacts & evidence.** Exercise logs  

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Optional | Recommended | Mandatory |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Training cycle | Execution of an exercise provided for in the training plan | QA + AppSec Engineer | Result and performance metrics recorded upon execution |

---

### US-05 - Measuring training effectiveness {#us-05---medição-de-eficácia-da-formação}
**Context.** Without measuring effectiveness, there is no continuous improvement.  

:::userstory
**Story.**   
As **GRC / Compliance**, I want **to measure upskilling KPIs (completion rate, effectiveness in audit)**, so that **the real impact of training is assessed**.  

**Acceptance criteria (BDD).**  
- **Given** a training cycle  
  **When** I collect metrics  
  **Then** KPIs are reported to management  

**Acceptance criteria (DoD).**  
- [ ] KPIs defined  
- [ ] Metrics collected  
- [ ] Quarterly reports  

:::

**Artefacts & evidence.** GRC reports  

**Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic | Annual KPIs | Quarterly KPIs with targets |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Audit | Collection of metrics in the training cycle | GRC / Compliance | Annual KPIs (L2); quarterly KPIs with targets (L3) |

---

### US-06 - Structured and Recurring Code Clinics {#us-06---code-clinics-estruturadas-e-recorrentes}
**Context.** Code clinics are regular sessions of public review of real code, educating on secure patterns. Without structure, they become ad hoc and lose impact.

:::userstory
**Story.**  
As an **AppSec Engineer**, I want **to run structured code clinics** (reviews of real PRs, educational, with a security checklist applied), so that **continuous learning and the visible application of secure patterns are ensured**.

**Acceptance criteria (BDD).**  
- **Given** that one or more PRs are selected  
  **When** the session is conducted (in person or asynchronously)  
  **Then** the security checklist is applied publicly  
- And feedback is recorded and shared in an internal channel  
- And lessons learned are documented for reuse  

**Checklist.**  
- [ ] Cadence defined (weekly or fortnightly)  
- [ ] Checklist templates by domain (Dev, DevOps, IaC)  
- [ ] Exemplary PRs archived (good practices + failures)  
- [ ] Sessions recorded (video, summary, asynchronous discussion)  
- [ ] Rotating participation (Developers, Security Champions, QA)  

:::

**Artefacts & evidence.**  
- Repository of exemplary PRs (with comments)  
- Session summaries and feedback  
- Participation statistics  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Occasional (monthly) | Recurring (fortnightly) | Recurring + rotating (weekly) |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Development | Submission of PRs | AppSec Engineer + Security Champion | Weekly/fortnightly |

**Useful links.**  
[Advanced Training Techniques](./addon/tecnicas-formativas)  
[Example - Secure Pull Request](./addon/exemplo-manual-dev-pr)  
[Roles and Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-07 - Threat Modeling Peer-led and Rotating {#us-07---threat-modeling-peer-led-e-rotativo}
**Context.** Threat modelling is a critical practice but concentrated in AppSec. Operationalising it as a peer-led, rotating activity increases the distribution of knowledge.

:::userstory
**Story.**  
As a **Developer / Security Champion**, I want **to lead threat modelling sessions** (per feature, epic or refactor), so that **risk analysis knowledge is disseminated and SbD is applied in design**.

**Acceptance criteria (BDD).**  
- **Given** that a new feature or refactor is planned  
  **When** the threat modelling session is scheduled  
  **Then** it is facilitated by a Developer or Champion with the support of an AppSec Engineer  
- And the output is documented (diagram, risk matrix)  
- And security decisions are traced to the Manual's requirements  

**Checklist.**  
- [ ] Session scheduled before design is finalised  
- [ ] Threat modelling template (e.g. STRIDE) applied  
- [ ] Architecture/flow diagram documented  
- [ ] Risk matrix (threat × impact × control)  
- [ ] Decisions and exceptions justified  
- [ ] Rotation of leadership among Security Champions  

:::

**Artefacts & evidence.**  
- Diagrams (draw.io, Lucidchart)  
- Session minutes  
- Risk matrix with traceability to the requirements of Ch. 02  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Optional / ad hoc | Recommended per epic | Mandatory before design is finalised |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Planning/Design | Feature approval | Security Champion + AppSec Engineer | Before the development sprint |

**Useful links.**  
[Advanced Training Techniques](./addon/tecnicas-formativas)  
[Cross-cutting Integration with the Technical Chapters](./addon/integracao-transversal)  
[Threat Modelling - Chapter 03](/sbd-toe/sbd-manual/threat-modeling/intro)  
[Roles and Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-08 - War Room and Incident Simulations {#us-08---war-room-e-simulações-de-incidentes}
**Context.** Incident simulations train teams to respond under pressure, validate processes and build a culture of readiness.

:::userstory
**Story.**  
As **Executive Management / GRC**, I want **to run incident simulations (war room)** regularly, so that **teams are trained in response and communication and remediation processes are validated**.

**Acceptance criteria (BDD).**  
- **Given** that an incident scenario is simulated  
  **When** the response is executed in real time  
  **Then** all roles (Developer, DevOps, AppSec Engineer, Operations, Management) take part  
- And the process is documented and analysed in an educational debrief  
- And lessons learned are incorporated into runbooks  

**Checklist.**  
- [ ] Scenarios based on real or historical risks  
- [ ] Communication (alerts, escalation, internal/external comms) validated  
- [ ] Detection, response and resolution times measured (MTTD/MTTR)  
- [ ] Role of each participant documented (playbooks)  
- [ ] Debrief held with recommendations  
- [ ] Cadence defined (annual minimum, quarterly ideal)  

:::

**Artefacts & evidence.**  
- Simulation scenarios and scripts  
- Execution logs (timelines, communications)  
- Debrief report with observed MTTD/MTTR  
- Updated playbooks and runbooks  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Recommended annually | Quarterly | Quarterly + rotating by threat |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Operations/Audit | Quarterly or post-incident | Executive Management + GRC | Planned annually |

**Useful links.**  
[Advanced Training Techniques](./addon/tecnicas-formativas)  
[Monitoring and Operations - Chapter 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)  
[Roles and Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-09 - Maintenance and Updating of Training Tracks {#us-09---manutenção-e-atualização-de-trilhos-formativos}
**Context.** Training tracks need periodic review based on new risks, technologies and lessons learned.

:::userstory
**Story.**  
As an **AppSec Engineer / GRC**, I want **to maintain and update training tracks by profile and risk** (annually or on a trigger), so that **it is ensured that training reflects current practices and lessons learned**.

**Acceptance criteria (BDD).**  
- **Given** that a year has passed or a new risk is identified  
  **When** the review of tracks is scheduled  
  **Then** content is reassessed against incidents, technology updates and feedback from Security Champions  
- And tracks are updated or new content is added  
- And changes are communicated to HR and to the teams  

**Checklist.**  
- [ ] Annual review scheduled (e.g. Q1 of each year)  
- [ ] Feedback from Security Champions collected (survey or meeting)  
- [ ] Lessons learned from incidents integrated  
- [ ] New technical chapters or practices mapped  
- [ ] Tracks updated (document and matrix)  
- [ ] Communication to stakeholders (HR, teams, Executive Management)  

:::

**Artefacts & evidence.**  
- Document with version and changelog  
- Feedback survey of Security Champions  
- Mapping of new content to chapters  
- Release note with changes  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Occasional | Annual | Annual + continuous on trigger |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Governance/Audit | Annual (Q1) or new risk | AppSec Engineer + GRC / Compliance + Security Champion (HR) | Before the new training cycle |

**Useful links.**  
[Training Catalogue by Technical Profile](./addon/catalogo-formativo)  
[Training Tracks by Role and Risk](./addon/trilho-formativo)  
[Roles and Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-10 - Training Tracks Proportional to Risk (L1–L3) {#us-10---trilhos-formativos-proporcionais-por-risco-l1l3}

**Context.**  
Training tracks need to be explicitly proportional to the application's risk. Although US-02 mentions "by profile", there is a lack of clarity about the L1–L3 application and its integration with the risk classification matrix of Ch. 01.

:::userstory
**Story.**  
As an **AppSec Engineer / GRC**, I want **to apply training tracks in a way that is explicitly proportional to the risk level** (L1, L2, L3) of the application and to the technical profile, so that **each staff member receives training suited to their context and responsibility**.

**Acceptance criteria (BDD).**  
- **Given** an application classified as L1, L2 or L3  
  **When** a new staff member is onboarded or a track is updated  
  **Then** the training track applied corresponds to the proportionality matrix  
- And content reflects the mandatory practices according to the risk level  
- And traceability between classification → track is documented  

**Checklist.**  
- [ ] Application risk classification documented (Ch. 01)  
- [ ] Track matrix (addon/02) referenced in the training plan  
- [ ] L1 track: basic content (secure coding, dependencies, policies)  
- [ ] L2 track: intermediate content (threat modelling, SCA, secure PR, CI/CD scanners)  
- [ ] L3 track: advanced content (secure architecture, labs on vulnerable apps, fuzzing, IRP integration)  
- [ ] Explicit assignment of the track per staff member in the LMS or a document  
- [ ] Traceability: link between application classification → track → HR/LMS  
- [ ] Periodic review (annual or on a reclassification trigger)  
- 
- [ ] Catalogue → Track: there is a catalogue→track mapping artefact (`catalogo_trilhos.csv` or `catalogo_trilhos.json`) that lists, for each chapter/topic of `addon/01`, the recommended module/track and the applicable L1/L2/L3 version.  
- 
**Additional artefacts & evidence.** `catalogo_trilhos.csv` with minimum columns: capitulo, topico, trilho_L1, trilho_L2, trilho_L3, formato_sugerido, exemplo_import_lms. An import example (small CSV) must accompany the training plan.  

- 
:::

**Artefacts & evidence.**  
Risk classification document (Ch. 01), track matrix (addon/02) with the selection of the track applied, assignment in the LMS or training plan document, documented traceability.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic track (essential content) | Intermediate track (mandatory content + labs) | Advanced track (complete content + simulations + continuous audit) |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Onboarding / Governance | Application classification | AppSec Engineer + Security Champion (HR) | Before the first technical assignment |

**Useful links.**  
[Training Tracks by Role and Risk](./addon/trilho-formativo)  
[Risk Management and Classification - Chapter 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)  
[Roles and Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-11 - Formal Onboarding Validation via Checklist {#us-11---validação-formal-de-onboarding-via-checklist}
**Context.** Onboarding without formal validation leaves gaps. A structured checklist ensures that all the minimum steps are completed before any technical access.

:::userstory
**Story.**  
As **HR / GRC**, I want **to formally validate the onboarding of each staff member** (via a structured checklist), so that **it is ensured that everyone meets the minimum requirements before technical access and auditable traceability is created**.

**Acceptance criteria (BDD).**  
- **Given** that a new staff member starts  
  **When** the onboarding process is carried out  
  **Then** all checklist items are validated by a designated owner  
- And the formal record is archived  
- And technical access is blocked until completion  

**Checklist.**  
- [ ] Correct training track assigned by role and risk  
- [ ] Track completion validated (LMS or practical evidence)  
- [ ] Knowledge validation completed (quiz, exercise or PR)  
- [ ] Access to good-practice repositories and templates confirmed  
- [ ] Technical access (Git, pipelines, environments) conditional on completion  
- [ ] Formal record archived with date and owner  
- [ ] Support contact (Champion, SPOC) identified  
- [ ] Applicable to internal and external staff (suppliers with technical access)  

:::

**Artefacts & evidence.**  
- Checklist completed and signed (digital or paper)  
- Record in the LMS, permissions system or GitHub/ADO  
- Evidence of completion (certificate, PDF, closed issue)  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic (role) | Structured (role + risk) | Structured + periodic audit |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Onboarding | Arrival of a new staff member | Security Champion (HR) + GRC / Compliance | Before technical access |

**Useful links.**  
[Technical Onboarding Checklist](./addon/checklist-onboarding)  
[Training Tracks by Role and Risk](./addon/trilho-formativo)  
[Roles and Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-12 - Knowledge Validation via Structured Quizzes {#us-12---validação-de-conhecimento-via-quizzes-estruturados}
**Context.** Training without validation of knowledge retention is ineffective. Structured quizzes ensure real understanding and act as objective traceability.

:::userstory
**Story.**  
As an **AppSec Engineer / HR**, I want **to implement and run validation quizzes** (post-onboarding, continuous, by role) so that **knowledge retention is ensured and an auditable record of competence is created**.

**Acceptance criteria (BDD).**  
- **Given** that a staff member completes training  
  **When** the quiz is administered  
  **Then** a result ≥ 80% is obtained  
- And the record (score, date, validator) is archived  
- And technical access is only unblocked with a pass result  

**Checklist.**  
- [ ] Quizzes defined by training track (onboarding, continuous, role)  
- [ ] Questions adapted to the real content of the Manual and the application  
- [ ] Accessible format (LMS, form, online tool, paper)  
- [ ] Minimum pass mark defined (e.g. 80%)  
- [ ] Immediate feedback with explanations of answers  
- [ ] Record with timestamp, name, result and validator  
- [ ] Periodic refresher (e.g. annual or on a new-risk trigger)  
- [ ] Applicable to internal staff, suppliers and third parties with access  

:::

**Artefacts & evidence.**  
- Quiz templates by track and role  
- Submission records with results  
- Trend analysis (pass rate, most-failed topics)  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| One-off (onboarding) | Periodic (annual) | Periodic + adaptive (on trigger) |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Onboarding / Continuous | Track completion or annually | AppSec Engineer + Security Champion (HR) | Before/during access |

**Useful links.**  
[Quiz Template for Onboarding](./addon/quiz-onboarding)  
[Validation Quiz for Third Parties](./addon/quiz-terceiros)  
[Training Catalogue by Technical Profile](./addon/catalogo-formativo)  
[Roles and Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-13 - Operationalising Third-Party Training {#us-13---operacionalização-de-formação-de-terceiros}
**Context.** Suppliers and third parties with technical access need mandatory minimum training to reduce the risk of security failures.

:::userstory
**Story.**  
As **GRC / Executive Management**, I want **to ensure that suppliers and third parties with access receive mandatory minimum training**, so that **the risk of security failures through lack of knowledge is reduced and regulatory obligations (NIS2, DORA) are met**.

**Acceptance criteria (BDD).**  
- **Given** that a supplier with technical access is onboarded  
  **When** access is established  
  **Then** they complete a mandatory training track (e.g. the organisation's policy, support channels, minimum requirements)  
- And the certification is recorded contractually  
- And access is blocked until completion  

**Checklist.**  
- [ ] Categorisation of third parties (access level, data sensitivity)  
- [ ] Minimum track defined per category  
- [ ] Quiz or practical validation with a result ≥ 80%  
- [ ] Certificate issued and archived  
- [ ] Compliance record in GRC  
- [ ] Access conditional on completion  
- [ ] Quarterly or annual refresher  

:::

**Artefacts & evidence.**  
- Tracks by third-party category (as per addon/21)  
- Validation quizzes and templates (as per addon/22)  
- Certificates and completion records  
- Contractual compliance record  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Recommended | Mandatory | Mandatory + annual |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Onboarding | Supplier contract | GRC / Compliance + Security Champion (HR) + AppSec Engineer | Before access |

**Useful links.**  
[Model for the Inclusion of Third Parties](./addon/inclusao-terceiros)  
[Training Plan for Third Parties](./addon/plano-formacao-terceiros)  
[Validation Quiz for Third Parties](./addon/quiz-terceiros)  
[Governance and Contracting - Chapter 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)  
[Roles and Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

### US-14 - Upskilling KPIs and Reporting (GRC) {#us-14---kpis-de-capacitação-e-reporte-grc}
**Context.** Scattered KPIs reduce the ability to assess the impact of training. It is necessary to formalise the list, owners and cadence.

:::userstory
**Story.**
As **GRC / Executive Management**, I want **to define and collect upskilling KPIs** (completion rate, pass rate, effectiveness in audit, MTTR in exercises), so that **impact is assessed and compliance is reported**.

**Acceptance criteria (BDD).**
- **Given** a defined training cycle
  **When** the metrics are collected
  **Then** the KPIs are reported to the dashboard and sent quarterly to Executive Management

**Checklist.**
- [ ] List of KPIs defined (e.g. completion rate, pass rate ≥80%, % of failed topics, average time to complete labs)
- [ ] Owner defined (GRC owner)
- [ ] Collection and reporting cadence defined (monthly/quarterly)
- [ ] Automated dashboard or report configured (e.g. PowerBI/Looker/Grafana)
- [ ] Evidence archived for audit (CSV/PDF report)

:::

**Artefacts & evidence.** `KPIs_formacao.md` document with definition, owner, cadence; sample CSV export; link to the dashboard.

**Proportionality L1–L3.**
| L1 | L2 | L3 |
|----|----|----|
| Annual KPIs | Quarterly KPIs with targets | Quarterly KPIs + targets per track and practical audit |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Audit/Training | Monthly/Quarterly | GRC / Compliance + AppSec Engineer | Quarterly report |

---

### US-15 - Delivery Formats and DoD per Format {#us-15---formatos-de-entrega-e-dod-por-formato}
**Context.** The lack of a minimum specification per format (labs, code clinics, microlearning, simulations) hinders replicability and quality levels.

:::userstory
**Story.**
As an **AppSec Engineer / HR**, I want **to define the delivery formats and the minimum DoD per format** (labs, code clinics, microlearning, quizzes, simulations), so that **consistency and quality in training are ensured**.

**Acceptance criteria (BDD).**
- **Given** a chosen format (e.g. lab)
  **When** the session is planned
  **Then** there is a minimum DoD (infra + scenario + scoring + record) and associated artefacts

**Checklist / DoD per format.**
- Labs: provisioned infra + vulnerable app (or VM) + exercise guide + automatic/manual scoring + logs and report
- Code clinics: selected PRs + checklist applied + recording/summary + lessons-learned package
- Microlearning: micro-modules ≤15min + quiz of 3–5 questions + reference material
- Simulations: scripted scenario + updated playbook + debrief with MTTD/MTTR and improvements
- Quizzes: template per track + threshold (e.g. ≥80%) + timestamped record

:::

**Artefacts & evidence.** Examples: `lab_template.md`, `code_clinic_template.md`, `microlearning_manifest.csv`, `simulation_script.yaml`.

**Proportionality L1–L3.**
| L1 | L2 | L3 |
|----|----|----|
| Basic formats (microlearning) | Structured labs and quizzes | Labs with scoring + simulations + audit |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Planning | Planning of a session in a chosen format | AppSec Engineer / HR | Minimum DoD and associated artefacts defined at planning |

---

### US-16 - Remediation Path Below the Threshold {#us-16---caminho-de-remediação-abaixo-do-limiar}

A result below the minimum threshold cannot leave onboarding in an undefined state.  

**Context.** `TRN-003` requires results below the acceptance threshold to have a defined remediation path. Without that path, a staff member who fails the validation is left in limbo: access is neither blocked in a traceable way, nor is there a clear route to recover the competence. Operationalising remediation closes the cycle between objective validation and the unblocking of access.  

:::userstory
**Story.**   
As an **AppSec Engineer / HR**, I want **to define and execute a remediation path for those who fall below the validation threshold**, so that **it is ensured that failing has an operational consequence and a traceable recovery route, with no technical access until a pass**.  

**Acceptance criteria (BDD).**  
- **Given** a staff member who obtains a result below the minimum threshold in the onboarding validation  
  **When** the result is recorded  
  **Then** a remediation plan (targeted retraining + new validation) is triggered automatically and technical access remains blocked until a pass  

**Checklist.**  
- [ ] Minimum pass threshold documented and versioned alongside the content  
- [ ] Remediation plan defined per track (retraining targeted at the failed topics)  
- [ ] Maximum number of attempts and escalation to AppSec/management once exhausted  
- [ ] Technical access blocked until a new validation is passed (enforcement of `TRN-004`)  
- [ ] Record of the failure, the remediation and the reassessment traceable to the staff member and to the content version  

:::

**Artefacts & evidence.** Record of results (score, date, validator, content version); remediation plan per failed topic; record of access blocking until re-approval; trail of attempts and escalations.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Informal retraining + new attempt | Documented remediation plan + access block | Formal plan + attempt limit + escalation to AppSec and audit |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Onboarding | Result below the threshold | AppSec Engineer + Security Champion (HR) | Remediation started before any granting of access |

**Useful links.** [Training Requirements Catalogue (TRN-003)](./addon/catalogo-requisitos-formacao)  
[Technical Onboarding Checklist](./addon/checklist-onboarding)  
[Roles and Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-17 - Third-Party Responsibility Statement {#us-17---termo-de-responsabilidade-de-terceiros}

The onboarding of a third party is only complete when responsibility has been formally accepted and recorded.  

**Context.** `TRN-007` requires the onboarding of third parties and contractors to include a responsibility statement and a formal record (name, entity, date, validator). Training on its own is not binding: without explicit acceptance of the security obligations and without an auditable record, there is no evidence that the third party has taken on the commitment proportional to its access profile. This statement is the piece that makes the onboarding of third parties equivalent — and not merely similar — to that of internal staff.  

:::userstory
**Story.**   
As **GRC / Executive Management**, I want **to record a responsibility statement signed by each third party with technical access**, so that **the third party is formally bound to the security obligations and auditable evidence is created that conditions access (NIS2, DORA)**.  

**Acceptance criteria (BDD).**  
- **Given** a third party or contractor with access to code, pipelines or sensitive data  
  **When** they complete the security onboarding  
  **Then** they sign a responsibility statement and the record (name, entity, date, validator, access profile) is archived before access is granted  

**Checklist.**  
- [ ] Responsibility statement defined per access profile (proportional)  
- [ ] Minimum fields of the record: name, entity, date, validator, access scope  
- [ ] Signature (digital or contractual) collected before access is granted  
- [ ] Record archived in a traceable institutional repository  
- [ ] Link to the contract/GRC compliance (NIS2, DORA)  
- [ ] Access blocked in the absence of a valid statement  

:::

**Artefacts & evidence.** Responsibility statement signed by the third party; formal record with minimum fields (name, entity, date, validator); contractual link in GRC; evidence of access blocking without a statement.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Simple statement + record | Statement per profile + traceable archive | Statement per profile + contractual binding + periodic audit |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Onboarding | Contract with a third party with technical access | GRC / Compliance + Security Champion (HR) + AppSec Engineer | Statement recorded before access |

**Useful links.** [Training Requirements Catalogue (TRN-007)](./addon/catalogo-requisitos-formacao)  
[Model for the Inclusion of Third Parties](./addon/inclusao-terceiros)  
[Training Plan for Third Parties](./addon/plano-formacao-terceiros)  
[Roles and Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-18 - Corrective Action on KPI Deviations {#us-18---ação-corretiva-sobre-desvios-de-kpis}

KPIs without corrective action are decorative metrics.  

**Context.** `TRN-009` requires deviations of training KPIs from defined thresholds to generate corrective action with an owner and a deadline. US-14 defines and collects the KPIs, but collection does not close the cycle: what is missing is the mechanism that turns a deviation (e.g. onboarding coverage below target, a falling pass rate) into an actionable and traceable decision. This US operationalises the triggering, not the definition of the indicators.  

:::userstory
**Story.**   
As **GRC / Executive Management**, I want **to trigger a corrective action whenever a training KPI deviates from the threshold**, so that **it is ensured that the indicators produce decisions with an owner and a deadline, and not just reports**.  

**Acceptance criteria (BDD).**  
- **Given** a training KPI with a defined threshold  
  **When** periodic collection reveals a deviation from the threshold  
  **Then** a corrective action is opened with an owner and a deadline, recorded and followed up until closure  

**Checklist.**  
- [ ] Explicit threshold per KPI (onboarding coverage, pass rate, average time, content updating)  
- [ ] Triggering rule documented (deviation → corrective action)  
- [ ] Corrective action with a named owner and a defined deadline  
- [ ] Follow-up until closure recorded (status, evidence of resolution)  
- [ ] Deviations and actions reported to Executive Management in the reporting cycle  

:::

**Artefacts & evidence.** Record of deviations from thresholds; corrective actions with owner and deadline; follow-up trail until closure; deviations section in the quarterly report to Executive Management.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Informal review of deviations | Corrective action with owner and deadline recorded | Corrective action + follow-up until closure + reporting and audit |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Audit/Training | KPI deviation from the threshold | GRC / Compliance + AppSec Engineer | Action opened in the collection cycle; closure within the defined deadline |

**Useful links.** [Training Requirements Catalogue (TRN-009)](./addon/catalogo-requisitos-formacao)  
[Training KPIs and Metrics](./addon/kpis-metricas-formacao)  
[Roles and Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-19 - Training in the Secure Use of AI and Tooling {#us-19---formação-em-uso-seguro-de-ia-e-tooling}

Tools assist; humans decide. Training has to teach where the boundary lies.  

**Context.** With the pervasive adoption of code assistants, code/test generators, SAST/DAST/SCA and SOAR, it is critical that training covers **when to trust vs. when to validate** the outputs. Addon/12 defines the content by technical chapter — anti-patterns (accepting generated code without reading it, tests that merely "prove" the implementation, blind trust in alerts), the limits of automation (guardrails) and the principle that non-deterministic automation always requires validation. What is missing is a US that makes this training mandatory and verifiable.  

:::userstory
**Story.**   
As an **AppSec Engineer / HR**, I want **to make training in the secure use of AI and tooling mandatory and verifiable**, so that **vulnerabilities from unreviewed generated code, tautological tests and automated decisions without governance in non-deterministic contexts are prevented**.  

**Acceptance criteria (BDD).**  
- **Given** a staff member with access to code assistants, generators or pipeline/SOAR automation  
  **When** they complete the training track for their profile  
  **Then** it includes the module on the secure use of AI/tooling (when to trust vs. validate, guardrails, validation of generated code and tests) with a passed objective validation  

**Checklist.**  
- [ ] Module on the secure use of AI/tooling included in the track per profile (Developer, QA, DevOps, AppSec, IR/Ops, Management)  
- [ ] Content covers anti-patterns, guardrails and validation of outputs (code and tests) from addon/12  
- [ ] Practical labs: identify vulnerabilities in generated code and tautological tests  
- [ ] Objective validation (quiz ≥ threshold) specific to the module  
- [ ] Secure prompt engineering (explicit security requirements) covered  
- [ ] Content review annually or on a new-risk trigger  

:::

**Artefacts & evidence.** AI/tooling modules per profile; completion and validation records in the LMS; lab outputs (vulnerabilities and tautological tests identified); version of the training content.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Microlearning on principles (assisting vs. deciding) | Module per profile + labs + quiz (≥ half-yearly) | Module per profile + advanced labs + adaptive validation (≥ quarterly) |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Onboarding / Continuous cycle | Access to AI/automation tooling or new risk | AppSec Engineer + Security Champion (HR) | Before autonomous use of AI tooling |

**Useful links.** [Training in the Secure Use of AI and Tooling](./addon/formacao-uso-seguro-ia-tooling)  
[Training Catalogue by Technical Profile](./addon/catalogo-formativo)  
[Roles and Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-20 - Isolated Sandbox for Contractor Practice {#us-20---sandbox-isolado-para-prática-de-contractors}

Contractors practise in an isolated environment before touching real systems.  

**Context.** The sandbox preparation guide (addon/13) defines an isolated, controlled and ephemeral environment in which contractors practise security tools and procedures before production access — with read-only initial permissions, network isolation from production, logging of all activity, validation through exercises (≥70%) and a quiz (≥80%), and destruction after onboarding. What is missing is a US that makes this sandbox a verifiable step of the contractor track, with a sign-off that conditions real access.  

:::userstory
**Story.**   
As a **DevOps / AppSec Engineer**, I want **to provision and operate an isolated sandbox for contractor practice before access to real systems**, so that **the risk of error in production is reduced and understanding of policies is validated empirically before access is granted**.  

**Acceptance criteria (BDD).**  
- **Given** a contractor in technical onboarding  
  **When** the sandbox is provisioned  
  **Then** the contractor practises in an environment isolated from production (initially read-only, logging active) and real access is only granted after exercises (≥70%), a quiz (≥80%) and sign-off  

**Checklist.**  
- [ ] Sandbox provisioned per profile (Developer, DevOps, QA) with a demonstration app  
- [ ] Network isolation from production and resource limits applied  
- [ ] Read-only initial permissions, evolving only after validation  
- [ ] Logging of all activity (logins, commits, access to secrets) enabled  
- [ ] Practical exercises (≥70%) and comprehension quiz (≥80%) completed  
- [ ] Completion sign-off (Scrum Master / Team Lead + AppSec) conditions real access  
- [ ] Sandbox destroyed and credentials revoked after onboarding; logs archived  

:::

**Artefacts & evidence.** Sandbox infrastructure definition (repos, namespace, IaC); activity logging records; exercise and quiz results; signed completion sign-off; evidence of destruction and revocation after onboarding.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Optional simple sandbox | Isolated sandbox per profile + exercises + quiz | Isolated sandbox + audited logging + formal sign-off + traceable destruction |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Onboarding | Technical onboarding of a contractor | DevOps / SRE + AppSec Engineer + Security Champion (Training Manager) | Provisioning T-5 days; sign-off before real access (T+7) |

**Useful links.** [Sandbox Preparation Guide for Contractors](./addon/guia-preparacao-sandbox)  
[Model for the Inclusion of Third Parties](./addon/inclusao-terceiros)  
[Governance and Contracting - Chapter 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)  
[Roles and Responsibilities](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

## 📦 Expected artefacts {#-artefactos-esperados}

| Artefact | Evidence |
|-----------|-----------|
| LMS certificates | Onboarding completed |
| LMS reports | Continuous training |
| Champion records | Meetings + feedback |
| Exercise logs | Results and metrics |
| GRC reports | KPIs and effectiveness |
| **Repository of exemplary PRs** | **Recorded code clinics** |
| **Threat modelling diagrams** | **Minutes and risk matrix** |
| **Simulation scenarios and logs** | **Debrief reports and playbooks** |
| **Tracks document with changelog** | **Champions survey + feedback** |
| **Validated onboarding checklist** | **Formal records per staff member** |
| **Quiz records** | **Scores, dates and validators** |
| **Third-party certificates** | **GRC contractual compliance records** |

---

## ⚖️ L1–L3 proportionality matrix {#️-matriz-de-proporcionalidade-l1l3}

| Practice | L1 | L2 | L3 |
|---------|----|----|----|
| Secure onboarding | Basic | Mandatory | Mandatory + practical assessment |
| Continuous training | Basic | Annual | Quarterly |
| Champions | Optional | Recommended | Mandatory |
| Practical exercises | Optional | Recommended | Mandatory |
| Effectiveness metrics | Basic | Annual | Quarterly with targets |
| **Code Clinics** | **Occasional** | **Recurring (fortnightly)** | **Recurring + rotating (weekly)** |
| **Threat Modelling** | **Optional** | **Recommended per epic** | **Mandatory before design** |
| **Incident simulations** | **Recommended annually** | **Quarterly** | **Quarterly + rotating** |
| **Track maintenance** | **Occasional** | **Annual** | **Annual + continuous on trigger** |
| **Tracks proportional to risk** | **Basic track** | **Intermediate track + labs** | **Advanced track + simulations + audit** |
| **Onboarding validation (checklist)** | **Basic** | **Structured (role + risk)** | **Structured + periodic audit** |
| **Knowledge validation (quizzes)** | **One-off** | **Periodic (annual)** | **Periodic + adaptive** |
| **Third-party training** | **Recommended** | **Mandatory** | **Mandatory + annual** |

---

## 🏁 Final recommendations {#-recomendações-finais}

- **Onboarding is critical**: without initial training, basic errors propagate.  
- **Formal validation via checklist** ensures that all the minimum steps are completed.  
- **Structured quizzes** validate knowledge retention in an auditable way.  
- **Continuous training** keeps practices up to date.  
- **Champions** create a security culture within teams.  
- **Practical exercises** increase retention and readiness.  
- **Structured Code Clinics** ensure visible and replicable learning.  
- **Peer-led Threat Modelling** distributes risk analysis knowledge.  
- **Incident simulations** train response under pressure and validate processes.  
- **Periodic maintenance of tracks** ensures the continuing relevance of training.  
- **Tracks proportional to risk** ensure training is suited to context.  
- **Third-party training** reduces the risk of failures through lack of knowledge and meets regulatory obligations.  
- **KPI measurement** ensures continuous improvement and a link to organisational objectives.

```
