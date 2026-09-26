---
id: intro
title: Chapter 4 - Secure Architecture
description: Foundations, objectives and framing of the chapter dedicated to secure architecture in the software lifecycle
tags: [introducao, arquitetura, requisitos, segurança]
sidebar_position: 4
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/intro.md
  source_sha256: b23aa316ea41e2ce007a0d4cdc51f695a30d4c1f407d0550357a4d3a07667416
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: c869c88a98eeb0b7ecefca035e997c10b650004441ff9aa2bde54873afef4b78
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5536afdcc04f76a07c66e747133c73d68308884707c296abf945937a9630a312
  glossary_keys: [basilar, chapter_role, cycle_iteration, lifecycle_phase, plain_rag, practitioner_manual, requirement_runtime, risk_level, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: 5eeaa0fe83fe469eca9743cf2cefe74226720d46d7aaf1fd16f91237b95aa76e
  translated_at: 2026-09-26T08:32:11Z
  reviewed_by: null
---

import ChapterTypeCallout from '@site/src/components/ChapterTypeCallout';

<ChapterTypeCallout kind="basilar" title="Capítulo Basilar">

This chapter is considered **foundational** in the *Security by Design - Theory of Everything (SbD-ToE)* model.
Its application is **mandatory** to guarantee the coherence, traceability and effectiveness of the remaining security practices.

The foundational chapters constitute the **technical and methodological foundation** of the model; the absence or partial application of any one of them compromises the **overall integrity** of SbD-ToE, making a coherent adoption of the operational and governance practices unfeasible.

</ChapterTypeCallout>


# Secure Architecture

In SbD-ToE, Secure Architecture is treated as an **explicit technical decision process**, proportional to the application's risk (L1–L3).  
Architectural decisions materialise the response to identified threats and condition requirements, development, testing and operation, and must be validated, versioned and supported by verifiable evidence.

This chapter defines the practices that guarantee that an application's architecture **acts as containment and mitigation of structural risk**, through:

- Delimitation of **trust zones** and their respective boundaries
- **Logical and physical segmentation** of components and data
- Control and validation of **inter-zone flows**
- Support for **threat modelling, authentication, access control, validation and secure operations**
- Formal documentation of the architecture and traceability of decisions

It covers different architecture styles:

- Modern monoliths and 3-tier applications
- Microservices and API-first
- Hybrid and cloud-native environments
- Serverless and pipelines as architecture

---

## 🧭 Secure architecture and non-deterministic components {#-arquitetura-segura-e-componentes-não-determinísticos}

Secure Architecture, in the context of SbD-ToE, **does not assume that every component of the system is deterministic**. Modern architectures may integrate components whose behaviour depends on probabilistic, heuristic or inferential processes, introducing variability in results and additional challenges in terms of security, audit and control.

These components **are not treated as exceptions**, but as **first-order architectural elements**, and must be explicitly identified, isolated and governed. Their presence implies conscious decisions at the architecture level, including the definition of trust boundaries, supervision mechanisms, operational *fallbacks*, decision evidence and traceability against threats and security requirements.

This framing applies regardless of the concrete technology used. The focus of the chapter remains on the **architectural governance of risk**, ensuring that non-deterministic decisions remain controllable, auditable and proportional to the application's criticality level.

The operationalisation of this framing for systems with AI/ML components — LLMs, predictive models, RAG, autonomous agents — is defined in [Advanced Recommendations — §AI/ML](./recomendacoes-avancadas#ai-ml) and in requirement [ARC-014](./addon/catalogo-requisitos-arquitetura#arc-014). It includes specific trust boundaries (training-time / inference-time / agentic), architectural controls against prompt injection (LLM01-2025), and isolation of agentic tool invocations (`AML.T0086`).

---

## 🧪 2. Practical prescription: what, who, how, when, why and to what end {#-2-prescrição-prática-o-quê-quem-como-quando-porquê-e-para-quê}

### 📌 What must be done {#-o-que-deve-ser-feito}

1. **Define trust zones** and explicit boundaries
2. **Establish architecture patterns** proportional to risk
3. **Document architecture decisions** (e.g. ADRs, versioned diagrams)
4. **Validate the architecture before go-live** and on significant changes
5. **Record and manage exceptions** when requirements cannot be met

### ⚙️ How it must be done {#️-como-deve-ser-feito}

- Apply **Threat Modelling** techniques (e.g. DFD, STRIDE)
- Use **reusable reference models** (`04-diagramas-referencia.md`)
- Implement controls such as:
  - API Gateway with mutual authentication
  - Traffic segmentation (e.g. ACLs, namespaces, subnets)
  - Containment mechanisms (rate limiting, circuit breakers)
- Validate the architecture on the basis of the criteria in `05-validacao.md`

### 📆 When to apply {#-quando-aplicar}

| Moment                              | Expected action                                         |
|--------------------------------------|-------------------------------------------------------|
| Project start                    | Define the ZTCs and the architecture pattern                    |
| New feature or service       | Review boundaries and inter-zone controls              |
| Integration with third parties             | Analyse the trust and exposure implications         |
| Refactoring or technology migration  | Assess the risk of additional exposure                  |
| Pre-production                         | Validate the architecture against requirements and patterns      |

### 👥 Who is involved and how {#-quem-está-envolvido-e-como}

| Role/Function               | Technical responsibilities                                         |
|----------------------------|--------------------------------------------------------------------|
| **Software Architects** | Define models, diagrams and decisions                               |
| **Developer**              | Implement and maintain the defined controls                         |
| **QA**                     | Validate architecture requirements in tests                          |
| **AppSec Engineer**        | Take part in threat modelling and architecture reviews              |
| **Product Owner**          | Assess the impact on deadlines and cost                                   |
| **DevOps / SRE**           | Automate the verification of architecture controls                 |

> ✅ Every architecture exception must be **recorded, justified and validated** with a compensating plan.

### 🎯 Why / What for {#-porquê--para-quê}

- Reduce the attack surface and limit the propagation of failures.
- Establish a solid technical foundation for all the remaining security controls.
- Enable better-informed, traceable and auditable design decisions.
- Guarantee the proportionality of controls on the basis of the application's risk.

---

## ⚠️ 3. Caveats or limitations of the prescription {#️-3-caveats-ou-limitações-da-prescrição}

- Not every control can be applied to every architecture - the model must be adapted.
- Inconsistent, incomplete or outdated models **generate untraceable risk**. **Relates to.** Violates `ARC-010`; materialises `MT-059`.
- Threat modelling without a clear architecture **is ineffective**. **Relates to.** Violates `ARC-005`; materialises `MT-046`.
- Undocumented exceptions **invalidate traceability and the control of residual risk**. **Relates to.** Violates `CLA-007`; materialises `MT-066`.

---

## 💡 4. Examples of application {#-4-exemplos-de-aplicação}

In an L3 system with microservices and exposure to third parties:

- The architecture defines 4 trust zones (frontend, backend, admin, third parties).
- Each inter-zone flow is validated with authentication, access control and logging.
- The versioned diagram is kept in the repository and validated before each release.
- A justified exception was approved for a circular dependency between two services, mitigated with timeouts and circuit breakers.
- The architecture review was carried out on the basis of the `05-validacao.md` checklist, with evidence of threat modelling and ADRs.

---

## 🧩 Links to other chapters {#-ligações-a-outros-capítulos}

| Chapter                      | Technical and process relationship                                       |
|-------------------------------|---------------------------------------------------------------------|
| `01-gestao-risco`             | The risk level defines the rigour and depth of the architecture     |
| `02-requisitos-seguranca`     | Defines the technical requirements of type `ARC-00x`                     |
| `03-threat-modeling`          | Uses the architecture as the basis for modelling threats                    |
| `06-desenvolvimento-seguro`   | Applies controls defined by the architecture (e.g. validations, filters)|
| `09-containers-imagens`       | Defines execution and isolation patterns consistent with the architecture |

---

## 📜 Relevant Organisational Policies {#-políticas-organizacionais-relevantes}

| Policy | Mandatory | Application | Minimum content |
|----------|-------------|-----------|-----------------|
| [Secure Architecture Policy](/sbd-toe/assets/policies/policy-arquitetura-segura) | Yes | All projects | Definition of principles, patterns and minimum architecture controls |
| [Architecture Review Policy](/sbd-toe/assets/policies/policy-arquitetura-segura) | Recommended | L2–L3 projects | Formal criteria for AppSec review and approval |
| [Pipeline Automation Policy](/sbd-toe/assets/policies/policy-cicd-seguro) | Recommended | Projects with CI/CD | Rules for the automated validation of architecture controls |
| [Architecture Decision Traceability Policy](/sbd-toe/assets/policies/policy-rastreabilidade) | Recommended | GRC, Architecture | Traceability of ADRs, evidence and architectural decisions |
| [Exception Management Policy](/sbd-toe/assets/policies/policy-gestao-excecoes) | Recommended | AppSec, Management | Technical architecture exceptions: justification, deadline and approval |

In the printed version, the relevant policies can be found in the **manual's policies annex**, including: Secure Architecture Policy, Architecture Review Policy and Pipeline Automation Policy.

---

> 🧱 This chapter is **foundational** for the coherent application of the SbD-ToE model. Its absence compromises the proportionality of controls, the effectiveness of threat modelling and the integrity of security measures at runtime.