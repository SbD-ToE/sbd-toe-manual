---
id: intro
title: AI Act - Normative cross-check
description: Analysis of how SbD-ToE covers the technical requirements of Regulation (EU) 2024/1689 (AI Act) - accuracy, robustness, cybersecurity, logging, risk management and post-market monitoring of AI systems
tags: [cross-check, ai-act, regulamento-ia, ia, machine-learning, robustez, ciberseguranca, gpai]
sidebar_position: 6
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/ai-act/01-intro.md
  source_sha256: ae22bac0310d5337d8c9259c2a36edc93275663ca9c2030577841eb922fe309d
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 87b3cc1a3872d8ee6e4847a516b989e3aa9453e8b94688f03c4185dd928e19b8
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5f18169e44cb78faceac7d31df119020c508135f27e39f4105f054ecf5a72d33
  glossary_keys: [audit_trail, avaliacao, capacitacao, chapter_role, cycle_iteration, discipline, esquema_regime, eu_ai_fria, eu_ai_gpai_model, eu_ai_high_risk_system, eu_ai_human_oversight, eu_ai_instructions_for_use, eu_ai_qms, eu_ai_system, eu_ai_training_data, eu_ai_widespread_infringement, eu_biometric_identification, eu_ce_marking, eu_critical_infrastructure, eu_market_surveillance_authority, eu_notified_body, eu_placing_on_market, eu_reasonably_foreseeable_misuse, framework_source_corpus, gap_family, layer, lifecycle_phase, llm, mapping, mcp, mcp_reading_programa, normative_empirical, papel_suporte, practitioner_manual, programme_line, provenance, requirement_runtime, role_juridico, role_tech_lead, sbdtoe_sbd, schema, slug_threat_modeling, traceability, trilho_formativo, validation_evaluation]
  glossary_sha256: 7b013ae242071785e1dd4c4af9bfaa8930d8b1950f3550f2f0a5795ef08bc04a
  translated_at: 2026-09-26T18:11:52Z
  reviewed_by: null
---

# AI Act: Normative cross-check

> For practical implementation, see the [SbD-ToE 4 AI Act Playbook](/sbd-toe/cross-check-normativo/ai-act/playbook).
>
> For universal application patterns, see the core chapters of SbD-ToE (01–14).

## Scope {#âmbito}

### 🤖 AI Act - Artificial Intelligence Regulation {#-ai-act---regulamento-de-inteligência-artificial}

The **AI Act** is **Regulation (EU) 2024/1689** (CELEX: [32024R1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)), the world's first horizontal legal framework dedicated to artificial intelligence. It entered into force on 1 August 2024 and applies in phases:

- **2 February 2025** - prohibited practices (Art. 5) and AI literacy (Art. 4).
- **2 August 2025** - general-purpose AI models (GPAI, Chapter V), governance and the penalties regime.
- **2 August 2026** - the bulk of the obligations for **high-risk** AI systems in Annex III.
- **2 August 2027** - high-risk systems covered by the product legislation in Annex I.

> ℹ️ **Note (2026):** the **Digital Omnibus** political agreement (2026) provides for **deferring** the high-risk obligations — Annex III to **2 December 2027** and Annex I to **2 August 2028**. The dates above are the **enacted** ones; the deferral only takes effect upon publication in the Official Journal.

The AI Act adopts a **risk-based approach**, with four tiers: **unacceptable** risk (prohibited, Art. 5), **high risk** (Art. 6 and Annexes I/III, subject to the bulk of the technical obligations), **limited** risk (transparency duties, Art. 50) and **minimal** risk (no specific obligations). On top of these tiers sit specific rules for **GPAI** (Art. 53) and GPAI with **systemic risk** (Art. 55).

It is essential to frame the nature of the regulation: the AI Act is, first and foremost, **product safety and fundamental rights protection legislation** applied to AI systems, not an application security (AppSec) standard. However, the obligations for high-risk systems incorporate **substantial technical requirements** that intersect directly with SbD-ToE - in particular:

- **Art. 9** - risk management system throughout the lifecycle;
- **Art. 12 / Art. 19** - automatic recording of events (logging) and keeping of logs;
- **Art. 15** - accuracy, robustness and **cybersecurity** (including resilience to adversarial attacks);
- **Art. 17** - quality management system (QMS);
- **Art. 72** - post-market monitoring;
- **Art. 73** - reporting of serious incidents.

In SbD-ToE, the AI Act is operationalised through the same technical disciplines that underpin any secure software - secure engineering (requirements, architecture, development, IaC, pipelines, testing), supply chain and provenance (dependencies, containers, SBOM), monitoring and response processes, and governance/contracting - now applied to the **lifecycle of AI systems** (datasets, models, training and inference pipelines, inference services).

> ⚖️ **Editorial note.**
> This section is an **operational synthesis** of the relevant articles of the AI Act, not a literal quotation of the regulation.
> It draws in particular on Articles 9 (risk management), 10 (data and data governance), 11 and Annex IV (technical documentation), 12 and 19 (records/logs), 13–14 (transparency and human oversight), 15 (accuracy, robustness, cybersecurity), 17 (QMS), 72 (post-market monitoring), 73 (serious incidents) and 53/55 (GPAI and systemic risk).

> ⚖️ **Note on technical references.**
> The AI Act sets essential requirements but defers the technical detail to **harmonised standards** (to be developed by CEN-CENELEC) and common specifications.
> Standards such as **ISO/IEC 42001** (AI management system), **ISO/IEC 23894** (AI risk management), **ISO/IEC 27090** (AI security, under development), the **NIST AI Risk Management Framework (AI RMF 1.0)**, **MITRE ATLAS** (adversarial tactics and techniques against ML), the **OWASP Machine Learning Security Top 10** and the **OWASP Top 10 for LLM Applications** are widely recognised and provide a solid basis for meeting the technical and procedural requirements.
> SbD-ToE treats these standards as **recommended good practice**, not as legal requirements in themselves.

## Regulatory Notice {#aviso-regulatório}

SbD-ToE covers the **technical "how"** of the high-risk requirements, but **does not replace** the legal, AI-domain and conformity assessment dimensions of the AI Act. Specifically, the following are **out of scope** for the manual:

- **Risk classification** (Art. 6 and Annexes I/III) - the legal determination of whether a system is high-risk.
- **Governance of training data, validation data and testing data** (Art. 10) - representativeness, detection and mitigation of bias (*bias*), statistical quality of the data sets. These are **AI/data science domain** questions, not AppSec ones.
- **Transparency and information to deployers** (Art. 13) and to natural persons (Art. 50).
- **Human oversight** (Art. 14) - the **design/UX** of *human-in-the-loop* / *human-on-the-loop* mechanisms and human judgement (oversight-as-understanding). The **interruption (*stop/override*) and governance** facet is technically covered (see matrix, Art. 14).
- **Fundamental rights impact assessment (FRIA)** (Art. 27) - an obligation of deployers (*deployers*).
- **Conformity assessment** (Art. 43), involvement of **notified bodies**, **EU declaration of conformity** (Art. 47), **CE marking** (Art. 48) and **registration in the EU database** (Art. 49/71).
- **Determination of prohibited practices** (Art. 5) and the legal qualification of roles (provider, deployer, importer, distributor).

