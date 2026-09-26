---
id: policy-gestao-segredos
title: Secrets Management Policy
description: Organisational policy that defines the requirements for the storage, injection, rotation, audit and revocation of secrets (keys, tokens, credentials, certificates) in applications, CI/CD pipelines, containers and infrastructure, proportional to the criticality level (L1, L2, L3).
tags: [policy, segredos, secrets, vault, OIDC, rotação, pipeline, container, infraestrutura, cap07, cap09, cap11, L1, L2, L3, governance, credenciais]
grupo: pipeline-entrega
sidebar_position: 18
translation:
  source_locale: pt
  source_path: 020-assets/policies/18_policy-gestao-segredos.md
  source_sha256: 39561dd7c3c711181153e283586a598d055762b3b28c9a22ed6282a84364c08f
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 63f66cca76689f34f467f4b6e03a05aec9aa8f478e3c4031c105cd0b84624273
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, framework_source_corpus, gdpr_pseudonymisation, lifecycle_phase, practitioner_manual, requirement_runtime, role_juridico, role_tech_lead, sbdtoe_sbd, traceability]
  glossary_sha256: 077f37bc925ed0aa91cdef68a608b0b398676281e1f550abaa13dcefb6ad59b5
  translated_at: 2026-09-26T14:10:53Z
  stamped_at: 2026-09-26T18:36:54Z
  reviewed_by: null
---

# Secrets Management Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for **managing the complete lifecycle of secrets** - API keys, access tokens, passwords, certificates, database credentials and any other values that, if exposed, allow unauthorised access to systems, data or infrastructure.

Secrets are one of the most frequent and most damaging compromise vectors: exposed in repositories, logs, container images or pipelines, they often persist for months without being rotated, turning a temporary exposure into a permanent risk. Effective secrets management is not merely a matter of technical hygiene - it is a fundamental security control whose failure can compromise the organisation's entire security posture.

The objective of this policy is to ensure that:

- No secret is stored in code repositories, logs, images or build artefacts
- Secrets are managed centrally in secrets vaults with controlled and audited access
- Secrets in pipelines are injected ephemerally, preferably via OIDC/workload identity
- Rotation is automated or scheduled, with TTLs defined by type and criticality level
- Revocation in the event of exposure is immediate and verifiable

---

## 2. Scope {#2-âmbito}

This policy covers all secrets used in the development, pipeline, runtime and infrastructure contexts, regardless of type:

- Access credentials for databases, caches, queues and messaging systems
- API keys for external services
- Access tokens for cloud systems, image registries and artefact repositories
- CI/CD tokens (pipeline tokens, deploy keys)
- TLS/mTLS certificates and their associated private keys
- Encryption keys for data at rest or in transit
- Service account passwords

---

## 3. Absolute prohibitions {#3-proibições-absolutas}

The following practices are **prohibited** regardless of criticality level or context:

| Prohibited practice | Justification |
|---|---|
| Hardcoding secrets in source code | Propagation through version history; impossible to rotate without changing code |
| Secrets in versioned configuration files (e.g. committed `.env`, `application.yml` with passwords) | Exposure to everyone with read access to the repository |
| Secrets in environment variables that are not masked in pipeline logs | Exposure in logs, often stored without adequate access control |
| Secrets embedded in container images | Impossible to rotate without a rebuild; exposure in the image layers |
| Secrets in build artefacts (JARs, wheels, binaries) | Uncontrolled distribution of the secret along with the artefact |
| Use of "global secrets" shared across multiple pipelines or environments | Violation of the principle of least privilege; compromising one pipeline compromises all of them |
| Production secrets accessible in development environments | Unnecessary exposure; risk of leakage through a less controlled environment |

:::warning
Detection of hardcoded secrets in code or configuration must be automated in the pipeline (secret detection). Any finding blocks the merge at L2/L3, regardless of the severity of the other gates.
:::

---

## 4. Centralised storage {#4-armazenamento-centralizado}

All secrets must be stored in a centralised secrets vault, with controlled and audited access:

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Centralised secrets vault in use | Recommended | Mandatory | Mandatory |
| Vault access controlled by RBAC with least privilege | Recommended | Mandatory | Mandatory |
| Vault access audited and log retained | Recommended | Mandatory | Mandatory |
| Production secrets segregated from the other environments | Recommended | Mandatory | Mandatory |
| Vault with high availability and backup | Recommended | Mandatory | Mandatory |

Reference tools: HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager.

---

## 5. Runtime injection {#5-injeção-em-runtime}

Secrets must be injected into applications and pipelines exclusively at execution time - never persisted permanently in the file system or in environment variables:

### 5.1 Applications {#51-aplicações}

- [ ] Secrets injected via environment variable at runtime (not at build time)
- [ ] Environment variables holding secrets not exposed in diagnostic endpoints or health checks
- [ ] Preferred alternative at L2/L3: direct access to the vault via SDK at runtime, using the workload's identity

### 5.2 CI/CD pipelines {#52-pipelines-cicd}

- [ ] Secrets referenced via the CI system's native mechanism (`secrets.*`, `CI/CD Variables masked`, `Variable Groups`)
- [ ] Output of commands that access secrets masked in the logs
- [ ] Cloud credentials via OIDC/workload identity (ephemeral token, TTL ≤ 1h) - eliminates long-lived static keys

### 5.3 Containers {#53-containers}

- [ ] Secrets mounted as orchestrator secret volumes (e.g. Kubernetes Secrets, with encryption at rest)
- [ ] Preferred alternative at L3: access via the vault with workload identity (e.g. Vault Agent, AWS IRSA, GCP Workload Identity)
- [ ] Secrets never passed as a Docker ARG during the build

---

## 6. TTL, rotation and revocation {#6-ttl-rotação-e-revogação}

### 6.1 TTL by secret type {#61-ttl-por-tipo-de-segredo}

| Secret type | Recommended maximum TTL | L3 (mandatory maximum TTL) |
|---|---|---|
| Pipeline tokens (ephemeral OIDC) | ≤ 1 hour | ≤ 1 hour |
| API access tokens (short-lived) | ≤ 24 hours | ≤ 8 hours |
| Database credentials (automatic rotation) | 30 days | 15 days |
| API keys for external services | 90 days | 30 days |
| TLS certificates (application) | 1 year | 90 days |
| Data encryption keys | 1 year (with envelope rotation) | 90 days |

### 6.2 Rotation {#62-rotação}

- [ ] Automated rotation wherever the issuing system supports it (e.g. Vault dynamic secrets, AWS IAM roles, OIDC)
- [ ] Scheduled manual rotation for secrets without automatic rotation support, with alerts before expiry
- [ ] Rotation verifiable without code changes or image rebuilds
- [ ] Auditable rotation history

### 6.3 Revocation on suspected exposure {#63-revogação-por-exposição-suspeita}

When the exposure of a secret is suspected or confirmed:

1. Revoke the secret immediately (do not wait for the TTL)
2. Issue a new secret and distribute it to the systems that depend on it
3. Review the vault access logs to assess misuse during the exposure period
4. Record the incident and notify in accordance with the Traceability Policy and the IRP process

---

## 7. Third-party secrets and integrations {#7-segredos-de-terceiros-e-integrações}

Secrets received from third parties (e.g. supplier API keys) must be:

- [ ] Stored in the centralised vault, not in shared files or ticketing systems
- [ ] With minimum scope and permissions negotiated with the supplier
- [ ] With a known validity period and a renewal alert
- [ ] Revoked immediately when the integration is terminated

---

## 8. Responsibilities {#8-responsabilidades}

| Role | Responsibility |
|---|---|
| Developer | Never hardcode secrets; use approved injection mechanisms; report accidentally exposed secrets |
| DevOps / SRE | Manage the secrets vault; configure rotation; implement OIDC/workload identity; monitor access |
| AppSec Engineer | Define TTLs and the rotation policy; configure secret detection in the pipeline; audit vault access |
| Tech Lead | Ensure the team knows and follows this policy; do not approve PRs with hardcoded secrets |
| GRC / Compliance | Audit compliance; verify that production secrets are segregated; verify access logs |

---

## 9. AI agents as non-human *principals* {#9-agentes-ai-como-principals-não-humanos}

The previous chapter describes secrets for traditional CI identities (*runners*, *workloads*). When an AI agent comes to operate the organisation's pipeline or resources — `Claude Code` executing *tool calls*, `Copilot Workspace` acting on PRs, in-house agents via SDK — that agent is **one more non-human *principal*** subject to the same principles as this policy, with three specialisations.

### 9.1 Dedicated identity per agent and per environment {#91-identidade-dedicada-por-agente-e-por-ambiente}

- Each AI agent has a distinct **ephemeral *workload* identity** (OIDC) — no reuse of human credentials, no reuse across environments (dev / staging / prod) or across agents.
- TTL ≤ 1h (the same rule as for the other *workload identities*).
- The identity is declared in the agent's *mandate* (field `identity_ref` — see [Policy 38 — AI Agent Mandates](./policy-mandates-agentes)).

