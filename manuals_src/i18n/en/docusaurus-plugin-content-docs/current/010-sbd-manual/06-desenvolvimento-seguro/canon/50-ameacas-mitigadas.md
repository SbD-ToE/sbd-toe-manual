---
id: ameacas-mitigadas
translation:
  source_locale: pt
  source_path: 010-sbd-manual/06-desenvolvimento-seguro/canon/50-ameacas-mitigadas.md
  source_sha256: e91c72b3cbe5b5eeec3626c2d1fcd6749a2beaf1008ec35b57e90e504f73c374
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 1f536982b02158f88c66752cb37d246070d9b10fa7743ef0cd53f17388377349
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [appsec_core, chapter_role, practitioner_manual, sbdtoe_sbd, threat, traceability, validation_evaluation]
  glossary_sha256: 85dcb385cdb433b184f5cb947a9fa418dc4a7114756f45b37e36065438f2741d
  translated_at: 2026-09-26T08:57:17Z
  reviewed_by: null
---

# 50. Mitigated Threats — Secure Development

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
| Threat | `MT-093` | Inclusion of insecure patterns out of habit | normative | heuristic |
| Threat | `MT-094` | Use of deprecated or dangerous functions | normative | heuristic |
| Threat | `MT-095` | Code injection without adequate escaping | normative | heuristic |
| Threat | `MT-096` | Insecure code without detection | normative | heuristic |
| Threat | `MT-097` | Absence of traceability between issues and decisions | normative | heuristic |
| Threat | `MT-098` | Only reactive validation (e.g. QA tests) | normative | heuristic |
| Threat | `MT-099` | Security removed due to “incompatibility” | normative | heuristic |
| Threat | `MT-100` | Exceptions not reviewed or revalidated | normative | heuristic |
| Threat | `MT-101` | Untracked deviations between guideline and practice | normative | heuristic |
| Threat | `MT-102` | Generation of insecure code via AI | normative | heuristic |
| Threat | `MT-103` | Inclusion of known vulnerabilities | normative | heuristic |
| Threat | `MT-104` | Lack of accountability for generated code | normative | heuristic |
| Threat | `MT-105` | Inclusion of discontinued libraries | normative | heuristic |
| Threat | `MT-106` | Lack of justification for the use of an insecure dependency | normative | heuristic |
| Threat | `MT-107` | Vulnerable component kept in the final build | normative | heuristic |
| Threat | `MT-108` | Inconsistency across teams and projects | normative | heuristic |
| Threat | `MT-109` | Absence of a security baseline | normative | heuristic |
| Threat | `MT-110` | Weak accountability for code security | normative | heuristic |

---

## § Threat surfaces — Manual + CAPEC primary {#-threat-surfaces--manual--capec-primary}

Canonical threat surfaces per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (strong / partial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-093` | STRIDE | Inclusion of insecure patterns out of habit | — | `addon/02-linters-validacoes.md` | partial | Explicit |
| `MT-094` | STRIDE | Use of deprecated or dangerous functions | — | `addon/01-boas-praticas-codigo.md` | partial | Explicit |
| `MT-095` | STRIDE | Code injection without adequate escaping | — | `addon/08-validacoes-codigo.md` | partial | Explicit |
| `MT-096` | STRIDE | Insecure code without detection | — | `addon/08-validacoes-codigo.md` | partial | Explicit |
| `MT-097` | STRIDE | Absence of traceability between issues and decisions | — | `addon/09-anotacoes-evidencia.md` | partial | Explicit |
| `MT-098` | STRIDE | Only reactive validation (e.g. QA tests) | — | `addon/08-validacoes-codigo.md` | partial | Explicit |
| `MT-099` | STRIDE | Security removed due to “incompatibility” | — | `addon/05-excecoes-e-justificacoes.md` | partial | Explicit |
| `MT-100` | STRIDE | Exceptions not reviewed or revalidated | — | `15-aplicacao-lifecycle.md` | partial | Explicit |
| `MT-101` | STRIDE | Untracked deviations between guideline and practice | — | `addon/07-guidelines-equipa.md` | partial | Explicit |
| `MT-102` | STRIDE | Generation of insecure code via AI | — | `addon/10-genia-e-seguranca.md` | partial | Explicit |
| `MT-103` | STRIDE | Inclusion of known vulnerabilities | — | `addon/10-genia-e-seguranca.md` | partial | Explicit |
| `MT-104` | STRIDE | Lack of accountability for generated code | — | `addon/09-anotacoes-evidencia.md` | partial | Explicit |
| `MT-105` | STRIDE | Inclusion of discontinued libraries | — | `addon/03-seguranca-dependencias.md` | partial | Explicit |
| `MT-106` | STRIDE | Lack of justification for the use of an insecure dependency | — | `addon/05-excecoes-e-justificacoes.md` | partial | Explicit |
| `MT-107` | STRIDE | Vulnerable component kept in the final build | — | `addon/08-validacoes-codigo.md` | partial | Explicit |
| `MT-108` | STRIDE | Inconsistency across teams and projects | — | `addon/07-guidelines-equipa.md` | partial | Explicit |
| `MT-109` | STRIDE | Absence of a security baseline | — | `addon/01-boas-praticas-codigo.md` | partial | Explicit |
| `MT-110` | STRIDE | Weak accountability for code security | — | `addon/09-anotacoes-evidencia.md` | partial | Explicit |

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
