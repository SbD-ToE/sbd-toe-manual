---
id: validacao-continuada
title: Continuous Governance Validation
sidebar_position: 6
description: Strategies and cycles for keeping validations, KPIs and exceptions auditable
tags: [validacao, excecoes, auditoria, ciclo-continuo]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/addon/06-validacao-continuada.md
  source_sha256: 7b45d5f7718668baf214b9050c0ed4b2f74894c914f7cb7f9bd021380b1c985b
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 195b09469f3fa87ade52c751a76c46e867c9049a3917fd9939f6fd5abbe6e97b
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [cycle_iteration, lifecycle_phase, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: 0da2c8bc3c92bf62222625f5f05deb6d78e72225f5e0cee733c6eca7b1ab43e7
  translated_at: 2026-09-26T12:00:15Z
  reviewed_by: null
---

# Continuous Validation and Reviews

This annex describes the mechanisms for recurring validation of applications, suppliers and contracts, so as to ensure that the requirements remain applied, effective and correctly governed over time.

Continuous validation guarantees not only the execution of the defined controls, but also that the authority delegated to processes, contracts and technical mechanisms remains explicit, adequate and revocable.

---

## ⏳ 1. Suggested review periodicity {#-1-periodicidade-de-revisão-sugerida}

| Asset type            | Suggested frequency            | Primary responsible         |
| ------------------------ | ------------------------------ | ---------------------------- |
| Critical applications (L3) | Quarterly or per release      | AppSec + Application manager |
| L2 applications            | Half-yearly or every 2 releases | AppSec + Dev Lead            |
| External suppliers    | Annually or per renewal    | Procurement + AppSec         |
| Active contracts         | Annually or per amendment   | Legal + Functional manager     |

> 🔹 Frequencies must be adjusted on the basis of incidents, findings, changes of risk or relevant changes to automated processes that execute security validations, approvals or controls.

---

## 🔢 2. Items to validate per cycle {#-2-itens-a-validar-por-ciclo}

Beyond the technical and contractual verification, each validation cycle must confirm that the governance assumptions remain valid:

* Does the risk classification of the application or service still hold?
* Do the requirements applied remain valid and effective?
* Has any control stopped working (e.g. bypass, deactivation or silent change)?
* Does the evidence remain accessible, legible and traceable?
* Are there new exceptions or compensations to approve or renew?
* Does the supplier continue to meet the agreed SLA and security requirements?
* Are there automated processes or mechanisms that have started executing validations, blocks or approvals not previously framed in the defined governance model?
* Does the delegation of execution to technical processes remain aligned with the assigned organisational authority?

---

## 🌎 3. Integration with tools {#-3-integração-com-ferramentas}

The continuous validation process may be automated or supported by tools that allow consistent execution and traceable evidence, such as:

* Jira (cyclical review tasks per application or contract);
* SharePoint / Confluence (review forms or records);
* Git (labels, issues or workflows per release);
* SIEM or dashboards with findings and validation results.

> 💡 Preference should be given to tools that support an audit trail, change history and dated recording, making it possible to identify when automated processes were introduced, changed or deactivated.

---

## 📊 4. Example of an annual review plan {#-4-exemplo-de-plano-de-revisão-anual}

**Plan:** Annual review of the contracts and integrations of the finance unit

**Steps:**

1. Export the list of applications classified as L2/L3
2. Validate for each one:
   * Requirements applied
   * Evidence of tests or validation
   * SBOM and supplier compliance
   * Active automated processes with an impact on security or governance
3. Collect active exceptions, associated decisions and deadlines
4. Report deviations, changes of authority and corrective actions

---

## ✅ Final recommendations {#-recomendações-finais}

* Integrate reviews with the release cycle or with internal oversight mechanisms;
* Create alerts for expired or non-revalidated exceptions;
* Use this process to feed the governance KPIs (see `addon/kpis-governanca.md`);
* Treat recurring validation as an integral part of the security lifecycle;
* Use continuous validation as a mechanism for detecting implicit delegations of authority to processes or systems, ensuring their review or revocation when necessary.

---

## 🔗 Cross-links {#-ligações-cruzadas}

* Ch. 1 - Review of the risk classification (`addon/15-aplicacao-lifecycle.md`)
* Ch. 2 - Requirements checklist per project
* `addon/03-modelo-validacao-fornecedores.md` - Supplier onboarding and validation
* `addon/04-rastreabilidade-organizacional.md` - Organisational traceability
* `addon/05-exemplos-praticos.md` - Examples of decisions and exceptions
