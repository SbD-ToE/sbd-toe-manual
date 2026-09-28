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
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/canon/25-rastreabilidade.md
  source_sha256: 2cec555bbfb290ddf3f83b390172ea143896eb3db5efc1510cb6ff19bd1ee406
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: cc6de4da5b014de696e065aec37299757a434b1f3e5e36a564fc9fcf88f5367a
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [appsec_core, capacitacao, chapter_role, mcp_reading_programa, practitioner_manual, programme_line, slice, slug_threat_modeling, traceability, trilho_formativo, v1_entity_tmr_peer_review, validation_evaluation]
  glossary_sha256: 663d20babc06557dea04ce39234f59f49885fc553b729b9170a93c4203d0adb5
  translated_at: 2026-09-28T09:12:22Z
  stamped_at: 2026-09-28T09:12:22Z
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

Total: **97 entities** of Manual ontology V2 mapped to this chapter.

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
| Threat | `MT-212` | Insecure configuration due to lack of knowledge | normative | heuristic | bounded |
| Threat | `MT-213` | Improper reuse of secrets or tokens | normative | heuristic | bounded |
| Threat | `MT-214` | Technical access granted without validation | normative | heuristic | bounded |
| Threat | `MT-215` | Inclusion of third parties without validation | normative | heuristic | bounded |
| Threat | `MT-216` | Lack of ownership of security | normative | heuristic | bounded |
| Threat | `MT-217` | Behavioural regression / fragile culture | normative | heuristic | bounded |
| Threat | `MT-218` | Non-traceable training | normative | heuristic | bounded |
| Threat | `MT-219` | Uneven training across teams or roles | normative | heuristic | bounded |
| Threat | `MT-220` | Theoretical training without practical impact | normative | heuristic | bounded |
| Threat | `MT-221` | Outdated or non-applicable content | normative | heuristic | bounded |
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

> Authority class / source mode / confidence model: as defined by the Manual ontology (v2).
