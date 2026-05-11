# 25. Rastreabilidade — Dependências, SBOM e SCA

## Sumário

Este capítulo é a **âncora primária** das slices AppSec Core V1: `ACO-SCBI` (Integridade da supply chain de software e do build).

Cobertura V1 entity-level: **20 entidades** primárias. Estrutura abaixo expõe four-way routing (per P8 pipeline primitive demonstration 2026-05-11):

- **§ Core-mapped coverage** — V1 entity → Manual section anchor → ES grounding
- **§ Manual-only coverage** — Manual sections out-of-Core-scope mas com ES grounding direct
- **§ Out-of-AppSec coverage** — Pure editorial sections (examples, narratives) sem ES grounding
- **§ Future-work register** — Content gaps registered as P8 §10 candidates

---

## § Core-mapped coverage

Tabela exposing V1 entity-level coverage with Manual section anchor + substrate v7 ES grounding. Three-way alignment per row: V1 (ontology) ↔ Manual (prose) ↔ ES (substrate).

### Slice `ACO-SCBI` — Integridade da supply chain de software e do build

| V1 entity | Type | Manual section anchor | ES grounding |
|---|---|---|---|
| `ACM-SCBI-001` — Versioned Pipelines | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-AU-1, SP800-53-AU-2.3; SAMM v2.1: SAMM-ACTIVITY-G_PC_1_A, SAMM-ACTIVITY-G_PC_3_B; PCI SSLC v1.1: PCISSLC-5.1, PCISSLC-5.2; DSOMM: DSOMM-ACTIVITY-C7D99B18C3E14D22B2E39AA9146C0B17, DSOMM-ACTIVITY-86D490B9D7984A5BA011AB9688014C46; + 4 more sources |
| `ACM-SCBI-002` — Automated Security Scanners | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-AC-2.4, SP800-53-AC-4.28; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_A, SAMM-ACTIVITY-D_SA_1_B; DSOMM: DSOMM-ACTIVITY-67E1A9AA9FBF4EC5A2DE400F01960C51, DSOMM-ACTIVITY-8AE0B92C10E04602BA227524D6AED488; CIS Controls v8.1.2: CIS-2.4, CIS-3.13; + 15 more sources |
| `ACM-SCBI-003` — Release Promotion Gates | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-3.5; PCI DSS v4.0.1: PCI-3.7.2, PCI-3.7.3; CAPEC v3.9: CAPEC-2, CAPEC-36; SAMM v2.1: SAMM-ACTIVITY-G_EG_2_A, SAMM-ACTIVITY-I_DM_1_A; + 8 more sources |
| `ACM-SCBI-004` — Artifact Signing And Attestation | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-AU-9.1, SP800-53-AU-9.3; CAPEC v3.9: CAPEC-206, CAPEC-459; ASVS v5: ASVS-REQ-V4.1.5, ASVS-REQ-V6.7.1; DSOMM: DSOMM-ACTIVITY-A340F46B63604CB8847BA0D3483D09D3, DSOMM-ACTIVITY-F3C4971E9F4D4E598ED0F0BDB6262477; + 14 more sources |
| `ACM-SCBI-005` — Build And Image Inventory Generation | M | addon/00-catalogo-requisitos.md (mechanism) | DSOMM: DSOMM-ACTIVITY-2858AC12017940D99ACF1B839C030473, DSOMM-ACTIVITY-2A44B708734F4463B0CB86DC46344B2F; CIS Controls v8.1.2: CIS-1, CIS-1.1; MITRE ATLAS: AML.T0060, AML.M0023; SP 800-53 r5: SP800-53-CM-8, SP800-53-SR-4.4; + 3 more sources |
| `ACM-SCBI-006` — Registry Allowlisting And Approved Source Enforcement | M | chapter prose (enforcement, proxy, registries kws verified) | SP 800-53 r5: SP800-53-AC-3.3, SP800-53-AC-3.11; PCI DSS v4.0.1: PCI-REQ-7, PCI-1.3.2; CAPEC v3.9: CAPEC-51, CAPEC-203; CIS Controls v8.1.2: CIS-2.2, CIS-2.5; + 10 more sources |
| `ACO-SCBI-001` — Dependency Inventory And SBOM Traceability | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-CM-8, SP800-53-CM-8.1; CIS Controls v8.1.2: CIS-1, CIS-1.1; DSOMM: DSOMM-ACTIVITY-2858AC12017940D99ACF1B839C030473, DSOMM-ACTIVITY-2A44B708734F4463B0CB86DC46344B2F; SAMM v2.1: SAMM-ACTIVITY-I_SB_1_B, SAMM-ACTIVITY-O_EM_1_A; + 8 more sources |
| `ACO-SCBI-002` — Dependency Risk Evaluation And Policy Gating | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-CA-7.4, SP800-53-PM-9; NIST AI RMF 1.0: NIST-AI-RMF-GOVERN-1.3, NIST-AI-RMF-GOVERN-1.5; CIS Controls v8.1.2: CIS-15.2; EU NIS2: NIS2-ART-21; + 2 more sources |
| `ACO-SCBI-003` — Controlled Dependency And Image Sources | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AC-3.3, SP800-53-AC-3.9; CWE SDV v4.19.1: CWE-1220, CWE-1230; CIS Controls v8.1.2: CIS-2.5, CIS-2.6; NIST AI 100-2 e2025: NIST-AI-100-2-E2025-4.2.1; + 2 more sources |
| `ACO-SCBI-004` — Build Definition And Execution Integrity | CO | intro.md; aplicacao-lifecycle.md | SAMM v2.1: SAMM-ACTIVITY-D_SA_3_A, SAMM-ACTIVITY-D_SA_3_B; DSOMM: DSOMM-ACTIVITY-F6F7737F25A943178DE209BF59F29B5B, DSOMM-ACTIVITY-9F10792761E9457485AD3F2B4BCA8665; SSDF v1.1: SSDF-PRACTICE-PO.1, SSDF-PRACTICE-PO.4; CAPEC v3.9: CAPEC-443, CAPEC-523; + 10 more sources |
| `ACO-SCBI-005` — Release Promotion And Human Approval Integrity | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AC-4.9, SP800-53-AC-13; CWE SDV v4.19.1: CWE-205, CWE-250; PCI DSS v4.0.1: PCI-3.7.8, PCI-7.2.3; MITRE ATLAS: AML.T0054, AML.M0029; + 7 more sources |
| `ACO-SCBI-006` — Artifact Attestation And Provenance Integrity | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-CP-9.1, SP800-53-IA-12; MITRE ATLAS: AML.TA0009, AML.T0002; DSOMM: DSOMM-ACTIVITY-F3C4971E9F4D4E598ED0F0BDB6262477, DSOMM-ACTIVITY-A854B48D83BD4F8D8621A0BDD470837F; SLSA v1.0: SLSA-BUILD-L1, SLSA-PRINCIPLE-PREFER-ATTESTATIONS; + 10 more sources |
| `ACO-SCBI-007` — Container Image Supply Integrity | CO | intro.md; aplicacao-lifecycle.md | DSOMM: DSOMM-ACTIVITY-DA4FF665DCB94E939D2048CDEDC50FC2, DSOMM-ACTIVITY-34869EAFF2E14926B0BD28C43402F057; SP 800-53 r5: SP800-53-SA-12.3, SP800-53-SI-7.4; MITRE ATLAS: AML.T0010.004, AML.M0032; EU CRA: CRA-ART-19; + 1 more sources |
| `ACP-SCBI-001` — Build-Linked SBOM Generation | P | addon/00-catalogo-requisitos.md | SAMM v2.1: SAMM-ACTIVITY-D_SA_2_A, SAMM-ACTIVITY-I_SB_1_A; DSOMM: DSOMM-ACTIVITY-2858AC12017940D99ACF1B839C030473, DSOMM-ACTIVITY-2A44B708734F4463B0CB86DC46344B2F; SLSA v1.0: SLSA-PRODUCER-CHOOSE-BUILD-PLATFORM, SLSA-PRODUCER-CONSISTENT-BUILD; ASVS v5: ASVS-REQ-V15.1.2; + 2 more sources |
| `ACP-SCBI-002` — Automated Dependency And Image Risk Gating | P | addon/00-catalogo-requisitos.md | DSOMM: DSOMM-ACTIVITY-A340F46B63604CB8847BA0D3483D09D3, DSOMM-ACTIVITY-0DE465A655A74343AF79948BB5FF10BA; SAMM v2.1: SAMM-ACTIVITY-D_TA_1_A, SAMM-ACTIVITY-D_TA_2_A; CAPEC v3.9: CAPEC-35, CAPEC-187; SP 800-53 r5: SP800-53-CA-7.4, SP800-53-CM-5.7; + 16 more sources |
| `ACP-SCBI-003` — Approved Source And Registry Governance | P | addon/00-catalogo-requisitos.md | SP 800-53 r5: SP800-53-AC-3.11, SP800-53-AC-4.19; CIS Controls v8.1.2: CIS-2.2, CIS-2.6; SAFECode SIC: SCSIC-SOURCING, SCSIC-SOURCING-OSS; SAMM v2.1: SAMM-ACTIVITY-G_PC_1_A, SAMM-ACTIVITY-G_PC_1_B; + 7 more sources |
| `ACP-SCBI-004` — Pipeline Definition As Reviewed Code | P | addon/00-catalogo-requisitos.md | OWASP LLM Top 10: LLM03-2025 |
| `ACP-SCBI-005` — Governed Promotion And Release Approval | P | chapter prose (approval, enforce, gates kws verified) | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2; PCI DSS v4.0.1: PCI-REQ-12, PCI-1.1.1; CAPEC v3.9: CAPEC-2, CAPEC-13; HIPAA: HIPAA-164-308a1, HIPAA-164-308a2; + 14 more sources |
| `ACP-SCBI-006` — Artifact Signature And Provenance Validation | P | addon/00-catalogo-requisitos.md | SP 800-53 r5: SP800-53-AU-10.5, SP800-53-AU-12.1; ASVS v5: ASVS-REQ-V2.1.2, ASVS-REQ-V4.1.5; DSOMM: DSOMM-ACTIVITY-9F10792761E9457485AD3F2B4BCA8665, DSOMM-ACTIVITY-830570280B774D2E813540969768AE88; PCI DSS v4.0.1: PCI-1.1.2, PCI-2.1.2; + 13 more sources |
| `ACP-SCBI-007` — Trusted Container Image Supply | P | chapter prose (build, container, policy kws verified) | SP 800-53 r5: SP800-53-AC-19.5, SP800-53-MP-5; DSOMM: DSOMM-ACTIVITY-16E39C8F5336400188EDA552D2447531, DSOMM-ACTIVITY-485A33837F2E4DBABB84479377070904; MITRE ATLAS: AML.T0010.004, AML.T0105; CWE SDV v4.19.1: CWE-426, CWE-829; + 2 more sources |

