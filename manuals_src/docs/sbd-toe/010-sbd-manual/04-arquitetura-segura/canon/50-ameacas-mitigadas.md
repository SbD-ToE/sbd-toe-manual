# 50. Ameaças Mitigadas — Arquitetura Segura

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

Total: **22 entidades** (Threat × 18, AntiPattern × 4, Signal × 0) mapped a este capítulo.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-055` | Interfaces expostas sem isolamento | normative | heuristic |
| Threat | `MT-056` | Mistura de dados e controlo na mesma zona | normative | heuristic |
| Threat | `MT-057` | Acesso lateral não controlado entre módulos | normative | heuristic |
| Threat | `MT-058` | Ausência de isolamento entre utilizadores | normative | heuristic |
| Threat | `MT-059` | Arquitetura inexistente ou desatualizada | normative | heuristic |
| Threat | `MT-060` | Confusão sobre localização de controlos | normative | heuristic |
| Threat | `MT-061` | Ambiguidade sobre fronteiras e zonas | normative | heuristic |
| Threat | `MT-062` | Arquitetura não revê mecanismos de fallback | normative | heuristic |
| Threat | `MT-063` | Arquitetura nunca revista | normative | heuristic |
| Threat | `MT-064` | Alterações estruturais sem revalidação | normative | heuristic |
| Threat | `MT-065` | Design informal ou ad hoc | normative | heuristic |
| Threat | `MT-066` | Exceções de arquitetura sem rasto | normative | heuristic |
| Threat | `MT-067` | Requisitos de arquitetura não definidos | normative | heuristic |
| Threat | `MT-068` | Impossibilidade de mapear decisões a controlos | normative | heuristic |
| Threat | `MT-069` | Diagrama não reflete controlos implementados | normative | heuristic |
| Threat | `MT-070` | Aplicações L1 tratadas como críticas | normative | heuristic |
| Threat | `MT-071` | Sobredimensionamento de segurança da arquitetura | normative | heuristic |
| Threat | `MT-072` | Ambientes de execução não refletidos no design | normative | heuristic |
| AntiPattern | `sem:antipattern:dependencia-circular` | dependência circular | semantic | scored |
| AntiPattern | `sem:antipattern:excecoes-nao-documentadas` | Exceções não documentadas | semantic | scored |
| AntiPattern | `sem:antipattern:modelos-inconsistentes-incompletos-ou-desatualizados` | Modelos inconsistentes, incompletos ou desatualizados | semantic | scored |
| AntiPattern | `sem:antipattern:threat-modeling-sem-arquitetura-clara` | Threat modeling sem arquitetura clara | semantic | scored |

---

## § Threat surfaces — Manual + CAPEC primary

Threat surfaces canónicas per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (forte / parcial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-055` | STRIDE | Interfaces expostas sem isolamento | — | `addon/01-catalogo-requisitos.md` | parcial | Explícito |
| `MT-056` | STRIDE | Mistura de dados e controlo na mesma zona | — | `addon/04-diagramas-referencia.md` | parcial | Explícito |
| `MT-057` | STRIDE | Acesso lateral não controlado entre módulos | — | `addon/02-casos-praticos.md` | parcial | Explícito |
| `MT-058` | STRIDE | Ausência de isolamento entre utilizadores | — | `addon/01-catalogo-requisitos.md` | parcial | Explícito |
| `MT-059` | STRIDE | Arquitetura inexistente ou desatualizada | — | `addon/04-diagramas-referencia.md` | parcial | Explícito |
| `MT-060` | STRIDE | Confusão sobre localização de controlos | — | `addon/01-catalogo-requisitos.md` | parcial | Explícito |
| `MT-061` | STRIDE | Ambiguidade sobre fronteiras e zonas | — | `addon/04-diagramas-referencia.md` | parcial | Explícito |
| `MT-062` | STRIDE | Arquitetura não revê mecanismos de fallback | — | `addon/01-catalogo-requisitos.md` | parcial | Explícito |
| `MT-063` | STRIDE | Arquitetura nunca revista | — | `15-aplicacao-lifecycle.md` | parcial | Explícito |
| `MT-064` | STRIDE | Alterações estruturais sem revalidação | — | `addon/05-validacao.md` | parcial | Explícito |
| `MT-065` | STRIDE | Design informal ou ad hoc | — | `addon/05-validacao.md` | parcial | Explícito |
| `MT-066` | STRIDE | Exceções de arquitetura sem rasto | — | `addon/03-excecoes.md` | parcial | Explícito |
| `MT-067` | STRIDE | Requisitos de arquitetura não definidos | — | `addon/01-catalogo-requisitos.md` | parcial | Explícito |
| `MT-068` | STRIDE | Impossibilidade de mapear decisões a controlos | — | `addon/06-rastreabilidade.md` | parcial | Explícito |
| `MT-069` | STRIDE | Diagrama não reflete controlos implementados | — | `addon/05-validacao.md` | parcial | Explícito |
| `MT-070` | STRIDE | Aplicações L1 tratadas como críticas | — | `15-aplicacao-lifecycle.md` | parcial | Explícito |
| `MT-071` | STRIDE | Sobredimensionamento de segurança da arquitetura | — | `addon/02-casos-praticos.md` | parcial | Explícito |
| `MT-072` | STRIDE | Ambientes de execução não refletidos no design | — | `addon/04-diagramas-referencia.md` | parcial | Explícito |

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
