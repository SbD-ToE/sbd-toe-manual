---
id: policy-rastreabilidade
title: Traceability and Audit Policy
description: Cross-cutting organisational policy that defines the traceability requirements between requirements, controls, validation evidence, build artefacts and operational events, ensuring that the security posture is auditable continuously and in proportion to the application's risk level.
tags: [policy, rastreabilidade, auditoria, evidências, logs, WORM, commit, pipeline, release, cap02, cap06, cap07, cap08, cap09, cap12, cap14, L1, L2, L3, governance, transversal]
grupo: governacao
sidebar_position: 6
translation:
  source_locale: pt
  source_path: 020-assets/policies/06_policy-rastreabilidade.md
  source_sha256: a16e652a797f1369672ae49cfa8aff310ce99c0bff9a9c067dc7fd222082d81d
  source_commit: be49273442123786a27c269d98751832652acabb
  target_sha256: c6384d929ee0f1ece3e63f9bbcec34e9f9b46ee8d132fa795b1d7c07798c53d5
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, avaliacao, cycle_iteration, lifecycle_phase, mapping, mcp_reading_programa, practitioner_manual, programme_line, provenance, requirement_runtime, risk_level, role_tech_lead, sbdtoe_sbd, traceability, transversal, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 8d8c42644fbae55d04dc05ac622a3177cc6115d2fe7b21d627c95a717739bb92
  translated_at: 2026-09-26T23:27:28Z
  stamped_at: 2026-09-26T23:27:28Z
  reviewed_by: null
---

# Traceability and Audit Policy

## 1. Objective {#1-objetivo}

This policy defines the cross-cutting **traceability and audit** requirements that must be met throughout the entire lifecycle of each application.

Traceability is the ability to reconstruct, at any moment, the chain of decisions, evidence and artefacts that support an application's security posture - from the defined requirements to the code in production, including the validations executed, the exceptions approved and the operational events recorded.

Without effective traceability:

- Security audits become exercises in speculative reconstruction
- Incident investigation loses rigour and reach
- Regulatory compliance cannot be demonstrated objectively
- Risk decisions are left without associated evidence

This policy is **cross-cutting** - it applies to all domains of the SbD-ToE Manual in which evidence, approvals, artefacts or auditable events are produced.

---

## 2. Scope {#2-âmbito}

This policy covers the following dimensions of traceability:

| Dimension | Description | Chapters |
|---|---|---|
| **Requirements** | Traceability between security requirements, backlog work and validation evidence | Ch. 02 |
| **Code and pipeline** | Traceability commit → build → pipeline → release → deploy | Ch. 07 |
| **Artefacts** | Provenance and integrity of build artefacts (SBOM, signatures, SCA) | Ch. 05, 07, 09 |
| **Infrastructure** | Traceability IaC file → resource → environment | Ch. 08 |
| **Validation evidence** | Archive of SAST, DAST, fuzzing and SCA reports and exceptions | Ch. 06, 10 |
| **Operational events** | Structured logs with guaranteed integrity, correlatable with incidents | Ch. 12 |
| **Security decisions** | Approvals, exceptions, risk acceptances, threat modelling results | Ch. 01, 03, 14 |
| **Regulatory compliance** | Mapping between technical controls and normative requirements | Ch. 12, 14 |

---

## 3. Fundamental principles {#3-princípios-fundamentais}

- **Bidirectional traceability** - it must be possible to navigate from the requirement to the code and from the code to the requirement
- **Executable evidence** - reports produced by real execution, never by manual declaration without technical support
- **Immutability** - audit evidence must not be alterable after it is produced; WORM storage recommended at L2/L3
- **Correlation** - events from different sources (commit, pipeline, log, incident) must be correlatable through common identifiers
- **Proportionality** - the level of detail and formality scales with the application's criticality level

---

## 4. Requirements traceability (Ch. 02) {#4-rastreabilidade-de-requisitos-cap-02}

### 4.1 Requirements by level {#41-requisitos-por-nível}

