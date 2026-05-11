# 25. Rastreabilidade — Desenvolvimento Seguro

## Sumário

Este capítulo é a **âncora primária** das slices AppSec Core V1: `ACO-IVF` (Validação de input, parsing seguro e tratamento controlado de erros), `ACO-SPC` (Gestão de segredos, configuração protegida e identidades operacionais).

Cobertura V1 entity-level: **37 entidades** primárias. Estrutura abaixo expõe four-way routing (per P8 pipeline primitive demonstration 2026-05-11):

- **§ Core-mapped coverage** — V1 entity → Manual section anchor → ES grounding
- **§ Manual-only coverage** — Manual sections out-of-Core-scope mas com ES grounding direct
- **§ Out-of-AppSec coverage** — Pure editorial sections (examples, narratives) sem ES grounding
- **§ Future-work register** — Content gaps registered as P8 §10 candidates

---

## § Core-mapped coverage

Tabela exposing V1 entity-level coverage with Manual section anchor + substrate v7 ES grounding. Three-way alignment per row: V1 (ontology) ↔ Manual (prose) ↔ ES (substrate).

### Slice `ACO-IVF` — Validação de input, parsing seguro e tratamento controlado de erros

| V1 entity | Type | Manual section anchor | ES grounding |
|---|---|---|---|
| `ACM-IVF-001` — Code Review For Input And Error Discipline | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-AC-4.9, SP800-53-AC-13; ASVS v5: ASVS-REQ-V1.2.5, ASVS-REQ-V1.2.6; CAPEC v3.9: CAPEC-14, CAPEC-24; SAMM v2.1: SAMM-ACTIVITY-D_SR_1_B, SAMM-ACTIVITY-D_TA_3_A; + 15 more sources |
| `ACM-IVF-002` — Static Rulepacks And Security Linters | M | addon/00-catalogo-requisitos.md (mechanism) | MITRE ATLAS: AML.T0010.001, AML.T0020; CAPEC v3.9: CAPEC-15, CAPEC-35; CWE SDV v4.19.1: CWE-183, CWE-184; SP 800-53 r5: SP800-53-AC-4.1, SP800-53-AC-4.6; + 10 more sources |
| `ACM-IVF-003` — Schema And Contract Validators | M | addon/00-catalogo-requisitos.md (mechanism) | ASVS v5: ASVS-REQ-V2.1.1, ASVS-REQ-V2.1.2; SP 800-53 r5: SP800-53-SA-9.3, SP800-53-SA-10.1; CAPEC v3.9: CAPEC-95, CAPEC-146; CWE SDV v4.19.1: CWE-112, CWE-353; + 7 more sources |
| `ACM-IVF-004` — Centralized Error Translation And Redaction | M | ⚠️ future-work (P8 §10) | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2.4; PCI DSS v4.0.1: PCI-REQ-1, PCI-1.1.1; CIS Controls v8.1.2: CIS-2, CIS-4.9; DSOMM: DSOMM-ACTIVITY-994151396B50441B89E10AA59ACCD43D, DSOMM-ACTIVITY-8AE0B92C10E04602BA227524D6AED488; + 11 more sources |
| `ACM-IVF-005` — Context-Aware Encoder Selection And Application | M | chapter prose (html, json, output kws verified) | CAPEC v3.9: CAPEC-18, CAPEC-19; ASVS v5: ASVS-REQ-V1.1.2, ASVS-REQ-V1.2.1; CWE SDV v4.19.1: CWE-1021, CWE-838; MITRE ATLAS: AML.T0054, AML.T0077; + 3 more sources |
| `ACO-IVF-001` — External Input Contract Validation | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AC-20, SP800-53-AC-20.1; ASVS v5: ASVS-REQ-V2.1.1, ASVS-REQ-V2.2.1; CWE SDV v4.19.1: CWE-1284, CWE-1286; OWASP LLM Top 10: LLM02-2025, LLM10-2025; + 4 more sources |
| `ACO-IVF-002` — Schema, Type And Allowlist Discipline | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AC-3.11, SP800-53-AC-4.1; CAPEC v3.9: CAPEC-13, CAPEC-80; CWE SDV v4.19.1: CWE-1056, CWE-1070; CIS Controls v8.1.2: CIS-2.5, CIS-2.6; + 5 more sources |
| `ACO-IVF-003` — Injection-Resistant Input Handling And Dangerous Pattern Exclusion | CO | intro.md; aplicacao-lifecycle.md | CAPEC v3.9: CAPEC-3, CAPEC-6; CWE SDV v4.19.1: CWE-115, CWE-186; ASVS v5: ASVS-REQ-V1.2.4, ASVS-REQ-V1.2.7; MITRE ATLAS: AML.T0051, AML.T0051.000; + 6 more sources |
| `ACO-IVF-004` — Validation Before Internal Use And Trust Crossing | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AC-4.19, SP800-53-CA-3.6; ASVS v5: ASVS-REQ-V2.3.1, ASVS-REQ-V2.3.3; CIS Controls v8.1.2: CIS-3.4, CIS-18.4; CWE SDV v4.19.1: CWE-346, CWE-349; + 1 more sources |
| `ACO-IVF-005` — Controlled Failure And Non-Revealing Client Error Surface | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AC-3.5, SP800-53-AC-3.6; CAPEC v3.9: CAPEC-2, CAPEC-8; CWE SDV v4.19.1: CWE-1058, CWE-1073; PCI DSS v4.0.1: PCI-1.2.2, PCI-1.2.3; + 17 more sources |
| `ACO-IVF-006` — Centralized Error Handling And Sensitive Error Logging Hygiene | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AC-4.24, SP800-53-AU-1; CIS Controls v8.1.2: CIS-3.14, CIS-4.9; SAMM v2.1: SAMM-ACTIVITY-D_SA_3_B, SAMM-ACTIVITY-G_EG_2_B; ASVS v5: ASVS-REQ-V16.1.1, ASVS-REQ-V16.2.1; + 12 more sources |
| `ACO-IVF-007` — Input Validation And Safe Failure Integrity | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-PE-5, SP800-53-SC-7; CIS Controls v8.1.2: CIS-16.1, CIS-16.8; CAPEC v3.9: CAPEC-522, CAPEC-624; OWASP ML Top 10: ML02-2023, ML09-2023; + 6 more sources |
| `ACO-IVF-008` — Context-Aware Output Encoding And Rendering Safety | CO | intro.md; aplicacao-lifecycle.md | CAPEC v3.9: CAPEC-18, CAPEC-19; ASVS v5: ASVS-REQ-V1.2.1, ASVS-REQ-V1.2.2; CWE SDV v4.19.1: CWE-1021, CWE-79; MITRE ATLAS: AML.T0054, AML.T0077; + 3 more sources |
| `ACP-IVF-001` — Boundary Input Validation | P | addon/00-catalogo-requisitos.md | CWE SDV v4.19.1: CWE-1173, CWE-1284; ASVS v5: ASVS-REQ-V1.1.1, ASVS-REQ-V2.2.2; SP 800-53 r5: SP800-53-SI-10, SP800-53-SI-10.2; OWASP LLM Top 10: LLM02-2025, LLM10-2025; + 2 more sources |
| `ACP-IVF-002` — Schema And Allowlist Enforcement | P | chapter prose (accepted, allowlist, enforcement kws verified) | SP 800-53 r5: SP800-53-AC-3, SP800-53-AC-3.8; ASVS v5: ASVS-REQ-V1.2.6, ASVS-REQ-V1.5.1; PCI DSS v4.0.1: PCI-REQ-8, PCI-REQ-9; CAPEC v3.9: CAPEC-13, CAPEC-58; + 14 more sources |
| `ACP-IVF-003` — Dangerous Pattern Exclusion | P | addon/00-catalogo-requisitos.md | CAPEC v3.9: CAPEC-6, CAPEC-7; CWE SDV v4.19.1: CWE-115, CWE-184; NIST AI 100-2 e2025: NIST-AI-100-2-E2025-2.3.3, NIST-AI-100-2-E2025-3.2.2; ASVS v5: ASVS-REQ-V1.2.8, ASVS-REQ-V1.2.9; + 7 more sources |
| `ACP-IVF-004` — Pre-Use Data Validation Discipline | P | addon/00-catalogo-requisitos.md | SP 800-53 r5: SP800-53-CA-3.6, SP800-53-CA-7.4; CIS Controls v8.1.2: CIS-1.1, CIS-3; ASVS v5: ASVS-REQ-V2.2.3, ASVS-REQ-V2.3.1; SAMM v2.1: SAMM-ACTIVITY-D_TA_1_A, SAMM-ACTIVITY-D_TA_3_A; + 10 more sources |
| `ACP-IVF-005` — Non-Revealing Error Surface Control | P | addon/00-catalogo-requisitos.md | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2; PCI DSS v4.0.1: PCI-REQ-1, PCI-1.1.1; CAPEC v3.9: CAPEC-12, CAPEC-22; CWE SDV v4.19.1: CWE-1073, CWE-1084; + 18 more sources |
| `ACP-IVF-006` — Centralized Error Governance | P | cross-chapter → Cap. 00, Cap. 07, Cap. 10, Cap. 12, Cap. 13, Cap. 14 | SP 800-53 r5: SP800-53-AU-1, SP800-53-AU-2; SAMM v2.1: SAMM-ACTIVITY-G_EG_2_B, SAMM-ACTIVITY-G_EG_3_A; DSOMM: DSOMM-ACTIVITY-95CAEF9636ED458CA0875C35D4F9DEC2, DSOMM-ACTIVITY-8B994601575E4EA5B228ACCB18C8E514; CIS Controls v8.1.2: CIS-8.1, CIS-8.3; + 5 more sources |
| `ACP-IVF-007` — Context-Aware Output Encoding At Rendering Boundaries | P | chapter prose (encoding, escaping, html kws verified) | ASVS v5: ASVS-REQ-V1.1.2, ASVS-REQ-V1.2.1; CAPEC v3.9: CAPEC-19, CAPEC-32; MITRE ATLAS: AML.T0054, AML.T0077; CWE SDV v4.19.1: CWE-838; + 3 more sources |

