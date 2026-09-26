---
id: policy-guidelines-desenvolvimento
title: Secure Development Guidelines Curation Policy
description: Organisational policy that defines the requirements for the selection, tailoring, publication, versioning and periodic review of secure development guidelines per technology stack, including the conversion of rules into automatic linter and SAST configurations, proportional to the criticality level (L1, L2, L3).
tags: [policy, guidelines, desenvolvimento seguro, curadoria, linters, SAST, rulesets, tailoring, cap06, L1, L2, L3, governance]
grupo: desenvolvimento
sidebar_position: 14
translation:
  source_locale: pt
  source_path: 020-assets/policies/14_policy-guidelines-desenvolvimento.md
  source_sha256: 9d7e94456e4f9991bfc197b5ffb35cf25464622fc7c11bb9e2db03a2475a5a44
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 09eb9ffd0853ea6e13d8556f58a1d5111d368110c65f38ba021b6e419fa2ba5a
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bc04ded428e40ee1c214f8535dfb1904655b64166d0aa82b5df521e4230b8cb0
  glossary_keys: [cycle_iteration, framework_source_corpus, lifecycle_phase, requirement_runtime, sbdtoe_sbd, transversal, verification_taxonomy]
  glossary_sha256: add21735274f5514d238dc6a3f335e37402dc7968666ccf892ef3e9b803eeb02
  translated_at: 2026-09-26T14:10:51Z
  reviewed_by: null
---

# Secure Development Guidelines Curation Policy

## 1. Objective {#1-objetivo}

This policy defines the requirements for the **selection, curation, versioning and periodic review of secure development guidelines** applicable to the technology stacks used by the organisation.

Secure development guidelines are not static good-practice documents - they are living mechanisms of technical governance. When well curated and operationalised as linter configurations and SAST rulesets, they reduce reliance on ad hoc decisions, ensure consistency across teams and make compliance verifiable in an automated way.

The objective of this policy is to ensure that:

- Each technology stack in use has approved and published secure development guidelines
- The guidelines are derived from recognised sources, with tailoring documented for the organisation's context
- The rules are operationalised as tool configurations (linters, SAST) whenever technically feasible
- Curation is carried out in regular cycles with formal approval

---

## 2. Scope {#2-âmbito}

This policy applies to all technology stacks used in software development in the organisation. A "stack" is understood as the combination of language + runtime + main frameworks (e.g. Python/FastAPI, Java/Spring, TypeScript/Node, Go, Terraform/AWS).

---

## 3. Reference sources for guidelines {#3-fontes-de-referência-para-guidelines}

Organisational guidelines must be derived from recognised technical sources, which include (non-exclusively):

| Source | Domain |
|---|---|
| OWASP Secure Coding Practices | Cross-cutting secure development baseline |
| OWASP Cheat Sheet Series (per technology) | Specific references per language and framework |
| CWE Top 25 / SANS Top 25 | Most critical implementation weaknesses |
| NIST SSDF (SP 800-218) | Secure software framework by lifecycle phase |
| Upstream rulesets of SAST tools | Semgrep, CodeQL, SonarQube, Bandit, ESLint Security, etc. |
| Vendor benchmarks | Security guidelines of the language or framework (e.g. Go security, Python security model) |

Organisational tailoring based on these sources must be explicitly documented - indicating which rules were adopted unchanged, which were tightened, which were disabled and with what justification.

---

## 4. Structure of a guideline per stack {#4-estrutura-de-uma-guideline-por-stack}

Each published guideline must have, at a minimum:

- [ ] Identification of the stack covered (language, minimum version, main frameworks)
- [ ] Document version and publication date
- [ ] Sources used and version referenced
- [ ] Mandatory rules (cannot be disabled by individual projects)
- [ ] Recommended rules (may be disabled with a recorded justification)
- [ ] Tool configuration derived from the rules (linter/SAST configuration files)
- [ ] Documented tailoring (upstream rules disabled and justification)
- [ ] Person responsible for curation and approval

---

## 5. Operationalisation as tool configurations {#5-operacionalização-como-configurações-de-ferramentas}

The guidelines must be converted into tool configurations whenever the ecosystem allows it:

| Objective | Reference tools |
|---|---|
| Static security analysis (SAST) | Semgrep, CodeQL, Bandit, Brakeman, SpotBugs, ESLint Security |
| Quality and security linters | ESLint, Pylint, Flake8, golangci-lint, ktlint, Checkstyle |
| Verification of dangerous patterns | Semgrep with customised rulesets, grep-based rules |
| Secret detection | TruffleHog, Gitleaks, detect-secrets |

