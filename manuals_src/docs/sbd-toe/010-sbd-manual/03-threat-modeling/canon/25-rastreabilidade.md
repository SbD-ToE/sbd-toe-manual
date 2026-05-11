# 25. Rastreabilidade — Threat Modeling

## Sumário

Este capítulo é a **âncora primária** das slices AppSec Core V1: `ACO-TMR` (Threat modeling, gestão de risco e rastreabilidade de mitigações).

Cobertura V1 entity-level: **25 entidades** primárias. Estrutura abaixo expõe **five-section routing** (per Run 1 amendment 2026-05-11; P8 pipeline primitive demonstration):

- **§ Manual ontology V2 entities** — entidades canónicas Manual ontology V2 mapped a este capítulo (KG canonical data)
- **§ Core-mapped coverage** — V1 entity → Manual ontology V2 anchor → Manual section anchor → §26 methodology label → ES grounding
- **§ Manual-only coverage** — Manual sections out-of-Core-scope mas ES-grounded direct
- **§ Out-of-AppSec coverage** — Pure editorial sections (examples, narratives) sem ES grounding
- **§ Future-work register** — Content gaps registered as P8 §10 candidates

---

## § Manual ontology V2 — entities canónicas deste capítulo

Total: **61 entidades** Manual ontology V2 mapped a este capítulo via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `THR-001` | Threat modeling formal em aplicações L2+ e alterações arquitecturais significati | normative | explicit | deterministic |
| Requirement | `THR-002` | Arquitectura actual representada com DFDs e trust boundaries explícitos | normative | explicit | deterministic |
| Requirement | `THR-003` | Metodologia estruturada aplicada com cobertura mínima garantida | normative | explicit | deterministic |
| Requirement | `THR-004` | Disposição formal de cada ameaça identificada com owner | normative | explicit | deterministic |
| Requirement | `THR-005` | Rastreabilidade ameaça → requisito → backlog → validação | normative | explicit | deterministic |
| Requirement | `THR-006` | Threat model versionado e actualizado dentro do ciclo ou após trigger | normative | explicit | deterministic |
| Requirement | `THR-007` | Revisão independente por AppSec antes de go-live em L2 e L3 | normative | explicit | deterministic |
| Control | `CTRL-governance-threat-modeling-e-gestao-de-risco-272c9a8ed0` | Threat modeling e gestão de risco | normative | explicit | deterministic |
| Practice | `03-threat-modeling:aplicacao-linddun-quando-existir-tratamento-de-dados-pessoais-novo` | Aplicação LINDDUN quando existir tratamento de dados pessoais  *(novo)* | normative | explicit | deterministic |
| Practice | `03-threat-modeling:aprovacao-formal-do-threat-model-baseline-e-revisoes` | Aprovação formal do Threat Model (baseline e revisões) | normative | explicit | deterministic |
| Practice | `03-threat-modeling:atualizacao-do-modelo-apos-alteracao-tecnica` | Atualização do modelo após alteração técnica | normative | explicit | deterministic |
| Practice | `03-threat-modeling:controlo-de-acesso-classificacao-e-retencao-dos-artefactos-de-threat-modeling` | Controlo de acesso, classificação e retenção dos artefactos de Threat Modeling | normative | explicit | deterministic |
| Practice | `03-threat-modeling:criacao-do-modelo-de-ameaca` | Criação do modelo de ameaça | normative | explicit | deterministic |
| Practice | `03-threat-modeling:gate-de-controlo-de-consistencia-no-ci-cd` | Gate de controlo de consistência no CI/CD | normative | explicit | deterministic |
| Practice | `03-threat-modeling:justificacao-formal-de-risco-aceite` | Justificação formal de risco aceite | normative | explicit | deterministic |
| Practice | `03-threat-modeling:reutilizacao-controlada-e-revisao-de-modelos-anteriores` | Reutilização controlada e revisão de modelos anteriores | normative | explicit | deterministic |
| Practice | `03-threat-modeling:validacao-de-arquitetura-com-threat-modeling` | Validação de arquitetura com threat modeling | normative | explicit | deterministic |
| Practice | `03-threat-modeling:validacao-de-impacto-no-negocio` | Validação de impacto no negócio | normative | explicit | deterministic |
| Threat | `None` | hybrid | normative | heuristic | bounded |
| Concept | `sem:concept:backlog-items` | Backlog Items | semantic | scored | bounded |
| Concept | `sem:concept:catalogo-de-requisitos` | Catálogo de Requisitos | semantic | scored | bounded |
| Concept | `sem:concept:context-diagrams` | Context Diagrams | semantic | scored | bounded |
| Concept | `sem:concept:dfds` | DFDs | semantic | scored | bounded |
| Concept | `sem:concept:evidencia-minima-obrigatoria` | Evidência mínima obrigatória | semantic | scored | bounded |
| Concept | `sem:concept:linddun` | LINDDUN | semantic | scored | bounded |
| Concept | `sem:concept:modelo-de-arquitetura` | Modelo de arquitetura | semantic | scored | bounded |
| Concept | `sem:concept:modelos-reutilizaveis` | Modelos reutilizáveis | semantic | scored | bounded |
| Concept | `sem:concept:niveis-de-criticidade` | Níveis de criticidade | semantic | scored | bounded |
| Concept | `sem:concept:omissao-estrutural-de-ameacas` | Omissão estrutural de ameaças | semantic | scored | bounded |
| Concept | `sem:concept:pasta` | PASTA | semantic | scored | bounded |
| Concept | `sem:concept:processo-decisional-estruturado` | Processo decisional estruturado | semantic | scored | bounded |
| Concept | `sem:concept:stride` | STRIDE | semantic | scored | bounded |
| Concept | `sem:concept:threat-modeling` | Threat Modeling | semantic | scored | bounded |
| Mechanism | `sem:mechanism:data-e-versao-do-modelo` | Data e versão do modelo | semantic | scored | bounded |
| Mechanism | `sem:mechanism:dfds` | DFDs | semantic | scored | bounded |
| Mechanism | `sem:mechanism:diagramas-versionados` | Diagramas versionados | semantic | scored | bounded |
| Mechanism | `sem:mechanism:identificacao-do-responsavel-pela-validacao` | Identificação do responsável pela validação | semantic | scored | bounded |
| Mechanism | `sem:mechanism:ligacao-a-requisitos-de-seguranca-ou-mitigacoes` | Ligação a requisitos de segurança ou mitigações | semantic | scored | bounded |
| Mechanism | `sem:mechanism:linddun` | LINDDUN | semantic | scored | bounded |
| Mechanism | `sem:mechanism:lista-de-ameacas-com-decisao-explicita` | Lista de ameaças com decisão explícita | semantic | scored | bounded |
| Mechanism | `sem:mechanism:pasta` | PASTA | semantic | scored | bounded |
| Mechanism | `sem:mechanism:specialized-tools` | Specialized Tools | semantic | scored | bounded |
| Mechanism | `sem:mechanism:stride` | STRIDE | semantic | scored | bounded |
| Mechanism | `sem:mechanism:trust-boundaries` | trust boundaries | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:ausencia-de-ameaca-no-modelo` | Ausência de ameaça no modelo | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:omissao-estrutural-de-ameacas` | Omissão estrutural de ameaças | semantic | scored | bounded |

