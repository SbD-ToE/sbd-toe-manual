---
id: rastreabilidade
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/canon/25-rastreabilidade.md
  source_sha256: c413746d30df02fc6b444f5b5327a80a86a7d9e0e87aa76c59951360775a9370
  source_commit: e341b40c451d9ef4be61e6cd59d994cda54c1aa0
  target_sha256: 1292d8e06a75f08fbe5e37c3f92a641b92cf9efa4902ba6c47c45499c4641470
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [appsec_core, avaliacao, chapter_role, discipline, mcp, practitioner_manual, sbdtoe_sbd, slice, slug_threat_modeling, traceability, v1_entity_atb_dfd_modeling, v1_entity_iat_authorization_policy, v1_entity_iat_least_privilege_authorization, v1_entity_its_authorized_peer_policies, v1_entity_its_authorized_peer_validation, validation_evaluation]
  glossary_sha256: 7825a4c17bfb909ab7d3ce5dd01c502a94b97e8d51e6dddd88bae0c831b58bae
  translated_at: 2026-09-26T13:36:58Z
  reviewed_by: null
---

# 25. Traceability — Secure Architecture

## Summary {#sumário}

This chapter is the **primary anchor** of the AppSec Core V1 slices: `ACO-ATB` (Secure architecture and trust boundaries), `ACO-IAT` (Identity, authentication and session management), `ACO-ITS` (Integration and service-to-service security).

V1 entity-level coverage: **56 primary entities**. The structure below exposes the **five-section routing** (per Run 1 amendment 2026-05-11; P8 pipeline primitive demonstration):

- **§ Manual ontology V2 entities** — canonical Manual ontology V2 entities mapped to this chapter (KG canonical data)
- **§ Core-mapped coverage** — V1 entity → Manual ontology V2 anchor → Manual section anchor → §26 methodology label → ES grounding
- **§ Manual-only coverage** — Manual sections out-of-Core-scope but directly ES-grounded
- **§ Out-of-AppSec coverage** — Pure editorial sections (examples, narratives) without ES grounding
- **§ Future-work register** — Content gaps registered as P8 §10 candidates

---

## § Manual ontology V2 — canonical entities of this chapter {#-manual-ontology-v2--entities-canónicas-deste-capítulo}

