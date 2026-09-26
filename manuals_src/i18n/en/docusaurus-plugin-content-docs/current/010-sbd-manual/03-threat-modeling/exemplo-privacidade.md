---
id: exemplo-privacidade-lindunn
title: Threat Modelling Example with LINDDUN
description: Application of the LINDDUN model to identify privacy threats in an authentication system
sidebar_position: 8
tags: [exemplo, linddun, threat-modeling, privacidade, capitulo2]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/exemplo-privacidade.md
  source_sha256: 42fba21e891881ec6635064dfead9ea7d5101d091507766e060731e40985c010
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 97fc3895d89f9431f6e9eef65c0fa2329e263fa7850b467a2fc5c94942fa5ffb
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, gdpr_pseudonymisation, requirement_runtime, role_tech_lead, threat, validation_evaluation]
  glossary_sha256: 9525a76c4baa0f9f3278672cd0b83d968a13c363492c0c3ed2275106f149c100
  translated_at: 2026-09-25T20:17:05Z
  stamped_at: 2026-09-26T18:33:26Z
  reviewed_by: null
---

# Practical Example - Threat Modelling with LINDDUN

This example demonstrates how to apply the **LINDDUN** model to identify privacy threats in an application that processes personal data and user authentication.

The LINDDUN model makes it possible to identify specific threats associated with:

* *Linkability*, *Identifiability*, *Non-repudiation*, *Detectability*, *Disclosure*, *Unawareness*, *Non-compliance*

---

## 🎯 Application context {#-contexto-da-aplicação}

Authentication service `auth-service` with the following characteristics:

* Login via form (`POST /login` with `email` and `password`)
* JWT generation with claims: `sub`, `email`, `role`, `iat`, `exp`
* Endpoint `/me` returns the authenticated user's data
* Endpoint `/admin/audits` returns the user's logs and actions
* No explicit consent or information about data retention

---

## 📈 Data model and flows (simplified DFD) {#-modelo-de-dados-e-fluxos-dfd-simplificado}

```mermaid
flowchart LR
    U[Utilizador] --> L[POST /login]
    L --> AS[Auth Service]
    AS --> DB[(DB Utilizadores)]
    AS --> JG[JWT Generator]
    JG --> JWT[JWT Token]
    JWT --> ME[GET /me]
    JWT --> AD[GET /admin/audits]
```

---

## 🔍 Threats identified (LINDDUN model) {#-ameaças-identificadas-modelo-linddun}

| Category       | Threat identified                                         | Impact | Associated requirement (Ch. 2)                             |
| --------------- | ----------------------------------------------------------- | ------- | -------------------------------------------------------- |
| Linkability     | JWT allows users to be tracked across sessions and apps      | High    | EX-DAT-008: JWT must not contain traceable IDs         |
| Identifiability | Endpoint `/me` exposes `email` and `role` directly           | Medium   | EX-DAT-002: Minimise exposure of identifiable data |
| Unawareness     | User not informed about the use of their data                | High    | EX-PRI-001: Mandatory privacy policy         |
| Non-compliance  | No record of consent or legal basis                  | High    | EX-PRI-004: Explicit and auditable consent         |
| Disclosure      | Logs accessible via `/admin/audits` contain full email addresses | High    | EX-LOG-004: Pseudonymisation of data in logs            |

*Illustrative identifiers (`EX-…`); they do not correspond to the Requirements Catalogue of Ch. 02.*

---

## ✅ Control recommendations {#-recomendações-de-controlo}

* Anonymise or pseudonymise sensitive claims in the JWTs (use `sub` without `email`)
* Apply RBAC to the `/admin/audits` endpoint and filter the data returned
* Show a notice and a link to the privacy policy before login
* Implement a consent record with date, IP and purpose

---

## 🧭 Validation of Ch. 2 requirements {#-validação-de-requisitos-do-cap-2}

This model demonstrates the need to apply security and privacy requirements (Ch. 2) in three domains:

- **Privacy and Personal Data** (minimisation, pseudonymisation, purpose)
- **Information and Transparency** (duty to inform, consent where applicable)
- **Logging and Auditing** (data minimisation in logs, access control and retention)

Integration rules (prescriptive):
- The requirements **must be recorded in the backlog** as traceable items (e.g. `THREAT-*` / `REQ-*` according to the taxonomy in use in the project).
- The prioritisation and acceptance of trade-offs is a **human decision** (PO + Tech Lead + AppSec, as the case may be).
- The evidence of implementation must be verifiable (commits, tests, versioned configurations, review records).
- The model and the decisions must remain **versioned** and referenceable per release.

---

> The use of LINDDUN makes it possible to anticipate legal and operational risks associated with personal data and to reinforce the coverage of Chapter 2 in a threat-oriented way.

---