These dimensions fall within the remit of compliance, legal, data science teams and of the relationship with the competent authority. SbD-ToE provides the technical controls and the evidence; it does not issue the conformity judgement.

---

## Cross-Check Matrix (summary) {#matriz-de-cross-check-resumo}

> ✏️ **Refresh 2026-05-30.** This matrix was updated following the *agentic release* (Ch. 02 §A0–A4, Ch. 03 agentic playbook, [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), `DEP-012..014`, `OPS-012..014`, Policy 38, Policy 39, US-13/14/15/16/19/21). Several gaps that were classified as "intentional" (out of AppSec by design) have been **partially or fully closed** — these are flagged where they apply.

| AI Act domain | Reference (article) | SbD-ToE coverage | Residual gap | Adaptation action |
|---|---|---|---|---|
| AI literacy | Art. 4 | Ch. 13 (training), Policy 37 §11 (matrix per *role*) | Formal literacy assessment | Document completions of training tracks as evidence |
| Risk management system | Art. 9 | Ch. 01 (classification), Ch. 02 (requirements), Ch. 02 §A0–A4 + [`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) (autonomy levels), Ch. 03 (threat modelling + agentic playbook), Ch. 12 (monitoring) | Risk to health, safety and fundamental rights throughout the intended use | Extend the threat model with an AI risk taxonomy (ATLAS — already included) and societal impact |
| Data and data governance | Art. 10 | Ch. 05 (provenance), [`DEP-011`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011) (AI inventory), [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) (AI BOM CycloneDX 1.6 ml-bom), Policy 39, Ch. 02 (data requirements) | Representativeness, bias, statistical quality (AI domain) | Data science *data governance* process; *datasheets*/*data cards* |
| Technical documentation | Art. 11, Annex IV | Ch. 02, Ch. 04 (architecture + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)), Ch. 05 ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) AI BOM), Ch. 06, Policy 38 (mandate) | Formal structure of Annex IV; *model cards* | Map SbD-ToE artefacts (including mandate + AI BOM) to the Annex IV index |
| Recording of events (logging) | Art. 12, Art. 19 | Ch. 12 (observability), [`OPS-011`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes) (AI/ML), [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) (audit per *tool invocation* with `mandate_ref`), Ch. 12 US-13 (agentic telemetry), Policy 30 §9 | Field schema specific to the *model output* remains configurable | Document the inference schema per system |
| Transparency to deployers | Art. 13 | Ch. 02, Ch. 04 (partial), Policy 38 (mandate as a structured source of *capabilities*, limitations and oversight) | Model-specific performance metrics | Derive "instructions for use" from the mandate + Ch. 04/06 artefacts |
| Human oversight | Art. 14 ⚡ | Ch. 02 §A0–A4 + `REQ-AGN-001..004` (mandate, level classification, *kill-switch*, *intent declaration*), Ch. 04 [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (OOB approval + architectural *kill-switch*), Policy 38 (mandate lifecycle) | Human intervention UX/flow (AI/product domain) | UX design remains with the AI team; technical control and operational governance already inside |
| Accuracy, robustness and cybersecurity | Art. 15 | Ch. 03 agentic playbook + MITRE ATLAS, Ch. 04 ([`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)+[`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)), Ch. 05 (AI BOM), Ch. 10 §C5 (*eval suites*), Ch. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) (*jailbreak* / *off-policy*) | Declared accuracy metrics; regulatory thresholds | Declare metrics in coordination with the AI team |
| Quality management system | Art. 17 | Ch. 07 (CI/CD), Ch. 11 (release), Ch. 06, Ch. 14, Policy 38 (mandate lifecycle), Policy 39 (AI BOM lifecycle) | Formal quality manual | Map SbD-ToE gates + Policy 38/39 cycles to the QMS elements |
| Supply chain | Art. 25 | [`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013) (*pinning*), [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) (list of approved *providers*), Policy 39, Ch. 14 US-21 | — | — |
| Obligations of the *deployer* | Art. 26 | Policy 38 (mandate + ownership), Ch. 02 §A0–A4, Ch. 12 US-13 (logs under the *deployer*'s control) | Operational documentation of the *deployer* | Extend the mandate with specific obligations when the organisation is a *deployer* |
| Conformity and CE marking | Art. 43, 47–49 | — ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) is the *provider*'s declaration of conformity, not the organisation's own CE marking) | Conformity assessment of the system + the organisation's CE marking | Establish a GRC + legal swimlane for the assessment circuit |
| GPAI and systemic risk | Art. 53, Art. 55 | Ch. 03 playbook + Ch. 05 (AI BOM), Ch. 10 §C5 (*eval suites* + *red teaming*), Ch. 12 US-13 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014), Policy 19 §7, Policy 30 §9 | GPAI technical documentation (Annex XI/XII); *copyright* policy | Documentation delegated to the AI team; *cybersecurity* already inside |
| Post-market monitoring | Art. 72 | Ch. 12 (monitoring, *drift*), `OPS-011..014`, Ch. 12 US-13 | Formal post-market monitoring plan per system | Formalise a plan per system based on the signals already available |
| Serious incidents | Art. 73 | Ch. 12, Ch. 14, [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) (*off-policy* → IR), Policy 30 §9.3, Policy 16 §11.4 (agentic-specific incidents) | Regulatory definition of "serious incident"; deadlines (2/10/15 days) and *templates* | Parameterise the *runbook* and the SIEM/ITSM exporters |

---

## PART I: NORMATIVE ANALYSIS {#parte-i-análise-normativa}

### Article 4 - AI literacy {#artigo-4---literacia-em-ia}

**Normative content**

Art. 4 requires *providers* and *deployers* to ensure that staff involved in the operation or use of AI systems have a **sufficient level of AI literacy**, taking into account their technical knowledge, experience, education and training, as well as the context in which the system is to be used and the intended recipients.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Training proportionate to role | Ch. 13 + Policy 37 §11 | Coverage matrix per *role* (developer, appsec, devops, grc, tech lead, PO/SM, CISO) + practical exercises |
| Periodic refresh | Policy 37 §11 | Cadences: onboarding + annual or half-yearly refresh depending on the *role* |
| Tracks for assisted vs autonomous use | Ch. 13 (addon 12) + Policy 16 + Policy 38 | Differentiation between assisted use (A0–A1) and autonomous operation (A2+) |

