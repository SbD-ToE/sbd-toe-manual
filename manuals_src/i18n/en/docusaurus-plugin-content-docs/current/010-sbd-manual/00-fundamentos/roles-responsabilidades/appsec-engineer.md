---
id: appsec-engineer
title: AppSec Engineer
sidebar_label: 🔐 AppSec Engineer
description: Responsibilities of the AppSec Engineer in the SbD-ToE
tags: [appsec, seguranca, vulnerabilidades, responsabilidades]
sidebar_position: 5
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/appsec-engineer.md
  source_sha256: 4755b6b7ebdabdc3b0f79c4dc2292f1ea6641ba9066ce749089372b8c03218e7
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 526b46ba2a6385e7fd722eba309b108969893b7c5bd2b186e15f23216b0986e2
  engine: claude-fable-5-1
  prompt_sha256: 13029ebd6497cb63207d12577bb94bbd3b20a5d9c8d3ebd2e4a450d20a45a251
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [alcada, audit_trail, chapter_role, cycle_iteration, framework_source_corpus, lifecycle_phase, provenance, sbdtoe_sbd, traceability, trilho_formativo, validation_evaluation, verification_taxonomy]
  glossary_sha256: c9d864ddbf667d6870459e290b0a96887d8330ab68dbc820d947988bdf2fb318
  translated_at: 2026-09-25T20:19:55Z
  reviewed_by: null
---

# AppSec Engineer

## Overview {#visão-geral}

AppSec is the **bridge between abstract standards and technical execution**.  
It turns regulatory obligations into **concrete, auditable controls proportionate to risk**, ensuring that security is embedded across the complete lifecycle.

### Key Responsibilities {#responsabilidades-principais}
- Translate standards and regulations into technical requirements
- Facilitate threat modelling sessions and architecture reviews
- Define secure development guidelines
- Support audits and produce security evidence

### Organisational Context {#contexto-organizacional}
They act as the **link between technical teams and governance**, ensuring the traceability required by **NIS2** and **DORA**. Without AppSec, security policies become detached from technical reality.

## Regulatory Framework {#enquadramento-regulatório}

Essential for:
- **NIS2**: Traceability and vulnerability management
- **DORA**: Supplier governance and operational resilience
- **GDPR**: Security by design and privacy by default

---

## Activities by Chapter {#atividades-por-capítulo}

### Ch. 01 - Application Classification {#cap-01---classificação-de-aplicações}
Review the **criticality classification** whenever relevant technical changes occur or at a fixed cadence (L1 yearly, L2 half-yearly, L3 quarterly). Verify that expected threats are covered by the controls applied.

**User Stories:**
- [US-02: Criticality review on relevant changes](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-02---aplicação-da-matriz-de-controlo) - Keep the classification up to date
- [US-03: Periodic criticality review](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-03---revisão-por-alteração-relevante-event-based) - Fixed cadence per level
- [US-06: Threat coverage verification](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-06---mapeamento-de-ameaças-por-nível-de-risco) - Validate the adequacy of controls

### Ch. 02 - Security Requirements {#cap-02---requisitos-de-segurança}
Establish and maintain a **security requirements catalogue**, versioned and auditable throughout the SDLC.

**User Stories:**
- [US-04: Security Requirements Catalogue](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-04---rastreabilidade-de-requisitos) - Consistent and traceable application

### Ch. 03 - Threat Modelling {#cap-03---threat-modeling}
Document and **formally approve residual risks** identified in threat modelling, ensuring transparent and auditable decisions.

**User Stories:**
- [US-04: Documentation and approval of residual risks](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-04---justificação-formal-de-risco-aceite) - Transparent decisions

### Ch. 04 - Secure Architecture {#cap-04---arquitetura-segura}
Review **architecture designs** to ensure compliance with established security patterns.

**User Stories:**
- [US-03: Review of architecture designs](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-03---revisão-formal-do-design-arquitetural) - Validate technical compliance

### Ch. 05 - Dependencies and SBOM {#cap-05---dependências-e-sbom}
Run **automatic SCA in pipelines** and formalise CVE exceptions with explicit governance. Audit manually copied libraries.

**User Stories:**
- [US-03: Automatic SCA with gates](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-03---sca-automático-com-gates) - Detect CVEs before production
- [US-04: Formal, temporary CVE exceptions](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-04---exceções-a-cves-formais-e-temporárias) - Residual risk governance
- [US-09: Audit of manually copied libraries](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-09---auditoria-periódica-de-bibliotecas-copiadas-manualmente) - Blocking in CI/CD

### Ch. 06 - Secure Development {#cap-06---desenvolvimento-seguro}
Validate external dependencies, record technical exceptions, **review guidelines** quarterly, define L1-L3 validation profiles, detect dangerous patterns automatically.

**User Stories:**
- [US-02: Validation of external dependencies](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-02---revisão-de-código-segura) - Reduce supply chain risk
- [US-03: Recording and approval of technical exceptions](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-03---gestão-de-dependências-no-código) - Traceability and review
- [US-04: Quarterly review of guidelines](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-04---automatização-em-cicd-linters--sast) - Formal governance
- [US-05: L1-L3 validation profiles](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-05---gestão-de-exceções-técnicas) - Adequacy to risk
- [US-06: Automatic detection of dangerous patterns](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-06---uso-validado-de-genia) - Blocking with educational feedback

### Ch. 07 - Secure CI/CD {#cap-07---cicd-seguro}
Apply **distinct gates per L1-L3** and ensure container/SBOM scanners in pipelines. Run DAST in staging.