### 9.2 Per-tool *scoping* {#92-scoping-per-tool}

The agent's identity receives **only the *scopes* needed for the *tools* declared in the `tools_allowlist`** of the *mandate* — not the maximum *scopes* supported by the runtime. Practical examples:

- Agent that opens PRs: `gh:pr:write`, `gh:repo:read`. **Not** `gh:repo:write` or `gh:repo:delete`.
- Agent that applies Kubernetes manifests in *staging*: `k8s:deploy:staging:apply`. **Not** `cluster-admin`.
- Agent that publishes packages: `npm:publish:scoped-package`. **Not** `npm:publish:*`.

Changing the `tools_allowlist` or the *scopes* is a change structurally equivalent to changing an IAM policy — it requires a new *mandate* approval cycle (see Policy 38 §5).

### 9.3 Operational *kill-switch* {#93-kill-switch-operacional}

For agents at level A2+, the **immediate revocation** procedure ([`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) must be exercised periodically:

| Autonomy level | Minimum exercise cadence |
|---|---|
| A2 | Annual (in sandbox/staging) |
| A3 | Quarterly (in sandbox/staging) |
| A4 | Monthly (in sandbox/staging) |

The exercise measures the total time between triggering and effective revocation (OIDC revocation + runtime termination + namespace isolation). The result is recorded; a failed exercise is treated as operational degradation and blocks new activations of A3/A4 agents until it is resolved.

### 9.4 Specific prohibitions {#94-proibições-específicas}

- ❌ **Reusing human credentials** to authenticate the agent — violates the fundamental principle of this policy as applied to AI *principals*.
- ❌ **A *long-lived* token (>1h)** in any AI agent identity — the same rule that applies to CI runners.
- ❌ **A `scope` that exceeds the *mandate*'s `tools_allowlist`** — silent *over-privilege* is an operational incident.
- ❌ **Sharing an identity** between two agents or between an agent and a human — breaks the *audit trail*.
- ❌ **Operating at A3/A4 without a *kill-switch* exercised** within the required cadence — the *kill-switch* is decorative if it has never been measured.

> 📌 Everything else in this policy (absolute prohibitions §3, centralised storage §4, runtime injection §5, TTL/rotation §6) applies without rewording to the case of AI agents.

---

## 10. PII and sensitive data in *prompts* (cross-link GDPR) {#10-pii-e-dados-sensíveis-em-prompts-cross-link-rgpd}

The previous chapters cover classic secrets — *tokens*, keys, credentials. When an AI agent receives user input (chat, *document upload*, *form*), **personal data** enter the *prompt* and, by extension, may travel all the way to the model *provider*. The category of the problem is similar — sensitive information flowing through an uncontrolled channel — but the applicable legal regime is the **GDPR**, not this policy. This section explicitly links the two so that operational coherence is not lost at the boundary.

### 10.1 Minimisation principle {#101-princípio-de-minimização}

- The *prompt* sent to the model must contain **only the personal data strictly necessary** for the task. The GDPR minimisation principle of Art. 5(1)(c) applies directly.
- **Redaction / pseudonymisation before sending** where feasible — replace names, e-mails and IDs with *placeholders* (`<USER_X>`, `<EMAIL_REDACTED>`) and remap them in the output.
- Where redaction is not feasible (e.g. tasks that require the literal content), the decision is recorded and reviewed at the *mandate*'s cadence (Policy 38).

### 10.2 Explicit legal basis {#102-base-legal-explícita}

Each operational use in which the agent sees PII has a **declared GDPR legal basis** — Art. 6 (consent, contract, legal obligation, legitimate interest, etc.) and, for special categories (Art. 9), a reinforced legal basis. The legal basis is part of the agent's *mandate* (Policy 38 — add the field `legal_basis` where applicable) or of the project's processing record, and it is revisited in the periodic reviews.

### 10.3 Sub-processors {#103-sub-processadores}

The model *provider* is a **sub-processor** when it processes personal data on behalf of the organisation (GDPR Art. 28). The contractual clause set out in [Policy 33 §10](./policy-contratacao-segura) applies:

- Sub-processor contract with explicit clauses (retention, *training opt-out*, audit rights).
- Processing location documented; *Standard Contractual Clauses* (SCCs) or another valid mechanism for international transfers (GDPR Arts. 44–49) when the *provider* processes outside the EEA.
- **No PII to *providers* outside the approved list** ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)).

### 10.4 Mandatory *training opt-out* for PII {#104-training-opt-out-obrigatório-para-pii}

When the content of the *prompt* includes personal data, the *provider* is contractually required **not to use that content for future training of the model**. **Zero retention** is preferred for PII; where the *provider* keeps operational logs, retention is minimised and its purpose declared.

### 10.5 Telemetry under the *deployer*'s control {#105-telemetria-sob-controlo-do-deployer}

Inference logs under the organisation's control (AI Act Art. 19 / GDPR Art. 5) comply with [`OPS-003`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes) (retention) and [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) (audit per *tool invocation*) with **redaction of PII in the `args`** — the *audit trail* preserves enough to respond to an audit without replicating the personal data.

### 10.6 Data subject rights {#106-direitos-do-titular-dos-dados}

When the user's interaction with the agent generates personal data, the GDPR rights apply (access Art. 15, rectification Art. 16, erasure Art. 17, objection Art. 21). In particular:

- **Erasure of the *audit events*** under the *deployer*'s control when the data subject exercises the right to be forgotten (subject to competing legal retention obligations).
- **Non-retention by the *provider*** — verified contractually. Where retention by the *provider* exists, the data subject must be able to exercise the right there too.

### 10.7 Proportionality {#107-proporcionalidade}

| Requirement | L1 | L2 | L3 |
|---|:--:|:--:|:--:|
| Minimisation / redaction before sending | Recommended | Mandatory where feasible | Mandatory (special categories always redacted) |
| Declared legal basis | Recommended | Mandatory | Mandatory (GRC review) |
| Sub-processor with Art. 28 clauses | Mandatory (whenever there is PII) | Mandatory | Mandatory + Legal review |
| Contracted *training opt-out* | Mandatory (whenever there is PII) | Mandatory | Mandatory |
| EEA location / SCCs where applicable | Mandatory (when there is PII and processing outside the EEA) | Mandatory | Mandatory (preference for processing in the EEA) |
| Redaction of PII in the `audit events` ([`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012)) | Recommended | Mandatory | Mandatory |
| Procedure for data subject rights | Recommended | Mandatory | Mandatory (incl. erasure under the *deployer*'s control) |

### 10.8 Anti-patterns {#108-anti-padrões}

- ❌ Sending PII to a *provider* outside the approved list — *shadow AI* with GDPR risk.
- ❌ Logging *prompts* with PII without redaction in [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012) — the `audit trail` itself becomes a repository of personal data with no specific legal basis.
- ❌ Trusting that the *provider* "does not use it for training" without a contractual clause — operational statements do not replace Art. 28.
- ❌ Ignoring special categories (GDPR Art. 9) in the prompt — health, biometrics, children's data, etc. require a reinforced legal basis that many chatbot use cases do not satisfy.
- ❌ Treating redaction as sufficient obfuscation — *pseudonymisation* (GDPR) is not anonymisation; pseudonymised PII remains personal data.

### 10.9 Crossover with the GDPR cross-check {#109-cruzamento-com-cross-check-rgpd}

For detailed alignment with the regulation, see the [GDPR cross-check](/sbd-toe/cross-check-normativo/gdpr/intro). This section maintains operational coherence at the AppSec ↔ GDPR boundary; the cross-check deals with the legal obligations in detail.

---

## 11. Review and audit of this policy {#11-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- An incident originating from an exposed or unrotated secret
- Adoption of a new secrets vault or cloud platform
- A change of supplier with an impact on integration keys

---

## 12. Normative and technical references {#12-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 07 - Secure CI/CD | Secrets management and injection in the pipeline; **US-19 — AI agents as principals in the pipeline** |
| SbD-ToE Ch. 09 - Containers and Images | Secrets kept out of images; workload identity |
| SbD-ToE Ch. 11 - Secure Deployment | Secrets in the deploy runtime |
| SbD-ToE Ch. 04 — Secure Architecture ([`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)) | Agent as an isolated *principal*; least privilege per tool |
| Secure CI/CD Policy (`17_policy-cicd-seguro.md`) | Secret detection in the pipeline; log masking |
| Policy 38 — AI Agent Mandates | Operationalises [`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn): mandate, ownership, kill-switch |
| Policy 16 — Use of Support Tools | A2+ operational rules for agents |
| NIST SP 800-207 — Zero Trust Architecture | Principles applied to non-human *principals* (including AI agents) |
| OWASP Secrets Management Cheat Sheet | Reference for good secrets management practices |
| HashiCorp Vault Documentation | Reference vault; dynamic secrets; OIDC |
| NIST SP 800-57 | Key Management Guidelines |
| CIS Benchmark - Secrets Management | Reference controls |
| SSDF PO.5.2 | Implement and maintain secure environments for software development |