**What SbD-ToE covers**

- **Training coverage matrix per *role*** (Policy 37 §11) — defines minimum content, cadence and practical exercises per role.
- **Distinction between assisted and autonomous use** — those who operate A2+ agents have a specific training track (A0–A4 model, `REQ-AGN-*`, *kill-switch*, OOB approval), in addition to the assisted-use track.
- **Practical exercises** — *tabletops* of *off-policy action*, *red team* against an agent in a sandbox, *mandate* classification exercise (Policy 37 §11.2).
- **Automatic activation** — when the organisation adopts AI agents at A1+, the agentic module of Policy 37 §11 becomes **mandatory** (instead of recommended).

**Residual gaps**

**Formal literacy assessment** (tests, internal certifications, tracking of competence over time) is work for HR and the upskilling function. SbD-ToE defines the **minimum content** and the **cadence**, not the method of individual assessment.

**How to comply**

Policy 37 §11 can be operationalised directly. For organisations with heavy adoption of agents, it is suggested to complement it with periodic competence assessment and formal recording of track completions as evidence for Art. 4.

---

### Article 9 - Risk management system {#artigo-9---sistema-de-gestão-de-risco}

**Normative content**

Art. 9 requires a **continuous iterative** risk management system throughout the entire lifecycle of the high-risk AI system: identification and analysis of the known and reasonably foreseeable risks to health, safety and fundamental rights; estimation of the risks under intended use and under reasonably foreseeable misuse; adoption of appropriate risk management measures; and testing to identify the most appropriate measures.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Risk identification and analysis | Ch. 03 | Threat modelling (STRIDE, MITRE ATT&CK) + [agentic playbook](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) with MITRE ATLAS already included |
| Proportionality to risk | Ch. 01 + Ch. 02 §A0–A4 | L1–L3 classification + agentic autonomy levels A0–A4 ([`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) |
| Risk management measures | Ch. 02 | Requirements catalogue per level + `REQ-AGN-001..004` |
| Iterative and continuous evaluation | Ch. 12 | Continuous monitoring, improvement + `OPS-011..014` |

**What SbD-ToE covers**

- Structured threat identification through threat modelling (Ch. 03), with the **agentic playbook** already incorporated and MITRE ATLAS as an active catalogue (not merely extensible).
- Application criticality classification (Ch. 01), the basis for the proportionality of controls, **complemented by the autonomy levels A0–A4** for systems that include AI agents with *tool-use* ([`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)).
- Catalogue of security requirements and their measures (Ch. 02), including the agentic subset `REQ-AGN-001..004`.
- Continuous reassessment, in a cycle, with operational metrics (Ch. 12), including agentic-specific signals (`OPS-011..014`).

**Intentional gaps**

SbD-ToE threat modelling is, by construction, **domain-agnostic**: it covers security threats to the system, but does not prescribe the analysis of risks to **health, safety and fundamental rights** specific to the AI Act (e.g. risk of discrimination, societal impact). This dimension is specific to the AI Act and requires the involvement of domain, ethics and legal teams.

**How to comply**

It is suggested to extend the Ch. 03 threat model with an AI risk taxonomy - using **MITRE ATLAS** for the adversarial vector and the **NIST AI RMF** / **ISO/IEC 23894** for the risk framing - and to link the iteration to the continuous improvement cycle of Ch. 12. The residual risk and the measures should be documented, maintaining the auditable record that Art. 9 presupposes.

---

### Article 10 - Data and data governance {#artigo-10---dados-e-governação-de-dados}

**Normative content**

Art. 10 requires that the training data sets, validation data sets and testing data sets be subject to appropriate data governance practices: relevance, representativeness, freedom from errors and completeness to the best extent possible, appropriate statistical properties, and examination of possible biases likely to affect health, safety or fundamental rights.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Data provenance and integrity | Ch. 05 + [`DEP-011`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011) (AI inventory) + [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) (AI BOM CycloneDX 1.6 *ml-bom*) | Provenance, integrity and *pinning* of *datasets* and models |
| Data handling requirements | Ch. 02 | Data security requirements |
| Access control and protection | Ch. 04 | Secure architecture, data classification |
| *Pinning* + list of approved *providers* | `DEP-013/014` + Policy 39 | Explicit fixed version; approved *providers* with contractual clauses |

**What SbD-ToE covers**

- Provenance and integrity of supply chain artefacts, applicable to *datasets*, models, MCP *tools* and embedded prompts (Ch. 05 §`DEP-011..014`).
- **AI BOM per *build*** in a standardised format (CycloneDX 1.6 *ml-bom*) — operationalises the *AI-BOM* that was suggested in the first version of this cross-check (Policy 39, Ch. 05 US-14).
- Data protection, classification and access control requirements (Ch. 02, Ch. 04).

**Residual gaps**

**Statistical quality, representativeness and bias detection/mitigation** remain problems of **data science and of the application domain**, not of application security. SbD-ToE does not prescribe *fairness* metrics, *debiasing* techniques or representativeness criteria — rightly so, since they vary by use case and fall within the remit of the AI/data teams.

**How to comply**

The *AI-BOM* that was suggested in earlier versions of this document **is already implemented** ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012), Policy 39, Ch. 05 US-14). What remains is to complement SbD-ToE with a data science *data governance* process — data lineage, *datasheets for datasets*, *data cards*, bias assessment — coordinated with the AI team.

---

### Article 11 and Annex IV - Technical documentation {#artigo-11-e-anexo-iv---documentação-técnica}

**Normative content**

Art. 11 requires technical documentation drawn up **before** the placing on the market and kept up to date, demonstrating conformity. Annex IV details the minimum index: general description of the system, development and design elements, monitoring and control, risk management, changes throughout the lifecycle, and the list of standards applied.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Technical and architectural description | Ch. 04 + `ARC-014/015` | Secure architecture documentation, including agentic patterns |
| Security requirements and measures | Ch. 02 + `REQ-AGN-001..004` | Requirements catalogue (including the agentic subset) |
| Development process | Ch. 06, Ch. 07 | Secure development, CI/CD with gates |
| Risk and change management | Ch. 03, Ch. 12 | Threat model + agentic playbook; monitoring and improvement |
| Inventory of components and models | Ch. 05 + [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) AI BOM + Policy 39 | List of components (Annex IV, point 2(a)) including models, datasets, *tools* and prompts |
| Operation under mandate | Policy 38 | Documented and versioned *mandate* per AI agent |

**What SbD-ToE covers**

