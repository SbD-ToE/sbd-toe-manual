---
id: rastreabilidade
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/canon/25-rastreabilidade.md
  source_sha256: 3796492514ff67db90a6e55e4df6cac70fa157f136b4ab6a0b19abc16a9a9949
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 25c1a7a1665083521aea595429015233bdb7b0ce0905d8026940283b21e9e3f1
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 2ffd43fd37c8802a693f5fa1e43a3d3a9df1ca9d5ea898c88f6f405bedc9d687
  glossary_keys: [appsec_core, audit_trail, avaliacao, chapter_role, practitioner_manual, risk_level, sbdtoe_sbd, slice, traceability, v1_entity_tsv_specialized_depth, v1_entity_tsv_specialized_testing, validation_evaluation]
  glossary_sha256: be6895156acc86f557b151d045dcd8425ab0eb9aa2847cf9ebc7c87c095af0f8
  translated_at: 2026-09-26T10:31:37Z
  reviewed_by: null
---

# 25. Traceability — Security Testing

## Summary {#sumário}

This chapter is the **primary anchor** of the AppSec Core V1 slices: `ACO-TSV` (Security testing and empirical validation).

V1 entity-level coverage: **19 primary entities**. The structure below exposes the **five-section routing** (per Run 1 amendment 2026-05-11; P8 pipeline primitive demonstration):

- **§ Manual ontology V2 entities** — canonical Manual ontology V2 entities mapped to this chapter (KG canonical data)
- **§ Core-mapped coverage** — V1 entity → Manual ontology V2 anchor → Manual section anchor → §26 methodology label → ES grounding
- **§ Manual-only coverage** — Manual sections out-of-Core-scope but directly ES-grounded
- **§ Out-of-AppSec coverage** — Pure editorial sections (examples, narratives) without ES grounding
- **§ Future-work register** — Content gaps registered as P8 §10 candidates

---

## § Manual ontology V2 — canonical entities of this chapter {#-manual-ontology-v2--entities-canónicas-deste-capítulo}

Total: **43 entities** of Manual ontology V2 mapped to this chapter via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `TST-001` | Formal security testing strategy by risk level | normative | explicit | deterministic |
| Requirement | `TST-002` | SAST with managed coverage profile and false-positive baseline | normative | explicit | deterministic |
| Requirement | `TST-003` | Formal findings management with remediation SLA by severity | normative | explicit | deterministic |
| Requirement | `TST-004` | Reproducible, auditable test evidence linked to the build | normative | explicit | deterministic |
| Requirement | `TST-005` | DAST integrated in the staging environment before promotion | normative | explicit | deterministic |
| Requirement | `TST-006` | Security regression tests for fixed vulnerabilities | normative | explicit | deterministic |
| Requirement | `TST-007` | Minimum security test coverage thresholds by risk | normative | explicit | deterministic |
| Requirement | `TST-008` | Periodic penetration tests with defined scope and methodology | normative | explicit | deterministic |
| Requirement | `TST-009` | Systematic fuzzing on components that process complex input | normative | explicit | deterministic |
| Requirement | `TST-010` | IAST in the staging environment for behavioural validation at runtime | normative | explicit | deterministic |
| Control | `CTRL-testing-testes-de-seguranca-baseados-em-risco-55dcb62d34` | Risk-based security testing | normative | explicit | deterministic |
| Practice | `10-testes-seguranca:avaliacao-critica-de-cobertura-real-e-limitacoes` | Critical assessment of real coverage and limitations | normative | explicit | deterministic |
| Practice | `10-testes-seguranca:criterios-de-release-e-aceitacao-de-risco` | Release criteria and risk acceptance | normative | explicit | deterministic |
| Practice | `10-testes-seguranca:dast-autenticado-em-staging` | Authenticated DAST in Staging | normative | explicit | deterministic |
| Practice | `10-testes-seguranca:decisao-assistida-para-findings-de-testes-de-seguranca` | Assisted Decision for Security Test Findings | normative | explicit | deterministic |
| Practice | `10-testes-seguranca:estrategia-formal-de-testes-por-aplicacao` | Formal test strategy per application | normative | explicit | deterministic |
| Practice | `10-testes-seguranca:feedback-automatico-de-findings-as-equipas` | Automatic Feedback of Findings to Teams | normative | explicit | deterministic |
| Practice | `10-testes-seguranca:fuzzing-dirigido-a-apis-criticas` | Fuzzing targeted at critical APIs | normative | explicit | deterministic |
| Practice | `10-testes-seguranca:gates-de-seguranca-no-ci-cd` | Security gates in the CI/CD | normative | explicit | deterministic |
| Practice | `10-testes-seguranca:gestao-centralizada-de-findings-com-triagem-e-sla` | Centralised Findings Management with Triage and SLA | normative | explicit | deterministic |
| Practice | `10-testes-seguranca:iast-com-instrumentacao-em-staging` | IAST with Instrumentation in Staging | normative | explicit | deterministic |
| Practice | `10-testes-seguranca:pentesting-ofensivo-baseado-em-risco` | Risk-based offensive PenTesting | normative | explicit | deterministic |
| Practice | `10-testes-seguranca:regressoes-de-seguranca-automatizadas` | Automated security regressions | normative | explicit | deterministic |
| Practice | `10-testes-seguranca:reprodutibilidade-de-resultados-criticos-de-testes-de-seguranca` | Reproducibility of critical security test results | normative | explicit | deterministic |
| Practice | `10-testes-seguranca:sast-obrigatorio-em-pull-request` | Mandatory SAST in Pull Request | normative | explicit | deterministic |
| Practice | `10-testes-seguranca:separacao-formal-entre-sinal-automatico-e-decisao-de-bloqueio-override` | Formal separation between automatic signal and blocking/override decision | normative | explicit | deterministic |
| Practice | `10-testes-seguranca:validacao-empirica-de-exploitabilidade-de-findings` | Empirical Validation of Findings Exploitability | normative | explicit | deterministic |
| Practice | `10-testes-seguranca:validacao-humana-da-interpretacao-final-dos-resultados` | Human validation of the final interpretation of results | normative | explicit | deterministic |
| Threat | `None` | hybrid | normative | heuristic | bounded |

