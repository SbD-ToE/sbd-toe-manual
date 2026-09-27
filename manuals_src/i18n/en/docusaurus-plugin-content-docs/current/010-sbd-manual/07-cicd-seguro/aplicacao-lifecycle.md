---
id: aplicacao-lifecycle
title: How to Do It
description: How to apply secure CI/CD practices throughout the application lifecycle, with proportionality by risk, normalised user stories and auditable evidence
tags: [tipo:aplicacao, ciclo-vida, cicd, devsecops, pipelines, seguranca, rastreabilidade]
genia: us-format-normalization
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/aplicacao-lifecycle.md
  source_sha256: 5023737507c52572f27e4ae34ec5f8039a3e37b452199a1b6fc60bd55af4ae81
  source_commit: a7cc396e338fab4654022c3d9077a3472e358da2
  target_sha256: bd1ba42b6119c94ce0f82a8f23405f75cc5d263935062835ada4b93d718b7a8d
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [audit_trail, avaliacao, como_fazer, cycle_iteration, deterministic, eu_startups, framework_source_corpus, lifecycle_phase, practitioner_manual, provenance, requirement_runtime, risk_level, segregacao_de_funcoes, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 8e0a9e412a45cb18d7c66722a093bf4faba95364df8e5c65e23bbbf2434d4a47
  translated_at: 2026-09-27T15:09:26Z
  stamped_at: 2026-09-27T15:09:26Z
  reviewed_by: null
---

# Applying in the Lifecycle - Secure CI/CD

While `intro.md` explains **why pipelines are critical** and which practices must be applied, this document shows **how to turn those prescriptions into concrete actions** throughout the development and delivery lifecycle.

The guiding principle is simple and non-negotiable:

- the pipeline may automate **execution** and produce **signals**;
- but the organisation only gains security when there is **assigned human decision**, **empirical validation** and **auditable evidence**.

As automation becomes more sophisticated, additional process risks arise: non-determinism, “implicit approval” through outputs, plausible evidence without real execution, context leakage and dilution of responsibility.  
This document operationalises those concerns without “talking about technology”: it treats them as **engineering controls** and **pipeline governance**.

---

## 🧭 When to apply {#-quando-aplicar}

Security in pipelines does not happen only when something goes wrong - it is part of their DNA from the first commit.  
Whenever a pipeline is created, changed, executed or promoted, there are *triggers* that require specific controls:

| *Trigger* moment                                                   | Security objective                                                                 | Main roles                               |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------|
| Creation or refactoring of the pipeline                                    | Introduce baseline controls, ensure auditability and avoid changes “outside the PR”    | Developers, DevOps / SRE                       |
| Change to decision rules (gates/thresholds)                  | Ensure separation between automatic signal and decision; avoid implicit bypass           | AppSec Engineers, DevOps / SRE, GRC / Compliance |
| Change to tooling/infra (runners, permissions, secrets)         | Review isolation, secrets injection, blast radius and non-repudiation                      | DevOps / SRE, AppSec Engineers                 |
| Introduction/update of validators (scanners, tests, policies) | Increase coverage and gates proportional to risk; ensure evidence of real execution | Developers, AppSec Engineers, DevOps / SRE     |
| Integration of external services into the pipeline                        | Treat as a dependency; minimise context; mitigate exfiltration risk              | DevOps / SRE, AppSec Engineers, GRC / Compliance |
| Release preparation / promotion to production                        | Validate signature, provenance, traceability and human responsibility            | DevOps / SRE, AppSec Engineers                 |
| Exception record (gate *bypass*)                              | Formal approval, deadlines, compensations and automatic reversal                            | GRC / Compliance, Internal Auditors, AppSec Engineers |
| Audit or periodic review                                     | Demonstrate end-to-end traceability and reproducibility                            | GRC / Compliance, Internal Auditors, DevOps / SRE |

---

## 👥 Who carries out each action {#-quem-executa-cada-ação}

Responsibility in CI/CD is **shared**.  
A secure pipeline results from the sum of efforts: from the developer who submits code with active validations, to the DevOps engineer who hardens runners and secrets, to the GRC function that controls exceptions and evidences governance.

| Operational action                                                                 | Responsible                 | Support                                  | Evidence/Artefacts |
|----------------------------------------------------------------------------------|-----------------------------|----------------------------------------|----------------------|
| Define/change a versioned pipeline via PR                                        | Developers                  | DevOps / SRE                           | `ci-pipeline.yml`, review history |
| Define explicit, binary decision rules (gates/thresholds) by risk      | AppSec Engineers            | DevOps / SRE, GRC / Compliance         | Gate rules, published criteria, change records |
| Harden runners (ephemeral, non-privileged, segregated)                     | DevOps / SRE                | AppSec Engineers                       | Runner configuration, base images, evidence of isolation |
| Integrate validators (SAST, secrets, IaC, containers, SBOM, DAST when applicable)| Developers                  | AppSec Engineers, DevOps / SRE         | Reports + execution logs + *exit codes* |
| Secure secrets injection (OIDC, short TTL, masked logs)                         | DevOps / SRE                | AppSec Engineers                       | Secrets policies, access logs, evidence of rotation/TTL |
| Sign artefacts and generate provenance                                           | DevOps / SRE                | AppSec Engineers                       | Signatures, provenance, verification logs before promotion |
| Approve promotion/deploy (irreversible actions) with an explicit owner                 | DevOps / SRE                | AppSec Engineers (L2/L3), GRC (L3)     | Named approval record, context and associated evidence |
| Record and approve exceptions (with deadline and compensations)                            | GRC / Compliance, Internal Auditors | AppSec Engineers                   | Formal record of exceptions and approvals, TTL, compensating plan |
| Ensure commit→pipeline→release traceability                                  | DevOps / SRE                | GRC / Compliance, Internal Auditors   | Correlated logs, IDs, immutable export (when applicable) |
| Ensure log/output hygiene (minimisation of sensitive context)               | DevOps / SRE                | AppSec Engineers                       | Logging policy, evidence of masking/redaction, periodic review |

---

## 🧾 Normalised User Stories {#-user-stories-normalizadas}

Each practice is expressed as a **reusable user story**, with verifiable criteria, concrete artefacts and proportionality by risk level.

> Editorial note: these user stories explicitly assume that **“pretty output” is not evidence** and that **suggestions never amount to a decision**.  
> Whenever there are automatic signals (scores, recommendations, flags), they are treated as *inputs* to a formal human decision.

---

### US-01 - Secure source code management {#us-01---gestão-segura-de-código-fonte}

**Context.**  
Without control over the repository, any pipeline is vulnerable.

:::userstory
**Story.**  
As **Developers**, I want all changes to the repository to be protected by PR and mandatory review, so that integrity is ensured.

**Acceptance criteria (BDD).**
- **Given** that a protected repository exists  
  **When** I submit a PR to `main`  
  **Then** it is only accepted after mandatory review and all *checks* completed successfully.  
- **Given** that a *merge* occurs  
  **When** conflicts or relevant changes to the attack surface are detected  
  **Then** a new review and automatic re-execution of the defined validators are required.  

**Checklist.**
- [ ] Branch protection active  
- [ ] Mandatory reviewer  
- [ ] Status checks configured  
- [ ] `force push` prohibited
:::

**🧾 Artefacts & evidence.**  
Branch protection policies; review logs; Git history; merge audit.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|-------|---------------|----------|
| L1 | Yes | Simple review and mandatory *build check* |
| L2 | Yes | Technical reviewer + active security validation |
| L3 | Yes | Dual review (code owner + AppSec) and blocking on High failures |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| PR/MR | PR submission to `main` | Developers | Before the *merge* |
| Review | Conflict or relevant change to the attack surface in a *merge* | Developers | Before the *merge* |

---

### US-02 - Secure pipeline design (versioning, determinism and review) {#us-02---design-seguro-dos-pipelines-versionamento-determinismo-e-revisão}

**Context.**  
Insecure pipelines are prime targets for attack - and non-reproducible pipelines destroy audit.

:::userstory
**Story.**  
As **DevOps / SRE**, I want pipelines that are versioned and approved via PR, with deterministic behaviour, so that unaudited changes and non-reproducible results are avoided.

**Acceptance criteria (BDD).**
- **Given** that I change the pipeline definition  
  **When** I submit a PR  
  **Then** it is only accepted after review by DevOps and AppSec (at L2/L3).  
- **Given** that the pipeline depends on configuration or parameters  
  **When** it is executed  
  **Then** the effective configuration used is recorded as evidence (without sensitive data).  
- **Given** that there is a change to tools, stages or execution rules  
  **When** the pipeline is modified  
  **Then** a new traceable and auditable version is created (commit/hash + changelog in the PR).  

**Checklist.**
- [ ] `ci-pipeline.yml` versioned  
- [ ] Mandatory PR  
- [ ] Explicit triggers  
- [ ] Effective configuration recorded (without secrets)  
- [ ] Version history maintained
:::

**🧾 Artefacts & evidence.**  
Commit history; `ci-pipeline.yml` file; PR approval; review logs; record of effective configuration.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Pipeline versioned in the repository; changes only via PR with review |
| L2 | Yes | Versioning and mandatory review |
| L3 | Yes | Signed change control and reinforced provenance validation |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Creation/refactoring | Change to the pipeline definition submitted in a PR | DevOps / SRE | In the PR |
| Execution | Pipeline execution with configuration or parameters | DevOps / SRE | On every execution (effective configuration recorded) |
| Review | Change to tools, stages or execution rules | DevOps / SRE | In the PR (commit/hash + *changelog*) |

---

### US-03 - Integrated scanners (mandatory empirical validation) {#us-03---scanners-integrados-validação-empírica-obrigatória}

**Context.**  
Detecting early is cheaper and more effective - but it only counts if there is real execution.

:::userstory
**Story.**  
As **Developers**, I want the pipeline to run security validators with observable execution, so that serious failures in production are prevented.

**Acceptance criteria (BDD).**
- **Given** that I submit code  
  **When** the pipeline runs  
  **Then** the mandatory validators are executed and produce traceable logs/artefacts.  
- **Given** that there are critical failures  
  **When** the results are assessed  
  **Then** the merge/promotion is blocked in accordance with the defined gates.  
- **Given** that a new type of artefact is introduced  
  **When** the current validation set does not cover it  
  **Then** AppSec defines an additional rule and the change is versioned and approved.

**Checklist.**
- [ ] SAST active  
- [ ] Secrets scanning active  
- [ ] IaC scanning (when applicable)  
- [ ] Execution logs/artefacts retained  
- [ ] High/Critical failures block merge (L1–L3)
:::

**🧾 Artefacts & evidence.**  
Scanner reports; CI/CD logs; *exit codes*; blocking records; vulnerability dashboards.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Blocking baseline validation (SAST, SCA, secrets) + SBOM per build; image scanning where containers exist |
| L2 | Yes | L1 baseline + inclusion of IaC |
| L3 | Yes | Full validation including containers and SBOM |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| CI/CD | Code submission and pipeline execution | Developers | On every pipeline execution |
| Pre-promotion | Assessment of results with critical failures | Developers | Blocking of the *merge*/promotion at the *gate* |
| Review | New type of artefact not covered by current validation | AppSec | On approval of the additional versioned rule |

---

### US-04 - Secrets management {#us-04---gestão-de-segredos}

**Context.**  
Static secrets expose the organisation - and careless logs become a leakage channel.

:::userstory
**Story.**  
As **DevOps / SRE**, I want secrets injected via OIDC with a short TTL and masked outputs, so that the risk of abuse and indirect exposure is reduced.

**Acceptance criteria (BDD).**
- **Given** that the pipeline starts  
  **When** credentials are needed  
  **Then** they are issued *just-in-time*, with a short TTL and without exposure in logs.  
- **Given** that the token expires  
  **When** new access is needed  
  **Then** a new temporary token is generated without reuse.  

**Checklist.**
- [ ] OIDC configured  
- [ ] Short TTL  
- [ ] Masked variables  
- [ ] Logging reviewed so as not to expose sensitive context
:::

**🧾 Artefacts & evidence.**  
Secrets policies; access logs; OIDC configuration; evidence of TTL/rotation.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Secrets in a vault or protected platform variables + masking |
| L2 | Yes | OIDC implemented with controlled TTL |
| L3 | Yes | Automatic ephemeral tokens and frequent rotation |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| CI/CD | Pipeline start requiring credentials | DevOps / SRE | *Just-in-time*, at *job* start |
| Operation | Token expiry and need for new access | DevOps / SRE | On expiry, without reuse |

---

### US-05 - Runner isolation {#us-05---isolamento-de-runners}

**Context.**  
Insecure runners compromise the entire ecosystem.

:::userstory
**Story.**  
As **DevOps / SRE**, I want ephemeral, segregated runners, so that post-compromise persistence is reduced and the blast radius is limited.

**Acceptance criteria (BDD).**
- **Given** that a job finishes  
  **When** the runner shuts down  
  **Then** it is destroyed without retaining state.  
- **Given** that there are parallel pipelines  
  **When** they are executed  
  **Then** they are isolated by permissions, namespace and network segmentation.  

**Checklist.**
- [ ] Ephemeral runners  
- [ ] No excessive privileges  
- [ ] Network segmentation  
- [ ] No persistent state between jobs
:::

**🧾 Artefacts & evidence.**  
Runner configuration; execution logs; isolation records; provisioning scripts.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Shared runners with limits and hardening |
| L2 | Yes | Runner segregation per project |
| L3 | Yes | Ephemeral runners + isolated network + automatic destruction |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Provisioning | Execution of parallel *pipelines* | DevOps / SRE | On every execution |
| Operation | End of the *job* and shutdown of the *runner* | DevOps / SRE | At *job* shutdown |

---

### US-06 - Signature and provenance {#us-06---assinatura-e-proveniência}

**Context.**  
Unsigned artefacts lose legitimacy - and artefacts without provenance weaken audit and trust.

:::userstory
**Story.**  
As **DevOps / SRE**, I want all artefacts to be signed and to have validated provenance, so that trust is ensured and independent verification is possible.

**Acceptance criteria (BDD).**
- **Given** that an artefact is produced  
  **When** it is promoted  
  **Then** signature and provenance are verified before promotion.  
- **Given** that verification fails  
  **When** the signature/provenance is not valid  
  **Then** the artefact is rejected and an alert is issued.

**Checklist.**
- [ ] Automatic signing  
- [ ] Provenance generated  
- [ ] Verification before release  
- [ ] Automatic rejection on failure (L1–L3)
:::

**🧾 Artefacts & evidence.**  
Digital signatures; provenance files; promotion logs; build audit.

> **Reference:** This US complements the principle of generating an SBOM per build, integrating signature and provenance as build artefacts.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Verifiable hash generated at build + verification before promotion, with rejection on failure (signing recommended) |
| L2 | Yes | Automatic signing + mandatory verification |
| L3 | Yes | Automatic blocking + reinforced provenance validations |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Build/Promotion | Artefact production and promotion request | DevOps / SRE | Verification before promotion |
| Promotion | Invalid signature or provenance | DevOps / SRE | Rejection and alert on verification |

---

### US-07 - Gates by risk (signal/decision separation) {#us-07---gates-por-risco-separação-sinaldecisão}

**Context.**  
Not all apps require the same rigour - but in no app does a “signal” replace a decision.

:::userstory
**Story.**  
As **AppSec Engineers**, I want distinct, explicitly binary gates per L1–L3, so that proportional security is applied and implicit bypass is avoided.

**Acceptance criteria (BDD).**
- **Given** that an application is L3  
  **When** there is a High or Critical failure  
  **Then** the gate blocks promotion and requires a formal human decision for any exception.  
- **Given** that an application is L1  
  **When** there is a Medium failure  
  **Then** an alert is recorded without blocking, but with traceability and a remediation backlog.  
- **Given** that an automatic output (score/recommendation) exists  
  **When** it is presented  
  **Then** it is treated only as an input, never as approval.

**Checklist.**
- [ ] Policy published  
- [ ] Gates configured  
- [ ] Thresholds defined  
- [ ] Separation between signal and decision documented
:::

**🧾 Artefacts & evidence.**  
Gate policies; blocking logs; records of threshold changes; evidence of decision on exceptions.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Blocking on High/Critical |
| L2 | Yes | High/Critical blocking + AppSec approval for exceptions |
| L3 | Yes | Automatic blocking + reinforced governance (incl. GRC on exceptions) |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Pre-promotion | High or Critical failure in an L3 application | AppSec Engineers | Blocking at the *gate*, before promotion |
| Pre-promotion | Medium failure in an L1 application | AppSec Engineers | Alert at the *gate*, without blocking |
| Promotion | Presentation of an automatic *score*/recommendation | AppSec Engineers | At the promotion decision |

---

### US-08 - Extended coverage (containers and SBOM) {#us-08---cobertura-ampliada-containers-e-sbom}

**Context.**  
Limited coverage creates blind spots and weakens the supply chain.

:::userstory
**Story.**  
As **AppSec Engineers**, I want validation of containers and SBOM in pipelines, so that the supply chain is covered and component traceability is possible.

**Acceptance criteria (BDD).**
- **Given** that an image is built  
  **When** the pipeline runs  
  **Then** the SBOM is generated and attached to the artefact.  
- **Given** that a base image changes  
  **When** a vulnerability is detected  
  **Then** a mitigation task is opened and the risk is traceable to the affected release.

**Checklist.**
- [ ] Container scanning active  
- [ ] SBOM generated  
- [ ] Base images validated  
- [ ] Execution evidence retained
:::

**🧾 Artefacts & evidence.**  
Scanning reports; SBOM; image audit; build logs.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Image scanning in the pipeline (Critical blocks) + SBOM per build |
| L2 | Yes | Mandatory SBOM + validation of base images |
| L3 | Yes | Continuous scans + CVE correlation + blocking on critical risk |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Build | Image build | AppSec Engineers | On every *build*, with the SBOM attached to the artefact |
| Operation | Vulnerability detected in a base image in use | AppSec Engineers | On detection, with tracing to the affected *release* |

---

### US-09 - End-to-end traceability (commit→pipeline→release) {#us-09---rastreabilidade-ponta-a-ponta-commitpipelinerelease}

**Context.**  
Without tracing, audit is impossible - and incident investigation becomes speculative.

:::userstory
**Story.**  
As **GRC / Compliance**, I want to trace commit→pipeline→release, so that audits and incident investigation are supported.

**Acceptance criteria (BDD).**
- **Given** that an incident occurs  
  **When** I analyse a release  
  **Then** I can trace its origin back to the commit and pipeline execution.  
- **Given** that an auditor requests evidence  
  **When** I run a query  
  **Then** the system exports correlated, verifiable logs (without sensitive data).

**Checklist.**
- [ ] Correlation IDs  
- [ ] Logs retained  
- [ ] Immutable export (when applicable)  
- [ ] Explicit link between artefacts and execution
:::

**🧾 Artefacts & evidence.**  
Pipeline logs; dashboards; audit records; exports (immutable when required).

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Basic logs stored for 30 days |
| L2 | Yes | 90-day retention + commit-build correlation |
| L3 | Yes | Retention ≥1 year + immutable export + reinforced audit |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Incident | Analysis of a *release* following an incident | GRC / Compliance | Within retention: 30 days (L1), 90 days (L2), ≥1 year (L3) |
| Audit | Request for evidence by an auditor | GRC / Compliance | Correlated export within the level's retention |

---

### US-10 - Exception management (controlled bypass) {#us-10---gestão-de-exceções-bypass-controlado}

**Context.**  
Poorly managed exceptions become structural risk and normalise bypass.

:::userstory
**Story.**  
As **GRC / Compliance**, I want exceptions to be recorded, approved and temporary, so that accumulation of debt is avoided and governance is maintained.

**Acceptance criteria (BDD).**
- **Given** that an exception is requested  
  **When** it is analysed  
  **Then** it is only approved with a deadline, owner and compensations defined.  
- **Given** that the deadline expires  
  **When** there is no formal renewal  
  **Then** the exception is removed and the pipeline returns to its normal control mode.

**Checklist.**
- [ ] Owner recorded  
- [ ] Deadline defined  
- [ ] Dual approval (AppSec + GRC) at L2/L3  
- [ ] Record of compensations  
- [ ] Automatic reversal at the end of the deadline
:::

**🧾 Artefacts & evidence.**  
Exception register; approval logs; review reports; automatic deadlines in the GRC system.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Simple record with single approval |
| L2 | Yes | Dual approval and maximum deadline (e.g. 60 days) |
| L3 | Yes | Frequent review + mandatory audit |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Exception | Exception request submitted for analysis | GRC / Compliance | Approval only with deadline, *owner* and compensations; maximum deadline defined at L2 (e.g. 60 days) |
| Exception | Deadline expiry without formal renewal | GRC / Compliance | Automatic reversal at the end of the deadline |

---

### US-11 - Dynamic security testing (DAST) {#us-11---testes-de-segurança-dinâmicos-dast}

**Context.**  
Static tests provide only partial coverage; DAST in staging validates real behaviour.

:::userstory
**Story.**  
As **AppSec Engineers**, I want to run DAST in staging after deployment, so that behavioural vulnerabilities are validated before production.

**Acceptance criteria (BDD).**
- **Given** that a build is promoted to staging  
  **When** the DAST pipeline starts  
  **Then** relevant analyses are executed and the results are traceable to the commit/release.  
- **Given** that DAST finds a High failure  
  **When** the result is made available  
  **Then** it blocks promotion to production until a validated fix.

**Checklist.**
- [ ] DAST integrated into the pipeline  
- [ ] Segregated test credentials  
- [ ] Report correlated with the commit  
- [ ] Automatic blocking on High/Critical (L2/L3)
:::

**🧾 Artefacts & evidence.**  
DAST reports; execution logs; evidence of fixes; traceability.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Periodic manual DAST |
| L2 | Yes | DAST in pre-release staging |
| L3 | Yes | Continuous DAST + automatic blocking + post-fix revalidation |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Staging | Promotion of a *build* to *staging* | AppSec Engineers | On every promotion to *staging* |
| Pre-promotion | High failure reported by DAST | AppSec Engineers | Blocking of promotion to production until a validated fix |

---

### US-12 - Organisational metrics and compliance {#us-12---métricas-e-conformidade-organizacional}

**Context.**  
Without centralised visibility, risk accumulates unseen.

:::userstory
**Story.**  
As **Executive Management / CISO**, I want to view CI/CD metrics (coverage, gates, exceptions, blocks, MTTR), so that decisions are informed and corrective action is taken.

**Acceptance criteria (BDD).**
- **Given** that the pipeline executes  
  **When** events occur (merge, block, exception, promotion)  
  **Then** they are recorded with timestamp, context and actors.  
- **Given** that I consult the dashboard  
  **When** I filter by project/period/risk  
  **Then** I obtain actionable and auditable indicators.

**Checklist.**
- [ ] Centralised events  
- [ ] Dashboard with KPIs (coverage, MTTR, compliance rate)  
- [ ] Alerts on anomalies  
- [ ] Periodic reports for GRC
:::

**🧾 Artefacts & evidence.**  
Dashboard; centralised logs; reports; alerts; evidence of retention.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Periodic manual reports |
| L2 | Yes | Dashboard with main KPIs, updated daily |
| L3 | Yes | Near-real-time dashboard + automatic alerts |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Operation | Event in the pipeline (*merge*, block, exception, promotion) | Executive Management / CISO | Record with *timestamp*, context and actors at the time of the event |
| Audit | Query of the *dashboard* by project, period or risk | Executive Management / CISO | Daily update (L2); near real time (L3) |

---

### US-13 - Integrity validation of base images {#us-13---validação-de-integridade-de-imagens-base}

**Context.**  
Compromised base images propagate risk to the entire ecosystem.

:::userstory
**Story.**  
As **DevOps / SRE**, I want to validate the integrity of base images (hash/signature/drift) and correlate it with vulnerabilities, so that a compromised supply chain is avoided.

**Acceptance criteria (BDD).**
- **Given** that a base image is used  
  **When** the pipeline starts  
  **Then** the expected identifier is validated against a trusted source.  
- **Given** that a relevant vulnerability emerges  
  **When** it affects images in use  
  **Then** an alert is created and a mitigation action traceable to the release is opened.

**Checklist.**
- [ ] Hash/signature of base images recorded  
- [ ] Automatic validation on pull  
- [ ] Rejection on mismatch (L2/L3)  
- [ ] Continuous correlation with vulnerabilities
:::

**🧾 Artefacts & evidence.**  
Records of hashes/signatures; validation logs; drift reports; mitigation actions.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Periodic manual validation |
| L2 | Yes | Automatic validation on pull with logs |
| L3 | Yes | Validation + signature + automatic alerts on drift/vulnerability |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| CI/CD | Pipeline start with a base image | DevOps / SRE | Validation on *pull*, before the *build* |
| Operation | Relevant vulnerability affecting images in use | DevOps / SRE | Alert and mitigation action on detection |

---

## 🆕 Additional User Stories (process risks of modern CI/CD) {#-user-stories-adicionais-riscos-de-processo-do-cicd-moderno}

The following user stories make explicit the process concerns that, in practice, most degrade security as automation increases: **non-determinism, signal/decision confusion, weak evidence, context leakage and dilution of responsibility**.

---

### US-14 - Pipeline reproducibility and determinism {#us-14---reprodutibilidade-e-determinismo-do-pipeline}

**Context.**  
Without reproducibility, there is neither audit nor incident investigation.

:::userstory
**Story.**  
As **DevOps / SRE**, I want pipeline executions to be reproducible and deterministic (as far as possible), so that independent verification and audit are possible.

**Acceptance criteria (BDD).**
- **Given** that a build is executed  
  **When** I re-run the same pipeline on the same commit  
  **Then** I obtain equivalent results (or justified and recorded divergences).  
- **Given** that parameters/configuration exist  
  **When** the pipeline runs  
  **Then** the effective configuration used is recorded as evidence (without secrets).  

**Checklist.**
- [ ] Pipeline definition versioned  
- [ ] Relevant dependencies and versions stabilised/identified  
- [ ] Effective configuration recorded  
- [ ] Divergences documented when unavoidable
:::

**🧾 Artefacts & evidence.**  
Traceable execution (logs + effective config); link to commit; divergence records; artefacts produced.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | “Good-faith” reproducibility with sufficient logging |
| L2 | Yes | Reproducibility as a requirement; periodic validation |
| L3 | Yes | Mandatory reproducibility + reinforced audit and extended retention |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Execution | Re-execution of the same pipeline on the same *commit* | DevOps / SRE | Equivalent result, or justified and recorded divergence |
| Execution | Execution with parameters or configuration | DevOps / SRE | Effective configuration recorded on every execution |

---

### US-15 - Formal separation between automatic signal and promotion decision {#us-15---separação-formal-entre-sinal-automático-e-decisão-de-promoção}

**Context.**  
A “green score” is not a decision; a decision requires an owner and evidence.

:::userstory
**Story.**  
As **AppSec Engineers**, I want any recommendation/score/flag to be formally classified as a *signal*, and promotion to require an explicit human decision, so that implicit approval is avoided.

**Acceptance criteria (BDD).**
- **Given** that the pipeline produces signals (scores/recommendations)  
  **When** promotion is considered  
  **Then** the decision is recorded with a human owner and associated evidence.  
- **Given** that someone attempts to promote without a formal decision  
  **When** the pipeline assesses the action  
  **Then** it blocks and requires a named approval record.

**Checklist.**
- [ ] “Signal” vs “decision” distinction documented  
- [ ] Promotion requires named approval  
- [ ] Record includes referenced evidence  
- [ ] Automatic blocking of “ownerless” promotions
:::

**🧾 Artefacts & evidence.**  
Approval record; associated evidence; blocking logs; published policy.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Named approval for production |
| L2 | Yes | Named approval + segregation of duties rule |
| L3 | Yes | Named approval + reinforced audit + strict ACI rule (approval control integrity) |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Promotion | Promotion considered on the basis of signals (*scores*, recommendations) | AppSec Engineers | Named decision recorded before promotion |
| Promotion | Promotion attempt without a formal decision | AppSec Engineers | Blocking until a named approval is recorded |

---

### US-16 - Mandatory empirical evidence (anti-“reports without execution”) {#us-16---evidência-empírica-obrigatória-anti-relatórios-sem-execução}

**Context.**  
Plausible results do not replace real execution.

:::userstory
**Story.**  
As **GRC / Compliance**, I want any evidence of control in CI/CD to be based on observable execution (logs, *exit codes*, artefacts), so that apparent compliance without real validation is prevented.

**Acceptance criteria (BDD).**
- **Given** that a validation report exists  
  **When** it is used as evidence  
  **Then** it contains a verifiable reference to the execution (job/run id, logs, artefacts).  
- **Given** that there is no observable execution  
  **When** someone attempts to record a result as evidence  
  **Then** it is rejected as “not verifiable”.

**Checklist.**
- [ ] Evidence links to a real execution  
- [ ] Logs and *exit codes* available  
- [ ] Artefacts preserved in accordance with retention  
- [ ] Rejection of non-verifiable evidence
:::

**🧾 Artefacts & evidence.**  
Run IDs; logs; *exit codes*; artefacts; evidence policy.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Minimum evidence per execution |
| L2 | Yes | Mandatory evidence + reinforced retention |
| L3 | Yes | Mandatory evidence + immutable export and audit |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Audit | Use of a validation report as evidence | GRC / Compliance | Verifiable reference to the execution (*run id*, logs, artefacts) in the record |
| Audit | Recording of a result without observable execution | GRC / Compliance | Immediate rejection as «not verifiable» |

---

### US-17 - Context containment and log/output hygiene {#us-17---contenção-de-contexto-e-higiene-de-logsoutputs}

**Context.**  
The pipeline “sees” everything - so it is where context leakage is most likely.

:::userstory
**Story.**  
As **DevOps / SRE**, I want pipeline logs and outputs to be minimised and sanitised, so that exposure of secrets, sensitive data or intellectual property is prevented.

**Acceptance criteria (BDD).**
- **Given** that the pipeline executes  
  **When** it generates logs  
  **Then** secrets and sensitive identifiers are masked/redacted by default.  
- **Given** that debugging is needed  
  **When** it is temporarily enabled  
  **Then** it requires approval, is time-limited and produces evidence of deactivation.

**Checklist.**
- [ ] Logging policy published  
- [ ] Masking/redaction active by default  
- [ ] Temporary debugging controlled and auditable  
- [ ] Periodic review of logs and configurations
:::

**🧾 Artefacts & evidence.**  
Logging configuration; evidence of masking; records of debug activation/deactivation; review reports.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Basic masking + ad hoc review |
| L2 | Yes | Masking + formal debug control |
| L3 | Yes | Formal control + audit + retention and export as required |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| CI/CD | Log generation by the pipeline | DevOps / SRE | *Masking*/redaction by default, on every execution |
| Operation | Temporary activation of *debug* | DevOps / SRE | Prior approval, time-limited window and evidence of deactivation |

---

### US-18 - Non-repudiation and ownership of promotions (irreversible actions) {#us-18---não-repúdio-e-ownership-de-promoções-ações-irreversíveis}

**Context.**  
If nobody “signs” the promotion, nobody answers for the incident.

:::userstory
**Story.**  
As **DevOps / SRE**, I want any promotion to production to have an explicit human owner and a decision record, so that non-repudiation and accountability are ensured.

**Acceptance criteria (BDD).**
- **Given** that a promotion to production is requested  
  **When** it is executed  
  **Then** there is a named approval record and decision context (referenced evidence).  
- **Given** that no owner exists  
  **When** someone attempts to promote  
  **Then** the pipeline blocks the action.

**Checklist.**
- [ ] Promotion requires a human owner  
- [ ] Named record and timestamp  
- [ ] Referenced evidence (runs, artefacts, reports)  
- [ ] Blocking of promotions without a record
:::

**🧾 Artefacts & evidence.**  
Approval record; pipeline logs; associated evidence; audit trail.

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Named approval for production |
| L2 | Yes | Named approval + segregation of duties |
| L3 | Yes | Named approval + reinforced audit and extended retention |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Production | Promotion to production executed | DevOps / SRE | Named record and *timestamp* at the moment of promotion |
| Production | Promotion attempt without a human *owner* | DevOps / SRE | Immediate blocking of the action |

---

### US-19 - AI agents as *principals* in the pipeline {#us-19}

**Context.**
US-04 establishes the pattern for secrets in the pipeline: OIDC, short TTL, no *long-lived* credentials. When the pipeline comes to be **operated by AI agents** — `Claude Code` creating PRs and triggering *workflows*, `Copilot Workspace` performing *merges*, in-house agents built on SDKs executing *deploys* — those agents become **new non-human *principals*** with access to sensitive resources. The principle is the same as in US-04; what changes is that the *principal* is no longer a traditional CI *runner*, and the audit and *scoping* requirements have to be adjusted to the new reality.

:::userstory
**Story.**
As **DevOps / SRE** and **AppSec**, I want the AI agents that operate the pipeline to receive credentials via ephemeral *workload identity* (OIDC) with per-tool *scopes* and TTL ≤ 1h, and each *tool invocation* to generate a structured *audit event*, so that auditability, revocability and *least privilege* equivalent to classic CI runners are ensured.

**Acceptance criteria (BDD).**
- **Given** that an AI agent is going to operate in the pipeline at level A1+
  **When** it authenticates to invoke a *tool* (e.g. `gh pr create`, `kubectl apply`, `npm publish`)
  **Then** it receives credentials via OIDC with the minimum `scope` declared in the *mandate* ([`REQ-AGN-001`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)), TTL ≤ 1h, without reuse of human identity
- **Given** that the agent invokes a destructive *tool* (`destructive`/`external` in the *allowlist*)
  **When** it operates at level A2+
  **Then** it emits an *intent event* ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) before the invocation, and the *tool call* generates a complete *audit event*
