---
id: achievable-maturity
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/achievable-maturity.md
  source_sha256: 8e3bc85a88335aca62e4f8eb7a434cdce6dc74789fdc68b7df928d540b5ff63a
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 6090c8ff274848a127c7475732f432a44f5066edad0e438c7071022f1087f6be
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: d743dfcba33f930c34618b93d1eaaa34f697328d45aaf3bb657c33b8b3c59c9a
  glossary_keys: [chapter_role, framework_source_corpus, maturity, practitioner_manual, risk_level, sbdtoe_sbd, shacl_owl, traceability, trilho_formativo]
  glossary_sha256: 421c529234b0aad0a7729d8ff59baaf53911d413130fe6ea7311cd7667fcb57a
  translated_at: 2026-09-26T11:44:14Z
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

Total: **6 MaturityMapping entities** mapped to this chapter (via `sbd-toe-knowledge-graph/data/entities/maturity_mappings.json`).

| Entity type | ID | Framework | Framework area | Authority class | Source mode |
|---|---|---|---|---|---|
| MaturityMapping | `13-formacao-onboarding:maturity:owasp-dsomm:owasp-dsomm-education-training:education-training` | OWASP DSOMM | Education & Training | external | derived |
| MaturityMapping | `13-formacao-onboarding:maturity:owasp-dsomm:visao-geral-de-alinhamento:dsomm` | OWASP DSOMM | Adaptive training, continuous feedback, integration with matur | external | derived |
| MaturityMapping | `13-formacao-onboarding:maturity:owasp-samm:owasp-samm-governance-education-guidance:1` | OWASP SAMM | Governance → Education & Guidance | external | derived |
| MaturityMapping | `13-formacao-onboarding:maturity:owasp-samm:owasp-samm-governance-education-guidance:2` | OWASP SAMM | Governance → Education & Guidance | external | derived |
| MaturityMapping | `13-formacao-onboarding:maturity:owasp-samm:owasp-samm-governance-education-guidance:3` | OWASP SAMM | Governance → Education & Guidance | external | derived |
| MaturityMapping | `13-formacao-onboarding:maturity:owasp-samm:visao-geral-de-alinhamento:samm-v2-1` | OWASP SAMM | Training tracks by role and risk, traceability, cham | external | derived |

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

---

## Generation provenance {#generation-provenance}

- **Manual ontology V2 canonical:** `sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml` (`meta.version: '2.0'`)
- **KG canonical state:** sbd-toe-knowledge-graph master @ `5550a74`
- **Maturity mappings:** `data/entities/maturity_mappings.json` (168 items)
- **§26 methodology layer:** `00-fundamentos/canon/26-metodologia-validacao-claims.md` (Run 1 state @ a9e70c98)
- **§26 label rule:** deterministic per `confidence` field (≥0.85 Explicit; ≥0.65 Semantic; ≥0.4 Partial; &lt;0.4 Gap)
- **§26 §4 discipline applied:** SAMM/DSOMM primary; SLSA conditional; regulatory ≠ maturity
- **Generated by:** Manual Agent Run 2 (achievable-maturity enrichment)
- **Cycle:** Cycle B Run 2 — last content work pre frozen ceremony
