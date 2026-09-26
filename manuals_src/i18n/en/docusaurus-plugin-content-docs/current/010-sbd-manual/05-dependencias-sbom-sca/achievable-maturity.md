---
id: achievable-maturity
translation:
  source_locale: pt
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/achievable-maturity.md
  source_sha256: f17470aed1432b27f2b37f1f870c1179da0e5c10db78ffdda4ecd21f5d014f74
  source_commit: e341b40c451d9ef4be61e6cd59d994cda54c1aa0
  target_sha256: 2563ffd11157c28e87bd38f603b0fa5f49087efc5dd92560f2094d6865e36c01
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [chapter_role, framework_source_corpus, maturity, practitioner_manual, provenance, sbdtoe_sbd, shacl_owl, traceability, validation_evaluation]
  glossary_sha256: c549f75e0f101e1e0301dde3ae439a4c8223117053e0bb967c29e3b829cc38b3
  translated_at: 2026-09-26T13:36:59Z
  reviewed_by: null
---

# Achievable Maturity — Dependencies, SBOM and SCA

## Summary {#sumário}

Credible maturity posture attainable if this chapter is implemented as written. The analysis follows the **§26 canon §4 discipline**: SAMM v2.1 + DSOMM are the primary sources; SLSA only where it makes sense as a build/integrity progression; **regulatory alignment is NOT a maturity score** and is recorded in § Out-of-Maturity scope.

Five sections:

- **§ Manual ontology V2 entities** — relevant MaturityMapping + Practice + Control entities
- **§ SAMM v2 / DSOMM maturity progression** — primary maturity sources per §26 §4
- **§ SLSA build/integrity progression** — where applicable to this chapter
- **§ Out-of-Maturity scope** — regulatory alignment (NOT a maturity score)
- **§ Future-work register** — maturity gaps registered for P8 §10

---

## § Manual ontology V2 — entities relevant to maturity {#-manual-ontology-v2--entities-relevantes-para-maturity}

Total: **12 MaturityMapping entities** mapped to this chapter (via `sbd-toe-knowledge-graph/data/entities/maturity_mappings.json`).

| Entity type | ID | Framework | Framework area | Authority class | Source mode |
|---|---|---|---|---|---|
| MaturityMapping | `05-dependencias-sbom-sca:maturity:owasp-dsomm:owasp-dsomm-policy-build-deploy-tooling:build-deploy` | OWASP DSOMM | Policy, Build & Deploy, Tooling | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:owasp-dsomm:owasp-dsomm-policy-build-deploy-tooling:policy` | OWASP DSOMM | Policy, Build & Deploy, Tooling | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:owasp-dsomm:owasp-dsomm-policy-build-deploy-tooling:tooling` | OWASP DSOMM | Policy, Build & Deploy, Tooling | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Risk policies, hardening, CI/CD blocking, SCA traceability | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:owasp-samm:owasp-samm-construction-dependency-management:1` | OWASP SAMM | Construction → Dependency Management | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:owasp-samm:owasp-samm-construction-dependency-management:2` | OWASP SAMM | Construction → Dependency Management | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:owasp-samm:owasp-samm-construction-dependency-management:3` | OWASP SAMM | Construction → Dependency Management | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | SBOM, acceptance policies, exceptions, validation and blocking | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:slsa:slsa-provenance-dependency-control:1` | SLSA | Provenance & Dependency Control | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:slsa:slsa-provenance-dependency-control:2` | SLSA | Provenance & Dependency Control | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:slsa:slsa-provenance-dependency-control:3` | SLSA | Provenance & Dependency Control | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | SBOM, pinning, dependency provenance | external | derived |

---

## § SAMM v2 / DSOMM maturity progression {#-samm-v2--dsomm-maturity-progression}

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per the `confidence` field of the KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Policy, Build & Deploy, Tooling | Generation and publication of an SBOM with integration into the pipeline | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Policy, Build & Deploy, Tooling | Formal definition of acceptance criteria and exceptions | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | Policy, Build & Deploy, Tooling | Recommended tools for SCA, validation of findings | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP DSOMM | — | Risk policies, hardening, CI/CD blocking, SCA traceability | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Construction → Dependency Management | Manual identification and listing of dependencies | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Construction → Dependency Management | Formal process for risk acceptance, tracking and control | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | Construction → Dependency Management | Automation and continuous integration | `achievable-maturity.md` | 0.90 | Explicit |
| OWASP SAMM | — | SBOM, acceptance policies, exceptions, validation and blocking | `achievable-maturity.md` | 0.90 | Explicit |

---

## § SLSA build/integrity progression {#-slsa-buildintegrity-progression}

SLSA progression mapping (per §26 §4: SLSA only where it makes sense as a build/integrity progression — this chapter qualifies).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Provenance & Dependency Control | — | SBOM generated per build | `achievable-maturity.md` | Explicit |
| Provenance & Dependency Control | — | Formal control criteria | `achievable-maturity.md` | Explicit |
| Provenance & Dependency Control | — | Out of scope (see Ch. 06 and 08) | `achievable-maturity.md` | Explicit |
| — | — | SBOM, pinning, dependency provenance | `achievable-maturity.md` | Explicit |

---

## § Out-of-Maturity scope (regulatory alignment is NOT maturity) {#-out-of-maturity-scope-regulatory-alignment-não-maturity}

Per the §26 §4 discipline: regulatory alignment (PCI DSS, GDPR, NIS2, DORA, CRA, HIPAA) **must NOT be treated as a maturity score**. Regulatory items are recorded here for editorial visibility; conformance lives in separate obligations, not in the maturity progression.

_(Regulatory alignment for this chapter is handled via Manual ontology V2 ExternalObligation entities + the governance chapters (Ch. 14); not enumerated here to avoid conflation with the maturity claim.)_

---

## § Future-work register (maturity gaps) {#-future-work-register-maturity-gaps}

_(No maturity claim in gap state for this chapter.)_

---

## Generation provenance {#generation-provenance}

- **Manual ontology V2 canonical:** `sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml` (`meta.version: '2.0'`)
- **KG canonical state:** sbd-toe-knowledge-graph master @ `5550a74`
- **Maturity mappings:** `data/entities/maturity_mappings.json` (168 items)
- **§26 methodology layer:** `00-fundamentos/canon/26-metodologia-validacao-claims.md` (Run 1 state @ a9e70c98)
- **§26 label rule:** deterministic per the `confidence` field (≥0.85 Explicit; ≥0.65 Semantic; ≥0.4 Partial; &lt;0.4 Gap)
- **§26 §4 discipline applied:** SAMM/DSOMM primary; SLSA conditional; regulatory ≠ maturity
- **Generated by:** Manual Agent Run 2 (achievable-maturity enrichment)
- **Cycle:** Cycle B Run 2 — last content work pre frozen ceremony
