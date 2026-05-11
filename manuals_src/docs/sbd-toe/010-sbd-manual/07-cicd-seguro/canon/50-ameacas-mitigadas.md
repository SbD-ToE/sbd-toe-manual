# 50. Ameaças Mitigadas — CI/CD Seguro

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

Total: **24 entidades** (Threat × 21, AntiPattern × 2, Signal × 1) mapped a este capítulo.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-111` | Execução de código não autorizado em pipeline | normative | heuristic |
| Threat | `MT-112` | Comprometimento do ambiente de build | normative | heuristic |
| Threat | `MT-113` | Elevação de privilégios no pipeline | normative | heuristic |
| Threat | `MT-114` | Push não autorizado para branches protegidas | normative | heuristic |
| Threat | `MT-115` | Execução de código não auditado | normative | heuristic |
| Threat | `MT-116` | Substituição silenciosa de código legítimo | normative | heuristic |
| Threat | `MT-117` | Build forjado fora da pipeline | normative | heuristic |
| Threat | `MT-118` | Injeção de lógica dinâmica em pipeline | normative | heuristic |
| Threat | `MT-119` | Uso de componentes externos inseguros | normative | heuristic |
| Threat | `MT-120` | Vazamento de segredos via logs | normative | heuristic |
| Threat | `MT-121` | Segredos hardcoded | normative | heuristic |
| Threat | `MT-122` | Reutilização de segredos | normative | heuristic |
| Threat | `MT-123` | Ausência de gates de segurança | normative | heuristic |
| Threat | `MT-124` | Validações não executadas | normative | heuristic |
| Threat | `MT-125` | Falta de rastreabilidade | normative | heuristic |
| Threat | `MT-126` | Bypass de controlos sem rasto | normative | heuristic |
| Threat | `MT-127` | Alterações críticas sem visibilidade | normative | heuristic |
| Threat | `MT-128` | Promoções sem responsável humano | normative | heuristic |
| Threat | `MT-129` | Evidência plausível sem execução | normative | heuristic |
| Threat | `MT-130` | Não-determinismo do pipeline | normative | heuristic |
| Threat | `MT-131` | Exfiltração de contexto sensível | normative | heuristic |
| AntiPattern | `sem:antipattern:exposicao-excessiva-de-contexto-em-logs-e-artefactos` | exposição excessiva de contexto em logs e artefactos | semantic | scored |
| AntiPattern | `sem:antipattern:uso-de-segredos-estaticos` | uso de segredos estáticos | semantic | scored |
| Signal | `sem:signal:sinal-automatico` | sinal automático | semantic | scored |

---

## § Threat surfaces — Manual + CAPEC primary

Threat surfaces canónicas per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (forte / parcial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-111` | STRIDE | Execução de código não autorizado em pipeline | — | Design seguro de pipelines; isolamento de runners | parcial | Explícito |
| `MT-112` | STRIDE | Comprometimento do ambiente de build | — | Isolamento e efemeridade de runners | parcial | Explícito |
| `MT-113` | STRIDE | Elevação de privilégios no pipeline | — | Hardening de pipelines | parcial | Explícito |
| `MT-114` | STRIDE | Push não autorizado para branches protegidas | — | Gestão segura de código-fonte | parcial | Explícito |
| `MT-115` | STRIDE | Execução de código não auditado | — | Políticas de execução | parcial | Explícito |
| `MT-116` | STRIDE | Substituição silenciosa de código legítimo | — | Rastreabilidade e assinaturas | parcial | Explícito |
| `MT-117` | STRIDE | Build forjado fora da pipeline | — | Integridade e proveniência | parcial | Explícito |
| `MT-118` | STRIDE | Injeção de lógica dinâmica em pipeline | — | Segurança do código de pipeline | parcial | Explícito |
| `MT-119` | STRIDE | Uso de componentes externos inseguros | — | Controlo de dependências | parcial | Explícito |
| `MT-120` | STRIDE | Vazamento de segredos via logs | — | Gestão de segredos | parcial | Explícito |
| `MT-121` | STRIDE | Segredos hardcoded | — | Gestão de segredos | parcial | Explícito |
| `MT-122` | STRIDE | Reutilização de segredos | — | Lifecycle de segredos | parcial | Explícito |
| `MT-123` | STRIDE | Ausência de gates de segurança | — | Políticas de gates | parcial | Explícito |
| `MT-124` | STRIDE | Validações não executadas | — | Validações integradas | parcial | Explícito |
| `MT-125` | STRIDE | Falta de rastreabilidade | — | Rastreabilidade | parcial | Explícito |
| `MT-126` | STRIDE | Bypass de controlos sem rasto | — | Gestão de exceções | parcial | Explícito |
| `MT-127` | STRIDE | Alterações críticas sem visibilidade | — | Governação contínua | parcial | Explícito |
| `MT-128` | STRIDE | Promoções sem responsável humano | — | Gates e governação | parcial | Explícito |
| `MT-129` | STRIDE | Evidência plausível sem execução | — | Evidência empírica | parcial | Explícito |
| `MT-130` | STRIDE | Não-determinismo do pipeline | — | Reprodutibilidade | parcial | Explícito |
| `MT-131` | STRIDE | Exfiltração de contexto sensível | — | Controlo de integrações | parcial | Explícito |

---

## § AntiPattern exposure mapping

AntiPattern → Threat exposure relations per Manual ontology V2 `antipattern_threat_links.jsonl`. Cada link indica que o antipattern (quando presente em código/processo) expõe a ameaça.

| AntiPattern | Exposes threat | Confidence | Justification |
|---|---|---|---|
| `uso-de-segredos-estaticos` | `MT-121` | 0.76 | alias_match, bundle_grounding, threat_label_match |

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