| Practice | L1 | L2 | L3 |
|---|---|---|---|
| Security requirements in the backlog with tags | Recommended | Mandatory | Mandatory |
| Cross-reference requirement → validation | Recommended | Mandatory | Mandatory |
| Exportable traceability report | Optional | Recommended | Mandatory |
| Independent traceability review | Not applicable | Recommended | Mandatory |

### 4.2 Minimum requirements {#42-requisitos-mínimos}

- [ ] All applicable security requirements identified with a traceable taxonomy (e.g. `SEC-L2-AUT-001`)
- [ ] Each requirement linked to at least one backlog item, PR or technical task
- [ ] Validation evidence (test, review, report) associated with each applied requirement
- [ ] Exceptions to requirements formally recorded with a reference to the requirement under exception

---

## 5. Code and pipeline traceability (Ch. 07) {#5-rastreabilidade-de-código-e-pipeline-cap-07}

### 5.1 Mandatory chain {#51-cadeia-obrigatória}

Traceability must cover the complete chain:

```
commit SHA → execução de pipeline → artefacto produzido → release tag → deployment
```

### 5.2 Requirements by level {#52-requisitos-por-nível}

| Element | L1 | L2 | L3 |
|---|---|---|---|
| Commit SHA associated with the artefact | Recommended | Mandatory | Mandatory |
| Pipeline logs retained | Basic | Mandatory (90 days) | Mandatory (1 year) |
| Scanner results correlated with the commit | Optional | Mandatory | Mandatory |
| Immutable export of pipeline logs | Not applicable | Recommended | Mandatory |
| Non-repudiation of irreversible promotions | Not applicable | Recommended | Mandatory |

### 5.3 Minimum requirements {#53-requisitos-mínimos}

- [ ] Unique correlation ID per pipeline execution
- [ ] Security reports (SAST, DAST, SCA) archived as pipeline artefacts with a reference to the commit
- [ ] Pipeline logs retained as per the table above
- [ ] Promotions to production associated with traceable human approval (name, timestamp, context)

---

## 6. Artefact traceability (Ch. 05, 07, 09) {#6-rastreabilidade-de-artefactos-cap-05-07-09}

### 6.1 Requirements by level {#61-requisitos-por-nível}

| Element | L1 | L2 | L3 |
|---|---|---|---|
| SBOM generated per build | Recommended | Mandatory | Mandatory |
| Artefact signing | Not applicable | Mandatory | Mandatory |
| Recorded provenance (who/when/how) | Not applicable | Mandatory | Mandatory |
| Signature verification at deploy | Not applicable | Mandatory | Mandatory |
| Digest-only for container images | Recommended | Mandatory | Mandatory |

### 6.2 Minimum requirements {#62-requisitos-mínimos}

- [ ] SBOM in CycloneDX or SPDX format, generated automatically per build and archived
- [ ] Release artefacts signed with a managed key that is rotated periodically
- [ ] Provenance metadata (who built it, when, from which commit) associated with the artefact

---

## 7. Infrastructure traceability (Ch. 08) {#7-rastreabilidade-de-infraestrutura-cap-08}

### 7.1 Minimum requirements {#71-requisitos-mínimos}

- [ ] Each IaC file traceable to the resource it provisions and to the environment in which it was applied
- [ ] `plan` and `apply` history retained and auditable
- [ ] Infrastructure changes associated with a PR with a documented review
- [ ] Drift detected and recorded with a reference to the expected state

---

## 8. Archive of validation evidence (Ch. 06, 10) {#8-arquivo-de-evidências-de-validação-cap-06-10}

### 8.1 Requirements by level {#81-requisitos-por-nível}

| Evidence | L1 | L2 | L3 |
|---|---|---|---|
| SAST reports archived | Recommended | Mandatory | Mandatory |
| DAST reports archived | Optional | Mandatory | Mandatory |
| SCA reports archived | Recommended | Mandatory | Mandatory |
| Fuzzing reports archived | Optional | Mandatory | Mandatory |
| WORM storage or equivalent | Not applicable | Recommended | Mandatory |
| Evidence index per application/release | Optional | Recommended | Mandatory |

### 8.2 Minimum requirements {#82-requisitos-mínimos}

