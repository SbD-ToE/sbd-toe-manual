---
id: metodologia-validacao-claims
title: Claim Validation Methodology
description: Method used to validate claims of traceability, maturity and mitigated threats in the SbD-ToE manual
sidebar_position: 26
tags: [metodologia, rastreabilidade, maturidade, ameacas, ontology, knowledge-graph]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/canon/26-metodologia-validacao-claims.md
  source_sha256: 7681d08bed213e5403b087c69a93867d81c23fe1349204ce47bcee683ed6825e
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 3b616fba8b992f0a26a64319050f2a472326274b861f6618c96878049acebf7a
  engine: claude-fable-5-1
  prompt_sha256: 13029ebd6497cb63207d12577bb94bbd3b20a5d9c8d3ebd2e4a450d20a45a251
  terms_sha256: 779fcd2406a1a730ed65de83e52df7743a50456cc35d31f9ce5b9d1c8073cd3d
  translated_at: 2026-09-25T16:51:44Z
  reviewed_by: null
---

# Claim Validation Methodology

This note describes the common method used to underpin the canonical documents of:

- `25-rastreabilidade`
- `achievable-maturity`
- `50-ameacas-mitigadas`

The aim is not to replace the authors' technical judgement, but to make **explicit and auditable** how the claims in these documents were reviewed, validated, bounded where necessary and corrected.

---

## 1. The authors' empirical baseline {#1-baseline-empírica-dos-autores}

The starting point of the manual is a baseline that is **empirical and built by the authors**.

This means that:

- the structure of the chapters was built by the authors on the basis of real AppSec, DevSecOps, governance and operations practice
- the controls, examples, addons and application flows were not generated automatically from external frameworks
- the base semantics of the manual precede and guide the external mapping, not the other way round

For this reason, the canonical documents must not be read as a mere mechanical conversion of frameworks into editorial text.

---

## 2. Validation by semantic chunking and ontological backtrace {#2-validação-por-chunking-semântico-e-backtrace-ontológico}

After the empirical baseline, the claims were reviewed with the support of the `knowledge-graph` V2.

The canonical Manual ontology V2 lives in `sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml` (`meta.version: '2.0'`, status `current`). It defines 15 entity types: Requirement, Control, Practice, PracticeAssignment, Artifact, Threat, Role, SDLCPhase, UserStory, EvidencePattern, Concept, Mechanism, Pattern, AntiPattern, Signal. For each entity, V2 declares: **authority class** (normative / editorial / semantic / operational / external), **source mode** (explicit / derived / scored / heuristic / runtime) and **confidence model** (deterministic / bounded / probabilistic).

The validation uses, among others, these artefacts:

- Manual ontology V2 canonical: `sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml`
- `ontology_discovery_units.jsonl`
- `canonical_chunks.jsonl`
- semantic indexes derived from the complete manual
- runtime and overlay published in the `knowledge-graph`

In practice, this makes it possible to:

- locate relevant normative units by chapter
- check whether an editorial claim has a backtrace to concrete headings, addons, lifecycle stories or catalogues
- distinguish between explicit presence, semantic presence, partial presence and real absence

---

## 3. Comparison with mapped external sources {#3-comparação-com-fontes-externas-mapeadas}

The manual's claims were further confronted with pilots and artefacts from the `external-sources-inventory` repository.

Depending on the document type, outputs such as the following were used:

- `appsec_core_normalization.json` (canonical AppSec Core V1 substrate v7 grounding; supersedes earlier surface)
- AppSec Core V1 ontology @ `sbd-toe-ontology` tag `ontology-v1.1-fair-baseline` (`84fe8bf`)
- KG runtime @ `sbd-toe-knowledge-graph` master @ `5550a74` (tag `kg-v1-cycle-b-iter-3-aligned-2026-05-11`)
- `ExternalSourcesInventory/data/p8_gap_analysis/coverage_v1_to_manual.json` + `coverage_manual_to_v1.json` (Cartographer Phase 1)
- `ExternalSourcesInventory/data/p8_inputs/per_entity_source_map.json` (Cartographer per-entity source coverage @ commit `aa3c13c`)
- `ExternalSourcesInventory/data/p8_gap_analysis/phase2_3/phase2_3_per_entity_classification.json` (Cartographer Phase 2/3 refined classifications @ commit `b8cd401`)
- published threat surface comparisons
- published regulatory overlays (`DORA`, `NIS2`, `CRA`, `RGPD`)

