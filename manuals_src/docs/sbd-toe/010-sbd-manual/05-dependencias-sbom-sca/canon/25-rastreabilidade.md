---
id: rastreabilidade
title: Rastreabilidade — Capítulo 05: Dependências, SBOM e SCA
description: Rastreabilidade das práticas de gestão de dependências e supply chain face a frameworks normativos com pilot formal
tags: [rastreabilidade, dependencias, sbom, sca, supply-chain, ssdf, slsa, capec, cis, dora, nis2]
sidebar_position: 25
---

# Rastreabilidade — Capítulo 05: Dependências, SBOM e SCA

Este capítulo define práticas de **gestão segura de dependências** — inventário (SBOM), análise de composição (SCA), critérios de aceitação e governação de supply chain de software.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-TSV — Third-party & Supply Visibility | SBOM, inventário de dependências, controlo de origem |
| ACO-IVF — Integrity Verification & Findings | Análise contínua de vulnerabilidades (SCA), gestão de findings |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota |
|-----------|--------------------|-----------|----|
| SSDF PW.3 | Verify Third-Party Software | ✅ Explícito | Inventário sistemático (SBOM), critérios de aceitação SCA |
| SSDF PW.4 | Reuse Well-Secured Software | ✅ Semântico | Componentes controlados e com proveniência verificada |
| SSDF RV.1 | Identify and Confirm Vulnerabilities | ✅ Explícito | Análise SCA contínua, rastreabilidade de vulnerabilidades |
| CAPEC-185 | Malicious Software Download | ✅ Semântico | Controlo de origem, allowlist de componentes |
| CAPEC-446 | Malicious Logic via Third-Party Component | ✅ Semântico | SBOM, dependency risk, controlo de origem |
| CAPEC-691 | Spoof Open-Source Metadata | ⚠️ Parcial | Dependency confusion adjacent; metadata verification |
| CIS-2 | Inventory and Control of Software Assets | ⚠️ Parcial | Software inventory presente; CIS abrange âmbito mais largo |
| CIS-7 | Continuous Vulnerability Management | ⚠️ Parcial | Dependency scanning adjacent |
| ASVS architecture_and_dependency_hardening | Architecture & dependency hardening | ⚠️ Parcial | Dependências presente; hardening framing |
| SLSA-VERIFY-DEPENDENCIES | Check dependencies recursively | ⚠️ Parcial | SBOM e verification presente; recursão completa não garantida |
| DORA | Supply chain resilience | ✅ Explícito | Overlay regulatório publicado |
| NIS2 | Segurança de fornecedores e dependências | ✅ Explícito | Overlay regulatório publicado |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

---

## Modelos de maturidade — pendente de normalização

> Scores de maturidade (SAMM, DSOMM, BSIMM) estão pendentes de pilot formal.  
> Ver [achievable-maturity.md](../achievable-maturity.md) para o mapeamento de maturidade em curso.

| Modelo | Domínios relevantes |
|--------|---------------------|
| OWASP SAMM v2.1 | Operations → Component Management |
| OWASP DSOMM | Build & Deploy, Governance, Verification |
| BSIMM13 | Software Feature Design (SFD) |

---

## Ligações com outros capítulos

- **Cap. 01** — classificação de risco determina profundidade da análise SCA
- **Cap. 07** — SBOM e SCA integrados como gates no pipeline CI/CD
- **Cap. 09** — dependências de imagens base geridas via SBOM
- **Cap. 10** — scanning de dependências como parte da estratégia de testes
- **Cap. 14** — cláusulas contratuais de supply chain com fornecedores
