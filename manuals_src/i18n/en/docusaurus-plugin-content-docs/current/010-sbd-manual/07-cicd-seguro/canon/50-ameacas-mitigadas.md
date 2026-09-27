---
id: ameacas-mitigadas
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/canon/50-ameacas-mitigadas.md
  source_sha256: 83f02303ab244436c4370f6a5b2509828605a543ef27cda65a87f936399c013f
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 3aaae35f5b168ef918f968defe51b06501927442ddd7dfd2b45176eb84df0d25
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [appsec_core, chapter_role, deterministic, framework_source_corpus, practitioner_manual, provenance, sbdtoe_sbd, threat, traceability]
  glossary_sha256: 9db71a672aca7ca4646172a8b37c4c1d784f82d5813ae21fae00c62f3af15e32
  translated_at: 2026-09-26T09:09:22Z
  reviewed_by: null
---

# 50. Mitigated Threats — Secure CI/CD

## Summary {#sumário}

Threat families mitigated in this chapter + mitigation strength. The analysis follows the **§26 canon §4 discipline**: Manual surface + CAPEC primary; CWE supporting limited; mitigation strength explicitly labelled.

Six sections:

- **§ Manual ontology V2 entities** — canonical Threat + AntiPattern + Signal
- **§ Threat surfaces** — Manual + CAPEC primary surfaces
- **§ AntiPattern exposure mapping** — antipattern → threat exposure relations
- **§ CWE references** — supporting only (per §26 §4 discipline)
- **§ V1 overlay** — mitigation pathway where Core-mapped
- **§ Future-work register** — threat gaps registered for P8 §10

---

## § Manual ontology V2 — canonical entities (threats + antipatterns + signals) {#-manual-ontology-v2--entities-canónicas-threats--antipatterns--signals}

