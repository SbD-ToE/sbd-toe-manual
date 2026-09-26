---
id: exemplo-pipeline-container
title: Practical Case - Containerised Pipeline with Secure Execution
description: Complete example of a CI/CD pipeline with execution of *containers* in a secure and validated environment
tags: [exemplo, pipeline, containers, cicd, segurança, execucao]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/exemplo-pipeline-container.md
  source_sha256: 4b8f645969d06cca95766eae10eebbd0ec1db1c133d1a9728312ce2a56354f78
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: 983b6ae77aec4b9a327f885d283647fa4000458167adec1c5feafd9d4535d714
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, discipline, lifecycle_phase, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: dbac74bb410ff717defffcf21d0a994bddd846448839af4906e80581963f225b
  translated_at: 2026-09-26T12:48:49Z
  stamped_at: 2026-09-26T18:35:00Z
  reviewed_by: null
---

# Practical Case - Containerised Pipeline with Secure Execution

This example illustrates the practical application of the prescriptions of Chapter 09 - from the secure building of the base image to its controlled execution in a CI/CD pipeline and in Kubernetes.

The pipeline in question is responsible for **compiling, testing, signing and publishing a Node.js microservice**, with **100% containerised** execution aligned with the practices of SbD-ToE.

---

## 📦 Pipeline structure {#-estrutura-da-pipeline}

```text
.
├── /.github/workflows/build.yml
├── /Dockerfile
├── /.sbom/
├── /k8s/deployment.yaml
└── /policies/
```

---

## 🔐 Main steps implemented {#-passos-principais-implementados}

| Step                         | Actual implementation                           | Associated documentation                    |
|-------------------------------|-----------------------------------------------|-------------------------------------------|
| Secure base image            | `FROM node:18.17.0-alpine` + `USER node`      | `01-imagens-base.md`                      |
| Image signing          | `cosign sign` with GitHub OIDC                | `03-assinatura-cadeia-trust.md`           |
| SBOM generation               | `syft . -o cyclonedx-json > .sbom/container.json` | `06-inventario-sbom.md`               |
| Vulnerability scanner   | `trivy image` with blocking on CVSS > 7       | `07-vulnerabilidades-imagens.md`          |
| Isolated runners              | `runs-on: [self-hosted, ephemeral]`           | `02-runners-isolamento.md`                |
| Execution with enforcement      | Kyverno `validate` for labels, UID, origin   | `05-policies-runtime-opa.md`              |
| Controlled deploy on K8s      | Pod with `securityContext` and PSA: `restricted` | `08-kubernetes-execucao.md`               |

---

## 📜 Summarised example of the pipeline (GitHub Actions) {#-exemplo-resumido-do-pipeline-github-actions}

```yaml
jobs:
  build-and-push:
    runs-on: [self-hosted, hardened]
    steps:
      - uses: actions/checkout@v3
      - name: Build Docker image
        run: docker build -t registry/project/app:1.0.0 .
      - name: Generate SBOM
        run: syft docker:registry/project/app:1.0.0 -o cyclonedx-json > sbom.json
      - name: Scan for CVEs
        run: trivy image --exit-code 1 --severity HIGH registry/project/app:1.0.0
      - name: Sign image
        run: cosign sign --key env://COSIGN_KEY registry/project/app:1.0.0
      - name: Push image
        run: docker push registry/project/app:1.0.0
```

---

## ☸️ Controlled execution in Kubernetes {#️-execução-controlada-no-kubernetes}

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    app: microservico
    sbom: "true"
spec:
  securityContext:
    runAsNonRoot: true
    readOnlyRootFilesystem: true
    allowPrivilegeEscalation: false
  containers:
    - name: app
      image: registry/project/app:1.0.0
      ports: [ { containerPort: 3000 } ]
```

> 🔐 This pod will only be accepted in clusters with Pod Security Admission (`restricted`) + Kyverno policies validating origin and UID.

---

## ✅ Results obtained {#-resultados-obtidos}

- Pipeline execution that is **100% traceable** and aligned with policies;
- Final image with **SBOM, CVE scan and verifiable signature**;
- Deploy to Kubernetes with security enforcement at admission;
- Auditable, versioned process that can be reapplied to other projects.

---

## 🧹 Lessons learned {#-lições-aprendidas}

- The use of *containers* requires discipline and continuous automation;
- Enforcement at runtime is as important as the secure build;
- The validation of the image's origin and content must be done *before* execution - not after;
- A clear separation between build, validation and execution significantly reduces the attack surface.

---

## 📎 Cross-references {#-referências-cruzadas}

- Chapter 07 - `addon/10-sbd-no-proprio-pipeline.md`
- Chapter 05 - `06-validacao-dependencias.md`
- Chapter 10 - `intro.md` (tests of containerised execution)

> ✅ This example shows how to apply the practices of SbD-ToE to the complete lifecycle of containerised execution, in an integrated and realistic way.
