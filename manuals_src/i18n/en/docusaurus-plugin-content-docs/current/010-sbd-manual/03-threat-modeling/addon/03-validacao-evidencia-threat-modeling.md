---
id: validacao-evidencia-threat-modeling
title: Validation and Evidence in Threat Modelling
description: Acceptance criteria, human validation and minimum evidence for threat models
tags: [threat-modeling, validacao, evidencia, decisao]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/addon/03-validacao-evidencia-threat-modeling.md
  source_sha256: 3377b7642849840d4f077ba05f9c0d6a9f4c1bce3a4af86045cd32d03ba18eb8
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: cf3bce9d0ea472970827106278c6c6592845ffa77cbe4b78abac09bca7e18555
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, risk_level, role_tech_lead, threat, validation_evaluation]
  glossary_sha256: 2c86ba03a9e956247082f8844d8d6ef0b935a07ddc45929c43922f00572f30ae
  translated_at: 2026-09-25T20:16:58Z
  stamped_at: 2026-09-26T18:33:18Z
  reviewed_by: null
---

# Validation and Evidence in Threat Modelling

A threat model is only operationally valid when:
- it has been explicitly validated;
- it has an identified person responsible for it;
- it produces verifiable evidence.

Without these elements, Threat Modelling remains an exploratory activity, not a security control.

---

## 1. Mandatory human validation {#1-validação-humana-obrigatória}

Every threat model must be:
- critically reviewed;
- approved by an explicit role (e.g. Tech Lead, Security Architect).

Tools, methods or analytical aids **do not replace this decision**.

---

## 2. Minimum acceptance criteria {#2-critérios-mínimos-de-aceitação}

A Threat Model is considered accepted when, at a minimum:

- the system context is clearly defined;
- the analysed architecture is identified and versioned;
- the main threats have been identified and classified;
- each threat has an associated decision:
  - mitigated,
  - accepted,
  - transferred,
  - or rejected with justification.

---

## 3. Minimum mandatory evidence {#3-evidência-mínima-obrigatória}

The evidence associated with a Threat Model must include, at a minimum:

- versioned architectural diagram(s);
- a list of threats with an explicit decision;
- a clear link to security requirements or mitigations;
- identification of the person responsible for validation;
- date and version of the model.

The evidence must be:
- reproducible;
- auditable;
- preserved in accordance with the organisation's policies.

---

## 4. Distinction between support and decision {#4-distinção-entre-apoio-e-decisão}

It is mandatory to distinguish explicitly between:
- artefacts that support the analysis;
- the validated threat model.

Only the latter constitutes the basis for:
- defining requirements;
- risk acceptance;
- auditing.

---

## 5. Review and invalidation {#5-revisão-e-invalidação}

A threat model must be reviewed whenever there is:

- a significant change to the architecture;
- the introduction of new dependencies;
- a relevant change in the data flow;
- a reclassification of the risk level (L1–L3).

Models that have not been reviewed must be considered **potentially invalid**.

---

## 6. Integration with other chapters {#6-integração-com-outros-capítulos}

Validated Threat Modelling constitutes:
- direct input to Chapter 02 - Security Requirements;
- the basis of justification for architectural decisions;
- evidence of application proportional to the risk defined in Chapter 01.
