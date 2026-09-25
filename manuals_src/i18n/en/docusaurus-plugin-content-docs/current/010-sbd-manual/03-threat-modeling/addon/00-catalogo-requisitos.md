---
id: catalogo-requisitos-threat-modeling
title: Threat Modelling Requirements Catalogue
description: Canonical catalogue of threat modelling requirements (THR-001 to THR-007), with applicability by risk level and acceptance criteria for threat identification, formal disposition, requirement derivation and methodological traceability.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:threat-modeling, THR, STRIDE, LINDDUN, DFD, ameacas, requisitos, rastreabilidade, L2, L3, auditoria]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/addon/00-catalogo-requisitos.md
  source_sha256: b140e1847ccb150e23fe96003f5aa016fdf42303d40bc042a714d7ed7c244582
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 2366898cd4b2132aad01dd16f520705c1caa81fb6519af187b541f5e691eedef
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [cycle_iteration, framework_source_corpus, gap_family, mapping, plain_rag, practitioner_manual, requirement_runtime, risk_level, sbdtoe_sbd, threat, traceability, validation_evaluation]
  glossary_sha256: 23710a5bc0189b4ed6d9ed50a228bc5d2adcbf5c182acfc45c1a7de9cf0c49d6
  translated_at: 2026-09-25T20:16:56Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Threat Modelling Requirements Catalogue

## Scope: threat modelling as a formal mechanism for deriving controls {#âmbito-o-threat-modeling-como-mecanismo-formal-de-derivação-de-controlos}

This catalogue covers the **requirements of the threat modelling process** — the controls that ensure the threats relevant to a system are identified with methodological rigour, have a documented disposition and generate traceable security requirements.

Threat modelling is not an academic activity: it is the mechanism by which a system's architecture translates abstract risks into concrete, verifiable controls. A superficial or outdated threat model gives false confidence — it is worse than the formal absence of the artefact, because it hides control gaps behind the appearance of compliance.

The THR requirements are verifiable: the existence of a threat model with current DFDs, of a formal disposition per threat, of traceability to the backlog and of independent review before go-live are auditable facts. Absence of evidence is equivalent to absence of control.

