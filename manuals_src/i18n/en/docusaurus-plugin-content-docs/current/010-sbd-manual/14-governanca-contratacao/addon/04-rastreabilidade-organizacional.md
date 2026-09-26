---
id: rastreabilidade-organizacional
title: Organisational Security Traceability
sidebar_position: 4
description: Model for the recording and formal justification of security decisions and deliverables
tags: [rastreabilidade, evidencias, compliance, auditoria]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/addon/04-rastreabilidade-organizacional.md
  source_sha256: ce1c6d3e992e255367bce410e8d3977e15f6ba5c9e9d2f8ce60f67a8de3450a2
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 34d6b3d99675464915e4891577182c50166a7c89cf785cb039d1de3781b9d2b4
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [audit_trail, avaliacao, chapter_role, framework_source_corpus, maturity, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: c181321ea0ec3ba2bc5decb138318f5e62a6b1bec425367d0c8504dd0254004b
  translated_at: 2026-09-26T12:00:14Z
  reviewed_by: null
---



# Organisational Traceability Model

## 🌟 Objective {#-objetivo}

To guarantee that there is a **clear, documented and auditable link** between:

* The **risk classification** assigned to each application or system;
* The **security requirements applied** (Ch. 2);
* The **contractual clauses and demands on third parties** (`addon/02-clausulas-contratuais.md`);
* The **validation mechanisms** (tests, reviews, evidence);
* The **documentation of exceptions or compensations** (`addon/12-processo-excecoes.md`);
* And the **named owners** of each decision.

This traceability model assumes that all evidence, regardless of whether it is produced manually or by automated technical processes, is always associated with an explicit organisational owner.

The existence of technical evidence does not replace the need for a conscious decision and formal accountability.

---

## 📈 Recommended traceability structure {#-estrutura-de-rastreabilidade-recomendada}

| Application / Project | Risk (L1-L3) | Requirements applied | Approved exceptions  | Supplier / Service | Existing evidence | Security owner  |
| -------------------- | ------------- | -------------------- | ------------------- | -------------------- | ------------------- | ------------------- |
| E.g. HR Portal        | L3            | REQ-001, REQ-002...  | EX-REQ-017 justified | Supplier ABC       | CI test + clause | joao.silva\@empresa |

*Illustrative identifiers (`EX-…`); they do not correspond to the Requirements Catalogue of Ch. 02.*

> 🔹 This structure may be maintained in Excel, SharePoint, Jira or another ALM tool with support for traceability.

Where applicable, the evidence column must make it possible to identify whether the validation was supported by automated mechanisms, as well as the person responsible for accepting that evidence.

---

## 🔄 Update mechanisms {#-mecanismos-de-atualização}

* The table must be updated:

  * At each relevant release;
  * Whenever there are changes of risk, supplier or requirements;
  * On the approval of exceptions or the onboarding of new third parties.

* Responsibility for updating must be assigned to the **project's security owner**.

---

## 🔢 Integration with GRC, audits and compliance {#-integração-com-grc-auditorias-e-conformidade}

* This model may be used as a **source of truth** for:

  * Compliance assessment against ISO 27001, NIS2, PCI-DSS;
  * Internal GRC reviews;
  * Analysis of exceptions and compensations by the AppSec team.

* It may be consolidated with **quarterly or half-yearly dashboards**, such as:

  * % of applications with complete traceability;
  * % of applications with approved exceptions;
  * % of applications with validated evidence.

---

## 📊 Suggested visualisation {#-sugestão-de-visualização}

```mermaid
flowchart LR
  R[Risco Classificado: L1/L2/L3] --> Q[Requisitos Selecionados]
  Q --> C[Contrato com Cláusulas Alinhadas]
  C --> V[Validação: testes, revisões, SBOM]
  V --> E[Evidência Documentada]
  E --> D[Decisões de exceção se aplicável]
  D --> O[Owner nomeado / revalidação futura]
```

---

## ✅ Final recommendations {#-recomendações-finais}

* This table must be used as the **basis for technical governance** and executive decision;
* It must integrate the data coming from the **per-chapter checklists SbD-ToE**;
* It may be used to **build maturity and visibility KPIs** (see `addon/kpis-governanca.md`).

---

## 🔗 Cross-links {#-ligações-cruzadas}

* Ch. 1 - Risk classification
* Ch. 2 - Requirements and application matrix
* `addon/01-modelo-governancao.md` - Governance and exceptions
* `addon/02-clausulas-contratuais.md` - Contractual clauses
* `addon/03-modelo-validacao-fornecedores.md` - Supplier validation
* `addon/kpis-governanca.md` - Governance KPIs

---
