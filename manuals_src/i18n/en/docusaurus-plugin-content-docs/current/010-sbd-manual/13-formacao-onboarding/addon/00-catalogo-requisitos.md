---
id: catalogo-requisitos-formacao
title: Training and Onboarding Requirements Catalogue
description: Canonical catalogue of security training and onboarding requirements (TRN-001 to TRN-009), with applicability by risk level and acceptance criteria for training tracks, verifiable onboarding, Security Champions and training effectiveness.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:formacao, TRN, onboarding, champions, trilhos, capacitacao, terceiros, formacao-continua, L1, L2, L3, auditoria]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/addon/00-catalogo-requisitos.md
  source_sha256: aade3ceaa9c6d496d4d38dbaf5137ee82bddf8ddeb53b6a8a762b9144f4cc18d
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 5ae51320c0d54984a2a3024cb414ce4164722181b754b63bf2ce6352c83f36fb
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: d743dfcba33f930c34618b93d1eaaa34f697328d45aaf3bb657c33b8b3c59c9a
  glossary_keys: [avaliacao, capacitacao, chapter_role, cycle_iteration, lifecycle_phase, mapping, papel_suporte, programme_line, requirement_runtime, risk_level, sbdtoe_sbd, traceability, trilho_formativo, validation_evaluation]
  glossary_sha256: 7dca685935c380a0e917b803e051dfb144db45665b3a453c3e9809fef0260827
  translated_at: 2026-09-26T11:44:15Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Training and Onboarding Requirements Catalogue

## Scope: upskilling as a verifiable organisational control {#âmbito-capacitação-como-controlo-organizacional-verificável}

This catalogue covers the **security training and onboarding requirements** — the controls that guarantee that the people who build, operate and maintain systems have the competence needed to do so securely, and that this competence is verifiable.

Training is not an optional benefit: it is an organisational control with a direct impact on the attack surface. The most prevalent vulnerabilities — injection, weak authentication, secrets management, insecure configuration — are, to a large extent, the consequence of competence gaps traceable to the absence of training proportional to the risk.

The TRN requirements are verifiable: the existence of defined training tracks, of evidence of validated onboarding, of up-to-date content and of collected KPIs are auditable facts. The absence of evidence is equivalent to the absence of control.

