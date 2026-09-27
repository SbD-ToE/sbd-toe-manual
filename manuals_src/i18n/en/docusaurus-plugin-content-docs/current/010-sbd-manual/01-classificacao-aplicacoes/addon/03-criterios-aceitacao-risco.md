---
id: criterios-aceitacao-risco
title: Risk Acceptance Criteria
sidebar_position: 3
tags: [tipo:criterios, aceitacao, excecao, rastreabilidade]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/addon/03-criterios-aceitacao-risco.md
  source_sha256: 77273d8cfae5f340fb6c72e258d2d478d7f8686ed87d1f75fc41a087a6ea943f
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 6f2501aa07c9c6da52476dd474ad881e448f84ac43d6ed0c490352463759a207
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [avaliacao, deterministic, evidenciabilidade, maturity, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: 94651bac05151f3c8b48eca533f8a62e9f908158e80885f31ecab73ca560e116
  translated_at: 2026-09-25T20:18:45Z
  stamped_at: 2026-09-26T18:32:44Z
  reviewed_by: null
---

<!--template: sbdtoe-core -->

# Risk Acceptance Criteria

Formal risk acceptance is a fundamental step in the risk management process and must be supported by **clear, objective and documented criteria**.

In *Security by Design – Theory of Everything (SbD-ToE)*, accepting risk **does not mean ignoring it**, but explicitly assuming that, under the current conditions, the residual risk is considered tolerable for the application's criticality level.

This file defines the **minimum criteria** for risk acceptance, aligned with the SbD-ToE model and with the **L1–L3** application levels.

---

## 🧠 Fundamental principle {#-princípio-fundamental}

A risk **may only be accepted** when:

- its **attributes are understood**;
- the **applied controls are known and verifiable**;
- there is **sufficient evidence** of their effectiveness;
- the residual impact is **compatible with the application's level**.

Whenever these assumptions do not hold, risk acceptance **is not valid**, regardless of urgency, cost or the team's maturity.

---

## 📌 Assessment parameters {#-parâmetros-para-avaliação}

The risk acceptance decision must consider, at a minimum:

- **Residual value of the risk** (after applying controls);
- **Criticality level of the application** (L1, L2 or L3);
- **Type of associated impact** (business, legal, operational, reputational);
- **Confidence in the existing controls**, including their verifiability;
- **Reversibility of the impact** or rollback capability;
- **Availability of contingency plans**;
- **Objective evidence** supporting the assessment carried out.

---

## ⚖️ Acceptance thresholds by level {#️-limiares-de-aceitação-por-nível}

| Application level         | Maximum Acceptable Residual Risk | Notes                                     |
| -------------------------- | ------------------------------- | ----------------------------------------------- |
| **L1** (low criticality) | ≤ 9 (medium)                     | Informal acceptance possible                     |
| **L2** (medium criticality) | ≤ 6 (low to medium)             | Requires formal validation and recording               |
| **L3** (high criticality)  | ≤ 4 (low)                     | Exception only with risk manager approval |

> 📌 These thresholds assume **effective control and adequate evidence**.  
> Absence of evidence automatically invalidates the acceptance.

---

## 🧩 Additional conditions in automation and decision-support contexts {#-condições-adicionais-em-contextos-de-automação-e-apoio-à-decisão}

The use of automation or decision support (including AI) **does not by itself invalidate** risk acceptance.

However, acceptance **becomes conditional** when such mechanisms change relevant attributes of the risk, namely when they:

- **reduce the detectability** of errors or failures;
- **diminish the evidentiability** of decisions;
- **introduce relevant non-determinism**;
- **carry out actions with real impact** without mandatory human validation.

### ❌ Situations in which risk acceptance **is not permitted** {#-situações-em-que-a-aceitação-de-risco-não-é-permitida}

It is not acceptable to accept risk when:

- automated decisions or actions with real impact are applied **without effective human review**;
- the results are not reproducible or cannot be validated independently;
- there is no clear evidence that the controls work correctly;
- the potential impact is significant in legal, regulatory or reputational terms;
- the risk falls within an **L3** application and depends exclusively on implicit trust in the automated mechanism.

---

## 🧾 Examples of valid formal acceptance criteria {#-exemplos-de-critérios-formais-de-aceitação-válidos}

Acceptance may be considered when, cumulatively:

- the residual risk is assessed as **low** by at least two independent profiles (e.g. AppSec + Product Owner);
- **compensating controls** are active and monitored;
- the impact is **strictly internal and operational** and a validated recovery plan exists;
- the automation is **assistive**, with mandatory human validation before any real effect;
- the decision is **documented**, with an identified responsible person and a **defined review date**.

---

## 🏡 Recommended acceptance process {#-processo-recomendado-de-aceitação}

1. **Clear identification** of the risk and its relevant attributes.
2. Validation of the applied controls and the available evidence.
3. Assessment of the residual risk against the L1–L3 thresholds.
4. Formal decision to accept, reject or further mitigate.
5. Recording of the decision, including rationale, responsible person and review date.
6. Mandatory reassessment whenever relevant changes occur.

---

## 📌 Final recommendations {#-recomendações-finais}

- Formalise an **application risk acceptance policy**, with defined roles and responsibilities.
- Integrate acceptance decisions into the **release and governance artefacts**.
- Record accepted risks in a repository with **GRC visibility**.
- Never accept risk **without sufficient evidence**, regardless of the application's level.

> Risk acceptance is not an abdication of responsibility,  
> but a **conscious, informed and traceable decision**.
