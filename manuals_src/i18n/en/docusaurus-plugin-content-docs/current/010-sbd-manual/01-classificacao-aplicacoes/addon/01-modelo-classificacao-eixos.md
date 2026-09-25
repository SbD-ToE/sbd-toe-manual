---
id: modelo-classificacao-eixos
title: Classification Model
sidebar_position: 1
tags: [tipo:modelo, tema:criticidade, eixo, risco]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/addon/01-modelo-classificacao-eixos.md
  source_sha256: 1f8052a4b29caf049dceae3fc8cac362f3cce54a2c45252b193ab3b87b3b9ac7
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 57f7e324a0c856b3ad7af04a1bd947ec88d95b0de17dec057f3732fd3e841050
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: f3ae07385fc10c458f9087ea5ea231fd2bbf0e4852b0e4c0e84ec84618762443
  glossary_keys: [avaliacao, chapter_role, cycle_iteration, evidenciabilidade, lifecycle_phase, normative_empirical, prescriptive, risk_level, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: 810520c14b1b36fe29cd04aa4ceae969711bb8ff2349bea38075782e3be447c6
  translated_at: 2026-09-25T17:59:11Z
  reviewed_by: null
---
<!--template: sbdtoe-core -->

# Classification Model by Risk Axes

## 🎯 Objective {#-objetivo}

To provide a **practical, proportional and applicable** model for the software development context, for assessing the **risk level of an application** based on three fundamental axes:

- **Exposure (E)**
- **Data Type (D)**
- **Potential Impact (I)**

This model allows quick, documented decisions on the minimum security controls to apply, with traceability throughout the lifecycle.

---

## 🧠 Conceptual framing {#-enquadramento-conceptual}

In *Security by Design – Theory of Everything (SbD-ToE)*, risk is treated as a **single concept**, characterised by multiple **internal attributes** (origin, mechanism, detectability, evidentiability, reproducibility, among others).

The **E/D/I** model is a **simplified, operational projection** of that risk, focused on the factors that most directly influence:
- the technical exposure of the system,
- the nature of the data processed,
- and the potential impact of a failure or abuse.

This model **does not aim to capture the whole of the risk**, but to provide a consistent and sufficient basis for application classification and proportional application of controls.

---

## 🧮 Simplified Model Formula {#-fórmula-do-modelo-simplificado}

Risk classification is based on the sum of the three axes:

**Classified Risk (R) = E + D + I**

**Where:**

- **E (Exposure)**: Degree of technical and operational accessibility of the application
- **D (Data Type)**: Sensitivity, value and legal framing of the data processed
- **I (Potential Impact)**: Expected consequence of a failure, breach or incorrect decision

### Classification by Score {#classificação-por-pontuação}

| Total Sum | Risk Classification | Code |
|------------|------------------------|--------|
| 3–4        | **Low**              | L1     |
| 5–6        | **Medium**              | L2     |
| 7–9        | **High**            | L3     |

This classification represents the **minimum level of rigour** to apply in requirements, controls, validations and evidence.

---

## 🧱 Axis Details {#-detalhe-dos-eixos}

### 🧭 Exposure (E) {#-exposição-e}

Assesses how accessible the application or system is, considering attack surfaces, interfaces and network context.

| Level | Description                                          | Points |
|-------|----------------------------------------------------|--------|
| 1     | Accessible internally only (no external access) | 1      |
| 2     | Accessible externally, with authentication           | 2      |
| 3     | Public or widely exposed (open or unauthenticated access) | 3 |

---

### 📑 Data Type (D) {#-tipo-de-dados-d}

Classifies the nature, sensitivity and legal framing of the data processed.

| Level | Description                                                              | Points |
|-------|------------------------------------------------------------------------|--------|
| 1     | Public or non-sensitive data                                    | 1      |
| 2     | Personal, identifiable or internally confidential data               | 2      |
| 3     | Regulated or highly sensitive data (e.g. health, financial, location) | 3 |

---

### ⚠️ Potential Impact (I) {#️-impacto-potencial-i}

Assesses the expected impact on the organisation should the risk materialise.

| Level | Description                                                                  | Points |
|-------|----------------------------------------------------------------------------|--------|
| 1     | No or negligible impact                                                 | 1      |
| 2     | Limited, localised or reversible impact                                 | 2      |
| 3     | High impact: significant financial, regulatory, operational or reputational | 3 |

---

## 🧩 Complementary criteria in automation and decision-support contexts {#-critérios-complementares-em-contextos-de-automação-e-apoio-à-decisão}

The use of automation or decision-support mechanisms (including AI) **does not create new risk axes**, nor does it, by itself, imply a change in the application's criticality.

Such mechanisms should be considered **only when they modify relevant attributes of the risk**, namely exposure, the type of data processed or the effective impact of the decisions and actions carried out.

### 🧭 Mandatory application rule {#-regra-de-aplicação-obrigatória}

Reassessment of the **E**, **D** and **I** axes is **mandatory** whenever automation or decision support:

- introduces a new exposure surface or external integration;
- involves additional processing of personal or regulated data, secrets or confidential information;
- increases the delegation, reach or speed of decisions with real impact on the system, the data or the business.

Whenever **any of these conditions holds**, the team **must** adjust the affected axes and **explicitly record the rationale for the decision**.

Keeping the original classification **is only acceptable** when there is:
- mandatory and effective human validation;
- explicit control of the automated outputs;
- sufficient evidence that the attributes of the risk have not changed.

### 🔎 Minimum practical guidance {#-orientação-prática-mínima}

| Observed situation                                                                 | Expected adjustment |
|-----------------------------------------------------------------------------------|-----------------|
| Integration with external automation or AI services                                | Assess E       |
| Sending personal or regulated data or IP in prompts, context or artefacts        | D ≥ 2           |
| Automatic execution of code, infrastructure or decisions without human review       | I = 3           |
| Non-deterministic results accepted as final evidence                        | I = 3           |

> 📌 This guidance is prescriptive as to the need for assessment, not as to the final outcome, which must always be contextual and documented.

---

## 🔎 Why sum the axes? {#-porquê-somar-os-eixos}

The choice of a **simple sum** of the axes favours:

- operational simplicity;
- ease of adoption by technical teams;
- consistency across projects;
- clarity and transparency in audits.

More complex models were considered, but they tend to introduce excessive variability and hinder organisational standardisation.

This model is empirical and prescriptive, suited to agile and DevSecOps contexts, while maintaining proportionality and traceability.

---

## ⚠️ Final considerations {#️-considerações-finais}

- This model **does not replace** threat modelling or formal risk analyses;
- It should be used as a **quick classification mechanism** and a starting point for decisions;
- It should be reviewed whenever relevant changes occur in functionality, data, exposure or process assumptions.

Despite its simplicity, the model makes it possible to determine, quickly and on a sound basis, **the level of security rigour to apply**, ensuring coherence throughout the lifecycle.

---

## 🔗 Useful links {#-ligações-úteis}

- Alternative model: [Adoption of existing classifications (DRP/BIA)](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia)
- [Chapter 01 – Application Criticality Classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
