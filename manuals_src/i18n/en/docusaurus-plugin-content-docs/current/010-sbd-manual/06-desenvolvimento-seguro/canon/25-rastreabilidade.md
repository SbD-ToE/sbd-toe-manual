---
id: rastreabilidade
translation:
  source_locale: pt
  source_path: 010-sbd-manual/06-desenvolvimento-seguro/canon/25-rastreabilidade.md
  source_sha256: d0091d24510789e73b41b3f967acaf6eaedbff7a2d1832d82412dd9580e9e48a
  source_commit: e341b40c451d9ef4be61e6cd59d994cda54c1aa0
  target_sha256: 43608962a396bdd030cd4df0bc18904e6421cceda4b40ab7ac75eff7ab2bdff1
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [appsec_core, chapter_role, llm, practitioner_manual, provenance, risk_level, sbdtoe_sbd, slice, traceability, v1_entity_ivf_centralized_error_governance, v1_entity_ivf_centralized_error_handling, v1_entity_ivf_centralized_error_translation, validation_evaluation]
  glossary_sha256: 41649295f7acd8649cf31b8fb65912d83beab0182df1e4e715cded27f42c9e1c
  translated_at: 2026-09-26T13:37:01Z
  reviewed_by: null
---

# 25. Traceability — Secure Development

## Summary {#sumário}

This chapter is the **primary anchor** of the AppSec Core V1 slices: `ACO-IVF` (Input validation, safe parsing and controlled error handling), `ACO-SPC` (Secrets management, protected configuration and operational identities).

V1 entity-level coverage: **37 primary entities**. The structure below exposes the **five-section routing** (per Run 1 amendment 2026-05-11; P8 pipeline primitive demonstration):

- **§ Manual ontology V2 entities** — canonical Manual ontology V2 entities mapped to this chapter (KG canonical data)
- **§ Core-mapped coverage** — V1 entity → Manual ontology V2 anchor → Manual section anchor → §26 methodology label → ES grounding
- **§ Manual-only coverage** — Manual sections out-of-Core-scope but directly ES-grounded
- **§ Out-of-AppSec coverage** — Pure editorial sections (examples, narratives) without ES grounding
- **§ Future-work register** — Content gaps registered as P8 §10 candidates

---

## § Manual ontology V2 — canonical entities of this chapter {#-manual-ontology-v2--entities-canónicas-deste-capítulo}

