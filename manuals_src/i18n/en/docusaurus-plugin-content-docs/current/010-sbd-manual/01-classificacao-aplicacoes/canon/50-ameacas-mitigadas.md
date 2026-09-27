---
id: ameacas-mitigadas
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/canon/50-ameacas-mitigadas.md
  source_sha256: 12a2eb51eef43f86618ad67fda0389cf236e5820b1e819f26e769ffe7fc7f8df
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 6e6e9b076bcf8bd77c972f534c180270c2180dcaaab66399f7e1ab220cbffbfb
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [appsec_core, chapter_role, practitioner_manual, sbdtoe_sbd, threat]
  glossary_sha256: d6848e25b6e12f5a07a18c089cbfa4014a47146b90f01e8b6c8f85d7d44995c4
  translated_at: 2026-09-25T20:18:53Z
  reviewed_by: null
---

# 50. Mitigated Threats — Application Classification

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

Total: **22 entities** (Threat × 20, AntiPattern × 1, Signal × 1) mapped to this chapter.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-001` | Failure to apply minimum controls | normative | heuristic |
| Threat | `MT-002` | Over-engineering and excessive friction | normative | heuristic |
| Threat | `MT-003` | Inconsistency between projects with the same risk | normative | heuristic |
| Threat | `MT-004` | Optional security in low-risk products | normative | heuristic |
| Threat | `MT-005` | Critical changes without reclassification | normative | heuristic |
| Threat | `MT-006` | Integration with APIs or third parties ignored | normative | heuristic |
| Threat | `MT-007` | Deploy with altered risk not reviewed | normative | heuristic |
| Threat | `MT-008` | Different versions with divergent classifications | normative | heuristic |
| Threat | `MT-009` | Informal acceptance of critical risks | normative | heuristic |
| Threat | `MT-010` | Impossibility of subsequent audit | normative | heuristic |
| Threat | `MT-011` | Risk accepted by inappropriate parties | normative | heuristic |
| Threat | `MT-012` | Lack of regulatory explainability | normative | heuristic |
| Threat | `MT-013` | Poorly assessed exposed interfaces | normative | heuristic |
| Threat | `MT-014` | Unrecognised sensitive data | normative | heuristic |
| Threat | `MT-015` | Assumption of secure environments by default | normative | heuristic |
| Threat | `MT-016` | Ignoring critical dependencies | normative | heuristic |
| Threat | `MT-017` | Residual risk never reviewed | normative | heuristic |
| Threat | `MT-018` | Lack of planned reassessment events | normative | heuristic |
| Threat | `MT-019` | Reclassification dependent on exceptions | normative | heuristic |
| Threat | `MT-020` | Risk decisions without business feedback | normative | heuristic |
| AntiPattern | `sem:antipattern:aceitacao-de-risco-invalida` | invalid risk acceptance | semantic | scored |
| Signal | `sem:signal:alteracao-na-exposicao-dados-impacto-ou-forma-de-decisoes-e-validacoes` | change in exposure, data, impact or the way decisions and validations are made | semantic | scored |

---

## § Threat surfaces — Manual + CAPEC primary {#-threat-surfaces--manual--capec-primary}

Canonical threat surfaces per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (strong / partial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-001` | STRIDE | Failure to apply minimum controls | — | `addon/matriz-controlos-por-risco.md` | partial | Explicit |
| `MT-002` | STRIDE | Over-engineering and excessive friction | — | `addon/modelo-classificacao-eixos.md` | partial | Explicit |
| `MT-003` | STRIDE | Inconsistency between projects with the same risk | — | `addon/matriz-controlos-por-risco.md` | partial | Explicit |
| `MT-004` | STRIDE | Optional security in low-risk products | — | `addon/modelo-classificacao-eixos.md` | partial | Explicit |
| `MT-005` | STRIDE | Critical changes without reclassification | — | `addon/ciclo-vida-risco.md`, `15-aplicacao-lifecycle.md` | partial | Explicit |
| `MT-006` | STRIDE | Integration with APIs or third parties ignored | — | `addon/adopcao-drp-bia.md` | partial | Explicit |
| `MT-007` | STRIDE | Deploy with altered risk not reviewed | — | `checklist-revisao.md` | partial | Explicit |
| `MT-008` | STRIDE | Different versions with divergent classifications | — | `addon/risco-residual.md` | partial | Explicit |
| `MT-009` | STRIDE | Informal acceptance of critical risks | — | `addon/criterios-aceitacao-risco.md` | partial | Explicit |
| `MT-010` | STRIDE | Impossibility of subsequent audit | — | `addon/risco-residual.md` | partial | Explicit |
| `MT-011` | STRIDE | Risk accepted by inappropriate parties | — | `addon/criterios-aceitacao-risco.md` | partial | Explicit |
| `MT-012` | STRIDE | Lack of regulatory explainability | — | `addon/modelo-classificacao-eixos.md` | partial | Explicit |
| `MT-013` | STRIDE | Poorly assessed exposed interfaces | — | `addon/01-modelo-classificacao-eixos.md` | partial | Explicit |
| `MT-014` | STRIDE | Unrecognised sensitive data | — | `addon/08-mapeamento-ameacas-risco.md` | partial | Explicit |
| `MT-015` | STRIDE | Assumption of secure environments by default | — | `addon/03-adopcao-drp-bia.md` | partial | Explicit |
| `MT-016` | STRIDE | Ignoring critical dependencies | — | `addon/08-mapeamento-ameacas-risco.md` | partial | Explicit |
| `MT-017` | STRIDE | Residual risk never reviewed | — | `addon/06-risco-residual.md` | partial | Explicit |
| `MT-018` | STRIDE | Lack of planned reassessment events | — | `addon/07-ciclo-vida-risco.md` | partial | Explicit |
| `MT-019` | STRIDE | Reclassification dependent on exceptions | — | `20-checklist-revisao.md` | partial | Explicit |
| `MT-020` | STRIDE | Risk decisions without business feedback | — | `addon/09-criterios-aceitacao-risco.md` | partial | Explicit |

---

## § AntiPattern exposure mapping {#-antipattern-exposure-mapping}

AntiPattern → Threat exposure relations per Manual ontology V2 `antipattern_threat_links.jsonl`. Each link indicates that the antipattern (when present in code/process) exposes the threat.

| AntiPattern | Exposes threat | Confidence | Justification |
|---|---|---|---|
| `aceitacao-de-risco-invalida` | `MT-009` | 0.70 | alias_match, bundle_grounding, risk_match |
| `aceitacao-de-risco-invalida` | `MT-020` | 0.76 | alias_match, bundle_grounding, how_it_arises_match |

---

## § CWE references (supporting only) {#-cwe-references-supporting-only}

_(No threat with a CWE reference for this chapter.)_

---

## § V1 overlay — mitigation pathway (where Core-mapped) {#-v1-overlay--mitigation-pathway-where-core-mapped}

V1 controls/mechanisms anchored to this chapter that mitigate the threats listed above. The V1 overlay keeps the three-way routing visible per Manual ontology V2 + AppSec Core V1 + Substrate v7.

_(V1 overlay surfacing per Manual ontology V2 antipattern_exposes_threat / control_mitigates_threat relations not fully extracted in this KG state; deferred to Codex post-Run-2 delta evaluation. Consult `25-rastreabilidade.md` for V1 entity → ES grounding per chapter; mitigation pathway inferable from the existing Iter 4 + Run 1 layered output.)_

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
