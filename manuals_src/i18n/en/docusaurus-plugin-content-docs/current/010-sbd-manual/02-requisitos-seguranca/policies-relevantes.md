---
id: policies-relevantes
title: Relevant policies
description: Policies that underpin the definition, exception and validation of requirements
tags: [políticas, requisitos, exceções, validação, rastreabilidade]
sidebar_position: 60
translation:
  source_locale: pt
  source_path: 010-sbd-manual/02-requisitos-seguranca/policies-relevantes.md
  source_sha256: 2a2ca657aba9111a9cfe10aee5b6a17b2478a50a51ff2bdfeff4c9155eca9657
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 96183937b3b9ae93ecf3022f513216af36750a2af7a7e0c95f2c6aefb92e2a54
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [avaliacao, chapter_role, mapping, maturity, practitioner_manual, requirement_runtime, traceability, transversal, validation_evaluation]
  glossary_sha256: caa23711b2c685c3c20ba049a01bdd2279a3a3223ddb7958efeacc9c9611be19
  translated_at: 2026-09-25T20:20:19Z
  reviewed_by: null
---


# Organisational Policies - Security Requirements

The effective adoption of Chapter 02 - Security Requirements - requires the existence of **formal organisational policies** that **frame, legitimise and sustain the application of the practices described in this chapter**.

---

## 📌 Fundamental note {#-nota-fundamental}

> ⚠️ The operational practices prescribed in this chapter (catalogue, risk-based selection, traceability, acceptance criteria) **must be formally legitimised by approved organisational policies**.

These policies:

- Make the application of security requirements from the start of development **binding**;
- Allow the controls applied to be **proportional to the identified risk**;
- Serve as the normative basis for **internal audits, technical reviews and contracting with third parties**.

> 🧩 This chapter **implements, in practice, what the policies define**. The policy approves, the chapter operationalises.

> 📎 The requirement for formal policies on security requirements is explicitly referred to in frameworks such as **NIST SSDF**, **ISO/IEC 27001**, **OWASP SAMM**, **ENISA SDLC** and **CIS Controls v8** - these policies are not just good practice, they are a normative expectation.

---

## 🧾 Recommended policies {#-políticas-recomendadas}

| Policy Name                                        | Mandatory? | Application                                | Summary of required content |
|---------------------------------------------------------|--------------|-------------------------------------------|-------------------------------|
| [Application Security Requirements Policy](/sbd-toe/assets/policies/policy-requisitos-seguranca)       | ✅ Yes       | All projects and product teams    | Mandatory catalogue, risk-based selection, traceability, acceptance criteria |
| [Policy on the Integration of Requirements into the Backlog](/sbd-toe/assets/policies/policy-requisitos-seguranca)         | ⚠️ Optional  | Development team, PO, QA         | Requirements must appear in the planning artefacts (stories/tasks) with tags |
| [Policy on the Validation of Requirements in Pipelines](/sbd-toe/assets/policies/policy-requisitos-seguranca)        | ⚠️ Optional  | DevOps, QA, security                     | Minimum automated criteria for blocking builds and validating releases |
| [Traceability and Audit Policy](/sbd-toe/assets/policies/policy-rastreabilidade) | ⚠️ Optional | Critical apps, audited contexts | Requirement→control→validation mapping; traceable evidence for audit |
| [Security Exception Management Policy](/sbd-toe/assets/policies/policy-gestao-excecoes) | ✅ Yes | All applications | Formal process of justification, recording, deadline and acceptance of exceptions to requirements |

---

## 🧩 Suggested structure of each policy {#-estrutura-sugerida-de-cada-política}

Each organisational policy must contain, at a minimum:

- **Objective and scope** of the policy;
- **Scope of application**: who, where and when it applies;
- **Mandatory criteria and rules** (e.g. when to apply, how to select requirements, when to review);
- **Roles and responsibilities** (product team, architecture, security, management);
- **Traceability and evidence mechanisms**;
- **Review periodicity of the policy itself** (e.g. annual, with review after incidents).

---

## ✅ Final recommendations {#-recomendações-finais}

- Policies must be **approved by the security leadership** and communicated across the organisation;
- They must be **documented, accessible and versioned**;
- The existence of these policies is a precondition for:
  - Guaranteeing **organisational coherence and maturity**;
  - Sustaining **security audits or certifications**;
  - Serving as the basis for **software procurement and supplier assessment** processes.

> 📌 Templates for these policies may be made available as complementary `60-*.md` files in future versions of the manual.