- **Given** that the *kill-switch* ([`REQ-AGN-003`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) is triggered
  **When** credential revocation occurs
  **Then** the agent's credentials become invalid within seconds and the session is terminated
- **Given** that there is a divergence between the declared `intent` and the actual action
  **When** the divergence is detected
  **Then** the signal lands as an IR incident (Ch. 12) and the *mandate* is reviewed

**Checklist.**
- [ ] Dedicated *workload* identity per agent and per environment (no reuse of human credentials and no cross-env)
- [ ] *Scopes* declared in the *mandate* applied in the infra (not only in the document) — e.g. `gh:pr:write` but not `gh:repo:delete`
- [ ] Credential TTL ≤ 1h; no *long-lived* keys (cross-link with US-04)
- [ ] *Audit event* per *tool invocation* with `timestamp`, `agent_id`, `session_id`, `mandate_ref`, `autonomy_level`, `tool`, `tool_version`, `args` (PII redacted), `intent_event_ref`, `outcome`, `external_effect`
- [ ] Operational *kill-switch*: credential revocation + runtime termination + namespace isolation + on-call alert
- [ ] *Kill-switch* exercised in sandbox/staging at a cadence according to autonomy level (quarterly A3, monthly A4)
- [ ] *Secret scanning* + *diff review* of the *skill files* / *agent files* / *rules* that direct the agent (cross-link Policy 15 §2)

:::

**🧾 Artefacts & evidence.**
- OIDC / *workload identity* configuration (IaC) per agent and environment
- Record of `mandate_ref` in the audit *trail* of each *tool invocation*
- Structured *logs* of *intent events* + *tool invocation audit events*
- *Log* of the *kill-switch* exercise (timestamp + stopwatch + outcome)
- Evidence of *secret scanning* of prompts/skills (cross-link Policy 15)

**⚖️ Proportionality.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes for A1+ | OIDC mandatory; A2+ typically outside production |
| L2 | Yes for A1+ | OIDC + full audit + *intent events* at A2+; *kill-switch* exercised quarterly at A3 |
| L3 | Yes for A1+ | OIDC + full audit + *intent events* at A2+ + *kill-switch* exercised monthly at A4; independent `appsec` review |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Agent onboarding | Activation of the *mandate* (Policy 38) | `devops` + `appsec` | Before the first *tool call* |
| Operation | Each *tool invocation* | Agent (with automatic audit) | *Real-time* |
| Review | `review_cadence` of the *mandate* | `appsec` | According to cadence |

**Useful links.**
- 🔗 [`REQ-AGN-*` catalogue (Ch. 02)](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)
- 🔗 [`ARC-015` — agent as *principal* (Ch. 04)](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)
- 🔗 [US-04 — Secrets management (inherited pattern)](#us-04---gestão-de-segredos)
- 🔗 [Policy 18 — Secrets Management (agents annex)](/sbd-toe/assets/policies/policy-gestao-segredos)
- 🔗 [Policy 38 — AI Agent Mandates](/sbd-toe/assets/policies/policy-mandates-agentes)

---

### US-20 - Enterprise identity in the SCM and signing of commits/tags {#us-20}

Whoever writes to the repository must be identifiable, authorised and non-repudiable.  

**Context.** `CIC-001` requires pipelines as code subject to review and `CIC-002` restricts *triggers* to authorised sources (protected *branches*, signed *tags*, approved *merges*). Without granular write access anchored in enterprise identity (SSO/RBAC) and without cryptographic signing of *commits*/*tags*, the *branch* protection of US-01 protects the flow but does not guarantee **who** originated it — and *trigger* authorisation by *tag* loses value if the *tag* is not verifiable.  

:::userstory
**Story.**   
As **DevOps / SRE** and **AppSec Engineers**, I want write access to the SCM to be granular per *branch*/project through enterprise identity (SSO/RBAC), and L3 applications to require verified signing of *commits* and *tags*, so that minimum authorisation and non-repudiation at the origin of the pipeline are ensured.  

**Acceptance criteria (BDD).**  
- **Given** that a collaborator needs to write to a protected *branch*  
  **When** access is granted  
  **Then** it is mediated by SSO/RBAC with minimum scope per *branch*/project, without shared accounts or excessive inherited permissions.  
- **Given** that an application is L3  
  **When** a *commit* or *tag* enters the promotion flow  
  **Then** the signature is verified and, on failure, the *trigger* is refused and recorded.  
- **Given** that a *trigger* is fired by a *tag*  
  **When** the *tag* is not signed by an authorised identity  
  **Then** the execution is blocked as an untrusted source.  

**Checklist.**  
- [ ] Granular write access per *branch*/project via SSO/RBAC  
- [ ] No shared accounts or *long-lived* personal *tokens* for writing  
- [ ] Signing of *commits*/*tags* verified at L3  
- [ ] Signature failure refuses the *trigger* and generates a record  

:::

**🧾 Artefacts & evidence.** SCM RBAC matrix; SSO configuration; *branch protection* policy; signature verification records; logs of refused *triggers*.  

**⚖️ Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Enterprise identity in the SCM; basic RBAC per project | Granular RBAC per *branch*; signing of *tags* recommended | Granular RBAC + signing of *commits* **and** *tags* mandatory and verified in the pipeline |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Onboarding/offboarding | Granting or revocation of SCM access | `devops` + `appsec` | On access change |
| Promotion | Each *trigger* by *commit*/*tag* | Pipeline (automatic verification) | *Real-time* |
| Review | Periodic access audit | `grc` | Half-yearly |

**Useful links.**  
- 🔗 [`CIC-001`/`CIC-002` catalogue (Ch. 07)](/sbd-toe/sbd-manual/cicd-seguro/addon/catalogo-requisitos-cicd)  
- 🔗 [Secure Pipeline Design](/sbd-toe/sbd-manual/cicd-seguro/addon/design-seguro-pipelines)  
- 🔗 [US-01 — Secure source code management](#us-01---gestão-segura-de-código-fonte)

---

### US-21 - CI/CD separation, build/test/deploy and versioned templates {#us-21}

Each phase of the pipeline has its own privileges; crossing them invites escalation.  

**Context.** `CIC-008` requires distinct *jobs* for *build*, *test* and *deploy*, without cross-permissions and with credential scope per *stage*. The checklist adds the functional separation between **CI** and **CD** and the reuse of **versioned pipeline templates**. US-02 ensures the pipeline as versioned code, but does not impose the privilege boundary between phases — a *test* *job* with *deploy* credentials nullifies the separation in practice.  

:::userstory
**Story.**   
As **DevOps / SRE**, I want pipelines with CI and CD separated by function, *build*/*test*/*deploy* phases in distinct *jobs* without cross-permissions, and reusable versioned *templates*, so that the *blast radius* of each phase is limited and the effective configuration is auditable.  

**Acceptance criteria (BDD).**  
- **Given** that a *build* or *test* *job* is executed  
  **When** it requires credentials  
  **Then** it receives only the scope of its phase, without access to *deploy*/production credentials.  
- **Given** that the pipeline reuses common logic  
  **When** that logic is changed  
  **Then** it lives in a versioned *template* under PR, and the effective configuration of the execution is recorded as evidence.  
- **Given** that there is a promotion phase (CD)  
  **When** it is triggered  
  **Then** it is separated from the integration flow (CI) by function and identity, without inherited permissions between the two.  

**Checklist.**  
- [ ] CI and CD separated by function and identity  
- [ ] Distinct *jobs* for *build*, *test* and *deploy*  
- [ ] Credential scope per *stage* documented and *enforced*  
- [ ] Reusable pipeline *templates* versioned under PR  

:::

**🧾 Artefacts & evidence.** Pipeline definition with separate *stages*; versioned *templates*; credential matrix per *stage*; record of the effective configuration; execution logs per phase.  

**⚖️ Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Logically distinct phases; versioned *templates* | Separate CI/CD + credential scope per *stage* | Reinforced separation with dedicated identities per *stage* and verified absence of cross-permissions |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Creation/refactoring | Change to the pipeline structure | `devops` | In the PR |
| Review | Change to *templates* or *stage* credentials | `appsec` + `devops` | In the PR |
| Audit | Periodic review of permissions per *stage* | `grc` | Half-yearly |

**Useful links.**  
- 🔗 [`CIC-008` catalogue (Ch. 07)](/sbd-toe/sbd-manual/cicd-seguro/addon/catalogo-requisitos-cicd)  
- 🔗 [Secure Pipeline Design](/sbd-toe/sbd-manual/cicd-seguro/addon/design-seguro-pipelines)  
- 🔗 [US-02 — Secure pipeline design](#us-02---design-seguro-dos-pipelines-versionamento-determinismo-e-revisão)

---

### US-22 - Protection against privilege escalation in runners {#us-22}

A *job* with access to the Docker socket has effective control of the *host*.  

**Context.** `CIC-010` (L3) requires strong *runner* isolation — ephemeral *containers* or disposable VMs — **without access to the Docker socket** by non-privileged *jobs*, without privilege-escalation capabilities and with logs of blocked attempts. US-05 (*runner* isolation) covers ephemerality and segmentation, but does not make explicit the prohibition of *privesc* or the evidence of blocking, which the checklist treats as a control in its own right.  

:::userstory
**Story.**   
As **DevOps / SRE**, I want *runners* not to expose the Docker socket to non-privileged *jobs* nor to allow privilege escalation, with blocked attempts recorded, so that compromise of the *host* from a pipeline *job* is prevented.  

**Acceptance criteria (BDD).**  
- **Given** that a non-privileged *job* is executed  
  **When** it attempts to access the Docker socket or privileged capabilities  
  **Then** access is denied and the attempt is recorded.  
- **Given** that an application is L3  
  **When** the *runner* is provisioned  
  **Then** it runs in strong isolation (ephemeral *container* or disposable VM) without *privesc* capabilities.  
- **Given** that an escalation attempt occurs  
  **When** it is detected  
  **Then** it generates auditable evidence and an alert for response.  

**Checklist.**  
- [ ] No access to the Docker socket by non-privileged *jobs*  
- [ ] No privilege-escalation capabilities on the *runners*  
- [ ] Strong isolation (ephemeral/disposable) at L3  
- [ ] Logs of blocked attempts available  

:::

**🧾 Artefacts & evidence.** *Runner* configuration (no exposed socket); capability/`securityContext` policies; logs of blocked attempts; evidence of ephemerality.  

**⚖️ Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Baseline *hardening*; no unnecessary privileges | Segregated *runners* with no socket exposed to non-privileged *jobs* | Strong isolation (ephemeral/disposable) + prohibition of *privesc* + verified blocking logs |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Provisioning | Creation/change of *runners* | `devops` | In the infra PR |
| Operation | Privileged access attempt | *Runner* (automatic detection) | *Real-time* |
| Review | *Runner* configuration audit | `appsec` | Half-yearly |

**Useful links.**  
- 🔗 [`CIC-006`/`CIC-010` catalogue (Ch. 07)](/sbd-toe/sbd-manual/cicd-seguro/addon/catalogo-requisitos-cicd)  
- 🔗 [Runner Isolation and Protection](/sbd-toe/sbd-manual/cicd-seguro/addon/isolamento-runners)  
- 🔗 [US-05 — Runner isolation](#us-05---isolamento-de-runners)

---

### US-23 - Artefact custody, exception visibility and external integrations {#us-23}

What is stored, where it travels and what connects to the pipeline is all attack surface.  

**Context.** Three prescriptions converge at the pipeline boundary: `CIC-007` requires secure storage and transport of artefacts with verifiable provenance and tamper detection; the checklist requires that **exceptions** to controls be **visibly flagged** in the pipeline (not only recorded — US-10); and `intro` treats any external system (scanners, *registries*, services) as a **supply chain dependency** and a potential exfiltration channel. US-06 covers signature/provenance, but not secure custody or minimised external integration.  

:::userstory
**Story.**   
As **DevOps / SRE** and **AppSec Engineers**, I want artefacts stored and transported securely with tamper detection, exceptions visibly flagged in the pipeline, and external integrations treated as supply chain dependencies with minimised context, so that integrity across the delivery chain is preserved and silent exfiltration is prevented.  

**Acceptance criteria (BDD).**  
- **Given** that a signed artefact is stored or transported  
  **When** it is consumed downstream  
  **Then** integrity is verified and tampering is detected before promotion.  
- **Given** that a *gate* is subject to an exception (bypass)  
  **When** the pipeline executes  
  **Then** the exception is visibly flagged in the execution, in addition to being formally recorded.  
- **Given** that the pipeline integrates an external service  
  **When** it is configured  
  **Then** it is treated as a dependency (provenance/trust assessed) and receives only the minimum context necessary.  

**Checklist.**  
- [ ] Secure artefact storage/transport with tamper detection  
- [ ] Integrity/provenance verification before promotion  
- [ ] Exceptions to *gates* visibly flagged in the pipeline execution  
- [ ] External integrations treated as dependencies with minimum context  

:::

**🧾 Artefacts & evidence.** *Artifact store* configuration (access/transport control); integrity verification records; exception flagging in the execution logs/UI; inventory of external integrations and their respective context scope.  

**⚖️ Proportionality.**  
| L1 | L2 | L3 |
|----|----|----|
| Controlled storage; exception recorded | Secure transport + tamper detection + exception flagged in the execution | Reinforced custody + mandatory downstream verification + audited external integrations and minimised context |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Build/Promotion | Production and consumption of artefacts | `devops` | On every promotion |
| Operation | Recording/application of an exception to a *gate* | `appsec` + `grc` | On the exception request |
| Integration | Addition/change of an external service | `devops` + `appsec` | In the integration PR |

**Useful links.**  
- 🔗 [`CIC-007` catalogue (Ch. 07)](/sbd-toe/sbd-manual/cicd-seguro/addon/catalogo-requisitos-cicd)  
- 🔗 [Artefact Integrity and Provenance](/sbd-toe/sbd-manual/cicd-seguro/addon/integridade-proveniencia)  
- 🔗 [Exceptions and Visibility in CI/CD](/sbd-toe/sbd-manual/cicd-seguro/addon/controle-excecoes-visibilidade)  
- 🔗 [US-06 — Signature and provenance](#us-06---assinatura-e-proveniência)  
- 🔗 [US-10 — Exception management (controlled bypass)](#us-10---gestão-de-exceções-bypass-controlado)

---

## 📦 Expected Artefacts {#-artefactos-esperados}

Each practice leaves technical footprints. Without them, there is no proof of compliance:

| Artefact / Evidence                              | Owner                         | Notes |
|---------------------------------------------------|------------------------------|------------|
| `ci-pipeline.yml`                                 | Developers                   | Versioned via PR (US-01, US-02) |
| Record of effective configuration (without secrets)     | DevOps / SRE                 | Supports reproducibility (US-02, US-14) |
| Published gate/threshold rules              | AppSec Engineers             | Signal/decision separation (US-07, US-15) |
| Logs + *exit codes* + execution artefacts       | DevOps / SRE                 | Empirical evidence (US-03, US-16) |
| Signatures + provenance                         | DevOps / SRE                 | Verification before promotion (US-06) |
| Validator reports (SAST, secrets, etc.)    | Developers / AppSec Engineers| Always linked to real execution (US-03, US-16) |
| SBOM per build                                     | AppSec Engineers             | Attached to the artefact (US-08) |
| Exception register (TTL, compensations, approvals) | GRC / Compliance             | Bypass governance (US-10) |
| Correlated commit→pipeline→release logs        | DevOps / SRE                 | Auditable traceability (US-09) |
| Log hygiene policy and evidence            | DevOps / SRE                 | Context minimisation (US-17) |
| Named promotion/deploy records               | DevOps / SRE                 | Non-repudiation (US-18) |
| Metrics and events dashboard                     | Executive Management / CISO      | Organisational visibility (US-12) |

---

## ⚖️ L1–L3 proportionality matrix {#️-matriz-de-proporcionalidade-l1l3}

Not all apps require the same level of rigour.  
The matrix ensures that effort is proportional to risk **without ever compromising**: human decision, empirical evidence and traceability.

| Category           | L1 (low)                        | L2 (medium)                                 | L3 (critical) |
|--------------------|-----------------------------------|--------------------------------------------|--------------|
| Branches/PR         | 1 reviewer + build check          | Reviewer + security validation           | ≥2 reviewers + code owners + AppSec |
| Determinism        | Sufficient logging                 | Reproducibility as a requirement            | Reproducibility + reinforced audit |
| Signal vs decision    | Named approval for production    | Named approval + segregation of duties    | Named approval + reinforced control + audit |
| Empirical evidence  | Basic logs + key artefacts    | Logs + *exit codes* + reinforced retention    | Full evidence + immutable export (when required) |
| Scanners            | SAST + SCA + secrets + SBOM (+ images, if any) | + IaC                                        | + extended coverage |
| Secrets            | Masking + secure storage     | OIDC preferred + controlled TTL             | OIDC mandatory + short TTL + frequent rotation |
| Runners             | Shared with hardening          | Segregated per project                       | Ephemeral + network segmentation + automatic destruction |
| Artefacts          | Hash verified before promotion + rejection on failure; signing recommended | Signing + mandatory verification        | Automatic blocking on failure + reinforced provenance |
| Exceptions            | Simple record                    | Dual approval + TTL                         | Dual approval + frequent review + audit |
| Traceability     | Logs 30 days                       | Logs 90 days + commit-build correlation        | ≥1 year + immutable export + dashboards |
| DAST                | Periodic manual                   | In pre-release staging                       | Continuous + automatic blocking |
| Metrics            | Manual reports                 | Daily dashboard                              | Near real time + alerts |

---

## 🏁 Final Recommendations {#-recomendações-finais}

Pipeline security is not optional: it is the **trust mechanism** of all continuous delivery.

- **Version and review the pipeline as code** - and require sufficient determinism for audit.  
- **Define binary, governable gates** - and never confuse automatic signals with decisions.  
- **Require empirical evidence** - logs, *exit codes* and artefacts, not just reports.  
- **Protect secrets and minimise context** - the pipeline is a privileged exfiltration point.  
- **Assign ownership to irreversible actions** - promotions without an owner are a structural risk.  
- **Control exceptions with TTL and compensations** - bypass only exists when it is governed.

A secure CI/CD is the silent guarantor that everything reaching production is **intact, verifiable, traceable and owned by real responsible parties**.
