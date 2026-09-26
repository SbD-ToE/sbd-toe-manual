---
id: policy-kpis-governacao
title: Security Governance KPIs Policy
description: Organisational policy that defines the requirements for the definition, collection, analysis and reporting of security governance KPIs, including metric categories, reporting cadence, responsibilities, intervention thresholds and integration with maturity frameworks (SAMM, SSDF), proportionate to the criticality level (L1, L2, L3).
tags: [policy, KPIs, governação, métricas, maturidade, SAMM, SSDF, reporting, dashboard, cap14, L1, L2, L3, governance, CISO, GRC]
grupo: governacao
sidebar_position: 35
translation:
  source_locale: pt
  source_path: 020-assets/policies/35_policy-kpis-governacao.md
  source_sha256: d132e7b71ce25e2521faf545e44a02c37e245751c91b1550d5b982a8db5c6017
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: bd7a168e39981e5268365bbf505988bd426556bfcefaef62202b77cf7247983f
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [avaliacao, capacitacao, chapter_role, cycle_iteration, framework_source_corpus, maturity, mcp_reading_programa, programme_line, risk_level, role_procurement, role_tech_lead, sbdtoe_sbd, traceability, trilho_formativo]
  glossary_sha256: 639410b3fc031123bcb00e29436061550d3fbf8c70c46e03b9ed66b38b339fcf
  translated_at: 2026-09-26T14:11:04Z
  stamped_at: 2026-09-26T18:37:06Z
  reviewed_by: null
---

# Security Governance KPIs Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for the **definition, collection, analysis and reporting of key performance indicators (KPIs) of the organisation's security governance programme**.

A security programme without metrics is a programme without a feedback loop - it is not possible to determine whether it is working, whether it is improving or whether resources are being applied to the right problems. Security governance KPIs turn technical activity into evidence of performance: they allow executive management to take well-founded strategic decisions, to identify systemic deviations before they become incidents, and to demonstrate maturity to regulators and auditors. Poorly defined metrics, or metrics collected without rigour, are as harmful as the absence of metrics - they create false confidence and divert attention from the real risks.

The objective of this policy is to ensure that:

- The security programme has a defined set of KPIs, with established sources, owners and collection cadence
- The KPIs cover the relevant governance dimensions: compliance, operations, incidents, suppliers and maturity
- Reporting is carried out with a cadence proportionate to the risk level and distributed to the correct recipients
- Deviations in critical KPIs give rise to corrective actions with an owner and a deadline
- The maturity level of the programme is assessed periodically with reference to recognised frameworks

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

| Level | Applicability |
|---|---|
| L1 | Basic; minimum compliance KPIs; annual reporting to management |
| L2 | Mandatory; defined set of KPIs; dashboard recommended; half-yearly reporting |
| L3 | Mandatory; complete KPIs; dashboard configured; automatic alerts; quarterly reporting to executive management |

---

## 3. KPI categories {#3-categorias-de-kpis}

Security governance KPIs must cover the following categories:

### 3.1 Compliance and traceability {#31-conformidade-e-rastreabilidade}

| KPI | Description | Target |
|---|---|---|
| % of applications with an up-to-date compliance repository | Applications with a valid repository (last review within the period) | > 90% |
| % of L2/L3 applications with a designated Security Champion | Applications with a formal owner and training completed | 100% |
| % of SbD-ToE chapters with verified compliance per application | Average coverage of the applicable chapters | > 80% |
| % of active exceptions within the TTL | Non-expired exceptions as a proportion of the active total | > 95% |
| % of exceptions resolved within the deadline | Exceptions with remediation completed within the approved deadline | > 70% |

### 3.2 Remediation quality and speed {#32-qualidade-e-velocidade-de-remediação}

| KPI | Description | Target |
|---|---|---|
| MTTR by severity | Average time between identification and remediation of findings | Critical ≤ 7 days; High ≤ 30 days |
| Finding recurrence rate | % of findings of the same type that reappear within 90 days | &lt; 10% |
| % of Critical/High findings remediated within the SLA | Compliance with the SLAs defined in the testing policy | > 90% |
| Rate of active exceptions vs. total findings | Indicator of accumulation of accepted risk | Downward trend |

