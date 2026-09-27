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
  source_sha256: 9be0861040b5d9e27937440e717fbaab32316e4fee7f68b5c99d99d20795c894
  source_commit: 32978973a6e4e01d6abcfe36fb0e33a8192cb20d
  target_sha256: 6f084e2ea966ef377e6524ebbd521babebb3c7563837480cd5df380108134212
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [framework_source_corpus, mirror_osf, practitioner_manual, requirement_runtime, role_tech_lead, sbdtoe_sbd]
  glossary_sha256: d28cee49fed70ce111a4e88cb69e29b3a9dc847756e51a3c97cc20e5e2e9e1a9
  translated_at: 2026-09-27T15:08:13Z
  stamped_at: 2026-09-27T15:08:13Z
  reviewed_by: null
---

# Automatic Dependency Update Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for the **controlled operation of automatic dependency update bots** in software repositories classified as L2 or L3.

Outdated dependencies accumulate vulnerabilities and drift from the approved secure state. Systematic manual updating is inefficient and prone to omissions. Automation tools such as Renovate or Dependabot make it possible to detect and propose updates continuously - but, without clear governance criteria, they can introduce breaking changes without adequate human review or, conversely, create noise that leads to the bots being deactivated out of operational frustration.

The objective of this policy is to ensure that:

- Update bots are active and configured in all L2/L3 repositories
- The auto-merge criterion is restricted to *patch* or security updates, with all mandatory gates green and a traceable record
- Updates with breaking change potential require human review and approval
- The cadence and grouping of PRs are configured to minimise operational noise

---

## 2. Scope and applicability {#2-âmbito-e-obrigatoriedade}

| Level | Applicability |
|---|---|
| L1 | Recommended; minimal configuration without auto-merge |
| L2 | Mandatory; active bot with conditional auto-merge |
| L3 | Mandatory; active bot without auto-merge and human handoff for all updates (expedited review for *security patches*) |

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

Automatic auto-merge of update PRs is only permitted at the levels and for the update types declared in section 4.1, when **all** of the following criteria are met and each automatic merge is recorded traceably (PR, previous and new version, gate results):

| Criterion | Requirement |
|---|---|
| Type of update | Patch or security update (CVE fix), with no declared breaking change; minor and major always require human review |
| Impact analysis | The bot confirms: no change to the public API, no semver major, no breaking change flags in the release notes |
| CI pipeline | All mandatory jobs and gates pass (tests, SAST, SCA, linters) |
| Security gates | No new CVE introduced by the update |
| Licence | Licence of the new version identical or equivalent to the previous one; no new licence added that is not on the whitelist |

:::warning
Minor and major updates always require human review, at any level, even if CI passes. At L3 there is no auto-merge: patches and *security patches* follow human review (expedited in the case of a CVE), as per section 4.1.
:::

### 4.1 Proportionality of auto-merge {#41-proporcionalidade-do-auto-merge}

| Type of update | L1 | L2 | L3 |
|---|---|---|---|
| Patch (e.g. 1.2.3 → 1.2.4) | Requires review (no auto-merge at L1, see §2) | Auto-merge if CI is green + gates OK | Requires human review |
| Minor without breaking (e.g. 1.2.x → 1.3.0) | Requires review | Requires review | Requires review + AppSec approval |
| Major (e.g. 1.x → 2.0.0) | Requires review + tests | Requires review + AppSec + tests | Requires review + AppSec + architect |
| Security patch (CVE fix) | Requires review (no auto-merge at L1, see §2) | Priority auto-merge if CI is green + gates OK | Expedited review: deadline ≤ 24h |

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