Total: **59 entities** of Manual ontology V2 mapped to this chapter via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `DEV-001` | Secure code guidelines versioned and approved per stack | normative | explicit | deterministic |
| Requirement | `DEV-002` | Security linters and rulesets configured and enforced | normative | explicit | deterministic |
| Requirement | `DEV-003` | Static analysis (SAST) integrated as an integration gate | normative | explicit | deterministic |
| Requirement | `DEV-004` | Code review with a security checklist on critical components | normative | explicit | deterministic |
| Requirement | `DEV-005` | Formal management of technical exceptions and deviations from guidelines | normative | explicit | deterministic |
| Requirement | `DEV-006` | Provenance of incorporated code identified and controlled | normative | explicit | deterministic |
| Requirement | `DEV-007` | Explicit technical constraints for AI-generated code | normative | explicit | deterministic |
| Requirement | `DEV-008` | Quality profiles with minimum security thresholds per risk level | normative | explicit | deterministic |
| Requirement | `DEV-009` | Traceable security annotations in code and tests | normative | explicit | deterministic |
| Control | `CTRL-code-integrity-desenvolvimento-seguro-e-validacao-de-codigo-63dedd7460` | Secure development and code validation | normative | explicit | deterministic |
| Practice | `06-desenvolvimento-seguro:arquivo-central-de-evidencias-de-validacao` | Central Archive of Validation Evidence | normative | explicit | deterministic |
| Practice | `06-desenvolvimento-seguro:automatizacao-em-ci-cd-linters-sast` | Automation in CI/CD (Linters & SAST) | normative | explicit | deterministic |
| Practice | `06-desenvolvimento-seguro:gate-de-seguranca-pre-release` | Pre-release Security Gate | normative | explicit | deterministic |
| Practice | `06-desenvolvimento-seguro:gestao-de-dependencias-no-codigo` | Dependency Management in Code | normative | explicit | deterministic |
| Practice | `06-desenvolvimento-seguro:gestao-de-excecoes-tecnicas` | Technical Exception Management | normative | explicit | deterministic |
| Practice | `06-desenvolvimento-seguro:governacao-e-curadoria-de-guidelines` | Governance and Curation of Guidelines | normative | explicit | deterministic |
| Practice | `06-desenvolvimento-seguro:guidelines-de-desenvolvimento-seguro` | Secure Development Guidelines | normative | explicit | deterministic |
| Practice | `06-desenvolvimento-seguro:monitorizacao-de-conformidade-e-metricas-de-seguranca` | Compliance Monitoring and Security Metrics | normative | explicit | deterministic |
| Practice | `06-desenvolvimento-seguro:perfis-de-validacao-por-nivel-de-risco-l1l3` | Validation Profiles per Risk Level (L1–L3) | normative | explicit | deterministic |
| Practice | `06-desenvolvimento-seguro:rastreabilidade-com-anotacoes-de-seguranca` | Traceability with Security Annotations | normative | explicit | deterministic |
| Practice | `06-desenvolvimento-seguro:revisao-de-codigo-segura` | Secure Code Review | normative | explicit | deterministic |
| Practice | `06-desenvolvimento-seguro:uso-validado-de-genia` | Validated Use of GenAI | normative | explicit | deterministic |
| Practice | `06-desenvolvimento-seguro:validacao-de-padroes-perigosos-e-anti-patterns` | Validation of Dangerous Patterns and Anti-patterns | normative | explicit | deterministic |
| Practice | `06-desenvolvimento-seguro:validacoes-locais-obrigatorias-pre-commit` | Mandatory Local Validations (Pre-commit) | normative | explicit | deterministic |
| Threat | `MT-093` | Inclusion of insecure patterns out of habit | normative | heuristic | bounded |
| Threat | `MT-094` | Use of deprecated or dangerous functions | normative | heuristic | bounded |
| Threat | `MT-095` | Code injection without adequate escaping | normative | heuristic | bounded |
| Threat | `MT-096` | Insecure code without detection | normative | heuristic | bounded |
| Threat | `MT-097` | Absence of traceability between issues and decisions | normative | heuristic | bounded |
| Threat | `MT-098` | Only reactive validation (e.g. QA tests) | normative | heuristic | bounded |
| Threat | `MT-099` | Security removed due to “incompatibility” | normative | heuristic | bounded |
| Threat | `MT-100` | Exceptions not reviewed or revalidated | normative | heuristic | bounded |
| Threat | `MT-101` | Untracked deviations between guideline and practice | normative | heuristic | bounded |
| Threat | `MT-102` | Generation of insecure code via AI | normative | heuristic | bounded |
| Threat | `MT-103` | Inclusion of known vulnerabilities | normative | heuristic | bounded |
| Threat | `MT-104` | Lack of accountability for generated code | normative | heuristic | bounded |
| Threat | `MT-105` | Inclusion of discontinued libraries | normative | heuristic | bounded |
| Threat | `MT-106` | Lack of justification for the use of an insecure dependency | normative | heuristic | bounded |
| Threat | `MT-107` | Vulnerable component kept in the final build | normative | heuristic | bounded |
| Threat | `MT-108` | Inconsistency across teams and projects | normative | heuristic | bounded |
| Threat | `MT-109` | Absence of a security baseline | normative | heuristic | bounded |
| Threat | `MT-110` | Weak accountability for code security | normative | heuristic | bounded |

> Authority class / source mode / confidence model: per Manual ontology V2 definition (`sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml`, `meta.version: '2.0'`).

---

## § Core-mapped coverage {#-core-mapped-coverage}

Table exposing V1 entity-level coverage with Manual ontology V2 anchor + Manual section anchor + §26 methodology label + substrate v7 ES grounding.

### Slice `ACO-IVF` — Input validation, safe parsing and controlled error handling {#slice-aco-ivf--validação-de-input-parsing-seguro-e-tratamento-controlado-de-erros}