**User Stories:**
- [US-07: Gates by risk](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-07---gates-por-risco-separação-sinaldecisão) - Proportionate security
- [US-08: Extended coverage](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-08---cobertura-ampliada-containers-e-sbom) - Containers and SBOM
- [US-11: DAST in staging](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-11---testes-de-segurança-dinâmicos-dast) - Behavioural validation

### Ch. 08 - IaC and Infrastructure {#cap-08---iac-e-infraestrutura}
Govern **IaC modules from trusted origins**, apply automatic policy enforcement, audit drift periodically.

**User Stories:**
- [US-04: Governance of IaC modules](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-04---governança-e-origem-confiável-de-módulos) - Reduce supply chain risk
- [US-08: Automatic policy enforcement](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-08---enforcement-automático-de-políticas) - Systematic compliance
- [US-11: Periodic drift audit](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-11---deteção-e-correção-de-drift) - IaC vs infrastructure coherence

### Ch. 09 - Containers and Images {#cap-09---containers-e-imagens}
Digitally sign **all images** with verifiable provenance. Monitor container behaviour at runtime.

**User Stories:**
- [US-03: Digital signing of images](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-03---assinatura-e-verificação-de-proveniência-de-imagens-com-cosign-e-rekor) - Integrity and origin
- [US-05: Runtime behaviour monitoring](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-05---monitorização-e-resposta-a-incidentes-em-runtime) - Detection of suspicious events

### Ch. 10 - Security Testing {#cap-10---testes-de-segurança}
Define a **testing strategy per application** proportionate to risk. Centralise findings on a unified platform and automate delivery to the teams.

**User Stories:**
- [US-01: Security testing strategy](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-01---estratégia-formal-de-testes-por-aplicação) - Coverage proportionate to risk
- [US-10: Centralised findings management](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-10---gestão-centralizada-de-findings-com-triagem-e-sla) - Unified platform
- [US-11: Automatic findings feedback](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-11---feedback-automático-de-findings-às-equipas) - Contextualised delivery

### Ch. 11 - Secure Deployment {#cap-11---deploy-seguro}
Define **automatic gates and thresholds** for deployment. Run technical validation with conditional gates by risk.

**User Stories:**
- [US-01: Automatic gates on deploy](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-01---deploy-apenas-de-artefactos-assinados) - Block insecure releases
- [US-04: Conditional gates by risk](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-04---rollback-r%C3%A1pido-e-testado) - Proportionate technical validation

### Ch. 12 - Monitoring and Operations {#cap-12---monitorização-e-operações}
Define **critical security events and metrics**. Classify monitoring domains, correlate multi-source events, tune alerts, apply controls proportionate to risk.

**User Stories:**
- [US-02: Definition of critical events](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-02---definição-de-eventos-e-métricas-críticas) - Coverage of relevant risks
- [US-04: Classification of monitoring domains](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-04---integração-com-processos-de-resposta-a-incidentes) - Proportionate coverage
- [US-05: Multi-source event correlation](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-05---métricas-de-eficácia-mttdmttr) - Detection of suspicious patterns
- [US-06: Alert validation and tuning](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-06---classificação-e-cobertura-de-domínios-de-monitorização) - Reduce false positives
- [US-09: Controls proportionate to risk](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-09---correlação-de-eventos-e-deteção-comportamental) - Balance cost and coverage

### Ch. 13 - Training and Onboarding {#cap-13---formação-e-onboarding}
Provide **continuous training per profile**, run code clinics, keep training tracks up to date, apply training proportionate to risk, implement validation quizzes, define the DoD per format.

**User Stories:**
- [US-02: Continuous training per profile](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-02---formação-contínua-por-perfil) - Kept current with recent practices
- [US-03: Structured code clinics](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-03---programa-de-security-champions) - Continuous learning
- [US-07: Maintenance of training tracks](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-07---threat-modeling-peer-led-e-rotativo) - Reflect current practices
- [US-08: Tracks proportionate to risk](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-08---war-room-e-simulações-de-incidentes) - Adequacy to context
- [US-09: Validation quizzes](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-09---manutenção-e-atualização-de-trilhos-formativos) - Auditable record of competence
- [US-10: Definition of DoD per format](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-10---trilhos-formativos-proporcionais-por-risco-l1l3) - Consistency and quality

### Ch. 14 - Governance and Contracting {#cap-14---governança-e-contratação}
Aggregate practices in an **organisational dashboard**, review exceptions periodically, maintain the compliance repository, run periodic validation, formalise governance with delegated authority levels, maintain the centralised checklist, monitor suppliers.

**User Stories:**
- [US-02: Organisational dashboard](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-02---cláusulas-contratuais-de-segurança) - Visibility and measurement
- [US-04: Periodic review of exceptions](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-04---rastreabilidade-organizacional) - Validate mitigations
- [US-06: Compliance repository](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-06---execução-de-fluxo-formal-de-validação-de-fornecedores) - Facilitate audits
- [US-07: Periodic compliance validation](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-07---ciclo-contínuo-de-revisão-e-reavaliação-de-exceções) - Detect deviations
- [US-10: Centralised compliance checklist](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-10---valida%C3%A7%C3%A3o-peri%C3%B3dica-de-aplica%C3%A7%C3%B5es-ciclo-de-conformidade) - Actual state of all practices
- [US-14: Continuous supplier monitoring](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-14---reavaliação-contínua-e-rotação-de-fornecedores-pós-onboarding) - Real-time event detection

---

## Chapter References {#referências-aos-capítulos}

For full context and framing:

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
