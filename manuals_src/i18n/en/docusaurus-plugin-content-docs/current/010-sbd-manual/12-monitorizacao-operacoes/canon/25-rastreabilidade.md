---
id: rastreabilidade
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/canon/25-rastreabilidade.md
  source_sha256: 69d901701a4296ed6120dc000636c2d32d7b89eef63a2c173bd9fdd12fe9371d
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 000e0fce7a34a1f7436a4628c92b2b693370242a7528c9ebb4aca3ae588daf8c
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: ebb6c6bf48bf281085379aa982dcfe014d642265f07b08070d51366e58764173
  glossary_keys: [appsec_core, chapter_role, framework_source_corpus, llm, practitioner_manual, sbdtoe_sbd, slice, traceability, v1_entity_slg_central_ingestion_normalization, v1_entity_slg_centralized_ingestion_accountability, v1_entity_slg_critical_event_catalog_discipline, v1_entity_slg_critical_event_catalog_governance, v1_entity_slg_event_catalog_coverage, v1_entity_slg_structured_centralized_logging, validation_evaluation]
  glossary_sha256: 9d3d1f77d71f6aee8e15f512459f22d004b89606ddae43692003320739592508
  translated_at: 2026-09-26T11:17:35Z
  reviewed_by: null
---

# 25. Traceability — Monitoring and Operations

## Summary {#sumário}

This chapter is the **primary anchor** of the AppSec Core V1 slices: `ACO-SLG` (Security event logging and audit trail).

V1 entity-level coverage: **18 primary entities**. The structure below exposes the **five-section routing** (per Run 1 amendment 2026-05-11; P8 pipeline primitive demonstration):

- **§ Manual ontology V2 entities** — canonical Manual ontology V2 entities mapped to this chapter (KG canonical data)
- **§ Core-mapped coverage** — V1 entity → Manual ontology V2 anchor → Manual section anchor → §26 methodology label → ES grounding
- **§ Manual-only coverage** — Manual sections out-of-Core-scope but directly ES-grounded
- **§ Out-of-AppSec coverage** — Pure editorial sections (examples, narratives) without ES grounding
- **§ Future-work register** — Content gaps registered as P8 §10 candidates

---

## § Manual ontology V2 — canonical entities of this chapter {#-manual-ontology-v2--entities-canónicas-deste-capítulo}