> Authority class / source mode / confidence model: per Manual ontology V2 definition (`sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml`, `meta.version: '2.0'`).

---

## § Core-mapped coverage {#-core-mapped-coverage}

Table exposing V1 entity-level coverage with Manual ontology V2 anchor + Manual section anchor + §26 methodology label + substrate v7 ES grounding.

### Slice `ACO-TSV` — Security testing and empirical validation {#slice-aco-tsv--testes-de-segurança-e-validação-empírica}

| V1 entity | Type | Manual V2 anchor | Manual section anchor | Authority | Source mode | §26 label | ES grounding |
|---|---|---|---|---|---|---|---|
| `ACM-TSV-001` — Integrated Security Scanners | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AU-6.2, SP800-53-CA-3.1; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_A, SAMM-ACTIVITY-D_SA_1_B; DSOMM: DSOMM-ACTIVITY-47419324E263415B815DE7161B6B905E, DSOMM-ACTIVITY-48F97F31931C46EB9B3EE2FEC0CD0426; PCI DSS v4.0.1: PCI-REQ-2, PCI-REQ-5; + 17 more sources |
| `ACM-TSV-002` — Test Execution Surfaces | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | DSOMM: DSOMM-ACTIVITY-A340F46B63604CB8847BA0D3483D09D3, DSOMM-ACTIVITY-BFDACB521E3F431DAE72D844A5E86415; SP 800-53 r5: SP800-53-CA-8.2, SP800-53-CM-2.6; SAMM v2.1: SAMM-ACTIVITY-I_SB_3_B, SAMM-ACTIVITY-I_SD_2_A; MITRE ATLAS: AML.TA0005, AML.T0011; + 4 more sources |
| `ACM-TSV-003` — CI/CD Gate And Release Promotion | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-3.9, SP800-53-AU-10.3; PCI DSS v4.0.1: PCI-1.2.2, PCI-1.3.1; SAMM v2.1: SAMM-ACTIVITY-I_SD_3_B, SAMM-ACTIVITY-O_OM_1_A; MITRE ATLAS: AML.T0054, AML.M0001; + 7 more sources |
| `ACM-TSV-004` — Findings Workflow And Exception Governance | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-4.9, SP800-53-AU-1; SAMM v2.1: SAMM-ACTIVITY-G_EG_3_A, SAMM-ACTIVITY-G_PC_1_A; CIS Controls v8.1.2: CIS-17, CIS-17.1; PCI DSS v4.0.1: PCI-2.1.2, PCI-6.5.2; + 10 more sources |
| `ACM-TSV-005` — Static Analysis Profile Management | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | DSOMM: DSOMM-ACTIVITY-71699DAFB2A4466BA0B289F7DBB18506, DSOMM-ACTIVITY-E237176BBEC5447DA926E37D6DD60E4B; SP 800-53 r5: SP800-53-CM-2, SP800-53-CM-8; NIST AI RMF 1.0: NIST-AI-RMF-MEASURE-4.3, NIST-AI-RMF-MANAGE-4.3; SAMM v2.1: SAMM-ACTIVITY-D_TA_3_A, SAMM-ACTIVITY-O_EM_3_A; + 1 more sources |
| `ACO-TSV-001` — Risk-Proportional Security Testing Strategy | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-CP-8.5, SP800-53-PL-2; SAMM v2.1: SAMM-ACTIVITY-D_SR_2_A, SAMM-ACTIVITY-D_SR_3_A; CAPEC v3.9: CAPEC-420; CIS Controls v8.1.2: CIS-16.14; + 5 more sources |
| `ACO-TSV-002` — Static Analysis Signal Quality And Baseline Governance | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | DSOMM: DSOMM-ACTIVITY-E237176BBEC5447DA926E37D6DD60E4B, DSOMM-ACTIVITY-6C05C8378C9946E2828B7C903E27DBA4; SAMM v2.1: SAMM-ACTIVITY-G_PC_1_B, SAMM-ACTIVITY-G_PC_2_B; SP 800-53 r5: SP800-53-SA-11.1; SAFECode Agile: SCAGILE-OPS-4 |
| `ACO-TSV-003` — Security Finding Triage And Correction Closure | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-3.5, SP800-53-AU-6; PCI DSS v4.0.1: PCI-3.3.2, PCI-3.3.3; ASVS v5: ASVS-REQ-V14.2.4, ASVS-REQ-V14.2.7; CAPEC v3.9: CAPEC-54, CAPEC-144; + 9 more sources |
| `ACO-TSV-004` — Reproducible Security Test Evidence And Build Traceability | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | ASVS v5: ASVS-REQ-V1.4.1, ASVS-REQ-V1.4.3; SAMM v2.1: SAMM-ACTIVITY-I_SB_1_A, SAMM-ACTIVITY-I_SB_2_B; SLSA v1.0: SLSA-BUILD-L1, SLSA-BUILD-L2; DSOMM: DSOMM-ACTIVITY-A340F46B63604CB8847BA0D3483D09D3, DSOMM-ACTIVITY-7121B0C76ACE4D6B95D094535DBCCB57; + 10 more sources |
| `ACO-TSV-005` — Staged Dynamic Validation And Release Gate Discipline | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | MITRE ATLAS: AML.T0054, AML.T0073; SP 800-53 r5: SP800-53-CM-3, SP800-53-CM-3.5; CAPEC v3.9: CAPEC-443, CAPEC-671; SAMM v2.1: SAMM-ACTIVITY-I_SD_1_A, SAMM-ACTIVITY-I_SD_2_A; + 3 more sources |
| `ACO-TSV-006` — Specialized Empirical Testing Depth And Regression Assurance | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | NIST AI 100-2 e2025: NIST-AI-100-2-E2025-2.1, NIST-AI-100-2-E2025-2.1.3; MITRE ATLAS: AML.T0001, AML.T0016.000; DSOMM: DSOMM-ACTIVITY-F0E018143B884BD0A3A9F91DB001D20BADVANCED, DSOMM-ACTIVITY-5E0FF85BEC894EF096B15695FA0025DC; CAPEC v3.9: CAPEC-28, CAPEC-100; + 9 more sources |
| `ACO-TSV-007` — Security Testing And Empirical Assurance Integrity | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AU-6.2, SP800-53-CA-4; SAMM v2.1: SAMM-ACTIVITY-D_SA_2_A, SAMM-ACTIVITY-D_SA_3_B; DSOMM: DSOMM-ACTIVITY-12C90CC63D584D9B82FFD469D2A0C298, DSOMM-ACTIVITY-0B28367B75A04BAEA9263725C1BF9BB0; PCI SSLC v1.1: PCISSLC-1.3, PCISSLC-2.3; + 13 more sources |
| `ACP-TSV-001` — Risk-Based Security Test Planning | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-CA-2, SP800-53-CA-7.4; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_A, SAMM-ACTIVITY-D_SR_1_A; CIS Controls v8.1.2: CIS-7, CIS-7.1; PCI DSS v4.0.1: PCI-REQ-6, PCI-5.2.3; + 7 more sources |
| `ACP-TSV-002` — Governed Static Analysis Execution | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | DSOMM: DSOMM-ACTIVITY-517B095749814AC0B4C70D8D1934C474, DSOMM-ACTIVITY-E237176BBEC5447DA926E37D6DD60E4B; SAFECode Agile: SCAGILE-OPS-4, SCAGILE-OPS-9; CAPEC v3.9: CAPEC-190, CAPEC-191; SP 800-53 r5: SP800-53-SA-11.1, SP800-53-SA-11.8; + 2 more sources |
| `ACP-TSV-003` — Findings Triage, SLA And Retest Closure | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AU-1, SP800-53-CA-1; SAMM v2.1: SAMM-ACTIVITY-G_EG_3_A, SAMM-ACTIVITY-G_PC_1_A; CIS Controls v8.1.2: CIS-15.5; PCI SSLC v1.1: PCISSLC-5.1; + 2 more sources |
| `ACP-TSV-004` — Reproducible Test Evidence Management | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AU-2.1, SP800-53-AU-3; CIS Controls v8.1.2: CIS-3.1, CIS-8; PCI DSS v4.0.1: PCI-10.2.2, PCI-10.3.3; SLSA v1.0: SLSA-BUILD-L1, SLSA-BUILD-L2; + 6 more sources |
| `ACP-TSV-005` — Staged Dynamic Testing And Gate Enforcement | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-3.12, SP800-53-CM-3.5; CAPEC v3.9: CAPEC-121, CAPEC-443; MITRE ATLAS: AML.TA0001, AML.T0011.000; SAMM v2.1: SAMM-ACTIVITY-I_SD_2_A, SAMM-ACTIVITY-I_SD_3_B; + 7 more sources |
| `ACP-TSV-006` — Specialized Empirical Testing | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SSDF v1.1: SSDF-PRACTICE-PW.8, SSDF-PRACTICE-RV.1; CAPEC v3.9: CAPEC-28, CAPEC-215; NIST AI 100-2 e2025: NIST-AI-100-2-E2025-3.3.1, NIST-AI-100-2-E2025-3.6; MITRE ATLAS: AML.T0001, AML.M0008; + 5 more sources |
| `ACP-TSV-007` — Human Review Of Security Test Signals | P | Practice | chapter prose (final, release, review kws verified) | normative | explicit | Semantic | SP 800-53 r5: SP800-53-AC-4.9, SP800-53-AU-6.2; PCI DSS v4.0.1: PCI-1.2.2, PCI-5.4.1; SAMM v2.1: SAMM-ACTIVITY-D_SA_3_B, SAMM-ACTIVITY-I_SD_2_A; PCI SSLC v1.1: PCISSLC-2.6, PCISSLC-6.2; + 11 more sources |

