---
id: intro
title: AI Act - Normative cross-check
description: Analysis of how SbD-ToE responds to the obligations of Regulation (EU) 2024/1689 (AI Act) - cybersecurity, record-keeping, human oversight, transparency, post-market monitoring and serious incidents of AI systems, with accuracy and robustness pending a future round
tags: [cross-check, ai-act, regulamento-ia, ia, machine-learning, robustez, ciberseguranca, gpai]
sidebar_position: 6
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/ai-act/01-intro.md
  source_sha256: 4064ab9435c67d5b74af8fa2e163a5d4e5af359b37734b855b7d7a1ba859ea34
  source_commit: cd59ce0074d2e282eb290ceeaea128a60266b266
  target_sha256: e256b700da06912e0fcffa39cb8fcced643b4beaf5cc3e7c5a33f53727f60cfe
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [ai_service_vendor, appsec_core, audit_trail, avaliacao, capacitacao, chapter_role, cycle_iteration, discipline, esquema_regime, eu_ai_deployer, eu_ai_fria, eu_ai_gpai_model, eu_ai_high_risk_system, eu_ai_human_oversight, eu_ai_instructions_for_use, eu_ai_literacy, eu_ai_post_market_monitoring, eu_ai_qms, eu_ai_risk_management_system, eu_ai_system, eu_ai_training_data, eu_ai_widespread_infringement, eu_biometric_identification, eu_ce_marking, eu_market_surveillance_authority, eu_notified_body, eu_placing_on_market, eu_reasonably_foreseeable_misuse, eu_startups, framework_source_corpus, gap_family, gdpr_pseudonymisation, layer, lifecycle_phase, llm, mcp, mcp_reading_programa, normative_empirical, papel_suporte, piso_limiar, piso_relacao, practitioner_manual, programme_line, provenance, requirement_runtime, role_juridico, role_tech_lead, sbdtoe_sbd, schema, slug_threat_modeling, traceability, trilho_formativo, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 687f80aa0544aa71e211cfe59e5efb5638ebf1d29fb833664cd4d8142c656575
  translated_at: 2026-09-28T09:11:46Z
  stamped_at: 2026-09-28T09:11:46Z
  reviewed_by: null
---

# AI Act: Normative cross-check

> For practical implementation, see the [SbD-ToE 4 AI Act Playbook](/sbd-toe/cross-check-normativo/ai-act/playbook).
>
> For universal application patterns, see the core chapters of SbD-ToE (01–14).
>
> The Manual's response to each obligation (covered, declared gap or out of scope) is summarised in [“What this Manual covers and what stays out”](#o-que-este-manual-cobre-e-o-que-fica-de-fora) and listed, obligation by obligation, in [Applicable requirements](./requisitos-aplicaveis#cobertura).

## Scope {#âmbito}

### 🤖 AI Act - Artificial Intelligence Regulation {#-ai-act---regulamento-de-inteligência-artificial}

The **AI Act** is **Regulation (EU) 2024/1689** (CELEX: [32024R1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)), the world's first horizontal legal framework dedicated to artificial intelligence. It entered into force on 1 August 2024 and applies in phases:

- **2 February 2025** - prohibited practices (Art. 5) and AI literacy (Art. 4; since 27 July 2026, as worded by Regulation (EU) 2026/1744). The exceptions are the new prohibitions in Article 5(1), first subparagraph, points (ba) and (bb), and paragraphs 1a and 1b of the same Article, inserted by Regulation (EU) 2026/1744, which apply from **2 December 2026** (Article 113, third paragraph, point (a)).
- **2 August 2025** - general-purpose AI models (GPAI, Chapter V), notifying authorities and notified bodies (Chapter III, Section 4), governance (Chapter VII) and penalties (Chapter XII), **with the exception of Article 101** (fines for providers of general-purpose AI models).
- **2 August 2026** - general application of the regulation (Article 113, second paragraph), including the transparency obligations of Art. 50 and Article 101; for systems generating synthetic content placed on the market before that date, Article 50(2) must be complied with by 2 December 2026 (Article 111(4)).
- **2 December 2027** - Chapter III, Sections 1 to 3 (with the exception of Article 6(5)), for **high-risk** AI systems in Annex III (Regulation (EU) 2026/1744, which amended Article 113).
- **2 August 2028** - high-risk AI systems covered by the product legislation in Annex I (Regulation (EU) 2026/1744).

> ℹ️ **Note (2026):** Regulation (EU) 2026/1744 («Digital Omnibus on AI»), published in OJ L of 24.7.2026 and in force since 27.7.2026, amended Article 113: the high-risk obligations (Chapter III, Sections 1–3) apply from **2 December 2027** (Annex III / Article 6(2)) and from **2 August 2028** (Annex I / Article 6(1)).

The AI Act adopts a **risk-based approach** with four tiers: **unacceptable** risk (prohibited, Art. 5), **high risk** (Art. 6 and Annexes I/III, subject to the bulk of the technical obligations), **limited** risk (a common designation; Art. 50 lays down transparency obligations for «certain AI systems») and **minimal** risk (no specific obligations beyond the horizontal ones, such as the AI literacy of Art. 4). On top of these tiers come specific rules for **GPAI** (Art. 53) and GPAI with **systemic risk** (Art. 55).

It is essential to frame the nature of the regulation: the AI Act is, first and foremost, **product safety and fundamental rights protection legislation** applied to AI systems, not an application security (AppSec) standard. However, the obligations for high-risk AI systems incorporate **substantial technical requirements** that intersect directly with SbD-ToE - in particular:

- **Art. 12 / Art. 19** - automatic recording of events (logging) and keeping of logs;
- **Art. 14** - human oversight;
- **Art. 15** - **cybersecurity** (including resilience against adversarial attacks); the accuracy and robustness required by the same Article are pending a future round;
- **Art. 50** - transparency for certain AI systems;
- **Art. 72** - post-market monitoring;
- **Art. 73** - reporting of serious incidents.

Articles 9 (risk management system) and 17 (quality management system) are outside the Manual's scope: they are management systems of the organisation, not requirements of the application. The Manual's controls serve as evidence for them.

In SbD-ToE, the AI Act is operationalised through the same technical disciplines that underpin any secure software - secure engineering (requirements, architecture, development, IaC, pipelines, testing), supply chain and provenance (dependencies, containers, SBOM), monitoring and response processes, and governance/contracting - now applied to the **lifecycle of AI systems** (datasets, models, training and inference pipelines, inference services).

> ⚖️ **Editorial note.**
> This section is an **operational synthesis** of the relevant articles of the AI Act, not a literal quotation of the regulation.
> It draws in particular on Articles 9 (risk management), 10 (data and data governance), 11 and Annex IV (technical documentation), 12 and 19 (records/logs), 13–14 (transparency and human oversight), 15 (accuracy, robustness, cybersecurity), 17 (QMS), 72 (post-market monitoring), 73 (serious incidents) and 53/55 (GPAI and systemic risk).

> ⚖️ **Note on technical references.**
> The AI Act sets essential requirements but defers the technical detail to **harmonised standards** (to be developed by CEN-CENELEC) and common specifications.
> Standards such as **ISO/IEC 42001** (AI management system), **ISO/IEC 23894** (AI risk management), **ISO/IEC 27090** (AI security, under development), the **NIST AI Risk Management Framework (AI RMF 1.0)**, **MITRE ATLAS** (adversarial tactics and techniques against ML), the **OWASP Machine Learning Security Top 10** and the **OWASP Top 10 for LLM Applications** are widely recognised and provide a solid basis for meeting the technical and procedural requirements.
> SbD-ToE treats these standards as **recommended good practice**, not as legal requirements in themselves.

## Regulatory Notice {#aviso-regulatório}

SbD-ToE covers the **technical "how"** of a good part of the high-risk obligations, but it **does not replace** the legal and conformity assessment dimensions of the AI Act. On the matters most often confused, the answer is as follows:

- **Risk classification** (Art. 6 and Annexes I/III): the legal determination of whether a system is high-risk is a compliance matter. The outcome is declared per application as context CTX-AIA-RE, with the legal qualification attached, and the floor entries of that context apply at any level L1–L3. The Manual's L3 level is not the same as high-risk.
- **Governance of training data and of validation and testing data** (Art. 10): representativeness, detection and mitigation of bias and the statistical quality of the data sets are **out of scope**, by programme decision: they are data science work. The provenance and integrity of the data sets (`DEP-011`) provide incidental evidence for them.
- **Transparency** (Arts. 13 and 50): Art. 50 is **covered** by two requirements added by the regime (CTX-AIA-RE-R01 and R02). For the instructions for use of Art. 13, the Manual provides evidence, and the drafting is the provider's. Out of scope is the disclosure of AI-generated text published on matters of public interest (Article 50(4), second subparagraph): it is an editorial decision, not an engineering one.
- **Human oversight** (Art. 14): paragraphs 1 to 4 are **covered** for any high-risk system, with or without agents, by `ARC-014` with the floor CTX-AIA-RE-P08. Out of scope are the specifics of **biometric identification systems** (Annex III, point 1): the records of Article 12(3) and the verification by two persons of Article 14(5). An application of that kind is developed with the Manual like any other, and biometrics as an authentication factor is in `AUT-012`.
- **Fundamental rights impact assessment (FRIA)** (Art. 27): an obligation of certain deployers: bodies governed by public law, private entities providing public services and deployers of the systems referred to in Annex III, point 5(b) and (c), for high-risk systems under Article 6(2) (with the exception of those in Annex III, point 2) (Article 27(1)). The FRIA belongs to the deployer; the Ch. 03 threat model (including LINDDUN) provides evidence for it. Only the notification of the result to the authority (Article 27(3)) is out of scope.
- **Conformity assessment** (Art. 43), involvement of **notified bodies**, **EU declaration of conformity** (Art. 47), **CE marking** (Art. 48) and **registration in the EU database** (Art. 49/71): out of scope.
- **Determination of prohibited practices** (Art. 5) and legal qualification of roles (provider, deployer, importer, distributor): out of scope. The technical safeguards that Article 5(1a) requires of generators of realistic images, video or audio are **covered** (floor entries CTX-AIA-RE-P09 and P10).

Legal judgement on these matters belongs to the compliance and legal teams and to the relationship with the competent authority. SbD-ToE provides the technical controls and the evidence; it does not issue the conformity judgement.

## What this Manual covers and what stays out {#o-que-este-manual-cobre-e-o-que-fica-de-fora}

SbD-ToE is centred on the application: requirements, architecture, code, dependencies, pipeline, deployment and operation of the software. For each AI Act obligation, the Manual answers in one of three categories, and no obligation is left unanswered:

- **Covers**, and says how: a catalogue requirement, a policy, a floor or a requirement added by the regime, or engineering evidence for a duty that sits on another plane.
- **Declared gap**: what the Manual does not cover by omission, with what is missing.
- **Out of scope**: what the Manual does not address, with the reason.

The full list, obligation by obligation, is generated from the coverage matrix and is in [Applicable requirements — What this Manual covers and what stays out](./requisitos-aplicaveis#cobertura). Where this page and the list differ, the list prevails.

**Out of scope, by programme decision:**
- Security of the entity as a whole (corporate network and administration channels, EDR, patching of operating systems and equipment, inventory and classification of all assets): the Manual is centred on the application.
- Risk management system (Article 9) and quality management system (Article 17): these are management systems of the organisation; the Manual's controls serve as evidence for them.
- Governance of training data and bias assessment (Article 10): this is data science work; the provenance and integrity of the data sets (`DEP-011`) provide only incidental evidence.
- Conformity assessment and drafting of the declaration of conformity: these belong to the product conformity plane, in the hands of the provider.
- Specifics of biometric identification systems (records of Article 12(3) and verification by two persons of Article 14(5)): the application is developed with the Manual like any other, and biometrics as an authentication factor is in `AUT-012`.

Declared gap pending the AISVS/SAIF round of AppSec Core: accuracy and robustness (Article 15). The technical documentation (Annex IV) has an [evidence map](./requisitos-aplicaveis#mapa-evidencia) on the generated page. AI comes in like any other topic; there is no separate AI manual.

---

## Cross-Check Matrix (summary) {#matriz-de-cross-check-resumo}

> ✏️ **Refresh 2026-09-27.** This table summarises the AI Act coverage matrix, which incorporates the *agentic release* (Ch. 02 §A0–A4, Ch. 03 agentic playbook, [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), `DEP-012..014`, `OPS-012..014`, Policy 38, Policy 39) and the floor entries and requirements of context CTX-AIA-RE. The «Residual gap» column records only declared gaps; what is out of scope is marked as such. The obligation-by-obligation answer is in [Applicable requirements](./requisitos-aplicaveis#cobertura).

| AI Act domain | Reference (article) | SbD-ToE coverage | Residual gap | Adaptation action |
|---|---|---|---|---|
| AI literacy | Art. 4 | Ch. 13 (training), Policy 37 §11 (matrix per *role*) | Partial: business staff who operate or use product AI systems; consideration of the context of use and of the persons targeted | Document completions of training tracks as evidence |
| Special categories of data to correct bias | Article 4a | `ENC-002`, `PRI-001`, `ACC-001..003`, `LOG-001`, `PRI-002`, `PRI-004` | Partial: limitation of re-use and pseudonymisation of these data sets; documentation per access; general prohibition on transmission to third parties; deletion as soon as the bias has been corrected; justification of strict necessity | The judgement of necessity (paragraph 1, point (a)) is out of scope |
| Risk management system | Art. 9 | Out of scope (programme decision): management system of the organisation | — | The artefacts of Ch. 01, 03 and 12 serve as evidence |
| Data and data governance | Art. 10 | Out of scope (programme decision): governance of training data and bias | — | [`DEP-011`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011) and [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) provide incidental evidence of provenance |
| Technical documentation | Art. 11, Annex IV | Ch. 02, Ch. 04 (architecture + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)), Ch. 05 ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) AI BOM), Ch. 06, Policy 38 (mandate) | Declared gaps per point of Annex IV (see the [evidence map](./requisitos-aplicaveis#mapa-evidencia)); adequacy of the performance metrics (point 4) pending the AISVS/SAIF round | Map SbD-ToE artefacts (including mandate + AI BOM) to the Annex IV index; the drafting is the provider's |
| Recording of events (logging) | Art. 12, Art. 19 | Ch. 12 (observability), [`OPS-011`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes) (AI/ML), [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) (audit per *tool invocation* with `mandate_ref`), Ch. 12 US-13 (agentic telemetry), Policy 30 §9 | — (*model output* schema configurable per system, with the minimums of the floor entries CTX-AIA-RE-P01 to P03 and P11; records of biometric identification, Article 12(3): out of scope) | Document the inference schema per system |
| Transparency to deployers | Art. 13 | Ch. 02, Ch. 04 (partial), Policy 38 (mandate as a structured source of *capabilities*, limitations and oversight) | Levels of accuracy and robustness in the instructions: declared gap, pending the AISVS/SAIF round of AppSec Core; intended purpose and description of the interface | Derive "instructions for use" from the mandate + Ch. 04/06 artefacts; the drafting is the provider's |
| Human oversight | Art. 14 ⚡ | [`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014) with the floor CTX-AIA-RE-P08 (any high-risk system); for agents, Ch. 02 §A0–A4 + `REQ-AGN-001..004` (mandate, level classification, *kill-switch*, *intent declaration*), Ch. 04 [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (OOB approval + architectural *kill-switch*), Policy 38 (mandate lifecycle) | — (Article 14(5), biometric identification: out of scope) | Oversight interface in any high-risk system (the concrete UX belongs to the product); *kill-switch*, *intent declaration* and OOB approval for agents |
| Accuracy, robustness and cybersecurity | Art. 15 | Ch. 03 agentic playbook + MITRE ATLAS, Ch. 04 ([`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)+[`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)), Ch. 05 (AI BOM), Ch. 10 §C5 (*eval suites*), Ch. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) (*jailbreak* / *off-policy*) | Accuracy and robustness: declared gap, pending the AISVS/SAIF round of AppSec Core; redundancy and mitigation of bias in feedback loops (Article 15(4), partial) | Await the round; until then, record the metrics obtained as evidence, without presenting them as compliance |
| Quality management system | Art. 17 | Out of scope (programme decision): management system of the organisation | — | The gates (Ch. 06, 07, 11, 14) and Policies 38/39 serve as evidence |
| Supply chain | Art. 25 | [`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013) (*pinning*), [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) (list of approved AI service vendors), Policy 39, Ch. 14 US-21 | Partial: the written agreement does not specify information, capabilities, technical access and assistance (Article 25(4)) | Review the clauses of Policy 33 §10 with the legal team |
| Obligations of the *deployer* | Art. 26 | Policy 38 (mandate + ownership), Ch. 02 §A0–A4, Ch. 12 US-13 (logs under the *deployer*'s control) | Operation in accordance with the provider's instructions in acquired systems; overseers of non-agentic systems; relevance and representativeness of input data; informing the provider and suspending non-agentic systems | Extend the mandate with specific obligations when the organisation is a *deployer* |
| Conformity and CE marking | Art. 43, 47–49 | — (DEP-014 records the conformity declared contractually by the AI service vendor; it is not the EU declaration of conformity of Art. 47, nor does it replace the conformity assessment and CE marking that fall to the provider of the system) | — (out of scope: conformity plane, in the hands of the provider) | Establish a GRC + legal swimlane for the assessment circuit |
| GPAI and systemic risk | Art. 53, Art. 55 | Ch. 03 playbook + Ch. 05 (AI BOM), Ch. 10 §C5 (*eval suites* + *red teaming*), Ch. 12 US-13 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014), Policy 19 §7, Policy 30 §9 | Partial: model evaluation with standardised protocols and documented adversarial testing (Article 55(1)(a)) | Annexes XI/XII drafted by the model provider, with evidence from the Manual; *copyright* policy and summary of training data out of scope (legal plane) |
| Post-market monitoring | Art. 72 | Ch. 12 (monitoring, *drift*), `OPS-011..014`, Ch. 12 US-13 + plan per system ([CTX-AIA-RE-R04](./requisitos-aplicaveis#acrescentos), integrated into Annex IV, point 9) | — | Apply R04 when the organisation is the provider |
| Serious incidents | Art. 73 | Ch. 12, Ch. 14, [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) (*off-policy* → IR), Policy 30 §9.3, Policy 16 §11.4 (agentic-specific incidents), Policy 32 §4.1 and [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) (definition and deadlines) | Partial: not altering the system in a way that affects the analysis of causes without first informing the authority (Article 73(6)) | Configure SIEM/ITSM exporters for the notification |
| Safeguards for realistic content generators | Article 5(1a) | `THR-008` and `ARC-014` with the floor entries CTX-AIA-RE-P09 and P10 (ART50 grade) | — (out of scope: judgement on the admissibility of the purpose, Article 5) | Threat model of the generated content, red-team and input and output filters |
| Transparency for certain AI systems | Art. 50 | CTX-AIA-RE-R01 (inform) and R02 (mark synthetic content), ART50 grade | — (out of scope: text on matters of public interest, Article 50(4), second subparagraph) | Declare the ART50 grade on the application and verify the notice and the marking in testing |
| Substantial modification | Article 43(4); Annex IV, point 2(f) | `ARC-009` with the floor CTX-AIA-RE-P11 | — | Classify and record each change; flag the substantial modification |
| Explanation to affected persons | Article 26(11); Art. 86 | CTX-AIA-RE-R03 + `OPS-011` | — | Record, per decision, the outcome and the main elements that determined it |
| Corrective actions and duty of information | Art. 20 | `DPL-005` (rollback), Policy 32 | Partial: withdrawal or recall of the system; informing distributors, deployers, the authorised representative and importers; joint investigation with the deployer | — |
| Documentation keeping | Art. 16, point (d); Art. 18 | Policy 06 §10 | Partial: no 10-year period for the documentation of high-risk AI systems | — |

---

## PART I: NORMATIVE ANALYSIS {#parte-i-análise-normativa}

### Article 4 - AI literacy {#artigo-4---literacia-em-ia}

**Normative content**

Art. 4, as worded by Regulation (EU) 2026/1744 (in force since 27 July 2026), provides: «Providers and deployers of AI systems shall take measures to support the development of AI literacy of their staff and other persons dealing with the operation and use of AI systems on their behalf, taking into account their technical knowledge, experience, education and training and the context the AI systems are to be used in, and considering the persons or groups of persons on whom the AI systems are to be used. This obligation does not require providers or deployers to guarantee any specific level of AI literacy of any individual.» (Article 4(1)). In the Manual's reading, this is an obligation of means. Between 2 February 2025 and 26 July 2026 the original wording applied, which required measures to ensure, «to their best extent», a «sufficient level of AI literacy».

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

**Declared gap (partial)**

The Manual covers the technical roles of the SDLC and the use of AI as a tool or agent, but not the business staff who operate or use product AI systems on behalf of the organisation, nor the consideration of the context of use and of the persons targeted. Article 4 does not require any specific level of literacy to be reached; individual competence assessment, where the organisation wants it, is work for HR and the training and upskilling function.

**How to comply**

Policy 37 §11 can be operationalised directly for the technical roles. Until the gap is closed in the Manual, the organisation includes on its own initiative the business staff who operate product AI systems and records the completions of the tracks as evidence for Art. 4.

---

### Article 9 - Risk management system {#artigo-9---sistema-de-gestão-de-risco}

**Normative content**

Art. 9 requires a **continuous and iterative** risk management system throughout the entire lifecycle of the high-risk AI system: identification and analysis of the known and reasonably foreseeable risks to health, safety and fundamental rights; estimation of the risks under intended use and under reasonably foreseeable misuse; adoption of appropriate risk management measures; and testing to identify the most appropriate measures.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Risk identification and analysis | Ch. 03 | Threat modelling (STRIDE, MITRE ATT&CK) + [agentic playbook](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) with MITRE ATLAS already included |
| Proportionality to risk | Ch. 01 + Ch. 02 §A0–A4 | L1–L3 classification + agentic autonomy levels A0–A4 ([`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) |
| Risk management measures | Ch. 02 | Requirements catalogue per level + `REQ-AGN-001..004` |
| Iterative and continuous evaluation | Ch. 12 | Continuous monitoring, improvement + `OPS-011..014` |

> ℹ️ **Note:** L3 is the Manual's risk classification; it is not equivalent to a high-risk AI system within the meaning of the AI Act (Article 6).

**What SbD-ToE covers**

- Structured threat identification through threat modelling (Ch. 03), with the **agentic playbook** already incorporated and MITRE ATLAS as an active catalogue (not merely extensible).
- Application criticality classification (Ch. 01), the basis for the proportionality of controls, **complemented by the autonomy levels A0–A4** for systems that include AI agents with *tool-use* ([`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)).
- Catalogue of security requirements and their measures (Ch. 02), including the agentic subset `REQ-AGN-001..004`.
- Continuous reassessment, in a cycle, with operational metrics (Ch. 12), including agentic-specific signals (`OPS-011..014`).

**Out of scope**

The risk management system of Article 9 (health, safety and fundamental rights throughout the lifecycle) is a management system of the organisation and is outside the Manual's scope by programme decision. The threat model, classification and monitoring described above serve as evidence for it; the Manual does not prescribe the analysis of risks to health, safety and fundamental rights (e.g., risk of discrimination, societal impact).

**How to comply**

The organisation runs the risk management system within its own framework (e.g., **NIST AI RMF** or **ISO/IEC 23894**) and references as evidence the Ch. 03 threat model, which already uses **MITRE ATLAS** for the adversarial vector, and the Ch. 12 monitoring.

---

### Article 10 - Data and data governance {#artigo-10---dados-e-governação-de-dados}

**Normative content**

Art. 10 requires that the training data sets, validation data sets and testing data sets be subject to appropriate data governance practices: relevance, representativeness, freedom from errors and completeness to the best extent possible, appropriate statistical properties, and examination of possible biases likely to affect health, safety or fundamental rights (Article 10(2) and (3)). With Regulation (EU) 2026/1744, the exceptional processing of special categories of personal data for bias detection and correction moved from Article 10(5) (deleted) to the new Article 4a.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Data provenance and integrity | Ch. 05 + [`DEP-011`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011) (AI inventory) + [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) (AI BOM CycloneDX 1.6 *ml-bom*) | Provenance, integrity and *pinning* of *datasets* and models |
| Data handling requirements | Ch. 02 | Data security requirements |
| Access control and protection | Ch. 04 | Secure architecture, data classification |
| *Pinning* + list of approved AI service vendors | `DEP-013/014` + Policy 39 | Explicit fixed version; approved AI service vendors with contractual clauses |

**What SbD-ToE covers**

- Provenance and integrity of supply chain artefacts, applicable to *datasets*, models, MCP *tools* and embedded prompts (Ch. 05 §`DEP-011..014`).
- **AI BOM per *build*** in a standardised format (CycloneDX 1.6 *ml-bom*) — operationalises the *AI-BOM* that was suggested in the first version of this cross-check (Policy 39, Ch. 05 US-14).
- Data protection, classification and access control requirements (Ch. 02, Ch. 04).

**Out of scope**

The governance of training data and of validation and testing data (statistical quality, representativeness, detection and mitigation of bias) is outside the Manual's scope by programme decision: it is data science work. The Manual does not prescribe *fairness* metrics, *debiasing* techniques or representativeness criteria; the provenance and integrity of the data sets (`DEP-011`, `DEP-012`) provide incidental evidence for it.

**Article 4a: partial coverage**

The exceptional processing of special categories of personal data to correct bias (Article 4a) has partial coverage: there is encryption at rest, access control with logging, and a retention period with verifiable deletion (`ENC-002`, `ACC-001`, `ACC-003`, `LOG-001`, `PRI-002`). Missing are the technical limitations on the re-use of these data sets and their pseudonymisation, documentation per access and the duty of confidentiality of those who access them, the general prohibition on transmission to third parties, deletion as soon as the bias has been corrected and the recording of the justification of strict necessity. The judgement of necessity (paragraph 1, point (a)) is out of scope: it is a data science and data protection decision.

**How to comply**

The *AI-BOM* that was suggested in earlier versions of this document **is already implemented** ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012), Policy 39, Ch. 05 US-14). The governance of training data (data lineage, *datasheets for datasets*, *data cards*, bias assessment) follows the organisation's data science process, outside the Manual.

---

### Article 11 and Annex IV - Technical documentation {#artigo-11-e-anexo-iv---documentação-técnica}

**Normative content**

Art. 11 requires technical documentation drawn up **before** placing on the market or putting into service and kept up to date, demonstrating compliance; since Regulation (EU) 2026/1744, SMEs (including start-ups) and small mid-cap enterprises may provide the elements of Annex IV in a simplified manner, using a Commission form (Article 11(1), second subparagraph). Annex IV sets out the minimum contents: general description of the system, development and design elements, monitoring and control, risk management, changes over the lifecycle, and the list of standards applied.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Technical and architectural description | Ch. 04 + `ARC-014/015` | Secure architecture documentation, including agentic patterns |
| Security requirements and measures | Ch. 02 + `REQ-AGN-001..004` | Requirements catalogue (including the agentic subset) |
| Development process | Ch. 06, Ch. 07 | Secure development, CI/CD with gates |
| Risk and change management | Ch. 03, Ch. 12 | Threat model + agentic playbook; monitoring and improvement |
| Inventory of components and models | Ch. 05 + [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) AI BOM + Policy 39 | Evidence for Annex IV (point 2(a) and (c): third-party systems/tools and component architecture; point 1(c): software versions) including models, datasets, *tools* and prompts |
| Operation under mandate | Policy 38 | Documented and versioned *mandate* per AI agent |

**What SbD-ToE covers**

- Documentation of architecture and security decisions (Ch. 04), including agentic patterns [`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014) and [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015).
- Requirements and measures per criticality level (Ch. 02), including the `REQ-AGN-*` requirements for AI agents.
- Evidence of the development process and pipeline (Ch. 06, Ch. 07).
- **AI BOM** as an auditable artefact that materialises part of the list of components required by Annex IV, point 2(a) ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012), Policy 39).
- The ***mandate*** of each AI agent as a traceable operational artefact (Policy 38) — it enters the Annex IV, point 2(b) index (development and design elements) whenever the system includes agents.

**Declared gaps and out of scope**

SbD-ToE does not generate the documentation **in the formal structure of Annex IV** nor a standardised **model card**: the drafting is the provider's, and the Manual provides the engineering evidence. The [evidence map](./requisitos-aplicaveis#mapa-evidencia) on the generated page links each point of Annex IV to the artefacts and lists the gaps per point. The adequacy of the performance metrics (Annex IV, point 4) is a declared gap, pending the AISVS/SAIF round of AppSec Core. Points 2(d) and 5 refer to Articles 10 and 9, which are out of scope, as are the list of applied standards and the EU declaration (points 7 and 8). The monitoring plan (point 9) and the pre-determined changes (point 2(f)) are covered by CTX-AIA-RE-R04 and by the floor CTX-AIA-RE-P11.

**How to comply**

It is suggested to build an "Annex IV index" pointing to the existing SbD-ToE artefacts (architecture, requirements, threat model, pipeline and test evidence), complemented by a *model card* (purpose, training data, performance metrics, limitations) drafted by the provider; the performance metrics do not yet have a criterion in the Manual (AISVS/SAIF round).

---

### Article 12 and Article 19 - Recording of events (logging) and keeping of logs {#artigo-12-e-artigo-19---registo-de-eventos-logging-e-conservação-de-logs}

**Normative content**

Art. 12 requires the capability for **automatic recording of events** (logs) throughout the lifecycle, with a level of traceability appropriate to the intended purpose, making it possible to identify risk situations and support post-market monitoring. Art. 19 requires providers to **keep the logs** automatically generated, to the extent that they are under their control, «for a period appropriate to the intended purpose of the high-risk AI system, of at least six months» (Article 19(1)); Article 26(6) imposes the same minimum on deployers.

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
- **Full audit per *tool invocation*** when AI agents are present ([`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012)) — each call generates an event with `timestamp`, `agent_id`, `session_id`, `mandate_ref`, `autonomy_level`, `tool`, `tool_version`, `args` (PII redacted), `intent_event_ref`, `outcome`, `external_effect`. Granular in a **complementary** (operational) dimension to the recording of inference events that each system must define to comply with Art. 12 — it does not replace it.
- Auditable trail and event correlation, with guidance on retention and immutability (Ch. 12).
- **Agentic operational telemetry** (Ch. 12 US-13) that underpins the evidence base for Art. 72 (post-market monitoring) and Art. 73 (serious incidents).
- **Floor entries of context CTX-AIA-RE**: in high-risk systems, and at any level, AI/ML observability (`OPS-011`, floor P01), audit per *tool invocation* when there are agents (`OPS-012`, floor P02) and retention of logs for at least six months, with no exception below the legal floor (`OPS-003`, floor P03).

**Configuration per system and out of scope**

The *model output* schema (model version, relevant *features*, decision, confidence) remains **configurable per system**, with two minimums: the record that makes it possible to identify substantial modifications (floor CTX-AIA-RE-P11) and, when an Annex III system supports decisions about people, the outcome and the main elements of each decision (CTX-AIA-RE-R03). Ch. 12 fixes the *operational* schema (who invoked, under which mandate, on which resource); the *epistemic* schema (why this output) is declared per system. The records specific to biometric identification (Article 12(3)) are out of scope.

**How to comply**

The operational layer is already implemented (`OPS-011..014` + Ch. 12 US-13). What remains is to declare the *model output* schema per system, ensuring retention for a period appropriate to the intended purpose of the system, of at least six months (Articles 19(1) and 26(6)), and compatible with the GDPR. Document the retention period as evidence for Art. 12/19.

---

### Article 13 - Transparency and provision of information to deployers {#artigo-13---transparência-e-prestação-de-informação-aos-utilizadores-implementadores}

**Normative content**

Art. 13 requires high-risk AI systems to be sufficiently transparent to enable deployers to interpret and use the output appropriately, accompanied by **instructions for use** with the identity and contact details of the provider, characteristics, capabilities, performance limitations, known risks and human oversight measures.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Documentation of capabilities and limitations | Ch. 02, Ch. 04, Policy 38 (mandate) | Requirements, architecture and *mandate* with `capabilities` + `scope` + `risk_residual` |
| Identity of the AI service vendor and *runtime* | Policy 38 (`agent_runtime` in the mandate) + [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) (list of AI service vendors) | Identity of the AI service vendor + *pinned* model version |
| Required human oversight | Ch. 02 §A0–A4 + Policy 38 | Autonomy level A0–A4 declared per use/context |

**What SbD-ToE covers**

- Documentary basis of requirements and architecture that feeds part of the instructions for use (Ch. 02, Ch. 04).
- The ***mandate*** (Policy 38) as a **structured source** of *capabilities*, *scope*, *autonomy_level*, *risk_residual* and oversight procedures — directly extractable into the *deployer*'s "instructions for use".

**Declared gaps**

The declaration of the levels of accuracy and robustness in the instructions for use (Article 13(3)(b)(ii)) is a declared gap, pending the AISVS/SAIF round of AppSec Core. The matrix also declares the intended purpose and the description of the interface as gaps. The drafting of the instructions is the provider's; the Manual provides the evidence, and the interpretation of the output is supported by the minimum oversight of `ARC-014` (floor CTX-AIA-RE-P08).

**How to comply**

It is suggested to derive an "instructions for use" document from the ***mandate*** (Policy 38) and from the artefacts of Ch. 04 (architecture, trust boundaries) and Ch. 06, complemented by the performance metrics and limitations that the provider declares; until the AISVS/SAIF round, those metrics have no criterion in the Manual.

---

### Article 14 - Human oversight {#artigo-14---supervisão-humana}

> ⚡ **Refresh 2026-09-27.** The first version of this cross-check treated Art. 14 as largely outside AppSec. With the agentic layer — A0–A4, `REQ-AGN-*`, [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), Policy 38 — and the floor CTX-AIA-RE-P08, paragraphs 1 to 4 of Art. 14 are **covered** for any high-risk system, with or without agents. The oversight interface is a requirement of the Manual; the concrete design of the UX that meets it belongs to the product.

**Normative content**

Art. 14 requires high-risk AI systems to be designed to enable **effective human oversight**, including the ability to understand capabilities and limitations, detect and interpret the output, decide not to use or to override the system, and interrupt its operation (*stop*).

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Oversight interface in any high-risk system | [`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014) + floor CTX-AIA-RE-P08 | Understand capabilities and limitations, detect anomalies, interpret the output, decide not to use it or override it, stop the system; warning to those who oversee about automation bias |
| Define a proportionate oversight level | Ch. 02 §A0–A4 + [`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) | Five autonomy levels (A0 read-only → A4 autonomous); classification per context |
| Operational mandate with declared oversight | Policy 38 (mandate) + [`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) | *Owner*, *approver*, `review_cadence`, *kill-switch*, *intent audit sink* |
| Architectural interruption capability (*stop*) | [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) + [`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) (*kill-switch*) | Credential revocation + *runtime* termination + *namespace* isolation + on-call alert, within seconds |
| Conscious override of a destructive action | [`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) (*intent declaration*) + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (OOB approval) | The agent declares its intent before a destructive *tool call*; *out-of-band* human approval required at A2+ |
| Periodic exercise of the *stop* | Policy 38 + Policy 18 §9.3 | *Kill-switch* exercised in sandbox/staging (annual at A2, quarterly at A3, monthly at A4: the Manual's cadences) with a recorded timer |
| Audit of *off-policy actions* | [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 30 §9.3 + Policy 16 §11.4 | Divergence between the declared `intent` and the actual action generates an actionable alert + enters IR |

**What SbD-ToE covers**

- **Normative model of oversight levels** (Ch. 02 §A0–A4). The choice of *human-in-the-loop* / *human-on-the-loop* / *autonomous* is declared explicitly per context, with promotion and demotion criteria; moving up a level requires operational evidence of the prerequisites.
- ***Mandate*** (Policy 38) — operationalises Art. 14 by declaring, for each agent in use, **who oversees**, **at what cadence**, **with which *kill-switch*** and **under which signed mandate**.
- **Architectural *kill-switch*** ([`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) + [`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) — it is not a symbolic button: it revokes OIDC credentials + terminates sessions + isolates the *namespace* + alerts on-call, with measured time. Exercised periodically according to the autonomy level.
- ***Intent declaration*** ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) — at A2+, before each destructive *tool call* the agent declares to the infrastructure *what it is going to do and why*; the gate cross-checks intent against the actual action a posteriori ([`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014)).
- ***Out-of-band* human approval** — outside the agent's channel (Slack, GitHub review, signed webhook), so that *prompt injection* in the main channel cannot "self-approve".

**Systems without agents and out of scope**

Policy 38 and `REQ-AGN` apply to agents with tool use. For high-risk systems without agents, the floor CTX-AIA-RE-P08 elevates `ARC-014` at any level: the oversight interface makes it possible to understand the capabilities and limitations of the system, detect anomalies, interpret the output, decide not to use it or override it and stop the system, and those who oversee are warned about automation bias. In the coverage matrix, paragraphs 1 to 4 of Art. 14 are covered. The concrete design of the UX (what information to show, when to ask for confirmation) belongs to the product; the requirement that this UX must meet belongs to the Manual.

Verification by two persons before a decision based on biometric identification (Article 14(5)) is out of scope, along with the other specifics of those systems.

**How to comply**

Most of the technical work is now inside the manual: declare the A0–A4 level in the *mandate* (Policy 38), instrument an exercised *kill-switch* ([`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) and *intent declaration* ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) in line with [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), and configure [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) to detect divergence. For systems without agents, `ARC-014` applies with the scope of the floor P08, and the product team designs the UX that meets it. For high-risk AI systems with an agentic component, US-15 (Ch. 02) + US-16 (Ch. 04) make up the operational checklist.

---

### Article 15 - Accuracy, robustness and cybersecurity {#artigo-15---exatidão-robustez-e-cibersegurança}

> 🎯 **Core of the cross-check.** It is in the cybersecurity of Art. 15 that SbD-ToE offers its strongest and most direct coverage. The cybersecurity of AI systems is, to a large extent, the manual's central discipline applied to a new type of artefact (ML models and pipelines). The accuracy and robustness required by the same Article are pending a future round.

**Normative content**

Art. 15 requires high-risk AI systems to achieve an appropriate level of **accuracy, robustness and cybersecurity** and to perform consistently throughout their lifecycle. Paragraph 5 is explicit about the adversarial vector: systems must be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting vulnerabilities, and the technical measures must prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (**data poisoning**, *data poisoning*) or pre-trained components used in training (**model poisoning**, *model poisoning*), inputs designed to cause the AI model to make a mistake (**adversarial examples or model evasion**, *adversarial examples / model evasion*), **confidentiality attacks** or **model flaws** — measures to be included «where appropriate» (Article 15(5), third subparagraph).

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Identification of adversarial threats | Ch. 03 + [agentic playbook](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) | MITRE ATLAS + OWASP LLM Top 10 2025 already incorporated as active catalogues |
| Defence in depth and isolation | Ch. 04 ([`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)/[`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)) | Trust boundaries (incl. *agentic boundary*); agent as an isolated *principal* |
| Chain integrity (data/models) | Ch. 05 (`DEP-011..014`) + Policy 39 | Provenance + AI BOM + *pinning* + approved AI service vendors |
| Robustness testing and *red teaming* | Ch. 10 §C5 + Policy 19 §7 | Continuous *eval suites* (prompt regression, abuse corpus, *A/B*, drift) |
| Detection and response at *runtime* | Ch. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 30 §9 | Detection of *jailbreak* / *off-policy*; *audit per tool invocation* |
| Hardening of the inference service | Ch. 04, Ch. 09 + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) | Architecture, containers/runtime, ephemeral identity |

**What SbD-ToE covers**

- **Threat modelling** (Ch. 03), with the **agentic playbook** (DFD + MITRE ATLAS threat library + OWASP LLM Top 10 2025) already included as an active catalogue — not merely extensible.
- **Defensive architecture** (Ch. 04): trust boundaries (including the *agentic boundary* in [`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014) and the agent as a *principal* in [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)), segregation, input validation, limitation of the exposure of the inference service.
- **Supply chain integrity** (Ch. 05 `DEP-011..014`): provenance, AI BOM ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) CycloneDX 1.6 *ml-bom*), version *pinning* ([`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013) — mitigates `AML.T0109` *Supply Chain Rug Pull*), list of approved AI service vendors ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)).
- **Security testing** (Ch. 10 §C5 *eval suites*): prompt/skill regression tests, *abuse* / *red-team corpus* (LLM01-2025 prompt injection, LLM06-2025 excessive agency), *drift detection*, *A/B testing*.
- **Runtime monitoring** (Ch. 12 + `OPS-011..014`): anomaly detection, *model drift*, *audit per tool invocation* ([`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012)), *budget / runaway* ([`OPS-013`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013)), *jailbreak* / *off-policy actions* ([`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014)).
- **Runtime hardening** (Ch. 09 + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)): isolation of the inference service in containers; AI agent with ephemeral OIDC *workload identity* + minimum *scope* per *tool*.

**Declared gap**

Accuracy and robustness (levels, parameters and metrics; Article 15(1) and (3)) are a declared gap, pending the AISVS/SAIF round of AppSec Core. The cybersecurity of Article 15(5) is covered. Of paragraph 4, *fallback*, *fail-secure* and fail-closed output validation are in place; missing are redundancy and fail-safe plans for performance, and the mitigation of bias in feedback loops of systems that continue to learn. *Adversarial training* is not prescribed in the base version; content-safety filters on input and output are required for realistic content generators (floor CTX-AIA-RE-P10).

**How to comply**

It is suggested to: (1) extend the threat model (Ch. 03) with **MITRE ATLAS** and the **OWASP ML/LLM Top 10**; (2) add **adversarial robustness tests** and an **AI red teaming** programme to the test catalogue (Ch. 10); (3) treat data and model provenance as a critical supply chain (Ch. 05); (4) configure monitoring (Ch. 12) for *drift* and attack patterns; (5) record the accuracy metrics obtained as evidence, without presenting them as compliance, until the AISVS/SAIF round.

---

### Article 17 - Quality management system (QMS) {#artigo-17---sistema-de-gestão-da-qualidade-qms}

**Normative content**

Art. 17 requires providers of high-risk AI systems to have a documented quality management system (whose implementation, since Regulation (EU) 2026/1744, «shall be proportionate to the size of the provider’s organisation», without lowering the degree of rigour required — Article 17(2)), covering compliance strategy, design and development procedures, quality control, testing and validation, risk management, post-market monitoring and incident reporting.

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
- **Formal governance lifecycle for AI agents** (Policy 38) — *mandate* with proposal → assessment → approval → activation → operation → review / revocation. It serves as evidence for elements of the QMS in Article 17(1) (e.g., the record-keeping of point (k)).
- **Formal lifecycle for the AI *supply chain*** (Policy 39) — AI BOM format, *pinning*, approved list of AI service vendors, response to *upstream* incidents by class.

**Out of scope**

The quality management system of Article 17 is a management system of the organisation and is outside the Manual's scope by programme decision. The components described above serve as evidence for it: the matrix records them as engineering evidence for design, development, reporting of serious incidents, record-keeping and accountability (Article 17(1), points (b), (c), (i), (k) and (m)).

**How to comply**

An organisation that has to maintain the QMS can reference the SbD-ToE gates and processes (Ch. 06/07/10/11/14) as evidence, re-using, where applicable, an existing **ISO/IEC 42001** system.

---

### Article 25 - Supply chain and responsibilities along the chain {#artigo-25---cadeia-de-fornecimento-e-responsabilidades-ao-longo-da-cadeia}

**Normative content**

Art. 25 (amended by Regulation (EU) 2026/1744) deals with responsibilities along the AI value chain: a distributor, importer, deployer or other third party is considered a provider, with the obligations of Article 16, if it puts its name or trademark on a high-risk AI system, makes a substantial modification to it or modifies its intended purpose in such a way that it becomes high-risk (paragraph 1); the initial provider must then cooperate with the new providers (paragraph 2); and the provider of a high-risk AI system and the third party that supplies «an AI system, AI model, tools, services, components, or processes» used or integrated in it must, «by written agreement», specify the necessary information, capabilities, technical access and assistance (paragraph 4). Non-compliance with paragraphs 2 and 4 is now subject to fines (Article 99(4), point (da)).

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| *Pinned* version of models and AI components | [`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013) | Explicit fixed version; no `latest` / ranges / dynamic aliases |
| List of approved AI service vendors | [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) + Policy 39 | Versioned list with `risk_classification`, `contract_ref`, critical clauses |
| AI BOM per *build* | [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) + Policy 39 | CycloneDX 1.6 *ml-bom* generated per *release* |
| Contractual clauses with AI service vendors | Ch. 14 US-21 + Policy 33 §10 | Clauses on retention, location, audit, notification, compliance |
| Response to *upstream* incidents | Policy 39 §7 | Triage by class (`AML.T0019` *data poisoning*, `AML.T0109` *rug pull*, `AML.T0110` *tool poisoning*, *provider outage*) |

**What SbD-ToE covers**

- **Materialisation of the AI supply chain** as an auditable inventory: *pinning*, list of approved AI service vendors, AI BOM per *release*.
- **Contractual clauses** specific to AI service vendors (Policy 33 §10) — data retention, training opt-out, location (GDPR Art. 44–49), *audit rights*, SLA for prior notification of changes, declaration of compliance with Art. 53/55 in the case of GPAI.
- **Response to *upstream* incidents** by class — `AML.T0019` *Publish Poisoned Datasets*, `AML.T0109` *AI Supply Chain Rug Pull*, `AML.T0110` *AI Agent Tool Poisoning*, *provider outage* — with specific *runbooks*.
- **Reclassification on material change** — Ch. 03 US-11 and Ch. 04 US-16 require a review of the *threat model* and of the architecture when the AI service vendor changes the model's major version or when the `tools_allowlist` changes.

**Declared gap (partial)**

The clauses of Policy 33 §10 do not yet specify the information, capabilities, technical access and assistance that Article 25(4) requires in the written agreement. The qualification of who becomes a provider (paragraph 1) is out of scope: it is a legal qualification. The legal drafting of responsibilities along the chain belongs to the legal team; SbD-ToE provides the technical and operational structure.

**How to comply**

The operational basis exists (Policy 39 + `DEP-013/014` + Ch. 14 US-21). What remains is to complete the clauses with the content of Article 25(4), in coordination with the legal team — in particular for systems in which the organisation is both *provider* and *deployer*.

---

### Article 26 - Obligations of *deployers* {#artigo-26---obrigações-dos-deployers}

**Normative content**

Art. 26 sets out specific obligations for deployers of high-risk AI systems: use the system in accordance with the instructions for use, assign qualified human oversight, ensure appropriate input data, monitor operation, keep the logs under their control for at least six months (Article 26(6)), and cooperate with authorities.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Use in accordance with instructions; assigned oversight | Policy 38 (mandate with `owner`, `approver`, `autonomy_level`) | The *mandate* declares *who oversees*, *at what cadence*, *under which mandate* |
| Assignment of qualified oversight | Ch. 00 (AI Reliability Engineer note) + Policy 37 §11 | Composite function + mandatory literacy per *role* |
| Monitoring of the operation | Ch. 12 US-13 + `OPS-011..014` | Agentic telemetry in production |
| Keeping of logs (Article 26(6)) | Ch. 12 + `OPS-003` (retention) + [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) (audit per tool) | Complete *audit trail* under the *deployer*'s control |
| Communication with authorities | Ch. 12 + Ch. 14 + Policy 30 §9.3 + Policy 32 (IRP) | IR feeds notification to authorities |

**What SbD-ToE covers**

- **Mandate as a *deployer* artefact** (Policy 38) — when the organisation operates (rather than supplies) a high-risk AI system, the *mandate* is the formal evidence of "how this system is used, under what oversight, with which *kill-switch*". Directly extractable for an Art. 26 audit.
- **Composite function for qualified oversight** (Ch. 00 *AI Reliability Engineer* note) — `appsec` + `devops` + `grc` under the mandate of the `CISO`, with mandatory literacy (Policy 37 §11).
- **Operational monitoring** (Ch. 12 US-13, `OPS-011..014`) — logs and signals under the *deployer*'s control, kept in accordance with policy (`OPS-003`).
- **Incident response** linked to notification to authorities (Ch. 12 + Policy 30 §9.3 + Policy 32) — *off-policy actions* and *jailbreak* in production enter the IR flow that feeds Art. 73.

**Declared gaps**

The matrix declares: operating acquired AI systems in accordance with the provider's instructions for use (paragraph 1, partial); competence, authority and support of those who oversee non-agentic systems on the deployer's side (paragraph 2, partial); relevance and representativeness of input data for the purpose (paragraph 4, gap); informing the provider and suspending non-agentic systems when there is a risk (paragraph 5, partial). Covered are the keeping of logs (paragraph 6, floor CTX-AIA-RE-P03) and informing affected persons (paragraph 11, CTX-AIA-RE-R03). Informing and consulting workers (paragraph 7) is out of scope: it is a matter of labour law.

When the organisation is simultaneously provider (*provider*) and deployer (*deployer*) (a common case in *first-party* development), the separation of obligations between the two roles becomes blurred — it is advisable to clarify internally (and contractually when there are sub-deployers) which role is assumed in each use.

**How to comply**

For uses in which the organisation is a *deployer*, the *mandate* (Policy 38) is the central artefact. A specific *template* for a *deployer mandate* is suggested, explicitly documenting the reference to the AI service vendor (`contract_ref` + [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)), the instructions for use received, and the alignment with the requirements of Art. 26.

---

### Article 72 - Post-market monitoring {#artigo-72---monitorização-pós-comercialização}

**Normative content**

Art. 72 requires providers to establish and document a proportionate post-market monitoring system that collects, documents and analyses data on the performance of the system throughout its lifetime, allowing continuous compliance to be evaluated. The system must be based on a post-market monitoring plan that, since Regulation (EU) 2026/1744, «shall be part of the technical documentation referred to in Annex IV»; the Commission adopts guidance, including a template, by 2 September 2027 (Article 72(3)).

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
- **Agentic telemetry** (Ch. 12 US-13) that provides the evidence base for the post-market monitoring plan: *tool invocation audit events*, *intent events*, *budget metrics*, *off-policy / jailbreak detection*.
- Detection of performance degradation and *model drift* (Ch. 12, [`OPS-011`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes)).
- **Feedback cycle for *eval suites*** (Ch. 10 §C5) — incidents detected in production feed the offline suite, strengthening future regression.

**Coverage by the regime**

When the organisation is the provider, the monitoring plan per system is a requirement added by the regime ([CTX-AIA-RE-R04](./requisitos-aplicaveis#acrescentos)): it forms part of the technical documentation (Annex IV, point 9) and names the signals collected in production (`OPS-011`) and those supplied by deployers, the performance criteria, the cadence and owner of the analysis, and the triggers for corrective action. The model drift metrics remain pending the AISVS/SAIF round of AppSec Core.

**How to comply**

Apply R04 on top of the Ch. 12 observability, with *dashboards* for performance, *drift* and vulnerability status, and triggers that set off rollback, reclassification, review of the threat model or notification of a serious incident.

---

### Article 73 - Reporting of serious incidents {#artigo-73---comunicação-de-incidentes-graves}

**Normative content**

Art. 73 requires providers to report **serious incidents** to the market surveillance authorities of the Member States where they occurred, **immediately** after establishing a causal link between the AI system and the incident (or the reasonable likelihood of such a link) and, in any event, **not later than 15 days** after the provider or, where applicable, the deployer becomes aware of it; **within 10 days** in the event of the death of a person; and **within 2 days** in the event of a widespread infringement or of a serious incident as defined in Article 3, point (49)(b). An initial report that is incomplete may be submitted, followed by a complete report (paragraph 5). Investigation and corrective action follow (paragraph 6).

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Incident detection and response | Ch. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) (*jailbreak* / *off-policy*) + Policy 30 §9.3 | Detection, response and post-incident process; actionable agentic signals |
| Agentic-specific incident classes | Policy 16 §11.4 | *Off-policy action*, *intent-action divergence*, successful *prompt injection*, *kill-switch* failure, *credential exposure* |
| Response to *upstream* incidents | Policy 39 §7 | *Rug pull*, *dataset poisoning*, *tool poisoning*, *provider outage* |
| Escalation and responsibilities | Ch. 14 + Policy 38 | Roles and responsibilities; *owner* + *approver* declared in the *mandate* |
| Severity classification | Ch. 01, Ch. 12 | Impact criteria, classification |
| Definition and notification deadlines | Policy 32 §4.1 and [Policy 32 §6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória) | Definition of serious incident and the deadlines of Article 73 |

**What SbD-ToE covers**

- Detection, response and post-incident process (Ch. 12).
- **Agentic-specific incident classes** defined (Policy 16 §11.4): *off-policy action*, *intent-action divergence*, successful *prompt injection* that resulted in an unauthorised *tool call*, *kill-switch* failure, *credential exposure*.
- **Response to *upstream* incidents** (Policy 39 §7) — when the incident originates at the model / dataset / MCP server AI service vendor, and not in internal operations.
- Escalation roles and responsibilities (Ch. 14, Policy 38).
- Impact criteria that support severity classification (Ch. 01, Ch. 12).

**Declared gap (partial)**

The definition of serious incident and the deadlines are in Policy 32 (§4.1 and §6), and the matrix records Article 73(1) to (5) as covered. The deadlines are those of Article 73 (15 days / 10 days / 2 days, counted from awareness). Missing is the rule of not altering the system, in a way that affects the analysis of causes, without first informing the authority (Article 73(6)): the IRP favours containment “where possible”.

**How to comply**

Configure the Ch. 12 incident schema and the SIEM/ITSM exporters to produce the notification provided for in Policy 32 §6, and add to the runbook the prior informing of the authority before any change to the system that affects the analysis of causes.

---

### General-purpose AI models - Articles 53 and 55 (GPAI) {#modelos-de-ia-de-finalidade-geral---artigos-53-e-55-gpai}

**Normative content**

Art. 53 requires providers of **general-purpose AI models** (GPAI) to provide technical documentation of the model (Annex XI), information and documentation for providers of AI systems that integrate the model (Annex XII), a copyright compliance policy and a «sufficiently detailed summary about the content used for training». Art. 55 adds, for models with **systemic risk**, model evaluation including «adversarial testing» (*adversarial testing* / *red teaming*), assessment and mitigation of systemic risks, reporting of serious incidents and ensuring **an adequate level of cybersecurity protection for the model and the physical infrastructure**.

**SbD-ToE coverage**

| AI Act requirement | SbD-ToE chapter | Coverage |
|---|---|---|
| Adversarial evaluation / *red teaming* | Ch. 10 §C5 + Policy 19 §7 + Ch. 03 agentic playbook | Continuous *eval suites* (prompt regression, *abuse corpus*, *A/B*, *drift*) + MITRE ATLAS threat library |
| Cybersecurity of the model and infrastructure | Ch. 04 ([`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)/[`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)), Ch. 08, Ch. 09 | Agentic architecture, IaC, containers/runtime |
| Protection of weights and artefacts | Ch. 05 (`DEP-011..014`) + Policy 39 + Ch. 04 | Integrity, provenance, AI BOM, *pinning*, access control |
| Monitoring and incidents | Ch. 12 + `OPS-011..014` + Policy 30 §9 | Detection of *off-policy* / *jailbreak* / *exfiltration* via tool |
| Contractual clauses for GPAI | Ch. 14 US-21 + Policy 33 §10 + [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) | Contractual declaration of compliance with Art. 53/55 by the AI service vendors |

**What SbD-ToE covers**

- **Continuous AI red teaming** made concrete (Ch. 10 §C5 + Policy 19 §7) — not merely as a recommendation. *Eval suites* include an *abuse corpus* (LLM01-2025 *prompt injection*, LLM06-2025 *excessive agency*) with a monthly cadence at A4 (the Manual's choice).
- **Cybersecurity of the infrastructure** that serves the model (Ch. 04 incl. [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), Ch. 08, Ch. 09).
- **Integrity and access protection** for weights, *checkpoints* and *datasets* — now with an auditable AI BOM and required *pinning* (`DEP-012/013`, Policy 39). Response to `AML.T0109` *Supply Chain Rug Pull* documented in Policy 39 §7.
- **Monitoring and response** (Ch. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014)) — active detection of *jailbreak* (LLM01-2025) and *off-policy actions* in production; detection corpus updated according to the cadence of the *mandate*.
- **Contractual compliance declared by GPAI service vendors** ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014), Ch. 14 US-21, Policy 33 §10) — required in the AI service vendor approval process.

