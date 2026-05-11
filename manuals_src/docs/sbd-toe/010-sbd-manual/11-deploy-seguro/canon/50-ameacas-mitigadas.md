# 50. Ameaças Mitigadas — Deploy Seguro

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
| Threat | `MT-182` | Código em produção sem validação | normative | heuristic |
| Threat | `MT-183` | Ativação funcional sem controlo | normative | heuristic |
| Threat | `MT-184` | Promoção manual fora do CI/CD | normative | heuristic |
| Threat | `MT-185` | Deploy falhado sem rollback | normative | heuristic |
| Threat | `MT-186` | Feature irreversível | normative | heuristic |
| Threat | `MT-187` | Falha sem reação | normative | heuristic |
| Threat | `MT-188` | Release conjunta sem segmentação | normative | heuristic |
| Threat | `MT-189` | Feature exposta a todos os utilizadores | normative | heuristic |
| Threat | `MT-190` | Falta de validação operacional | normative | heuristic |
| Threat | `MT-191` | Falhas pós-deploy não detetadas | normative | heuristic |
| Threat | `MT-192` | Reação tardia a problemas críticos | normative | heuristic |
| Threat | `MT-193` | Eventos críticos ignorados | normative | heuristic |
| Threat | `MT-194` | Toggle ativado inadvertidamente | normative | heuristic |
| Threat | `MT-195` | Release sem segmentação geográfica ou lógica | normative | heuristic |
| Threat | `MT-196` | Execução de função crítica não validada | normative | heuristic |

---

## § Threat surfaces — Manual + CAPEC primary

Threat surfaces canónicas per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (forte / parcial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-182` | STRIDE | Código em produção sem validação | — | `addon/04-validacoes-pre-deploy.md` | parcial | Explícito |
| `MT-183` | STRIDE | Ativação funcional sem controlo | — | `addon/03-feature-flags-e-toggle.md` | parcial | Explícito |
| `MT-184` | STRIDE | Promoção manual fora do CI/CD | — | `addon/01-modelo-controle-execucao.md` | parcial | Explícito |
| `MT-185` | STRIDE | Deploy falhado sem rollback | — | `addon/06-controle-versao-e-rollback.md` | parcial | Explícito |
| `MT-186` | STRIDE | Feature irreversível | — | `addon/03-feature-flags-e-toggle.md` | parcial | Explícito |
| `MT-187` | STRIDE | Falha sem reação | — | `addon/05-monitorizacao-e-reacao.md` | parcial | Explícito |
| `MT-188` | STRIDE | Release conjunta sem segmentação | — | `addon/02-praticas-release-management.md` | parcial | Explícito |
| `MT-189` | STRIDE | Feature exposta a todos os utilizadores | — | `addon/03-feature-flags-e-toggle.md` | parcial | Explícito |
| `MT-190` | STRIDE | Falta de validação operacional | — | `addon/08-segregacao-e-validacao-operacional.md` | parcial | Explícito |
| `MT-191` | STRIDE | Falhas pós-deploy não detetadas | — | `addon/05-monitorizacao-e-reacao.md` | parcial | Explícito |
| `MT-192` | STRIDE | Reação tardia a problemas críticos | — | `addon/05-monitorizacao-e-reacao.md` | parcial | Explícito |
| `MT-193` | STRIDE | Eventos críticos ignorados | — | `addon/06-controle-versao-e-rollback.md` | parcial | Explícito |
| `MT-194` | STRIDE | Toggle ativado inadvertidamente | — | `addon/03-feature-flags-e-toggle.md` | parcial | Explícito |
| `MT-195` | STRIDE | Release sem segmentação geográfica ou lógica | — | `addon/07-deploy-progressivo-e-risco.md` | parcial | Explícito |
| `MT-196` | STRIDE | Execução de função crítica não validada | — | `addon/08-segregacao-e-validacao-operacional.md` | parcial | Explícito |

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
