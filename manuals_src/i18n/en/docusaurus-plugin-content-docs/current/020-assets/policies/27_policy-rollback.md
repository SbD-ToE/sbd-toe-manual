---
id: policy-rollback
title: Rollback Policy
description: Organisational policy that defines the requirements for the rollback capability of deploys in production, including types of rollback by component (binary, configuration, database, infrastructure), activation criteria, RTO by criticality level, periodic testing procedures and traceability, proportional to the criticality level (L1, L2, L3).
tags: [policy, rollback, reversão, deploy, RTO, base de dados, infraestrutura, resiliência, cap11, L1, L2, L3, governance]
grupo: pipeline-entrega
sidebar_position: 27
translation:
  source_locale: pt
  source_path: 020-assets/policies/27_policy-rollback.md
  source_sha256: 50cc18778be19f708ca9c6c7914d00dd00027ccd08d5bb641cc714daa37e31e6
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: f47bd4270e7b03411497d80cc8faeb6f857929fc606277b4a17ad08d677140a0
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bc04ded428e40ee1c214f8535dfb1904655b64166d0aa82b5df521e4230b8cb0
  glossary_keys: [audit_trail, lifecycle_phase, practitioner_manual, requirement_runtime, sbdtoe_sbd, traceability, verification_taxonomy]
  glossary_sha256: 110399c81782b2b857b934c1ae1c80750bfc6edbbd743b4b25bf177ee1e0a7bd
  translated_at: 2026-09-26T14:10:59Z
  reviewed_by: null
---

# Rollback Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for the **rollback capability of deploys in production** - the capability to revert, in a controlled and verifiable manner, a version of software or infrastructure to the previous state in the event of an incident, regression or anomaly detected post-deploy.

Rollback is not a last-resort contingency plan - it is a resilience requirement that must be planned, implemented and tested before it is needed. The difference between a crisis and a controlled resolution often lies in the capability to revert in minutes rather than hours. Without tested rollback, every deploy in production accumulates operational risk that only materialises at the worst possible moment.

The objective of this policy is to ensure that:

- Rollback capability is available before any deploy to production
- The rollback RTO is defined and periodically tested by criticality level
- The different types of rollback (binary, configuration, DB, infrastructure) have specific procedures
- Rollback is executed in a controlled manner and leaves auditable evidence

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

| Level | Applicability |
|---|---|
| L1 | Recommended; documented manual rollback; previous version available |
| L2 | Mandatory; automated rollback for binaries and configuration; tested quarterly |
| L3 | Mandatory; automated rollback for all types; tested quarterly; RTO ≤ 15 minutes |

---

## 3. Types of rollback and specific requirements {#3-tipos-de-rollback-e-requisitos-específicos}

### 3.1 Binary rollback (application/image) {#31-rollback-de-binário-aplicaçãoimagem}

The most frequent and generally the simplest type - reverting to the previous version of the artefact:

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Previous version available in the registry (no immediate expiry) | Mandatory | Mandatory | Mandatory |
| Rollback via pipeline (not manual) | Recommended | Mandatory | Mandatory |
| RTO | No definition | ≤ 30 minutes | ≤ 15 minutes |

### 3.2 Configuration rollback {#32-rollback-de-configuração}

Configuration changes (environment variables, feature flags, service configurations) must be reversible:

- [ ] Configurations versioned (Git, ConfigMap, centralised configuration system)
- [ ] Previous version of the configuration identifiable and applicable without a rebuild
- [ ] Configuration rollback independent of binary rollback (they can be executed separately)
- [ ] Feature flags as a functional rollback mechanism without a new deploy

### 3.3 Database rollback {#33-rollback-de-base-de-dados}

Rollback of database changes is the most complex and the one with the greatest risk of data loss:

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Reversible DB migrations (down migration available) | Recommended | Mandatory | Mandatory |
| Pre-deploy snapshot/backup available | Recommended | Mandatory | Mandatory |
| Consistency verification after DB rollback | Recommended | Mandatory | Mandatory |
| Documented plan for destructive changes (where no down migration is possible) | Recommended | Mandatory | Mandatory |

:::warning
Destructive DB changes (removal of columns, tables, changes of type) are irreversible without data loss. They must be planned in multiple phases: first deprecate/ignore, then remove in a later release. Direct removal without a transition phase precludes rollback without data loss.
:::

### 3.4 Infrastructure rollback (IaC) {#34-rollback-de-infraestrutura-iac}

The reversal of infrastructure changes (IaC) must follow the same approval process as the original apply:

- [ ] Previous IaC state available in the version history
- [ ] Rollback plan generated and reviewed before the reverse apply
- [ ] IaC rollback executed via pipeline, not manually
- [ ] Snapshot of the real pre-change infrastructure state available at L3

---

## 4. Rollback activation criteria {#4-critérios-de-activação-de-rollback}

Rollback must be activated when one of the following criteria is met after the deploy:

| Criterion | Activation threshold |
|---|---|
| HTTP 5xx error rate | > defined threshold (e.g. > 1% for 5 minutes) |
| Response latency (P99) | > defined threshold (e.g. > 2x baseline for 10 minutes) |
| Production health check | Persistent failure in ≥ 2 instances/pods |
| Security alert | Security anomaly detected by runtime monitoring |
| Crash loop | Container in a restart loop after deploy |
| Manual rollback requested | Explicit human decision by the Tech Lead or On-Call |

Thresholds must be documented, versioned and periodically reviewed.

---

## 5. Rollback process {#5-processo-de-rollback}

### 5.1 Automatic rollback {#51-rollback-automático}

At L2/L3, rollback must be started automatically when the activation criteria are reached during a post-deploy observation window:

1. Monitoring system detects a violation of the health criterion
2. Alert generated with identification of the affected deployment
3. Rollback started automatically to the previous version of the binary
4. Confirmation of health status after rollback
5. Notification to the team with details of the reversal

### 5.2 Manual rollback {#52-rollback-manual}

When rollback is started by human decision (outside the automatic window or for types not covered by automatic rollback):

1. Documented decision (who decided, when, on what basis)
2. Target version identified
3. Rollback executed via pipeline (not directly on the platform)
4. Post-rollback health verification
5. Record of the execution with evidence

---

## 6. Rollback RTO by level {#6-rto-de-rollback-por-nível}

| Level | Target RTO (binary rollback) | Target RTO (simple DB rollback) |
|---|---|---|
| L1 | No formal definition | No formal definition |
| L2 | ≤ 30 minutes | ≤ 60 minutes |
| L3 | ≤ 15 minutes | ≤ 30 minutes |

RTO must be measured from the detection of the problem until the service is available on the previous version with verified health status.

---

## 7. Periodic rollback testing {#7-teste-periódico-de-rollback}

Rollback capability must be tested periodically - an untested rollback is a theoretical capability, not an operational one:

| Level | Minimum cadence | Scope of the test |
|---|---|---|
| L1 | Annual | Binary rollback in staging |
| L2 | Quarterly | Binary + configuration rollback in staging |
| L3 | Quarterly | Rollback of all types in staging; RTO measured and documented |

The test results must be documented, including:

- [ ] Actual RTO measured
- [ ] Problems found and corrective actions
- [ ] Comparison with the defined target RTO
- [ ] Approval that the capability is operational

---

## 8. Traceability of rollbacks {#8-rastreabilidade-de-rollbacks}

Each rollback executed in production must produce auditable evidence:

| Artefact | Content |
|---|---|
| Rollback log | Timestamp, source version, target version, trigger, executor |
| Post-rollback health status | Result of the health checks after reversal |
| Decision record | Who decided, when, with what information available |
| Associated incident | Reference to the incident that prompted the rollback |

---

## 9. Responsibilities {#9-responsabilidades}

| Role | Responsibility |
|---|---|
| DevOps / SRE | Configure and maintain automatic rollback capability; run periodic tests; document procedures |
| Developer | Ensure that DB migrations have a down migration; test rollback in staging before deploy to production |
| Tech Lead / On-Call | Take the manual rollback decision when necessary; record the decision |
| AppSec Engineer | Verify that the rollback process does not compromise security controls |
| GRC / Compliance | Audit rollback records; verify that RTOs are met in the tests |

---

## 10. Review and audit of this policy {#10-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Incident in which rollback failed or exceeded the target RTO
- Change of the deploy platform that affects rollback capability
- Architectural change that introduces new types of state (e.g. new database, new messaging system)

---

## 11. Normative and technical references {#11-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 11 - Secure Deployment | US-04 (fast and tested rollback), US-12 (rollback structured by type) |
| Secure Deployment Policy (`25_policy-deploy-seguro.md`) | Progressive deploy strategies and automatic rollback |
| Post-Deployment Monitoring Policy (`28_policy-monitorizacao-pos-deploy.md`) | Rollback activation criteria based on monitoring |
| ISO/IEC 22301 | Business Continuity Management - RTO and RPO |
| NIST SP 800-61 | Computer Security Incident Handling Guide |
| Site Reliability Engineering (Google SRE Book) | Rollback practices and error budget |
