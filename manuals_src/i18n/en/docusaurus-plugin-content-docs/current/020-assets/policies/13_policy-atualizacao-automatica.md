---
id: policy-atualizacao-automatica
title: Automatic Dependency Update Policy
description: Organisational policy that defines the requirements for operating automatic dependency update bots, including auto-merge criteria, impact analysis, human handoff and configuration proportional to the application's criticality level (L2, L3).
tags: [policy, dependências, atualização, Renovate, Dependabot, auto-merge, impact analysis, handoff, cap05, L2, L3, governance, supply chain]
grupo: supply-chain
sidebar_position: 13
translation:
  source_locale: pt
  source_path: 020-assets/policies/13_policy-atualizacao-automatica.md
  source_sha256: 8d7cab5f4ef127db452cbf0648562f6b3f2206957490d9b384359d8b25cbba4b
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: dd697639639d42443eee299b7687903932eefd904087cd189da5f3c16d8fc161
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bc04ded428e40ee1c214f8535dfb1904655b64166d0aa82b5df521e4230b8cb0
  glossary_keys: [framework_source_corpus, mirror_osf, practitioner_manual, requirement_runtime, sbdtoe_sbd]
  glossary_sha256: 05793a370ed1fb201060fb6b2cf031539a610595620b79431a30c5c282aa2aa9
  translated_at: 2026-09-26T14:10:50Z
  reviewed_by: null
---

# Automatic Dependency Update Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for the **controlled operation of automatic dependency update bots** in software repositories classified as L2 or L3.

Outdated dependencies accumulate vulnerabilities and drift from the approved secure state. Systematic manual updating is inefficient and prone to omissions. Automation tools such as Renovate or Dependabot make it possible to detect and propose updates continuously - but, without clear governance criteria, they can introduce breaking changes without adequate human review or, conversely, create noise that leads to the bots being deactivated out of operational frustration.

The objective of this policy is to ensure that:

- Update bots are active and configured in all L2/L3 repositories
- The auto-merge criterion is restricted to updates with verified zero or minimal impact
- Updates with breaking change potential require human review and approval
- The cadence and grouping of PRs are configured to minimise operational noise

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

| Level | Applicability |
|---|---|
| L1 | Recommended; minimal configuration without auto-merge |
| L2 | Mandatory; active bot with conditional auto-merge |
| L3 | Mandatory; active bot with restricted auto-merge and human handoff for any update with an impact |

---

## 3. Accepted tools {#3-ferramentas-aceites}

The organisation accepts the following tools for dependency update automation:

| Tool | Supported ecosystems | Notes |
|---|---|---|
| **Renovate** | npm, pip, Maven, Go, Docker, Terraform, Helm, etc. | Preferred; greater configuration granularity |
| **Dependabot** | npm, pip, Maven, Go, Docker, GitHub Actions, etc. | Accepted; native integration with GitHub |
| Equivalent alternatives | Variable | Must support impact analysis, grouping and auto-merge configuration |

---

## 4. Auto-merge criteria {#4-critérios-de-auto-merge}

Automatic auto-merge of update PRs is only permitted when **all** of the following criteria are met:

| Criterion | Requirement |
|---|---|
| Type of update | Patch or minor with no declared breaking change |
| Impact analysis | The bot confirms: no change to the public API, no semver major, no breaking change flags in the release notes |
| CI pipeline | All jobs pass (tests, SAST, SCA, linters) |
| Security gates | No new CVE introduced by the update |
| Licence | Licence of the new version identical or equivalent to the previous one; no new licence added that is not on the whitelist |

:::warning
Auto-merge at L3 is restricted to patch updates. Minor updates at L3 require human review, even if CI passes.
:::

### 4.1 Proportionality of auto-merge {#41-proporcionalidade-do-auto-merge}

| Type of update | L1 | L2 | L3 |
|---|---|---|---|
| Patch (e.g. 1.2.3 → 1.2.4) | Auto-merge if CI is green | Auto-merge if CI is green + gates OK | Requires human review |
| Minor without breaking (e.g. 1.2.x → 1.3.0) | Requires review | Requires review | Requires review + AppSec approval |
| Major (e.g. 1.x → 2.0.0) | Requires review + tests | Requires review + AppSec + tests | Requires review + AppSec + architect |
| Security patch (CVE fix) | Auto-merge if CI is green | Priority auto-merge if CI is green | Expedited review: deadline ≤ 24h |

