---
id: aplicacao-lifecycle
title: How to Do It
description: Practical integration of monitoring and response practices into the secure lifecycle
tags: [tipo:aplicacao, ciclo-vida, monitorizacao, deteccao, operacoes, incidentes]
genia: us-format-normalization
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/aplicacao-lifecycle.md
  source_sha256: ecf280a765babffdc3c506f4103025913696b0d9cc72b8553caeb6269871831f
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: 715ceea4f59625c29bb28a448cf275c7a146a2dbbf6d078fe04d6fafc84d1269
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, como_fazer, cycle_iteration, deterministic, framework_source_corpus, lifecycle_phase, mapping, mcp_reading_programa, papel_suporte, piso_limiar, piso_relacao, practitioner_manual, programme_line, requirement_runtime, risk_level, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 554488124abc29c0a074ab0f564738d25c3197109db2ea24fbb3cc6f965ed64c
  translated_at: 2026-09-26T12:48:58Z
  stamped_at: 2026-09-26T18:35:46Z
  reviewed_by: null
---

# Applying Monitoring and Operations Throughout the Lifecycle

## 🧭 When to apply {#-quando-aplicar}

Monitoring and operating securely is not a one-off activity: it is a common thread that must be present in every phase of the lifecycle.  
From the first line of code to the audit review, the application needs to generate visibility, support detection and enable coordinated response.  

The following table shows **the critical moments at which each control must be applied** and how it can be evidenced:

| Phase / Event | Expected action | Evidence |
|---------------|---------------|-----------|
| Development | Code instrumentation with metrics and logs | Code + dev logs |
| QA/Staging | Validation of event and alert generation | QA reports |
| Deploy | Configuration of logging and metrics pipelines | Centralised logs |
| Production | Continuous monitoring + alerts | Dashboards + alerts |
| Incident | Execution of IRP playbooks | Response reports |
| Audit | Review of metrics (MTTD/MTTR) | GRC reports |

---

## 👥 Who carries out each action {#-quem-executa-cada-ação}

Secure monitoring and operations require well-distributed responsibilities.  
It is not enough for a team to “have logs”: each role must take on a clear function in the creation and validation of events and in the reaction to them.  

| Role | Responsibility |
|-------|------------------|
| **Developer** | Expose metrics and structured logs |
| **QA** | Validate event generation and thresholds |
| **AppSec Engineer** | Define critical events and monitor alerts |
| **DevOps / SRE** | Configure pipelines and dashboards |
| **Operations (Ops)** | Analyse alerts and execute playbooks |
| **GRC / Compliance** | Review metrics and ensure compliance |

---

## 📖 Reusable User Stories {#-user-stories-reutilizáveis}

The following user stories translate the chapter's principles into concrete practices.  
Each one reflects real risk situations and the measures needed to ensure visibility, detection and response.

### US-01 - Structured and centralised logging {#us-01---logging-estruturado-e-centralizado}

The first step towards secure operation is **ensuring visibility**.  
Without consistent and centralised logs, any investigation starts blind.  

**Context.** Scattered, non-normalised logs make incident detection harder.  

:::userstory
**Story.**   
As a **Developer**, I want **to generate structured and centralised logs**, so that **full visibility in incidents is assured**.  

**Acceptance criteria (BDD).**  
- **Given** running code  
  **When** a relevant event occurs  
  **Then** it is recorded in a structured format and sent to the central log  

**Checklist.**  
- [ ] Logs in JSON/ECS format  
- [ ] Centralisation pipeline configured  
- [ ] Retention according to policy  

:::

**Artefacts & evidence.** Centralised logs.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic | Structured | Structured + correlation in SIEM |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Development/Deploy | Code execution | Dev + DevOps | Continuous |

**Useful links.** [Secure Deployment](/sbd-toe/sbd-manual/deploy-seguro/intro)  

---

### US-02 - Definition of critical events and metrics {#us-02---definição-de-eventos-e-métricas-críticas}

Visibility without context generates only noise.  
It is essential to decide **what deserves to be observed** and which events should trigger alerts.  

**Context.** Without a clear definition, alerts do not reflect real risks.  

:::userstory
**Story.**   
As an **AppSec Engineer**, I want **to define critical security events and metrics**, so that **it is assured that monitoring covers relevant risks**.  

**Acceptance criteria (BDD).**  
- **Given** a system in production  
  **When** I define critical metrics  
  **Then** dashboards reflect real risks and alerts are configured  

**Checklist.**  
- [ ] Approved list of critical events  
- [ ] Dashboards configured  
- [ ] Alerts tested  

