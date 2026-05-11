# 50. Ameaças Mitigadas — Monitorização e Operações

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

Total: **25 entidades** (Threat × 15, AntiPattern × 7, Signal × 3) mapped a este capítulo.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-197` | Eventos críticos não registados | normative | heuristic |
| Threat | `MT-198` | Logs voláteis ou truncados | normative | heuristic |
| Threat | `MT-199` | Falta de rastreabilidade de execução | normative | heuristic |
| Threat | `MT-200` | Incidentes sem alerta | normative | heuristic |
| Threat | `MT-201` | Alertas ignorados por ruído | normative | heuristic |
| Threat | `MT-202` | Falta de correlação de alertas | normative | heuristic |
| Threat | `MT-203` | Incidentes sem owner definido | normative | heuristic |
| Threat | `MT-204` | Reação ad-hoc ou tardia | normative | heuristic |
| Threat | `MT-205` | Eventos sem acionamento de ação | normative | heuristic |
| Threat | `MT-206` | Ausência de métricas de postura | normative | heuristic |
| Threat | `MT-207` | Impossibilidade de priorizar riscos | normative | heuristic |
| Threat | `MT-208` | Dados sem granularidade ou visão | normative | heuristic |
| Threat | `MT-209` | Novos sistemas sem monitorização | normative | heuristic |
| Threat | `MT-210` | Equipas ignoram alertas operacionais | normative | heuristic |
| Threat | `MT-211` | Dados não usados para melhoria contínua | normative | heuristic |
| AntiPattern | `sem:antipattern:alertas-nao-acionaveis` | Alertas não acionáveis | semantic | scored |
| AntiPattern | `sem:antipattern:demasiados-alertas` | Demasiados alertas | semantic | scored |
| AntiPattern | `sem:antipattern:detecao-sem-resposta` | Deteção sem resposta | semantic | scored |
| AntiPattern | `sem:antipattern:falta-de-integracao-com-irp` | Falta de integração com IRP | semantic | scored |
| AntiPattern | `sem:antipattern:logs-incompletos-ou-ignorados` | Logs incompletos ou ignorados | semantic | scored |
| AntiPattern | `sem:antipattern:logs-nao-estruturados` | Logs não estruturados | semantic | scored |
| AntiPattern | `sem:antipattern:retencao-insuficiente` | Retenção insuficiente | semantic | scored |
| Signal | `sem:signal:falhas-de-login` | Falhas de login | semantic | scored |
| Signal | `sem:signal:logs` | Logs | semantic | scored |
| Signal | `sem:signal:metricas-mttd-mttr` | Métricas MTTD/MTTR | semantic | scored |

---

## § Threat surfaces — Manual + CAPEC primary

Threat surfaces canónicas per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (forte / parcial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-197` | STRIDE | Eventos críticos não registados | — | `addon/02-controles-logging-centralizado.md` | parcial | Explícito |
| `MT-198` | STRIDE | Logs voláteis ou truncados | — | `addon/02-controles-logging-centralizado.md` | parcial | Explícito |
| `MT-199` | STRIDE | Falta de rastreabilidade de execução | — | `addon/06-correlacao-anomalias.md` | parcial | Explícito |
| `MT-200` | STRIDE | Incidentes sem alerta | — | `addon/03-alertas-eventos-criticos.md` | parcial | Explícito |
| `MT-201` | STRIDE | Alertas ignorados por ruído | — | `addon/03-alertas-eventos-criticos.md`, `addon/07-metricas-indicadores.md` | parcial | Explícito |
| `MT-202` | STRIDE | Falta de correlação de alertas | — | `addon/06-correlacao-anomalias.md` | parcial | Explícito |
| `MT-203` | STRIDE | Incidentes sem owner definido | — | `addon/05-monitorizacao-operacoes.md` | parcial | Explícito |
| `MT-204` | STRIDE | Reação ad-hoc ou tardia | — | `addon/05-monitorizacao-operacoes.md` | parcial | Explícito |
| `MT-205` | STRIDE | Eventos sem acionamento de ação | — | `addon/05-monitorizacao-operacoes.md` | parcial | Explícito |
| `MT-206` | STRIDE | Ausência de métricas de postura | — | `addon/07-metricas-indicadores.md` | parcial | Explícito |
| `MT-207` | STRIDE | Impossibilidade de priorizar riscos | — | `addon/08-matriz-controles-por-risco.md` | parcial | Explícito |
| `MT-208` | STRIDE | Dados sem granularidade ou visão | — | `addon/07-metricas-indicadores.md` | parcial | Explícito |
| `MT-209` | STRIDE | Novos sistemas sem monitorização | — | `15-aplicacao-lifecycle.md` | parcial | Explícito |
| `MT-210` | STRIDE | Equipas ignoram alertas operacionais | — | `addon/05-monitorizacao-operacoes.md` | parcial | Explícito |
| `MT-211` | STRIDE | Dados não usados para melhoria contínua | — | `addon/07-metricas-indicadores.md`, `20-checklist-revisao.md` | parcial | Explícito |

---

## § AntiPattern exposure mapping

AntiPattern → Threat exposure relations per Manual ontology V2 `antipattern_threat_links.jsonl`. Cada link indica que o antipattern (quando presente em código/processo) expõe a ameaça.

| AntiPattern | Exposes threat | Confidence | Justification |
|---|---|---|---|
| `alertas-nao-acionaveis` | `MT-200` | 0.70 | alias_match, bundle_grounding, risk_match |

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
