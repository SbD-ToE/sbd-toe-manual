---
id: rastreabilidade
translation:
  source_locale: pt
  source_path: 010-sbd-manual/02-requisitos-seguranca/canon/25-rastreabilidade.md
  source_sha256: 3e9a4a35906ea9c0f16447f670b7b104d18b4996aeb99ae1ae8fc9c06cab1d27
  source_commit: e341b40c451d9ef4be61e6cd59d994cda54c1aa0
  target_sha256: 6aea1e568d56996a9b70162b76992f3b0100869a672530befd81e308bbc4bb0e
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [appsec_core, capacitacao, chapter_role, esquema_regime, practitioner_manual, requirement_runtime, sbdtoe_sbd, schema, slice, slug_threat_modeling, threat, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: ca13bac80ae8d80cdc0ec48f0418bfcb678511b55fb904f828fb263e68d270b4
  translated_at: 2026-09-26T13:36:56Z
  stamped_at: 2026-09-26T18:33:10Z
  reviewed_by: null
---

# 25. Traceability — Security Requirements

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

Total: **156 entities** of Manual ontology V2 mapped to this chapter via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `ACC-001` | RBAC access control | normative | explicit | deterministic |
| Requirement | `ACC-002` | Principle of least privilege | normative | explicit | deterministic |
| Requirement | `ACC-003` | Blocking and auditing of illegitimate access | normative | explicit | deterministic |
| Requirement | `ACC-004` | Separation of profiles | normative | explicit | deterministic |
| Requirement | `ACC-005` | Access control for APIs and services | normative | explicit | deterministic |
| Requirement | `ACC-006` | Protection of sensitive resources | normative | explicit | deterministic |
| Requirement | `ACC-007` | Validation of the access model | normative | explicit | deterministic |
| Requirement | `ACC-008` | Real-time revocation | normative | explicit | deterministic |
| Requirement | `ACC-009` | Attribute-based authorisation (ABAC) | normative | explicit | deterministic |
| Requirement | `ACC-010` | Periodic review of permissions | normative | explicit | deterministic |
| Requirement | `API-001` | Authentication and authorisation of API calls | normative | explicit | deterministic |
| Requirement | `API-002` | Unnecessary endpoints removed or hidden | normative | explicit | deterministic |
| Requirement | `API-003` | Input validation in APIs | normative | explicit | deterministic |
| Requirement | `API-004` | Rate limiting and abuse detection | normative | explicit | deterministic |
| Requirement | `API-005` | TLS protection and up-to-date certificates | normative | explicit | deterministic |
| Requirement | `API-006` | Verification of the SDKs and wrappers used | normative | explicit | deterministic |
| Requirement | `API-007` | Logging and auditing of external calls | normative | explicit | deterministic |
| Requirement | `AUT-001` | Mandatory MFA | normative | explicit | deterministic |
| Requirement | `AUT-002` | Password policy | normative | explicit | deterministic |
| Requirement | `AUT-003` | Protection against brute force | normative | explicit | deterministic |
| Requirement | `AUT-004` | Active revocation of sessions | normative | explicit | deterministic |
| Requirement | `AUT-005` | Automatic session expiry | normative | explicit | deterministic |
| Requirement | `AUT-006` | Prohibition of credentials in the clear | normative | explicit | deterministic |
| Requirement | `AUT-007` | Support for federated authentication | normative | explicit | deterministic |
| Requirement | `AUT-008` | Step-up for sensitive actions | normative | explicit | deterministic |
| Requirement | `AUT-009` | Re-authentication for critical changes | normative | explicit | deterministic |
| Requirement | `AUT-010` | Alerting on suspicious access | normative | explicit | deterministic |
| Requirement | `CFG-001` | Debug and flags disabled in production | normative | explicit | deterministic |
| Requirement | `CFG-002` | Environment separation with automatic validation | normative | explicit | deterministic |
| Requirement | `CFG-003` | No hardcoded parameters | normative | explicit | deterministic |
| Requirement | `CFG-004` | External configuration with controlled permissions | normative | explicit | deterministic |
| Requirement | `CFG-005` | Configuration validation at start-up | normative | explicit | deterministic |
| Requirement | `CFG-006` | Use of vaults and secure secrets management | normative | explicit | deterministic |
| Requirement | `CFG-007` | Monitoring of configuration drift | normative | explicit | deterministic |
| Requirement | `DST-001` | Authenticated and auditable repositories | normative | explicit | deterministic |
| Requirement | `DST-002` | Approval for public publication | normative | explicit | deterministic |
| Requirement | `DST-003` | Digital signature or checksum | normative | explicit | deterministic |
| Requirement | `DST-004` | Inclusion of SBOM in the artefacts | normative | explicit | deterministic |
| Requirement | `DST-005` | Access segregated by role and environment | normative | explicit | deterministic |
| Requirement | `DST-006` | Deploy only via validated pipeline | normative | explicit | deterministic |
| Requirement | `DST-007` | Revocation and clean-up of compromised artefacts | normative | explicit | deterministic |
| Requirement | `ENC-001` | Encryption of all communications in transit | normative | explicit | deterministic |
| Requirement | `ENC-002` | Encryption of sensitive data at rest | normative | explicit | deterministic |
| Requirement | `ENC-003` | Robust cryptographic algorithms and configurations | normative | explicit | deterministic |
| Requirement | `ENC-004` | Adaptive password hashing | normative | explicit | deterministic |
| Requirement | `ENC-005` | Masking of sensitive data in logs, outputs and API responses | normative | explicit | deterministic |
| Requirement | `ENC-006` | Detection and prevention of secrets exposed in repositories | normative | explicit | deterministic |
| Requirement | `ENC-007` | Periodic rotation of keys and secrets | normative | explicit | deterministic |
| Requirement | `ENC-008` | Prevention of client-side caching of sensitive data | normative | explicit | deterministic |
| Requirement | `ENC-009` | Verifiable integrity of critical data | normative | explicit | deterministic |
| Requirement | `ERR-001` | Errors do not expose sensitive data | normative | explicit | deterministic |
| Requirement | `ERR-002` | Generic messages on the client | normative | explicit | deterministic |
| Requirement | `ERR-003` | Do not reveal the existence of resources | normative | explicit | deterministic |
| Requirement | `ERR-004` | Localised and safe messages | normative | explicit | deterministic |
| Requirement | `ERR-005` | Standardised and centralised handling | normative | explicit | deterministic |
| Requirement | `ERR-006` | Automated tests for excessive errors | normative | explicit | deterministic |
| Requirement | `ERR-007` | Error logs with pseudonymised context | normative | explicit | deterministic |
| Requirement | `IDE-001` | Authorised tools and IDEs | normative | explicit | deterministic |
| Requirement | `IDE-002` | Updating and vulnerability management | normative | explicit | deterministic |
| Requirement | `IDE-003` | Auditing of tool-generated code | normative | explicit | deterministic |
| Requirement | `IDE-004` | Extensions and plugins from trusted sources | normative | explicit | deterministic |
| Requirement | `IDE-005` | Control of extension permissions | normative | explicit | deterministic |
| Requirement | `IDE-006` | Limitation of uncontrolled local environments | normative | explicit | deterministic |
| Requirement | `INT-001` | Validation of messages between systems | normative | explicit | deterministic |
| Requirement | `INT-002` | Mutual authentication or secure tokens | normative | explicit | deterministic |
| Requirement | `INT-003` | Encrypted transmission with TLS | normative | explicit | deterministic |
| Requirement | `INT-004` | Prohibition of insecure protocols | normative | explicit | deterministic |
| Requirement | `INT-005` | Message signing and integrity | normative | explicit | deterministic |
| Requirement | `INT-006` | Cross-validation of origin and destination | normative | explicit | deterministic |
| Requirement | `INT-007` | Monitoring and detection of anomalous patterns | normative | explicit | deterministic |
| Requirement | `INT-008` | Security and contract review in integrations | normative | explicit | deterministic |
| Requirement | `LOG-001` | Recording of critical events | normative | explicit | deterministic |
| Requirement | `LOG-002` | Minimum attributes in logs | normative | explicit | deterministic |
| Requirement | `LOG-003` | Protection of log integrity and access | normative | explicit | deterministic |
| Requirement | `LOG-004` | Periodic log analysis | normative | explicit | deterministic |
| Requirement | `LOG-005` | Minimum log retention | normative | explicit | deterministic |
| Requirement | `LOG-006` | Forwarding to a centralised system | normative | explicit | deterministic |
| Requirement | `LOG-007` | Classification and anomaly detection | normative | explicit | deterministic |
| Requirement | `LOG-008` | Alarm on failures of the logging mechanism | normative | explicit | deterministic |
| Requirement | `LOG-009` | Logs support incident response | normative | explicit | deterministic |
| Requirement | `LOG-010` | Logging of critical business events | normative | explicit | deterministic |
| Requirement | `REQ-001` | Inclusion of security requirements | normative | explicit | deterministic |
| Requirement | `REQ-002` | Formal security review of the requirements | normative | explicit | deterministic |
| Requirement | `REQ-003` | Alignment with risk classification | normative | explicit | deterministic |
| Requirement | `REQ-004` | Versioning and management of requirements | normative | explicit | deterministic |
| Requirement | `REQ-005` | New threat analysis after a requirement change | normative | explicit | deterministic |
| Requirement | `REQ-006` | Traceability requirement → threat → test | normative | explicit | deterministic |
| Requirement | `REQ-007` | Iterative review with teams | normative | explicit | deterministic |
| Requirement | `SES-001` | Automatic expiry on inactivity | normative | explicit | deterministic |
| Requirement | `SES-002` | Manual logout and logout after credential changes | normative | explicit | deterministic |
| Requirement | `SES-003` | Unpredictable session identifiers | normative | explicit | deterministic |
| Requirement | `SES-004` | Secure transmission of tokens | normative | explicit | deterministic |
| Requirement | `SES-005` | Binding of the session to the client context | normative | explicit | deterministic |
| Requirement | `SES-006` | Explicit session revocation | normative | explicit | deterministic |
| Requirement | `SES-007` | Prevention of long-lived sessions | normative | explicit | deterministic |
| Requirement | `SES-008` | Scope, TTL and revocation of JWT tokens | normative | explicit | deterministic |
| Requirement | `VAL-001` | General validation of external inputs | normative | explicit | deterministic |
| Requirement | `VAL-002` | Use of whitelists instead of blacklists | normative | explicit | deterministic |
| Requirement | `VAL-003` | Schema validators (JSON/XML schema) | normative | explicit | deterministic |
| Requirement | `VAL-004` | Sanitisation against injection | normative | explicit | deterministic |
| Requirement | `VAL-005` | Validation before internal use | normative | explicit | deterministic |
| Requirement | `VAL-006` | Safe error messages in validation | normative | explicit | deterministic |
| Requirement | `VAL-007` | Automated tests against malicious inputs | normative | explicit | deterministic |
| Control | `CTRL-code-integrity-desenvolvimento-seguro-e-validacao-de-codigo-63dedd7460` | Secure development and code validation | normative | explicit | deterministic |
| Control | `CTRL-governance-capacitacao-e-onboarding-de-seguranca-f84db7abdf` | Security upskilling and onboarding | normative | explicit | deterministic |
| Control | `CTRL-governance-classificacao-e-governacao-por-risco-97aceecf29` | Risk-based classification and governance | normative | explicit | deterministic |
| Control | `CTRL-infrastructure-infraestrutura-como-codigo-governada-5228bca905` | Governed infrastructure as code | normative | explicit | deterministic |
| Control | `CTRL-supply-chain-inventario-e-analise-de-dependencias-6b0fd9f7fb` | Dependency inventory and analysis | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:catalogo-de-requisitos-do-projeto-criacao-e-manutencao` | Project requirements catalogue (creation and maintenance) | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:definicao-de-criterios-de-validacao` | Definition of validation criteria | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:gates-automaticos-em-ci-cd-para-requisitos-de-seguranca` | Automatic CI/CD gates for security requirements | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:geracao-de-sbom-e-assinatura-de-artefactos-de-build` | SBOM generation and signing of build artefacts | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:gestao-de-excecoes-com-ttl-e-revalidacao-obrigatoria` | Exception Management with TTL and Mandatory Revalidation | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:politica-formacao-e-procedimentos-operacionais` | Policy, Training and Operational Procedures | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:rastreabilidade-de-requisitos` | Requirements traceability | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:revisao-por-alteracao-relevante` | Review upon relevant change | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:selecao-de-requisitos-por-criticidade` | Selection of requirements by criticality | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:validacao-de-cobertura-de-testes` | Validation of test coverage | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:validacao-de-tags-sec-lx-e-requisitos-no-pipeline` | Validation of `SEC-Lx-*` tags and requirements in the pipeline | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:validacao-e-aprovacao-final` | Final validation and approval | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:validacao-por-requisito-dominio-req-xxx-evidencia` | Validation per requirement/domain (REQ-XXX → evidence) | normative | explicit | deterministic |
| Threat | `MT-021` | Absence of security requirements | normative | heuristic | bounded |
| Threat | `MT-022` | Ambiguous or untestable definition | normative | heuristic | bounded |
| Threat | `MT-023` | Generic, non-specific requirements | normative | heuristic | bounded |
| Threat | `MT-024` | Lack of requirements in legacy systems | normative | heuristic | bounded |
| Threat | `MT-025` | Requirements not aligned with risk | normative | heuristic | bounded |
| Threat | `MT-026` | Requirements defined but never verified | normative | heuristic | bounded |
| Threat | `MT-027` | Inconsistent validations across projects | normative | heuristic | bounded |
| Threat | `MT-028` | No tracing between requirement and test | normative | heuristic | bounded |
| Threat | `MT-029` | Requirements not verified in CI/CD | normative | heuristic | bounded |
| Threat | `MT-030` | Risk accepted without documentary validation | normative | heuristic | bounded |
| Threat | `MT-031` | Undocumented exceptions to requirements | normative | heuristic | bounded |
| Threat | `MT-032` | Security omitted for “not being functional” | normative | heuristic | bounded |
| Threat | `MT-033` | Acceptance of exceptions without approval | normative | heuristic | bounded |
| Threat | `MT-034` | Exceptions not re-verified in time | normative | heuristic | bounded |
| Threat | `MT-035` | Not knowing whether requirements were applied | normative | heuristic | bounded |
| Threat | `MT-036` | Requirements applied but not tested | normative | heuristic | bounded |
| Threat | `MT-037` | Requirement changes not propagated | normative | heuristic | bounded |
| Threat | `MT-038` | Ambiguity between requirement and control | normative | heuristic | bounded |

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
