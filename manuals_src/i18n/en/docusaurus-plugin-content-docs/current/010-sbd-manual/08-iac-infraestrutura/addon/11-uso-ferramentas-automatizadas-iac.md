---
id: uso-ferramentas-automatizadas-iac
title: Use of Automated and Assisted Tools in IaC Authoring
description: Prescriptive rules for the secure use of automation/assistance in writing and changing IaC, with validations and evidence by risk level
tags: [tipo:addon, iac, automacao, assistencia, validacao, evidencias, supply-chain]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/08-iac-infraestrutura/addon/11-uso-ferramentas-automatizadas-iac.md
  source_sha256: e8be8f104a89a252ea0376ae926e1641c62cc3dc8b6bb0aa24747ce7d60aa4b0
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 10d81e2bd91b687f9b5cc5cf53c99bd58480343069c72cec8cf636c9c574de31
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [audit_trail, risk_level, traceability, validation_evaluation]
  glossary_sha256: 6b14db5feb320bfd298696742b34fdae566e2d885d9a44525f2ac81503a44c7a
  translated_at: 2026-09-26T09:25:39Z
  reviewed_by: null
---

# Use of Automated and Assisted Tools in IaC Authoring

Writing and changing Infrastructure as Code is frequently supported by **automation** (templates, generators, normalisers, snippets, scripts) and by **assisted mechanisms** (suggestions and composition).  
These tools increase productivity, but introduce specific risks: changes with low explainability, insecure defaults, excessive permissions, unexpected resources and involuntary exposure of sensitive information.

This document defines **what is acceptable**, **what is prohibited**, and **which validations and evidence are mandatory** to ensure that automation/assistance does not reduce control, traceability and auditability.

---

## 1) Base principle: suggestion ≠ decision {#1-princípio-base-sugestão--decisão}

Regardless of its origin, **the proposed IaC is always treated as untrusted input**.  
The decision to execute (`apply`) is always human and formalised by gates and approvals (proportional to risk).

---

## 2) Acceptable vs prohibited patterns {#2-padrões-aceitáveis-vs-proibidos}

### ✅ Acceptable (with control) {#-aceitável-com-controlo}

- Generating **drafts** of IaC (skeletons) for subsequent human review.
- Normalising formatting/structure (e.g. reorganisation of files), provided there is a `plan` and validations.
- Generating documentation and comments (non-executable) from the code.
- Creating change proposals in branches/PRs with mandatory execution of `plan` and scanners.

### ❌ Prohibited (by default) {#-proibido-por-defeito}

- Any mechanism that executes `apply` in production without gates and formal approval.
- “Bulk” automatic changes without explainability and without correlation with risk/impact.
- Publishing `plan`, detailed logs or sensitive diffs to external systems without minimisation/redaction.
- Introducing new dependencies/modules/providers without governance (allowlist + pinning + review).

> Exceptions are acceptable only with a formal record (TTL, owner, compensations) and approval according to criticality.

---

## 3) Typical error classes in automated/assisted IaC {#3-classes-de-erro-típicas-em-iac-automatizadoassistido}

These classes must be assumed as baseline risk and covered by semantic validation:

1. **“Hallucinatory” / unexpected resources**: creation of unintended resources (services, endpoints, rules).
2. **Insecure defaults**: encryption switched off, logging absent, “open” permissions.
3. **Overly broad IAM**: wildcards, admin roles, improper cross-account access.
4. **Network exposure**: permissive security groups, public ports, flat networks.
5. **Accidental destruction**: implicit `destroy`, recreations, destructive replacements.
6. **Masked drift**: indirect changes by providers/modules, uncontrolled upgrades.
7. **Exfiltration through logs/artefacts**: improper publication of topology, IDs, endpoints and secrets.

---

## 4) Mandatory validations (gates) and minimum evidence {#4-validações-obrigatórias-gates-e-evidência-mínima}

### 4.1 Minimum gates (always applicable) {#41-gates-mínimos-sempre-aplicáveis}

- **Lint/syntax**: validation of format and consistency.
- **Security scanning**: misconfigurations, exposures and dangerous patterns.
- **Policy-as-code**: blocking of critical violations.
- **Secret scanning**: preventing secrets in repos/logs/artefacts.

### 4.2 Semantic validation of the `plan` (mandatory when applicable) {#42-validação-semântica-do-plan-obrigatória-quando-aplicável}

- Impact of the `plan`: creation/change/destruction per resource and environment.
- Effective permissions: increase in privileges, wildcards, admin roles.
- Exposure: public endpoints, permissive network rules, public storage.
- Encryption/logging: critical resources without minimum guarantees.
- Unexpected diffs: upgrades and indirect changes.

### 4.3 Minimum (auditable) evidence {#43-evidência-mínima-auditável}

- `plan` associated with the PR/MR + commit + environment.
- Scanner/policy reports associated with the same PR/MR.
- Record of approvals before `apply` (who, when, why).
- Retention of artefacts proportional to risk.

---

## 5) Handling of external systems {#5-tratamento-de-sistemas-externos}

Any external system that processes:
- repository content,
- `plan`,
- logs,
- diffs,
- outputs,

must be treated as a **security dependency**:

- classified and authorised organisationally;
- subject to logging/retention and isolation requirements;
- subject to context minimisation rules (**no secrets / no infra topology**);
- subject to contractual obligations when applicable.

---

## ⚖️ Proportionality L1–L3 {#️-proporcionalidade-l1l3}

| Dimension | L1 | L2 | L3 |
|---|---|---|---|
| Use of automation/assistance | Permitted with review | Permitted with blocking gates | Permitted with gates + reinforced SoD |
| Semantic validation of the `plan` | Recommended | Mandatory | Mandatory (reinforced) |
| Approval before `apply` | Simple | 2nd reviewer | Dual approval + change window |
| Evidence and retention | Basic | Mandatory | Mandatory + reinforced retention |
| External integrations | Restrict | Minimise and redact | Minimise+redact + reinforced control |

---

## ✅ Control checklist per project {#-checklist-de-controlo-por-projeto}

- [ ] Automation/assistance is used only for proposals (not for uncontrolled execution)
- [ ] Minimum gates active (lint, scanning, policies, secret scanning)
- [ ] Semantic validation of the `plan` applied when relevant
- [ ] `plan` and reports correlated with the PR/MR + approval
- [ ] External integrations follow context minimisation and redaction
- [ ] Exceptions are formal, temporary and with compensations
