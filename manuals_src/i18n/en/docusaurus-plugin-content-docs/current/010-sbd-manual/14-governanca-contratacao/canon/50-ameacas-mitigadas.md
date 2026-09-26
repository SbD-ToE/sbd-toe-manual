---
id: ameacas-mitigadas
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/canon/50-ameacas-mitigadas.md
  source_sha256: f10a935c8fec91cff3d178001725ccacb0a2e036c692c1a5ce77ee902b679620
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 0763e57df8911a6512fe11ba7d84a24dfe42d25a92b5fe11b5f84e308b34afb8
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [appsec_core, avaliacao, chapter_role, practitioner_manual, sbdtoe_sbd, threat, validation_evaluation]
  glossary_sha256: 11b8aee46be47b15de2b0cf58999afa5c34de8d8a2fc7086f4a31fe81552f5c3
  translated_at: 2026-09-26T12:00:23Z
  reviewed_by: null
---

# 50. Mitigated Threats — Governance and Contracting

## Summary {#sumário}

Threat families mitigated in this chapter + mitigation strength. The analysis follows the **§26 canon §4 discipline**: Manual surface + CAPEC primary; CWE supporting limited; mitigation strength explicitly labelled.

Six sections:

- **§ Manual ontology V2 entities** — canonical Threat + AntiPattern + Signal
- **§ Threat surfaces** — Manual + CAPEC primary surfaces
- **§ AntiPattern exposure mapping** — antipattern → threat exposure relations
- **§ CWE references** — supporting only (per §26 §4 discipline)
- **§ V1 overlay** — mitigation pathway where Core-mapped
- **§ Future-work register** — threat gaps registered for P8 §10

---

## § Manual ontology V2 — canonical entities (threats + antipatterns + signals) {#-manual-ontology-v2--entities-canónicas-threats--antipatterns--signals}

Total: **23 entities** (Threat × 12, AntiPattern × 2, Signal × 9) mapped to this chapter.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-222` | Supplier adoption without assessment | normative | heuristic |
| Threat | `MT-223` | Lack of contractual clauses | normative | heuristic |
| Threat | `MT-224` | Use of services without tracking | normative | heuristic |
| Threat | `MT-225` | Parallel initiatives without coordination | normative | heuristic |
| Threat | `MT-226` | Lack of organisational continuity | normative | heuristic |
| Threat | `MT-227` | Risk of legacy decisions without control | normative | heuristic |
| Threat | `MT-228` | Decisions not reviewed when the context changes | normative | heuristic |
| Threat | `MT-229` | Lack of governance over historical decisions | normative | heuristic |
| Threat | `MT-230` | Lack of knowledge of the security state | normative | heuristic |
| Threat | `MT-231` | Disjointed security strategy | normative | heuristic |
| Threat | `MT-232` | Security defined but not applied | normative | heuristic |
| Threat | `MT-233` | Security policies not institutionalised | normative | heuristic |
| AntiPattern | `sem:antipattern:confianca-exclusiva-em-mecanismos-tecnicos-automatizados` | exclusive reliance on automated technical mechanisms | semantic | scored |
| AntiPattern | `sem:antipattern:limitacao-do-sbd-toe-a-pratica-tecnica-local` | limitation of the SbD-ToE to local technical practice | semantic | scored |
| Signal | `sem:signal:clausulas-contratuais-rastreadas` | Tracked contractual clauses | semantic | scored |
| Signal | `sem:signal:excecoes-as-praticas-prescritas` | exceptions to the prescribed practices | semantic | scored |
| Signal | `sem:signal:excecoes-registadas-e-aprovadas` | Recorded and approved exceptions | semantic | scored |
| Signal | `sem:signal:kpis-consolidados` | Consolidated KPIs | semantic | scored |
| Signal | `sem:signal:kpis-de-governacao` | Governance KPIs | semantic | scored |
| Signal | `sem:signal:ligacao-explicita-a-frameworks-normativos` | Explicit linkage to regulatory frameworks | semantic | scored |
| Signal | `sem:signal:registo-e-aprovacao-de-excecoes` | recording and approval of exceptions | semantic | scored |
| Signal | `sem:signal:reporting-periodico-a-gestao` | periodic reporting to management | semantic | scored |
| Signal | `sem:signal:validacao-continua-de-fornecedores` | continuous supplier validation | semantic | scored |

---

## § Threat surfaces — Manual + CAPEC primary {#-threat-surfaces--manual--capec-primary}

Canonical threat surfaces per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (strong / partial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-222` | STRIDE | Supplier adoption without assessment | — | `addon/03-modelo-validacao-fornecedores.md` | partial | Explicit |
| `MT-223` | STRIDE | Lack of contractual clauses | — | `addon/02-clausulas-contratuais.md` | partial | Explicit |
| `MT-224` | STRIDE | Use of services without tracking | — | `addon/04-rastreabilidade-organizacional.md` | partial | Explicit |
| `MT-225` | STRIDE | Parallel initiatives without coordination | — | `addon/01-modelo-governancao.md` | partial | Explicit |
| `MT-226` | STRIDE | Lack of organisational continuity | — | `addon/07-governancao-e-maturidade.md` | partial | Explicit |
| `MT-227` | STRIDE | Risk of legacy decisions without control | — | `addon/10-governanca-legada.md` | partial | Explicit |
| `MT-228` | STRIDE | Decisions not reviewed when the context changes | — | `addon/06-validacao-continuada.md` | partial | Explicit |
| `MT-229` | STRIDE | Lack of governance over historical decisions | — | `addon/04`, `addon/06` | partial | Explicit |
| `MT-230` | STRIDE | Lack of knowledge of the security state | — | `addon/07-governancao-e-maturidade.md` | partial | Explicit |
| `MT-231` | STRIDE | Disjointed security strategy | — | `30`, `90` | partial | Explicit |
| `MT-232` | STRIDE | Security defined but not applied | — | `addon/01`, `addon/05`, `addon/06` + 1 more | strong | Explicit |
| `MT-233` | STRIDE | Security policies not institutionalised | — | `60-politicas-recomendadas.md` | partial | Explicit |

