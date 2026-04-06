---
id: rastreabilidade
title: "Rastreabilidade — Capítulo 14: Governança e Contratação"
description: Rastreabilidade das práticas de governança e contratação face a frameworks normativos com pilot formal
tags: [rastreabilidade, governanca, contratos, fornecedores, ssdf, cis, asvs, dora, nis2]
sidebar_position: 25

---


> **Método:** Ver [Metodologia de Validação de Claims](../../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# Rastreabilidade — Capítulo 14: Governança e Contratação Segura

Este capítulo define práticas de **governação formal** — exceções, cláusulas contratuais, ownership, onboarding de terceiros — como mecanismo transversal de enforcement e conformidade do modelo SbD-ToE.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-SLG — Security Event Logging, Audit Trail & Centralized Logging | Governance formal, KPIs, audit trail de conformidade, ciclo de vida de exceções |
| ACO-SCBI — Supply Chain & Build Integrity | Gestão de fornecedores, cláusulas contratuais de supply chain, validação de terceiros |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota | Fonte verificada |
|-----------|--------------------|-----------|----|-----------------|
| SSDF PO.1 | Define Security Requirements | ✅ Explícito | Governação de requisitos e exceções formalizadas | requirements_catalog (strong): Catálogo GOV - Governação e Contratação |
| SSDF PO.2 | Implement Roles and Responsibilities | 🔧 Reparação | Ownership forte; sem row explícita PO.2 publicada — rastreabilidade distribuída por Cap. 00 + 13 + 14 | addon (medium): Modelo de Governação para Security by Design |
| SSDF PO.3 | Implement Supporting Toolchains | ✅ Explícito | Toolchain de governação publicada | requirements_catalog (strong): Catálogo GOV - Governação e Contratação |
| SSDF RV.2 | Assess, Prioritize, and Remediate Vulnerabilities | ⚠️ Parcial | Ações corretivas e auditoria; RV.2 mais técnico que governação | addon (medium): Validação Continuada e Revisões |
| CIS-5 | Account Management | ⚠️ Parcial | Governance semântico; offboarding e gestão de acessos | addon (medium): Checklist de Offboarding Seguro |
| CIS-15 | Service Provider Management | ✅ Semântico | Gestão e validação contínua de fornecedores (15.1, 15.6) | addon (medium): Modelo de Validação de Fornecedores e Terceiros |
| CIS-17 | Incident Response Management | ✅ Semântico | Auditoria e governação de exceções e conformidade (17.1) | addon (medium): Processo Canónico de Gestão de Excepções |
| ASVS authorization_and_least_privilege | Authorization | ⚠️ Parcial | Governance semântico; sem unit dedicado | sem unit dedicado no capítulo |
| ASVS protected_secret_storage | Secret storage | ⚠️ Parcial | Governance adjacente; sem unit dedicado | sem unit dedicado no capítulo |
| DORA | Governança e contratação | ✅ Explícito | Overlay regulatório publicado | requirements_catalog (strong): Catálogo GOV + addon (medium): Cláusulas Contratuais de Segurança |
| NIS2 | Governança de fornecedores | ✅ Explícito | Overlay regulatório publicado | requirements_catalog (strong): Catálogo GOV - Governação e Contratação |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Nota SSDF PO.2:** A rastreabilidade completa de PO.2 distribui-se por Cap. 00 (definição de papéis), Cap. 13 (formação e validação) e este capítulo (ownership formal e governação). A ausência de uma row PO.2 explícita publicada é o único item de reparação activo neste capítulo.

> **Metodologia:** Cobertura verificada contra `ontology_discovery_units.jsonl` (4139 units, manual completo). "Explícito" = unit normative_weight strong/medium com heading directo. "Semântico" = conteúdo confirmado em addon ou via mapeamento canónico. "Parcial" = sem unit dedicado no capítulo.

---

## Maturidade — referência separada

A leitura de maturidade deste capítulo é tratada em [achievable-maturity.md](../achievable-maturity.md).

Neste documento, os modelos de maturidade surgem apenas como contexto editorial complementar. A sua normalização formal é apresentada no documento dedicado do capítulo.

---

## Ligações com outros capítulos

- **Cap. 00** — papéis e responsabilidades formalizados aqui via ownership
- **Cap. 01** — critérios de risco aplicados a decisões de exceção
- **Cap. 05** — cláusulas de supply chain e gestão SCA com fornecedores
- **Cap. 07 / 09** — contratualização de práticas CI/CD e execução segura
- **Cap. 13** — controlo de formação estendido a terceiros e fornecedores
