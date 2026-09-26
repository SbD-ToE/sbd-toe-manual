---
id: intro
title: Application Criticality Classification
description: Determining the criticality of applications in order to apply proportionality in security controls
tags: [base, classificacao, risco, proporcionalidade, ciclo-vida]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/intro.md
  source_sha256: b289e7aa0f89193cb030454414943dde07970c2773de5c4998ae389630b5ee81
  source_commit: 112711064196b71c545672fe3fb3ae412b36575e
  target_sha256: 034ddf62b8bd4d79ea7cddfb1d727c5a5e046065f06593dae1b107d336c847d1
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 69aedbbdd11831f1cdc997bd1abfda3e2e4d3b411b1b43faf096628c510f395b
  glossary_keys: [basilar, chapter_role, cycle_iteration, evidenciabilidade, lifecycle_phase, mapping, maturity, mcp_reading_normativa, normative_empirical, papel_suporte, practitioner_manual, risk_level, role_tech_lead, sbdtoe_sbd, traceability]
  glossary_sha256: 4b3633ac9d030a8bd44ab5d39fd20b7957ac4c2e8e01e0bde8aa8c3259b800a9
  translated_at: 2026-09-26T17:23:43Z
  reviewed_by: null
---

import ChapterTypeCallout from '@site/src/components/ChapterTypeCallout';

<ChapterTypeCallout kind="basilar" title="Capítulo Basilar">

This chapter is considered **foundational** in the *Security by Design – Theory of Everything (SbD-ToE)* model.
Its application is **mandatory** to guarantee the coherence, traceability and effectiveness of the remaining security practices.

The foundational chapters constitute the **technical and methodological foundation** of the model.
The absence or partial application of any one of them compromises the **overall integrity** of SbD-ToE, making the coherent adoption of the operational and governance practices unfeasible.

</ChapterTypeCallout>

# Application Criticality Classification

This chapter defines and prescribes **how to classify applications according to their criticality**, so as to allow the **proportional application of requirements, controls, validations and security evidence** throughout the entire lifecycle.

In SbD-ToE, classification **does not aim to label technologies or tools**, but rather to **characterise application risk sufficiently to support consistent technical and organisational decisions**.

Automation and decision-support tools (including AI) are treated as a **normal part of the modern SDLC** and must be considered in the classification **whenever they alter exposure, data, impact or the way decisions and validations are carried out**.  
Their presence **does not create new risk categories**, but it influences the **internal attributes of the risk** and, consequently, the controls required.

This chapter suggests a **simple, direct and economically viable classification model**, suited to most application contexts.  
The organisation may, however, opt for an existing alternative model (for example DRP/BIA or another formal risk analysis method), provided that its results can be **mapped to the context of application development**.

The central objective of the manual is to:
1. **Classify applications consistently**, to ensure adequate proportionality;  
2. **Provide clear, fast and traceable mechanisms** for doing so, without excessive dependence on heavy processes or specific tools.

> 📌 Criticality classification is the entry point for the chapters:  
> [Chapter 02 – Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro),  
> [Chapter 04 – Architecture](/sbd-toe/sbd-manual/arquitetura-segura/intro),  
> [Chapter 07 – CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro) and  
> [Chapter 10 – Testing](/sbd-toe/sbd-manual/testes-seguranca/intro).

---

## 🧠 Conceptual note: risk and attributes {#-nota-conceptual-risco-e-atributos}

SbD-ToE treats **risk as a single concept**, regardless of its technical or procedural origin.  
What varies are the **attributes of the risk** - such as origin, mechanism, detectability, reproducibility and evidentiability - which directly influence the applicable requirements and controls.

> 📌 See: [Risk Attributes](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/atributos-risco)

---

## 🧪 Practical prescription: what, who, how, when, why and to what end {#-prescrição-prática-o-quê-quem-como-quando-porquê-e-para-quê}

### 📌 What must be done {#-o-que-deve-ser-feito}

1. Classify the application according to **exposure, sensitive data and impact**, as proposed in the manual, or adopt another equivalent model;
2. Explicitly consider how **automation and decision support (incl. AI)** influence the relevant **risk attributes**;
3. Document the classification, the assumptions and the evidence used;
4. Apply minimum controls based on the level assigned;
5. Review the classification at key points of the lifecycle;
6. Apply formal criteria for risk acceptance, where necessary.

---

### ⚙️ How it must be done {#️-como-deve-ser-feito}

