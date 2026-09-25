---
id: ameacas-mitigadas
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/canon/50-ameacas-mitigadas.md
  source_sha256: b6402d1672c2039ea63efb2af99e8149a0503f42fbf83d1c9eb4c0e3995300c7
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: a94fce87965c5319543c60eaebf195a03180ca42dd0e9b8da5f853e739107575
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [appsec_core, chapter_role, cycle_iteration, practitioner_manual, sbdtoe_sbd, threat, validation_evaluation]
  glossary_sha256: 6708f846bd79b416a80378292695254fd5e0c58ff12db585a70697c0cd922bee
  translated_at: 2026-09-25T20:17:05Z
  reviewed_by: null
---

# 50. Mitigated Threats — Threat Modelling

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

Total: **18 entities** (Threat × 16, AntiPattern × 2, Signal × 0) mapped to this chapter.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-039` | Unknown and unaddressed threats | normative | heuristic |
| Threat | `MT-040` | Poorly defined security priorities | normative | heuristic |
| Threat | `MT-041` | Requirements defined without a basis in threats | normative | heuristic |
| Threat | `MT-042` | Privacy threats ignored | normative | heuristic |
| Threat | `MT-043` | Lack of coverage of non-technical threats | normative | heuristic |
| Threat | `MT-044` | Insecure architecture not identified | normative | heuristic |
| Threat | `MT-045` | Superficial validation in design reviews | normative | heuristic |
| Threat | `MT-046` | Controls applied without a basis in architecture | normative | heuristic |
| Threat | `MT-047` | Absence of review of critical interfaces | normative | heuristic |
| Threat | `MT-048` | Threats discovered too late | normative | heuristic |
| Threat | `MT-049` | Critical changes without new modelling | normative | heuristic |
| Threat | `MT-050` | Discontinuity between teams and phases | normative | heuristic |
| Threat | `MT-051` | Threats not visible in the CI/CD pipeline | normative | heuristic |
| Threat | `MT-052` | Threat knowledge not accumulated | normative | heuristic |
| Threat | `MT-053` | Inconsistency between projects and teams | normative | heuristic |
| Threat | `MT-054` | Tools disconnected from the cycle | normative | heuristic |
| AntiPattern | `sem:antipattern:ausencia-de-ameaca-no-modelo` | Absence of a threat from the model | semantic | scored |
| AntiPattern | `sem:antipattern:omissao-estrutural-de-ameacas` | Structural omission of threats | semantic | scored |

---

## § Threat surfaces — Manual + CAPEC primary {#-threat-surfaces--manual--capec-primary}

Canonical threat surfaces per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (strong / partial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-039` | STRIDE | Unknown and unaddressed threats | — | `addon/01-metodologias-e-ferramentas.md` | partial | Explicit |
| `MT-040` | STRIDE | Poorly defined security priorities | — | `addon/07-mapeamento-threats-requisitos.md` | partial | Explicit |
| `MT-041` | STRIDE | Requirements defined without a basis in threats | — | `addon/07-mapeamento-threats-requisitos.md` | partial | Explicit |
| `MT-042` | LINDDUN | Privacy threats ignored | — | `addon/08-exemplo-privacidade.md` | partial | Explicit |
| `MT-043` | STRIDE | Lack of coverage of non-technical threats | — | `addon/01-metodologias-e-ferramentas.md` | partial | Explicit |
| `MT-044` | STRIDE | Insecure architecture not identified | — | `addon/09-validacao-arquitetura.md` | partial | Explicit |
| `MT-045` | STRIDE | Superficial validation in design reviews | — | `15-aplicacao-lifecycle.md` | partial | Explicit |
| `MT-046` | STRIDE | Controls applied without a basis in architecture | — | `addon/07-mapeamento-threats-requisitos.md` | partial | Explicit |
| `MT-047` | STRIDE | Absence of review of critical interfaces | — | `addon/01-metodologias-e-ferramentas.md` | partial | Explicit |
| `MT-048` | STRIDE | Threats discovered too late | — | `15-aplicacao-lifecycle.md` | partial | Explicit |
| `MT-049` | STRIDE | Critical changes without new modelling | — | `addon/09-validacao-arquitetura.md` | partial | Explicit |
| `MT-050` | STRIDE | Discontinuity between teams and phases | — | `addon/07-mapeamento-threats-requisitos.md` | partial | Explicit |
| `MT-051` | STRIDE | Threats not visible in the CI/CD pipeline | — | `addon/06-threat-modeling-ci.md` | partial | Explicit |
| `MT-052` | STRIDE | Threat knowledge not accumulated | — | `addon/10-integracao-iriusrisk.md` | partial | Explicit |
| `MT-053` | STRIDE | Inconsistency between projects and teams | — | `addon/01-metodologias-e-ferramentas.md` | partial | Explicit |
| `MT-054` | STRIDE | Tools disconnected from the cycle | — | `addon/07-mapeamento-threats-requisitos.md` | partial | Explicit |

---

## § AntiPattern exposure mapping {#-antipattern-exposure-mapping}

_(No antipattern→threat relation mapped to this chapter.)_

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