> Authority class / source mode / confidence model: per Manual ontology V2 definition (`sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml`, `meta.version: '2.0'`).

---

## § Core-mapped coverage

Tabela expondo cobertura V1 entity-level com Manual ontology V2 anchor + Manual section anchor + §26 methodology label + substrate v7 ES grounding.

### Slice `ACO-TMR` — Threat modeling, gestão de risco e rastreabilidade de mitigações

| V1 entity | Type | Manual V2 anchor | Manual section anchor | Authority | Source mode | §26 label | ES grounding |
|---|---|---|---|---|---|---|---|
| `ACM-TMR-001` — Threat Representation Models | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explícito | SP 800-53 r5: SP800-53-SA-8.10, SP800-53-SA-8.16; CWE SDV v4.19.1: CWE-807; PCI SSLC v1.1: PCISSLC-3.2 |
| `ACM-TMR-002` — Structured Threat Analysis Frameworks | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explícito | SP 800-53 r5: SP800-53-CP-12, SP800-53-IR-10; EU DORA: DORA-ART-6, DORA-ART-13; SAMM v2.1: SAMM-ACTIVITY-D_TA_1_A, SAMM-ACTIVITY-D_TA_2_A; SSDF v1.1: SSDF-TASK-PW.1.1, SSDF-TASK-RV.2.1; + 9 more sources |
| `ACM-TMR-003` — Threat Model Versioning Controls | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explícito | MITRE ATLAS: AML.TA0006, AML.T0010.003; SP 800-53 r5: SP800-53-CM-2.3, SP800-53-CP-2; CAPEC v3.9: CAPEC-166, CAPEC-186; SAMM v2.1: SAMM-ACTIVITY-D_SA_3_A, SAMM-ACTIVITY-D_TA_2_B; + 10 more sources |
| `ACM-TMR-004` — Explicit Threat Disposition Register | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explícito | HIPAA: HIPAA-164-308a6; SP 800-53 r5: SP800-53-AT-2.2; SAMM v2.1: SAMM-ACTIVITY-G_SM_1_A |
| `ACM-TMR-005` — Threat Mitigation Linkage Controls | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explícito | SP 800-53 r5: SP800-53-AC-3.5, SP800-53-AC-3.6; CAPEC v3.9: CAPEC-37, CAPEC-38; MITRE ATLAS: AML.T0003, AML.T0008; PCI DSS v4.0.1: PCI-REQ-5, PCI-1.2.3; + 17 more sources |
| `ACM-TMR-006` — Reviewer Accountability And Consistency Gates | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explícito | SP 800-53 r5: SP800-53-AC-4.9, SP800-53-AC-6.7; CIS Controls v8.1.2: CIS-8.1, CIS-8.11; SAMM v2.1: SAMM-ACTIVITY-G_EG_2_A, SAMM-ACTIVITY-G_EG_3_A; HIPAA: HIPAA-164-308a8; + 1 more sources |
| `ACM-TMR-007` — Requirements Registry And Derivation Traceability | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explícito | SP 800-53 r5: SP800-53-PL-2, SP800-53-PM-3; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_B, SAMM-ACTIVITY-D_SA_2_A; PCI DSS v4.0.1: PCI-REQ-8, PCI-1.2.4; SSDF v1.1: SSDF-PRACTICE-PO.1, SSDF-PRACTICE-PO.3; + 10 more sources |
| `ACM-TMR-008` — Compliance Monitoring And Regulatory Change Feeds | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explícito | SP 800-53 r5: SP800-53-AU-1, SP800-53-AU-2; SAMM v2.1: SAMM-ACTIVITY-G_PC_1_A, SAMM-ACTIVITY-G_PC_1_B; CIS Controls v8.1.2: CIS-4.4, CIS-7.5; DSOMM: DSOMM-ACTIVITY-67E1A9AA9FBF4EC5A2DE400F01960C51, DSOMM-ACTIVITY-8AE0B92C10E04602BA227524D6AED488; + 9 more sources |
| `ACO-TMR-001` — Threat Modeling Scope And Trigger Discipline | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explícito | SAMM v2.1: SAMM-ACTIVITY-D_TA_1_B, SAMM-ACTIVITY-D_TA_2_B; DSOMM: DSOMM-ACTIVITY-47419324E263415B815DE7161B6B905E, DSOMM-ACTIVITY-48F97F31931C46EB9B3EE2FEC0CD0426; SP 800-53 r5: SP800-53-PM-9; SAFECode Agile: SCAGILE-EXP-3 |
| `ACO-TMR-002` — Architecture-Grounded Threat Representation | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explícito | SP 800-53 r5: SP800-53-PL-8.1, SP800-53-PM-7; SAMM v2.1: SAMM-ACTIVITY-V_AA_1_A, SAMM-ACTIVITY-V_AA_1_B; MITRE ATLAS: AML.M0017 |
| `ACO-TMR-003` — Structured Threat Analysis Method Discipline | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explícito | SP 800-53 r5: SP800-53-IR-4.13, SP800-53-PM-28; SSDF v1.1: SSDF-PRACTICE-RV.3, SSDF-TASK-RV.2.1; PCI DSS v4.0.1: PCI-6.2.4, PCI-11.4.1; CAPEC v3.9: CAPEC-425; + 5 more sources |
| `ACO-TMR-004` — Threat Disposition, Risk Acceptance And Ownership | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explícito | CWE SDV v4.19.1: CWE-1230, CWE-212; SP 800-53 r5: SP800-53-AT-2.2, SP800-53-IR-4.6; CAPEC v3.9: CAPEC-414, CAPEC-418; MITRE ATLAS: AML.T0048, AML.T0051.001; + 1 more sources |
| `ACO-TMR-005` — Threat-To-Mitigation And Validation Traceability | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explícito | SP 800-53 r5: SP800-53-AC-2.13, SP800-53-AC-25; CAPEC v3.9: CAPEC-51, CAPEC-81; MITRE ATLAS: AML.TA0002, AML.TA0007; PCI DSS v4.0.1: PCI-1.4.3, PCI-5.2.1; + 22 more sources |
| `ACO-TMR-006` — Independent Review And Threat Model Lifecycle Governance | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explícito | SP 800-53 r5: SP800-53-AU-2.3, SP800-53-AU-10.3; NIST AI RMF 1.0: NIST-AI-RMF-GOVERN-1.5; SAMM v2.1: SAMM-ACTIVITY-G_PC_3_B |
| `ACO-TMR-007` — Threat Modeling And Risk Governance Integrity | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explícito | SAMM v2.1: SAMM-ACTIVITY-D_TA_2_A, SAMM-ACTIVITY-G_EG_2_A; EU NIS2: NIS2-ART-20 |
| `ACO-TMR-008` — Security Requirements Lifecycle Management | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explícito | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-3.3; PCI DSS v4.0.1: PCI-REQ-1, PCI-REQ-2; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_A, SAMM-ACTIVITY-D_SA_1_B; CIS Controls v8.1.2: CIS-2.2, CIS-4; + 13 more sources |
| `ACP-TMR-001` — Threat Model Creation And Triggered Refresh | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explícito | MITRE ATLAS: AML.TA0006, AML.T0018; SP 800-53 r5: SP800-53-CP-2, SP800-53-SA-3.3; SAMM v2.1: SAMM-ACTIVITY-D_TA_1_B, SAMM-ACTIVITY-D_TA_2_B; NIST AI 100-2 e2025: NIST-AI-100-2-E2025-2.3.4, NIST-AI-100-2-E2025-3.2.2; + 5 more sources |
| `ACP-TMR-002` — DFD And Trust-Boundary Grounding | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explícito | SP 800-53 r5: SP800-53-SA-8.10, SP800-53-SA-9.3; CIS Controls v8.1.2: CIS-4.9; CWE SDV v4.19.1: CWE-807; PCI SSLC v1.1: PCISSLC-3.2 |
| `ACP-TMR-003` — Structured Threat Analysis Method Selection | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explícito | SP 800-53 r5: SP800-53-AT-2.6, SP800-53-CP-6.1; SSDF v1.1: SSDF-PRACTICE-RV.2, SSDF-TASK-PW.1.1; SAMM v2.1: SAMM-ACTIVITY-D_TA_2_A, SAMM-ACTIVITY-I_DM_2_A; CAPEC v3.9: CAPEC-420, CAPEC-427; + 7 more sources |
| `ACP-TMR-004` — Threat Disposition And Accepted Risk Governance | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explícito | SAMM v2.1: SAMM-ACTIVITY-G_SM_1_A |
| `ACP-TMR-005` — Threat Traceability Into Requirements And Validation | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explícito | SP 800-53 r5: SP800-53-AC-4.19, SP800-53-AC-17.6; CAPEC v3.9: CAPEC-37, CAPEC-51; MITRE ATLAS: AML.TA0011, AML.T0002; ASVS v5: ASVS-REQ-V1.3.6, ASVS-REQ-V1.5.2; + 22 more sources |
| `ACP-TMR-006` — Independent Review And Threat Model Approval | P | Practice | chapter prose (go-live, model, models kws verified) | normative | explicit | Semântico | SP 800-53 r5: SP800-53-AC-13, SP800-53-AU-2.3; CIS Controls v8.1.2: CIS-17.8; SAMM v2.1: SAMM-ACTIVITY-G_EG_3_A |
| `ACP-TMR-007` — Threat Model Artifact Governance | P | Practice | chapter prose (access, artifacts, lifecycle kws verified) | normative | explicit | Semântico | NIST AI RMF 1.0: NIST-AI-RMF-GOVERN-2; SAMM v2.1: SAMM-ACTIVITY-G_SM_1_A |
| `ACP-TMR-008` — Security Requirements Identification And Derivation | P | Practice | chapter prose (models, policies, requirements kws verified) | normative | explicit | Semântico | SP 800-53 r5: SP800-53-AC-2, SP800-53-AC-3.5; PCI DSS v4.0.1: PCI-REQ-2, PCI-REQ-6; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_A, SAMM-ACTIVITY-D_SA_2_A; PCI SSLC v1.1: PCISSLC-1.2, PCISSLC-1.3; + 11 more sources |
| `ACP-TMR-009` — Requirements Communication And Compliance Monitoring | P | Practice | chapter prose (compliance, development, requirements kws verified) | normative | explicit | Semântico | SP 800-53 r5: SP800-53-AU-1, SP800-53-AU-6.1; SAMM v2.1: SAMM-ACTIVITY-G_EG_2_B, SAMM-ACTIVITY-G_PC_1_A; PCI DSS v4.0.1: PCI-1.1.2, PCI-2.1.2; PCI SSLC v1.1: PCISSLC-2.1, PCISSLC-5.1; + 3 more sources |