| V1 entity | Type | Manual V2 anchor | Manual section anchor | Authority | Source mode | §26 label | ES grounding |
|---|---|---|---|---|---|---|---|
| `ACM-IVF-001` — Code Review For Input And Error Discipline | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-4.9, SP800-53-AC-13; ASVS v5: ASVS-REQ-V1.2.5, ASVS-REQ-V1.2.6; CAPEC v3.9: CAPEC-14, CAPEC-24; SAMM v2.1: SAMM-ACTIVITY-D_SR_1_B, SAMM-ACTIVITY-D_TA_3_A; + 15 more sources |
| `ACM-IVF-002` — Static Rulepacks And Security Linters | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | MITRE ATLAS: AML.T0010.001, AML.T0020; CAPEC v3.9: CAPEC-15, CAPEC-35; CWE SDV v4.19.1: CWE-183, CWE-184; SP 800-53 r5: SP800-53-AC-4.1, SP800-53-AC-4.6; + 10 more sources |
| `ACM-IVF-003` — Schema And Contract Validators | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | ASVS v5: ASVS-REQ-V2.1.1, ASVS-REQ-V2.1.2; SP 800-53 r5: SP800-53-SA-9.3, SP800-53-SA-10.1; CAPEC v3.9: CAPEC-95, CAPEC-146; CWE SDV v4.19.1: CWE-112, CWE-353; + 7 more sources |
| `ACM-IVF-004` — Centralized Error Translation And Redaction | M | Mechanism | ⚠️ future-work (P8 §10) | semantic | scored | Gap | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2.4; PCI DSS v4.0.1: PCI-REQ-1, PCI-1.1.1; CIS Controls v8.1.2: CIS-2, CIS-4.9; DSOMM: DSOMM-ACTIVITY-994151396B50441B89E10AA59ACCD43D, DSOMM-ACTIVITY-8AE0B92C10E04602BA227524D6AED488; + 11 more sources |
| `ACM-IVF-005` — Context-Aware Encoder Selection And Application | M | Mechanism | chapter prose (html, json, output kws verified) | semantic | scored | Semantic | CAPEC v3.9: CAPEC-18, CAPEC-19; ASVS v5: ASVS-REQ-V1.1.2, ASVS-REQ-V1.2.1; CWE SDV v4.19.1: CWE-1021, CWE-838; MITRE ATLAS: AML.T0054, AML.T0077; + 3 more sources |
| `ACO-IVF-001` — External Input Contract Validation | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-20, SP800-53-AC-20.1; ASVS v5: ASVS-REQ-V2.1.1, ASVS-REQ-V2.2.1; CWE SDV v4.19.1: CWE-1284, CWE-1286; OWASP LLM Top 10: LLM02-2025, LLM10-2025; + 4 more sources |
| `ACO-IVF-002` — Schema, Type And Allowlist Discipline | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-3.11, SP800-53-AC-4.1; CAPEC v3.9: CAPEC-13, CAPEC-80; CWE SDV v4.19.1: CWE-1056, CWE-1070; CIS Controls v8.1.2: CIS-2.5, CIS-2.6; + 5 more sources |
| `ACO-IVF-003` — Injection-Resistant Input Handling And Dangerous Pattern Exclusion | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | CAPEC v3.9: CAPEC-3, CAPEC-6; CWE SDV v4.19.1: CWE-115, CWE-186; ASVS v5: ASVS-REQ-V1.2.4, ASVS-REQ-V1.2.7; MITRE ATLAS: AML.T0051, AML.T0051.000; + 6 more sources |
| `ACO-IVF-004` — Validation Before Internal Use And Trust Crossing | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-4.19, SP800-53-CA-3.6; ASVS v5: ASVS-REQ-V2.3.1, ASVS-REQ-V2.3.3; CIS Controls v8.1.2: CIS-3.4, CIS-18.4; CWE SDV v4.19.1: CWE-346, CWE-349; + 1 more sources |
| `ACO-IVF-005` — Controlled Failure And Non-Revealing Client Error Surface | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-3.5, SP800-53-AC-3.6; CAPEC v3.9: CAPEC-2, CAPEC-8; CWE SDV v4.19.1: CWE-1058, CWE-1073; PCI DSS v4.0.1: PCI-1.2.2, PCI-1.2.3; + 17 more sources |
| `ACO-IVF-006` — Centralized Error Handling And Sensitive Error Logging Hygiene | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-4.24, SP800-53-AU-1; CIS Controls v8.1.2: CIS-3.14, CIS-4.9; SAMM v2.1: SAMM-ACTIVITY-D_SA_3_B, SAMM-ACTIVITY-G_EG_2_B; ASVS v5: ASVS-REQ-V16.1.1, ASVS-REQ-V16.2.1; + 12 more sources |
| `ACO-IVF-007` — Input Validation And Safe Failure Integrity | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-PE-5, SP800-53-SC-7; CIS Controls v8.1.2: CIS-16.1, CIS-16.8; CAPEC v3.9: CAPEC-522, CAPEC-624; OWASP ML Top 10: ML02-2023, ML09-2023; + 6 more sources |
| `ACO-IVF-008` — Context-Aware Output Encoding And Rendering Safety | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | CAPEC v3.9: CAPEC-18, CAPEC-19; ASVS v5: ASVS-REQ-V1.2.1, ASVS-REQ-V1.2.2; CWE SDV v4.19.1: CWE-1021, CWE-79; MITRE ATLAS: AML.T0054, AML.T0077; + 3 more sources |
| `ACP-IVF-001` — Boundary Input Validation | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | CWE SDV v4.19.1: CWE-1173, CWE-1284; ASVS v5: ASVS-REQ-V1.1.1, ASVS-REQ-V2.2.2; SP 800-53 r5: SP800-53-SI-10, SP800-53-SI-10.2; OWASP LLM Top 10: LLM02-2025, LLM10-2025; + 2 more sources |
| `ACP-IVF-002` — Schema And Allowlist Enforcement | P | Practice | chapter prose (accepted, allowlist, enforcement kws verified) | normative | explicit | Semantic | SP 800-53 r5: SP800-53-AC-3, SP800-53-AC-3.8; ASVS v5: ASVS-REQ-V1.2.6, ASVS-REQ-V1.5.1; PCI DSS v4.0.1: PCI-REQ-8, PCI-REQ-9; CAPEC v3.9: CAPEC-13, CAPEC-58; + 14 more sources |
| `ACP-IVF-003` — Dangerous Pattern Exclusion | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | CAPEC v3.9: CAPEC-6, CAPEC-7; CWE SDV v4.19.1: CWE-115, CWE-184; NIST AI 100-2 e2025: NIST-AI-100-2-E2025-2.3.3, NIST-AI-100-2-E2025-3.2.2; ASVS v5: ASVS-REQ-V1.2.8, ASVS-REQ-V1.2.9; + 7 more sources |
| `ACP-IVF-004` — Pre-Use Data Validation Discipline | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-CA-3.6, SP800-53-CA-7.4; CIS Controls v8.1.2: CIS-1.1, CIS-3; ASVS v5: ASVS-REQ-V2.2.3, ASVS-REQ-V2.3.1; SAMM v2.1: SAMM-ACTIVITY-D_TA_1_A, SAMM-ACTIVITY-D_TA_3_A; + 10 more sources |
| `ACP-IVF-005` — Non-Revealing Error Surface Control | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2; PCI DSS v4.0.1: PCI-REQ-1, PCI-1.1.1; CAPEC v3.9: CAPEC-12, CAPEC-22; CWE SDV v4.19.1: CWE-1073, CWE-1084; + 18 more sources |
| `ACP-IVF-006` — Centralized Error Governance | P | Practice | cross-chapter → Ch. 00, Ch. 07, Ch. 10, Ch. 12, Ch. 13, Ch. 14 | normative | explicit | Partial | SP 800-53 r5: SP800-53-AU-1, SP800-53-AU-2; SAMM v2.1: SAMM-ACTIVITY-G_EG_2_B, SAMM-ACTIVITY-G_EG_3_A; DSOMM: DSOMM-ACTIVITY-95CAEF9636ED458CA0875C35D4F9DEC2, DSOMM-ACTIVITY-8B994601575E4EA5B228ACCB18C8E514; CIS Controls v8.1.2: CIS-8.1, CIS-8.3; + 5 more sources |
| `ACP-IVF-007` — Context-Aware Output Encoding At Rendering Boundaries | P | Practice | chapter prose (encoding, escaping, html kws verified) | normative | explicit | Semantic | ASVS v5: ASVS-REQ-V1.1.2, ASVS-REQ-V1.2.1; CAPEC v3.9: CAPEC-19, CAPEC-32; MITRE ATLAS: AML.T0054, AML.T0077; CWE SDV v4.19.1: CWE-838; + 3 more sources |