### 3.3 Operations and incident response {#33-operações-e-resposta-a-incidentes}

| KPI | Description | Target |
|---|---|---|
| % of P1/P2 alerts responded to within the SLA | Compliance with the SLAs of the alert management policy | > 95% |
| True positive rate (P1/P2 alerts) | % of P1/P2 alerts that correspond to real incidents | > 70% |
| Number of security incidents per period | Trend of occurrences | Downward or stable trend |
| Mean time to detect (MTTD) | Time between the start of the incident and its detection | Internal reference by type |
| Mean time to resolve (incident MTTR) | Time between detection and resolution of incidents | Internal reference by severity |
| % of incidents with a post-mortem held within the deadline | Post-mortems completed ≤ 5 working days after resolution | 100% for P1; > 80% for P2 |

### 3.4 Pipeline and development {#34-pipeline-e-desenvolvimento}

| KPI | Description | Target |
|---|---|---|
| % of pipelines with active security gates | Proportion of pipelines with SAST, SCA and secrets scanning | > 95% at L2/L3 |
| Pipeline blocking rate due to security | % of executions blocked by a security gate | Internal reference; downward trend desirable |
| % of artefacts with a generated and signed SBOM | SBOM generation coverage | 100% at L3 |
| % of secrets in a vault vs. hardcoded secrets detected | Proportion of secrets managed correctly | Hardcoded = 0 |

### 3.5 Suppliers and third parties {#35-fornecedores-e-terceiros}

| KPI | Description | Target |
|---|---|---|
| % of active suppliers with up-to-date due diligence | Suppliers within the reassessment cycle | 100% |
| % of contracts with compliant security clauses | Contracts that include the mandatory minimum clauses | 100% at L2/L3 |
| % of contractors with technical onboarding completed | Active contractors with a validated training track and quiz | 100% |
| Supplier incident notification SLA | Rate of compliance with the contractual notification deadline | > 90% |

### 3.6 Training and upskilling {#36-formação-e-capacitação}

| KPI | Description | Target |
|---|---|---|
| Mandatory training completion rate | % of staff with a completed training track | > 90% |
| Training quiz pass rate | % of participants with a score ≥ 80% | > 85% |
| % of Security Champions with up-to-date training | Champions with valid, non-expired training | 100% |

---

## 4. Data sources and collection {#4-fontes-de-dados-e-recolha}

| Category | Primary sources | Responsible for collection |
|---|---|---|
| Compliance and traceability | Compliance repositories; GRC tool; owner records | GRC / AppSec |
| Remediation | DefectDojo or a centralised findings platform; tickets | AppSec / DevOps |
| Operations and incidents | SIEM; on-call platform (PagerDuty/OpsGenie); IRP records | SOC / GRC |
| Pipeline and development | CI/CD platform; pipeline records; signed artefacts | DevOps / AppSec |
| Suppliers | Contract records; due diligence results; onboarding | GRC / Procurement |
| Training | LMS; completion records; quiz scores | GRC / HR |

---

## 5. Collection and reporting cadence {#5-cadência-de-recolha-e-reporte}

| Activity | L1 | L2 | L3 |
|---|---|---|---|
| Automatic collection of metrics | Not applicable | Recommended (monthly) | Mandatory (continuous + consolidated monthly) |
| Dashboard updated | Not applicable | Monthly | Continuous |
| Report for Tech Lead / AppSec | Not applicable | Monthly | Monthly |
| Report for CISO / Executive Management | Annual | Half-yearly | Quarterly |
| Report for Audit | Annual | Annual | Half-yearly (or on request) |

---

## 6. Intervention thresholds {#6-thresholds-de-intervenção}

Certain deviations in the KPIs must trigger immediate corrective actions, regardless of the regular reporting cycle:

