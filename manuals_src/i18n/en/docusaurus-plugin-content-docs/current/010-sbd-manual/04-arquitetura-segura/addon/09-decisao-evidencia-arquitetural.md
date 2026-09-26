---
id: decisao-evidencia-arquitetural
title: Architectural Decision and Evidence
description: Decision, validation and minimum evidence criteria for secure architecture, including the architectural baseline model and invalidation conditions
tags: [tipo:addon, tema:arquitetura, decisao, evidencia, ADR, baseline, rastreabilidade]
sidebar_position: 9
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/addon/09-decisao-evidencia-arquitetural.md
  source_sha256: fa9417fb0799e559e8d8e5815dd9e93d62ba6f83726aeb4aedb31133101ac74d
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: f7333ceb0db155e3e3260a02cae7e0a0c40e71f9ab81b97f322a3007e7342b14
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5536afdcc04f76a07c66e747133c73d68308884707c296abf945937a9630a312
  glossary_keys: [audit_trail, risk_level, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: aaa40ca4a9c92a4fb1be202d20bdd66809715d793c3e0a9e1ef04d05b54d55d2
  translated_at: 2026-09-26T08:32:07Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Architectural Decision and Evidence

An architecture is only operationally valid when its decisions:
- are explicit;
- have an identified owner;
- produce verifiable evidence;
- can be reviewed or invalidated.

Isolated diagrams or descriptions **do not constitute an architectural decision**.

---

## 1. What constitutes an architectural decision {#1-o-que-constitui-uma-decisão-arquitetural}

An architectural decision is any technical choice that:
- affects security, isolation or trust properties;
- introduces or removes external dependencies;
- conditions security requirements or threat mitigation;
- is costly or difficult to reverse.

Purely local implementation details do not, by themselves, constitute architectural decisions.

---

## 2. Minimum acceptance criteria for a decision {#2-critérios-mínimos-de-aceitação-de-uma-decisão}

An architectural decision is considered valid when, at a minimum:

- the context and the problem are clearly described;
- the main alternatives have been identified;
- the decision taken is explicit;
- the accepted trade-offs are documented;
- there is a link to threats (Ch. 3) and requirements (Ch. 2);
- there is an identified owner for the decision.

---

## 3. Minimum mandatory evidence {#3-evidência-mínima-obrigatória}

The evidence associated with architectural decisions must include:

- a decision record (e.g. ADR or equivalent);
- versioned architectural diagrams;
- a reference to the version of the system/context;
- a link to the relevant threats and requirements;
- date and owner of the approval.

The evidence must be:
- versioned;
- reproducible;
- auditable.

---

## 4. Architectural baseline {#4-baseline-arquitetural}

The set of approved decisions constitutes the system's **architectural baseline**.

The baseline:
- is valid only for the approved context/versioning;
- serves as a reference for development, testing and operation;
- must be easily identifiable and consultable.

---

## 5. Invalidation and review of decisions {#5-invalidação-e-revisão-de-decisões}

An architectural decision must be reviewed or invalidated when there is:

- a significant change to the architecture;
- the introduction of new external dependencies;
- a relevant change in the data flows;
- a reclassification of the risk level (L1–L3);
- the identification of new critical threats.

Decisions that have not been reviewed must be considered **potentially invalid**.

---

## 6. Integration with other chapters {#6-integração-com-outros-capítulos}

Architectural decisions:
- materialise the mitigation of threats identified in Ch. 3;
- justify requirements of Ch. 2;
- condition development, testing and operation practices.

The absence of an explicit link compromises the coherence of the SbD-ToE model.
