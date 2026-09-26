---
id: excecoes-deploy
title: Exceptions in Secure Deployment
sidebar_position: 9
description: Specifics of exception management in the context of secure deployment - emergency deploy, break glass and deviations from promotion gates
tags: [exceções, deploy, emergency, break-glass, gates, aprovacao, rollback]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/addon/09-excecoes-deploy.md
  source_sha256: 5b490a47e2ab096739744cba19de0b9afa864823e7eddf6f114490f0e71103d1
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: cac52c2a0d852a0a517f1e89722909ff24a4057de5c1895fd934edd04a6d4977
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 112d795f9bd927f0d4c24114e389470217eb00c1d6b919ae2df2e4f7bdb4878d
  glossary_keys: [alcada, provenance, validation_evaluation]
  glossary_sha256: 706f29934f8dd95ae4cbf35015548fd6869a7662d89c2b2b88c6da069fac2100
  translated_at: 2026-09-26T11:00:52Z
  reviewed_by: null
---

# Exceptions in Secure Deployment

> The base process, approval authorities, mandatory fields, chain of authority and lifecycle are defined in **Ch. 14 - `addon/12-processo-excecoes.md`**. This file defines only the specifics of this domain.

---

## Scope {#âmbito}

Exceptions to requirements of the secure deployment catalogue: `DPL-001` to `DPL-009`. This includes the emergency deploy (break glass) scenario as a case of immediate exception with post-facto evidence.

---

## Triggers specific to this domain {#triggers-específicos-deste-domínio}

- an emergency deployment (critical hotfix, response to an incident in production) that cannot wait for the normal approval and gates process - "break glass" (DPL-001, DPL-003);
- an artefact without verifiable provenance in a disaster recovery context where the normal pipeline is unavailable (DPL-002);
- staging not sufficiently representative of production for a given type of validation, with documented technical justification (DPL-007);
- rollback not testable for a given legacy component - with operational compensation (DPL-005);
- progressive deployment architecturally unfeasible for a specific component, with technical justification (DPL-009).

---

## Emergency deploy - break glass {#emergency-deploy---break-glass}

The emergency deploy is the only scenario in which the exception may be approved *post-facto*, immediately after the deployment and before the end of the deployment window. It is not a permanent bypass - it is a one-off, traceable exception.

Specific requirements:

| Element | Mandatory |
|---|---|
| Reference to the incident or emergency reason | Yes |
| Notification to the CISO or equivalent before or during the deployment | Yes |
| Emergency change record in the change management system | Yes |
| Post-facto approval within a maximum of 24h after the deployment | Yes |
| Documented post-mortem with cause analysis and corrective actions | Yes |
| Process review to prevent recurrence | Recommended |

The absence of an emergency change record or of the notification to the CISO invalidates the emergency deploy as an exception - it becomes an unauthorised deployment.

---

## Additional mandatory fields (deployment) {#campos-adicionais-obrigatórios-deploy}

| Field | Mandatory | Notes |
|---|---|---|
| Deployment / release ID | Yes | Unique traceable identifier |
| Affected environment | Yes | staging / production / etc. |
| Promoted artefact(s) | Yes | Name, version, commit SHA |
| Gates not executed | Yes | Which gates were skipped and why |
| Reference to the incident (if emergency) | Conditional | Mandatory in break glass |

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|---|---|
| `00-catalogo-requisitos.md` | DPL-001..009 catalogue - requirements that may have exceptions |
| `04-validacoes-pre-deploy.md` | Security gates that may be the object of an exception |
| `06-controle-versao-e-rollback.md` | Rollback as compensation in deployment exceptions |
| Ch. 07 - `addon/09-controle-excecoes-visibilidade.md` | Bypass of CI/CD gates - distinct from the emergency deploy to production |
| Ch. 14 - `addon/12-processo-excecoes.md` | Canonical exception management process |
