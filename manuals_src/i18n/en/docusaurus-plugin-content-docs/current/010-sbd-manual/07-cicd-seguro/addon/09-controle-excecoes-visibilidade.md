---
id: controle-excecoes-visibilidade
title: Exceptions and Visibility in CI/CD
sidebar_position: 9
description: Specifics of exception management in the context of CI/CD pipelines - bypass of gates, visibility and metrics
tags: [exceções, visibilidade, cicd, governação, auditoria]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/addon/09-controle-excecoes-visibilidade.md
  source_sha256: ee1b1b330b1f43e9f95177a7ed820a5a97a9b9243a5d701878730bdbe9cee28e
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: e0478ce4a6f4a000c0f3f7baf9e524ea13ff41808370491150ac7218c0800f18
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [alcada, cycle_iteration, maturity, validation_evaluation]
  glossary_sha256: 0d2035d37ce2d8b2b77f6785af938c081aa0d7dbc56efc89f588dace95e27018
  translated_at: 2026-09-26T09:09:17Z
  stamped_at: 2026-09-26T18:34:22Z
  reviewed_by: null
---

# Exceptions and Visibility in CI/CD

> The base process, approval authorities, mandatory fields, chain of authority and lifecycle are defined in **Ch. 14 - `addon/12-processo-excecoes.md`**. This file defines only the specifics of this domain.

---

## Scope {#âmbito}

Exceptions to security gates, pipeline policies and CI/CD controls - temporary bypass of validations, disabling of tools or deviation from execution policies.

---

## Triggers specific to this domain {#triggers-específicos-deste-domínio}

- a blocking security gate in the context of a critical incident with a need for an urgent, documented deploy;
- a validation tool unavailable with an impact on the release cycle;
- a legacy application integrated into the pipeline without technical support for the required controls;
- an exception window during a pipeline migration with a bounded deadline.

---

## Mandatory visibility in the pipeline {#visibilidade-obrigatória-no-pipeline}

Every active exception must be **explicitly flagged** in the logs, execution artefacts or pipeline metadata. An exception that is invisible in the pipeline is equivalent to an uncontrolled bypass.

Flagging mechanisms by tool:

| Tool | Suggested mechanism |
|---|---|
| GitHub Actions | `bypass-security-gate` label on the PR; approval visible in the execution history |
| GitLab CI | `exception.yaml` file in the MR; review by `Security Approval` |
| Azure DevOps | Override on a release associated with a Work Item referencing the exception record |
| Jenkins | `bypass=true` flag commented in the `Jenkinsfile`; integration with Jira or ServiceNow |

---

## Associated metrics {#métricas-associadas}

CI/CD exceptions contribute directly to the maturity KPIs (see Ch. 14 - `kpis-governanca.md`):

- % of pipelines with active security gates;
- no. of active exceptions by category (SAST, SBOM, signing, deploy gates);
- L3 applications with enforcement disabled or under exception.

These indicators must be reported in the governance cycle.

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|---|---|
| `addon/06-politicas-gates-pipeline.md` | Pipeline gates and policies that may be subject to exception |
| `addon/07-validacoes-seguranca-integradas.md` | Integrated validations and bypass conditions |
| Ch. 14 - `addon/12-processo-excecoes.md` | Canonical exception management process |
| Ch. 14 - `kpis-governanca.md` | Compliance indicators and active exceptions |