### Slice `ACO-SPC` — Secrets management, protected configuration and operational identities {#slice-aco-spc--gestão-de-segredos-configuração-protegida-e-identidades-operacionais}

| V1 entity | Type | Manual V2 anchor | Manual section anchor | Authority | Source mode | §26 label | ES grounding |
|---|---|---|---|---|---|---|---|
| `ACM-SPC-001` — Secret Management Systems | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-3.5, SP800-53-AC-3.6; CAPEC v3.9: CAPEC-24, CAPEC-39; ASVS v5: ASVS-REQ-V6.1.2, ASVS-REQ-V6.5.2; SSDF v1.1: SSDF-PRACTICE-PO.1, SSDF-PRACTICE-PO.4; + 19 more sources |
| `ACM-SPC-002` — OIDC-Based Operational Identity | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-4.12, SP800-53-AC-14; ASVS v5: ASVS-REQ-V6.8.4, ASVS-REQ-V7.5.3; CAPEC v3.9: CAPEC-21, CAPEC-151; PCI DSS v4.0.1: PCI-8.2.1, PCI-8.2.2; + 7 more sources |
| `ACM-SPC-003` — Short-Lived Credential Controls | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | ASVS v5: ASVS-REQ-V6.1.1, ASVS-REQ-V6.2.10; CIS Controls v8.1.2: CIS-5, CIS-6.8; MITRE ATLAS: AML.TA0013, AML.T0098; SP 800-53 r5: SP800-53-AC-2.4, SP800-53-AC-2.8; + 1 more sources |
| `ACM-SPC-004` — Secret Scope And Binding Controls | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2.7; CAPEC v3.9: CAPEC-13, CAPEC-35; MITRE ATLAS: AML.T0109, AML.T0002.002; NIST AI RMF 1.0: NIST-AI-RMF-GOVERN-1, NIST-AI-RMF-GOVERN-1.6; + 13 more sources |
| `ACO-SPC-001` — Secret Leak Prevention And Hardcoded-Secret Exclusion | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | CWE SDV v4.19.1: CWE-215, CWE-348; SP 800-53 r5: SP800-53-AC-4.31, SP800-53-PE-19; CAPEC v3.9: CAPEC-65, CAPEC-242; MITRE ATLAS: AML.T0057, AML.T0068; + 6 more sources |
| `ACO-SPC-002` — Protected Secret Storage And Controlled Retrieval | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-3.6, SP800-53-AC-3.9; CIS Controls v8.1.2: CIS-3, CIS-3.1; CWE SDV v4.19.1: CWE-256, CWE-257; CAPEC v3.9: CAPEC-37, CAPEC-204; + 7 more sources |
| `ACO-SPC-003` — Secret Rotation And Expiry Discipline | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | ASVS v5: ASVS-REQ-V6.2.10, ASVS-REQ-V6.4.1; CWE SDV v4.19.1: CWE-262, CWE-263 |
| `ACO-SPC-004` — Operational Identity Binding And Short-Lived Credentials | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-2, SP800-53-IA-2; CAPEC v3.9: CAPEC-21, CAPEC-59; ASVS v5: ASVS-REQ-V6.3.4, ASVS-REQ-V6.8.4; CWE SDV v4.19.1: CWE-1392, CWE-289; + 9 more sources |
| `ACO-SPC-005` — Secret Usage Isolation Across Pipeline, Workload And Deploy Surfaces | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | DSOMM: DSOMM-ACTIVITY-DA4FF665DCB94E939D2048CDEDC50FC2, DSOMM-ACTIVITY-DF428C9DEFA042269F47A15BB53F822B; MITRE ATLAS: AML.T0008.000, AML.T0024; SP 800-53 r5: SP800-53-SC-7.20, SP800-53-SC-39; CIS Controls v8.1.2: CIS-4.12, CIS-16.8; + 4 more sources |
| `ACO-SPC-006` — Secret Change Auditability And Governance | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-2.7, SP800-53-AC-3.10; PCI DSS v4.0.1: PCI-10.3.2, PCI-11.5.2; ASVS v5: ASVS-REQ-V11.1.4; CAPEC v3.9: CAPEC-678; + 5 more sources |
| `ACO-SPC-007` — Secret Handling And Operational Identity Integrity | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-3; PCI DSS v4.0.1: PCI-REQ-2, PCI-REQ-7; CIS Controls v8.1.2: CIS-3.5, CIS-4; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_A, SAMM-ACTIVITY-D_SA_2_A; + 16 more sources |
| `ACP-SPC-001` — Secret Leak Prevention In Source And Pipeline | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | DSOMM: DSOMM-ACTIVITY-F3C4971E9F4D4E598ED0F0BDB6262477, DSOMM-ACTIVITY-8AE0B92C10E04602BA227524D6AED488; CAPEC v3.9: CAPEC-38, CAPEC-44; SSDF v1.1: SSDF-PRACTICE-PO.1, SSDF-PRACTICE-PS.2; SAMM v2.1: SAMM-ACTIVITY-I_DM_1_A, SAMM-ACTIVITY-I_DM_2_A; + 14 more sources |
| `ACP-SPC-002` — Vault-Backed Secret Storage | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-3.13, SP800-53-AC-4.4; PCI DSS v4.0.1: PCI-REQ-3, PCI-REQ-4; CWE SDV v4.19.1: CWE-256, CWE-257; CIS Controls v8.1.2: CIS-3, CIS-3.1; + 14 more sources |
| `ACP-SPC-003` — Secret Rotation And Renewal Discipline | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-IA-5.13, SP800-53-PS-1; ASVS v5: ASVS-REQ-V6.4.5, ASVS-REQ-V13.3.4; CIS Controls v8.1.2: CIS-14.1; HIPAA: HIPAA-164-308a6; + 3 more sources |
| `ACP-SPC-004` — Operational Identity Binding And OIDC Use | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-2, SP800-53-AC-4.12; ASVS v5: ASVS-REQ-V6.8.1, ASVS-REQ-V6.8.2; PCI DSS v4.0.1: PCI-1.1.1, PCI-4.1.1; CAPEC v3.9: CAPEC-21, CAPEC-196; + 8 more sources |
| `ACP-SPC-005` — Secret Isolation Across Technical Surfaces | P | Practice | cross-chapter → Ch. 07, Ch. 08, Ch. 11 | normative | explicit | Partial | SP 800-53 r5: SP800-53-AC-17.6, SP800-53-AC-20; CAPEC v3.9: CAPEC-22, CAPEC-36; MITRE ATLAS: AML.TA0013, AML.TA0010; CWE SDV v4.19.1: CWE-1104, CWE-1220; + 10 more sources |
| `ACP-SPC-006` — Secret Configuration Governance | P | Practice | cross-chapter → Ch. 00, Ch. 05, Ch. 07, Ch. 13, Ch. 14 | normative | explicit | Partial | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-4.20; NIST AI RMF 1.0: NIST-AI-RMF-GOVERN-1, NIST-AI-RMF-GOVERN-1.3; SAMM v2.1: SAMM-ACTIVITY-G_EG_2_A, SAMM-ACTIVITY-G_EG_3_A; PCI DSS v4.0.1: PCI-REQ-2, PCI-2.2.1; + 9 more sources |

