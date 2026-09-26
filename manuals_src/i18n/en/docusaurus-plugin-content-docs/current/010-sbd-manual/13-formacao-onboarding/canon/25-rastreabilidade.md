---
id: rastreabilidade
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/canon/25-rastreabilidade.md
  source_sha256: 2498f19aafd46f99b94d846b12258e80778a15e14edca6698ad4b300a1e4704b
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: df3726e234da66813184dd4687d92035bf83a7906e18b2b6e80dcb0ac7b400ae
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: d743dfcba33f930c34618b93d1eaaa34f697328d45aaf3bb657c33b8b3c59c9a
  glossary_keys: [appsec_core, capacitacao, chapter_role, practitioner_manual, programme_line, sbdtoe_sbd, slice, traceability, trilho_formativo, v1_entity_tmr_peer_review, validation_evaluation]
  glossary_sha256: 48d89a5bc6cffd877a1eab1e9f9706a91f3e40eca990977103a29aafeacb5f35
  translated_at: 2026-09-26T11:44:29Z
  reviewed_by: null
---

# 25. Traceability — Training and Onboarding

## Summary {#sumário}

This chapter **is not the primary anchor** of any AppSec Core V1 slice. The external references relevant to this domain are found in the chapters where each slice is primarily anchored.

| Slice | Description | Anchored in |
|---|---|---|
| `ACO-ATB` | Secure architecture and trust boundaries | Ch. 04 (04-arquitetura-segura) |
| `ACO-IAT` | Identity, authentication and session management | Ch. 04 (04-arquitetura-segura) |
| `ACO-ITS` | Integration and service-to-service security | Ch. 04 (04-arquitetura-segura) |
| `ACO-IVF` | Input validation, secure parsing and controlled error handling | Ch. 06 (06-desenvolvimento-seguro) |
| `ACO-RPR` | Release promotion, controlled rollout and rollback readiness | Ch. 11 (11-deploy-seguro) |
| `ACO-SCBI` | Software supply chain and build integrity | Ch. 05 (05-dependencias-sbom-sca) |
| `ACO-SLG` | Security event logging and audit trail | Ch. 12 (12-monitorizacao-operacoes) |
| `ACO-SPC` | Secrets management, protected configuration and operational identities | Ch. 06 (06-desenvolvimento-seguro) |
| `ACO-TMR` | Threat modelling, risk management and mitigation traceability | Ch. 03 (03-threat-modeling) |
| `ACO-TSV` | Security testing and empirical validation | Ch. 10 (10-testes-seguranca) |

---

## § Manual ontology V2 — canonical entities of this chapter {#-manual-ontology-v2--entities-canónicas-deste-capítulo}

