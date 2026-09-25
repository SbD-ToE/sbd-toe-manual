---
id: devops-sre
title: DevOps / SRE
sidebar_label: ⚙️ DevOps / SRE
description: Responsibilities of DevOps/SRE in the SbD-ToE
tags: [devops, sre, cicd, responsabilidades]
sidebar_position: 4
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/devops-sre.md
  source_sha256: 2a070503fbe14808260a06f8573f31e999b6832712f6cdc28a458a7414b09592
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: c49f2e03d87dbf2ac894d33d5b9ca0a0399ea07d505a84d1bcbd8717b182c295
  engine: claude-fable-5-1
  prompt_sha256: 13029ebd6497cb63207d12577bb94bbd3b20a5d9c8d3ebd2e4a450d20a45a251
  terms_sha256: a23b4b0245c8f70929c4cf8742f32b3c89fb297f85b057d601b8189193ae0417
  glossary_keys: [avaliacao, chapter_role, framework_source_corpus, provenance, sbdtoe_sbd, threat, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: eba85d6ee3c1ca988b1ef8a34762596e4cdc881df22b0c47a4acafaf624e22bd
  translated_at: 2026-09-25T17:57:19Z
  reviewed_by: null
---

# DevOps / SRE

## Overview {#visão-geral}

DevOps/SRE are the **artisans of automation and infrastructure**.  
They ensure that security is embedded in pipelines and at runtime, not bolted on afterwards. They build **security highways** that verify, validate and block insecure code.

### Key Responsibilities {#responsabilidades-principais}
- Integrate security verification into pipelines (Ch. 07)
- Automate SBOM generation and dependency scans (Ch. 05)
- Ensure secure execution of IaC and containers (Ch. 08-09)
- Maintain continuous monitoring in production (Ch. 12)

### Organisational Context {#contexto-organizacional}
They respond directly to the requirements of **DORA** (digital operational resilience) and **NIS2** (appropriate technical measures). They are the bridge between development and secure operations.

## Regulatory Framework {#enquadramento-regulatório}

Essential for:
- **DORA**: Digital operational resilience
- **NIS2**: Implementation of appropriate technical measures

---

## Activities by Chapter {#atividades-por-capítulo}

### Ch. 01 - Application Classification {#cap-01---classificação-de-aplicações}
Classify **technical artefacts** (Dockerfile, pipeline, IaC, images) with the same criticality as the application, ensuring that security controls follow the integrity of the delivery.

**User Stories:**
- [Classification of technical artefacts](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle) - Security traceability across artefacts

### Ch. 02 - Security Requirements {#cap-02---requisitos-de-segurança}
Ensure that the **CI/CD pipeline automatically verifies** security requirements (SAST, SCA, DAST, SBOM, signatures), blocking non-compliant merges and releases.

**User Stories:**
- [US-10: Automatic gates in CI/CD](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-10---gates-automáticos-em-cicd-para-requisitos-de-segurança) - Automatic verification of requirements
- [US-11: SBOM generation and signing](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-11---geração-de-sbom-e-assinatura-de-artefactos-de-build) - SBOM and signatures in the pipeline

### Ch. 03 - Threat Modelling {#cap-03---threat-modeling}
Update the **threat model** on significant changes and integrate validation into the pipeline for automatic review.

**User Stories:**
- [US-03: Model update after a change](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-03---atualização-do-modelo-após-alteração-técnica) - Keep the model up to date
- [US-05: Integration with CI/CD](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-05---gate-de-controlo-de-consistência-no-cicd) - Automatic validation
- [US-07: Automation and reuse of models](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-07---reutilização-controlada-e-revisão-de-modelos-anteriores) - Tools for consistency

### Ch. 04 - Secure Architecture {#cap-04---arquitetura-segura}
Validate **architecture controls in the pipeline** (topology, IaC, policies). Implement **environment segregation** (dev, QA, stage, prod) with logical and physical isolation.

**User Stories:**
- [US-05: Architecture validation in CI/CD](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-05---revisão-de-fronteiras-de-confiança-e-integrações) - Ensure automatic compliance
- [US-13: Environment segregation](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-13---catálogo-de-padrões-de-arquitetura-segura-reutilização-governada) - Isolation with least-privilege permissions

### Ch. 05 - Dependencies and SBOM {#cap-05---dependências-e-sbom}
Automate **SBOM generation and management**, integrating dependency vulnerability analysis into the pipeline.

**User Stories:**
- [US-02: SBOM on every build](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-02---sbom-em-cada-build) - Complete traceability of components
- [US-06: Internal repositories as the single source](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-06---repositórios-internos-como-fonte-única) - Provenance and consistency
- [US-08: Update automation with impact assessment](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-08---automação-da-atualização-com-avaliação-de-impacto) - Automated secure PRs
- [US-10: Inventory and SBOM per Build](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-10---inventário-e-sbom-por-build) - Signed SBOM per artefact
- [US-11: Vulnerability alerts](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-11---alertas-sobre-vulnerabilidades-em-componentes-usados) - Proactive notifications

### Ch. 06 - Secure Development {#cap-06---desenvolvimento-seguro}
Integrate **linters and SAST into the pipeline** to detect failures early and generate continuous evidence of compliance.

**User Stories:**
- [US-04: Automation in CI/CD](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-04---automatização-em-cicd-linters--sast) - Automatic linters and SAST
- [US-09: Pre-release security gate](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-09---gate-de-segurança-pré-release) - Consolidation of evidence
- [US-12: Mandatory local validation](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-12---validações-locais-obrigatórias-pre-commit) - Pre-commit hooks

### Ch. 07 - Secure CI/CD {#cap-07---cicd-seguro}
Design **pipelines with scanners, gates and release signatures**, ensuring that only validated artefacts advance from one phase to the next.

**User Stories:**
- [US-02: Secure pipeline design](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-02---design-seguro-dos-pipelines-versionamento-determinismo-e-revisão) - Versioned and auditable pipelines
- [US-04: Secrets management](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-04---gestão-de-segredos) - OIDC with short TTL
- [US-05: Runner isolation](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-05---isolamento-de-runners) - Ephemeral, segregated runners
- [US-06: Signing and provenance](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-06---assinatura-e-proveniência) - Trust in artefacts
- [US-13: Base image integrity validation](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-13---validação-de-integridade-de-imagens-base) - Supply chain protection

### Ch. 08 - IaC {#cap-08---iac}
Apply **policy enforcement** in IaC with *policy-as-code*, validating compliance before deployment.

**User Stories:**
- [US-01: Remote backend, locking and traceability](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-01---backend-remoto-locking-e-rastreabilidade) - Secure state without drift
- [US-02: Environment segregation, tagging and least-privilege permissions](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-02---segregação-de-ambientes-tagging-e-permissões-mínimas) - Isolation and traceability
- [US-05: Traceability, versioning and naming](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-05---rastreabilidade-versionamento-e-naming) - Complete history with rollback
- [US-06: Formal plan review before apply](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-06---revisão-formal-de-plan-antes-de-apply) - Impact validation
- [US-09: Signing and Provenance of IaC artefacts](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-09---assinatura-e-proveniência-de-artefactos-iac) - End-to-end integrity
- [US-10: Secrets and identity management for IaC](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-10---gestão-de-segredos-e-identidades-para-iac) - OIDC with least-privilege permissions
- [US-12: Rollback and destroy safeguard](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-12---rollback-e-salvaguarda-de-destroy) - Restore points

### Ch. 09 - Containers and Images {#cap-09---containers-e-imagens}
Run vulnerability scanners on every build, validate executions against formal policies (OPA/Kyverno), generate SBOM automatically, enforce a registry allowlist and SHA256 digests, prohibit static credentials, apply minimal RBAC and NetworkPolicy, maintain the Golden Images catalogue.

**User Stories:**
- [US-02: Automatic vulnerability validation of images](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-02---validação-automática-de-vulnerabilidades-em-imagens-no-pipeline-cicd) - SCA with automatic blocking
- [US-04: Formal runtime security policies](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-04---aplicação-de-políticas-formais-de-segurança-no-runtime-com-opakyverno) - OPA/Kyverno for validation
- [US-06: SBOM Generation and Traceability](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-06---geração-e-rastreabilidade-de-sbom-em-imagens) - Versioned SBOM per build
- [US-07: Registry Governance](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-07---governação-de-registries-com-allowlist-e-digest-only) - Allowlist + SHA256 digest
- [US-08: Secrets Management with OIDC](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-08---gestão-de-segredos-fora-da-imagem-com-oidc-e-workload-identity) - Ephemeral identities
- [US-09: Minimal RBAC and ServiceAccounts](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-09---rbac-mínimo-e-serviceaccounts-dedicadas) - Isolation per workload
- [US-10: Network Segmentation](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-10---segmentação-de-rede-e-networkpolicy) - NetworkPolicy per namespace
- [US-11: Golden Base Images](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-11---golden-base-images-com-patching-automático) - Standardised catalogue with SLA
- [US-12: Secure Builders and Runners](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-12---builders-e-runners-ephemerais-assinados-e-com-auditoria) - Protection of the CI/CD pipeline

### Ch. 10 - Security Testing {#cap-10---testes-de-segurança}
Integrate **automatic gates into the pipeline** (SAST/SCA/IAST) with thresholds per Lx. Centralise findings on a unified platform and automate delivery to the teams.

**User Stories:**
- [US-04: Security gates in CI/CD](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-04---gates-de-segurança-no-cicd) - Thresholds per criticality level
- [US-10: Centralised Findings Management](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-10---gestão-centralizada-de-findings-com-triagem-e-sla) - Unified platform
- [US-11: Automatic Findings Feedback](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-11---feedback-automático-de-findings-às-equipas) - Contextualised delivery

### Ch. 11 - Secure Deployment {#cap-11---deploy-seguro}
Deploy **only signed, versioned artefacts**. Implement fast rollback tested periodically, enable post-deploy monitoring, implement feature flags with metadata, ensure that secrets are never embedded, implement progressive deployment (canary/blue-green).

**User Stories:**
- [US-02: Deploy only signed artefacts](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-02---valida%C3%A7%C3%A3o-em-staging-antes-da-promo%C3%A7%C3%A3o) - Cryptographic integrity
- [US-05: Fast, tested rollback](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-05---rastreabilidade-end-to-end) - Documented and validated
- [US-06: Post-deploy monitoring](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-06---monitorização-pós-deploy) - Anomaly detection
- [US-08: Feature Flags with Governance](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-08---gestão-segura-de-segredos-no-deploy) - Metadata and expiry
- [US-09: Secure Secrets Management](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09---versionamento-semântico-e-changelog-técnico) - Zero secrets in artefacts
- [US-10: Progressive Deployment](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-10---deploy-progressivo-com-estratégias-canaryblue-green) - Canary/Blue-Green
- [US-11: Documented rollback per type](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-11---validações-técnicas-pré-deploy-com-gates-condicionais) - Tested rollback procedures

### Ch. 12 - Monitoring and Operations {#cap-12---monitorização-e-operações}
Configure production environments with **continuous monitoring** and coordinate alert response. Ensure log security and integrity (WORM retention), integrate with the SIEM.

**User Stories:**
- [US-06: Monitoring domains](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-06---classificação-e-cobertura-de-domínios-de-monitorização) - Coverage proportionate to risk
- [US-07: Log security and integrity](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-07---segurança-e-integridade-de-logs) - WORM retention + restricted access
- [US-08: SIEM integration](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-08---integração-com-siem-e-normalização-de-eventos) - Parsing and normalisation

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