- [ ] Evidence repository defined, with appropriate access control
- [ ] Automatic export per build/release to the evidence repository
- [ ] Evidence retained in line with the defined retention periods (see section 10)
- [ ] Evidence not alterable after archiving (WORM or equivalent at L2/L3)

---

## 9. Operational event traceability (Ch. 12) {#9-rastreabilidade-de-eventos-operacionais-cap-12}

### 9.1 Minimum requirements {#91-requisitos-mínimos}

- [ ] Logs in a structured format (JSON or equivalent) with minimum fields: timestamp, level, event, origin, context
- [ ] Correlation identifier (`request_id` or equivalent) propagated across all logs of the same flow
- [ ] Logs sent to a centralised system (L2/L3)
- [ ] Access to logs restricted and audited - no direct access by production functions
- [ ] Verifiable log integrity (hash or signature) at L2/L3
- [ ] WORM retention enabled in storage at L3

---

## 10. Minimum retention periods {#10-prazos-de-retenção-mínimos}

| Type of evidence | L1 | L2 | L3 |
|---|---|---|---|
| Application logs | 30 days | 90 days | 1 year |
| CI/CD pipeline logs | 30 days | 90 days | 1 year |
| Security reports (SAST/DAST/SCA) | 30 days | 90 days | 1 year |
| Build artefacts and SBOM | Per release | 1 year | 2 years |
| Records of approvals and exceptions | 1 year | 2 years | 3 years |
| Classification and reassessment records | 2 years | 3 years | 5 years |

:::note
In regulated contexts (DORA, NIS2, healthcare, financial), retention periods may be longer; the GDPR may, conversely, require shorter periods for logs containing personal data. Applicable regulatory requirements always prevail.
:::

---

## 11. Traceability of security decisions {#11-rastreabilidade-de-decisões-de-segurança}

The following decisions must always be recorded with complete traceability:

| Decision | Minimum elements of the record |
|---|---|
| Exception approval | Who approved, when, for which control, with what deadline |
| Residual risk acceptance | Who approved, severity, mitigation, TTL |
| Pipeline gate override | Who authorised, context, timestamp |
| Change of classification level | Who decided, justification, date |
| Release approval | Who approved, checklist executed, open findings |
| Threat modelling result | Threats identified, mitigation or acceptance decisions, approval |

---

## 12. Responsibilities {#12-responsabilidades}

| Role | Responsibility |
|---|---|
| Developer / Tech Lead | Ensure traceability tags in the backlog and PRs; produce validation evidence |
| DevOps / SRE | Configure automatic archiving of artefacts and logs; ensure retention and immutability |
| AppSec Engineer | Verify the completeness of traceability in security reviews and audits |
| GRC / Compliance | Maintain the centralised evidence index; issue compliance reports |
| CISO | Oversee the traceability programme; ensure alignment with regulatory requirements |

---

## 13. Review and audit of this policy {#13-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Incident in which the lack of traceability hindered the investigation
- Regulatory change with an impact on retention periods or evidence requirements
- Significant change to the pipeline or logging architecture

The evidence index and the audit logs must be made available in full in internal and external audits.

---

## 14. Normative and technical references {#14-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 02 - Security Requirements | Traceability requirement → control → validation |
| SbD-ToE Ch. 06 - Secure Development | Central archive of validation evidence |
| SbD-ToE Ch. 07 - Secure CI/CD | Traceability commit → pipeline → release |
| SbD-ToE Ch. 08 - IaC and Infrastructure | Traceability file → resource → environment |
| SbD-ToE Ch. 09 - Containers and Images | Provenance and signing of images |
| SbD-ToE Ch. 12 - Monitoring and Operations | Log integrity and retention |
| SbD-ToE Ch. 14 - Governance and Contracting | Organisational traceability and compliance |
| ISO/IEC 27001 - Clause 9.1 | Monitoring, measurement, analysis and evaluation |
| NIST SP 800-92 | Guide to Computer Security Log Management |
| SSDF PW.8 | Archive and protect each software release |
| NIS2 - Articles 21 and 23 | Risk-management measures and reporting obligations |
| DORA - Article 10 | Traceability of events and logs |