- Documentation of architecture and security decisions (Ch. 04), including agentic patterns [`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014) and [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015).
- Requirements and measures per criticality level (Ch. 02), including the `REQ-AGN-*` requirements for AI agents.
- Evidence of the development process and pipeline (Ch. 06, Ch. 07).
- **AI BOM** as an auditable artefact that materialises part of the list of components required by Annex IV, point 2(a) ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012), Policy 39).
- The ***mandate*** of each AI agent as a traceable operational artefact (Policy 38) — it enters the Annex IV, point 2(b) index (development and design elements) whenever the system includes agents.

**Intentional gaps**

SbD-ToE does not generate documentation **in the formal structure of Annex IV** nor a normalised **model card**. Organising the artefacts according to the regulatory index is mapping work, not new technical production.

**How to comply**

It is suggested to build an "Annex IV index" pointing to the existing SbD-ToE artefacts (architecture, requirements, threat model, pipeline and testing evidence), complemented by a *model card* (purpose, training data, performance metrics, limitations) under the responsibility of the AI team.

---

### Article 12 and Article 19 - Recording of events (logging) and keeping of logs {#artigo-12-e-artigo-19---registo-de-eventos-logging-e-conservação-de-logs}

**Normative content**

Art. 12 requires the capability for **automatic recording of events** (logs) throughout the lifecycle, with a level of traceability appropriate to the purpose, enabling the identification of risk situations and supporting post-market monitoring. Art. 19 requires providers to **keep the logs** automatically generated, to the extent that they are under their control.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Logging "by design" | Ch. 12 | Observability, structured logging |
| Event traceability | Ch. 12 + [`OPS-011`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes) (AI/ML) + [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) (audit per *tool invocation*) | Auditable trail and correlation, with the agent identified by `agent_id` + `session_id` + `mandate_ref` |
| *Tool invocation audit* | [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) + Ch. 12 US-13 | Each *tool call* generates a structured *audit event* (with `intent_event_ref` at A2+) |
| Detection of *off-policy* and *jailbreak* | [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 30 §9.3 | Actionable signals linked to IR |
| Keeping and retention | Ch. 12 + `OPS-003` | Retention and immutability policies |

**What SbD-ToE covers**

- Structured logging and observability "by design" (Ch. 12).
- **Full audit per *tool invocation*** when there are AI agents ([`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012)) — each call generates an event with `timestamp`, `agent_id`, `session_id`, `mandate_ref`, `autonomy_level`, `tool`, `tool_version`, `args` (PII redacted), `intent_event_ref`, `outcome`, `external_effect`. Granular in a **complementary** (operational) dimension to that of the epistemic inference log required by Art. 12 — it does not replace it.
- Auditable trail and event correlation, with guidance on retention and immutability (Ch. 12).
- **Agentic operational telemetry** (Ch. 12 US-13) that sustains the evidential basis for Art. 72 (post-market monitoring) and Art. 73 (serious incidents).

**Residual gaps**

The *model output* schema (model version, relevant *features*, decision, confidence) remains **configurable per system** — it depends on the use case and on the balance with personal data protection. Ch. 12 fixes the *operational* schema (who invoked, under which mandate, on which resource); the *epistemic* schema (why this output) is declared per system.

**How to comply**

The operational layer is already implemented (`OPS-011..014` + Ch. 12 US-13). What remains is to declare the *model output* schema per system, ensuring retention aligned with the useful life and with GDPR requirements. The retention period should be documented as evidence for Art. 12/19.

---

### Article 13 - Transparency and provision of information to deployers {#artigo-13---transparência-e-prestação-de-informação-aos-utilizadores-implementadores}

**Normative content**

Art. 13 requires high-risk systems to be sufficiently transparent to enable *deployers* to interpret the output and use it appropriately, accompanied by **instructions for use** with the identity of the provider, characteristics, capabilities, limitations of performance, known risks and human oversight measures.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Documentation of capabilities and limitations | Ch. 02, Ch. 04, Policy 38 (mandate) | Requirements, architecture and *mandate* with `capabilities` + `scope` + `risk_residual` |
| Identity of the *provider* and *runtime* | Policy 38 (`agent_runtime` in the mandate) + [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) (list of *providers*) | Identity of the AI *provider* + *pinned* model version |
| Required human oversight | Ch. 02 §A0–A4 + Policy 38 | Autonomy level A0–A4 declared per use/context |

**What SbD-ToE covers**

- Documentary basis of requirements and architecture that feeds part of the instructions for use (Ch. 02, Ch. 04).
- The ***mandate*** (Policy 38) as a **structured source** of *capabilities*, *scope*, *autonomy_level*, *risk_residual* and oversight procedures — directly extractable into the *deployer*'s "instructions for use".

**Residual gaps**

**Performance metrics** (accuracy, precision, *recall*) and **levels of accuracy** continue to depend on the specific model and domain — to be declared by the AI team. SbD-ToE does not replace that work, but it has materially reduced what remains to be produced for the instructions for use.

**How to comply**

It is suggested to derive an "instructions for use" document from the ***mandate*** (Policy 38), from the artefacts of Ch. 04 (architecture, trust boundaries) and Ch. 06, complemented by the performance metrics and limitations provided by the AI team.

---

### Article 14 - Human oversight {#artigo-14---supervisão-humana}

> ⚡ **Refresh 2026-05-30.** The first version of this cross-check treated Art. 14 as largely outside AppSec ("the design of oversight mechanisms is an AI/product problem"). With the agentic layer introduced in 2026 — A0–A4, `REQ-AGN-*`, [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), Policy 38 — the **interruption (*stop/override*) and governance facet** became covered. **Oversight-as-understanding** (human judgement and the intervention UX) remains the domain of the AI/product team; the architectural *how* and the governance *when* already live in the manual.

**Normative content**

