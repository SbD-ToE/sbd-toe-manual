# 50. Ameaças Mitigadas — Requisitos de Segurança

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

Total: **18 entidades** (Threat × 18, AntiPattern × 0, Signal × 0) mapped a este capítulo.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-021` | Ausência de requisitos de segurança | normative | heuristic |
| Threat | `MT-022` | Definição ambígua ou não testável | normative | heuristic |
| Threat | `MT-023` | Requisitos genéricos não específicos | normative | heuristic |
| Threat | `MT-024` | Falta de requisitos em sistemas legados | normative | heuristic |
| Threat | `MT-025` | Requisitos não alinhados com risco | normative | heuristic |
| Threat | `MT-026` | Requisitos definidos mas nunca verificados | normative | heuristic |
| Threat | `MT-027` | Validações inconsistentes entre projetos | normative | heuristic |
| Threat | `MT-028` | Ausência de rastreio entre requisito e teste | normative | heuristic |
| Threat | `MT-029` | Requisitos não verificados em CI/CD | normative | heuristic |
| Threat | `MT-030` | Risco aceite sem validação documental | normative | heuristic |
| Threat | `MT-031` | Exceções a requisitos não documentadas | normative | heuristic |
| Threat | `MT-032` | Segurança omitida por “não ser funcional” | normative | heuristic |
| Threat | `MT-033` | Aceitação de exceções sem aprovação | normative | heuristic |
| Threat | `MT-034` | Exceções não reverificadas no tempo | normative | heuristic |
| Threat | `MT-035` | Não saber se requisitos foram aplicados | normative | heuristic |
| Threat | `MT-036` | Requisitos aplicados mas não testados | normative | heuristic |
| Threat | `MT-037` | Mudanças de requisitos não propagadas | normative | heuristic |
| Threat | `MT-038` | Ambiguidade entre requisito e controlo | normative | heuristic |

---

## § Threat surfaces — Manual + CAPEC primary

Threat surfaces canónicas per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (forte / parcial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-021` | STRIDE | Ausência de requisitos de segurança | — | `addon/01-catalogo-requisitos.md` | parcial | Explícito |
| `MT-022` | STRIDE | Definição ambígua ou não testável | — | `addon/07-validacao-requisitos.md` | parcial | Explícito |
| `MT-023` | STRIDE | Requisitos genéricos não específicos | — | `addon/09-taxonomia-rastreabilidade.md` | parcial | Explícito |
| `MT-024` | STRIDE | Falta de requisitos em sistemas legados | — | `addon/08-gestao-excecoes.md` | parcial | Explícito |
| `MT-025` | STRIDE | Requisitos não alinhados com risco | — | `addon/06-matriz-controlos-por-risco.md` | parcial | Explícito |
| `MT-026` | STRIDE | Requisitos definidos mas nunca verificados | — | `addon/10-validacao-requisitos.md` | parcial | Explícito |
| `MT-027` | STRIDE | Validações inconsistentes entre projetos | — | `addon/07-validacao-requisitos.md` | parcial | Explícito |
| `MT-028` | STRIDE | Ausência de rastreio entre requisito e teste | — | `addon/04-rastreabilidade-controlo.md` | parcial | Explícito |
| `MT-029` | STRIDE | Requisitos não verificados em CI/CD | — | `addon/10-validacao-requisitos.md` | parcial | Explícito |
| `MT-030` | STRIDE | Risco aceite sem validação documental | — | `addon/08-gestao-excecoes.md` | parcial | Explícito |
| `MT-031` | STRIDE | Exceções a requisitos não documentadas | — | `addon/08-gestao-excecoes.md` | parcial | Explícito |
| `MT-032` | STRIDE | Segurança omitida por “não ser funcional” | — | `addon/01-catalogo-requisitos.md` | parcial | Explícito |
| `MT-033` | STRIDE | Aceitação de exceções sem aprovação | — | `addon/08-gestao-excecoes.md` | parcial | Explícito |
| `MT-034` | STRIDE | Exceções não reverificadas no tempo | — | `15-aplicacao-lifecycle.md` | parcial | Explícito |
| `MT-035` | STRIDE | Não saber se requisitos foram aplicados | — | `addon/04-rastreabilidade-controlo.md` | parcial | Explícito |
| `MT-036` | STRIDE | Requisitos aplicados mas não testados | — | `addon/07-validacao-requisitos.md` | parcial | Explícito |
| `MT-037` | STRIDE | Mudanças de requisitos não propagadas | — | `addon/01-catalogo-requisitos.md` | parcial | Explícito |
| `MT-038` | STRIDE | Ambiguidade entre requisito e controlo | — | `addon/04-rastreabilidade-controlo.md` | parcial | Explícito |

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
