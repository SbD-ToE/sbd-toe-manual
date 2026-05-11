# 50. Ameaças Mitigadas — Containers e Imagens

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
| Threat | `MT-149` | Imagens base vulneráveis/obsoletas | normative | heuristic |
| Threat | `MT-150` | Inclusão de dependências inseguras no build | normative | heuristic |
| Threat | `MT-151` | Conteúdo inesperado no _context_ de build | normative | heuristic |
| Threat | `MT-152` | Configurações inseguras no Dockerfile | normative | heuristic |
| Threat | `MT-153` | Imagens não assinadas / sem verificação | normative | heuristic |
| Threat | `MT-154` | Substituição maliciosa em registo | normative | heuristic |
| Threat | `MT-155` | Falta de trilho de auditoria (quem construiu o quê) | normative | heuristic |
| Threat | `MT-156` | Execução como root / capabilities excessivas | normative | heuristic |
| Threat | `MT-157` | Montagens e volumes inseguros | normative | heuristic |
| Threat | `MT-158` | Falta de políticas de rede | normative | heuristic |
| Threat | `MT-159` | _Admission_ permissivo | normative | heuristic |
| Threat | `MT-160` | Segredos embebidos em imagem | normative | heuristic |
| Threat | `MT-161` | Exposição em variáveis de ambiente | normative | heuristic |
| Threat | `MT-162` | Manifestos inseguros aprovados | normative | heuristic |
| Threat | `MT-163` | Desalinhamento imagem↔manifesto | normative | heuristic |
| Threat | `MT-164` | Falta de rastreabilidade de deploys | normative | heuristic |
| Threat | `MT-165` | _Shadow containers_ fora do pipeline | normative | heuristic |
| Threat | `MT-166` | _Drift_ de configuração | normative | heuristic |

---

## § Threat surfaces — Manual + CAPEC primary

Threat surfaces canónicas per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (forte / parcial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-149` | STRIDE | Imagens base vulneráveis/obsoletas | — | *Checklist 3–4*, *Policies: Gestão de Vulnerabilidades*, *Rastreabilidade: SSDF RV.1* | forte | Explícito |
| `MT-150` | STRIDE | Inclusão de dependências inseguras no build | — | Cap. 05 (SBOM/SCA), *Checklist 3–4* | parcial | Explícito |
| `MT-151` | STRIDE | Conteúdo inesperado no _context_ de build | — | *Policies: Construção Segura de Imagens* | parcial | Explícito |
| `MT-152` | STRIDE | Configurações inseguras no Dockerfile | — | *Checklist 6*, *Policies: Construção Segura* | parcial | Explícito |
| `MT-153` | STRIDE | Imagens não assinadas / sem verificação | — | *Checklist 5 & 10–11*, *Policies: Assinatura e Proveniência* | parcial | Explícito |
| `MT-154` | STRIDE | Substituição maliciosa em registo | — | *Rastreabilidade: SLSA/SSDF*, *Policies: Repositórios* | parcial | Explícito |
| `MT-155` | STRIDE | Falta de trilho de auditoria (quem construiu o quê) | — | *Checklist 14–15*, *Rastreabilidade: DSOMM Ops* | parcial | Explícito |
| `MT-156` | STRIDE | Execução como root / capabilities excessivas | — | *Checklist 7–9*, *Policies: Hardening de Runtime* | parcial | Explícito |
| `MT-157` | STRIDE | Montagens e volumes inseguros | — | *Policies: Hardening de Runtime* | parcial | Explícito |
| `MT-158` | STRIDE | Falta de políticas de rede | — | *Policies: Runtime*, *Checklist 8* | parcial | Explícito |
| `MT-159` | STRIDE | _Admission_ permissivo | — | *Checklist 11*, *Policies: Validação de Manifestos* | parcial | Explícito |
| `MT-160` | STRIDE | Segredos embebidos em imagem | — | *Policies: Segredos*, *Checklist 3 & 5* | parcial | Explícito |
| `MT-161` | STRIDE | Exposição em variáveis de ambiente | — | *Policies: Segredos* | parcial | Explícito |
| `MT-162` | STRIDE | Manifestos inseguros aprovados | — | *Checklist 11*, *Policies: Validação de Manifestos* | parcial | Explícito |
| `MT-163` | STRIDE | Desalinhamento imagem↔manifesto | — | *Rastreabilidade: SLSA*, *Checklist 2 & 10–11* | parcial | Explícito |
| `MT-164` | STRIDE | Falta de rastreabilidade de deploys | — | *Checklist 14–15*, *DSOMM Ops Monitoring* | parcial | Explícito |
| `MT-165` | STRIDE | _Shadow containers_ fora do pipeline | — | *Policies: Runtime/Registos*, *Rastreabilidade: DSOMM* | parcial | Explícito |
| `MT-166` | STRIDE | _Drift_ de configuração | — | *Policies: Runtime*, Cap. 08 (IaC) | parcial | Explícito |

---

## § AntiPattern exposure mapping

_(Nenhuma antipattern→threat relation mapped a este capítulo.)_

---

## § CWE references (supporting only)

CWE references per §26 §4: **CWE apenas como suporte limitado, NÃO como substituto de taxonomy de threat**. Mapping para Manual threats listed below.

| CWE-ID | Linked threat | Note |
|---|---|---|
| `CWE-1104` | `?` | supporting reference; primary anchor é Manual threat |

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
