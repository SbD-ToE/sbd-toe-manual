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
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/canon/25-rastreabilidade.md
  source_sha256: 7a2615489dfda3a2b551cfea3857697d2d28e4c914fa7716fb9374fead1baab0
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: 8eaead52b5e21445be59ddc3835199818d2b1467dbf1862b7dc1d39c0e4295e8
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [appsec_core, chapter_role, cycle_iteration, lifecycle_phase, mapping, practitioner_manual, risk_level, slice, slug_threat_modeling, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 57b57134d152784e2dc4e2221a170e7ddce9a5e64a36fe287400aeeeae364fe4
  translated_at: 2026-09-28T09:11:54Z
  stamped_at: 2026-09-28T09:11:54Z
  reviewed_by: null
---

# 25. Traceability — Application Classification

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

Total: **78 entities** of Manual ontology V2 mapped to this chapter.

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `CLA-001` | Formal classification according to the risk axes model | normative | explicit | deterministic |
| Requirement | `CLA-002` | Approval proportional to the assigned risk level | normative | explicit | deterministic |
| Requirement | `CLA-003` | Activation of base controls determined by the classification | normative | explicit | deterministic |
| Requirement | `CLA-004` | Documented and monitored reclassification criteria | normative | explicit | deterministic |
| Requirement | `CLA-005` | Periodic classification review cycle differentiated by level | normative | explicit | deterministic |
| Requirement | `CLA-006` | Classification reassessment after a significant change event | normative | explicit | deterministic |
| Requirement | `CLA-007` | Residual risk with formalised compensation, owner and TTL | normative | explicit | deterministic |
| Requirement | `CLA-008` | Application inventory kept up to date and accessible for audit | normative | explicit | deterministic |
| Control | `CTRL-governance-classificacao-e-governacao-por-risco-97aceecf29` | Risk-based classification and governance | normative | explicit | deterministic |
| Practice | `01-classificacao-aplicacoes:analise-de-risco-residual` | Residual risk analysis | normative | explicit | deterministic |
| Practice | `01-classificacao-aplicacoes:aplicacao-da-matriz-de-controlo` | Application of the control matrix | normative | explicit | deterministic |
| Practice | `01-classificacao-aplicacoes:classificacao-inicial-da-aplicacao` | Initial classification of the application | normative | explicit | deterministic |
| Practice | `01-classificacao-aplicacoes:mapeamento-de-ameacas-por-nivel-de-risco` | Threat mapping by risk level | normative | explicit | deterministic |
| Practice | `01-classificacao-aplicacoes:revisao-por-alteracao-relevante-event-based` | Review upon relevant change (event-based) | normative | explicit | deterministic |
| Practice | `01-classificacao-aplicacoes:validacao-antes-do-go-live` | Validation before go-live | normative | explicit | deterministic |
| Threat | `MT-001` | Failure to apply minimum controls | normative | heuristic | bounded |
| Threat | `MT-002` | Over-engineering and excessive friction | normative | heuristic | bounded |
| Threat | `MT-003` | Inconsistency between projects with the same risk | normative | heuristic | bounded |
| Threat | `MT-004` | Optional security in low-risk products | normative | heuristic | bounded |
| Threat | `MT-005` | Critical changes without reclassification | normative | heuristic | bounded |
| Threat | `MT-006` | Integration with APIs or third parties ignored | normative | heuristic | bounded |
| Threat | `MT-007` | Deploy with altered risk not reviewed | normative | heuristic | bounded |
| Threat | `MT-008` | Different versions with divergent classifications | normative | heuristic | bounded |
| Threat | `MT-009` | Informal acceptance of critical risks | normative | heuristic | bounded |
| Threat | `MT-010` | Impossibility of subsequent audit | normative | heuristic | bounded |
| Threat | `MT-011` | Risk accepted by inappropriate parties | normative | heuristic | bounded |
| Threat | `MT-012` | Lack of regulatory explainability | normative | heuristic | bounded |
| Threat | `MT-013` | Poorly assessed exposed interfaces | normative | heuristic | bounded |
| Threat | `MT-014` | Unrecognised sensitive data | normative | heuristic | bounded |
| Threat | `MT-015` | Assumption of secure environments by default | normative | heuristic | bounded |
| Threat | `MT-016` | Ignoring critical dependencies | normative | heuristic | bounded |
| Threat | `MT-017` | Residual risk never reviewed | normative | heuristic | bounded |
| Threat | `MT-018` | Lack of planned reassessment events | normative | heuristic | bounded |
| Threat | `MT-019` | Reclassification dependent on exceptions | normative | heuristic | bounded |
| Threat | `MT-020` | Risk decisions without business feedback | normative | heuristic | bounded |
| Concept | `sem:concept:aceitacao-de-risco` | risk acceptance | semantic | scored | bounded |
| Concept | `sem:concept:atributos-do-risco` | risk attributes | semantic | scored | bounded |
| Concept | `sem:concept:ciclo-de-desenvolvimento` | development cycle | semantic | scored | bounded |
| Concept | `sem:concept:ciclo-de-vida-do-risco` | risk lifecycle | semantic | scored | bounded |
| Concept | `sem:concept:classificacao-de-criticidade` | criticality classification | semantic | scored | bounded |
| Concept | `sem:concept:ferramentas-de-automacao-e-apoio-a-decisao` | automation and decision-support tools | semantic | scored | bounded |
| Concept | `sem:concept:gates-explicitos-de-validacao-de-risco` | explicit risk validation gates | semantic | scored | bounded |
| Concept | `sem:concept:impacto-residual` | residual impact | semantic | scored | bounded |
| Concept | `sem:concept:modelo-de-classificacao-simples` | simple classification model | semantic | scored | bounded |
| Concept | `sem:concept:modelo-e-d-i` | E/D/I model | semantic | scored | bounded |
| Concept | `sem:concept:risco` | risk | semantic | scored | bounded |
| Mechanism | `sem:mechanism:dashboards-de-risco` | risk dashboards | semantic | scored | bounded |
| Mechanism | `sem:mechanism:evidencia-da-eficacia` | evidence of effectiveness | semantic | scored | bounded |
| Mechanism | `sem:mechanism:integracao-em-ferramentas-de-backlog` | integration into backlog tools | semantic | scored | bounded |
| Mechanism | `sem:mechanism:mecanismo` | mechanism | semantic | scored | bounded |
| Mechanism | `sem:mechanism:mecanismos-claros-rapidos-e-rastreaveis` | clear, fast and traceable mechanisms | semantic | scored | bounded |
| Mechanism | `sem:mechanism:modelo-de-classificacao-simples-direto-e-economicamente-viavel` | simple, direct and economically viable classification model | semantic | scored | bounded |
| Mechanism | `sem:mechanism:pipelines-ci-cd` | CI/CD Pipelines | semantic | scored | bounded |
| Mechanism | `sem:mechanism:registo-versionado-em-git` | versioned record in Git | semantic | scored | bounded |
| Mechanism | `sem:mechanism:verificacao-dos-controlos-aplicados` | verification of the controls applied | semantic | scored | bounded |
| Pattern | `sem:pattern:user-stories-reutilizaveis` | reusable user stories | semantic | scored | bounded |
| Pattern | `sem:pattern:uso-de-modelo-alternativo-de-classificacao` | use of an alternative classification model | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:aceitacao-de-risco-invalida` | invalid risk acceptance | semantic | scored | bounded |
| Signal | `sem:signal:alteracao-na-exposicao-dados-impacto-ou-forma-de-decisoes-e-validacoes` | change in exposure, data, impact or the way decisions and validations are made | semantic | scored | bounded |

> Authority class / source mode / confidence model: as defined by the Manual ontology (v2).
