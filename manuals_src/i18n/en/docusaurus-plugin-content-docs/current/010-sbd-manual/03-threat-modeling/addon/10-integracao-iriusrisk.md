---
id: integracao-iriusrisk
title: Integration with IriusRisk and Automated Tools
description: How to replace the manual threat → requirement mapping using platforms such as IriusRisk, while maintaining traceability with Chapter 2
tags: [iriusrisk, integração, ameaças, requisitos, rastreabilidade, capitulo2]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/addon/10-integracao-iriusrisk.md
  source_sha256: 24cdd7aefc36d1125ce429ec3ea90ca957b10fcc4674b1aa148039a3c9f1496a
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: b9cea7630b67f0ae5660152038e069f8dee40894c47917cd3af21ab36e6964d5
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, cycle_iteration, lifecycle_phase, mapping, practitioner_manual, requirement_runtime, sbdtoe_sbd, slug_threat_modeling, threat, traceability, validation_evaluation]
  glossary_sha256: 56a493b25f3fb8fa5859175ddaedd2683fdfed3d454477f88ed3277477a73aba
  translated_at: 2026-09-25T20:17:00Z
  stamped_at: 2026-09-26T18:33:20Z
  reviewed_by: null
---

# Integration with IriusRisk and Automated Tools

## 🌟 Objective {#-objetivo}

Demonstrate how to apply the normative principles of this chapter using **automated Threat Modelling platforms**, such as **IriusRisk**, replacing the manual files and maintaining traceability with the requirements defined in **Chapter 2 - Security Requirements**.

This integration aims to:

- Automate the threat → requirement → control mapping;
- Eliminate the need for manual files (`yaml`, `md`, `csv`);
- Enable continuous validation via CI/CD, maintaining coherence with the SbD-ToE model.

---

## 🧭 What the tool replaces {#-o-que-é-substituído-pela-ferramenta}

| Manual file (local model) | Equivalent in IriusRisk                                    |
| ------------------------------ | ----------------------------------------------------------- |
| `threats.yaml`                 | Threats generated automatically from templates               |
| `requisitos.yaml`              | Security Requirements assigned per threat                 |
| `mitigations.md`               | List of controls with status (implemented / planned / n/a) |
| `decisions.md`                 | Risk Decisions documented with justification and date         |
| `mapeamento.md`                | Export of threat → requirement → control mappings        |

---

## 🔗 Link with Chapter 2 - Security Requirements {#-ligação-com-o-capítulo-2---requisitos-de-segurança}

To maintain consistency and traceability, the requirements defined in IriusRisk must:

- Reference the **same requirement codes as Ch. 2**, e.g. `AUT-003`, `ACC-010`;
- Be classified in the same **functional category** (authentication, access control, privacy);
- Have an associated criticality (low / medium / high) according to the risk context;
- Indicate the **current status** of the implementation.

### Example of correspondence: {#exemplo-de-correspondência}

| Threat (IriusRisk)               | Derived requirement (Ch. 2)           | Status       |
| -------------------------------- | ------------------------------------- | ------------ |
| Unsigned JWT token           | `EX-AUT-003`: Mandatory signature | Implemented |
| Endpoint `/admin/config` exposed | `EX-AC-010`: Mandatory RBAC        | In progress     |
| Excessive claims in the JWT         | `EX-DAT-005`: Minimal claims         | Justified  |

*Illustrative identifiers (`EX-…`); they do not correspond to the Requirements Catalogue of Ch. 02.*

---

## 📁 Export structure in the project {#-estrutura-de-exportação-no-projeto}

```
📁 threat-model/
├── iriusrisk-export/
│   ├── threats.json         # Lista de ameaças exportadas via API
│   ├── requirements.csv     # Requisitos de segurança atribuídos por ameaça
│   ├── controls.csv         # Estado de controlos aplicados
│   ├── decisions.csv        # Justificações de risco
├── threat-model.yml         # Metadados (última sincronização, projeto, versão)
```

---

## 🛠️ How to apply with IriusRisk in CI/CD {#️-como-aplicar-com-iriusrisk-no-cicd}

The pipeline may include validations such as:

- Checking that all threats with high criticality have:
  - a control applied **OR**
  - a documented justification;
- Confirming that Ch. 2 requirements with `estado != implemented` have an associated ticket;
- Exporting a summary report with the percentage of threats covered.

### Example (bash pseudocode): {#exemplo-pseudocódigo-bash}

```bash
# Verifica se há threats sem mitigação nem justificação

cat threats.json | jq '.[] | select(.criticality == "High")' |
  while read threat; do
    REQ=$(jq '.requirement_id' <<< "$threat")
    STATUS=$(grep $REQ requirements.csv | cut -d',' -f3)
    if [[ "$STATUS" != "Implemented" && "$STATUS" != "Justified" ]]; then
      echo "❌ Ameaça $REQ sem controlo válido"
      exit 1
    fi
  done
```

---

## ✅ Benefits of the Integration {#-benefícios-da-integração}

| Benefit                          | Impact                                                   |
| ---------------------------------- | --------------------------------------------------------- |
| Eliminates manual files          | Reduces the risk of outdated information, increases reliability     |
| Maintains a direct link to requirements | Facilitates audits and cross-validation with Ch. 2        |
| Enables validation in CI/CD         | Automates security by design as a release requirement |
| Supports formal risk decisions  | Justifications with owner, date and context            |

---

## ✅ Good practices {#-boas-práticas}

- Reuse the threat and requirement templates offered by the tool;
- Keep naming and requirement codes synchronised with Chapter 2;
- Include the automatic export in CI/CD for continuous auditing;
- Use the tool's dashboards to measure coverage and status;
- Validate exports with local scripts and integrate with the backlog.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                        | Relation to this file                                 |
|----------------------------------|-----------------------------------------------------------|
| `addon/07-mapeamento-threats-requisitos.md` | Manual alternative to the mapping between threats and requirements |
| `addon/06-threat-modeling-ci.md` | Validation of threat modelling in CI/CD pipelines           |
| `25-rastreabilidade.md`    | Formal traceability with frameworks and requirements         |
| `15-aplicacao-lifecycle.md`| Integration with the project lifecycle                 |

---

> The adoption of tools such as IriusRisk must be accompanied by processes that guarantee coherence with the taxonomy and security requirements defined in the SbD-ToE manual. The tool **does not replace** the responsibility for traceability - it only systematises and automates it.
