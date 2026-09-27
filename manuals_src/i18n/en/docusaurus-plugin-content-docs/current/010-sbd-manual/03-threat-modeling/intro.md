---
id: intro
title: Chapter 3 - Threat Modelling
description: Structured identification, analysis and mitigation of threats during the development lifecycle
tags: [threat-modeling, stride, linddun, requisitos, mitigacao, risco, arquitetura, SAMM, SSDF, SLSA, DSOMM]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/intro.md
  source_sha256: 342445740e9cfa551ef20e9323880072ce8241c787882bca29ac536a189243c6
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 05f923f6f0812ac7dfb1ad637fd51ab4444eca29f980cd8ce5f88a81de016259
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [basilar, chapter_role, cycle_iteration, framework_source_corpus, papel_suporte, plain_rag, practitioner_manual, requirement_runtime, risk_level, sbdtoe_sbd, slug_threat_modeling, threat, traceability, validation_evaluation]
  glossary_sha256: e8aae862a7e3c7af3e775d6a3081850f1a15c6b17db9df5ab37e72c69f270d62
  translated_at: 2026-09-25T20:17:07Z
  stamped_at: 2026-09-26T18:33:28Z
  reviewed_by: null
---

import ChapterTypeCallout from '@site/src/components/ChapterTypeCallout';

<ChapterTypeCallout kind="basilar" title="Capítulo Basilar">

This chapter is considered **foundational** in the *Security by Design - Theory of Everything (SbD-ToE)* model.
Its application is **mandatory** to guarantee the coherence, traceability and effectiveness of the remaining security practices.

The absence or partial application of Threat Modelling compromises the **formal link between risk, architecture and requirements**, making a consistent adoption of SbD-ToE unfeasible.

</ChapterTypeCallout>

# Chapter 3 - Threat Modelling

## 1. 🧭 What it covers technically {#1--o-que-cobre-tecnicamente}

**Threat Modelling** is the practice that makes it possible to **anticipate real threats** before implementation, on the basis of the application's **architecture, data flows and risk context**. It is treated as a **structured decision process**, subject to human validation and to the production of verifiable evidence.  
The absence of a threat from a model is not proof that it does not exist; the risks of omission and bias must be explicitly assumed and mitigated.

In SbD-ToE, Threat Modelling is the **formal origin of the mitigation requirements**, directly linking:
- the risk classification (Ch. 1),
- the security requirements (Ch. 2),
- and the architecture decisions (Ch. 4).

This chapter covers:

- The systematic integration of threat modelling into the development lifecycle
- Structured threat analysis methods (STRIDE, LINDDUN, PASTA)
- Creation and maintenance of architecture-based threat models (DFDs, trust boundaries)
- Identification of relevant technical and business threats
- Explicit derivation of requirements and controls from the identified threats
- Traceability between threat → requirement → mitigation → validation
- Controlled reuse of models in standardised architectures
- **Extension to AI/ML systems** — systems with artificial intelligence components (LLMs, predictive models, RAG, autonomous agents) require extended threat modelling with specific adversarial threats (model poisoning, prompt injection, data exfiltration, AI supply chain compromise) catalogued in MITRE ATLAS and NIST AI 100-2; see [Methodologies — §AI/ML](./addon/metodologias-e-ferramentas#ai-ml) and requirement [THR-008](./addon/catalogo-requisitos-threat-modeling)

---

## 2. 🧪 Practical prescription: what, who, how, when, why and to what end {#2--prescrição-prática-o-quê-quem-como-quando-porquê-e-para-quê}

### 🔐 Threat Modelling as the link between risk, architecture and control {#-threat-modeling-como-elo-entre-risco-arquitetura-e-controlo}

> *Without Threat Modelling, security requirements lose their context  
> and the controls applied no longer have a justified origin.*

### 📌 What must be done {#-o-que-deve-ser-feito}

- Carry out threat modelling on the basis of the **application's risk level**
- Model data flows and trust boundaries on the basis of architecture artefacts
- Identify relevant threats using recognised models
- Associate each threat with:
  - one or more mitigation requirements,
  - technical or organisational controls,
  - and validation criteria
- Document decisions, accepted risks and future actions
- Validate the threat model as part of the architecture review

### ⚙️ How it must be done {#️-como-deve-ser-feito}

- Use clear, versioned diagrams (DFDs, context diagrams)
- Apply methodologies such as STRIDE, LINDDUN or PASTA proportionally
- Integrate the exercise into existing rituals (design review, technical refinement)
- Create traceable backlog items for each relevant mitigation
- Align the derived requirements with the Requirements Catalogue (Ch. 2)
- Reuse models only when the architecture and the context are equivalent

> Specialised tools can **support** the process,  
> but **do not replace human analysis or technical validation**.

### 📆 When to apply {#-quando-aplicar}

- At the start of relevant projects or epics
- Before external integrations, exposures or architectural changes
- Whenever the application is classified as **L2 or L3**
- Whenever changes occur that may alter the threat profile

### 👥 Who is involved {#-quem-está-envolvido}

| Role/Function              | Main responsibilities                                   |
|---------------------------|----------------------------------------------------------------|
| Software Architects / DevOps / SRE   | Facilitate the process and keep the models up to date           |
| Development Team | Explain flows, logic and attack surfaces                |
| Security / AppSec        | Identify relevant threats, vectors and attack techniques   |
| Product Owner / Business   | Validate the impact, priority and acceptability of the risk          |

---

## 3. ⚠️ Caveats and limitations {#3-️-caveats-e-limitações}

- Models that are too abstract become useless
- Unversioned documentation loses operational value
- Automated tools do not capture business context
- The absence of a link to requirements and the backlog nullifies the value of the exercise

---

## 4. 💡 Examples and reuse {#4--exemplos-e-reutilização}

- Examples of applying STRIDE by architecture type
- Examples of privacy-focused threat modelling (LINDDUN)
- Examples of integration with supporting tools (e.g. IriusRisk)

---

## 5. 🔍 What more can be done (and why) {#5--o-que-pode-ser-feito-mais-e-porquê}

- Create internal libraries of reusable threats by system type
- Integrate threat modelling with validation pipelines and architecture gates
- Use the history of incidents and findings to enrich the models
- Train technical facilitators for iterative, lightweight sessions

---

## 🧩 Links to other chapters {#-ligações-a-outros-capítulos}

| Chapter | Technical relationship |
|---------|-----------------|
| Ch. 1 – Risk Management | Determines when threat modelling is mandatory |
| Ch. 2 – Security Requirements | Receives requirements derived from the threats |
| Ch. 4 – Secure Architecture | Primary source of the modelled artefacts |
| Ch. 7 – Secure CI/CD | Supports traceability and validation |
| Ch. 10 – Security Testing | Validates derived requirements |

---

> 📌 This chapter is **mandatory** for **L2 and L3** applications.  
> It is the mechanism that guarantees that security requirements **respond to real threats**,  
> and that the architecture is assessed **before** it is exploited in production.

---

## 📜 Relevant Organisational Policies {#-políticas-organizacionais-relevantes}

| Policy | Mandatory? | Application | Minimum content |
|----------|--------------|-----------|------------------|
| [Threat Modelling Policy](/sbd-toe/assets/policies/policy-threat-modeling) | ✅ Yes (L2–L3) | AppSec, Architecture | Mandatory methodology, scope, minimum artefacts, traceability and cadence |

[📎 See the details of the policies recommended for this chapter](./policies-relevantes)  
For the printed version, see the **manual's Organisational Policies Annex**.
