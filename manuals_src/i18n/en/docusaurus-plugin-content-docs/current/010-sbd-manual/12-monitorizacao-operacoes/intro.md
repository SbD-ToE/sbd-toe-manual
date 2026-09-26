---
id: intro
title: Monitoring and Operations
description: Principles and practices to ensure visibility, detection and effective response in production environments
tags: [monitorizacao, operacoes, deteção, resposta, logs, métricas, incidentes]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/intro.md
  source_sha256: c6a3ea15865bcb07e3a81cb45dc615ad11ab9f7a7583add938d47b473d41b15f
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: 62d9be1bea56ce79558963777f9c524276ebf8ff2a699a0147935800096532cd
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [basilar, capacitacao, chapter_role, cycle_iteration, lifecycle_phase, practitioner_manual, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: 4e4c8a329c7550f5284f312e7fe7b7b5197dee9c019258792f558e2fc096478c
  translated_at: 2026-09-26T12:48:59Z
  stamped_at: 2026-09-26T18:35:49Z
  reviewed_by: null
---

import ChapterTypeCallout from '@site/src/components/ChapterTypeCallout';

<ChapterTypeCallout kind="operacional" title="Capítulo Operacional">

This chapter is considered **operational** in the *Security by Design - Theory of Everything (SbD-ToE)* model.
Its function is to **apply, automate and validate** the practices defined in the foundational chapters, ensuring their continuous and measurable execution.

The operational chapters implement the SbD-ToE in specific technical contexts. These chapters translate the foundational prescriptions into practices of **verifiable execution**, promoting the **continuous integration of security** throughout the software lifecycle.

</ChapterTypeCallout>


# Monitoring and Operations

Monitoring is much more than collecting technical data.  
It is turning scattered signals into **actionable intelligence** that allows teams to anticipate risks, detect failures and respond before a problem turns into a serious incident.  

Experience shows that a large share of attacks are discovered not because of the adversary's sophistication, but because of a lack of visibility. Cases such as Equifax or Target proved that **the logs were there** - but they were incomplete, poorly structured or simply ignored.  

That is why frameworks such as the **SSDF**, and regulations such as **NIS2** require clear monitoring and response controls. Preventing is not enough: it is necessary to **detect and react**.  

👉 This chapter links directly to:  
- **Ch. 11 - Secure Deployment**, which guarantees that observable versions enter production.  
- **Ch. 13 - Training and Upskilling**, which ensures that people know how to interpret alerts and run playbooks.  

---

## 🧭 What it covers technically {#-o-que-cobre-tecnicamente}

Monitoring and operations, as used here, refers to a complete ecosystem of controls:  

- **Structured and centralised logging**, so that every relevant event is accessible and correlated.  
- **Definition of critical events and metrics**, to distinguish noise from what matters.  
- **Alerts with thresholds and SLAs**, which turn detection into an obligation to respond.  
- **Correlation in SIEM and automation in SOAR**, because human scale is no longer enough.  
- **Integration with incident response processes (IRP)**, ensuring that every alert has an associated plan.  
- **Effectiveness measurement (MTTD/MTTR)**, to know whether the organisation is improving.  

These practices are complementary: they only make sense when they act together, forming a continuous cycle of observation, detection and reaction.

---

## Automation and Governance in Monitoring {#-automação-e-governação-em-monitorização}

Secure monitoring combines **extensive automation** with **explicit governance**, distinguishing between:

### Deterministic Decisions (Sovereign Automation) {#decisões-determinísticas-automação-soberana}

When criteria are **objective, reproducible and context-free**, automation may operate without intervention:

- **Threshold alerts**: CPU >90% for 5 min → automatic alert
- **IP blocking by rate limiting**: >1000 req/min → automatic block
- **Simple temporal correlation**: 5 failed logins in 60s → automatic alert
- **SIEM ingestion**: Valid log → automatic parsing and indexing

**Principle**: Deterministic automation **may operate without human approval** if the criteria are formally defined and versioned.

### Non-Deterministic Decisions (Mandatory Governance) {#decisões-não-determinísticas-governação-obrigatória}

⚠️ **CRITICAL**: Non-deterministic automation **MUST NOT** operate without human governance.

When decisions involve **context, heuristics or behaviour**, they require human validation:

- **Behavioural correlation**: Suspicious but unconfirmed pattern → IR validates before action
- **Threshold adjustment**: Alert with >30% false positives → AppSec approves the new threshold
- **Alert exceptions**: Legitimate but suspicious pattern → Formal exception with time validity
- **High-impact actions**: Isolating an entire subnet → IR + Management approve

**Principle**: Non-deterministic decisions **MUST NOT** be automated without human validation, approval and traceability. Automation may **assist**, but never **decide alone**.

### Automation Guardrails in SOAR {#guardrails-de-automação-em-soar}

Even automated playbooks have **explicit limits**:

| SOAR action | Limit | Reason |
|-----------|--------|-------|
| IP blocking | Max. 100 IPs/hour | Prevent self-inflicted DoS |
| Machine isolation | Max. 10 hosts/hour | Prevent a cascade of isolations |
| Log purge | **NEVER automatic** | Evidence is irreversible |
| Alert deactivation | **NEVER automatic** | Creates blind spots |
| Baseline changes | Always manual + approval | Lateral impact on correlation |

**Principle**: Automation **MUST NOT** execute irreversible actions or actions with critical operational impact without human intervention. Even in deterministic contexts, high-risk actions require approval.

---

## 🔐 Alert Exception Management {#-gestão-de-exceções-em-alertas}

Alert exceptions (e.g. a legitimate but suspicious pattern) follow a formal process:

1. **Exception template** (versioned in the repo):
   ```yaml
   exception_id: ALERT-EX-2026-001
   alert_id: CORR-BEHAVIOR-001
   pattern: "User X downloads 10GB/dia (backup legítimo)"
   justification: "Processo de backup automático, validado com Dev"
   approved_by: "AppSec Engineer (email@example.com)"
   approved_date: "2026-01-04"
   expiration_date: "2026-07-04"  # Máximo 6 meses
   evidence: "link/to/ticket-JIRA-123"
   ```

2. **Approver by alert severity**:
   - CRITICAL: AppSec + IR Lead
   - HIGH: AppSec Engineer
   - MEDIUM: IR Analyst

3. **Time validity**: Exceptions expire automatically (max. 6 months L2, 3 months L3)

4. **Reassessment**: Before expiry, the pattern is reassessed

---

## 🚨 Kill Switch for Poorly Calibrated Alerts {#-kill-switch-para-alertas-mal-calibrados}

In the event of an "alert storm" or a poorly calibrated alert:

1. **Temporary kill switch**: IR may deactivate an alert for a maximum of 2 hours
2. **Mandatory notification**: Deactivation automatically notifies the AppSec Engineer
3. **Root cause analysis**: Mandatory before reactivation
4. **Documentation**: RCA template + correction applied

**Example**:
```yaml
kill_switch_id: KS-2026-001
alert_id: CORR-BEHAVIOR-001
reason: "Falsos positivos em 80% dos alertas (threshold mal calibrado)"
disabled_by: "IR Analyst (email@example.com)"
disabled_at: "2026-01-04 14:30"
expiration: "2026-01-04 16:30"  # Máx 2 horas
rca_required: true
```

---

## 🧪 Practical prescription {#-prescrição-prática}

In practice, applying this chapter means answering four fundamental questions:  

1. **What to observe?** - Logs, integrity metrics, authentication failures, privileged access.  
2. **How to observe?** - Collection pipelines, real-time dashboards, clear thresholds.  
3. **How to react?** - Alerts with SLAs, predefined playbooks, integration with SOAR.  
4. **Is there improvement?** - Continuous measurement of MTTD and MTTR, reports to GRC.  

Each organisation must start with the essentials - structured logging and centralisation - and evolve towards full response automation. The path is proportional to the risk, but the logic is always the same: **see early, react fast, always learn**.

---

## 👥 Roles involved {#-papéis-envolvidos}

Monitoring is a collective effort:  

- **Dev** → includes metrics and logs in the code.  
- **QA/Testing** → ensures that the events generated are valid and actionable.  
- **AppSec** → defines which critical security events to follow.  
- **DevOps/SRE** → keeps pipelines and dashboards operational.  
- **Operations (Ops)** → analyses alerts and runs playbooks.  
- **GRC** → measures effectiveness and ensures regulatory compliance.  

Without this matrix of responsibilities, technical controls become invisible or ineffective.

---

## ⚠️ Risks and common pitfalls {#️-riscos-e-armadilhas-comuns}

It is common to fall into errors such as:  

- **Too many alerts** → without tuning, *alert fatigue* sets in. **Relates to.** Violates `OPS-005`; materialises `MT-201`.  
- **Unstructured logs** → prevent correlation and delay investigations. **Relates to.** Violates `OPS-001`; materialises `MT-202`.  
- **Lack of integration with the IRP** → detection that does not lead to response. **Relates to.** Violates `OPS-007`; materialises `MT-205`.  
- **Insufficient retention** → without history, there is neither audit nor forensics. **Relates to.** Violates `OPS-003`; materialises `MT-198`.  

Recognising these risks from the outset helps to build more robust systems.

---

## 📝 Practical examples {#-exemplos-práticos}

- A DevOps team sends Kubernetes *logs* to a SIEM such as Splunk or Elastic, normalised in ECS.  
- AppSec defines *repeated failed logins*, *unexpected root access* and *creation of privileged pods* as critical events.  
- SREs configure Prometheus/Grafana to alert on service degradation associated with DoS attacks.  
- The SOC integrates SOAR to automatically block malicious IPs or rotate compromised credentials.  

These examples illustrate that monitoring is not abstract: these are practices already applied in thousands of organisations and required by regulators.

---

## 🔗 Integration in the lifecycle {#-integração-no-ciclo-de-vida}

Monitoring accompanies the software from the first commit to the audit:  

- **Development** → instrumentation of logs and metrics in the code.  
- **QA/Staging** → validation of event generation.  
- **Deploy** → pipelines configure collection and alerts by default.  
- **Production** → active dashboards and continuous monitoring.  
- **Incident** → execution of playbooks with traceable evidence.  
- **Audit** → MTTD and MTTR metrics reported to GRC.  

In this way, runtime security stops being reactive and becomes an integral part of the SDLC.

---

## 📊 Organisational traceability {#-rastreabilidade-organizacional}

The effectiveness of monitoring is measured in metrics.  

- **Key KPIs**: MTTD (mean time to detect) and MTTR (mean time to respond).  
- **Audit**: quarterly review of logs, dashboards and reports.  
- **Governance**: operations reports delivered to GRC and management, turning technical metrics into business decisions.  

---

## 🏁 Conclusion {#-conclusão}

Security does not end at deploy: it extends into runtime through visibility, detection and response.  
- No logs → no visibility.  
- No metrics → no improvement.  
- No SLAs → no commitment to respond.  
- No IRP → no coordinated action.  

This chapter is **foundational** because it translates security into the capacity to **detect, react and learn**. It is here that theory becomes living practice, every day, in production.

---

## 📜 Relevant Organisational Policies {#-políticas-organizacionais-relevantes}

| Policy | Mandatory? | Application | Minimum content |
|----------|--------------|-----------|-----------------|
| [Structured Logging Policy](/sbd-toe/assets/policies/policy-logging-estruturado) | Yes | Dev + DevOps | Normalised and centralised logs |
| [Security Monitoring Policy](/sbd-toe/assets/policies/policy-monitorizacao-seguranca) | Yes | AppSec + SRE | Critical metrics, dashboards and thresholds |
| [Alert Management Policy](/sbd-toe/assets/policies/policy-gestao-alertas) | Yes | Operations (Ops) + AppSec | Critical alerts with a defined SLA |
| [IRP Integration Policy](/sbd-toe/assets/policies/policy-irp) | Yes | Operations (Ops) + GRC | Documented playbooks and traceability |
| [Security Governance KPIs Policy](/sbd-toe/assets/policies/policy-kpis-governacao) | Recommended | GRC | Periodic review of MTTD and MTTR |

In the printed version, consult the **Manual's Organisational Policies Annex**, where these policies are consolidated on a cross-cutting basis.
