---
id: diagramas-referencia
title: Reusable Secure Architecture Models
description: Prescriptive models linked to requirements (ARC), risk and mitigated threats
sidebar_position: 4
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/addon/04-diagramas-referencia.md
  source_sha256: b9d16cd67f6d40ed8c74f49534716ac7e632db0b1a2aa57ef2f6e811bf36654c
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 95c5903bd6175420d5776f5e1479ee72764ee18376fad193bee6c898696f67d2
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5536afdcc04f76a07c66e747133c73d68308884707c296abf945937a9630a312
  glossary_keys: [chapter_role, risk_level, traceability, validation_evaluation]
  glossary_sha256: 9e8d22c7194b682031fab6c0caa59a12fe9bdc91f0ef56df523e59973e5128d8
  translated_at: 2026-09-26T08:32:04Z
  reviewed_by: null
---

# Reusable Secure Architecture Models

This document presents reference models that can be used as a secure basis for new projects.  
Each model is associated with:

- A **typical risk level** (L1, L2 or L3)
- The **applicable ARC requirements**
- The **mitigated threats**
- The suggested `.drawio` or PlantUML files

---

## 🧱 Model 1 - Web Monolith with Internal Backend (Risk L1) {#-modelo-1---monólito-web-com-backend-interno-risco-l1}

### 📝 Description {#-descrição}

- Traditional application with an internal backend and a local database
- No public APIs
- Access controlled via a private network

### ✔️ Applicable requirements {#️-requisitos-aplicáveis}

- `ARC-001` (Trust zones identified and documented)
- `ARC-007` (Reusable and approved architecture patterns)
- `ARC-010` (Versioned and accessible architecture diagrams)

### 🔑 Mitigated threats {#-ameaças-mitigadas}

- STRIDE: Tampering, Information Disclosure

### 🖼️ Suggested diagram {#️-diagrama-sugerido}

```plaintext
[UI] --> [Web Server] --> [Database]
```

> ⚠️ In this model, control is ensured above all by **simplicity** and **restricted exposure**.

---

## ☁️ Model 2 - Microservices with External APIs (Risk L2) {#️-modelo-2---microserviços-com-apis-externas-risco-l2}

### 📝 Description {#-descrição-1}

- APIs exposed via an authenticated Gateway
- Microservices with logical segmentation
- mTLS on internal communication

### ✔️ Applicable requirements {#️-requisitos-aplicáveis-1}

- `ARC-001`, `ARC-002`, `ARC-003`, `ARC-004`, `ARC-005`, `ARC-006`
- `ARC-007`, `ARC-008`, `ARC-009`, `ARC-010`

### 🔑 Mitigated threats {#-ameaças-mitigadas-1}

- STRIDE: Elevation of Privilege, Spoofing, Repudiation

### 🖼️ Suggested diagram {#️-diagrama-sugerido-1}

```plaintext
[API Gateway] <--> [Service A] <--> [Service B] <--> [DB]
                      |
                 [Auth Service]
```

> ✅ Requires formal technical validation (ARC-005) and threat modelling review (ARC-010).

---

## 🧐 Model 3 - Regulated Critical Platform (Risk L3) {#-modelo-3---plataforma-crítica-regulada-risco-l3}

### 📝 Description {#-descrição-2}

- Application subject to regulation (e.g. healthcare, financial)
- Strict control of boundaries
- Physical and logical segmentation (Kubernetes namespaces, DMZs)

### ✔️ Applicable requirements {#️-requisitos-aplicáveis-2}

- All requirements ARC-001 to ARC-013

### 🔑 Mitigated threats {#-ameaças-mitigadas-2}

- STRIDE: All

### 🖼️ Suggested diagram {#️-diagrama-sugerido-2}

```plaintext
[Client] --> [Web Gateway] --> [Frontend Pod]
                            --> [Backend Pod] --> [Data Services]
```

> ✅ This model requires full application of the chapter, including segmentation between environments (ARC-011), formal approval (ARC-012), automatic topology validation (ARC-013) and end-to-end traceability (ARC-008).

---

## 📁 Reuse suggestions {#-sugestões-de-reutilização}

- Make the models available in `.drawio` or `.puml` in the internal repository
- Assign a technical owner per model
- Validate annually and associate with real projects as a reference

> These models do not replace the specific design of each application, but they constitute **mandatory minimum patterns to be validated** according to the risk level.

---
