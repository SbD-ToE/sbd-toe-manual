---
id: exemplos-aplicacao-stride
title: Threat Modelling Examples with DFD and STRIDE
description: Complete example with DFD, STRIDE and mitigation in an authentication service with JWT
tags: [exemplos, threat-modeling, stride, dfd, mitigação]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/exemplos-aplicacao-stride.md
  source_sha256: 95ca7f3f42c23a40fb6432954def730383c204cb7585d86a8fef38beff283ba6
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 94da943cf85a9b121c4e7b35382c413b61e9888950a20eaa45daecbadec63b39
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [framework_source_corpus, lifecycle_phase, threat, validation_evaluation]
  glossary_sha256: 5703039decea24c8b9fe2c496045b1d37f2289a50c0bfa268d3e96d47dee6c95
  translated_at: 2026-09-25T20:17:06Z
  stamped_at: 2026-09-26T18:33:27Z
  reviewed_by: null
---

# Practical example - Threat Modelling of an authentication service with JWT

## 🎯 Technical context {#-contexto-técnico}

During the design phase of a new authentication service (`auth-service`), the team identified the following components and flows:

- Publicly accessible REST API at `https://auth.exemplo.com`
- Login flow:
  1. The user submits `email + password` via `POST /login`
  2. The service validates the credentials locally in a database
  3. If valid, the service **generates a JWT token**
  4. The JWT is returned to the client and used in future requests (`Authorization: Bearer`)
- Initial configuration:
  - JWT with `alg: none` (no signature)
  - Claims: `sub`, `email`, `role`, `exp` (24h)
  - No MFA
  - Endpoint `/admin/config` accessible with any JWT
  - No structured logging and no profile control

---

## 🔁 Modelling with a DFD (representation of the system) {#-modelação-com-dfd-representação-do-sistema}

### 🔷 Threat Model - auth-service (DFD in Mermaid) {#-threat-model---auth-service-dfd-em-mermaid}

```mermaid
flowchart TD
  subgraph Cliente
    A[Browser / Mobile App]
  end

  subgraph AuthService
    B[auth.exemplo.com \nAPI REST]
    C[JWT Generator]
    D[User Database]
    E[Admin Config Endpoint]
    F[Logging - SIEM / Local]
  end

  subgraph Backend
    G[Backend APIs]
  end

  %% Fluxos de dados
  A -->|"1. POST /login\n(email/pwd)"| B
  B -->|"2. Verifica utilizador"| D
  B -->|"3. Gera JWT"| C
  C -->|"4. Retorna JWT"| A

  A -->|"5. Chamada autenticada com JWT"| G
  A -->|"6. Acesso a /admin/config com JWT"| E
  B -->|"7. Logging (opcional)"| F

  style A fill:#e3f2fd,stroke:#2196f3,stroke-width:2px
  style B fill:#fff3e0,stroke:#ff9800,stroke-width:2px
  style C fill:#ede7f6,stroke:#673ab7,stroke-width:2px
  style D fill:#f1f8e9,stroke:#8bc34a,stroke-width:2px
  style E fill:#fce4ec,stroke:#e91e63,stroke-width:2px
  style F fill:#f3e5f5,stroke:#9c27b0,stroke-width:2px
  style G fill:#e8f5e9,stroke:#4caf50,stroke-width:2px
```

---

### 🧱 Elements identified {#-elementos-identificados}

| Element                | Type             | Description                                                         |
|-------------------------|------------------|-------------------------------------------------------------------|
| `Browser / Mobile App`  | External Actor   | Client that initiates the login                                          |
| `auth.exemplo.com`      | Process          | Public API that exposes the `/login` endpoint                         |
| `JWT Generator`         | Process          | Logic that generates the JWT tokens                                     |
| `User Database`         | Data Store       | User database                                     |
| `SIEM / Logs`           | Data Store       | Structured event storage                              |
| `Admin Config Endpoint` | Process          | Sensitive endpoint: `/admin/config`                                |
| `Backend APIs`          | Process          | Protected APIs that consume and validate the JWT                      |

---

### 🔁 Data flows {#-fluxos-de-dados}

| Source                   | Destination              | Data Transmitted                                  |
|------------------------|----------------------|-----------------------------------------------------|
| Browser → auth API     | `email/password` via `POST /login` (HTTPS)               |
| auth API → DB          | User lookup                                  |
| auth API → JWT Gen     | JWT token request                                      |
| JWT Gen → Browser      | JWT (`Authorization: Bearer &lt;token&gt;`)                   |
| Browser → Backend APIs | Authenticated request with JWT                              |
| Browser → Admin Config | Access with JWT to `/admin/config`                        |
| auth API → SIEM        | (Absent) - no structured logs                       |

---

### 🔍 STRIDE threats per element {#-ameaças-stride-por-elemento}

| Element               | STRIDE Category         | Threat Identified                                                                | Severity | Recommended Mitigation                                                               |
|------------------------|--------------------------|------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------|
| `auth.exemplo.com`     | **Spoofing**             | Login with reused credentials or without MFA                                     | High      | MFA, rate limiting, context analysis (device/IP)                                |
| `JWT Generator`        | **Tampering**            | Tamperable JWTs (`alg: none`)                                                    | High      | RS256 signature, header validation, reduced TTL                                |
| `Admin Config`         | **Elevation of Privilege** | Any user can access administrative endpoints                        | High      | Claims-based RBAC, validation of `role` in the backend                             |
| `auth.exemplo.com`     | **Repudiation**          | No record of logins or sensitive changes                                       | Medium     | Structured logging with `userId`, IP, action, result                             |
| `JWT Generator`        | **Information Disclosure** | Excessive claims (`email`, `role`, `createdAt`) exposed to the client               | Medium     | Minimise claims in the JWT, context-based scoping                               |
| `auth.exemplo.com`     | **Denial of Service**    | Brute force on `/login` or mass reuse of JWTs                                  | Medium     | Rate limiting, CAPTCHA, progressive delays                                        |

---

### 🛡️ Threat ↔ control map {#️-mapa-ameaça--controlo}

| Threat                      | Recommended Control                                                                 |
|----------------------------|----------------------------------------------------------------------------------------|
| Spoofing                   | Mandatory MFA; context-aware login; device binding                                 |
| Tampering                  | Signed JWT (RS256); validation of `alg`, `aud`, `iss`; TTL ≤ 15 min                 |
| Elevation of Privilege     | RBAC with explicit control of claims (e.g. `role: admin`)                            |
| Repudiation                | Centralised logging; action tracking; integration with SIEM                    |
| Information Disclosure     | Minimal JWT; segregation of claims per endpoint; scoping                          |
| Denial of Service          | Rate limiting on the `/login` endpoint; protection at the API Gateway; quotas                 |

---

### ✅ Conclusion {#-conclusão}

This example illustrates a typical case of modern architecture with:

- JWT-based authentication
- Public API accessible via the Internet
- Lack of basic validations and controls

> Even in apparently simple architectures, the **misuse of standards** (e.g. unsigned JWT) can introduce **critical flaws**.  
> The use of a structured approach (e.g. STRIDE) and an explicit representation of the flows (DFD) makes it possible to identify and mitigate threats before going into production.

This threat model must be documented, versioned and reused in other services with an identical architecture, as described in the section “♻️ Reuse of Threat Models”.
