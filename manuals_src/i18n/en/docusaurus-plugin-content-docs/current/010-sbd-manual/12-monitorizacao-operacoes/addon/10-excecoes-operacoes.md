---
id: excecoes-operacoes
title: Exceptions in Monitoring and Operations
sidebar_position: 10
description: Specifics of exception management in the context of monitoring and operations - alert silencing, log retention and regulatory implications
tags: [exceções, operacoes, monitorizacao, alertas, retencao, DORA, NIS2, SIEM]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/addon/10-excecoes-operacoes.md
  source_sha256: 7609a2d94bca704d066d88703f9d90114b5c05b6f8b10aa98bf06860866ea638
  source_commit: 50f5914ebc90e4135e6678b2278709d5082dd237
  target_sha256: 444dd407783cc3833dc76634606db0621c834f919c594a3649b57c646a509fb4
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [alcada, avaliacao, eu_ai_high_risk_system, eu_ai_system, framework_source_corpus, practitioner_manual, requirement_runtime, risk_level, validation_evaluation]
  glossary_sha256: 99e0d8587c7733c5c6dc374a84d95e5ca9b4bffd25c4838cac143ed3a2e2ab05
  translated_at: 2026-09-27T07:06:03Z
  stamped_at: 2026-09-27T07:06:03Z
  reviewed_by: null
---

# Exceptions in Monitoring and Operations

> The base process, approval authorities, mandatory fields, chain of authority and lifecycle are defined in **Ch. 14 - `addon/12-processo-excecoes.md`**. This file defines only the specifics of this domain.

---

## Scope {#âmbito}

Exceptions to requirements of the monitoring and operations catalogue: `OPS-001` to `OPS-015`. Two scenarios have relevant specifics: alert silencing (OPS-005) and log retention below the regulatory minimum (OPS-003).

---

## Triggers specific to this domain {#triggers-específicos-deste-domínio}

- an alert temporarily silenced due to scheduled maintenance, excessive false-positive noise, or technical inability to respond within a defined period (OPS-005);
- log retention below the minimum defined in the policy or required by regulation - due to storage constraints, cost or conflict with another legal obligation (OPS-003);
- a log source not integrated into the SIEM due to technical incompatibility or the absence of a connector, with alternative monitoring as compensation (OPS-004);
- an alert response SLA that cannot be met for a given type of event due to a lack of operational capacity, with a reinforcement plan (OPS-006).

---

## Alert silencing - specific requirements {#alert-silencing---requisitos-específicos}

Alert silencing is the highest-risk scenario in this domain: it removes active visibility without leaving automatic evidence. Every silencing exception requires:

- precise identification of the silenced alert (ID, rule, source);
- technical justification of the impossibility of keeping the alert active;
- a silencing period with a mandatory end date - no permanent silencing;
- a compensating visibility control active during the period (e.g. periodic manual review, alternative alert, manual monitoring of the source);
- notification to the person responsible for operational security (SOC lead or equivalent).

Silenced alerts without an end date or without a compensating control are treated as non-compliance.

---

## Log retention - regulatory implications {#retenção-de-logs---implicações-regulatórias}

Exceptions to OPS-003 with retention below an applicable statutory minimum (e.g. at least six months for the logs of high-risk AI systems — AI Act, Articles 19(1) and 26(6)), below the period set by the entity in its risk assessment (DORA; NIS2, where applicable) or below the internal policy have implications that go beyond technical approval:

- the chain of authority must include legal or compliance validation, not only AppSec;
- the exception must reference the specific regulatory requirement that is being compromised;
- the maximum duration is determined by the regulatory risk, not by the generic 90-day deadline.

---

## Additional mandatory fields (operations) {#campos-adicionais-obrigatórios-operações}

| Field | Mandatory | Notes |
|---|---|---|
| Affected source / system | Yes | Component, application or infrastructure |
| Silenced alert / rule (if applicable) | Conditional | Mandatory in OPS-005 exceptions |
| Effective retention period vs. required minimum | Conditional | Mandatory in OPS-003 exceptions |
| Regulation or policy compromised | Conditional | Mandatory in exceptions with a regulatory implication |
| Compensating visibility control | Yes | Mechanism active during the exception window |

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|---|---|
| `00-catalogo-requisitos.md` | OPS-001..015 catalogue - requirements that may have exceptions |
| `03-alertas-eventos-criticos.md` | Alerts that may be the object of silencing with an exception |
| `08-matriz-controles-por-risco.md` | Controls matrix by risk level |
| Ch. 14 - `addon/12-processo-excecoes.md` | Canonical exception management process |
