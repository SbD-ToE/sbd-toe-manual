---
id: governanca-legada
title: Governance in Legacy Systems
sidebar_position: 10
description: Strategies for applying formal security governance to legacy systems and contracts
tags: [legado, governanca, excecoes, migração]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/addon/10-governanca-legada.md
  source_sha256: 3c75491d5635ba9f0a1bb28d92eb4242a66d3f0996d60d4c2bd5a366b5b30e4f
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: ba9b675eabdd5ba33cfa6f43686987227c644351e28b341b7157d52d0a772094
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [cycle_iteration, maturity, risk_level, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: 6dd9db856b0e29a2fdf7f28064521de7fcea738f04c6692f6ecf0f5737c392df
  translated_at: 2026-09-26T12:00:17Z
  stamped_at: 2026-09-26T18:36:17Z
  reviewed_by: null
---


# Governance of Legacy Systems and Non-Compliant Contexts

This document addresses the proportional and adapted application of the SbD-ToE model to **legacy systems, old pipelines, pre-existing contracts or organisational contexts where full control is not immediate or feasible**.

---

## 🌟 Objective {#-objetivo}

* To allow legacy projects to be framed within a structured governance model;
* To guarantee visibility, traceability and compensations even when it is not possible to apply all the requirements;
* To avoid silent exceptions that put the coherence of the SbD-ToE model at risk.

---

## 🧰 Typical contexts {#-contextos-típicos}

* Inherited critical applications without technical documentation or active owners;
* Old CI/CD pipelines, operational but outside the control of the AppSec team;
* Contracts in force with suppliers that do not meet the minimum requirements;
* Shared libraries or modules without security review.

---

## 🛠️ Proposed approach {#️-abordagem-proposta}

1. **Identify and classify the legacy asset** (using the criteria of Ch. 1);
2. **Map the applicable requirements**, even if not met;
3. **Analyse the feasibility of the technical application of controls**;
4. **Record formal exceptions**, where applicable, with:
   * Business justification
   * Acknowledged risks
   * Proposed compensations
   * Validity and reassessment plan

5. **Include the asset in the continuous review cycle** (`addon/06-validacao-continuada.md`)

---

## 📋 Example of a legacy governance record {#-exemplo-de-registo-de-governação-de-legado}

| Field                    | Value                                                |
| ------------------------ | ---------------------------------------------------- |
| System                  | Internal DataBroker                                   |
| Risk level           | L3                                                   |
| Requirements not met | EX-AUD-002, LOG-003                                  |
| Justification             | Core system dependent on pre-existing architecture |
| Compensations             | Monitoring by external SIEM + access control  |
| Owner                    | joana.sousa\@empresa                                 |
| Scheduled reassessment     | 6 months (future integration with a new project)         |

*Illustrative identifiers (`EX-…`); they do not correspond to the Requirements Catalogue of Ch. 02.*

---

## ✅ Recommendations {#-recomendações}

* Never ignore legacy assets: treat them as a formal exception with traceability;
* Incorporate the cycle of review and continuous improvement;
* Monitor compensations and document deviations transparently;
* Include these cases in the **maturity and governance KPIs**.

---

## 🔗 Cross-links {#-ligações-cruzadas}

* Ch. 1 - Risk classification
* Ch. 2 - Minimum requirements by risk
* `addon/01-modelo-governancao.md` - Decision and exceptions model
* `addon/06-validacao-continuada.md` - Continuous validation
* Ch. 08 / 09 - Integration with pipelines and isolated execution

---