**Declared gaps and out of scope**

The documentation of Annexes XI and XII draws on evidence from the Manual (AI BOM, *eval suites*), but its drafting is the model provider's; the Manual is written from the side of those who consume the model. Model evaluation with standardised protocols and documented adversarial testing at model level (Article 55(1)(a)) has partial coverage. The reporting of serious incidents and the cybersecurity of the model and of the infrastructure (Article 55(1)(c) and (d)) are covered. The copyright policy and the summary of the training content (Article 53(1)(c) and (d)) are out of scope: they belong to the legal plane. The assessment of systemic risks at Union level (Article 55(1)(b)) belongs to the AI domain; the adversarial threat model provides evidence for it.

**How to comply**

It is suggested to: treat weights, *checkpoints* and *datasets* as supply chain assets with provenance and access control (Ch. 05); institute continuous AI red teaming (Ch. 10) aligned with MITRE ATLAS; apply infrastructure hardening (Ch. 04/08/09); and refer GPAI documentation, copyright and systemic risk assessment to the AI, legal and compliance teams.

---

### Prohibited practices and transparency (Articles 5 and 50) {#práticas-proibidas-e-transparência-artigos-5-e-50}

**Normative content**

Art. 5 prohibits a set of practices (e.g. harmful subliminal manipulation, social scoring — *social scoring* —, the use of «real-time» remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement, subject to exceptions); from 2 December 2026, also the generation or manipulation of realistic intimate images, videos, audio or similar material of an identifiable person without their consent and of child sexual abuse material (Article 5(1), first subparagraph, points (ba) and (bb), under the conditions of paragraphs 1a and 1b, inserted by Regulation (EU) 2026/1744; Article 113, third paragraph, point (a)). Art. 50 imposes transparency duties on «certain AI systems» (informing people that they are interacting with AI; marking synthetic content / *deepfakes*).