---

## § Manual-only coverage (out-of-Core-scope; ES-grounded direct) {#-manual-only-coverage-out-of-core-scope-es-grounded-direct}

Manual sections covering topics outside the scope of the V1 AppSec Core ontology (maturity models, organisational policies, KPIs/metrics, glossaries) but with direct ES grounding.

| Manual section | Manual V2 anchor | Authority | ES grounding (direct) |
|---|---|---|---|
| `achievable-maturity.md` | MaturityMapping | external | SAMM v2.1 ST maturity; DSOMM testing activities |
| `policies-relevantes.md` | PolicyReference | editorial / external | Security Testing Policy |
| `addon/00-catalogo-requisitos.md` | ExternalFramework | external | Requirements catalogue with meta-testing components |

---

## § Out-of-AppSec coverage (pure editorial) {#-out-of-appsec-coverage-pure-editorial}

Manual sections that are pure editorial content (worked examples, narratives, illustrative cases, vendor-specific tooling integration). No ES grounding.

| Manual section | Content type | Manual V2 anchor (if any) |
|---|---|---|
| `addon/11-pen-testing.md` | Pen-testing narrative and operational content | DocumentUnit |
| `addon/13-ia-nos-testes.md` | AI in testing — operational guidance | DocumentUnit |

---

## § Future-work register (P8 §10 candidates) {#-future-work-register-p8-10-candidates}

