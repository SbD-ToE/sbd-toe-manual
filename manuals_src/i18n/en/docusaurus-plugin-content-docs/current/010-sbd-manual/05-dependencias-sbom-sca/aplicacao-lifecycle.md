---
id: aplicacao-lifecycle
title: How to Do It
description: Practical integration of the dependency management, SBOM generation and SCA execution prescriptions throughout the application lifecycle
tags: [tipo:aplicacao, ciclo-vida, dependencias, sbom, sca, supply-chain, governance]
genia: us-format-normalization
translation:
  source_locale: pt
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/aplicacao-lifecycle.md
  source_sha256: 838568365bfc022d8c9a988d97bbb4fc8db080406552ce25cf0f9da9054080a7
  source_commit: 810e8083697d2705d15e9913f01ca8634db01cd4
  target_sha256: 306b6b8183cbe91931180b896b6e4b27ec96128f6092e9d21d991ed5ceed2e63
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [avaliacao, chapter_role, como_fazer, cra_pde, cycle_iteration, eu_startups, framework_source_corpus, lifecycle_phase, mcp, papel_suporte, practitioner_manual, provenance, spdx_license_list, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 89835127121febfa7f22d2e5d73221c4e6b128713d2606b31a491997dc8d0822
  translated_at: 2026-09-27T15:09:24Z
  stamped_at: 2026-09-27T15:09:24Z
  reviewed_by: null
---

# Applying in the Lifecycle - Dependencies, SBOM and SCA

## 🧭 When to apply {#-quando-aplicar}

The practices accompany the application from kick-off to *post‑release*.  
Each event is a **trigger** that must produce objective evidence.

| SDLC Phase / Event | Expected action | Artefact/Evidence |
|--------------------|---------------|---------------------|
| Project start  | Publish the policy and configure internal repositories | Policy document + `repo-config.yaml` |
| New dependency   | Review origin, licence, maintenance and CVEs | Approval ticket + record |
| Build / CI         | Generate the SBOM and run SCA with *gates* | `sbom.*` + `sca-report.*` + logs |
| Release            | Review findings/exceptions and decide *go/no-go* | `releases.md` + `excecoes.yaml` |
| Regular cycle      | **Bots** open update PRs with **impact assessment** | Automatic PRs + tests/logs |
| Public critical CVE| Impact analysis + *backport/fix* | Response issue + mitigation plan |

---

## 👥 Who carries out each action {#-quem-executa-cada-ação}

Governance is **collective** - roles and responsibilities consistent with intro.md.

| Role | Responsibility |
|------|-------------------|
| **Developer / Lead** | Include dependencies, initial triage, *pinning*, fixes |
| **AppSec Engineer** | Policies, *gate* *tuning*, exception and risk management |
| **DevOps / CI/CD** | SBOM, SCA, internal repositories, update bots and *impact analysis* |
| **QA** | Evidence, regression tests, validation of bot PRs |
| **Product Owner** | *Go/no-go* decision and acceptance of residual risk |
| **GRC / Management** | Audit, compliance, evidence retention |

---

## 📖 Reusable User Stories {#-user-stories-reutilizáveis}

Each US turns the prescription into an actionable backlog, with **context, scientific rationale, BDD/checklist, artefacts, L1–L3 proportionality and integration into the SDLC**.

---

### US-01 - Secure dependency management {#us-01---gestão-de-dependências-seguras}

**Context.**  
External dependencies without validation introduce invisible risk (abandoned components, dubious origin, incompatible licences).

:::userstory
**Story.**   
As a **Developer**, I want to **use only approved dependencies**, so that **the risk of inherited vulnerabilities and licence conflicts is reduced**.

**Acceptance criteria (BDD).**
- **Given** that I intend to include a dependency
  **When** I submit an approval request
  **Then** the dependency is validated according to the policy (origin, licence, maintenance, CVEs)

**Checklist.**
- [ ] Dependency formally approved  
- [ ] Licence validated / compatible  
- [ ] No known critical CVEs  
- [ ] Provenance confirmed (internal repository)

:::

**Artefacts & evidence.**
- `dependencies-approval.md`  
- Validation ticket in the backlog

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Simplified approval |
| L2 | Yes | Formal validation + licence |
| L3 | Yes | AppSec review + provenance

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Design/Dev | Inclusion of a dependency | Developer + AppSec | At dependency approval |

**Useful links.**  
- [Governance pillars](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro#pilares-de-governação)

---

### US-02 - SBOM in every build {#us-02---sbom-em-cada-build}

**Context.**  
Without an up-to-date SBOM it is not possible to quickly determine exposure to CVEs and meet audit requirements.

:::userstory
**Story.**   
As **DevOps / SRE**, I want to **generate an SBOM in every build**, so that there is **complete component traceability**.

**Acceptance criteria (BDD).**
- **Given** that a build is triggered
  **When** the artefact is produced
  **Then** an SBOM is generated in CycloneDX or SPDX format

- **Given** a generated SBOM
- **When** it is associated with the release
- **Then** it is stored and accessible for audit

**Checklist.**
- [ ] SBOM in CycloneDX or SPDX format  
- [ ] SBOM versioned and associated with the release  
- [ ] Accessible for audit

:::

**Artefacts & evidence.**
- `sbom.json` / `sbom.xml`

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Basic SBOM |
| L2 | Yes | Complete SBOM, included in the release |
| L3 | Yes | Signed SBOM + integrity verification

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| CI | Build execution | DevOps | According to the US cycle |

**Useful links.**  
- [SBOM - CycloneDX and SPDX standards](https://www.cyclonedx.org)
- [US-10 - Inventory and SBOM per Build](#us-10---inventário-e-sbom-por-build)

---

### US-03 - Automatic SCA with *gates* {#us-03---sca-automático-com-gates}

**Context.**  
SCA identifies known vulnerabilities in dependencies (direct and transitive) and must block unacceptable risk.

:::userstory
**Story.**   
As an **AppSec Engineer**, I want to **run automatic SCA in the pipelines**, so that **CVEs are detected before production**.

**Acceptance criteria (BDD).**
- **Given** a build
  **When** the SBOM is generated
  **Then** the SCA runs and **blocks** findings that exceed the threshold per Lx

**Checklist.**
- [ ] SCA scanner integrated (e.g. Dependency‑Check/Trivy/Grype)  
- [ ] Findings documented and triaged  
- [ ] Automatic blocking for critical CVEs (L2) and medium+ (L3)

:::

**Artefacts & evidence.**
- `sca-report.html` / JSON
- Pipeline logs with *gates*

**Proportionality by risk.**
| Level | Policy |
|---|---|
| L1 | Block High/Critical |
| L2 | Block High/Critical |
| L3 | Block Medium+

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| CI | Generation of the SBOM | DevOps + AppSec | During the build (immediate blocking) |

**Useful links.**  
- [Threshold guide per L1–L3](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#matriz-de-proporcionalidade-l1l3)

---

### US-04 - Formal and temporary CVE exceptions {#us-04---exceções-a-cves-formais-e-temporárias}

**Context.**  
Not all findings can be resolved immediately; exceptions must be **formal, justified and temporary**.

:::userstory
**Story.**   
As an **AppSec Engineer**, I want to **formalise CVE exceptions**, so that **governance is maintained and residual risk is justified**.

**Acceptance criteria (BDD).**
- **Given** that there is an unresolved CVE
  **When** an exception is requested
  **Then** the exception is formalised in `excecoes.yaml` with technical and business justification, approver and deadline

- **Given** an exception with a defined deadline
- **When** the deadline passes
- **Then** a periodic review with risk reassessment is triggered

**Checklist.**
- [ ] `excecoes.yaml` with technical and business justification  
- [ ] Approver and deadline defined  
- [ ] Compensating control specified  
- [ ] Periodic review scheduled

:::

**Artefacts & evidence.**
- `excecoes.yaml` (versioned)
- Approval recorded in the backlog

> **Reference:** This US implements [Ch. 14-US-01: Formal exception process]
> in the context of vulnerabilities in dependencies (CVEs). The approval process, TTL and revalidation must follow the master exception policy in Ch. 14.

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Formal record with justification, compensating control, approver and deadline |
| L2 | Yes | Revalidation at expiry (TTL of Policy 05 §7: 60 days Low/Medium, 30 days High) |
| L3 | Yes | Executive validation + risk metrics

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Release | Pending findings | AppSec + Product Owner | According to the deadline defined in the exception |

**Useful links.**  
- [Exceptions and Risk Acceptance for Vulnerabilities](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/excecoes-e-aceitacao-risco)

---

### US-05 - Release validation (*go/no-go*) {#us-05---validação-de-release-gono-go}

**Context.**  
Each release is a risk decision that must be **explicit and traceable**.

:::userstory
**Story.**   
As a **Product Owner**, I want to **validate findings and exceptions before go‑live**, so that I can **make an informed *go/no-go* decision**.

**Acceptance criteria (BDD).**
- **Given** a release candidate
  **When** I check the security criteria and residual risk
  **Then** I document the decision and any conditions (if they exist)

**Checklist.**
- [ ] List of findings and status  
- [ ] Approved and valid exceptions  
- [ ] *Go/no-go* decision documented

:::

**Artefacts & evidence.**
- `releases.md` with history and justifications

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Simple decision |
| L2 | Yes | Formal review |
| L3 | Yes | Formal review + AppSec involved

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Pre‑release | RC ready | Product Owner + QA + AppSec | Before deploy to production |

**Useful links.**  
<!-- genia_suggest: Criar addon/10-checklist-release-segura.md com checklist de validação de release por L1-L3 -->
- [Expected artefacts](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#-artefactos-esperados)

---

### US-06 - Internal repositories as the single source {#us-06---repositórios-internos-como-fonte-única}

**Context.**  
Without internal repositories, dependencies may be resolved from uncontrolled sources (*typosquatting*, *confusion*, malice).

:::userstory
**Story.**   
As **DevOps / SRE**, I want to ***enforce* approved internal repositories**, so that **provenance and consistency are guaranteed**.

**Acceptance criteria (BDD).**
- **Given** that the *package manager* resolves dependencies
  **When** the build takes place
  **Then** it only accepts sources from the approved internal repository

**Checklist.**
- [ ] `repo-config.yaml` active (internal proxy/registry)  
- [ ] Blocking of external sources (allowlist)  
- [ ] Access logs monitored and retained

:::

**Artefacts & evidence.**
- `repo-config.yaml`  
- CI/CD logs with validated origin

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Recommended |
| L2 | Yes | Mandatory |
| L3 | Yes | Mandatory + package signature/verification

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Build | Dependency resolution | DevOps/CI | Immediate (real-time blocking) |

**Useful links.**  
- SLSA Provenance (concepts)

---

### US-07 - Prohibit manually copied libraries {#us-07---proibir-bibliotecas-copiadas-manualmente}

**Context.**  
JS, PHP, DLLs and JARs copied directly into the repo escape the SBOM and the SCA, creating *shadow dependencies*.

:::userstory
**Story.**   
As a **Developer**, I want to **use only *package managers*/internal repositories**, **never** copying libraries into the repo.

**Acceptance criteria (BDD).**
- **Given** that I need an external library
  **When** I add it to the project
  **Then** it is managed via a *package manager* and **not** by manual copying

**Checklist.**
- [ ] Zero manually copied libs  
- [ ] All via *package manager*  
- [ ] Periodic audit confirms absence

:::

**Artefacts & evidence.**
- `package.json` / `pom.xml` / `composer.json`  
- Build logs (resolution via internal repos)

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Documented policy |
| L2 | Yes | Periodic audits |
| L3 | Yes | Automatic enforcement in CI/CD

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Dev | Inclusion of a new lib | Developer + AppSec | At dependency approval |

**Useful links.**  
<!-- genia_suggest: Criar addon/11-bibliotecas-locais-migracao.md com padrões de migração por stack (npm, maven, composer, etc) -->
- [Third-Party Library Governance](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/governanca-libs-terceiros)

---

### US-08 - Update automation with impact assessment {#us-08---automação-da-atualização-com-avaliação-de-impacto}

**Context.**  
Dependencies degrade over time; they need to be updated **safely and quickly**.  
Modern tools assess **impact** (semver, *release notes*, *diffs*, test coverage) and:
- **open automatic PRs** with *auto‑merge* when the change is safe (*patch/minor* with no impact, green tests, *gates* OK);
- **mark as requires‑human** when there is impact (broken API, *major*), attaching *refactor* *guidelines*.

:::userstory
**Story.**   
As **DevOps/Developer**, I want **update bots with impact assessment**, so that I **receive safe PRs automatically and a human *handoff* when necessary**.

**Acceptance criteria (BDD).**
- **Given** that a new version is published
  **When** the bot runs **impact analysis**
- Then:
  - If **no‑impact** ⇒ PR with **auto‑merge** conditional on green CI and *gates* OK  
  - If **impact** ⇒ **requires‑human** PR with *diff*, *breaking notes*, *refactor hints*, or even *GenAI with the appropriate change*.

**Checklist.**
- [ ] Bot active (Renovate/Dependabot/similar)  
- [ ] **Impact analysis** configured (semver + tests + changelog)  
- [ ] **Safe auto‑merge** criteria per L1–L3  
- [ ] Labels (`no-impact`, `requires-human`) and *routing* to reviewers  
- [ ] *Canary/rollout* defined (L3)

:::

**Artefacts & evidence.**
- Automatic PRs with labels and logs  
- CI/CD test and *gate* reports

**Proportionality by risk.**
| Level | Policy |
|---|---|
| L1 | Optional bots; *auto‑PR* for *patch/minor* |
| L2 | Mandatory bots; *auto‑merge* only for *patch* or security updates, with all mandatory *gates* green, a traceable record and declared in the policy; *minor/major* requires human review |
| L3 | Mandatory bots; *impact analysis* + *canary*; no *auto‑merge*: *patch* and security updates with human review (expedited for CVEs, Policy 13 §4.1); *minor/major* requires human approval and staged promotion |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Dev/CI | New version published | DevOps + Developer + QA | Automatic (PR opened and processed by a bot) |

**Useful links.**  
- [Automatic Updates Policy](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/politica-atualizacoes)
- [CI/CD Integration](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/integracao-ci-cd)

---

### US-09 - Periodic Audit of Manually Copied Libraries {#us-09---auditoria-periódica-de-bibliotecas-copiadas-manualmente}

**Context.**  
Manually copied libraries escape the SBOM and the SCA. **Periodic automation** is needed to detect these hidden dependencies and ***enforce* replacement** via a package manager or blocking in CI/CD.

:::userstory
**Story.**   
As an **AppSec Engineer**, I want to **run an automated periodic audit** to detect manually copied libraries (JS, PHP, DLL, JAR, etc.), so that **their use is blocked in CI/CD and a complete SBOM and SCA are guaranteed**.

**Acceptance criteria (BDD).**
- **Given** that a periodic audit is run (weekly/monthly according to Lx)
  **When** copied libraries not managed via a package manager are found
  **Then** an issue is created in the backlog with a deadline for replacement via the repository/package manager

**Checklist.**
- [ ] Automatic scanner configured (e.g. search for patterns of copied libs, JS/PHP/DLL/JAR extensions)
- [ ] Audit frequency defined per Lx (L1: monthly, L2: fortnightly, L3: weekly)
- [ ] Results versioned in the repository (`.audit-libs.json`)
- [ ] Blocking in CI/CD for L2–L3 when copied libs are detected
- [ ] Zero libs detected as the target

:::

**Artefacts & evidence.**
- `.audit-libs.json` / `.audit-libs.yaml` (versioned)
- Audit and scanner logs
- Remediation issues in the backlog

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Yes | Documented policy; monthly manual audit |
| L2 | Yes | Fortnightly automatic scanner; alert in the pipeline |
| L3 | Yes | Weekly automatic scanner; blocking in CI/CD |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Regular cycle | Periodic audit (schedule) | AppSec Engineer + DevOps | L1: monthly, L2: fortnightly, L3: weekly |
| Build | Detection in CI/CD (L2–L3) | DevOps (blocking) | Immediate (real-time blocking) |
| Backlog | Detected libs | Developer (remediation)

**Useful links.**  
- [US-07 - Prohibit manually copied libraries](#us-07---proibir-bibliotecas-copiadas-manualmente)
<!-- genia_suggest: Criar addon/12-padroes-deteccao-libs.md com padrões regex e ferramentas por stack (npm, Python, Java, PHP, etc) -->
- [Third-Party Library Governance](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/governanca-libs-terceiros)

---

### US-10 - Inventory and SBOM per Build {#us-10---inventário-e-sbom-por-build}

**Context.**  
Each build must produce a signed and traceable **Software Bill of Materials (SBOM)**, identifying all the dependencies used (direct and transitive).  
This SBOM must be able to be **correlated with the deployed artefact** and serve as the basis for detecting deviations (“drift”) between what was built and what is actually running.

:::userstory
**Story.**  
As **DevOps / SRE**, I want to automatically generate a **signed SBOM per build**, which remains associated with each deployed image, package or artefact, making it possible to identify all components and their versions.

**Acceptance criteria (BDD).**
- **Given** a build pipeline  
  **When** the artefact is produced  
  **Then** a signed **CycloneDX or SPDX SBOM** is generated and archived with commit, version and hash metadata.  
  
- **Given** an SBOM signed at build time  
  **When** the service is deployed to `stage` or `prod`  
  **Then** the orchestrator maintains **provenance labels** (commit, build-id, image) that associate each instance with the correct SBOM. 

- **Given** runtime telemetry  
  **When** a loaded component that does not exist in the SBOM is detected  
  **Then** a **drift incident** is opened with a required fix.  

- **Given** an audit or compliance request  
  **When** the auditor requests the component inventory  
  **Then** it is possible to export the SBOM and provenance per version.

**Checklist.**
- [ ] SBOM generated per build (SPDX or CycloneDX standard).  
- [ ] Signature and secure storage of the SBOM.  
- [ ] Deploy provenance (attestations and labels per environment).  
- [ ] Runtime vs SBOM comparison and drift detection.  
- [ ] Export of the inventory to a CMDB or compliance data lake.  
- [ ] Integration with vulnerability alerts and with Ch. 12 (Monitoring and Operations).

:::

**Artefacts & evidence.**  
`sbom-<build>.json`, `attestation-<build>.json`, `proveniencia-<deploy>.json`, drift reports and build logs.

**Proportionality.**
| Level | Mandatory? | Coverage |
|---|---:|---|
| L1 | Yes | SBOM per build and basic association per image. |
| L2 | Yes | Attestations + labels per environment, basic drift detection. |
| L3 | Yes | Continuous drift + blocking of non-attested executions. |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| CI | Build execution | DevOps / SRE | At build time (automatic generation) |
| Deploy | Deployment to an environment | DevOps / SRE | Immediate (association with metadata) |
| Operations | Continuous monitoring | DevOps + AppSec | Continuous (drift detection) |

**Useful links.**
- [SLSA Provenance - Concepts and Implementation](https://slsa.dev)
- [Inventory and SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/inventario-sbom)
- [US-11 - Vulnerability Alerts](#us-11---alertas-sobre-vulnerabilidades-em-componentes-usados)

---

### US-11 - Alerts on Vulnerabilities in Components in Use {#us-11---alertas-sobre-vulnerabilidades-em-componentes-usados}

**Context.**  
Systems must **automatically detect known vulnerabilities (CVEs)** in the dependencies used.  
Besides the alerts during the build, there must be **alerts in production**, correlating the versions actually deployed and the environments where they are.  
The system must know **where each version runs** in order to assess real impact and prioritise remediation.

:::userstory
**Story.**  
As **Application Manager** and **AppSec**, I want to **receive alerts correlated by environment** when a CVE emerges that affects running versions, so that I can prioritise the fix and reduce the MTTR.

**Acceptance criteria (BDD).**
- **Given** an inventory per service/environment with an associated SBOM  
  **When** a CVE is published that affects a deployed version  
  **Then** a **single alert** is generated with component, version, impacted services/environments, *exploitability*, exposure and recommended SLA.  
- **Given** an alert with an L2/L3 SLA  
  **When** the triage time passes without action  
  **Then** it is **escalated automatically** (Ch. 12) and an incident is created in the ITSM system.  
- **Given** an accepted risk exception (VEX/justification)  
  **When** an *active exploit* comes to exist  
  **Then** the exception is reassessed and the alert reactivated.  
- **Given** the patch management lifecycle  
  **When** the fix is deployed  
  **Then** the alert is closed automatically and recorded as a *resolved CVE*.  

**Checklist.**
- [ ] Continuous inventory per service and environment with an associated SBOM.  
- [ ] Correlation of CVEs and advisories to deployed versions.  
- [ ] Risk enrichment (exploit available, exposure, sensitive data).  
- [ ] Integration with Ch. 12 (SIEM/SOAR/alerting) and ITSM (incidents/tasks).  
- [ ] Exception process with VEX and automatic reassessment.  
- [ ] KPIs: MTTA/MTTR per severity and environment; % inventory coverage vs deploys.

:::

**Artefacts & evidence.**  
Signed `sbom-<build>.json`; `inventario-runtime-<servico>-<ambiente>.json`; feed of correlated CVEs; tickets/incidents; VEX decisions.

**Proportionality.**
| Level | Mandatory? | Triage SLA | Mitigation SLA | Adjustments |
|---|---:|---:|---:|---|
| L1 | Yes | Critical ≤ 24 h; High ≤ 48 h; Medium 5 working days; Low 10 working days | Critical 30 days | Alert only on deployed *high/critical* without compensating measures. |
| L2 | Yes | Critical ≤ 24 h; High ≤ 48 h; Medium 5 working days; Low 10 working days | Critical 7 days | Include *medium* in exposed services; automatic escalation. |
| L3 | Yes | Critical ≤ 24 h; High ≤ 48 h; Medium 5 working days; Low 10 working days | Critical 3 days | *Blockers* with auto-rollback/kill-switch where applicable. |

> These SLAs are the Manual's choice. A vulnerability with an indication of active exploitation in a product with digital elements that the organisation places on the market leaves this ladder: triage ≤4 h and, if confirmed, the CRA Article 14 track (early warning notification ≤24 h to the CSIRT designated as coordinator and to ENISA).

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| CVE publication | New public vulnerability | Automatic (feed) | Automatic detection (1–6h) |
| Triage | CVE correlated with a deployed version | AppSec + DevOps | L1: 5d, L2: 2d, L3: 1d |
| Mitigation | Remediation plan or exception | DevOps + AppSec | Critical: L1 30d, L2 7d, L3 3d (Policy 19 §4.3) |

**Useful links.**
- [US-02 - SBOM in every build](#us-02---sbom-em-cada-build)
- [US-10 - Inventory and SBOM per Build](#us-10---inventário-e-sbom-por-build)
- [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle)


---

### US-12 - Automatic Validation of Licence Compatibility {#us-12---validação-automática-de-compatibilidade-de-licenças}

**Context.**  
Dependencies with incompatible licences (GPL, AGPL, etc.) may introduce unexpected legal obligations. It is necessary to **automatically validate compatibility** against an organisational allowlist.

:::userstory
**Story.**   
As a **Developer**, I want to **automatically validate the licence compatibility** of new dependencies, so that **legal compliance is guaranteed and conflicts are avoided**.

**Acceptance criteria (BDD).**
- **Given** that a new dependency is added
  **When** the build runs
  **Then** a licence validator assesses compatibility against the organisational allowlist

- **Given** that a licence is incompatible
- **When** the build tries to resolve the dependency
- **Then** the pipeline blocks with a clear message (L2–L3) or warns (L1)

**Checklist.**
- [ ] Allowlist of approved licences defined (e.g. MIT, Apache 2.0, BSD)
- [ ] Automatic licence validator integrated into the CI/CD
- [ ] Blocking for prohibited/incompatible licences (L2–L3)
- [ ] Alert for unrecognised licences (for manual review)
- [ ] Documentation of the approval criterion per licence

:::

**Artefacts & evidence.**
- `licenses-whitelist.yaml` / `.licenseignore` (versioned)
- CI/CD logs with licence validation
- Remediation issues (swap the dependency or request a formal exception)

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Manual, ad hoc validation |
| L2 | Yes | Automatic with alert; blocking for GPL/AGPL |
| L3 | Yes | Automatic with blocking; exceptions require formal approval |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Design/Dev | Inclusion of a dependency | Developer | At dependency approval |
| Build | Dependency resolution | CI/CD (blocking/alert) | During the build (immediate) |
| Exception | Licence incompatible with the business case | AppSec + Legal (if necessary) | Before go-live |

**Useful links.**  
- [US-01 - Secure dependency management](#us-01---gestão-de-dependências-seguras)
- [SPDX License List](https://spdx.org/licenses/)

---

### US-13 - Inventory and control of emergent dependencies {#us-13---inventário-e-controlo-de-dependências-emergentes}

**Context.**  
In modern architectures, not all dependencies enter through explicit declaration in manifests or lockfiles. Build tools, pipelines, code generation, plugins and runtime loading can introduce **emergent dependencies** that are not immediately visible.

:::userstory
**Story.**  
As **Software Architects + AppSec Engineer**, I want to identify and control emergent dependencies (not explicitly declared), so that the real composition of the software remains governed, traceable and aligned with the security requirements.

**Acceptance criteria (BDD).**
- **Given** that an SBOM is generated for the application or pipeline  
  **When** I compare the current composition with the known baseline  
  **Then** I can identify new, unexpected or out-of-boundary dependencies

**Checklist.**
- [ ] Inventory boundary (SBOM boundary) defined and documented
- [ ] Dependency sources identified (build tools, plugins, pipelines, runtime fetch)
- [ ] Dependency baseline approved and versioned
- [ ] Dependency *delta* detection implemented
- [ ] Emergent dependencies subject to review/approval
- [ ] Evidence archived per release

:::

**Artefacts & evidence.**
- `sbom-boundary.md`
- `sbom-baseline.json`
- Dependency *delta* report per build/release

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Optional | Occasional manual analysis |
| L2 | Yes | Automatic *delta* detection |
| L3 | Yes | Automatic *gate* + formal approval |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| CI/CD | Build / Release | DevOps + AppSec | At each release |

**Useful links.**
- 🔗 Ch. 04 - Secure Architecture: `/sbd-manual/arquitetura-segura/intro`
- 🔗 Ch. 07 - Secure CI/CD: `/sbd-manual/cicd-seguro/intro`

---

### US-14 - AI BOM and management of AI model *providers* {#us-14}

**Context.**
US-10 covers the classic SBOM — packages via a *package manager*, direct and transitive dependencies. When the system includes **AI components** (models, datasets, MCP servers/tools, embedded prompts), there is a class of "dependencies" that escapes the traditional *package manager*: opaque artefacts with their own version, external *providers* (Anthropic, OpenAI, HuggingFace), and update mechanisms that can change behaviour without changing the visible version. [`DEP-011`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011), [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012), [`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013) and [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) are operationalised here so that these dependencies become as auditable as the rest of the *stack*.

:::userstory
**Story.**
As **AppSec / DevOps**, I want each *release* of the system to generate an **AI BOM in a standardised format** (preferably CycloneDX 1.6 `ml-bom`) with models, datasets, MCP servers/tools and embedded prompts *pinned* to specific versions, aligned with the list of approved *providers*, so that there is traceability equivalent to that of the classic SBOM and rapid detection of *upstream* incidents in any of the classes.

**Acceptance criteria (BDD).**
- **Given** a system *build* with AI components
  **When** the pipeline generates the SBOM
  **Then** the **AI BOM** is also generated in `ml-bom` format (CycloneDX 1.6) or equivalent, integrated with the main SBOM
- **Given** an AI model in operational use
  **When** declared in the AI BOM
  **Then** it comes **with an explicit fixed version** (e.g. `claude-opus-4-7@sha:…`) — no `latest`, no ranges, no dynamic aliases
- **Given** that an AI *provider* changes the model's major version
  **When** the *pinning* is updated
  **Then** a new *eval suite* runs (Ch. 10 §C5) and the *threat model* is reviewed (Ch. 03 US-11) before the *cutover*
- **Given** that an AI *provider* is **not** on the approved list
  **When** an attempt is made to use it in production code
  **Then** the CI *gate* blocks (cross-link Ch. 07 US-19) or requires a formal exception

**Checklist.**
- [ ] AI BOM generated per *build* in a standardised format (preference: CycloneDX 1.6 `ml-bom`)
- [ ] Models, datasets, MCP servers/tools, prompts with *pinned* version + hash + *provider*
- [ ] List of approved AI *providers* versioned in VCS, with risk classification
- [ ] Applicable contractual clauses recorded per *provider* (cross-link Ch. 14, Policy 33)
- [ ] CI *gate* that fails if: (a) the AI BOM was not generated, (b) a component uses `latest`/range, (c) the *provider* is not on the approved list
- [ ] `DEP-007` triage process extended to incidents in models/datasets/MCP/prompts (`AML.T0010`, `AML.T0019`, `AML.T0109`, `AML.T0110`, LLM03-2025)
- [ ] *Eval suite* + *threat model* run at each major version change

**Artefacts & evidence.**
- `ai-bom.cdx.json` (CycloneDX 1.6) or equivalent per *release*, archived and linked to the main SBOM
- List of approved *providers* in VCS (`governance/ai-providers.yaml` or equivalent)
- CI *gate* *logs* confirming AI BOM compliance
- Eval/threat-review record per version change (references `eval_run_id` and `threat_model_ref`)
- History of pinned versions per model, with date and SHA

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Recommended | AI BOM in a simple format; known list of providers |
| L2 | Yes | AI BOM in a standard format; approved *providers*; CI *gate* |
| L3 | Yes | Standard AI BOM + GRC review of the *providers*; detailed contractual clauses (data retention, audit rights, location); cross-link with the AI Act cross-check |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Build | Each *build* | DevOps (generates the AI BOM) + AppSec (reviews) | Per *build* |
| Provider approval | Addition of a new AI *provider* | AppSec + GRC (+ Legal if necessary) | Before operational use |
| Version change | *Bump* of model / MCP server / dataset | AppSec + DevOps | Before the *cutover* — with *eval* and *threat review* completed |

**Useful links.**
- 🔗 [`DEP-011..014` — AI inventory and supply chain](./addon/catalogo-requisitos-dependencias#dep-011)
- 🔗 [Policy 39 — AI BOM and Supply Chain](/sbd-toe/assets/policies/policy-ai-bom-supply-chain)
- 🔗 [Policy 10 — Dependencies (AI providers annex)](/sbd-toe/assets/policies/policy-dependencias)
- 🔗 [Policy 11 — SBOM (AI BOM annex)](/sbd-toe/assets/policies/policy-sbom)
- 🔗 [Ch. 14 — Contracting of AI providers](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle)
- 🔗 [AI Act cross-check](/sbd-toe/cross-check-normativo/ai-act/intro)

---

### US-15 - Version pinning and hash integrity {#us-15---pinning-de-versões-e-integridade-por-hash}

A dependency without a fixed version and without a verifiable hash is an open door to silent substitution in the supply chain.  

**Context.** `DEP-003` requires a versioned *lockfile*, with no `latest`/`*` references or unbounded ranges, and integrity verifiable by hash (`integrity` in npm, `--hash` in pip). No US operationalises this control directly — US-01 addresses approval and US-13 addresses the inventory *delta*, but *pinning* and hash verification were left without a backlog of their own. Without a fixed version, the same manifest resolves different artefacts between builds; without a hash, an artefact tampered with *upstream* (typosquatting, compromised *registry*) goes unnoticed.  

:::userstory
**Story.**   
As a **Developer/Lead**, I want to **pin all dependencies to exact versions and verify their integrity by hash at each resolution**, so that **builds are reproducible and unauthorised substitution of artefacts is blocked**.  

**Acceptance criteria (BDD).**  
- **Given** a dependency manifest  
  **When** the build resolves the dependencies  
  **Then** there is a *lockfile* versioned in VCS with no `latest`/`*`/unbounded ranges, and the build fails if the *lockfile* is missing or out of date  
- **Given** a *lockfile* with integrity hashes  
  **When** the *package manager* downloads an artefact  
  **Then** the downloaded hash is compared with the *pinned* hash and resolution aborts in case of divergence  

**Checklist.**  
- [ ] *Lockfile* present and versioned, regenerated deterministically  
- [ ] Absence of `latest`/`*`/unbounded ranges (verifiable by a *linter* in CI)  
- [ ] Hash integrity field present and validated at resolution  
- [ ] CI *gate* that fails on a missing/out-of-date *lockfile* or hash divergence  

:::

**Artefacts & evidence.** `package-lock.json`/`poetry.lock`/`Gemfile.lock`/`go.sum` (versioned); *pinning* *linter* report; CI logs with hash verification.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| *Lockfile* mandatory, no `latest`/`*`/unbounded ranges, + hash verification | Mandatory *lockfile* + hash verification | *Lockfile* + hash + verified provenance (*attestation*) and blocking *gate* |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Dev | Inclusion/change of a dependency | Developer/Lead | On change of the manifest |
| Build | Dependency resolution | DevOps/CI | During the build (immediate blocking) |

**Useful links.** [DEP-003 — Fixed and auditable versions](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias)

---

### US-16 - Documented governance of severity policy, registries and approval record {#us-16---governação-documentada-de-política-de-severidade-registries-e-registo-de-aprovação}

Supply chain controls are only auditable when the rule that distinguishes blocking from alerting, the permitted origin and the record of who approved what are written down and versioned.  

**Context.** Three prescriptions of the catalogue were only partially operationalised. `DEP-002` requires a **documented severity policy** that distinguishes findings that block from those that only alert (US-03 applies *gates* but does not require the written policy). `DEP-005` requires an enforced *allowlist* of *registries* **with a controlled and audited fallback to external sources** (US-06 enforces the *allowlist* but does not address the *fallback*). `DEP-006` requires a traceable approval record **with version, hash, owner and date** (US-01 approves but does not fix the fields of the record). They are consolidated because they are all documented governance artefacts that make the existing *gates* auditable.  

:::userstory
**Story.**   
As an **AppSec Engineer**, I want to **keep versioned the severity policy, the *allowlist* of *registries* with an audited *fallback* rule and the approval record with mandatory fields**, so that **supply chain decisions are explicit, traceable and auditable**.  

**Acceptance criteria (BDD).**  
- **Given** the SCA pipeline  
  **When** a finding is assessed  
  **Then** the block-vs-alert decision follows a documented and versioned severity policy, and not *ad hoc* scanner criteria  
- **Given** that the build resolves dependencies from a source outside the *allowlist*  
  **When** a *fallback* to an external *registry* occurs  
  **Then** the event is recorded, audited and subject to approval according to the policy, or blocked  
- **Given** the approval of a new dependency  
  **When** it is recorded  
  **Then** the record includes version, hash, owner and date, and is traceable per dependency  

**Checklist.**  
- [ ] Severity policy documented and versioned (block/alert thresholds per Lx)  
- [ ] *Allowlist* of *registries* enforced with an explicit and audited *fallback* rule  
- [ ] Approval record with version, hash, owner and date per dependency  
- [ ] Audit evidence of *fallback* events (logs retained)  

:::

**Artefacts & evidence.** `severity-policy.yaml`; `repo-config.yaml` with *fallback* rule; `dependencies-approval.md` with version/hash/owner/date fields; audited *fallback* logs.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Minimum severity policy documented; recommended *registries*; simple approval | Versioned policy; *allowlist* enforced + audited *fallback*; record with mandatory fields | Same + AppSec/GRC review of the *fallback* and of the record; *fallback* requires formal approval per event |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Project start | Publication/review of the policy | AppSec + GRC | On adoption and at periodic review |
| Build | *Fallback* to an external *registry* | AppSec + DevOps | On the event (immediate recording/audit) |
| Dev | Approval of a new dependency | AppSec + Developer | At dependency approval |

**Useful links.** [DEP-002/005/006 — Requirements Catalogue](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias) · [Control of origin registries](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/controle-registos-origem)

---

## 🧩 Complementary note - Continuous component inventory and alerts in production {#-nota-complementar---inventário-contínuo-de-componentes-e-alertas-em-produção}

Dependency management does not end at the build.  
There must be a **continuous inventory of third-party components** per project and environment (dev/test/stage/prod), with **automatic alerts** when vulnerabilities affecting deployed versions are published.  

This complements the SCA in the pipeline by:  
- Closing the *build → deploy → run* cycle;  
- Prioritising by real risk (exposure and exploitability);  
- Triggering an operational response via Ch. 12 (Monitoring and Operations).

**Recommended practice.**
1. Generate the SBOM at build time and sign it.  
2. Label per environment in the registry/orchestrator.  
3. Continuous discovery at runtime (inventory per deploy) and comparison with the SBOM.  
4. Correlation of CVEs and alerts when: deployed version affected / active exploit / critical path.  
5. Automatic opening of an incident/task with an SLA proportional to L1–L3.  
6. Evidence: SBOM, inventory, alerts, VEX, patching history.

**Integration with Ch. 12 - Monitoring and Operations.**

User stories 10 and 11 are closely related to what is set out in **Ch. 12 - Monitoring and Operations.**, highlighting the critical aspect of monitoring beyond the execution of any build pipeline. It is easy to implement security measures during the build, but, once in production, an application may go a long period of time without returning to the development pipeline, so it is essential to review the SBOM of applications in production periodically, or spontaneously. A new vulnerability being found in an application in production is more serious than during the development process, especially without alarm or periodic detection measures.
One of the fundamental aspects in **Ch. 12 - Monitoring and Operations.** is precisely that control, defining:

- Events: alert creation/closure, change in exploitability, SLA breach, drift.  
- Metrics: MTTA, MTTR, affected assets, % active exceptions, *patch latency*.  
- Automation: enrichment, prioritisation, escalation, SOAR playbooks.  
- Executive reporting: Ch. 05 + Ch. 12 compliance, view per L1–L3.

---
## 📦 Expected artefacts {#-artefactos-esperados}

| Artefact | Evidence |
|-----------|-----------|
| `dependencies-approval.md` | Approved list of dependencies |
| `sbom.json` / `sbom.xml` | Inventory per build (CycloneDX/SPDX) |
| `attestation-<build>.json` | Build provenance and signature |
| `inventario-runtime-<servico>-<ambiente>.json` | Inventory of components actually deployed |
| `sca-report.html/json` | Detected vulnerabilities and applied *gates* |
| `cve-alerts.json` | Alerts correlated by environment and severity |
| `vex.yaml` | Justified exceptions and reassessment status |
| `excecoes.yaml` | Approved formal exceptions |
| `releases.md` | *Go/no-go* decisions and *patching* history |
| `repo-config.yaml` | Configured internal repositories |
| `.audit-libs.json` / `.audit-libs.yaml` | Periodic audit results for copied libs |
| `licenses-whitelist.yaml` | Allowlist of approved licences |
| **Bot PRs** | Impact *labels*, logs and tests |
| **Drift reports** | Differences between SBOM and runtime |
| **ITSM tickets / Incidents** | Evidence of CVE handling and SLA met |

---

## ⚖️ L1–L3 proportionality matrix {#matriz-de-proporcionalidade-l1l3}

| Practice | L1 | L2 | L3 |
|---------|----|----|----|
| SBOM | Basic per build | Complete per release | Signed + integrity + provenance |
| Runtime inventory | Recommended | Mandatory | Continuous + *drift* detection |
| SCA | Block High/Critical | Block High/Critical | Block Medium+ + active CVE feed |
| Alerts for deployed CVEs | Manual, with triage within the SLA by severity | Automatic per environment | Automatic + correlation and escalation |
| Version pinning | Mandatory (*lockfile* + hash) | Mandatory | Mandatory + provenance validation |
| Exceptions / VEX | Formal (justification, compensating control, approver and deadline) | Formal + periodic review | Formal + automatic revalidation |
| Internal repository | Recommended | Mandatory | Mandatory + signature and *provenance attestation* |
| Copied libraries | Prohibited (policy) | Periodic audit | CI/CD enforcement + blocking |
| Audit of copied libs | Documented policy; monthly | Automatic scanner; fortnightly | Automatic scanner; weekly + CI/CD blocking |
| Licence validation | Manual, ad hoc | Automatic with alert | Automatic with blocking (except formal exceptions) |
| Bots / patching automation | Optional | Active + *auto-merge* only for *patch*/security with green *gates*, a traceable record and declared in the policy; *minor/major* with human review | Active + *impact analysis*, *canary* and rollback |
| Integration with Ch. 12 | Optional | Basic SIEM alerts | Full: SOAR, MTTR/MTTA metrics and escalation |

---

## 🏁 Final recommendations {#-recomendações-finais}

- The **SBOM** must be treated as a living document, with signature and verifiable provenance per build and per environment.  
- **Continuous inventory** in production is essential: it detects *drift* and vulnerabilities in versions actually deployed.  
- **Automated SCA** with *gates* proportional to risk and integration with CVE alerts at runtime.  
- **Internal repositories** and *attestations* are the foundation of trust in the supply chain.  
- **Formal and temporary exceptions** (VEX) must be reassessed automatically when the risk changes or an *active exploit* emerges.  
- **Eliminate manually copied libraries** (US-07) with an **automated periodic audit** (US-09) and blocking in CI/CD for L2–L3.  
- **Validate licence compatibility** (US-12) against an allowlist, blocking or alerting according to criticality.  
- **Bots with impact assessment** (US-08):  
  - PRs for *trivial patches* → *auto-merge*;  
  - PRs with impact → human review, *canary* and staged promotion (especially in L3).  
- **Integration with Ch. 12** must guarantee full visibility, real-time alerts and operational response metrics (MTTA/MTTR) per severity and environment.

