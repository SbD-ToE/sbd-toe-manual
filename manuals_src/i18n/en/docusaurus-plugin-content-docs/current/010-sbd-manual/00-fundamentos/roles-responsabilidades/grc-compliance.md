---
id: grc-compliance
title: GRC / Compliance
sidebar_label: 📑 GRC / Compliance
description: Responsibilities of GRC/Compliance in SbD-ToE
tags: [grc, compliance, governance, responsabilidades]
sidebar_position: 11
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/grc-compliance.md
  source_sha256: 2bf41a1412be3ce1ae0f344b75f92938b213224f248980214af84fa9a0a3b16a
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 122510d9bf7514a168c799f58b6af6d52d63c54d82abfb5a1d595275c2031dea
  engine: claude-fable-5-1
  prompt_sha256: 13029ebd6497cb63207d12577bb94bbd3b20a5d9c8d3ebd2e4a450d20a45a251
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [capacitacao, chapter_role, maturity, sbdtoe_sbd, traceability, transversal, validation_evaluation]
  glossary_sha256: ff819aceba272daea94eb488db971d15151abd5adda27a41296d9c620259dc61
  translated_at: 2026-09-25T20:19:59Z
  reviewed_by: null
---

# GRC / Compliance

## Overview {#visão-geral}

GRC ensures that **internal practices are aligned with external standards and regulations**.  
It coordinates audits, maintains residual-risk documentation, manages exceptions and provides the documentary evidence required by NIS2, DORA and GDPR.

### Key Responsibilities {#responsabilidades-principais}
- Ensure traceability to standards (SSDF, ISO) and regulations (NIS2, DORA, GDPR, AI Act)
- Monitor exceptions and ensure residual-risk documentation
- Coordinate internal and external audits
- Link technical requirements to legal obligations

### Organisational Context {#contexto-organizacional}
GRC is the guarantor of the **documentary evidence** required by NIS2 (audit, reporting) and DORA (operational resilience and third-party management). Without GRC, there is no demonstration of compliance.

## Regulatory Framework {#enquadramento-regulatório}

Provides the documentary evidence required by:
- **NIS2**: Audits, reporting, traceability
- **DORA**: Resilience, third-party governance, testing
- **GDPR**: Demonstration of compliance (*accountability*)

---

## Activities by Chapter {#atividades-por-capítulo}

### Ch. 01 - Application Classification {#cap-01---classificação-de-aplicações}
Record **residual risk** after applying controls, record acceptances with an explicit TTL, and consolidate monthly/quarterly KPIs on classification and exceptions.

**User Stories:**
- [US-04: Residual risk record](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-04---an%C3%A1lise-de-risco-residual) - Substantiate acceptance decisions
- [US-08: Risk Acceptance with TTL](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-08---aceitação-de-risco-com-ttl-e-revalidação-obrigatória) - Avoid permanent exceptions
- [Classification governance KPIs](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle) - Demonstrate maturity

### Ch. 02 - Security Requirements {#cap-02---requisitos-de-segurança}
Publish the policy for applying requirements and provide training (with Executive Management / CISO).

**User Stories:**
- [US-07: Policy for applying requirements](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-07---validação-e-aprovação-final) - Clear procedures (with Executive Management / CISO)

### Ch. 07 - Secure CI/CD {#cap-07---cicd-seguro}
Trace **commit → pipeline → release** to support audits. Ensure that exceptions are recorded, approved and temporary.

**User Stories:**
- [US-09: End-to-end traceability](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-09---rastreabilidade-ponta-a-ponta-commitpipelinerelease) - Support audits
- [US-10: Exception management](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-10---gestão-de-exceções-bypass-controlado) - Avoid technical debt

### Ch. 08 - IaC and Infrastructure {#cap-08---iac-e-infraestrutura}
Map **IaC file → resource → environment** to validate impact and traceability. Ensure change windows and approvals by role. Record exceptions with a deadline and countermeasures.

**User Stories:**
- [US-07: File → resource → environment traceability](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-07---rastreabilidade-ficheiro--recurso--ambiente) - Validate impact (with Auditors)
- [US-13: Change window and approvals](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-13---janela-de-mudança-e-aprovações-por-papel) - Reduce operational risk (with Auditors)
- [US-14: Formal exceptions in IaC](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-14---exceções-formais-em-iac) - Avoid structural debt (with AppSec Engineer)

### Ch. 12 - Monitoring and Operations {#cap-12---monitorização-e-operações}
Measure **incident MTTD and MTTR**. Document compliance between controls and regulatory requirements (SSDF, NIS2, ISO 27001).

**User Stories:**
- [US-11: Incident MTTD and MTTR](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-11---proporcionalidade-de-controlos-por-risco-l1l3-e-dom%C3%ADnios) - Evaluate effectiveness
- [US-12: Regulatory compliance documentation](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-12---rastreabilidade-e-conformidade-com-regulações-ssdf-nis2-iso-27001) - Demonstrate alignment (with Auditors)

### Ch. 13 - Training and Onboarding {#cap-13---formação-e-onboarding}
Measure **upskilling KPIs**, run incident simulations, ensure minimum training for third parties, and define and collect KPIs.

**User Stories:**
- [US-03: Upskilling KPIs](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-03---programa-de-security-champions) - Evaluate impact in audit
- [US-04: Incident simulations](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-04---exercícios-práticos-e-simulações) - Validate processes (with Executive Management)
- [US-11: Detailed upskilling KPIs](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-11---validação-formal-de-onboarding-via-checklist) - Report compliance (with Executive Management)
- [US-12: Minimum training for third parties](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-12---validação-de-conhecimento-via-quizzes-estruturados) - NIS2/DORA (with Executive Management)

### Ch. 14 - Governance and Contracting {#cap-14---governança-e-contratação}
Validate **suppliers continuously**, run periodic compliance validations, and formally validate employee onboarding.

**User Stories:**
- [US-01: Continuous supplier validation](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-01---processo-formal-de-exceções-com-alçadas-por-nível-de-risco) - Contractual compliance
- [US-07: Periodic compliance validations](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-07---ciclo-contínuo-de-revisão-e-reavaliação-de-exceções) - Detect deviations (with AppSec Engineer)

### Cross-cutting - All Chapters {#transversal---todos-os-capítulos}
Link **technical requirements to legal obligations** (NIS2, DORA, GDPR, AI Act). Coordinate audits and maintain documentary traceability.

---

## Chapter References {#referências-aos-capítulos}

For full context and framing:

- [Ch. 01 - Application Classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
- [Ch. 02 - Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Ch. 04 - Secure Architecture](/sbd-toe/sbd-manual/arquitetura-segura/intro)
- [Ch. 07 - Secure CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro)
- [Ch. 08 - IaC and Infrastructure](/sbd-toe/sbd-manual/iac-infraestrutura/intro)
- [Ch. 09 - Containers and Images](/sbd-toe/sbd-manual/containers-imagens/intro)
- [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)
- [Ch. 13 - Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
- [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)
