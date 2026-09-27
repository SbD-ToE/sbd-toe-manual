---
id: aplicacao-lifecycle
title: How to Do It
description: Practical integration of continuous validation practices across the different phases of the application lifecycle
tags: [tipo:aplicacao, ciclo-vida, testes, seguranca, integracao, validacao]
genia: us-format-normalization
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/aplicacao-lifecycle.md
  source_sha256: 81214fa795470ee1b6ff8e353399d9c4311e5cd24b2b094a3ecbdd85f01a1e67
  source_commit: 036d74010f423f247be988e4a417375c74edb9d9
  target_sha256: 69fdd59ddb9a98ba09e718d9dfd924af56a3876888ddd4e55fb3e8181724781d
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [audit_trail, avaliacao, candidate, chapter_role, como_fazer, cycle_iteration, deterministic, framework_source_corpus, gap_family, lifecycle_phase, mapping, maturity, mcp_reading_programa, oracle, papel_suporte, practitioner_manual, programme_line, risk_level, role_tech_lead, sbdtoe_sbd, traceability, transversal, validation_evaluation]
  glossary_sha256: 2ef62e6832b405cb282ff0bf137e48289f24be2502c02c91f2166c43fb4cfc32
  translated_at: 2026-09-27T07:53:51Z
  stamped_at: 2026-09-27T07:53:51Z
  reviewed_by: null
---

# Applying Security Testing Throughout the Lifecycle

## 🧭 When to apply {#-quando-aplicar}

Security testing accompanies the application in every phase - it is not a final step, but a **continuous rhythm** of validation.  
From the initial definition of requirements to the final audit, every moment of the lifecycle must generate **objective evidence** that the application is protected against known flaws and emerging threats.  

| SDLC Phase / Event | Testing action | Artefact/Evidence |
|--------------------|----------------|---------------------|
| Specification      | Define testable security requirements and acceptance criteria | Requirements matrix + Test plan |
| Development    | Run SAST and linters; create regression tests | SAST reports + regressions |
| Pull request       | Run automatic SAST with inline comments | CI logs + SARIF |
| Build / CI         | Run SCA, SAST, IAST (where applicable), generate SBOM | Pipeline logs + SBOM |
| Staging            | Run authenticated DAST and fuzzing of critical endpoints | DAST reports + fuzzing |
| Pre-release        | Validate release criteria and manage exceptions | Release checklist |
| Post-release        | Continuous fuzzing / IAST; dynamic monitoring | Alerts + reports |
| Audit          | Carry out risk-based offensive PenTesting | PenTest technical report |

---

## 👥 Who carries out each action {#-quem-executa-cada-ação}

Responsibility for the quality of testing is **collective**.  
Each role contributes a unique perspective, but only together is a robust and auditable validation process obtained.  

| Role | Responsibility |
|-------|------------------|
| **Developer** | Fix findings, create automated regressions |
| **QA** | Run DAST, fuzzing, validate criteria |
| **AppSec Engineer** | Define strategy, *tune* rules, manage findings and exceptions |
| **DevOps / SRE** | Integrate scanners, gates and evidence into CI/CD |
| **Product Owner** | Approve residual risk and decide *go/no-go* |
| **AppSec Engineer** | Offensively validate controls and report impact |

---

## 📖 Reusable User Stories {#-user-stories-reutilizáveis}

The following stories turn principles into practice.  
Each US represents an **essential control**, designed to be integrated directly into the team's backlog and applied in proportion to the application's risk (L1–L3).  

---

### US-01 - Formal testing strategy per application {#us-01---estratégia-formal-de-testes-por-aplicação}

Validation begins with planning.  
Without a clear strategy, coverage becomes uneven and impossible to audit.  

**Context.**  
Without a strategy, coverage is uneven and difficult to audit.

:::userstory
**Story.**   
As an **AppSec Engineer**, I want **to define a security testing strategy per application**, so that **coverage proportional to risk and traceability to the requirements of Ch. 02 are assured**.

**Acceptance criteria (BDD).**  
- **Given** that the application has criticality Lx  
  **When** I define the strategy  
  **Then** the test types and gates are established per L1–L3 and linked to requirements

**Checklist.**  
- [ ] Versioned strategy document  
- [ ] Minimum coverage per L1–L3 defined  
- [ ] Mapping Ch. 2 ⇄ tests published  

:::

**Artefacts & evidence.** `strategy-testing.md` document, requirements⇄tests matrix.  

**Proportionality by risk.**  
| Level | Mandatory? | Minimum coverage |
|---|---|---|
| L1 | Yes | SAST + checklist |
| L2 | Yes | + authenticated DAST |
| L3 | Yes | + fuzzing/IAST + PenTest |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Planning | Lx classification / kick-off | AppSec Engineer | By the end of the 1st sprint |

---

### US-02 - Mandatory SAST on Pull Request {#us-02---sast-obrigatório-em-pull-request}

Detecting early is always cheaper.  
Running SAST at PR time ensures that vulnerabilities never reach the main *branch*.  

**Context.**  
PRs without SAST allow vulnerabilities to enter the codebase early.

:::userstory
**Story.**   
As a **Developer**, I want **to run automatic SAST on the PR with inline comments**, so that **vulnerabilities are fixed before the merge**.

**Acceptance criteria (BDD).**  
- **Given** that I open a PR  
  **When** the pipeline runs SAST  
  **Then** results appear inline and block above the defined threshold  

**Checklist.**  
- [ ] Trigger on PR active  
- [ ] SARIF report attached  
- [ ] Threshold per Lx applied  

:::

**Artefacts & evidence.** CI logs + SARIF.  

**Proportionality by risk.**  
| Level | Gate policy |
|---|---|
| L1 | Warning |
| L2 | Blocking on High/Critical |
| L3 | Blocking on Medium+ |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Code review | PR opened | Developer + DevOps / SRE | Before the merge |

---

### US-03 - Authenticated DAST in Staging {#us-03---dast-autenticado-em-staging}

Many critical flaws only reveal themselves after login.  
Running authenticated DAST in staging is the natural step before promoting a release.  

**Context.**  
Many flaws only surface when authenticated.

:::userstory
**Story.**   
As a **QA** role, I want **to run authenticated DAST in staging**, so that **vulnerabilities exploitable at runtime are detected**.

**Acceptance criteria (BDD).**  
- **Given** a configured staging environment  
  **When** I run authenticated DAST  
  **Then** reports are generated and findings opened in the backlog  

