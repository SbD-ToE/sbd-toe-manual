# 50. Ameaças Mitigadas — Classificação de Aplicações

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

Total: **22 entidades** (Threat × 20, AntiPattern × 1, Signal × 1) mapped a este capítulo.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-001` | Falta de aplicação de controlos mínimos | normative | heuristic |
| Threat | `MT-002` | Overengineering e fricção excessiva | normative | heuristic |
| Threat | `MT-003` | Inconsistência entre projetos com mesmo risco | normative | heuristic |
| Threat | `MT-004` | Segurança opcional em produtos low-risk | normative | heuristic |
| Threat | `MT-005` | Mudanças críticas sem reclassificação | normative | heuristic |
| Threat | `MT-006` | Integração com APIs ou terceiros ignorada | normative | heuristic |
| Threat | `MT-007` | Deploy com risco alterado não revisto | normative | heuristic |
| Threat | `MT-008` | Versões diferentes com classificações divergentes | normative | heuristic |
| Threat | `MT-009` | Aceitação informal de riscos críticos | normative | heuristic |
| Threat | `MT-010` | Impossibilidade de auditoria posterior | normative | heuristic |
| Threat | `MT-011` | Risco aceite por responsáveis inapropriados | normative | heuristic |
| Threat | `MT-012` | Falta de explicabilidade regulatória | normative | heuristic |
| Threat | `MT-013` | Interfaces expostas mal avaliadas | normative | heuristic |
| Threat | `MT-014` | Dados sensíveis não reconhecidos | normative | heuristic |
| Threat | `MT-015` | Assunção de ambientes seguros por defeito | normative | heuristic |
| Threat | `MT-016` | Ignorar dependências críticas | normative | heuristic |
| Threat | `MT-017` | Risco residual nunca revisto | normative | heuristic |
| Threat | `MT-018` | Falta de eventos de reavaliação planeados | normative | heuristic |
| Threat | `MT-019` | Reclassificação dependente de exceções | normative | heuristic |
| Threat | `MT-020` | Decisões de risco sem feedback do negócio | normative | heuristic |
| AntiPattern | `sem:antipattern:aceitacao-de-risco-invalida` | aceitação de risco inválida | semantic | scored |
| Signal | `sem:signal:alteracao-na-exposicao-dados-impacto-ou-forma-de-decisoes-e-validacoes` | alteração na exposição, dados, impacto ou forma de decisões e validações | semantic | scored |

---

## § Threat surfaces — Manual + CAPEC primary

Threat surfaces canónicas per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (forte / parcial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-001` | STRIDE | Falta de aplicação de controlos mínimos | — | `addon/matriz-controlos-por-risco.md` | parcial | Explícito |
| `MT-002` | STRIDE | Overengineering e fricção excessiva | — | `addon/modelo-classificacao-eixos.md` | parcial | Explícito |
| `MT-003` | STRIDE | Inconsistência entre projetos com mesmo risco | — | `addon/matriz-controlos-por-risco.md` | parcial | Explícito |
| `MT-004` | STRIDE | Segurança opcional em produtos low-risk | — | `addon/modelo-classificacao-eixos.md` | parcial | Explícito |
| `MT-005` | STRIDE | Mudanças críticas sem reclassificação | — | `addon/ciclo-vida-risco.md`, `15-aplicacao-lifecycle.md` | parcial | Explícito |
| `MT-006` | STRIDE | Integração com APIs ou terceiros ignorada | — | `addon/adopcao-drp-bia.md` | parcial | Explícito |
| `MT-007` | STRIDE | Deploy com risco alterado não revisto | — | `checklist-revisao.md` | parcial | Explícito |
| `MT-008` | STRIDE | Versões diferentes com classificações divergentes | — | `addon/risco-residual.md` | parcial | Explícito |
| `MT-009` | STRIDE | Aceitação informal de riscos críticos | — | `addon/criterios-aceitacao-risco.md` | parcial | Explícito |
| `MT-010` | STRIDE | Impossibilidade de auditoria posterior | — | `addon/risco-residual.md` | parcial | Explícito |
| `MT-011` | STRIDE | Risco aceite por responsáveis inapropriados | — | `addon/criterios-aceitacao-risco.md` | parcial | Explícito |
| `MT-012` | STRIDE | Falta de explicabilidade regulatória | — | `addon/modelo-classificacao-eixos.md` | parcial | Explícito |
| `MT-013` | STRIDE | Interfaces expostas mal avaliadas | — | `addon/01-modelo-classificacao-eixos.md` | parcial | Explícito |
| `MT-014` | STRIDE | Dados sensíveis não reconhecidos | — | `addon/08-mapeamento-ameacas-risco.md` | parcial | Explícito |
| `MT-015` | STRIDE | Assunção de ambientes seguros por defeito | — | `addon/03-adopcao-drp-bia.md` | parcial | Explícito |
| `MT-016` | STRIDE | Ignorar dependências críticas | — | `addon/08-mapeamento-ameacas-risco.md` | parcial | Explícito |
| `MT-017` | STRIDE | Risco residual nunca revisto | — | `addon/06-risco-residual.md` | parcial | Explícito |
| `MT-018` | STRIDE | Falta de eventos de reavaliação planeados | — | `addon/07-ciclo-vida-risco.md` | parcial | Explícito |
| `MT-019` | STRIDE | Reclassificação dependente de exceções | — | `20-checklist-revisao.md` | parcial | Explícito |
| `MT-020` | STRIDE | Decisões de risco sem feedback do negócio | — | `addon/09-criterios-aceitacao-risco.md` | parcial | Explícito |

---

## § AntiPattern exposure mapping

AntiPattern → Threat exposure relations per Manual ontology V2 `antipattern_threat_links.jsonl`. Cada link indica que o antipattern (quando presente em código/processo) expõe a ameaça.

| AntiPattern | Exposes threat | Confidence | Justification |
|---|---|---|---|
| `aceitacao-de-risco-invalida` | `MT-009` | 0.70 | alias_match, bundle_grounding, risk_match |
| `aceitacao-de-risco-invalida` | `MT-020` | 0.76 | alias_match, bundle_grounding, how_it_arises_match |

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
