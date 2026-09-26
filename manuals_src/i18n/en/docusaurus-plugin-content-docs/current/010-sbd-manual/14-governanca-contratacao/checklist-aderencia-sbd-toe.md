---
id: checklist-aderencia-sbd-toe
title: SbD-ToE Model Adherence Checklist
sidebar_position: 85
description: Instrument for assessing the adoption of the SbD-ToE model - 96 verification points organised by domain and risk level, derived from the organisational policies. It answers the question "is this team/organisation doing SbD-ToE?" and serves as a tool for self-assessment, internal audit and contractual requirement.
tags: [checklist, aderencia, auditoria, governacao, L1, L2, L3, conformidade]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/checklist-aderencia-sbd-toe.md
  source_sha256: ab7030c658f8017c8f4d0bcbf539ecb174cf97b77e866e7d52ed9c4a7859fc59
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: 66a0bfc4a9bc19dc586acd0f750b56f4fe5931c5056bc4f5e9cb5c6a51181990
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [avaliacao, instrument, programme_line, provenance, requirement_runtime, risk_level, sbdtoe_sbd, segregacao_de_funcoes, slug_threat_modeling, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: 869ac6db14832708406f00b0b42fd8ffeaf3ce2d2a91a2ca1b34a47a963c89e1
  translated_at: 2026-09-26T12:49:09Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# SbD-ToE Model Adherence Checklist

## What this document is for {#para-que-serve-este-documento}

This checklist answers a different question from the KPIs and KRIs:

| Instrument | Question |
|-------------|----------|
| **This checklist** | "Is this team/organisation doing SbD-ToE?" |
| Domain KPIs | "How well is it working?" |
| Executive KRIs | "What risk are we exposed to?" |

The checklist is an **adoption** instrument - it assesses whether the processes, controls and artefacts exist and are being followed. It does not measure the quality of the results - for that, see [`kpis-governanca`](./kpis-governanca) and [`kpis-kri-executivo`](./kpis-kri-executivo).

**Main uses:**
- Team self-assessment before a security review
- Internal audit of compliance with the model
- Contractual requirement for suppliers and third parties
- Onboarding of new teams to the SbD-ToE programme

---

## How to use it {#como-usar}

**Application:** The checklist is applied per application (or per portfolio for an organisational assessment). For each item, the following is recorded:

| Answer | Meaning |
|----------|-------------|
| ✔ | Compliant - evidence available |
| ✗ | Non-compliant |
| ~ | Partially compliant - in progress or with identified gaps |
| N/A | Not applicable to the specific context (requires justification) |

**Risk levels:** The items are marked with the level from which they are mandatory:

| Marking | Mandatory status |
|----------|----------------|
| **S** | Always - regardless of the risk level of the application |
| **L1+** | Mandatory from L1 (low risk) |
| **L2+** | Mandatory from L2 (medium risk) |
| **L3** | Only for L3 applications (high/critical risk) |

The levels are cumulative: L3 includes all L2+ items, which include all L1+ items, which include all S items.

**Recommended assessment cadence:** L1 - annual; L2 - half-yearly; L3 - quarterly.

---

## 1 - Classification and Risk Management {#1---classificação-e-gestão-de-risco}

*Policies: `classificacao-risco`, `aceitacao-risco`, `revisao-periodica-risco`, `gestao-excecoes`*

| # | Item | Level | Policy |
|---|------|:-----:|---------|
| 1.01 | Each application has a formal risk level (L1/L2/L3) assigned, using the three mandatory axes: Exposure, Data, Impact | **S** | pol-02 |
| 1.02 | The classification is formally approved (Tech Lead at minimum) | **L1+** | pol-02 |
| 1.03 | The classification is reassessed when the defined triggers occur: new external integration, new data type, change of exposure, change of architecture, new user profile | **S** | pol-02, pol-04 |
| 1.04 | The classification is reassessed periodically: L1 annual, L2 half-yearly, L3 quarterly | **L1+** | pol-04 |
| 1.05 | For L3, the periodic reassessment requires AppSec + CISO approval | **L3** | pol-02 |
| 1.06 | Exceptions to controls have a defined maximum TTL (L1: 90 days; L2: 60 days; L3: 30 days), technical justification and documented compensating mitigation | **S** | pol-03, pol-05 |
| 1.07 | Exceptions are reassessed before expiry - there are no expired exceptions without renewal or formal closure | **S** | pol-05 |

---

## 2 - Requirements, Threats and Architecture {#2---requisitos-ameaças-e-arquitectura}

*Policies: `requisitos-seguranca`, `threat-modeling`, `arquitetura-segura`, `rastreabilidade`*

| # | Item | Level | Policy |
|---|------|:-----:|---------|
| 2.01 | The security requirements applicable to the application's level are mapped and documented (essential subset at L1; full catalogue at L2/L3) | **L1+** | pol-07 |
| 2.02 | Each requirement has a defined validation criterion | **L2+** | pol-07 |
| 2.03 | Traceability is bidirectional: requirement ↔ control ↔ evidence | **L2+** | pol-06 |
| 2.04 | Pipeline logs and SAST/SCA/DAST reports are retained according to the minimum periods (L2: 90 days; L3: 1 year) | **L2+** | pol-06 |
| 2.05 | Threat modelling has been carried out using STRIDE as the base methodology | **L2+** | pol-08 |
| 2.06 | Threat modelling is reassessed at the defined triggers: new integration, new data type, change of architecture | **L2+** | pol-08 |
| 2.07 | Up-to-date security architecture documentation (solution-architecture.md or equivalent) exists | **L2+** | pol-09 |
| 2.08 | Architecture decisions with a security impact are documented in ADRs with context, alternatives considered and security impact | **L2+** | pol-09 |
| 2.09 | Threat modelling includes LINDDUN for applications that process personal data | **L3** | pol-08 |
| 2.10 | Threat modelling has an independent review (by an entity not involved in the design) | **L3** | pol-08 |
| 2.11 | There is a gate in the CI/CD pipeline that verifies whether the architecture documentation is up to date | **L3** | pol-09 |

---

## 3 - Dependencies and SBOM {#3---dependências-e-sbom}

*Policies: `dependencias`, `sbom`, `excecoes-cve`, `atualizacao-automatica`*

| # | Item | Level | Policy |
|---|------|:-----:|---------|
| 3.01 | A lock file is generated and versioned in the repository | **L1+** | pol-10 |
| 3.02 | SCA is integrated into the pipeline and produces results for every build | **L1+** | pol-17 |
| 3.03 | Critical and high SCA findings block the pipeline | **L2+** | pol-10, pol-17 |
| 3.04 | New dependencies require formal approval with licence validation | **L2+** | pol-10 |
| 3.05 | SBOM is generated automatically per release, includes transitive dependencies and is associated with the artefact with a reference to the commit SHA | **L2+** | pol-11 |
| 3.06 | SBOM is archived for the mandatory minimum period (L2: 1 year; L3: 2 years) | **L2+** | pol-11 |
| 3.07 | CVE exceptions have an explicit type (not affected / fix not available / fix deferred / risk accepted), a compensating control and a TTL according to level | **S** | pol-12 |
| 3.08 | The CVE triage SLA is respected: Critical ≤ 24h, High ≤ 48h | **S** | pol-12 |
| 3.09 | An automatic dependency update process (Renovate, Dependabot or equivalent) is active and configured | **L2+** | pol-13 |
| 3.10 | SBOM is digitally signed, with signature verification at deploy | **L3** | pol-11 |
| 3.11 | Complete provenance is recorded (SLSA attestation or equivalent) | **L3** | pol-11 |
| 3.12 | Medium SCA findings block the pipeline | **L3** | pol-10 |

---

## 4 - Secure Development {#4---desenvolvimento-seguro}

*Policies: `guidelines-desenvolvimento`, `revisao-codigo`, `uso-ferramentas-apoio`*

| # | Item | Level | Policy |
|---|------|:-----:|---------|
| 4.01 | SAST is integrated into the pipeline for all active repositories | **L1+** | pol-19 |
| 4.02 | Secret detection is active in the pipeline and blocks any finding | **S** | pol-17, pol-18 |
| 4.03 | There are no credentials, tokens, keys or passwords hardcoded in code, configuration files or versioned environment variables | **S** | pol-18 |
| 4.04 | Self-approval is blocked by repository configuration (no one approves their own code) | **S** | pol-15 |
| 4.05 | Suppressions of SAST rules (mutes/waives) have formal approval with the finding ID, technical justification, owner and validity period | **S** | pol-14 |
| 4.06 | There is a set of secure development guidelines derived from recognised sources (OWASP, CWE, NIST) and operationalised in linters or SAST rules | **L2+** | pol-14 |
| 4.07 | Code review with an explicit security checklist is mandatory for all code that goes to production | **L2+** | pol-15 |
| 4.08 | Critical and high SAST findings block the merge | **L2+** | pol-15, pol-17 |
| 4.09 | AppSec review is mandatory for authentication, authorisation, sensitive data and security configuration code | **L2+** | pol-15 |
| 4.10 | The use of generative AI tools for code production follows an approved policy, with mandatory human review and no sending of confidential data | **L2+** | pol-16 |
| 4.11 | Guidelines are operationalised as policy-as-code and deviations require AppSec approval | **L3** | pol-14 |

---

## 5 - CI/CD and Pipeline {#5---cicd-e-pipeline}

*Policies: `cicd-seguro`, `gestao-segredos`*

| # | Item | Level | Policy |
|---|------|:-----:|---------|
| 5.01 | The pipeline configuration is versioned as code and subject to code review | **L2+** | pol-17 |
| 5.02 | The security gates are in blocking mode (not just report / continue-on-error) | **L2+** | pol-17 |
| 5.03 | The gate thresholds are documented and versioned (e.g. gates-config.yaml) | **S** | pol-17 |
| 5.04 | The pipeline identity is dedicated, with least privilege - without auto-merge permission | **S** | pol-17 |
| 5.05 | Security gate bypasses have recorded formal approval: owner, technical justification, reference to a ticket/exception, timestamp | **S** | pol-17 |
| 5.06 | Artefacts are associated with the commit SHA that produced them and are reproducible | **S** | pol-17 |
| 5.07 | Pipeline secrets are injected via a centralised vault (Vault, AWS Secrets Manager, Azure Key Vault or equivalent) with access auditing | **L2+** | pol-18 |
| 5.08 | There is segregation of secrets between production and non-production environments | **L2+** | pol-18 |
| 5.09 | The pipeline uses OIDC / workload identity with a short TTL (≤ 1h) instead of long-lived credentials | **L3** | pol-18 |
| 5.10 | Automatic rotation of pipeline credentials is configured | **L3** | pol-18 |
| 5.11 | Artefacts are digitally signed and the signature is verified before deploy | **L3** | pol-17, pol-25 |

---

## 6 - IaC and Containers {#6---iac-e-containers}

*Policies: `iac-seguro`, `aprovacao-plan-iac`, `containers-seguros`, `golden-base-images`*

| # | Item | Level | Policy |
|---|------|:-----:|---------|
| 6.01 | IaC is managed as code: versioned, reviewed and applied via pipeline - never manually in production | **S** | pol-21 |
| 6.02 | The principle of least privilege is applied: no wildcards in IAM policies in production | **S** | pol-21 |
| 6.03 | IaC linting and scanning are integrated into the pipeline, with critical and high findings blocking the apply | **L2+** | pol-21 |
| 6.04 | The IaC apply requires formal approval before execution, recorded with identity and timestamp | **L2+** | pol-22 |
| 6.05 | Container images use bases of verified origin, referenced by digest (never by a mutable tag such as `latest`) | **L2+** | pol-23, pol-24 |
| 6.06 | Images are built with a multi-stage build and run as a non-root user | **L2+** | pol-23 |
| 6.07 | Secrets are not present in ARG or ENV of the Dockerfile, nor in image layers | **S** | pol-23, pol-18 |
| 6.08 | Image vulnerability scanning is integrated into the pipeline with critical and high findings blocking | **L2+** | pol-23 |
| 6.09 | There is a catalogue of golden base images with defined patching SLAs and a deprecation process | **L2+** | pol-24 |
| 6.10 | There is segregation of duties in the IaC apply: author ≠ reviewer ≠ executor | **L3** | pol-22 |
| 6.11 | The admission controller is active in blocking mode (enforce / Deny) - not just audit or warn | **L3** | pol-23 |
| 6.12 | Medium IaC and container findings block the pipeline | **L3** | pol-21, pol-23 |

---

## 7 - Security Testing {#7---testes-de-segurança}

*Policies: `dast-fuzzing`, `estrategia-testes`, `release-seguro`, `aprovacao-release`, `pentesting`*

| # | Item | Level | Policy |
|---|------|:-----:|---------|
| 7.01 | There is a centralised findings management platform (DefectDojo or equivalent) to consolidate SAST, DAST and SCA | **L2+** | pol-19 |
| 7.02 | Finding resolution SLAs are defined by severity and findings are tracked against those SLAs | **L2+** | pol-19 |
| 7.03 | High/Critical severity false positives have technical evidence and AppSec approval before being discarded | **S** | pol-19 |
| 7.04 | DAST is integrated into the staging environment with coverage of the priority endpoints | **L2+** | pol-01, pol-19 |
| 7.05 | There is a pre-release gate that aggregates SAST/DAST/SCA/secret detection with an APPROVED/REJECTED result before any deploy to production | **L2+** | pol-20, pol-26 |
| 7.06 | Open critical or high findings block the release (unless there is an active formal exception) | **L2+** | pol-20 |
| 7.07 | Release approval is formally recorded: who approved, when, reference to the gate report | **L2+** | pol-26 |
| 7.08 | L3 applications have a pentest carried out before first going into production | **L3** | pol-36 |
| 7.09 | L3 applications have an annual pentest with signed formal authorisation (scope, period, rules of engagement) | **L3** | pol-36 |
| 7.10 | Critical pentest findings block going to production and require a mandatory retest after remediation | **L3** | pol-36 |
| 7.11 | DAST covers ≥ 80% of the endpoints in production | **L3** | pol-01 |

---

## 8 - Deployment and Operations {#8---deploy-e-operações}

*Policies: `deploy-seguro`, `rollback`, `monitorizacao-pos-deploy`, `logging-estruturado`, `monitorizacao-seguranca`, `gestao-alertas`, `irp`*

| # | Item | Level | Policy |
|---|------|:-----:|---------|
| 8.01 | Deploys use the artefact produced by the pipeline, never rebuilt (immutable digest) | **S** | pol-25 |
| 8.02 | Production secrets are injected at runtime via a vault (not in static versioned configuration) | **S** | pol-18, pol-25 |
| 8.03 | Rollback activation criteria are defined (error rate, latency, health check failures, security alert) | **S** | pol-27 |
| 8.04 | Emergency deploys (outside the normal process) have post-facto approval recorded in less than 24h | **S** | pol-25, pol-26 |
| 8.05 | There is a rollback strategy that is documented, tested and executable via pipeline (never directly by hand) | **L2+** | pol-27 |
| 8.06 | There is a post-deploy observation period with monitored metrics and formal closure criteria (L2: 30 min; L3: 60 min) | **L2+** | pol-28 |
| 8.07 | Security event logs are in a structured format (JSON) with a mandatory minimum schema (timestamp UTC, level, event.action, application, trace.id) | **L2+** | pol-29 |
| 8.08 | Logs do not contain passwords, full tokens, card data or unmasked PII | **S** | pol-29 |
| 8.09 | Security logs are centralised with a minimum retention of 1 year (L2) / 2 years for security and 3 years for audit (L3/DORA) | **L2+** | pol-29 |
| 8.10 | Critical security events have defined alerts with runbooks (diagnosis, immediate actions, escalation) | **L2+** | pol-30, pol-31 |
| 8.11 | Each alert has a defined response SLA and automatic routing | **L2+** | pol-31 |
| 8.12 | There is an Incident Response Plan with activation criteria, structured phases and playbooks | **L2+** | pol-32 |
| 8.13 | Security incidents have a post-mortem carried out in less than 5 working days | **L2+** | pol-32 |
| 8.14 | Automatic rollback is configured for all artefact types with RTO ≤ 15 minutes | **L3** | pol-27 |
| 8.15 | Regulatory notifications (GDPR ≤ 72h, DORA ≤ 4h initial alert, NIS2 ≤ 24h) are made within the legal deadlines | **L3** | pol-32 |

---

## 9 - Governance and Training {#9---governação-e-formação}

*Policies: `contratacao-segura`, `rastreabilidade-organizacional`, `kpis-governacao`, `formacao-seguranca`*

| # | Item | Level | Policy |
|---|------|:-----:|---------|
| 9.01 | Each application has a formally designated security owner (Security Champion or equivalent) | **L2+** | pol-34 |
| 9.02 | There is a compliance record per application with minimum fields: level, owner, chapters verified, active exceptions, date of last validation and date of the next | **L2+** | pol-34 |
| 9.03 | Deviations identified in the compliance record have corrective action with an owner and a deadline | **S** | pol-35 |
| 9.04 | There is a security training programme with training tracks defined per profile (developer, QA, DevOps, PO, Tech Lead) | **L2+** | pol-37 |
| 9.05 | Onboarding of new people includes security training with a minimum assessment score of 80% | **L2+** | pol-37 |
| 9.06 | There is a set of security KPIs defined with data sources, owners and collection cadence | **L2+** | pol-35 |
| 9.07 | Suppliers and third parties undergo security due diligence before contract (security policy, vulnerability management, incidents in the last 12 months) | **L2+** | pol-33 |
| 9.08 | Contracts with suppliers include SbD-ToE clauses (incident notification, prohibition of subcontracting without approval, termination for non-compliance) | **L2+** | pol-33 |
| 9.09 | Offboarding of suppliers and staff includes revocation of all access in less than 2 hours (immediate in the event of a security incident) | **S** | pol-33 |
| 9.10 | L3 suppliers deliver SBOM per release and periodic security testing reports | **L3** | pol-33 |
| 9.11 | There is a Security Champion with specific training, with active participation in a champions community (monthly meetings) | **L3** | pol-37 |
| 9.12 | Practical security exercises are carried out periodically (labs, CTF or incident tabletop) | **L3** | pol-37 |

---

## Summary and scorecard {#resumo-e-scorecard}

This table serves to calculate adherence per domain after completing the checklist.

| Domain | S items | L1+ items | L2+ items | L3 items | Total |
|---------|:-------:|:---------:|:---------:|:--------:|:-----:|
| 1 - Classification and Risk | 4 | 2 | 0 | 1 | 7 |
| 2 - Requirements and Threats | 0 | 0 | 7 | 3 | 11 |
| 3 - Dependencies and SBOM | 2 | 2 | 5 | 3 | 12 |
| 4 - Secure Development | 5 | 1 | 4 | 1 | 11 |
| 5 - CI/CD and Pipeline | 4 | 0 | 4 | 3 | 11 |
| 6 - IaC and Containers | 3 | 0 | 5 | 3 | 12 |
| 7 - Security Testing | 1 | 0 | 6 | 4 | 11 |
| 8 - Deployment and Operations | 4 | 0 | 8 | 3 | 15 |
| 9 - Governance and Training | 2 | 0 | 7 | 3 | 12 |
| **Total** | **25** | **5** | **46** | **24** | **96** |

### Reading the score {#leitura-do-score}

| Score on S items | Interpretation |
|-----------------|---------------|
| &lt; 70% | The model is not adopted - fundamental controls missing |
| 70% – 89% | Partial adoption - gaps in absolute controls that require priority remediation |
| ≥ 90% | Baseline respected - now assess the items per level |

| Total score per level (S + L1+ + L2+ + L3) | Interpretation |
|--------------------------------------------|---------------|
| ≥ 80% on S + L1+ | Compliant for L1 applications |
| ≥ 80% on S + L1+ + L2+ | Compliant for L2 applications |
| ≥ 80% on all items | Compliant for L3 applications |

**Note:** Items marked S with a ✗ answer cannot be compensated for by the score in other areas - they represent absolute controls that must be resolved regardless of the overall score.

---

## References {#referências}

| Document | Relation |
|-----------|---------|
| [`kpis-governanca`](./kpis-governanca) | Domain KPIs for measuring effectiveness (complement to this checklist) |
| [`kpis-kri-executivo`](./kpis-kri-executivo) | KRIs for CISO/board reporting |
| `020-assets/policies/` | Full text of the 37 policies on which this checklist is based |
| [`addon/12-processo-excecoes`](./addon/processo-excecoes) | Canonical exception management process (items 1.06, 1.07, 3.07, 4.05) |
