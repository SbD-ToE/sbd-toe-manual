---
id: rastreabilidade
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/canon/25-rastreabilidade.md
  source_sha256: 8eef1b2663776e072ed6508a801499302df9a1b804d894a0b26912d46a9da1b8
  source_commit: e341b40c451d9ef4be61e6cd59d994cda54c1aa0
  target_sha256: 6597a3f0c89fa74e19d0f77300818f5cb675ed2635d9af78f2220f93b05c6429
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [appsec_core, audit_trail, chapter_role, deterministic, framework_source_corpus, practitioner_manual, provenance, sbdtoe_sbd, slice, slug_threat_modeling, traceability, validation_evaluation]
  glossary_sha256: d1fbe3d3f4ce30693e0f2a49efc5b78648828f7f406cf21d867314a332ad9028
  translated_at: 2026-09-26T13:37:03Z
  stamped_at: 2026-09-26T18:34:28Z
  reviewed_by: null
---

# 25. Traceability — Secure CI/CD

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

Total: **121 entities** of Manual ontology V2 mapped to this chapter via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `CIC-001` | Pipelines as code, versioned and subject to review | normative | explicit | deterministic |
| Requirement | `CIC-002` | Triggers controlled and restricted to authorised sources | normative | explicit | deterministic |
| Requirement | `CIC-003` | Secure management of secrets in the pipeline | normative | explicit | deterministic |
| Requirement | `CIC-004` | Mandatory security gates before promotion between environments | normative | explicit | deterministic |
| Requirement | `CIC-005` | Complete traceability of each pipeline execution | normative | explicit | deterministic |
| Requirement | `CIC-006` | Isolation of runners and execution environments | normative | explicit | deterministic |
| Requirement | `CIC-007` | Verifiable integrity and provenance of the artefacts produced | normative | explicit | deterministic |
| Requirement | `CIC-008` | Separation of responsibilities between build, test and deploy | normative | explicit | deterministic |
| Requirement | `CIC-009` | Pipeline credentials with minimum scope and defined rotation | normative | explicit | deterministic |
| Requirement | `CIC-010` | Protection against execution of unauthorised code on runners | normative | explicit | deterministic |
| Control | `CTRL-code-integrity-integridade-e-governacao-de-pipelines-d5b14eeef2` | Integrity and governance of pipelines | normative | explicit | deterministic |
| Control | `CTRL-secrets-gestao-de-segredos-e-identidades-operacionais-e2c86cdfe9` | Management of secrets and operational identities | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:assinatura-e-proveniencia` | Signing and provenance | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:cobertura-ampliada-containers-e-sbom` | Extended coverage (containers and SBOM) | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:contencao-de-contexto-e-higiene-de-logs-outputs` | Context containment and hygiene of logs/outputs | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:design-seguro-dos-pipelines-versionamento-determinismo-e-revisao` | Secure design of pipelines (versioning, determinism and review) | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:evidencia-empirica-obrigatoria-anti-relatorios-sem-execucao` | Mandatory empirical evidence (anti-“reports without execution”) | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:gates-por-risco-separacao-sinal-decisao` | Gates by risk (signal/decision separation) | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:gestao-de-excecoes-bypass-controlado` | Exception management (controlled bypass) | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:gestao-de-segredos` | Secrets management | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:gestao-segura-de-codigo-fonte` | Secure source code management | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:isolamento-de-runners` | Runner isolation | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:metricas-e-conformidade-organizacional` | Metrics and organisational compliance | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:nao-repudio-e-ownership-de-promocoes-acoes-irreversiveis` | Non-repudiation and ownership of promotions (irreversible actions) | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:rastreabilidade-ponta-a-ponta-commitpipelinerelease` | End-to-end traceability (commit→pipeline→release) | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:reprodutibilidade-e-determinismo-do-pipeline` | Reproducibility and determinism of the pipeline | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:scanners-integrados-validacao-empirica-obrigatoria` | Integrated scanners (mandatory empirical validation) | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:separacao-formal-entre-sinal-automatico-e-decisao-de-promocao` | Formal separation between automatic signal and promotion decision | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:testes-de-seguranca-dinamicos-dast` | Dynamic security testing (DAST) | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:validacao-de-integridade-de-imagens-base` | Validation of base image integrity | normative | explicit | deterministic |
| Threat | `MT-111` | Execution of unauthorised code in the pipeline | normative | heuristic | bounded |
| Threat | `MT-112` | Compromise of the build environment | normative | heuristic | bounded |
| Threat | `MT-113` | Privilege escalation in the pipeline | normative | heuristic | bounded |
| Threat | `MT-114` | Unauthorised push to protected branches | normative | heuristic | bounded |
| Threat | `MT-115` | Execution of unaudited code | normative | heuristic | bounded |
| Threat | `MT-116` | Silent replacement of legitimate code | normative | heuristic | bounded |
| Threat | `MT-117` | Build forged outside the pipeline | normative | heuristic | bounded |
| Threat | `MT-118` | Injection of dynamic logic into the pipeline | normative | heuristic | bounded |
| Threat | `MT-119` | Use of insecure external components | normative | heuristic | bounded |
| Threat | `MT-120` | Leakage of secrets via logs | normative | heuristic | bounded |
| Threat | `MT-121` | Hardcoded secrets | normative | heuristic | bounded |
| Threat | `MT-122` | Reuse of secrets | normative | heuristic | bounded |
| Threat | `MT-123` | Absence of security gates | normative | heuristic | bounded |
| Threat | `MT-124` | Validations not executed | normative | heuristic | bounded |
| Threat | `MT-125` | Lack of traceability | normative | heuristic | bounded |
| Threat | `MT-126` | Bypass of controls without a trace | normative | heuristic | bounded |
| Threat | `MT-127` | Critical changes without visibility | normative | heuristic | bounded |
| Threat | `MT-128` | Promotions without a human owner | normative | heuristic | bounded |
| Threat | `MT-129` | Plausible evidence without execution | normative | heuristic | bounded |
| Threat | `MT-130` | Non-determinism of the pipeline | normative | heuristic | bounded |
| Threat | `MT-131` | Exfiltration of sensitive context | normative | heuristic | bounded |
| Concept | `sem:concept:ambientes-de-execucao` | Execution environments | semantic | scored | bounded |
| Concept | `sem:concept:appsec` | AppSec | semantic | scored | bounded |
| Concept | `sem:concept:artefact-protection` | Artefact Protection | semantic | scored | bounded |
| Concept | `sem:concept:assinatura-e-proveniencia-de-artefactos` | Artefact signing and provenance | semantic | scored | bounded |
| Concept | `sem:concept:auditorias-regulares` | Regular audits | semantic | scored | bounded |
| Concept | `sem:concept:ci-cd-seguro` | Secure CI/CD | semantic | scored | bounded |
| Concept | `sem:concept:dependencia-externa` | External dependency | semantic | scored | bounded |
| Concept | `sem:concept:dev-team` | Dev Team | semantic | scored | bounded |
| Concept | `sem:concept:devops` | DevOps | semantic | scored | bounded |
| Concept | `sem:concept:gates-de-promocao` | promotion gates | semantic | scored | bounded |
| Concept | `sem:concept:gestao-de-segredos` | Secrets management | semantic | scored | bounded |
| Concept | `sem:concept:grc-auditoria` | GRC/Audit | semantic | scored | bounded |
| Concept | `sem:concept:mvp` | MVP | semantic | scored | bounded |
| Concept | `sem:concept:oidc` | OIDC | semantic | scored | bounded |
| Concept | `sem:concept:organizational-trust` | Organisational Trust | semantic | scored | bounded |
| Concept | `sem:concept:pipeline` | Pipeline | semantic | scored | bounded |
| Concept | `sem:concept:proveniencia` | provenance | semantic | scored | bounded |
| Concept | `sem:concept:rastreabilidade-ponta-a-ponta` | End-to-end traceability | semantic | scored | bounded |
| Concept | `sem:concept:reprodutibilidade-e-determinismo-operacional` | Reproducibility and operational determinism | semantic | scored | bounded |
| Concept | `sem:concept:runners` | runners | semantic | scored | bounded |
| Concept | `sem:concept:runners-ephemerais` | Ephemeral runners | semantic | scored | bounded |
| Concept | `sem:concept:runners-tooling-gates-segredos` | Runners, tooling, gates, secrets | semantic | scored | bounded |
| Concept | `sem:concept:scanners-de-seguranca` | Security scanners | semantic | scored | bounded |
| Concept | `sem:concept:secure-release` | Secure Release | semantic | scored | bounded |
| Concept | `sem:concept:slsa` | SLSA | semantic | scored | bounded |
| Concept | `sem:concept:supply-chain-attack` | Supply Chain Attack | semantic | scored | bounded |
| Mechanism | `sem:mechanism:assinatura-de-artefactos` | Artefact signing | semantic | scored | bounded |
| Mechanism | `sem:mechanism:auditorias-regulares` | Regular audits | semantic | scored | bounded |
| Mechanism | `sem:mechanism:configuracao-de-oidc-e-ttl-curto-para-segredos` | Configuration of OIDC and short TTL for secrets | semantic | scored | bounded |
| Mechanism | `sem:mechanism:controlo-de-logging-e-debug-com-ativacao-temporaria-e-auditavel` | Control of logging and debug with temporary and auditable activation | semantic | scored | bounded |
| Mechanism | `sem:mechanism:gestao-de-segredos` | Secrets management | semantic | scored | bounded |
| Mechanism | `sem:mechanism:integracao-de-ferramentas-como-semgrep-trivy-cosign-scorecard-e-scanners-de-iac-containers` | Integration of tools such as semgrep, trivy, cosign, scorecard and IaC/container scanners | semantic | scored | bounded |
| Mechanism | `sem:mechanism:integracao-de-scanners-servicos-repositorios-registries` | Integration of scanners, services, repositories, registries | semantic | scored | bounded |
| Mechanism | `sem:mechanism:logs-mascarados` | masked logs | semantic | scored | bounded |
| Mechanism | `sem:mechanism:oidc` | OIDC | semantic | scored | bounded |
| Mechanism | `sem:mechanism:politicas-de-gates` | Gate policies | semantic | scored | bounded |
| Mechanism | `sem:mechanism:promocao-de-releases` | Release promotion | semantic | scored | bounded |
| Mechanism | `sem:mechanism:registo-de-configuracao-efetiva` | Recording of effective configuration | semantic | scored | bounded |
| Mechanism | `sem:mechanism:retencao-estruturada-de-logs-metadados-e-correlacoes-commit-pipeline-release` | Structured retention of logs, metadata and commit→pipeline→release correlations | semantic | scored | bounded |
| Mechanism | `sem:mechanism:runners-e-agentes` | Runners and agents | semantic | scored | bounded |
| Mechanism | `sem:mechanism:scanners-automaticos` | automatic scanners | semantic | scored | bounded |
| Mechanism | `sem:mechanism:scanners-de-seguranca-integrados` | Integrated security scanners | semantic | scored | bounded |
| Mechanism | `sem:mechanism:tokens-de-curta-duracao` | short-lived tokens | semantic | scored | bounded |
| Mechanism | `sem:mechanism:uso-de-runners-ephemerais-nao-privilegiados-e-segregados` | Use of ephemeral, unprivileged and segregated runners | semantic | scored | bounded |
| Mechanism | `sem:mechanism:versionamento-de-pipelines` | Versioning of pipelines | semantic | scored | bounded |
| Pattern | `sem:pattern:registro-formal-de-excecoes` | formal record of exceptions | semantic | scored | bounded |
| Pattern | `sem:pattern:separacao-entre-sinal-automatico-e-decisao-de-promocao` | separation between automatic signal and promotion decision | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:exposicao-excessiva-de-contexto-em-logs-e-artefactos` | excessive exposure of context in logs and artefacts | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:uso-de-segredos-estaticos` | use of static secrets | semantic | scored | bounded |
| Signal | `sem:signal:sinal-automatico` | automatic signal | semantic | scored | bounded |

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
