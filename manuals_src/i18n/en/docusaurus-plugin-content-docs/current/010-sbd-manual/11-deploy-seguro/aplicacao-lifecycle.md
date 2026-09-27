---
id: aplicacao-lifecycle
title: How to Do It
description: Practical integration of secure release and deployment practices into the software lifecycle
tags: [tipo:aplicacao, ciclo-vida, deploy, release, rollback, gates, producao]
genia: us-format-normalization
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/aplicacao-lifecycle.md
  source_sha256: a700cb969f0276173ea35e8f6d8ae58dd99dd53e30ee8a274ca44acef1660527
  source_commit: 5e4b3eab6144ef4347232513856d6d9cb86a487c
  target_sha256: 604643eff7eb18909239ded16c0b55c236d7358ef72d5a42047937dea9223253
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [audit_trail, avaliacao, chapter_role, como_fazer, cycle_iteration, eu_startups, lifecycle_phase, papel_suporte, practitioner_manual, provenance, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 9e6c5264e0dcf80bffbf109b706282f8a82f7579508ae44459a982778bc99a09
  translated_at: 2026-09-27T15:08:15Z
  stamped_at: 2026-09-27T15:08:15Z
  reviewed_by: null
---

# Applying Secure Deployment Throughout the Lifecycle

## 🧭 When to apply {#-quando-aplicar}

A secure *deployment* does not happen all at once: it is the culmination of several critical stages, from building the artefact to the post-*release* audit.  
Each phase has specific risks and therefore requires its own controls and clear evidence.

The following table shows where each practice must be applied and how to prove its execution:

| SDLC Phase / Event | Action | Evidence |
|--------------------|------|-----------|
| Build | Ensure a signed and versioned artefact | Signature + SBOM |
| Pre-release | Validation in *staging* + *gates* | Validation reports |
| Deploy | Pipeline execution with *rollback* prepared | Deployment logs |
| Post-release | Health and integrity monitoring | Metrics + alerts |
| Audit | *End-to-end* traceability review | Audit reports |

---

## 👥 Who carries out each action {#-quem-executa-cada-ação}

Responsibility for a secure *deployment* is necessarily shared.  
There is no “single owner”: each role contributes a part of the integrity assurance.  
The following table clarifies this division:

| Role | Responsibility |
|-------|------------------|
| **Developer** | Produce artefacts ready to *deploy* |
| **QA** | Validate *staging*, acceptance criteria |
| **AppSec Engineer** | Approve *gates* and manage exceptions |
| **DevOps / SRE** | Run pipelines, *rollback* and monitoring |
| **Product Owner** | Decide *go/no-go*, accept residual risk |

---

## 📖 Reusable User Stories {#-user-stories-reutilizáveis}

The following stories describe typical risk scenarios in *deployment* and how they must be handled consistently.  
By formalising them in the *backlog*, the organisation is able to align roles, practices and evidence in an auditable way.

---

### US-01 - Deployment of signed artefacts only {#us-01---deploy-apenas-de-artefactos-assinados}

Integrity begins with provenance: if the origin is not controlled, the whole process becomes vulnerable.

**Context.** *Deployments* of untrusted artefacts compromise the whole system.

:::userstory
**Story.**  
As a **DevOps/SRE**, I want **to *deploy* only signed and versioned artefacts**, so that **integrity and traceability are assured**.

**Acceptance criteria (BDD).**  
- **Given** a *deployment* pipeline  
  **When** an artefact is not signed  
  **Then** the *deployment* is blocked

**Checklist.**  
- [ ] Signature validated (e.g. cosign / in-toto)  
- [ ] SBOM attached to the artefact  
- [ ] Provenance verified  
:::

**Artefacts & evidence.** Signed artefact + SBOM.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Mandatory (verified signature or *hash*) + automatic rejection | Mandatory + automatic rejection | Mandatory + automatic rejection |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Build/Release | Artefact production | DevOps/SRE | Every release |

**Useful links.** [Secure CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro) ; [Secure Deployment](/sbd-toe/sbd-manual/deploy-seguro/intro)

> **Common pattern:** signing and provenance verification occur in multiple contexts (CI/CD, IaC, *container* images, *deployment*).  
> This US focuses on the validation context at *deployment* time, where artefacts are verified before being promoted; see also the equivalent US in chapters 07, 08 and 09 (same principle: *sign → validate → use*).

---

### US-02 - Validation in *staging* before promotion {#us-02---validação-em-staging-antes-da-promoção}

*Staging* is the “dress rehearsal”: without it, production becomes a testing ground.

**Context.** Promoting directly to production increases the risk of incidents.

:::userstory
**Story.**  
As a **QA** role, I want **to validate *releases* in *staging* with a segregated environment, controlled data and functional + security tests**, so that **the *readiness* of the release is ensured without exposing real data**.

**Acceptance criteria (BDD).**  
- **Given** a *staging* environment equivalent to production (same versions and configuration)  
  **When** I run validations (functional + DAST + SBOM verification)  
  **Then** only *releases* approved by QA and AppSec proceed to production

- **Given** that *staging* is used to validate *releases*  
  **When** I prepare the environment and the data  
  **Then** only fictitious/masked data are used (never real data)

- **Given** that the *staging* environment contains test data and credentials  
  **When** I grant access  
  **Then** access is segregated (MFA + RBAC) and auditable

**Checklist.**  
- [ ] *Staging* environment with infrastructure equivalent to production  
- [ ] Test data (no real data; masked/fictitious)  
- [ ] Functional and regression tests executed  
- [ ] Authenticated DAST completed  
- [ ] SBOM validated (no malicious / non-compliant dependencies)  
- [ ] Segregated access (MFA, role-based permissions)  
- [ ] Validation report attached to the *release*  
- [ ] Formal approval recorded (QA + AppSec)
:::

**Artefacts & evidence.** *Staging* reports.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Optional | Mandatory | Mandatory |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Pre-release | Preparation for production | QA/Testing | Every release |

**Useful links.** [Security Testing](/sbd-toe/sbd-manual/testes-seguranca/intro)

---

### US-03 - Approval *gates* in *deployment* {#us-03---gates-de-aprovação-no-deploy}

Without *gates*, promotion to production becomes a gamble - and security cannot be a game of chance.

**Context.** *Releases* without *gates* can promote insecure code.

:::userstory
**Story.**  
As an **AppSec Engineer**, I want **to define automatic *gates* and *thresholds* in *deployment***, so that **insecure *releases* are blocked**.

**Acceptance criteria (BDD).**  
- **Given** a candidate *release*  
  **When** there are unresolved critical *findings*  
  **Then** the *deployment* is blocked until a formal decision (fix or approved exception)

**Checklist.**  
- [ ] Automatic *gates* configured  
- [ ] *Thresholds* documented  
- [ ] Exceptions recorded and approved
:::

**Artefacts & evidence.** Pipeline configuration + exception register.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Block on Critical | Blocking on High/Critical | Blocking on Medium+ |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Release | Promotion to production | AppSec + DevOps | Every release |

**Useful links.** [Secure CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro) ; [Security Testing](/sbd-toe/sbd-manual/testes-seguranca/intro)

---

### US-04 - Fast and tested *rollback* {#us-04---rollback-rápido-e-testado}

Failures happen. The difference between crisis and resilience lies in how quickly it is possible to go back.

**Context.** Without safe *rollback*, failures in production amplify the impact.

:::userstory
**Story.**  
As a **DevOps/SRE**, I want **to have fast and periodically tested *rollback***, so that **problematic *releases* can be reverted**.

**Acceptance criteria (BDD).**  
- **Given** an incident in production  
  **When** I trigger *rollback*  
  **Then** the previous version is restored in a controlled way and with recorded evidence

**Checklist.**  
- [ ] Automated *rollback* configured  
- [ ] Quarterly *rollback* tests  
- [ ] Documented evidence
:::

**Artefacts & evidence.** *Rollback* logs + reports.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Documented manual + tested annually | Automated + tested quarterly | Automated + tested quarterly |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Production | Incident or failure | DevOps/SRE | Rollback RTO in line with Policy 27 §6 (≤ 30 min at L2, ≤ 15 min at L3) |

**Useful links.** [Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### US-05 - *End-to-end* traceability {#us-05---rastreabilidade-end-to-end}

If it is not possible to reconstruct the path from the *commit* to the *deployment*, there is no real governance.

**Context.** Without traceability, it is not possible to audit incidents rigorously.

:::userstory
**Story.**  
As a **Product Owner**, I want **to ensure traceability across *commit* → build → release → deploy**, so that **risk decisions can be audited and justified**.

**Acceptance criteria (BDD).**  
- **Given** a post-release incident  
  **When** I audit the history  
  **Then** I can trace the origin back to the initial *commit* and the artefacts produced

**Checklist.**  
- [ ] Logs preserved and correlatable (build/release/deploy)  
- [ ] Reports attached to the *release*  
- [ ] Audit completed and recorded
:::

**Artefacts & evidence.** Traceability record, CI/CD logs.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Complete (who approved, artefact + *commit* SHA, when, environment, *gates*) | Complete | Complete + continuous audit |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Audit | Incident or periodic review | Executive Management + AppSec | Annual |

**Useful links.** [Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro) ; [Secure CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro)

---

### US-06 - Post-deployment monitoring {#us-06---monitorização-pós-deploy}

A *deployment* does not end at the *merge*: it is only considered complete when the version is stable and visible in production.

**Context.** Insecure *deployments* can give rise to undetected failures.

:::userstory
**Story.**  
As a **DevOps/SRE**, I want **to activate post-deployment monitoring**, so that **anomalies and regressions are detected in real time**.

**Acceptance criteria (BDD).**  
- **Given** a new version in production  
  **When** a relevant anomaly occurs (errors, latency, integrity)  
  **Then** automatic alerts are generated and routed for response

**Checklist.**  
- [ ] *Dashboards* updated  
- [ ] Alerts configured  
- [ ] Response process defined
:::

**Artefacts & evidence.** Logs + health metrics.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic | Critical | Complete + automatic response |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Post-release | Entry into production | DevOps/SRE | ≤ 15 min |

**Useful links.** [Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### US-07 - Execution control with *feature flags* {#us-07---controlo-de-execução-com-feature-flags}

The ability to enable or disable functionality in production without a new *deployment* is essential to mitigate risks and respond quickly to incidents.

**Context.** Without dynamic control, every problem requires a new *deployment* or *rollback*, amplifying the impact.

:::userstory
**Story.**  
As **DevOps/AppSec**, I want **to implement *feature flags* with metadata, *owner* and expiry**, so that **functionality can be enabled/disabled dynamically without a new *deployment* and with full traceability**.

**Acceptance criteria (BDD).**  
- **Given** that a new piece of functionality is delivered  
  **When** the *flag* is active  
  **Then** the functionality is controlled by scope rules (environment, group, geo) and recorded for audit

- **Given** that a *flag* is changed  
  **When** the change is applied  
  **Then** who changed it, when and why is recorded

- **Given** that a *flag* has a defined expiry  
  **When** the expiry is reached  
  **Then** the *flag* is automatically disabled and reported

**Checklist.**  
- [ ] *Flags* with metadata (owner, expiry, justification)  
- [ ] *Flags* versioned as code (YAML/JSON)  
- [ ] PR validation with approval for critical *flags*  
- [ ] Enable/disable logs in the audit system  
- [ ] *Kill switch* configured for sensitive functionality  
- [ ] *Fallback* tests for every critical *toggle*
:::

**Artefacts & evidence.** *Flag* configuration (versioned), audit logs, report of expired *flags*.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Optional | Recommended | Mandatory |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Deploy/Production | Functionality activation | DevOps + AppSec | Immediate |

**Useful links.** [Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### US-08 - Secure secrets management in *deployment* {#us-08---gestão-segura-de-segredos-no-deploy}

Secrets embedded in artefacts create exposure that is difficult to revoke and amplify *supply chain* risk.

**Context.** Credentials in images/artefacts increase the impact of a leak and complicate rotation.

:::userstory
**Story.**  
As **DevOps/AppSec**, I want **to ensure that secrets are never embedded in *deployment* artefacts**, so that **exposure is reduced and dynamic rotation is possible without a new *deployment***.

**Acceptance criteria (BDD).**  
- **Given** a *deployment* pipeline  
  **When** the artefact is built  
  **Then** *secret scanning* blocks embedded credentials

- **Given** that a credential is required at execution time  
  **When** the application is started  
  **Then** the credential is injected only at *runtime* via a secrets vault and with audit

- **Given** that the platform supports short-lived identities  
  **When** we authenticate to obtain secrets  
  **Then** OIDC / *workload identity* is used (no long-lived keys)

**Checklist.**  
- [ ] *Secret scanning* active in CI (e.g. trivy, gitleaks, truffleHog)  
- [ ] Pipeline fails if credentials are detected  
- [ ] Secrets injected via a secure mechanism (*secrets manager*, volumes, restricted env)  
- [ ] OIDC / *workload identity* configured (no persistent keys)  
- [ ] Secret rotation documented (TTL, expiry policy)  
- [ ] Centralised audit of access to secrets
:::

**Artefacts & evidence.** *Secret scanning* logs, secret injection configuration, access audit report.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Mandatory (blocking *secret scanning*, no embedded secrets; OIDC recommended) | Mandatory | Mandatory + automatic rotation |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Build/Deploy | Artefact build | DevOps + AppSec | Every build |

**Useful links.** [Secure CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro)

---

### US-09 - Semantic versioning and technical *changelog* {#us-09---versionamento-semântico-e-changelog-técnico}

Clear communication of the changes in each *release* is essential for informed decisions on risk acceptance and for post-incident audits.

**Context.** Without a structured *changelog*, there is no reliable way to communicate compatibility risks or fixed vulnerabilities.

:::userstory
**Story.**  
As **Developer/Executive Management**, I want **to maintain semantic versioning with a technical and security *changelog***, so that **the changes, risks and compatibility of each *release* are clearly communicated**.

**Acceptance criteria (BDD).**  
- **Given** a new *release*  
  **When** a version *tag* is created  
  **Then** the version follows semantic versioning (MAJOR.MINOR.PATCH) and references the exact *commit*

- **Given** the publication of the *release*  
  **When** I update the *changelog*  
  **Then** technical changes (breaking changes, dependencies, fixed CVEs) and security notes are recorded

**Checklist.**  
- [ ] Semantic versioning applied (vX.Y.Z)  
- [ ] `CHANGELOG.md` updated per *release*  
- [ ] Security section with CVEs/mitigations and severity  
- [ ] *Owner* of the *release* defined and recorded  
- [ ] *Commit* hash and date associated with the version  
- [ ] Compatibility / breaking changes document where applicable
:::

**Artefacts & evidence.** Versioned `CHANGELOG.md`, Git *tags* with metadata, breaking changes report (where applicable).

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic | Complete + security | Complete + security + compatibility |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Release | *Release* creation | Developer + Executive Management | Every version |

**Useful links.** [Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro)

---

### US-10 - Progressive *deployment* with *canary*/*blue-green* strategies {#us-10---deploy-progressivo-com-estratégias-canaryblue-green}

Promoting to 100% of users simultaneously amplifies the impact of any failure. Progressiveness makes it possible to detect regressions with controlled risk.

**Context.** Immediate *deployment* to 100% increases the probability of a widespread incident.

:::userstory
**Story.**  
As **DevOps / SRE / Executive Management**, I want **to implement progressive *deployment* (*canary*, *blue/green*, staged rules)**, so that **risk is mitigated and fast *rollback* with minimised impact is possible**.

**Acceptance criteria (BDD).**  
- **Given** a candidate *release* with a *rollout* plan  
  **When** I start the *deployment*  
  **Then** the version is promoted gradually (e.g. 1% → 5% → 20% → 100%)

- **Given** that I am at a *rollout* stage  
  **When** I assess the success metrics (errors, latency, security)  
  **Then** promotion to the next stage only happens if the criteria are met; otherwise, it blocks or reverts

- **Given** a triggered blocking criterion  
  **When** the *threshold* is exceeded  
  **Then** automatic *rollback* occurs or a human decision is required according to criticality

**Checklist.**  
- [ ] *Rollout* strategy documented (*canary* by percentage or *blue/green* by validation)  
- [ ] Success metrics per stage defined (baseline vs *canary*)  
- [ ] Blocking criteria parameterised (e.g. 5xx errors, latency, alerts)  
- [ ] Tests on *canary* validated before general promotion  
- [ ] Automatic *rollback* by *threshold* or manual by *owner*  
- [ ] Real-time *rollout* status *dashboard*  
- [ ] Clear decision roles (who approves promotion between stages)
:::

**Artefacts & evidence.** *Rollout* configuration, baseline vs *canary* metrics, event logs, status *dashboard*.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Recommended (manual by stages) | Automated with metrics | Automated + *rollback* by *threshold* |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Deploy | Promotion to production | DevOps + QA | Per stage ≤ 30 min |

**Useful links.** [Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### US-11 - Pre-deployment technical validations with conditional *gates* {#us-11---validações-técnicas-pré-deploy-com-gates-condicionais}

Without structured validations before *deployment*, insecure or non-functional code can reach production.

**Context.** Inadequate validations compromise integrity and raise operational risk.

:::userstory
**Story.**  
As **AppSec/QA**, I want **to run technical validations (SAST, DAST, SBOM, *findings* analysis) with risk-conditional *gates***, so that **insecure *releases* are blocked automatically**.

**Acceptance criteria (BDD).**  
- **Given** a candidate *release*  
  **When** the *deployment* pipeline starts  
  **Then** minimum validations are run (SAST, DAST in *staging*, SBOM/dependency verification) and a report is produced

- **Given** the result of the validations  
  **When** there are *findings* above the threshold defined for Lx  
  **Then** the *deployment* is blocked, unless a formal approved exception exists

**Checklist.**  
- [ ] SAST configured (e.g. SonarQube, Semgrep or equivalent)  
- [ ] Authenticated DAST in *staging*  
- [ ] SBOM generated (CycloneDX/SPDX) and validated  
- [ ] Dependency analysis (CVE/licensing/policies)  
- [ ] *Findings* with a justified decision (accepted/mitigated/false positive)  
- [ ] *Gates* parameterised by risk L1–L3  
- [ ] Exceptions recorded with *owner*, justification and review/expiry date  
- [ ] Validation report attached to each *release*
:::

**Artefacts & evidence.** SAST/DAST reports, SBOM, list of *findings* with status, *gate* logs (blocks, approvals, exceptions), versioned pipeline configuration.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| SAST + block on Critical | SAST + DAST + blocking on High/Critical | SAST + DAST + blocking on Medium+ |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Pre-release | Validation before production | AppSec + DevOps | ≤ 30 min |

**Useful links.** [Security Testing](/sbd-toe/sbd-manual/testes-seguranca/intro)

---

### US-12 - Structured *rollback* by type (binary, configuration, DB, infra) {#us-12---rollback-estruturado-por-tipo-binário-configuração-bd-infra}

Not all *rollbacks* are alike. Without a specific plan per type, rollback tends to be manual, slow and risky.

**Context.** Unplanned *rollbacks* amplify recovery time and the risk of inconsistency.

:::userstory
**Story.**  
As a **DevOps/SRE**, I want **to document and test *rollback* for each type of change (binary, configuration, DB, infrastructure)**, so that **incidents can be reverted quickly and with confidence**.

**Acceptance criteria (BDD).**  
- **Given** an incident in production  
  **When** I trigger *rollback*  
  **Then** there is a procedure applicable to the type of change and evidence is recorded (who, when, target version)

- **Given** a DB or infrastructure change  
  **When** a rollback occurs  
  **Then** there is consistency control (reversible migrations/snapshots; known IaC state) and post-*rollback* validation

**Checklist.**  
- [ ] *Rollback* plan per type documented and reviewed  
- [ ] Binary *rollback*: previous Git *tag* identified + tested  
- [ ] Configuration *rollback*: revertible *feature flags* / variables  
- [ ] DB *rollback*: reverse migration or tested *snapshot*  
- [ ] Infra *rollback*: Terraform/Helm with known state and safe procedure  
- [ ] *Rollback* tests executed quarterly (evidence)  
- [ ] SLA per type defined and communicated  
- [ ] *Rollback* approval and audit process
:::

**Artefacts & evidence.** Procedures (1 per type), quarterly test logs, evidence of DB rollback, IaC configuration with rollback, audit of executed *rollbacks*.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Documented manual + tested annually | Automated (binary + config) + tested quarterly | Automated for all types + tested quarterly |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Incident | Failure in production | DevOps/SRE | Rollback RTO in line with Policy 27 §6 (≤ 30 min at L2, ≤ 15 min at L3) |

**Useful links.** [Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### US-13 - Mandatory human validation after automated deployment {#us-13---validação-humana-obrigatória-após-deploy-automatizado}

A successful automated deployment is not synonymous with secure operation.
This US ensures that any automatic promotion to production is validated by a human owner.

:::userstory
**Story.**  
As **Ops/AppSec**, I want **to explicitly validate the security state after an automated deployment**, so that **it is ensured that there are no unexpected impacts before the release is considered complete**.

**Acceptance criteria (BDD).**  
- **Given** that an automated deployment to production is completed  
  **When** the system enters an operational state  
  **Then** there is documented human validation before the release is closed

- **Given** that metrics or alerts indicate anomalous behaviour  
  **When** the validation takes place  
  **Then** the deployment is marked as pending or reverted until the analysis is concluded
:::

**Artefacts & evidence.** Post-deployment validation record, observed metrics, final decision.

**Proportionality.**  
L1: sample-based validation  
L2: mandatory validation  
L3: validation + dual approval

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Production | Post-deployment | Ops/AppSec | `<`24h |

---

### US-14 - Operational drift control and validation {#us-14---controlo-e-validação-de-drift-operacional}

Continuous automation introduces the risk of silent drift between the desired and the actual state.

:::userstory
**Story.**  
As **Ops**, I want **to detect and validate operational drift**, so that **it is ensured that automatic or manual changes do not introduce unsafe deviations**.

**Acceptance criteria (BDD).**  
- **Given** a defined desired state  
  **When** drift occurs in production  
  **Then** the deviation is recorded, analysed and validated before automatic correction
:::

**Artefacts & evidence.** Drift reports, human decision, history of corrections.

**Proportionality.**  
L1: alert  
L2: mandatory validation  
L3: blocking until validation

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Continuous operation | Drift detection | Ops | `<48h` |

---

### US-15 - Reproducibility of incidents at runtime {#us-15---reprodutibilidade-de-incidentes-em-runtime}

Without reproducibility, there is neither audit nor improvement.

:::userstory
**Story.**  
As **Ops/AppSec**, I want **to ensure that incidents in production are reproducible**, so that **root causes and the effectiveness of fixes can be validated**.

**Acceptance criteria (BDD).**  
- **Given** an operational incident  
  **When** it is analysed  
  **Then** there is sufficient context to reproduce the observed behaviour
:::

**Artefacts & evidence.** Versioned logs, configuration snapshots, RCA report.

**Proportionality.**  
L1: basic reproducibility  
L2: documented reproducibility  
L3: complete and auditable reproducibility

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Production | Incident | Ops/AppSec | Defined SLA |

---
## 📦 Expected artefacts {#-artefactos-esperados}

Every practice must leave a verifiable trail.  
These artefacts constitute the objective evidence required for audits and compliance:

| Artefact | Evidence |
|-----------|-----------|
| Signed artefact + SBOM | Validated provenance |
| *Staging* reports | Functional tests + DAST + data segregation |
| *Gate* configuration | Versioned pipeline |
| *Rollback* logs | Evidence of rollback |
| *End-to-end* traceability | *Commit* → *release* → *deploy* |
| Post-deployment monitoring | *Dashboards* + alerts |
| *Feature flag* configuration | Versioned (YAML/JSON) + audit logs |
| *Secret scanning* logs | Blocks in CI + clean artefacts |
| `CHANGELOG.md` and Git *tags* | Versioning + *release* metadata |
| Progressive *rollout* configuration | Configuration + metrics per stage |
| Pre-deployment technical validations | Reports + *findings* decisions + evidence |
| *Rollback* procedures per type | Documents + quarterly tests |

---

### US-16 - Separation between automatic action and irreversible authorisation {#us-16---separação-entre-ação-automática-e-autorização-irreversível}

Tools can act, but not decide on irreversible impacts.

:::userstory
**Story.**  
As **DevOps / SRE**, I want **to separate the automatic execution of irreversible actions from human authorisation**, so that **control and explicit accountability are ensured**.

**Acceptance criteria (BDD).**  
- **Given** that an irreversible action is proposed automatically  
  **When** it is executed  
  **Then** human authorisation has been recorded beforehand
:::

**Artefacts & evidence.** Authorisation record, execution logs, identity of the decision-maker.

**Proportionality.**  
L1: explicit recorded human authorisation  
L2: formal authorisation  
L3: dual approval

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Production | Critical action | DevOps / SRE | Before execution |

---

### US-17 - Auditable operational evidence {#us-17---evidência-operacional-auditável}

Logs and metrics only have value when treated as evidence.

:::userstory
**Story.**  
As **GRC/AppSec**, I want **to treat operational evidence as an auditable artefact**, so that **effective control in operation can be demonstrated**.

**Acceptance criteria (BDD).**  
- **Given** a relevant event (deploy, rollback, incident)  
  **When** it occurs  
  **Then** the evidence is preserved, versioned and accessible for audit
:::

**Artefacts & evidence.** Immutable logs, defined retention, audit trails.

**Proportionality.**  
L1: minimum retention defined in policy  
L2: defined retention  
L3: retention + periodic review

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Continuous operation | Event | Ops/GRC | Immediate |

---

### US-18 - Specific release gates for systems with AI agents {#us-18}

**Context.**
When the system includes **AI agents** or an **AI model as a *load-bearing* dependency**, the *release* is no longer just "new application binary → production". There are three new artefacts on the critical path that can change behaviour without the application binary changing: the **model version**, the ***skill files* / *system prompts*** that direct the agent, and the ***eval suite*** that underpins the A0–A4 autonomy classification. The *release* has to treat these three as dimensions in their own right, with *gates*, independent *rollback* and a *canary* strategy.

:::userstory
**Story.**
As a **DevOps / SRE** and **AppSec**, I want the *release* of systems with AI agents to have specific *gates* — the *eval suite* as a gate; model *rollback* independent of application *rollback*; *canary release* of the model version — so that changes affecting agentic behaviour are as controllable and reversible as code changes.

**Acceptance criteria (BDD).**
- **Given** a promotion to production that changes the model, *skill files* or *system prompts*
  **When** the *release* pipeline runs
  **Then** the *eval suite* (Ch. 10 §C5) runs as a mandatory *gate*; a *fail* blocks the promotion
- **Given** that a model version in production shows degradation ([`OPS-011`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes) *drift*, [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) *off-policy actions* have increased, [`OPS-013`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013) *budget overrun*)
  **When** the decision is taken to roll back
  **Then** there is a *rollback* procedure for the model version **without** reverting the application binary (and vice versa)
- **Given** a major version change of the model (provider changes, new *fine-tune*, or new *system prompt* with material impact)
  **When** it is promoted to production
  **Then** the strategy is *canary* — a controlled fraction of traffic directed to the new version during an observable window, with objective criteria for promotion or rollback
- **Given** an agent *mandate* (Policy 38) with a declared `autonomy_level`
  **When** the *eval suite* fails or the coverage `m_recall` drops below the threshold
  **Then** the agent is automatically demoted to the lower level (e.g. A3 → A2) until resolution; it does not operate at the requested level

**Acceptance criteria (DoD).**
- [ ] *Eval suite* registered as a mandatory *gate* in the pipeline (cross-link Ch. 07 [US-19](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle))
- [ ] `eval_run_id` linked to the *release* and archived as evidence
- [ ] Independent model *rollback* procedure documented (revoke the model *deployment* in the *artefact registry* / *model registry*, without touching the application binary)
- [ ] Independent *system prompt* / *skill file* *rollback* procedure (reverting the *commit* of the *skill files* does not require an application redeploy if the *runtime* reads dynamically from the *registry*)
- [ ] *Canary* strategy configured for model promotions: initial fraction (typically 5–10%), promotion criteria (error rate, *off-policy events*, latency, *user satisfaction* when available), automatic *rollback* criteria
- [ ] Automatic *gate* that lowers the `autonomy_level` when the *eval suite* does not confirm the intended level (cross-link [Policy 38](/sbd-toe/assets/policies/policy-mandates-agentes) §5.4)
- [ ] *Release notes* include model version, *skill files* version, *eval suite* version, `mandate_ref`

:::

**🧾 Artefacts & evidence.**
- *Pipeline manifest* with *eval gate* configured
- `eval_run_id` per *release* archived and correlated with `mandate_ref`
- *Model rollback* *runbook* (separate from application *rollback*)
- *Prompt/skill rollback* *runbook*
- *Canary release plan* per major model version change, with objective criteria
- *Logs* of automatic *autonomy demotion* when the *eval* fails
- Extended *release notes* with agentic versions

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Recommended | Simple *eval gate*; model *rollback* may share the pipeline with the application |
| L2 | Yes for A1+ | Full *eval gate*; independent model *rollback* documented; *canary* recommended |
| L3 | Yes for A1+ | Full *eval gate* + mandatory *canary* on major version change + audit of the `eval_run_id` |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Pre-promotion | *Eval gate* fails | DevOps + AppSec | Immediate block |
| Promotion | Major model / prompt version change | DevOps + AppSec + agent *owner* (Policy 38) | Declared *canary* window |
| Degradation in production | `OPS-011/013/014` fires | Ops + AppSec | *Rollback* according to severity level |
| Audit | `review_cadence` of the *mandate* | AppSec | According to cadence |

**Useful links.**
- 🔗 [Ch. 07 US-19 — Agents in the pipeline](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle)
- 🔗 [Ch. 10 §C5 — Eval suites](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites)
- 🔗 [Ch. 12 — `OPS-011..014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes)
- 🔗 [Ch. 12 US-13 — Agentic telemetry](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle)
- 🔗 [Policy 38 §5.4 — Mandate activation](/sbd-toe/assets/policies/policy-mandates-agentes)
- 🔗 [Policy 39 §5 — Version pinning](/sbd-toe/assets/policies/policy-ai-bom-supply-chain)
- 🔗 Canonical grounding: [`DPL-010` / `DPL-011`](./addon/catalogo-requisitos-deploy)

---

### US-19 - Per-application, ephemeral *deployment* credentials {#us-19---credenciais-de-deploy-isoladas-por-aplicação-e-efémeras}

A shared *deployment* credential turns the compromise of one pipeline into the compromise of everything it reaches.  

**Context.** The credentials used at *deployment* time combine privileged access to production environments with unsupervised automation. When they are permanent or shared between applications, a single exfiltrated *token* gives lateral movement across the whole portfolio and makes it impossible to attribute misuse to a specific application. US-08 covers *application* secrets injected at *runtime*; this US addresses the credentials *of the deployment pipeline* — minimum scope, short life and isolation per application (`DPL-006`).  

:::userstory
**Story.**   
As a **DevOps/SRE**, I want **each application to use its own *deployment* credentials, with minimum scope and short duration, never shared between applications**, so that **the blast radius of a compromised credential is contained and usage is attributable and auditable**.  

**Acceptance criteria (BDD).**  
- **Given** an application's *deployment* pipeline  
  **When** the pipeline authenticates to promote to production  
  **Then** it uses an ephemeral identity per run (OIDC / *workload identity*), with no persistent keys  
- **Given** the set of *deployment* credentials of the portfolio  
  **When** their scope is audited  
  **Then** no *deployment* credential is shared between applications and each one has only the permissions needed for its target  
- **Given** a promotion to production  
  **When** the credential is used  
  **Then** the usage is recorded (identity, application, timestamp, environment) and correlatable with the *deployment*  

**Checklist.**  
- [ ] OIDC / *workload identity* configured (no long-lived keys in *deployment*)  
- [ ] Distinct *deployment* credentials per application (no sharing between apps)  
- [ ] Minimum scope per credential (permissions limited to the target)  
- [ ] Credential usage logs centralised and correlatable with the *deployment*  

:::

**Artefacts & evidence.** *Workload identity*/OIDC configuration per pipeline, inventory of *deployment* credentials per application, credential usage logs.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Minimum scope and duration documented; no sharing between apps; usage logs available | OIDC/*workload identity* (ephemeral tokens); isolation per app | OIDC mandatory + periodic audit of scope and usage logs |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Build/Deploy | Pipeline authentication | DevOps/SRE | Every deployment |

**Useful links.** [DPL-006 catalogue](/sbd-toe/sbd-manual/deploy-seguro/addon/catalogo-requisitos-deploy) · [Secure CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro)

---

### US-20 - *Feature flags* evaluated in the *backend* as the trust boundary {#us-20---feature-flags-avaliadas-no-backend-como-fronteira-de-confiança}

A *toggle* evaluated on the client controls nothing: it protects only what the user chooses not to bypass.  

**Context.** *Feature flags* that decide the exposure of sensitive functionality have to be evaluated in the *backend*. *Client-side* evaluation can be manipulated through the UI and allows trivial *bypass*; and a *toggle* never replaces access control. US-07 covers the *flag* lifecycle (metadata, *owner*, expiry, versioning as code); this US addresses the security property of the evaluation — where the decision is taken and how the *fallback* is validated.  

:::userstory
**Story.**   
As **Dev/AppSec**, I want **toggles that control sensitive logic to be evaluated in the *backend*, never only in the *frontend*, and never as a substitute for access control**, so that **UI-manipulation *bypass* is prevented and the server is guaranteed to be the trust boundary**.  

**Acceptance criteria (BDD).**  
- **Given** a *toggle* that controls sensitive functionality or a sensitive flow  
  **When** the functionality is requested  
  **Then** the activation decision is evaluated and enforced in the *backend* (the UI is not the decision boundary)  
- **Given** a *toggle* manipulated on the client (UI/parameter)  
  **When** the request reaches the server  
  **Then** the *backend* enforces the correct state and the *bypass* has no effect  
- **Given** a critical *toggle*  
  **When** it is on and when it is off  
  **Then** both logical paths (with and without the *toggle*) are testable and have a defined *fallback*  

**Checklist.**  
- [ ] Sensitive-logic *toggles* evaluated in the *backend* (not only in the *frontend*)  
- [ ] *Toggle* not used as a substitute for access control (independent authorisation)  
- [ ] Paths with and without the *toggle* testable, with a defined *fallback*  
- [ ] *Toggle* evaluation/change recorded in logs (not silent)  

:::

**Artefacts & evidence.** Evidence of *server-side* evaluation (code/configuration), tests of the paths with and without the *toggle*, *toggle* evaluation logs.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| *Backend* for sensitive *toggles*; documented *fallback* | *Backend* for all logic *toggles*; both paths tested | *Backend* + independent authorisation + auditable evaluation logs |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Development/Deploy | Introduction or change of a sensitive *toggle* | Dev + AppSec | Every *toggle* PR |

**Useful links.** [Feature Flags and Toggles](/sbd-toe/sbd-manual/deploy-seguro/addon/03-feature-flags-e-toggle) · [Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

## ⚖️ L1–L3 proportionality matrix {#️-matriz-de-proporcionalidade-l1l3}

Not all applications require the same level of control.  
Proportionality makes it possible to adapt rigour without compromising security:

| Practice | L1 | L2 | L3 |
|---------|----|----|----|
| Deployment of signed artefacts | Mandatory + automatic rejection | Mandatory + automatic rejection | Mandatory + automatic rejection |
| Validation in *staging* | Optional | Mandatory | Mandatory |
| Approval *gates* | Block on Critical | Blocking on High/Critical | Blocking on Medium+ |
| *Rollback* | Manual + tested annually | Automated + tested quarterly | Automated + tested quarterly |
| Traceability | Complete | Complete | Complete + audit |
| Monitoring | Basic | Critical | Complete + automatic response |
| Feature flags and toggles | Optional | Recommended | Mandatory |
| Secrets management (OIDC/Workload Identity) | Mandatory (no embedded secrets; OIDC recommended) | Mandatory | Mandatory + automatic rotation |
| Semantic versioning and changelog | Basic | Complete + security | Complete + security + compatibility |
| Progressive deployment (Canary/Blue-Green) | Recommended (manual) | Automated with metrics | Automated + threshold-triggered rollback |
| Pre-deployment technical validations | SAST + block on Critical | SAST + DAST + blocking on High/Critical | SAST + DAST + blocking on Medium+ |
| Rollback by type (binary, config, DB, infra) | Documented manual + tested annually | Automated (binary + config) + tested quarterly | Automated for all types + tested quarterly |

---

## 🏁 Final recommendations {#-recomendações-finais}

- **Never promote directly** to production without staging.  
- **Automate deployments, trace and roll back** whenever necessary.  
- **Regularly tested rollback** ensures resilience.  
- **Post-deployment monitoring** must be integrated with incident response (Ch. 12).  
- **Applying L1–L3 proportionality** ensures a balance between cost and risk.  
