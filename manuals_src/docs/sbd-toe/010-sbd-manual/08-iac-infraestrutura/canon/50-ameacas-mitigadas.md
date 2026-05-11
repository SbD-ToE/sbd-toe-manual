# 50. Ameaças Mitigadas — IaC e Infraestrutura

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

Total: **28 entidades** (Threat × 17, AntiPattern × 6, Signal × 5) mapped a este capítulo.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-132` | Defaults inseguros ou permissivos | normative | heuristic |
| Threat | `MT-133` | Configurações sem validação | normative | heuristic |
| Threat | `MT-134` | Campos críticos deixados em branco ou default | normative | heuristic |
| Threat | `MT-135` | Ambientes inconsistentes entre execuções | normative | heuristic |
| Threat | `MT-136` | Uso de módulos inseguros ou sem validação | normative | heuristic |
| Threat | `MT-137` | Hardcoded de parâmetros críticos | normative | heuristic |
| Threat | `MT-138` | Ambientes inseguros provisionados por erro | normative | heuristic |
| Threat | `MT-139` | Provisionamento com permissões excessivas | normative | heuristic |
| Threat | `MT-140` | Falta de tags de classificação de dados | normative | heuristic |
| Threat | `MT-141` | Uso de dados reais em ambientes de teste | normative | heuristic |
| Threat | `MT-142` | Segredos hardcoded ou mal geridos | normative | heuristic |
| Threat | `MT-143` | Alterações aplicadas sem revisão | normative | heuristic |
| Threat | `MT-144` | Falta de owner e accountability | normative | heuristic |
| Threat | `MT-145` | Reutilização de módulos sem tracking | normative | heuristic |
| Threat | `MT-146` | Aplicação de alterações inseguras por bypass | normative | heuristic |
| Threat | `MT-147` | Justificações informais ou inexistentes | normative | heuristic |
| Threat | `MT-148` | Ambientes provisionados com exceções acumuladas | normative | heuristic |
| AntiPattern | `sem:antipattern:ambientes-mal-segregados` | Ambientes mal segregados | semantic | scored |
| AntiPattern | `sem:antipattern:confianca-na-experiencia-individual-sem-automacao` | Confiança na experiência individual sem automação | semantic | scored |
| AntiPattern | `sem:antipattern:erros-de-configuracao` | Erros de configuração | semantic | scored |
| AntiPattern | `sem:antipattern:ignorar-momentos-criticos-no-ciclo-de-vida-do-iac` | Ignorar momentos críticos no ciclo de vida do IaC | semantic | scored |
| AntiPattern | `sem:antipattern:permissoes-excessivas` | Permissões excessivas | semantic | scored |
| AntiPattern | `sem:antipattern:uso-de-modulos-maliciosos` | Uso de módulos maliciosos | semantic | scored |
| Signal | `sem:signal:catalogo-de-modulos-certificados` | Catálogo de módulos certificados | semantic | scored |
| Signal | `sem:signal:dashboards-de-validacao` | Dashboards de validação | semantic | scored |
| Signal | `sem:signal:gestao-centralizada-de-excecoes` | Gestão centralizada de exceções | semantic | scored |
| Signal | `sem:signal:pipelines-ci-cd-obrigatorios` | Pipelines CI/CD obrigatórios | semantic | scored |
| Signal | `sem:signal:uso-de-ferramentas-de-scanning` | Uso de ferramentas de scanning | semantic | scored |

---

## § Threat surfaces — Manual + CAPEC primary

Threat surfaces canónicas per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (forte / parcial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-132` | STRIDE | Defaults inseguros ou permissivos | — | `addon/02-validacoes-e-checks.md` | parcial | Explícito |
| `MT-133` | STRIDE | Configurações sem validação | — | `addon/06-controle-enforcement.md` | parcial | Explícito |
| `MT-134` | STRIDE | Campos críticos deixados em branco ou default | — | `addon/07-rastreabilidade-e-tags.md` | parcial | Explícito |
| `MT-135` | STRIDE | Ambientes inconsistentes entre execuções | — | `addon/06`, `addon/30-recomendacoes-avancadas` | parcial | Explícito |
| `MT-136` | STRIDE | Uso de módulos inseguros ou sem validação | — | `addon/03-governanca-modulos.md` | parcial | Explícito |
| `MT-137` | STRIDE | Hardcoded de parâmetros críticos | — | `addon/02-validacoes-e-checks.md` | parcial | Explícito |
| `MT-138` | STRIDE | Ambientes inseguros provisionados por erro | — | `addon/01-planeamento-e-controle.md` | parcial | Explícito |
| `MT-139` | STRIDE | Provisionamento com permissões excessivas | — | `addon/04-principios-sbd-iac.md` | parcial | Explícito |
| `MT-140` | STRIDE | Falta de tags de classificação de dados | — | `addon/07-rastreabilidade-e-tags.md` | parcial | Explícito |
| `MT-141` | STRIDE | Uso de dados reais em ambientes de teste | — | `addon/01-planeamento-e-controle.md` | parcial | Explícito |
| `MT-142` | STRIDE | Segredos hardcoded ou mal geridos | — | `addon/06-controle-enforcement.md` | parcial | Explícito |
| `MT-143` | STRIDE | Alterações aplicadas sem revisão | — | `addon/01-planeamento-e-controle.md` | parcial | Explícito |
| `MT-144` | STRIDE | Falta de owner e accountability | — | `addon/07-rastreabilidade-e-tags.md` | parcial | Explícito |
| `MT-145` | STRIDE | Reutilização de módulos sem tracking | — | `addon/03-governanca-modulos.md` | parcial | Explícito |
| `MT-146` | STRIDE | Aplicação de alterações inseguras por bypass | — | `addon/06-controle-enforcement.md` | parcial | Explícito |
| `MT-147` | STRIDE | Justificações informais ou inexistentes | — | `addon/09-gestao-excecoes.md` | parcial | Explícito |
| `MT-148` | STRIDE | Ambientes provisionados com exceções acumuladas | — | `15-aplicacao-lifecycle.md` | parcial | Explícito |

---

## § AntiPattern exposure mapping

AntiPattern → Threat exposure relations per Manual ontology V2 `antipattern_threat_links.jsonl`. Cada link indica que o antipattern (quando presente em código/processo) expõe a ameaça.

| AntiPattern | Exposes threat | Confidence | Justification |
|---|---|---|---|
| `permissoes-excessivas` | `MT-139` | 0.76 | alias_match, bundle_grounding, threat_label_match |

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
