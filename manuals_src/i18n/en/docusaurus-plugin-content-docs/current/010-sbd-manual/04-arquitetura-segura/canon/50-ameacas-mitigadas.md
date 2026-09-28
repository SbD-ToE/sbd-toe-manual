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
  source_path: 010-sbd-manual/04-arquitetura-segura/canon/50-ameacas-mitigadas.md
  source_sha256: 5a346558e2258d46e90edeea58cb097a0aa0e897b58ce2dae36a1f4b45fcf7b8
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: 93873087aafbf731022a7b10f98f7fc9e946023bb3388e18b3bab01fcef1b2cd
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [appsec_core, chapter_role, practitioner_manual, slug_threat_modeling, threat, traceability]
  glossary_sha256: 8c6c3b5b201f1f5f30b58439992f31fce8a70332973e3be9cc5ed9dbf9016362
  translated_at: 2026-09-28T09:12:02Z
  stamped_at: 2026-09-28T09:12:02Z
  reviewed_by: null
---

# 50. Mitigated Threats — Secure Architecture

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

Total: **22 entities** (Threat × 18, AntiPattern × 4, Signal × 0) mapped to this chapter.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-055` | Exposed interfaces without isolation | normative | heuristic |
| Threat | `MT-056` | Data and control mixed in the same zone | normative | heuristic |
| Threat | `MT-057` | Uncontrolled lateral access between modules | normative | heuristic |
| Threat | `MT-058` | Absence of isolation between users | normative | heuristic |
| Threat | `MT-059` | Non-existent or outdated architecture | normative | heuristic |
| Threat | `MT-060` | Confusion about the location of controls | normative | heuristic |
| Threat | `MT-061` | Ambiguity about boundaries and zones | normative | heuristic |
| Threat | `MT-062` | Architecture does not review fallback mechanisms | normative | heuristic |
| Threat | `MT-063` | Architecture never reviewed | normative | heuristic |
| Threat | `MT-064` | Structural changes without revalidation | normative | heuristic |
| Threat | `MT-065` | Informal or ad hoc design | normative | heuristic |
| Threat | `MT-066` | Architecture exceptions without a trace | normative | heuristic |
| Threat | `MT-067` | Architecture requirements not defined | normative | heuristic |
| Threat | `MT-068` | Impossibility of mapping decisions to controls | normative | heuristic |
| Threat | `MT-069` | Diagram does not reflect implemented controls | normative | heuristic |
| Threat | `MT-070` | L1 applications treated as critical | normative | heuristic |
| Threat | `MT-071` | Over-dimensioning of the architecture's security | normative | heuristic |
| Threat | `MT-072` | Execution environments not reflected in the design | normative | heuristic |
| AntiPattern | `sem:antipattern:dependencia-circular` | circular dependency | semantic | scored |
| AntiPattern | `sem:antipattern:excecoes-nao-documentadas` | Undocumented exceptions | semantic | scored |
| AntiPattern | `sem:antipattern:modelos-inconsistentes-incompletos-ou-desatualizados` | Inconsistent, incomplete or outdated models | semantic | scored |
| AntiPattern | `sem:antipattern:threat-modeling-sem-arquitetura-clara` | Threat modelling without a clear architecture | semantic | scored |

---

## § Threat surfaces — Manual + CAPEC primary {#-threat-surfaces--manual--capec-primary}

Canonical threat surfaces per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (strong / partial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-055` | STRIDE | Exposed interfaces without isolation | — | `addon/01-catalogo-requisitos.md` | partial | Explicit |
| `MT-056` | STRIDE | Data and control mixed in the same zone | — | `addon/04-diagramas-referencia.md` | partial | Explicit |
| `MT-057` | STRIDE | Uncontrolled lateral access between modules | — | `addon/02-casos-praticos.md` | partial | Explicit |
| `MT-058` | STRIDE | Absence of isolation between users | — | `addon/01-catalogo-requisitos.md` | partial | Explicit |
| `MT-059` | STRIDE | Non-existent or outdated architecture | — | `addon/04-diagramas-referencia.md` | partial | Explicit |
| `MT-060` | STRIDE | Confusion about the location of controls | — | `addon/01-catalogo-requisitos.md` | partial | Explicit |
| `MT-061` | STRIDE | Ambiguity about boundaries and zones | — | `addon/04-diagramas-referencia.md` | partial | Explicit |
| `MT-062` | STRIDE | Architecture does not review fallback mechanisms | — | `addon/01-catalogo-requisitos.md` | partial | Explicit |
| `MT-063` | STRIDE | Architecture never reviewed | — | `15-aplicacao-lifecycle.md` | partial | Explicit |
| `MT-064` | STRIDE | Structural changes without revalidation | — | `addon/05-validacao.md` | partial | Explicit |
| `MT-065` | STRIDE | Informal or ad hoc design | — | `addon/05-validacao.md` | partial | Explicit |
| `MT-066` | STRIDE | Architecture exceptions without a trace | — | `addon/03-excecoes.md` | partial | Explicit |
| `MT-067` | STRIDE | Architecture requirements not defined | — | `addon/01-catalogo-requisitos.md` | partial | Explicit |
| `MT-068` | STRIDE | Impossibility of mapping decisions to controls | — | `addon/06-rastreabilidade.md` | partial | Explicit |
| `MT-069` | STRIDE | Diagram does not reflect implemented controls | — | `addon/05-validacao.md` | partial | Explicit |
| `MT-070` | STRIDE | L1 applications treated as critical | — | `15-aplicacao-lifecycle.md` | partial | Explicit |
| `MT-071` | STRIDE | Over-dimensioning of the architecture's security | — | `addon/02-casos-praticos.md` | partial | Explicit |
| `MT-072` | STRIDE | Execution environments not reflected in the design | — | `addon/04-diagramas-referencia.md` | partial | Explicit |

---

## § AntiPattern exposure mapping {#-antipattern-exposure-mapping}

_(No antipattern→threat relation mapped to this chapter.)_

---

## § CWE references (supporting only) {#-cwe-references-supporting-only}

_(No threat with a CWE reference for this chapter.)_

---

## § V1 overlay — mitigation pathway (where Core-mapped) {#-v1-overlay--mitigation-pathway-where-core-mapped}

V1 controls/mechanisms anchored to this chapter that mitigate the threats listed above. The V1 overlay keeps the three-way routing visible per Manual ontology V2 + AppSec Core V1 + Substrate v7.

_(The relations between anti-patterns, threats and controls are not yet complete in this version. Each entity's grounding in external sources is in the chapter's [Traceability](/sbd-toe/sbd-manual/arquitetura-segura/canon/rastreabilidade) page.)_

---

## § Future-work register (threat gaps) {#-future-work-register-threat-gaps}

_(No threat in gap state for this chapter.)_
