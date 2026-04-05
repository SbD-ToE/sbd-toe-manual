---
id: rastreabilidade
title: Rastreabilidade — Capítulo 08: IaC e Infraestrutura como Código
description: Rastreabilidade das práticas de IaC face a frameworks normativos com pilot formal
tags: [rastreabilidade, iac, infraestrutura, ssdf, slsa, capec, asvs, cis, nis2]
sidebar_position: 25
---

# Rastreabilidade — Capítulo 08: IaC e Infraestrutura como Código

Este capítulo define práticas de **infraestrutura definida como código** — validação, enforcement de políticas, gestão de segredos e segregação de ambientes — como camada de enforcement contínuo.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-SCBI — Secure Coding & Build Integrity | IaC como código sujeito às mesmas práticas de revisão e validação |
| ACO-SPC — Security Policy & Controls | Policy-as-code, OPA/Conftest, enforcement de políticas de segurança |
| ACO-TSV — Third-party & Supply Visibility | Controlo de módulos externos, proveniência de componentes IaC |

> **Nota adjunct:** CIS-4 e ASVS `secure_configuration_baseline_gap` têm pressão significativa aqui. IaC tem semantics de configuração segura mas sem secção dedicada a baseline integrity. Candidato ao adjunct `secure_configuration_baseline_integrity` (pendente de promoção).

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota |
|-----------|--------------------|-----------|----|
| SSDF PO.3 | Implement Supporting Toolchains | ✅ Explícito | IaC como toolchain formal e controlado |
| SSDF PW.3 | Verify Third-Party Software | ✅ Explícito | Módulos IaC externos validados |
| SSDF PW.6 | Configure the Build and Test Environments | ✅ Explícito | Ambientes definidos e validados via IaC |
| SSDF RV.3 | Analyze Vulnerabilities to Root Causes | ✅ Explícito | Análise de vulnerabilidades em IaC |
| SLSA-BUILD-L2 | Hosted build platform | ✅ Explícito | IaC e pipeline integrados |
| SLSA-PRODUCER-CHOOSE-BUILD-PLATFORM | Choose build platform | ⚠️ Parcial | IaC e runners |
| SLSA-BUILD-PLATFORM-ISOLATION | Isolation strength | ⚠️ Parcial | IaC segmentation semântica |
| CAPEC-511 | Infiltration of Software Development Environment | ⚠️ Parcial | IaC infrastructure compromise |
| CIS-4 | Secure Configuration of Enterprise Assets | ⚠️ Parcial | IaC hardening; enterprise config além do âmbito AppSec |
| ASVS protected_secret_storage | Secret storage | ⚠️ Parcial | IaC e gestão de cofres |
| ASVS secret_leak_prevention | Secret leak prevention | ⚠️ Parcial | IaC e prevenção de exposição |
| ASVS secret_usage_isolation | Secret usage isolation | ⚠️ Parcial | IaC e isolamento de segredos |
| ASVS secure_transport | Secure transport | ⚠️ Parcial | IaC e deploy |
| ASVS service_to_service_auth | Service-to-service auth | ⚠️ Parcial | IaC |
| ASVS secure_configuration_baseline_gap | Secure configuration baseline | 🔴 Gap | IaC tem semantics; sem secção dedicada a baseline integrity |
| NIS2 | Infraestrutura como código governada | ✅ Explícito | Overlay regulatório publicado |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

---

## Modelos de maturidade — pendente de normalização

> Scores de maturidade (SAMM, DSOMM, BSIMM) estão pendentes de pilot formal.  
> Ver [achievable-maturity.md](../achievable-maturity.md) para o mapeamento de maturidade em curso.

| Modelo | Domínios relevantes |
|--------|---------------------|
| OWASP SAMM v2.1 | Implementation → Environment Hardening |
| OWASP DSOMM | Design & Development, Build & Test |
| BSIMM13 | Configuration & Deployment (CD1–CD3) |

---

## Ligações com outros capítulos

- **Cap. 01** — proporcionalidade de validação por risco de ambiente
- **Cap. 02** — requisitos IAC-XXX definidos e validados aqui
- **Cap. 07** — controlos IaC aplicados e orquestrados no pipeline
- **Cap. 09** — containers dependem da infraestrutura provisionada aqui
- **Cap. 14** — exceções técnicas de IaC legitimadas pelo processo de governação