_(No entries in the future-work register for this chapter.)_

---

## Generation provenance {#generation-provenance}

- **Manual ontology V2 canonical:** `sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml` (`meta.version: '2.0'`)
- **KG canonical state:** sbd-toe-knowledge-graph master @ `5550a74` (`kg-v1-cycle-b-iter-3-aligned-2026-05-11`)
- **Substrate version:** v7 (SUPPLIER sha256 `596783ed984d9c0e8c8ef6439a0eaee8fbaf2d863af37138cde8fad55d62be04`)
- **V1 entity index:** `ontology-v1.1-fair-baseline` @ `84fe8bf` in sbd-toe-ontology
- **Per-entity source map:** `data/p8_inputs/per_entity_source_map.json` @ ESI commit `aa3c13c`
- **Phase 2/3 gap analysis:** `phase2_3_per_entity_classification.json` @ ESI commit `b8cd401`
- **Generated by:** Manual Agent Run 1 (Iter 4 baseline @ `16dfa5ae` + Manual ontology V2 vocab layer injection)
- **Format:** 5-section (Manual V2 entities + Core-mapped + Manual-only + Out-of-AppSec + Future-work) per dispatch vision 2026-05-11
- **§26 methodology labels:** per `00-fundamentos/canon/26-metodologia-validacao-claims.md` (post Run 1 Step 0 refresh)
- **Cycle:** Cycle B Run 1 (post Iter 4)
