---
id: gestao-excecoes
title: Exceptions to Application Security Requirements
description: Specifics of exception management in the context of the application requirements of Ch. 02
tags: [exceções, requisitos, risco, validação, aplicacional]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/02-requisitos-seguranca/addon/08-gestao-excecoes.md
  source_sha256: 0e3dc594b6657549a5c4f8c8934502930e8535dec34defaa5b0d951f0dd8b3b6
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 4ec4a3da3716d3b172c8571537575b69610ea7b2d6303e84902883a608799eae
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [alcada, framework_source_corpus, requirement_runtime, traceability, validation_evaluation]
  glossary_sha256: c801a96ce95dd623d92a0c7cdab49e9fdfdbc1a9d0317859f10098f20c79f7e5
  translated_at: 2026-09-25T20:20:11Z
  stamped_at: 2026-09-26T18:33:03Z
  reviewed_by: null
---

# Exceptions to Application Security Requirements

> The base process, approval authorities, mandatory fields, chain of authority and lifecycle are defined in **Ch. 14 - `addon/12-processo-excecoes.md`**. This file defines only the specifics of this domain.

---

## Scope {#âmbito}

Exceptions to requirements of the application catalogue: `AUT`, `ACC`, `LOG`, `SES`, `VAL`, `ERR`, `CFG`, `ENC`, `API`, `INT`.

---

## Triggers specific to this domain {#triggers-específicos-deste-domínio}

- framework or library without native support for the control (e.g. absence of MFA, limited input validation);
- third-party component integrated with no possibility of modification within the scope of the project;
- MVP or proof-of-concept context with an explicitly bounded L1 risk scope;
- conflict with a functional or contractual requirement, with documented evidence;
- progressive migration of a legacy system with a known and time-bounded window of non-compliance.

---

## Identification of the affected requirement {#identificação-do-requisito-afectado}

The "Affected requirement" field must identify:

- the canonical ID from the application catalogue (e.g. `AUT-003`, `VAL-002`, `ENC-005`);
- the project's operational tag (e.g. `SEC-L2-AUT-003`).

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|---|---|
| `01-catalogo-requisitos.md` | Application catalogue - requirements that may have exceptions |
| `04-rastreabilidade-controlo.md` | Traceability matrix where the exception is recorded |
| Ch. 14 - `addon/12-processo-excecoes.md` | Canonical exception management process |
