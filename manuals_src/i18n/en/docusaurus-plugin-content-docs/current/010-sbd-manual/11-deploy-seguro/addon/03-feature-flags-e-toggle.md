---
id: 03-feature-flags-e-toggle
title: Feature Control with Feature Flags
description: Use of feature toggles with security, traceability and the capacity for reversal in production.
tags: [tipo:anexo, grupo:execucao, tema:feature-flags, toggles, deploy, rastreabilidade]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/addon/03-feature-flags-e-toggle.md
  source_sha256: de5a2bf212bf5f3ea1c1ee7926bcc8ccdd7b26739d31399881ea9d64eae8a67c
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: fc9f192a9a4564a66b69f185604e5d8523b1e970c6ec46f48dc843dc0f508c2c
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [avaliacao, chapter_role, discipline, traceability, validation_evaluation]
  glossary_sha256: 4c352f0352ff64aa4eca008d4f8409f9204dc6d5bb1b886ce0b6c2d80e8843e9
  translated_at: 2026-09-26T11:00:48Z
  stamped_at: 2026-09-26T18:35:25Z
  reviewed_by: null
---


# Secure Use of Feature Flags and Toggles

## 🌟 Objective {#-objetivo}

To establish good practices for the secure use of **feature flags** (or toggles), with a focus on:

- Minimising the risk of failures in production;
- Enabling progressive and reversible deliveries;
- Reinforcing traceability, governance and formal validation;
- Preventing abuse or uncontrolled behaviour at runtime.

---

## 🧬 What Feature Flags are {#-o-que-são-feature-flags}

Feature flags are mechanisms that make it possible to activate or deactivate functionality **without a new deployment**, based on configuration rules. They are widely used for:

- Progressive delivery;
- Canary releases;
- A/B testing;
- Failure containment;
- Operational management of critical functionality.

### Common types of toggles {#tipos-comuns-de-toggles}

| Type                    | Description                                                    | Practical example                                  |
|-------------------------|--------------------------------------------------------------|--------------------------------------------------|
| **Release Toggle**      | Controls functionality under development                  | New API visible only to the internal team        |
| **Ops Toggle**          | Switches technical flows or sensitive integrations on/off        | Temporarily deactivating the sending of emails        |
| **Permission Toggle**   | Defines who can access a functionality                 | Only admins access internal dashboards           |
| **Experiment Toggle**   | Supports experiments and optimisations by user group | Showing a new layout to 50% of users       |
| **Kill Switch**         | Deactivates functionality immediately                   | Interrupting notifications after an incident          |

---

## 🛠️ How to apply {#️-como-aplicar}

### 🔐 Security and isolation {#-segurança-e-isolamento}

- Never use toggles as a substitute for access control;
- Evaluate toggles in the **backend** - not only in the frontend;
- Avoid **client-side toggles** for sensitive logic;
- Ensure that all the associated logical paths are testable.

### 🛡️ Traceability and metadata {#️-rastreabilidade-e-metadata}

Each toggle must have:

- A unique and descriptive name;
- An owner (responsible team or person);
- A scope (environment, group, tenant, region...);
- An activation condition and an expiry condition;
- A functional and security justification.

### 📜 Management as code {#-gestão-como-código}

- Manage toggles as infrastructure (e.g. Feature Flags as Code);
- Version the configuration (YAML, JSON, etc.);
- Apply via PRs, with review and formal approval.

---

## 🧪 Example of toggle metadata {#-exemplo-de-metadata-de-toggle}

```yaml
toggle: enable_enhanced_logging
description: Ativa logging estendido para debugging
owner: equipa-devsecops
enabled_by_default: false
scope: ["staging", "grupo-beta"]
expires_after: 2025-12-01
justification: Necessário para investigação de comportamento anómalo
```

---

## ⚠️ Risks and bad practices {#️-riscos-e-más-práticas}

| Anti-pattern                        | Consequence                                      |
|----------------------------------|---------------------------------------------------|
| Toggle without an owner                 | Nobody knows who controls it                      |
| No expiry                    | Accumulated technical debt                          |
| Evaluation only in the frontend     | Bypass possible through UI manipulation             |
| Silent toggle (no logs)     | Difficulty in debugging and auditing              |
| No defined fallback            | Unpredictable behaviour if switched off           |

---

## ✅ Good practices {#-boas-práticas}

- Define a **periodic review SLA** (e.g. all toggles reviewed monthly);
- Alert on toggles active for more than 60 days;
- Block merges of code with toggles without metadata;
- Validate the alternative paths (with and without the toggle active);
- Include toggles in the release approval process.

---

## 🧰 Supporting tools {#-ferramentas-de-suporte}

| Tool         | Type                  | Notes                                     |
|--------------------|-----------------------|-------------------------------------------|
| **LaunchDarkly**   | SaaS                  | Dashboards, multi-language SDKs          |
| **Unleash**        | Open Source / SaaS    | Self-hosted, rollout strategy        |
| **Flagsmith**      | SaaS / Open Source    | Integration with GitOps and RBAC              |
| **FeatureHub**     | Open Source           | Focus on multiple teams, multi-tenancy  |

---

## 📎 Cross-references {#-referências-cruzadas}

| Document / Chapter              | Relation to this topic                             |
|-----------------------------------|---------------------------------------------------|
| Ch. 01 - Risk Management         | Risk assessment associated with toggles            |
| Ch. 06 - Secure Development  | Testability of conditional paths            |
| Ch. 10 - Security Testing     | A/B tests, induced failures and fallback           |
| Ch. 11 - Secure Deployment           | Toggles as an execution control mechanism    |
| Ch. 12 - Monitoring and Operations           | Active observation of behaviour with toggles    |

---

> 🌟 Toggles are powerful - but only when used with discipline, control and traceability.  
> They must be treated as **critical runtime assets**, with direct implications for security and operational risk.
