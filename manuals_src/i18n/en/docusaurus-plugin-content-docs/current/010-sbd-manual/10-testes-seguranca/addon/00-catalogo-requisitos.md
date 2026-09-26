---
id: catalogo-requisitos-testes
title: Security Testing Requirements Catalogue
description: Canonical catalogue of requirements for the security testing programme (TST-001 to TST-010), with applicability by risk level and acceptance criteria for testing strategy, SAST, DAST, findings management, regression, pentesting and auditable evidence.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:testes, TST, SAST, DAST, IAST, fuzzing, pentesting, findings, rastreabilidade, L1, L2, L3, auditoria, evidencia]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/addon/00-catalogo-requisitos.md
  source_sha256: f33d36ea8c6b914979a4a9977a8db62fba3278734c6cd0f682098b20923253de
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 806906b450fc52b00120f392e4ca46bd2a32acf12d7be4e13e48e9b4613b554d
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 2ffd43fd37c8802a693f5fa1e43a3d3a9df1ca9d5ea898c88f6f405bedc9d687
  glossary_keys: [audit_trail, cycle_iteration, framework_source_corpus, lifecycle_phase, mapping, programme_line, requirement_runtime, risk_level, sbdtoe_sbd, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: 298158f90e7ced41926306b01a96db3981b562dd78e17cf0304552dfffd8b293
  translated_at: 2026-09-26T10:31:24Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Security Testing Requirements Catalogue

## Scope: the testing programme as a process requirement {#âmbito-o-programa-de-testes-como-requisito-de-processo}

This catalogue covers **requirements of the security testing programme** - the process controls that define how security tests are planned, executed, managed and evidenced throughout the lifecycle. It differs from the application-level input validation requirements (Ch. 02, VAL-) in that it focuses on the testing *programme* itself, not on the properties the software must have.

The scope includes: a formal testing strategy proportional to risk, SAST as a programmatic gate with managed coverage, DAST in a staging environment, findings management with SLAs, regression tests for fixed vulnerabilities, fuzzing and IAST for high-risk cases, periodic pentesting and the production of auditable and reproducible evidence.

For the complete mapping of all SbD-ToE requirements catalogues by technical domain, canonical prefix and owner, see [Ch. 02 - Catalogue Mapping](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **On curation:** Consolidated from OWASP SAMM (Practice: Security Testing), NIST SSDF (RV.1), OWASP ASVS (programmatic verification), DSOMM, NIST SP 800-115 (Technical Guide to Information Security Testing) and good practice for integrating security testing into the SDLC. It must be adapted to the technological context and reviewed with each update cycle of the testing strategy.

For instantiation in a project and operational naming (`SEC-Lx-TST-CODIGO`), see [Taxonomy and Traceability](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Conventions {#convenções}

| Symbol | Meaning |
|---------|-------------|
| ✔ | Requirement mandatory at this level |
| - | Not applicable or not mandatory at this level |

Levels are cumulative: L3 includes all L1 and L2 requirements; L2 includes all L1 requirements.

---

## TST Catalogue - Security Testing {#catálogo-tst---testes-de-segurança}

Requirements ensuring that the security testing programme is planned, executed, managed and evidenced in a way that is proportional to risk and auditable.

| ID | Name | L1 | L2 | L3 | Acceptance criterion |
|----|------|:--:|:--:|:--:|----------------------|
| TST-001 | Formal security testing strategy by risk level | ✔ | ✔ | ✔ | Strategy document with test types, frequency, owners and acceptance criteria by risk level; reviewed at least annually or after a significant change in risk or architecture. |
| TST-002 | SAST with a managed coverage profile and false-positive baseline | ✔ | ✔ | ✔ | SAST scanner with a documented and versioned rule profile; false-positive baseline approved by AppSec; evidence of coverage of critical components; false-positive rate reviewed periodically. |
| TST-003 | Formal findings management with remediation SLA by severity | ✔ | ✔ | ✔ | Remediation SLA defined by severity (e.g. critical ≤ 7 days, high ≤ 30 days); traceability finding → ticket → fix → verification; findings not resolved within the SLA with a formalised exception. |
| TST-004 | Reproducible, auditable test evidence linked to the build | ✔ | ✔ | ✔ | Security test reports associated with the build that generated them; reproducible from the same code state; retained for the period defined in policy; available for audit without the need for re-execution. |
| TST-005 | DAST integrated in a staging environment before promotion | - | ✔ | ✔ | DAST scanner active in a staging environment representative of production; findings policy defined (what blocks vs. what alerts); evidence of execution per release; staging environment with non-real data. |
| TST-006 | Security regression tests for fixed vulnerabilities | - | ✔ | ✔ | Each fixed vulnerability gives rise to a regression test that proves the fix and prevents recurrence; regression tests integrated in the pipeline; coverage evidence available. |
| TST-007 | Minimum security test coverage thresholds by risk | - | ✔ | ✔ | Minimum coverage criteria defined by risk level (e.g. authentication, authorisation, input validation components); coverage measured and reported; deviations documented and addressed. |
| TST-008 | Periodic penetration tests with defined scope and methodology | - | ✔ | ✔ | Pentesting executed with a minimum frequency defined by risk level (e.g. annual for L2, half-yearly for L3); documented scope; report with findings, severity and remediation plan; fixes verified in retest. |
| TST-009 | Systematic fuzzing of components processing complex input | - | - | ✔ | Fuzzing integrated in the pipeline or executed periodically for parsers, deserialisers, APIs with structured input or logic with high input entropy; managed corpus and evidence of execution available. |
| TST-010 | IAST in a staging environment for behavioural validation at runtime | - | - | ✔ | IAST instrumented in a staging environment for L3 applications; coverage of critical flows verified; IAST findings processed under the same management policy as other test findings. |

---

## Explanatory notes {#notas-explicativas}

- **TST-001**: The testing strategy is not a single, static document - it is an operational agreement that must be updated when the risk, the architecture or the technology stack changes. A strategy not reviewed for two years is probably inadequate.
- **TST-002**: The distinction between DEV-003 (SAST as a development gate) and TST-002 is one of perspective: DEV-003 deals with the gate in the coding/PR cycle; TST-002 deals with the SAST programme as a coverage control - which components are covered, what the quality of the profile is and how noise is managed.
- **TST-003**: Findings management is often the weak point of testing programmes: it is common to have active tools but untreated findings. An SLA without traceability is ineffective; traceability without an SLA is unauditable.
- **TST-005**: The staging environment must be sufficiently representative of production for the DAST results to be relevant - a staging environment whose configuration differs substantially from production produces misleading results.
- **TST-008**: Pentesting does not replace continuous automated testing - it complements it with contextualised adversarial validation. Retesting of fixes is an element frequently omitted but essential to close the cycle.

---

> For the integrated testing strategy in the SDLC, see [Testing Strategy](./estrategia-testes).
> For SAST, see [Static Analysis (SAST)](./sast).
> For DAST, see [Dynamic Analysis (DAST)](./dast).
> For findings management, see [Findings Management](./gestao-findings).
> For evidence and reproducibility, see [Evidence and Reproducibility](./evidencia-reprodutibilidade).
> For penetration testing, see [Pen Testing](./pen-testing).
