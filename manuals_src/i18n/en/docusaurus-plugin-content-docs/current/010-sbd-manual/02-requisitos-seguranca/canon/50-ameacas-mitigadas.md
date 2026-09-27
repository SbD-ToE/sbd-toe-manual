---
id: ameacas-mitigadas
translation:
  source_locale: pt
  source_path: 010-sbd-manual/02-requisitos-seguranca/canon/50-ameacas-mitigadas.md
  source_sha256: c1ee0c4d83e967322abae49dfc6f3863b0c4e5c5341cb648bc69c34c7c5f6f27
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 94670bc2102601a05946f408f9f380ccd2261640799367974b250985fde45ad6
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [appsec_core, chapter_role, practitioner_manual, requirement_runtime, sbdtoe_sbd, threat, validation_evaluation]
  glossary_sha256: 7c38fcf2d45fb4f99a6ffb52b7340a97175bbf08d2f4c8e566e7784560043cf2
  translated_at: 2026-09-25T20:20:17Z
  stamped_at: 2026-09-26T18:33:11Z
  reviewed_by: null
---

# 50. Mitigated Threats — Security Requirements

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

Total: **18 entities** (Threat × 18, AntiPattern × 0, Signal × 0) mapped to this chapter.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-021` | Absence of security requirements | normative | heuristic |
| Threat | `MT-022` | Ambiguous or untestable definition | normative | heuristic |
| Threat | `MT-023` | Generic, non-specific requirements | normative | heuristic |
| Threat | `MT-024` | Lack of requirements in legacy systems | normative | heuristic |
| Threat | `MT-025` | Requirements not aligned with risk | normative | heuristic |
| Threat | `MT-026` | Requirements defined but never verified | normative | heuristic |
| Threat | `MT-027` | Inconsistent validations across projects | normative | heuristic |
| Threat | `MT-028` | No tracing between requirement and test | normative | heuristic |
| Threat | `MT-029` | Requirements not verified in CI/CD | normative | heuristic |
| Threat | `MT-030` | Risk accepted without documentary validation | normative | heuristic |
| Threat | `MT-031` | Undocumented exceptions to requirements | normative | heuristic |
| Threat | `MT-032` | Security omitted for “not being functional” | normative | heuristic |
| Threat | `MT-033` | Acceptance of exceptions without approval | normative | heuristic |
| Threat | `MT-034` | Exceptions not re-verified in time | normative | heuristic |
| Threat | `MT-035` | Not knowing whether requirements were applied | normative | heuristic |
| Threat | `MT-036` | Requirements applied but not tested | normative | heuristic |
| Threat | `MT-037` | Requirement changes not propagated | normative | heuristic |
| Threat | `MT-038` | Ambiguity between requirement and control | normative | heuristic |

---

## § Threat surfaces — Manual + CAPEC primary {#-threat-surfaces--manual--capec-primary}

Canonical threat surfaces per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (strong / partial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-021` | STRIDE | Absence of security requirements | — | `addon/01-catalogo-requisitos.md` | partial | Explicit |
| `MT-022` | STRIDE | Ambiguous or untestable definition | — | `addon/07-validacao-requisitos.md` | partial | Explicit |
| `MT-023` | STRIDE | Generic, non-specific requirements | — | `addon/09-taxonomia-rastreabilidade.md` | partial | Explicit |
| `MT-024` | STRIDE | Lack of requirements in legacy systems | — | `addon/08-gestao-excecoes.md` | partial | Explicit |
| `MT-025` | STRIDE | Requirements not aligned with risk | — | `addon/06-matriz-controlos-por-risco.md` | partial | Explicit |
| `MT-026` | STRIDE | Requirements defined but never verified | — | `addon/10-validacao-requisitos.md` | partial | Explicit |
| `MT-027` | STRIDE | Inconsistent validations across projects | — | `addon/07-validacao-requisitos.md` | partial | Explicit |
| `MT-028` | STRIDE | No tracing between requirement and test | — | `addon/04-rastreabilidade-controlo.md` | partial | Explicit |
| `MT-029` | STRIDE | Requirements not verified in CI/CD | — | `addon/10-validacao-requisitos.md` | partial | Explicit |
| `MT-030` | STRIDE | Risk accepted without documentary validation | — | `addon/08-gestao-excecoes.md` | partial | Explicit |
| `MT-031` | STRIDE | Undocumented exceptions to requirements | — | `addon/08-gestao-excecoes.md` | partial | Explicit |
| `MT-032` | STRIDE | Security omitted for “not being functional” | — | `addon/01-catalogo-requisitos.md` | partial | Explicit |
| `MT-033` | STRIDE | Acceptance of exceptions without approval | — | `addon/08-gestao-excecoes.md` | partial | Explicit |
| `MT-034` | STRIDE | Exceptions not re-verified in time | — | `15-aplicacao-lifecycle.md` | partial | Explicit |
| `MT-035` | STRIDE | Not knowing whether requirements were applied | — | `addon/04-rastreabilidade-controlo.md` | partial | Explicit |
| `MT-036` | STRIDE | Requirements applied but not tested | — | `addon/07-validacao-requisitos.md` | partial | Explicit |
| `MT-037` | STRIDE | Requirement changes not propagated | — | `addon/01-catalogo-requisitos.md` | partial | Explicit |
| `MT-038` | STRIDE | Ambiguity between requirement and control | — | `addon/04-rastreabilidade-controlo.md` | partial | Explicit |

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