This step does not serve to "make the manual identical to the sources", but to:

- validate whether the editorial claim is materially supported
- identify `claim gaps`
- identify `cross-reference gaps`
- separate a real `content gap` from a `scope boundary`

---

## 4. Reading rule by document type {#4-regra-de-leitura-por-tipo-de-documento}

### `25-rastreabilidade` {#25-rastreabilidade}

Here the main question is:

- which frameworks or external sources this chapter supports
- and with what type of coverage

Claims must be classified explicitly, for example as:

- `Explícito`
- `Semântico`
- `Parcial`
- `Reparação`
- `Gap`
- `Scope boundary`, where applicable

### `achievable-maturity` {#achievable-maturity}

Here the main question is:

- if this chapter is implemented as written, what maturity posture is it credible to reach

The reading must be bounded and explicit. In particular:

- `SAMM` and `DSOMM` are primary sources
- `SLSA` should only be used where it makes sense as a build/integrity progression
- regulatory alignment must not be treated as a maturity score

### `50-ameacas-mitigadas` {#50-ameacas-mitigadas}

Here the main question is:

- which threat families or attack patterns this chapter mitigates
- and whether the mitigation is strong, partial or dependent on other chapters

The reading must be based above all on:

- the manual's own threat surfaces
- `CAPEC`
- `CWE` only as limited support, not as a substitute for a threat taxonomy

---

## 5. What the method avoids {#5-o-que-o-método-evita}

This method exists precisely to avoid four frequent editorial errors:

1. promoting weak semantic presence to full coverage
2. confusing regulatory alignment with maturity
3. confusing practice frameworks with threat catalogues
4. erasing the authors' empirical baseline in favour of a purely framework-driven reconstruction

---

## 6. Editorial formula in brief {#6-fórmula-editorial-resumida}

The rule used should be read as follows:

1. the authors' empirical baseline
2. review by semantic chunking and ontology backtrace
3. confrontation with pilots and mapped external sources
4. explicit exposure of claims that are bounded, partial or under repair

---

## 7. Short rule for use in the canonical documents {#7-regra-curta-para-usar-nos-documentos-canónicos}

Whenever a `25-rastreabilidade`, `achievable-maturity` or
`50-ameacas-mitigadas` document makes a material claim, the correct reading must be:

1. there is an empirical baseline in the manual
2. the claim was confronted with the semantic indexes of the `knowledge-graph`
3. the claim was reviewed against the external sources relevant to that document type
4. the claim is exposed as explicit, semantic, partial, under repair or out of scope

---

## 8. Conclusion {#8-conclusão}

The `25-rastreabilidade`, `achievable-maturity` and `50-ameacas-mitigadas` documents must be read as **validated editorial artefacts**, not as automatically generated tables.

The method combines:

- empirical authorship of the manual
- factual validation through semantic indexes
- structured comparison with external sources
- explicit discipline of boundary and claim calibration

---

## 9. Operational pipeline primitive (Cycle B closure 2026-05-11) {#pipeline-primitive}

From Cycle B onwards (closure 2026-05-11), the method was reframed as an **operational pipeline primitive** — not merely an Editorial Feedback cycle, but a reusable production pipeline that combines four distinct layers:

1. **Manual ontology V2** (semi-formal YAML; structural backbone) — defines entity types, authority classes, source modes and confidence model. Canonical in `sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml`.
2. **AppSec Core V1 overlay** (ES grounding mediation) — provides per-entity mediation between Manual ontology V2 entities and the external substrate via `ExternalSourcesInventory/data/p8_inputs/per_entity_source_map.json`. Anchor: `sbd-toe-ontology` tag `ontology-v1.1-fair-baseline`.
3. **Substrate v7** (P7 normalisation output) — corpus of external sources normalised by the P7 pipeline with GROUNDED / LabDepthPending / out-of-scope classification. Anchor: `ExternalSourcesInventory` tag `cycle-a-frozen-2026-05-08`.
4. **§26 methodology layer** (claim quality discipline) — this note; classifies each claim as Explicit / Semantic / Partial / Repair / Gap / Scope boundary.

Combined, the layers produce **Manual + KG frozen joint snapshots** per cycle (e.g. Cycle B 2026-05-11). Each cycle is an **instantiation** of the pipeline; future cycles can re-run against updated substrate / V1 / Manual states without restructuring.

**Stream 2 future work** (P8 §10 future-work register): Manual ontology V2 OWL+SHACL formalisation + operational corpus validation pipeline.
