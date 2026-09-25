---
id: qa
title: Quality Assurance (QA)
sidebar_label: 🧪 Quality Assurance (QA)
description: Responsibilities of QA in SbD-ToE
tags: [qa, quality-assurance, testes, responsabilidades]
sidebar_position: 3
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/qa.md
  source_sha256: 615dbac3e0e85553424ec60d1a33acfe86f4b3ba2e4d5ad91132aa0de1478b32
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 644d81983756a47493f531eff1c34d2d4278b0670f89d36065c4e544555ee00b
  engine: claude-fable-5-1
  prompt_sha256: 13029ebd6497cb63207d12577bb94bbd3b20a5d9c8d3ebd2e4a450d20a45a251
  terms_sha256: a23b4b0245c8f70929c4cf8742f32b3c89fb297f85b057d601b8189193ae0417
  glossary_keys: [chapter_role, requirement_runtime, risk_level, sbdtoe_sbd, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: 4cc8e063f31c47c86a3ce86b4586a79e8a367c66e949c0165a689914b8850404
  translated_at: 2026-09-25T17:57:23Z
  reviewed_by: null
---

# Quality Assurance (QA)

## Overview {#visão-geral}

QA **validates security requirements by turning them into clear, testable acceptance criteria**.  
It is no longer enough to validate that the software "works": it is necessary to prove that it works resiliently and protected against threats.

### Key Responsibilities {#responsabilidades-principais}
- Validate security requirements (Ch. 02)
- Run functional and security tests in parallel
- Confirm that fixes do not introduce regressions
- Ensure that security controls work as expected

### Organisational Context {#contexto-organizacional}
QA is the first line of defence against vulnerabilities that slip past development. Without robust security testing, insecure code reaches production.

## Regulatory Framework {#enquadramento-regulatório}

QA gives effect to the demands of:
- **NIS2**: Verification of technical measures
- **DORA**: Regular digital resilience testing

---

## Activities by Chapter {#atividades-por-capítulo}

### Ch. 01 - Application Classification {#cap-01---classificação-de-aplicações}
Validate that **requirements applicable per risk level are met** before entry into production, ensuring compliance with the assigned classification.

**User Stories:**
- [US-05: Validation before go-live](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-05---validação-antes-do-go-live) - Verify that requirements are met per level

### Ch. 02 - Security Requirements {#cap-02---requisitos-de-segurança}
Ensure that all **requirements have traceability in the backlog** and an associated validation, preventing false positives or absence of control.

**User Stories:**
- [US-04: Requirements traceability](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-04---rastreabilidade-de-requisitos) - Audit and tracking verification
- [US-05: Definition of validation criteria](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-05---definição-de-critérios-de-validação) - All requirements with clear validation
- [US-09: Validation per requirement/domain](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-09---validação-por-requisitodomínio-req-xxx--evidência) - Objective, traceable evidence of fulfilment
- [US-12: Validation of SEC-Lx-* tags in the pipeline](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-12---validação-de-tags-sec-lx--e-requisitos-no-pipeline) - Automatic traceability

### Ch. 03 - Threat Modelling {#cap-03---threat-modeling}
Translate **threat modelling scenarios into objective tests**, ensuring that identified threats have a counterpart in practical validations.

### Ch. 04 - Secure Architecture {#cap-04---arquitetura-segura}
Validate the **architecture before go-live**, ensuring that all defined controls are in place and exceptions are documented.

**User Stories:**
- [US-08: Architecture validation before go-live](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-08---avaliação-de-impacto-no-negócio-e-priorização-de-trade-offs) - Verify controls and documented exceptions

### Ch. 06 - Secure Development {#cap-06---desenvolvimento-seguro}
Conduct **static and dynamic testing** in collaboration with AppSec, validating that the code meets security standards.

**User Stories:**
- [US-11: Central Archive of Validation Evidence](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-11---arquivo-central-de-evidências-de-validação) - Centralised traceability and audit

### Ch. 07 - Secure CI/CD {#cap-07---cicd-seguro}
Ensure that **pipelines incorporate automated security verification**, validating that gates work correctly.

### Ch. 10 - Security Testing {#cap-10---testes-de-segurança}
Run authenticated dynamic tests, fuzzing on critical endpoints and IAST instrumentation in staging to detect vulnerabilities exploitable at runtime.

**User Stories:**
- [US-03: Authenticated DAST in Staging](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-03---dast-autenticado-em-staging) - Detect vulnerabilities exploitable at runtime
- [US-06: Fuzzing targeted at critical APIs](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-06---fuzzing-dirigido-a-apis-críticas) - Detect flaws invisible to conventional tests
- [US-09: IAST with Instrumentation in Staging](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-09---iast-com-instrumentação-em-staging) - Observe insecure calls at runtime

### Ch. 11 - Secure Deployment {#cap-11---deploy-seguro}
Validate releases in **staging with a segregated environment**, controlled data and functional + security tests. Run technical validations with risk-conditional gates.

**User Stories:**
- [US-03: Validation in pre-production staging](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-03---gates-de-aprovação-no-deploy) - Segregated environment with full tests
- [US-04: Risk-conditional deploy gates](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-04---rollback-r%C3%A1pido-e-testado) - Proportional technical validations

### Ch. 12 - Monitoring {#cap-12---monitorização}
Validate that **runtime alerts and metrics** are correctly configured, confirming that critical events are detected.

### Ch. 13 - Training {#cap-13---formação}
Take part in **structured hands-on exercises** (labs, CTFs, simulations) to ensure knowledge that is applicable in a real context.

**User Stories:**
- [US-05: Structured hands-on exercises](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-05---medição-de-eficácia-da-formação) - Consolidate knowledge through practice

---

## Chapter References {#referências-aos-capítulos}

For full context and framing:

- [Ch. 01 - Application Classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
- [Ch. 02 - Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Ch. 03 - Threat Modelling](/sbd-toe/sbd-manual/threat-modeling/intro)
- [Ch. 04 - Secure Architecture](/sbd-toe/sbd-manual/arquitetura-segura/intro)
- [Ch. 06 - Secure Development](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro)
- [Ch. 07 - Secure CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro)
- [Ch. 10 - Security Testing](/sbd-toe/sbd-manual/testes-seguranca/intro)
- [Ch. 11 - Secure Deployment](/sbd-toe/sbd-manual/deploy-seguro/intro)
- [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)
- [Ch. 13 - Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
