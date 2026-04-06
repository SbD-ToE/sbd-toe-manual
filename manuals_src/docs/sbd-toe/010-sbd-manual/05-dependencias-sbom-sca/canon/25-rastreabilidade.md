---
id: rastreabilidade
title: "Rastreabilidade — Capítulo 05: Dependências, SBOM e SCA"
description: Rastreabilidade das práticas de gestão de dependências e supply chain face a frameworks normativos com pilot formal
tags: [rastreabilidade, dependencias, sbom, sca, supply-chain, ssdf, slsa, capec, cis, dora, nis2]
sidebar_position: 25

---


> **Método:** Ver [Metodologia de Validação de Claims](../../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# Rastreabilidade — Capítulo 05: Dependências, SBOM e SCA

Este capítulo define práticas de **gestão segura de dependências** — inventário (SBOM), análise de composição (SCA), critérios de aceitação e governação de supply chain de software.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-SCBI — Supply Chain & Build Integrity | SBOM, inventário de dependências, controlo de origem, supply chain threats |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota | Fonte verificada |
|-----------|--------------------|-----------|----|-----------------|
| SSDF PW.3 | Verify Third-Party Software | ✅ Explícito | Inventário sistemático (SBOM), critérios de aceitação SCA | requirements_catalog (strong): Catálogo DEP — Dependências, SBOM e SCA |
| SSDF PW.4 | Reuse Well-Secured Software | ✅ Semântico | Componentes controlados e com proveniência verificada | addon (medium): Controlo de Registos e Origem de Pacotes |
| SSDF RV.1 | Identify and Confirm Vulnerabilities | ✅ Explícito | Análise SCA contínua, rastreabilidade de vulnerabilidades | aplicacao_lifecycle (strong): US-03 — SCA automático com gates |
| CAPEC-185 | Malicious Software Download | ✅ Semântico | Controlo de origem, allowlist de componentes | addon (medium): Ameaças à Cadeia de Fornecimento (Supply Chain) |
| CAPEC-446 | Malicious Logic via Third-Party Component | ✅ Semântico | SBOM, dependency risk, controlo de origem | addon (medium): Ameaças à Cadeia de Fornecimento (Supply Chain) |
| CAPEC-691 | Spoof Open-Source Metadata | ⚠️ Parcial | Dependency confusion adjacent; metadata verification | addon (medium): Controlo de Registos e Origem de Pacotes |
| CIS-2 | Inventory and Control of Software Assets | ⚠️ Parcial | Software inventory presente; CIS abrange âmbito mais largo | addon (medium): Inventário de Dependências e SBOM |
| CIS-7 | Continuous Vulnerability Management | ⚠️ Parcial | Dependency scanning adjacent | addon (medium): Análise de Vulnerabilidades em Dependências (SCA) |
| ASVS architecture_and_dependency_hardening | Architecture & dependency hardening | ⚠️ Parcial | Dependências presente; hardening framing | addon (medium): Governança de Bibliotecas e Componentes de Terceiros |
| SLSA-VERIFY-DEPENDENCIES | Check dependencies recursively | ⚠️ Parcial | SBOM e verification presente; recursão completa não garantida | addon (medium): Inventário de Dependências e SBOM |
| DORA | Supply chain resilience | ✅ Explícito | Overlay regulatório publicado | aplicacao_lifecycle (strong): US-06 — Repositórios internos como fonte única |
| NIS2 | Segurança de fornecedores e dependências | ✅ Explícito | Overlay regulatório publicado | aplicacao_lifecycle (strong): US-01 — Gestão de dependências seguras |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Metodologia:** Cobertura verificada contra `ontology_discovery_units.jsonl` (4139 units, manual completo). "Explícito" = unit normative_weight strong/medium com heading directo. "Semântico" = conteúdo confirmado em addon ou via mapeamento canónico. "Parcial" = sem unit dedicado no capítulo.

---

## Maturidade — referência separada

A leitura de maturidade deste capítulo é tratada em [achievable-maturity.md](../achievable-maturity.md).

Neste documento, os modelos de maturidade surgem apenas como contexto editorial complementar. A sua normalização formal é apresentada no documento dedicado do capítulo.

---

## Ligações com outros capítulos

- **Cap. 01** — classificação de risco determina profundidade da análise SCA
- **Cap. 07** — SBOM e SCA integrados como gates no pipeline CI/CD
- **Cap. 09** — dependências de imagens base geridas via SBOM
- **Cap. 10** — scanning de dependências como parte da estratégia de testes
- **Cap. 14** — cláusulas contratuais de supply chain com fornecedores
