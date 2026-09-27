---
id: aplicacao-lifecycle
title: How to Do It
description: Integration of threat modelling throughout the development cycle
tags: [tipo:aplicacao, ciclo-vida, threat-modeling, requisitos, mitigacao, rastreabilidade]
genia: us-format-normalization
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/aplicacao-lifecycle.md
  source_sha256: e67701bee73eb6cb6adb944b609328813c3665c0f0ce7df16cb6c5b6afcebb47
  source_commit: 44d2d3451e163f3ad4ab710e3ee2ec8d02f9e02d
  target_sha256: b550ee0b448a4195624a106e6352451fb059429dbd0f9d5821498de0952d60ab
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [audit_trail, avaliacao, chapter_role, como_fazer, cycle_iteration, deterministic, eu_startups, framework_source_corpus, gap_family, lifecycle_phase, llm, mapping, papel_suporte, plain_rag, practitioner_manual, requirement_runtime, risk_level, role_tech_lead, slug_threat_modeling, threat, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: b9e81e02eb64c52b49420a86d83285b20fc614a9727106cda2975cea0f68b2b7
  translated_at: 2026-09-27T18:03:18Z
  stamped_at: 2026-09-27T18:03:18Z
  reviewed_by: null
---


# Applying Threat Modelling in the Lifecycle

This annex prescribes **how to systematically apply the Threat Modelling practices defined in Chapter 3** throughout the development cycle, ensuring traceability, proportionality to risk and integration with the security requirements.

It includes reusable user story templates, actions per role, expected artefacts and application tables per criticality level (L1–L3).

---

## 📅 When to apply Threat Modelling {#-quando-aplicar-threat-modeling}

| Phase / Event                    | Expected action                                                                 | Who takes part                                                     | Minimum evidence (main artefact) |
|----------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------|----------------------------------------|
| Project / epic start        | Create the Threat Model baseline and define scope/assumptions                     | DevOps / SRE, Product Owner, Software Architects, AppSec Engineer, Scrum Master / Team Lead           | DFD + initial list of threats + decision record (*baseline*) |
| Grooming / Planning           | Review the impact of new user stories on the Threat Model (delta)                   | Developer, Software Architects (where applicable), AppSec Engineer                    | Versioned update + link to backlog (`THREAT-*`)          |
| Architecture Review / ADR     | Validate threats before irreversible architectural decisions                 | Software Architects, AppSec Engineer, Scrum Master / Team Lead                                      | ADR + reviewed Threat Model + decisions per threat                 |
| Critical changes / refactors  | Revalidate the model whenever there is a structural change (flows, trust boundaries, deps) | Developer, QA, Software Architects, AppSec Engineer                              | Updated model + diffs + justifications                         |
| Release / Go-live                | Confirm open threats, exceptions, residual risk and compensating measures            | QA, AppSec Engineer, Product Owner (impact), Scrum Master / Team Lead                | Decisions (mitigate/accept) + evidence of approval              |
| CI/CD (control gate)         | Check the “freshness” of the Threat Model against relevant changes (deterministic) | DevOps / SRE, AppSec Engineer                                                 | Verification result + link to the model version             |

---

## 👥 Who does what {#-quem-faz-o-quê}

| Role / Function             | Key responsibilities |
|----------------------------|--------------------------|
| Software Architects     | Facilitate sessions, keep models up to date and ensure architectural consistency |
| Tech Lead                  | **Responsible for the final decision on the model** in the team/project context (approval of the baseline and revisions) |
| Developer                  | Identify flows, entry points, business rules and relevant technical changes |
| QA                         | Translate threats into acceptance criteria and validate evidence of mitigation/testing |
| AppSec Engineer            | Identify technical threats, review mitigation, validate residual risk and support exception decisions |
| Product Owner              | Prioritise mitigation by business impact and accept explicit trade-offs |
| DevOps / SRE               | Implement deterministic gates, ensure traceability and evidence retention |

---

## 📝 Reusable User Stories and Cards {#-user-stories-e-cartões-reutilizáveis}
### US-01 - Creating the threat model {#us-01---criação-do-modelo-de-ameaça}

**Context.**  
At project start, a threat model proportional to the application's risk must be created.

:::userstory
**Story.**   
As **Software Architects** and **Scrum Master / Team Lead**, I want to create an initial threat model with DFDs and STRIDE/LINDDUN, so that architectural risks are visible and addressed from the outset.

**Acceptance criteria (BDD).**
- **Given** that the project is starting  
  **When** I build the threat model with DFDs  
  **Then** the identified threats are recorded with explicit decisions and minimum evidence,
  **and** the model's assumptions/limits are documented.

**Checklist.**
- [ ] Threat modelling session held  
- [ ] DFDs created and documented  
- [ ] Threats catalogued (STRIDE, LINDDUN, PASTA)  
- [ ] Threats linked to mitigation requirements  
- [ ] Evidence archived in the architecture repository
- [ ] Scope, assumptions and limits of the model documented
- [ ] Person responsible for approving the baseline identified

:::

**Artefacts & evidence.**
- Artefact: initial threat model (tool or Markdown)  
- Evidence: link to backlog `THREAT-*`

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Simplified checklist |
| L2 | Yes | Formal models with STRIDE |
| L3 | Yes | Full models with STRIDE/LINDDUN/PASTA |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Start | Project kick-off | Software Architects + AppSec Engineer | Before the initial backlog |

**Useful links.**
- 🔗 [OWASP Threat Modelling](https://owasp.org/www-community/Threat_Modeling)  

---

### US-02 - Architecture validation with threat modelling {#us-02---validação-de-arquitetura-com-threat-modeling}

**Context.**  
Architecture reviews must include threat modelling in order to identify structural threats.

:::userstory
**Story.**   
As **Software Architects** and **AppSec Engineer**, I want to validate the architecture through threat modelling, so that critical threats are identified before design decisions are made.

**Acceptance criteria (BDD).**
- **Given** that an architecture review takes place  
  **When** I apply threat modelling  
  **Then** structural threats are recorded and mitigated

**Checklist.**
- [ ] Formal architecture review held  
- [ ] Threat model updated  
- [ ] Design decisions documented  
- [ ] Evidence archived

:::

**Artefacts & evidence.**
- Artefact: architecture review reports  
- Evidence: recorded threats linked to requirements

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Simplified review |
| L2 | Yes | Architecture review with threat modelling |
| L3 | Yes | Detailed review + independent validation |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Design / Review | Architecture review | Software Architects + AppSec Engineer | Before design approval |

---

### US-03 - Updating the model after a technical change {#us-03---atualização-do-modelo-após-alteração-técnica}

**Context.**  
Whenever a significant change occurs (new feature, integration or refactor), the threat model must be updated.

:::userstory
**Story.**   
As **Software Architects** and **DevOps/SRE**, I want to update the threat model whenever there are significant changes, so that the model remains valid and useful.

**Acceptance criteria (BDD).**
- **Given** that a significant change occurs  
  **When** I update the model  
  **Then** new or changed threats are recorded and mapped to requirements

**Checklist.**
- [ ] Significant change identified  
- [ ] Threat model updated  
- [ ] New threats recorded  
- [ ] Evidence archived

:::

**Artefacts & evidence.**
- Artefact: updated threat model  
- Evidence: commit or issue linked to the change

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | External integrations only |
| L2 | Yes | All critical changes |
| L3 | Yes | Any change to the architecture |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Refactor / Change | Significant change | Software Architects + Scrum Master / Team Lead | Before the release |

**Useful links.**
- 🔗 [SSDF Practices](https://csrc.nist.gov/publications/detail/sp/800-218/final)  

---
### US-04 - Formal justification of accepted risk {#us-04---justificação-formal-de-risco-aceite}

**Context.**  
Not all threats can be mitigated; residual risks must be formally documented, approved and reviewed.

:::userstory
**Story.**   
As an **AppSec Engineer** and **GRC/Compliance**, I want to document and formally approve the residual risks identified in threat modelling, so that acceptance decisions are transparent and auditable.

**Acceptance criteria (BDD).**
- **Given** that there are unmitigated threats  
  **When** I record an accepted risk  
  **Then** the decision is documented, approved and archived

**Checklist.**
- [ ] Residual risk identified  
- [ ] Justification documented  
- [ ] Formal approval by AppSec  
- [ ] Deadline and reassessment defined  
- [ ] Evidence attached to the risk repository

:::

**Artefacts & evidence.**
- Artefact: `riscos/*.md` files  
- Evidence: issue or PR with approval

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes (when there is accepted risk) | Simple, referenceable record of the acceptance (ticket or note), stating who requested, assessed and approved it |
| L2 | Yes | Formal documentation |
| L3 | Yes | Formal documentation + compensating mitigation |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Planning/Release | Identification of an unmitigated risk | AppSec Engineer | Before go-live |

**Useful links.**
- 🔗 [Exception management](/sbd-toe/sbd-manual/requisitos-seguranca/addon/gestao-excecoes) and [residual risk](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/risco-residual)  

---

### US-05 - Consistency control gate in CI/CD {#us-05---gate-de-controlo-de-consistência-no-cicd}

**Context.**  
The pipeline must ensure that relevant changes do not pass without an update/review of the Threat Model, maintaining traceability and evidence.

:::userstory
**Story.**  
As a **DevOps/SRE** and **AppSec Engineer**, I want to apply a **deterministic gate** that checks whether the Threat Model is up to date with respect to relevant changes, so that releases with an obsolete model are prevented.

**Acceptance criteria (BDD).**
- **Given** that a relevant change is introduced (e.g. new flow, new dependency, new trust boundary)  
  **When** the pipeline runs  
  **Then** the gate requires a reference to an updated version of the Threat Model or an approved justification  
- **And** the evidence of the gate is recorded and auditable

**Checklist.**
- [ ] Objective criteria for “relevant change” defined and versioned
- [ ] Gate implemented with deterministic verification (rules, metadata, diffs)
- [ ] Gate output recorded (logs + reference to the versioned artefact)
- [ ] Exceptions follow an approval workflow (where applicable)

:::

**Artefacts & evidence.**
- Artefact: rule/versioning of criteria + reference to the approved Threat Model
- Evidence: pipeline logs + link to the model's commit/tag

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | No | Manual review in major releases only |
| L2 | Yes | Non-blocking gate with alert and mandatory review |
| L3 | Yes | Blocking gate with formal exceptions and deadline |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| CI/CD | Relevant change (new flow, new dependency, new *trust boundary*) | DevOps/SRE + AppSec Engineer | Non-blocking gate with alert (L2); blocking with formal exception and deadline (L3) |

---

### US-06 - Business impact validation {#us-06---validação-de-impacto-no-negócio}

**Context.**  
The identified threats must be prioritised on the basis of business impact, not only on technical metrics.

:::userstory
**Story.**   
As a **Product Owner**, I want to prioritise the threats identified in the model according to business impact, so that mitigation and investment are optimised.

**Acceptance criteria (BDD).**
- **Given** that threats have been identified  
  **When** I assess them by business impact  
  **Then** priorities are recorded and communicated

**Checklist.**
- [ ] Impact assessed (financial, reputational, legal)  
- [ ] Prioritisation documented  
- [ ] Derived requirements prioritised in the backlog  
- [ ] Evidence archived

:::

**Artefacts & evidence.**
- Artefact: impact vs threat matrix  
- Evidence: prioritised backlog

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Simplified assessment |
| L2 | Yes | Formal impact analysis |
| L3 | Yes | Formal analysis + executive review |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Planning / Grooming | Impact assessment | Product Owner + Executive Management/CISO | Before sprint prioritisation |

---
### US-07 - Controlled reuse and review of previous models {#us-07---reutilização-controlada-e-revisão-de-modelos-anteriores}

**Context.**  
Reusing previous models is useful, but it introduces risk when the context has changed. An explicit review must take place before a model is considered valid.

:::userstory
**Story.**  
As **Software Architects** and **AppSec Engineer**, I want to reuse previous models only with an explicit review of context changes, so that omissions are reduced and incorrect inherited decisions are avoided.

**Acceptance criteria (BDD).**
- **Given** that a similar previous model exists  
  **When** I reuse it as a basis  
  **Then** I document the differences in context/architecture and revalidate critical decisions  
- **And** I record a person responsible for approving the review

**Checklist.**
- [ ] Previous model identified (versioned reference)
- [ ] Differences in architecture/flows/dependencies analysed
- [ ] Critical decisions revalidated (mitigate/accept/transfer)
- [ ] Approval recorded and auditable

:::

**Artefacts & evidence.**
- Artefact: review delta + reference to the approved model
- Evidence: review PR/issue with approval

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Simplified review |
| L2 | Yes | Formal review with diffs |
| L3 | Yes | Formal review + independent review |


**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Design / Review | Reuse of a previous model as a basis | Software Architects + AppSec Engineer | Before the reused model is considered valid |

---

### US-08 - Applying LINDDUN when personal data is processed  *(new)* {#us-08---aplicação-linddun-quando-existir-tratamento-de-dados-pessoais--novo}

**Context.**  
When the system processes personal data, the privacy analysis must complement the security analysis.

:::userstory
**Story.**  
As **Software Architects + AppSec Engineer**, I want to apply **LINDDUN** whenever personal data is processed, so that privacy threats are covered.

**Acceptance criteria (BDD).**
- **Given** that the system processes personal data  
  **When** I carry out Threat Modelling  
  **Then** **I include a LINDDUN analysis** with threats, mitigation and **mapping to the privacy requirements of Ch. 02 (`PRI-001`–`PRI-007`)**  
- And **I create a `privacy-dfd`** with specific trust boundaries  

**Checklist.**
- [ ] `privacy-dfd` created  
- [ ] LINDDUN list filled in  
- [ ] **Link to the privacy requirements of Ch. 02 (`PRI-001`–`PRI-007`)**  
- [ ] **Threats classified by severity and mitigation**  
- [ ] Evidence archived in the architecture repository  
:::

**Artefacts & evidence.**
- `privacy-dfd.*`  
- `privacy-threats.md`  
- LINDDUN report exported / validated  

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|:---|:---|:---|
| L1 | Yes | Lightweight form: the seven LINDDUN categories worked through over the personal-data flows, with the threats linked to the `PRI-*` requirements |
| L2 | Yes | Formal privacy analysis |
| L3 | Yes | Full LINDDUN + independent validation (DPO) |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|:---|:---|:---|:---|
| Design / Review | Presence of personal data | Software Architects + GRC / Compliance | Before design approval |

**Useful links.**
- 🔗 [LINDDUN Framework](https://www.linddun.org/)  
- 🔗 [ENISA - Privacy by Design Guidelines](https://www.enisa.europa.eu/)  

---
### US-09 - Formal approval of the Threat Model (baseline and revisions) {#us-09---aprovação-formal-do-threat-model-baseline-e-revisões}

**Context.**  
Threat Modelling is only a security control when there is an approved model, with a person responsible and minimum evidence.

:::userstory
**Story.**  
As **Tech Lead** and **AppSec Engineer**, I want to formally approve the Threat Model (baseline and revisions), so as to ensure an explicit decision, traceability and auditability.

**Acceptance criteria (BDD).**
- **Given** that the Threat Model has been updated  
  **When** I conclude the review  
  **Then** there is a formal approval decision with an identified person responsible  
- **And** the minimum mandatory evidence is present and versioned

**Checklist.**
- [ ] Scope, assumptions and limits documented
- [ ] Threats identified with a decision per item (mitigate/accept/transfer/reject)
- [ ] Links to requirements/mitigations created (e.g. `REQ-*`, `THREAT-*`)
- [ ] Minimum evidence attached (diagrams/versioning/decision)
- [ ] Approval recorded (PR/issue/signature according to the process)

:::

**Artefacts & evidence.**
- Artefact: approved Threat Model (version/tag) + `decisions.md`
- Evidence: approval record + links to backlog and requirements

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Lightweight approval (simple record) |
| L2 | Yes | Formal approval by Tech Lead + AppSec Engineer |
| L3 | Yes | Formal approval + independent review (segregation) |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Approval | Conclusion of the review of an updated Threat Model | Scrum Master / Team Lead + AppSec Engineer | Lightweight approval by simple record (L1); formal (L2); formal + independent review (L3) |

---

### US-10 - Access control, classification and retention of Threat Modelling artefacts {#us-10---controlo-de-acesso-classificação-e-retenção-dos-artefactos-de-threat-modeling}

**Context.**  
Threat modelling diagrams and decisions are sensitive assets and must have protection proportional to the risk.

:::userstory
**Story.**  
As **Software Architects** and **DevOps/SRE**, I want to control access to and retention of Threat Modelling artefacts, so that the risk of exposing the architecture and critical decisions is reduced.

**Acceptance criteria (BDD).**
- **Given** that Threat Modelling artefacts are produced  
  **When** they are stored and shared  
  **Then** they follow the defined rules for least-privilege access, classification and retention  
- **And** there is evidence of where they are stored and who has access

**Checklist.**
- [ ] Storage location defined and versioned
- [ ] Access control applied (least privilege)
- [ ] Classification defined (sensitivity/internal sharing)
- [ ] Retention and deletion defined (where applicable)
- [ ] Evidence of access and changes available/auditable

:::

**Artefacts & evidence.**
- Artefact: repository policy/rules + directory structure
- Evidence: ACLs/groups + audit logs (where applicable)

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Basic control and internal storage |
| L2 | Yes | Formal control + change tracking |
| L3 | Yes | Reinforced control + segregation and auditing |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Continuous | Storage or sharing of Threat Modelling artefacts | Software Architects + DevOps/SRE | Basic control with internal storage (L1); formal with change tracking (L2); reinforced with segregation and auditing (L3) |

---

### US-11 - Threat modelling for a system with an AI agent (tool-use) {#us-11}

**Context.**
When the system integrates **autonomous agents** with *tool-use* — models that invoke real *tools* to create PRs, read secrets, run *deploys* or contact APIs — the attack surface is no longer just the model: it comes to include the closed set of invocable *tools*, the identity under which the agent operates and the `agentic → tool` boundary where the real effect materialises. The agentic playbook of Ch. 03 is applied before operation and at every rise in autonomy level, so that the applicable MITRE ATLAS threats are identified and anchored in citable controls.

:::userstory
**Story.**
As a **Software Architect** and **AppSec Engineer**, I want to run the [agentic playbook](./addon/metodologias-e-ferramentas#playbook-agentic) whenever an A1+ agent is introduced into the system or rises in autonomy level, so that the applicable threats are catalogued with real IDs (MITRE ATLAS `AML.T*` and OWASP LLM Top 10 2025) and each one is linked to concrete controls in Chs. 04, 07, 10 or 12 before *go-live*.

**Acceptance criteria (BDD).**
- **Given** that an AI agent is going to operate at A1+ in the project
  **When** its *mandate* ([`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) is proposed
  **Then** there is an agentic DFD with five participants (human → client → model → *tool runtime* → external system) and four explicit boundaries (input · inference · agentic · tool)
- **Given** the agentic DFD
  **When** the playbook exercise is carried out
  **Then** the destructive/*side-effectful* *tools* are marked, the applicable threats are cited by canonical ID (`AML.T0051.001`, `AML.T0086`, `AML.T0110`, `LLM06-2025`, etc.) and each one has a mitigation anchored in a chapter of the manual
- **Given** a rise in autonomy level (A1→A2, A2→A3, …) or a change to the `tools_allowlist`
  **When** activation is intended
  **Then** the exercise is repeated and the *mandate* record references the new *threat model*

**Acceptance criteria (DoD).**
- [ ] Agentic DFD versioned in a repository, with trust boundaries marked
- [ ] List of *tools* invocable by the agent, labelled `read` / `write` / `destructive` / `external`
- [ ] Applicable *threats* identified with **canonical IDs** (MITRE ATLAS `AML.T*` or OWASP LLM Top 10 2025); eliminated threats come with a short justification
- [ ] Each non-eliminated *threat* has a control entry landing in Ch. 04 ([`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)/[`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)), Ch. 07, Ch. 10 or Ch. 12
- [ ] *Mitigation confidence* (`derived` vs `heuristic`) labelled on each *threat*↔control link
- [ ] Cross-check against the organisational register: if a mitigation is not implemented, the agent does not operate at the requested level

:::

**Artefacts & evidence.**
- Versioned agentic DFD (Mermaid, drawio or equivalent)
- *Threat model document* with a `threat_id` × `boundary` × `mitigations` × `confidence` table
- Cross-reference `mandate_ref` ↔ `threat_model_ref` in the *mandate* record
- Revision history of the *threat model* linked to the level rises

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Recommended for A1; mandatory for A2+ | Simplified DFD + short *threat library* (Top 3–5 *threats*) |
| L2 | Mandatory for A1+ | Full DFD + the playbook's full *threat library* + anchored *mitigations* |
| L3 | Mandatory for A1+ | Full DFD + *threat library* + independent `appsec` review + cross-reference with the AI Act cross-check where applicable |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Design | Introduction of the agent into the system | Software Architects + AppSec Engineer | Before activation of the *mandate* |
| Level rise | Promotion A1→A2 or higher | `appsec` | Before the new activation |
| Change of *tools* | Addition/removal in `tools_allowlist` | `appsec` | Before the *tool* enters into use |
| Model change | Major version of the *provider* | `appsec` | Before the *cutover* |

**Useful links.**
- 🔗 [Full agentic playbook (Ch. 03)](./addon/metodologias-e-ferramentas#playbook-agentic)
- 🔗 [`REQ-AGN-*` catalogue (Ch. 02)](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)
- 🔗 [`ARC-015` — agent as *principal* (Ch. 04)](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)
- 🔗 [Policy 38 — AI Agent Mandates](/sbd-toe/assets/policies/policy-mandates-agentes)

---

### US-12 - Extended threat modelling for non-agentic AI/ML components {#us-12---threat-modeling-estendido-para-componentes-aiml-não-agentic}

Systems with predictive models, conversational LLMs or RAG have adversarial threats that classic STRIDE does not cover, even without a tool-use agent.  

**Context.** [`THR-008`](./addon/catalogo-requisitos-threat-modeling) requires an extended threat model for all AI/ML components, but US-11 only covers the agentic case (tool-use). A predictive model, a classifier, an LLM in a conversational interface or a RAG pipeline have adversarial surfaces of their own — model poisoning, training data poisoning, evasion, model theft, direct/indirect prompt injection — that remain unmodelled when there is no agent. This gap leaves AI systems without tool-use with no formal coverage.  

:::userstory
**Story.**   
As a **Software Architect** and **AppSec Engineer**, I want to extend the threat model with AI/ML adversarial threats whenever the system integrates artificial intelligence components without tool-use (predictive models, conversational LLMs, RAG), so that the specific threats are catalogued by canonical ID and anchored in controls before go-live.  

**Acceptance criteria (BDD).**  
- **Given** a system that integrates an AI/ML component without a tool-use agent  
  **When** threat modelling is carried out  
  **Then** the STRIDE/LINDDUN baseline is complemented (not replaced) with AI/ML framing, and the additional trust boundaries are identified (training data → model, prompt input → model, model → output)  
- **Given** the AI/ML framing applied  
  **When** each threat is catalogued  
  **Then** it is cited by canonical ID (MITRE ATLAS `AML.T*`, NIST AI 100-2 e2025, or OWASP LLM/ML Top 10) and has a mitigation anchored in a chapter of the manual  

**Checklist.**  
- [ ] Additional AI/ML trust boundaries marked in the DFD (training-time, inference-time, output)  
- [ ] Adversarial threats catalogued by canonical ID (ATLAS `AML.T*` / NIST AI 100-2 / OWASP LLM/ML Top 10)  
- [ ] STRIDE/LINDDUN baseline complemented, not replaced  
- [ ] Each non-eliminated threat linked to a control in a chapter of the manual  

:::

**Artefacts & evidence.** DFD with AI/ML trust boundaries; `threat_id` × `boundary` × `mitigations` table referenced to ATLAS/NIST/OWASP; link to derived `REQ-*`.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Recommended: triage by OWASP LLM/ML Top 10 | Mandatory: full AI/ML framing + boundaries + anchored mitigations | Mandatory: full framing + adversary capabilities (NIST AI 100-2) + independent `appsec` review |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Design | Introduction of an AI/ML component without tool-use | Software Architects + AppSec Engineer | Before go-live |
| Change | Replacement of the base model, dataset or RAG pipeline | `appsec` | Before cutover |

**Useful links.** [Methodologies — §AI/ML](./addon/metodologias-e-ferramentas#ai-ml) · [`THR-008`](./addon/catalogo-requisitos-threat-modeling)

---

### US-13 - Deriving abuse/misuse cases for the backlog {#us-13---derivação-de-abusemisuse-cases-para-o-backlog}

Analysis centred on the legitimate user misses abuse paths that only an adversarial perspective reveals.  

**Context.** The [abuse/misuse cases method](./addon/abuse-misuse-cases) prescribes a cross-functional workshop that makes requirements elicitation adversarial, but no user story operationalises it. Without that, abuse cases remain a one-off exercise whose conclusions are lost between sprints. The method only changes the product when each prioritised abuse materialises as a traceable backlog item, with an owner and an adversarial acceptance criterion, feeding the threat model and the tests.  

:::userstory
**Story.**   
As an **AppSec Engineer** and **Product Owner**, I want to derive abuse/misuse cases in a cross-functional workshop and integrate them into the backlog as traceable requirements, so that the identified abuse paths translate into verifiable controls and are not lost.  

**Acceptance criteria (BDD).**  
- **Given** a relevant functional flow of an L2+ system  
  **When** the abuse cases workshop is conducted (product + dev + security + QA)  
  **Then** each flow generates its adversarial counterpart ("as an attacker, I want ⟨goal⟩ by exploiting ⟨weakness⟩"), prioritised by risk (Ch. 01)  
- **Given** the prioritised abuse cases  
  **When** the exercise is closed  
  **Then** each one enters the backlog as a requirement with an owner, an adversarial acceptance criterion and a status, and feeds the threat model and the test cases (Ch. 10)  

**Checklist.**  
- [ ] Cross-functional workshop held (product, dev, security, QA)  
- [ ] Abuse cases derived per flow and prioritised by risk  
- [ ] Each prioritised abuse case in the backlog with an owner and an adversarial acceptance criterion  
- [ ] Abuse cases linked to the threat model and to test cases  

:::

**Artefacts & evidence.** Workshop record; list of prioritised abuse/misuse cases; backlog items with an adversarial acceptance criterion; link to `THREAT-*` and to tests.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Not applicable | Mandatory: workshop on critical flows + integration into the backlog | Mandatory: systematic workshop + coverage per flow + traceability to tests |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Requirements / Threat Modelling | Start of an epic or of a relevant functional flow | AppSec Engineer + Product Owner | Before requirements derivation |

**Useful links.** [Abuse and Misuse Cases Method](./addon/abuse-misuse-cases) · [Testing strategy (Ch. 10)](/sbd-toe/sbd-manual/testes-seguranca/addon/estrategia-testes)

---

### US-14 - Independent review at L2 and PASTA in high risk {#us-14---revisão-independente-em-l2-e-pasta-em-alto-risco}

Independent review covers the team's blind spots; in high risk, the method must escalate to risk-based analysis.  

**Context.** [`THR-007`](./addon/catalogo-requisitos-threat-modeling) requires independent review by AppSec before go-live already at **L2** (not only L3), but US-09 only makes independent review explicit at L3 — leaving L2 without operationalisation. In parallel, [`THR-003`](./addon/catalogo-requisitos-threat-modeling) prescribes **PASTA or equivalent** in high-risk contexts (regulated systems, formal demand for threat → risk → control tracing), a prescription that no US operationalises. This US closes both gaps: independent review from L2 onwards and methodological escalation to PASTA at L3.  

:::userstory
**Story.**   
As an **AppSec Engineer** and **Tech Lead**, I want the threat model to be reviewed by someone independent of the delivery team before go-live from L2 onwards, and high-risk systems to apply PASTA as the methodology, so as to ensure coverage of blind spots and formal tracing threat → risk → control.  

**Acceptance criteria (BDD).**  
- **Given** an L2+ system about to go live or with a material architectural change  
  **When** the threat model is finalised  
  **Then** it is reviewed by AppSec or by someone with equivalent competence, independent of the delivery team, with evidence (record, approval or list of deviations with a plan)  
- **Given** the absence of that review  
  **When** an attempt is made to proceed to go-live  
  **Then** go-live is blocked  
- **Given** a high-risk system (regulated or L3)  
  **When** the methodology is selected  
  **Then** PASTA or equivalent is applied, with threat → risk → control tracing declared in the artefact  

**Checklist.**  
- [ ] Reviewer independent of the delivery team identified (L2+)  
- [ ] Evidence of the review produced (record/approval/list of deviations)  
- [ ] Go-live blocked in the absence of review  
- [ ] PASTA (or equivalent) applied and declared in high-risk systems  

:::

**Artefacts & evidence.** Independent review record with a named person responsible; list of deviations with a plan (where applicable); PASTA artefact with threat → risk → control mapping (high risk).  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Not applicable | Independent review mandatory before go-live; PASTA optional | Independent review mandatory + PASTA (or equivalent) with formal tracing |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Pre-go-live | Go-live of an L2+ application or material architectural change | `appsec` (independent) | Before go-live (blocking) |
| Design | Regulated / high-risk system | Software Architects + AppSec Engineer | At methodology selection |

**Useful links.** [`THR-007`](./addon/catalogo-requisitos-threat-modeling) · [`THR-003`](./addon/catalogo-requisitos-threat-modeling) · [Methodologies — PASTA comparison](./addon/metodologias-e-ferramentas)

---

### US-15 - Explicit treatment of the process risks of threat modelling {#us-15---tratamento-explícito-dos-riscos-de-processo-do-threat-modeling}

A plausible but incomplete threat model gives false confidence — worse than the absence of the artefact.  

**Context.** The [process risks of threat modelling](./addon/riscos-processo-threat-modeling) — structural omission, perspective bias, confusion between intermediate analysis and formal decision, uncritical dependence on previous models, plausible but incorrect results — are fallible by nature and independent of the method. The manual assumes them explicitly, but no user story requires them to be acknowledged and mitigated in the artefact. Without that, the team treats the threat model as validated truth instead of a hypothesis subject to error.  

:::userstory
**Story.**   
As an **AppSec Engineer** and **Software Architects**, I want to explicitly acknowledge and treat the process risks of threat modelling in each model produced, so that omissions, biases and misleading plausibility are assumed as inherent risk and not confused with real coverage.  

**Acceptance criteria (BDD).**  
- **Given** that a threat model is produced  
  **When** the artefact is finalised  
  **Then** supporting material (notes, exploratory lists, hypotheses) is clearly distinguished from validated and approved decision  
- **Given** the reuse of a previous model  
  **When** it is adopted as a basis  
  **Then** it is treated as a starting hypothesis, with explicit revalidation of the context changes (cross-reference US-07)  
- **Given** the finalised artefact  
  **Then** it is recorded that the absence of a threat is not proof that it does not exist, and the risks of omission/bias are assumed  

**Checklist.**  
- [ ] Supporting material distinguished from approved formal decision  
- [ ] Reused models treated as hypotheses, with revalidation of context  
- [ ] Risk of omission/bias explicitly assumed in the artefact  
- [ ] Plausibility not treated as a substitute for validation and evidence  

:::

**Artefacts & evidence.** Assumptions/limits section in the threat model; versioned separation between exploratory notes and approved decision; note on the risk of omission in the artefact.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Informal note of assumptions | Assumptions and limits documented; separation of support/decision | Formal treatment of process risks + independent review of coverage |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Threat Modelling | Finalisation or reuse of a threat model | AppSec Engineer + Software Architects | Before approval of the baseline |

**Useful links.** [Process Risks in Threat Modelling](./addon/riscos-processo-threat-modeling) · [Validation and Evidence](./addon/validacao-evidencia-threat-modeling)

---
## ⚖️ Proportional application by risk level (L1–L2–L3) {#️-aplicação-proporcional-por-nível-de-risco-l1l2l3}

| Practice / Activity              | L1 (low risk)                         | L2 (medium risk)                                | L3 (high risk)                                                  |
|----------------------------------|------------------------------------------|-------------------------------------------------|------------------------------------------------------------------|
| Threat Modelling sessions       | Basic (simplified STRIDE checklist)  | Formal models with STRIDE                     | Full models with STRIDE **and LINDDUN** (where applicable) + PASTA + automation |
| Architecture review           | Optional                                 | Mandatory inclusion                           | Always mandatory, with independent review                      |
| Integration into CI/CD              | Not applicable                            | Periodic review                              | Integrated, blocking automation                                 |
| Accepted risk                     | Informal                                 | Documented                                    | Formal, approved by the AppSec Engineer and with a defined sunset       |
| Automation / Reuse         | Not applicable                            | Recommended (tool or script)             | Mandatory (centralised tool, continuous integration)       |
| **LINDDUN analysis (privacy)**| Not applicable                            | Mandatory if there is personal data           | Always mandatory, with review by the DPO                          |

---

## 📄 Templates and expected artefacts {#-templates-e-artefactos-esperados}

| Artefact                          | Suggested format     | Where to store / reference                |
|-----------------------------------|----------------------|-------------------------------------------|
| Initial threat model (STRIDE) | Tool / `.md`   | `docs/` directory or repository          |
| **Privacy model (LINDDUN)** | Tool / `.md`  | `docs/privacy/` directory or a sub-folder of the model |
| Model updates            | Tool / `.md`   | `docs/` directory or repository          |
| Derived cards (`THREAT-*`)     | Board / Jira         | Team backlog                         |
| **Privacy cards (`PRIV-*`)** | Board / Jira        | Team backlog                         |
| Accepted risk justification       | Markdown / issue     | `riscos/` directory or board              |
| Traceability reports      | Export / `.csv`      | Audit archive                      |
| **LINDDUN reports**             | Export / `.pdf`/`.csv`| `docs/privacy/` directory or audit    |
| Automated models              | Tool           | Central model repository            |
