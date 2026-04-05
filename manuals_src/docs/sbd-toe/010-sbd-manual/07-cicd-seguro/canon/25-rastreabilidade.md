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
| ACO-SCBI — Supply Chain & Build Integrity | Integridade do build, execução autenticada, assinatura de artefactos, supply chain do pipeline |
| ACO-RPR — Release Promotion, Controlled Rollout & Rollback Readiness | Proveniência, trusted builders, gates de promoção, rollout controlado |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota | Fonte verificada |
|-----------|--------------------|-----------|----|-----------------|
| SSDF PW.4 | Establish Security Criteria | ✅ Explícito | Gates de segurança por risco (L1–L3) | aplicacao_lifecycle (strong): US-07 — Gates por risco |
| SSDF PW.7 | Review and/or Analyze Code | ✅ Explícito | Validação obrigatória antes de promoção | addon (medium): Segurança do código dentro do pipeline |
| SSDF PS.3 | Archive and Protect Each Release | ✅ Explícito | Assinatura e proveniência end-to-end | addon (medium): Integridade e proveniência de artefactos |
| SSDF RV.3 | Analyze Vulnerabilities to Root Causes | ✅ Explícito | Análise pós-build; rastreabilidade de findings | addon (medium): Validações de segurança integradas no pipeline |
| SSDF GV.2 | Perform Security Checkpoints | ✅ Explícito | Governação e rastreabilidade de execuções | aplicacao_lifecycle (strong): US-09 — Rastreabilidade ponta-a-ponta |
| SSDF GV.3 | Implement Vulnerability Response Processes | ✅ Explícito | Logs, segregação rastreável | addon (medium): Rastreabilidade de assinaturas e deploys |
| SLSA-BUILD-L1 | Provenance exists | ✅ Explícito | Artefactos assinados e com proveniência | addon (medium): Integridade e proveniência de artefactos |
| SLSA-BUILD-L2 | Hosted build platform | ✅ Explícito | Plataforma de build controlada e auditada | requirements_catalog (strong): Catálogo CIC — CI/CD Seguro |
| SLSA-BUILD-L3 | Hardened builds | ⚠️ Parcial | Hardening presente; L3 exige isolamento mais específico | addon (medium): Isolamento e proteção de runners |
| SLSA-PRINCIPLE-PREFER-ATTESTATIONS | Prefer attestations | ✅ Explícito | Assinatura e attestation de artefactos | addon (medium): Integridade e proveniência de artefactos |
| SLSA-PRODUCER-DISTRIBUTE-PROVENANCE | Distribute provenance | ✅ Explícito | Proveniência distribuída com artefactos | addon (medium): Rastreabilidade de assinaturas e deploys |
| SLSA-BUILD-PLATFORM-PROVENANCE-GENERATION | Provenance generation | ✅ Explícito | CI/CD provenance gerada no pipeline | aplicacao_lifecycle (strong): US-06 — Assinatura e proveniência |
| SLSA-PRODUCER-CONSISTENT-BUILD | Consistent build process | ✅ Semântico | Pipeline-as-code versionado e determinístico | aplicacao_lifecycle (strong): US-14 — Reprodutibilidade e determinismo |
| SLSA-PRODUCER-CHOOSE-BUILD-PLATFORM | Choose build platform | ⚠️ Parcial | Runners e plataformas controladas | addon (medium): Isolamento e proteção de runners |
| SLSA-BUILD-PLATFORM-ISOLATION | Isolation strength | ⚠️ Parcial | Runner isolation presente; L3 mais específico | addon (medium): Isolamento e proteção de runners |
| SLSA-VERIFY-BUILD-LEVEL | Check SLSA Build level | ⚠️ Parcial | Critérios de verificação presentes | requirements_catalog (strong): Catálogo CIC — CI/CD Seguro |
| CAPEC-445 | Replication Through Removable Media / Config Manipulation | ⚠️ Parcial | Pipeline integrity | addon (medium): Design seguro dos pipelines |
| CAPEC-511 | Infiltration of Software Development Environment | ⚠️ Parcial | CI/CD infrastructure compromise | addon (medium): Gestão segura de código fonte |
| CIS-2 | Inventory and Control of Software Assets | ⚠️ Parcial | Software authorization e CI/CD toolchain | addon (medium): Políticas e gates por nível de aplicação |
| ASVS log_integrity_and_protection | Log integrity | ✅ Explícito | Rastreabilidade de deploys e integridade de logs | addon (medium): Rastreabilidade de assinaturas e deploys |
| ASVS security_event_logging_coverage | Security logging | ⚠️ Parcial | CI/CD logging adjacent | addon (medium): Excepções e Visibilidade em CI/CD |
| SSDF PO.5 | Implement and Maintain Secure Environments for Software Development | 🔧 Reparação | Ambientes de CI/CD segregados e runners isolados cobertos semanticamente; sem row SSDF PO.5 explícita publicada | addon (medium): Isolamento e proteção de runners |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Metodologia:** Cobertura verificada contra `ontology_discovery_units.jsonl` (4139 units, manual completo). "Explícito" = unit normative_weight strong/medium com heading directo. "Semântico" = conteúdo confirmado em addon ou via mapeamento canónico. "Parcial" = sem unit dedicado no capítulo.

---

## Modelos de maturidade — pendente de normalização

> ⏳ pendente — Scores de maturidade (SAMM, DSOMM, BSIMM) estão pendentes de pilot formal.  
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