Art. 14 requires high-risk systems to be designed to allow **effective human oversight**, including the ability to understand the capacities and limitations, detect and interpret the output, decide not to use or to override the system, and interrupt its operation (*stop*).

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Define a proportionate oversight level | Ch. 02 §A0–A4 + [`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) | Five autonomy levels (A0 read-only → A4 autonomous); classification per context |
| Operational mandate with declared oversight | Policy 38 (mandate) + [`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) | *Owner*, *approver*, `review_cadence`, *kill-switch*, *intent audit sink* |
| Architectural interruption capability (*stop*) | [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) + [`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) (*kill-switch*) | Credential revocation + *runtime* termination + *namespace* isolation + on-call alert, within seconds |
| Conscious override of a destructive action | [`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) (*intent declaration*) + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (OOB approval) | The agent declares its intent before a destructive *tool call*; *out-of-band* human approval required at A2+ |
| Periodic exercise of the *stop* | Policy 38 + Policy 18 §9.3 | *Kill-switch* exercised in sandbox/staging (annually at A2, quarterly at A3, monthly at A4) with the timing recorded |
| Audit of *off-policy actions* | [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 30 §9.3 + Policy 16 §11.4 | Divergence between the declared `intent` and the actual action generates an actionable alert + enters IR |

**What SbD-ToE covers**

- **Normative model of oversight levels** (Ch. 02 §A0–A4). The choice of *human-in-the-loop* / *human-on-the-loop* / *autonomous* is declared explicitly per context, with promotion and demotion criteria; moving up a level requires operational evidence of the prerequisites.
- ***Mandate*** (Policy 38) — operationalises Art. 14 by declaring, for each agent in use, **who oversees**, **at what cadence**, **with which *kill-switch*** and **under which signed mandate**.
- **Architectural *kill-switch*** ([`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) + [`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) — it is not a symbolic button: it revokes OIDC credentials + terminates sessions + isolates the *namespace* + alerts on-call, with measured time. Exercised periodically according to the autonomy level.
- ***Intent declaration*** ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) — at A2+, before each destructive *tool call* the agent declares to the infrastructure *what it is going to do and why*; the gate cross-checks intent against the actual action a posteriori ([`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014)).
- ***Out-of-band* human approval** — outside the agent's channel (Slack, GitHub review, signed webhook), so that *prompt injection* in the main channel cannot "self-approve".

**Residual gaps**

The **UX of the human decision** (how the user interprets the output and decides to intervene) and the specification of the **cognitive oversight points** (when the system should ask for confirmation, what information to show) remain outside the AppSec scope — they are AI system design and human factors. SbD-ToE ensures that interruption is **implementable, exercised, audited and required by governance**; it does not design the oversight interface.

**How to comply**

Most of the technical work is now inside the manual: declare the A0–A4 level in the *mandate* (Policy 38), instrument an exercised *kill-switch* ([`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) and *intent declaration* ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) in line with [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), and configure [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) to detect divergence. The AI/product team complements this with the intervention UX and the cognitive oversight points. For high-risk systems with an agentic component, US-15 (Ch. 02) + US-16 (Ch. 04) constitute the operational checklist.

---

### Article 15 - Accuracy, robustness and cybersecurity {#artigo-15---exatidão-robustez-e-cibersegurança}

> 🎯 **Core of the cross-check.** It is in Art. 15 that SbD-ToE offers the strongest and most direct coverage. The cybersecurity of AI systems is, to a large extent, the central discipline of the manual applied to a new type of artefact (ML models and pipelines).

**Normative content**

Art. 15 requires high-risk systems to achieve an appropriate level of **accuracy, robustness and cybersecurity** and to perform consistently throughout the lifecycle. Paragraph 5 is explicit about the adversarial vector: systems must be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting vulnerabilities, and the technical measures must prevent, detect, respond to, resolve and control for attacks involving **manipulation of the training data set (*data poisoning*)**, **manipulation of pre-trained components used in training (*model poisoning*)**, **inputs designed to cause the model to make a mistake (*adversarial examples / model evasion*)**, **confidentiality attacks** and **model flaws (*model flaws*)**.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Identification of adversarial threats | Ch. 03 + [agentic playbook](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) | MITRE ATLAS + OWASP LLM Top 10 2025 already incorporated as active catalogues |
| Defence in depth and isolation | Ch. 04 ([`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)/[`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)) | Trust boundaries (incl. *agentic boundary*); agent as an isolated *principal* |
| Chain integrity (data/models) | Ch. 05 (`DEP-011..014`) + Policy 39 | Provenance + AI BOM + *pinning* + approved *providers* |
| Robustness testing and *red teaming* | Ch. 10 §C5 + Policy 19 §7 | Continuous *eval suites* (prompt regression, abuse corpus, *A/B*, drift) |
| Detection and response at *runtime* | Ch. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 30 §9 | Detection of *jailbreak* / *off-policy*; *audit per tool invocation* |
| Hardening of the inference service | Ch. 04, Ch. 09 + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) | Architecture, containers/runtime, ephemeral identity |

**What SbD-ToE covers**

- **Threat modelling** (Ch. 03), with the **agentic playbook** (DFD + MITRE ATLAS threat library + OWASP LLM Top 10 2025) already included as an active catalogue — not merely extensible.
- **Defensive architecture** (Ch. 04): trust boundaries (including the *agentic boundary* in [`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014) and the agent as a *principal* in [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)), segregation, input validation, limitation of the exposure of the inference service.
- **Supply chain integrity** (Ch. 05 `DEP-011..014`): provenance, AI BOM ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) CycloneDX 1.6 *ml-bom*), version *pinning* ([`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013) — mitigates `AML.T0109` *Supply Chain Rug Pull*), list of approved *providers* ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)).
- **Security testing** (Ch. 10 §C5 *eval suites*): prompt/skill regression tests, *abuse* / *red-team corpus* (LLM01-2025 prompt injection, LLM06-2025 excessive agency), *drift detection*, *A/B testing*.
- **Runtime monitoring** (Ch. 12 + `OPS-011..014`): anomaly detection, *model drift*, *audit per tool invocation* ([`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012)), *budget / runaway* ([`OPS-013`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013)), *jailbreak* / *off-policy actions* ([`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014)).
- **Runtime hardening** (Ch. 09 + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)): isolation of the inference service in containers; AI agent with ephemeral OIDC *workload identity* + minimum *scope* per *tool*.

**Intentional gaps**

SbD-ToE does not set **accuracy metrics** or regulatory performance thresholds (they are specific to the model and the use case). In the base version, it does not prescribe concrete adversarial techniques (*adversarial training*, ML-specific *input sanitisation*, LLM *output filtering*) - these are domain additions that the manual frames but does not impose, in order to preserve universality.

**How to comply**

It is suggested to: (1) extend the threat model (Ch. 03) with **MITRE ATLAS** and the **OWASP ML/LLM Top 10**; (2) add **adversarial robustness tests** and an **AI red teaming** programme to the test catalogue (Ch. 10); (3) treat the provenance of data and models as a critical supply chain (Ch. 05); (4) configure monitoring (Ch. 12) for *drift* and attack patterns; (5) declare the accuracy metrics obtained and the acceptable thresholds, in coordination with the AI team.

---

### Article 17 - Quality management system (QMS) {#artigo-17---sistema-de-gestão-da-qualidade-qms}

**Normative content**

Art. 17 requires providers to have a documented quality management system, covering the regulatory compliance strategy, design and development procedures, quality control, testing and validation, risk management, post-market monitoring and incident reporting.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Development procedures | Ch. 06, Ch. 07 (incl. US-19) | Secure development, CI/CD with gates, agents as *principals* in the pipeline |
| Quality control and validation | Ch. 10 §C5 (*eval suites*) + Ch. 11 | Tests, release gate, prompt regression |
| Risk management | Ch. 03 + agentic playbook | Threat modelling + MITRE ATLAS threat library |
| Governance and responsibilities | Ch. 14 + Policy 38 (mandates) + Policy 39 (AI BOM lifecycle) | RACI, policies, approvals; formal lifecycle for agents and the AI supply chain |
| Monitoring and incidents | Ch. 12 + `OPS-012..014` + Policy 30 §9 | Agentic monitoring + IR for *off-policy* / *jailbreak* |