---

## § AntiPattern exposure mapping {#-antipattern-exposure-mapping}

_(No antipattern→threat relation mapped to this chapter.)_

---

## § CWE references (supporting only) {#-cwe-references-supporting-only}

_(No threat with a CWE reference for this chapter.)_

---

## § V1 overlay — mitigation pathway (where Core-mapped) {#-v1-overlay--mitigation-pathway-where-core-mapped}

V1 controls/mechanisms anchored to this chapter that mitigate the threats listed above. The V1 overlay keeps the three-way routing visible per Manual ontology V2 + AppSec Core V1 + Substrate v7.

_(V1 overlay surfacing per Manual ontology V2 antipattern_exposes_threat / control_mitigates_threat relations not fully extracted in this KG state; deferred to Codex post-Run-2 delta evaluation. Consult `25-rastreabilidade.md` for V1 entity → ES grounding per chapter; mitigation pathway inferable from existing Iter 4 + Run 1 layered output.)_

---

## § Future-work register (threat gaps) {#-future-work-register-threat-gaps}

_(No threat in gap state for this chapter.)_

---

## Generation provenance {#generation-provenance}

- **Manual ontology V2 canonical:** `sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml` (`meta.version: '2.0'`)
- **KG canonical state:** sbd-toe-knowledge-graph master @ `5550a74`
- **Threats canonical:** `data/entities/mitigated_threats.json` (233 items)
- **AntiPatterns canonical:** `data/publish/semantic/antipatterns.jsonl` (26 items)
- **Signals canonical:** `data/publish/semantic/signals.jsonl` (23 items)
- **AntiPattern→Threat relations:** `data/publish/semantic/antipattern_threat_links.jsonl`
- **§26 methodology layer:** `00-fundamentos/canon/26-metodologia-validacao-claims.md` (Run 1 state @ a9e70c98)
- **§26 §4 discipline applied:** Manual + CAPEC primary; CWE supporting only
- **Mitigation strength rule:** deterministic per `associated_controls` count + cross_chapter flag + confidence
- **Generated by:** Manual Agent Run 2 (50-ameacas-mitigadas enrichment)
- **Cycle:** Cycle B Run 2 — last content work pre frozen ceremony