| Condition | Action |
|---|---|
| % of P1 alerts responded to within the SLA &lt; 80% | Immediate review of the on-call and escalation process |
| Finding recurrence rate > 25% | Review of the remediation process and of the development guidelines |
| % of expired exceptions without reassessment > 10% | Audit of exceptions; escalation to decision-makers |
| Active contractor without completed onboarding | Access blocked until onboarding is completed |
| Active supplier with expired due diligence at L3 | Immediate review; suspension of new access until reassessment |
| MTTD of a P1 incident > 24 hours | Review of detection rules and monitoring coverage |

---

## 7. Maturity assessment {#7-avaliação-de-maturidade}

In addition to the operational KPIs, the organisation must periodically assess the maturity level of the security programme with reference to recognised frameworks:

| Framework | Dimensions assessed | Cadence |
|---|---|---|
| OWASP SAMM | Governance, Design, Implementation, Verification, Operations | Annual |
| NIST SSDF | Prepare, Protect, Produce, Respond | Annual |
| BSIMM (optional) | Benchmark against industry | Every 2 years |

The result of the maturity assessment must:

- Be documented and compared with the previous assessment (evolution)
- Identify the dimensions with the largest gap against the organisation's maturity target
- Give rise to an improvement plan with priorities, owners and deadlines
- Be presented to executive management as part of the annual security report

:::note
The maturity assessment does not replace the operational KPIs - they are complementary perspectives. The KPIs measure current performance; the maturity assessment measures the installed capability to sustain that performance over time.
:::

---

## 8. Report format and distribution {#8-formato-e-distribuição-de-relatórios}

| Report type | Recipients | Minimum content |
|---|---|---|
| Monthly operational report | AppSec, Tech Leads, DevOps | Status of operational KPIs; deviations; actions in progress |
| Quarterly / half-yearly report | CISO, Executive Management | Aggregated view of the portfolio; trends; strategic KPIs; action plan |
| Report for audit | Internal / external auditors | Compliance status per chapter; evidence; active exceptions; history |
| Continuous dashboard | AppSec, GRC, CISO | Real-time status of critical operational KPIs; active alerts |

---

## 9. Responsibilities {#9-responsabilidades}

| Role | Responsibility |
|---|---|
| GRC / Compliance | Define and maintain the set of KPIs; coordinate data collection; produce reports; manage threshold alerts |
| AppSec Engineer | Provide data on findings, pipelines and technical compliance; validate the quality of the metrics; support the maturity assessment |
| DevOps / SRE | Provide data on pipelines, alerts and operations; configure collection automation |
| Security Champion | Provide the application's compliance data; update the compliance repository |
| CISO / Executive Management | Analyse reports; approve KPI targets; take data-driven strategic decisions; ensure resources for corrective actions |

---

## 10. Review and audit of this policy {#10-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- A significant change to the security programme that makes the current KPIs inadequate
- A maturity assessment result that identifies gaps in the defined KPIs
- A regulatory change that imposes new measurement or reporting requirements

---

## 11. Normative and technical references {#11-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 14 - Governance and Contracting | US-05: governance KPIs; US-11: consolidation of KPIs and maturity |
| Organisational Traceability Policy (`34_policy-rastreabilidade-organizacional.md`) | Data source for compliance KPIs |
| Alert Management Policy (`31_policy-gestao-alertas.md`) | Alert quality KPIs and SLAs |
| IRP Policy (`32_policy-irp.md`) | Incident response KPIs (MTTD, MTTR) |
| OWASP SAMM v2 | Software Assurance Maturity Model - maturity framework |
| NIST SSDF (SP 800-218) | Secure Software Development Framework - practices and maturity |
| BSIMM | Building Security In Maturity Model - industry benchmark |
| ISO/IEC 27001 - A.18 | Compliance; security reviews and audits |
| DORA - Art. 6, 17 | ICT risk management and reporting requirements |
| NIS2 - Art. 21 | Security measures and governance obligations |
