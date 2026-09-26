---
id: security-champion
title: Security Champion
sidebar_label: 🏅 Security Champion
description: Responsibilities of the Security Champion in SbD-ToE
tags: [security-champion, seguranca, advocacy, responsabilidades]
sidebar_position: 12
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/security-champion.md
  source_sha256: c61c613154aec68aee5c7e5627d10463843c4f76436c0089fbf6b4803057005f
  source_commit: 112711064196b71c545672fe3fb3ae412b36575e
  target_sha256: 8e6fe3956edcb7ff64d37abb4393b142ab02e3804e4275bc5d46eb9252e0c359
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [capacitacao, chapter_role, role_rh_peopleops, role_tech_lead, sbdtoe_sbd, slug_threat_modeling, transversal]
  glossary_sha256: 8b8164c78ee0a92a41d6d9ca373d72cd5d688e3ba2df2ac41bedb8ea52248266
  translated_at: 2026-09-26T17:23:41Z
  stamped_at: 2026-09-26T18:32:41Z
  reviewed_by: null
---

# Security Champion

## Overview {#visão-geral}

Security Champions are **local catalysts for security**.  
They do not replace AppSec, but bring security **closer to the team's daily work**, ensuring that good practices are followed and security stories are not ignored.

### Key Responsibilities {#responsabilidades-principais}
- Act as catalysts for good practices in each team
- Reinforce adoption of the prescriptions close to daily work
- Ensure that security is not ignored in sprint planning
- Mentor and evangelise the team

### Organisational Context {#contexto-organizacional}
Facilitate the creation of a **security culture** - an element provided for in both **NIS2** and **DORA**, which call for demonstration of training and awareness.

## Regulatory Framework {#enquadramento-regulatório}

Support the creation of the security culture required by:
- **NIS2** and **DORA**: Awareness and continuous technical upskilling

---

## Activities by Chapter {#atividades-por-capítulo}

### Cross-cutting - All Chapters {#transversal---todos-os-capítulos}
Help **Developers and QA** day to day, ensure that **security checklists** are followed, and make sure that **security stories** (requirements, threat modelling, fixes) are not ignored in the backlog.

### Ch. 13 - Training and Onboarding {#cap-13---formação-e-onboarding}
**Mentor and evangelise** the team in security practices. Lead threat modelling sessions per feature, epic or refactor.

**User Stories:**
- [US-06: Threat modelling per feature/epic/refactor](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-06---code-clinics-estruturadas-e-recorrentes) - The Security Champion leads the threat analysis (referenced as Developer in the lifecycle)

### Ch. 14 - Governance and Contracting {#cap-14---governança-e-contratação}
Act as the **designated security owner** for critical applications. Run a structured contractor preparation process, run secure offboarding, review access quarterly, and collect post-project feedback.

**User Stories:**
- [US-05: Formal Security Champion appointment](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-05---kpis-de-governação) - Clear accountability (with Executive Management)
- [US-11: Technical preparation of contractors](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-11---consolidação-de-kpis-de-governação-e-maturidade) - Ensure preparation before access (with HR / People Operations)
- [US-12: Secure offboarding](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-12---formaliza%C3%A7%C3%A3o-de-modelo-de-governa%C3%A7%C3%A3o-por-n%C3%ADvel-de-risco) - Revoke access completely (with HR / People Operations / DevOps / SRE)
- [US-15: Quarterly access review](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-15---preparação-técnica-e-validação-de-contractors-pré-acesso) - Maintain least privilege (with Tech Lead)
- [US-16: Post-project feedback](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-16---trilho-de-formação-obrigatória-pré-acesso-contractors) - Inform re-hiring (with Tech Lead)

---

## Chapter References {#referências-aos-capítulos}

For full context and framing:

- [Ch. 01 - Application Classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
- [Ch. 02 - Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Ch. 03 - Threat Modelling](/sbd-toe/sbd-manual/threat-modeling/intro)
- [Ch. 06 - Secure Development](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro)
- [Ch. 10 - Security Testing](/sbd-toe/sbd-manual/testes-seguranca/intro)
- [Ch. 13 - Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
- [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)
