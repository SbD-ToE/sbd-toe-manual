---
id: policy-revisao-codigo
title: Code Review Policy
description: Organisational policy that defines the requirements for code review as a security control point, including a mandatory checklist, approval criteria, reviewer roles, minimum coverage and integration with automated tools, proportional to the criticality level (L1, L2, L3).
tags: [policy, code review, revisão de código, checklist, PR, SAST, desenvolvimento seguro, cap06, L1, L2, L3, governance]
grupo: desenvolvimento
sidebar_position: 15
translation:
  source_locale: pt
  source_path: 020-assets/policies/15_policy-revisao-codigo.md
  source_sha256: b5c6e5bebc459305813c484389a69933bde0fe5465731680340ba0673a9ffcb7
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: c9987075f5743283f244de979412ea57f3b6b2945b2e7d88725ebbfbe8f69bd0
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, discipline, provenance, role_tech_lead, sbdtoe_sbd, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 1242300918c450ee45119d249cdb72a718ed02c0fb103efc0f0427408fc75e6a
  translated_at: 2026-09-26T14:10:51Z
  stamped_at: 2026-09-26T18:36:52Z
  reviewed_by: null
---

# Code Review Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for **code review as a formal security control point**, applicable to all pull requests (PRs) that introduce changes to production code, security configuration or infrastructure as code.

Code review is, at the same time, a technical quality control and a vulnerability detection mechanism. When systematised with a checklist and clear approval criteria, it complements automated tools (SAST, linters) with human judgement on business logic, authorisation flows and design decisions that tools cannot assess reliably.

The objective of this policy is to ensure that:

- Every relevant PR is reviewed by at least one reviewer with adequate technical competence
- The review includes security verification based on a standardised checklist
- Approval is recorded in a traceable and auditable way
- Human review is complemented - not replaced - by automated analysis

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

| Type of change | L1 | L2 | L3 |
|---|---|---|---|
| Business logic code | Recommended | Mandatory (1 reviewer) | Mandatory (2 reviewers) |
| Authentication, authorisation, sessions | Mandatory | Mandatory + AppSec | Mandatory + AppSec |
| Handling of sensitive data or PII | Mandatory | Mandatory + AppSec | Mandatory + AppSec |
| Security configuration (CORS, headers, TLS) | Mandatory | Mandatory + AppSec | Mandatory + AppSec |
| IaC with a security impact | Recommended | Mandatory + DevOps | Mandatory + DevOps + AppSec |
| New external integration | Recommended | Mandatory | Mandatory + AppSec |
| Change to the CI/CD pipeline | Recommended | Mandatory | Mandatory + AppSec |
| **Prompts, *skill files*, *agent files* and *rules*** (`.claude/skills/*`, `.claude/agents/*`, `.cursorrules`, `.github/copilot-instructions.md`, `AGENTS.md`) | Recommended | Mandatory | Mandatory + AppSec |
| **Change to the `tools_allowlist` or *scopes* of an AI agent** | Mandatory + AppSec | Mandatory + AppSec | Mandatory + AppSec + GRC |
| **AI agent mandate** (Policy 38) | Tech Lead approval | Tech Lead + AppSec approval | Tech Lead + AppSec + GRC approval; A4 with `CISO` |

