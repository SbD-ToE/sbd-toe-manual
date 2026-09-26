---
id: ameacas-mitigadas
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/canon/50-ameacas-mitigadas.md
  source_sha256: 6b72fafbb58599fe2af96b2433bb816ecdee6e8cf570b105efcc1590226b007e
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: fcfc3616caeffb140919c5ab06c374d9e0745eada647799a7bcce1bc7fecc3b2
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5536afdcc04f76a07c66e747133c73d68308884707c296abf945937a9630a312
  glossary_keys: [appsec_core, chapter_role, practitioner_manual, sbdtoe_sbd, threat]
  glossary_sha256: d6848e25b6e12f5a07a18c089cbfa4014a47146b90f01e8b6c8f85d7d44995c4
  translated_at: 2026-09-26T08:32:11Z
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