---

## § Manual-only coverage (out-of-Core-scope; ES-grounded direct)

Manual sections que cobrem tópicos fora do scope V1 AppSec Core ontology (maturity models, organizational policies, KPIs/metrics, glossaries) mas com ES grounding direct.

| Manual section | Manual V2 anchor | Authority | ES grounding (direct) |
|---|---|---|---|
| `achievable-maturity.md` | MaturityMapping | external | SAMM v2.1 maturity dimensions; DSOMM activities |
| `policies-relevantes.md` | PolicyReference | editorial / external | Política de Threat Modeling (organizational) |
| `addon/11-kpis-metricas.md` | ExternalFramework | external | KPIs e métricas operacionais |

---

## § Out-of-AppSec coverage (pure editorial)

Manual sections que são pure editorial content (worked examples, narrativas, illustrative cases, vendor-specific tooling integration). Sem ES grounding.

| Manual section | Content type | Manual V2 anchor (if any) |
|---|---|---|
| `exemplo-privacidade.md` | Worked example: LINDDUN privacy threat modeling | DocumentUnit |
| `exemplos-aplicacao-stride.md` | Worked examples: STRIDE per architecture pattern | DocumentUnit |
| `addon/02-riscos-processo-threat-modeling.md` | Process-level reflections / lessons learned | DocumentUnit |
| `addon/10-integracao-iriusrisk.md` | Tooling integration example (IriusRisk) | — |

