---
id: rastreabilidade
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/canon/25-rastreabilidade.md
  source_sha256: d403d5cadd0e0c97e6cb84c76096eae84d8f49642cebaf71bef03eeb1cf7b1d2
  source_commit: e341b40c451d9ef4be61e6cd59d994cda54c1aa0
  target_sha256: 011c0ad1d282147365a6cec0c9040da551ab0cdd9fa397a528f6efffb420c3a6
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [appsec_core, audit_trail, chapter_role, practitioner_manual, provenance, sbdtoe_sbd, slice, traceability, v1_entity_rpr_release_authorization, v1_entity_rpr_verified_artifact_promotion, validation_evaluation]
  glossary_sha256: e741e8e3090cbce63aca5cd2f76cb885d3effa4dafedbbbb3ad45d5f97a89eb8
  translated_at: 2026-09-26T13:37:08Z
  stamped_at: 2026-09-26T18:35:33Z
  reviewed_by: null
---

# 25. Traceability — Secure Deployment

## Summary {#sumário}

This chapter is the **primary anchor** of the AppSec Core V1 slices: `ACO-RPR` (Release promotion, controlled rollout and rollback readiness).

V1 entity-level coverage: **27 primary entities**. The structure below exposes the **five-section routing** (per Run 1 amendment 2026-05-11; P8 pipeline primitive demonstration):

- **§ Manual ontology V2 entities** — canonical Manual ontology V2 entities mapped to this chapter (KG canonical data)
- **§ Core-mapped coverage** — V1 entity → Manual ontology V2 anchor → Manual section anchor → §26 methodology label → ES grounding
- **§ Manual-only coverage** — Manual sections out-of-Core-scope but directly ES-grounded
- **§ Out-of-AppSec coverage** — Pure editorial sections (examples, narratives) without ES grounding
- **§ Future-work register** — Content gaps registered as P8 §10 candidates

---

## § Manual ontology V2 — canonical entities of this chapter {#-manual-ontology-v2--entities-canónicas-deste-capítulo}

