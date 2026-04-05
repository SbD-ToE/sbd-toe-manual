---
id: rastreabilidade
title: Rastreabilidade — Capítulo 13: Formação e Onboarding
description: Rastreabilidade das práticas de formação e onboarding face a frameworks normativos com pilot formal
tags: [rastreabilidade, formacao, onboarding, ssdf, cis, nis2]
sidebar_position: 25
---

# Rastreabilidade — Capítulo 13: Formação e Onboarding Seguro

Este capítulo define **programas de formação por papel** — contínuos, rastreáveis, com validação de conhecimento — como componente crítica da adoção do SbD-ToE.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-SLG — Security Lifecycle & Governance | Formação como componente do ciclo de vida organizacional de segurança |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota |
|-----------|--------------------|-----------|----|
| SSDF PO.2 | Implement Roles and Responsibilities | ✅ Semântico | PO.2.1/PO.2.2 cobertos via formação por função; conteúdo primário de PO.2 está em Cap. 00 |
| SSDF PO.2.1 | Each role receives security training | ✅ Explícito | Formação obrigatória por papel com rastreabilidade |
| SSDF PO.2.2 | Validate security knowledge before access | ✅ Explícito | Validação de conhecimento antes de atribuição de privilégios |
| CIS-14 | Security Awareness and Skills Training | ✅ Explícito | 14.1/14.2/14.3 — formação proporcional ao risco, validação de acesso, formação contínua |
| ASVS authentication_lifecycle | Auth lifecycle & recovery | ⚠️ Parcial | Onboarding semantics |
| NIS2 | Capacitação e onboarding de segurança | ✅ Explícito | Overlay regulatório publicado |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

> **Nota SSDF PO.2:** O conteúdo primário de PO.2 (definição formal de papéis e responsabilidades) reside em `00-fundamentos/roles-responsabilidades/`. Cap. 13 cobre os sub-requisitos de formação e validação (PO.2.1, PO.2.2). A rastreabilidade completa de PO.2 requer leitura conjunta de Cap. 00 + Cap. 13 + Cap. 14.

---

## Modelos de maturidade — pendente de normalização

> Scores de maturidade (SAMM, DSOMM, BSIMM) estão pendentes de pilot formal.  
> Ver [achievable-maturity.md](../achievable-maturity.md) para o mapeamento de maturidade em curso.

| Modelo | Domínios relevantes |
|--------|---------------------|
| OWASP SAMM v2.1 | Governance → Education & Guidance |
| OWASP DSOMM | Education & Training |
| BSIMM13 | Training & Culture (T1–T3) |

---

## Ligações com outros capítulos

- **Cap. 00** — papéis definidos aqui recebem a formação prescrita em Cap. 13
- **Cap. 01** — formação obrigatória com base na classificação de risco da aplicação
- **Cap. 14** — controlo de formação aplicado a terceiros e fornecedores
- **Cap. 02–12** — cada capítulo tem trilha de formação correspondente
