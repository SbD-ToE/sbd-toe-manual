---
id: intro
title: Organisational Roles and Responsibilities
sidebar_label: Roles and Responsibilities
description: The 13 roles involved in implementing the SbD-ToE, with responsibilities mapped to the technical chapters and to regulations (NIS2, DORA, GDPR)
tags: [roles, responsabilidades, governance, organizacao, nis2, dora]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/00-fundamentos/roles-responsabilidades/intro.md
  source_sha256: 5edfe767c6f2d5168913d6347848018d9a455ad9232515c74e112b3cf473dbb0
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 2b19aa994a5be165721cffbb5639e92b137d114dda583535615d982629169b47
  engine: claude-fable-5-1
  prompt_sha256: 13029ebd6497cb63207d12577bb94bbd3b20a5d9c8d3ebd2e4a450d20a45a251
  terms_sha256: 779fcd2406a1a730ed65de83e52df7743a50456cc35d31f9ce5b9d1c8073cd3d
  translated_at: 2026-09-25T16:51:53Z
  reviewed_by: null
---

# Organisational Roles and Responsibilities

## Structure and scope {#estrutura-e-âmbito}

The SbD-ToE defines 13 organisational roles with specific responsibilities linked to the technical chapters and to regulatory obligations (NIS2, DORA, GDPR). Each role is documented with User Stories mapped to the chapters where it intervenes.

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

## The 13 Roles {#os-13-roles}
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
- [Operations (Ops)](operacoes)

**Product and management roles:**
- [Product Owner](product-owner)
- [Scrum Master / Team Lead](scrum-master)
- [Executive Management](gestao-executiva)

**Security and governance roles:**
- [Security Champion](security-champion)
- [GRC / Compliance](grc-compliance)

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

No new canonical role is created for this. Instead, a **composite function** is recognised — informally called **"AI Reliability Engineer"** — which combines, in proportions that vary from one organisation to another, three of the 13 roles already defined:

- **`AppSec Engineer`** — agentic *threat modelling*, validation of *mandates*, review of *intent events*, response to *off-policy actions*
- **`DevOps / SRE`** — provisioning of *workload identity* for agents, operational *kill-switch*, telemetry *sinks*, *kill-switch* drills
- **`GRC / Compliance`** — regulatory compliance of the *mandates* (AI Act, GDPR), A3/A4 approval, periodic audit of the register

The function operates under an **explicit mandate from the `CISO`** (or equivalent) that delimits what it may decide without escalating, and keeps the 13 canonical roles unchanged — this preserves the stability of the SbD-ToE ontology and its compatibility with what has already been written in the Manual and in the academic papers that cite these roles.

> 🧭 **In one sentence:** organisations mature in their use of agents need this function; the Manual does not need to typify it as a new role. It is composed from the 13.

---
