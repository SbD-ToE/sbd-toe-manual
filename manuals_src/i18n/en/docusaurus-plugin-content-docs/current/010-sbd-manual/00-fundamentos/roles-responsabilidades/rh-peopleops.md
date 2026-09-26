---
id: rh-peopleops
title: HR / People Operations
sidebar_label: 🧑‍🤝‍🧑 HR / People Operations
description: What SbD-ToE requires to exist on the HR / People Operations side
tags: [rh, peopleops, formacao, onboarding, offboarding, responsabilidades]
sidebar_position: 11.3
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/rh-peopleops.md
  source_sha256: a4772be8bc204cca0d6cf8d10df8fd6bfb01d8c826865a16f0d0fa14452021ae
  source_commit: 112711064196b71c545672fe3fb3ae412b36575e
  target_sha256: f1aa3d1bd2d77d3c665bc480230ed9875fdf96dd68c2db1ed71d36825eff63c9
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 69aedbbdd11831f1cdc997bd1abfda3e2e4d3b411b1b43faf096628c510f395b
  glossary_keys: [audit_trail, chapter_role, practitioner_manual, role_rh_formacao, role_rh_peopleops, role_rh_recrutamento, sbdtoe_sbd, trilho_formativo, validation_evaluation]
  glossary_sha256: fff9605ae2c09188088fe27455aae49c3b61cf080279279ca918971acd3a0276
  translated_at: 2026-09-26T17:23:58Z
  reviewed_by: null
---

# HR / People Operations

## Overview {#visão-geral}

HR / People Operations is **another domain of the organisation**. The Manual does not say how HR works; it says what must exist on its side for security to work: recorded training, onboarding before access, timely offboarding.

### Key Responsibilities {#responsabilidades-principais}
- Run the LMS, manage onboarding and integrate security training into individual plans
- Ensure that mandatory training is completed and recorded before technical access
- Coordinate the preparation and offboarding of contractors, within the deadlines the Manual sets
- Keep the training record that supports audits

**Specialisations:** HR (Learning & Development) — the *Training Manager*, who coordinates the training tracks; HR (Recruiting) — the *Recruiter*, who screens contractors.

### Organisational Context {#contexto-organizacional}
Recorded training is evidence under **NIS2** (cybersecurity training) and **DORA** (staff competence). Timely offboarding closes access that would otherwise outlive the contract.

## Regulatory Framework {#enquadramento-regulatório}

Supports:
- **NIS2**: Cybersecurity training for staff
- **DORA**: Staff competence and awareness of ICT risk
- **GDPR**: Training for those who process personal data

---

## Activities by Chapter {#atividades-por-capítulo}

### Ch. 13 - Training and Onboarding {#cap-13---formação-e-onboarding}
Ensure **mandatory onboarding training** before technical access, continuous training cycles with communicated deadlines, and remediation when the result falls below the threshold.

**User Stories:**
- [US-01: Mandatory secure onboarding](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-01---onboarding-seguro-obrigatório) - Everyone starts out aligned with the practices
- [US-11: Formal onboarding validation via checklist](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-11---validação-formal-de-onboarding-via-checklist) - Onboarding completed before access (with GRC / Compliance)
- [US-12: Knowledge validation via quizzes](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-12---validação-de-conhecimento-via-quizzes-estruturados) - Auditable record of competence (with AppSec Engineer)
- [US-15: Delivery formats and DoD per format](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-15---formatos-de-entrega-e-dod-por-formato) - Verifiable completion in each format (with AppSec Engineer)
- [US-16: Remediation path below the threshold](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-16---caminho-de-remediação-abaixo-do-limiar) - Remediation before any access (with AppSec Engineer)
- [US-19: Training in safe use of AI and tooling](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-19---formação-em-uso-seguro-de-ia-e-tooling) - Training before autonomous use of AI (with AppSec Engineer)

### Ch. 14 - Governance and Contracting {#cap-14---governança-e-contratação}
Coordinate the **preparation of contractors** before access, the mandatory training track and **secure offboarding** when the contract ends.

**User Stories:**
- [US-15: Technical preparation and validation of contractors before access](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-15---preparação-técnica-e-validação-de-contractors-pré-acesso) - Contractors prepared before access (with Security Champion)
- [US-16: Mandatory pre-access training track](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-16---trilho-de-formação-obrigatória-pré-acesso-contractors) - Training Manager coordinates the track (with CISO)
- [US-17: Secure offboarding of contractors](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-17---offboarding-seguro-de-contractors-e-rescisão-de-fornecedores) - Access revoked in less than 24h (with Security Champion and DevOps / SRE)

---

## Chapter References {#referências-aos-capítulos}

For full context and framing:

- [Ch. 13 - Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
- [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)