**SbD-ToE coverage**

Art. 50 is **covered** by two requirements added by the regime, declared with the ART50 grade of context CTX-AIA-RE (which can also be declared on its own, for systems that are not high-risk): informing people that they are interacting with an AI system or that they are exposed to emotion recognition or biometric categorisation, and disclosing deep fakes (CTX-AIA-RE-R01); and marking synthetic content in a machine-readable format, with the marking verified in testing (CTX-AIA-RE-R02).

For points (ba) and (bb) of Article 5(1), placing on the market a system whose intended purpose is not that generation is prohibited only if, among other conditions, the system does not have “reasonable and adequate technical safety measures and other safeguards to reliably prevent that generation or manipulation” (Article 5(1a)(a)(ii)). Those safeguards are **covered** by the floor entries CTX-AIA-RE-P09 (threat model of the misuse of generated content, assessed with red-team and content-safety tests) and P10 (content-safety filters and classifiers on input and output), without replacing the legal qualification.

**Out of scope**

The judgement on the admissibility of a purpose (Art. 5) is a legal and product qualification and is out of scope; for points (a), (b) and (e) of paragraph 1, the Manual provides evidence (Ch. 02 US-17, `DEP-011`). Also out of scope is the disclosure of AI-generated text published on matters of public interest (Article 50(4), second subparagraph): it is an editorial decision of the deployer.

