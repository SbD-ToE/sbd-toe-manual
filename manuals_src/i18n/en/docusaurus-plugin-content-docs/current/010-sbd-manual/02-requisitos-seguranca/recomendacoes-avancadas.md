---
id: recomendacoes-avancadas
title: Advanced Practices in Security Requirements
description: Reinforced recommendations for environments with greater regulatory demands or maturity
tags: [avançado, requisitos, rastreabilidade, validação, políticas]
sidebar_position: 30
translation:
  source_locale: pt
  source_path: 010-sbd-manual/02-requisitos-seguranca/recomendacoes-avancadas.md
  source_sha256: e0f6e505bfd8614d6cca9e983f94a56f15341831dd8e642498405bfacdb21836
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: a0bc0db2ffa1f1f64413097494190789494301f8192a875b45cf1c1e5ff5e011
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [mapping, maturity, requirement_runtime, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: 0a7b9e978aeefac6f56427ce97f72e2d922241729c8649f00dd1cf2e887e6476
  translated_at: 2026-09-25T20:22:04Z
  stamped_at: 2026-09-26T18:33:14Z
  reviewed_by: null
---

# Advanced Practices in Security Requirements

This annex presents **non-mandatory advanced practices** that may be adopted by organisations with greater maturity, normative demands (e.g. PCI-DSS, ISO 26262, IEC 62443), or a need for formal traceability and audit.

> These recommendations **do not replace** the requirements of the SbD-ToE catalogue, nor are they considered in the calculation of maturity or threat mitigation.  
> They serve as an **optional extension** for critical contexts, and contribute to alignment with models such as **DSOMM** (Design & Development).

---

## 🔀 1. Automated Traceability {#-1-rastreabilidade-automatizada}

> **Objective**: Enable continuous traceability between requirements, code, tests and validations.

- Use an ALM with traceability support (e.g. Codebeamer, Jama, Polarion, Jira + plugins)
- Create **bidirectional links** between requirements and artefacts
- Automate the extraction of coverage per requirement (e.g. CI validates that each requirement is covered)

---

## 🧪 2. Acceptance Criteria in BDD / Formal Language {#-2-critérios-de-aceitação-em-bdd--linguagem-formal}

> **Objective**: Make requirements testable and machine-verifiable.

- Use Gherkin (Given–When–Then) or equivalent formats
- For critical environments, consider languages such as OCL, TLA⁺ or EARS models
- Example in Gherkin:

```gherkin
Feature: Autenticação multifator

  Scenario: Acesso por utilizador administrativo
    Given o utilizador possui privilégios de administrador
    When efetua login com credenciais válidas
    Then é solicitado a fornecer segundo fator de autenticação
```

---

## 📦 3. Internal Catalogues and Requirement Profiles {#-3-catálogos-internos-e-perfis-de-requisitos}

> **Objective**: Reuse and standardise common requirements by application type.

- Create profiles by domain (e.g. internal API, mobile app)
- Keep versioned templates with REQ-IDs and criteria by type
- Validate the profiles with technical and architecture teams

---

## 📄 4. Integration with Threat Modelling {#-4-integração-com-threat-modeling}

> **Objective**: Align requirements with real modelled threats.

- Link REQ-IDs to threats (e.g. `VAL-002` mitigates [STRIDE] Input Validation)
- Justify requirements with model outputs (e.g. DFDs, IriusRisk)
- Use automated annotations with tools such as ThreatSpec or Diagrams as Code

---

## 📊 5. Coverage Measurement and Management {#-5-medição-e-gestão-de-coverage}

> **Objective**: Monitor the definition, application and validation of requirements.

- Useful metrics:
  - % with defined criteria
  - % with automated tests
  - % validated in QA
  - % traceable in the backlog

- Generate reports per release or pipeline with the coverage status

---

## 🔐 6. Integration with Regulatory Compliance {#-6-integração-com-conformidade-regulatória}

> **Objective**: Guarantee that the requirements cover mandatory normative controls.

- Maintain a mapping with:
  - PCI-DSS v4.0
  - ISO/IEC 27001 + 27002
  - NIST 800-53, 800-171
  - HIPAA, GDPR, ENS, etc.
- Create layers of regulatory requirements with tags (e.g. `#PCI-REQ-8.3`)

---

## 🧠 7. Examples of High Maturity {#-7-exemplos-de-maturidade-elevada}

| Practice                                 | Added value                                  | Suggested tools              |
|-----------------------------------------|-----------------------------------------------------|-------------------------------------|
| Automated link between REQ-ID and code      | Auditability and compliance                         | Semgrep, GitHub Adv. Security      |
| Criteria in Gherkin                    | Testability and continuous validation                | Cucumber, Behave                   |
| Bidirectional traceability            | Support for regulated audits                      | Jama, Jira Traceability Matrix     |
| Requirements coverage metrics      | Visibility and continuous improvement                   | TestRail, customised dashboards  |
| Internal requirement profiles           | Scalability and standardisation                     | Versioned internal catalogue        |

---

## ✅ Final Considerations {#-considerações-finais}

These practices **are not mandatory**, but are recommended when:

- The organisation is subject to formal certifications
- Criticality demands full traceability
- There are large, multidisciplinary teams
- Third-party audits need to be supported

> 📌 This annex may be extended with real examples and automatic traceability scripts.

---

## 🤖 8. Requirements as Code (Policy as Code) {#-8-requisitos-como-código-policy-as-code}

> **Objective**: Represent requirements in a structured, automatically enforceable format.

- Use YAML, Rego (OPA), JSON Schema, `.policy`
- Integrate with pipelines for automatic validation
- Example in Rego:

```rego
# Identificadores ilustrativos (EX-…); não correspondem ao Catálogo de Requisitos do Cap. 02.
package security.requisitos

default permitir = false

permitir {
  input.req_id == "EX-AUT-001"
  input.mfa_ativo == true
}
```

> 📍 This practice responds directly to **DSOMM - Policy as Code**.

---

## 🧰 9. Requirements Derived from Secure Design Principles {#-9-requisitos-derivados-de-princípios-de-design-seguro}

> **Objective**: Translate architecture principles into verifiable requirements.

- Map REQ-IDs to principles such as *Least Privilege*, *Fail Safe Defaults*
- Create "Design Guidelines to REQ" mappings
- Ensure that architecture decisions result in traceable requirements

> 🧐 This practice reinforces alignment with **DSOMM - Design & Development**.
