---
id: diagramas-governanca
title: Security Governance Diagrams
sidebar_position: 8
description: Visual diagrams of the governance, exception and formal validation flows
tags: [diagramas, excecoes, fluxo, validacao]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/addon/08-diagramas-governanca.md
  source_sha256: 9e778ccbb43e5eb31623d50adc9978a70257040b56c81dbcfa5023740c59f411
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 68521ec15e778d89368728b1b3ae21aeb20c45a507b5e8f9e5d667e4bc24dc9c
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [chapter_role, cycle_iteration, traceability, validation_evaluation]
  glossary_sha256: e6af5d51e7cf4f5f881b8f67ae82d5e5c37d5139af54ee1380e11acb011a958b
  translated_at: 2026-09-26T12:00:16Z
  reviewed_by: null
---


# Governance Support Diagrams

This annex includes diagrams representing the main decision, traceability and validation flows described in Chapter 14 - Governance and Contracting.

---

## 📌 1. Exception approval flow {#-1-fluxo-de-aprovação-de-exceção}

```mermaid
flowchart TD
  A[Requisito não aplicável] --> B[Justificação técnica documentada]
  B --> C[Proposta de compensação]
  C --> D[Avaliação AppSec]
  D --> E{Aprovação formal?}
  E -->|Sim| F[Exceção registada com owner e validade]
  E -->|Não| G[Controlo obrigatório aplica-se]
```

---

## 📅 2. External supplier onboarding {#-2-onboarding-de-fornecedor-externo}

```mermaid
flowchart TD
  A[Pedido de integração de fornecedor] --> B[Classificação de risco do sistema]
  B --> C[Checklist e questionário de segurança]
  C --> D[Análise AppSec + Procurement]
  D --> E{Requisitos cumpridos?}
  E -->|Sim| F[Aprovação de onboarding]
  E -->|Não| G[Negociação / Compensação / Rejeição]
```

---

## 🔗 3. Organisational traceability {#-3-rastreabilidade-organizacional}

```mermaid
flowchart LR
  R[Risco: L1/L2/L3] --> Q[Requisitos do Catálogo SbD-ToE]
  Q --> C[Contrato com cláusulas]
  C --> V[Validação: testes, auditoria, evidência]
  V --> E[Registo de exceções se aplicável]
  E --> O[Owner e prazo de revisão]
```

---

## 🔄 4. Continuous review and validation cycle {#-4-ciclo-de-revisão-e-validação-continuada}

```mermaid
flowchart TD
  A[Release / Evento crítico] --> B[Reavaliação do risco]
  B --> C[Revisão dos requisitos aplicados]
  C --> D[Validação de conformidade + evidência]
  D --> E{Alterou-se o risco ou requisitos?}
  E -->|Sim| F[Atualização do registo / exceção]
  E -->|Não| G[Confirmação e encerramento do ciclo]
```
