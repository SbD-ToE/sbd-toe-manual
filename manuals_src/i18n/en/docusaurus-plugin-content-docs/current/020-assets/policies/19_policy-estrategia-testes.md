---
id: policy-estrategia-testes
title: Security Testing Strategy Policy
description: Organisational policy that defines the requirements for the security testing strategy throughout the application lifecycle, including SAST, DAST, SCA, IAST, fuzzing and manual testing, with mandatory gates, finding triage SLAs and centralised management of results, proportional to the criticality level (L1, L2, L3).
tags: [policy, testes de segurança, SAST, DAST, IAST, SCA, fuzzing, gates, findings, triagem, SLA, cap10, L1, L2, L3, governance, DevSecOps]
grupo: testes
sidebar_position: 19
translation:
  source_locale: pt
  source_path: 020-assets/policies/19_policy-estrategia-testes.md
  source_sha256: c347475e642b983ed20ecbb23ec9ea6b463efdc08bb5da7c2eee079ee2eefa32
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 4457112a7ff3f6e1bddb545cb9e2edd4a866d26b1c68c8c8e983ac8c8ad5e072
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, avaliacao, cycle_iteration, framework_source_corpus, lifecycle_phase, llm, requirement_runtime, role_tech_lead, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: 11ab60cf00ad1cc8d2b92b29aacda14b014b8500df7ae344df638b0af44aceb2
  translated_at: 2026-09-26T14:10:54Z
  stamped_at: 2026-09-26T18:36:55Z
  reviewed_by: null
---

# Security Testing Strategy Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for the **security testing strategy** throughout the lifecycle of applications classified as L1, L2 or L3.

Security testing is not a phase - it is a set of complementary practices that must be integrated into every stage of the SDLC, from code review to validation in production. Each technique has a distinct scope and distinct limitations: SAST finds patterns in static code but does not see runtime behaviour; DAST validates the running application but does not cover every code path; fuzzing uncovers unexpected conditions that neither of the others finds systematically. Effective coverage requires a composite strategy, proportional to risk.

The objective of this policy is to ensure that:

- Security test coverage is proportional to the application's criticality level
- Automated gates block serious regressions before promotion to production
- Findings are managed centrally, with formal triage and a defined SLA
- Test reports are archived as auditable evidence per release

---

## 2. Testing techniques and applicability {#2-técnicas-de-teste-e-obrigatoriedade}

### 2.1 Applicability matrix by level {#21-matriz-de-obrigatoriedade-por-nível}

| Technique | L1 | L2 | L3 |
|---|---|---|---|
| **SAST** (static analysis) | Recommended | Mandatory | Mandatory |
| **Secret detection** | Mandatory | Mandatory | Mandatory |
| **SCA** (software composition) | Mandatory (alert) | Mandatory (gate) | Mandatory (gate) |
| **DAST** (dynamic analysis) | Recommended | Mandatory in staging | Mandatory in staging + coverage criteria |
| **IAST** (runtime instrumentation) | Optional | Recommended | Recommended |
| **Fuzzing** | Optional | Recommended (critical endpoints) | Mandatory (public endpoints + parsing) |
| **Manual security testing** | Not mandatory | Recommended per release | Mandatory per major release |
| **PenTesting** | Not mandatory | Recommended annually | Mandatory (see PenTesting Policy) |

### 2.2 SAST {#22-sast}

- Run on every PR and every integration build
- Configured with rulesets derived from the development guidelines for each stack
- Findings classified by severity (Critical, High, Medium, Low, Informational)
- Inline suppressions require a justification comment and are reported as a metric

### 2.3 DAST {#23-dast}

- Run in the staging environment after each successful promotion
- Requires an environment with authentication configured so that protected endpoints are covered
- Scope defined to avoid testing against real external systems (mocks or sandbox for integrations)
- Minimum endpoint coverage per release documented and measured

### 2.4 Fuzzing {#24-fuzzing}

- Focused on input parsers, upload endpoints and APIs that accept complex structures
- Run as a nightly job or per release, not necessarily on every PR
- Findings classified and integrated into the centralised management system