**How to comply**

Declare the ART50 grade on the application when the system is covered by Art. 50 and apply requirements R01 and R02 and, in generators of realistic images, video or audio, the floor entries P09 and P10. The determination of prohibitions and the legal qualification of the transparency duties remain with the legal and product teams.

---

## PART II: SYNTHESIS AND REFERENCES {#parte-ii-síntese-e-referências}

### Synthesis of AI Act / SbD-ToE coverage {#síntese-da-cobertura-ai-act--sbd-toe}

The AI Act calls for AI systems that are **safe, robust, documented and open to oversight**, with the provider responsible throughout the entire lifecycle. SbD-ToE offers the **technical-operational core** of that effort: technical risk management (Ch. 01, 03), defensive architecture (Ch. 04), integrity of the data and model supply chain (Ch. 05), pipelines and quality gates (Ch. 06, 07, 11), testing and adversarial robustness (Ch. 10), logging and post-market monitoring (Ch. 12) and governance (Ch. 14).

The **strongest and most direct** coverage lies in the **cybersecurity of Art. 15** and its operational correlates (Art. 12 and 19 record-keeping, Art. 14 human oversight, Art. 50 transparency, Art. 72 post-market monitoring, Art. 73 incidents) - this is where the technical evidence of SbD-ToE is most directly reusable — without this amounting to compliance with the AI Act, which requires all the requirements of Section 2 and the conformity assessment.

