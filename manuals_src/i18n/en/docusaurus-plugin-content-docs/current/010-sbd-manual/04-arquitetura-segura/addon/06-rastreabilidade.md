---
id: rastreabilidade-arquitetural
title: Architectural Traceability
description: Traceability model between ARC requirements, threats, architectural decisions and auditable evidence, with a matrix template and update criteria
tags: [tipo:addon, tema:arquitetura, ARC, rastreabilidade, ADR, evidencia, threat-modeling, L1, L2, L3]
sidebar_position: 6
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/addon/06-rastreabilidade.md
  source_sha256: c461f46db3863d4409542003c8bb25fcfd78d90aec44cde7355df8c9846fb640
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 55f62cf7012095f9130c5c8796835229aa496f2a4e1f4e17281201e7ff6dfee0
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, requirement_runtime, risk_level, threat, traceability, validation_evaluation]
  glossary_sha256: f41cc6fea7e3406fa75dd019f153870f69097a2e2cc29f2a885a67a56ac560b0
  translated_at: 2026-09-26T08:32:05Z
  stamped_at: 2026-09-26T18:33:34Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Architectural Traceability

Architectural traceability is the ability to demonstrate, verifiably, that every relevant security requirement has an associated design decision, an implemented control and auditable evidence.

Without traceability, an architecture may be correct but not *demonstrably* secure - which is insufficient in audit, compliance or post-incident analysis contexts.

---

## Traceability model {#modelo-de-rastreabilidade}

The model links five elements in a chain:

```
Ameaça (Cap. 03)  →  Requisito de arquitectura  →  Decisão (ADR)  →  Controlo implementado  →  Evidência
```

| Element | Description | Typical artefact |
|----------|-----------|-----------------|
| **Threat** | Threat identified in threat modelling (Ch. 03) - STRIDE, PASTA or equivalent | TM record, annotated DFD |
| **Architecture requirement** | Canonical requirement from this chapter's catalogue that mitigates the threat | `01-catalogo-requisitos.md` |
| **Decision (ADR)** | Architecture Decision Record documenting how the requirement is satisfied in the context of the project | `adr/ADR-xxxx.md`, decisions section in `solution-architecture.md` |
| **Implemented control** | The technical or procedural measure in force that gives effect to the decision | Network configuration, admission policy, review process |
| **Evidence** | Verifiable artefact that proves the control - versioned, reproducible and auditable | Versioned diagram, CI/CD log, review minutes, completed checklist |

---

## Traceability matrix template {#template-de-matriz-de-rastreabilidade}

The matrix can be kept as a Markdown table in the repository, as backlog items with labels, or as a section in `solution-architecture.md`. The format is secondary; the substance - a verifiable link between requirement, decision and evidence - is the determining criterion.

| ARC Req. | Name | Associated threat (Ch. 03) | Decision / ADR | Implemented control | Evidence | Status |
|----------|------|---------------------------|---------------|-----------------------|-----------|--------|
| ARC-001 | Trust zones identified | Spoofing, Information Disclosure | ADR-003 | C4 diagram with delimited trust boundaries | `docs/arch/trust-zones-v3.drawio` (rev. 2024-11) | Compliant |
| ARC-005 | Integrated threat modelling | Elevation of Privilege, Tampering | ADR-007 | STRIDE applied in a quarterly design session | `docs/tm/checkout-flow-2024-11.md` | Compliant |
| ARC-006 | Isolation between sensitive domains | Lateral movement, Info Disclosure | ADR-009 | Kubernetes network policies + ACLs on the API Gateway | CI log: `validate-isolation` (pipeline #247) | Compliant |
| ARC-011 | Segmentation between environments | Cross-env tampering | ADR-012 | Isolated namespaces + separate credentials per environment | IAM audit 2024-10, network policy review | Compliant |

*For L1: the `Ameaça associada` and `Decisão / ADR` columns are recommended but not mandatory. For L2 and L3: all fields are mandatory.*

---

## Update criteria {#critérios-de-actualização}

The traceability matrix must be updated when:

- an ARC requirement is instantiated or reviewed in the project;
- an ADR is created, updated or invalidated;
- an architectural review event occurs (see the triggers in [Operational Glossary](./termos-e-glossario-arquitetura));
- the application's risk level is reclassified;
- an exception is approved, renewed or expires.

Outdated traceability is equivalent to the absence of traceability for audit purposes.

---

## Operational instantiation {#instanciação-operacional}

For instantiation in a project, each ARC requirement is identified with the operational tag `SEC-Lx-ARC-CODIGO` (e.g. `SEC-L2-ARC-005`), as described in [Taxonomy and Traceability](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

The operational tag is the link between the architectural traceability matrix and the project's backlog or compliance management system.

---

> For the requirements catalogue, see [ARC Requirements Catalogue](./catalogo-requisitos-arquitetura).
> For the validation criteria per requirement, see [Architectural Validation Plan](./validacao-arquitetural).
> For the decision and evidence model, see [Architectural Decision and Evidence](./decisao-evidencia-arquitetural).
> For the management of exceptions to traceability, see [Exception Management](./excecoes).
