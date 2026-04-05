---
id: rastreabilidade
title: Rastreabilidade — Capítulo 07: CI/CD Seguro
description: Rastreabilidade das práticas de segurança de pipeline face a frameworks normativos com pilot formal
tags: [rastreabilidade, cicd, supply-chain, ssdf, slsa, capec, asvs, cis]
sidebar_position: 25
---

# Rastreabilidade — Capítulo 07: CI/CD Seguro

Este capítulo define práticas de **segurança operacional para pipelines CI/CD** — o pipeline como ativo crítico da cadeia de fornecimento de software. É o capítulo com maior pressão de supply chain e SLSA.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-SCBI — Secure Coding & Build Integrity | Integridade do build, execução autenticada, assinatura de artefactos |
| ACO-RPR — Release Process & Readiness | Proveniência, trusted builders, gates de promoção |
| ACO-IVF — Integrity Verification & Findings | Validação contínua, rastreabilidade de execuções |
| ACO-TSV — Third-party & Supply Visibility | Controlo de dependências externas no pipeline (actions, scripts) |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota |
|-----------|--------------------|-----------|----|
| SSDF PW.4 | Establish Security Criteria | ✅ Explícito | Gates de segurança por risco (L1–L3) |
| SSDF PW.7 | Review and/or Analyze Code | ✅ Explícito | Validação obrigatória antes de promoção |
| SSDF PS.3 | Archive and Protect Each Release | ✅ Explícito | Assinatura e proveniência end-to-end |
| SSDF RV.3 | Analyze Vulnerabilities to Root Causes | ✅ Explícito | Row publicada; análise pós-build |
| SSDF GV.2 | Perform Security Checkpoints | ✅ Explícito | Governação e rastreabilidade de execuções |
| SSDF GV.3 | Implement Vulnerability Response Processes | ✅ Explícito | Logs, segregação rastreável |
| SLSA-BUILD-L1 | Provenance exists | ✅ Explícito | Artefactos assinados e com proveniência |
| SLSA-BUILD-L2 | Hosted build platform | ✅ Explícito | Row publicada |
| SLSA-BUILD-L3 | Hardened builds | ⚠️ Parcial | Hardening presente; L3 exige isolamento mais específico |
| SLSA-PRINCIPLE-PREFER-ATTESTATIONS | Prefer attestations | ✅ Explícito | Row publicada |
| SLSA-PRODUCER-DISTRIBUTE-PROVENANCE | Distribute provenance | ✅ Explícito | Row publicada |
| SLSA-BUILD-PLATFORM-PROVENANCE-GENERATION | Provenance generation | ✅ Explícito | CI/CD provenance |
| SLSA-PRODUCER-CONSISTENT-BUILD | Consistent build process | ✅ Semântico | Pipeline-as-code |
| SLSA-PRODUCER-CHOOSE-BUILD-PLATFORM | Choose build platform | ⚠️ Parcial | Runners e plataformas controladas |
| SLSA-BUILD-PLATFORM-ISOLATION | Isolation strength | ⚠️ Parcial | Runner isolation presente; L3 mais específico |
| SLSA-VERIFY-BUILD-LEVEL | Check SLSA Build level | ⚠️ Parcial | Critérios de verificação presentes |
| CAPEC-445 | Replication Through Removable Media / Config Manipulation | ⚠️ Parcial | Pipeline integrity |
| CAPEC-511 | Infiltration of Software Development Environment | ⚠️ Parcial | CI/CD infrastructure compromise |
| CIS-2 | Inventory and Control of Software Assets | ⚠️ Parcial | Software authorization e CI/CD toolchain |
| ASVS log_integrity_and_protection | Log integrity | ✅ Explícito | Row publicada |
| ASVS security_event_logging_coverage | Security logging | ⚠️ Parcial | CI/CD logging adjacent |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

---

## Modelos de maturidade — pendente de normalização

> Scores de maturidade (SAMM, DSOMM, BSIMM) estão pendentes de pilot formal.  
> Ver [achievable-maturity.md](../achievable-maturity.md) para o mapeamento de maturidade em curso.

| Modelo | Domínios relevantes |
|--------|---------------------|
| OWASP SAMM v2.1 | Implementation → Build & Deployment Automation |
| OWASP DSOMM | Build, Test, Release, Operate |
| BSIMM13 | Software Environment, Compliance & Policy |

---

## Ligações com outros capítulos

- **Cap. 05** — SBOM e SCA integrados como gates no pipeline
- **Cap. 06** — práticas de codificação aplicadas como passos automatizados
- **Cap. 08** — IaC como base de configuração dos ambientes de build
- **Cap. 09** — imagens produzidas e assinadas por este pipeline
- **Cap. 10** — testes de segurança integrados como gates obrigatórios