For the complete mapping of all SbD-ToE requirements catalogues by technical domain, canonical prefix and owner, see [Ch. 02 - Mapping of Catalogues](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **On curation:** Consolidated from NIST SSDF, NIST SP 800-30, ISO/IEC 27001, ISO/IEC 27005, OWASP SAMM v2.1, OWASP DSOMM, BSIMM13 and risk-oriented application governance practices. It must be adapted to the organisational risk model, but without losing traceability to L1, L2 and L3.

For project instantiation and operational naming (`SEC-Lx-THR-CODIGO`), see [Taxonomy and Traceability](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Conventions {#convenções}

| Symbol | Meaning |
|---------|-------------|
| ✔ | Mandatory requirement at this level |
| - | Not applicable or not mandatory at this level |

Levels are cumulative: L3 includes all L1 and L2 requirements; L2 includes all L1 requirements.

---

## THR Catalogue - Threat Modelling {#catálogo-thr---threat-modeling}

Requirements that ensure the threat modelling process is conducted with methodological rigour, produces a verifiable disposition for each identified threat and generates end-to-end traceability for the derived controls.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| THR-001 | Formal threat modelling in L2+ applications and significant architectural changes | - | ✔ | ✔ | Applications classified L2 or higher have a formal, documented threat model; the process is applied to new applications before go-live and to significant architectural changes (new component, new external integration, new exposure surface); the artefact is traceable to the architecture version assessed. |
| THR-002 | Current architecture represented with explicit DFDs and trust boundaries | - | ✔ | ✔ | The threat model includes up-to-date Data Flow Diagrams (DFDs) that reflect the real architecture in production; trust boundaries are explicitly marked and justified; each sensitive data flow identifies origin, destination, channel and trust level; outdated DFDs invalidate the threat model. |
| THR-003 | Structured methodology applied with guaranteed minimum coverage | - | ✔ | ✔ | The process uses a structured methodology — STRIDE as the baseline; LINDDUN in applications with personal data flows or a privacy context; PASTA or equivalent for high-risk contexts; the chosen methodology is declared in the artefact, applied consistently and covers at least the critical elements identified in the DFDs. |
| THR-004 | Formal disposition of each identified threat, with an owner | - | ✔ | ✔ | Each identified threat has an explicit, documented disposition — mitigated, accepted, transferred or excluded — with a rationale, an associated control or compensation and a named owner; threats without a declared disposition are treated as an active control gap; the threat list is part of the evidence artefact. |
| THR-005 | Traceability threat → requirement → backlog → validation | - | ✔ | ✔ | Identified threats with a mitigation disposition generate traceable security requirements; those requirements are recorded in the backlog with a reference to the originating threat ID; validation of the requirement in test or review references the corresponding threat ID; the chain is verifiable without manual reconstruction. |
| THR-006 | Threat model versioned and updated within the cycle or after a trigger | - | ✔ | ✔ | The threat model is under explicit version control; it is reviewed and updated at least every significant release cycle or within 30 days of a change trigger (new integration, trust boundary change, security incident or new threat with relevant impact); the threat model version is referenced in the architecture artefacts and in the go-live process. |
| THR-007 | Independent review by AppSec before go-live in L2 and L3 | - | ✔ | ✔ | Before go-live of new L2+ applications or of architectural changes with material impact on an L2+ system, the threat model is reviewed by AppSec or by someone with equivalent competence who is independent of the team; the review produces evidence (record, approval or list of deviations with a plan); absence of review blocks the go-live. |
| THR-008 | Threat modelling extended to systems with AI/ML components | - | ✔ | ✔ | Systems that integrate artificial intelligence or machine learning components (predictive models, LLMs behind a conversational interface, RAG systems, autonomous agents with tool invocation) have an extended threat model covering specific adversarial threats — model poisoning, direct and indirect prompt injection, training data poisoning, model theft, evasion attacks, AI supply chain compromise — referenced to established catalogues (MITRE ATLAS, NIST AI 100-2 e2025); the model identifies additional trust boundaries for training data, model artefacts, inference endpoints and tool invocations; STRIDE or LINDDUN are complemented (not replaced) with AI/ML framing as applicable. |

---

## Explanatory notes {#notas-explicativas}

- **THR-001**: Applicability from L2 upwards is intentional — threat modelling is a control with an execution cost that must be proportional to the risk. For L1, informal risk analysis practices are sufficient and recommended; for L2 and L3, formality is necessary because the complexity of the systems and the impact of compromise justify the investment.
- **THR-002**: Outdated DFDs are the most common vector for invalidating threat models in production. A system that has evolved without its DFD being updated has wrong trust boundaries, unmapped flows and threats the threat model does not cover, simply because it is unaware of the current components.
- **THR-003**: The distinction between STRIDE and LINDDUN matters operationally. STRIDE covers the classic security threat categories (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege); LINDDUN is specific to personal data flows and privacy — using STRIDE alone is insufficient in systems that process personal data subject to the GDPR or equivalent.
- **THR-004**: The "excluded" (out of scope) disposition is legitimate but requires rigorous justification — it is not a way of ignoring inconvenient threats. The absence of a documented disposition is the most common form of a threat model that formally exists but is operationally useless.
- **THR-005**: Bidirectional traceability (threat→requirement→backlog→validation and validation→backlog→requirement→threat) is what turns threat modelling into a verifiable control. Without it, the threat model is an isolated document that does not influence the system's real controls.
- **THR-006**: The 30-day TTL after a trigger is conservative by design. In L3 contexts, the review trigger may be more granular (any PR affecting trust boundaries, for example). Integrating threat modelling into the CI cycle — even in lightweight review mode — is the recommended practice for L3.
- **THR-007**: Independent review serves two purposes: covering the team's blind spots (a team may struggle to identify threats in systems it knows deeply) and acting as a formal governance gate before go-live. Independence can be ensured by a centralised AppSec team, by peer review from a senior architect or by specialised consultancy — the criterion is the absence of a conflict of interest with the delivery.
- **THR-008**: The extension to AI/ML systems is mandatory when the system integrates components that produce decisions, classifications or content based on trained models or on prompts to LLMs. Adversarial threats to these components are qualitatively distinct — they do not reduce to classic STRIDE because the targets (training data, model weights, prompt context) and the mechanisms (adversarial examples, prompt injection, data poisoning) have no direct equivalent among traditional threats. MITRE ATLAS provides a catalogue of tactics/techniques specific to AI systems (in a format analogous to MITRE ATT&CK); NIST AI 100-2 e2025 establishes the formal taxonomy of adversarial ML attacks; NIST AI RMF 1.0 provides the organisation-level AI risk management framework. For operational methodology, see [Methodologies and Tools — §AI/ML](./metodologias-e-ferramentas#ai-ml).

---

> For threat modelling methodologies and tools, see [Methodologies and Tools](./metodologias-e-ferramentas).
> For validation and evidence of the threat modelling process, see [Validation and Evidence](./validacao-evidencia-threat-modeling).
> For the risks of the threat modelling process itself, see [Risks of the Threat Modelling Process](./riscos-processo-threat-modeling).
> For mapping threats to security requirements, see [Threat → Requirement Mapping](./mapeamento-threats-requisitos).
> For integrating threat modelling into CI/CD, see [Threat Modelling in CI/CD](./threat-modeling-ci).
> For threat modelling KPIs and metrics, see [Threat Modelling KPIs and Metrics](./11-kpis-metricas.md).
