---
id: riscos-processo-arquitetura
title: Process Risks in Software Architecture
description: Identification and mitigation of the risks inherent to the architectural decision process
tags: [tipo:addon, tema:arquitetura, risco-processo, decisao, baseline, dependencias, drift]
sidebar_position: 8
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/addon/08-riscos-processo-arquitetura.md
  source_sha256: e78facc68fe87eb5f71cac06ad463c750d87364b1e7cad706457f8e20947d5b7
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 0f4a7ff42bb3776d80d579fe7c73dd4e28c0f6814dff592c9a37d9a649a4bebc
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, requirement_runtime, sbdtoe_sbd, threat, validation_evaluation]
  glossary_sha256: 4e45e4a3856e347ddafee8ea81fcbbcb8a07fa6c89059b8ec8673aeeb43fa7a5
  translated_at: 2026-09-26T08:32:07Z
  stamped_at: 2026-09-26T18:33:36Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Process Risks in Software Architecture

The architecture of a system is the result of a **set of technical decisions** that determine its structure, security properties, capacity to evolve and operational impact.

Regardless of the architectural style, technology or domain, the **architectural decision process** is subject to risks of its own which, if not explicitly addressed, compromise the security of the delivered system.

---

## 1. Architecture as drawing vs architecture as decision {#1-arquitetura-como-desenho-vs-arquitetura-como-decisão}

A recurring risk is treating architecture as a technical drawing exercise (diagrams, boxes and arrows), instead of an explicit decision process.

Typical consequences:
- absence of owners for the decisions;
- impossibility of justifying the accepted trade-offs;
- difficulty in reassessing decisions when the context changes.

In SbD-ToE, **architecture is decision**, and must be treated as such.

**Relates to.** Violates `ARC-004`; materialises `MT-065`.

---

## 2. Architectural decisions without an explicit owner {#2-decisões-arquiteturais-sem-responsável-explícito}

Architectural decisions without a clear *owner* introduce:
- ambiguity of responsibility;
- difficulty of auditing;
- risk of architectural drift over time.

Every relevant architectural decision must have an identified owner and an approval date/context.

**Relates to.** Violates `ARC-004`; no linkable threat in the current catalogue.

---

## 3. External dependencies treated as neutral infrastructure {#3-dependências-externas-tratadas-como-infraestrutura-neutra}

External services, managed platforms, third-party APIs or components outside the organisation's direct control **are architectural decisions**, not mere implementation details.

Associated risks:
- dependency on third parties as a *single point of failure*;
- exposure of data and metadata;
- limitations on control, audit and exit (*exit strategy*).

Accepting an external dependency must be treated as an **explicit architectural decision**.

**Relates to.** Violates `ARC-004`; no linkable threat in the current catalogue.

---

## 4. Implicit data flows not modelled {#4-fluxos-de-dados-implícitos-não-modelados}

Beyond the explicit functional flows, modern architectures generate implicit flows, such as:
- logs;
- metrics;
- telemetry;
- observability events and signals.

Ignoring these flows leads to:
- inadvertent exposure of sensitive data;
- non-compliance with retention and minimisation requirements;
- gaps in the threat analysis.

These flows are part of the architecture and must be treated as such.

**Relates to.** Violates `ARC-008`; no linkable threat in the current catalogue.

---

## 5. Opaque or non-deterministic components {#5-componentes-opacos-ou-não-determinísticos}

Components whose behaviour:
- is not fully predictable,
- depends on external state,
- or is not fully observable,

introduce additional architectural risk.

The architecture must provide for:
- containment of impact;
- validation of critical outputs;
- safe degradation mechanisms;
- sufficient observability to detect deviations.

**Relates to.** No linkable requirement in the current catalogue; materialises `MT-062`.

---

## 6. Uncritical reuse of previous architectures {#6-reutilização-acrítica-de-arquiteturas-anteriores}

Reusing existing architectures is common practice, but it becomes risky when:
- the context has changed;
- the risk profile is different;
- new dependencies or flows have been introduced.

Inherited architectures must be treated as **initial hypotheses**, not as validated truths.

**Relates to.** Violates `ARC-007`; materialises `MT-064`.

---

## 7. Divergence between documented architecture and real architecture {#7-divergência-entre-arquitetura-documentada-e-arquitetura-real}

When the documented architecture does not reflect the system actually implemented:
- decisions become invalid;
- threats are no longer covered;
- the evidence loses its value.

This risk requires periodic review mechanisms and explicit architectural *gates*.

**Relates to.** Violates `ARC-013`; materialises `MT-069`.

---

## 8. Implications for SbD-ToE {#8-implicações-para-o-sbd-toe}

SbD-ToE assumes that:
- architectural decisions are fallible;
- architectural process risks must be explicitly addressed;
- mitigation requires human decision, validation and verifiable evidence.

The decision and evidence criteria are defined in this chapter's architectural decision file.
