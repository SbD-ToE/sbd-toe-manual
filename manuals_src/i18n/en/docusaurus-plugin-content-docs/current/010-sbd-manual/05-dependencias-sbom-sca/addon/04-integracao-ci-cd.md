---
id: integracao-ci-cd
title: Integration with CI/CD Pipelines
description: Automated integration of SBOM, SCA and exception control into the build and release cycle
tags: [dependencias, sbom, sca, supply-chain, ci-cd]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/addon/04-integracao-ci-cd.md
  source_sha256: 9f189906dd7e6d15450525e6c023bd8acca3bf4b499060d6a59ead9aa5712366
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 02ee6bc351a3b2169291fd730a7822bb0f96a86a3663b4c9a2c60cdaf182386c
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [cycle_iteration, framework_source_corpus, lifecycle_phase, traceability, validation_evaluation]
  glossary_sha256: 7d055735da51ec2e2c8a2c3b7d4faeee5e2da88e5eac02a0d9f3de3e164db7f7
  translated_at: 2026-09-26T08:45:24Z
  stamped_at: 2026-09-26T18:33:48Z
  reviewed_by: null
---

# Integration with CI/CD Pipelines

## 🌟 Objective {#-objetivo}

Guarantee that SBOM, SCA and dependency governance practices are applied in an **automated and traceable** way in the applications' build, test and release pipelines.

> 🚀 Automating these practices ensures consistent application, early detection of risks and controlled blocking of releases with serious findings.

---

## 🛠️ Expected actions in CI/CD pipelines {#️-ações-esperadas-em-pipelines-cicd}

| CI/CD Phase        | Expected action                                           | Result                              |
|-------------------|---------------------------------------------------------------|----------------------------------------|
| Build             | Automatic generation of the SBOM (e.g. Syft, CycloneDX)           | Versioned `.json` or `.xml` artefact |
| Security analysis | Execution of SCA with an open source or commercial scanner       | Findings report (SARIF/JSON/HTML) |
| Validation         | Checks the severity of findings and applies policies         | Blocker or warning + record              |
| Release           | Attaches the SBOM and findings to the final artefact                     | Traceability per version            |

---

## 💡 Integration examples (pseudocode) {#-exemplos-de-integração-pseudocódigo}

```yaml
steps:
  - name: Generate SBOM
    run: syft . -o cyclonedx-json > sbom.json

  - name: Run SCA
    run: grype sbom:sbom.json -o sarif > results.sarif

  - name: Validate findings
    run: ./scripts/validate-findings.sh results.sarif
```

> Can be integrated into GitHub Actions, Azure DevOps, GitLab CI, Jenkins, etc.

---

## 🔐 Blocking policies (examples) {#-políticas-de-bloqueio-exemplos}

| Criterion                              | Action              |
|----------------------------------------|----------------------|
| CVSS >= 9.0 and not mitigated             | Blocks the pipeline    |
| Vulnerability with a known exploit | Requires formal approval |
| "Medium" finding with a patch available | Generates a warning + task  |

> The rules may be maintained in a versioned file (`policy.yaml`) or in a central system.

---

## 🔧 Integration with the backlog and traceability {#-integração-com-backlog-e-rastreabilidade}

- Findings must automatically generate:
  - A task in Jira/Azure DevOps
  - An association with the commit/PR
  - A cross-reference to the SBOM and the release artefact

> 📄 The use of formats such as SARIF is suggested, to allow automatic import by IDEs and ALM platforms.

---

## 🔒 Recommended practices by risk {#-práticas-recomendadas-por-risco}

| Application risk | Mandatory CI/CD practice                                |
|---------------------|-------------------------------------------------------------|
| L1 (low)          | SBOM generation + lightweight SCA (e.g. `npm audit`)              |
| L2 (medium)          | Formal SCA + blocking of critical findings                 |
| L3 (high)        | Complete SBOM, automated SCA, recording and approval of exceptions |

---

## 🔗 Links to other files {#-ligações-com-outros-ficheiros}

| Document                   | Relationship with the pipeline                              |
|-----------------------------|---------------------------------------------------------|
| `01-inventario-sbom.md`     | Mandatory input source                            |
| `02-analise-sca.md`         | Integrated scanner and validation                       |
| `09-excecoes-e-aceitacao-risco.md` | Control of findings with documented justification |

---

> 🚀 Integrating SBOM and SCA into pipelines is the bridge between theory and execution. It ensures that the policies defined by the security team are effectively applied, auditable and repeatable.
