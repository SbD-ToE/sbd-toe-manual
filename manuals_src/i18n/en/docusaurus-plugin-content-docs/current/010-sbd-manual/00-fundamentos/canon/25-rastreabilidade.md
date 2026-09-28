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
  source_path: 010-sbd-manual/00-fundamentos/canon/25-rastreabilidade.md
  source_sha256: 961292625dd8f1e6975276e9bd676e2d8413b61cc5aede535dd2c9599f322ed4
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: c6374ce5252764286053c36fee3498a464a478675b8145f24ffd19a9cbfab0c6
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [appsec_core, chapter_role, practitioner_manual, slice, slug_threat_modeling, traceability, validation_evaluation]
  glossary_sha256: 00e6987efd50b173c0cd9abfc0f10b061c65bca8a577e8c1c7a55c3c75ef08bd
  translated_at: 2026-09-28T09:11:52Z
  stamped_at: 2026-09-28T09:11:52Z
  reviewed_by: null
---

# 25. Traceability — Foundations

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

_(No Manual ontology V2 entity is directly mapped to this chapter in the current canonical files.)_