**Checklist.**  
- [ ] Login flow configured  
- [ ] Scope defined  
- [ ] Report attached to the release  

:::

**Artefacts & evidence.** DAST reports.  

**Proportionality by risk.**  
| Level | Coverage |
|---|---|
| L1 | Manual/exploratory |
| L2 | Automated authenticated |
| L3 | Automated + extended coverage |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Staging | Build/Deploy to staging | QA | Before release approval |

---

### US-04 - Security gates in CI/CD {#us-04---gates-de-segurança-no-cicd}

Without gates, findings become mere ignored reports.  
Automatic gates are the barrier that stops serious regressions from moving forward.  

**Context.**  
Without gates, findings do not prevent regressions.

:::userstory
**Story.**   
As a **DevOps / SRE**, I want **to integrate automatic gates into the pipeline (SAST/SCA/IAST) with thresholds per Lx**, so that **insecure builds are avoided**.

**Acceptance criteria (BDD).**  
- **Given** a running pipeline  
  **When** a finding exceeds the Lx threshold  
  **Then** the job fails and promotion is blocked until a fix or an approved exception  

**Checklist.**  
- [ ] Versioned pipelines with declared gates  
- [ ] Thresholds per Lx published  
- [ ] Logs exported  
- [ ] Exceptions approved (L3: dual approval)  

:::

**Artefacts & evidence.** `ci.yml` configuration, reports and exception register.  

**Proportionality by risk.**  
| Level | Policy |
|---|---|
| L1 | Warning |
| L2 | Blocking on High/Critical |
| L3 | Blocking on Medium+ |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| CI/CD | Pipeline run | DevOps / SRE + AppSec Engineer | On every build |

**Traceability details (expanded):**  
- Logs of every run with timestamp, commit, branch, tools executed, thresholds applied  
- Report of approved exceptions (JSON file with PR, justification, approver, expiry date)  
- Gate metrics: % of blocks by severity, override rate, mean time to remediation  
- Prometheus/Grafana dashboard with historical series of blocked vs allowed findings  
- Integration with the backlog for automatic opening of issues for blocked findings  

---

### US-05 - Automated security regressions {#us-05---regressões-de-segurança-automatizadas}

Fixing is not enough - it is necessary to ensure that the same flaw does not return.  
Automated regression tests turn every fix into future protection.  

**Context.**  
Fixed flaws come back without automated regression.

:::userstory
**Story.**   
As a **Developer**, I want **to create regression tests for fixed findings**, so that **future reintroduction is avoided**.

**Acceptance criteria (BDD).**  
- **Given** a resolved finding  
  **When** I create the regression test  
  **Then** it fails if the vulnerability returns  

**Checklist.**  
- [ ] Test created and versioned  
- [ ] Link to the original finding (ID)  
- [ ] Execution in future builds  

:::

**Artefacts & evidence.** Regression code + CI logs.  

**Proportionality by risk.**  
| Level | Requirement |
|---|---|
| L1 | Critical cases |
| L2 | Per known flaw |
| L3 | Mandatory coverage |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Dev/CI | Finding closed | Developer | In the fix PR |

---

### US-06 - Fuzzing targeted at critical APIs {#us-06---fuzzing-dirigido-a-apis-críticas}

Conventional tests do not capture every flaw.  
Fuzzing, by exploring unexpected inputs, reveals vulnerabilities invisible to the naked eye.  

**Context.**  
Complex inputs reveal uncovered flaws.

:::userstory
**Story.**   
As a **QA** role, I want **to apply fuzzing to critical endpoints**, so that **flaws invisible to conventional tests are detected**.

**Acceptance criteria (BDD).**  
- **Given** defined critical endpoints  
  **When** I run fuzzing  
  **Then** anomalies are recorded with a minimal PoC  

**Checklist.**  
- [ ] Targets and profiles defined  
- [ ] Isolated test environment  
- [ ] Report with reproducible cases  

:::

**Artefacts & evidence.** Fuzzing report + corpora.  

**Proportionality by risk.**  
| Level | Coverage |
|---|---|
| L1 | Optional |
| L2 | Priority endpoints |
| L3 | Critical endpoints mandatory |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Staging | Release candidate | QA | Before go-live |

---

### US-07 - Release criteria and risk acceptance {#us-07---critérios-de-release-e-aceitação-de-risco}

Every release is also a risk decision.  
Formalising criteria and explicitly accepting residual risk is part of governance.  

**Context.**  
Releases without clear criteria dilute responsibility.

:::userstory
**Story.**   
As a **Product Owner**, I want **to establish security acceptance criteria per release and a residual-risk acceptance process**, so that **go/no-go decisions are informed**.

**Acceptance criteria (BDD).**  
- **Given** a release that is ready  
  **When** I check criteria and findings  
  **Then** I approve, delay or grant an exception with a deadline and compensations  

**Checklist.**  
- [ ] Checklist completed  
- [ ] Critical findings: 0 or formal exception  
- [ ] Risk justification recorded  

:::

**Artefacts & evidence.** Release checklist + exception register.  

**Proportionality by risk.**  
| Level | Policy |
|---|---|
| L1 | Simple checklist |
| L2 | Blocking on High/Critical |
| L3 | No critical without a formal exception |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Pre-release | Release candidate | Executive Management + AppSec Engineer | By D-1 before go-live |

**Release Checklist Template (L3):**  

```markdown
## 📋 Checklist de Release - v{VERSION}

**Release:** v2.3.0  
**Data planeada:** YYYY-MM-DD  
**Owner:** Product Manager X, AppSec Engineer Y  

| Critério | Status | Evidência | Observação |
|---|---|---|---|
| **Findings Críticos** | ✅ ZERO | Screenshot dashboard | Aceite se mitigação documentada |
| **SAST Thresholds** | ✅ OK | Build log #4521 | Bloqueio High/Critical não acionado |
| **DAST Cobertura** | ✅ 85% | Relatório DAST | Meta L3 = 80%+ |
| **Fuzzing endpoints críticos** | ✅ Completo | Log fuzzer noturno | 3 findings Low resolvidos |
| **Regressões** | ✅ PASS | CI #4521 | Nenhuma regressão detetada |
| **PenTest (se L3)** | ⚠️ Em curso | Relatório preliminar | Conclusão em +5d |
| **SCA cobertura** | ✅ 100% | SBOM + scanning | 0 CVE não mitigadas |
| **Documentação segurança** | ✅ Atualizada | Wiki link | Ameaças, controlos, mitigações |
| **Aprovação formal risco** | ⏳ Pendente | - | Aguarda AppSec + Produto |

**Risco residual aceite:**  
- [X] 1 CVE Medium em dependência com patch disponível, mas adquirido em PR separado (até 2025-12-31)  
- [X] Endpoint POST /admin/users sem DAST (acesso VPN, compensado por network policy)  

**Aprovações:**  
- AppSec Engineer Y - aprovado em YYYY-MM-DD  
- Product Manager X - aprovado em YYYY-MM-DD  
```

