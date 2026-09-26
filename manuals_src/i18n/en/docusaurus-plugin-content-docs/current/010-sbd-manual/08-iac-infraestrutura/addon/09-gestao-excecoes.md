---
id: gestao-excecoes
title: Exceptions in IaC
sidebar_position: 9
description: Specifics of exception management in the context of Infrastructure as Code - policy engines, enforcement and TTL
tags: [excecoes, governacao, iac, controlo, opa, enforcement]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/addon/09-gestao-excecoes.md
  source_sha256: 20f43f812ddf9e26854b455066ab393c80e3a51fc4e89a82f7a433b7438f8f57
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 9e5d126fbdfd2f9379b2581dba9bc6a481b018a9e48a5997bd585e080c09f06e
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [alcada, avaliacao, requirement_runtime, validation_evaluation]
  glossary_sha256: 67091f71e27e85835e96d582511fe43a6602640a11fa4479a0d6d8911b617f1b
  translated_at: 2026-09-26T09:25:38Z
  reviewed_by: null
---

# Exceptions in IaC

> The base process, approval authorities, mandatory fields, chain of authority and lifecycle are defined in **Ch. 14 - `addon/12-processo-excecoes.md`**. This file defines only the specifics of this domain.

---

## Scope {#âmbito}

Exceptions to security policies and controls applied by policy engines (OPA, Sentinel, Rego) to IaC modules, resources and pipelines - requirements `IAC-001` to `IAC-013`.

---

## Triggers specific to this domain {#triggers-específicos-deste-domínio}

- an IaC validation tool unavailable with a need for a deploy documented as urgent;
- a requirement technically impossible to apply to the module or resource concerned, with an architectural justification;
- an intentional deviation in a staging environment with an active compensating control;
- a legacy module integrated without support for the current policies, with a migration plan.

---

## Additional mandatory fields (IaC) {#campos-adicionais-obrigatórios-iac}

| Field | Mandatory | Notes |
|---|---|---|
| Affected environment | Yes | `staging` / `production` / `shared` |
| Affected IaC artefact | Yes | Name of the module, resource or pipeline |
| Violated rule / policy | Yes | OPA / Sentinel / Rego rule ID |

---

## Record in the repository {#registo-no-repositório}

**File:** `exceptions/` directory in the IaC repository, or a dedicated central repository with traceable equivalence.

**Format:** versioned YAML or JSON. `.md` format only for documentary exceptions without policy engine integration.

```yaml
id: IAC-EXC-003-2025-07-10
requisito: IAC-003
ambiente: staging
artefacto_afetado: pipeline-iac-staging
justificacao: "Deploy urgente para restauro de capacidade após incidente P1"
impacto: "Possível omissão temporária de detecção de má configuração"
mitigacao: "Execução manual de tfsec pós-deploy + revisão AppSec"
aprovado_por: "appsec@org"
validade: "2025-07-20"
```

**Link to the code:** a structured comment on the affected resource:

```hcl
# iac-exception: IAC-EXC-003-2025-07-10
```

---

## Integration with policy engines {#integração-com-policy-engines}

- Exceptions are assessed **per rule and per context** - they do not disable rules globally;
- Policy engines (OPA/Sentinel/Rego) must be configured to interpret active exceptions as assessment context;
- Expired exceptions result in **automatic blocking** of the pipeline - expiry is neither silent nor falls back to a permissive state by default.

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|---|---|
| `addon/06-controle-enforcement.md` | Technical handling of exceptions in policy-as-code |
| `addon/08-matriz-requisitos-iac.md` | Requirements IAC-001..013 that may have exceptions |
| Ch. 14 - `addon/12-processo-excecoes.md` | Canonical exception management process |