> 📌 **On prompts and *skill files* as code.** These artefacts decide what the assistant knows, which *tools* it can invoke and how it interacts with the organisation. They are treated with the same review discipline that applies to code — including *secret scanning* and heightened attention to changes to `tools_allowlist`/*scopes*. See the operational detail in [Ch. 06 — Prompts as code](/sbd-toe/sbd-manual/desenvolvimento-seguro/addon/genia-e-seguranca#prompts-como-codigo) and in [Policy 38 — AI Agent Mandates](./policy-mandates-agentes).

---

## 3. Minimum security checklist {#3-checklist-de-segurança-mínima}

Each PR must be assessed against the following control points. The checklist must be included in the repository's PR template and completed by the reviewer before approval:

### 3.1 Authentication and authorisation {#31-autenticação-e-autorização}
- [ ] Endpoints protected with authentication appropriate to the context
- [ ] Authorisation logic verified - not just authentication
- [ ] No horizontal or vertical privilege escalation
- [ ] Tokens, sessions or credentials not exposed in logs or responses

### 3.2 Input and output validation {#32-validação-de-input-e-output}
- [ ] Inputs validated and sanitised before processing
- [ ] No direct concatenation of input into queries, commands or templates (SQLi, CMDi, SSTI)
- [ ] Output encoded appropriately for the context (HTML, JSON, SQL) to prevent XSS

### 3.3 Management of secrets and sensitive data {#33-gestão-de-segredos-e-dados-sensíveis}
- [ ] No secret, password, key or token hardcoded in the code or configuration
- [ ] Sensitive data or PII not exposed in logs, traces or error responses
- [ ] Classified data handled according to the assigned classification

### 3.4 Dependencies and imports {#34-dependências-e-imports}
- [ ] New dependencies approved in accordance with the Dependency Management Policy
- [ ] Library imports validated - no copying of external code without provenance

### 3.5 Error handling and logging {#35-tratamento-de-erros-e-logging}
- [ ] Errors handled without exposing technical information to the user (stack traces, paths, versions)
- [ ] Relevant security events logged (access attempts, authorisation errors)
- [ ] Logging without exposure of sensitive data

### 3.6 Cryptography and communications {#36-criptografia-e-comunicações}
- [ ] Cryptographic algorithms approved by the organisation (no MD5, SHA-1, DES, RC4)
- [ ] External communications over TLS; no disabled certificate validation

### 3.7 Patterns and anti-patterns {#37-padrões-e-anti-patterns}
- [ ] No dangerous patterns detected by SAST/linters
- [ ] No unjustified inline suppressions (`# noqa`, `// nosec`, `// nolint`)
- [ ] Concurrency or shared-state logic without obvious race conditions

---

## 4. Approval criteria {#4-critérios-de-aprovação}

A PR may only be approved and merged when:

- [ ] All critical checklist items have been verified
- [ ] Blocking SAST/linter findings are resolved or have an approved formal exception
- [ ] The minimum number of approving reviewers has been reached (as per the table in section 2)
- [ ] No reviewer has approved their own code (self-approval prohibited)

:::warning
Approval of a PR is not confirmation that the code is free of vulnerabilities - it is confirmation that it has been subjected to competent and systematic review. Responsibility for security is shared between the author and the reviewers.
:::

---

## 5. Reviewers and competence {#5-reviewers-e-competência}

### 5.1 Reviewer requirements {#51-requisitos-de-reviewer}

| Level | Minimum reviewer | Additional reviewer where applicable |
|---|---|---|
| L1 | Developer with competence in the stack | - |
| L2 | Senior Developer or Tech Lead | AppSec Engineer for security changes |
| L3 | Tech Lead | AppSec Engineer mandatory for security changes |

### 5.2 Self-review {#52-self-review}

Self-review (approval by the author themselves) is prohibited regardless of the level. In one-person teams, the peer review process must be followed with an external member or with the AppSec Engineer.

### 5.3 Reviewer rotation {#53-reviewer-rotation}

At L3, reviewer rotation is recommended to avoid systematic blind spots. The same author/reviewer combination must not be the only valid one for the same module on a continuing basis.

---

## 6. Integration with automated tools {#6-integração-com-ferramentas-automáticas}

Human review complements - it does not replace - automated analysis. The pipeline must run the following automated checks before or during the PR:

| Verification | When it runs | Blocks merge at L2/L3? |
|---|---|---|
| Security linters (ESLint Security, Bandit, etc.) | On every push to the PR | Yes, for critical findings |
| SAST (Semgrep, CodeQL, SonarQube) | On every push to the PR | Yes, for High/Critical findings |
| Secret detection (TruffleHog, Gitleaks) | On every push to the PR | Yes, for any finding |
| SCA (new dependencies) | When the manifest is changed | Yes, in accordance with the Dependency Management Policy |

The results of the automated checks must be visible in the PR (comment or status check) before the reviewer starts the human review.

---

## 7. Traceability and evidence {#7-rastreabilidade-e-evidência}

Each review must produce traceable evidence:

- [ ] Approval recorded on the version control platform (PR approved, not just commented on)
- [ ] Checklist completed and visible in the PR (template or structured comment)
- [ ] Review comments with corrective actions recorded and resolved before the merge
- [ ] Review history retained in accordance with the Traceability Policy

---

## 8. Educational dimension {#8-dimensão-educativa}

Code review is also a knowledge transfer mechanism. Reviewers must:

- Explain the problems found with reference to the corresponding guideline or CWE
- Suggest the secure alternative, not just point out the problem
- Avoid approvals without comment when there are identified points for improvement

Recurring vulnerability patterns identified in PRs must be reported to the AppSec Engineer so that the guidelines and the SAST configurations can be updated.

---

## 9. Responsibilities {#9-responsabilidades}

| Role | Responsibility |
|---|---|
| Developer (author) | Submit the PR with a completed checklist; resolve findings before requesting review |
| Developer / Tech Lead (reviewer) | Review with the checklist; record comments; approve only when the criteria are met |
| AppSec Engineer | Review PRs with security changes at L2/L3; update the checklist with emerging patterns |
| Scrum Master / Tech Lead | Ensure that the process is followed; manage PRs with no reviewer available |
| DevOps / SRE | Configure branch protection rules that enforce the minimum number of approvals |

---

## 10. Review and audit of this policy {#10-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Vulnerability introduced into production that should have been detected in code review
- Change to the development guidelines that introduces new checklist items
- Change to the SAST tools with an impact on the pipeline gates

---

## 11. Normative and technical references {#11-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 06 - Secure Development | Code review as a security control, L1-L3 proportionality |
| Secure Development Guidelines Curation Policy (`14_policy-guidelines-desenvolvimento.md`) | Checklist derived from the guidelines per stack |
| Secure CI/CD Policy (`17_policy-cicd-seguro.md`) | Integration of SAST/linters into the PR pipeline |
| OWASP Code Review Guide | Reference for secure code review good practices |
| CWE Top 25 | Implementation weaknesses to check in review |
| NIST SP 800-218 (SSDF) PW.2 | Review the software design to address security requirements |
| SAFECode Fundamental Practices | Peer code review as a fundamental security practice |