Total: **82 entities** of Manual ontology V2 mapped to this chapter via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `OPS-001` | Structured and persistent logging for all components in production | normative | explicit | deterministic |
| Requirement | `OPS-002` | Catalogue of critical security events defined and verified | normative | explicit | deterministic |
| Requirement | `OPS-003` | Log retention in accordance with policy and regulatory requirements | normative | explicit | deterministic |
| Requirement | `OPS-004` | Centralisation of logs in a SIEM system or equivalent | normative | explicit | deterministic |
| Requirement | `OPS-005` | Automatic alerts for critical security events | normative | explicit | deterministic |
| Requirement | `OPS-006` | Alert response SLA defined and measured | normative | explicit | deterministic |
| Requirement | `OPS-007` | Integration with a formal incident response process | normative | explicit | deterministic |
| Requirement | `OPS-008` | Correlation of events across multiple sources | normative | explicit | deterministic |
| Requirement | `OPS-009` | Behavioural detection and baseline of normal activity | normative | explicit | deterministic |
| Requirement | `OPS-010` | Monitoring effectiveness metrics measured and reviewed | normative | explicit | deterministic |
| Control | `CTRL-monitoring-monitorizacao-e-resposta-operacional-1797f0af70` | Monitoring and operational response | normative | explicit | deterministic |
| Practice | `12-monitorizacao-operacoes:alertas-com-slas-definidosum-alerta-sem-prazo-de-resposta-e-apenas-ruido` | Alerts with defined SLAsAn alert without a response deadline is just noise. | normative | explicit | deterministic |
| Practice | `12-monitorizacao-operacoes:classificacao-e-cobertura-de-dominios-de-monitorizacao` | Classification and Coverage of Monitoring Domains | normative | explicit | deterministic |
| Practice | `12-monitorizacao-operacoes:correlacao-de-eventos-e-detecao-comportamental` | Event Correlation and Behavioural Detection | normative | explicit | deterministic |
| Practice | `12-monitorizacao-operacoes:definicao-de-eventos-e-metricas-criticas` | Definition of critical events and metrics | normative | explicit | deterministic |
| Practice | `12-monitorizacao-operacoes:integracao-com-processos-de-resposta-a-incidentes` | Integration with incident response processes | normative | explicit | deterministic |
| Practice | `12-monitorizacao-operacoes:integracao-com-siem-e-normalizacao-de-eventos` | SIEM Integration and Event Normalisation | normative | explicit | deterministic |
| Practice | `12-monitorizacao-operacoes:logging-estruturado-e-centralizado` | Structured and centralised logging | normative | explicit | deterministic |
| Practice | `12-monitorizacao-operacoes:metricas-de-eficacia-mttd-mttr` | Effectiveness metrics (MTTD/MTTR) | normative | explicit | deterministic |
| Practice | `12-monitorizacao-operacoes:proporcionalidade-de-controlos-por-risco-l1l3-e-dominios` | Proportionality of Controls by Risk (L1–L3) and Domains | normative | explicit | deterministic |
| Practice | `12-monitorizacao-operacoes:rastreabilidade-e-conformidade-com-regulacoes-ssdf-nis2-iso-27001` | Traceability and Compliance with Regulations (SSDF, NIS2, ISO 27001) | normative | explicit | deterministic |
| Practice | `12-monitorizacao-operacoes:seguranca-e-integridade-de-logs` | Log Security and Integrity | normative | explicit | deterministic |
| Practice | `12-monitorizacao-operacoes:validacao-e-tuning-de-alertas` | Alert Validation and *Tuning* | normative | explicit | deterministic |
| Threat | `None` | hybrid | normative | heuristic | bounded |
| Concept | `sem:concept:alert-fatigue` | Alert fatigue | semantic | scored | bounded |
| Concept | `sem:concept:alertas-acionaveis` | Actionable alerts | semantic | scored | bounded |
| Concept | `sem:concept:canal-de-notificacao` | Notification channel | semantic | scored | bounded |
| Concept | `sem:concept:condicao` | Condition | semantic | scored | bounded |
| Concept | `sem:concept:dominios-de-monitorizacao` | monitoring domains | semantic | scored | bounded |
| Concept | `sem:concept:fonte-de-dados` | Data source | semantic | scored | bounded |
| Concept | `sem:concept:integracao-com-irp` | Integration with IRP | semantic | scored | bounded |
| Concept | `sem:concept:inteligencia-acionavel` | Actionable intelligence | semantic | scored | bounded |
| Concept | `sem:concept:logging-estruturado` | structured logging | semantic | scored | bounded |
| Concept | `sem:concept:logs` | Logs | semantic | scored | bounded |
| Concept | `sem:concept:logs-nao-estruturados` | Unstructured logs | semantic | scored | bounded |
| Concept | `sem:concept:medicao-continua` | Continuous measurement | semantic | scored | bounded |
| Concept | `sem:concept:nis2` | NIS2 | semantic | scored | bounded |
| Concept | `sem:concept:proporcionalidade` | Proportionality | semantic | scored | bounded |
| Concept | `sem:concept:retencao-insuficiente` | Insufficient retention | semantic | scored | bounded |
| Concept | `sem:concept:runbook` | Runbook | semantic | scored | bounded |
| Concept | `sem:concept:severidade` | Severity | semantic | scored | bounded |
| Concept | `sem:concept:ssdf` | SSDF | semantic | scored | bounded |
| Concept | `sem:concept:visibilidade` | Visibility | semantic | scored | bounded |
| Mechanism | `sem:mechanism:alertas-com-slas-e-playbooks` | Alerts with SLAs and playbooks | semantic | scored | bounded |
| Mechanism | `sem:mechanism:automacao` | Automation | semantic | scored | bounded |
| Mechanism | `sem:mechanism:canal-de-notificacao` | Notification channel | semantic | scored | bounded |
| Mechanism | `sem:mechanism:controlos-de-monitorizacao` | Monitoring controls | semantic | scored | bounded |
| Mechanism | `sem:mechanism:formato-legivel-por-maquina-ex-json` | machine-readable format (e.g. JSON) | semantic | scored | bounded |
| Mechanism | `sem:mechanism:integracao-com-irp` | Integration with IRP | semantic | scored | bounded |
| Mechanism | `sem:mechanism:logging` | logging | semantic | scored | bounded |
| Mechanism | `sem:mechanism:metricas` | Metrics | semantic | scored | bounded |
| Mechanism | `sem:mechanism:regra-de-alerta` | Alert rule | semantic | scored | bounded |
| Mechanism | `sem:mechanism:resposta-a-incidentes` | Incident response | semantic | scored | bounded |
| Mechanism | `sem:mechanism:runbook` | Runbook | semantic | scored | bounded |
| Mechanism | `sem:mechanism:sistema-centralizado` | centralised system | semantic | scored | bounded |
| Pattern | `sem:pattern:alerta-baseado-em-evento-critico` | Alert based on critical event | semantic | scored | bounded |
| Pattern | `sem:pattern:monitorizacao-proativa` | Proactive monitoring | semantic | scored | bounded |
| Pattern | `sem:pattern:proporcionalidade-na-monitorizacao` | Proportionality in monitoring | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:alertas-nao-acionaveis` | Non-actionable alerts | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:demasiados-alertas` | Too many alerts | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:detecao-sem-resposta` | Detection without response | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:falta-de-integracao-com-irp` | Lack of integration with IRP | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:logs-incompletos-ou-ignorados` | Incomplete or ignored logs | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:logs-nao-estruturados` | Unstructured logs | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:retencao-insuficiente` | Insufficient retention | semantic | scored | bounded |
| Signal | `sem:signal:falhas-de-login` | Login failures | semantic | scored | bounded |
| Signal | `sem:signal:logs` | Logs | semantic | scored | bounded |
| Signal | `sem:signal:metricas-mttd-mttr` | MTTD/MTTR metrics | semantic | scored | bounded |

> Authority class / source mode / confidence model: per Manual ontology V2 definition (`sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml`, `meta.version: '2.0'`).

---

## § Core-mapped coverage {#-core-mapped-coverage}

Table exposing V1 entity-level coverage with Manual ontology V2 anchor + Manual section anchor + §26 methodology label + substrate v7 ES grounding.

### Slice `ACO-SLG` — Security event logging and audit trail {#slice-aco-slg--logging-de-eventos-de-segurança-e-audit-trail}

| V1 entity | Type | Manual V2 anchor | Manual section anchor | Authority | Source mode | §26 label | ES grounding |
|---|---|---|---|---|---|---|---|
| `ACM-SLG-001` — Machine-Readable Structured Logging | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SAMM v2.1: SAMM-ACTIVITY-V_AA_1_A, SAMM-ACTIVITY-V_AA_1_B; CAPEC v3.9: CAPEC-637; DSOMM: DSOMM-ACTIVITY-7C7350896A83419F8B27C1E676CEDEA1; PCI DSS v4.0.1: PCI-REQ-10 |
| `ACM-SLG-002` — Central Log Ingestion And Normalization | M | Mechanism | chapter prose (central, forwarding, ingestion kws verified) | semantic | scored | Semantic | CIS Controls v8.1.2: CIS-1, CIS-1.1; SP 800-53 r5: SP800-53-CM-8.7, SP800-53-SA-19.3; DSOMM: DSOMM-ACTIVITY-2A44B708734F4463B0CB86DC46344B2F; OWASP LLM Top 10: LLM03-2025; + 1 more sources |
| `ACM-SLG-003` — Log Integrity And Access Controls | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2; PCI DSS v4.0.1: PCI-REQ-1, PCI-REQ-3; CAPEC v3.9: CAPEC-1, CAPEC-21; ASVS v5: ASVS-REQ-V1.2.4, ASVS-REQ-V1.5.2; + 21 more sources |
| `ACM-SLG-004` — Logging Failure Visibility Controls | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AU-5.4, SP800-53-MA-1; CWE SDV v4.19.1: CWE-1118, CWE-391; SAMM v2.1: SAMM-ACTIVITY-I_DM_1_A, SAMM-ACTIVITY-O_IM_3_A; ASVS v5: ASVS-REQ-V16.5.2, ASVS-REQ-V16.5.4; + 4 more sources |
| `ACM-SLG-005` — Security Event Catalog And Coverage Verification | M | Mechanism | chapter prose (audit, coverage, define kws verified) | semantic | scored | Semantic | SAMM v2.1: SAMM-ACTIVITY-D_SR_1_B, SAMM-ACTIVITY-D_TA_3_A; SP 800-53 r5: SP800-53-AU-1, SP800-53-AU-2; DSOMM: DSOMM-ACTIVITY-9768F154357A4C06AF6FD66570677C9B, DSOMM-ACTIVITY-F0E018143B884BD0A3A9F91DB001D20BADVANCED; PCI DSS v4.0.1: PCI-REQ-11, PCI-1.1.1; + 12 more sources |
| `ACM-SLG-006` — Log Retention Lifecycle Management Controls | M | Mechanism | chapter prose (lifecycle, logs, management kws verified) | semantic | scored | Semantic | SP 800-53 r5: SP800-53-AU-5.1, SP800-53-CM-1; CIS Controls v8.1.2: CIS-3.4, CIS-5.3; CAPEC v3.9: CAPEC-546; DSOMM: DSOMM-ACTIVITY-7F36B9BABC054FD69A2A73344C249722; + 5 more sources |
| `ACO-SLG-001` — Critical Security Event Coverage And Catalog Discipline | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-1, SP800-53-AU-5.2; PCI DSS v4.0.1: PCI-REQ-11, PCI-5.2.3; DSOMM: DSOMM-ACTIVITY-48F97F31931C46EB9B3EE2FEC0CD0426, DSOMM-ACTIVITY-0A929C3EAB9A42068761ADF84B74622E; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_A, SAMM-ACTIVITY-D_SR_1_B; + 12 more sources |
| `ACO-SLG-002` — Structured Audit Fields And Machine-Readable Log Shape | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-4.1, SP800-53-AC-16; ASVS v5: ASVS-REQ-V15.3.1; PCI DSS v4.0.1: PCI-1.2.4 |
| `ACO-SLG-003` — Log Integrity Protection And Access Discipline | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-3, SP800-53-AC-3.4; PCI DSS v4.0.1: PCI-REQ-3, PCI-4.2.1; CIS Controls v8.1.2: CIS-3.1, CIS-3.2; ASVS v5: ASVS-REQ-V6.3.8, ASVS-REQ-V11.3.3; + 9 more sources |
| `ACO-SLG-004` — Audit Record Retention And Lifecycle Governance | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AU-7, SP800-53-AU-10.3; CIS Controls v8.1.2: CIS-3.4, CIS-6.2; PCI DSS v4.0.1: PCI-3.2.1, PCI-10.5.1; CAPEC v3.9: CAPEC-675; + 3 more sources |
| `ACO-SLG-005` — Centralized Log Ingestion And Source Accountability | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-2, SP800-53-AC-8; CIS Controls v8.1.2: CIS-1, CIS-2; CAPEC v3.9: CAPEC-150, CAPEC-384; DSOMM: DSOMM-ACTIVITY-95CAEF9636ED458CA0875C35D4F9DEC2, DSOMM-ACTIVITY-82E499D1F4634A4BBE9068812A874AF6; + 3 more sources |
| `ACO-SLG-006` — Logging Pipeline Health And Silent-Failure Visibility | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | CWE SDV v4.19.1: CWE-117, CWE-391 |
| `ACO-SLG-007` — Security Logging And Audit Trail Assurance | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AT-4, SP800-53-AU-5; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_B, SAMM-ACTIVITY-D_SA_2_A; ASVS v5: ASVS-REQ-V6.1.3, ASVS-REQ-V6.3.4; CIS Controls v8.1.2: CIS-4.1, CIS-4.2; + 12 more sources |
| `ACP-SLG-001` — Critical Event Catalog Governance | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AU-2, SP800-53-AU-2.2; CWE SDV v4.19.1: CWE-778; PCI DSS v4.0.1: PCI-10.7.2 |
| `ACP-SLG-002` — Structured And Centralized Security Logging | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | CIS Controls v8.1.2: CIS-1.1, CIS-1.4; SP 800-53 r5: SP800-53-AC-12.1, SP800-53-AU-2; DSOMM: DSOMM-ACTIVITY-4ECED38A79044C45ADB050B663065540, DSOMM-ACTIVITY-FE875E17AE4A45F8A359244AA4FCBC04; SAMM v2.1: SAMM-ACTIVITY-I_DM_1_A, SAMM-ACTIVITY-I_SB_3_A; + 4 more sources |
| `ACP-SLG-003` — Log Integrity And Protected Access | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2; PCI DSS v4.0.1: PCI-REQ-3, PCI-REQ-4; ASVS v5: ASVS-REQ-V1.2.4, ASVS-REQ-V1.2.6; CAPEC v3.9: CAPEC-21, CAPEC-22; + 22 more sources |
| `ACP-SLG-004` — Log Retention And Lifecycle Governance | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AU-4, SP800-53-AU-5.1; SAMM v2.1: SAMM-ACTIVITY-G_PC_1_A, SAMM-ACTIVITY-G_PC_3_B; CIS Controls v8.1.2: CIS-3.4, CIS-8.1; PCI DSS v4.0.1: PCI-3.2.1, PCI-10.5.1; + 1 more sources |
| `ACP-SLG-005` — Logging Pipeline Health Visibility | P | Practice | chapter prose (detect, logging, pipeline kws verified) | normative | explicit | Semantic | SP 800-53 r5: SP800-53-AU-5.4, SP800-53-MA-1; SAMM v2.1: SAMM-ACTIVITY-O_EM_3_A, SAMM-ACTIVITY-O_IM_3_A; ASVS v5: ASVS-REQ-V16.5.4; OWASP LLM Top 10: LLM03-2025 |

---

## § Manual-only coverage (out-of-Core-scope; ES-grounded direct) {#-manual-only-coverage-out-of-core-scope-es-grounded-direct}

Manual sections covering topics outside the scope of the V1 AppSec Core ontology (maturity models, organisational policies, KPIs/metrics, glossaries) but with direct ES grounding.

| Manual section | Manual V2 anchor | Authority | ES grounding (direct) |
|---|---|---|---|
| `achievable-maturity.md` | MaturityMapping | external | SAMM v2.1 OE/IM maturity; DSOMM operations activities |
| `policies-relevantes.md` | PolicyReference | editorial / external | Monitoring and Incident Response Policy |
| `addon/04-integracao-siem.md` | ExternalObligation | external | SIEM/SOAR integration (operational) |

---

## § Out-of-AppSec coverage (pure editorial) {#-out-of-appsec-coverage-pure-editorial}

Manual sections that are pure editorial content (worked examples, narratives, illustrative cases, vendor-specific tooling integration). No ES grounding.

| Manual section | Content type | Manual V2 anchor (if any) |
|---|---|---|
| `casos-praticos-monitorizacao.md` | Worked examples: incident response cases | DocumentUnit |
| `addon/09-exemplos-eventos.md` | Examples of security events | DocumentUnit |

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
