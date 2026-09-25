---
id: risco-residual
title: Residual Risk Analysis and Acceptance Decision
sidebar_position: 4
tags: [tipo:analise, risco-residual, aceitacao, excecao]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/addon/04-risco-residual.md
  source_sha256: 0a28d24e5e2c536e1bd985a90ad9521822d035168207f6bd7640117f5644d460
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 295a95f5c01108b92de158de99da3eacd7c59bda78657600318e34debf778c93
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [audit_trail, avaliacao, chapter_role, cycle_iteration, deterministic, evidenciabilidade, lifecycle_phase, normative_empirical, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: 8a93efebc29d9782994bae6f41b6786c9df4b338680af658bf90836ec30e6012
  translated_at: 2026-09-25T20:18:45Z
  reviewed_by: null
---

<!--template: sbdtoe-core -->

# Residual Risk Analysis

**Residual risk** is the risk that **remains after the effective application of the defined controls**, and it is the factual basis for any conscious decision to accept, further mitigate or reject.

In *Security by Design – Theory of Everything (SbD-ToE)*, residual risk **is not an abstract value**, but the result of a contextual assessment that considers:
- the criticality level of the application (L1–L3),
- the **attributes of the risk**,
- the **actual effectiveness of the controls**,
- and the **available evidence**.

This file complements the risk classification and acceptance model by introducing the logic of **“before and after controls”**, in an operational and auditable way.

---

## 🔢 Fundamental definitions {#-definições-fundamentais}

- **Gross (inherent) Risk**  
  Risk identified **before the application of controls**, resulting from the combination of exposure, data and impact.

- **Residual Risk**  
  Risk remaining **after the effective application of controls**, considering:
  - actual reduction of impact,
  - increase in detectability,
  - improvement in evidentiability,
  - and limitation of reach or surface.

- **Acceptable Risk**  
  Maximum limit of residual risk tolerated by the organisation, depending on the application's level (L1–L3).

> 📌 In SbD-ToE, residual risk **does not result from a simple mathematical subtraction**, but from a **conscious reassessment of the attributes of the risk after control**.

---

## 🧠 Relationship with the E/D/I model {#-relação-com-o-modelo-edi}

Residual risk analysis must always be consistent with the application's **E/D/I** classification:

- controls **do not retroactively change the exposure or the data processed**;
- controls may:
  - reduce impact,
  - limit the likelihood of exploitation,
  - increase detection,
  - and improve evidence.

Whenever the application of controls **does not materially change the relevant attributes of the risk**, the residual risk **remains high**, even if “theoretical” controls exist.

---

## 🧩 Practical assessment of residual risk {#-avaliação-prática-do-risco-residual}

The assessment of residual risk must explicitly answer the following questions:

- Are the controls **implemented and active**?
- Is their effectiveness **verifiable and evidentiable**?
- Is there **effective human validation**, where applicable?
- Is the residual behaviour **deterministic and reproducible**?
- Is the residual impact **compatible with the application's level**?

The absence of a positive answer to any of these questions **prevents valid acceptance of the risk**.

---

## 📝 Illustrative example (non-normative) {#-exemplo-ilustrativo-não-normativo}

**Scenario:** Exposed API with strong authentication

| Dimension assessed            | Before controls | After effective controls                  |
|-----------------------------|---------------------|------------------------------------------|
| Exposure (E)               | 3                   | 3 (remains exposed)                    |
| Data Type (D)           | 2                   | 2                                        |
| Impact (I)                 | 3                   | 2 (abuse limitation, rate limiting)    |
| Detectability              | Low               | High (alerts, logging)                  |
| Evidentiability           | Limited            | High (logs, metrics)                 |

👉 The residual risk is **reduced**, but **not eliminated**.  
Its acceptance depends on the application's level and on the available evidence.

---

## ⚖️ Role of residual risk in the decision {#️-papel-do-risco-residual-na-decisão}

Residual risk must be compared with the **acceptance thresholds defined by application level**:

| Application Level         | Maximum Acceptable Residual Risk |
|---------------------------|----------------------------------|
| **L1** (low criticality) | up to 9                            |
| **L2** (medium criticality) | up to 6                            |
| **L3** (high criticality)  | up to 4                            |

> 📌 These values **assume adequate evidence and effective control**.  
> Without sufficient evidence, residual risk **cannot be considered low**, regardless of the estimated value.

---

## ❌ Situations in which residual risk **is not acceptable** {#-situações-em-que-o-risco-residual-não-é-aceitável}

It is not acceptable to consider residual risk tolerable when:

- the controls are not demonstrably active;
- the decision depends exclusively on implicit trust in automation or tooling;
- the results are not reproducible or verifiable;
- there is significant legal, regulatory or reputational impact;
- the application is **L3** and the residual risk depends on non-deterministic validation.

---

## 🔄 Integration with the lifecycle and with GRC {#-integração-com-o-ciclo-de-vida-e-com-grc}

- Residual risk must be **reassessed whenever a relevant change occurs** in:
  - architecture,
  - data,
  - exposure,
  - automation or process.
- It must integrate:
  - release gates,
  - security review artefacts,
  - and GRC systems with explicit thresholds.
- Residual risk **is not permanent**: it has a deadline, a context and responsible persons.

---

## 📌 Final recommendation {#-recomendação-final}

Every residual risk acceptance decision must be:

- **formally recorded**;
- **justified with technical evidence**;
- **compatible with the application's level**;
- **time-limited and subject to reassessment**.

> Residual risk is not an “inevitable remainder”,  
> it is a **conscious decision about what the organisation is willing to take on, here and now**.
