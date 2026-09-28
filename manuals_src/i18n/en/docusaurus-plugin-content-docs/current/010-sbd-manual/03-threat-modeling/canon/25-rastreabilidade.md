---
# Proveniência da geração: não se mostra ao leitor (extraída do corpo na v1.17.1).
sbdtoe_provenance:
  ontology_v2: 'sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml (meta.version: ''2.0'')'
  kg_state: sbd-toe-knowledge-graph master @ 5550a743bb9de205676c503da5e81863ed62ab54 (2026-05-11; commit de governação imediatamente a seguir à tag kg-v1-cycle-b-iter-3-aligned-2026-05-11 @ 482ece916cc254126894019432ebd113695365d9)
  substrate: v7 (SUPPLIER sha256 596783ed984d9c0e8c8ef6439a0eaee8fbaf2d863af37138cde8fad55d62be04)
  v1_index: ontology-v1.1-fair-baseline @ 84fe8bf6f5de1443d778f9b2f0555b722540bbff em sbd-toe-ontology
  source_map: data/p8_inputs/per_entity_source_map.json @ ESI commit aa3c13cd39db8277a7066755d692eb37ee5b7ecd
  gap_analysis: phase2_3_per_entity_classification.json @ ESI commit b8cd4016f8876721046953363eee2995bc62a3f0
  generated_by: Manual Agent Run 1 (Iter 4 baseline @ 16dfa5ae1f6aabd811e34dd8f7299453f4f9b786 + Manual ontology V2 vocab layer injection)
  cycle: Cycle B Run 1 (post Iter 4)
  notes:
  - 'Format: 5-section (Manual V2 entities + Core-mapped + Manual-only + Out-of-AppSec + Future-work) per dispatch vision 2026-05-11'
  - '§26 methodology labels: per 00-fundamentos/canon/26-metodologia-validacao-claims.md (post Run 1 Step 0 refresh)'
  - Five-section routing per Run 1 amendment 2026-05-11 (P8 pipeline primitive demonstration)
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/canon/25-rastreabilidade.md
  source_sha256: 359150b8a813983fcf94ebd6243e0174f4aa178824d7a691e835c0f69e54e0f8
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: fc74ba22eeee254d649333378f535e6392567cfbc10142ced49d1ac3d3c6598f
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [appsec_core, chapter_role, cycle_iteration, practitioner_manual, requirement_runtime, slice, slug_threat_modeling, threat, traceability, v1_entity_tmr_risk_governance, v1_entity_tmr_scope_trigger, validation_evaluation]
  glossary_sha256: eb27950a32da6f4f7a0b128c3904eb05fe16381dd52e8f86196a66157357fc86
  translated_at: 2026-09-28T09:11:59Z
  stamped_at: 2026-09-28T09:11:59Z
  reviewed_by: null
---

# 25. Traceability — Threat Modelling

## Summary {#sumário}

This chapter is the **primary anchor** of the AppSec Core V1 slices: `ACO-TMR` (Threat modelling, risk management and mitigation traceability).

V1 entity-level coverage: **25 primary entities**. The structure below exposes the **five-section routing**:

- **§ Manual ontology V2 entities** — canonical Manual ontology V2 entities mapped to this chapter (KG canonical data)
- **§ Core-mapped coverage** — V1 entity → Manual ontology V2 anchor → Manual section anchor → §26 methodology label → ES grounding
- **§ Manual-only coverage** — Manual sections out-of-Core-scope but directly ES-grounded
- **§ Out-of-AppSec coverage** — Pure editorial sections (examples, narratives) without ES grounding
- **§ Future-work register** — Content gaps registered as P8 §10 candidates

---

## § Manual ontology V2 — canonical entities of this chapter {#-manual-ontology-v2--entities-canónicas-deste-capítulo}