Total: **100 entities** of Manual ontology V2 mapped to this chapter via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `ARC-001` | Trust zones identified and documented | normative | explicit | deterministic |
| Requirement | `ARC-002` | External exposure minimised and justified | normative | explicit | deterministic |
| Requirement | `ARC-003` | Architecture review with a security focus | normative | explicit | deterministic |
| Requirement | `ARC-004` | Architecture decisions documented | normative | explicit | deterministic |
| Requirement | `ARC-005` | Threat modelling integrated into critical flows | normative | explicit | deterministic |
| Requirement | `ARC-006` | Technical isolation controls between sensitive domains | normative | explicit | deterministic |
| Requirement | `ARC-007` | Reusable and approved architecture patterns | normative | explicit | deterministic |
| Requirement | `ARC-008` | Data flows between trust zones protected | normative | explicit | deterministic |
| Requirement | `ARC-009` | Significant changes trigger a new review | normative | explicit | deterministic |
| Requirement | `ARC-010` | Architecture diagrams versioned and accessible | normative | explicit | deterministic |
| Requirement | `ARC-011` | Logical and physical segmentation between environments | normative | explicit | deterministic |
| Requirement | `ARC-012` | Formal approval criteria for high-risk applications | normative | explicit | deterministic |
| Requirement | `ARC-013` | Automatic topology validation in CI/CD or as code | normative | explicit | deterministic |
| Control | `CTRL-governance-arquitetura-segura-e-rastreavel-74562442c4` | Secure and traceable architecture | normative | explicit | deterministic |
| Control | `CTRL-infrastructure-segmentacao-e-controlo-arquitetural-dceb3c1f0b` | Segmentation and architectural control | normative | explicit | deterministic |
| Practice | `04-arquitetura-segura:atualizacao-da-baseline-apos-alteracao-arquitetural-significativa` | Updating of the baseline after a significant architectural change | normative | explicit | deterministic |
| Practice | `04-arquitetura-segura:avaliacao-de-impacto-no-negocio-e-priorizacao-de-trade-offs` | Business impact assessment and prioritisation of trade-offs | normative | explicit | deterministic |
| Practice | `04-arquitetura-segura:catalogo-de-padroes-de-arquitetura-segura-reutilizacao-governada` | Catalogue of secure architecture patterns (governed reuse) | normative | explicit | deterministic |
| Practice | `04-arquitetura-segura:definicao-de-principios-e-baseline-de-arquitetura-segura` | Definition of secure architecture principles and baseline | normative | explicit | deterministic |
| Practice | `04-arquitetura-segura:ficha-de-solucao-com-controlos-e-rastreabilidade-arquitetural` | Solution sheet with controls and architectural traceability | normative | explicit | deterministic |
| Practice | `04-arquitetura-segura:gate-arquitetural-antes-do-go-live` | Architectural gate before Go-live | normative | explicit | deterministic |
| Practice | `04-arquitetura-segura:gestao-de-decisoes-arquiteturais-adr` | Management of architectural decisions (ADR) | normative | explicit | deterministic |
| Practice | `04-arquitetura-segura:gestao-de-excecoes-arquiteturais-com-controlos-compensatorios` | Management of architectural exceptions with compensating controls | normative | explicit | deterministic |
| Practice | `04-arquitetura-segura:identificacao-e-governacao-de-componentes-nao-deterministicos` | Identification and governance of non-deterministic components | normative | explicit | deterministic |
| Practice | `04-arquitetura-segura:revisao-de-fronteiras-de-confianca-e-integracoes` | Review of trust boundaries and integrations | normative | explicit | deterministic |
| Practice | `04-arquitetura-segura:revisao-formal-de-arquitetura-para-l3-governacao-reforcada` | Formal architecture review for L3 (reinforced governance) | normative | explicit | deterministic |
| Practice | `04-arquitetura-segura:revisao-formal-do-design-arquitetural` | Formal review of the architectural design | normative | explicit | deterministic |
| Practice | `04-arquitetura-segura:sincronizacao-threat-modeling-arquitetura` | Threat Modelling ↔ Architecture synchronisation | normative | explicit | deterministic |
| Practice | `04-arquitetura-segura:triggers-de-arquitetura-viva-e-disciplina-de-revisao` | “Living architecture” triggers and review discipline | normative | explicit | deterministic |
| Practice | `04-arquitetura-segura:validacao-arquitetural-automatizavel-no-ci-cd-quando-aplicavel` | Automatable architectural validation in the CI/CD (where applicable) | normative | explicit | deterministic |
| Threat | `MT-055` | Exposed interfaces without isolation | normative | heuristic | bounded |
| Threat | `MT-056` | Data and control mixed in the same zone | normative | heuristic | bounded |
| Threat | `MT-057` | Uncontrolled lateral access between modules | normative | heuristic | bounded |
| Threat | `MT-058` | Absence of isolation between users | normative | heuristic | bounded |
| Threat | `MT-059` | Non-existent or outdated architecture | normative | heuristic | bounded |
| Threat | `MT-060` | Confusion about the location of controls | normative | heuristic | bounded |
| Threat | `MT-061` | Ambiguity about boundaries and zones | normative | heuristic | bounded |
| Threat | `MT-062` | Architecture does not review fallback mechanisms | normative | heuristic | bounded |
| Threat | `MT-063` | Architecture never reviewed | normative | heuristic | bounded |
| Threat | `MT-064` | Structural changes without revalidation | normative | heuristic | bounded |
| Threat | `MT-065` | Informal or ad hoc design | normative | heuristic | bounded |
| Threat | `MT-066` | Architecture exceptions without a trace | normative | heuristic | bounded |
| Threat | `MT-067` | Architecture requirements not defined | normative | heuristic | bounded |
| Threat | `MT-068` | Impossibility of mapping decisions to controls | normative | heuristic | bounded |
| Threat | `MT-069` | Diagram does not reflect implemented controls | normative | heuristic | bounded |
| Threat | `MT-070` | L1 applications treated as critical | normative | heuristic | bounded |
| Threat | `MT-071` | Over-dimensioning of the architecture's security | normative | heuristic | bounded |
| Threat | `MT-072` | Execution environments not reflected in the design | normative | heuristic | bounded |
| Concept | `sem:concept:confianca` | trust | semantic | scored | bounded |
| Concept | `sem:concept:controlos-de-seguranca` | Security controls | semantic | scored | bounded |
| Concept | `sem:concept:controlos-interzonais` | inter-zone controls | semantic | scored | bounded |
| Concept | `sem:concept:decisoes-de-arquitetura` | Architecture decisions | semantic | scored | bounded |
| Concept | `sem:concept:dependencia-circular` | circular dependency | semantic | scored | bounded |
| Concept | `sem:concept:excecoes-nao-documentadas` | Undocumented exceptions | semantic | scored | bounded |
| Concept | `sem:concept:exposicao` | exposure | semantic | scored | bounded |
| Concept | `sem:concept:fronteiras` | boundaries | semantic | scored | bounded |
| Concept | `sem:concept:gestao-centralizada-de-excecoes` | Centralised management of exceptions | semantic | scored | bounded |
| Concept | `sem:concept:modelo-de-arquitetura` | Architecture model | semantic | scored | bounded |
| Concept | `sem:concept:modelos-reutilizaveis` | Reusable models | semantic | scored | bounded |
| Concept | `sem:concept:padroes-de-arquitetura` | Architecture patterns | semantic | scored | bounded |
| Concept | `sem:concept:proporcionalidade-dos-controlos` | Proportionality of controls | semantic | scored | bounded |
| Concept | `sem:concept:requisitos-e-padroes` | requirements and patterns | semantic | scored | bounded |
| Concept | `sem:concept:revisao-de-arquitetura` | architecture review | semantic | scored | bounded |
| Concept | `sem:concept:risco-nao-rastreavel` | Untraceable risk | semantic | scored | bounded |
| Concept | `sem:concept:superficie-de-ataque` | Attack surface | semantic | scored | bounded |
| Concept | `sem:concept:threat-modeling` | Threat Modelling | semantic | scored | bounded |
| Concept | `sem:concept:validacao-de-arquitetura` | Architecture validation | semantic | scored | bounded |
| Concept | `sem:concept:zonas-de-confianca` | Trust zones | semantic | scored | bounded |
| Concept | `sem:concept:ztcs` | ZTCs | semantic | scored | bounded |
| Mechanism | `sem:mechanism:adrs-architecture-decision-records` | ADRs (Architecture Decision Records) | semantic | scored | bounded |
| Mechanism | `sem:mechanism:api-gateway-com-autenticacao-mutua` | API Gateway with mutual authentication | semantic | scored | bounded |
| Mechanism | `sem:mechanism:autenticacao` | authentication | semantic | scored | bounded |
| Mechanism | `sem:mechanism:circuit-breakers` | circuit breakers | semantic | scored | bounded |
| Mechanism | `sem:mechanism:controlo-de-acesso` | access control | semantic | scored | bounded |
| Mechanism | `sem:mechanism:diagramas-versionados` | Versioned diagrams | semantic | scored | bounded |
| Mechanism | `sem:mechanism:logging` | logging | semantic | scored | bounded |
| Mechanism | `sem:mechanism:mecanismos-de-contencao` | Containment mechanisms | semantic | scored | bounded |
| Mechanism | `sem:mechanism:segmentacao-de-trafego` | Traffic segmentation | semantic | scored | bounded |
| Mechanism | `sem:mechanism:timeouts` | timeouts | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:dependencia-circular` | circular dependency | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:excecoes-nao-documentadas` | Undocumented exceptions | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:modelos-inconsistentes-incompletos-ou-desatualizados` | Inconsistent, incomplete or outdated models | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:threat-modeling-sem-arquitetura-clara` | Threat modelling without a clear architecture | semantic | scored | bounded |

