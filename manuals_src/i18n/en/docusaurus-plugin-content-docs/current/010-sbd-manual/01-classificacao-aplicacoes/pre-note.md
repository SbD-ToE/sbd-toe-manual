---

id: pre-note
title: ℹ️ Rationale
description: Why — determining the criticality of applications in order to apply proportionality in security controls
tags: [base, classificacao, risco, proporcionalidade, ciclo-vida]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/pre-note.md
  source_sha256: f6516c186dcdcbc34bc00bd1d4b34312a64d473604d31fa6f0ad3cf1dbbffe0b
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: db99375169926d279b60e161d33d87ea31add040d9d9b3fddb54b3d7da552226
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: f3ae07385fc10c458f9087ea5ea231fd2bbf0e4852b0e4c0e84ec84618762443
  glossary_keys: [chapter_role, cycle_iteration, gap_family, lifecycle_phase, maturity, normative_empirical, practitioner_manual, risk_level, traceability]
  glossary_sha256: 8430814a5bf3a5b07ecdaa5e69c9512f9cb407414f5d9da0318879386c60409e
  translated_at: 2026-09-25T17:59:21Z
  reviewed_by: null
---

# Application Criticality Classification

The application criticality classification proposed in this chapter follows a **pragmatic, fast and iterative** approach, suited to agile contexts with a continuous lifecycle. It is especially useful in organisations where:

- There is a gap in formal risk management, or  
- The traditional GRC approach does not fit the reality of the application portfolio.

Why? Because there is not always alignment between the **level of detail required by GRC** and the **practical nature of software systems under development**. In many cases, the organisational risk model is too generic or too complex to support agile decisions in the context of development teams.

> This proposal, compatible with the concept of *risk categorisation*, is fully aligned with the **Risk Management** domain of **OWASP SAMM**, with the principles of **DSOMM**, **SSDF (RM.1)**, **ISO 27005** and **SLSA**, ensuring integration with widely accepted maturity models.

It is important to stress: **this approach does not replace formal methods** of risk analysis (such as ISO 27005, NIST 800-30 or FAIR). The objective is to ensure that **every application receives, from the outset, a clear and justifiable decision about its risk level**, avoiding two frequent scenarios:

- **Under-engineering**: exposed applications without minimum controls;
- **Over-engineering**: excessive, unnecessary control, with wasted effort.

This initial classification makes it possible to apply security practices with **proportionality, traceability and a focus on concrete action**.

Where **previously defined organisational artefacts** exist - such as a BIA (Business Impact Analysis), a DRP (Disaster Recovery Plan), a BCP (Business Continuity Plan) or other forms of categorisation - **these can (and should) be used as the factual basis for the classification**. Even if they are not exact, they offer a valid and sufficient reference, as described in [Alternative - adoption of DRP, BIA or other Existing Classifications](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia).

## 🎯 Proposed model: simple, participatory and pragmatic {#-modelo-proposto-simples-participativo-e-pragmático}

This manual proposes an **empirical and simplified** classification model, inspired by the **OWASP Risk Rating** but adapted to practical contexts where a fast decision is essential. The model rests on three main axes:

- **E (Exposure)**: external accessibility and attack vectors;
- **D (Data Type)**: sensitivity, privacy and regulatory framing;
- **I (Potential Impact)**: technical, operational and reputational consequences in the event of failure or breach.

This model is influenced by widely recognised approaches:

- **OWASP SAMM** - *Threat Assessment* domain, especially activity A.2 (Assess Risk);
- **OWASP Risk Rating Methodology** - based on impact and likelihood;
- **NIST 800-30** and **ISO 27005** - which underpin formal risk analysis methodologies.

However, a **more accessible and pragmatic** approach is assumed here, one that favours:

- Speed of application (a few minutes per application);
- Direct participation of technical and business stakeholders;
- Empirical, iterative decisions that are easy to review over time.

> ⚠️ This classification serves only as a starting point. Whenever possible, there must be a **formal link to the organisational risk management process**.  
> Where no such process exists, or it is not suited to the application context, this approach serves as a viable and effective alternative.

As detailed in [Classification Model](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/modelo-classificacao-eixos), classification per application is done by assigning **values between 1 and 3 on each axis**, based on the informed perception of the main stakeholders.

**How accessible is the application or system, given its network and interface context?**

|   |                                                    |
| - | -------------------------------------------------- |
| ☐ | Only accessible internally (no external access) |
| ☐ | Accessible externally, but with authentication       |
| ☐ | Public (open or unauthenticated access)         |

---

**How is the nature and criticality of the information processed classified?**

|   |                                                                        |
| - | ---------------------------------------------------------------------- |
| ☐ | Public data, with no sensitivity or legal impact                     |
| ☐ | Personal, identifiable or internally confidential data              |
| ☐ | Regulated or highly sensitive data (banking, health, location) |

---

**What impact would a breach have, in an extreme case, on the organisation?**

|   |                                                                        |
| - | ---------------------------------------------------------------------- |
| ☐ | Nil or irrelevant impact                                            |
| ☐ | Limited, reversible or narrow-reaching impact                      |
| ☐ | High impact: significant reputational, regulatory or financial consequences |

---
The Criticality value is determined by the sum of the empirical "qualitative quantification" of the 3 axes:
```md
Criticidade Total (C) = E + D + I
```

The arithmetic sum defines the application's criticality level:

| Sum | Classification | Risk Level |
| ---- | ------------- | -------------- |
| 3–4  | L1            | Low          |
| 5–6  | L2            | Medium          |
| 7–9  | L3            | High        |

> The classification must be reviewed by security, architecture or GRC, considering:
>
> * Regulatory cases;
> * External integrations;
> * Relevant technical contexts.

---
