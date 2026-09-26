---
id: policy-aprovacao-release
title: Release Approval Policy
description: Organisational policy that defines the formal go/no-go decision process for software releases, including approval authorities by criticality level, separation between automatic signal and human decision, formal acceptance of residual risk and recording of evidence, proportional to the criticality level (L1, L2, L3).
tags: [policy, release, aprovação, go/no-go, risco residual, sign-off, alçadas, cap10, cap11, L1, L2, L3, governance]
grupo: pipeline-entrega
sidebar_position: 26
translation:
  source_locale: pt
  source_path: 020-assets/policies/26_policy-aprovacao-release.md
  source_sha256: 7bea1a5c0c5eda9e32b4bb78b4390b7499d4fb727c4d1bebdb6eeb54114a10e3
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 7845272c13531fba1558d4d1a4326d6e0663257baa4b1898a302bf9d4d29ef6b
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bc04ded428e40ee1c214f8535dfb1904655b64166d0aa82b5df521e4230b8cb0
  glossary_keys: [alcada, audit_trail, avaliacao, framework_source_corpus, risk_level, sbdtoe_sbd, traceability]
  glossary_sha256: de7e41b4e7023c0a4113d6e80bb15edbec587fd0b7b37d57ad3c43cc7be4ffcc
  translated_at: 2026-09-26T14:10:58Z
  reviewed_by: null
---

# Release Approval Policy

## 1. Objective {#1-objetivo}

This policy defines the formal **go/no-go decision process for software releases**, clarifying the approval authorities, the acceptance criteria, the separation between automatic signal and human decision, and the recording of evidence.

The approval of a release is a risk decision - not a formality. The result of the automatic gates (SAST, DAST, SCA) is a signal that informs the decision, but does not replace it. The decision requires an identified human owner, who explicitly accepts the residual risk and the operational risk of promoting the version, on the basis of the available evidence.

The objective of this policy is to ensure that:

- The go/no-go decision is taken by a person with an approval authority appropriate to the risk level of the application
- The decision is recorded with verifiable evidence (who, when, on what basis)
- Residual risk is accepted explicitly, never by omission
- The distinction between automatic signal and human decision is clear and auditable

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

| Level | Applicability |
|---|---|
| L1 | Recommended; informal approval by the Tech Lead |
| L2 | Mandatory; formal recorded approval; explicit acceptance of residual risk if applicable |
| L3 | Mandatory; dual approval; immutable record; acceptance of residual risk with CISO approval authority |

---

## 3. Distinction between automatic signal and human decision {#3-distinção-entre-sinal-automático-e-decisão-humana}

The pipeline produces **signals** - results of automatic gates that inform the security state of the release. These signals are not decisions:

| Signal (automatic) | What it indicates | Does not decide |
|---|---|---|
| Pre-release gate APPROVED | Minimum criteria met | That the release is ready for production |
| Pre-release gate REJECTED | Minimum criteria not met | Automatic block, but the decision to resolve/grant an exception is human |
| Quality score (e.g. SonarQube quality gate) | Code quality level | Approval of the release |

Promotion to production always requires a human decision recorded by name, even when the automatic gate returns APPROVED. A "green score" is not an approval.

---

## 4. Approval authorities by level {#4-alçadas-de-aprovação-por-nível}

### 4.1 Go approval {#41-aprovação-de-go}

| Level | Minimum approver(s) | Condition |
|---|---|---|
| L1 | Tech Lead | Automatic gate APPROVED + checklist review |
| L2 | Tech Lead + AppSec Engineer | Automatic gate APPROVED + checklist verified + residual risk assessed |
| L3 | Tech Lead + AppSec Engineer + Security Officer (or delegated CISO) - dual approval | Automatic gate APPROVED + checklist verified + formal acceptance of residual risk |

### 4.2 No-go approval with exception {#42-aprovação-de-no-go-com-exceção}

When the automatic gate returns REJECTED but there is a business justification for proceeding (e.g. urgent production fix, regulatory deadline), the no-go may be overridden with:

