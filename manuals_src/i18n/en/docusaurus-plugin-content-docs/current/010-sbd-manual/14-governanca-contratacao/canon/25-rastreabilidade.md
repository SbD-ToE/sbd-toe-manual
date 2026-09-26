---
id: rastreabilidade
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/canon/25-rastreabilidade.md
  source_sha256: 598d1e6a46757caee4fb1b7f7ecfcc6749636db77434eae9b3ab3481a7280843
  source_commit: e341b40c451d9ef4be61e6cd59d994cda54c1aa0
  target_sha256: 28997424a2fc52d898aea34c0fd7b2369e6ffa41867a200be115e996d8f5fcc2
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [alcada, appsec_core, avaliacao, chapter_role, cycle_iteration, maturity, practitioner_manual, risk_level, sbdtoe_sbd, slice, slug_threat_modeling, traceability, validation_evaluation]
  glossary_sha256: b2bdf0bd2dcf1849ee48321b749c0508f0bc7bc577a7f4935dc4f29a1d99a10b
  translated_at: 2026-09-26T13:37:12Z
  reviewed_by: null
---

# 25. Traceability — Governance and Contracting

## Summary {#sumário}

This chapter **is not the primary anchor** of any AppSec Core V1 slice. The external references relevant to this domain are found in the chapters where each slice is primarily anchored.

| Slice | Description | Anchored in |
|---|---|---|
| `ACO-ATB` | Secure architecture and trust boundaries | Ch. 04 (04-arquitetura-segura) |
| `ACO-IAT` | Identity, authentication and session management | Ch. 04 (04-arquitetura-segura) |
| `ACO-ITS` | Integration and service-to-service security | Ch. 04 (04-arquitetura-segura) |
| `ACO-IVF` | Input validation, secure parsing and controlled error handling | Ch. 06 (06-desenvolvimento-seguro) |
| `ACO-RPR` | Release promotion, controlled rollout and rollback readiness | Ch. 11 (11-deploy-seguro) |
| `ACO-SCBI` | Software supply chain and build integrity | Ch. 05 (05-dependencias-sbom-sca) |
| `ACO-SLG` | Security event logging and audit trail | Ch. 12 (12-monitorizacao-operacoes) |
| `ACO-SPC` | Secrets management, protected configuration and operational identities | Ch. 06 (06-desenvolvimento-seguro) |
| `ACO-TMR` | Threat modelling, risk management and mitigation traceability | Ch. 03 (03-threat-modeling) |
| `ACO-TSV` | Security testing and empirical validation | Ch. 10 (10-testes-seguranca) |

---

## § Manual ontology V2 — canonical entities of this chapter {#-manual-ontology-v2--entities-canónicas-deste-capítulo}

