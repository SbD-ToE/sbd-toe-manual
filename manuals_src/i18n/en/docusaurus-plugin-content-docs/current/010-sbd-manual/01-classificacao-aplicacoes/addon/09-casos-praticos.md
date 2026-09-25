---
id: casos-praticos
title: Examples of Applying Risk Classification
sidebar_position: 9
tags: [tipo:exemplo, tema:classificacao, risco, aplicacao]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/addon/09-casos-praticos.md
  source_sha256: bd9f6e8329056ae9167a9fe05fb7c2c8fa83f03c0e1d55c96f8778f8f6c1504c
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: e6f2643b8b40ac512eaec88cc9e0eeb76366e09bcb324188cc7aeaac4fca32de
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [sbdtoe_sbd, validation_evaluation]
  glossary_sha256: 3a9b85df8a952c312898acf08c8c1475f977410b078c334d48a095fde978e4f9
  translated_at: 2026-09-25T20:18:48Z
  reviewed_by: null
---

# Practical Cases of Risk Classification

The following examples illustrate **different legitimate ways of classifying applications** in SbD-ToE, demonstrating:

- direct application of the **E/D/I** model;
- impact of **data and regulatory context**;
- use of **conservative classification by operational criticality**;
- influence of **advanced automation (incl. AI)** where relevant.

The objective is not to find the “perfect classification”,  
but to **ensure the appropriate level of care and control**.

---

## 📝 Case 1 - Public E-commerce Platform {#-caso-1---plataforma-de-e-commerce-pública}

**Context**  
Online sales platform, with direct payments and integration with third parties.

- **Exposure (E)**: Public (web + mobile app) → **3**  
- **Data Type (D)**: Personal data + payment data → **3**  
- **Impact (I)**: Financial, reputational and legal → **3**

**Classification:**  
**E + D + I = 9 → L3 (High Risk)**

**Rationale**  
Even without considering past incidents, the combination of public exposure, sensitive data and direct business impact justifies **maximum rigour**.

**Practical implications**:
- Complete and traceable security requirements  
- Formal threat modelling  
- Continuous SBOM and SCA  
- Continuous DAST, fuzzing and regression validation  

---

## 📝 Case 2 - Internal Hospital HR Portal {#-caso-2---portal-interno-de-rh-hospitalar}

**Context**  
Internal application, accessible only on the hospital network, used for HR management.

- **Exposure (E)**: Internal → **1**  
- **Data Type (D)**: Clinical and financial data of staff → **3**  
- **Impact (I)**: Legal (GDPR), sensitive confidentiality → **3**

**Classification:**  
**E + D + I = 7 → L3 (High Risk)**

**Rationale**  
Low exposure **does not offset** the nature of the data or the legal impact.  
This is a classic example of a common error avoided by the SbD-ToE model.

**Important note**  
This case demonstrates that:
> *“internal” does not mean “low risk”*.

---

## 📝 Case 3 - B2B Invoicing System {#-caso-3---sistema-de-faturação-b2b}

**Context**  
System used by authenticated business customers, with ERP integration.

- **Exposure (E)**: Authenticated external access → **2**  
- **Data Type (D)**: Financial and customer data → **2**  
- **Impact (I)**: Operational and financial → **2**

**Classification:**  
**E + D + I = 6 → L2 (Medium Risk)**

**Rationale**  
Relevant system, but with manageable impact and no critical regulated data.

**Practical implications**:
- Formal but proportional security requirements  
- Simplified threat modelling  
- SCA with a severity policy  
- Regular, not continuous, security testing  

---

## 📝 Case 4 - Internal Task Management Tool {#-caso-4---ferramenta-interna-de-gestão-de-tarefas}

**Context**  
Simple application, used internally for task management.

- **Exposure (E)**: Internal → **1**  
- **Data Type (D)**: Non-sensitive → **1**  
- **Impact (I)**: Low → **1**

**Classification:**  
**E + D + I = 3 → L1 (Low Risk)**

**Rationale**  
Low exposure, low impact and the absence of sensitive data justify minimal controls.

**Practical implications**:
- Linters and basic code review  
- General security good practices  
- No requirement for advanced testing  

---

## 📝 Case 5 - Core Service with Critical DRP (Conservative Classification) {#-caso-5---serviço-core-com-drp-crítico-classificação-conservadora}

**Context**  
Central business service, classified as **Critical in the DRP**:

- RTO < 1h  
- RPO ≈ 0  
- An outage halts the organisation's operations  

**Strict technical analysis**:
- Controlled exposure  
- Moderately sensitive data  

**Decision adopted**:
- **Direct classification as L3**, by operational criticality

**Rationale**  
Even if the technical risk could be L2, the cost of failure justifies  
**treatment as a high-risk application**.

> This is an explicit example of *deliberate over-classification*,  
> accepted and recommended in SbD-ToE.

---

## 📝 Case 6 - Application with Advanced Automation (incl. AI) {#-caso-6---aplicação-com-automação-avançada-incl-ia}

**Context**  
Internal application that uses assistive automation to:
- generate code,
- approve configuration changes,
- execute actions with real impact.

- **Exposure (E)**: Internal, but with external integrations → **2**  
- **Data Type (D)**: Code, configurations, occasional secrets → **2**  
- **Impact (I)**: Automatic changes with real effect → **3**

**Classification:**  
**E + D + I = 7 → L3 (High Risk)**

**Rationale**  
The classification **is not high because of “using AI”**,  
but because there is:
- delegation,
- speed,
- and impact without mandatory human validation.

---

## 📌 Conclusion {#-conclusão}

These examples demonstrate that:

- risk classification **is not mechanical**;
- SbD-ToE accepts conservative and pragmatic decisions;
- the ultimate objective is always:
  > **to apply the right level of care, control and validation**.

The coherence of the model lies in **proportionality**,  
not in an obsession with the perfect score.
