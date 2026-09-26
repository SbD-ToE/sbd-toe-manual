---
id: rastreabilidade-vulnerabilidades
title: Traceability between Vulnerabilities, Components and Actions
description: Model linking SCA findings, SBOM, backlog and releases
tags: [dependencias, sbom, sca, supply-chain, rastreabilidade]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/addon/08-rastreabilidade-vulnerabilidades.md
  source_sha256: 6706802651508e8987263a1fe412340c5e8fe670894e7ebe4a5de55dab415130
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: b3c7bbc7adc3ff61ffa3878c7061b665ecb2f2429af4d1691662eede87375c01
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 0594036caa5df5f000ba40e62fe5e20f348d76f6f2035281e833391c2c9abd3a
  glossary_keys: [framework_source_corpus, traceability, validation_evaluation]
  glossary_sha256: 83d00d60612bab4550210f0e2f7b28627b8ef20385c7d37aee2ea56d623bee1f
  translated_at: 2026-09-26T08:45:26Z
  reviewed_by: null
---

# Traceability between Vulnerabilities, Components and Actions

## 🌟 Objective {#-objetivo}

Ensure that each vulnerability identified in third-party components has **complete traceability** from its origin (SBOM + SCA), through analysis, to remediation or documented acceptance.

> ✅ This traceability makes it possible to demonstrate compliance, mitigate risks in a justified way, and maintain control over the real security state of the dependencies.

---

## 🔢 Elements of traceability {#-elementos-da-rastreabilidade}

| Element                 | Example                                      |
|--------------------------|----------------------------------------------|
| **Component**           | `log4j:log4j-core@2.14.1`                     |
| **SBOM identifier**   | `purl:maven/log4j/log4j-core@2.14.1`         |
| **Finding / CVE**        | `CVE-2021-44228`                             |
| **Scanner / Report**  | `grype`, `snyk`, `OWASP DC`, etc.            |
| **Affected artefact**    | `app-backend-1.2.5.jar`                      |
| **Origin commit**     | `abc123` (pull request where the dep was used) |
| **Associated task**     | `EX-SEC-456` (issue, PR or remediation task)  |
| **Final state**         | Fixed / Accepted with justification         |

*Illustrative identifiers (`EX-…`); they do not correspond to the Requirements Catalogue of Ch. 02.*

---

## 📄 Record template {#-template-de-registo}

```yaml
# Identificadores ilustrativos (EX-…); não correspondem ao Catálogo de Requisitos do Cap. 02.
- cve: CVE-2021-44228
  componente: log4j-core@2.14.1
  purl: pkg:maven/log4j/log4j-core@2.14.1
  artefacto: app-v1.2.5.jar
  introduzido_por: commit abc123
  tarefa: EX-SEC-456
  decisao: corrigido
  evidencias:
    - commit: def789
    - release: v1.2.6
    - scanner: grype-scan-2024-06-02.json
```

> 📁 It is suggested that this record be kept in a versioned file (`vulns.yaml`) or in a database integrated with Jira or GitHub Projects.

---

## 🛠️ Integration with ALM / backlog {#️-integração-com-alm--backlog}

- SCA findings must **automatically create remediation tasks** (via API or webhook)
- Tickets must contain:
  - Link to the CVE (NVD, GH Advisory)
  - Affected components
  - SBOM + affected pipeline
  - Acceptance criterion (validated fix or approved exception)

> 🔗 Use normalised labels: `cve`, `sca`, `seguranca`, `sbom`, `rastreabilidade`

---

## ✅ Finding closure criteria {#-critérios-de-conclusão-de-finding}

| Final state        | Mandatory requirements                                  |
|---------------------|-------------------------------------------------------------|
| **Fixed**       | PR with the update, new release validated by SCA                |
| **Accepted**          | Technical justification + AppSec/documented approval        |
| **Mitigated**        | Compensating control + technical validation + defined deadline  |
| **Obsolete**        | Package no longer in use (excluded from the current SBOM)         |

---

## 🔗 Links to other files {#-ligações-com-outros-ficheiros}

| Document                   | Role in traceability                          |
|-----------------------------|---------------------------------------------------------|
| `01-inventario-sbom.md`     | Source of components by version                        |
| `02-analise-sca.md`         | Generates findings with references to CVEs                   |
| `04-integracao-ci-cd.md`    | Connects findings to the artefact and release                 |
| `09-excecoes-e-aceitacao-risco.md` | Formalises acceptance of findings if they are not fixed |

---

> 🔒 Traceability is a critical factor in audits, incident response and security governance. It must be systematised, versioned and accessible.
