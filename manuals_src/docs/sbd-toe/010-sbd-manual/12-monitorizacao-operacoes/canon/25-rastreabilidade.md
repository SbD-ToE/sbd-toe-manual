# 25. Rastreabilidade — Monitorização e Operações

## Sumário

Este capítulo é a **âncora primária** das slices AppSec Core V1: `ACO-SLG` (Logging de eventos de segurança e audit trail).

Cobertura V1 entity-level: **18 entidades** primárias. Estrutura abaixo expõe four-way routing (per P8 pipeline primitive demonstration 2026-05-11):

- **§ Core-mapped coverage** — V1 entity → Manual section anchor → ES grounding
- **§ Manual-only coverage** — Manual sections out-of-Core-scope mas com ES grounding direct
- **§ Out-of-AppSec coverage** — Pure editorial sections (examples, narratives) sem ES grounding
- **§ Future-work register** — Content gaps registered as P8 §10 candidates

---

## § Core-mapped coverage

Tabela exposing V1 entity-level coverage with Manual section anchor + substrate v7 ES grounding. Three-way alignment per row: V1 (ontology) ↔ Manual (prose) ↔ ES (substrate).

### Slice `ACO-SLG` — Logging de eventos de segurança e audit trail

| V1 entity | Type | Manual section anchor | ES grounding |
|---|---|---|---|
| `ACM-SLG-001` — Machine-Readable Structured Logging | M | addon/00-catalogo-requisitos.md (mechanism) | SAMM v2.1: SAMM-ACTIVITY-V_AA_1_A, SAMM-ACTIVITY-V_AA_1_B; CAPEC v3.9: CAPEC-637; DSOMM: DSOMM-ACTIVITY-7C7350896A83419F8B27C1E676CEDEA1; PCI DSS v4.0.1: PCI-REQ-10 |
| `ACM-SLG-002` — Central Log Ingestion And Normalization | M | chapter prose (central, forwarding, ingestion kws verified) | CIS Controls v8.1.2: CIS-1, CIS-1.1; SP 800-53 r5: SP800-53-CM-8.7, SP800-53-SA-19.3; DSOMM: DSOMM-ACTIVITY-2A44B708734F4463B0CB86DC46344B2F; OWASP LLM Top 10: LLM03-2025; + 1 more sources |
| `ACM-SLG-003` — Log Integrity And Access Controls | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2; PCI DSS v4.0.1: PCI-REQ-1, PCI-REQ-3; CAPEC v3.9: CAPEC-1, CAPEC-21; ASVS v5: ASVS-REQ-V1.2.4, ASVS-REQ-V1.5.2; + 21 more sources |
| `ACM-SLG-004` — Logging Failure Visibility Controls | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-AU-5.4, SP800-53-MA-1; CWE SDV v4.19.1: CWE-1118, CWE-391; SAMM v2.1: SAMM-ACTIVITY-I_DM_1_A, SAMM-ACTIVITY-O_IM_3_A; ASVS v5: ASVS-REQ-V16.5.2, ASVS-REQ-V16.5.4; + 4 more sources |
| `ACM-SLG-005` — Security Event Catalog And Coverage Verification | M | chapter prose (audit, coverage, define kws verified) | SAMM v2.1: SAMM-ACTIVITY-D_SR_1_B, SAMM-ACTIVITY-D_TA_3_A; SP 800-53 r5: SP800-53-AU-1, SP800-53-AU-2; DSOMM: DSOMM-ACTIVITY-9768F154357A4C06AF6FD66570677C9B, DSOMM-ACTIVITY-F0E018143B884BD0A3A9F91DB001D20BADVANCED; PCI DSS v4.0.1: PCI-REQ-11, PCI-1.1.1; + 12 more sources |
| `ACM-SLG-006` — Log Retention Lifecycle Management Controls | M | chapter prose (lifecycle, logs, management kws verified) | SP 800-53 r5: SP800-53-AU-5.1, SP800-53-CM-1; CIS Controls v8.1.2: CIS-3.4, CIS-5.3; CAPEC v3.9: CAPEC-546; DSOMM: DSOMM-ACTIVITY-7F36B9BABC054FD69A2A73344C249722; + 5 more sources |
| `ACO-SLG-001` — Critical Security Event Coverage And Catalog Discipline | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AC-1, SP800-53-AU-5.2; PCI DSS v4.0.1: PCI-REQ-11, PCI-5.2.3; DSOMM: DSOMM-ACTIVITY-48F97F31931C46EB9B3EE2FEC0CD0426, DSOMM-ACTIVITY-0A929C3EAB9A42068761ADF84B74622E; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_A, SAMM-ACTIVITY-D_SR_1_B; + 12 more sources |
| `ACO-SLG-002` — Structured Audit Fields And Machine-Readable Log Shape | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AC-4.1, SP800-53-AC-16; ASVS v5: ASVS-REQ-V15.3.1; PCI DSS v4.0.1: PCI-1.2.4 |
| `ACO-SLG-003` — Log Integrity Protection And Access Discipline | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AC-3, SP800-53-AC-3.4; PCI DSS v4.0.1: PCI-REQ-3, PCI-4.2.1; CIS Controls v8.1.2: CIS-3.1, CIS-3.2; ASVS v5: ASVS-REQ-V6.3.8, ASVS-REQ-V11.3.3; + 9 more sources |
| `ACO-SLG-004` — Audit Record Retention And Lifecycle Governance | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AU-7, SP800-53-AU-10.3; CIS Controls v8.1.2: CIS-3.4, CIS-6.2; PCI DSS v4.0.1: PCI-3.2.1, PCI-10.5.1; CAPEC v3.9: CAPEC-675; + 3 more sources |
| `ACO-SLG-005` — Centralized Log Ingestion And Source Accountability | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AC-2, SP800-53-AC-8; CIS Controls v8.1.2: CIS-1, CIS-2; CAPEC v3.9: CAPEC-150, CAPEC-384; DSOMM: DSOMM-ACTIVITY-95CAEF9636ED458CA0875C35D4F9DEC2, DSOMM-ACTIVITY-82E499D1F4634A4BBE9068812A874AF6; + 3 more sources |
| `ACO-SLG-006` — Logging Pipeline Health And Silent-Failure Visibility | CO | intro.md; aplicacao-lifecycle.md | CWE SDV v4.19.1: CWE-117, CWE-391 |
| `ACO-SLG-007` — Security Logging And Audit Trail Assurance | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AT-4, SP800-53-AU-5; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_B, SAMM-ACTIVITY-D_SA_2_A; ASVS v5: ASVS-REQ-V6.1.3, ASVS-REQ-V6.3.4; CIS Controls v8.1.2: CIS-4.1, CIS-4.2; + 12 more sources |
| `ACP-SLG-001` — Critical Event Catalog Governance | P | addon/00-catalogo-requisitos.md | SP 800-53 r5: SP800-53-AU-2, SP800-53-AU-2.2; CWE SDV v4.19.1: CWE-778; PCI DSS v4.0.1: PCI-10.7.2 |
| `ACP-SLG-002` — Structured And Centralized Security Logging | P | addon/00-catalogo-requisitos.md | CIS Controls v8.1.2: CIS-1.1, CIS-1.4; SP 800-53 r5: SP800-53-AC-12.1, SP800-53-AU-2; DSOMM: DSOMM-ACTIVITY-4ECED38A79044C45ADB050B663065540, DSOMM-ACTIVITY-FE875E17AE4A45F8A359244AA4FCBC04; SAMM v2.1: SAMM-ACTIVITY-I_DM_1_A, SAMM-ACTIVITY-I_SB_3_A; + 4 more sources |
| `ACP-SLG-003` — Log Integrity And Protected Access | P | addon/00-catalogo-requisitos.md | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2; PCI DSS v4.0.1: PCI-REQ-3, PCI-REQ-4; ASVS v5: ASVS-REQ-V1.2.4, ASVS-REQ-V1.2.6; CAPEC v3.9: CAPEC-21, CAPEC-22; + 22 more sources |
| `ACP-SLG-004` — Log Retention And Lifecycle Governance | P | addon/00-catalogo-requisitos.md | SP 800-53 r5: SP800-53-AU-4, SP800-53-AU-5.1; SAMM v2.1: SAMM-ACTIVITY-G_PC_1_A, SAMM-ACTIVITY-G_PC_3_B; CIS Controls v8.1.2: CIS-3.4, CIS-8.1; PCI DSS v4.0.1: PCI-3.2.1, PCI-10.5.1; + 1 more sources |
| `ACP-SLG-005` — Logging Pipeline Health Visibility | P | chapter prose (detect, logging, pipeline kws verified) | SP 800-53 r5: SP800-53-AU-5.4, SP800-53-MA-1; SAMM v2.1: SAMM-ACTIVITY-O_EM_3_A, SAMM-ACTIVITY-O_IM_3_A; ASVS v5: ASVS-REQ-V16.5.4; OWASP LLM Top 10: LLM03-2025 |

---

## § Manual-only coverage (out-of-Core-scope; ES-grounded direct)

Manual sections that cover topics outside V1 AppSec Core ontology scope (maturity models, organizational policies, KPIs/metrics, glossaries) but with direct ES grounding to substrate v7 sources.

| Manual section | ES grounding (direct) |
|---|---|
| `achievable-maturity.md` | SAMM v2.1 OE/IM maturity; DSOMM operations activities |
| `policies-relevantes.md` | Política de Monitorização e Resposta a Incidentes |
| `addon/04-integracao-siem.md` | Integração SIEM/SOAR (operacional, vendor-specific) |

---

## § Out-of-AppSec coverage (pure editorial)

Manual sections that are pure editorial content (worked examples, narratives, illustrative cases, vendor-specific tooling integration). Sem ES grounding.

| Manual section | Content type |
|---|---|
| `casos-praticos-monitorizacao.md` | Worked examples: incident response cases |
| `addon/09-exemplos-eventos.md` | Examples of security events |

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