Total: **76 entities** of Manual ontology V2 mapped to this chapter.

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `THR-001` | Formal threat modelling in L2+ applications and significant architectural changes | normative | explicit | deterministic |
| Requirement | `THR-002` | Current architecture represented with explicit DFDs and trust boundaries | normative | explicit | deterministic |
| Requirement | `THR-003` | Structured methodology applied with guaranteed minimum coverage | normative | explicit | deterministic |
| Requirement | `THR-004` | Formal disposition of each identified threat, with an owner | normative | explicit | deterministic |
| Requirement | `THR-005` | Threat → requirement → backlog → validation traceability | normative | explicit | deterministic |
| Requirement | `THR-006` | Threat model versioned and updated within the cycle or after a trigger | normative | explicit | deterministic |
| Requirement | `THR-007` | Independent review by AppSec before go-live at L2 and L3 | normative | explicit | deterministic |
| Control | `CTRL-governance-threat-modeling-e-gestao-de-risco-272c9a8ed0` | Threat modelling and risk management | normative | explicit | deterministic |
| Practice | `03-threat-modeling:aplicacao-linddun-quando-existir-tratamento-de-dados-pessoais-novo` | LINDDUN application where personal data are processed  *(new)* | normative | explicit | deterministic |
| Practice | `03-threat-modeling:aprovacao-formal-do-threat-model-baseline-e-revisoes` | Formal approval of the Threat Model (baseline and revisions) | normative | explicit | deterministic |
| Practice | `03-threat-modeling:atualizacao-do-modelo-apos-alteracao-tecnica` | Updating of the model after a technical change | normative | explicit | deterministic |
| Practice | `03-threat-modeling:controlo-de-acesso-classificacao-e-retencao-dos-artefactos-de-threat-modeling` | Access control, classification and retention of Threat Modelling artefacts | normative | explicit | deterministic |
| Practice | `03-threat-modeling:criacao-do-modelo-de-ameaca` | Creation of the threat model | normative | explicit | deterministic |
| Practice | `03-threat-modeling:gate-de-controlo-de-consistencia-no-ci-cd` | Consistency control gate in the CI/CD | normative | explicit | deterministic |
| Practice | `03-threat-modeling:justificacao-formal-de-risco-aceite` | Formal justification of accepted risk | normative | explicit | deterministic |
| Practice | `03-threat-modeling:reutilizacao-controlada-e-revisao-de-modelos-anteriores` | Controlled reuse and review of earlier models | normative | explicit | deterministic |
| Practice | `03-threat-modeling:validacao-de-arquitetura-com-threat-modeling` | Architecture validation with threat modelling | normative | explicit | deterministic |
| Practice | `03-threat-modeling:validacao-de-impacto-no-negocio` | Business impact validation | normative | explicit | deterministic |
| Threat | `MT-039` | Unknown and unaddressed threats | normative | heuristic | bounded |
| Threat | `MT-040` | Poorly defined security priorities | normative | heuristic | bounded |
| Threat | `MT-041` | Requirements defined without a basis in threats | normative | heuristic | bounded |
| Threat | `MT-042` | Privacy threats ignored | normative | heuristic | bounded |
| Threat | `MT-043` | Lack of coverage of non-technical threats | normative | heuristic | bounded |
| Threat | `MT-044` | Insecure architecture not identified | normative | heuristic | bounded |
| Threat | `MT-045` | Superficial validation in design reviews | normative | heuristic | bounded |
| Threat | `MT-046` | Controls applied without a basis in architecture | normative | heuristic | bounded |
| Threat | `MT-047` | Absence of review of critical interfaces | normative | heuristic | bounded |
| Threat | `MT-048` | Threats discovered too late | normative | heuristic | bounded |
| Threat | `MT-049` | Critical changes without new modelling | normative | heuristic | bounded |
| Threat | `MT-050` | Discontinuity between teams and phases | normative | heuristic | bounded |
| Threat | `MT-051` | Threats not visible in the CI/CD pipeline | normative | heuristic | bounded |
| Threat | `MT-052` | Threat knowledge not accumulated | normative | heuristic | bounded |
| Threat | `MT-053` | Inconsistency between projects and teams | normative | heuristic | bounded |
| Threat | `MT-054` | Tools disconnected from the cycle | normative | heuristic | bounded |
| Concept | `sem:concept:backlog-items` | Backlog Items | semantic | scored | bounded |
| Concept | `sem:concept:catalogo-de-requisitos` | Requirements Catalogue | semantic | scored | bounded |
| Concept | `sem:concept:context-diagrams` | Context Diagrams | semantic | scored | bounded |
| Concept | `sem:concept:dfds` | DFDs | semantic | scored | bounded |
| Concept | `sem:concept:evidencia-minima-obrigatoria` | Minimum mandatory evidence | semantic | scored | bounded |
| Concept | `sem:concept:linddun` | LINDDUN | semantic | scored | bounded |
| Concept | `sem:concept:modelo-de-arquitetura` | Architecture model | semantic | scored | bounded |
| Concept | `sem:concept:modelos-reutilizaveis` | Reusable models | semantic | scored | bounded |
| Concept | `sem:concept:niveis-de-criticidade` | Criticality levels | semantic | scored | bounded |
| Concept | `sem:concept:omissao-estrutural-de-ameacas` | Structural omission of threats | semantic | scored | bounded |
| Concept | `sem:concept:pasta` | PASTA | semantic | scored | bounded |
| Concept | `sem:concept:processo-decisional-estruturado` | Structured decision process | semantic | scored | bounded |
| Concept | `sem:concept:stride` | STRIDE | semantic | scored | bounded |
| Concept | `sem:concept:threat-modeling` | Threat Modelling | semantic | scored | bounded |
| Mechanism | `sem:mechanism:data-e-versao-do-modelo` | Date and version of the model | semantic | scored | bounded |
| Mechanism | `sem:mechanism:dfds` | DFDs | semantic | scored | bounded |
| Mechanism | `sem:mechanism:diagramas-versionados` | Versioned diagrams | semantic | scored | bounded |
| Mechanism | `sem:mechanism:identificacao-do-responsavel-pela-validacao` | Identification of the person responsible for validation | semantic | scored | bounded |
| Mechanism | `sem:mechanism:ligacao-a-requisitos-de-seguranca-ou-mitigacoes` | Link to security requirements or mitigations | semantic | scored | bounded |
| Mechanism | `sem:mechanism:linddun` | LINDDUN | semantic | scored | bounded |
| Mechanism | `sem:mechanism:lista-de-ameacas-com-decisao-explicita` | List of threats with an explicit decision | semantic | scored | bounded |
| Mechanism | `sem:mechanism:pasta` | PASTA | semantic | scored | bounded |
| Mechanism | `sem:mechanism:specialized-tools` | Specialised Tools | semantic | scored | bounded |
| Mechanism | `sem:mechanism:stride` | STRIDE | semantic | scored | bounded |
| Mechanism | `sem:mechanism:trust-boundaries` | trust boundaries | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:ausencia-de-ameaca-no-modelo` | Absence of a threat from the model | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:omissao-estrutural-de-ameacas` | Structural omission of threats | semantic | scored | bounded |

