---
id: gestao-executiva
title: Executive Management / CISO
sidebar_label: 🏛️ Executive Management / CISO
description: Responsibilities of Executive Management in SbD-ToE
tags: [gestao-executiva, ciso, governance, responsabilidades]
sidebar_position: 10
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/gestao-executiva.md
  source_sha256: 00f90a58b54480243afc99846123e7bb78112b72e3b7263d30c60646111754e2
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: b3c6e117ad1af86802dcf99418c09f8783d16ccc8b919829d50b498dfdc71e85
  engine: claude-fable-5-1
  prompt_sha256: 13029ebd6497cb63207d12577bb94bbd3b20a5d9c8d3ebd2e4a450d20a45a251
  terms_sha256: 1bfef9a72816fbf492eb0960150a7457c7572375ed258eed99a7d94ef48cf520
  glossary_keys: [audit_trail, capacitacao, chapter_role, maturity, sbdtoe_sbd, traceability, trilho_formativo]
  glossary_sha256: 2d6d943485e1307fba1710a7d4c56e9ad6d1702753e7d55d818c609439718a85
  translated_at: 2026-09-25T17:10:41Z
  reviewed_by: null
---

# Executive Management / CISO

## Overview {#visão-geral}

Executive Management **sets direction and secures the conditions for application**.  
Without sponsorship at the highest level, security loses priority and resources. The CISO translates strategy into executable programmes.

### Key Responsibilities {#responsabilidades-principais}
- Sponsor and secure the conditions for applying SbD-ToE
- Define the budget and support the choice of tooling and training
- Assume final responsibility for security governance
- Take strategic decisions on residual risk

### Organisational Context {#contexto-organizacional}
This role is **central to NIS2 and DORA**, which explicitly assign the management body **responsibility for overseeing and executing** cybersecurity and digital operational resilience measures.

## Regulatory Framework {#enquadramento-regulatório}

**NIS2** and **DORA** assign **explicit responsibility to the management body** for digital security and operational resilience.

---

## Activities by Chapter {#atividades-por-capítulo}

### Ch. 01 - Application Classification {#cap-01---classificação-de-aplicações}
Publish **formal organisational policies** (Risk Classification, Risk Acceptance, Periodic Review, Traceability/Audit) to ensure uniform criteria.

**User Stories:**
- [Formal organisational policies](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle) - Uniform, auditable operation

### Ch. 02 - Security Requirements {#cap-02---requisitos-de-segurança}
Approve **minimum requirement templates** and publish the policy for applying them, with training for technical teams.

**User Stories:**
- [US-07: Publication of the policy for applying requirements](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-07---validação-e-aprovação-final) - Clear procedures and SLAs (with GRC / Compliance)

### Ch. 04 - Secure Architecture {#cap-04---arquitetura-segura}
Establish a **formal architecture approval process for L3**, with a technical committee or governance review.

**User Stories:**
- [US-14: Formal architecture review for L3](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-14---revisão-formal-de-arquitetura-para-l3-governação-reforçada) - Mitigate structural risks before go-live (with Software Architects)

### Ch. 05-09 - Tooling and Infrastructure {#cap-05-09---tooling-e-infraestrutura}
Support **investment in tooling** (SCA, SAST, DAST, SBOM, policy engines) and automated processes.

### Ch. 07 - Secure CI/CD {#cap-07---cicd-seguro}
View the **CI/CD metrics dashboard** (coverage, exceptions, gate blocks, remediation time) for informed decision-making.

**User Stories:**
- [US-12: CI/CD metrics dashboard](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-12---métricas-e-conformidade-organizacional) - Strategic corrective action

### Ch. 10 - Security Testing {#cap-10---testes-de-segurança}
Establish **security acceptance criteria per release** and a residual-risk acceptance process.

**User Stories:**
- [US-07: Acceptance criteria per release](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-07---critérios-de-release-e-aceitação-de-risco) - Informed go/no-go decisions

### Ch. 11 - Deployment and Operations {#cap-11---deploy-e-operações}
Decide on **high risks in production** and ensure traceability from commit → build → release → deploy.

**User Stories:**
- [US-07: End-to-end traceability](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-07---controlo-de-execu%C3%A7%C3%A3o-com-feature-flags) - Audit risk decisions

### Ch. 13 - Training and Onboarding {#cap-13---formação-e-onboarding}
Run **incident simulations** (war room) regularly, define upskilling KPIs, ensure minimum training for third parties, and define a mandatory training track per contractor profile.

**User Stories:**
- [US-04: Incident simulations (war room)](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-04---exercícios-práticos-e-simulações) - Validate response processes (with GRC / Compliance)
- [US-11: Upskilling KPIs](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-11---validação-formal-de-onboarding-via-checklist) - Evaluate real impact (with GRC / Compliance)
- [US-12: Minimum training for third parties](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-12---validação-de-conhecimento-via-quizzes-estruturados) - Comply with NIS2/DORA (with GRC / Compliance)
- [US-13: Training track for contractors](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-13---operacionalização-de-formação-de-terceiros) - SLA before technical access (with Security Champion (training))

### Ch. 14 - Governance and Contracting {#cap-14---governança-e-contratação}
Define and monitor **governance KPIs**, appoint a Security Champion per critical application, consolidate and report KPIs, and formalise a governance model with delegated authority levels.

**User Stories:**
- [US-01: Governance KPIs](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-01---processo-formal-de-exceções-com-alçadas-por-nível-de-risco) - Evaluate SbD-ToE effectiveness
- [US-05: Security Champion appointment](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-05---kpis-de-governação) - Clear accountability
- [US-08: KPI consolidation and reporting](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-08---repositório-de-conformidade-por-aplicação-controlo-sistemático) - Evaluate organisational maturity
- [US-09: Formal governance model](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-09---designação-formal-de-owners-de-segurança-por-aplicação) - Appropriate authority (with AppSec Engineer)

---

## Chapter References {#referências-aos-capítulos}

For full context and framing:

- [Ch. 01 - Application Classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
- [Ch. 02 - Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Ch. 04 - Secure Architecture](/sbd-toe/sbd-manual/arquitetura-segura/intro)
- [Ch. 05 - Dependencies and SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)
- [Ch. 07 - Secure CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro)
- [Ch. 09 - Containers and Images](/sbd-toe/sbd-manual/containers-imagens/intro)
- [Ch. 10 - Security Testing](/sbd-toe/sbd-manual/testes-seguranca/intro)
- [Ch. 11 - Secure Deployment](/sbd-toe/sbd-manual/deploy-seguro/intro)
- [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)
- [Ch. 13 - Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
- [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)