### Slice `ACO-SPC` — Gestão de segredos, configuração protegida e identidades operacionais

| V1 entity | Type | Manual section anchor | ES grounding |
|---|---|---|---|
| `ACM-SPC-001` — Secret Management Systems | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-AC-3.5, SP800-53-AC-3.6; CAPEC v3.9: CAPEC-24, CAPEC-39; ASVS v5: ASVS-REQ-V6.1.2, ASVS-REQ-V6.5.2; SSDF v1.1: SSDF-PRACTICE-PO.1, SSDF-PRACTICE-PO.4; + 19 more sources |
| `ACM-SPC-002` — OIDC-Based Operational Identity | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-AC-4.12, SP800-53-AC-14; ASVS v5: ASVS-REQ-V6.8.4, ASVS-REQ-V7.5.3; CAPEC v3.9: CAPEC-21, CAPEC-151; PCI DSS v4.0.1: PCI-8.2.1, PCI-8.2.2; + 7 more sources |
| `ACM-SPC-003` — Short-Lived Credential Controls | M | addon/00-catalogo-requisitos.md (mechanism) | ASVS v5: ASVS-REQ-V6.1.1, ASVS-REQ-V6.2.10; CIS Controls v8.1.2: CIS-5, CIS-6.8; MITRE ATLAS: AML.TA0013, AML.T0098; SP 800-53 r5: SP800-53-AC-2.4, SP800-53-AC-2.8; + 1 more sources |
| `ACM-SPC-004` — Secret Scope And Binding Controls | M | addon/00-catalogo-requisitos.md (mechanism) | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2.7; CAPEC v3.9: CAPEC-13, CAPEC-35; MITRE ATLAS: AML.T0109, AML.T0002.002; NIST AI RMF 1.0: NIST-AI-RMF-GOVERN-1, NIST-AI-RMF-GOVERN-1.6; + 13 more sources |
| `ACO-SPC-001` — Secret Leak Prevention And Hardcoded-Secret Exclusion | CO | intro.md; aplicacao-lifecycle.md | CWE SDV v4.19.1: CWE-215, CWE-348; SP 800-53 r5: SP800-53-AC-4.31, SP800-53-PE-19; CAPEC v3.9: CAPEC-65, CAPEC-242; MITRE ATLAS: AML.T0057, AML.T0068; + 6 more sources |
| `ACO-SPC-002` — Protected Secret Storage And Controlled Retrieval | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AC-3.6, SP800-53-AC-3.9; CIS Controls v8.1.2: CIS-3, CIS-3.1; CWE SDV v4.19.1: CWE-256, CWE-257; CAPEC v3.9: CAPEC-37, CAPEC-204; + 7 more sources |
| `ACO-SPC-003` — Secret Rotation And Expiry Discipline | CO | intro.md; aplicacao-lifecycle.md | ASVS v5: ASVS-REQ-V6.2.10, ASVS-REQ-V6.4.1; CWE SDV v4.19.1: CWE-262, CWE-263 |
| `ACO-SPC-004` — Operational Identity Binding And Short-Lived Credentials | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AC-2, SP800-53-IA-2; CAPEC v3.9: CAPEC-21, CAPEC-59; ASVS v5: ASVS-REQ-V6.3.4, ASVS-REQ-V6.8.4; CWE SDV v4.19.1: CWE-1392, CWE-289; + 9 more sources |
| `ACO-SPC-005` — Secret Usage Isolation Across Pipeline, Workload And Deploy Surfaces | CO | intro.md; aplicacao-lifecycle.md | DSOMM: DSOMM-ACTIVITY-DA4FF665DCB94E939D2048CDEDC50FC2, DSOMM-ACTIVITY-DF428C9DEFA042269F47A15BB53F822B; MITRE ATLAS: AML.T0008.000, AML.T0024; SP 800-53 r5: SP800-53-SC-7.20, SP800-53-SC-39; CIS Controls v8.1.2: CIS-4.12, CIS-16.8; + 4 more sources |
| `ACO-SPC-006` — Secret Change Auditability And Governance | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AC-2.7, SP800-53-AC-3.10; PCI DSS v4.0.1: PCI-10.3.2, PCI-11.5.2; ASVS v5: ASVS-REQ-V11.1.4; CAPEC v3.9: CAPEC-678; + 5 more sources |
| `ACO-SPC-007` — Secret Handling And Operational Identity Integrity | CO | intro.md; aplicacao-lifecycle.md | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-3; PCI DSS v4.0.1: PCI-REQ-2, PCI-REQ-7; CIS Controls v8.1.2: CIS-3.5, CIS-4; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_A, SAMM-ACTIVITY-D_SA_2_A; + 16 more sources |
| `ACP-SPC-001` — Secret Leak Prevention In Source And Pipeline | P | addon/00-catalogo-requisitos.md | DSOMM: DSOMM-ACTIVITY-F3C4971E9F4D4E598ED0F0BDB6262477, DSOMM-ACTIVITY-8AE0B92C10E04602BA227524D6AED488; CAPEC v3.9: CAPEC-38, CAPEC-44; SSDF v1.1: SSDF-PRACTICE-PO.1, SSDF-PRACTICE-PS.2; SAMM v2.1: SAMM-ACTIVITY-I_DM_1_A, SAMM-ACTIVITY-I_DM_2_A; + 14 more sources |
| `ACP-SPC-002` — Vault-Backed Secret Storage | P | addon/00-catalogo-requisitos.md | SP 800-53 r5: SP800-53-AC-3.13, SP800-53-AC-4.4; PCI DSS v4.0.1: PCI-REQ-3, PCI-REQ-4; CWE SDV v4.19.1: CWE-256, CWE-257; CIS Controls v8.1.2: CIS-3, CIS-3.1; + 14 more sources |
| `ACP-SPC-003` — Secret Rotation And Renewal Discipline | P | addon/00-catalogo-requisitos.md | SP 800-53 r5: SP800-53-IA-5.13, SP800-53-PS-1; ASVS v5: ASVS-REQ-V6.4.5, ASVS-REQ-V13.3.4; CIS Controls v8.1.2: CIS-14.1; HIPAA: HIPAA-164-308a6; + 3 more sources |
| `ACP-SPC-004` — Operational Identity Binding And OIDC Use | P | addon/00-catalogo-requisitos.md | SP 800-53 r5: SP800-53-AC-2, SP800-53-AC-4.12; ASVS v5: ASVS-REQ-V6.8.1, ASVS-REQ-V6.8.2; PCI DSS v4.0.1: PCI-1.1.1, PCI-4.1.1; CAPEC v3.9: CAPEC-21, CAPEC-196; + 8 more sources |
| `ACP-SPC-005` — Secret Isolation Across Technical Surfaces | P | cross-chapter → Cap. 07, Cap. 08, Cap. 11 | SP 800-53 r5: SP800-53-AC-17.6, SP800-53-AC-20; CAPEC v3.9: CAPEC-22, CAPEC-36; MITRE ATLAS: AML.TA0013, AML.TA0010; CWE SDV v4.19.1: CWE-1104, CWE-1220; + 10 more sources |
| `ACP-SPC-006` — Secret Configuration Governance | P | cross-chapter → Cap. 00, Cap. 05, Cap. 07, Cap. 13, Cap. 14 | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-4.20; NIST AI RMF 1.0: NIST-AI-RMF-GOVERN-1, NIST-AI-RMF-GOVERN-1.3; SAMM v2.1: SAMM-ACTIVITY-G_EG_2_A, SAMM-ACTIVITY-G_EG_3_A; PCI DSS v4.0.1: PCI-REQ-2, PCI-2.2.1; + 9 more sources |