> Authority class / source mode / confidence model: as defined by the Manual ontology (v2).

---

## § Core-mapped coverage {#-core-mapped-coverage}

Table exposing V1 entity-level coverage with Manual ontology V2 anchor + Manual section anchor + §26 methodology label + substrate v7 ES grounding.

### Slice `ACO-TMR` — Threat modelling, risk management and mitigation traceability {#slice-aco-tmr--threat-modeling-gestão-de-risco-e-rastreabilidade-de-mitigações}

| V1 entity | Type | Manual V2 anchor | Manual section anchor | Authority | Source mode | §26 label | ES grounding |
|---|---|---|---|---|---|---|---|
| `ACM-TMR-001` — Threat Representation Models | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-SA-8.10, SP800-53-SA-8.16; CWE SDV v4.19.1: CWE-807; PCI SSLC v1.1: PCISSLC-3.2 |
| `ACM-TMR-002` — Structured Threat Analysis Frameworks | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-CP-12, SP800-53-IR-10; EU DORA: DORA-ART-6, DORA-ART-13; SAMM v2.1: SAMM-ACTIVITY-D_TA_1_A, SAMM-ACTIVITY-D_TA_2_A; SSDF v1.1: SSDF-TASK-PW.1.1, SSDF-TASK-RV.2.1; + 9 more sources |
| `ACM-TMR-003` — Threat Model Versioning Controls | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | MITRE ATLAS: AML.TA0006, AML.T0010.003; SP 800-53 r5: SP800-53-CM-2.3, SP800-53-CP-2; CAPEC v3.9: CAPEC-166, CAPEC-186; SAMM v2.1: SAMM-ACTIVITY-D_SA_3_A, SAMM-ACTIVITY-D_TA_2_B; + 10 more sources |
| `ACM-TMR-004` — Explicit Threat Disposition Register | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | HIPAA: HIPAA-164-308a6; SP 800-53 r5: SP800-53-AT-2.2; SAMM v2.1: SAMM-ACTIVITY-G_SM_1_A |
| `ACM-TMR-005` — Threat Mitigation Linkage Controls | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-3.5, SP800-53-AC-3.6; CAPEC v3.9: CAPEC-37, CAPEC-38; MITRE ATLAS: AML.T0003, AML.T0008; PCI DSS v4.0.1: PCI-REQ-5, PCI-1.2.3; + 17 more sources |
| `ACM-TMR-006` — Reviewer Accountability And Consistency Gates | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-4.9, SP800-53-AC-6.7; CIS Controls v8.1.2: CIS-8.1, CIS-8.11; SAMM v2.1: SAMM-ACTIVITY-G_EG_2_A, SAMM-ACTIVITY-G_EG_3_A; HIPAA: HIPAA-164-308a8; + 1 more sources |
| `ACM-TMR-007` — Requirements Registry And Derivation Traceability | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-PL-2, SP800-53-PM-3; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_B, SAMM-ACTIVITY-D_SA_2_A; PCI DSS v4.0.1: PCI-REQ-8, PCI-1.2.4; SSDF v1.1: SSDF-PRACTICE-PO.1, SSDF-PRACTICE-PO.3; + 10 more sources |
| `ACM-TMR-008` — Compliance Monitoring And Regulatory Change Feeds | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AU-1, SP800-53-AU-2; SAMM v2.1: SAMM-ACTIVITY-G_PC_1_A, SAMM-ACTIVITY-G_PC_1_B; CIS Controls v8.1.2: CIS-4.4, CIS-7.5; DSOMM: DSOMM-ACTIVITY-67E1A9AA9FBF4EC5A2DE400F01960C51, DSOMM-ACTIVITY-8AE0B92C10E04602BA227524D6AED488; + 9 more sources |
| `ACO-TMR-001` — Threat Modeling Scope And Trigger Discipline | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SAMM v2.1: SAMM-ACTIVITY-D_TA_1_B, SAMM-ACTIVITY-D_TA_2_B; DSOMM: DSOMM-ACTIVITY-47419324E263415B815DE7161B6B905E, DSOMM-ACTIVITY-48F97F31931C46EB9B3EE2FEC0CD0426; SP 800-53 r5: SP800-53-PM-9; SAFECode Agile: SCAGILE-EXP-3 |
| `ACO-TMR-002` — Architecture-Grounded Threat Representation | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-PL-8.1, SP800-53-PM-7; SAMM v2.1: SAMM-ACTIVITY-V_AA_1_A, SAMM-ACTIVITY-V_AA_1_B; MITRE ATLAS: AML.M0017 |
| `ACO-TMR-003` — Structured Threat Analysis Method Discipline | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-IR-4.13, SP800-53-PM-28; SSDF v1.1: SSDF-PRACTICE-RV.3, SSDF-TASK-RV.2.1; PCI DSS v4.0.1: PCI-6.2.4, PCI-11.4.1; CAPEC v3.9: CAPEC-425; + 5 more sources |
| `ACO-TMR-004` — Threat Disposition, Risk Acceptance And Ownership | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | CWE SDV v4.19.1: CWE-1230, CWE-212; SP 800-53 r5: SP800-53-AT-2.2, SP800-53-IR-4.6; CAPEC v3.9: CAPEC-414, CAPEC-418; MITRE ATLAS: AML.T0048, AML.T0051.001; + 1 more sources |
| `ACO-TMR-005` — Threat-To-Mitigation And Validation Traceability | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-2.13, SP800-53-AC-25; CAPEC v3.9: CAPEC-51, CAPEC-81; MITRE ATLAS: AML.TA0002, AML.TA0007; PCI DSS v4.0.1: PCI-1.4.3, PCI-5.2.1; + 22 more sources |
| `ACO-TMR-006` — Independent Review And Threat Model Lifecycle Governance | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AU-2.3, SP800-53-AU-10.3; NIST AI RMF 1.0: NIST-AI-RMF-GOVERN-1.5; SAMM v2.1: SAMM-ACTIVITY-G_PC_3_B |
| `ACO-TMR-007` — Threat Modeling And Risk Governance Integrity | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SAMM v2.1: SAMM-ACTIVITY-D_TA_2_A, SAMM-ACTIVITY-G_EG_2_A; EU NIS2: NIS2-ART-20 |
| `ACO-TMR-008` — Security Requirements Lifecycle Management | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-3.3; PCI DSS v4.0.1: PCI-REQ-1, PCI-REQ-2; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_A, SAMM-ACTIVITY-D_SA_1_B; CIS Controls v8.1.2: CIS-2.2, CIS-4; + 13 more sources |
| `ACP-TMR-001` — Threat Model Creation And Triggered Refresh | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | MITRE ATLAS: AML.TA0006, AML.T0018; SP 800-53 r5: SP800-53-CP-2, SP800-53-SA-3.3; SAMM v2.1: SAMM-ACTIVITY-D_TA_1_B, SAMM-ACTIVITY-D_TA_2_B; NIST AI 100-2 e2025: NIST-AI-100-2-E2025-2.3.4, NIST-AI-100-2-E2025-3.2.2; + 5 more sources |
| `ACP-TMR-002` — DFD And Trust-Boundary Grounding | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-SA-8.10, SP800-53-SA-9.3; CIS Controls v8.1.2: CIS-4.9; CWE SDV v4.19.1: CWE-807; PCI SSLC v1.1: PCISSLC-3.2 |
| `ACP-TMR-003` — Structured Threat Analysis Method Selection | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AT-2.6, SP800-53-CP-6.1; SSDF v1.1: SSDF-PRACTICE-RV.2, SSDF-TASK-PW.1.1; SAMM v2.1: SAMM-ACTIVITY-D_TA_2_A, SAMM-ACTIVITY-I_DM_2_A; CAPEC v3.9: CAPEC-420, CAPEC-427; + 7 more sources |
| `ACP-TMR-004` — Threat Disposition And Accepted Risk Governance | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SAMM v2.1: SAMM-ACTIVITY-G_SM_1_A |
| `ACP-TMR-005` — Threat Traceability Into Requirements And Validation | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-4.19, SP800-53-AC-17.6; CAPEC v3.9: CAPEC-37, CAPEC-51; MITRE ATLAS: AML.TA0011, AML.T0002; ASVS v5: ASVS-REQ-V1.3.6, ASVS-REQ-V1.5.2; + 22 more sources |
| `ACP-TMR-006` — Independent Review And Threat Model Approval | P | Practice | chapter prose (go-live, model, models kws verified) | normative | explicit | Semantic | SP 800-53 r5: SP800-53-AC-13, SP800-53-AU-2.3; CIS Controls v8.1.2: CIS-17.8; SAMM v2.1: SAMM-ACTIVITY-G_EG_3_A |
| `ACP-TMR-007` — Threat Model Artifact Governance | P | Practice | chapter prose (access, artefacts, lifecycle kws verified) | normative | explicit | Semantic | NIST AI RMF 1.0: NIST-AI-RMF-GOVERN-2; SAMM v2.1: SAMM-ACTIVITY-G_SM_1_A |
| `ACP-TMR-008` — Security Requirements Identification And Derivation | P | Practice | chapter prose (models, policies, requirements kws verified) | normative | explicit | Semantic | SP 800-53 r5: SP800-53-AC-2, SP800-53-AC-3.5; PCI DSS v4.0.1: PCI-REQ-2, PCI-REQ-6; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_A, SAMM-ACTIVITY-D_SA_2_A; PCI SSLC v1.1: PCISSLC-1.2, PCISSLC-1.3; + 11 more sources |
| `ACP-TMR-009` — Requirements Communication And Compliance Monitoring | P | Practice | chapter prose (compliance, development, requirements kws verified) | normative | explicit | Semantic | SP 800-53 r5: SP800-53-AU-1, SP800-53-AU-6.1; SAMM v2.1: SAMM-ACTIVITY-G_EG_2_B, SAMM-ACTIVITY-G_PC_1_A; PCI DSS v4.0.1: PCI-1.1.2, PCI-2.1.2; PCI SSLC v1.1: PCISSLC-2.1, PCISSLC-5.1; + 3 more sources |

