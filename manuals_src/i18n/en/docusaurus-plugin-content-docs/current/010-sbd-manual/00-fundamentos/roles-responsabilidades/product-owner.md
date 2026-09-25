---
id: product-owner
title: Product Owner (PO)
sidebar_label: 📋 Product Owner (PO)
description: Responsibilities of the Product Owner in SbD-ToE
tags: [product-owner, po, produto, responsabilidades]
sidebar_position: 8
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/product-owner.md
  source_sha256: 7cc6750fe8004f53858b81ab38206bb1b59a674ceedf6ebae92f1f3875fe5843
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 6e4349013fdea3128fca965f71561cbf3f1f157974ab90555cabb7d5b48b13f6
  engine: claude-fable-5-1
  prompt_sha256: 13029ebd6497cb63207d12577bb94bbd3b20a5d9c8d3ebd2e4a450d20a45a251
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [chapter_role, cycle_iteration, lifecycle_phase, requirement_runtime, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: ec5b85ae5c44f19938071c42de502ec2a888bebdce4691d01b15b4af153825d9
  translated_at: 2026-09-25T20:20:01Z
  reviewed_by: null
---

# Product Owner (PO)

## Overview {#visão-geral}

The Product Owner **balances business and security**, ensuring that security is not seen as a cost but as **value intrinsic to the product**.  
Responsible for prioritising security requirements, validating the impact of architectural decisions and authorising releases only when the criteria are met.

### Key Responsibilities {#responsabilidades-principais}
- Balance business priorities with security requirements
- Ensure that security stories enter and remain in the backlog
- Approve acceptance criteria that include security
- Take go/no-go decisions informed by risk analysis

### Organisational Context {#contexto-organizacional}
The PO supports obligations under **DORA** (integration of security and digital continuity into all products) and **NIS2** (integration of risk management into business processes).

## Regulatory Framework {#enquadramento-regulatório}

Supports:
- **DORA**: Integration of digital resilience into the lifecycle
- **NIS2**: Incorporation of risk management into the business

---

## Activities by Chapter {#atividades-por-capítulo}

### Ch. 01 - Application Classification {#cap-01---classificação-de-aplicações}
Validate **risk classifications** against the product's strategic objectives.

### Ch. 02 - Security Requirements {#cap-02---requisitos-de-segurança}
Select **requirements applicable to the project** in proportion to risk. Ensure that each requirement in the backlog contains clear, testable security acceptance criteria.

**User Stories:**
- [US-01: Selection of applicable requirements](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-01---seleção-de-requisitos-por-criticidade) - Security proportional to risk
- [US-03: Security acceptance criteria](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-03---gestão-de-exceções-com-ttl-e-revalidação-obrigatória) - Consistent validation

### Ch. 03 - Threat Modelling {#cap-03---threat-modeling}
Prioritise **identified threats** according to business impact, optimising mitigation and investment.

**User Stories:**
- [US-05: Threat prioritisation by impact](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-05---gate-de-controlo-de-consistência-no-cicd) - Optimise mitigation resources

### Ch. 04 - Secure Architecture {#cap-04---arquitetura-segura}
Validate the **impact of architecture requirements** to prioritise mitigation. Manage exceptions with approval and compensating controls.

**User Stories:**
- [US-06: Requirement impact validation](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-06---atualização-da-baseline-após-alteração-arquitetural-significativa) - Prioritise mitigation
- [US-10: Architecture exception management](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-10---gestão-de-exceções-arquiteturais-com-controlos-compensatórios) - Balance risk and delivery (with AppSec Engineer)

### Ch. 05 - Dependencies and SBOM {#cap-05---dependências-e-sbom}
Validate **findings and exceptions before go-live**, taking an informed go/no-go decision based on risk analysis.

**User Stories:**
- [US-05: Release validation (go/no-go)](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-05---validação-de-release-gono-go) - Informed decision before go-live

### Ch. 07 - Secure CI/CD {#cap-07---cicd-seguro}
Define **release gates** that block insecure versions, ensuring compliance with established thresholds.

### Ch. 11 - Secure Deployment {#cap-11---deploy-seguro}
Authorise only **releases whose security criteria are met**, validating that controls are in place.

### Ch. 13-14 - Training and Governance {#cap-13-14---formação-e-governança}
Ensure that **training and contractual clauses** reflect secure practices and support product decisions.

---

## Chapter References {#referências-aos-capítulos}

For full context and framing:

- [Ch. 01 - Application Classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
- [Ch. 02 - Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Ch. 03 - Threat Modelling](/sbd-toe/sbd-manual/threat-modeling/intro)
- [Ch. 04 - Secure Architecture](/sbd-toe/sbd-manual/arquitetura-segura/intro)
- [Ch. 05 - Dependencies and SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)
- [Ch. 07 - Secure CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro)
- [Ch. 11 - Secure Deployment](/sbd-toe/sbd-manual/deploy-seguro/intro)
- [Ch. 13 - Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
- [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)