**What SbD-ToE covers**

- Development and pipeline procedures with auditable gates (Ch. 06, Ch. 07), including AI agents as *principals* (US-19).
- Technical quality control and pre-release validation (Ch. 10, Ch. 11), including continuous *eval suites* for agents (§C5).
- Governance structure, roles and approvals (Ch. 14).
- **Formal governance lifecycle for AI agents** (Policy 38) — *mandate* with proposal → assessment → approval → activation → operation → review / revocation. Directly mappable to the QMS elements of Article 17(3) (procedures, data management systems, communication records).
- **Formal lifecycle for the AI *supply chain*** (Policy 39) — AI BOM format, *pinning*, approved list of *providers*, response to *upstream* incidents by class.

**Intentional gaps**

SbD-ToE provides the **operational components** of a technical QMS, but not its **formal and documentary structure** as required by Art. 17 (written procedures, management responsibilities, quality manual). This formalisation is documentary organisation work.

**How to comply**

It is suggested to map the SbD-ToE gates and processes (Ch. 06/07/10/11/14) to the elements of Art. 17, producing a QMS document that references these controls as evidence - reusing, where applicable, an existing **ISO/IEC 42001** system.

---

### Article 25 - Supply chain and responsibilities along the chain {#artigo-25---cadeia-de-fornecimento-e-responsabilidades-ao-longo-da-cadeia}

**Normative content**

