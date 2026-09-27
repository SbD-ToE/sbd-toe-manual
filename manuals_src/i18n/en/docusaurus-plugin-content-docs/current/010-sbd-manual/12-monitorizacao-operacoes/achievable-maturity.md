---
id: achievable-maturity
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/achievable-maturity.md
  source_sha256: 8d7d9ca5067c41e4e56bfcc6a75b0aa3735eb5921d5443bd712ee9aedcefe06a
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 86a63327ff95705b39d9db48d242fcfc597526e766b727c266a79dc8dcc6719c
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: ebb6c6bf48bf281085379aa982dcfe014d642265f07b08070d51366e58764173
  glossary_keys: [chapter_role, framework_source_corpus, maturity, practitioner_manual, sbdtoe_sbd, shacl_owl, verification_taxonomy]
  glossary_sha256: 865b50f3419788161c3c7042c3ee19fc3607a68b383727b8e6194f64bd1eb4c9
  translated_at: 2026-09-26T11:17:24Z
  reviewed_by: null
---

# Achievable Maturity — Monitoring and Operations

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

Total: **11 MaturityMapping entities** mapped to this chapter (via `sbd-toe-knowledge-graph/data/entities/maturity_mappings.json`).

| Entity type | ID | Framework | Framework area | Authority class | Source mode |
|---|---|---|---|---|---|
| MaturityMapping | `12-monitorizacao-operacoes:maturity:owasp-dsomm:owasp-dsomm-operations:operations` | OWASP DSOMM | Operations | external | derived |
| MaturityMapping | `12-monitorizacao-operacoes:maturity:owasp-dsomm:visao-geral-de-alinhamento:dsomm` | OWASP DSOMM | Monitoring, detection, alerts, IR, correlation | external | derived |
| MaturityMapping | `12-monitorizacao-operacoes:maturity:owasp-samm:owasp-samm-operations-incident-management:1` | OWASP SAMM | Operations → Incident Management | external | derived |
| MaturityMapping | `12-monitorizacao-operacoes:maturity:owasp-samm:owasp-samm-operations-incident-management:2` | OWASP SAMM | Operations → Incident Management | external | derived |
| MaturityMapping | `12-monitorizacao-operacoes:maturity:owasp-samm:owasp-samm-operations-incident-management:3` | OWASP SAMM | Operations → Incident Management | external | derived |
| MaturityMapping | `12-monitorizacao-operacoes:maturity:owasp-samm:visao-geral-de-alinhamento:samm-v2-1` | OWASP SAMM | Logging, alerts, KPIs, integration with response | external | derived |
| MaturityMapping | `12-monitorizacao-operacoes:maturity:slsa:slsa-observabilidade:1` | SLSA | Observability | external | derived |
| MaturityMapping | `12-monitorizacao-operacoes:maturity:slsa:slsa-observabilidade:2` | SLSA | Observability | external | derived |
| MaturityMapping | `12-monitorizacao-operacoes:maturity:slsa:slsa-observabilidade:3` | SLSA | Observability | external | derived |
| MaturityMapping | `12-monitorizacao-operacoes:maturity:slsa:slsa-observabilidade:4` | SLSA | Observability | external | derived |
| MaturityMapping | `12-monitorizacao-operacoes:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Integrated logging and metrics | external | derived |

---

## § SAMM v2 / DSOMM maturity progression {#-samm-v2--dsomm-maturity-progression}

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per the `confidence` field of the KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Operations | Full coverage: logging, detection, correlation, IR integration | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Monitoring, detection, alerts, IR, correlation | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Operations → Incident Management | Basic and manual logging | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Operations → Incident Management | Continuous monitoring and alerts | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Operations → Incident Management | Integration with incident response | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | — | Logging, alerts, KPIs, integration with response | `achievable-maturity.md` | 0.90 | Explicit |

---

## § SLSA build/integrity progression {#-slsa-buildintegrity-progression}

SLSA progression mapping (per §26 §4: SLSA only where it makes sense as a build/integrity progression — this chapter qualifies).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Observability | — | Minimum logging in pipelines | `achievable-maturity.md` | Explicit |
| Observability | — | Operational KPIs and automated detection | `achievable-maturity.md` | Explicit |
| Observability | — | Partial - does not address cryptographic verification | `achievable-maturity.md` | Explicit |
| Observability | — | Not applicable in this context | `achievable-maturity.md` | Explicit |
| — | — | Integrated logging and metrics | `achievable-maturity.md` | Explicit |

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
