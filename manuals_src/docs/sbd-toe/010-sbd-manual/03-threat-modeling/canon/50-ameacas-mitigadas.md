# 50. Ameaças Mitigadas — Threat Modeling

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

Total: **18 entidades** (Threat × 16, AntiPattern × 2, Signal × 0) mapped a este capítulo.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-039` | Ameaças desconhecidas e não tratadas | normative | heuristic |
| Threat | `MT-040` | Prioridades de segurança mal definidas | normative | heuristic |
| Threat | `MT-041` | Requisitos definidos sem base em ameaças | normative | heuristic |
| Threat | `MT-042` | Ameaças a privacidade ignoradas | normative | heuristic |
| Threat | `MT-043` | Falta de cobertura de ameaças não técnicas | normative | heuristic |
| Threat | `MT-044` | Arquitetura insegura não identificada | normative | heuristic |
| Threat | `MT-045` | Validação superficial em design reviews | normative | heuristic |
| Threat | `MT-046` | Controles aplicados sem base em arquitetura | normative | heuristic |
| Threat | `MT-047` | Ausência de revisão em interfaces críticas | normative | heuristic |
| Threat | `MT-048` | Ameaças descobertas demasiado tarde | normative | heuristic |
| Threat | `MT-049` | Mudanças críticas sem nova modelação | normative | heuristic |
| Threat | `MT-050` | Descontinuidade entre equipas e fases | normative | heuristic |
| Threat | `MT-051` | Ameaças não visíveis na pipeline CI/CD | normative | heuristic |
| Threat | `MT-052` | Conhecimento de ameaças não acumulado | normative | heuristic |
| Threat | `MT-053` | Inconsistência entre projetos e equipas | normative | heuristic |
| Threat | `MT-054` | Ferramentas desconectadas do ciclo | normative | heuristic |
| AntiPattern | `sem:antipattern:ausencia-de-ameaca-no-modelo` | Ausência de ameaça no modelo | semantic | scored |
| AntiPattern | `sem:antipattern:omissao-estrutural-de-ameacas` | Omissão estrutural de ameaças | semantic | scored |

---

## § Threat surfaces — Manual + CAPEC primary

Threat surfaces canónicas per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (forte / parcial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-039` | STRIDE | Ameaças desconhecidas e não tratadas | — | `addon/01-metodologias-e-ferramentas.md` | parcial | Explícito |
| `MT-040` | STRIDE | Prioridades de segurança mal definidas | — | `addon/07-mapeamento-threats-requisitos.md` | parcial | Explícito |
| `MT-041` | STRIDE | Requisitos definidos sem base em ameaças | — | `addon/07-mapeamento-threats-requisitos.md` | parcial | Explícito |
| `MT-042` | LINDDUN | Ameaças a privacidade ignoradas | — | `addon/08-exemplo-privacidade.md` | parcial | Explícito |
| `MT-043` | STRIDE | Falta de cobertura de ameaças não técnicas | — | `addon/01-metodologias-e-ferramentas.md` | parcial | Explícito |
| `MT-044` | STRIDE | Arquitetura insegura não identificada | — | `addon/09-validacao-arquitetura.md` | parcial | Explícito |
| `MT-045` | STRIDE | Validação superficial em design reviews | — | `15-aplicacao-lifecycle.md` | parcial | Explícito |
| `MT-046` | STRIDE | Controles aplicados sem base em arquitetura | — | `addon/07-mapeamento-threats-requisitos.md` | parcial | Explícito |
| `MT-047` | STRIDE | Ausência de revisão em interfaces críticas | — | `addon/01-metodologias-e-ferramentas.md` | parcial | Explícito |
| `MT-048` | STRIDE | Ameaças descobertas demasiado tarde | — | `15-aplicacao-lifecycle.md` | parcial | Explícito |
| `MT-049` | STRIDE | Mudanças críticas sem nova modelação | — | `addon/09-validacao-arquitetura.md` | parcial | Explícito |
| `MT-050` | STRIDE | Descontinuidade entre equipas e fases | — | `addon/07-mapeamento-threats-requisitos.md` | parcial | Explícito |
| `MT-051` | STRIDE | Ameaças não visíveis na pipeline CI/CD | — | `addon/06-threat-modeling-ci.md` | parcial | Explícito |
| `MT-052` | STRIDE | Conhecimento de ameaças não acumulado | — | `addon/10-integracao-iriusrisk.md` | parcial | Explícito |
| `MT-053` | STRIDE | Inconsistência entre projetos e equipas | — | `addon/01-metodologias-e-ferramentas.md` | parcial | Explícito |
| `MT-054` | STRIDE | Ferramentas desconectadas do ciclo | — | `addon/07-mapeamento-threats-requisitos.md` | parcial | Explícito |

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