The matrix separates three answers. **Covered:** cybersecurity, record-keeping, human oversight, the transparency of Article 50, substantial modification, explanation to affected persons, post-market monitoring, serious incidents and the declaration of high-risk status as the application's context. **Declared gap:** accuracy and robustness (pending the AISVS/SAIF round of AppSec Core) and the specific gaps listed per Article. **Out of scope, with a reason:** risk management (Article 9), governance of training data (Article 10), quality management (Article 17), the specifics of biometric identification, conformity assessment, CE marking, the EU declaration and the judgement on prohibited practices. In these, SbD-ToE provides technical evidence to the teams responsible, not the conformity judgement.

The result is consistent with the philosophy of the manual:

- **Today**, SbD-ToE makes it possible to build and operate the software of an AI system with security by design.
- **Tomorrow**, when the organisation has to comply with the AI Act, it declares context CTX-AIA-RE on the application, applies the floor entries and requirements that it elevates, and works out with the teams responsible what is out of scope.

### Scope, roles and penalties {#âmbito-papéis-e-sanções}

The AI Act distinguishes **providers (providers)**, **deployers (deployers)**, importers and distributors, with distinct obligations. The bulk of the technical obligations (and of the SbD-ToE coverage) falls on the **provider of high-risk AI systems**; the *deployer* has its own obligations (use in accordance with the instructions, human oversight, FRIA in certain cases - Art. 26, 27).

