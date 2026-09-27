---

id: kubernetes-execucao
title: Secure Execution of Containers in Kubernetes Clusters
description: Effective application and verification of security, isolation and control practices for containerised workloads
tags: [kubernetes, containers, execucao-segura, isolamento, runtime, seguranca]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/addon/08-kubernetes-execucao.md
  source_sha256: 41866be4b7002e988c5083eb47c2f6a837c8cf833ac971800f8ff440443b1e45
  source_commit: 4430e7c4ca4536589773f3f465bd05857a1e6c38
  target_sha256: eae7d0259b70fc96a8e8c2bd7232705ae3d97b44fe4400df8b215835df2f35a7
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [sbdtoe_sbd, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: d14d9e9ca72dbd8bb75594f51d6c09de77e0653f04f890656226cb4fa42e60de
  translated_at: 2026-09-26T09:58:18Z
  stamped_at: 2026-09-26T18:34:53Z
  reviewed_by: null
---

# ☸️ Secure Execution of Containers in Kubernetes Clusters

## 🌟 Objective {#-objetivo}

Ensure that the **execution of containers in Kubernetes environments** - applications, pipelines, sidecars or agents - takes place with **explicit restrictions, technical enforcement and verifiable evidence**, reducing risks such as:

* Execution with excessive privileges;
* Escalation of permissions at node level;
* Undue access to secrets, volumes or the network;
* Executions outside the organisational baseline.

Kubernetes provides **mechanisms**, not guarantees.
Execution security depends on **correct configuration, active enforcement and continuous verification**.

---

## 🧬 What secure execution in Kubernetes means (in SbD-ToE) {#-o-que-significa-execução-segura-em-kubernetes-no-sbd-toe}

In the SbD-ToE model, running containers securely in Kubernetes implies:

* **Declaring execution restrictions** (`securityContext`, PSA);
* **Imposing those restrictions technically** (admission control);
* **Verifying that the real state of the pod matches what is expected**;
* **Maintaining traceability between decision, configuration and execution**.

> ⚠️ A pod may be accepted by the cluster and still violate security expectations if the effective state is not verified.

---

## ⚠️ Configuration is not a guarantee of security {#️-configuração-não-é-garantia-de-segurança}

It is essential to avoid the implicit equivalence:

* ✔️ `securityContext` defined
* ❌ automatically secure execution

There are three distinct levels:

1. **Platform capability**
   What Kubernetes allows to be configured.
2. **Declared configuration**
   What is in the manifests.
3. **Effective execution state**
   What the pod actually applies at runtime.

This file explicitly addresses **all three levels**, not only the second.

---

## 📘 Applicable security mechanisms {#-mecanismos-de-segurança-aplicáveis}

| Mechanism                  | Technical function                             | Inherent limitation                |
| -------------------------- | ------------------------------------------ | --------------------------------- |
| `securityContext`          | Defines UID, capabilities, privileges      | May be bypassed if poorly applied |
| Pod Security Standards     | Pod acceptance baseline              | Does not validate post-admission state   |
| Kyverno / OPA (Gatekeeper) | Blocking of out-of-policy configurations | Does not assess contextual risk       |
| NetworkPolicies            | Traffic isolation                      | Requires complete coverage         |
| RuntimeClass / Sandboxing  | Reinforced isolation                       | Does not eliminate logical risk          |
| Admission Webhooks         | Pre-execution validation                     | Acts before runtime             |

---

## 🛠️ How to apply it correctly {#️-como-aplicar-de-forma-correta}

### 1️⃣ Declare mandatory minimum restrictions {#1️⃣-declarar-restrições-mínimas-obrigatórias}

All pods must explicitly declare:

```yaml
securityContext:
  runAsNonRoot: true
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities:
    drop: ["ALL"]
```

These declarations are **necessary**, but not sufficient.

---

### 2️⃣ Impose technical enforcement {#2️⃣-impor-enforcement-técnico}

* Enable Pod Security Admission (`restricted` or `baseline`);
* Apply policies via Kyverno or OPA to:

  * prohibit `privileged: true`;
  * block images from outside an authorised origin;
  * require traceability labels and metadata.

Enforcement **reduces human error**; it does not replace governance.

---

### 3️⃣ Verify the effective state at runtime {#3️⃣-verificar-estado-efetivo-em-runtime}

For critical workloads (L2/L3), it is necessary to:

* Confirm the effective UID of the process;
* Validate real mounts and permissions;
* Verify that the seccomp / AppArmor profile is active;
* Detect deviations (*drift*) after admission;
* Record evidence for audit.

Without this verification, security is merely **assumed**.

---

## 📂 Where to configure, version and observe {#-onde-configurar-versionar-e-observar}

* Manifests in versioned Git repositories;
* Policies as code via GitOps;
* Admission and rejection logs preserved;
* Compliance and deviation metrics monitored;
* Execution evidence associated with the workload.

---

## ✅ Good practices {#-boas-práticas}

* Treat Kubernetes as an **execution platform**, not as an autonomous security barrier;
* Clearly separate:

  * configuration,
  * enforcement,
  * verification;
* Apply policies progressively (`audit` → `enforce`);
* Review permissions after cluster upgrades;
* Document exceptions as temporary and traceable decisions;
* Assume that **configuration without observation is a hypothesis, not a fact**.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                       | Relation to execution in Kubernetes     |
| ------------------------------- | -------------------------------------- |
| `02-runners-isolamento.md`      | Runners as ephemeral pods             |
| `04-hardening-containers.md`    | Restrictions applied to the runtime        |
| `05-policies-runtime-opa.md`    | Technical enforcement at admission       |
| `09-riscos-processo-imagens.md` | Separation between intention and real state |
| `15-aplicacao-lifecycle.md`     | Integration into the SSDLC                    |

> ☁️ Kubernetes executes what it is asked to.
> Security exists only when **what is executed matches what was consciously decided**.
