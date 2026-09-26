---
id: developer
title: Developer
sidebar_label: 👨‍💻 Developer
description: Responsibilities of the Developer in the SbD-ToE
tags: [developer, dev, codigo, responsabilidades]
sidebar_position: 2
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/developer.md
  source_sha256: 96c0fc5cf50a6f59032714ab1e6eabbbd90bf7a7172a7d267d89e0548688f779
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: e4a10f34913ba0bfee9a9e23c55f60431000712dad8a1bd9ec110630e9ccfd18
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, avaliacao, capacitacao, chapter_role, eu_ai_system, framework_source_corpus, papel_suporte, practitioner_manual, risk_level, sbdtoe_sbd, slug_threat_modeling, threat, traceability, transversal, validation_evaluation]
  glossary_sha256: 7fe664ea0122d53250932b9c888014dd13e3a8e78c1123ab92acb8911186f8b6
  translated_at: 2026-09-25T20:22:02Z
  stamped_at: 2026-09-26T18:32:31Z
  reviewed_by: null
---

# Developer

## Overview {#visão-geral}

Developers are the **front line of the practical implementation of *security by design***.  
It is in the act of writing code that a large part of the security practices prescribed in the SbD-ToE materialise.

### Key Responsibilities {#responsabilidades-principais}
- Write code in accordance with security guidelines (Ch. 06)
- Fix vulnerabilities identified in reviews and scans
- Contribute to threat modelling and provide technical information on data flows (Ch. 03)
- Ensure that the software meets functional **and security** requirements in a robust and traceable way

### Organisational Context {#contexto-organizacional}
The Developer role is **cross-cutting to almost the whole Manual**. The responsibility is twofold: deliver functionality and ensure security. Without the active collaboration of developers, no security policy materialises.

## Regulatory Framework {#enquadramento-regulatório}

The Developer's work gives effect to obligations under:
- **NIS2**: Secure development practices and vulnerability management
- **DORA**: Digital resilience in financial systems  
- **GDPR**: *Security by design* principles
- **AI Act**: Security and transparency in AI systems

---

## Activities by Chapter {#atividades-por-capítulo}

### Ch. 01 - Criticality Classification {#cap-01---classificação-da-criticidade}
Provide technical information on the application's **dependencies, integrations and operational impact**, contributing to the risk assessment and to determining the criticality level (L1/L2/L3).

**User Stories:**
- [US-01: Initial classification of the application](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-01---classificação-inicial-da-aplicação) - Apply the E+D+I model to determine the L1–L3 level
- [US-02: Applying the control matrix](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-02---aplicação-da-matriz-de-controlo) - Map requirements to the Ch. 02 requirements

### Ch. 02 - Security Requirements {#cap-02---requisitos-de-segurança}
Implement the **minimum security requirements** derived from the classification, integrating them into the *definition of done* and ensuring compliance in every delivery.

**User Stories:**
- [US-03: Exception Management with TTL and Revalidation](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-03---gestão-de-exceções-com-ttl-e-revalidação-obrigatória) - Record formal exceptions with TTL and AppSec approval
- [US-11: SBOM generation and artefact signing](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-11---geração-de-sbom-e-assinatura-de-artefactos-de-build) - Automatic SBOM and artefact signing
- [US-12: Validation of SEC-Lx-* tags in the pipeline](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-12---validação-de-tags-sec-lx--e-requisitos-no-pipeline) - Automatic traceability of requirements

### Ch. 03 - Threat Modelling {#cap-03---threat-modeling}
Take an active part in **threat modelling sessions**, translating diagrams and threat scenarios into practical controls implemented in code.

**User Stories:**
- [US-01: Creating the threat model](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-01---criação-do-modelo-de-ameaça) - DFDs and STRIDE/LINDDUN at the start of the project

### Ch. 04 - Secure Architecture {#cap-04---arquitetura-segura}
Ensure that the implementation respects the defined **architectural patterns**. Keep the architecture sheet up to date when critical changes occur.

**User Stories:**
- [US-04: Architecture update on critical changes](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-04---gestão-de-decisões-arquiteturais-adr) - Update the architecture sheet when structural changes arise

### Ch. 05 - Dependencies and SBOM {#cap-05---dependências-e-sbom}
Explicitly declare all **libraries and dependencies** used, supporting the creation of auditable inventories (SBOM) essential for vulnerability management.