---

## 3. Security gates by level {#3-gates-de-segurança-por-nível}

Blocking thresholds must be documented and versioned in `gates-config.yaml` or equivalent:

| Gate | L1 | L2 | L3 |
|---|---|---|---|
| SAST Critical/High | Alert | Blocks merge | Blocks merge |
| SAST Medium | Not applicable | Alert | Blocks merge |
| Secret detection (any finding) | Blocks | Blocks | Blocks |
| SCA High/Critical CVE without exception | Alert | Blocks promotion | Blocks promotion |
| DAST High/Critical in staging | Not applicable | Blocks promotion to production | Blocks promotion to production |
| DAST coverage below threshold | Not applicable | Alert | Blocks (threshold: 80% of endpoints) |
| Fuzzing with a confirmed crash | Not applicable | Blocks release | Blocks release |

:::warning
A gate configured in alert-only mode at L2/L3 must be recorded as a formal exception with an expiry date. Expired exceptions to security gates without reassessment are treated as non-compliance.
:::

---

## 4. Centralised management of findings {#4-gestão-centralizada-de-findings}

### 4.1 Unified platform {#41-plataforma-unificada}

All SAST, DAST, IAST, SCA and fuzzing findings must be consolidated in a centralised platform (e.g. DefectDojo, SonarQube Security Dashboard, GitHub Security, GitLab Security Dashboard), with:

- [ ] Deduplication of findings with the same origin across multiple tools
- [ ] Unified metadata: CVE/CWE, severity, tool, commit, module, status
- [ ] Status history (open, in progress, resolved, accepted, suppressed)
- [ ] Traceability between the finding and the resolving PR/commit

### 4.2 Formal triage {#42-triagem-formal}

Each blocking finding must be triaged with a documented decision:

| Decision | Condition | Requirement |
|---|---|---|
| **FIX** | Valid and exploitable finding | Resolution estimate; ticket created |
| **ACCEPT** | Risk assessed and explicitly accepted | Formal exception in accordance with the Exception Policy |
| **SUPPRESS (FP)** | False positive demonstrated | Technical evidence; AppSec approval |
| **DEFER** | Resolution postponed with justification | Deadline defined; temporary risk acceptance |

### 4.3 Triage and resolution SLAs {#43-slas-de-triagem-e-resolução}

| Severity | Triage SLA | Resolution SLA (L2) | Resolution SLA (L3) |
|---|---|---|---|
| Critical | 24 hours | 7 days | 3 days |
| High | 48 hours | 30 days | 15 days |
| Medium | 5 working days | 90 days | 45 days |
| Low | 10 working days | 180 days | 90 days |

---

## 5. Traceability and evidence per release {#5-rastreabilidade-e-evidência-por-release}

For each release, there must be evidence of the tests performed:

- [ ] SAST, DAST, SCA and fuzzing reports (where applicable) archived as pipeline artefacts
- [ ] Release checklist completed with the status of each gate
- [ ] Critical findings with documented status (fixed, approved exceptions)
- [ ] DAST coverage measured and recorded
- [ ] Formal release approval with reference to the reports (see Secure Release Policy)

---

## 6. Handling false positives {#6-tratamento-de-falsos-positivos}

False positives (FP) are inevitable in any static or dynamic analysis tool. The process for suppressing a finding as an FP must be formal:

- [ ] Technical evidence of non-exploitability documented (code path analysis, failed proof of concept)
- [ ] Approval by an AppSec Engineer for High/Critical findings
- [ ] Record of the suppression in the centralised platform with reason, responsible person and date
- [ ] Inline suppressions in the code (e.g. `# nosec`, `// noqa`) linked to the identifier of the suppressed finding and subject to periodic review

FP metrics per tool must be tracked in order to calibrate the scanners' configurations.

---

## 7. *Eval suites* for AI agents {#eval-suites-agentes}

When the system includes an AI agent in operation (or when an agent is part of the testing process — e.g. an automated PR auditor), **eval suites** are included among the mandatory testing techniques. They do not replace SAST/DAST/SCA — they cover the agentic slice, which those tools do not see.

