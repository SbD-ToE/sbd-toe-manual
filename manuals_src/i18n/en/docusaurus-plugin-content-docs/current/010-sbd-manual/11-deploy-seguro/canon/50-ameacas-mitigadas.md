---
id: ameacas-mitigadas
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/canon/50-ameacas-mitigadas.md
  source_sha256: 7d5593c99d0408d2d14ff1da03363e12977112c337bc2b850dfab3aa6fe8c2ae
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: e0f2f34031c0f08912ba71fb5f741bde35af7d197419e0e8428e17e25339fa84
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [appsec_core, chapter_role, practitioner_manual, sbdtoe_sbd, threat, validation_evaluation]
  glossary_sha256: 1ca9ef565e0e29811dee08c8b3d54599c55f8fae7c7e5fe54615dec97baf7b98
  translated_at: 2026-09-26T11:00:55Z
  stamped_at: 2026-09-26T18:35:34Z
  reviewed_by: null
---

# 50. Mitigated Threats — Secure Deployment

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

Total: **15 entities** (Threat × 15, AntiPattern × 0, Signal × 0) mapped to this chapter.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-182` | Code in production without validation | normative | heuristic |
| Threat | `MT-183` | Functional activation without control | normative | heuristic |
| Threat | `MT-184` | Manual promotion outside the CI/CD | normative | heuristic |
| Threat | `MT-185` | Failed deployment without rollback | normative | heuristic |
| Threat | `MT-186` | Irreversible feature | normative | heuristic |
| Threat | `MT-187` | Failure without response | normative | heuristic |
| Threat | `MT-188` | Joint release without segmentation | normative | heuristic |
| Threat | `MT-189` | Feature exposed to all users | normative | heuristic |
| Threat | `MT-190` | Lack of operational validation | normative | heuristic |
| Threat | `MT-191` | Undetected post-deployment failures | normative | heuristic |
| Threat | `MT-192` | Late response to critical problems | normative | heuristic |
| Threat | `MT-193` | Critical events ignored | normative | heuristic |
| Threat | `MT-194` | Toggle activated inadvertently | normative | heuristic |
| Threat | `MT-195` | Release without geographical or logical segmentation | normative | heuristic |
| Threat | `MT-196` | Execution of a non-validated critical function | normative | heuristic |

---

## § Threat surfaces — Manual + CAPEC primary {#-threat-surfaces--manual--capec-primary}

Canonical threat surfaces per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (strong / partial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-182` | STRIDE | Code in production without validation | — | `addon/04-validacoes-pre-deploy.md` | partial | Explicit |
| `MT-183` | STRIDE | Functional activation without control | — | `addon/03-feature-flags-e-toggle.md` | partial | Explicit |
| `MT-184` | STRIDE | Manual promotion outside the CI/CD | — | `addon/01-modelo-controle-execucao.md` | partial | Explicit |
| `MT-185` | STRIDE | Failed deployment without rollback | — | `addon/06-controle-versao-e-rollback.md` | partial | Explicit |
| `MT-186` | STRIDE | Irreversible feature | — | `addon/03-feature-flags-e-toggle.md` | partial | Explicit |
| `MT-187` | STRIDE | Failure without response | — | `addon/05-monitorizacao-e-reacao.md` | partial | Explicit |
| `MT-188` | STRIDE | Joint release without segmentation | — | `addon/02-praticas-release-management.md` | partial | Explicit |
| `MT-189` | STRIDE | Feature exposed to all users | — | `addon/03-feature-flags-e-toggle.md` | partial | Explicit |
| `MT-190` | STRIDE | Lack of operational validation | — | `addon/08-segregacao-e-validacao-operacional.md` | partial | Explicit |
| `MT-191` | STRIDE | Undetected post-deployment failures | — | `addon/05-monitorizacao-e-reacao.md` | partial | Explicit |
| `MT-192` | STRIDE | Late response to critical problems | — | `addon/05-monitorizacao-e-reacao.md` | partial | Explicit |
| `MT-193` | STRIDE | Critical events ignored | — | `addon/06-controle-versao-e-rollback.md` | partial | Explicit |
| `MT-194` | STRIDE | Toggle activated inadvertently | — | `addon/03-feature-flags-e-toggle.md` | partial | Explicit |
| `MT-195` | STRIDE | Release without geographical or logical segmentation | — | `addon/07-deploy-progressivo-e-risco.md` | partial | Explicit |
| `MT-196` | STRIDE | Execution of a non-validated critical function | — | `addon/08-segregacao-e-validacao-operacional.md` | partial | Explicit |

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
