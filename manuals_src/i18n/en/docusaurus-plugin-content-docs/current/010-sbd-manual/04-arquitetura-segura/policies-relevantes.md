---
id: policies-relevantes
title: Policies
description: Organisational policies that support the adoption of secure architecture practices
tags: [politicas, arquitetura, governanca]
sidebar_position: 60
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/policies-relevantes.md
  source_sha256: 87e8570bf3d762b429c190bad0561806deac0dea2c4a8e556fddcee96cce4b9e
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: d6483bb7ecbcc59bf7d395442cb5924a9cf94ae40dbb02bda52b5b69d0ff20f5
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5536afdcc04f76a07c66e747133c73d68308884707c296abf945937a9630a312
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, lifecycle_phase, mapping, requirement_runtime, traceability, transversal, validation_evaluation]
  glossary_sha256: b9d1f76bcfd513a8e7b700cd1ec93d6310ac95f7193056eae80605d5a1057e45
  translated_at: 2026-09-26T08:32:12Z
  reviewed_by: null
---

# Organisational Policies - Secure Architecture

The effective adoption of Chapter 04 - Secure Architecture - requires the existence of **formal organisational policies** that sustain, legitimise and make auditable the application of the practices described here.

---

## 📌 Fundamental note {#-nota-fundamental}

> ⚠️ The technical practices of defining trust zones, validating the architecture, justified exceptions and traceability **must be supported by approved and published organisational policies**.

These policies:

- Formalise responsibilities and technical acceptance criteria;
- Make the governance of the architecture visible throughout the lifecycle;
- Allow objective auditing of architectural decisions and exceptions;
- Support traceability between requirements, architecture and technical evidence.

> 🧩 This chapter operationalises formal decisions about architecture - the policy defines, the chapter executes.

---

## 🧾 Recommended policies {#-políticas-recomendadas}

| Policy Name                                 | Mandatory | Application                                 | Minimum expected content                                                                 |
|--------------------------------------------------|--------------|--------------------------------------------|--------------------------------------------------------------------------------------------|
| [Secure Architecture Policy](/sbd-toe/assets/policies/policy-arquitetura-segura)                   | ✅ Yes       | All teams with technical responsibility | Mandatory patterns, definition of trust zones, segmentation, minimum requirements     |
| [Technical Design Approval Policy](/sbd-toe/assets/policies/policy-arquitetura-segura)          | ✅ Yes       | Projects with an impact on the architecture            | Formal review process, roles and responsibilities, technical acceptance criteria    |
| [Architectural Documentation and Versioning Policy](/sbd-toe/assets/policies/policy-arquitetura-segura) | ✅ Yes   | Systems with L2 or L3 criticality            | Diagram rules, controlled versioning, updates on structural changes               |
| [Architectural Traceability Policy](/sbd-toe/assets/policies/policy-rastreabilidade)        | ✅ Yes       | Projects subject to control or audit    | Mapping of requirements (ARC-00x) → component → technical control                         |
| [Policy on Technical Exceptions in Architecture](/sbd-toe/assets/policies/policy-gestao-excecoes)     | ✅ Yes       | Whenever a requirement is not applicable    | Formal form, review cycle, compensating plan, validity and technical owner         |

---

## 📋 Suggested structure of each policy {#-estrutura-sugerida-de-cada-política}

Each organisational policy must contain:

- **Objective and scope** (e.g. applies to all L2+ projects);
- **Mandatory technical criteria** (e.g. ZTCs, checklists, exception model);
- **Roles and responsibilities** (architecture, security, development, operations);
- **Requirement for evidence and traceability** (e.g. diagram, validation records);
- **Process for reviewing and updating the policy itself** (e.g. annual);
- **Integration with release processes and technical audit**.

---

## ✅ Final recommendations {#-recomendações-finais}

- These policies must be **formal, accessible and approved by the architecture and security areas**;
- Their application must be **integrated into the lifecycle** via templates, gates and CI/CD practices;
- The existence of these policies **makes secure architecture viable as an auditable and cross-cutting practice**, ensuring traceability and consistency.

> 📌 Their absence compromises the coherence of technical decisions, the validation of exceptions and the auditability of the architecture - in internal projects as much as in regulated contexts.