The resulting configurations must be:

- [ ] Versioned in the organisation's central configuration repository
- [ ] Reusable by projects (by reference, not by copy)
- [ ] Applied automatically by the CI pipeline - not dependent on the developer's local configuration

### 5.1 Proportionality {#51-proporcionalidade}

| Requirement | L1 | L2 | L3 |
|---|---|---|---|
| Guidelines documented per stack | Upstream rules without tailoring | Curated with documented tailoring | Curated + policy-as-code |
| Operationalisation as tool configuration | Recommended | Mandatory | Mandatory |
| Centralised and reusable configuration | Recommended | Mandatory | Mandatory |
| Deviations from the guideline recorded per project | Optional | Mandatory | Mandatory |

---

## 6. Review and publication cadence {#6-cadência-de-revisão-e-publicação}

| Level | Minimum review cadence |
|---|---|
| L1 | Annual or upon a major stack change |
| L2 | Quarterly or upon a major stack change |
| L3 | Continuous; formal quarterly review; automatic alerts for new upstream rules |

### 6.1 Triggers for an extraordinary review {#61-triggers-de-revisão-extraordinária}

In addition to the regular cadence, a stack's guideline must be reviewed whenever:

- A critical vulnerability is published that originates in a code pattern covered by the guideline
- A new major version of the language or framework with relevant security changes is adopted
- A SAST tool in use publishes rulesets with material changes
- A recurring vulnerability pattern that was not covered is identified in code reviews

### 6.2 Publication process {#62-processo-de-publicação}

Each new version of a guideline must follow the process:

1. Update of the document and tool configurations by the designated curator
2. Review by an AppSec Engineer (mandatory at L2/L3)
3. Review by Software Architects (mandatory at L2/L3)
4. Publication of a versioned release/tag in the central repository
5. Communication to the teams with a record of changes (changelog)

---

## 7. Project-level deviations {#7-desvios-a-nível-de-projeto}

Individual projects may disable recommended rules, but not mandatory rules. Every deviation must be recorded:

- [ ] Disabled rule identified (e.g. `semgrep-rule-id`)
- [ ] Documented technical justification (e.g. systematic false positive in the context of the project)
- [ ] Approval by an AppSec Engineer at L2/L3
- [ ] Record in the project's configuration file with an explicit comment (not just an inline suppression)

:::warning
Inline suppressions without reference to an approved deviation record (e.g. `# noqa`, `// nosec`, `// nolint` without context) are treated as non-compliance at L2/L3 and must be detected and reported by the pipeline.
:::

---

## 8. Responsibilities {#8-responsabilidades}

| Role | Responsibility |
|---|---|
| AppSec Engineer | Curate and maintain guidelines per stack; approve versions and deviations; select and configure SAST tools |
| Software Architect | Review guidelines for technical adequacy and architectural impact; approve versions |
| Developer | Apply the stack's guidelines; record justified deviations; not suppress rules without a formal record |
| Tech Lead | Ensure that the project references the correct version of the guidelines; review the team's deviations |
| DevOps / SRE | Integrate linter/SAST configurations into the pipeline; ensure that the pipeline references central configurations |

---

## 9. Review and audit of this policy {#9-revisão-e-auditoria-desta-política}

This policy must be **reviewed annually** or after any of the following events:

- Incident originating in a code pattern not covered by existing guidelines
- Adoption of a new technology stack by the organisation
- Significant change in the SAST tools used

---

## 10. Normative and technical references {#10-referências-normativas-e-técnicas}

| Reference | Relevance |
|---|---|
| SbD-ToE Ch. 06 - Secure Development | Curation of guidelines, operationalisation, L1-L3 proportionality |
| OWASP Secure Coding Practices | Secure development baseline |
| OWASP Cheat Sheet Series | References per language and framework |
| CWE Top 25 | Most critical implementation weaknesses |
| NIST SP 800-218 (SSDF) | Secure software framework by phase |
| Semgrep Registry | Reference rulesets for SAST |
| Code Review Policy (`15_policy-revisao-codigo.md`) | Application of guidelines in code review |
| Secure CI/CD Policy (`17_policy-cicd-seguro.md`) | Integration of linters/SAST into the pipeline |