**User Stories:**
- [US-01: Secure dependency management](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-01---gestão-de-dependências-seguras) - Use only approved dependencies
- [US-07: Prohibit manually copied libraries](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-07---proibir-bibliotecas-copiadas-manualmente) - Use package managers, never manual copies
- [US-12: Automatic validation of licence compatibility](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-12---validação-automática-de-compatibilidade-de-licenças) - Ensure legal compliance

### Ch. 06 - Secure Development {#cap-06---desenvolvimento-seguro}
Follow **secure coding guidelines**, use linters and automatic validation, fix SAST findings. Prevent trivial vulnerabilities through tools integrated into the development workflow.

**User Stories:**
- [US-01: Secure Development Guidelines](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-01---guidelines-de-desenvolvimento-seguro) - Apply the approved guidelines per stack
- [US-06: Validated Use of GenAI](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-06---uso-validado-de-genia) - Generative AI with mandatory review
- [US-08: Traceability with Security Annotations](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-08---rastreabilidade-com-anotações-de-segurança) - Annotate each validation with @sec:*
- [US-12: Mandatory Local Validation](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-12---validações-locais-obrigatórias-pre-commit) - Linters and pre-commit validation

### Ch. 07 - Secure CI/CD {#cap-07---cicd-seguro}
Collaborate with DevOps on **configuring secure pipelines**, ensuring that code passes through security gates (SAST, dependency check) before being merged or deployed.

**User Stories:**
- [US-01: Secure source code management](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-01---gestão-segura-de-código-fonte) - PRs with mandatory review and branch protection
- [US-03: Integrated scanners](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-03---scanners-integrados-validação-empírica-obrigatória) - SAST, secrets scanning and blocking of critical failures

### Ch. 08 - IaC (Infrastructure as Code) {#cap-08---iac-infraestrutura-como-código}
Collaborate on the writing and **validation of secure IaC templates**, ensuring that infrastructure is versioned and auditable.

**User Stories:**
- [US-03: Integrated automatic validation](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-03---validações-automáticas-integradas) - Mandatory linters, scanners and policy-as-code

### Ch. 09 - Containers and Images {#cap-09---containers-e-imagens}
Build images from **trusted, versioned bases** (SHA256 digest). Ensure that Dockerfiles follow security best practices.

**User Stories:**
- [US-01: Trusted base images](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-01---construção-de-imagens-a-partir-de-bases-seguras-minimalistas-e-pinned-por-digest) - Use only official images with a SHA256 digest

### Ch. 10 - Security Testing {#cap-10---testes-de-segurança}
Run **automatic SAST on the PR** with inline comments, fixing vulnerabilities before merge. Create regression tests for fixed findings.

**User Stories:**
- [US-02: Automatic SAST on the PR](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-02---sast-obrigatório-em-pull-request) - Static analysis with contextual feedback
- [US-05: Security regression tests](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-05---regressões-de-segurança-automatizadas) - Prevent the reintroduction of vulnerabilities

### Ch. 11 - Secure Deployment {#cap-11---deploy-seguro}
Maintain **semantic versioning** with a technical and security changelog. Ensure that only validated artefacts are promoted between environments.

**User Stories:**
- [US-01: Semantic versioning + changelog](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-01---deploy-apenas-de-artefactos-assinados) - Complete traceability of changes

### Ch. 12 - Monitoring and Operations {#cap-12---monitorização-e-operações}
Implement **structured, centralised logging**, generating events with enough context for incident detection and investigation.

**User Stories:**
- [US-01: Structured logs + centralisation](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-01---logging-estruturado-e-centralizado) - Ensure full visibility during incidents

### Ch. 13 - Training and Onboarding {#cap-13---formação-e-onboarding}
Take part in **continuous upskilling programmes** and, as Security Champion, lead threat modelling sessions per feature, epic or refactor.

**User Stories:**
- [US-06: Threat modelling per feature/epic/refactor](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-06---code-clinics-estruturadas-e-recorrentes) - Security Champion leads the threat analysis

### Ch. 14 - Governance and Contracting {#cap-14---governança-e-contratação}
Submit **security exceptions** through a formal flow with automatic routing by risk level. Maintain a structured compliance repository for each application (with the Scrum Master / Team Lead).

**User Stories:**
- [US-03: Security exceptions + approval workflow](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-03---validação-contínua-de-fornecedores) - Formal exception management
- [US-06: Compliance repository per application](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-06---execução-de-fluxo-formal-de-validação-de-fornecedores) - Centralise evidence and documentation

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
