---
id: rastreabilidade
title: Rastreabilidade — Capítulo 14: Governança e Contratação
description: Rastreabilidade das práticas de governança e contratação face a frameworks normativos com pilot formal
tags: [rastreabilidade, governanca, contratos, fornecedores, ssdf, cis, asvs, dora, nis2]
sidebar_position: 25
---

# Rastreabilidade — Capítulo 14: Governança e Contratação Segura

Este capítulo define práticas de **governação formal** — exceções, cláusulas contratuais, ownership, onboarding de terceiros — como mecanismo transversal de enforcement e conformidade do modelo SbD-ToE.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-SLG — Security Lifecycle & Governance | Governance formal, KPIs, ciclo de vida de conformidade |
| ACO-SPC — Security Policy & Controls | Políticas formais, cláusulas contratuais, enforcement de controlos |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota |
|-----------|--------------------|-----------|----|
| SSDF PO.1 | Define Security Requirements | ✅ Explícito | Row publicada; governação de requisitos e exceções |
| SSDF PO.2 | Implement Roles and Responsibilities | 🔧 Reparação | Ownership forte; sem row explicita PO.2 publicada — rastreabilidade precisa de authoring em Cap. 00 + 13 + 14 |
| SSDF PO.3 | Implement Supporting Toolchains | ✅ Explícito | Row publicada |
| SSDF RV.2 | Assess, Prioritize, and Remediate Vulnerabilities | ⚠️ Parcial | Ações corretivas e auditoria; RV.2 mais técnico que governação |
| CIS-5 | Account Management | ⚠️ Parcial | Governance semantics |
| CIS-15 | Service Provider Management | ✅ Semântico | Gestão e validação contínua de fornecedores (15.1, 15.6) |
| CIS-17 | Incident Response Management | ✅ Semântico | Auditoria e governação de conformidade (17.1) |
| ASVS authorization_and_least_privilege | Authorization | ⚠️ Parcial | Governance semantics |
| ASVS protected_secret_storage | Secret storage | ⚠️ Parcial | Governance adjacente |
| DORA | Governança e contratação | ✅ Explícito | Overlay regulatório publicado |
| NIS2 | Governança de fornecedores | ✅ Explícito | Overlay regulatório publicado |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Nota SSDF PO.2:** A rastreabilidade completa de PO.2 distribui-se por Cap. 00 (definição de papéis), Cap. 13 (formação e validação) e este capítulo (ownership formal e governação). A ausência de uma row PO.2 explícita publicada é o único item de reparação activo neste capítulo.

---

## Modelos de maturidade — pendente de normalização

> Scores de maturidade (SAMM, DSOMM, BSIMM) estão pendentes de pilot formal.  
> Ver [achievable-maturity.md](../achievable-maturity.md) para o mapeamento de maturidade em curso.

| Modelo | Domínios relevantes |
|--------|---------------------|
| OWASP SAMM v2.1 | Governance → Strategy & Metrics, Supplier Management |
| OWASP DSOMM | Governance, Third-Party Management, Policies & Standards |
| BSIMM13 | Strategy & Metrics (SM1–SM3), Compliance & Policy (CP1) |

---

## Ligações com outros capítulos

- **Cap. 00** — papéis e responsabilidades formalizados aqui via ownership
- **Cap. 01** — critérios de risco aplicados a decisões de exceção
- **Cap. 05** — cláusulas de supply chain e gestão SCA com fornecedores
- **Cap. 07 / 09** — contratualização de práticas CI/CD e execução segura
- **Cap. 13** — controlo de formação estendido a terceiros e fornecedores