For the complete mapping of all SbD-ToE requirements catalogues by technical domain, canonical prefix and owner, see [Ch. 02 - Catalogue Mapping](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **On curation:** Consolidated from NIST SSDF, NIST SP 800-30, ISO/IEC 27001, ISO/IEC 27005, OWASP SAMM v2.1, OWASP DSOMM, BSIMM13 and risk-oriented application governance practices. It must be adapted to the organisational risk model, but without losing traceability to L1, L2 and L3.

For instantiation in a project and operational naming (`SEC-Lx-TRN-CODIGO`), see [Taxonomy and Traceability](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Conventions {#convenções}

| Symbol | Meaning |
|---------|-------------|
| ✔ | Requirement mandatory at this level |
| - | Not applicable or not mandatory at this level |

Levels are cumulative: L3 includes all L1 and L2 requirements; L2 includes all L1 requirements.

---

## TRN Catalogue - Training and Onboarding {#catálogo-trn---formação-e-onboarding}

Requirements ensuring that the security competence of the teams is proportional to the risk, verifiable by objective evidence and maintained throughout the project lifecycle.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| TRN-001 | Security training tracks defined by profile and criticality level | ✔ | ✔ | ✔ | Security training tracks exist, defined by staff profile (developer, ops, PO, QA, tech lead) and by project criticality level (L1, L2, L3); the tracks specify mandatory modules, estimated duration and renewal periodicity; the tracks are documented and accessible. |
| TRN-002 | Mandatory security onboarding before autonomous work | ✔ | ✔ | ✔ | Every member of staff with access to code, pipelines or production environments completes security onboarding before operating autonomously; the onboarding includes: policies and good practices relevant to the profile, handling of secrets, the incident process and basic controls of secure development or secure operations according to the role. |
| TRN-003 | Objective validation of onboarding with a defined acceptance criterion | ✔ | ✔ | ✔ | Completion of onboarding is verified with an objective criterion — quiz, practical exercise or another form of assessment with a defined minimum pass rate; the result is recorded and traceable to the member of staff and to the version of the content administered; results below the threshold have a defined remediation path. |
| TRN-004 | Access to critical environments conditional on validated onboarding | ✔ | ✔ | ✔ | Access to repositories, production pipelines or environments classified as L2+ is conditional on evidence of valid security onboarding; the condition is verifiable — the onboarding record is checked in the access onboarding process; access without valid onboarding is blocked or escalated to the security owner. |
| TRN-005 | Continuous security training for teams on L2 and L3 projects | - | ✔ | ✔ | Staff on L2+ projects receive continuous security training — at least one relevant session or module per half-year (L2) or quarter (L3); continuous training covers the evolution of threats, new attack techniques relevant to the context and policy updates; participation is recorded and traceable. |
| TRN-006 | Training content versioned and updated after defined triggers | - | ✔ | ✔ | Training and onboarding content has explicit version control; it is reviewed and updated after relevant security incidents, policy changes or the identification of new classes of vulnerabilities in the project context; the version of the content administered is traceable to each member of staff's training record. |
| TRN-007 | Equivalent security onboarding for third parties and contractors | ✔ | ✔ | ✔ | Third parties, contractors and partners with access to code, pipelines or sensitive data complete security onboarding equivalent to that of internal staff, proportional to their access profile; the validation and recording process is the same; the absence of valid onboarding blocks access. |
| TRN-008 | Formal Security Champions programme in L3 teams | - | - | ✔ | Teams on L3 projects have one or more formally designated Security Champions — with a documented role, defined responsibilities, access to AppSec resources and participation in a community of practice or equivalent; the Champion does not replace centralised AppSec, but amplifies security competence within the team; the designation is traceable and kept up to date. |
| TRN-009 | Training KPIs defined, collected and acted upon | - | ✔ | ✔ | Training effectiveness KPIs are defined, collected periodically and analysed — including at least: % onboarding coverage per team, pass rate in objective validations, average onboarding time and content update rate; deviations from defined thresholds generate corrective action with an owner and a deadline. |

---

## Explanatory notes {#notas-explicativas}

- **TRN-001**: The definition of tracks by profile is decisive — generic onboarding that covers every role superficially is less effective than differentiated tracks with less volume but greater contextual relevance. A PO does not need to know how to configure SAST; a PO needs to understand lightweight threat modelling and risk acceptance criteria.
- **TRN-002 and TRN-003**: The distinction is operationally important: TRN-002 verifies whether onboarding happens before autonomous work (timing and coverage); TRN-003 verifies whether completion has verifiable evidence (objective validity). It is possible to have onboarding carried out (TRN-002 met) without traceable validation (TRN-003 not met).
- **TRN-004**: The access condition is the enforcement mechanism for TRN-002 and TRN-003 — without it, onboarding is recommended but not mandatory in practice. For L3, enforcement must be automated or verified by a formal access onboarding process.
- **TRN-005**: The frequency differentiated by level (half-yearly for L2, quarterly for L3) reflects the faster evolution of the threat context in systems of higher criticality. For L1, annual training or training in performance cycles is sufficient and recommended even without a formal obligation.
- **TRN-006**: Versioning of training content serves two purposes: it makes it possible to trace what each member of staff learnt and when (relevant in incidents — "was the good practice being taught?") and it guarantees that the content reflects the current state of threats and policies.
- **TRN-007**: Equivalence of onboarding for third parties is frequently neglected in favour of onboarding speed. The criterion of proportionality to the access profile is the right calibrator: a contractor with read access to non-critical repositories does not require the same level of onboarding as a partner with access to L3 production pipelines.
- **TRN-008**: The Security Champions programme is the mechanism for scaling AppSec without needing to grow the centralised team in proportion to the number of projects. The Champion is a multiplier — but their effectiveness depends directly on having formally dedicated time, access to specialised training and a connection to the organisation's AppSec community. A Champion without time and without support is only a title.
- **TRN-009**: KPIs without thresholds and without corrective action are decorative metrics. The acceptance criterion of TRN-009 explicitly requires that the KPIs produce decisions. The pass rate in objective validations is the KPI most predictive of real training effectiveness.

---

> For the detailed training catalogue by module and profile, see [Training Catalogue](./catalogo-formativo).
> For the training tracks by profile and criticality level, see [Training Tracks](./trilho-formativo).
> For the Security Champions programme, see [Security Champions Programme](./programa-champions).
> For the canonical onboarding checklist, see [Onboarding Checklist](./checklist-onboarding).
> For the model for the inclusion of third parties and contractors, see [Third-Party Inclusion Model](./20-modelo-inclusao-terceiros.md).
> For KPIs and training effectiveness metrics, see [Training KPIs and Metrics](./11-kpis-metricas.md).
