---
# Proveniência da geração: não se mostra ao leitor (extraída do corpo na v1.17.1).
sbdtoe_provenance:
  ontology_v2: 'sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml (meta.version: ''2.0'')'
  kg_state: sbd-toe-knowledge-graph master @ 5550a743bb9de205676c503da5e81863ed62ab54 (2026-05-11; commit de governação imediatamente a seguir à tag kg-v1-cycle-b-iter-3-aligned-2026-05-11 @ 482ece916cc254126894019432ebd113695365d9)
  generated_by: Manual Agent Run 2 (50-ameacas-mitigadas enrichment)
  cycle: Cycle B Run 2 — last content work pre frozen ceremony
  notes:
  - 'Threats canonical: data/entities/mitigated_threats.json (233 items)'
  - 'AntiPatterns canonical: data/publish/semantic/antipatterns.jsonl (26 items)'
  - 'Signals canonical: data/publish/semantic/signals.jsonl (23 items)'
  - 'AntiPattern→Threat relations: data/publish/semantic/antipattern_threat_links.jsonl'
  - '§26 methodology layer: 00-fundamentos/canon/26-metodologia-validacao-claims.md (Run 1 state @ a9e70c98937d41587e86712199fab46854a8d6aa)'
  - '§26 §4 discipline applied: Manual + CAPEC primary; CWE supporting only'
  - 'Mitigation strength rule: deterministic per associated_controls count + cross_chapter flag + confidence'
  - V1 overlay surfacing per Manual ontology V2 antipattern_exposes_threat / control_mitigates_threat relations não totalmente extraídas neste estado do KG; deferred a Codex post-Run-2 delta evaluation; mitigation pathway inferable from Iter 4 + Run 1 layered output
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/canon/50-ameacas-mitigadas.md
  source_sha256: 2f037805df49c5f8f6f9578a19092b27d99405f52ab019cc502b65463248356c
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: fed42428a4218d72703793302d94993c078258cfeaa082c9af683ecccdc197c8
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [appsec_core, audit_trail, chapter_role, practitioner_manual, provenance, threat, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 3ca0b795496dc73def092ef360b0b4a9480128ced36d2e14ed042b5e5a836bad
  translated_at: 2026-09-28T09:12:14Z
  stamped_at: 2026-09-28T09:12:14Z
  reviewed_by: null
---

# 50. Mitigated Threats — Containers and Images

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

Total: **18 entities** (Threat × 18, AntiPattern × 0, Signal × 0) mapped to this chapter.

| Entity type | ID | Label | Authority class | Source mode |
|---|---|---|---|---|
| Threat | `MT-149` | Vulnerable/obsolete base images | normative | heuristic |
| Threat | `MT-150` | Inclusion of insecure dependencies in the build | normative | heuristic |
| Threat | `MT-151` | Unexpected content in the build _context_ | normative | heuristic |
| Threat | `MT-152` | Insecure configurations in the Dockerfile | normative | heuristic |
| Threat | `MT-153` | Unsigned images / without verification | normative | heuristic |
| Threat | `MT-154` | Malicious substitution in the registry | normative | heuristic |
| Threat | `MT-155` | Lack of an audit trail (who built what) | normative | heuristic |
| Threat | `MT-156` | Execution as root / excessive capabilities | normative | heuristic |
| Threat | `MT-157` | Insecure mounts and volumes | normative | heuristic |
| Threat | `MT-158` | Lack of network policies | normative | heuristic |
| Threat | `MT-159` | Permissive _admission_ | normative | heuristic |
| Threat | `MT-160` | Secrets embedded in the image | normative | heuristic |
| Threat | `MT-161` | Exposure in environment variables | normative | heuristic |
| Threat | `MT-162` | Insecure manifests approved | normative | heuristic |
| Threat | `MT-163` | Image↔manifest misalignment | normative | heuristic |
| Threat | `MT-164` | Lack of traceability of deploys | normative | heuristic |
| Threat | `MT-165` | _Shadow containers_ outside the pipeline | normative | heuristic |
| Threat | `MT-166` | Configuration _drift_ | normative | heuristic |

---

## § Threat surfaces — Manual + CAPEC primary {#-threat-surfaces--manual--capec-primary}

Canonical threat surfaces per Manual + CAPEC primary anchor (per §26 §4 discipline). Mitigation strength explicitly labelled (strong / partial / dependente_de_outros_capitulos).

| Threat ID | Category | Essence | CAPEC anchor | Associated controls | Mitigation strength | §26 label |
|---|---|---|---|---|---|---|
| `MT-149` | STRIDE | Vulnerable/obsolete base images | — | *Checklist 3–4*, *Policies: Vulnerability Management*, *Traceability: SSDF RV.1* | strong | Explicit |
| `MT-150` | STRIDE | Inclusion of insecure dependencies in the build | — | Ch. 05 (SBOM/SCA), *Checklist 3–4* | partial | Explicit |
| `MT-151` | STRIDE | Unexpected content in the build _context_ | — | *Policies: Secure Image Building* | partial | Explicit |
| `MT-152` | STRIDE | Insecure configurations in the Dockerfile | — | *Checklist 6*, *Policies: Secure Building* | partial | Explicit |
| `MT-153` | STRIDE | Unsigned images / without verification | — | *Checklist 5 & 10–11*, *Policies: Signing and Provenance* | partial | Explicit |
| `MT-154` | STRIDE | Malicious substitution in the registry | — | *Traceability: SLSA/SSDF*, *Policies: Repositories* | partial | Explicit |
| `MT-155` | STRIDE | Lack of an audit trail (who built what) | — | *Checklist 14–15*, *Traceability: DSOMM Ops* | partial | Explicit |
| `MT-156` | STRIDE | Execution as root / excessive capabilities | — | *Checklist 7–9*, *Policies: Runtime Hardening* | partial | Explicit |
| `MT-157` | STRIDE | Insecure mounts and volumes | — | *Policies: Runtime Hardening* | partial | Explicit |
| `MT-158` | STRIDE | Lack of network policies | — | *Policies: Runtime*, *Checklist 8* | partial | Explicit |
| `MT-159` | STRIDE | Permissive _admission_ | — | *Checklist 11*, *Policies: Manifest Validation* | partial | Explicit |
| `MT-160` | STRIDE | Secrets embedded in the image | — | *Policies: Secrets*, *Checklist 3 & 5* | partial | Explicit |
| `MT-161` | STRIDE | Exposure in environment variables | — | *Policies: Secrets* | partial | Explicit |
| `MT-162` | STRIDE | Insecure manifests approved | — | *Checklist 11*, *Policies: Manifest Validation* | partial | Explicit |
| `MT-163` | STRIDE | Image↔manifest misalignment | — | *Traceability: SLSA*, *Checklist 2 & 10–11* | partial | Explicit |
| `MT-164` | STRIDE | Lack of traceability of deploys | — | *Checklist 14–15*, *DSOMM Ops Monitoring* | partial | Explicit |
| `MT-165` | STRIDE | _Shadow containers_ outside the pipeline | — | *Policies: Runtime/Registries*, *Traceability: DSOMM* | partial | Explicit |
| `MT-166` | STRIDE | Configuration _drift_ | — | *Policies: Runtime*, Ch. 08 (IaC) | partial | Explicit |

---

## § AntiPattern exposure mapping {#-antipattern-exposure-mapping}

_(No antipattern→threat relation mapped to this chapter.)_

---

## § CWE references (supporting only) {#-cwe-references-supporting-only}

CWE references per §26 §4: **CWE only as limited support, NOT as a substitute for a threat taxonomy**. Mapping to the Manual threats listed below.

| CWE-ID | Linked threat | Note |
|---|---|---|
| `CWE-1104` | `?` | supporting reference; the primary anchor is the Manual threat |

---

## § V1 overlay — mitigation pathway (where Core-mapped) {#-v1-overlay--mitigation-pathway-where-core-mapped}

V1 controls/mechanisms anchored to this chapter that mitigate the threats listed above. The V1 overlay keeps the three-way routing visible per Manual ontology V2 + AppSec Core V1 + Substrate v7.

_(The relations between anti-patterns, threats and controls are not yet complete in this version. Each entity's grounding in external sources is in the chapter's [Traceability](/sbd-toe/sbd-manual/containers-imagens/canon/rastreabilidade) page.)_

---

## § Future-work register (threat gaps) {#-future-work-register-threat-gaps}

_(No threat in gap state for this chapter.)_
