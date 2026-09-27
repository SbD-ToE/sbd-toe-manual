---
id: excecoes
sidebar_position: 3
title: Exceptions to Secure Architecture Requirements
description: Specifics of exception management in the context of the secure architecture requirements (ARC-001..013)
tags: [exceções, arquitectura, risco, rastreabilidade, adr]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/addon/03-excecoes.md
  source_sha256: 50d012daa1521db8e1731d0d56d63e6e8f2961991e745f6c8b473681d0e1505c
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: aee3be2cfb15e3e06960ca7f6f8c28b3670edda8e7ead4b3fa8afa61859ed123
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5536afdcc04f76a07c66e747133c73d68308884707c296abf945937a9630a312
  glossary_keys: [alcada, gap_family, normative_empirical, requirement_runtime, risk_level, threat, traceability]
  glossary_sha256: 71670370741a8945f1564c84034a8c0edc6565786841dba3b509606aa1f8d35a
  translated_at: 2026-09-26T08:32:03Z
  reviewed_by: null
---

# Exceptions to Secure Architecture Requirements

> The base process, approval authorities, mandatory fields, chain of authority and lifecycle are defined in **Ch. 14 - `addon/12-processo-excecoes.md`**. This file defines only the specifics of this domain.

---

## Scope {#âmbito}

Exceptions to requirements of the architecture catalogue: `ARC-001` to `ARC-013`.

---

## Triggers specific to this domain {#triggers-específicos-deste-domínio}

- phased migration between environments or architectures with a bounded window of non-compliance and a completion plan;
- integration of a legacy or third-party component with no possibility of architectural modification within the scope of the project;
- cost of architectural refactoring disproportionate to the effective risk level of the context (L1);
- architecture decision documented in an ADR with explicit and approved risk acceptance.

---

## Identification of the affected requirement {#identificação-do-requisito-afectado}

- canonical ID from the catalogue (e.g. `ARC-003`, `ARC-008`);
- operational tag (e.g. `SEC-L2-ARC-003`);
- reference to the associated ADR, if one exists.

---

## Integration with architectural traceability {#integração-com-rastreabilidade-arquitectural}

Exceptions to ARC requirements must be reflected in the traceability matrix (`06-rastreabilidade.md`), with:

- identification of the threat not mitigated by the missing control;
- reference to the ADR that documents the decision and the conditions for reversal;
- expiry date aligned with the architecture plan.

Exceptions not recorded in the traceability matrix are treated as a coverage gap.

---

## Normative alignment {#alinhamento-normativo}

- ISO/IEC 27001 A.18.1.4 - formal acceptance of residual risks
- SSDF GV.3 - approval of exceptions and deviations from security processes
- OWASP SAMM Governance - recording and lifecycle of exceptional decisions

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|---|---|
| `01-catalogo-requisitos.md` | Catalogue ARC-001..013 - requirements that may have exceptions |
| `06-rastreabilidade.md` | Traceability matrix where the exception is recorded |
| Ch. 14 - `addon/12-processo-excecoes.md` | Canonical exception management process |
