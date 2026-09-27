---
id: threat-modeling-ci
title: Threat Modelling in CI/CD
description: Requirements and practical validations to ensure the existence, integrity and impact of threat modelling in the CI/CD lifecycle
tags: [ci, cd, devsecops, threat modeling, automação, validação, iriusrisk]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/addon/06-threat-modeling-ci.md
  source_sha256: e06fdc32a00904115d7086397454fc1be8e11291792e4b8e8af1f9bf5dd90016
  source_commit: 036d74010f423f247be988e4a417375c74edb9d9
  target_sha256: adc1b410aa9a24048c1996e144f71b23feb7de6993420c4fd09a49402a533465
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [como_fazer, cycle_iteration, lifecycle_phase, mapping, practitioner_manual, requirement_runtime, sbdtoe_sbd, threat, traceability, validation_evaluation]
  glossary_sha256: ab801d496384b679b03c1ad3c038b6b1d1ba3c5f559337976bbc75fad4a59ad1
  translated_at: 2026-09-27T07:53:39Z
  stamped_at: 2026-09-27T07:53:39Z
  reviewed_by: null
---

# Threat Modelling in CI/CD

## 🌟 Objective {#-objetivo}

To define how to ensure - in a testable and automatable way - that the *threat modelling* activity:

- Has been carried out and is up to date;
- Has produced traceable artefacts that are useful to the project;
- Has influenced real decisions and security controls;
- Is integrated into the lifecycle via CI/CD;
- Meets the requirements of frameworks such as NIST SSDF, SAMM or SLSA.

---

## 📌 Minimum requirements per project {#-requisitos-mínimos-por-projeto}

The presence of threat modelling cannot be merely symbolic: it must result in **traceable artefacts, effective controls and measurable validations**.

| Mandatory element                           | Description                                                                 |
| ---------------------------------------------- | ------------------------------------------------------------------------- |
| Versioned threat model                    | DFD diagram (`dfd.drawio`, `dfd.mmd`), threat list (`threats.yaml`) |
| Threat → requirement → control mapping       | `mitigations.md` file with status and cross-reference                 |
| Documented justifications for accepted risks | `decisions.md` file with date, author and reason for acceptance               |
| Traceability in the backlog or code           | Identifiers such as `TM-001` or `ACC-003` referenced in PRs/issues |
| Date of last review                         | `last_reviewed` field in a `threat-model.yml` file                     |

---

## 🧲 How to validate in the pipeline (CI/CD) {#-como-validar-no-pipeline-cicd}

The CI/CD pipeline must verify not only that the files are present, but also whether they:

- Are up to date with respect to changes in the code;
- Were used as the basis for development decisions;
- Generated related tickets, commits or tests.

| Stage           | Recommended validation                                                |
| --------------- | -------------------------------------------------------------------- |
| `pre-commit`    | Mandatory files exist (`dfd`, `threats.yaml`)               |
| `build`         | Linting of the models (`yaml`, `mermaid`), parsing of `mitigations.md` |
| `security test` | Threat → control link exists (or has a justification)               |
| `release`       | Last review has been carried out + critical threats have defined plans |

---

## ✅ Minimum compliance CI/CD checklist {#-checklist-cicd-de-conformidade-mínima}

| Item                                                                | Verified |
| ------------------------------------------------------------------- | ---------- |
| `/threat-model/` structure present in the repository                  | ☑️         |
| Main files exist (`dfd`, `threats.yaml`, `mitigations`) | ☑️         |
| `mitigations.md` or `yaml` file has a defined state per threat  | ☑️         |
| `decisions.md` documents accepted risks with date + justification     | ☑️         |
| Commits or issues reference threats (`TM-001`, etc.)              | ☑️         |
| Model reviewed within the cadence of Policy 08 and ≤ 30 days after the latest architectural change | ☑️         |

---

## 📂 Suggested structure of the model {#-estrutura-sugerida-do-modelo}

```
📁 threat-model/
📌 README.md              # âmbito e método
📌 dfd.drawio             # Diagrama técnico ou .mmd (Mermaid)
📌 threats.yaml           # Lista de ameaças (id, descrição, severidade, requisito associado)
📌 mitigations.md         # Tabela com status (mitigado, em curso, aceite)
📌 decisions.md           # Justificações de risco aceite
📌 threat-model.yml       # Metadados: última revisão, revisores, etc.
```

---

## 🛠️ Practical examples and automated validations {#️-exemplos-práticos-e-validações-automatizadas}

### Artefact linting: {#linting-de-artefactos}

```yaml
- name: Verificar syntax YAML
  run: yamllint threat-model/threats.yaml
```

### Cross-reference validation: {#validação-de-referências-cruzadas}

```bash
grep -E 'TM-[0-9]{3}' threat-model/mitigations.md \
  | while read threat_id; do
    git log --oneline | grep "$threat_id" || echo "❌ Threat $threat_id sem commit associado"
  done
```

### Checking the last review: {#verificar-última-revisão}

```bash
REVIEWED=$(yq '.last_reviewed' threat-model/threat-model.yml)
if [ "$REVIEWED" < "$(date -d '30 days ago' +%F)" ]; then
  echo "❌ Threat model desatualizado"; exit 1;
fi
```

---

## 🔄 Integration with IriusRisk {#-integração-com-iriusrisk}

### 🧠 What IriusRisk can do automatically: {#-o-que-iriusrisk-pode-fazer-automaticamente}

| Capability                              | Detail                                               |
| --------------------------------------- | ----------------------------------------------------- |
| Derive threats based on components | Templates model threats by type (e.g. JWT, API, S3) |
| Generate requirements and controls            | Automatic, with criticality and state                  |
| Export data via API                  | JSON/YAML for integration with CI/CD                   |
| Create tickets in Jira / ADO             | Integration with backlog flows                      |

### 🧲 What still needs to be verified in CI/CD: {#-o-que-ainda-precisa-ser-verificado-no-cicd}

| Required validation                         | How to Do It                                                 |
| -------------------------------------------- | ---------------------------------------------------------- |
| Do the exported threats have a control applied? | Scripts cross-check IDs against code, PRs or tests               |
| Are the justifications documented?        | `decisions.md` extracted from IriusRisk or maintained locally |
| Was the review recent?                       | Check metadata or synchronisation via API               |

---

## ⚠️ Expected pipeline behaviour {#️-comportamento-esperado-da-pipeline}

| Type of failure                                 | Recommended pipeline reaction    |
| --------------------------------------------- | --------------------------------- |
| Model missing                            | ❌ Critical failure                   |
| Outdated model (> 30 days after an architectural change, or outside the cadence of Policy 08) | ⚠️ Alert + conditional block  |
| Threats neither mitigated nor justified        | ⚠️ Warning + requires issue/document |
| Linting fails (invalid YAML, Mermaid)        | ❌ Build fails                     |
| No link between threat and code/backlog | ⚠️ Alert for manual review     |

---

## ✅ Good practices {#-boas-práticas}

- Treat threat modelling as a **mandatory, verifiable artefact**;
- Ensure traceability between threat, control, requirement and backlog;
- Automate freshness and coverage validations in the pipeline;
- Integrate results with risk management tools (e.g. IriusRisk);
- Include references to threats in relevant commits, issues and PRs.

---

## 🛍️ Final considerations {#️-considerações-finais}

The objective of CI/CD is not merely to **detect the presence of the model**, but to **confirm its real impact on the project**.
This impact manifests itself in:

- Documented decisions;
- Implemented mitigations;
- Derived requirements;
- Risks accepted with accountability.

> This approach reinforces traceability and provides concrete evidence of compliance with *Security by Design* through threat modelling.