---

## § Manual-only coverage (out-of-Core-scope; ES-grounded direct)

Manual sections that cover topics outside V1 AppSec Core ontology scope (maturity models, organizational policies, KPIs/metrics, glossaries) but with direct ES grounding to substrate v7 sources.

| Manual section | ES grounding (direct) |
|---|---|
| `achievable-maturity.md` | SAMM v2.1 SCA maturity; DSOMM dependency activities |
| `policies-relevantes.md` | Política de SBOM e Gestão de Dependências |
| `addon/10-kpis-metricas.md` | KPIs operacionais SBOM/SCA |

---

## § Out-of-AppSec coverage (pure editorial)

Manual sections that are pure editorial content (worked examples, narratives, illustrative cases, vendor-specific tooling integration). Sem ES grounding.

| Manual section | Content type |
|---|---|
| `addon/04-integracao-ci-cd.md` | Integração CI/CD examples (tooling-specific) |
| `addon/07-controle-registos-origem.md` | Registros de origem worked examples |

---

## § Future-work register (P8 §10 candidates)

_(Sem entradas no future-work register para este capítulo.)_

---

## Generation provenance

- **Substrate version:** v7 (SUPPLIER sha256 `596783ed984d9c0e8c8ef6439a0eaee8fbaf2d863af37138cde8fad55d62be04`)
- **V1 entity index:** `ontology-v1.1-fair-baseline` @ `84fe8bf` em sbd-toe-ontology
- **Per-entity source map:** `data/p8_inputs/per_entity_source_map.json` @ ESI commit `aa3c13c`
- **Phase 2/3 gap analysis:** `phase2_3_per_entity_classification.json` @ ESI commit `b8cd401`
- **Slice → chapter map:** `slice_to_chapter_map.yaml` @ ESI commit `adbe4e0`
- **Generated by:** Manual Agent Iter 4 (rastreabilidade richness extension)
- **Format:** 4-section tabular (Core-mapped + Manual-only + Out-of-AppSec + Future-work) per dispatch vision 2026-05-11
- **Cycle:** Cycle B Iteration 4 (P8 pipeline primitive demonstration)
