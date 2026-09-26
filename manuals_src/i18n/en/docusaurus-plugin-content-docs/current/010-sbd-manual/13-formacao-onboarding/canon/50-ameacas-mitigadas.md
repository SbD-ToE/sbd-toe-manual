---
id: ameacas-mitigadas
translation:
  source_locale: pt
  source_path: 010-sbd-manual/13-formacao-onboarding/canon/50-ameacas-mitigadas.md
  source_sha256: eae817507db0a65c9f7ce6d09e7bfedef9713b2f7526c97d416b3f941dc3ef69
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: a6e4bc513dfd53ab32f88505f150d42a51eb3099a46905caa621ff7b0577455a
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: d743dfcba33f930c34618b93d1eaaa34f697328d45aaf3bb657c33b8b3c59c9a
  glossary_keys: [appsec_core, chapter_role, practitioner_manual, sbdtoe_sbd, threat, validation_evaluation]
  glossary_sha256: 66dc1ea81e0696f526385701404677faa1969855e799b1d5c40b1faa7ae6f170
  translated_at: 2026-09-26T11:44:29Z
  reviewed_by: null
---

# 50. Mitigated Threats — Training and Onboarding

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

Total: **16 entities** (Threat × 10, AntiPattern × 2, Signal × 4) mapped to this chapter.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-212` | Insecure configuration due to lack of knowledge | normative | heuristic |
| Threat | `MT-213` | Improper reuse of secrets or tokens | normative | heuristic |
| Threat | `MT-214` | Technical access granted without validation | normative | heuristic |
| Threat | `MT-215` | Inclusion of third parties without validation | normative | heuristic |
| Threat | `MT-216` | Lack of ownership of security | normative | heuristic |
| Threat | `MT-217` | Behavioural regression / fragile culture | normative | heuristic |
| Threat | `MT-218` | Non-traceable training | normative | heuristic |
| Threat | `MT-219` | Uneven training across teams or roles | normative | heuristic |
| Threat | `MT-220` | Theoretical training without practical impact | normative | heuristic |
| Threat | `MT-221` | Outdated or non-applicable content | normative | heuristic |
| AntiPattern | `sem:antipattern:dependencia-exclusiva-de-ferramentas-automatizadas` | exclusive reliance on automated tools | semantic | scored |
| AntiPattern | `sem:antipattern:falta-de-onboarding` | Lack of Onboarding | semantic | scored |
| Signal | `sem:signal:checklist-completo` | Completed Checklist | semantic | scored |
| Signal | `sem:signal:kpis-de-eficacia-formativa` | Training effectiveness KPIs | semantic | scored |
| Signal | `sem:signal:kpis-de-formacao` | Training KPIs | semantic | scored |
| Signal | `sem:signal:resultados-de-quiz` | Quiz Results | semantic | scored |

---

## § Threat surfaces — Manual + CAPEC primary {#-threat-surfaces--manual--capec-primary}

Canonical threat surfaces per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (strong / partial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-212` | STRIDE | Insecure configuration due to lack of knowledge | — | `addon/01-catalogo-formativo.md`, `addon/02-trilho-formativo.md` | partial | Explicit |
| `MT-213` | STRIDE | Improper reuse of secrets or tokens | — | `addon/04-tecnicas-formativas.md`, `addon/06-manual-formacao-por-capitulo.md` | partial | Explicit |
| `MT-214` | STRIDE | Technical access granted without validation | — | `addon/10-checklist-onboarding.md`, `addon/11-template-quiz-onboarding.md` | partial | Explicit |
| `MT-215` | STRIDE | Inclusion of third parties without validation | — | `addon/20-modelo-inclusao-terceiros.md`, `addon/21-plano-formacao-terceiros.md` | partial | Explicit |
| `MT-216` | STRIDE | Lack of ownership of security | — | `addon/03-programa-champions.md` | partial | Explicit |
| `MT-217` | STRIDE | Behavioural regression / fragile culture | — | `addon/04-tecnicas-formativas.md`, `addon/90-indicadores-metricas.md` | partial | Explicit |
| `MT-218` | STRIDE | Non-traceable training | — | `addon/10-checklist-onboarding.md`, `addon/11-template-quiz-onboarding.md` | partial | Explicit |
| `MT-219` | STRIDE | Uneven training across teams or roles | — | `addon/02-trilho-formativo.md`, `addon/05-integracao-transversal.md` | partial | Explicit |
| `MT-220` | STRIDE | Theoretical training without practical impact | — | `addon/04-tecnicas-formativas.md`, `addon/06-manual-formacao-por-capitulo.md` | partial | Explicit |
| `MT-221` | STRIDE | Outdated or non-applicable content | — | `addon/06-manual-formacao-por-capitulo.md`, `addon/07-exemplo1-manual-formacao-dev-pr-seguro.md` | partial | Explicit |

---

## § AntiPattern exposure mapping {#-antipattern-exposure-mapping}

_(No antipattern→threat relation mapped to this chapter.)_

---

## § CWE references (supporting only) {#-cwe-references-supporting-only}

CWE references per §26 §4: **CWE only as limited support, NOT as a substitute for a threat taxonomy**. Mapping to the Manual threats listed below.

| CWE-ID | Linked threat | Note |
|---|---|---|
| `CWE-693` | `?` | supporting reference; the primary anchor is the Manual threat |
| `CWE-798` | `?` | supporting reference; the primary anchor is the Manual threat |

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
