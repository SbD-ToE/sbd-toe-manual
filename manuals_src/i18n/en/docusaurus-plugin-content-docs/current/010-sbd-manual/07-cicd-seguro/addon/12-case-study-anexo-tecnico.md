---
id: case-study-anexo-tecnico
title: Technical Annex - Applying SbD-ToE to the CI/CD Pipeline
sidebar_position: 9
description: Formal rules for allowing exceptions in the pipeline, with registration, approval, expiry date and visibility by function.
tags: [exceções, visibilidade, cicd, governação, auditoria, segurança]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/addon/12-case-study-anexo-tecnico.md
  source_sha256: be89ee30f703350feb49cd055fe22f77e88c27e3642c5eb536f1dcb29ee0d196
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 7e6d99548714dbbda1c68f05fecdadc87f948a19dcc23caf13cc6ad535b577e1
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, cycle_iteration, framework_source_corpus, lifecycle_phase, maturity, practitioner_manual, provenance, sbdtoe_sbd, traceability, validation_evaluation]
  glossary_sha256: c5cffdaf18682625638385d3dde397a2b0d2e4ff5098327a7caa014c2621cf7c
  translated_at: 2026-09-26T09:09:18Z
  stamped_at: 2026-09-26T18:34:24Z
  reviewed_by: null
---


# Technical Annex - Applying SbD-ToE to the CI/CD Pipeline

This annex complements the case study on applying the SbD-ToE manual to the CI/CD pipeline as an L3 project, providing reusable technical and operational artefacts for engineering, security and governance teams.

---

## ✅ Validation Checkpoints by Phase {#-checkpoints-de-validação-por-fase}

| Phase          | Validation                           | Suggested tool         | SbD-ToE chapter         |
| ------------- | ----------------------------------- | --------------------------- | ------------------------ |
| Planning   | Documented threat modelling         | IriusRisk, Excel            | Ch. 03 - Threat Model   |
| Design        | L3 requirements assigned to the project | Catalogue of Ch. 02, 07     | Ch. 02, 07 - Requirements |
| Implementation | Linters, mandatory review        | Semgrep, ESLint, PRs        | Ch. 06 - Secure Dev     |
| Build         | SBOM generated for the pipeline         | `syft`, `cyclonedx`         | Ch. 05, 07              |
| Tests        | Security validations of the pipeline | `trivy`, `semgrep`, CI      | Ch. 07, Ch. 10         |
| Deploy        | Provenance and signing           | `cosign`, `slsa-provenance` | Ch. 07, 09              |
| Operations     | Logging, traceability, alerts   | AuditLogs, Kibana           | Ch. 12 - Monitoring and Operations  |

---

## 🧩 Relevant User Stories {#-user-stories-relevantes}

```markdown
**Como engenheiro de DevOps**,  

Quero que o pipeline da plataforma gere um SBOM próprio,  
Para garantir que todas as tasks, containers e SDKs usados estão inventariados e rastreados.

**Como responsável de segurança**,  

Quero aplicar threat modeling formal ao pipeline CI/CD,  
Para identificar vetores de ataque e definir controlos preventivos.

**Como gestor de conhecimento**,  

Quero que o processo de onboarding inclua formação sobre segurança do pipeline,  
Para garantir que todos os contribuidores compreendem o impacto da infraestrutura de entrega.

**Como auditor de segurança**,  

Quero validar se os runners utilizados estão isolados e corretamente configurados,  
Para mitigar riscos de execução maliciosa ou persistência de agentes externos.
```

---

## 📜 Applicable Requirements {#-requisitos-aplicáveis}

| ID         | Description                                                           | Applicable | Source       |
| ---------- | ------------------------------------------------------------------- | --------- | ----------- |
| REQ-L3-001 | The pipeline must have a versioned SBOM per build                       | ✔         | Ch. 05, 07 |
| REQ-L3-014 | The runner used must be segregated by function                        | ✔         | Ch. 09     |
| REQ-L3-019 | The pipeline tasks must be analysed for vulnerabilities | ✔         | Ch. 05, 07 |
| REQ-L3-027 | Every change to the pipeline must go through review                  | ✔         | Ch. 06     |
| REQ-L3-038 | The pipeline must be subject to explicit threat modelling             | ✔         | Ch. 03, 07 |
| REQ-L3-045 | The pipeline must undergo automated security testing        | ✔         | Ch. 07, 10 |
| REQ-L3-048 | There must be logging and traceability of runs                 | ✔         | Ch. 12     |
| REQ-L3-052 | Training of teams on CI/CD security                        | ✔         | Ch. 13     |

---

## 📋 Operational Checklist {#-checklist-operacional}

| Item                                                              | Yes/No |
| ----------------------------------------------------------------- | ------- |
| Has the pipeline been formally classified as an L3 asset?            |         |
| Is there a documented threat model, reviewed periodically?         |         |
| Are the runners used segregated and controlled?                   |         |
| Does the pipeline itself have a generated and signed SBOM?                    |         |
| Are the tasks used (e.g. GitHub Actions, SDKs) inventoried?     |         |
| Are the pipeline dependencies subject to SCA analysis?           |         |
| Is the `ci-pipeline.yml` versioned and subject to mandatory review?       |         |
| Have secure development practices been applied to the pipeline?   |         |
| Is there a formal exception and review process for bypasses?        |         |
| Has training on secure CI/CD been delivered to the relevant teams? |         |
| Have security tests been applied to the pipeline?                  |         |
| Is end-to-end traceability ensured (build → deploy)?   |         |

---

## ✅ Final Considerations {#-considerações-finais}

This annex translates the narrative prescription of the case study into concrete and auditable technical elements, promoting the **effective and traceable adoption** of SbD-ToE in the lifecycle of the pipelines themselves.

> 📌 The pipeline is a critical asset. Treating its lifecycle like that of any other L3 product is a fundamental step towards maturity in supply chain security.
