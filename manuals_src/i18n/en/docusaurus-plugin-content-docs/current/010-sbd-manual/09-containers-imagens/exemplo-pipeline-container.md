---
id: exemplo-pipeline-container
title: Practical Case - Containerised Pipeline with Secure Execution
description: Complete example of a CI/CD pipeline with execution of *containers* in a secure and validated environment
tags: [exemplo, pipeline, containers, cicd, segurança, execucao]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/exemplo-pipeline-container.md
  source_sha256: d59d6ba443cf9c121159cd4b084c6ef5e686437ab20f922015debf088a10ebd4
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 7596649b76d079b0fecc3d06ea960590222f9d1ceaa8711c43120e25aa2b20b3
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 6163399f3326e10bced3afe0b9ddfa197cae2c643b2beeb28c226f7164a47a99
  glossary_keys: [audit_trail, chapter_role, cycle_iteration, discipline, lifecycle_phase, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: d67e5693fd05335bd5c291314dd57c07488698842bdb384d1f418d5108307257
  translated_at: 2026-09-26T09:58:23Z
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
| SBOM generation               | `syft . -o cyclonedx-json > .sbom/container.json` | `06-sbom-containers.md`               |
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
