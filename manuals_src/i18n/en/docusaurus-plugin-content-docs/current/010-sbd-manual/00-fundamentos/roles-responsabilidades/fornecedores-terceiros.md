---
id: fornecedores-terceiros
title: Suppliers / Third Parties
sidebar_label: 🤝 Suppliers / Third Parties
description: Responsibilities of Suppliers and Third Parties in the SbD-ToE
tags: [fornecedores, terceiros, supply-chain, responsabilidades]
sidebar_position: 13
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/fornecedores-terceiros.md
  source_sha256: df42e2de7fe621af6199fd4e0b8edd706362bdab8c758d5511f004e61389a6af
  source_commit: 112711064196b71c545672fe3fb3ae412b36575e
  target_sha256: f4a06c26b78f2d617e03a9f1fe6ca5d54a4990891d2a9797412f18d7e416c724
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 69aedbbdd11831f1cdc997bd1abfda3e2e4d3b411b1b43faf096628c510f395b
  glossary_keys: [avaliacao, chapter_role, practitioner_manual, role_rh_peopleops, sbdtoe_sbd, traceability, trilho_formativo, validation_evaluation]
  glossary_sha256: cf4559bc5afee0b7806d6405613705b33201af4d0728cef7c7236630b3ab682d
  translated_at: 2026-09-26T17:23:38Z
  reviewed_by: null
---

# Suppliers / Third Parties

## Overview {#visão-geral}

Suppliers and third parties are **part of the chain of responsibility and lie outside the Manual's domain of prescription**.  
The Manual tells the organisation what it must require, verify and record; it does not tell the supplier how to work — what is required of the supplier lives in the contract. A supplier that adopts the SbD-ToE will find its own practices here.

The boundary moves with the process, not with the contract: whoever is contracted to work inside the organisation's repositories, pipelines and environments operates inside its process, and the practices apply to them as to any team (Ch. 14, US-15 to US-20).

### Key Responsibilities {#responsabilidades-principais}
- Comply with contractual security clauses (Ch. 14)
- Deliver an up-to-date SBOM and evidence of compliance
- Ensure that external components meet security requirements
- Submit to periodic validation

### Organisational Context {#contexto-organizacional}
They are critical for **NIS2** and **DORA**, which mandate explicit management of the digital supply chain (Art. 21 NIS2, Art. 28-30 DORA) and continuous assessment of third parties.

## Regulatory Framework {#enquadramento-regulatório}

Supply chain management is an explicit requirement in:
- **NIS2**: Art. 21 - Supply chain cybersecurity risk management measures
- **DORA**: Art. 28-30 - Management of third-party ICT risk

---

## Activities by Chapter {#atividades-por-capítulo}

What the organisation requires, verifies and records, per chapter:

### Ch. 05 - Dependencies and SBOM {#cap-05---dependências-e-sbom}
The organisation requires an **up-to-date SBOM** for the components delivered and verifies it at acceptance, to maintain complete traceability of the chain.

### Ch. 08-09 - IaC and Containers {#cap-08-09---iac-e-containers}
The organisation requires **vulnerability validation and digital signature** on the IaC modules and images supplied, and verifies them before promotion.

### Ch. 13 - Training and Onboarding {#cap-13---formação-e-onboarding}
The organisation requires and records the **mandatory minimum training** before granting access to systems or data (NIS2/DORA compliance).

**Associated requirements:**
- [US-12: Minimum training for third parties](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-12---validação-de-conhecimento-via-quizzes-estruturados) - Receive mandatory training (GRC / Compliance / Executive Management responsible for ensuring it)
- [US-13: Training track for contractors](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-13---operacionalização-de-formação-de-terceiros) - SLA before technical access (CISO / Training Manager responsible for executing it)

### Ch. 14 - Governance and Contracting {#cap-14---governança-e-contratação}
The organisation sets the **contractual security clauses**, validates the supplier before onboarding, monitors compliance throughout the contract and carries out formal offboarding at the end.

**Associated requirements:**
- [US-03: Continuous validation of suppliers](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-03---validação-contínua-de-fornecedores) - GRC validates compliance
- [US-15: Technical preparation of contractors](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-15---preparação-técnica-e-validação-de-contractors-pré-acesso) - Security Champion + HR / People Operations carry out the preparation
- [US-17: Secure offboarding](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-17---offboarding-seguro-de-contractors-e-rescisão-de-fornecedores) - Security Champion + HR / People Operations + DevOps / SRE carry out the offboarding
- [US-14: Periodic reassessment of suppliers](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-14---reavaliação-contínua-e-rotação-de-fornecedores-pós-onboarding) - Submit to reassessment
- [US-18: Continuous monitoring of suppliers](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-18---monitorização-contínua-de-conformidade-de-fornecedores-alertas-e-escalação) - Allow monitoring (AppSec Engineer / Operations (Ops) carry it out)

---

## Chapter References {#referências-aos-capítulos}

For full context and framing:

- [Ch. 05 - Dependencies and SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)
- [Ch. 08 - IaC and Infrastructure](/sbd-toe/sbd-manual/iac-infraestrutura/intro)
- [Ch. 09 - Containers and Images](/sbd-toe/sbd-manual/containers-imagens/intro)
- [Ch. 13 - Training and Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
- [Ch. 14 - Governance and Contracting](/sbd-toe/sbd-manual/governanca-contratacao/intro)
