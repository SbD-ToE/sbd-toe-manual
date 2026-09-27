---
id: rastreabilidade
translation:
  source_locale: pt
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/canon/25-rastreabilidade.md
  source_sha256: fa082cae7e65048087cdab1a8e6b3376f0160fa55397ea2cdda07d7a81f5d0aa
  source_commit: e341b40c451d9ef4be61e6cd59d994cda54c1aa0
  target_sha256: ba0f4f9bddd77cf67709c729a3d41f6fc5a63abcbf6a1c5e1cae9ad7c88b8e09
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [appsec_core, avaliacao, chapter_role, cycle_iteration, framework_source_corpus, llm, practitioner_manual, sbdtoe_sbd, slice, traceability, validation_evaluation]
  glossary_sha256: 1e3d8181a25c1f474c228c8a1be4b50a366afc0e7798daccd42a274d83ba004d
  translated_at: 2026-09-26T13:37:00Z
  stamped_at: 2026-09-26T18:33:54Z
  reviewed_by: null
---

# 25. Traceability — Dependencies, SBOM and SCA

## Summary {#sumário}

This chapter is the **primary anchor** of the AppSec Core V1 slices: `ACO-SCBI` (Software supply chain and build integrity).

V1 entity-level coverage: **20 primary entities**. The structure below exposes the **five-section routing** (per Run 1 amendment 2026-05-11; P8 pipeline primitive demonstration):

- **§ Manual ontology V2 entities** — canonical Manual ontology V2 entities mapped to this chapter (KG canonical data)
- **§ Core-mapped coverage** — V1 entity → Manual ontology V2 anchor → Manual section anchor → §26 methodology label → ES grounding
- **§ Manual-only coverage** — Manual sections out-of-Core-scope but directly ES-grounded
- **§ Out-of-AppSec coverage** — Pure editorial sections (examples, narratives) without ES grounding
- **§ Future-work register** — Content gaps registered as P8 §10 candidates

---

## § Manual ontology V2 — canonical entities of this chapter {#-manual-ontology-v2--entities-canónicas-deste-capítulo}

