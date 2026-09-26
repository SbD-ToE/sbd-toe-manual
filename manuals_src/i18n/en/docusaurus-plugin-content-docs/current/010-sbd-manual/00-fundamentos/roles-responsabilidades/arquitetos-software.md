---
id: arquitetos-software
title: Software Architects
sidebar_label: 🏗️ Software Architects
description: Responsibilities of Software Architects in the SbD-ToE
tags: [arquitetura, design, seguranca, responsabilidades]
sidebar_position: 6
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/arquitetos-software.md
  source_sha256: f78a72ecdda50bf28e9cf5b3ad1ac8c6eadb7f4208d25ab4f14fa4db2951eb5b
  source_commit: 112711064196b71c545672fe3fb3ae412b36575e
  target_sha256: e21b95260d4ff548abfb020eec7c61688b94b51abd20b0e88e103472e4f8c6f5
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, sbdtoe_sbd, slug_threat_modeling, threat, traceability, validation_evaluation]
  glossary_sha256: 1b15b415482eadd538bd24f802b88f0758c117c59c12d1a875aabe22b0109d17
  translated_at: 2026-09-26T17:23:37Z
  stamped_at: 2026-09-26T18:32:30Z
  reviewed_by: null
---

# Software Architects

## Overview {#visão-geral}

Architects design solutions that **withstand time and threats**.  
They ensure that security principles are embedded in structural decisions from the outset. They apply **secure patterns from the foundation up**.

### Key Responsibilities {#responsabilidades-principais}
- Design solutions with secure patterns (Ch. 04)
- Anticipate risk implications in integrations and data flows
- Ensure architectural consistency across pipelines, IaC and deploys
- Take documented architectural decisions (ADR)
- Own the design rules: they accept the *policies* that check them automatically and approve the exceptions to those rules

### Organisational Context {#contexto-organizacional}
The architects' work supports the *security by design* principles set out in **GDPR** and the **AI Act**, as well as **NIS2** obligations related to planning appropriate technical measures. Without secure architecture, later fixes are costly and ineffective.

## Regulatory Framework {#enquadramento-regulatório}

They give effect to:
- **GDPR** and **AI Act**: *Security by design* and *privacy by design*
- **NIS2**: Appropriate structural technical measures

---

## Activities by Chapter {#atividades-por-capítulo}

### Ch. 02 - Security Requirements {#cap-02---requisitos-de-segurança}
Review **classification and requirements** whenever a critical integration or relevant structural change occurs.

**User Stories:**
- [US-02: Review on critical changes](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-02---revisão-por-alteração-relevante) - Update controls and traceability

### Ch. 03 - Threat Modelling {#cap-03---threat-modeling}
Create the **initial threat model** with DFDs and STRIDE/LINDDUN, validate the architecture by identifying critical threats before design, update the model on significant changes, apply LINDDUN when personal data is processed.

**User Stories:**
- [US-01: Initial threat model](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-01---criação-do-modelo-de-ameaça) - Risks visible from the outset
- [US-02: Architecture validation via threat modelling](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-02---validação-de-arquitetura-com-threat-modeling) - Identify threats before design
- [US-03: Update on significant changes](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-03---atualização-do-modelo-após-alteração-técnica) - Keep the model valid
- [US-06: Applying LINDDUN for privacy](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-06---validação-de-impacto-no-negócio) - Coverage of GDPR threats

### Ch. 04 - Secure Architecture {#cap-04---arquitetura-segura}
Define **secure architecture principles**, produce the architecture sheet with controls, record decisions (ADR) with their security rationale, review trust boundaries and integrations, synchronise the threat model with decisions, maintain review triggers and the catalogue of secure patterns, specify isolation controls, run threat modelling in the initial design for L2-L3.

**User Stories:**
- [US-01: Secure architecture principles](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-01---definição-de-princípios-e-baseline-de-arquitetura-segura) - Guide technical decisions
- [US-02: Architecture sheet with controls](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-02---ficha-de-solução-com-controlos-e-rastreabilidade-arquitetural) - Secure and scalable solution
- [US-07: Decision records (ADR)](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-07---validação-arquitetural-automatizável-no-cicd-quando-aplicável) - Traceability and consistency
- [US-08: Review of trust boundaries](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-08---avaliação-de-impacto-no-negócio-e-priorização-de-trade-offs) - Validate authentication, authorisation, isolation
- [US-09: Threat model ↔ architecture synchronisation](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-09---sincronização-threat-modeling--arquitetura) - Controls cover threats
- [US-10: Architecture review triggers](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-10---gestão-de-exceções-arquiteturais-com-controlos-compensatórios) - Up-to-date documentation
- [US-11: Catalogue of secure patterns](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-11---triggers-de-arquitetura-viva-e-disciplina-de-revisão) - Reuse of validated designs
- [US-12: Technical isolation controls](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-12---gate-arquitetural-antes-do-go-live) - Resilience to overload and failures
- [US-15: Identification and governance of non-deterministic components](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-15---identifica%C3%A7%C3%A3o-e-governa%C3%A7%C3%A3o-de-componentes-n%C3%A3o-determin%C3%ADsticos) - Specify proportionate controls

### Ch. 08 - IaC and Infrastructure {#cap-08---iac-e-infraestrutura}
Collaborate on **environment segregation** with tagging and least-privilege permissions, govern IaC modules from trusted origins.

**User Stories:**
- [US-02: Environment segregation with tagging](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-02---segregação-de-ambientes-tagging-e-permissões-mínimas) - Isolation and traceability
- [US-04: Governance of IaC modules](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-04---governança-e-origem-confiável-de-módulos) - Prevent the spread of bad practices

### Ch. 11-12 - Deployment and Operations {#cap-11-12---deploy-e-operações}
Support the **resilient design of production environments** with availability and recovery patterns.

---

## Chapter References {#referências-aos-capítulos}

For full context and framing:

- [Ch. 02 - Security Requirements](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Ch. 03 - Threat Modelling](/sbd-toe/sbd-manual/threat-modeling/intro)
- [Ch. 04 - Secure Architecture](/sbd-toe/sbd-manual/arquitetura-segura/intro)
- [Ch. 07 - Secure CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro)
- [Ch. 08 - IaC and Infrastructure](/sbd-toe/sbd-manual/iac-infraestrutura/intro)
- [Ch. 11 - Secure Deployment](/sbd-toe/sbd-manual/deploy-seguro/intro)
- [Ch. 12 - Monitoring and Operations](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)
