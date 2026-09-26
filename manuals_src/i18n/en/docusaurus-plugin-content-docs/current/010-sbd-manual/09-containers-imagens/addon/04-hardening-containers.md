---
id: hardening-containers
title: Hardening and Execution Restrictions in Containers
description: Minimisation, hardening and effective verification of permissions in images and containerised environments
tags: [containers, hardening, permissoes, runtime, isolamento, seguranca]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/addon/04-hardening-containers.md
  source_sha256: 9ad1c5ca587d3b901623950721b9b6e2fcc451c198a25021abb477df0161a98c
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 9304d084d96839ec7fe2a1619ef9da1723d4a8f67938cebb4fa24734ac8029ca
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, layer, provenance, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 3098a29a57b5b3cc455599de215632264caa875f506ea9481de2218f28d88fe0
  translated_at: 2026-09-26T09:58:15Z
  stamped_at: 2026-09-26T18:34:50Z
  reviewed_by: null
---

# Hardening and Execution Restrictions in Containers

## 🌟 Objective {#-objetivo}

Strengthen the security of container execution through **reduction of the attack surface**, **removal of unnecessary components** and **explicit restriction of runtime permissions**, ensuring that each container runs **only what is necessary, with the least privilege possible**.

In the modern SSDLC, hardening **cannot be treated as a declared intention**.  
It is necessary to ensure that the restrictions defined **are effectively applied and verifiable** at execution time.

These measures complement the choice of secure images and the validation of their provenance, reducing the impact of exploitable vulnerabilities, configuration errors and runtime abuse.

---

## 🧬 What container hardening means {#-o-que-significa-fazer-hardening-de-containers}

**Container hardening** consists of the systematic application of measures that:

- **Remove unnecessary binaries and packages** (e.g. `curl`, `bash`, `ping`);
- **Prevent execution as `root`**;
- **Restrict kernel `capabilities`** to what is strictly necessary;
- **Limit syscalls and interactions with the host** (seccomp, AppArmor, SELinux);
- **Apply immutability to the filesystem**;
- **Block dangerous interfaces** such as `/proc`, `/sys` or the Docker socket.

> 🧱 A container can only be considered hardened if **the effective runtime state** matches what was defined in the build and in the manifests.

---

## ⚠️ Configured hardening ≠ effective hardening {#️-hardening-configurado--hardening-efetivo}

One of the most common errors in automated environments is to assume that:

- a well-written `Dockerfile`,
- a defined `securityContext`,
- or an applied policy,

automatically guarantee a secure runtime.

In practice, there are three distinct states:

1. **Declared hardening**  
   What is defined in code or configuration.
2. **Applied hardening**  
   What the platform actually attempts to apply.
3. **Effective hardening**  
   What can be empirically observed in the running container.

This chapter explicitly treats hardening as a **verifiable state**, not as an assumed property.

---

## 📘 Examples of hardening practices {#-exemplos-de-práticas-de-hardening}

| Practice                          | Technique / Mechanism                          | Operational observations                         |
|---------------------------------|-----------------------------------------------|--------------------------------------------------|
| Non-root user             | `USER` in the Dockerfile                          | Must be validated at runtime                     |
| Read-only FS                    | `readOnlyRootFilesystem: true` (K8s)          | Requires verification of mounts                     |
| Minimal capabilities            | `drop: ALL` + explicit add                   | Avoid permissive defaults                      |
| Seccomp                         | `runtime/default` or custom profile            | Confirm the active profile                           |
| AppArmor / SELinux              | Restrictive profiles                            | Depends on host support                       |
| Unprivileged execution       | No `--privileged`, no Docker socket         | Must be blocked by policy                  |

---

## 🛠️ How to apply and verify at build and runtime {#️-como-aplicar-e-verificar-no-build-e-runtime}

### 1️⃣ At build (image) {#1️⃣-no-build-imagem}

- Define a non-root user (`USER`);
- Avoid installing interactive tools;
- Minimise `ENTRYPOINT` and `CMD`;
- Add security and context labels;
- Validate the Dockerfile with linters (e.g. Hadolint).

> The build **defines intentions**; it does not guarantee application.

---

### 2️⃣ At deploy (orchestration / CI/CD) {#2️⃣-no-deploy-orquestração--cicd}

- Define an explicit `securityContext`:
  - `runAsNonRoot: true`
  - `readOnlyRootFilesystem: true`
  - `allowPrivilegeEscalation: false`
  - `capabilities: drop: ["ALL"]`
- Apply Pod Security Standards / PSA;
- Enforce through OPA or Kyverno (see `05-policies-runtime-opa.md`).

> Technical enforcement **blocks insecure configurations**, but does not validate the real state.

---

### 3️⃣ At runtime (effective verification) {#3️⃣-em-runtime-verificação-efetiva}

- Verify the effective user (`id`, `/proc/self/status`);
- Validate mounts and permissions;
- Confirm that the seccomp/AppArmor profile is active;
- Detect deviations (*drift*) from the expected configuration;
- Record results for audit.

Without this verification, hardening is merely **assumed**, not demonstrated.

---

## 📂 Where to configure and control {#-onde-configurar-e-controlar}

- **Dockerfile**: minimal and reproducible baseline;
- **Manifests / Helm charts**: declarative definition of restrictions;
- **CI/CD**: automatic validation of insecure configurations;
- **Admission Controllers**: centralised enforcement;
- **Runtime monitoring**: empirical confirmation of the state.

Each layer reduces the likelihood of error, but **none is sufficient on its own**.

---

## ✅ Good practices {#-boas-práticas}

- Define hardening profiles by workload type;
- Prohibit privileged containers by policy;
- Validate hardening after deploy, not only before;
- Treat exceptions as formal and temporary decisions;
- Review hardening after platform or kernel changes;
- Integrate continuous runtime verification in critical environments.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                         | Relation to hardening                          |
|----------------------------------|------------------------------------------------|
| `01-imagens-base.md`             | Minimisation of the surface in the image            |
| `02-runners-isolamento.md`       | Isolation of the execution environment             |
| `05-policies-runtime-opa.md`     | Technical enforcement of restrictions              |
| `08-kubernetes-execucao.md`      | Practical application in clusters                  |
| `09-riscos-processo-imagens.md`  | Difference between intention and effective state      |

> 🔐 Hardening only exists when it can be **observed, reproduced and audited**.  
> Configuration without verification is merely assumption.