---

### US-08 - Risk-based offensive PenTesting {#us-08---pentesting-ofensivo-baseado-em-risco}

Automation is fundamental, but not sufficient.  
The offensive human eye identifies attack chains that scanners never simulate.  

**Context.**  
Human validation complements automation.

:::userstory
**Story.**   
As an **AppSec Engineer**, I want **to offensively validate the effectiveness of controls**, so that **exploitable flaws are detected before production**.

**Acceptance criteria (BDD).**  
- **Given** a risk-based scope  
  **When** I run a PenTest  
  **Then** I issue a report with vectors, impact and recommendations  

**Checklist.**  
- [ ] scope defined and consent  
- [ ] Report with PoCs and severity  
- [ ] Retest planned for criticals  

:::

**Artefacts & evidence.** PenTest technical report + evidence.  

**Proportionality by risk.**  
| Level | Requirement |
|---|---|
| L1 | Not applicable |
| L2 | Annual + after a significant architectural change (Policy 36) |
| L3 | Annual + before the first production release + major release (Policy 36) |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Audit / Pre-production | Audit window or critical L3 | AppSec Engineer | Report before go-live |

---

### US-09 - IAST with Instrumentation in Staging {#us-09---iast-com-instrumentação-em-staging}

DAST validates externally, but IAST offers internal visibility of unsanitised flows, insecure calls and misuse of libraries.  
Essential for L2/L3 of high criticality.  

**Context.**  
DAST validates externally, but IAST offers internal visibility.

:::userstory
**Story.**   
As a **QA + AppSec Engineer**, I want **to instrument the application in staging with IAST to observe insecure calls in real time during tests**, so that **findings are correlated with real execution context and false positives are reduced**.

**Acceptance criteria (BDD).**  
- **Given** that an application is instrumented with an IAST agent in staging  
  **When** functional or automated tests are run  
  **Then** findings are captured with full visibility of the stack (function, line, parameter, value)  

- **Given** an observed IAST finding  
- **When** it is correlated with DAST/SAST  
- **Then** the result is prioritised as critical/high if confirmed in multiple layers  

**Checklist.**  
- [ ] IAST agent installed and configured in staging  
- [ ] Instrumentation coverage of critical endpoints validated  
- [ ] Application performance monitored (`<10%` overhead accepted)  
- [ ] IAST findings exported in structured format  
- [ ] Integration with a centralised findings tool (DefectDojo or similar)  
- [ ] Sensitive data masked in IAST logs  
- [ ] Retest after fixing critical findings scheduled  

:::

**Artefacts & evidence.** IAST agent configuration (versioned YAML/HCL), IAST reports (JSON/XML), performance logs, SAST↔DAST↔IAST correlation dashboard, coverage metrics.  

**Proportionality by risk.**  
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | No | Optional, investigative |
| L2 | Recommended | On critical endpoints (authentication, payment) |
| L3 | Mandatory | Full coverage + correlation with DAST |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Staging | Deploy of release candidate | QA + AppSec Engineer | Before formal approval |

---

### US-10 - Centralised Findings Management with Triage and SLA {#us-10---gestão-centralizada-de-findings-com-triagem-e-sla}

Findings scattered across isolated tools create redundancy, noise and lack of visibility.  
Centralisation with formal triage, SLA and traceability is imperative for governance.  

**Context.**  
Scattered findings create noise and lack of visibility.

:::userstory
**Story.**   
As an **AppSec Engineer + DevOps / SRE**, I want **to centralise all findings from SAST, DAST, IAST, SCA, fuzzing and manual tests in a unified platform with triage by criticality, state and SLA**, so that **complete traceability and effective prioritisation are guaranteed**.

**Acceptance criteria (BDD).**  
- **Given** that findings are produced by multiple tools  
  **When** they are correlated in the centralised platform  
  **Then** duplicates are consolidated and metadata unified (CVE, CWE, CVSS, commit, module)  

- **Given** a triaged finding  
- **When** it obtains a state (Open/Under investigation/Accepted/Fixed/Validated)  
- **Then** an SLA is associated and alerts are triggered if exceeded  

- **Given** a fixed finding  
- **When** validation occurs  
- **Then** it is marked as Closed and fix traceability (commit, release) is recorded  

**Checklist.**  
- [ ] Centralised platform deployed (DefectDojo, Vulcan, Security Hub, etc.)  
- [ ] Connectors for all tools (SAST, DAST, IAST, SCA) configured  
- [ ] Deduplication and correlation rules active  
- [ ] Triage criteria documented (CWE, OWASP, organisational risk)  
- [ ] SLAs defined by severity and Lx (Policy 19 §4.3; e.g. Critical: 30 / 7 / 3 days, High: 90 / 30 / 15 days at L1 / L2 / L3)  
- [ ] Public dashboards with KPIs (open findings, resolution rate, mean time)  
- [ ] Integration with the backlog (Jira/Azure Boards) for automatic assignment  
- [ ] Audit of exceptions with dual approval for L2/L3  

:::

**Artefacts & evidence.** Versioned centralised platform configuration, deduplication rules, findings dashboard, SLA document, state-change logs, monthly KPI reports.  

**Proportionality by risk.**  
| Level | Requirement | Details |
|---|---|---|
| L1 | Simple centralisation | Manual triage, SLA recommended |
| L2 | Centralisation with SLA | Formal states, alerts on exception |
| L3 | Centralisation + audit | Strict SLA, dual approval, monthly report |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Continuous | Production of findings | AppSec Engineer + DevOps / SRE | In real time |

---

### US-11 - Automatic Feedback of Findings to Teams {#us-11---feedback-automático-de-findings-às-equipas}

Findings that are not communicated effectively are ignored.  
Automatic feedback in the channels where developers work reduces friction and speeds up fixing.  

**Context.**  
Findings that are not communicated are ignored.

