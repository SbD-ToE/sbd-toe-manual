---
id: rastreabilidade
title: Rastreabilidade — Capítulo 09: Containers e Imagens
description: Rastreabilidade das práticas de segurança de containers face a frameworks normativos com pilot formal
tags: [rastreabilidade, containers, imagens, ssdf, slsa, capec, asvs]
sidebar_position: 25
---

# Rastreabilidade — Capítulo 09: Containers e Imagens

Este capítulo define práticas de **construção, assinatura, proveniência, hardening e execução segura de containers e imagens** — desde o build até ao runtime.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-RPR — Release Process & Readiness | Assinatura de imagens, proveniência, aprovação antes de deploy |
| ACO-TSV — Third-party & Supply Visibility | Imagens base e dependências de containers |
| ACO-IVF — Integrity Verification & Findings | Image scanning, validação de manifesto, findings por severidade |

> **Nota adjunct:** ASVS `secure_configuration_baseline_gap` tem pressão aqui — containers têm semantics de configuração segura (securityContext, policies) mas sem secção dedicada. Candidato ao adjunct `secure_configuration_baseline_integrity` (pendente de promoção).

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota |
|-----------|--------------------|-----------|----|
| SSDF PW.5 | Create Source Code with Secure Coding Techniques | ✅ Explícito | Integridade de imagem; digest pinning; reprodutibilidade |
| SSDF PS.1 | Protect Code and Data from Unauthorized Access | ✅ Explícito | Manifesto e aprovação formal antes de deploy |
| SSDF RV.1 | Identify and Confirm Vulnerabilities | ✅ Explícito | Image scanning contínuo com bloqueios por severidade |
| SSDF RV.2 | Assess, Prioritize, and Remediate Vulnerabilities | ✅ Explícito | Scanning + critérios de aceitação formais |
| SLSA-BUILD-L1 | Provenance exists | ✅ Explícito | Artefactos assinados; proveniência presente |
| SLSA-BUILD-L3 | Hardened builds | ⚠️ Parcial | Hardening presente; L3 exige isolamento mais específico |
| SLSA-PRINCIPLE-PREFER-ATTESTATIONS | Prefer attestations | ✅ Explícito | Atestações e proveniência de imagens |
| SLSA-PRODUCER-DISTRIBUTE-PROVENANCE | Distribute provenance | ✅ Explícito | Row publicada |
| SLSA-BUILD-PLATFORM-PROVENANCE-GENERATION | Provenance generation | ✅ Explícito | Container provenance |
| SLSA-BUILD-PLATFORM-ISOLATION | Isolation | ⚠️ Parcial | Container isolation semântica |
| SLSA-VERIFY-DEPENDENCIES | Check dependencies | ⚠️ Parcial | Container deps e SBOM presentes |
| CAPEC-206 | Signing Malicious Code | ✅ Semântico | Artefactos assinados com verificação |
| CAPEC-186 | Malicious Software Update | ✅ Semântico | Promoção verificada via digest pinning |
| ASVS secure_configuration_baseline_gap | Secure configuration baseline | 🔴 Gap | Containers têm semantics; sem secção dedicada a baseline |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

---

## Modelos de maturidade — pendente de normalização

> Scores de maturidade (SAMM, DSOMM, BSIMM) estão pendentes de pilot formal.  
> Ver [achievable-maturity.md](../achievable-maturity.md) para o mapeamento de maturidade em curso.

| Modelo | Domínios relevantes |
|--------|---------------------|
| OWASP SAMM v2.1 | Implementation → Deployment, Verification |
| OWASP DSOMM | Supply Chain, Build & Deploy, Ops Monitoring |
| BSIMM13 | CMVM 1.3, SE 2.2, ST 1.1–1.4 |

---

## Ligações com outros capítulos

- **Cap. 05** — inventário de componentes e vulnerabilidades herdadas pelas imagens base
- **Cap. 07** — gates de controlo automático no pipeline (policy enforcement, proveniência)
- **Cap. 08** — manifests de deploy coerentes com a infraestrutura provisionada
- **Cap. 10** — scanners e testes funcionais de segurança integrados
- **Cap. 14** — políticas de operação de registos, retenção e auditoria
