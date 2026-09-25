---
id: matriz-controlos-por-risco
title: Application of Requirements by Classification
description: Minimum mandatory requirements by application criticality classification
tags: [proporcionalidade, risco, requisitos, matriz, controlo]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/02-requisitos-seguranca/addon/06-matriz-controlos-por-risco.md
  source_sha256: 13338c9020122670444c665ed0f926d3b9c843cc950ca7602d1fa88c780d06fe
  source_commit: 1e6b81059f620fc0e330ba97f305988ac23b0279
  target_sha256: 580757b0c074c8035135c9faeb73279ff0e9b5dfe7a5ed2adfc8b23b05781c05
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [cycle_iteration, lifecycle_phase, requirement_runtime, risk_level, traceability, validation_evaluation]
  glossary_sha256: 5447788c5bc5d14d917dee2b1163b7073f852508e760bd50eeb2d10391e221f2
  translated_at: 2026-09-25T20:20:09Z
  reviewed_by: null
---

# Requirements Application Matrix by Risk Level

This matrix summarises, by **technical security theme**, the domains where **mandatory requirements** exist for each risk level (L1, L2, L3).

> ⚠️ **Important:** The ✔ mark indicates that **mandatory requirements exist within that theme for the risk level in question** - **it does not imply that every requirement of the theme applies** to every level.  
> The [full application requirements catalogue](./catalogo-requisitos) gives the details per requirement and level.

---

| Requirements Theme                                | L1 | L2 | L3 |
|---------------------------------------------------|:--:|:--:|:--:|
| 🔐 1. Authentication and Identity Management         | ✔ | ✔ | ✔ |
| 🧾 2. Access Control                          | ✔ | ✔ | ✔ |
| 📈 3. Logging, Auditing and Monitoring          |    | ✔ | ✔ |
| 📮 4. Session Management                            | ✔ | ✔ | ✔ |
| 🧱 5. Input Validation                        | ✔ | ✔ | ✔ |
| 🪪 6. Sensitive Data Protection                 |    | ✔ | ✔ |
| 🧮 7. Cryptography and Key Management             |    | ✔ | ✔ |
| 🚧 8. Error Handling and Unusual Behaviour | ✔ | ✔ | ✔ |
| 🧯 9. API and Interface Security                | ✔ | ✔ | ✔ |
| 🧼 10. Sanitisation and Safe Output                | ✔ | ✔ | ✔ |
| 🛡️ 11. Code Security and Build Cycle       | ✔ | ✔ | ✔ |
| 🪪 12. Third-Party and Library Security       | ✔ | ✔ | ✔ |
| 📦 13. Dependency Management (SBOM, SCA)         |    | ✔ | ✔ |
| 🐳 14. *Containers* and Isolated Environments           |    | ✔ | ✔ |
| ⚙️ 15. Secure Configuration                        | ✔ | ✔ | ✔ |
| 🏁 16. Deploy, Release and Runtime Controls         |    | ✔ | ✔ |
| 🔍 17. Security Testing and Validations           |    | ✔ | ✔ |
| 📊 18. Continuous Monitoring and Alerting           |    | ✔ | ✔ |
| 👥 19. Onboarding, Profiles and Access Segregation | ✔ | ✔ | ✔ |
| 📜 20. Governance, Compliance and Lifecycle   | ✔ | ✔ | ✔ |

---

> The matrix above must be used together with the annexes:
> - [requirements catalogue](./catalogo-requisitos)
> - [acceptance criteria](./criterios-aceitacao)
> - [traceability](./rastreabilidade-controlo)

