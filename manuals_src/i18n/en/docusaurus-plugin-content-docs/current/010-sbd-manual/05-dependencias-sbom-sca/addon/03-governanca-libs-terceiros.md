---
id: governanca-libs-terceiros
title: Governance of Third-Party Libraries and Components
description: Practices for the control, approval and traceability of external libraries and third-party packages
tags: [dependencias, sbom, sca, supply-chain, governance]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/addon/03-governanca-libs-terceiros.md
  source_sha256: 1a0fe80e442de7a9a476d25aaea1f08e63cdce81cf2874825b9142d0a92ea47f
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 174f1c64b9162aed558c4665c751510f6178cd19460b36c38d53b0a356a6e8be
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [maturity, traceability, validation_evaluation]
  glossary_sha256: f9a5a9e56e7fa1ecaeafd95addd1673d2210324c41890ac3b0befd102a0bda7c
  translated_at: 2026-09-26T08:45:23Z
  stamped_at: 2026-09-26T18:33:47Z
  reviewed_by: null
---

# Governance of Third-Party Libraries and Components

## 🌟 Objective {#-objetivo}

Establish clear and verifiable rules for the **use, approval, replacement and traceability** of third-party libraries and components in internally developed applications.

> 🚨 Many supply chain incidents originate in malicious, abandoned or unverified libraries. This control is fundamental.

---

## 🔢 Governance principles {#-princípios-de-governaça}

1. **Permitted repositories** must be explicitly defined and controlled.
2. Every library must have:
   - Active maintenance
   - A compatible licence
   - Validated minimum popularity/community
3. Libraries with active CVEs **may not be used without a formalised exception**.
4. The use of "exotic" or single-author libraries must be justified.

---

## 🚀 Approval process {#-processo-de-aprovação}

| Stage                     | Action                                                     | Artefact                  |
|--------------------------|-----------------------------------------------------------|-----------------------------|
| Request for a new lib   | Dev submits name, version, function, origin             | Form / issue          |
| Security analysis       | AppSec or reviewer checks: CVEs, origin, history      | Comment with approval or veto |
| Legal validation           | (optional) Checks licence compatibility          | List of approved licences |
| Formal approval          | Record of the decision and validity period (if applicable)    | Approvals repository     |

> This process may be lightweight (via Pull Request) or formalised (via a registration tool).

---

## 🔎 Acceptance criteria {#-critérios-de-aceitação}

| Criterion                         | Recommended? | Justification                                   |
|----------------------------------|--------------|--------------------------------------------------|
| Permissive open source licence   | Yes          | E.g. MIT, Apache 2.0                             |
| Actively maintained (>1 year)    | Yes          | Recent commits and updated versions          |
| Active community (issues/PRs)   | Yes          | Avoids abandoned libraries                   |
| Use in other projects   | Yes          | Reinforces trust and stability                |
| Presence of tests or CI         | Yes          | Indicates the project's maturity                    |
| Obfuscated or minified code   | No          | Avoid opaque dependencies                      |
| Unknown or suspicious origin  | No          | Exclude unverified sources                   |

---

## 📝 Decision record {#-registo-de-decisões}

Each library must be traceable to an approval decision. Recording the following is suggested:

- Name, version, package hash
- Justification for use
- Result of the SCA analysis
- Approval or exception
- Owner and date

> This record may live in a `.yaml` file, a Git repository, Confluence, Jira, etc.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                   | Relationship with governance                            |
|-----------------------------|---------------------------------------------------------|
| `01-inventario-sbom.md`     | Control of what is being used                   |
| `02-analise-sca.md`         | Basis for acceptance or blocking                      |
| `09-excecoes-e-aceitacao-risco.md` | Formal justifications for deviations               |

---

> 🔍 Dependency governance is one of the pillars of modern security, especially in exposed environments or those with regulatory obligations (NIS2, CRA, ISO 27001).
