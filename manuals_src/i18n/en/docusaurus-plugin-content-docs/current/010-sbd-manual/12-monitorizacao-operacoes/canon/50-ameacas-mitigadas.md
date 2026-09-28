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
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/canon/50-ameacas-mitigadas.md
  source_sha256: 229f5fef46d98870549111f2e30cfb9f6ab489ae9325d4bf88d1ae4afe71f77b
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: f4d7614cfd7a1de89446d9089f20460040f4a5ed86efcf64e81f9fcdd00c1a14
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [appsec_core, chapter_role, practitioner_manual, threat, traceability]
  glossary_sha256: ee9254db342fbd435a6a08ff5fdf55af403af8d5e22e5fc3dea01aa8913d64d7
  translated_at: 2026-09-28T09:12:20Z
  stamped_at: 2026-09-28T09:12:20Z
  reviewed_by: null
---

# 50. Mitigated Threats — Monitoring and Operations

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

Total: **25 entities** (Threat × 15, AntiPattern × 7, Signal × 3) mapped to this chapter.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-197` | Critical events not recorded | normative | heuristic |
| Threat | `MT-198` | Volatile or truncated logs | normative | heuristic |
| Threat | `MT-199` | Lack of execution traceability | normative | heuristic |
| Threat | `MT-200` | Incidents without an alert | normative | heuristic |
| Threat | `MT-201` | Alerts ignored due to noise | normative | heuristic |
| Threat | `MT-202` | Lack of alert correlation | normative | heuristic |
| Threat | `MT-203` | Incidents without a defined owner | normative | heuristic |
| Threat | `MT-204` | Ad-hoc or late reaction | normative | heuristic |
| Threat | `MT-205` | Events without action triggered | normative | heuristic |
| Threat | `MT-206` | Absence of posture metrics | normative | heuristic |
| Threat | `MT-207` | Inability to prioritise risks | normative | heuristic |
| Threat | `MT-208` | Data without granularity or overview | normative | heuristic |
| Threat | `MT-209` | New systems without monitoring | normative | heuristic |
| Threat | `MT-210` | Teams ignore operational alerts | normative | heuristic |
| Threat | `MT-211` | Data not used for continuous improvement | normative | heuristic |
| AntiPattern | `sem:antipattern:alertas-nao-acionaveis` | Non-actionable alerts | semantic | scored |
| AntiPattern | `sem:antipattern:demasiados-alertas` | Too many alerts | semantic | scored |
| AntiPattern | `sem:antipattern:detecao-sem-resposta` | Detection without response | semantic | scored |
| AntiPattern | `sem:antipattern:falta-de-integracao-com-irp` | Lack of integration with IRP | semantic | scored |
| AntiPattern | `sem:antipattern:logs-incompletos-ou-ignorados` | Incomplete or ignored logs | semantic | scored |
| AntiPattern | `sem:antipattern:logs-nao-estruturados` | Unstructured logs | semantic | scored |
| AntiPattern | `sem:antipattern:retencao-insuficiente` | Insufficient retention | semantic | scored |
| Signal | `sem:signal:falhas-de-login` | Login failures | semantic | scored |
| Signal | `sem:signal:logs` | Logs | semantic | scored |
| Signal | `sem:signal:metricas-mttd-mttr` | MTTD/MTTR metrics | semantic | scored |

---

## § Threat surfaces — Manual + CAPEC primary {#-threat-surfaces--manual--capec-primary}

Canonical threat surfaces per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (strong / partial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-197` | STRIDE | Critical events not recorded | — | `addon/02-controles-logging-centralizado.md` | partial | Explicit |
| `MT-198` | STRIDE | Volatile or truncated logs | — | `addon/02-controles-logging-centralizado.md` | partial | Explicit |
| `MT-199` | STRIDE | Lack of execution traceability | — | `addon/06-correlacao-anomalias.md` | partial | Explicit |
| `MT-200` | STRIDE | Incidents without an alert | — | `addon/03-alertas-eventos-criticos.md` | partial | Explicit |
| `MT-201` | STRIDE | Alerts ignored due to noise | — | `addon/03-alertas-eventos-criticos.md`, `addon/07-metricas-indicadores.md` | partial | Explicit |
| `MT-202` | STRIDE | Lack of alert correlation | — | `addon/06-correlacao-anomalias.md` | partial | Explicit |
| `MT-203` | STRIDE | Incidents without a defined owner | — | `addon/05-monitorizacao-operacoes.md` | partial | Explicit |
| `MT-204` | STRIDE | Ad-hoc or late reaction | — | `addon/05-monitorizacao-operacoes.md` | partial | Explicit |
| `MT-205` | STRIDE | Events without action triggered | — | `addon/05-monitorizacao-operacoes.md` | partial | Explicit |
| `MT-206` | STRIDE | Absence of posture metrics | — | `addon/07-metricas-indicadores.md` | partial | Explicit |
| `MT-207` | STRIDE | Inability to prioritise risks | — | `addon/08-matriz-controles-por-risco.md` | partial | Explicit |
| `MT-208` | STRIDE | Data without granularity or overview | — | `addon/07-metricas-indicadores.md` | partial | Explicit |
| `MT-209` | STRIDE | New systems without monitoring | — | `15-aplicacao-lifecycle.md` | partial | Explicit |
| `MT-210` | STRIDE | Teams ignore operational alerts | — | `addon/05-monitorizacao-operacoes.md` | partial | Explicit |
| `MT-211` | STRIDE | Data not used for continuous improvement | — | `addon/07-metricas-indicadores.md`, `20-checklist-revisao.md` | partial | Explicit |

---

## § AntiPattern exposure mapping {#-antipattern-exposure-mapping}

AntiPattern → Threat exposure relations per Manual ontology V2 `antipattern_threat_links.jsonl`. Each link indicates that the antipattern (when present in code/process) exposes the threat.

| AntiPattern | Exposes threat | Confidence | Justification |
|---|---|---|---|
| `alertas-nao-acionaveis` | `MT-200` | 0.70 | alias_match, bundle_grounding, risk_match |

---

## § CWE references (supporting only) {#-cwe-references-supporting-only}

_(No threat with a CWE reference for this chapter.)_

---

## § V1 overlay — mitigation pathway (where Core-mapped) {#-v1-overlay--mitigation-pathway-where-core-mapped}

V1 controls/mechanisms anchored to this chapter that mitigate the threats listed above. The V1 overlay keeps the three-way routing visible per Manual ontology V2 + AppSec Core V1 + Substrate v7.

_(The relations between anti-patterns, threats and controls are not yet complete in this version. Each entity's grounding in external sources is in the chapter's [Traceability](/sbd-toe/sbd-manual/monitorizacao-operacoes/canon/rastreabilidade) page.)_

---

## § Future-work register (threat gaps) {#-future-work-register-threat-gaps}

_(No threat in gap state for this chapter.)_