:::

**Artefacts & evidence.** List of events + dashboards.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic | Partial definition | Full definition + quarterly review |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Planning/Operations | Entry into production | AppSec | Quarterly |

**Useful links.** [Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### US-03 - Alerts with defined SLAs {#us-03---alertas-com-slas-definidos}

An alert without a response deadline is just noise.  
For monitoring to have impact, each alert needs to be tied to a **time commitment**.  

**Context.** Without SLAs, critical incidents have no guaranteed response.  

:::userstory
**Story.**   
As **Ops**, I want **to configure critical alerts with defined SLAs**, so that **timely incident response is assured**.  

**Acceptance criteria (BDD).**  
- **Given** a critical alert  
  **When** the SLA is exceeded  
  **Then** the incident is escalated automatically  

**Checklist.**  
- [ ] SLAs documented  
- [ ] Alerts configured  
- [ ] Escalation tested  

:::

**Artefacts & evidence.** Alert configuration + SLA reports.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Warning | Critical SLA | Critical SLA + automation |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Production | Critical incident | Ops + AppSec | According to SLA |

**Useful links.** [Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)

---

### US-04 - Integration with incident response processes {#us-04---integração-com-processos-de-resposta-a-incidentes}

Detection only creates value when it leads to a response.  
Isolated alerts solve nothing: they need to be tied to **clear and tested playbooks**.  

**Context.** Isolated alerts without an IRP become useless.  

:::userstory
**Story.**   
As **Ops**, I want **to integrate alerts with incident response playbooks**, so that **fast and coordinated action is assured**.  

**Acceptance criteria (BDD).**  
- **Given** a security alert  
  **When** it is confirmed  
  **Then** the associated playbook is executed  

**Checklist.**  
- [ ] Playbooks defined  
- [ ] Integration with SIEM/SOAR  
- [ ] Execution validated  

:::

**Artefacts & evidence.** Playbooks + SOAR logs.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Manual | Playbooks defined | Automated playbooks |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Operations | Confirmed alert | Operations (Ops) | ≤ 30 min |

**Useful links.** [Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)

---

### US-05 - Effectiveness metrics (MTTD/MTTR) {#us-05---métricas-de-eficácia-mttdmttr}

Only what is measured can be improved.  
Without effectiveness metrics, any monitoring effort runs the risk of becoming static and complacent.  

**Context.** Without measuring effectiveness, there is no continuous improvement.  

:::userstory
**Story.**   
As **GRC / Compliance**, I want **to measure the MTTD and MTTR of incidents**, so that **the effectiveness of monitoring and response can be assessed**.  

**Acceptance criteria (BDD).**  
- **Given** recorded incidents  
  **When** I calculate the metrics  
  **Then** MTTD and MTTR are reported periodically  

**Checklist.**  
- [ ] Metrics defined  
- [ ] Automatic calculation  
- [ ] Quarterly reports  

:::

**Artefacts & evidence.** Metrics reports.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic | Metrics calculated | Metrics + defined targets |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Audit | Periodic review | GRC | Quarterly |

**Useful links.** [Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### US-06 - Classification and Coverage of Monitoring Domains {#us-06---classificação-e-cobertura-de-domínios-de-monitorização}

An effective monitoring approach does not cover everything indiscriminately: it must be **proportional and focused on the domains that matter most** for the security and operation of each application.

**Context.** Without clear domain mapping, coverage becomes patchy and inefficient.

:::userstory
**Story.**  
As **AppSec/DevOps**, I want **to classify and map monitoring domains** (technical, security, business, compliance, CI/CD), so that **it is assured that logging coverage is proportional to risk and encompasses critical flows**.

**Acceptance criteria (BDD).**  
- **Given** an application with a risk classification  
  **When** I map the applicable domains  
  **Then** I define data sources, tools and retention for each domain  
- And coverage is documented and validated periodically  

**Checklist.**  
- [ ] Domain mapping per application  
- [ ] Data sources identified per domain  
- [ ] Tools selected (app logs, infra metrics, CI/CD events, etc.)  
- [ ] Proportionality to risk defined  
- [ ] Coverage reviewed annually  

:::

**Artefacts & evidence.** Domain mapping document, list of sources, coverage matrix.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic (technical) | Technical + security | Complete (technical, security, business, compliance, CI/CD) |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Design/Planning | Application classification | AppSec + DevOps | Before design |

**Useful links.** [Monitoring Domains](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/dominios-monitorizacao)

---

### US-07 - Log Security and Integrity {#us-07---segurança-e-integridade-de-logs}

Logs are evidence: if they can be altered, the evidence loses its value.  
Ensuring immutability, audited access and appropriate retention turns logs into security and compliance assets.

**Context.** Alterable or lost logs compromise investigations and audits.

:::userstory
**Story.**  
As **DevOps/GRC**, I want **to ensure log security and integrity** (WORM retention, restricted access, signature/hash, function isolation), so that **alteration or loss of evidence in the event of an incident is prevented**.

**Acceptance criteria (BDD).**  
- **Given** logs in the central store  
  **When** protection policies are applied  
  **Then** logs are immutable, access is audited and integrity is verifiable  
- And retention meets regulatory requirements  

**Checklist.**  
- [ ] WORM retention enabled on the storage  
- [ ] Access to logs restricted and audited  
- [ ] Hash or digital signature applied per batch  
- [ ] Logs separated from the application (forwarder, sidecar, service)  
- [ ] Minimum retention: 30d (L1), 90d (L2/L3)  
- [ ] Retention reversal test every quarter  

:::

**Artefacts & evidence.** WORM configuration, access policies, access audit logs, hashes/signatures.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Local (no retention) | WORM + 90d | WORM + 180d + verifiable integrity |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Deploy/Operations | Entry into production | DevOps + GRC | Immediate |

**Useful links.** [Centralised Logging Controls](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/controles-logging-centralizado)

---

### US-08 - SIEM Integration and Event Normalisation {#us-08---integração-com-siem-e-normalização-de-eventos}

Isolated logs have limited value.  
A SIEM with normalised events enables **correlation, fast search and automated detection** that would be impossible in data silos.

**Context.** Logs not integrated into a SIEM become operationally invisible.

:::userstory
**Story.**  
As **DevOps/AppSec**, I want **to integrate logs with the SIEM** (parsing, normalisation, enrichment), so that **effective correlation and centralised anomaly detection are possible**.

**Acceptance criteria (BDD).**  
- **Given** structured logs emitted  
  **When** sent to the SIEM  
  **Then** they are parsed, normalised into ECS/a common format, enriched with context  
- And available for queries, dashboards and alerts  

**Checklist.**  
- [ ] Forwarder configured (Filebeat, Fluentbit, Vector)  
- [ ] Secure channel (TLS 1.2+) with authentication  
- [ ] Parser/ingest pipeline configured  
- [ ] Tagging per application/environment  
- [ ] Ingestion validation (volume, latency, format)  
- [ ] Failover and buffering test  

:::

**Artefacts & evidence.** Forwarder configuration, parsing rules, SIEM dashboards, ingestion logs.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Optional | Mandatory | Mandatory + full ECS normalisation |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Deploy/Operations | Pipeline construction | DevOps + AppSec | Before go-live |

**Useful links.** [SIEM Integration](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/integracao-siem)

---

### US-09 - Event Correlation and Behavioural Detection {#us-09---correlação-de-eventos-e-deteção-comportamental}

Isolated events may be harmless; patterns of events reveal intentions.  
Correlation turns data into **intelligence** and makes it possible to anticipate attacks or chained failures.

**Context.** Without correlation, sophisticated (multi-stage) attacks remain invisible.

:::userstory
**Story.**  
As **AppSec/IR**, I want **to correlate events across multiple sources** (application, infrastructure, CI/CD) and detect suspicious behavioural patterns, so that **attacks or chained failures can be anticipated**.

**Acceptance criteria (BDD).**  
- **Given** events from multiple centralised sources  
  **When** correlation rules are applied  
  **Then** suspicious patterns (e.g. login + mass download) generate high-severity alerts  
- And baseline deviations per user/IP/role are detected  

**Checklist.**  
- [ ] Temporal/contextual correlation rules defined  
- [ ] Behaviour baselines per user/role created  
- [ ] Time windows for correlation tuned (5m, 15m, 1h)  
- [ ] Persistent IDs (user.id, session.id, trace.id) normalised  
- [ ] Correlation alerts tested with simulated events  
- [ ] Aggregated score per user/device/application implemented  

:::

**Artefacts & evidence.** Correlation rules (SIEM), behavioural baselines, tested correlation alerts, pattern documentation.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Not applicable | Optional | Mandatory |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Operations | After 1 month of data in production | AppSec + Operations (Ops) | Continuous implementation |

**Useful links.** [Anomaly Correlation](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/correlacao-anomalias)

---

### US-10 - Alert Validation and *Tuning* {#us-10---validação-e-tuning-de-alertas}

A poorly calibrated alert is worse than no alert: it causes noise and discredits the system.  
Validating and tuning alerts is **continuous work**, not a one-off.

**Context.** Unvalidated alerts generate false positives and alert fatigue.

:::userstory
**Story.**  
As **AppSec/IR**, I want **to validate and tune alerts** (*trigger* testing, active simulation, replay with real data, *tuning* of *thresholds*), so that **false positives are reduced and it is assured that alerts reflect real risk**.

**Acceptance criteria (BDD).**  
- **Given** a configured alert  
  **When** it is tested  
  **Then** it behaves as expected in real and simulated scenarios  
- And the threshold is tuned to minimise false positives  
- And it is documented with an associated runbook  

**Checklist.**  
- [ ] Active simulation (*trigger* event in staging)  
- [ ] Rule unit test (automated logic tests)  
- [ ] Replay with historical data for retroactive validation  
- [ ] Threshold tuned based on real statistics  
- [ ] False positives documented and cause identified  
- [ ] Runbook/playbook associated with the alert  
- [ ] Quarterly validation of alerts  

:::

**Artefacts & evidence.** Alert tests, simulation logs, tuning report, runbooks, false-positive documentation.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Occasional manual | Periodic validation | Continuous validation + automation |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Operations | Alert creation/review | AppSec + Operations (Ops) | Before activation in production |

**Useful links.** [Alerts and Critical Events](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/alertas-eventos-criticos)

---

### US-11 - Proportionality of Controls by Risk (L1–L3) and Domains {#us-11---proporcionalidade-de-controlos-por-risco-l1l3-e-domínios}

Not all applications require the same level of monitoring. It is essential that organisations apply controls in proportion to risk, ensuring efficiency without underestimating threats.

**Context.** Monitoring controls must be proportional to the application's risk, not applied indiscriminately.

:::userstory
**Story.**  
As **AppSec/GRC**, I want **to apply monitoring controls in proportion to the application's risk level**, so that **operational cost is balanced with adequate security coverage**.

**Acceptance criteria (BDD).**  
- **Given** an application classified at risk L1, L2 or L3  
  **When** I define the monitoring architecture  
  **Then** the minimum mandatory controls for the level are applied  
- And documentation reflects the proportionality matrix  
- And exceptions (e.g. L1 with sensitive data) are approved and audited  

**Checklist.**  
- [ ] Application risk classification carried out  
- [ ] L1–L3 proportionality matrix referenced  
- [ ] Minimum controls per level identified (logging, retention, alerts, SIEM, correlation)  
- [ ] Justification of exceptions documented where applicable  
- [ ] Annual proportionality review scheduled  
- [ ] Traceability between classification → applied controls  

:::

**Artefacts & evidence.**  
Risk classification document, proportionality matrix with selected controls, justification of exceptions, documented annual review.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Local logging + basic domain mapping | Matrix applied; SIEM and alerts implemented | Matrix applied + continuous review with metrics |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Design/Risk | Application classification | AppSec + GRC | Before design |

**Useful links.**  
[Controls Matrix by Risk](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/matriz-controles-por-risco)

---

### US-12 - Traceability and Compliance with Regulations (SSDF, NIS2, ISO 27001) {#us-12---rastreabilidade-e-conformidade-com-regulações-ssdf-nis2-iso-27001}

Monitoring is not an isolated technical exercise: it is an increasingly demanding regulatory requirement. There must be clear traceability between technical controls and regulatory requirements, with auditable evidence.

**Context.** Without regulatory traceability, the security posture becomes misaligned with compliance.

:::userstory
**Story.**  
As **GRC/Audit**, I want **to document and demonstrate compliance between monitoring controls and regulatory requirements** (SSDF, NIS2, ISO 27001), so that **it is assured that the security posture is aligned with regulations**.

**Acceptance criteria (BDD).**  
- **Given** an applicable compliance framework (SSDF, NIS2, ISO 27001)  
  **When** I map technical controls (logging, alerts, correlation, IRP, metrics)  
  **Then** each technical control is traceable to a specific regulatory requirement  
- And auditable evidence exists (logs, dashboards, reports, metrics)  
- And compliance reports are generated quarterly  

**Checklist.**  
- [ ] Technical control → regulatory requirement mapping created and versioned  
- [ ] Traceability matrix (e.g. US-01 Logging → ISO 27001 A.12.4.1)  
- [ ] Technical evidence documented (screenshots, logs, configurations)  
- [ ] Compliance metrics (% of controls active, MTTD vs target, etc.)  
- [ ] Quarterly reports generated and reviewed by audit  
- [ ] Gaps identified and remediation plan created  
- [ ] Internal audits scheduled (annual)  

:::

**Artefacts & evidence.**  
Traceability matrix (control → regulation), technical evidence per control, quarterly compliance reports, compliance metrics, remediation plan, internal audit reports.

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic mapping | Mapping + documented evidence | Mapping + evidence + metrics + continuous audit |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Compliance | Regulatory requirement, audit | GRC + Internal Audit | Quarterly |

**Useful links.**  
[Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro); [Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro) (requirements)

---

### US-13 - Telemetry of AI agents in production {#us-13}

**Context.**
US-01 to US-12 of this chapter cover the classic operational programme — logs, alerts, SIEM, IRP, MTTD/MTTR. When the system includes **AI agents in operation** (agents that execute real *tool calls* with effect on external systems), three signals emerge that traditional observability does not see and that need dedicated instrumentation: *tool invocations* (who did what, under which *mandate*), *token spend* (model consumption, *runaway* protection), and *off-policy actions* / *jailbreak* (divergence between what the agent declares it intends to do and what it does). This US operationalises the requirements [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012), [`OPS-013`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013) and [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014).

:::userstory
**Story.**
As **Ops / AppSec**, I want to collect dedicated telemetry on the operation of AI agents in production — *tool invocations* with full audit, *token spend* with budget enforcement, detection of *jailbreak* and *off-policy actions* — so that abuse, *runaway loops* and actions outside the *mandate* are detected in good time, before material impact.

**Acceptance criteria (BDD).**
- **Given** that an AI agent operates in the system at level A1+
  **When** it invokes a *tool*
  **Then** a structured *audit event* is emitted with `agent_id`, `session_id`, `mandate_ref`, `autonomy_level`, `tool`, `args` (PII redacted), `intent_event_ref` (A2+), `outcome`, `external_effect` (cross-link [`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012))
- **Given** that the agent's *token spend* reaches the warning threshold defined in the *mandate*
  **When** the system observes it
  **Then** an alert goes to the human *owner*; at the maximum threshold the session pauses or the *kill-switch* is triggered according to the autonomy level (cross-link [`OPS-013`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013))
- **Given** that there is a material divergence between the declared `intent_event` and the real *tool invocation audit event*
  **When** the detector runs
  **Then** the signal is handled as an IR incident (Ch. 12 US-04) with immediate escalation to the *owner* (cross-link [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014))
- **Given** that a *jailbreak* or *off-policy action* pattern is detected
  **When** it occurs at A2+
  **Then** the signal feeds the offline *eval suite* (Ch. 10 §C5) for future regression

**Checklist.**
- [ ] *Tool invocation audit events* flowing to the SIEM (OPS-004) with the OPS-012 minimum schema
- [ ] *Token spend* *budget* declared per *mandate*, with warning and maximum thresholds
- [ ] `intent` ↔ action divergence detector configured for all A2+ agents
- [ ] *Jailbreak* detection corpus (LLM01-2025) updated according to the *mandate* cadence
- [ ] OPS-012/013/014 signals linked to IR *runbooks* (US-04 of this chapter)
- [ ] *Drift detection* of the *eval suite* (Ch. 10 §C5) fed back by incidents detected in production

:::

**Artefacts & evidence.**
- Structured *tool invocation* *audit events* (OPS-012)
- *Budget* configuration + *token spend* metrics per agent / mandate (OPS-013)
- Active detection rules / models for *jailbreak* / *off-policy* (OPS-014)
- IR *runbooks* specific to agentic incidents
- SIEM dashboards with agentic signals; periodic reports per *mandate_ref*

**Proportionality by risk.**
| Level | Mandatory? | Adjustments |
|---|---|---|
| L1 | Recommended for A1+; mandatory if the agent is in production | OPS-012 essential; OPS-013 with a simple budget; OPS-014 not mandatory |
| L2 | Yes for A1+ | OPS-012 + OPS-013 mandatory; OPS-014 recommended |
| L3 | Yes for A1+ | OPS-012 + OPS-013 + OPS-014 mandatory; A4 with quarterly review of the detection corpus |

**Integration into the SDLC.**
| Phase | Trigger | Responsible | SLA |
|---|---|---|---|
| Agent onboarding | *Mandate* activation (Policy 38) | `devops` + `appsec` | Before operation in production |
| Operation | Every *tool invocation* | Agent (automatic audit) + `appsec` (signal review) | *Real-time* |
| Incident | OPS-014 fires | `appsec` + `ops` | According to severity (US-04 of this chapter) |
| Review | `review_cadence` of the *mandate* | `appsec` + *owner* | According to cadence |

**Useful links.**
- 🔗 [`OPS-012` — Full audit per *tool invocation*](./addon/catalogo-requisitos-operacoes#ops-012)
- 🔗 [`OPS-013` — Budget and *runaway* detection](./addon/catalogo-requisitos-operacoes#ops-013)
- 🔗 [`OPS-014` — *Jailbreak* / *off-policy* detection](./addon/catalogo-requisitos-operacoes#ops-014)
- 🔗 [`REQ-AGN-*` catalogue (Ch. 02)](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)
- 🔗 [Continuous eval suites (Ch. 10 §C5)](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites)
- 🔗 [Policy 30 — Security Monitoring (agentic annex)](/sbd-toe/assets/policies/policy-monitorizacao-seguranca)
- 🔗 [Policy 38 — AI Agent Mandates](/sbd-toe/assets/policies/policy-mandates-agentes)

---

### US-14 - Non-logging of secrets and management of operational exceptions {#us-14---não-logging-de-secrets-e-gestão-de-exceções-operacionais}

A log that captures a password is a credential leak waiting to happen.  

**Context.** Log centralisation (US-01, US-08) amplifies a silent risk: secrets, tokens and PII in clear text in the events themselves turn the SIEM into a repository of exposed credentials. `OPS-001` requires normalised fields **with no sensitive data in clear text**; when a legitimate pattern wrongly triggers alerts, suppression has to follow a formal exception process, not ad hoc silencing.  

:::userstory
**Story.**   
As **DevOps/AppSec**, I want **to ensure that no secret or PII is logged in clear text and that any alert exception follows a formal process**, so that **credential leakage via logs is prevented and alert suppression remains auditable and temporary**.  

**Acceptance criteria (BDD).**  
- **Given** a component in production that emits logs  
  **When** a field contains a credential, token or PII  
  **Then** the value is redacted/masked before persistence and the redaction is verifiable by sampling  
- **Given** a legitimate pattern that triggers an unwarranted alert  
  **When** it is to be suppressed  
  **Then** a versioned exception is created with justification, approver by severity and expiry date (max 6 months L2, 3 months L3)  

**Checklist.**  
- [ ] Redaction/masking of secrets and PII applied before persistence  
- [ ] Sample-based verification of the absence of sensitive data in clear text  
- [ ] Versioned exception template (justification, approver, expiry, evidence)  

:::

**Artefacts & evidence.** Redaction/masking rules, log sampling report, exception register with time-bound validity and approval by severity.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Basic redaction of credentials | Redaction + formal exceptions (max 6 months) | Redaction verified by sampling + exceptions (max 3 months) + pre-expiry reassessment |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Development/Operations | Log emission / exception creation | DevOps + AppSec | Before persistence / before suppression |

**Useful links.** [Centralised Logging Controls](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/controles-logging-centralizado); [Operations Exceptions](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/excecoes-operacoes)

---

### US-15 - Ingestion failure detection and operational dashboards {#us-15---deteção-de-falha-de-ingestão-e-dashboards-operacionais}

The silence of a log source can be as serious as an explicit alert.  

**Context.** `OPS-004` requires log centralisation to have **verifiable ingestion** and that **delivery failures are detected and alerted** — a source that stops reporting creates a *blind spot* that no content alert detects. This visibility of the pipeline itself materialises in operational dashboards that make coverage, volume and latency continuously observable.  

:::userstory
**Story.**   
As a **DevOps/SRE**, I want **to detect and alert on log ingestion failures and expose the pipeline state in dashboards**, so that **blind spots caused by silent sources are eliminated and monitoring coverage becomes observable**.  

**Acceptance criteria (BDD).**  
- **Given** a log source expected in the SIEM  
  **When** the volume drops below the baseline or the source goes silent beyond the expected window  
  **Then** an actionable ingestion failure alert is generated for the responsible team  
- **Given** the monitoring pipeline in operation  
  **When** its state is observed  
  **Then** dashboards reflect coverage per source, volume, latency and ingestion failures  

**Checklist.**  
- [ ] Ingestion failure/absence alert per source configured  
- [ ] Volume/latency baseline per source established  
- [ ] Pipeline coverage, volume and latency dashboards available  

:::

**Artefacts & evidence.** Ingestion failure detection rules, volume baselines per source, operational dashboards of the logging pipeline.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Manual verification of sources | Ingestion failure alert + basic dashboard | Baseline-based detection + full coverage/latency dashboards |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Deploy/Operations | Pipeline construction / silent source | DevOps + SRE | Continuous |

**Useful links.** [SIEM Integration](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/integracao-siem); [Metrics and Indicators](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/metricas-indicadores)

---

### US-16 - ATT&CK coverage and EPSS/KEV prioritisation {#us-16---cobertura-attck-e-priorização-epsskev}

Detecting without mapping coverage is trusting to luck; remediating without prioritising is wasting effort.  

**Context.** Detection rules must declare the **MITRE ATT&CK** techniques they cover (with the ATT&CK version in use recorded), making coverage gaps explicit. In parallel, remediation prioritisation must apply **EPSS** (probability of exploitation) and **KEV** (confirmed exploitation) on top of the SLAs by severity, keeping the SLA by severity as a floor.  

:::userstory
**Story.**   
As **AppSec/IR**, I want **to map detection rules to MITRE ATT&CK techniques and prioritise remediation with EPSS and KEV**, so that **detection coverage gaps are exposed and remediation effort is concentrated on genuinely exploitable risk**.  

**Acceptance criteria (BDD).**  
- **Given** the set of active detection rules  
  **When** coverage is mapped  
  **Then** each rule declares the ATT&CK techniques it covers and the ATT&CK version in use is recorded  
- **Given** a vulnerability to remediate  
  **When** the priority is defined  
  **Then** EPSS and KEV adjust the order on top of the SLA by severity, which remains as a floor  

**Checklist.**  
- [ ] Detection rules mapped to ATT&CK techniques with the version recorded  
- [ ] ATT&CK coverage gaps identified and prioritised  
- [ ] EPSS and KEV applied in prioritisation, with the SLA by severity as a floor  

:::

**Artefacts & evidence.** ATT&CK coverage matrix per rule with version, gap register, prioritisation policy with EPSS/KEV and SLA by severity.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Not applicable | ATT&CK mapping of critical rules + KEV in prioritisation | Full ATT&CK coverage + EPSS/KEV with continuous review |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Operations | Rule creation/review / vulnerability triage | AppSec + Operations (Ops) | Per release / per triage |

**Useful links.** [MITRE ATT&CK as a Detection Engineering Vocabulary](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/attack-detection-engineering); [Prioritisation with EPSS and KEV](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/epss-kev-priorizacao)

---

### US-17 - End-to-end incident response exercises {#us-17---exercícios-de-resposta-a-incidentes-end-to-end}

A playbook that has never been executed is a hypothesis, not a capability.  

**Context.** `OPS-007` requires integration with the formal incident response process and **evidence of playbook activation in a real incident or a documented exercise in the last cycle**. Without end-to-end exercises — from alert to resolution — the detection→escalation→response chain remains unvalidated and the real MTTR is unknown.  

:::userstory
**Story.**   
As **IR/AppSec**, I want **to run end-to-end incident response exercises at a defined periodicity**, so that **the alert→playbook→resolution chain is validated and response times are confirmed to meet the SLA before a real incident**.  

**Acceptance criteria (BDD).**  
- **Given** a representative incident scenario  
  **When** the exercise is executed  
  **Then** the associated playbook is activated end to end and the times (acknowledge/resolve) are measured against the SLA  
- **Given** the conclusion of the exercise  
  **When** the review is carried out  
  **Then** gaps are recorded and generate traceable corrective actions  

**Checklist.**  
- [ ] Representative exercise scenario defined  
- [ ] Playbook activated end-to-end with times measured against the SLA  
- [ ] Gaps and corrective actions recorded in the last cycle  

:::

**Artefacts & evidence.** Exercise plan and report, record of times vs SLA, list of gaps and corrective actions.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Occasional manual walkthrough | Annual exercise of critical playbooks | Periodic end-to-end exercises + MTTR measurement and continuous improvement |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Operations | Exercise cycle / playbook review | Operations (Ops) + AppSec | In the last cycle (annual minimum) |

**Useful links.** [Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro); [Operations Requirements Catalogue](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes)

---

### US-18 - SOAR automation governance and alert kill-switch {#us-18---governação-de-automação-soar-e-kill-switch-de-alertas}

Automation that executes irreversible actions without human approval is an operational risk, not a control.  

**Context.** SOAR automation combines deterministic decisions (which may operate without approval) with non-deterministic decisions (which require human validation), and has explicit guardrails: irreversible actions — log purging, alert deactivation, baseline changes — are **never** automatic. When a poorly calibrated alert causes an *alert storm*, the kill-switch allows temporary deactivation with a time limit, mandatory notification and RCA before reactivation.  

:::userstory
**Story.**   
As **IR/AppSec**, I want **to govern SOAR automation with explicit guardrails and a controlled alert kill-switch**, so that **automation is prevented from executing irreversible actions without human approval and alert storms are stopped without creating permanent blind spots**.  

**Acceptance criteria (BDD).**  
- **Given** an automated action in SOAR  
  **When** the action is irreversible or high-impact (log purging, alert deactivation, baseline changes, mass isolation)  
  **Then** it requires human approval and respects the defined guardrail limits  
- **Given** an *alert storm* caused by a poorly calibrated alert  
  **When** the kill-switch is triggered  
  **Then** the deactivation has a time limit (max 2h), notifies the AppSec Engineer automatically and requires a documented RCA before reactivation  

**Checklist.**  
- [ ] SOAR guardrails documented (action, limit, reason) with human approval for irreversible actions  
- [ ] Kill-switch with time limit, automatic notification and mandatory RCA before reactivation  
- [ ] Deterministic/non-deterministic distinction applied in the decision to automate  

:::

**Artefacts & evidence.** Versioned SOAR guardrails table, approval records for high-impact actions, kill-switch records with associated RCA.  

**Proportionality L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Simple deterministic automation; irreversible actions manual | Documented guardrails + kill-switch with RCA | Guardrails + kill-switch + audit of approvals and review of limits |

**Integration into the SDLC.**  
| Phase | Trigger | Responsible | SLA |
|------|---------|-------------|-----|
| Operations | High-impact SOAR action / alert storm | Operations (Ops) + AppSec | According to severity (kill-switch ≤ 2h) |

**Useful links.** [Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro); [Operations Exceptions](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/excecoes-operacoes)

---

## 📦 Expected artefacts {#-artefactos-esperados}

Every practice leaves verifiable traces.  
These artefacts constitute the objective evidence that underpins audits and regulatory compliance:  

| Artefact | Evidence |
|-----------|-----------|
| Structured logs | Centralised JSON/ECS |
| List of critical events | Versioned document |
| Alert configuration | Dashboards + reports |
| IRP playbooks | Document + SOAR logs |
| Metrics reports | GRC reports |
| Domain mapping | Coverage document per domain |
| WORM and integrity configuration | Immutable logs + hashes/signatures |
| Forwarder and SIEM configuration | Parsing rules + SIEM dashboards |
| Correlation rules | Behavioural baselines + correlated alerts |
| Alert tests | Simulations, unit tests, *tuning* reports |
| L1–L3 proportionality matrix | Controls applied per level + justifications |
| Regulatory traceability | Control → regulation mapping matrix + auditable evidence |

---

## ⚖️ L1–L3 proportionality matrix {#️-matriz-de-proporcionalidade-l1l3}

Not all applications carry the same risk or require the same effort.  
The following matrix translates the controls into proportional levels (L1–L3), balancing cost and impact:  

| Practice | L1 | L2 | L3 |
|---------|----|----|----|
| Logging | Basic | Structured | Structured + SIEM |
| Critical events | Basic | Partial definition | Complete + quarterly review |
| Alerts | Warning | Critical SLA | Critical SLA + automation |
| IRP integration | Manual | Playbooks defined | Automated playbooks |
| Metrics | Basic | Calculated | Calculated + targets |
| Monitoring domains | Technical only | Technical + security | Complete (technical, security, business, compliance, CI/CD) |
| Log security | Basic | WORM + controlled access | WORM + signature + function isolation |
| SIEM integration | Optional | Forwarder configured | SIEM + parsing + dashboards |
| Behavioural correlation | Not applicable | Optional | Mandatory |
| Alert validation | Occasional manual | Periodic | Continuous + automation |
| Proportionality by domain | Local logging + basic mapping | Matrix applied; SIEM and alerts implemented | Matrix applied + continuous review with metrics |
| Regulatory traceability | Basic mapping | Mapping + documented evidence | Mapping + evidence + metrics + continuous audit |

---

## 🏁 Final recommendations {#-recomendações-finais}

- **Visibility is key**: without logging and metrics, there is no security in production.  
- **Alerts must be actionable**: without SLAs and playbooks, they only generate noise.  
- **Proportionality matters**: L1 focuses on the essentials, L3 requires automation and targets.  
- **Integration with the IRP**: detection without response brings no value.  
- **Continuous measurement**: MTTD/MTTR metrics make it possible to learn and evolve.  
