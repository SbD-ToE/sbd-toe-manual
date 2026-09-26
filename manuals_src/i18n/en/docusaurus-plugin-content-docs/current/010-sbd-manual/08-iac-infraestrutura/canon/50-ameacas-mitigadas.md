---
id: ameacas-mitigadas
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/canon/50-ameacas-mitigadas.md
  source_sha256: ae04e91497b31db7e4c3c389b80c45eeab8c48bd44d6ced6fdda4e6134342303
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 97e6504bbcc8c3319968aac418e944dddd0ee5cdafbdb699c1afdf39f6739353
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [appsec_core, chapter_role, cycle_iteration, lifecycle_phase, practitioner_manual, sbdtoe_sbd, threat, validation_evaluation]
  glossary_sha256: 5a04226a675e95805042c589c14e80029ea0fd1d635a0791f8a1a1a02b87bc71
  translated_at: 2026-09-26T09:25:43Z
  reviewed_by: null
---

# 50. Mitigated Threats — IaC and Infrastructure

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

Total: **28 entities** (Threat × 17, AntiPattern × 6, Signal × 5) mapped to this chapter.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-132` | Insecure or permissive defaults | normative | heuristic |
| Threat | `MT-133` | Configurations without validation | normative | heuristic |
| Threat | `MT-134` | Critical fields left blank or default | normative | heuristic |
| Threat | `MT-135` | Inconsistent environments between executions | normative | heuristic |
| Threat | `MT-136` | Use of insecure or unvalidated modules | normative | heuristic |
| Threat | `MT-137` | Hardcoding of critical parameters | normative | heuristic |
| Threat | `MT-138` | Insecure environments provisioned by mistake | normative | heuristic |
| Threat | `MT-139` | Provisioning with excessive permissions | normative | heuristic |
| Threat | `MT-140` | Lack of data classification tags | normative | heuristic |
| Threat | `MT-141` | Use of real data in test environments | normative | heuristic |
| Threat | `MT-142` | Hardcoded or poorly managed secrets | normative | heuristic |
| Threat | `MT-143` | Changes applied without review | normative | heuristic |
| Threat | `MT-144` | Lack of owner and accountability | normative | heuristic |
| Threat | `MT-145` | Reuse of modules without tracking | normative | heuristic |
| Threat | `MT-146` | Application of insecure changes through bypass | normative | heuristic |
| Threat | `MT-147` | Informal or non-existent justifications | normative | heuristic |
| Threat | `MT-148` | Environments provisioned with accumulated exceptions | normative | heuristic |
| AntiPattern | `sem:antipattern:ambientes-mal-segregados` | Poorly segregated environments | semantic | scored |
| AntiPattern | `sem:antipattern:confianca-na-experiencia-individual-sem-automacao` | Reliance on individual experience without automation | semantic | scored |
| AntiPattern | `sem:antipattern:erros-de-configuracao` | Configuration errors | semantic | scored |
| AntiPattern | `sem:antipattern:ignorar-momentos-criticos-no-ciclo-de-vida-do-iac` | Ignoring critical moments in the IaC lifecycle | semantic | scored |
| AntiPattern | `sem:antipattern:permissoes-excessivas` | Excessive permissions | semantic | scored |
| AntiPattern | `sem:antipattern:uso-de-modulos-maliciosos` | Use of malicious modules | semantic | scored |
| Signal | `sem:signal:catalogo-de-modulos-certificados` | Catalogue of certified modules | semantic | scored |
| Signal | `sem:signal:dashboards-de-validacao` | Validation dashboards | semantic | scored |
| Signal | `sem:signal:gestao-centralizada-de-excecoes` | Centralised management of exceptions | semantic | scored |
| Signal | `sem:signal:pipelines-ci-cd-obrigatorios` | Mandatory CI/CD pipelines | semantic | scored |
| Signal | `sem:signal:uso-de-ferramentas-de-scanning` | Use of scanning tools | semantic | scored |

---

## § Threat surfaces — Manual + CAPEC primary {#-threat-surfaces--manual--capec-primary}

Canonical threat surfaces per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (strong / partial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-132` | STRIDE | Insecure or permissive defaults | — | `addon/02-validacoes-e-checks.md` | partial | Explicit |
| `MT-133` | STRIDE | Configurations without validation | — | `addon/06-controle-enforcement.md` | partial | Explicit |
| `MT-134` | STRIDE | Critical fields left blank or default | — | `addon/07-rastreabilidade-e-tags.md` | partial | Explicit |
| `MT-135` | STRIDE | Inconsistent environments between executions | — | `addon/06`, `addon/30-recomendacoes-avancadas` | partial | Explicit |
| `MT-136` | STRIDE | Use of insecure or unvalidated modules | — | `addon/03-governanca-modulos.md` | partial | Explicit |
| `MT-137` | STRIDE | Hardcoding of critical parameters | — | `addon/02-validacoes-e-checks.md` | partial | Explicit |
| `MT-138` | STRIDE | Insecure environments provisioned by mistake | — | `addon/01-planeamento-e-controle.md` | partial | Explicit |
| `MT-139` | STRIDE | Provisioning with excessive permissions | — | `addon/04-principios-sbd-iac.md` | partial | Explicit |
| `MT-140` | STRIDE | Lack of data classification tags | — | `addon/07-rastreabilidade-e-tags.md` | partial | Explicit |
| `MT-141` | STRIDE | Use of real data in test environments | — | `addon/01-planeamento-e-controle.md` | partial | Explicit |
| `MT-142` | STRIDE | Hardcoded or poorly managed secrets | — | `addon/06-controle-enforcement.md` | partial | Explicit |
| `MT-143` | STRIDE | Changes applied without review | — | `addon/01-planeamento-e-controle.md` | partial | Explicit |
| `MT-144` | STRIDE | Lack of owner and accountability | — | `addon/07-rastreabilidade-e-tags.md` | partial | Explicit |
| `MT-145` | STRIDE | Reuse of modules without tracking | — | `addon/03-governanca-modulos.md` | partial | Explicit |
| `MT-146` | STRIDE | Application of insecure changes through bypass | — | `addon/06-controle-enforcement.md` | partial | Explicit |
| `MT-147` | STRIDE | Informal or non-existent justifications | — | `addon/09-gestao-excecoes.md` | partial | Explicit |
| `MT-148` | STRIDE | Environments provisioned with accumulated exceptions | — | `15-aplicacao-lifecycle.md` | partial | Explicit |

---

## § AntiPattern exposure mapping {#-antipattern-exposure-mapping}

AntiPattern → Threat exposure relations per Manual ontology V2 `antipattern_threat_links.jsonl`. Each link indicates that the antipattern (when present in code/process) exposes the threat.

| AntiPattern | Exposes threat | Confidence | Justification |
|---|---|---|---|
| `permissoes-excessivas` | `MT-139` | 0.76 | alias_match, bundle_grounding, threat_label_match |

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