:::userstory
**Story.**   
As an **AppSec Engineer + DevOps / SRE**, I want **to automate the delivery of findings at the teams' points of contact (PR comments, Slack notifications, IDE dashboards)**, so that **visibility is assured and remediation is accelerated**.

**Acceptance criteria (BDD).**  
- **Given** that SAST detects a vulnerability in a PR  
  **When** the pipeline completes  
  **Then** an inline comment is published on the PR with context (CWE, severity, fix recommendation)  

- **Given** a detected critical finding  
- **When** it is triaged in the centralised platform  
- **Then** an alert is sent to Slack/Teams to the team owner with urgency  

- **Given** a developer at work  
- **When** the IDE integrated with SonarQube/Semgrep is active  
- **Then** warnings appear in real time with fix suggestions  

**Checklist.**  
- [ ] Integration of automatic comments on PRs active (e.g. GitHub Actions, GitLab CI)  
- [ ] Webhooks configured for sending notifications (Slack, Teams, Email)  
- [ ] Severity and context included in every notification  
- [ ] Avoid duplication of notifications (coalescing of alerts)  
- [ ] Public dashboard of findings per project/team  
- [ ] Team satisfaction feedback collected (e.g. "Very useful", "False positive")  
- [ ] Rules adjusted periodically based on feedback (monthly/quarterly)  

:::

**Artefacts & evidence.** Webhook and integration configuration (versioned YAML), PR comment templates, communication dashboard, feedback logs, quarterly effectiveness report.  

**Proportionality by risk.**  
| Level | Channels | Frequency |
|---|---|---|
| L1 | Email/weekly report | Aggregated |
| L2 | PR comments + daily Slack | By severity |
| L3 | PR comments + Slack + IDE + dashboard | Real-time for criticals |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Continuous | Generation/triage of findings | AppSec Engineer + DevOps / SRE | `<15min` for criticals |

---

### US-12 - Assisted Decision for Security Testing Findings {#us-12---decisão-assistida-para-findings-de-testes-de-segurança}

**Context.**  
Testing tools (SAST, DAST, IAST, fuzzing) report hundreds of findings per build, blocking pipelines without context analysis. Without a structured decision framework, teams accept risks "blindly" or bypass gates to meet deadlines, without traceability.

:::userstory
**Story.**   
As an **AppSec Engineer + DevOps / SRE**, I want **a structured decision framework for security testing findings**, so as to separate suggestion (tool) from decision (human), document the rationale with checklist C1 and escalate conflicts between timeline and security.

**Acceptance criteria (BDD).**  
- **Given** that SAST reports a CRITICAL finding (SQL injection)  
  **When** the Developer analyses it with checklist C1 (exploitability, mitigations, remediation, business)  
  **Then** the decision is documented in template T1 (FIX/ACCEPT/SUPPRESS/DEFER) with a traceable justification
- **Given** a HIGH finding in L3  
  **When** DevOps proposes ACCEPT-risk but AppSec disagrees  
  **Then** the conflict is escalated with template T2 to the CISO/Tech Lead, with resolution within a 4h SLA
- **Given** a FIX-IMMEDIATELY decision  
  **When** the fix is applied in a PR  
  **Then** revalidation confirms that the finding has disappeared and no new CRITICAL finding was introduced
- **Given** a decision metric  
  **When** the quarterly review takes place  
  **Then** >95% of CRITICAL/HIGH findings have C1 documented, time-to-decision `<4h`, blocking rate `<10%`

**Checklist.**  
- [ ] Checklist C1 integrated into the findings workflow (4 questions: exploitability, mitigations, remediation, business)
- [ ] Decision template T1 (FIX/ACCEPT/SUPPRESS/DEFER) with mandatory fields (Finding ID, C1 analysis, rationale, implementation, approver)
- [ ] Escalation template T2 for conflicts (Timeline vs. Security, FP disputes, Compensating controls)
- [ ] Decision-maker matrix by severity (CRITICAL/HIGH/MEDIUM/LOW) × level (L1/L2/L3)
- [ ] SLA by severity: 2h analysis CRITICAL (L3), 4h HIGH, 8h MEDIUM, 24h LOW
- [ ] Decision repository in Git (decisoes/DEC-YYYY-MM-DD-XXX.md) linked to the Finding ID
- [ ] KPI dashboard: % of findings documented, time-to-decision, pipeline blocking rate, risk acceptance rate
- [ ] Integration with the centralised platform (DefectDojo/Vulcan) for traceability

:::

