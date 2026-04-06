---
id: rastreabilidade
title: Rastreabilidade — Capítulo 01: Classificação de Aplicações
description: Rastreabilidade das práticas de classificação de risco face a frameworks normativos com pilot formal
tags: [rastreabilidade, classificacao, risco, ssdf, nis2, dora]
sidebar_position: 25

---


> **Método:** Ver [Metodologia de Validação de Claims](../../00-fundamentos/canon/26-metodologia-validacao-claims.md) para a baseline empírica dos autores, validação por índices semânticos, ontology backtrace e comparação com fontes externas.

# Rastreabilidade — Capítulo 01: Classificação de Aplicações

Este capítulo define o **mecanismo de classificação de risco** que determina a aplicação proporcional de práticas de segurança (L1–L3) em todos os capítulos do manual.

---

## Camada AppSec Core

| Slice AppSec Core | Relevância |
|-------------------|-----------|
| ACO-TMR — Threat Modeling, Risk Disposition & Mitigation Traceability | Avaliação de risco como input da classificação de aplicações (primário) |
| ACO-SLG — Security Event Logging, Audit Trail & Centralized Logging | Classificação formal como base de governação do ciclo de vida |

---

## Frameworks normativos — cobertura verificada

> Inclui apenas frameworks com pilot formal publicado no ExternalSourcesInventory.

> **Metodologia:** Cobertura verificada contra `ontology_discovery_units.jsonl` (4139 units, manual completo). "Explícito" = unit normative_weight strong/medium com heading directo. "Semântico" = conteúdo confirmado em addon ou via mapeamento de requisito canónico. "Parcial" = sem unit dedicado no capítulo.

| Framework | Requisito / Prática | Cobertura | Fonte verificada | Nota |
|-----------|--------------------|-----------|-----------------|----|
| SSDF PO.1 | Define Security Requirements | ✅ Explícito | aplicacao_lifecycle (strong): US-02 — Aplicação da matriz de controlo | Classificação de risco como base de requisitos proporcionais |
| SSDF PO.3.2 | Maintain security toolchain configurations | ✅ Explícito | aplicacao_lifecycle (strong): US-09 — Classificação de Artefactos Técnicos (Pipeline, IaC, Imagens) | Proporcionalidade por nível de risco aplicada a toolchains |
| DORA | Classificação por risco operacional | ✅ Explícito | policy_reference (medium): Políticas Organizacionais — Gestão de Risco > Enquadramento Regulatório | Overlay regulatório publicado |
| NIS2 | Classificação e governação por risco | ✅ Explícito | policy_reference (medium): Políticas Organizacionais — Gestão de Risco > Enquadramento Regulatório | Overlay regulatório publicado |

**Legenda:** ✅ Explícito · ✅ Semântico · ⚠️ Parcial · 🔧 Reparação · 🔴 Gap

---

## Maturidade — referência separada

A leitura de maturidade deste capítulo é tratada em [achievable-maturity.md](../achievable-maturity.md).

Neste documento, os modelos de maturidade surgem apenas como contexto editorial complementar. A sua normalização formal é apresentada no documento dedicado do capítulo.

---

## Ligações com outros capítulos

- **Cap. 02–12** — a classificação L1/L2/L3 determina a exigência proporcional de todas as práticas
- **Cap. 03** — threat modeling obrigatório a partir de nível L2
- **Cap. 14** — exceções e aceitação de risco residual requerem classificação formal como pré-condição