Art. 25 deals with the distribution of responsibilities when several actors contribute to an AI system — upstream *providers*, distributors, importers, integrators, *deployers* — and requires contractual cooperation, sharing of the information necessary to fulfil the obligations, and handling of substantial changes that may reclassify the system.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| *Pinned* version of models and AI components | [`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013) | Explicit fixed version; no `latest` / ranges / dynamic aliases |
| List of approved AI *providers* | [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) + Policy 39 | Versioned list with `risk_classification`, `contract_ref`, critical clauses |
| AI BOM per *build* | [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) + Policy 39 | CycloneDX 1.6 *ml-bom* generated per *release* |
| Contractual clauses with *providers* | Ch. 14 US-21 + Policy 33 §10 | Clauses on retention, location, audit, notification, compliance |
| Response to *upstream* incidents | Policy 39 §7 | Triage by class (`AML.T0019` *data poisoning*, `AML.T0109` *rug pull*, `AML.T0110` *tool poisoning*, *provider outage*) |

**What SbD-ToE covers**

- **Materialisation of the AI supply chain** as an auditable inventory: *pinning*, list of approved *providers*, AI BOM per *release*.
- **Contractual clauses** specific to AI *providers* (Policy 33 §10) — data retention, training opt-out, location (GDPR Art. 44–49), *audit rights*, SLA for prior notification of changes, declaration of compliance with Art. 53/55 in the case of GPAI.
- **Response to *upstream* incidents** by class — `AML.T0019` *Publish Poisoned Datasets*, `AML.T0109` *AI Supply Chain Rug Pull*, `AML.T0110` *AI Agent Tool Poisoning*, *provider outage* — with specific *runbooks*.
- **Reclassification on material change** — Ch. 03 US-11 and Ch. 04 US-16 require a review of the *threat model* and of the architecture when the *provider* changes the model's major version or when the `tools_allowlist` changes.

**Residual gaps**

The **legal contractual definition** of responsibilities along the chain (who answers for what in the event of an incident, allocation of the SLA for notification to authorities) remains within the Legal scope — SbD-ToE provides the technical and operational structure, not the legal drafting.

**How to comply**

Operationally, it is already implemented (Policy 39 + `DEP-013/014` + Ch. 14 US-21). What remains is coordination with Legal to ensure that the contractual clauses aligned with Policy 33 §10 also satisfy the requirements of Art. 25 — in particular for systems in which the organisation is simultaneously *provider* and *deployer*.

---

### Article 26 - Obligations of *deployers* {#artigo-26---obrigações-dos-deployers}

**Normative content**

Art. 26 defines specific obligations of *deployers* of high-risk AI systems: use the system in accordance with the instructions for use, assign qualified human oversight, ensure appropriate input data, monitor the operation, keep the logs under their control (Art. 19), and cooperate with authorities.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Use in accordance with instructions; assigned oversight | Policy 38 (mandate with `owner`, `approver`, `autonomy_level`) | The *mandate* declares *who oversees*, *at what cadence*, *under which mandate* |
| Assignment of qualified oversight | Ch. 00 (AI Reliability Engineer note) + Policy 37 §11 | Composite function + mandatory literacy per *role* |
| Monitoring of the operation | Ch. 12 US-13 + `OPS-011..014` | Agentic telemetry in production |
| Keeping of logs (Art. 19) | Ch. 12 + `OPS-003` (retention) + [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) (audit per tool) | Complete *audit trail* under the *deployer*'s control |
| Communication with authorities | Ch. 12 + Ch. 14 + Policy 30 §9.3 + Policy 32 (IRP) | IR feeds notification to authorities |

**What SbD-ToE covers**

- **Mandate as a *deployer* artefact** (Policy 38) — when the organisation operates (rather than provides) a high-risk AI system, the *mandate* is the formal evidence of "how this system is used, under what oversight, with which *kill-switch*". Directly extractable for the Art. 26 audit.
- **Composite function for qualified oversight** (Ch. 00 *AI Reliability Engineer* note) — `appsec` + `devops` + `grc` under the mandate of the `CISO`, with mandatory literacy (Policy 37 §11).
- **Operational monitoring** (Ch. 12 US-13, `OPS-011..014`) — logs and signals under the *deployer*'s control, kept in accordance with policy (`OPS-003`).
- **Incident response** linked to notification to authorities (Ch. 12 + Policy 30 §9.3 + Policy 32) — *off-policy actions* and *jailbreak* in production enter the IR flow that feeds Art. 73.

**Residual gaps**

When the organisation is simultaneously *provider* and *deployer* (a common case in *first-party* development), the separation of obligations between the two roles becomes blurred — it is advisable to clarify internally (and contractually when there are sub-deployers) which role is assumed in each use.

**How to comply**

For uses in which the organisation is a *deployer*, the *mandate* (Policy 38) is the central artefact. A specific *template* for a *deployer mandate* is suggested, explicitly documenting the reference to the *provider* (`contract_ref` + [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)), the instructions for use received, and the alignment with the requirements of Art. 26.

---

### Article 72 - Post-market monitoring {#artigo-72---monitorização-pós-comercialização}

**Normative content**

Art. 72 requires a proportionate post-market monitoring system, with a documented plan, that collects and analyses data on the performance of the system throughout its lifetime, making it possible to evaluate continuous compliance.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Continuous telemetry collection | Ch. 12 + `OPS-011..014` + Ch. 12 US-13 | AI/ML observability + agentic-specific signals |
| Performance and degradation analysis | Ch. 12 + [`OPS-011`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes) | Detection of *drift*, anomalies, degradation of precision |
| *Audit per tool invocation* | [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) | *Post-mortem* reconstruction of any agentic session |
| *Token budget* and *runaway* | [`OPS-013`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013) | Detection of uncontrolled consumption and changes in efficiency |
| *Off-policy actions* and *jailbreak* | [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 30 §9.3 | Actionable signals linked to IR |
| Continuous improvement | Ch. 12 + Ch. 10 §C5 (*eval suites*) | Post-incident cycle feeds back into the offline *eval suite* |

**What SbD-ToE covers**

- Continuous collection and analysis of operational telemetry (Ch. 12), with complete agentic-specific signals (`OPS-011..014`).
- **Agentic telemetry** (Ch. 12 US-13) that materialises the evidential basis for the post-market monitoring plan: *tool invocation audit events*, *intent events*, *budget metrics*, *off-policy / jailbreak detection*.
- Detection of performance degradation and *model drift* (Ch. 12, [`OPS-011`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes)).
- **Feedback cycle for *eval suites*** (Ch. 10 §C5) — incidents detected in production feed the offline suite, strengthening future regression.

**Intentional gaps**

SbD-ToE does not define the **formal post-market monitoring plan** with the structure of Art. 72, nor the specific AI performance indicators to be reported to the authority.

**How to comply**

It is suggested to formalise a post-market monitoring plan based on the observability of Ch. 12, with *dashboards* for performance, *drift* and vulnerability status, and reassessment triggers that feed the Art. 9 cycle.

---

### Article 73 - Reporting of serious incidents {#artigo-73---comunicação-de-incidentes-graves}

**Normative content**

Art. 73 requires providers to report **serious incidents** to the market surveillance authorities, within defined deadlines — as a rule **not later than 15 days** after becoming aware; **not later than 10 days** in the event of the death of a person; and **not later than 2 days** in the event of a widespread infringement or of a serious and irreversible disruption of critical infrastructure (Article 3, point (49)(b)) — and to take corrective action.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Incident detection and response | Ch. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) (*jailbreak* / *off-policy*) + Policy 30 §9.3 | Detection, response and post-incident process; actionable agentic signals |
| Agentic-specific incident classes | Policy 16 §11.4 | *Off-policy action*, *intent-action divergence*, successful *prompt injection*, *kill-switch* failure, *credential exposure* |
| Response to *upstream* incidents | Policy 39 §7 | *Rug pull*, *dataset poisoning*, *tool poisoning*, *provider outage* |
| Escalation and responsibilities | Ch. 14 + Policy 38 | Roles and responsibilities; *owner* + *approver* declared in the *mandate* |
| Severity classification | Ch. 01, Ch. 12 | Impact criteria, classification |

**What SbD-ToE covers**

- Detection, response and post-incident process (Ch. 12).
- **Agentic-specific incident classes** defined (Policy 16 §11.4): *off-policy action*, *intent-action divergence*, successful *prompt injection* that resulted in an unauthorised *tool call*, *kill-switch* failure, *credential exposure*.
- **Response to *upstream* incidents** (Policy 39 §7) — when the incident originates at the model / dataset / MCP server *provider*, and not in internal operations.
- Escalation roles and responsibilities (Ch. 14, Policy 38).
- Impact criteria that support severity classification (Ch. 01, Ch. 12).

**Intentional gaps**

SbD-ToE does not set the AI Act **regulatory definition of "serious incident"**, nor the deadlines (15 days / 10 days / 2 days depending on severity), submission templates or the circuit to the competent authority. As with NIS2 and DORA, these fields are left configurable.

**How to comply**

It is suggested to parameterise the Ch. 12 runbook and incident schema with the typology and deadlines of Art. 73, and to configure the SIEM/ITSM exporters to generate the notification ready for submission to the market surveillance authority.

---

### General-purpose AI models - Articles 53 and 55 (GPAI) {#modelos-de-ia-de-finalidade-geral---artigos-53-e-55-gpai}

**Normative content**

Art. 53 requires **GPAI** providers to provide technical documentation of the model, information for downstream integrators, a policy to comply with copyright and a summary of the training data. For GPAI with **systemic risk**, Art. 55 adds the obligation of **adversarial evaluation (*adversarial testing* / *red teaming*)**, assessment and mitigation of systemic risks, reporting of serious incidents and ensuring **adequate cybersecurity of the model and of the physical infrastructure**.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Adversarial evaluation / *red teaming* | Ch. 10 §C5 + Policy 19 §7 + Ch. 03 agentic playbook | Continuous *eval suites* (prompt regression, *abuse corpus*, *A/B*, *drift*) + MITRE ATLAS threat library |
| Cybersecurity of the model and infrastructure | Ch. 04 ([`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)/[`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)), Ch. 08, Ch. 09 | Agentic architecture, IaC, containers/runtime |
| Protection of weights and artefacts | Ch. 05 (`DEP-011..014`) + Policy 39 + Ch. 04 | Integrity, provenance, AI BOM, *pinning*, access control |
| Monitoring and incidents | Ch. 12 + `OPS-011..014` + Policy 30 §9 | Detection of *off-policy* / *jailbreak* / *exfiltration* via tool |
| Contractual clauses for GPAI | Ch. 14 US-21 + Policy 33 §10 + [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) | Contractual declaration of compliance with Art. 53/55 by the *providers* |

**What SbD-ToE covers**

- **Continuous AI red teaming** materialised (Ch. 10 §C5 + Policy 19 §7) — not merely as a recommendation. *Eval suites* include an *abuse corpus* (LLM01-2025 *prompt injection*, LLM06-2025 *excessive agency*) with the cadence required at A4 (monthly).
- **Cybersecurity of the infrastructure** that serves the model (Ch. 04 incl. [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), Ch. 08, Ch. 09).
- **Integrity and access protection** for weights, *checkpoints* and *datasets* — now with an auditable AI BOM and required *pinning* (`DEP-012/013`, Policy 39). Response to `AML.T0109` *Supply Chain Rug Pull* documented in Policy 39 §7.
- **Monitoring and response** (Ch. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014)) — active detection of *jailbreak* (LLM01-2025) and *off-policy actions* in production; detection corpus updated according to the cadence of the *mandate*.
- **Contractual compliance declared by GPAI *providers*** ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014), Ch. 14 US-21, Policy 33 §10) — required in the *provider* approval process.

**Intentional gaps**

SbD-ToE does not prescribe the **GPAI technical documentation** (Annex XI/XII), the **copyright policy** or the **summary of the training data** - these are domain and legal obligations. The assessment of **systemic risks** (high-impact capabilities at scale) is likewise external to AppSec.

**How to comply**

It is suggested to: treat weights, *checkpoints* and *datasets* as supply chain assets with provenance and access control (Ch. 05); institute continuous AI red teaming (Ch. 10) aligned with MITRE ATLAS; apply infrastructure hardening (Ch. 04/08/09); and refer GPAI documentation, copyright and systemic risk assessment to the AI, legal and compliance teams.

---

### Prohibited practices and transparency (Articles 5 and 50) {#práticas-proibidas-e-transparência-artigos-5-e-50}

**Normative content**

Art. 5 prohibits a set of practices (e.g. harmful subliminal manipulation, *social scoring* by public bodies, certain real-time remote biometric identification). Art. 50 imposes transparency duties on limited-risk systems (informing people that they are interacting with AI; marking synthetic content / *deepfakes*).

**SbD-ToE coverage**

Both articles are **essentially legal and product-design in nature**, outside the technical-AppSec scope of SbD-ToE.

**Intentional gaps (by design)**

SbD-ToE does not determine the admissibility of a purpose (Art. 5) nor design the mechanisms of disclosure to the user (Art. 50). Technically, it can support **content provenance marking** (e.g. *watermarking*/content credentials) once that product decision is taken.

**How to comply**

The determination of prohibitions and the transparency duties must be led by legal and product. SbD-ToE comes in only for the **reliable technical implementation** of the chosen mechanisms (integrity of the marking, auditable record).

---

## PART II: SYNTHESIS AND REFERENCES {#parte-ii-síntese-e-referências}

### Synthesis of AI Act / SbD-ToE coverage {#síntese-da-cobertura-ai-act--sbd-toe}

The AI Act asks for AI systems that are **secure, robust, documented and capable of being overseen**, with provider responsibility throughout the entire lifecycle. SbD-ToE offers the **technical-operational core** of that effort: technical risk management (Ch. 01, 03), defensive architecture (Ch. 04), integrity of the data and model chain (Ch. 05), pipelines and quality gates (Ch. 06, 07, 11), testing and adversarial robustness (Ch. 10), logging and post-market monitoring (Ch. 12) and governance (Ch. 14).

The **strongest and most direct** coverage is in **Art. 15** (accuracy, robustness, cybersecurity) and its operational correlates (Art. 12 logging, Art. 72 monitoring, Art. 73 incidents, Art. 17 QMS) - this is where "implementing SbD-ToE" comes close to "complying with the AI Act".

The gaps observed **are not flaws in the model**, but **deliberate abstentions**: dimensions specific to the AI domain (data governance/bias, statistical accuracy, human oversight, transparency) and legal dimensions (risk classification, FRIA, conformity assessment, CE marking, prohibited practices). These require data science, ethics, product, legal and compliance teams - SbD-ToE provides them with the technical evidence, not the conformity judgement.

The result is consistent with the philosophy of the manual:

- **Today**, SbD-ToE makes it possible to build and operate the software of an AI system with security by design.
- **Tomorrow**, when the organisation has to comply with the AI Act, it connects the details - it extends the threat model to the adversarial vector (ATLAS), formalises the QMS (Art. 17), parameterises incidents (Art. 73) and post-market monitoring (Art. 72), and coordinates the data, oversight and transparency dimensions with the domain teams.

### Scope, roles and penalties {#âmbito-papéis-e-sanções}

The AI Act distinguishes **providers**, **deployers**, importers and distributors, with distinct obligations. The bulk of the technical obligations (and of the SbD-ToE coverage) falls on the **provider of a high-risk system**; the *deployer* has its own obligations (use in accordance with the instructions, human oversight, in certain cases FRIA - Art. 26, 27).

In terms of penalties (Art. 99), the regulation sets maximum tiers:

- **Prohibited practices (Art. 5)**: up to **€35 M** or **7%** of total worldwide annual turnover (whichever is higher).
- **Non-compliance with other obligations** (including those of the high-risk provider, Art. 16): up to **€15 M** or **3%**.
- **Incorrect, incomplete or misleading information** to notified bodies or authorities: up to **€7.5 M** or **1%**.
- For **GPAI** providers (Art. 101): up to **€15 M** or **3%**.

### References {#referências}

- **AI Act**: Regulation (EU) 2024/1689 (CELEX: [32024R1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)).
- **Art. 9** - Risk management system (lifecycle).
- **Art. 10** - Data and data governance (representativeness, bias).
- **Art. 11 and Annex IV** - Technical documentation.
- **Art. 12 / Art. 19** - Recording of events and keeping of logs.
- **Art. 13 / Art. 14** - Transparency to deployers and human oversight.
- **Art. 15** - Accuracy, robustness and cybersecurity (resilience to adversarial attacks).
- **Art. 17** - Quality management system.
- **Art. 72 / Art. 73** - Post-market monitoring and serious incidents.
- **Art. 53 / Art. 55** - GPAI obligations and GPAI with systemic risk.
- **Art. 99 / Art. 101** - Penalties regime.
- **ISO/IEC 42001** - Artificial intelligence management system.
- **ISO/IEC 23894** - AI risk management.
- **ISO/IEC 27090** (under development) - AI cybersecurity.
- **NIST AI Risk Management Framework (AI RMF 1.0)**.
- **MITRE ATLAS** - Adversarial Threat Landscape for Artificial-Intelligence Systems.
- **OWASP Machine Learning Security Top 10** and **OWASP Top 10 for LLM Applications**.

---

:::note Exceptions and control evidence

The AI Act, like NIS2 and DORA, benefits from a formal process of compliance exceptions. Cases in which a requirement is not applicable, or in which a temporary residual risk is accepted (e.g. an adversarial vector mitigated by compensation while the *retraining* is being prepared), must be documented, approved at the appropriate level and reviewed periodically.

Ch. 14 (Governance and Contracting) of SbD-ToE provides the necessary artefacts: exception register, risk acceptance criteria, approval chain and remediation plan. It should be noted that certain deviations **cannot be made exceptions** in the AI Act context - first and foremost, any use that falls within the prohibited practices of Art. 5. The existence of a formal exceptions process is not a sign of fragility: it is evidence of mature governance and of conscious control over the risk profile.

:::

---

**Version:** 1.0
**Date:** May 2026
**Next review:** November 2026