In terms of penalties (Art. 99), the regulation sets maximum tiers (for SMEs, including start-ups, each fine may not exceed the percentage or the amount, «whichever thereof is lower» — Article 99(6); the same applies to small mid-cap enterprises as regards the fines in paragraphs 4 and 5 — Article 99(6a), inserted by Regulation (EU) 2026/1744):

- **Prohibited practices (Art. 5)**: up to **€35 M** or **7%** of total worldwide annual turnover (whichever is higher).
- **Non-compliance with the obligations listed in Article 99(4)** — providers (Article 16), authorised representatives (Article 22), importers (Article 23), distributors (Article 24), providers and operators pursuant to Article 25(2) and (4) (point (da), inserted by Regulation (EU) 2026/1744), deployers (Article 26), notified bodies (Article 31, Article 33(1), (3) and (4), and Article 34) and transparency (Article 50): up to **EUR 15 M** or **3%**.
- **Incorrect, incomplete or misleading information** supplied to notified bodies or national competent authorities in reply to a request: up to **EUR 7.5 M** or **1%**.
- For providers of **general-purpose AI models** (Art. 101): fines imposed by the Commission, up to **EUR 15 M** or **3%** (whichever is higher), applicable from 2 August 2026 (Article 113, third paragraph, point (b), excepts Article 101 from the 2 August 2025 date).

