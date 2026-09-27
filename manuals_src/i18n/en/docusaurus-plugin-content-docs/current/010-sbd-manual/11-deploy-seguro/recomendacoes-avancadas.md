---
id: recomendacoes-avancadas
title: Advanced Recommendations
description: Advanced practices to reinforce the security, traceability and auditability of critical deployments.
tags: [tipo:avancado, grupo:execucao, tema:deploy, validação, reversibilidade, maturidade]
sidebar_position: 30
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/recomendacoes-avancadas.md
  source_sha256: 64a263ac029bdea2c940090b8c4ba7f9f34eb7c6458b32f1b61c337915c7df41
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: c93c72a2fb5a9aa5491becb8a02a993f691bc12f3e8da82c5f29fdb5271cbd5e
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, cycle_iteration, maturity, provenance, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 1697342abc868ef456837d2f93b12f37484c318b593f69c008e8feb9599179ab
  translated_at: 2026-09-26T11:00:58Z
  stamped_at: 2026-09-26T18:35:36Z
  reviewed_by: null
---


# Advanced Recommendations for Secure Deployment

This document complements the base practices of Chapter 11 - Secure Deployment with **technical and organisational recommendations for contexts of greater maturity**, increasing the resilience, traceability and auditability of deliveries to production.

The practices described here are not mandatory, but **highly recommended for applications classified as L3 or in regulated environments**.

---

## 1. Deployment Validated on the Basis of Observability {#1-deploy-validado-com-base-em-observabilidade}

- Use of *dashboards* with readiness metrics for automatic gating;
- Configuration of *canary release* with *automatic promotion* and rollback.

## 2. Reversibility Validated in the Pipeline {#2-reversibilidade-validada-em-pipeline}

- Execution of rollback in staging before each release;
- Scripts tested and documented as part of the build.

## 3. Signed Release Contract {#3-contrato-de-release-assinado}

- `release-contract.yaml` file containing:
  - Versions, owners, validations, exceptions, rollback;
- Digital signature or hash for later validation.

## 4. Deployment with Provenance Verification {#4-deploy-com-verificação-de-proveniência}

- Validation of SBOM, signature, provenance and build agent;
- Requirement for authorised pipelines.

## 5. Formalised "Break-Glass" Policy {#5-política-de-break-glass-formalizada}

- Approved process for emergency deployments:
  - Mandatory audit;
  - Dual approval (product + security);
  - Planned post-event rollback.

## 6. Post-Production Security Verification {#6-verificação-de-segurança-pós-produção}

- Execution of runtime-aware tests:
  - HTTP headers, ports, endpoints;
  - Hardening validation.

## 7. Dashboards with Deployment Traceability {#7-dashboards-com-rastreabilidade-de-deploy}

- Visualisation per release:
  - Date, owners, validations, findings, rollback and SLOs.

## 8. Multi-Factor Approval of Critical Deployments {#8-aprovação-multi-fatorial-de-deploys-críticos}

- Approval by security + product + operations;
- Based on a checklist and technical evidence.

## 9. Reinforced Immutability at Runtime {#9-reforço-de-imutabilidade-no-runtime}

- Prohibition of post-deployment modifications;
- Rejection of manual patches or “hotfixes” outside the build cycle.

## 10. Environment Integrity Verification {#10-verificação-de-integridade-do-ambiente}

- Checksum, versions, permissions, configurations and environment variables;
- Validation before and after deployment.

## 11. *Release Freezing* with Time-Based Revalidation {#11-release-freezing-com-revalidação-temporal}

- Automatic freeze of releases that remain more than `X` days without promotion;
- Mandatory re-execution of security validations before deployment;
- Avoids the promotion of obsolete artefacts without revalidation.

## 12. Secure Configuration Management in Deployment {#12-gestão-de-configuração-segura-no-deploy}

- Validation of the integrity of `secrets`, feature toggles and `config maps`;
- Policy enforcement via OPA/Rego or Kyverno;
- Approval of sensitive changes via controlled PRs.

## 13. Automatic Lockdown after Critical Deployment {#13-lockdown-automático-após-deploy-crítico}

- Application of a temporary *lockdown* after critical deployments:
  - Deactivation of experimental toggles;
  - Restriction of administrative access;
  - Reinforced logging until stabilisation.

---

## ✅ Conclusion {#-conclusão}

These advanced practices extend the chapter's base model, covering scenarios of **high operational demand**, including:

- Management of old artefacts and expiry of validations;
- Security and traceability of configuration in real time;
- Lockdown and proactive containment of risk in production.

> 📌 Their application is especially relevant in contexts of **high availability, high reputational impact or regulatory requirements**.

> 💡 Deployment maturity does not depend only on the tool used, but **on the ability to take secure, justified and auditable decisions about what goes into production.**
