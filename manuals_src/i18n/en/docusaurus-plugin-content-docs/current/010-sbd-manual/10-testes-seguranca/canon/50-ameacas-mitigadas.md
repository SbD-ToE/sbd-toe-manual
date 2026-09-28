---
# Proveniência da geração: não se mostra ao leitor (extraída do corpo na v1.17.1).
sbdtoe_provenance:
  ontology_v2: 'sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml (meta.version: ''2.0'')'
  kg_state: sbd-toe-knowledge-graph master @ 5550a743bb9de205676c503da5e81863ed62ab54 (2026-05-11; commit de governação imediatamente a seguir à tag kg-v1-cycle-b-iter-3-aligned-2026-05-11 @ 482ece916cc254126894019432ebd113695365d9)
  generated_by: Manual Agent Run 2 (50-ameacas-mitigadas enrichment)
  cycle: Cycle B Run 2 — last content work pre frozen ceremony
  notes:
  - 'Threats canonical: data/entities/mitigated_threats.json (233 items)'
  - 'AntiPatterns canonical: data/publish/semantic/antipatterns.jsonl (26 items)'
  - 'Signals canonical: data/publish/semantic/signals.jsonl (23 items)'
  - 'AntiPattern→Threat relations: data/publish/semantic/antipattern_threat_links.jsonl'
  - '§26 methodology layer: 00-fundamentos/canon/26-metodologia-validacao-claims.md (Run 1 state @ a9e70c98937d41587e86712199fab46854a8d6aa)'
  - '§26 §4 discipline applied: Manual + CAPEC primary; CWE supporting only'
  - 'Mitigation strength rule: deterministic per associated_controls count + cross_chapter flag + confidence'
  - V1 overlay surfacing per Manual ontology V2 antipattern_exposes_threat / control_mitigates_threat relations não totalmente extraídas neste estado do KG; deferred a Codex post-Run-2 delta evaluation; mitigation pathway inferable from Iter 4 + Run 1 layered output
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/canon/50-ameacas-mitigadas.md
  source_sha256: c568cad776d0334f49dd25e85b8c45a1c58fa8d1c7b4bd30b5cf8395d310e8fa
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: aa75fd1a41fef94586fe4dc0271fc0b051259a6a6817afe54c8f116b548f27e4
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [appsec_core, chapter_role, practitioner_manual, threat, traceability]
  glossary_sha256: ee9254db342fbd435a6a08ff5fdf55af403af8d5e22e5fc3dea01aa8913d64d7
  translated_at: 2026-09-28T09:12:16Z
  stamped_at: 2026-09-28T09:12:16Z
  reviewed_by: null
---

# 50. Mitigated Threats — Security Testing

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
| Threat | `MT-167` | Injections (SQLi, OS Command, etc.) | normative | heuristic |
| Threat | `MT-168` | Access control failures | normative | heuristic |
| Threat | `MT-169` | Exploitable business logic | normative | heuristic |
| Threat | `MT-170` | Security regression | normative | heuristic |
| Threat | `MT-171` | Low test coverage | normative | heuristic |
| Threat | `MT-172` | Known flaws not tested | normative | heuristic |
| Threat | `MT-173` | Flaws detected but not resolved | normative | heuristic |
| Threat | `MT-174` | Team without technical feedback | normative | heuristic |
| Threat | `MT-175` | Non-repeatable validations | normative | heuristic |
| Threat | `MT-176` | Non-scalable manual tests | normative | heuristic |
| Threat | `MT-177` | Lack of testing before go-live | normative | heuristic |
| Threat | `MT-178` | Quality decision made without basis | normative | heuristic |
| Threat | `MT-179` | New classes not detected by SAST/DAST | normative | heuristic |
| Threat | `MT-180` | Superficial tests without technical context | normative | heuristic |
| Threat | `MT-181` | Tools not calibrated by context | normative | heuristic |

---

## § Threat surfaces — Manual + CAPEC primary {#-threat-surfaces--manual--capec-primary}

Canonical threat surfaces per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (strong / partial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-167` | STRIDE | Injections (SQLi, OS Command, etc.) | — | `addon/01-sast.md`, `addon/02-dast.md` | partial | Explicit |
| `MT-168` | STRIDE | Access control failures | — | `addon/02-dast.md`, `addon/03-iast.md` | partial | Explicit |
| `MT-169` | STRIDE | Exploitable business logic | — | `addon/04-fuzzing.md`, `addon/11-pen-testing.md` | partial | Explicit |
| `MT-170` | STRIDE | Security regression | — | `addon/05-validacao-regressao.md` | partial | Explicit |
| `MT-171` | STRIDE | Low test coverage | — | `addon/06-cobertura-e-priorizacao.md` | partial | Explicit |
| `MT-172` | STRIDE | Known flaws not tested | — | `addon/08-gestao-findings.md`, `addon/09-feedback-equipa.md` | partial | Explicit |
| `MT-173` | STRIDE | Flaws detected but not resolved | — | `addon/08-gestao-findings.md` | partial | Explicit |
| `MT-174` | STRIDE | Team without technical feedback | — | `addon/09-feedback-equipa.md` | partial | Explicit |
| `MT-175` | STRIDE | Non-repeatable validations | — | `addon/00-estrategia-testes.md`, `addon/07-integracao-pipeline.md` | partial | Explicit |
| `MT-176` | STRIDE | Non-scalable manual tests | — | `addon/07-integracao-pipeline.md` | partial | Explicit |
| `MT-177` | STRIDE | Lack of testing before go-live | — | `20-checklist-revisao.md` | partial | Explicit |
| `MT-178` | STRIDE | Quality decision made without basis | — | `addon/06-cobertura-e-priorizacao.md` | partial | Explicit |
| `MT-179` | STRIDE | New classes not detected by SAST/DAST | — | `addon/11-pen-testing.md` | partial | Explicit |
| `MT-180` | STRIDE | Superficial tests without technical context | — | `addon/00-estrategia-testes.md` | partial | Explicit |
| `MT-181` | STRIDE | Tools not calibrated by context | — | `addon/00-estrategia-testes.md`, `addon/09-feedback-equipa.md` | partial | Explicit |

---

## § AntiPattern exposure mapping {#-antipattern-exposure-mapping}

_(No antipattern→threat relation mapped to this chapter.)_

---

## § CWE references (supporting only) {#-cwe-references-supporting-only}

_(No threat with a CWE reference for this chapter.)_

---

## § V1 overlay — mitigation pathway (where Core-mapped) {#-v1-overlay--mitigation-pathway-where-core-mapped}

V1 controls/mechanisms anchored to this chapter that mitigate the threats listed above. The V1 overlay keeps the three-way routing visible per Manual ontology V2 + AppSec Core V1 + Substrate v7.

_(The relations between anti-patterns, threats and controls are not yet complete in this version. Each entity's grounding in external sources is in the chapter's [Traceability](/sbd-toe/sbd-manual/testes-seguranca/canon/rastreabilidade) page.)_

---

## § Future-work register (threat gaps) {#-future-work-register-threat-gaps}

_(No threat in gap state for this chapter.)_