### References {#referências}

- **AI Act**: Regulation (EU) 2024/1689 (CELEX: [32024R1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)), amended by Regulation (EU) 2026/1744 («Digital Omnibus on AI», CELEX: [32026R1744](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R1744)); consolidated text of 27.7.2026 (CELEX: [02024R1689-20260727](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727)).
- **Art. 9** - Risk management system (lifecycle).
- **Art. 10** - Data and data governance (representativeness, bias).
- **Art. 11 and Annex IV** - Technical documentation.
- **Art. 12 / Art. 19** - Recording of events and keeping of logs.
- **Art. 13 / Art. 14** - Transparency to deployers and human oversight.
- **Art. 15** - Accuracy, robustness and cybersecurity (resilience to attacks, incl. adversarial examples).
- **Art. 17** - Quality management system.
- **Art. 72 / Art. 73** - Post-market monitoring and reporting of serious incidents.
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

The application of SbD-ToE in an AI Act context, as in NIS2 and DORA, benefits from a formal process of internal exceptions to technical requirements. An internal exception does not alter any legal obligation under the AI Act; it only documents an accepted technical risk for the evidence dossier. Cases in which a requirement is not applicable, or in which a temporary residual risk is accepted (e.g. an adversarial vector mitigated by compensating controls while the *retraining* is prepared), must be documented, approved at the appropriate level and reviewed periodically.

Ch. 14 (Governance and Contracting) of SbD-ToE provides the necessary artefacts: exception register, risk acceptance criteria, approval chain and remediation plan. It should be noted that certain deviations **cannot be made exceptions** in the AI Act context - first and foremost, any use that falls within the prohibited practices of Art. 5. The existence of a formal exceptions process is not a sign of fragility: it is evidence of mature governance and of conscious control over the risk profile.

:::

---

**Version:** 1.1
**Date:** September 2026
**Next review:** with the next revision of the AI Act coverage matrix
