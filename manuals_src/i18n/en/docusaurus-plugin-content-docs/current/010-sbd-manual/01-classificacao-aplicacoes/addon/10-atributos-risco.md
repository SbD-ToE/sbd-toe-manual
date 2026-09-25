---
id: atributos-risco
title: Risk Attributes
description: Unified model for characterising risk in SbD-ToE, applicable to technical and process risks
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/addon/10-atributos-risco.md
  source_sha256: 4c044b91fcd95376d775fd21dd9383d6b23cd16ee9841ce7c11bd38a16455296
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: a52c5a2e2f6f99b012db2e2577cc89fe15a5f299f3dcb7cd7649789f42a37932
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [audit_trail, cycle_iteration, deterministic, evidenciabilidade, lifecycle_phase, normative_empirical, practitioner_manual, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: 84ab9dbdb7294b9a1ffe5e19bbf578b2a80fd0005dc94404e2a267dfab7c6686
  translated_at: 2026-09-25T20:18:48Z
  reviewed_by: null
---

## 🎯 Objective {#-objetivo}

This document defines a **unified model for characterising risk** in the context of **Security by Design – Theory of Everything (SbD-ToE)**.

The objective **is not to create distinct categories of risk** (e.g. “technical risk” vs. “process risk”), but rather to establish a **set of internal attributes** that make it possible to:

- describe any relevant risk rigorously;
- understand its origin and its mechanism of materialisation;
- determine **proportional requirements, controls and validations**;
- keep the model **timeless**, extensible and technologically neutral.

This model applies to the **entire application lifecycle** and to **every chapter of the Manual**.

---

## 🧠 Fundamental principle {#-princípio-fundamental}

In SbD-ToE, **risk is treated as a single, indivisible concept**.

A risk may have a technical, process, organisational or external origin, but **its impact always materialises in the delivered system**, in its operation or in its compliance.

What varies **is not the type of risk**, but rather:
- **how it arises**;
- **how it manifests**;
- **how it can (or cannot) be observed, validated and mitigated**.

These variations are captured through **risk attributes**.

---

## 🧩 Risk attribute model {#-modelo-de-atributos-do-risco}

Each risk identified within the scope of SbD-ToE must be described, explicitly or implicitly, through the attributes below.

### 1️⃣ Origin of the risk {#1️⃣-origem-do-risco}

Identifies **where the risk is introduced** into the system or the process.

Typical values (non-exclusive):
- Technical (architecture, code, configuration)
- Process (decision, omission, automation)
- Organisational (governance, responsibilities)
- External (suppliers, dependencies, services)

> Example:  
> An error introduced by automatic code generation has a **process origin**, even if it materialises as a technical vulnerability.

---

### 2️⃣ Mechanism of introduction {#2️⃣-mecanismo-de-introdução}

Describes **how the risk is introduced**.

Common examples:
- Known technical vulnerability
- Human error
- Omission of analysis or validation
- Inadequate decision
- Excessive trust in automated results
- Implicit or inherited configuration

This attribute is critical for defining **preventive vs. detective controls**.

---

### 3️⃣ Surface of materialisation {#3️⃣-superfície-de-materialização}

Indicates **where the impact manifests** when the risk materialises.

Typical values:
- Product (software, data, interfaces)
- Operation (availability, integrity, continuity)
- Compliance (legal, regulatory, contractual)
- Reputation / business

The same risk may materialise on **more than one surface**.

---

### 4️⃣ Detectability {#4️⃣-detetabilidade}

Characterises **how easily the risk can be identified** before or after its materialisation.

- High – easily detectable by tests or objective controls
- Medium – requires specialised analysis or correlation
- Low – hard to observe without incidents or in-depth audits

Risks with low detectability require **stronger upstream controls**.

---

### 5️⃣ Reproducibility {#5️⃣-reprodutibilidade}

Indicates whether the behaviour associated with the risk is:

- Deterministic – consistently reproducible
- Partially deterministic – context-dependent
- Non-deterministic – variable results for the same input

This attribute is particularly relevant in contexts of:
- advanced automation;
- decision-support systems;
- heuristics-based analysis.

Low reproducibility **increases operational and validation risk**.

---

### 6️⃣ Evidentiability {#6️⃣-evidenciabilidade}

Describes **the degree to which the risk and its mitigation can be supported by verifiable evidence**.

- High – objective, versioned and auditable evidence
- Limited – indirect or interpretative evidence
- Weak – based on plausibility or implicit trust

In SbD-ToE, **a risk without adequate evidence cannot be considered mitigated**, regardless of the sophistication of the analysis.

---

## 🧪 Illustrative example (non-normative) {#-exemplo-ilustrativo-não-normativo}

A risk identified through an AI-assisted analysis can be characterised as:

- Origin: Process  
- Mechanism: Assisted decision with insufficient validation  
- Surface: Product and compliance  
- Detectability: Medium  
- Reproducibility: Low  
- Evidentiability: Limited  

👉 The consequence **is not to reject the tool**, but to **require additional controls**, such as:
- explicit human review;
- independent empirical validation;
- recording of the decision and of the evidence used.

From the model's point of view, this example is equivalent to:
- a misconfigured ORM;
- a CI pipeline with implicit gates;
- a scanner with excessively permissive rules.

---

## 🔗 Relationship with other elements of SbD-ToE {#-relação-com-outros-elementos-do-sbd-toe}

- The **L1–L3 classification** continues to reflect **the impact and criticality of the system**, not the internal attributes of the risk.
- The **risk attributes** influence:
  - security requirements (Ch. 02);
  - threat modelling (Ch. 03);
  - architectural decisions (Ch. 04);
  - acceptance and evidence criteria;
  - governance and audit (Ch. 14).

This model allows the Manual to evolve **without needing to redefine base concepts** whenever new forms of automation or abstraction emerge.

---

## ✅ Conclusion {#-conclusão}

SbD-ToE treats risk as a **single concept**, rich in attributes, capable of capturing both classic technical risks and risks introduced by modern development practices.

This approach:
- avoids conceptual fragmentation;
- supports the proportional definition of controls;
- keeps the Manual timeless;
- reinforces the demand for responsibility, validation and evidence.

The following chapters assume this model as a **canonical premise**.