Total: **88 entities** of Manual ontology V2 mapped to this chapter via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `TRN-001` | Security training tracks defined by profile and criticality level | normative | explicit | deterministic |
| Requirement | `TRN-002` | Mandatory security onboarding before autonomous work | normative | explicit | deterministic |
| Requirement | `TRN-003` | Objective validation of onboarding with a defined acceptance criterion | normative | explicit | deterministic |
| Requirement | `TRN-004` | Access to critical environments conditional on validated onboarding | normative | explicit | deterministic |
| Requirement | `TRN-005` | Continuous security training for teams on L2 and L3 projects | normative | explicit | deterministic |
| Requirement | `TRN-006` | Training content versioned and updated after defined triggers | normative | explicit | deterministic |
| Requirement | `TRN-007` | Equivalent security onboarding for third parties and contractors | normative | explicit | deterministic |
| Requirement | `TRN-008` | Formal Security Champions programme in L3 teams | normative | explicit | deterministic |
| Requirement | `TRN-009` | Training KPIs defined, collected and acted upon | normative | explicit | deterministic |
| Control | `CTRL-governance-capacitacao-e-onboarding-de-seguranca-f84db7abdf` | Security upskilling and onboarding | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:code-clinics-estruturadas-e-recorrentes` | Structured and Recurring Code Clinics | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:exercicios-praticos-e-simulacoes` | Practical exercises and simulations | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:formacao-continua-por-perfil` | Continuous training per profile | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:formatos-de-entrega-e-dod-por-formato` | Delivery Formats and DoD per Format | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:kpis-de-capacitacao-e-reporte-grc` | Upskilling KPIs and Reporting (GRC) | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:manutencao-e-atualizacao-de-trilhos-formativos` | Maintenance and Updating of Training Tracks | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:medicao-de-eficacia-da-formacao` | Measurement of training effectiveness | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:onboarding-seguro-obrigatorio` | Mandatory secure onboarding | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:operacionalizacao-de-formacao-de-terceiros` | Operationalisation of Third-Party Training | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:programa-de-security-champions` | Security Champions Programme | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:threat-modeling-peer-led-e-rotativo` | Threat Modeling Peer-led and Rotating | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:trilhos-formativos-proporcionais-por-risco-l1l3` | Risk-Proportional Training Tracks (L1–L3) | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:validacao-de-conhecimento-via-quizzes-estruturados` | Knowledge Validation via Structured Quizzes | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:validacao-formal-de-onboarding-via-checklist` | Formal Onboarding Validation via Checklist | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:war-room-e-simulacoes-de-incidentes` | War Room and Incident Simulations | normative | explicit | deterministic |
| Threat | `None` | hybrid | normative | heuristic | bounded |
| Concept | `sem:concept:champion-seguranca` | security champions | semantic | scored | bounded |
| Concept | `sem:concept:champions` | Champions | semantic | scored | bounded |
| Concept | `sem:concept:checklist-de-validacao` | Validation Checklist | semantic | scored | bounded |
| Concept | `sem:concept:code-clinic` | Code Clinics | semantic | scored | bounded |
| Concept | `sem:concept:contextualizadas` | Contextualised | semantic | scored | bounded |
| Concept | `sem:concept:envolventes` | Engaging | semantic | scored | bounded |
| Concept | `sem:concept:exercicios-praticos` | practical exercises | semantic | scored | bounded |
| Concept | `sem:concept:facilitadas` | Facilitated | semantic | scored | bounded |
| Concept | `sem:concept:formacao-continua` | continuous training | semantic | scored | bounded |
| Concept | `sem:concept:formacao-e-capacitacao` | Training and Upskilling | semantic | scored | bounded |
| Concept | `sem:concept:formacao-em-seguranca` | security training | semantic | scored | bounded |
| Concept | `sem:concept:iterativas` | Iterative | semantic | scored | bounded |
| Concept | `sem:concept:kpis-de-eficacia-formativa` | Training effectiveness KPIs | semantic | scored | bounded |
| Concept | `sem:concept:kpis-de-formacao` | Training KPIs | semantic | scored | bounded |
| Concept | `sem:concept:onboarding` | Onboarding | semantic | scored | bounded |
| Concept | `sem:concept:papeis-envolvidos` | roles involved | semantic | scored | bounded |
| Concept | `sem:concept:programas-de-onboarding` | onboarding programmes | semantic | scored | bounded |
| Concept | `sem:concept:quiz-estruturados` | Structured Quizzes | semantic | scored | bounded |
| Concept | `sem:concept:sandbox` | Sandbox | semantic | scored | bounded |
| Concept | `sem:concept:simulacoes-de-incidentes` | Incident Simulations | semantic | scored | bounded |
| Concept | `sem:concept:sla-de-conclusao` | Completion SLA | semantic | scored | bounded |
| Concept | `sem:concept:tecnicas-formativas-avancadas` | Advanced Training Techniques | semantic | scored | bounded |
| Concept | `sem:concept:threat-modeling` | Threat Modelling | semantic | scored | bounded |
| Concept | `sem:concept:trilho-formacao` | Training Track | semantic | scored | bounded |
| Concept | `sem:concept:trilhos-proporcionais-por-risco` | Risk-Proportional Tracks | semantic | scored | bounded |
| Mechanism | `sem:mechanism:apoio-de-champions` | Champions Support | semantic | scored | bounded |
| Mechanism | `sem:mechanism:checklist-formal` | Formal Checklist | semantic | scored | bounded |
| Mechanism | `sem:mechanism:clinics` | Clinics | semantic | scored | bounded |
| Mechanism | `sem:mechanism:code-clinic-estruturadas` | Structured Code Clinics | semantic | scored | bounded |
| Mechanism | `sem:mechanism:exercicios-praticos` | Practical Exercises | semantic | scored | bounded |
| Mechanism | `sem:mechanism:formacao-continua` | continuous training | semantic | scored | bounded |
| Mechanism | `sem:mechanism:integracao-em-backlog-e-planos-individuais-de-desenvolvimento` | integration into backlog and individual development plans | semantic | scored | bounded |
| Mechanism | `sem:mechanism:kpis-de-eficacia-formativa` | Training effectiveness KPIs | semantic | scored | bounded |
| Mechanism | `sem:mechanism:labs` | Labs | semantic | scored | bounded |
| Mechanism | `sem:mechanism:lms` | LMS | semantic | scored | bounded |
| Mechanism | `sem:mechanism:medicao-de-kpis` | KPI Measurement | semantic | scored | bounded |
| Mechanism | `sem:mechanism:onboarding` | Onboarding | semantic | scored | bounded |
| Mechanism | `sem:mechanism:programas-de-champion-seguranca` | security champions programmes | semantic | scored | bounded |
| Mechanism | `sem:mechanism:programas-de-onboarding` | onboarding programmes | semantic | scored | bounded |
| Mechanism | `sem:mechanism:quiz` | Quizzes | semantic | scored | bounded |
| Mechanism | `sem:mechanism:sessoes-peer-led` | Peer-led sessions | semantic | scored | bounded |
| Mechanism | `sem:mechanism:simulacoes` | Simulations | semantic | scored | bounded |
| Mechanism | `sem:mechanism:simulacoes-de-incidentes` | Incident Simulations | semantic | scored | bounded |
| Pattern | `sem:pattern:champion-seguranca` | Security Champions | semantic | scored | bounded |
| Pattern | `sem:pattern:formacao-continua` | Continuous Training | semantic | scored | bounded |
| Pattern | `sem:pattern:pessoas-como-vetor-de-resiliencia` | people as a vector of resilience | semantic | scored | bounded |
| Pattern | `sem:pattern:trilho-formacao-proporcionais` | Proportional Training Tracks | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:dependencia-exclusiva-de-ferramentas-automatizadas` | exclusive reliance on automated tools | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:falta-de-onboarding` | Lack of Onboarding | semantic | scored | bounded |
| Signal | `sem:signal:checklist-completo` | Completed Checklist | semantic | scored | bounded |
| Signal | `sem:signal:kpis-de-eficacia-formativa` | Training effectiveness KPIs | semantic | scored | bounded |
| Signal | `sem:signal:kpis-de-formacao` | Training KPIs | semantic | scored | bounded |
| Signal | `sem:signal:resultados-de-quiz` | Quiz Results | semantic | scored | bounded |

> Authority class / source mode / confidence model: per Manual ontology V2 definition (`sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml`, `meta.version: '2.0'`).

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