---

## § Future-work register (P8 §10 candidates)

_(Sem entradas no future-work register para este capítulo.)_

---

## Generation provenance

- **Manual ontology V2 canonical:** `sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml` (`meta.version: '2.0'`)
- **KG canonical state:** sbd-toe-knowledge-graph master @ `5550a74` (`kg-v1-cycle-b-iter-3-aligned-2026-05-11`)
- **Substrate version:** v7 (SUPPLIER sha256 `596783ed984d9c0e8c8ef6439a0eaee8fbaf2d863af37138cde8fad55d62be04`)
- **V1 entity index:** `ontology-v1.1-fair-baseline` @ `84fe8bf` em sbd-toe-ontology
- **Per-entity source map:** `data/p8_inputs/per_entity_source_map.json` @ ESI commit `aa3c13c`
- **Phase 2/3 gap analysis:** `phase2_3_per_entity_classification.json` @ ESI commit `b8cd401`
- **Generated by:** Manual Agent Run 1 (Iter 4 baseline @ `16dfa5ae` + Manual ontology V2 vocab layer injection)
- **Format:** 5-section (Manual V2 entities + Core-mapped + Manual-only + Out-of-AppSec + Future-work) per dispatch vision 2026-05-11
- **§26 methodology labels:** per `00-fundamentos/canon/26-metodologia-validacao-claims.md` (post Run 1 Step 0 refresh)
- **Cycle:** Cycle B Run 1 (post Iter 4)