| Level | Override approval authority | Additional requirements |
|---|---|---|
| L1 | Tech Lead | Documented justification; remediation plan with a deadline |
| L2 | AppSec Engineer + Tech Lead | Technical justification; formal exception approved; remediation plan |
| L3 | CISO (or delegated Security Officer) + AppSec Engineer | Technical and business justification; formal exception; remediation plan with a date; notification to GRC |

:::warning
Overriding a rejected gate does not eliminate the risk - it postpones its resolution. Every approval with override must be treated as an acceptance of residual risk with a maximum TTL equal to the deadline of the remediation plan.
:::

---

## 5. Formal acceptance of residual risk {#5-aceitação-formal-de-risco-residual}

When a release is approved with open findings (with formal exceptions), the approver must explicitly record the acceptance of residual risk:

- [ ] Identification of the open findings and reference to the approved exceptions
- [ ] Assessment of the potential impact if the risk is exploited
- [ ] Business justification for proceeding with residual risk
- [ ] Active compensating controls that reduce the risk of exploitation
- [ ] Resolution deadline with a defined owner
- [ ] Identity of the approver and timestamp

The acceptance of residual risk is a formal declaration - not an optional field of the checklist.

---

## 6. Approval record {#6-registo-de-aprovação}

Each go/no-go decision must be recorded with the following minimum fields:

| Field | Description |
|---|---|
| Release / version | Semantic tag or release identifier |
| Target environment | staging / production |
| Decision | GO / NO-GO / GO with override / GO with residual risk |
| Approver(s) | Identity(ies) with individual timestamp |
| Reference to the gate report | Link or identifier of the pre-release gate report |
| Reference to the artefact | SHA256 digest of the approved artefact |
| Residual risk accepted | Yes / No; reference to the exceptions if yes |
| Notes | Any additional context relevant to the decision |

At L3, the record must be immutable (WORM or equivalent) and retained in accordance with the Traceability Policy.

---

## 7. Emergency releases {#7-releases-de-emergência}

Situations of an active incident in production may require an urgent fix release outside the normal process. In these cases:

- [ ] Emergency approval obtained before the deploy (even if through informal channels - it must be formalised a posteriori within a maximum of 24h)
- [ ] Security gates executed even in accelerated mode - no complete bypass of SAST and secret detection
- [ ] The emergency release is marked as such in the record with justification
- [ ] Post-mortem carried out after resolution, with an analysis of the process and preventive measures

---

## 8. Responsibilities {#8-responsabilidades}

| Role | Responsibility |
|---|---|
| Tech Lead | Coordinate the release process; verify the checklist; approve at L1/L2 |
| AppSec Engineer | Verify the status of findings and exceptions; approve at L2/L3; validate residual risk |
| Security Officer / CISO | Approve releases with significant residual risk at L3; be notified of overrides |
| Product Manager | Present the business justification when there is a conflict between deadline and security |
| DevOps / SRE | Execute the deploy after recorded approval; do not start a deploy without approval |
| GRC / Compliance | Audit approval records; verify traceability; compliance reports |

---

## 9. Review and audit of this policy {#9-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Incident originating in a release approved with undocumented residual risk
- Change to the organisation's governance approval authorities
- Regulatory change that imposes additional formal approval requirements

---

## 10. Normative and technical references {#10-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 10 - Security Testing | Go/no-go criteria and acceptance of residual risk |
| SbD-ToE Ch. 11 - Secure Deployment | Deployment approval gates |
| SbD-ToE Ch. 07 - Secure CI/CD | Separation between automatic signal and human decision |
| Secure Release Policy (`20_policy-release-seguro.md`) | Pre-release gate and security checklist |
| Secure Deployment Policy (`25_policy-deploy-seguro.md`) | Execution of the deploy after approval |
| Exception Management Policy (`05_policy-gestao-excecoes.md`) | Active exceptions referenced in the acceptance of residual risk |
| ISO/IEC 27001 - A.12.5 | Control of operational software |
| ITIL Release Management | Release management framework |