- Use the [Classification Model](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/modelo-classificacao-eixos);  
- Or an alternative model adopted by the organisation (e.g. [Adoption of DRP/BIA](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia));  
- Where automated/assistive tooling exists (incl. AI), **assess its impact on the risk attributes** and calibrate E/D/I accordingly;  
- Incorporate the [Risk Classification Lifecycle](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/ciclo-vida-risco);  
- Apply the [Risk Acceptance Criteria](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/criterios-aceitacao-risco);  
- Consider real threats through the [Threat Mapping by Risk Level](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/mapeamento-ameacas-risco);  
- Record decisions in a versioned repository, a risk tool or traceable documentation.

---

### 📆 When to apply {#-quando-aplicar}

- During the initial phase of the project or the definition of the architecture;
- Whenever there are relevant changes: new functionality, data, exposure or integrations;
- When automation/assistance mechanisms (incl. AI) with an impact on the risk attributes are introduced or changed;
- At major releases or critical milestones (e.g. production);
- After relevant security incidents;
- At least every **6 months** or **at each architecture review or security roadmap review**.

> Periodic review of the risk classification directly supports **intermediate maturity** practices in **SAMM**, **DSOMM** and **SSDF**.

---

### 👥 Who is involved and how {#-quem-está-envolvido-e-como}

| Role                | Contribution                                                                 |
| -------------------- | -------------------------------------------------------------------------- |
| Developer / Tech Lead | Propose the classification, identify relevant changes                    |
| AppSec Engineer      | Validate the model applied, adjust the risk level, apply the matrix             |
| Software Architects | Review technical implications, flows and exposure                            |
| Product Owner / Executive Management | Approve risk acceptance, assess the impact of exceptions        |
| GRC / Compliance     | Ensure traceability and normative alignment                           |
| QA                   | Validate compliance with the requirements per risk level before go-live       |

> ✅ *All contributions must be recorded and versioned for traceability and audit purposes.*

---

### 🎯 Why / To what end {#-porquê--para-quê}

- Guarantee proportionality in the security controls applied;
- Reduce costs by avoiding over-protection or unnecessary exposure;
- Support normative compliance and audits;
- Inform strategic decisions (roadmap, budgeting, outsourcing);
- Promote continuous improvement and risk visibility.

> 📌 The proportional application of controls may be guided by the  
> [Controls Matrix by Risk](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/matriz-controlos-por-risco).

---

## 🧪 Risk Classification Lifecycle {#-ciclo-de-vida-da-classificação-de-risco}

Risk classification **is not a one-off event**, but a continuous process. It must be reviewed:

- On changes to architecture, exposure, data or automation/assistance;
- Before critical releases;
- Periodically (e.g. every 6 months);
- After relevant incidents or detections.

> 📌 See: [Risk Classification Lifecycle](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/ciclo-vida-risco)

This continuous reassessment ensures that the controls applied remain proportional and up to date.

---

## ✅ Risk Acceptance Criteria {#-critérios-para-aceitação-de-risco}

Not every identified risk requires additional mitigation. Some may be **formally accepted**, provided that they meet clear criteria:

- Compatibility with the application's L1–L3 level;
- Residual value within the defined thresholds;
- Sufficient evidence of the controls applied;
- Formal documentation of the decision and of the review deadline.

> 📌 See: [Risk Acceptance Criteria](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/criterios-aceitacao-risco)

---

## 🛡️ Mapping Threats to Risks {#️-mapeamento-de-ameaças-a-riscos}

To ensure that the classification reflects the technical reality, it is essential to map known threats (e.g. STRIDE, MITRE ATT&CK) to the adopted risk model.

> 📌 See: [Threat Mapping by Risk Level](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/mapeamento-ameacas-risco)

---

## 📜 Relevant Organisational Policies {#-políticas-organizacionais-relevantes}

The practical application of this chapter requires formal policies that ensure standardisation, traceability and governance of risk:

| Policy                                        | Mandatory? | Application                                | Minimum expected content                                                             |
| ----------------------------------------------- | ------------ | ---------------------------------------- | ------------------------------------------------------------------------------------ |
| [Application Risk Classification Policy](/sbd-toe/assets/policies/policy-classificacao-risco) | ✅ Yes        | All projects and product teams   | Classification model; moments of application; formal record.                      |
| [Residual Risk Acceptance Policy](/sbd-toe/assets/policies/policy-aceitacao-risco)         | ✅ Yes        | Security, management, product owners      | Acceptance criteria; those responsible; validity; traceable evidence.                |
| [Periodic Risk Review Policy](/sbd-toe/assets/policies/policy-revisao-periodica-risco)          | ✅ Yes        | The whole organisation                       | Minimum frequency; mandatory triggers; documentation.                              |
| [Decision Traceability Policy](/sbd-toe/assets/policies/policy-rastreabilidade)         | ⚠️ Optional  | Regulated or auditable contexts        | Versioning; link to architecture, requirements and controls.                        |

> 📌 See the details in the **manual's policy annex**.
