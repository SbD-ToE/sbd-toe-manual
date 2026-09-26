---
id: recomendacoes-avancadas
title: Advanced Practices in Threat Modelling
description: Reinforced recommendations for organisations with high maturity or demanding normative requirements
tags: [avançado, threat-modeling, baseline, sincronizacao, governação, métricas]
sidebar_position: 30
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/recomendacoes-avancadas.md
  source_sha256: 08ea0ba6a3dd54329dbe4117ea3efe9bec1bbd84ebe918af8fdb91280186417b
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 4d7b92df4c7cbc85bb804b44a4da1f544ed281d707fbf090b0b781aac235e27b
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, basilar, chapter_role, discipline, framework_source_corpus, maturity, segregacao_de_funcoes, threat, traceability]
  glossary_sha256: 33107224395756424a324b1feda5d49bb1f92dfdc9ac4766dafdb4eedeb81d32
  translated_at: 2026-09-25T20:17:08Z
  stamped_at: 2026-09-26T18:33:29Z
  reviewed_by: null
---

# Advanced Practices in Threat Modelling

This annex presents **optional** practices intended for organisations with greater maturity, demanding normative obligations (e.g. NIS2, DORA, ISO 27034, IEC 62443) or teams with already consolidated security engineering processes.

> These practices **do not replace** the foundational prescriptions of Chapter 3.  
> They are optional extensions that **reinforce governance, traceability and evidence**, contributing to higher maturity levels (e.g. OWASP SAMM / OWASP DSOMM), when adopted.

---

## 🧱 1. Baselines and *Tailoring* of Threat Models {#-1-baselines-e-tailoring-de-modelos-de-ameaça}

**Objective:** Standardise the Threat Modelling process across projects and reuse previously validated knowledge, reducing variability and the risk of omission.

- Define **organisational baselines** by relevant architectural patterns (e.g. 3-tier web, microservices, event-driven, batch/ETL, B2B integrations).
- Each project must **adopt a baseline** as its starting point and document changes (*tailoring*) with:
  - context differences (data, trust boundaries, dependencies, exposure);
  - threats removed and why;
  - threats added and why.
- The *tailoring* review must be **approved** by an explicit role (e.g. AppSec / Security Architect) before the model is considered “approved”.
- Baselines must maintain **stable links** to relevant requirements and controls (e.g. `REQ-*`, `THREAT-*`, `ARC-*` where applicable).

**Expected artefacts**
- `baseline/<pattern>.(md|yaml|json)`
- `tailoring-notes.md`
- Approval record (PR/issue/signature according to the process)

---

## 🔄 2. Synchronisation between Model Representations {#-2-sincronização-entre-representações-do-modelo}

**Objective:** Avoid divergences between the representation of the Threat Model in the versioned repository and other representations used by the team (e.g. exports, internal templates, structured formats).

- Define a **canonical format** for the Threat Model for versioning (e.g. Markdown + structured YAML, or another stable internal format).
- Implement a synchronisation process that guarantees:
  - **stable identifiers** for threats and decisions (`THREAT-*`, `DEC-*`, etc.);
  - **idempotence** (running again must neither degrade nor duplicate information);
  - a record of **differences** (*diff report*) when inconsistencies exist.
- Generate consistency and coverage reports **as outputs** (artefacts), not as decisions:
  - decision coverage (all threats have a decision);
  - link coverage (threats linked to requirements/mitigations);
  - percentage of “fresh” models (reviewed within the defined window).

**Expected artefacts**
- `tm-sync.log` (or equivalent)
- `tm-diff-report.(md|csv|json)`
- `tm-coverage.(md|csv|json)` (objective and auditable metrics)

---

## ⚖️ 3. Proportional Security *Gates* (L1–L3) {#️-3-gates-de-segurança-proporcionais-l1l3}

**Objective:** Ensure that Threat Modelling effectively influences release decisions, in proportion to the risk, and with auditable evidence.

Instead of rigid percentages, use **deterministic state-based criteria**:

### 3.1 Minimum criteria (per level L1–L3) {#31-critérios-mínimos-por-nível-l1l3}

- **L1 (low risk)**
  - Existing Threat Model **or** approved justification of non-applicability.
  - No “High” threat in the “No decision” state.
  - Exceptions allowed with a simple record and a review deadline.

- **L2 (medium risk)**
  - **Approved** Threat Model (baseline + reviews) for the version/architecture to be released.
  - All “High” threats:
    - with an explicit decision (mitigate/accept/transfer/reject with justification),
    - with an *owner*,
    - with evidence of mitigation or formal acceptance.
  - Exceptions with a *sunset* and compensating mitigation where applicable.

- **L3 (high risk)**
  - Approved Threat Model with **segregation of duties** (independent review).
  - No “High” threat may go into production without:
    - mitigation implemented **or**
    - formal acceptance with compensations, a short *sunset* and appropriate approval.
  - Mandatory revalidation when structural changes exist since the last approval.

### 3.2 *Gate* evidence {#32-evidência-do-gate}
The *gate* must produce verifiable evidence:
- referenced Threat Model version (commit/tag);
- status report (high threats, decisions, owners, deadlines);
- record of approvals and exceptions.

**Expected artefacts**
- `gates-l1-l3.md` (defined rules and thresholds)
- `tm-gate-report.(md|csv|json)`
- Formal approval recorded

**Relation to frameworks**
| Reference | Domain | Benefit |
|---|---|---|
| SSDF (RV) | Risk Validation | Objective governance before production |
| OWASP SAMM (Verification) | Quality & Release Gating | Evidence-based *go/no-go* criteria |
| OWASP DSOMM (Measurement/Metrics) | Continuous Improvement | Auditable and actionable metrics |

---

## 📈 4. Coverage Metrics and *Dashboards* {#-4-métricas-e-dashboards-de-cobertura}

**Objective:** Measure the effectiveness, currency and discipline of the Threat Modelling process without encouraging “gaming”.

Recommended metrics (objective and auditable):
- **Freshness**: time since the last review/approval of the Threat Model;
- **Decision Coverage**: % of threats with an explicit decision;
- **High-Risk Hygiene**:
  - no. of “High” threats without an owner,
  - no. of “High” threats without associated evidence,
  - no. of “High” exceptions past their deadline (expired *sunset*);
- **Traceability Coverage**: % of threats linked to requirements/mitigations and to evidence of tests/validations;
- **Delta Volume**: no. of significant changes since the last review (proxy for the risk of obsolescence).

The *dashboards* must be:
- derived from versioned artefacts and control outputs (not from opinion);
- reproducible (same source, same result);
- used for organisational decision-making (priority, risk debt, auditing).

---

## ✅ Final considerations {#-considerações-finais}

These practices raise maturity and operational discipline when:
- there is a regulatory/certification requirement;
- there are multiple teams/projects and a need for standardisation;
- systematic risk control with auditable evidence is intended.

> 📌 This annex complements the chapter's `15-aplicacao-lifecycle.md`, which defines the mandatory foundational practices and the integration into the SSDLC.