Total: **24 entities** (Threat × 21, AntiPattern × 2, Signal × 1) mapped to this chapter.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-111` | Execution of unauthorised code in the pipeline | normative | heuristic |
| Threat | `MT-112` | Compromise of the build environment | normative | heuristic |
| Threat | `MT-113` | Privilege escalation in the pipeline | normative | heuristic |
| Threat | `MT-114` | Unauthorised push to protected branches | normative | heuristic |
| Threat | `MT-115` | Execution of unaudited code | normative | heuristic |
| Threat | `MT-116` | Silent replacement of legitimate code | normative | heuristic |
| Threat | `MT-117` | Build forged outside the pipeline | normative | heuristic |
| Threat | `MT-118` | Injection of dynamic logic into the pipeline | normative | heuristic |
| Threat | `MT-119` | Use of insecure external components | normative | heuristic |
| Threat | `MT-120` | Leakage of secrets via logs | normative | heuristic |
| Threat | `MT-121` | Hardcoded secrets | normative | heuristic |
| Threat | `MT-122` | Reuse of secrets | normative | heuristic |
| Threat | `MT-123` | Absence of security gates | normative | heuristic |
| Threat | `MT-124` | Validations not executed | normative | heuristic |
| Threat | `MT-125` | Lack of traceability | normative | heuristic |
| Threat | `MT-126` | Bypass of controls without a trace | normative | heuristic |
| Threat | `MT-127` | Critical changes without visibility | normative | heuristic |
| Threat | `MT-128` | Promotions without a human owner | normative | heuristic |
| Threat | `MT-129` | Plausible evidence without execution | normative | heuristic |
| Threat | `MT-130` | Non-determinism of the pipeline | normative | heuristic |
| Threat | `MT-131` | Exfiltration of sensitive context | normative | heuristic |
| AntiPattern | `sem:antipattern:exposicao-excessiva-de-contexto-em-logs-e-artefactos` | excessive exposure of context in logs and artefacts | semantic | scored |
| AntiPattern | `sem:antipattern:uso-de-segredos-estaticos` | use of static secrets | semantic | scored |
| Signal | `sem:signal:sinal-automatico` | automatic signal | semantic | scored |

---

## § Threat surfaces — Manual + CAPEC primary {#-threat-surfaces--manual--capec-primary}

Canonical threat surfaces per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (strong / partial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-111` | STRIDE | Execution of unauthorised code in the pipeline | — | Secure design of pipelines; runner isolation | partial | Explicit |
| `MT-112` | STRIDE | Compromise of the build environment | — | Isolation and ephemerality of runners | partial | Explicit |
| `MT-113` | STRIDE | Privilege escalation in the pipeline | — | Hardening of pipelines | partial | Explicit |
| `MT-114` | STRIDE | Unauthorised push to protected branches | — | Secure source code management | partial | Explicit |
| `MT-115` | STRIDE | Execution of unaudited code | — | Execution policies | partial | Explicit |
| `MT-116` | STRIDE | Silent replacement of legitimate code | — | Traceability and signatures | partial | Explicit |
| `MT-117` | STRIDE | Build forged outside the pipeline | — | Integrity and provenance | partial | Explicit |
| `MT-118` | STRIDE | Injection of dynamic logic into the pipeline | — | Security of pipeline code | partial | Explicit |
| `MT-119` | STRIDE | Use of insecure external components | — | Dependency control | partial | Explicit |
| `MT-120` | STRIDE | Leakage of secrets via logs | — | Secrets management | partial | Explicit |
| `MT-121` | STRIDE | Hardcoded secrets | — | Secrets management | partial | Explicit |
| `MT-122` | STRIDE | Reuse of secrets | — | Secrets lifecycle | partial | Explicit |
| `MT-123` | STRIDE | Absence of security gates | — | Gate policies | partial | Explicit |
| `MT-124` | STRIDE | Validations not executed | — | Integrated validations | partial | Explicit |
| `MT-125` | STRIDE | Lack of traceability | — | Traceability | partial | Explicit |
| `MT-126` | STRIDE | Bypass of controls without a trace | — | Exception management | partial | Explicit |
| `MT-127` | STRIDE | Critical changes without visibility | — | Continuous governance | partial | Explicit |
| `MT-128` | STRIDE | Promotions without a human owner | — | Gates and governance | partial | Explicit |
| `MT-129` | STRIDE | Plausible evidence without execution | — | Empirical evidence | partial | Explicit |
| `MT-130` | STRIDE | Non-determinism of the pipeline | — | Reproducibility | partial | Explicit |
| `MT-131` | STRIDE | Exfiltration of sensitive context | — | Control of integrations | partial | Explicit |

---

## § AntiPattern exposure mapping {#-antipattern-exposure-mapping}

AntiPattern → Threat exposure relations per Manual ontology V2 `antipattern_threat_links.jsonl`. Each link indicates that the antipattern (when present in code/process) exposes the threat.

| AntiPattern | Exposes threat | Confidence | Justification |
|---|---|---|---|
| `uso-de-segredos-estaticos` | `MT-121` | 0.76 | alias_match, bundle_grounding, threat_label_match |

---

## § CWE references (supporting only) {#-cwe-references-supporting-only}

_(No threat with a CWE reference for this chapter.)_

---

## § V1 overlay — mitigation pathway (where Core-mapped) {#-v1-overlay--mitigation-pathway-where-core-mapped}

V1 controls/mechanisms anchored to this chapter that mitigate the threats listed above. The V1 overlay keeps the three-way routing visible per Manual ontology V2 + AppSec Core V1 + Substrate v7.

_(V1 overlay surfacing per Manual ontology V2 antipattern_exposes_threat / control_mitigates_threat relations not fully extracted in this KG state; deferred to Codex post-Run-2 delta evaluation. Consult `25-rastreabilidade.md` for V1 entity → ES grounding per chapter; mitigation pathway inferable from existing Iter 4 + Run 1 layered output.)_

---

## § Future-work register (threat gaps) {#-future-work-register-threat-gaps}

_(No threat in gap state for this chapter.)_

---

## Generation provenance {#generation-provenance}

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
