# 50. Ameaças Mitigadas — Testes de Segurança

## Sumário

Famílias de ameaça mitigadas neste capítulo + força da mitigação. Análise segue **§26 canon §4 discipline**: Manual surface + CAPEC primary; CWE supporting limited; mitigation strength explicitly labelled.

Seis secções:

- **§ Manual ontology V2 entities** — Threat + AntiPattern + Signal canonical
- **§ Threat surfaces** — Manual + CAPEC primary surfaces
- **§ AntiPattern exposure mapping** — antipattern → threat exposure relations
- **§ CWE references** — supporting only (per §26 §4 discipline)
- **§ V1 overlay** — mitigation pathway where Core-mapped
- **§ Future-work register** — threat gaps registered para P8 §10

---

## § Manual ontology V2 — entities canónicas (threats + antipatterns + signals)

Total: **15 entidades** (Threat × 15, AntiPattern × 0, Signal × 0) mapped a este capítulo.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-167` | Injeções (SQLi, OS Command, etc.) | normative | heuristic |
| Threat | `MT-168` | Falhas de controlo de acesso | normative | heuristic |
| Threat | `MT-169` | Lógicas de negócio exploráveis | normative | heuristic |
| Threat | `MT-170` | Regressão de segurança | normative | heuristic |
| Threat | `MT-171` | Baixa cobertura dos testes | normative | heuristic |
| Threat | `MT-172` | Falhas conhecidas não testadas | normative | heuristic |
| Threat | `MT-173` | Falhas detetadas mas não resolvidas | normative | heuristic |
| Threat | `MT-174` | Equipa sem feedback técnico | normative | heuristic |
| Threat | `MT-175` | Validações não repetíveis | normative | heuristic |
| Threat | `MT-176` | Testes manuais não escaláveis | normative | heuristic |
| Threat | `MT-177` | Falta de testes antes de go-live | normative | heuristic |
| Threat | `MT-178` | Decisão de qualidade feita sem base | normative | heuristic |
| Threat | `MT-179` | Classes novas não detetadas por SAST/DAST | normative | heuristic |
| Threat | `MT-180` | Testes superficiais sem contexto técnico | normative | heuristic |
| Threat | `MT-181` | Ferramentas não calibradas por contexto | normative | heuristic |

---

## § Threat surfaces — Manual + CAPEC primary

Threat surfaces canónicas per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (forte / parcial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-167` | STRIDE | Injeções (SQLi, OS Command, etc.) | — | `addon/01-sast.md`, `addon/02-dast.md` | parcial | Explícito |
| `MT-168` | STRIDE | Falhas de controlo de acesso | — | `addon/02-dast.md`, `addon/03-iast.md` | parcial | Explícito |
| `MT-169` | STRIDE | Lógicas de negócio exploráveis | — | `addon/04-fuzzing.md`, `addon/11-pen-testing.md` | parcial | Explícito |
| `MT-170` | STRIDE | Regressão de segurança | — | `addon/05-validacao-regressao.md` | parcial | Explícito |
| `MT-171` | STRIDE | Baixa cobertura dos testes | — | `addon/06-cobertura-e-priorizacao.md` | parcial | Explícito |
| `MT-172` | STRIDE | Falhas conhecidas não testadas | — | `addon/08-gestao-findings.md`, `addon/09-feedback-equipa.md` | parcial | Explícito |
| `MT-173` | STRIDE | Falhas detetadas mas não resolvidas | — | `addon/08-gestao-findings.md` | parcial | Explícito |
| `MT-174` | STRIDE | Equipa sem feedback técnico | — | `addon/09-feedback-equipa.md` | parcial | Explícito |
| `MT-175` | STRIDE | Validações não repetíveis | — | `addon/00-estrategia-testes.md`, `addon/07-integracao-pipeline.md` | parcial | Explícito |
| `MT-176` | STRIDE | Testes manuais não escaláveis | — | `addon/07-integracao-pipeline.md` | parcial | Explícito |
| `MT-177` | STRIDE | Falta de testes antes de go-live | — | `20-checklist-revisao.md` | parcial | Explícito |
| `MT-178` | STRIDE | Decisão de qualidade feita sem base | — | `addon/06-cobertura-e-priorizacao.md` | parcial | Explícito |
| `MT-179` | STRIDE | Classes novas não detetadas por SAST/DAST | — | `addon/11-pen-testing.md` | parcial | Explícito |
| `MT-180` | STRIDE | Testes superficiais sem contexto técnico | — | `addon/00-estrategia-testes.md` | parcial | Explícito |
| `MT-181` | STRIDE | Ferramentas não calibradas por contexto | — | `addon/00-estrategia-testes.md`, `addon/09-feedback-equipa.md` | parcial | Explícito |

---

## § AntiPattern exposure mapping

_(Nenhuma antipattern→threat relation mapped a este capítulo.)_

---

## § CWE references (supporting only)

_(Nenhuma threat com CWE reference para este capítulo.)_

---

## § V1 overlay — mitigation pathway (where Core-mapped)

V1 controls/mechanisms anchored a este capítulo que mitigam threats listed above. V1 overlay preserva three-way routing visible per Manual ontology V2 + AppSec Core V1 + Substrate v7.

_(V1 overlay surfacing per Manual ontology V2 antipattern_exposes_threat / control_mitigates_threat relations não totalmente extracted em este KG state; deferred a Codex post-Run-2 delta evaluation. Consult `25-rastreabilidade.md` for V1 entity → ES grounding per chapter; mitigation pathway inferable from existing Iter 4 + Run 1 layered output.)_

---

## § Future-work register (threat gaps)

_(Nenhum threat em gap state para este capítulo.)_

---

## Generation provenance

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
