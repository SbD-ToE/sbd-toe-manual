---
id: excecoes-e-justificacoes
title: Exceptions in Secure Development
sidebar_position: 5
description: Specifics of exception management in the context of secure development - SAST, linters and code review
tags: [exceções, validação, rastreabilidade, segurança, desenvolvimento, sast]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/06-desenvolvimento-seguro/addon/05-excecoes-e-justificacoes.md
  source_sha256: 08881af2bd2902f1c1e212c6d1e25aaf0c448ea3656acf0bb121c43bc1ce1bac
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: f00cc23c70021de54a2f7b7eebebb550ee6a4fb179fe4aff53372e3bf67b5bef
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [alcada, framework_source_corpus, traceability]
  glossary_sha256: 49d53669192f4e2a25f1ca7da322b75182814e9c9a4b825f3a1bab65adde5df5
  translated_at: 2026-09-26T08:57:11Z
  reviewed_by: null
---

# Exceptions in Secure Development

> The base process, approval authorities, mandatory fields, chain of authority and lifecycle are defined in **Ch. 14 - `addon/12-processo-excecoes.md`**. This file defines only the specifics of this domain.

---

## Scope {#âmbito}

Exceptions to practices and controls identified by SAST tools, linters or code review during development.

---

## Triggers specific to this domain {#triggers-específicos-deste-domínio}

- a SAST tool finding classified as a false positive with demonstrable technical evidence;
- a mandatory practice incompatible with a constraint of an external framework or library with no viable alternative;
- backward compatibility with a component that cannot be modified within the scope of the project;
- a temporary deviation accepted in a PR with a dated and recorded resolution plan.

---

## Recording mechanisms in SAST tools {#mecanismos-de-registo-em-ferramentas-sast}

SAST tools allow findings to be marked directly in the report - `mute`, `waive`, `false positive accepted`, inline annotation. These markings are valid as a technical recording mechanism, but **do not replace formal approval** nor the chain of authority required by the canonical process.

Reference tools: Kiuwan, SonarQube, Xygeni, Checkmarx, Semgrep.

---

## Traceability in the repository {#rastreabilidade-no-repositório}

In addition to the record in the tracking system, the exception must be visible in the repository:

- **Versioned file:** `excecoes-aprovadas.yml` with a reference to the finding, justification, approver and validity;
- **Inline annotation:** a `@sec:justificado: <ID-excepção>` comment in the affected code;
- **PR / merge commit:** an explicit link to the exception record in the PR body or in the commit message.

The record in the repository complements the record in the tracking system and ensures direct traceability to the code. It does not replace it.

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|---|---|
| `addon/01-boas-praticas-codigo.md` | Practices that may have associated exceptions |
| `addon/02-linters-validacoes.md` | Tools that generate findings that are candidates for exception |
| `addon/08-validacoes-codigo.md` | Code review and blocking in PRs |
| Ch. 14 - `addon/12-processo-excecoes.md` | Canonical exception management process |