Total: **58 entities** of Manual ontology V2 mapped to this chapter via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `DPL-001` | Mandatory formal approval before deployment to production | normative | explicit | deterministic |
| Requirement | `DPL-002` | Promotion only of artefacts with verified provenance | normative | explicit | deterministic |
| Requirement | `DPL-003` | Automatic security gates as a condition for promotion | normative | explicit | deterministic |
| Requirement | `DPL-004` | End-to-end traceability of each deployment | normative | explicit | deterministic |
| Requirement | `DPL-005` | Rollback configured, tested and with a defined SLA | normative | explicit | deterministic |
| Requirement | `DPL-006` | Deployment credentials with minimum scope and short life | normative | explicit | deterministic |
| Requirement | `DPL-007` | Validation in staging before promotion to production | normative | explicit | deterministic |
| Requirement | `DPL-008` | Active monitoring during and after deployment | normative | explicit | deterministic |
| Requirement | `DPL-009` | Progressive deployment with impact containment for critical applications | normative | explicit | deterministic |
| Control | `CTRL-identity-gestao-de-identidades-acessos-e-ownership-d0919c69af` | Management of identities, access and ownership | normative | explicit | deterministic |
| Control | `CTRL-infrastructure-deploy-seguro-e-reversivel-ae204be5f0` | Secure and reversible deployment | normative | explicit | deterministic |
| Control | `CTRL-secrets-gestao-de-segredos-e-identidades-operacionais-e2c86cdfe9` | Management of secrets and operational identities | normative | explicit | deterministic |
| Practice | `11-deploy-seguro:controlo-de-execucao-com-feature-flags` | Execution control with *feature flags* | normative | explicit | deterministic |
| Practice | `11-deploy-seguro:controlo-e-validacao-de-drift-operacional` | Control and validation of operational drift | normative | explicit | deterministic |
| Practice | `11-deploy-seguro:deploy-apenas-de-artefactos-assinados` | Deployment only of signed artefacts | normative | explicit | deterministic |
| Practice | `11-deploy-seguro:deploy-progressivo-com-estrategias-canary-blue-green` | Progressive *deployment* with *canary*/*blue-green* strategies | normative | explicit | deterministic |
| Practice | `11-deploy-seguro:evidencia-operacional-auditavel` | Auditable operational evidence | normative | explicit | deterministic |
| Practice | `11-deploy-seguro:gates-de-aprovacao-no-deploy` | Approval *gates* at *deployment* | normative | explicit | deterministic |
| Practice | `11-deploy-seguro:gestao-segura-de-segredos-no-deploy` | Secure secrets management at *deployment* | normative | explicit | deterministic |
| Practice | `11-deploy-seguro:monitorizacao-pos-deploy` | Post-deployment monitoring | normative | explicit | deterministic |
| Practice | `11-deploy-seguro:rastreabilidade-end-to-end` | *End-to-end* traceability | normative | explicit | deterministic |
| Practice | `11-deploy-seguro:reprodutibilidade-de-incidentes-em-runtime` | Reproducibility of incidents at runtime | normative | explicit | deterministic |
| Practice | `11-deploy-seguro:rollback-estruturado-por-tipo-binario-configuracao-bd-infra` | *Rollback* structured by type (binary, configuration, DB, infra) | normative | explicit | deterministic |
| Practice | `11-deploy-seguro:rollback-rapido-e-testado` | Fast, tested *rollback* | normative | explicit | deterministic |
| Practice | `11-deploy-seguro:separacao-entre-acao-automatica-e-autorizacao-irreversivel` | Separation between automatic action and irreversible authorisation | normative | explicit | deterministic |
| Practice | `11-deploy-seguro:validacao-em-staging-antes-da-promocao` | Validation in *staging* before promotion | normative | explicit | deterministic |
| Practice | `11-deploy-seguro:validacao-humana-obrigatoria-apos-deploy-automatizado` | Mandatory human validation after automated deployment | normative | explicit | deterministic |
| Practice | `11-deploy-seguro:validacoes-tecnicas-pre-deploy-com-gates-condicionais` | Pre-deployment technical validations with conditional *gates* | normative | explicit | deterministic |
| Practice | `11-deploy-seguro:versionamento-semantico-e-changelog-tecnico` | Semantic versioning and technical *changelog* | normative | explicit | deterministic |
| Threat | `MT-182` | Code in production without validation | normative | heuristic | bounded |
| Threat | `MT-183` | Functional activation without control | normative | heuristic | bounded |
| Threat | `MT-184` | Manual promotion outside the CI/CD | normative | heuristic | bounded |
| Threat | `MT-185` | Failed deployment without rollback | normative | heuristic | bounded |
| Threat | `MT-186` | Irreversible feature | normative | heuristic | bounded |
| Threat | `MT-187` | Failure without response | normative | heuristic | bounded |
| Threat | `MT-188` | Joint release without segmentation | normative | heuristic | bounded |
| Threat | `MT-189` | Feature exposed to all users | normative | heuristic | bounded |
| Threat | `MT-190` | Lack of operational validation | normative | heuristic | bounded |
| Threat | `MT-191` | Undetected post-deployment failures | normative | heuristic | bounded |
| Threat | `MT-192` | Late response to critical problems | normative | heuristic | bounded |
| Threat | `MT-193` | Critical events ignored | normative | heuristic | bounded |
| Threat | `MT-194` | Toggle activated inadvertently | normative | heuristic | bounded |
| Threat | `MT-195` | Release without geographical or logical segmentation | normative | heuristic | bounded |
| Threat | `MT-196` | Execution of a non-validated critical function | normative | heuristic | bounded |

> Authority class / source mode / confidence model: per Manual ontology V2 definition (`sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml`, `meta.version: '2.0'`).

---

## § Core-mapped coverage {#-core-mapped-coverage}

Table exposing V1 entity-level coverage with Manual ontology V2 anchor + Manual section anchor + §26 methodology label + substrate v7 ES grounding.

### Slice `ACO-RPR` — Release promotion, controlled rollout and rollback readiness {#slice-aco-rpr--release-promotion-rollout-controlado-e-readiness-para-rollback}

| V1 entity | Type | Manual V2 anchor | Manual section anchor | Authority | Source mode | §26 label | ES grounding |
|---|---|---|---|---|---|---|---|
| `ACM-RPR-001` — Release Promotion Controls | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-3.9, SP800-53-AC-22; CAPEC v3.9: CAPEC-677; SAFECode SIC: SCSIC-SOURCING |
| `ACM-RPR-002` — Approval Gates And Separation Of Signal From Promotion Decision | M | Mechanism | chapter prose (gate, gates, promotion kws verified) | semantic | scored | Semantic | SP 800-53 r5: SP800-53-MA-2, SP800-53-MA-3; CWE SDV v4.19.1: CWE-184, CWE-807; NIST AI RMF 1.0: NIST-AI-RMF-GOVERN-1.6, NIST-AI-RMF-GOVERN-1.7; MITRE ATLAS: AML.M0029; + 1 more sources |
| `ACM-RPR-003` — Provenance And Signature Verification At Promotion | M | Mechanism | chapter prose (identity, promotion, provenance kws verified) | semantic | scored | Semantic | SP 800-53 r5: SP800-53-AU-10.5, SP800-53-CM-14; SLSA v1.0: SLSA-BUILD-L1, SLSA-BUILD-L2; ASVS v5: ASVS-REQ-V4.1.5, ASVS-REQ-V6.7.1; CAPEC v3.9: CAPEC-459, CAPEC-475; + 10 more sources |
| `ACM-RPR-004` — Rollback And Containment Controls | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-CM-2.3, SP800-53-CM-3; CIS Controls v8.1.2: CIS-3, CIS-3.1; SAMM v2.1: SAMM-ACTIVITY-D_SR_3_B, SAMM-ACTIVITY-I_DM_1_A; DSOMM: DSOMM-ACTIVITY-A511799B045E4B9698437D63D8C1E2AD, DSOMM-ACTIVITY-C72DA77986CC45B1A339190CE5093171; + 7 more sources |
| `ACM-RPR-005` — Deployment Pipeline Traceability And Audit Controls | M | Mechanism | chapter prose (audit, deploy, deployment kws verified) | semantic | scored | Semantic | DSOMM: DSOMM-ACTIVITY-F6F7737F25A943178DE209BF59F29B5B, DSOMM-ACTIVITY-A340F46B63604CB8847BA0D3483D09D3; SP 800-53 r5: SP800-53-AU-2, SP800-53-AU-6.3; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_B, SAMM-ACTIVITY-I_SB_1_B; CIS Controls v8.1.2: CIS-1, CIS-8.1; + 12 more sources |
| `ACM-RPR-008` — Baseline Configuration Template Or Policy Bundle | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-CM-1, SP800-53-CM-2; SAMM v2.1: SAMM-ACTIVITY-D_SR_3_A, SAMM-ACTIVITY-I_SB_1_A; CAPEC v3.9: CAPEC-523, CAPEC-524; CIS Controls v8.1.2: CIS-4.1, CIS-4.2; + 2 more sources |
| `ACM-RPR-009` — Gate Or Policy Check For Prohibited Or Unsafe Overrides | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2.11; PCI DSS v4.0.1: PCI-REQ-1, PCI-REQ-5; CAPEC v3.9: CAPEC-2, CAPEC-13; ASVS v5: ASVS-REQ-V2.2.1, ASVS-REQ-V2.2.2; + 15 more sources |
| `ACM-RPR-010` — Change Review Control For Security-Relevant Baseline Deviations | M | Mechanism | chapter prose (baseline, change, record kws verified) | semantic | scored | Semantic | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2; CIS Controls v8.1.2: CIS-3.1, CIS-3.2; SAMM v2.1: SAMM-ACTIVITY-D_TA_3_A, SAMM-ACTIVITY-G_EG_3_A; PCI DSS v4.0.1: PCI-6.2.3, PCI-6.5.1; + 7 more sources |
| `ACO-RPR-001` — Release Authorization And Irreversible Change Accountability | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-14; CIS Controls v8.1.2: CIS-2.2, CIS-2.5; CWE SDV v4.19.1: CWE-212, CWE-283; PCI SSLC v1.1: PCISSLC-5.1, PCISSLC-7.1; + 4 more sources |
| `ACO-RPR-002` — Verified Artifact Promotion | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SLSA v1.0: SLSA-BUILD-L1, SLSA-BUILD-L2; SP 800-53 r5: SP800-53-MP-3, SP800-53-SA-3.2; CAPEC v3.9: CAPEC-523, CAPEC-524; SSDF v1.1: SSDF-PRACTICE-PS.2, SSDF-TASK-PS.2.1; + 9 more sources |
| `ACO-RPR-003` — Pre-Promotion Security Gates And Staging Assurance | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | MITRE ATLAS: AML.T0054 |
| `ACO-RPR-004` — End-to-End Deployment Traceability | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | DSOMM: DSOMM-ACTIVITY-67E1A9AA9FBF4EC5A2DE400F01960C51, DSOMM-ACTIVITY-2A44B708734F4463B0CB86DC46344B2F; SP 800-53 r5: SP800-53-IR-5, SP800-53-MA-2; SAMM v2.1: SAMM-ACTIVITY-I_SB_1_B, SAMM-ACTIVITY-I_SB_3_A; ASVS v5: ASVS-REQ-V13.4.4, ASVS-REQ-V13.4.5; + 8 more sources |
| `ACO-RPR-005` — Tested Rollback Readiness And Reversibility | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-CM-2.3, SP800-53-CP-2; CIS Controls v8.1.2: CIS-7.7, CIS-11.5; EU DORA: DORA-ART-12 |
| `ACO-RPR-006` — Controlled Rollout And Blast-Radius Containment | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-PE-3.6 |
| `ACO-RPR-007` — Release Promotion And Reversible Rollout Assurance | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-3.9, SP800-53-MP-8.3; CAPEC v3.9: CAPEC-439; CIS Controls v8.1.2: CIS-4.11; CWE SDV v4.19.1: CWE-1341; + 3 more sources |
| `ACO-RPR-008` — Secure Defaults And Hardened Baseline Selection | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | CWE SDV v4.19.1: CWE-1188; DSOMM: DSOMM-ACTIVITY-5992C38C8597403589DBD15820D81C3A; SAMM v2.1: SAMM-ACTIVITY-I_SB_3_A; PCI DSS v4.0.1: PCI-2.2.2; + 1 more sources |
| `ACO-RPR-009` — Security-Relevant Configuration Integrity And Override Control | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-2, SP800-53-AC-2.6; CAPEC v3.9: CAPEC-12, CAPEC-13; PCI DSS v4.0.1: PCI-REQ-1, PCI-REQ-2; CIS Controls v8.1.2: CIS-2.6, CIS-3; + 21 more sources |
| `ACO-RPR-010` — Baseline Review, Exception Visibility And Change Discipline | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AU-2, SP800-53-AU-6; SAMM v2.1: SAMM-ACTIVITY-D_TA_3_A, SAMM-ACTIVITY-G_EG_3_A; PCI DSS v4.0.1: PCI-10.3.4, PCI-10.4.1; SSDF v1.1: SSDF-TASK-PO.4.1, SSDF-TASK-PW.7.2; + 11 more sources |
| `ACP-RPR-001` — Accountable Release Approval | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AT-1, SP800-53-AU-1; SAMM v2.1: SAMM-ACTIVITY-D_TA_2_A, SAMM-ACTIVITY-G_EG_2_A; CIS Controls v8.1.2: CIS-17.3; CWE SDV v4.19.1: CWE-283; + 2 more sources |
| `ACP-RPR-002` — Verified Artifact Promotion | P | Practice | chapter prose (artefact, identity, promotion kws verified) | normative | explicit | Semantic | SP 800-53 r5: SP800-53-AU-10.5, SP800-53-IA-4.3; ASVS v5: ASVS-REQ-V4.1.5, ASVS-REQ-V6.7.1; SLSA v1.0: SLSA-BUILD-L1, SLSA-BUILD-L2; CAPEC v3.9: CAPEC-476, CAPEC-523; + 9 more sources |
| `ACP-RPR-003` — Pre-Promotion Gates And Staging Validation | P | Practice | chapter prose (gate, gates, policy kws verified) | normative | explicit | Semantic | ASVS v5: ASVS-REQ-V2.3.1, ASVS-REQ-V2.3.4; MITRE ATLAS: AML.M0020; SP 800-53 r5: SP800-53-CP-12 |
| `ACP-RPR-004` — End-to-End Deploy Traceability | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | DSOMM: DSOMM-ACTIVITY-F6F7737F25A943178DE209BF59F29B5B, DSOMM-ACTIVITY-A340F46B63604CB8847BA0D3483D09D3; SP 800-53 r5: SP800-53-CM-8.2, SP800-53-CM-8.7; SAMM v2.1: SAMM-ACTIVITY-I_SB_1_B, SAMM-ACTIVITY-I_SB_2_A; ASVS v5: ASVS-REQ-V13.4.4, ASVS-REQ-V13.4.5; + 10 more sources |
| `ACP-RPR-005` — Tested Rollback Discipline | P | Practice | chapter prose (production, rollback, rollout kws verified) | normative | explicit | Semantic | CIS Controls v8.1.2: CIS-11, CIS-11.1; SP 800-53 r5: SP800-53-CM-2.3, SP800-53-CP-4.4; SAMM v2.1: SAMM-ACTIVITY-O_EM_3_A, SAMM-ACTIVITY-O_OM_3_A; SAFECode FPSSD: SCFPSSD-TESTING |
| `ACP-RPR-006` — Progressive Rollout And Containment | P | Practice | chapter prose (change, progressive, rollout kws verified) | normative | explicit | Semantic | EU DORA: DORA-ART-5 |
| `ACP-RPR-008` — Define Hardened Baseline Profiles For Security-Relevant Components | P | Practice | chapter prose (baseline, components, define kws verified) | normative | explicit | Semantic | SP 800-53 r5: SP800-53-AC-16, SP800-53-AC-16.7; SAMM v2.1: SAMM-ACTIVITY-D_SR_2_A, SAMM-ACTIVITY-D_SR_3_A; DSOMM: DSOMM-ACTIVITY-47419324E263415B815DE7161B6B905E, DSOMM-ACTIVITY-B597928E54D648A5A8068003DCD56AAB; PCI DSS v4.0.1: PCI-REQ-2, PCI-REQ-8; + 9 more sources |
| `ACP-RPR-009` — Review Security-Relevant Overrides Before Promotion Or Deployment | P | Practice | chapter prose (change, deployment, promotion kws verified) | normative | explicit | Semantic | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-3; PCI DSS v4.0.1: PCI-REQ-12, PCI-1.2.7; CIS Controls v8.1.2: CIS-4.1, CIS-4.2; CAPEC v3.9: CAPEC-69, CAPEC-122; + 14 more sources |
| `ACP-RPR-010` — Record And Periodically Review Exceptions Against The Intended Baseline | P | Practice | chapter prose (baseline, record, review kws verified) | normative | explicit | Semantic | SP 800-53 r5: SP800-53-AC-2, SP800-53-AC-2.12; CIS Controls v8.1.2: CIS-3.1, CIS-3.8; PCI DSS v4.0.1: PCI-6.5.2, PCI-9.3.1; ASVS v5: ASVS-REQ-V7.5.1, ASVS-REQ-V14.2.7; + 11 more sources |

---

## § Manual-only coverage (out-of-Core-scope; ES-grounded direct) {#-manual-only-coverage-out-of-core-scope-es-grounded-direct}

Manual sections covering topics outside the scope of the V1 AppSec Core ontology (maturity models, organisational policies, KPIs/metrics, glossaries) but with direct ES grounding.

| Manual section | Manual V2 anchor | Authority | ES grounding (direct) |
|---|---|---|---|
| `achievable-maturity.md` | MaturityMapping | external | SAMM v2.1 OE maturity; DSOMM deploy activities |
| `policies-relevantes.md` | PolicyReference | editorial / external | Secure Deployment Policy |

---

## § Out-of-AppSec coverage (pure editorial) {#-out-of-appsec-coverage-pure-editorial}

Manual sections that are pure editorial content (worked examples, narratives, illustrative cases, vendor-specific tooling integration). No ES grounding.

| Manual section | Content type | Manual V2 anchor (if any) |
|---|---|---|
| `addon/04-incident-response-playbook.md` | IR playbooks examples | DocumentUnit |

---

## § Future-work register (P8 §10 candidates) {#-future-work-register-p8-10-candidates}

_(No entries in the future-work register for this chapter.)_

---

## Generation provenance {#generation-provenance}

- **Manual ontology V2 canonical:** `sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml` (`meta.version: '2.0'`)
- **KG canonical state:** sbd-toe-knowledge-graph master @ `5550a74` (`kg-v1-cycle-b-iter-3-aligned-2026-05-11`)
- **Substrate version:** v7 (SUPPLIER sha256 `596783ed984d9c0e8c8ef6439a0eaee8fbaf2d863af37138cde8fad55d62be04`)
- **V1 entity index:** `ontology-v1.1-fair-baseline` @ `84fe8bf` in sbd-toe-ontology
- **Per-entity source map:** `data/p8_inputs/per_entity_source_map.json` @ ESI commit `aa3c13c`
- **Phase 2/3 gap analysis:** `phase2_3_per_entity_classification.json` @ ESI commit `b8cd401`
- **Generated by:** Manual Agent Run 1 (Iter 4 baseline @ `16dfa5ae` + Manual ontology V2 vocab layer injection)
- **Format:** 5-section (Manual V2 entities + Core-mapped + Manual-only + Out-of-AppSec + Future-work) per dispatch vision 2026-05-11
- **§26 methodology labels:** per `00-fundamentos/canon/26-metodologia-validacao-claims.md` (post Run 1 Step 0 refresh)
- **Cycle:** Cycle B Run 1 (post Iter 4)
