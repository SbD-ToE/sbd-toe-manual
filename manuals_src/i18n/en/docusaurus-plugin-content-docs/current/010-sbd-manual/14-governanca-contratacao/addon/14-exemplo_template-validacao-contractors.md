---
id: template-validacao-contractors
title: Contractor Validation Template
description: Checklist and structured validation model for the screening, approval and onboarding of contractors
tags: [governanca, contractors, validacao, triagem, checklist, onboarding]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/addon/14-exemplo_template-validacao-contractors.md
  source_sha256: b80522063ed81275fc7801cd1b96859206c32c3ebb69aab23583a53f0eb6ce0f
  source_commit: 50f5914ebc90e4135e6678b2278709d5082dd237
  target_sha256: e9de10bfc720903eb32b039edc5eef89c0ad4fc90f770cad012d8f6b3a9914b9
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [avaliacao, chapter_role, papel_suporte, role_procurement, role_tech_lead, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: e1004a44534609d71c0d79b49f8667db265dee048efc1b57565ada71054115fb
  translated_at: 2026-09-27T07:06:07Z
  stamped_at: 2026-09-27T07:06:07Z
  reviewed_by: null
---

# Contractor Validation Template

**Version:** 1.0  
**Last update:** November 2025  
**Responsible:** HR + AppSec Engineer  
**Review frequency:** Annual (validate against the most recent security policies)

---

## 📖 Use of this Template {#-uso-deste-template}

This document serves as a **structured validation checklist for new contractors** before formal contracting or access to systems. It is used in **US-06 (initial supplier validation)** and **US-15 (pre-access technical preparation)**.

**Responsibilities:**
- **Procurement Officer:** Coordination of the flow, filling in parts 1–3
- **AppSec Engineer:** Filling in parts 4–5, security validation
- **Tech Lead:** Validate technical requirements and preparation (part 6)
- **HR:** Verification of references and legal documentation (part 2)

**Estimated time:** 2–3 weeks before the start date

---

## ✅ PART 1: Basic Information {#-parte-1-informações-básicas}

| Field | Entry | Observations |
|-------|---------------|-------------|
| **Contractor's full name** | [_______________] | |
| **Corporate email** | [_______________] | Will be created after approval |
| **Contact mobile phone** | [_______________] | |
| **Nationality** | [_______________] | Relevant for data residency (GDPR, etc.) |
| **Planned start date** | [_______________] | |
| **Contract duration** | [_______________] | E.g.: 3 months, 6 months, indefinite |
| **Supplier/Agency** | [_______________] | If applicable |
| **Role/Function** | [_______________] | E.g.: Backend Developer, DevOps Engineer, QA |
| **Team/Project** | [_______________] | |
| **Responsible Tech Lead** | [_______________] | Technical validator |
| **Security Champion** | [_______________] | Security validator |
| **Criticality classification** | [ ] L1  [ ] L2  [ ] L3 | Defined by Tech Lead + AppSec |

---

## ✅ PART 2: Background Verification and Legal Documentation {#-parte-2-verificação-de-background-e-documentação-legal}

### 2.1 Verification of References {#21-verificação-de-referências}

| Item | Yes | No | N/A | Observations |
|------|-----|-----|-----|-------------|
| **Contact with a previous reference (Tech Lead/Manager)** | [ ] | [ ] | [ ] | Date: [_____]. Feedback: [_________________] |
| **Background check verification (police/criminal)** | [ ] | [ ] | [ ] | Status: [_____________] |
| **Verification of professional credentials** | [ ] | [ ] | [ ] | Certifications validated? [_________________] |

### 2.2 Legal Documentation {#22-documentação-legal}

| Item | Submitted | Validated | Observations |
|------|-----------|----------|-------------|
| **Signed contract** | [ ] | [ ] | Date: [_____] |
| **NDA (Non-Disclosure Agreement)** | [ ] | [ ] | Digitally signed? [ ] Yes |
| **Confidentiality Agreement** | [ ] | [ ] | Post-termination duration: [___________] |
| **IP Assignment (if applicable)** | [ ] | [ ] | Developed code belongs to: [__________] |
| **Non-Compete (if applicable)** | [ ] | [ ] | Duration: [_____], scope: [____________] |
| **Data Protection/GDPR compliance** | [ ] | [ ] | Has the contractor confirmed acceptance of data processing? |

---

## ✅ PART 3: Initial Technical Assessment {#-parte-3-avaliação-técnica-inicial}

### 3.1 Technical Skills and Background {#31-skills-e-background-técnico}

| Question | Answer | Validated by | Observations |
|---------|----------|--------------|-------------|
| **Security experience** | [_______________] | Tech Lead | E.g.: "2 years in secure coding" |
| **Experience with security tools?** | [ ] Yes [ ] No | AppSec | Which: [__________________] |
| **Previous experience in regulated environments (DORA, ISO, PCI)?** | [ ] Yes [ ] No | AppSec | Details: [__________________] |
| **Relevant certifications** | [_______________] | HR | E.g.: OSCP, CEH, CSSLP, CKAD |
| **Programming languages** | [_______________] | Tech Lead | Relevant to the project |
| **CI/CD and Infra experience** | [ ] Yes [ ] No | DevOps | Tools: [__________________] |
| **Knowledge of containers/Kubernetes** | [ ] Yes [ ] No | DevOps | Level: [ ] Basic [ ] Intermediate [ ] Advanced |

### 3.2 Initial Security Screening {#32-triagem-de-segurança-inicial}

| Question | Answer | Assessment |
|---------|----------|-----------|
| **Does the contractor agree to accept the company's security policy?** | [ ] Yes [ ] No | Status: [ ] ✅ Approved [ ] ❌ Rejected |
| **Has the contractor confirmed that there is no conflict of interest?** | [ ] Yes [ ] No | Status: [ ] ✅ Approved [ ] ❌ Rejected |
| **Does the contractor agree to use secure corporate equipment?** | [ ] Yes [ ] No | Status: [ ] ✅ Approved [ ] ❌ Rejected |
| **Has the contractor confirmed that they are not on an international sanctions list?** | [ ] Yes [ ] No | Status: [ ] ✅ Approved [ ] ❌ Rejected |

**Screening Result:** [ ] ✅ Approved  [ ] ❌ Rejected

**Justification (if rejected):** [_____________________]

---

## ✅ PART 4: Security Validation (AppSec Engineer) {#-parte-4-validação-de-segurança-appsec-engineer}

### 4.1 Security Awareness Questions (Minimum Level) {#41-questões-de-security-awareness-nível-mínimo}

**Instructions:** Send this form to the contractor. Minimum required score: **70%**

| # | Question | Expected Answer | Did the Contractor Answer? | Score |
|---|----------|------------------|----------------------|-------|
| 1 | What is the first step if you suspect phishing? | Do not reply, report to security | [ ] Yes [ ] No | [ ] ✅ [ ] ❌ |
| 2 | Can you share corporate credentials with colleagues? | No, each person has personal access | [ ] Yes [ ] No | [ ] ✅ [ ] ❌ |
| 3 | What is the procedure if you forget your password? | Contact IT/Secure password reset | [ ] Yes [ ] No | [ ] ✅ [ ] ❌ |
| 4 | Can you connect a personal VPN or an external proxy? | No, only the corporate VPN | [ ] Yes [ ] No | [ ] ✅ [ ] ❌ |
| 5 | What is the process for reporting a security incident? | Contact [CISO/Security email] immediately | [ ] Yes [ ] No | [ ] ✅ [ ] ❌ |
| 6 | Can you bring unauthorised personal devices? | No, only approved equipment | [ ] Yes [ ] No | [ ] ✅ [ ] ❌ |
| 7 | Is MFA mandatory for corporate login? | Yes, always activate MFA | [ ] Yes [ ] No | [ ] ✅ [ ] ❌ |
| 8 | What is the session duration before automatic timeout? | [Internal policy, e.g.: 30 min] | [ ] Yes [ ] No | [ ] ✅ [ ] ❌ |
| 9 | Can you leave your workstation unlocked and unattended? | No, lock or logout mandatory | [ ] Yes [ ] No | [ ] ✅ [ ] ❌ |
| 10 | What is the post-termination confidentiality policy? | Confidential data remains confidential | [ ] Yes [ ] No | [ ] ✅ [ ] ❌ |

**Total Score:** __/10 (__%)  
**Minimum required:** 70% (7/10)  
**Result:** [ ] ✅ PASSED  [ ] ❌ FAILED (Retry: [ ] Scheduled for [____])

---

### 4.2 Equipment Validation {#42-validação-de-equipamentos}

| Item | Status | Observations |
|------|--------|-------------|
| **Is the computer personal or corporate?** | [ ] Personal [ ] Corporate | If personal, requires special approval |
| **Operating system and version** | [_______________] | Must be up to date (last 6 months of patches) |
| **Antivirus/Antimalware installed?** | [ ] Yes [ ] No | Tool: [__________________] |
| **Firewall activated?** | [ ] Yes [ ] No | |
| **Encrypted disk (LUKS/BitLocker)?** | [ ] Yes [ ] No | Mandatory for L2–L3 |
| **Last malware verification** | [_______________] | Date and result |
| **Confirmation: Contractor undertakes to keep equipment secure** | [ ] Yes [ ] No | |

**Result:** [ ] ✅ Approved  [ ] ⚠️ Conditional (with plan) [ ] ❌ Rejected

---

### 4.3 Risk Assessment (AppSec Engineer) {#43-avaliação-de-risco-appsec-engineer}

| Dimension | L1 | L2 | L3 | Observations |
|----------|----|----|-----|-------------|
| **Risk of access to sensitive data** | [ ] | [ ] | [ ] | [_________________] |
| **Risk of modification of critical code** | [ ] | [ ] | [ ] | [_________________] |
| **Risk of privilege escalation** | [ ] | [ ] | [ ] | [_________________] |
| **Risk of leakage of IP/confidential information** | [ ] | [ ] | [ ] | [_________________] |

**Overall Risk:** [ ] Low [ ] Medium [ ] High [ ] Very High  
**Approval:** [ ] ✅ Recommended  [ ] ⚠️ Conditional [ ] ❌ Not recommended

**Justification:** [_____________________________________]

---

## ✅ PART 5: Decision Report {#-parte-5-relatório-de-decisão}

### 5.1 Validation Summary {#51-síntese-de-validação}

| Criterion | Result | Responsible |
|----------|-----------|-------------|
| **Legal Documentation** | [ ] ✅ Complete [ ] ⚠️ Pending [ ] ❌ Missing | [__________] |
| **Background Check** | [ ] ✅ Passed [ ] ⚠️ Review [ ] ❌ Failed | [__________] |
| **Technical/Skills** | [ ] ✅ Approved [ ] ⚠️ Conditional [ ] ❌ Rejected | [__________] |
| **Security Awareness** | [ ] ✅ Passed (>70%) [ ] ⚠️ Retry [ ] ❌ Failed | [__________] |
| **Risk Assessment** | [ ] ✅ Approved [ ] ⚠️ Conditional [ ] ❌ Not recommended | [__________] |

### 5.2 Final Decision {#52-decisão-final}

**Overall Decision:**  
[ ] ✅ **APPROVED** → Proceed to Technical Preparation (US-15)  
[ ] ⚠️ **APPROVED WITH CONDITIONS** → Specify the mitigation plan below  
[ ] ❌ **REJECTED** → Contact Procurement with a justification  

**Mitigation Plan (if conditional):**
```
1. [_____________________________] → Prazo: [_____] → Owner: [_______] → Status: [ ]
2. [_____________________________] → Prazo: [_____] → Owner: [_______] → Status: [ ]
3. [_____________________________] → Prazo: [_____] → Owner: [_______] → Status: [ ]
```

### 5.3 Formal Approvals {#53-aprovações-formais}

| Role | Name | Digital Signature | Date | Observations |
|-------|------|-------------------|------|-------------|
| **HR Manager** | [__________] | [Signed] | [____] | |
| **Tech Lead** | [__________] | [Signed] | [____] | |
| **AppSec Engineer** | [__________] | [Signed] | [____] | |
| **Procurement Officer** | [__________] | [Signed] | [____] | If L2–L3 |

---

## ✅ PART 6: Next Steps (Post-Approval) {#-parte-6-próximos-passos-pós-aprovação}

If APPROVED, the following actions are triggered automatically:

### 6.1 Preparation Timeline {#61-timeline-de-preparação}

| Date | Action | Owner | Status |
|------|------|-------|--------|
| T-14 days | Sandbox setup + LMS enrolment | DevOps + Training | [ ] Done |
| T-10 days | Welcome email + onboarding info | HR | [ ] Done |
| T-7 days | Online training started | Training Manager | [ ] Done |
| T-3 days | Comprehension quiz (score >80%) | Contractor + AppSec | [ ] Done |
| T-1 day | Confirmation of completion | Security Champion | [ ] Done |
| T-0 (Day 1) | Access granted + technical onboarding | DevOps | [ ] Done |

### 6.2 Subsequent Checklists {#62-checklists-subsequentes}

After approval in this template, the contractor follows:
1. **US-15:** Technical Preparation (Sandbox, NDA, training)
2. **US-16:** Mandatory Training Track (Ch. 13)
3. **Actual Access:** After completion of US-15 and US-16

---

## 📎 Annexes and References {#-anexos-e-referências}

- [Ch. 13 - Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle)
- [US-06: Supplier Validation Flow](../aplicacao-lifecycle#us-06---execução-de-fluxo-formal-de-validação-de-fornecedores)
- [US-15: Technical Preparation of Contractors](../aplicacao-lifecycle#us-15---preparação-técnica-e-validação-de-contractors-pré-acesso)
- [US-16: Training Track](../aplicacao-lifecycle#us-16---trilho-de-formação-obrigatória-pré-acesso-contractors)
- [Governance Model](./modelo-governancao)

---

## 🏁 Final Notes {#-notas-finais}

- **This template is mandatory for L2–L3** and recommended for L1.
- **Keep the history of all validations** for the duration of the contract + 1 year (+ 3 years at L3), in line with [Policy 33](/sbd-toe/assets/policies/policy-contratacao-segura#8-registo-e-rastreabilidade).
- **Review this template annually** against updated security policies.
- **Escalation:** If any field raises a red flag, contact the CISO before approval.
