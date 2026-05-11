# 50. Ameaças Mitigadas — Formação e Onboarding

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

Total: **16 entidades** (Threat × 10, AntiPattern × 2, Signal × 4) mapped a este capítulo.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-212` | Configuração insegura por desconhecimento | normative | heuristic |
| Threat | `MT-213` | Reutilização indevida de segredos ou tokens | normative | heuristic |
| Threat | `MT-214` | Acesso técnico concedido sem validação | normative | heuristic |
| Threat | `MT-215` | Inclusão de terceiros sem validação | normative | heuristic |
| Threat | `MT-216` | Falta de ownership sobre segurança | normative | heuristic |
| Threat | `MT-217` | Regressão comportamental / cultura frágil | normative | heuristic |
| Threat | `MT-218` | Formação não rastreável | normative | heuristic |
| Threat | `MT-219` | Formação desigual entre equipas ou funções | normative | heuristic |
| Threat | `MT-220` | Formação teórica sem impacto prático | normative | heuristic |
| Threat | `MT-221` | Conteúdos desatualizados ou não aplicáveis | normative | heuristic |
| AntiPattern | `sem:antipattern:dependencia-exclusiva-de-ferramentas-automatizadas` | dependência exclusiva de ferramentas automatizadas | semantic | scored |
| AntiPattern | `sem:antipattern:falta-de-onboarding` | Falta de Onboarding | semantic | scored |
| Signal | `sem:signal:checklist-completo` | Checklist Completo | semantic | scored |
| Signal | `sem:signal:kpis-de-eficacia-formativa` | KPIs de eficácia formativa | semantic | scored |
| Signal | `sem:signal:kpis-de-formacao` | KPIs de Formação | semantic | scored |
| Signal | `sem:signal:resultados-de-quiz` | Resultados de Quizzes | semantic | scored |

---

## § Threat surfaces — Manual + CAPEC primary

Threat surfaces canónicas per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (forte / parcial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-212` | STRIDE | Configuração insegura por desconhecimento | — | `addon/01-catalogo-formativo.md`, `addon/02-trilho-formativo.md` | parcial | Explícito |
| `MT-213` | STRIDE | Reutilização indevida de segredos ou tokens | — | `addon/04-tecnicas-formativas.md`, `addon/06-manual-formacao-por-capitulo.md` | parcial | Explícito |
| `MT-214` | STRIDE | Acesso técnico concedido sem validação | — | `addon/10-checklist-onboarding.md`, `addon/11-template-quiz-onboarding.md` | parcial | Explícito |
| `MT-215` | STRIDE | Inclusão de terceiros sem validação | — | `addon/20-modelo-inclusao-terceiros.md`, `addon/21-plano-formacao-terceiros.md` | parcial | Explícito |
| `MT-216` | STRIDE | Falta de ownership sobre segurança | — | `addon/03-programa-champions.md` | parcial | Explícito |
| `MT-217` | STRIDE | Regressão comportamental / cultura frágil | — | `addon/04-tecnicas-formativas.md`, `addon/90-indicadores-metricas.md` | parcial | Explícito |
| `MT-218` | STRIDE | Formação não rastreável | — | `addon/10-checklist-onboarding.md`, `addon/11-template-quiz-onboarding.md` | parcial | Explícito |
| `MT-219` | STRIDE | Formação desigual entre equipas ou funções | — | `addon/02-trilho-formativo.md`, `addon/05-integracao-transversal.md` | parcial | Explícito |
| `MT-220` | STRIDE | Formação teórica sem impacto prático | — | `addon/04-tecnicas-formativas.md`, `addon/06-manual-formacao-por-capitulo.md` | parcial | Explícito |
| `MT-221` | STRIDE | Conteúdos desatualizados ou não aplicáveis | — | `addon/06-manual-formacao-por-capitulo.md`, `addon/07-exemplo1-manual-formacao-dev-pr-seguro.md` | parcial | Explícito |

---

## § AntiPattern exposure mapping

_(Nenhuma antipattern→threat relation mapped a este capítulo.)_

---

## § CWE references (supporting only)

CWE references per §26 §4: **CWE apenas como suporte limitado, NÃO como substituto de taxonomy de threat**. Mapping para Manual threats listed below.

| CWE-ID | Linked threat | Note |
|---|---|---|
| `CWE-693` | `?` | supporting reference; primary anchor é Manual threat |
| `CWE-798` | `?` | supporting reference; primary anchor é Manual threat |

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
