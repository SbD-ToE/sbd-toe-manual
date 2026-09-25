---
id: threat-modeling-ci
title: Threat Modelling in CI/CD
description: Requirements and practical validations to ensure the existence, integrity and impact of threat modelling in the CI/CD lifecycle
tags: [ci, cd, devsecops, threat modeling, automação, validação, iriusrisk]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/addon/06-threat-modeling-ci.md
  source_sha256: 6a0fa96ea28bb61616e01b81e34d307e4395aea33ee79fcc3702fddfd04dd774
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: ba52b35580323844f245c2083bb9e0b2f0f36137153781b07ec3e967bf8c4be5
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [como_fazer, cycle_iteration, lifecycle_phase, mapping, practitioner_manual, requirement_runtime, sbdtoe_sbd, threat, traceability, validation_evaluation]
  glossary_sha256: d2b4127984478fba3f7bc64ac5026915dcbbe446bc490a193bc4726626d694ca
  translated_at: 2026-09-25T20:16:59Z
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
| Last review of the model carried out within the last 30 days              | ☑️         |

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
| Model outdated (> 30 days)              | ⚠️ Alert + conditional block  |
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
