---
id: rastreabilidade
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/canon/25-rastreabilidade.md
  source_sha256: a1bbfeba7cb518f737c16e919a1a03e4637e2684bb422fad7c4ff4e3b42cbc00
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: ae4ba63b058e7916bad155c895b7f6a6e25aa20a2d88fe18278de5b127c0f416
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [appsec_core, chapter_role, cycle_iteration, lifecycle_phase, mapping, practitioner_manual, risk_level, sbdtoe_sbd, slice, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: 10be9a140a9763b8c028528defa137e6e6770d4fa00899fd48112b3b76b51b4e
  translated_at: 2026-09-25T20:18:53Z
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

Total: **59 entities** of Manual ontology V2 mapped to this chapter via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

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
| Threat | `None` | hybrid | normative | heuristic | bounded |
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
