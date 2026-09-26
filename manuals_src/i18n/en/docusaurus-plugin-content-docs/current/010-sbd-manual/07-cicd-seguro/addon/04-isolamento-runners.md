---
id: isolamento-runners
title: Runner Isolation and Protection
sidebar_position: 4
description: Measures to segregate runners by application, avoid persistence and ensure ephemeral, controlled execution environments.
tags: [cicd, runners, isolamento, segurança, execução, infraestrutura]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/addon/04-isolamento-runners.md
  source_sha256: 1c81577460facbd269ce0ca4797085b527c4f3b7e1cfb526b8920e241538c7ea
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 1a731deb551e9e616bd8ac89ef0a93dbf93577ab10791a0fe00f9e12705f7004
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [risk_level, validation_evaluation, verification_taxonomy]
  glossary_sha256: 71a0365e50290f268dccd15b8c6ae30cc3f5da9d1c1c60c5d6ade059daf2af5b
  translated_at: 2026-09-26T09:09:14Z
  reviewed_by: null
---

# Runner isolation and protection

Runners (or execution agents) are the environments where CI/CD pipelines are actually processed. If a runner is compromised, the entire build and delivery chain can be manipulated - from the introduction of backdoors to the exfiltration of secrets or the sabotage of artefacts.

> Runner security defines the trust boundaries of automated execution.

---

## 🎯 Objectives {#-objetivos}

- Ensure that pipelines are executed in **secure, controlled and ephemeral** environments;
- Prevent malicious code from compromising the runner or escaping the pipeline context;
- Reduce the attack surface associated with shared, persistent or misconfigured runners.

---

## 🛠️ Practices {#️-práticas}

1. **Execution on ephemeral or re-imageable runners**  
   - Each job must run in an isolated environment (e.g. VM, container);
   - Runners must be destroyed, restored or validated after each execution.

2. **Segregation by risk level and by project**  
   - L2 and L3 applications must not share runners with external or less critical projects;
   - Production runners must be dedicated and isolated from development environments.

3. **Hardening of execution environments**  
   - Runners must be minimal, up to date and have the smallest possible attack surface;
   - The base system must have strict control over binaries, permissions and active services.

4. **Integrity verification of agents and base images**  
   - Images must be signed and of validated origin;
   - The binaries and scripts used must be verified by hash or digital signature.

5. **Prohibition of privileged execution**  
   - Pipeline jobs must not run as `root` nor with elevated permissions;
   - Execution of commands such as `sudo`, `setcap`, or direct access to `docker` must be blocked.

---

## ⚖️ Proportional application by risk level {#️-aplicação-proporcional-por-nível-de-risco}

| Level | Mandatory requirements                                   | Enhanced requirements                                       |
|-------|------------------------------------------------------------|--------------------------------------------------------------|
| **L1** | Up-to-date runners; basic isolation per job             | -                                                            |
| **L2** | Dedicated runners per project; hardened image             | Periodic integrity verification                         |
| **L3** | Ephemeral runners, segregated by criticality; signed images | Formal hardening; no root; continuous auditing         |

---

## 📌 Practical examples {#-exemplos-práticos}

- **GitHub Actions**  
  - Use of dedicated `self-hosted runners` per project or critical application;  
  - Validation of images with `act`, `cosign` or `sigstore`.

- **GitLab Runners**  
  - `autoscaling runners` (on Kubernetes, EC2 spot) for per-job isolation;  
  - Execution via `docker+machine` or `k8s` with automatic destruction.

- **Azure DevOps**  
  - Dedicated pools per project; use of minimal images with pre-applied hardening;  
  - Blocking of access to local resources and disabling of elevated privileges.

- **Jenkins**  
  - Agents controlled by labels and node restriction (logical isolation);  
  - Pipelines with `agent { docker { image: "signed" } }` and prior hardening.

---

## 📉 Mitigated risks {#-riscos-mitigados}

- Persistence of malware between executions (OSC&R: CI0009);
- Exfiltration of secrets via contaminated runners (OSC&R: CI0003, CI0016);
- Privilege escalation via excessive permissions (OSC&R: SC0006);
- Compromise of the build through manipulation of the environment (OSC&R: CI0005).

---