---

## § Manual-only coverage (out-of-Core-scope; ES-grounded direct)

Manual sections that cover topics outside V1 AppSec Core ontology scope (maturity models, organizational policies, KPIs/metrics, glossaries) but with direct ES grounding to substrate v7 sources.

| Manual section | ES grounding (direct) |
|---|---|
| `achievable-maturity.md` | SAMM v2.1 SSDF practices maturity; DSOMM secure dev activities |
| `policies-relevantes.md` | Política de Desenvolvimento Seguro |
| `addon/07-guidelines-equipa.md` | Guidelines operacionais de equipa (organizational) |

---

## § Out-of-AppSec coverage (pure editorial)

Manual sections that are pure editorial content (worked examples, narratives, illustrative cases, vendor-specific tooling integration). Sem ES grounding.

| Manual section | Content type |
|---|---|
| `addon/01-boas-praticas-codigo.md` | Best practices narrative com code snippets |
| `addon/05-excecoes-e-justificacoes.md` | Exception cases narrative |
| `addon/09-anotacoes-evidencia.md` | Anotação semântica examples |

---

## § Future-work register (P8 §10 candidates)

Content gaps registered for future-cycle authoring; honest documentation per P8 §10 limitations.

| V1 entity / topic | Status |
|---|---|
| `ACM-IVF-004` — Centralized Error Translation And Redaction | Authoring pending — Phase 2/3 confirmed_content_gap; programme-lead 2026-05-11 ratified defer to future-cycle. Topic partially covered by Cap. 02 VAL-006/ERR family + Iter 2 §11 LLM input handling. Future authoring should consolidate into single Cap. 06 section. |

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