**🧾 Artefacts & evidence.**  
- Checklist C1 applied for every CRITICAL/HIGH finding (exploitability, mitigations, remediation, business)
- Template T1 completed for every decision (FIX/ACCEPT/SUPPRESS/DEFER with rationale)
- Escalation template T2 for conflicts documented (Timeline vs. Security, formal resolution)
- Decision-maker matrix defined (who decides by severity × level)
- Git decision repository (decisoes/*.md) with linkage Finding ID → PR → Commit
- Decision KPI dashboard (C1 coverage, time-to-decision, blocking, risk acceptance)
- Escalation logs with timestamps and formal resolution

**⚖️ Proportionality.**  
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Recommended | Simplified checklist for CRITICAL only, no strict SLA |
| L2 | Yes | Checklist C1 mandatory for CRITICAL+HIGH, template T1, decision-makers defined, 4h SLA for HIGH |
| L3 | Yes | Checklist C1 for all findings ≥MEDIUM, template T1+T2, formal escalation, 2h SLA for CRITICAL |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| CI/CD | Tool reports a finding | DevOps / SRE + AppSec Engineer | 2h CRITICAL, 4h HIGH, 8h MEDIUM |
| Deploy | Gate blocked by a finding | DevOps / SRE | Decision with C1 before override |
| Review | Quarterly | GRC / Compliance + AppSec Engineer | KPI analysis (coverage, time-to-decision) |

**Useful links.**  
[Addon 08 - Findings Management](/sbd-toe/sbd-manual/testes-seguranca/addon/gestao-findings)
[Addon 10 - Evidence and Reproducibility](/sbd-toe/sbd-manual/testes-seguranca/addon/evidencia-reprodutibilidade)

---

### US-13 - Empirical Validation of Findings Exploitability {#us-13---validação-empírica-de-exploitabilidade-de-findings}

**Context.**  
Tools report findings based on heuristics, not on empirical exploitation. False positives block pipelines unnecessarily; false negatives leave vulnerabilities in production. Without empirical validation, decisions rest on "gut feeling" ("it looks secure") without evidence.

:::userstory
**Story.**   
As an **AppSec Engineer + DevOps / SRE**, I want **an empirical validation framework for findings**, so as to test real exploitability with a reproducible PoC, document false positives/negatives with technical evidence, and optimise tool configuration.

**Acceptance criteria (BDD).**  
- **Given** that SAST reports a CRITICAL SQL injection  
  **When** DevOps runs test T1 (code path analysis + payload test in staging)  
  **Then** if exploitable, the finding is confirmed; if dead code or validation blocks it, it is marked as FP with template S1
- **Given** DAST reports a HIGH XSS  
  **When** test T2 is run (reproduce payload + test WAF bypasses)  
  **Then** if the bypass works, the finding is confirmed; if the WAF blocks all payloads, it is marked as mitigated with evidence
- **Given** fuzzing reports a crash with input >10KB  
  **When** test T4 is run (reproduce crash + root cause analysis + test RCE)  
  **Then** if DoS is confirmed, the severity is adjusted; if it is only a handled edge case, it is marked as LOW
- **Given** a production incident (exploited XSS)  
  **When** I confirm that SAST/DAST did not detect it  
  **Then** I record the FN with template S2 (Root Cause Analysis), adjust the tools, add a regression test
- **Given** a quality metric  
  **When** the monthly review takes place  
  **Then** FP `<20%`, FN `<5%`, validation time `<4h` (L2) or `<2h` (L3)

**Checklist.**  
- [ ] Taxonomy T1-T5 defined (SAST, DAST, IAST, Fuzzing, Pentesting) with test procedures per type
- [ ] Test procedures: T1 (code path + payload test), T2 (WAF bypass), T3 (manual IAST PoC), T4 (crash analysis), T5 (pentesting reproduction)
- [ ] FP suppression template S1 with mandatory fields (Finding ID, technical analysis, test evidence, AppSec approver)
- [ ] RCA template S2 for FN (undetected vulnerability, root cause, tool fix, future prevention)
- [ ] PoC repository versioned in Git (pocs/FINDING-ID-poc.py)
- [ ] Isolated staging environment for exploitation tests (segmented network, non-production data)
- [ ] Quality metrics dashboard: FP rate `<20%`, FN rate `<5%`, validation time, test coverage
- [ ] Integration with tools for automatic suppression of validated FPs (inline comments + whitelist)

:::

**🧾 Artefacts & evidence.**  
- Taxonomy T1-T5 applied (SAST, DAST, IAST, Fuzzing, Pentesting with specific procedures)
- Exploitation tests run in staging (T1: code path, T2: WAF bypass, T3: IAST PoC, T4: crash RCA, T5: pentesting reproduction)
- FP suppression template S1 completed (Finding ID, technical reason, evidence of non-exploitable test)
- RCA template S2 for FN documented (missed vulnerability, root cause, tool adjustment)
- PoC repository versioned in Git (pocs/*.py with reproducible payloads)
- Metrics dashboard: FP rate `<`20%, FN rate `<`5%, validation time `<`4h, confirmation rate \>70%
- Exploitation test logs with timestamps and evidence (screenshots, HTTP logs, crash dumps)

**⚖️ Proportionality.**  
| Level | Mandatory? | Adjustments |
|---|---:|---|
| L1 | Optional | Tests for CRITICAL only, no validation-time requirement |
| L2 | Yes | Tests T1-T5 for CRITICAL+HIGH, template S1 mandatory, metrics FP `<30%`, time `<4h` |
| L3 | Yes | Tests T1-T5 for all findings ≥MEDIUM, template S1+S2, metrics FP `<20%`, FN `<5%`, time `<2h` |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| CI/CD | Tool reports a finding | AppSec Engineer + DevOps / SRE | 4h HIGH (L2), 2h CRITICAL (L3) |
| Staging | Deploy of a new version | AppSec Engineer | Tests T1-T5 before production |
| Review | Monthly | AppSec Engineer + GRC / Compliance | Metrics analysis (FP, FN, coverage) |
| Incident | Exploited vulnerability | AppSec Engineer + CISO | Mandatory RCA with Template S2 |

**Useful links.**  
[Addon 10 - Evidence and Reproducibility](/sbd-toe/sbd-manual/testes-seguranca/addon/evidencia-reprodutibilidade)
[Addon 08 - Findings Management](/sbd-toe/sbd-manual/testes-seguranca/addon/gestao-findings)

---

---

### US-14 - Human validation of the final interpretation of results {#us-14---validação-humana-da-interpretação-final-dos-resultados}

Tools can correlate, prioritise and suggest severity - but **they do not replace human validation**.  
This US ensures that the team does not take decisions (merge/release/acceptance) based solely on automated scoring or aggregation of results.

**Context.**  
“Plausible” or well-prioritised results may be wrong, incomplete or out of context. Without human validation, the risk of false positives/negatives and of non-auditable decisions increases.

:::userstory
**Story.**  
As an **AppSec Engineer**, I want **to validate the final interpretation of test results (severity, exploitability, priority and recommended action)**, so that **engineering and governance decisions are guaranteed to rest on evidence and context, and not only on automatic correlation**.

**Acceptance criteria (BDD).**  
- **Given** that a set of tests (SAST/DAST/SCA/IAST/fuzzing) has produced findings  
  **When** triage is concluded  
  **Then** documented human validation exists for all findings above the threshold defined for Lx

- **Given** that a finding is marked as “false positive”, “mitigated” or “accepted”  
  **When** the decision is recorded  
  **Then** a technical rationale and attached evidence exist that support the classification

**Checklist.**  
- [ ] Human triage mandatory for severity ≥ Lx threshold  
- [ ] Rationale recorded (why it is critical/high/medium/low)  
- [ ] Evidence attached (logs, minimal PoC, technical references)  
- [ ] False positives with justification and approval  
- [ ] Final result published (e.g. backlog / central platform) with the responsible person identified  

:::

**Artefacts & evidence.** Triage record (ticket/note), technical attachments, link to the original finding and final decision.

**Proportionality by risk.**  
| Level | Requirement |
|---|---|
| L1 | Human triage for High/Critical |
| L2 | Human triage for Medium+ |
| L3 | Human triage for all findings above Low |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| CI/CD / Staging | Generation of findings | AppSec Engineer + QA | Before merge/release |

---

### US-15 - Reproducibility of critical security test results {#us-15---reprodutibilidade-de-resultados-críticos-de-testes-de-segurança}

Without reproducibility there is no reliable audit.  
This US ensures that any relevant finding can be re-run in a controlled manner, with sufficient context for independent validation.

**Context.**  
Tests may depend on configuration, seeds, environment states, tool versions and dynamic inputs. Non-reproducible results degrade governance and increase the risk of incorrect decisions.

:::userstory
**Story.**  
As a **QA** role, I want **to ensure that critical/high security test results are reproducible**, so that **independent validation, audit and effective fixing without ambiguity are possible**.

**Acceptance criteria (BDD).**  
- **Given** that a Critical/High finding is detected  
  **When** it is escalated for a fix or a decision  
  **Then** a documented procedure exists that allows the result to be reproduced in a controlled environment

- **Given** that the finding depends on dynamic inputs (e.g. fuzzing)  
  **When** the test is recorded  
  **Then** the input/corpus and the context (seed, version, configuration) are preserved and versioned

**Checklist.**  
- [ ] Test configuration versioned (ruleset, flags, scope)  
- [ ] Tool version recorded (e.g., container digest)  
- [ ] Relevant inputs preserved (request, payload, corpus, seed)  
- [ ] Reproduction environment defined (staging/lab)  
- [ ] Reproduction procedure documented (step by step)  
- [ ] Evidence of the retest after the fix (before/after)  

:::

**Artefacts & evidence.** Reproduction runbook, input/corpus files, before/after logs, identification of the tool version and configuration.

**Proportionality by risk.**  
| Level | Requirement |
|---|---|
| L1 | Reproducibility for Critical |
| L2 | Reproducibility for High/Critical |
| L3 | Reproducibility for Medium+ (with Critical/High mandatory) |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Staging / Pre-release | Finding ≥ threshold | QA + AppSec Engineer | Before the go/no-go decision |

---

### US-16 - Formal separation between automatic signal and block/override decision {#us-16---separação-formal-entre-sinal-automático-e-decisão-de-bloqueiooverride}

Gates are necessary, but they do not replace governance.  
This US ensures that the decision (block, grant an exception, promote) is always assigned to a human role and leaves evidence.

**Context.**  
Without a clear separation, pipelines become the “authority” and risk decisions remain implicit, difficult to audit and easy to circumvent informally.

:::userstory
**Story.**  
As a **DevOps / SRE**, I want **to formally separate the automatic signal (tool results) from the block/override decision**, so that **irreversible actions are guaranteed to be controlled and auditable, with explicit human responsibility**.

**Acceptance criteria (BDD).**  
- **Given** that a gate fails because of a finding above the threshold  
  **When** the team intends to override  
  **Then** the override is only permitted with a documented human decision and a defined temporal validity

- **Given** that a finding is marked as an exception  
  **When** the release is approved  
  **Then** the evidence of the decision (who, why, compensations, expiry) is recorded and attached to the release

**Checklist.**  
- [ ] Gates defined (what is signal vs what is blocking)  
- [ ] Override only via a formal mechanism (PR/issue/workflow)  
- [ ] Decision-maker identified (role and person)  
- [ ] Technical justification and compensations recorded  
- [ ] Mandatory expiry date for exceptions  
- [ ] Retest planned before the end of the expiry (L2/L3)  

:::

**Artefacts & evidence.** Override/acceptance record, evidence of compensations, expiry, link to release and findings.

**Proportionality by risk.**  
| Level | Requirement |
|---|---|
| L1 | Overrides permitted with a simple record |
| L2 | Override requires AppSec Engineer approval + expiry |
| L3 | Override requires dual approval (AppSec Engineer + Product Owner / Tech Lead) + expiry + mandatory retest |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| CI/CD / Pre-release | Gate failed or exception proposed | DevOps / SRE + AppSec Engineer | Before the merge/release |

---

### US-17 - Critical assessment of real coverage and limitations {#us-17---avaliação-crítica-de-cobertura-real-e-limitações}

“Good” coverage in metrics does not mean real security.  
This US introduces the process control that prevents over-confidence and forces documentation of gaps.

**Context.**  
Automatic metrics (percentages, green checks, test counts) can mask gaps: endpoints out of scope, authenticated flows not covered, rare paths, specific threats without a test.

:::userstory
**Story.**  
As an **AppSec Engineer**, I want **to critically assess the real coverage of security tests and document limitations**, so that **false assurances are avoided and relevant gaps are known and addressed**.

**Acceptance criteria (BDD).**  
- **Given** a set of tests run for a release  
  **When** the validation summary is produced  
  **Then** coverage metrics interpreted by a human and explicitly recorded limitations exist

- **Given** that there are areas outside coverage (e.g. untested critical endpoints)  
  **When** the release is approved  
  **Then** a mitigation plan exists (additional test, compensating control or formal exception)

**Checklist.**  
- [ ] Real scope documented (what was tested vs not tested)  
- [ ] Coverage by domain (authentication, authorisation, inputs, critical APIs)  
- [ ] Limitations recorded (why it was not covered)  
- [ ] Uncovered threats identified (link to the threat model where applicable)  
- [ ] Mitigation plan per gap (owner + deadline)  
- [ ] Review and approval by a human role (AppSec/QA)  

:::

**Artefacts & evidence.** Annotated coverage report, list of limitations and untested areas, record of uncovered threats, mitigation plan per gap with owner and deadline, and record of review and approval by AppSec/QA.  


**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Pre-release | Production of the validation summary of a release | AppSec Engineer | Metrics interpreted by a human and limitations recorded in the summary |
| Pre-release | Release approval with areas outside coverage | AppSec Engineer | Mitigation plan per gap, with owner and deadline, before approval |

---

### US-18 - Versioned SAST rule profile with false-positive baseline {#us-18---perfil-de-regras-sast-versionado-com-baseline-de-falsos-positivos}

SAST is only a reliable gate when its own noise is under control.  

**Context.**  
A SAST scanner with an ad-hoc rule profile and no false-positive (FP) baseline produces noise that erodes confidence in the gate: either the output is ignored, or it is bypassed. `TST-002` requires a documented and versioned rule profile and an FP baseline approved by AppSec, with the FP rate reviewed periodically. Without this, SAST ceases to be an oracle and becomes a source of alert fatigue.  

:::userstory
**Story.**   
As an **AppSec Engineer**, I want **to version the SAST rule profile and maintain an approved false-positive baseline**, so that **a stable gate is guaranteed, with controlled noise and auditable coverage of critical components**.  

**Acceptance criteria (BDD).**  
- **Given** a SAST scanner integrated into the pipeline  
  **When** the rule profile is changed or an FP is suppressed  
  **Then** the change is versioned in VCS, with recorded AppSec approval and a link to the suppressed finding  

**Checklist.**  
- [ ] Rule profile (ruleset/flags) versioned in VCS  
- [ ] FP baseline approved by AppSec, with a rationale per suppression  
- [ ] FP rate measured and reviewed periodically (aligned with TST-K07)  

:::

**Artefacts & evidence.** Versioned ruleset, register of approved suppressions (Finding ID + approver), time series of the FP rate.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Versioned profile; baseline for CRITICAL | + baseline for CRITICAL/HIGH; quarterly review of the FP rate | + monthly review; suppressions with dual validation and expiry |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| CI/CD | Ruleset change or FP suppression | AppSec Engineer + DevOps / SRE | In the PR that changes the profile |
| Review | Periodic (FP rate) | AppSec Engineer | Quarterly (L2) / monthly (L3) |

**Useful links.** [Static Code Validation (SAST)](/sbd-toe/sbd-manual/testes-seguranca/addon/sast) · [Requirements Catalogue (TST-002)](/sbd-toe/sbd-manual/testes-seguranca/addon/catalogo-requisitos-testes)

---

### US-19 - Protection of the assets of the testing process {#us-19---proteção-dos-ativos-do-processo-de-teste}

Testing must not itself become a vector of exposure.  

**Context.**  
The testing process handles data, credentials and telemetry — and each is an asset that can leak. `addon/10` prescribes real data prohibited by default in test environments, dedicated least-privilege technical accounts with rotation, masking of secrets in logs and egress control of the DAST/IAST/fuzzing environments. Without these controls, testing introduces the very risk it seeks to mitigate.  

:::userstory
**Story.**   
As a **DevOps / SRE + AppSec Engineer**, I want **to protect the assets of the testing process (data, credentials, egress, logs)**, so that **the execution of tests itself is prevented from exposing real data, secrets or uncontrolled network surfaces**.  

**Acceptance criteria (BDD).**  
- **Given** a DAST/IAST/fuzzing environment  
  **When** the test is run  
  **Then** there is no real data (by default), the credentials belong to a dedicated least-privilege technical account, secrets appear masked in the logs and egress is restricted to the scope of the test  

**Checklist.**  
- [ ] Real data prohibited by default; exceptional use with approval and justification  
- [ ] Dedicated technical accounts, least privilege, with credential rotation  
- [ ] Masking of secrets in logs and test artefacts; egress restricted  

:::

**Artefacts & evidence.** Test data policy, register of technical accounts and rotation, masking configuration, network policy/egress rules of the test environment.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| No real data; basic masking of secrets | + dedicated technical accounts with rotation; egress restricted | + full environment segregation, real-data exceptions with dual approval and audit |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Staging | Provisioning of the test environment | DevOps / SRE + AppSec Engineer | Before the 1st run |
| Continuous | Rotation of technical credentials | DevOps / SRE | As per the rotation policy |

**Useful links.** [Evidence and Reproducibility](/sbd-toe/sbd-manual/testes-seguranca/addon/evidencia-reprodutibilidade) · [Requirements Catalogue (TST-005)](/sbd-toe/sbd-manual/testes-seguranca/addon/catalogo-requisitos-testes)

---

### US-20 - KPIs of the effectiveness of the testing programme {#us-20---kpis-de-eficácia-do-programa-de-testes}

What is not measured is not governed — and a testing programme without indicators is an intuition.  

**Context.**  
`addon/15` defines indicators TST-K01..K07 (SAST/DAST coverage, % of findings resolved within SLA, regression rate, centralisation, noise/FP, external pentest) with thresholds per L1–L3, linked to the cross-cutting dimensions T-01 and T-03. Without periodic collection and a consistent denominator (F-02, applications with a formal risk classification), there is no objective basis for assessing the maturity of the programme or for aggregated reporting.  

:::userstory
**Story.**   
As an **AppSec Engineer**, I want **to collect and report the KPIs of the testing programme (TST-K01..K07) with thresholds per risk level**, so that **coverage, resolution speed and noise are measured, and improvement decisions are supported with aggregable evidence**.  

**Acceptance criteria (BDD).**  
- **Given** the set of classified applications (denominator F-02)  
  **When** the collection period closes  
  **Then** the indicators TST-K01..K07 are calculated, compared with the level's threshold, and deviations generate documented action  

**Checklist.**  
- [ ] Indicators TST-K01..K07 instrumented over the F-02 denominator  
- [ ] Thresholds per L1–L3 published and deviations with an action plan  
- [ ] Aggregable periodic reporting (cross-link T-01/T-03)  

:::

**Artefacts & evidence.** KPI dashboard, time series per indicator, register of deviations and corrective actions, mapping to T-01/T-03.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| TST-K01/K03/K05 with L1 thresholds | + TST-K02/K04/K07; quarterly review | + TST-K06; monthly review and reporting to governance |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Continuous | Production/triage of findings | AppSec Engineer + DevOps / SRE | Real time (collection) |
| Review | Period close | AppSec Engineer + GRC / Compliance | Monthly (L3) / quarterly (L2) |

**Useful links.** [Testing KPIs and Metrics](/sbd-toe/sbd-manual/testes-seguranca/addon/kpis-metricas-testes) · [Findings Management](/sbd-toe/sbd-manual/testes-seguranca/addon/gestao-findings)

---

### US-21 - Governance of the use of AI in testing and eval suites for agents {#us-21---governação-do-uso-de-ia-em-testes-e-eval-suites-para-agentes}

When AI assists testing, it is an accelerator; when the agent is the system under test, it is a target.  

**Context.**  
`addon/13` distinguishes two uses: AI that **assists** those who test (controls C1–C4: minimisation and masking of prompts, protection against prompt injection in artefacts, segregation of environments/credentials, prohibition of auto-merge of patches) and AI that is a **component in production**, requiring versioned eval suites (C5) — prompt regression, red-team corpus, drift detection — run as a gate before merging changes to system prompts, skill files, agent files or the model version, proportional to the level of autonomy. Without this governance, security decisions rest on AI output without deterministic evidence, and agents are promoted without validation.  

:::userstory
**Story.**   
As an **AppSec Engineer + DevOps / SRE**, I want **to frame the use of AI in testing by policy (C1–C4) and require versioned eval suites as a gate for AI agents (C5)**, so that **traceable human decision, confidentiality of data and validation of agentic behaviour before promotion are maintained**.  

**Acceptance criteria (BDD).**  
- **Given** that AI assists triage or test generation  
  **When** a decision of severity ≥ HIGH is taken  
  **Then** a C1 record exists, with no secrets/PII in the prompt, no auto-merge of the patch, and the confirmation rests on a deterministic artefact (PoC/test/log)  
- **Given** an AI agent in production or in the testing process  
  **When** the system prompt, skill file, agent file or the model version changes  
  **Then** the eval suite runs in CI as a gate and the result is archived with `eval_run_id` linked to the `mandate_ref`  

**Checklist.**  
- [ ] Policy on the use of AI in testing (minimisation, masking, no auto-merge) applied — controls C1–C4  
- [ ] Eval suite versioned in VCS, run in CI before merging prompt/skill/model (C5)  
- [ ] Eval results archived (`eval_run_id` ⇄ `mandate_ref`), coverage proportional to the level of autonomy  

:::

**Artefacts & evidence.** Policy on AI in testing, C1 decision records, versioned eval suite, eval run logs with `eval_run_id`, red-team corpus, drift reports.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Policy C1–C4; eval suite recommended (A1) | C1–C4 mandatory; eval suite as a gate for A2+ agents | + periodic manual red-team, drift in short windows and production telemetry (A4) |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| CI/CD | Change to system prompt / skill / agent file / model version | DevOps / SRE + AppSec Engineer | Gate before the merge |
| Review | Periodic | AppSec Engineer | Quarterly (corpus and drift) |

**Useful links.** [AI in the Testing Process — Eval suites (C5)](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites) · [Assisted Decision (US-12)](#us-12---decisão-assistida-para-findings-de-testes-de-segurança)

---

### US-22 - Readiness preparation for TLPT (DORA) {#us-22---preparação-de-readiness-para-tlpt-dora}

When the obligation arrives from the authority, the technical foundation must already be built.  

**Context.**  
`addon/14` frames Threat-Led Penetration Testing as a regulatory obligation (DORA, Art. 26/27; Delegated Reg. (EU) 2025/1190) for entities identified by the competent authority. Identification of subjection, qualification of testers/providers and attestation are outside the scope of the manual; what falls to SbD-ToE is **technical and documentary readiness**: a threat model baseline with crown jewels (Ch. 03), documented maturity of the testing programme (Ch. 10), monitoring and IR in production (Ch. 12) and evidence organised as support for the attestation process. For entities subject to DORA, this preparation is what gives the exercise substance and makes remediation credible.  

:::userstory
**Story.**   
As a **CISO + AppSec Engineer**, I want **to keep the technical readiness for TLPT documented and organised**, so that **a threat-led exercise with substance is supported and a contextual basis is provided to the attestation process, when the entity is subject to DORA**.  

**Acceptance criteria (BDD).**  
- **Given** that the entity may be subject to TLPT  
  **When** readiness is assessed  
  **Then** a threat model baseline with identified crown jewels, documented maturity of the testing programme, tested monitoring/IR in production and SbD-ToE evidence organised as documentary support for the attestation exist  

**Checklist.**  
- [ ] Threat model baseline approved with critical functions and crown jewels (Ch. 03)  
- [ ] Maturity level of the testing programme documented (Ch. 10)  
- [ ] Monitoring and IR in production with tested playbooks (Ch. 12); evidence organised for attestation  

:::

**Artefacts & evidence.** Threat model baseline, crown jewels inventory, maturity summary of the testing programme, tested IR playbooks, dossier of supporting evidence for the attestation.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| N/A (outside the typical regulatory scope) | Basic documentary readiness if there is DORA exposure | Full readiness for entities subject to DORA — threat model, maturity, IR and attestation dossier |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Audit | Notification of subjection or regulatory cycle (min. every 3 years) | CISO + GRC / Compliance | Before planning the exercise |
| Review | Periodic | AppSec Engineer + CISO | Annual (maintenance of readiness) |

**Useful links.** [TLPT — Readiness and DORA](/sbd-toe/sbd-manual/testes-seguranca/addon/tlpt-readiness) · [PenTesting (US-08)](#us-08---pentesting-ofensivo-baseado-em-risco)

---

## 📦 Expected artefacts {#-artefactos-esperados}

Every test leaves a tangible trail.  
These artefacts are what makes it possible to demonstrate security before audits or clients:  

| Artefact | Evidence |
|-----------|-----------|
| Testing strategy | Versioned document |
| SAST/DAST/IAST reports | SARIF / HTML |
| SBOM | CycloneDX/SPDX |
| Regressions | Code + CI logs |
| Release checklist | Final PR document + signatures |
| PenTest report | PDF/MD + PoCs |
| Exception register | GRC tool |
| **Centralised findings platform** | **DefectDojo, Vulcan, or similar** |
| **Feedback webhooks and integrations** | **YAML configuration + notification logs** |
| **KPI dashboard** | **Prometheus/Grafana + monthly reports** |

---

## ⚖️ L1–L3 proportionality matrix {#️-matriz-de-proporcionalidade-l1l3}

Proportionality avoids both excess and insufficiency.  
The goal is to calibrate testing according to the criticality of the application:  

| Practice | L1 | L2 | L3 |
|---------|----|----|----|
| SAST | Warning | Blocking on High/Critical | Blocking on Medium+ |
| DAST | Manual | Automated authenticated | Automated + extended coverage |
| **IAST** | **N/A** | **Recommended (criticals)** | **Mandatory (full coverage)** |
| Fuzzing | Optional | Priority endpoints | Critical endpoints |
| Regressions | Critical cases | Per findings | Mandatory |
| PenTesting | N/A | Occasional | Pre-production mandatory |
| **Findings management** | **Simple backlog** | **Centralised with SLA** | **Centralised + audit** |
| Release | Simple checklist | Blocking on High/Critical | No critical without an exception |

---

## 🏁 Final recommendations {#-recomendações-finais}

- **Test early and always**: integrate SAST into the PR and regressions from the 1st sprint.  
- **Validate the runtime**: authenticated DAST and fuzzing in staging are essential.  
- **Adjust to risk**: thresholds and policies must follow L1–L3.  
- **Concrete evidence**: reports, SBOM and versioned logs are the basis of the audit.  
- **Complementarity**: human Pentesting challenges and confirms automation.  
- **Continuous culture**: tests are not an end, but a permanent cycle of validation.  

---