> Authority class / source mode / confidence model: per Manual ontology V2 definition (`sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml`, `meta.version: '2.0'`).

---

## § Core-mapped coverage {#-core-mapped-coverage}

Table exposing V1 entity-level coverage with Manual ontology V2 anchor + Manual section anchor + §26 methodology label + substrate v7 ES grounding.

### Slice `ACO-ATB` — Secure architecture and trust boundaries {#slice-aco-atb--arquitetura-segura-e-fronteiras-de-confiança}

| V1 entity | Type | Manual V2 anchor | Manual section anchor | Authority | Source mode | §26 label | ES grounding |
|---|---|---|---|---|---|---|---|
| `ACM-ATB-001` — Versioned Diagrams And ADR Records | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2; PCI DSS v4.0.1: PCI-REQ-1, PCI-REQ-2; CIS Controls v8.1.2: CIS-2, CIS-2.2; SAMM v2.1: SAMM-ACTIVITY-D_SA_2_A, SAMM-ACTIVITY-D_SR_2_A; + 14 more sources |
| `ACM-ATB-002` — Trust-Boundary And DFD Modeling | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-4.19, SP800-53-CP-7.5; DSOMM: DSOMM-ACTIVITY-0DE465A655A74343AF79948BB5FF10BA, DSOMM-ACTIVITY-48F97F31931C46EB9B3EE2FEC0CD0426; SAMM v2.1: SAMM-ACTIVITY-D_SA_2_A, SAMM-ACTIVITY-D_SA_3_B; SAFECode FPSSD: SCFPSSD-DESIGN-PRINCIPLES, SCFPSSD-THREAT-MODELING; + 6 more sources |
| `ACM-ATB-003` — Boundary Mediation Controls | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AT-3.1, SP800-53-CP-10.3; CWE SDV v4.19.1: CWE-497, CWE-654 |
| `ACM-ATB-004` — Architecture Review Gates | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AU-2.3, SP800-53-CM-2.1; SAMM v2.1: SAMM-ACTIVITY-D_SA_2_B, SAMM-ACTIVITY-O_OM_3_B; NIST AI RMF 1.0: NIST-AI-RMF-GOVERN-1.5; DSOMM: DSOMM-ACTIVITY-3F63BDBCC75F4780A941E6AD42E894E1 |
| `ACM-ATB-005` — Automated Topology Validation Jobs | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-CA-5.1, SP800-53-CM-2.2; SAMM v2.1: SAMM-ACTIVITY-I_SB_2_A, SAMM-ACTIVITY-V_RT_2_A; DSOMM: DSOMM-ACTIVITY-67E1A9AA9FBF4EC5A2DE400F01960C51, DSOMM-ACTIVITY-017D9E2642B549A4B9459F59B308FB99; MITRE ATLAS: AML.M0008, AML.M0033; + 5 more sources |
| `ACO-ATB-001` — Architecture Baseline And Decision Traceability | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SAMM v2.1: SAMM-ACTIVITY-V_AA_1_A, SAMM-ACTIVITY-V_AA_1_B; SP 800-53 r5: SP800-53-SA-5.3 |
| `ACO-ATB-002` — Trust Boundary Clarity And Protected Data Flows | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-3; PCI DSS v4.0.1: PCI-REQ-3, PCI-1.2.2; CWE SDV v4.19.1: CWE-1220, CWE-182; CIS Controls v8.1.2: CIS-3, CIS-3.1; + 18 more sources |
| `ACO-ATB-003` — External Exposure Justification And Boundary Mediation | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | MITRE ATLAS: AML.T0048, AML.T0048.002; SP 800-53 r5: SP800-53-IR-9.4, SP800-53-MP-5.1 |
| `ACO-ATB-004` — Technical Segmentation And Sensitive Domain Isolation | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-4.23, SP800-53-AC-6.4; CAPEC v3.9: CAPEC-390, CAPEC-516; CIS Controls v8.1.2: CIS-3.12, CIS-16.8; CWE SDV v4.19.1: CWE-653; + 4 more sources |
| `ACO-ATB-005` — Architecture Review And Change Trigger Discipline | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AU-1, SP800-53-AU-2.3; SAMM v2.1: SAMM-ACTIVITY-D_TA_3_A, SAMM-ACTIVITY-V_AA_3_B; CIS Controls v8.1.2: CIS-17.8; NIST AI RMF 1.0: NIST-AI-RMF-GOVERN-1.5; + 1 more sources |
| `ACO-ATB-006` — Architectural Topology Validation And Pattern Conformance | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-CM-3.2, SP800-53-CM-6.1; SAMM v2.1: SAMM-ACTIVITY-V_AA_2_A, SAMM-ACTIVITY-V_RT_1_A; CAPEC v3.9: CAPEC-80, CAPEC-231; MITRE ATLAS: AML.T0042, AML.M0008; + 7 more sources |
| `ACO-ATB-007` — Secure Architecture Governance And Boundary Integrity | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-PL-2, SP800-53-PL-8; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_A, SAMM-ACTIVITY-D_SA_1_B; CIS Controls v8.1.2: CIS-4, CIS-4.1; CAPEC v3.9: CAPEC-184, CAPEC-440; + 16 more sources |
| `ACP-ATB-001` — Architecture Baseline Definition | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SAMM v2.1: SAMM-ACTIVITY-D_SA_3_A, SAMM-ACTIVITY-I_SB_3_A; SP 800-53 r5: SP800-53-CM-2, SP800-53-PL-2; CIS Controls v8.1.2: CIS-12.2; DSOMM: DSOMM-ACTIVITY-5992C38C8597403589DBD15820D81C3A; + 2 more sources |
| `ACP-ATB-002` — Architectural Decision And Solution Traceability | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AU-12.1, SP800-53-CM-8; SAMM v2.1: SAMM-ACTIVITY-I_DM_3_A, SAMM-ACTIVITY-O_EM_1_A; CAPEC v3.9: CAPEC-580, CAPEC-581; PCI DSS v4.0.1: PCI-REQ-8, PCI-10.4.2; + 5 more sources |
| `ACP-ATB-003` — Trust-Boundary And Flow Review | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-4, SP800-53-AC-4.1; DSOMM: DSOMM-ACTIVITY-0DE465A655A74343AF79948BB5FF10BA, DSOMM-ACTIVITY-AE22DAFDBCD641EEBA018B7FE6FC1AD9; SAMM v2.1: SAMM-ACTIVITY-D_SA_2_A, SAMM-ACTIVITY-D_SA_3_B; SSDF v1.1: SSDF-PRACTICE-PO.4, SSDF-PRACTICE-PO.5; + 10 more sources |
| `ACP-ATB-004` — External Exposure And Boundary Mediation Design | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-IR-9.4, SP800-53-MP-5.1; CWE SDV v4.19.1: CWE-1230, CWE-497; HIPAA: HIPAA-164-308a6; MITRE ATLAS: AML.T0048 |
| `ACP-ATB-005` — Architecture Review And Approval Governance | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SAMM v2.1: SAMM-ACTIVITY-G_PC_1_B, SAMM-ACTIVITY-G_SM_1_A; SP 800-53 r5: SP800-53-MA-3, SP800-53-PL-2.2 |
| `ACP-ATB-006` — Architecture Change Trigger Discipline | P | Practice | chapter prose (architecture, governance, review kws verified) | normative | explicit | Semantic | SP 800-53 r5: SP800-53-AU-1, SP800-53-AU-6; SAMM v2.1: SAMM-ACTIVITY-D_TA_3_A |
| `ACP-ATB-007` — Automatable Topology And Pattern Validation | P | Practice | cross-chapter → Ch. 03, Ch. 08, Ch. 13 | normative | explicit | Partial | SP 800-53 r5: SP800-53-CM-2.2, SP800-53-CM-3.2; SAMM v2.1: SAMM-ACTIVITY-V_AA_2_A, SAMM-ACTIVITY-V_RT_1_A; DSOMM: DSOMM-ACTIVITY-48E92BB1FDBA40E8B6C235DE0D431833, DSOMM-ACTIVITY-017D9E2642B549A4B9459F59B308FB99; CAPEC v3.9: CAPEC-80; + 3 more sources |

