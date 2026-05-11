# 50. Ameaças Mitigadas — Governança e Contratação

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

Total: **23 entidades** (Threat × 12, AntiPattern × 2, Signal × 9) mapped a este capítulo.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-222` | Adoção de fornecedor sem avaliação | normative | heuristic |
| Threat | `MT-223` | Falta de cláusulas contratuais | normative | heuristic |
| Threat | `MT-224` | Uso de serviços sem rastreio | normative | heuristic |
| Threat | `MT-225` | Iniciativas paralelas sem coordenação | normative | heuristic |
| Threat | `MT-226` | Falta de continuidade organizacional | normative | heuristic |
| Threat | `MT-227` | Risco de decisões legadas sem controlo | normative | heuristic |
| Threat | `MT-228` | Decisões não revistas com mudança de contexto | normative | heuristic |
| Threat | `MT-229` | Falta de governança em decisões históricas | normative | heuristic |
| Threat | `MT-230` | Falta de conhecimento sobre o estado de segurança | normative | heuristic |
| Threat | `MT-231` | Estratégia de segurança desarticulada | normative | heuristic |
| Threat | `MT-232` | Segurança definida mas não aplicada | normative | heuristic |
| Threat | `MT-233` | Políticas de segurança não institucionalizadas | normative | heuristic |
| AntiPattern | `sem:antipattern:confianca-exclusiva-em-mecanismos-tecnicos-automatizados` | confiança exclusiva em mecanismos técnicos automatizados | semantic | scored |
| AntiPattern | `sem:antipattern:limitacao-do-sbd-toe-a-pratica-tecnica-local` | limitação do SbD-ToE à prática técnica local | semantic | scored |
| Signal | `sem:signal:clausulas-contratuais-rastreadas` | Cláusulas contratuais rastreadas | semantic | scored |
| Signal | `sem:signal:excecoes-as-praticas-prescritas` | exceções às práticas prescritas | semantic | scored |
| Signal | `sem:signal:excecoes-registadas-e-aprovadas` | Exceções registadas e aprovadas | semantic | scored |
| Signal | `sem:signal:kpis-consolidados` | KPIs consolidados | semantic | scored |
| Signal | `sem:signal:kpis-de-governacao` | KPIs de governação | semantic | scored |
| Signal | `sem:signal:ligacao-explicita-a-frameworks-normativos` | Ligação explícita a frameworks normativos | semantic | scored |
| Signal | `sem:signal:registo-e-aprovacao-de-excecoes` | registo e aprovação de exceções | semantic | scored |
| Signal | `sem:signal:reporting-periodico-a-gestao` | reporting periódico à gestão | semantic | scored |
| Signal | `sem:signal:validacao-continua-de-fornecedores` | validação contínua de fornecedores | semantic | scored |

---

## § Threat surfaces — Manual + CAPEC primary

Threat surfaces canónicas per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (forte / parcial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-222` | STRIDE | Adoção de fornecedor sem avaliação | — | `addon/03-modelo-validacao-fornecedores.md` | parcial | Explícito |
| `MT-223` | STRIDE | Falta de cláusulas contratuais | — | `addon/02-clausulas-contratuais.md` | parcial | Explícito |
| `MT-224` | STRIDE | Uso de serviços sem rastreio | — | `addon/04-rastreabilidade-organizacional.md` | parcial | Explícito |
| `MT-225` | STRIDE | Iniciativas paralelas sem coordenação | — | `addon/01-modelo-governancao.md` | parcial | Explícito |
| `MT-226` | STRIDE | Falta de continuidade organizacional | — | `addon/07-governancao-e-maturidade.md` | parcial | Explícito |
| `MT-227` | STRIDE | Risco de decisões legadas sem controlo | — | `addon/10-governanca-legada.md` | parcial | Explícito |
| `MT-228` | STRIDE | Decisões não revistas com mudança de contexto | — | `addon/06-validacao-continuada.md` | parcial | Explícito |
| `MT-229` | STRIDE | Falta de governança em decisões históricas | — | `addon/04`, `addon/06` | parcial | Explícito |
| `MT-230` | STRIDE | Falta de conhecimento sobre o estado de segurança | — | `addon/07-governancao-e-maturidade.md` | parcial | Explícito |
| `MT-231` | STRIDE | Estratégia de segurança desarticulada | — | `30`, `90` | parcial | Explícito |
| `MT-232` | STRIDE | Segurança definida mas não aplicada | — | `addon/01`, `addon/05`, `addon/06` + 1 more | forte | Explícito |
| `MT-233` | STRIDE | Políticas de segurança não institucionalizadas | — | `60-politicas-recomendadas.md` | parcial | Explícito |

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