Total: **98 entities** of Manual ontology V2 mapped to this chapter via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `GOV-001` | Approved formal security governance model | normative | explicit | deterministic |
| Requirement | `GOV-002` | Security ownership assigned per application or project | normative | explicit | deterministic |
| Requirement | `GOV-003` | Approval authorities defined and known per risk level | normative | explicit | deterministic |
| Requirement | `GOV-004` | Active formal exception management process | normative | explicit | deterministic |
| Requirement | `GOV-005` | Exceptions with validity, monitoring and mandatory revalidation | normative | explicit | deterministic |
| Requirement | `GOV-006` | Risk-proportional security clauses in contracts with third parties | normative | explicit | deterministic |
| Requirement | `GOV-007` | Formal supplier validation before onboarding | normative | explicit | deterministic |
| Requirement | `GOV-008` | Organisational traceability of security decisions per application | normative | explicit | deterministic |
| Requirement | `GOV-009` | Traceable, referenceable and retained evidence of decisions | normative | explicit | deterministic |
| Requirement | `GOV-010` | Continuous validation cycle and periodic compliance review | normative | explicit | deterministic |
| Requirement | `GOV-011` | Governance KPIs defined, collected and reported | normative | explicit | deterministic |
| Requirement | `GOV-012` | Active maturity model with measured and planned evolution | normative | explicit | deterministic |
| Control | `CTRL-governance-governacao-de-fornecedores-e-excecoes-a9a9ab3628` | Governance of suppliers and exceptions | normative | explicit | deterministic |
| Control | `CTRL-identity-gestao-de-identidades-acessos-e-ownership-d0919c69af` | Management of identities, access and ownership | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:ciclo-continuo-de-revisao-e-reavaliacao-de-excecoes` | Continuous cycle of review and reassessment of exceptions | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:clausulas-contratuais-de-seguranca` | Security contractual clauses | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:consolidacao-de-kpis-de-governacao-e-maturidade` | Consolidation of governance and maturity KPIs | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:controlo-sistematico-e-periodico-por-capitulo-sbd-toe` | Systematic and periodic control per SbD-ToE chapter | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:designacao-formal-de-owners-de-seguranca-por-aplicacao` | Formal designation of security owners per application | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:execucao-de-fluxo-formal-de-validacao-de-fornecedores` | Execution of a formal supplier validation flow | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:feedback-pos-projeto-e-rating-de-contractors` | Post-Project Feedback and Contractor Rating | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:formalizacao-de-modelo-de-governacao-por-nivel-de-risco` | Formalisation of the governance model per risk level | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:kpis-de-governacao` | Governance KPIs | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:monitorizacao-continua-de-conformidade-de-fornecedores-alertas-e-escalacao` | Continuous Supplier Compliance Monitoring (Alerts and Escalation) | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:offboarding-seguro-de-contractors-e-rescisao-de-fornecedores` | Secure Contractor Offboarding and Supplier Termination | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:preparacao-tecnica-e-validacao-de-contractors-pre-acesso` | Technical Preparation and Validation of Contractors pre-Access | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:processo-formal-de-excecoes-com-alcadas-por-nivel-de-risco` | Formal exception process with approval authorities per risk level | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:rastreabilidade-organizacional` | Organisational traceability | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:reavaliacao-continua-e-rotacao-de-fornecedores-pos-onboarding` | Continuous reassessment and rotation of suppliers post-onboarding | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:repositorio-de-conformidade-por-aplicacao-controlo-sistematico` | Compliance repository per application (systematic control) | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:revisao-trimestral-de-acesso-de-contractors-least-privilege` | Quarterly Contractor Access Review (Least Privilege) | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:trilho-de-formacao-obrigatoria-pre-acesso-contractors` | Mandatory pre-Access Training Track (Contractors) | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:validacao-continua-de-fornecedores` | Continuous supplier validation | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:validacao-periodica-de-aplicacoes-ciclo-de-conformidade` | Periodic validation of applications (compliance cycle) | normative | explicit | deterministic |
| Threat | `MT-222` | Supplier adoption without assessment | normative | heuristic | bounded |
| Threat | `MT-223` | Lack of contractual clauses | normative | heuristic | bounded |
| Threat | `MT-224` | Use of services without tracking | normative | heuristic | bounded |
| Threat | `MT-225` | Parallel initiatives without coordination | normative | heuristic | bounded |
| Threat | `MT-226` | Lack of organisational continuity | normative | heuristic | bounded |
| Threat | `MT-227` | Risk of legacy decisions without control | normative | heuristic | bounded |
| Threat | `MT-228` | Decisions not reviewed when the context changes | normative | heuristic | bounded |
| Threat | `MT-229` | Lack of governance over historical decisions | normative | heuristic | bounded |
| Threat | `MT-230` | Lack of knowledge of the security state | normative | heuristic | bounded |
| Threat | `MT-231` | Disjointed security strategy | normative | heuristic | bounded |
| Threat | `MT-232` | Security defined but not applied | normative | heuristic | bounded |
| Threat | `MT-233` | Security policies not institutionalised | normative | heuristic | bounded |
| Concept | `sem:concept:ciclo-sbd-toe` | SbD-ToE cycle | semantic | scored | bounded |
| Concept | `sem:concept:clausulas-contratuais-de-sbd-toe` | SbD-ToE contractual clauses | semantic | scored | bounded |
| Concept | `sem:concept:clausulas-contratuais-de-seguranca` | security contractual clauses | semantic | scored | bounded |
| Concept | `sem:concept:excecoes` | exceptions | semantic | scored | bounded |
| Concept | `sem:concept:fluxo-explicito-de-excecoes-e-aceitacao-de-risco` | explicit flow of exceptions and risk acceptance | semantic | scored | bounded |
| Concept | `sem:concept:frameworks-normativos` | Regulatory frameworks | semantic | scored | bounded |
| Concept | `sem:concept:governacao` | governance | semantic | scored | bounded |
| Concept | `sem:concept:governanca-organizacional` | organisational governance | semantic | scored | bounded |
| Concept | `sem:concept:kpis-consolidados` | consolidated KPIs | semantic | scored | bounded |
| Concept | `sem:concept:kpis-de-governacao` | Governance KPIs | semantic | scored | bounded |
| Concept | `sem:concept:modelo-de-governacao-e-autoridade` | governance and authority model | semantic | scored | bounded |
| Concept | `sem:concept:modelo-formal-e-aprovado-de-governacao` | formal and approved governance model | semantic | scored | bounded |
| Concept | `sem:concept:papeis-envolvidos` | roles involved | semantic | scored | bounded |
| Concept | `sem:concept:rastreabilidade-organizacional` | organisational traceability | semantic | scored | bounded |
| Concept | `sem:concept:sbd-toe` | SbD-ToE | semantic | scored | bounded |
| Concept | `sem:concept:validacao-continua-de-terceiros` | continuous validation of third parties | semantic | scored | bounded |
| Mechanism | `sem:mechanism:dashboard-organizacional` | Organisational dashboard | semantic | scored | bounded |
| Mechanism | `sem:mechanism:definicao-e-analise-de-kpis-de-governacao` | definition and analysis of governance KPIs | semantic | scored | bounded |
| Mechanism | `sem:mechanism:documentos-de-governacao-aprovados-pela-direcao` | governance documents approved by management | semantic | scored | bounded |
| Mechanism | `sem:mechanism:ferramenta-de-grc` | GRC tool | semantic | scored | bounded |
| Mechanism | `sem:mechanism:gestao-de-excecoes-e-aceitacao-de-risco` | exception management and risk acceptance | semantic | scored | bounded |
| Mechanism | `sem:mechanism:integracao-de-clausulas-contratuais-de-seguranca` | integration of security contractual clauses | semantic | scored | bounded |
| Mechanism | `sem:mechanism:kpis` | KPIs | semantic | scored | bounded |
| Mechanism | `sem:mechanism:mecanismos-tecnicos-automatizados` | automated technical mechanisms | semantic | scored | bounded |
| Mechanism | `sem:mechanism:rastreabilidade-organizacional` | organisational traceability | semantic | scored | bounded |
| Mechanism | `sem:mechanism:reporting-periodico` | periodic reporting | semantic | scored | bounded |
| Mechanism | `sem:mechanism:validacao-continua-de-fornecedores` | continuous supplier validation | semantic | scored | bounded |
| Pattern | `sem:pattern:delegacao-consciente-e-documentada` | conscious and documented delegation | semantic | scored | bounded |
| Pattern | `sem:pattern:integracao-explicita-de-seguranca-em-fornecedores-e-contratos` | explicit integration of security into suppliers and contracts | semantic | scored | bounded |
| Pattern | `sem:pattern:integracao-juridico-e-procurement` | legal and procurement integration | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:confianca-exclusiva-em-mecanismos-tecnicos-automatizados` | exclusive reliance on automated technical mechanisms | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:limitacao-do-sbd-toe-a-pratica-tecnica-local` | limitation of the SbD-ToE to local technical practice | semantic | scored | bounded |
| Signal | `sem:signal:clausulas-contratuais-rastreadas` | Tracked contractual clauses | semantic | scored | bounded |
| Signal | `sem:signal:excecoes-as-praticas-prescritas` | exceptions to the prescribed practices | semantic | scored | bounded |
| Signal | `sem:signal:excecoes-registadas-e-aprovadas` | Recorded and approved exceptions | semantic | scored | bounded |
| Signal | `sem:signal:kpis-consolidados` | consolidated KPIs | semantic | scored | bounded |
| Signal | `sem:signal:kpis-de-governacao` | Governance KPIs | semantic | scored | bounded |
| Signal | `sem:signal:ligacao-explicita-a-frameworks-normativos` | Explicit linkage to regulatory frameworks | semantic | scored | bounded |
| Signal | `sem:signal:registo-e-aprovacao-de-excecoes` | recording and approval of exceptions | semantic | scored | bounded |
| Signal | `sem:signal:reporting-periodico-a-gestao` | periodic reporting to management | semantic | scored | bounded |
| Signal | `sem:signal:validacao-continua-de-fornecedores` | continuous supplier validation | semantic | scored | bounded |

> Authority class / source mode / confidence model: per Manual ontology V2 definition (`sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml`, `meta.version: '2.0'`).

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
