---
id: mapeamento-threats-requisitos
title: Mapping Threats to Security Requirements
description: How to link identified threats to the formal requirements defined in Chapter 2
tags: [mapeamento, requisitos, threats, stride, capitulo2, rastreabilidade]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/addon/07-mapeamento-threats-requisitos.md
  source_sha256: d4844007b1f9b071679e7d930408f1b1bbb1e742a0f2bb8a46e7595400fafb41
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 4d964bc95900e97ed4948d1411a9704d3ffd7ec09dd855410e65f36c97732120
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, lifecycle_phase, mapping, practitioner_manual, requirement_runtime, sbdtoe_sbd, slug_threat_modeling, threat, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: f3501507fc511bf8a504fc10d2edec54af0a4dcd831f192fdaba299365252a74
  translated_at: 2026-09-25T20:16:59Z
  stamped_at: 2026-09-26T18:38:31Z
  reviewed_by: null
---

# Mapping Threats to Security Requirements

## 🌟 Objective {#-objetivo}

To establish a systematic approach for mapping the threats identified in *threat modelling* to the **security requirements** defined in Chapter 2 of the SbD-ToE Manual, ensuring that:

- Each threat gives rise to at least one technical or organisational requirement;
- The derivation of requirements is traceable, auditable and documented;
- The link threat → requirement → control is explicit.

---

## 🧭 How to map threats to requirements {#-como-mapear-ameaças-a-requisitos}

The mapping must be based on unique identifiers and consistent formats:

| Threat ID | Threat description                                | Generated requirement                             | Ch. 2 category       | State       |
| --------- | -------------------------------------------------- | -------------------------------------------- | ---------------------- | ------------ |
| TM-001    | JWT with `alg: none` allows session forgery | EX-AUT-003: Mandatory JWT signature      | Authentication and Sessions | Mitigated     |
| TM-002    | `/admin/config` endpoint accessible to everyone         | EX-AC-010: Mandatory RBAC per endpoint    | Access Control     | Under validation |
| TM-003    | Excessive claims in the JWT expose sensitive data    | EX-DAT-005: Minimise claims per context   | Privacy and Data    | Justified  |
| TM-004    | Missing logging of administrative actions          | EX-LOG-001: Mandatory structured logging | Logging and Auditing    | In progress     |

*Illustrative identifiers (`EX-…`); they do not correspond to the Ch. 02 Requirements Catalogue.*

> ⚠️ Each row of the mapping must be documented in the repository or in the `mitigations.md` file.

---

## ✅ Examples of derived requirements {#-exemplos-de-requisitos-derivados}

| Requirement category (Ch. 2) | Typical threat type                           | Example of derived requirement                                      |
| ------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------ |
| Authentication and Sessions          | Reuse of unexpired JWTs              | EX-AUT-004: Maximum token TTL of 15 min                        |
| Access Control              | Uncontrolled access to administrative functions | EX-AC-012: Explicit verification of `role` in the backend             |
| Privacy and Data             | Unnecessary claims in tokens                 | EX-DAT-006: Dynamic scoping of claims per operation               |
| Logging and Auditing             | Actions without structured logging                   | EX-LOG-002: Logging of all sensitive actions with user ID |
| Protection against DoS             | Abuse of public endpoints (e.g. `/login`)      | EX-DOS-001: Rate limiting + CAPTCHA                               |

*Illustrative identifiers (`EX-…`); they do not correspond to the Ch. 02 Requirements Catalogue.*

---

## 🔗 Integration with the validation process {#-integração-com-o-processo-de-validação}

During the security validation phase of each project, this mapping must be used to:

- Confirm that each identified threat has a response (requirement or justification);
- Verify whether the requirement is implemented, tested or under a formal exception;
- Trace the origin of the requirement (where the real need came from).

---

## 📁 Suggested organisation {#-organização-sugerida}

```
📁 threat-model/
├── threats.yaml        # Lista de ameaças com threat_id, descrição, requisito associado
├── requisitos.yaml     # Requisitos com id, descrição, categoria, estado
└── mitigations.md      # Estado e histórico das decisões de segurança
```

---

## ✅ Good practices {#-boas-práticas}

- Always use unique, traceable identifiers (e.g. `TM-001`, `EX-AC-010` — illustrative identifiers; they do not correspond to the Ch. 02 Requirements Catalogue);
- Ensure consistency between the `threats.yaml`, `requisitos.yaml` and `mitigations.md` files;
- Update the mapping whenever new threats are introduced or requirements change;
- Use the mapping as mandatory input for security validations and technical audits;
- Integrate this process with ALM, CI/CD or GRC tools whenever possible.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                        | Relation to this file                            |
|----------------------------------|------------------------------------------------------|
| [threat-modeling-ci](./threat-modeling-ci) | Automated validation of the model in CI/CD pipelines |
| [base method](./metodologias-e-ferramentas)  | General principles of threat modelling in SbD-ToE     |

---

> This mapping consolidates the link between *threat analysis* and *formal security requirements*, making the process verifiable, justifiable and auditable.