Total: **63 entities** of Manual ontology V2 mapped to this chapter via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `DEP-001` | SBOM generated per build, in a standardised format | normative | explicit | deterministic |
| Requirement | `DEP-002` | SCA integrated into the pipeline with blocking by severity policy | normative | explicit | deterministic |
| Requirement | `DEP-003` | Pinned and auditable dependency versions | normative | explicit | deterministic |
| Requirement | `DEP-004` | Prohibition of dependencies introduced by manual copy | normative | explicit | deterministic |
| Requirement | `DEP-005` | Controlled registries and source repositories | normative | explicit | deterministic |
| Requirement | `DEP-006` | Formal approval for the introduction of new dependencies | normative | explicit | deterministic |
| Requirement | `DEP-007` | Update policy with an SLA defined by severity | normative | explicit | deterministic |
| Requirement | `DEP-008` | Automated update with impact analysis | normative | explicit | deterministic |
| Requirement | `DEP-009` | Detection of unintended or emergent dependencies | normative | explicit | deterministic |
| Requirement | `DEP-010` | SBOM → vulnerability → fix traceability | normative | explicit | deterministic |
| Control | `CTRL-supply-chain-inventario-e-analise-de-dependencias-6b0fd9f7fb` | Dependency inventory and analysis | normative | explicit | deterministic |
| Practice | `05-dependencias-sbom-sca:alertas-sobre-vulnerabilidades-em-componentes-usados` | Alerts on Vulnerabilities in Used Components | normative | explicit | deterministic |
| Practice | `05-dependencias-sbom-sca:auditoria-periodica-de-bibliotecas-copiadas-manualmente` | Periodic Audit of Manually Copied Libraries | normative | explicit | deterministic |
| Practice | `05-dependencias-sbom-sca:automacao-da-atualizacao-com-avaliacao-de-impacto` | Update automation with impact assessment | normative | explicit | deterministic |
| Practice | `05-dependencias-sbom-sca:excecoes-a-cves-formais-e-temporarias` | Formal and temporary CVE exceptions | normative | explicit | deterministic |
| Practice | `05-dependencias-sbom-sca:gestao-de-dependencias-seguras` | Secure dependency management | normative | explicit | deterministic |
| Practice | `05-dependencias-sbom-sca:inventario-e-controlo-de-dependencias-emergentes` | Inventory and control of emergent dependencies | normative | explicit | deterministic |
| Practice | `05-dependencias-sbom-sca:inventario-e-sbom-por-build` | Inventory and SBOM per Build | normative | explicit | deterministic |
| Practice | `05-dependencias-sbom-sca:proibir-bibliotecas-copiadas-manualmente` | Prohibit manually copied libraries | normative | explicit | deterministic |
| Practice | `05-dependencias-sbom-sca:repositorios-internos-como-fonte-unica` | Internal repositories as the single source | normative | explicit | deterministic |
| Practice | `05-dependencias-sbom-sca:sbom-em-cada-build` | SBOM on every build | normative | explicit | deterministic |
| Practice | `05-dependencias-sbom-sca:sca-automatico-com-gates` | Automatic SCA with *gates* | normative | explicit | deterministic |
| Practice | `05-dependencias-sbom-sca:validacao-automatica-de-compatibilidade-de-licencas` | Automatic Licence Compatibility Validation | normative | explicit | deterministic |
| Practice | `05-dependencias-sbom-sca:validacao-de-release-go-no-go` | Release validation (*go/no-go*) | normative | explicit | deterministic |
| Threat | `MT-073` | Inclusion of libraries with active CVEs | normative | heuristic | bounded |
| Threat | `MT-074` | Outdated dependencies | normative | heuristic | bounded |
| Threat | `MT-075` | Absence of a version record | normative | heuristic | bounded |
| Threat | `MT-076` | Inclusion of unaudited libraries | normative | heuristic | bounded |
| Threat | `MT-077` | Lack of knowledge of the libraries used | normative | heuristic | bounded |
| Threat | `MT-078` | Lack of association between vulnerability and artefact | normative | heuristic | bounded |
| Threat | `MT-079` | Lack of a history of package introduction | normative | heuristic | bounded |
| Threat | `MT-080` | Inclusion of packages from malicious repositories | normative | heuristic | bounded |
| Threat | `MT-081` | Transitive dependency with an insecure component | normative | heuristic | bounded |
| Threat | `MT-082` | Pipeline injects an unauthenticated version | normative | heuristic | bounded |
| Threat | `MT-083` | CVEs ignored without justification | normative | heuristic | bounded |
| Threat | `MT-084` | Mitigations applied without tracking | normative | heuristic | bounded |
| Threat | `MT-085` | Lack of an exception review cycle | normative | heuristic | bounded |
| Threat | `MT-086` | Arbitrary use of libraries | normative | heuristic | bounded |
| Threat | `MT-087` | Prohibited libraries are used | normative | heuristic | bounded |
| Threat | `MT-088` | Lack of a replacement policy | normative | heuristic | bounded |
| Threat | `MT-089` | Introduction of an undeclared vulnerable dependency | normative | heuristic | bounded |
| Threat | `MT-090` | Dependency confusion | normative | heuristic | bounded |
| Threat | `MT-091` | Backdoor via a build tool | normative | heuristic | bounded |
| Threat | `MT-092` | Composition drift between builds | normative | heuristic | bounded |

> Authority class / source mode / confidence model: per Manual ontology V2 definition (`sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml`, `meta.version: '2.0'`).

---

## § Core-mapped coverage {#-core-mapped-coverage}

Table exposing V1 entity-level coverage with Manual ontology V2 anchor + Manual section anchor + §26 methodology label + substrate v7 ES grounding.

### Slice `ACO-SCBI` — Software supply chain and build integrity {#slice-aco-scbi--integridade-da-supply-chain-de-software-e-do-build}

