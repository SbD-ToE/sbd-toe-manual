---
# Proveniência da geração: não se mostra ao leitor (extraída do corpo na v1.17.1).
sbdtoe_provenance:
  ontology_v2: 'sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml (meta.version: ''2.0'')'
  kg_state: sbd-toe-knowledge-graph master @ 5550a743bb9de205676c503da5e81863ed62ab54 (2026-05-11; commit de governação imediatamente a seguir à tag kg-v1-cycle-b-iter-3-aligned-2026-05-11 @ 482ece916cc254126894019432ebd113695365d9)
  generated_by: Manual Agent Run 2 (achievable-maturity enrichment)
  cycle: Cycle B Run 2 — last content work pre frozen ceremony
  notes:
  - 'Maturity mappings: data/entities/maturity_mappings.json (168 items)'
  - '§26 methodology layer: 00-fundamentos/canon/26-metodologia-validacao-claims.md (Run 1 state @ a9e70c98937d41587e86712199fab46854a8d6aa)'
  - '§26 label rule: deterministic per confidence field (≥0.85 Explícito; ≥0.65 Semântico; ≥0.4 Parcial; <0.4 Gap)'
  - '§26 §4 discipline applied: SAMM/DSOMM primary; SLSA conditional; regulatory ≠ maturity'
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/achievable-maturity.md
  source_sha256: 74929d246057e68bc5d7b6d4720583361618aafa4e1562f3672a12a448de2f74
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: 6b6434fbce8f9f9a55db7ca5d3db74ee9cf61c982fe560072f3f0d6c675ee471
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [chapter_role, framework_source_corpus, maturity, practitioner_manual, risk_level, shacl_owl, traceability, trilho_formativo]
  glossary_sha256: 721634573d82af361bccfac6646dde50a2c8207c20aeadb536cd4a2348b2765e
  translated_at: 2026-09-28T09:12:21Z
  stamped_at: 2026-09-28T09:12:21Z
  reviewed_by: null
---

# Achievable Maturity — Training and Onboarding

## Summary {#sumário}

Credible maturity posture attainable if this chapter is implemented as written. The analysis follows the **§26 canon §4 discipline**: SAMM v2.1 + DSOMM are the primary sources; SLSA only where it makes sense as a build/integrity progression; **regulatory alignment is NOT a maturity score** and is recorded in § Out-of-Maturity scope.

Five sections:

- **§ Manual ontology V2 entities** — relevant MaturityMapping + Practice + Control entities
- **§ SAMM v2 / DSOMM maturity progression** — primary maturity sources per §26 §4
- **§ SLSA build/integrity progression** — where applicable to this chapter
- **§ Out-of-Maturity scope** — regulatory alignment (NOT a maturity score)
- **§ Future-work register** — maturity gaps registered for P8 §10

---

## § Manual ontology V2 — entities relevant to maturity {#-manual-ontology-v2--entities-relevantes-para-maturity}

Total: **6 MaturityMapping entities** mapped to this chapter.

| Entity type | ID | Framework | Framework area | Authority class | Source mode |
|---|---|---|---|---|---|
| MaturityMapping | `13-formacao-onboarding:maturity:owasp-dsomm:owasp-dsomm-education-training:education-training` | OWASP DSOMM | Education & Training | external | derived |
| MaturityMapping | `13-formacao-onboarding:maturity:owasp-dsomm:visao-geral-de-alinhamento:dsomm` | OWASP DSOMM | Adaptive training, continuous feedback, integration with maturity | external | derived |
| MaturityMapping | `13-formacao-onboarding:maturity:owasp-samm:owasp-samm-governance-education-guidance:1` | OWASP SAMM | Governance → Education & Guidance | external | derived |
| MaturityMapping | `13-formacao-onboarding:maturity:owasp-samm:owasp-samm-governance-education-guidance:2` | OWASP SAMM | Governance → Education & Guidance | external | derived |
| MaturityMapping | `13-formacao-onboarding:maturity:owasp-samm:owasp-samm-governance-education-guidance:3` | OWASP SAMM | Governance → Education & Guidance | external | derived |
| MaturityMapping | `13-formacao-onboarding:maturity:owasp-samm:visao-geral-de-alinhamento:samm-v2-1` | OWASP SAMM | Training tracks by role and risk, traceability, champions | external | derived |

---

## § SAMM v2 / DSOMM maturity progression {#-samm-v2--dsomm-maturity-progression}

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per the `confidence` field of the KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Education & Training | Adapted, practical training, continuous feedback, integration with tracking | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Adaptive training, continuous feedback, integration with maturity | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Governance → Education & Guidance | Awareness training for all profiles | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Governance → Education & Guidance | Tracks by role and risk level, KPIs | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Governance → Education & Guidance | Partial - not yet integrated with management cycles | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | — | Training tracks by role and risk, traceability, champions | `achievable-maturity.md` | 0.90 | Explicit |

---

## § SLSA build/integrity progression {#-slsa-buildintegrity-progression}

_(SLSA not applicable to this chapter — no direct build/integrity progression.)_

---

## § Out-of-Maturity scope (regulatory alignment is NOT maturity) {#-out-of-maturity-scope-regulatory-alignment-não-maturity}

Per the §26 §4 discipline: regulatory alignment (PCI DSS, GDPR, NIS2, DORA, CRA, HIPAA) **must NOT be treated as a maturity score**. Regulatory items are recorded here for editorial visibility; conformance lives in separate obligations, not in the maturity progression.

_(Regulatory alignment for this chapter is handled via Manual ontology V2 ExternalObligation entities + the governance chapters (Ch. 14); not enumerated here to avoid conflation with the maturity claim.)_

---

## § Future-work register (maturity gaps) {#-future-work-register-maturity-gaps}

_(No maturity claim in gap state for this chapter.)_