---

## § Manual-only coverage (out-of-Core-scope; ES-grounded direct) {#-manual-only-coverage-out-of-core-scope-es-grounded-direct}

Manual sections covering topics outside the scope of the V1 AppSec Core ontology (maturity models, organisational policies, KPIs/metrics, glossaries) but with direct ES grounding.

| Manual section | Manual V2 anchor | Authority | ES grounding (direct) |
|---|---|---|---|
| `achievable-maturity.md` | MaturityMapping | external | SAMM v2.1 SSDF practices maturity; DSOMM secure dev activities |
| `policies-relevantes.md` | PolicyReference | editorial / external | Secure Development Policy |
| `addon/07-guidelines-equipa.md` | OverlayPlaybook | editorial / external | Operational team guidelines |

---

## § Out-of-AppSec coverage (pure editorial) {#-out-of-appsec-coverage-pure-editorial}

Manual sections that are pure editorial content (worked examples, narratives, illustrative cases, vendor-specific tooling integration). No ES grounding.

| Manual section | Content type | Manual V2 anchor (if any) |
|---|---|---|
| `addon/01-boas-praticas-codigo.md` | Best practices narrative with code snippets | DocumentUnit |
| `addon/05-excecoes-e-justificacoes.md` | Exception cases narrative | DocumentUnit |
| `addon/09-anotacoes-evidencia.md` | Semantic annotation examples | DocumentUnit |

---

## § Future-work register (P8 §10 candidates) {#-future-work-register-p8-10-candidates}

Content gaps registered for future-cycle authoring; honest documentation per P8 §10 limitations.

| V1 entity / topic | Status |
|---|---|
| `ACM-IVF-004` — Centralized Error Translation And Redaction | Authoring pending — Phase 2/3 confirmed_content_gap; programme-lead 2026-05-11 ratified defer. Topic partially covered by Ch. 02 VAL-006/ERR family + Iter 2 §11 LLM input handling. |

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