| V1 entity | Type | Manual V2 anchor | Manual section anchor | Authority | Source mode | §26 label | ES grounding |
|---|---|---|---|---|---|---|---|
| `ACM-SCBI-001` — Versioned Pipelines | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AU-1, SP800-53-AU-2.3; SAMM v2.1: SAMM-ACTIVITY-G_PC_1_A, SAMM-ACTIVITY-G_PC_3_B; PCI SSLC v1.1: PCISSLC-5.1, PCISSLC-5.2; DSOMM: DSOMM-ACTIVITY-C7D99B18C3E14D22B2E39AA9146C0B17, DSOMM-ACTIVITY-86D490B9D7984A5BA011AB9688014C46; + 4 more sources |
| `ACM-SCBI-002` — Automated Security Scanners | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-2.4, SP800-53-AC-4.28; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_A, SAMM-ACTIVITY-D_SA_1_B; DSOMM: DSOMM-ACTIVITY-67E1A9AA9FBF4EC5A2DE400F01960C51, DSOMM-ACTIVITY-8AE0B92C10E04602BA227524D6AED488; CIS Controls v8.1.2: CIS-2.4, CIS-3.13; + 15 more sources |
| `ACM-SCBI-003` — Release Promotion Gates | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-3.5; PCI DSS v4.0.1: PCI-3.7.2, PCI-3.7.3; CAPEC v3.9: CAPEC-2, CAPEC-36; SAMM v2.1: SAMM-ACTIVITY-G_EG_2_A, SAMM-ACTIVITY-I_DM_1_A; + 8 more sources |
| `ACM-SCBI-004` — Artifact Signing And Attestation | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AU-9.1, SP800-53-AU-9.3; CAPEC v3.9: CAPEC-206, CAPEC-459; ASVS v5: ASVS-REQ-V4.1.5, ASVS-REQ-V6.7.1; DSOMM: DSOMM-ACTIVITY-A340F46B63604CB8847BA0D3483D09D3, DSOMM-ACTIVITY-F3C4971E9F4D4E598ED0F0BDB6262477; + 14 more sources |
| `ACM-SCBI-005` — Build And Image Inventory Generation | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | DSOMM: DSOMM-ACTIVITY-2858AC12017940D99ACF1B839C030473, DSOMM-ACTIVITY-2A44B708734F4463B0CB86DC46344B2F; CIS Controls v8.1.2: CIS-1, CIS-1.1; MITRE ATLAS: AML.T0060, AML.M0023; SP 800-53 r5: SP800-53-CM-8, SP800-53-SR-4.4; + 3 more sources |
| `ACM-SCBI-006` — Registry Allowlisting And Approved Source Enforcement | M | Mechanism | chapter prose (enforcement, proxy, registries kws verified) | semantic | scored | Semantic | SP 800-53 r5: SP800-53-AC-3.3, SP800-53-AC-3.11; PCI DSS v4.0.1: PCI-REQ-7, PCI-1.3.2; CAPEC v3.9: CAPEC-51, CAPEC-203; CIS Controls v8.1.2: CIS-2.2, CIS-2.5; + 10 more sources |
| `ACO-SCBI-001` — Dependency Inventory And SBOM Traceability | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-CM-8, SP800-53-CM-8.1; CIS Controls v8.1.2: CIS-1, CIS-1.1; DSOMM: DSOMM-ACTIVITY-2858AC12017940D99ACF1B839C030473, DSOMM-ACTIVITY-2A44B708734F4463B0CB86DC46344B2F; SAMM v2.1: SAMM-ACTIVITY-I_SB_1_B, SAMM-ACTIVITY-O_EM_1_A; + 8 more sources |
| `ACO-SCBI-002` — Dependency Risk Evaluation And Policy Gating | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-CA-7.4, SP800-53-PM-9; NIST AI RMF 1.0: NIST-AI-RMF-GOVERN-1.3, NIST-AI-RMF-GOVERN-1.5; CIS Controls v8.1.2: CIS-15.2; EU NIS2: NIS2-ART-21; + 2 more sources |
| `ACO-SCBI-003` — Controlled Dependency And Image Sources | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-3.3, SP800-53-AC-3.9; CWE SDV v4.19.1: CWE-1220, CWE-1230; CIS Controls v8.1.2: CIS-2.5, CIS-2.6; NIST AI 100-2 e2025: NIST-AI-100-2-E2025-4.2.1; + 2 more sources |
| `ACO-SCBI-004` — Build Definition And Execution Integrity | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SAMM v2.1: SAMM-ACTIVITY-D_SA_3_A, SAMM-ACTIVITY-D_SA_3_B; DSOMM: DSOMM-ACTIVITY-F6F7737F25A943178DE209BF59F29B5B, DSOMM-ACTIVITY-9F10792761E9457485AD3F2B4BCA8665; SSDF v1.1: SSDF-PRACTICE-PO.1, SSDF-PRACTICE-PO.4; CAPEC v3.9: CAPEC-443, CAPEC-523; + 10 more sources |
| `ACO-SCBI-005` — Release Promotion And Human Approval Integrity | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-4.9, SP800-53-AC-13; CWE SDV v4.19.1: CWE-205, CWE-250; PCI DSS v4.0.1: PCI-3.7.8, PCI-7.2.3; MITRE ATLAS: AML.T0054, AML.M0029; + 7 more sources |
| `ACO-SCBI-006` — Artifact Attestation And Provenance Integrity | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-CP-9.1, SP800-53-IA-12; MITRE ATLAS: AML.TA0009, AML.T0002; DSOMM: DSOMM-ACTIVITY-F3C4971E9F4D4E598ED0F0BDB6262477, DSOMM-ACTIVITY-A854B48D83BD4F8D8621A0BDD470837F; SLSA v1.0: SLSA-BUILD-L1, SLSA-PRINCIPLE-PREFER-ATTESTATIONS; + 10 more sources |
| `ACO-SCBI-007` — Container Image Supply Integrity | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | DSOMM: DSOMM-ACTIVITY-DA4FF665DCB94E939D2048CDEDC50FC2, DSOMM-ACTIVITY-34869EAFF2E14926B0BD28C43402F057; SP 800-53 r5: SP800-53-SA-12.3, SP800-53-SI-7.4; MITRE ATLAS: AML.T0010.004, AML.M0032; EU CRA: CRA-ART-19; + 1 more sources |
| `ACP-SCBI-001` — Build-Linked SBOM Generation | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SAMM v2.1: SAMM-ACTIVITY-D_SA_2_A, SAMM-ACTIVITY-I_SB_1_A; DSOMM: DSOMM-ACTIVITY-2858AC12017940D99ACF1B839C030473, DSOMM-ACTIVITY-2A44B708734F4463B0CB86DC46344B2F; SLSA v1.0: SLSA-PRODUCER-CHOOSE-BUILD-PLATFORM, SLSA-PRODUCER-CONSISTENT-BUILD; ASVS v5: ASVS-REQ-V15.1.2; + 2 more sources |
| `ACP-SCBI-002` — Automated Dependency And Image Risk Gating | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | DSOMM: DSOMM-ACTIVITY-A340F46B63604CB8847BA0D3483D09D3, DSOMM-ACTIVITY-0DE465A655A74343AF79948BB5FF10BA; SAMM v2.1: SAMM-ACTIVITY-D_TA_1_A, SAMM-ACTIVITY-D_TA_2_A; CAPEC v3.9: CAPEC-35, CAPEC-187; SP 800-53 r5: SP800-53-CA-7.4, SP800-53-CM-5.7; + 16 more sources |
| `ACP-SCBI-003` — Approved Source And Registry Governance | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-3.11, SP800-53-AC-4.19; CIS Controls v8.1.2: CIS-2.2, CIS-2.6; SAFECode SIC: SCSIC-SOURCING, SCSIC-SOURCING-OSS; SAMM v2.1: SAMM-ACTIVITY-G_PC_1_A, SAMM-ACTIVITY-G_PC_1_B; + 7 more sources |
| `ACP-SCBI-004` — Pipeline Definition As Reviewed Code | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | OWASP LLM Top 10: LLM03-2025 |
| `ACP-SCBI-005` — Governed Promotion And Release Approval | P | Practice | chapter prose (approval, enforce, gates kws verified) | normative | explicit | Semantic | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2; PCI DSS v4.0.1: PCI-REQ-12, PCI-1.1.1; CAPEC v3.9: CAPEC-2, CAPEC-13; HIPAA: HIPAA-164-308a1, HIPAA-164-308a2; + 14 more sources |
| `ACP-SCBI-006` — Artifact Signature And Provenance Validation | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AU-10.5, SP800-53-AU-12.1; ASVS v5: ASVS-REQ-V2.1.2, ASVS-REQ-V4.1.5; DSOMM: DSOMM-ACTIVITY-9F10792761E9457485AD3F2B4BCA8665, DSOMM-ACTIVITY-830570280B774D2E813540969768AE88; PCI DSS v4.0.1: PCI-1.1.2, PCI-2.1.2; + 13 more sources |
| `ACP-SCBI-007` — Trusted Container Image Supply | P | Practice | chapter prose (build, container, policy kws verified) | normative | explicit | Semantic | SP 800-53 r5: SP800-53-AC-19.5, SP800-53-MP-5; DSOMM: DSOMM-ACTIVITY-16E39C8F5336400188EDA552D2447531, DSOMM-ACTIVITY-485A33837F2E4DBABB84479377070904; MITRE ATLAS: AML.T0010.004, AML.T0105; CWE SDV v4.19.1: CWE-426, CWE-829; + 2 more sources |

