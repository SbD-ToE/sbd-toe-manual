---
id: casos-praticos
title: Practical Cases of Applying Secure Architecture
sidebar_label: Practical Cases
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/addon/02-casos-praticos.md
  source_sha256: 2285f2e5a1285175ff5f76baf4b360fba5b7a199efbfd324357e50dbf7947f86
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 88a0ec0bf006be907d81ae1ab28aa990a14371ea8be9c64df9c1d4d53ceaaa6a
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, requirement_runtime, risk_level, validation_evaluation]
  glossary_sha256: d22f8d4860a0b2eb7091b4092427833b0989d4a375930fd9bb79c019ebf585b9
  translated_at: 2026-09-26T08:32:03Z
  stamped_at: 2026-09-26T18:33:32Z
  reviewed_by: null
---

# Practical Cases of Applying Secure Architecture

These examples demonstrate how to apply the secure architecture requirements in real contexts, according to the application's risk level (see Chapter 1).

---

## 🏥 Case 1 - Healthcare Application with Public Exposure (High Risk - L3) {#-caso-1---aplicação-de-saúde-com-exposição-pública-risco-elevado---l3}

- Web app in a public cloud with APIs for clinics and patients
- Clinical and personal data processed
- Integration with external services

**Requirements applied:**

| Requirement | Practical application |
|-----------|--------------------|
| ARC-001   | Trust zones defined (public frontend, backend, database) |
| ARC-005   | STRIDE threat modelling applied to the flows between components (critical flows covered and mitigations recorded) |
| ARC-011   | Segmentation between dev/stage/prod environments with isolated permissions and identity |
| ARC-012   | Formal approval checklist completed by AppSec before the deploy to production |
| ARC-013   | Automatic validation of the topology via `Cartography` in CI/CD |

---

## 🧾 Case 2 - B2B Invoicing System (Medium Risk - L2) {#-caso-2---sistema-de-faturação-b2b-risco-médio---l2}

- Internal web app with authenticated users
- Financial and customer data

**Requirements applied:**

| Requirement | Practical application |
|-----------|--------------------|
| ARC-002   | Inventory of externally exposed APIs with the associated controls documented |
| ARC-003   | Architecture review with a formal record and an AppSec checklist |
| ARC-006   | Critical services with active isolation in dedicated subnets |
| ARC-010   | Architecture diagram versioned in the repository (`.drawio`) |

---

## 📝 Case 3 - Internal Task Management Platform (Low Risk - L1) {#-caso-3---plataforma-de-gestão-de-tarefas-internas-risco-baixo---l1}

- Web application accessible only on the internal network
- No sensitive data or external APIs

**Requirements applied:**

| Requirement | Practical application |
|-----------|--------------------|
| ARC-001   | Simple diagram with a single trust zone |
| ARC-008   | Basic validation of the internal data flows |
| ARC-010   | Diagram included in the project wiki |

---

> 🔗 These examples show how to apply the requirements according to the risk, promoting proportionality and effectiveness without overload.
