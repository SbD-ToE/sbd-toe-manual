---
id: rastreabilidade
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/canon/25-rastreabilidade.md
  source_sha256: 7176b006cd508f50032480c61e87c7dbd4ed5b20ea8058c26fd718b208b9c076
  source_commit: e341b40c451d9ef4be61e6cd59d994cda54c1aa0
  target_sha256: 3143b703d1eb6871e8f098d8c3a4ead285f80e3093672de181560a359719f180
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [appsec_core, chapter_role, cycle_iteration, deterministic, lifecycle_phase, papel_suporte, practitioner_manual, provenance, sbdtoe_sbd, segregacao_de_funcoes, slice, slug_threat_modeling, traceability, validation_evaluation]
  glossary_sha256: 37dd6ee6315a54efce93ab6b414694d37c8f0af13f087ce74c477c7475e8111d
  translated_at: 2026-09-26T13:39:10Z
  stamped_at: 2026-09-26T18:34:42Z
  reviewed_by: null
---

# 25. Traceability — IaC and Infrastructure

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

Total: **119 entities** of Manual ontology V2 mapped to this chapter via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `IAC-001` | Authenticated remote backend with active locking | normative | explicit | deterministic |
| Requirement | `IAC-002` | Segregated and versioned environments | normative | explicit | deterministic |
| Requirement | `IAC-003` | Mandatory automatic validations in the pipeline | normative | explicit | deterministic |
| Requirement | `IAC-004` | Reused modules with trusted origin and immutable version | normative | explicit | deterministic |
| Requirement | `IAC-005` | Complete history with versioning, tags and releases | normative | explicit | deterministic |
| Requirement | `IAC-006` | Formal naming, tagging and layout conventions | normative | explicit | deterministic |
| Requirement | `IAC-007` | Traceable plan approved before any apply | normative | explicit | deterministic |
| Requirement | `IAC-008` | File → resource → environment traceability | normative | explicit | deterministic |
| Requirement | `IAC-009` | Automatic enforcement of policies in the pipeline | normative | explicit | deterministic |
| Requirement | `IAC-010` | Plan artefacts and manifests versioned and hashed | normative | explicit | deterministic |
| Requirement | `IAC-011` | Secure secrets management - prohibition of hardcoding | normative | explicit | deterministic |
| Requirement | `IAC-012` | Automated detection of drift between IaC and real state | normative | explicit | deterministic |
| Requirement | `IAC-013` | Formal periodic review of modules and templates | normative | explicit | deterministic |
| Control | `CTRL-identity-gestao-de-identidades-acessos-e-ownership-d0919c69af` | Management of identities, access and ownership | normative | explicit | deterministic |
| Control | `CTRL-infrastructure-infraestrutura-como-codigo-governada-5228bca905` | Governed infrastructure as code | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:assinatura-e-proveniencia-de-artefactos-iac` | Signing and Provenance of IaC artefacts | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:backend-remoto-locking-e-rastreabilidade` | Remote backend, locking and traceability | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:detecao-e-correcao-de-drift` | Detection and correction of *drift* | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:determinismo-e-reprodutibilidade-do-plan` | Determinism and reproducibility of the `plan` | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:enforcement-automatico-de-politicas` | Automatic enforcement of policies | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:excecoes-formais-em-iac` | Formal exceptions in IaC | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:gestao-de-segredos-e-identidades-para-iac` | Secrets and identity management for IaC | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:governanca-e-origem-confiavel-de-modulos` | Governance and trusted origin of modules | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:janela-de-mudanca-e-aprovacoes-por-papel` | Change window and approvals by role | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:minimizacao-de-contexto-e-protecao-de-informacao-sensivel-em-iac` | Context minimisation and protection of sensitive information in IaC | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:rastreabilidade-ficheiro-recurso-ambiente` | File → resource → environment traceability | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:rastreabilidade-versionamento-e-naming` | Traceability, versioning and naming | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:revisao-formal-de-plan-antes-de-apply` | Formal review of plan before apply | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:rollback-e-salvaguarda-de-destroy` | *Rollback* and *destroy* safeguard | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:segregacao-de-ambientes-tagging-e-permissoes-minimas` | Segregation of environments, tagging and minimum permissions | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:separacao-de-funcoes-sod-e-controlo-de-execucao-de-apply` | Segregation of duties (SoD) and control of `apply` execution | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:validacoes-automaticas-integradas` | Integrated automatic validations | normative | explicit | deterministic |
| Threat | `MT-132` | Insecure or permissive defaults | normative | heuristic | bounded |
| Threat | `MT-133` | Configurations without validation | normative | heuristic | bounded |
| Threat | `MT-134` | Critical fields left blank or default | normative | heuristic | bounded |
| Threat | `MT-135` | Inconsistent environments between executions | normative | heuristic | bounded |
| Threat | `MT-136` | Use of insecure modules or modules without validation | normative | heuristic | bounded |
| Threat | `MT-137` | Hardcoding of critical parameters | normative | heuristic | bounded |
| Threat | `MT-138` | Insecure environments provisioned by mistake | normative | heuristic | bounded |
| Threat | `MT-139` | Provisioning with excessive permissions | normative | heuristic | bounded |
| Threat | `MT-140` | Lack of data classification tags | normative | heuristic | bounded |
| Threat | `MT-141` | Use of real data in test environments | normative | heuristic | bounded |
| Threat | `MT-142` | Hardcoded or poorly managed secrets | normative | heuristic | bounded |
| Threat | `MT-143` | Changes applied without review | normative | heuristic | bounded |
| Threat | `MT-144` | Lack of owner and accountability | normative | heuristic | bounded |
| Threat | `MT-145` | Reuse of modules without tracking | normative | heuristic | bounded |
| Threat | `MT-146` | Application of insecure changes through bypass | normative | heuristic | bounded |
| Threat | `MT-147` | Informal or non-existent justifications | normative | heuristic | bounded |
| Threat | `MT-148` | Environments provisioned with accumulated exceptions | normative | heuristic | bounded |
| Concept | `sem:concept:catalogo-de-modulos-internos-certificados` | Catalogue of certified internal modules | semantic | scored | bounded |
| Concept | `sem:concept:dashboards-de-validacao-automatizada` | Automated validation dashboards | semantic | scored | bounded |
| Concept | `sem:concept:drift` | drift | semantic | scored | bounded |
| Concept | `sem:concept:drift-detection` | drift detection | semantic | scored | bounded |
| Concept | `sem:concept:enforcement-automatico` | Automatic enforcement | semantic | scored | bounded |
| Concept | `sem:concept:enforcement-de-politicas` | Policy enforcement | semantic | scored | bounded |
| Concept | `sem:concept:ferramentas-de-scanning` | Scanning tools | semantic | scored | bounded |
| Concept | `sem:concept:gestao-centralizada-de-excecoes` | Centralised management of exceptions | semantic | scored | bounded |
| Concept | `sem:concept:infraestrutura-como-codigo-iac` | Infrastructure as Code (IaC) | semantic | scored | bounded |
| Concept | `sem:concept:papel-funcao` | Role/Function | semantic | scored | bounded |
| Concept | `sem:concept:pipelines-ci-cd` | CI/CD Pipelines | semantic | scored | bounded |
| Concept | `sem:concept:rastreabilidade` | Traceability | semantic | scored | bounded |
| Concept | `sem:concept:responsabilidade-partilhada` | Shared responsibility | semantic | scored | bounded |
| Concept | `sem:concept:riscos-em-iac` | Risks in IaC | semantic | scored | bounded |
| Concept | `sem:concept:seguranca-em-iac` | Security in IaC | semantic | scored | bounded |
| Concept | `sem:concept:templates-e-scripts-de-provisionamento` | Provisioning templates and scripts | semantic | scored | bounded |
| Mechanism | `sem:mechanism:auditoria` | Audit | semantic | scored | bounded |
| Mechanism | `sem:mechanism:auditorias-periodicas` | periodic audits | semantic | scored | bounded |
| Mechanism | `sem:mechanism:checkov` | checkov | semantic | scored | bounded |
| Mechanism | `sem:mechanism:ciclo-de-vida` | Lifecycle | semantic | scored | bounded |
| Mechanism | `sem:mechanism:code-review` | code review | semantic | scored | bounded |
| Mechanism | `sem:mechanism:conftest` | Conftest | semantic | scored | bounded |
| Mechanism | `sem:mechanism:detecao-de-mas-praticas-e-permissoes-excessivas` | Detection of bad practices and excessive permissions | semantic | scored | bounded |
| Mechanism | `sem:mechanism:enforcement-automatico-de-politicas` | Automatic enforcement of policies | semantic | scored | bounded |
| Mechanism | `sem:mechanism:kics` | kics | semantic | scored | bounded |
| Mechanism | `sem:mechanism:minimizacao-de-informacao-sensivel` | Minimisation of sensitive information | semantic | scored | bounded |
| Mechanism | `sem:mechanism:opa` | OPA | semantic | scored | bounded |
| Mechanism | `sem:mechanism:pipelines` | Pipelines | semantic | scored | bounded |
| Mechanism | `sem:mechanism:pipelines-ci-cd` | CI/CD Pipelines | semantic | scored | bounded |
| Mechanism | `sem:mechanism:politicas` | Policies | semantic | scored | bounded |
| Mechanism | `sem:mechanism:pull-merge-requests` | pull/merge requests | semantic | scored | bounded |
| Mechanism | `sem:mechanism:requisitos` | Requirements | semantic | scored | bounded |
| Mechanism | `sem:mechanism:scanners-obrigatorios` | Mandatory scanners | semantic | scored | bounded |
| Mechanism | `sem:mechanism:sentinel` | Sentinel | semantic | scored | bounded |
| Mechanism | `sem:mechanism:templates-iac` | IaC Templates | semantic | scored | bounded |
| Mechanism | `sem:mechanism:terrascan` | terrascan | semantic | scored | bounded |
| Mechanism | `sem:mechanism:testes` | Tests | semantic | scored | bounded |
| Mechanism | `sem:mechanism:tfsec` | tfsec | semantic | scored | bounded |
| Mechanism | `sem:mechanism:validacao-e-controlo-de-configuracao` | Configuration validation and control | semantic | scored | bounded |
| Mechanism | `sem:mechanism:versionamento-de-modulos-e-dependencias` | Versioning of modules and dependencies | semantic | scored | bounded |
| Pattern | `sem:pattern:catalogo-de-modulos-certificados-e-versionados` | Catalogue of certified and versioned modules | semantic | scored | bounded |
| Pattern | `sem:pattern:gestao-formal-de-excecoes-com-validade-temporal` | Formal management of exceptions with time-bound validity | semantic | scored | bounded |
| Pattern | `sem:pattern:validacao-automatizada-em-pipelines-ci-cd` | Automated validation in CI/CD pipelines | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:ambientes-mal-segregados` | Poorly segregated environments | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:confianca-na-experiencia-individual-sem-automacao` | Reliance on individual experience without automation | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:erros-de-configuracao` | Configuration errors | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:ignorar-momentos-criticos-no-ciclo-de-vida-do-iac` | Ignoring critical moments in the IaC lifecycle | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:permissoes-excessivas` | Excessive permissions | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:uso-de-modulos-maliciosos` | Use of malicious modules | semantic | scored | bounded |
| Signal | `sem:signal:catalogo-de-modulos-certificados` | Catalogue of certified modules | semantic | scored | bounded |
| Signal | `sem:signal:dashboards-de-validacao` | Validation dashboards | semantic | scored | bounded |
| Signal | `sem:signal:gestao-centralizada-de-excecoes` | Centralised management of exceptions | semantic | scored | bounded |
| Signal | `sem:signal:pipelines-ci-cd-obrigatorios` | Mandatory CI/CD pipelines | semantic | scored | bounded |
| Signal | `sem:signal:uso-de-ferramentas-de-scanning` | Use of scanning tools | semantic | scored | bounded |

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
