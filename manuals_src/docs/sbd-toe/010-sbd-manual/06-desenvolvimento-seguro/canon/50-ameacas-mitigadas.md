# 50. Ameaças Mitigadas — Desenvolvimento Seguro

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
| Threat | `MT-093` | Inclusão de padrões inseguros por hábito | normative | heuristic |
| Threat | `MT-094` | Uso de funções descontinuadas ou perigosas | normative | heuristic |
| Threat | `MT-095` | Injeção de código sem escape adequado | normative | heuristic |
| Threat | `MT-096` | Código inseguro sem deteção | normative | heuristic |
| Threat | `MT-097` | Ausência de rastreabilidade entre problemas e decisões | normative | heuristic |
| Threat | `MT-098` | Validação apenas reativa (ex: testes QA) | normative | heuristic |
| Threat | `MT-099` | Segurança removida por “incompatibilidade” | normative | heuristic |
| Threat | `MT-100` | Exceções não revistas ou revalidadas | normative | heuristic |
| Threat | `MT-101` | Desvios não rastreados entre guideline e prática | normative | heuristic |
| Threat | `MT-102` | Geração de código inseguro via IA | normative | heuristic |
| Threat | `MT-103` | Inclusão de vulnerabilidades conhecidas | normative | heuristic |
| Threat | `MT-104` | Falta de accountability sobre código gerado | normative | heuristic |
| Threat | `MT-105` | Inclusão de bibliotecas descontinuadas | normative | heuristic |
| Threat | `MT-106` | Falta de justificação para uso de dependência insegura | normative | heuristic |
| Threat | `MT-107` | Componente vulnerável mantido no build final | normative | heuristic |
| Threat | `MT-108` | Inconsistência entre equipas e projetos | normative | heuristic |
| Threat | `MT-109` | Inexistência de baseline de segurança | normative | heuristic |
| Threat | `MT-110` | Fraca responsabilização pela segurança do código | normative | heuristic |

---

## § Threat surfaces — Manual + CAPEC primary

Threat surfaces canónicas per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (forte / parcial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-093` | STRIDE | Inclusão de padrões inseguros por hábito | — | `addon/02-linters-validacoes.md` | parcial | Explícito |
| `MT-094` | STRIDE | Uso de funções descontinuadas ou perigosas | — | `addon/01-boas-praticas-codigo.md` | parcial | Explícito |
| `MT-095` | STRIDE | Injeção de código sem escape adequado | — | `addon/08-validacoes-codigo.md` | parcial | Explícito |
| `MT-096` | STRIDE | Código inseguro sem deteção | — | `addon/08-validacoes-codigo.md` | parcial | Explícito |
| `MT-097` | STRIDE | Ausência de rastreabilidade entre problemas e decisões | — | `addon/09-anotacoes-evidencia.md` | parcial | Explícito |
| `MT-098` | STRIDE | Validação apenas reativa (ex: testes QA) | — | `addon/08-validacoes-codigo.md` | parcial | Explícito |
| `MT-099` | STRIDE | Segurança removida por “incompatibilidade” | — | `addon/05-excecoes-e-justificacoes.md` | parcial | Explícito |
| `MT-100` | STRIDE | Exceções não revistas ou revalidadas | — | `15-aplicacao-lifecycle.md` | parcial | Explícito |
| `MT-101` | STRIDE | Desvios não rastreados entre guideline e prática | — | `addon/07-guidelines-equipa.md` | parcial | Explícito |
| `MT-102` | STRIDE | Geração de código inseguro via IA | — | `addon/10-genia-e-seguranca.md` | parcial | Explícito |
| `MT-103` | STRIDE | Inclusão de vulnerabilidades conhecidas | — | `addon/10-genia-e-seguranca.md` | parcial | Explícito |
| `MT-104` | STRIDE | Falta de accountability sobre código gerado | — | `addon/09-anotacoes-evidencia.md` | parcial | Explícito |
| `MT-105` | STRIDE | Inclusão de bibliotecas descontinuadas | — | `addon/03-seguranca-dependencias.md` | parcial | Explícito |
| `MT-106` | STRIDE | Falta de justificação para uso de dependência insegura | — | `addon/05-excecoes-e-justificacoes.md` | parcial | Explícito |
| `MT-107` | STRIDE | Componente vulnerável mantido no build final | — | `addon/08-validacoes-codigo.md` | parcial | Explícito |
| `MT-108` | STRIDE | Inconsistência entre equipas e projetos | — | `addon/07-guidelines-equipa.md` | parcial | Explícito |
| `MT-109` | STRIDE | Inexistência de baseline de segurança | — | `addon/01-boas-praticas-codigo.md` | parcial | Explícito |
| `MT-110` | STRIDE | Fraca responsabilização pela segurança do código | — | `addon/09-anotacoes-evidencia.md` | parcial | Explícito |

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