---

## § Manual-only coverage (out-of-Core-scope; ES-grounded direct) {#-manual-only-coverage-out-of-core-scope-es-grounded-direct}

Manual sections covering topics outside the scope of the V1 AppSec Core ontology (maturity models, organisational policies, KPIs/metrics, glossaries) but with direct ES grounding.

| Manual section | Manual V2 anchor | Authority | ES grounding (direct) |
|---|---|---|---|
| `achievable-maturity.md` | MaturityMapping | external | SAMM v2.1 maturity dimensions; DSOMM activities |
| `policies-relevantes.md` | PolicyReference | editorial / external | Threat Modelling Policy (organisational) |
| `addon/11-kpis-metricas.md` | ExternalFramework | external | Operational KPIs and metrics |

---

## § Out-of-AppSec coverage (pure editorial) {#-out-of-appsec-coverage-pure-editorial}

Manual sections that are pure editorial content (worked examples, narratives, illustrative cases, vendor-specific tooling integration). No ES grounding.

| Manual section | Content type | Manual V2 anchor (if any) |
|---|---|---|
| `exemplo-privacidade.md` | Worked example: LINDDUN privacy threat modelling | DocumentUnit |
| `exemplos-aplicacao-stride.md` | Worked examples: STRIDE per architecture pattern | DocumentUnit |
| `addon/02-riscos-processo-threat-modeling.md` | Process-level reflections / lessons learned | DocumentUnit |
| `addon/10-integracao-iriusrisk.md` | Tooling integration example (IriusRisk) | — |

---

## § Future-work register (P8 §10 candidates) {#-future-work-register-p8-10-candidates}

_(No entries in the future-work register for this chapter.)_
