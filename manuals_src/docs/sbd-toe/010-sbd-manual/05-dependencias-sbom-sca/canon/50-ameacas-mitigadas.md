# 50. Ameaças Mitigadas — Dependências, SBOM e SCA

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

Total: **20 entidades** (Threat × 20, AntiPattern × 0, Signal × 0) mapped a este capítulo.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-073` | Inclusão de bibliotecas com CVEs ativos | normative | heuristic |
| Threat | `MT-074` | Dependências desatualizadas | normative | heuristic |
| Threat | `MT-075` | Ausência de registo de versões | normative | heuristic |
| Threat | `MT-076` | Inclusão de bibliotecas não auditadas | normative | heuristic |
| Threat | `MT-077` | Desconhecimento de bibliotecas utilizadas | normative | heuristic |
| Threat | `MT-078` | Falta de associação entre vulnerabilidade e artefacto | normative | heuristic |
| Threat | `MT-079` | Falta de histórico de introdução de pacotes | normative | heuristic |
| Threat | `MT-080` | Inclusão de pacotes de repositórios maliciosos | normative | heuristic |
| Threat | `MT-081` | Dependência transitiva com componente inseguro | normative | heuristic |
| Threat | `MT-082` | Pipeline injeta versão não autenticada | normative | heuristic |
| Threat | `MT-083` | CVEs ignoradas sem justificação | normative | heuristic |
| Threat | `MT-084` | Mitigações aplicadas sem rastreio | normative | heuristic |
| Threat | `MT-085` | Falta de ciclo de revisão de exceções | normative | heuristic |
| Threat | `MT-086` | Uso arbitrário de bibliotecas | normative | heuristic |
| Threat | `MT-087` | Bibliotecas proibidas são usadas | normative | heuristic |
| Threat | `MT-088` | Falta de política de substituição | normative | heuristic |
| Threat | `MT-089` | Introdução de dependência vulnerável não declarada | normative | heuristic |
| Threat | `MT-090` | Confusão de dependências | normative | heuristic |
| Threat | `MT-091` | Backdoor via ferramenta de build | normative | heuristic |
| Threat | `MT-092` | Drift de composição entre builds | normative | heuristic |

---

## § Threat surfaces — Manual + CAPEC primary

Threat surfaces canónicas per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (forte / parcial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-073` | STRIDE | Inclusão de bibliotecas com CVEs ativos | — | `addon/02-analise-sca.md` | parcial | Explícito |
| `MT-074` | STRIDE | Dependências desatualizadas | — | `addon/05-politica-atualizacoes.md` | parcial | Explícito |
| `MT-075` | STRIDE | Ausência de registo de versões | — | `addon/01-inventario-sbom.md` | parcial | Explícito |
| `MT-076` | STRIDE | Inclusão de bibliotecas não auditadas | — | `addon/03-governanca-libs-terceiros.md` | parcial | Explícito |
| `MT-077` | STRIDE | Desconhecimento de bibliotecas utilizadas | — | `addon/01-inventario-sbom.md` | parcial | Explícito |
| `MT-078` | STRIDE | Falta de associação entre vulnerabilidade e artefacto | — | `addon/08-rastreabilidade-vulnerabilidades.md` | parcial | Explícito |
| `MT-079` | STRIDE | Falta de histórico de introdução de pacotes | — | `addon/07-controle-registos-origem.md` | parcial | Explícito |
| `MT-080` | STRIDE | Inclusão de pacotes de repositórios maliciosos | — | `addon/07-controle-registos-origem.md` | parcial | Explícito |
| `MT-081` | STRIDE | Dependência transitiva com componente inseguro | — | `addon/02-analise-sca.md` | parcial | Explícito |
| `MT-082` | STRIDE | Pipeline injeta versão não autenticada | — | `addon/04-integracao-ci-cd.md` | parcial | Explícito |
| `MT-083` | STRIDE | CVEs ignoradas sem justificação | — | `addon/09-excecoes-e-aceitacao-risco.md` | parcial | Explícito |
| `MT-084` | STRIDE | Mitigações aplicadas sem rastreio | — | `addon/09-excecoes-e-aceitacao-risco.md` | parcial | Explícito |
| `MT-085` | STRIDE | Falta de ciclo de revisão de exceções | — | `15-aplicacao-lifecycle.md` | parcial | Explícito |
| `MT-086` | STRIDE | Uso arbitrário de bibliotecas | — | `addon/03-governanca-libs-terceiros.md` | parcial | Explícito |
| `MT-087` | STRIDE | Bibliotecas proibidas são usadas | — | `addon/04-integracao-ci-cd.md` | parcial | Explícito |
| `MT-088` | STRIDE | Falta de política de substituição | — | `addon/05-politica-atualizacoes.md` | parcial | Explícito |
| `MT-089` | STRIDE | Introdução de dependência vulnerável não declarada | — | SBOM boundary, revisão de dependências | parcial | Explícito |
| `MT-090` | STRIDE | Confusão de dependências | — | SCA, validação de origem | parcial | Explícito |
| `MT-091` | STRIDE | Backdoor via ferramenta de build | — | Governance de tooling | parcial | Explícito |
| `MT-092` | STRIDE | Drift de composição entre builds | — | CI/CD gating | parcial | Explícito |

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
