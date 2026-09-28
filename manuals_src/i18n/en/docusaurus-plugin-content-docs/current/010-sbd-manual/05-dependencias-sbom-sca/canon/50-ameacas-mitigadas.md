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
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/canon/50-ameacas-mitigadas.md
  source_sha256: 56db14891c8bea5c9c691067ba0c634c633fa16b9037f8ec9d8b9a7c1dbc65a0
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: 99059e457c3aef7a64b680f90d4c31e39b8526c9d45caa577a1944853f75f0f7
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [appsec_core, chapter_role, cycle_iteration, practitioner_manual, threat, traceability, validation_evaluation]
  glossary_sha256: 86f50985e8d41165ea57d8c206b563afbb77cfbd17d617ee3242313777a31fe6
  translated_at: 2026-09-28T09:12:04Z
  stamped_at: 2026-09-28T09:12:04Z
  reviewed_by: null
---

# 50. Mitigated Threats — Dependencies, SBOM and SCA

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

Total: **20 entities** (Threat × 20, AntiPattern × 0, Signal × 0) mapped to this chapter.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-073` | Inclusion of libraries with active CVEs | normative | heuristic |
| Threat | `MT-074` | Outdated dependencies | normative | heuristic |
| Threat | `MT-075` | Absence of a version record | normative | heuristic |
| Threat | `MT-076` | Inclusion of unaudited libraries | normative | heuristic |
| Threat | `MT-077` | Lack of knowledge of the libraries used | normative | heuristic |
| Threat | `MT-078` | Lack of association between vulnerability and artefact | normative | heuristic |
| Threat | `MT-079` | Lack of a history of package introduction | normative | heuristic |
| Threat | `MT-080` | Inclusion of packages from malicious repositories | normative | heuristic |
| Threat | `MT-081` | Transitive dependency with an insecure component | normative | heuristic |
| Threat | `MT-082` | Pipeline injects an unauthenticated version | normative | heuristic |
| Threat | `MT-083` | CVEs ignored without justification | normative | heuristic |
| Threat | `MT-084` | Mitigations applied without tracking | normative | heuristic |
| Threat | `MT-085` | Lack of an exception review cycle | normative | heuristic |
| Threat | `MT-086` | Arbitrary use of libraries | normative | heuristic |
| Threat | `MT-087` | Prohibited libraries are used | normative | heuristic |
| Threat | `MT-088` | Lack of a replacement policy | normative | heuristic |
| Threat | `MT-089` | Introduction of an undeclared vulnerable dependency | normative | heuristic |
| Threat | `MT-090` | Dependency confusion | normative | heuristic |
| Threat | `MT-091` | Backdoor via a build tool | normative | heuristic |
| Threat | `MT-092` | Composition drift between builds | normative | heuristic |

---

## § Threat surfaces — Manual + CAPEC primary {#-threat-surfaces--manual--capec-primary}

Canonical threat surfaces per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (strong / partial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-073` | STRIDE | Inclusion of libraries with active CVEs | — | `addon/02-analise-sca.md` | partial | Explicit |
| `MT-074` | STRIDE | Outdated dependencies | — | `addon/05-politica-atualizacoes.md` | partial | Explicit |
| `MT-075` | STRIDE | Absence of a version record | — | `addon/01-inventario-sbom.md` | partial | Explicit |
| `MT-076` | STRIDE | Inclusion of unaudited libraries | — | `addon/03-governanca-libs-terceiros.md` | partial | Explicit |
| `MT-077` | STRIDE | Lack of knowledge of the libraries used | — | `addon/01-inventario-sbom.md` | partial | Explicit |
| `MT-078` | STRIDE | Lack of association between vulnerability and artefact | — | `addon/08-rastreabilidade-vulnerabilidades.md` | partial | Explicit |
| `MT-079` | STRIDE | Lack of a history of package introduction | — | `addon/07-controle-registos-origem.md` | partial | Explicit |
| `MT-080` | STRIDE | Inclusion of packages from malicious repositories | — | `addon/07-controle-registos-origem.md` | partial | Explicit |
| `MT-081` | STRIDE | Transitive dependency with an insecure component | — | `addon/02-analise-sca.md` | partial | Explicit |
| `MT-082` | STRIDE | Pipeline injects an unauthenticated version | — | `addon/04-integracao-ci-cd.md` | partial | Explicit |
| `MT-083` | STRIDE | CVEs ignored without justification | — | `addon/09-excecoes-e-aceitacao-risco.md` | partial | Explicit |
| `MT-084` | STRIDE | Mitigations applied without tracking | — | `addon/09-excecoes-e-aceitacao-risco.md` | partial | Explicit |
| `MT-085` | STRIDE | Lack of an exception review cycle | — | `15-aplicacao-lifecycle.md` | partial | Explicit |
| `MT-086` | STRIDE | Arbitrary use of libraries | — | `addon/03-governanca-libs-terceiros.md` | partial | Explicit |
| `MT-087` | STRIDE | Prohibited libraries are used | — | `addon/04-integracao-ci-cd.md` | partial | Explicit |
| `MT-088` | STRIDE | Lack of a replacement policy | — | `addon/05-politica-atualizacoes.md` | partial | Explicit |
| `MT-089` | STRIDE | Introduction of an undeclared vulnerable dependency | — | SBOM boundary, dependency review | partial | Explicit |
| `MT-090` | STRIDE | Dependency confusion | — | SCA, origin validation | partial | Explicit |
| `MT-091` | STRIDE | Backdoor via a build tool | — | Tooling governance | partial | Explicit |
| `MT-092` | STRIDE | Composition drift between builds | — | CI/CD gating | partial | Explicit |

---

## § AntiPattern exposure mapping {#-antipattern-exposure-mapping}

_(No antipattern→threat relation mapped to this chapter.)_

---

## § CWE references (supporting only) {#-cwe-references-supporting-only}

_(No threat with a CWE reference for this chapter.)_

---

## § V1 overlay — mitigation pathway (where Core-mapped) {#-v1-overlay--mitigation-pathway-where-core-mapped}

V1 controls/mechanisms anchored to this chapter that mitigate the threats listed above. The V1 overlay keeps the three-way routing visible per Manual ontology V2 + AppSec Core V1 + Substrate v7.

_(The relations between anti-patterns, threats and controls are not yet complete in this version. Each entity's grounding in external sources is in the chapter's [Traceability](/sbd-toe/sbd-manual/dependencias-sbom-sca/canon/rastreabilidade) page.)_

---

## § Future-work register (threat gaps) {#-future-work-register-threat-gaps}

_(No threat in gap state for this chapter.)_
