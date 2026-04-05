---
id: rastreabilidade
title: Rastreabilidade — Capítulo 01: Classificação de Aplicações
description: Rastreabilidade das práticas de classificação de risco face a frameworks normativos com pilot formal
tags: [rastreabilidade, classificacao, risco, ssdf, nis2, dora]
sidebar_position: 25
---

# Rastreabilidade — Capítulo 01: Classificação de Aplicações

Este capítulo define o **mecanismo de classificação de risco** que determina a aplicação proporcional de práticas de segurança (L1–L3) em todos os capítulos do manual.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-SLG — Security Lifecycle & Governance | Classificação formal como base de governação do ciclo de vida |
| ACO-TMR — Threat Modeling & Risk | Avaliação de risco como input da classificação de aplicações |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

| Framework | Requisito / Prática | Cobertura | Nota |
|-----------|--------------------|-----------|----|
| SSDF PO.1 | Define Security Requirements | ✅ Explícito | Classificação de risco como base de requisitos proporcionais |
| SSDF PO.3.2 | Maintain security toolchain configurations | ✅ Explícito | Proporcionalidade por nível de risco aplicada a toolchains |
| DORA | Classificação por risco operacional | ✅ Explícito | Overlay regulatório publicado |
| NIS2 | Classificação e governação por risco | ✅ Explícito | Overlay regulatório publicado |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

---

## Modelos de maturidade — pendente de normalização

> Scores de maturidade (SAMM, DSOMM, BSIMM) estão pendentes de pilot formal.  
> Ver [achievable-maturity.md](../achievable-maturity.md) para o mapeamento de maturidade em curso.

| Modelo | Domínios relevantes |
|--------|---------------------|
| OWASP SAMM v2.1 | Governance → Risk Management |
| OWASP DSOMM | Governance, Requirements |
| BSIMM13 | Strategy & Metrics (SM1–SM3) |

---

## Ligações com outros capítulos

- **Cap. 02–12** — a classificação L1/L2/L3 determina a exigência proporcional de todas as práticas
- **Cap. 03** — threat modeling obrigatório a partir de nível L2
- **Cap. 14** — exceções e aceitação de risco residual requerem classificação formal como pré-condição