### Slice `ACO-IAT` — Identity, authentication and session management {#slice-aco-iat--identidade-autenticação-e-gestão-de-sessões}

| V1 entity | Type | Manual V2 anchor | Manual section anchor | Authority | Source mode | §26 label | ES grounding |
|---|---|---|---|---|---|---|---|
| `ACM-IAT-001` — Authentication And Federation Protocols | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-7.4, SP800-53-CP-13; ASVS v5: ASVS-REQ-V6.3.3, ASVS-REQ-V6.3.5; CWE SDV v4.19.1: CWE-1392, CWE-294; CAPEC v3.9: CAPEC-90, CAPEC-151; + 10 more sources |
| `ACM-IAT-002` — Access Policy Enforcement | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2; CAPEC v3.9: CAPEC-1, CAPEC-8; MITRE ATLAS: AML.TA0000, AML.TA0012; PCI DSS v4.0.1: PCI-REQ-7, PCI-REQ-9; + 20 more sources |
| `ACM-IAT-003` — Periodic Review And Access Audit | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-2, SP800-53-AC-2.4; SAMM v2.1: SAMM-ACTIVITY-D_SA_2_B, SAMM-ACTIVITY-G_EG_3_A; CIS Controls v8.1.2: CIS-5.5, CIS-6.2; HIPAA: HIPAA-164-308a8, HIPAA-164-312b; + 5 more sources |
| `ACM-IAT-004` — Short-Lived Token Controls | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | CAPEC v3.9: CAPEC-39, CAPEC-59; ASVS v5: ASVS-REQ-V7.2.3, ASVS-REQ-V7.2.4; SP 800-53 r5: SP800-53-AC-12, SP800-53-AC-12.1; OWASP MCP Top 10: MCP01-2025, MCP10-2025; + 3 more sources |
| `ACM-IAT-005` — API Gateway Mutual Authentication | M | Mechanism | chapter prose (boundaries, gateway, identity kws verified) | semantic | scored | Semantic | ASVS v5: ASVS-REQ-V4.1.2, ASVS-REQ-V4.1.3; SP 800-53 r5: SP800-53-IA-2.11, SP800-53-SA-9.3; CAPEC v3.9: CAPEC-384, CAPEC-461; MCP Official 2025: MCP-CONFUSED-DEPUTY; + 2 more sources |
| `ACM-IAT-006` — Structured Logging And Effective Configuration Recording | M | Mechanism | cross-chapter → Ch. 03, Ch. 12, Ch. 14 | semantic | scored | Partial | SP 800-53 r5: SP800-53-AU-2, SP800-53-AU-4.1; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_B, SAMM-ACTIVITY-D_SA_3_B; PCI DSS v4.0.1: PCI-REQ-10, PCI-1.1.1; CIS Controls v8.1.2: CIS-1, CIS-3.1; + 18 more sources |
| `ACO-IAT-001` — Authentication Strength And Identity Assurance | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | ASVS v5: ASVS-REQ-V6.1.1, ASVS-REQ-V6.3.1; PCI DSS v4.0.1: PCI-REQ-4, PCI-REQ-8; SP 800-53 r5: SP800-53-AC-7, SP800-53-AC-7.4; CWE SDV v4.19.1: CWE-290, CWE-305; + 11 more sources |
| `ACO-IAT-002` — Authorization Policy Integrity And Least Privilege | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2; PCI DSS v4.0.1: PCI-REQ-7, PCI-REQ-9; CAPEC v3.9: CAPEC-1, CAPEC-13; CWE SDV v4.19.1: CWE-1220, CWE-183; + 15 more sources |
| `ACO-IAT-003` — Access Revocation And Privilege Lifecycle Integrity | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-2, SP800-53-AC-2.3; CAPEC v3.9: CAPEC-447, CAPEC-675; CIS Controls v8.1.2: CIS-6, CIS-6.2; ASVS v5: ASVS-REQ-V10.4.9; + 3 more sources |
| `ACO-IAT-004` — Session And Token Trust Boundaries | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | ASVS v5: ASVS-REQ-V4.4.3, ASVS-REQ-V4.4.4; CAPEC v3.9: CAPEC-31, CAPEC-39; SP 800-53 r5: SP800-53-IA-13.3, SP800-53-SC-12.5; CWE SDV v4.19.1: CWE-488, CWE-565; + 4 more sources |
| `ACO-IAT-005` — API Caller Trust And Service Boundary Enforcement | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | ASVS v5: ASVS-REQ-V2.2.2, ASVS-REQ-V3.5.1; SP 800-53 r5: SP800-53-SA-8.10, SP800-53-SA-9.3; CAPEC v3.9: CAPEC-461; DSOMM: DSOMM-ACTIVITY-017D9E2642B549A4B9459F59B308FB99 |
| `ACO-IAT-006` — Access Abuse Detection And Auditability | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2.12; PCI DSS v4.0.1: PCI-2.3.2, PCI-8.2.7; CAPEC v3.9: CAPEC-5, CAPEC-54; DSOMM: DSOMM-ACTIVITY-BACF85B65BC0405DB5BAA5D971467CC1, DSOMM-ACTIVITY-0A929C3EAB9A42068761ADF84B74622E; + 16 more sources |
| `ACO-IAT-007` — Identity And Access Control Integrity | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-4.17, SP800-53-AC-17.2; ASVS v5: ASVS-REQ-V6.8.1, ASVS-REQ-V8.4.2; CAPEC v3.9: CAPEC-113, CAPEC-277; MITRE ATLAS: AML.T0021, AML.T0073; + 5 more sources |
| `ACP-IAT-001` — Strong Authentication And Step-Up Enforcement | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-7, SP800-53-AC-7.3; ASVS v5: ASVS-REQ-V6.1.1, ASVS-REQ-V6.1.3; CAPEC v3.9: CAPEC-2, CAPEC-16; CWE SDV v4.19.1: CWE-1392, CWE-290; + 13 more sources |
| `ACP-IAT-002` — Least-Privilege Authorization Governance | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2; CWE SDV v4.19.1: CWE-1220, CWE-183; CIS Controls v8.1.2: CIS-2.2, CIS-2.6; CAPEC v3.9: CAPEC-1, CAPEC-13; + 16 more sources |
| `ACP-IAT-003` — Access Review And Timely Revocation | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2; ASVS v5: ASVS-REQ-V10.4.9, ASVS-REQ-V12.1.4; CIS Controls v8.1.2: CIS-5.5, CIS-6.6; HIPAA: HIPAA-164-308a4, HIPAA-164-312a1; + 1 more sources |
| `ACP-IAT-004` — Bounded Session And Token Management | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | ASVS v5: ASVS-REQ-V4.4.3, ASVS-REQ-V4.4.4; SP 800-53 r5: SP800-53-AC-10, SP800-53-AC-12; CAPEC v3.9: CAPEC-21, CAPEC-39; CWE SDV v4.19.1: CWE-312, CWE-488; + 5 more sources |
| `ACP-IAT-005` — Authenticated API Boundary Enforcement | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | ASVS v5: ASVS-REQ-V1.3.6, ASVS-REQ-V2.2.2; CAPEC v3.9: CAPEC-8, CAPEC-14; SP 800-53 r5: SP800-53-AC-4.7, SP800-53-AC-4.29; MITRE ATLAS: AML.T0040, AML.T0011.000; + 6 more sources |
| `ACP-IAT-006` — Access Abuse Monitoring And Audit Trail | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-2, SP800-53-AC-2.4; PCI DSS v4.0.1: PCI-REQ-11, PCI-1.1.1; CIS Controls v8.1.2: CIS-1, CIS-2.3; SAMM v2.1: SAMM-ACTIVITY-D_SA_1_B, SAMM-ACTIVITY-D_SR_1_B; + 20 more sources |