---

## 5. Human handoff {#5-handoff-humano}

When the impact analysis determines that the update is not eligible for auto-merge, the bot must:

- [ ] Open a PR with the label `requires-human-review`
- [ ] Include in the body of the PR: previous version, new version, relevant changelog, identified breaking changes, refactoring guidelines when available
- [ ] Assign the PR to the Tech Lead or Developer responsible for the dependency
- [ ] Not merge without explicit approval

The PR must not remain open without a response for more than:

| Severity | L2 | L3 |
|---|---|---|
| Security patch (CVE) | 48 hours | 24 hours |
| Minor / Major | 14 days | 7 days |

Update PRs without a response within the deadline must generate an alert for the Tech Lead and the AppSec Engineer.

---

## 6. Mandatory configuration of the bots {#6-configuração-obrigatória-dos-bots}

### 6.1 Minimum configuration parameters {#61-parâmetros-mínimos-de-configuração}

The bot configuration (e.g. `renovate.json`, `.github/dependabot.yml`) must include:

- [ ] Grouping of related dependencies into single PRs (e.g. all `@types/*` dependencies grouped)
- [ ] Defined update window (e.g. Monday to Friday, outside freeze periods)
- [ ] Maximum number of simultaneously open PRs (recommended: ≤ 5 per repository)
- [ ] Automatic labels by type of update (`patch`, `minor`, `major`, `security`)
- [ ] Explicit auto-merge rules in the configuration file (not assumed by default)
- [ ] Exclusion of dependencies marked as manually managed

### 6.2 Internal repositories as the source {#62-repositórios-internos-como-fonte}

At L2/L3, the bot must resolve packages through the internal repository (proxy/mirror), not directly from the internet. The bot configuration must reference the organisation's internal registries.

---

## 7. Integration with SCA and gates {#7-integração-com-sca-e-gates}

Automatic updating does not waive SCA analysis:

- [ ] Each update PR triggers the complete CI pipeline, including SCA
- [ ] Auto-merge is blocked if SCA detects a new CVE introduced by the proposed version
- [ ] The SCA report is attached to the PR as an artefact or a comment

---

## 8. Freeze periods and exceptions {#8-freeze-periods-e-exceções}

During release freeze periods (e.g. pre-release, regulated maintenance windows), the bots must:

- Suspend the opening of new update PRs not related to security
- Allow security patch PRs even during a freeze (with mandatory human review at L3)

The definition of freeze periods must be configured in the bot's configuration file or managed through a pipeline variable.

---

## 9. Monitoring and metrics {#9-monitorização-e-métricas}

The following indicators must be monitored to assess the health of the update process:

| Metric | Description |
|---|---|
| Auto-merge rate | % of update PRs resolved by auto-merge vs. human review |
| Mean time to resolve security PRs | MTTR for security patches |
| Update PRs open for more than 14 days | Indicator of accumulating technical debt |
| CVEs detected post-merge | Updates that introduced CVEs not detected before the merge |

---

## 10. Responsibilities {#10-responsabilidades}

| Role | Responsibility |
|---|---|
| Developer | Respond to human handoff PRs within the deadline; review breaking changes |
| Tech Lead | Configure and maintain the bot's configuration file; manage PRs with major impact |
| AppSec Engineer | Define auto-merge criteria; validate update PRs with a security impact; review the configuration periodically |
| DevOps / SRE | Integrate the bot into the repository; configure internal repositories as the source; monitor metrics |

---

## 11. Review and audit of this policy {#11-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Incident caused by an automatic update that introduced a regression or vulnerability
- Significant change in the capabilities of the automation tools used
- Change to the release freeze policy that affects the operation of the bots

---

## 12. Normative and technical references {#12-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 05 - Dependencies, SBOM and SCA | Update automation, impact analysis, handoff |
| Dependency Management Policy (`10_policy-dependencias.md`) | Dependency approval and pinning |
| CVE Exceptions Policy (`12_policy-excecoes-cve.md`) | Management of CVEs detected during updates |
| Renovate Documentation | Configuration of update bots |
| Dependabot Documentation | Alternative configuration in GitHub ecosystems |
| Semantic Versioning (semver.org) | Basis for impact analysis by type of version |
| NIST SP 800-161 | Supply Chain Risk Management - updating of components |
