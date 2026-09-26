---
id: procurement
title: Procurement
sidebar_label: 🛒 Procurement
description: What SbD-ToE requires to exist on the Procurement side
tags: [procurement, fornecedores, contratacao, responsabilidades]
sidebar_position: 11.5
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/procurement.md
  source_sha256: 15dcf220ef5f101d56415be4fc853377115372de7cc0192cdcb864db4c6797e7
  source_commit: 112711064196b71c545672fe3fb3ae412b36575e
  target_sha256: 67fdfa22987483e6328294ef3d7eec7dcd402bb1117d57ae80a03e35e0c50a9f
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 69aedbbdd11831f1cdc997bd1abfda3e2e4d3b411b1b43faf096628c510f395b
  glossary_keys: [chapter_role, practitioner_manual, risk_level, role_juridico, role_procurement, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: 40827c67481c741514f39eb6ed8876f9ccff12a7b6db8989b36ec7d8c20b124a
  translated_at: 2026-09-26T17:23:57Z
  reviewed_by: null
---

# Procurement

## Overview {#visão-geral}

Procurement is **another domain of the organisation**. The Manual does not say how Procurement negotiates; it says what must exist before a supplier comes in: security validation, clauses in the contract, periodic reassessment.

### Key Responsibilities {#responsabilidades-principais}
- Execute the formal supplier validation flow (questionnaire → AppSec analysis → approval)
- Ensure, with Legal, that contracts include the security clauses
- Coordinate the periodic reassessment of suppliers and the escalation of critical incidents
- Take part in contracting AI model providers, with GRC / Compliance

**Specialisation:** *Procurement Officer*, who executes the validation flow.

### Organisational Context {#contexto-organizacional}
Third-party risk management is an express obligation in **DORA** (ICT third-party risk) and **NIS2** (supply chain security). The decision and the record stay with GRC / Compliance; executing the purchasing flow belongs to Procurement.

## Regulatory Framework {#enquadramento-regulatório}

Supports:
- **DORA**: ICT third-party risk management
- **NIS2**: Supply chain security
- **CRA**: Due diligence on third-party components

---

## Activities by Chapter {#atividades-por-capítulo}

### Ch. 14 - Governance and Contracting {#cap-14---governança-e-contratação}
Execute **supplier validation** before onboarding, include SbD-ToE clauses in contracts and **reassess suppliers** at the cadence of the risk level.

**User Stories:**
- [US-02: Contractual security clauses](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-02---cláusulas-contratuais-de-segurança) - Supplier compliance (with Legal)
- [US-06: Execution of the formal supplier validation flow](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-06---execução-de-fluxo-formal-de-validação-de-fornecedores) - Minimum requirements before onboarding
- [US-14: Continuous supplier reassessment](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-14---reavaliação-contínua-e-rotação-de-fornecedores-pós-onboarding) - Periodic re-approval (with AppSec Engineer)
- [US-21: Contracting AI model providers](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-21) - Minimum clauses for AI providers (with GRC / Compliance and Legal)

---

## Chapter References {#referências-aos-capítulos}

For full context and framing:

- [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)
