---
id: intro
title: Organisational Roles and Responsibilities
sidebar_label: Roles and Responsibilities
description: The 17 roles involved in implementing SbD-ToE, with responsibilities mapped to the technical chapters and regulations (NIS2, DORA, GDPR)
tags: [roles, responsabilidades, governance, organizacao, nis2, dora]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/intro.md
  source_sha256: 8b0b69b9354cb598a434e53b99a195aa1dc333967ab09a8f27dca6dc05653d3d
  source_commit: 112711064196b71c545672fe3fb3ae412b36575e
  target_sha256: b08893a85bc5fe52148bd79cc5549dab8d646678c51663c4680a7dfc782c4315
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 69aedbbdd11831f1cdc997bd1abfda3e2e4d3b411b1b43faf096628c510f395b
  glossary_keys: [chapter_role, framework_source_corpus, papel_suporte, practitioner_manual, role_juridico, role_procurement, role_rh_peopleops, role_secops, role_tech_lead, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: e99f765f41fc8635878c41542c13570a2e36df27a4b7d146a33052ddefcad471
  translated_at: 2026-09-26T17:23:40Z
  reviewed_by: null
---

# Organisational Roles and Responsibilities

## Structure and scope {#estrutura-e-âmbito}

SbD-ToE defines 17 organisational roles with specific responsibilities linked to the technical chapters and to regulatory obligations (NIS2, DORA, GDPR). Each role is documented with User Stories mapped to the chapters where it is involved.

A role is a set of responsibilities, not a person. One person may hold several roles; the only restrictions on who holds them are the incompatibilities (for example, whoever writes a change does not approve it, and whoever requests an exception does not approve it). The formal list — roles, aliases, specialisations, composites and incompatibilities — is kept as data in this folder (`_roles.yaml`) and is the source the knowledge graph reads.

## Assignment Principles {#princípios-de-atribuição}

### Existing Activities, Formalised {#atividades-existentes-formalizadas}

The activities prescribed in the SbD-ToE formalise processes that already exist:

- Vulnerability remediation → Developer role
- Validation of security criteria → QA role
- Prioritisation of security requirements → Product Owner role
- Pipelines with security controls → DevOps role

The Manual typifies these activities for traceability and regulatory compliance.

### Structural Flexibility {#flexibilidade-estrutural}

Role assignment varies by organisation. Several roles may be concentrated in one person, or distributed across specialised teams. The SbD-ToE requires the activities to be carried out; it does not prescribe an organisational structure.

---

## The 17 Roles {#os-13-roles}
## 📋 Roles Covered {#-roles-cobertos}

Each role has its own detailed document with:
- Description of the role and general responsibilities
- Specific activities per chapter of the Manual
- Regulatory framework (NIS2, DORA, GDPR, AI Act)
- References to the lifecycles where those activities are detailed

**Technical roles:**
- [Developer](developer)
- [Quality Assurance (QA)](qa)
- [DevOps / SRE](devops-sre)
- [AppSec Engineer](appsec-engineer)
- [Software Architects](arquitetos-software)
- [SecOps (Security Operations)](operacoes)

**Product and management roles:**
- [Product Owner](product-owner)
- [Scrum Master / Team Lead](scrum-master)
- [Tech Lead](tech-lead)
- [Executive Management](gestao-executiva)

**Security and governance roles:**
- [Security Champion](security-champion)
- [GRC / Compliance](grc-compliance)

**Other domains of the organisation** (the Manual says what must exist, not how they work):
- [HR / People Operations](rh-peopleops)
- [Procurement](procurement)
- [Legal](juridico)

**Third parties:**
- [Suppliers / Third Parties](fornecedores-terceiros)
- [Auditors](auditores)

## Each Role Includes {#cada-papel-inclui}

- Primary responsibility and scope of action
- Regulatory framework (NIS2, DORA, GDPR, ISO, NIST)
- User Stories per chapter
- Links to the technical chapters
- Coverage metrics

---

## Note: composite functions (operational, not canonical) {#nota-funções-compostas-operacionais-não-canónicas}

In organisations with **significant adoption of AI agents** with tool-use in the SDLC (autonomy levels A2+, see [Ch. 02](../../requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia)), the need naturally arises to operate the risk specific to those agents — *mandates*, *intent events*, *kill-switches*, agentic telemetry, *prompt injection* in production, provider *drift*.

No new canonical role is created for this. Instead, a **composite function** is recognised — informally called **"AI Reliability Engineer"** — which combines, in proportions that vary with the organisation, three of the roles already defined:

- **`AppSec Engineer`** — agentic *threat modelling*, validation of *mandates*, review of *intent events*, response to *off-policy actions*
- **`DevOps / SRE`** — provisioning of *workload identity* for agents, operational *kill-switch*, telemetry *sinks*, *kill-switch* drills
- **`GRC / Compliance`** — regulatory compliance of the *mandates* (AI Act, GDPR), A3/A4 approval, periodic audit of the register

The function operates under an **explicit mandate from the `CISO`** (or equivalent) that delimits what this function may decide without escalating, and it keeps the canonical roles unchanged — preserving the stability of the SbD-ToE ontology and its compatibility with what has already been written in the Manual and in the academic papers that cite these roles.

> 🧭 **In one sentence:** organisations mature in agents need this function; the Manual does not need to typify it as a new role. It is combined from the canonical roles.

---
