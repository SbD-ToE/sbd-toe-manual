---
id: validacao-arquitetura
title: Integrating Threat Modelling into Architecture Validation
description: How to integrate threat modelling practices into technical architecture artefacts and approval processes
tags: [arquitetura, threat modeling, validação, revisão técnica, rastreabilidade]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/addon/09-validacao-arquitetura.md
  source_sha256: b6d23a0655662ef05381b07226b6bed35b1850fe43d30d5850a4c618a47f9541
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 2eff6a37897e4e6740e9fc5ef72f41b72136bbede48402e957acc1c76b919c63
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [chapter_role, cycle_iteration, framework_source_corpus, lifecycle_phase, requirement_runtime, threat, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: bcaf69b0d463ffda5fb1eb1f619fd19205910436f10264acde1a86fbc45f2ff8
  translated_at: 2026-09-25T20:17:00Z
  reviewed_by: null
---

# Integrating Threat Modelling into Architecture Validation

## 🌟 Objective {#-objetivo}

To define how to incorporate *threat modelling* in a structured way into the **technical review and architecture validation** process, ensuring that:

- Threat analysis is a mandatory step in technical validation;
- Architecture artefacts include the results of threat modelling;
- There is traceability between architecture, threats and security requirements (Ch. 2).

---

## 📁 Artefacts to validate {#-artefactos-a-validar}

This process is aligned with the prescriptions of **Chapter 4 - Secure Architecture**, which defines the minimum artefacts required for technical validation:

| Architecture artefact     | Must contain…                                    | Validated by…               |
| ---------------------------- | ----------------------------------------------- | --------------------------- |
| Component Diagram      | Trust boundaries, sensitive flows              | Architect + Security       |
| Technical Solution Document | Summary of threats + mitigation or justification  | AppSec / PO / Dev team    |
| Release Sheet             | Confirmation of the control implemented per threat | Technical owner + QA          |
| Exceptions Sheet            | Formal justifications for unmitigated risks   | Security + Risk Management |

---

## ✅ Acceptance criteria for technical validation {#-critérios-de-aceitação-para-validação-técnica}

| Mandatory item                           | Source                                | Verified? |
| ------------------------------------------ | ------------------------------------ | ----------- |
| Complete threat model                  | DFD, STRIDE, LINDDUN or PASTA        | ☐           |
| Threats mapped to Ch. 2 requirements    | `threats.yaml` file or IriusRisk | ☐           |
| Mitigations defined and tested            | `mitigations.md`, backlog, tests    | ☐           |
| Accepted risks justified and documented | `decisions.md` or IriusRisk          | ☐           |
| Security participation in the validation     | Attendance / review record        | ☐           |

---

## 🧭 When to apply {#-quando-aplicar}

| Situation                                  | Validation requirement with threat modelling   |
| ----------------------------------------- | -------------------------------------------- |
| New critical application                    | ✅ Mandatory                                |
| Change to an existing architecture        | ✅ Mandatory                                |
| Integration with external systems          | ✅ Mandatory                                |
| Technical refactoring without functional impact | ⚠️ Recommended (if it affects sensitive flows) |

---

## 🔄 Integration with the lifecycle {#-integração-com-o-ciclo-de-vida}

This process must be articulated with **Chapter 6 - Secure Development**, ensuring that:

- Architecture validation takes place before development starts (technical gate);
- The threat model is available for review and included as a project deliverable;
- Changes to the system require updating the model and revalidation (automatic trigger);
- The validation status can be made visible in the backlog, ADO, GitHub or the management tool.

---

## ✅ Good practices {#-boas-práticas}

- Make the threat model a mandatory deliverable in critical projects;
- Use tools that integrate threat modelling and technical documentation (e.g. IriusRisk, PlantUML, Draw.io);
- Ensure that exception decisions are formalised with a justification, an owner and a deadline;
- Include security reviewers in the architecture stages (design review);
- Automate artefact verification and minimum validation as part of CI/CD.

---

> Integrating threat modelling into architecture is not optional in critical contexts - it is an integral part of informed technical decision-making and of security traceability.