### Slice `ACO-ITS` — Integration and service-to-service security {#slice-aco-its--integração-e-segurança-service-to-service}

| V1 entity | Type | Manual V2 anchor | Manual section anchor | Authority | Source mode | §26 label | ES grounding |
|---|---|---|---|---|---|---|---|
| `ACM-ITS-001` — API Gateway With Mutual Authentication | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | ASVS v5: ASVS-REQ-V2.2.2, ASVS-REQ-V4.1.2; SP 800-53 r5: SP800-53-CA-3.5, SP800-53-CM-3.5; CAPEC v3.9: CAPEC-14, CAPEC-21; MITRE ATLAS: AML.T0012, AML.T0075; + 12 more sources |
| `ACM-ITS-002` — Trust Boundary Models | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AU-2.3, SP800-53-AU-10.3; SAMM v2.1: SAMM-ACTIVITY-D_SA_3_B, SAMM-ACTIVITY-G_EG_3_A; NIST AI RMF 1.0: NIST-AI-RMF-GOVERN-3, NIST-AI-RMF-MEASURE-4; MITRE ATLAS: AML.T0054; + 3 more sources |
| `ACM-ITS-003` — Transport Security Controls | M | Mechanism | cross-chapter → Ch. 14 | semantic | scored | Partial | SP 800-53 r5: SP800-53-AC-1, SP800-53-AC-2; CIS Controls v8.1.2: CIS-3, CIS-3.1; PCI DSS v4.0.1: PCI-REQ-3, PCI-REQ-7; CWE SDV v4.19.1: CWE-1220, CWE-312; + 14 more sources |
| `ACM-ITS-004` — Message Integrity And Authorized Peer Policies | M | Mechanism | addon/00-catalogo-requisitos.md (mechanism) | semantic | scored | Explicit | SP 800-53 r5: SP800-53-AC-3.12, SP800-53-AC-8; PCI DSS v4.0.1: PCI-1.2.2, PCI-1.2.3; ASVS v5: ASVS-REQ-V2.3.5, ASVS-REQ-V4.1.5; CAPEC v3.9: CAPEC-330, CAPEC-418; + 14 more sources |
| `ACM-ITS-005` — Structured External Call Logging | M | Mechanism | chapter prose (calls, context, logging kws verified) | semantic | scored | Semantic | SP 800-53 r5: SP800-53-AU-2, SP800-53-AU-4; CIS Controls v8.1.2: CIS-8, CIS-8.1; PCI DSS v4.0.1: PCI-REQ-10, PCI-5.3.4; DSOMM: DSOMM-ACTIVITY-4ECED38A79044C45ADB050B663065540, DSOMM-ACTIVITY-FE875E17AE4A45F8A359244AA4FCBC04; + 12 more sources |
| `ACO-ITS-001` — Authenticated Service Interaction And Machine Identity Binding | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-2, SP800-53-AC-4.17; ASVS v5: ASVS-REQ-V6.3.3, ASVS-REQ-V6.6.1; CAPEC v3.9: CAPEC-21, CAPEC-36; CWE SDV v4.19.1: CWE-1392, CWE-289; + 7 more sources |
| `ACO-ITS-002` — Secure Transport And Insecure Protocol Exclusion | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-3.3, SP800-53-AC-3.5; PCI DSS v4.0.1: PCI-REQ-2, PCI-REQ-4; DSOMM: DSOMM-ACTIVITY-72737130472C498480F89AB2F1C2ED5D, DSOMM-ACTIVITY-29318D6018CE452680EAF5928E49F639; ASVS v5: ASVS-REQ-V3.4.1, ASVS-REQ-V12.1.2; + 8 more sources |
| `ACO-ITS-003` — Message Integrity And Authorized Peer Validation | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-3.12, SP800-53-AC-4.19; ASVS v5: ASVS-REQ-V1.5.2, ASVS-REQ-V2.3.5; CAPEC v3.9: CAPEC-12, CAPEC-22; CWE SDV v4.19.1: CWE-179, CWE-209; + 16 more sources |
| `ACO-ITS-004` — Boundary-Mediated External Exposure And Integration Path Control | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-MP-5.1, SP800-53-PE-3; CAPEC v3.9: CAPEC-433; CWE SDV v4.19.1: CWE-73 |
| `ACO-ITS-005` — Integration Security Review And Contract Assurance | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | CIS Controls v8.1.2: CIS-4, CIS-4.1; SP 800-53 r5: SP800-53-CA-3, SP800-53-CA-4; SAMM v2.1: SAMM-ACTIVITY-D_SR_1_B, SAMM-ACTIVITY-D_SR_2_B; HIPAA: HIPAA-164-308a1, HIPAA-164-308b1; + 9 more sources |
| `ACO-ITS-006` — External Interaction Auditability | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AU-2, SP800-53-AU-2.2; ASVS v5: ASVS-REQ-V13.4.5, ASVS-REQ-V16.1.1; DSOMM: DSOMM-ACTIVITY-E9A6D403A467445EB98A74F0C29DA0B1, DSOMM-ACTIVITY-1CD5E4B8BE364726ADC7D8F843F47AC8; PCI DSS v4.0.1: PCI-10.3.3, PCI-10.4.2; + 4 more sources |
| `ACO-ITS-007` — Integration Trust And Service Interaction Assurance | CO | Control / Requirement | intro.md; aplicacao-lifecycle.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-CA-6.1, SP800-53-CA-6.2; ASVS v5: ASVS-REQ-V8.4.2, ASVS-REQ-V12.2.2; CAPEC v3.9: CAPEC-677; NIST AI RMF 1.0: NIST-AI-RMF-MEASURE-4; + 2 more sources |
| `ACP-ITS-001` — Trust Boundary And Integration Review | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SAMM v2.1: SAMM-ACTIVITY-G_EG_2_A, SAMM-ACTIVITY-G_SM_1_A; MITRE ATLAS: AML.T0054; NIST AI RMF 1.0: NIST-AI-RMF-MEASURE-4; SP 800-53 r5: SP800-53-SA-13; + 1 more sources |
| `ACP-ITS-002` — Machine Identity And Mutual Authentication Discipline | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-3.2, SP800-53-AC-17.10; ASVS v5: ASVS-REQ-V6.3.3, ASVS-REQ-V6.5.3; CAPEC v3.9: CAPEC-21, CAPEC-36; MITRE ATLAS: AML.T0012, AML.T0083; + 6 more sources |
| `ACP-ITS-003` — Transport And Protocol Hardening | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-3.5, SP800-53-AC-3.6; PCI DSS v4.0.1: PCI-REQ-2, PCI-1.1.1; CAPEC v3.9: CAPEC-36, CAPEC-57; CIS Controls v8.1.2: CIS-3.1, CIS-4; + 15 more sources |
| `ACP-ITS-004` — Message Integrity And Authorized Peer Validation | P | Practice | addon/00-catalogo-requisitos.md | normative | explicit | Explicit | SP 800-53 r5: SP800-53-AC-4.19, SP800-53-AC-22; ASVS v5: ASVS-REQ-V2.2.2, ASVS-REQ-V2.3.3; CWE SDV v4.19.1: CWE-209, CWE-294; PCI DSS v4.0.1: PCI-1.1.2, PCI-1.2.4; + 10 more sources |
| `ACP-ITS-005` — Integration Contract And Change Assurance | P | Practice | chapter prose (integration, interface, review kws verified) | normative | explicit | Semantic | SP 800-53 r5: SP800-53-CA-3, SP800-53-CM-1; HIPAA: HIPAA-164-308b1, HIPAA-164-314a1; PCI SSLC v1.1: PCISSLC-5.1 |
| `ACP-ITS-006` — External Interaction Audit Logging | P | Practice | chapter prose (calls, context, logging kws verified) | normative | explicit | Semantic | SP 800-53 r5: SP800-53-AC-2.4, SP800-53-AC-3.10; PCI DSS v4.0.1: PCI-REQ-10, PCI-5.3.4; ASVS v5: ASVS-REQ-V13.4.5, ASVS-REQ-V16.1.1; CIS Controls v8.1.2: CIS-3.1, CIS-8; + 16 more sources |

