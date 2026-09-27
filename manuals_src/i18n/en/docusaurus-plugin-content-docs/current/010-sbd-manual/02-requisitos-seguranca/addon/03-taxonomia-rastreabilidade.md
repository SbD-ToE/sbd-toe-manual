---
id: taxonomia-rastreabilidade
title: Requirements Traceability Taxonomy
description: Two complementary identification systems - the canonical SbD-ToE catalogue and the project's operational tags - and how to articulate them across the lifecycle.
tags: [taxonomia, rastreabilidade, requisitos, domínios, ALM]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/02-requisitos-seguranca/addon/03-taxonomia-rastreabilidade.md
  source_sha256: d0148ebe92120a2ee23329bc54866e7b05276c026c34fd65310e64f59f71741b
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: f212e5100a738eb331ec3db6ddd59073e3a93cbec8c71275b2dd9ec2fef57081
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, cycle_iteration, framework_source_corpus, lifecycle_phase, normative_empirical, practitioner_manual, requirement_runtime, risk_level, sbdtoe_sbd, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 2d7fb0237e48d1c2e3a7b41c46353ea53bbcc10e7c6b1b9e4d59642563705529
  translated_at: 2026-09-25T20:20:07Z
  stamped_at: 2026-09-26T18:33:00Z
  reviewed_by: null
---

# Security Requirements Taxonomy and Traceability

SbD-ToE operates with **two complementary identification systems**, each with a distinct purpose. Understanding the difference and the relationship between them is a precondition for effective traceability - without it, the requirements catalogue becomes disconnected from the real development work.

---

## 1) Two systems, two purposes {#1-dois-sistemas-dois-propósitos}

### Canonical ID (SbD-ToE catalogue) {#id-canónico-catálogo-sbd-toe}

The Ch. 02 requirements catalogue assigns each requirement a **stable canonical identifier**:

```
CATEGORIA-NNN
```

| Component | Description | Example |
|------------|-----------|---------|
| `CATEGORIA` | 2–3 upper-case letters, identifies the security domain | `AUT`, `LOG`, `VAL` |
| `NNN` | 3-digit sequential number | `001`, `003`, `012` |

**Examples:** `AUT-001` (mandatory MFA), `LOG-003` (log integrity protection), `VAL-002` (input parameter validation)

This ID is the **permanent normative reference** - it identifies the requirement in the manual, in regulatory cross-checks, in control matrices and in architecture documentation. It is independent of any specific project.

---

### Operational tag (per-project instantiation) {#tag-operacional-instanciação-por-projecto}

When a canonical requirement is adopted by a concrete project, it is **instantiated** with that project's context - notably the risk level - giving rise to a traceable operational tag:

```
SEC-Lx-DOMINIO-CODIGO
```

| Component | Description | Example |
|------------|-----------|---------|
| `SEC` | Fixed prefix - indicates a security requirement | `SEC` |
| `Lx` | Risk level of the application (L1, L2 or L3) | `L2` |
| `DOMINIO` | Technical domain, aligned with the catalogue | `AUT`, `LOG` |
| `CODIGO` | Abbreviated semantic code of the requirement | `MFA`, `BRUTE` |

**Full example:** `SEC-L2-AUT-MFA`

This tag is the identifier used in the project's lifecycle artefacts - backlog, code, tests, pipeline, audit evidence.

---

## 2) The relationship between the two systems {#2-a-relação-entre-os-dois-sistemas}

The canonical ID is the **source**; the operational tag is the **contextualised instance**. The flow is always downward:

```
Catálogo SbD-ToE          Projecto concreto
─────────────────          ────────────────────────────────
AUT-001                →   SEC-L2-AUT-MFA   (aplicação pública, risco L2)
AUT-001                →   SEC-L1-AUT-MFA   (ferramenta interna, risco L1)
LOG-003                →   SEC-L2-LOG-INTEG
VAL-002                →   SEC-L3-VAL-SQLI  (app com dados regulados, risco L3)
```

The same canonical requirement can give rise to different tags in different projects, reflecting different risk contexts. This is intentional: **proportionality is a property of the project, not of the requirement**.

More importantly: traceability does not end at the operational tag. The tag is the project's visible identifier, but the minimum expected chain must continue upstream and downstream:

```text
classificação / risco → requisito canónico → tag operacional → ameaça / driver de risco
→ critério de validação / teste / revisão → evidência → exceção / decisão de revisão
```

Without this chain, the requirement is “present” in the project but ceases to be governable, auditable and reassessable when the context changes.

---

## 3) Supported technical domains {#3-domínios-técnicos-suportados}

| Domain | Associated canonical category |
|---------|------------------------------|
| `AUT` | Authentication and identity management |
| `ACC` | Access control and authorisation |
| `LOG` | Logging, auditing and monitoring |
| `SES` | Sessions and state management |
| `VAL` | Data validation and sanitisation |
| `ERR` | Error and message handling |
| `CFG` | Secure configuration and parameter management |
| `API` | Security of APIs and external services |
| `INT` | Integrations and message exchanges |
| `REQ` | Requirements definition and management |
| `DST` | Artefact distribution |
| `IDE` | Development tools and environments |
| `ENC` | Sensitive data and cryptography |

---

## 4) Where to apply each system {#4-onde-aplicar-cada-sistema}

| Context | System to use | Example |
|----------|---------------|---------|
| SbD-ToE Manual, normative cross-checks, architecture | Canonical ID | `LOG-003` |
| Backlog (stories, epics, tasks) | Operational tag | `SEC-L2-LOG-INTEG` |
| Comments in source code | Operational tag | `// SEC-L3-VAL-SQLI` |
| CI/CD gates and automated validations | Operational tag | `SEC-L2-AUT-MFA` |
| Test cases and acceptance criteria | Operational tag + reference to the canonical ID | `SEC-L2-AUT-MFA` → `AUT-001` |
| Audit reports and evidence | Both - full traceability | `AUT-001` / `SEC-L2-AUT-MFA` |

The presence of the canonical ID in reports and evidence is what links the project's work to the normative catalogue - and, by extension, to external frameworks such as ASVS, NIST or regulatory requirements.

---

## 5) Verification and maintenance {#5-verificação-e-manutenção}

Operational tags must be **validated periodically** against:
- The [canonical catalogue](./catalogo-requisitos) - to guarantee that the referenced IDs exist and are up to date;
- The [controls matrix by risk](./matriz-controlos-por-risco) - to confirm that the tag's `Lx` level is consistent with the application's current classification.

Whenever there is a material change of risk, architecture, integration, data processed or form of validation, this verification must be treated as a **requirement review event**. In such cases, the organisation must confirm whether:

- the requirement remains applicable as it stands;
- the operational tag remains consistent with the project's `Lx` level;
- the link to *Threat Modelling* and to validation remains valid;
- any [documented exception](./gestao-excecoes) has ceased to be acceptable or needs revalidation.

The organisation must keep a record of:
- Adopted requirements and their canonical IDs;
- Active operational tags per project/application;
- Records of review, change or re-trigger;
- Validations carried out and evidence generated;
- [Documented exceptions](./gestao-excecoes).

---

> 📌 The distinction between canonical ID and operational tag is not merely formal - it is the mechanism that allows **centralised governance of the catalogue** with **decentralised, traceable and auditable implementation** in each project.
