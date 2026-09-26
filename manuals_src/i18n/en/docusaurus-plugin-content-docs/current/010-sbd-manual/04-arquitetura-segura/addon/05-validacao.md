---
id: validacao-arquitetural
title: Architectural Validation Plan
description: Validation criteria per requirement (ARC-001 to ARC-013), with methods, moments and owners, organised by risk level
tags: [tipo:addon, tema:arquitetura, ARC, validacao, evidencia, L1, L2, L3]
sidebar_position: 5
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/addon/05-validacao.md
  source_sha256: db7d4cd7e54b0ae31fe2bdb4ee4cd1ec7db6f4cb47effb301b06bfc345b588bf
  source_commit: 112711064196b71c545672fe3fb3ae412b36575e
  target_sha256: 5ee7174cb8be030bdb43a859ac4f045a84dc24ea8fca7ed9f50a833b4f5880f5
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 69aedbbdd11831f1cdc997bd1abfda3e2e4d3b411b1b43faf096628c510f395b
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, lifecycle_phase, papel_suporte, requirement_runtime, risk_level, traceability, validation_evaluation]
  glossary_sha256: 7c88fc8fbff365d7c9f69db72c1f0b4a0f85ec26f541a8baab5bbe55ecd566ed
  translated_at: 2026-09-26T17:23:45Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Architectural Validation Plan

This document defines how to validate each requirement of the secure architecture catalogue (ARC-001 to ARC-013), specifying:

- **what to validate** - the concrete conformity criterion;
- **how to validate** - the method or artefact used;
- **when** - the moment in the lifecycle at which validation must take place;
- **owner** - the role that validates.

---

## Validation per Requirement {#validação-por-requisito}

| Requirement | What to validate | How to validate | When | Owner |
|-----------|---------------|--------------|--------|-------------|
| ARC-001 | Trust zones identified and documented | Diagram with zones marked, justified and versioned in a repository | Initial design; after a change of topology or boundaries | Technical architect |
| ARC-002 | External exposure minimised and justified | Inventory of exposed components; each exposure with an associated control and a documented technical justification | Architecture review; exposure audit | AppSec, Architect |
| ARC-003 | Security-focused architecture review | Formal review record (minutes, checklist or AppSec report) with date, participants and decisions | Before a significant release; after a structural change | AppSec |
| ARC-004 | Architecture decisions documented | ADR or equivalent with context, alternatives, decision taken, accepted trade-offs and owner | Whenever a structural decision with an impact on security, isolation or dependencies occurs | Technical architect |
| ARC-005 | Threat modelling integrated into critical flows | Threat modelling output with identified threats, flows covered and mitigations recorded; linked to the architecture diagram | Initial design; after a significant change of flow or component | AppSec, Architect |
| ARC-006 | Technical isolation controls between sensitive domains | Evidence of active isolation (network policies, logical firewalls, API segmentation); testable and auditable configuration | Architecture review; network configuration inspection | AppSec, DevSecOps |
| ARC-007 | Reusable and approved architecture patterns | Pattern repository with the date of last review; evidence of use of an approved pattern recorded in an architecture review | Project start; introduction of a new structural component | Architecture team |
| ARC-008 | Data flows between trust zones protected | DFD with explicit controls at each trust boundary; updated and versioned in a repository | Initial design; after a change to data flows | Architect, AppSec |
| ARC-009 | Significant changes trigger a new review | Documented process with a definition of the "significant change" threshold; evidence of a review carried out after the last relevant change | After each change that reaches the threshold defined in the process | Architect, PO |
| ARC-010 | Architecture diagrams versioned and accessible | Diagram in the repository with version history; accessible to the relevant teams; reviewed within the defined period | Periodic review (at least annual or per significant release) | Architect, DevOps |
| ARC-011 | Logical and physical segmentation between environments | Evidence of network, permission and identity segregation between dev, staging and prod; documented and verifiable by audit | Infrastructure review; cross-environment permissions audit | Platform engineering, Software Architects, AppSec |
| ARC-012 | Formal approval criteria for high-risk applications | Formal checklist completed and signed by the security owner; approval record prior to deployment to production | Release gate for L3 applications | AppSec, Security owner |
| ARC-013 | Automatic topology validation in CI/CD or as code | CI job with topology validation output; execution logs available; failures block promotion | Per pipeline run; periodic coverage review | DevSecOps, Architect |

---

## Application by risk level {#aplicação-por-nível-de-risco}

| Validation criterion | L1 | L2 | L3 |
|-----------------------|:--:|:--:|:--:|
| Informal validation by the technical architect | ✔ | ✔ | ✔ |
| Formal review with a record (minutes, checklist or AppSec report) | - | ✔ | ✔ |
| Evidence archived with the release | - | ✔ | ✔ |
| Update after a relevant change | ✔ | ✔ | ✔ |
| Review by an independent security role | - | - | ✔ |
| Formal approval gate before deployment to production | - | - | ✔ |
| Automatic topology validation in CI/CD | - | - | ✔ |

---

## Notes {#notas}

- Validation is not a one-off act: it accompanies the architecture throughout the lifecycle. Each review *trigger* (new integration, change to data flows, risk reclassification) must set off the validation of the affected ARC requirements.
- For L1, a simple checklist verified by the architect or technical lead is sufficient for the requirements marked as mandatory (ARC-001, ARC-002, ARC-006, ARC-008, ARC-010).
- ARC-003, ARC-004, ARC-005 and ARC-009 are oriented towards the decision process: the evidence is the record of the decision, not just the final diagram.

---

> For the requirements catalogue, see the [ARC Requirements Catalogue](./catalogo-requisitos-arquitetura).
> For requirement→decision→evidence traceability, see [Architectural Traceability](./rastreabilidade-arquitetural).
> For exception management, see [Exception Management](./excecoes).
