---
id: auditores
title: Internal and External Auditors
sidebar_label: 📋 Internal and External Auditors
description: Responsibilities of Auditors in the SbD-ToE
tags: [auditores, auditoria, compliance, responsabilidades]
sidebar_position: 14
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/auditores.md
  source_sha256: 0a2295eee3eba0b97f889d7eeda4aea6e085a57bf510e591b504317a789f1fba
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: c2751e73e92a07236440e3536492ecc2f5b83dc2ced2984085585d62f27ec7f9
  engine: claude-fable-5-1
  prompt_sha256: 13029ebd6497cb63207d12577bb94bbd3b20a5d9c8d3ebd2e4a450d20a45a251
  terms_sha256: 779fcd2406a1a730ed65de83e52df7743a50456cc35d31f9ce5b9d1c8073cd3d
  translated_at: 2026-09-25T16:51:49Z
  reviewed_by: null
---

# Internal and External Auditors

## Overview {#visão-geral}

Auditors **validate the effective application of the practices** described in the SbD-ToE.  
They verify risk classifications, traceability, evidence of application, and alignment with regulatory requirements across all chapters.

### Key Responsibilities {#responsabilidades-principais}
- Validate the effective application of the prescribed practices
- Assess risk classifications, requirements, traceability and evidence
- Produce independent reports and improvement recommendations
- Attest compliance before the authorities

### Organisational Context {#contexto-organizacional}
They are essential instruments for demonstrating compliance to supervisory authorities, as required by **NIS2**, **DORA**, **GDPR** and **ISO 27001**.

## Regulatory Framework {#enquadramento-regulatório}

They are formal instruments for demonstrating compliance to the authorities:
- **NIS2**: Security and compliance audits
- **DORA**: Resilience testing and third-party audits
- **GDPR**: Data protection audits
- **ISO 27001/27002**: ISMS audits

---

## Activities by Chapter {#atividades-por-capítulo}

### Cross-cutting - All Chapters {#transversal---todos-os-capítulos}
Validate **evidence of practice application**, verify **traceability of decisions** (ADR, exceptions, risk acceptances), confirm **alignment with regulatory requirements** (NIS2, DORA, GDPR, SSDF, ISO 27001).

**Associated requirements:**
- [US-12: Regulatory compliance documentation](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-12---rastreabilidade-e-conformidade-com-regulações-ssdf-nis2-iso-27001) - GRC / Compliance documents, Auditors validate

### Ch. 01 - Application Classification {#cap-01---classificação-de-aplicações}
Verify **risk classifications** and their adequacy to the technical and business context. Validate governance KPIs.

**Associated requirements:**
- [Classification governance KPIs](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle) - GRC / Compliance consolidates, Auditors validate
- [Formal organisational policies](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle) - Executive Management publishes, Auditors validate application

### Ch. 02 - Security Requirements {#cap-02---requisitos-de-segurança}
Validate the **implementation of requirements per level** (L1/L2/L3), verify traceability requirements → controls → evidence.

### Ch. 07 - Secure CI/CD {#cap-07---cicd-seguro}
Validate **commit → pipeline → release traceability**, verify exception management.

**Associated requirements:**
- [US-09: End-to-end traceability](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-09---rastreabilidade-ponta-a-ponta-commitpipelinerelease) - GRC / Compliance traces, Auditors validate
- [US-10: Exception management](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-10---gestão-de-exceções-bypass-controlado) - GRC / Compliance manages, Auditors validate

### Ch. 08 - IaC and Infrastructure {#cap-08---iac-e-infraestrutura}
Validate **file → resource → environment traceability**, verify change windows and approvals, validate formal exceptions.

**Associated requirements:**
- [US-07: File → resource → environment traceability](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-07---rastreabilidade-ficheiro--recurso--ambiente) - GRC / Compliance documents, Auditors validate
- [US-13: Change window and approvals](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-13---janela-de-mudança-e-aprovações-por-papel) - GRC / Compliance defines, Auditors validate
- [US-14: Formal exceptions in IaC](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-14---exceções-formais-em-iac) - GRC / Compliance / AppSec Engineer manage, Auditors validate

### Ch. 14 - Governance and Contracting {#cap-14---governança-e-contratação}
Audit **exception documentation**, verify **formal approvals**, validate **contractual compliance with suppliers**, verify complete traceability.

**Associated requirements:**
- [US-06: Compliance repository](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-06---execução-de-fluxo-formal-de-validação-de-fornecedores) - AppSec Engineer / Scrum Master / Team Lead maintain, Auditors validate
- [US-07: Periodic compliance validation](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-07---ciclo-contínuo-de-revisão-e-reavaliação-de-exceções) - AppSec Engineer / GRC / Compliance carry it out, Auditors validate
- [US-10: Centralised compliance checklist](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-10---valida%C3%A7%C3%A3o-peri%C3%B3dica-de-aplica%C3%A7%C3%B5es-ciclo-de-conformidade) - AppSec Engineer / Scrum Master / Team Lead maintain, Auditors use

---

## Chapter References {#referências-aos-capítulos}

Auditors use every chapter as a source of evidence:

- [Ch. 01 - Application Classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
- [Ch. 02 - Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Ch. 03 - Threat Modelling](/sbd-toe/sbd-manual/threat-modeling/intro)
- [Ch. 04 - Secure Architecture](/sbd-toe/sbd-manual/arquitetura-segura/intro)
- [Ch. 05 - Dependencies and SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)
- [Ch. 06 - Secure Development](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro)
- [Ch. 07 - Secure CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro)
- [Ch. 08 - IaC and Infrastructure](/sbd-toe/sbd-manual/iac-infraestrutura/intro)
- [Ch. 09 - Containers and Images](/sbd-toe/sbd-manual/containers-imagens/intro)
- [Ch. 10 - Security Testing](/sbd-toe/sbd-manual/testes-seguranca/intro)
- [Ch. 11 - Secure Deployment](/sbd-toe/sbd-manual/deploy-seguro/intro)
- [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)
- [Ch. 13 - Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
- [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)