### 7.1 Minimum composition {#71-composição-mínima}

For each AI agent at level A1+ in the project:

| Component | A1 | A2 | A3 | A4 |
|---|:--:|:--:|:--:|:--:|
| **Prompt / skill regression tests** | Recommended | Mandatory | Mandatory | Mandatory |
| **Abuse / red-team corpus** (*prompt injection*, *jailbreak*) | — | Recommended | Mandatory | Mandatory |
| **Drift detection** between model / prompt versions | — | Recommended | Mandatory | Mandatory (short window) |
| **A/B testing** before promoting a skill / system prompt | — | Recommended | Mandatory | Mandatory |
| **Test telemetry** correlated with real signals in production (Ch. 12) | — | — | Recommended | Mandatory |

### 7.2 Operation {#72-operação}

- *Eval suite* versioned in VCS, with the `eval_run_id` archived at each release and linked to the `mandate_ref` (Policy 38).
- Runs in CI before the *merge* of changes to *system prompts* / *skill files* / *agent files*, and after a *bump* of the model version (cross-link Ch. 07 US-19 and Ch. 06 §prompts-as-code).
- An *eval failure* blocks the *merge* or forces a drop in autonomy level until it is resolved.
- Coverage must be proportional to the declared autonomy level — raising the level without a matching suite is prohibited.

### 7.3 Anti-patterns {#73-anti-padrões}

- ❌ "*Vibe checks*" as the only validation.
- ❌ A suite that never fails — adversarial coverage is missing.
- ❌ Aggregated metrics without inspection of the critical cases.
- ❌ A suite in a repository separate from the skill/prompt — silent *drift*.

> 📌 Operational detail in [Ch. 10 — AI in testing §C5](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites).

---

## 8. Responsibilities {#8-responsabilidades}

| Role | Responsibility |
|---|---|
| Developer | Run local analysis before submitting a PR; triage SAST findings in PRs; do not suppress without a record |
| AppSec Engineer | Define and calibrate thresholds; manage the centralised findings platform; approve High/Critical FP suppressions; define the DAST strategy |
| DevOps / SRE | Integrate tools into the pipeline; configure DAST jobs in staging; archive reports |
| Tech Lead | Ensure findings are resolved within SLA; escalate conflicts between timeline and gates |
| Product Manager | Approve risk acceptance for findings that cannot be resolved before the release |

---

## 9. Review and audit of this policy {#9-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- A vulnerability introduced into production that should have been detected by one of the techniques covered
- Adoption of a new testing technique or tool with an impact on the strategy
- A change of thresholds with a material impact on the build blocking rate

---

## 10. Normative and technical references {#10-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 10 - Security Testing | Strategy, gates, findings, triage, SLA; **C5 — eval suites for agents** |
| SbD-ToE Ch. 07 - Secure CI/CD | SAST, DAST and SCA integrated into the pipeline; US-19 eval gates |
| SbD-ToE Ch. 02 — Requirements ([`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) | Justification of the autonomy level evidenced by an eval suite |
| DAST and Fuzzing Policy (`01_policy-dast-fuzzing.md`) | Specific DAST and Fuzzing requirements |
| Secure Release Policy (`20_policy-release-seguro.md`) | Release checklist and approval based on the tests |
| Policy 38 — AI Agent Mandates | Eval suite linked to `mandate_ref` |
| OWASP Testing Guide (v4.2) | Reference methodology for security testing |
| OWASP DAST Guide | Good practices for dynamic analysis |
| OWASP Top 10 for LLM Applications (2025) | LLM01 prompt injection; LLM06 excessive agency — red-team corpus |
| NIST SP 800-115 | Technical Guide to Information Security Testing |
| NIST AI RMF 1.0 (MEASURE-2.x) | Continuous assessment of AI systems in production |
| SSDF PW.8.2 | Test, evaluate, and remediate the software |
| DefectDojo | Reference platform for centralised management of findings |
