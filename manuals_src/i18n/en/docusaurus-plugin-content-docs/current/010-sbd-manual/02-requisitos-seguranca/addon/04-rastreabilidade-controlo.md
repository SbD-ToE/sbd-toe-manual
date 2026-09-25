---
id: rastreabilidade-controlo
title: Traceability Model between Risks, Requirements and Controls
description: How to build and maintain a traceability matrix that links identified risks, canonical requirements, project operational tags, technical controls and auditable evidence.
tags: [tipo:modelo, tema:rastreabilidade, requisitos, controlos, evidencia, ALM, auditoria]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/02-requisitos-seguranca/addon/04-rastreabilidade-controlo.md
  source_sha256: 6cdbfec253f116a0a61d75685b9fee4539ea5ae03bae3a83b2a2b1e821722ba0
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 408b6ab5ef64c13f3415f46d4c540e13b3bccad9ffc7fe4cbbe7fde1697bc961
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [audit_trail, cycle_iteration, framework_source_corpus, lifecycle_phase, mapping, practitioner_manual, requirement_runtime, risk_level, sbdtoe_sbd, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: 83c24f7fe8fc9e1d2bb12b5778c9840756623e81ad9e0734a6cfadeaff88dbec
  translated_at: 2026-09-25T20:20:08Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Traceability Model between Risks, Requirements and Controls

## Objective {#objetivo}

Throughout the software lifecycle, ensuring that a security requirement has actually been implemented demands more than its definition - it demands that the link between risk, requirement, technical control and evidence be explicit, traceable and auditable.

This model describes how to build that traceability chain, articulating the two identification systems of the SbD-ToE:

- The **canonical ID** (`AUT-001`, `LOG-003`) - stable normative reference originating in the catalogue;
- The **operational tag** (`SEC-L2-AUT-MFA`) - contextualised instance adopted by the project.

The distinction and the relationship between the two are detailed in [Taxonomy and Traceability](./taxonomia-rastreabilidade).

This model supports:

- Systematic verification of security coverage throughout the lifecycle;
- Preparation of internal, external and regulatory audits;
- Integration with ALM tools (Jira, ADO, Confluence, GitHub), risk management and compliance.

---

## Structure of the Traceability Matrix {#estrutura-da-matriz-de-rastreabilidade}

Each row of the matrix represents the direct link between an identified risk and the security requirement that addresses it, with the corresponding control, validation method and expected evidence.

### Recommended columns {#colunas-recomendadas}

| Column | Content | Example |
|--------|----------|---------|
| **Risk** | Identifier and summary description of the risk (originating in the threat analysis) | `RISK-AUTH-01` - unauthorised access due to absence of MFA |
| **Canonical ID** | Normative reference from the SbD-ToE catalogue | `AUT-001` |
| **Operational Tag** | Instantiation of the requirement in the project context | `SEC-L2-AUT-MFA` |
| **Control Type** | Classification of the control: `Preventivo`, `Detetivo` or `Corretivo` | `Preventivo` |
| **Validation** | Objective verification method | Automated test in CI/CD |
| **Evidence** | Auditable artefact produced | Log of authentication failure without MFA |

---

## Example Matrix {#exemplo-de-matriz}

The following is an example of instantiating the requirements catalogue for a concrete project. The full catalogue can be consulted in [Base Requirements List](./lista-requisitos-base).

| Risk | Canonical ID | Operational Tag | Control Type | Validation | Evidence |
|-------|-------------|-----------------|------------------|-----------|-----------|
| Unauthorised access due to absence of a second factor | `AUT-001` | `SEC-L2-AUT-MFA` | Preventive | Functional test - login without MFA fails | Failed authentication log; screenshot |
| Insufficient logging for incident response | `LOG-002` | `SEC-L2-LOG-DETALHE` | Detective | Review of logs at runtime | Sample log with who/when/what/where fields |
| SQL injection due to absence of input validation | `VAL-004` | `SEC-L2-VAL-SQLI` | Preventive | SAST tests + functional test with payload | Scanner report; code with prepared statements |
| Passwords stored in clear text | `AUT-006` | `SEC-L1-AUT-PLAIN` | Preventive | Configuration audit + scan | Evidence of hashing; absence of clear-text credentials |

---

## Examples by Technical Domain {#exemplos-por-domínio-técnico}

| Domain | Canonical ID | Operational Tag (L2 example) | Control Type | Validation | Evidence |
|---------|-------------|------------------------------|------------------|-----------|-----------|
| Authentication | `AUT-005` | `SEC-L2-AUT-IDLE` | Preventive | Idle timeout test | Expired session log; server configuration |
| Access Control | `ACC-002` | `SEC-L2-ACC-LEASTPRIV` | Preventive | Role review + test with restricted user | Permissions matrix; access denied log |
| Logging | `LOG-003` | `SEC-L2-LOG-INTEGRIDADE` | Detective | Attempted log modification; permissions check | Evidence of protection (read-only, remote syslog, WORM) |
| Error Handling | `ERR-001` | `SEC-L1-ERR-EXPOSICAO` | Preventive | Induce an error; check the response to the client | Generic message on the client; stack trace only in the internal log |
| Secure Configuration | `CFG-003` | `SEC-L1-CFG-HARDCODE` | Preventive | Static analysis + repository review | Absence of secrets in the source code; use of a vault |
| Dependencies and SDKs | `API-006` | `SEC-L2-API-SDK` | Preventive/Corrective | SCA scan; SBOM verification | SBOM generated; audited dependency report |
| Sensitive data | `ENC-002` | `SEC-L2-ENC-REST` | Preventive | Review of database and storage configuration | Screenshot of encryption policies; KMS/Vault output |
| Secure communication | `INT-003` | `SEC-L1-INT-TLS` | Preventive | TLS test; certificate scanner | TLS 1.2+ active; valid certificate; `Strict-Transport-Security` |

---

## How to apply this model {#como-aplicar-este-modelo}

- Each row represents the link between an **identified risk** and the **canonical requirement** that addresses it;
- The **operational tag** is the identifier that travels into the backlog, the code and the pipeline - it is what makes the requirement traceable to the lifecycle artefact;
- The **control type** classifies the nature of the measure: `Preventivo` (prevents the incident), `Detetivo` (detects it when it occurs) or `Corretivo` (mitigates the consequences);
- **Validation** must be objective and reproducible - automated test, static analysis, documented manual review;
- **Evidence** is the artefact that proves, in an audit context, that the control is active and effective.

---

## Recommended organisation per project {#organização-recomendada-por-projecto}

Each project must maintain its own traceability matrix, organised by:

1. **Header** - identification of the application, risk level (L1/L2/L3) and review date;
2. **Risk mapping** - originating in the threat analysis (threat modelling);
3. **Traceable table** - with the fields described above;
4. **Cross-reference** to the [Base Requirements Catalogue](./lista-requisitos-base) and the [Validation Plan](./validacao-requisitos);
5. **Pointers to evidence** - directories, commits, screenshots, pipeline reports.

**Suggested formats:**

- `.md` versioned in Git - for native traceability in the repository;
- `.csv` / `.xlsx` - for export and quick analysis;
- Custom fields in Jira, ADO, Confluence or equivalent ALM tools.

---

## Integration into the lifecycle {#integração-no-ciclo-de-vida}

The matrix must be revisited:

- In **requirements reviews** at the start of each cycle;
- During **release gates** and go/no-go processes;
- As support for **formal risk acceptance** and exception documentation;
- At audit checkpoints - ISO 27001, PCI-DSS, DORA, or equivalents.

---

## Supporting tools {#ferramentas-de-suporte}

| Purpose | Suggested tool |
|------------|---------------------|
| Lightweight versioning | Git + Markdown |
| Analysis and filtering | Excel / CSV |
| ALM integration | Jira, Azure DevOps, GitHub Issues |
| Static analysis (SAST) | SonarQube, Semgrep, CodeQL |
| Dynamic testing (DAST) | OWASP ZAP, Burp Suite |
| Dependency analysis (SCA) | Trivy, Snyk, Dependabot |
| Secrets management | HashiCorp Vault, AWS Secrets Manager, Azure Key Vault |
| Log / alert centralisation | SIEM (ELK Stack, Splunk, Microsoft Sentinel) |

---

## Good practices {#boas-práticas}

- Keep **one matrix per application or critical system**, not a single global matrix;
- Use the matrix as an **internal audit trail** - update it at every release;
- **Version every change** to the matrix and to the associated evidence;
- Always reference the **canonical ID** (`AUT-001`) and the **operational tag** (`SEC-L2-AUT-MFA`) - the first for normative traceability, the second for operational traceability;
- Document **exceptions** with justification and formal approval; see [Exception Management](./gestao-excecoes).

---

> For the full list of canonical requirements with acceptance criteria by domain, consult the [Base Requirements Catalogue](./lista-requisitos-base).
> For the recommended validation methods and expected evidence by domain, consult the [Requirements Validation Plan](./validacao-requisitos).
