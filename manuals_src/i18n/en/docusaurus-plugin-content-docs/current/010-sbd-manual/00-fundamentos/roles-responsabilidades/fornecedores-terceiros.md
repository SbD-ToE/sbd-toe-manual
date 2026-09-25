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
  source_sha256: 98f43e2c2dc3aed57c27dce2abe64641cda34ac35144d75eef3c71ea53dcef16
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 9444c34abce82c31cc1704aa0be939d1a93fed6f21fa3ed5a37b12510cdce1f2
  engine: claude-fable-5-1
  prompt_sha256: 13029ebd6497cb63207d12577bb94bbd3b20a5d9c8d3ebd2e4a450d20a45a251
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [avaliacao, chapter_role, practitioner_manual, sbdtoe_sbd, traceability, trilho_formativo, validation_evaluation]
  glossary_sha256: 6ada444a55b2b5e511c0e24c81d5881ea88dcef597cf613e60a518281766f35d
  translated_at: 2026-09-25T20:19:58Z
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
- [US-13: Training track for contractors](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-13---operacionalização-de-formação-de-terceiros) - SLA before technical access (CISO / Security Champion (training) responsible for executing it)

### Ch. 14 - Governance and Contracting {#cap-14---governança-e-contratação}
The organisation sets the **contractual security clauses**, validates the supplier before onboarding, monitors compliance throughout the contract and carries out formal offboarding at the end.

**Associated requirements:**
- [US-03: Continuous validation of suppliers](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-03---validação-contínua-de-fornecedores) - GRC validates compliance
- [US-15: Technical preparation of contractors](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-15---preparação-técnica-e-validação-de-contractors-pré-acesso) - Security Champion (HR) carries out the preparation
- [US-17: Secure offboarding](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-17---offboarding-seguro-de-contractors-e-rescisão-de-fornecedores) - Security Champion (HR) / DevOps / SRE carry out the offboarding
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