---

## § Manual-only coverage (out-of-Core-scope; ES-grounded direct) {#-manual-only-coverage-out-of-core-scope-es-grounded-direct}

Manual sections covering topics outside the scope of the V1 AppSec Core ontology (maturity models, organisational policies, KPIs/metrics, glossaries) but with direct ES grounding.

| Manual section | Manual V2 anchor | Authority | ES grounding (direct) |
|---|---|---|---|
| `achievable-maturity.md` | MaturityMapping | external | SAMM v2.1 SCA maturity; DSOMM dependency activities |
| `policies-relevantes.md` | PolicyReference | editorial / external | SBOM and Dependency Management Policy |
| `addon/10-kpis-metricas.md` | ExternalFramework | external | Operational SBOM/SCA KPIs |

---

## § Out-of-AppSec coverage (pure editorial) {#-out-of-appsec-coverage-pure-editorial}

Manual sections that are pure editorial content (worked examples, narratives, illustrative cases, vendor-specific tooling integration). No ES grounding.

| Manual section | Content type | Manual V2 anchor (if any) |
|---|---|---|
| `addon/04-integracao-ci-cd.md` | CI/CD integration examples (tooling-specific) | — |
| `addon/07-controle-registos-origem.md` | Origin registries worked examples | DocumentUnit |

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