---

## § Manual-only coverage (out-of-Core-scope; ES-grounded direct) {#-manual-only-coverage-out-of-core-scope-es-grounded-direct}

Manual sections covering topics outside the scope of the V1 AppSec Core ontology (maturity models, organisational policies, KPIs/metrics, glossaries) but with direct ES grounding.

| Manual section | Manual V2 anchor | Authority | ES grounding (direct) |
|---|---|---|---|
| `achievable-maturity.md` | MaturityMapping | external | SAMM v2.1 (DM, AA, SR); DSOMM architecture activities |
| `policies-relevantes.md` | PolicyReference | editorial / external | Secure Architecture Policy |
| `addon/07-termos-e-glossario-arquitetura.md` | DocumentUnit | editorial | Glossary and terminology |
| `addon/10-kpis-metricas.md` | ExternalFramework | external | Operational architecture KPIs |

---

## § Out-of-AppSec coverage (pure editorial) {#-out-of-appsec-coverage-pure-editorial}

Manual sections that are pure editorial content (worked examples, narratives, illustrative cases, vendor-specific tooling integration). No ES grounding.

| Manual section | Content type | Manual V2 anchor (if any) |
|---|---|---|
| `aplicacao-lifecycle.md` | Reusable user stories (illustrative narrative) | UserStory |
| `addon/02-casos-praticos.md` | Worked examples of practical cases | DocumentUnit |
| `addon/04-diagramas-referencia.md` | Reference diagrams (illustrative) | DocumentUnit |
| `addon/09-decisao-evidencia-arquitetural.md` | ADR examples and decision narrative | DocumentUnit |

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
