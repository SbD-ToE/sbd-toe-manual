---
id: runners-isolamento
title: Runners, Isolated Execution and Controlled Environments
description: Assurance of secure and controlled execution of containers in pipelines and shared environments
tags: [runners, isolamento, pipelines, execucao, seguranca, cicd]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/addon/02-runners-isolamento.md
  source_sha256: 7ad065da50347a56996e02982fa1b0b8698b947e7b0375df1ed01ddcf60bd9f8
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: 6119fa1dc6ca4c1f0df6346532a9c2b0c4e43a8da68d8b67caec0bc47743c646
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [audit_trail, cycle_iteration, lifecycle_phase]
  glossary_sha256: 6831e8f6b3201711af20558f305b3d3ae28178bc06c1099b9276e33615b1dbd1
  translated_at: 2026-09-26T12:48:46Z
  reviewed_by: null
---

# Runners, Isolated Execution and Controlled Environments

## 🌟 Objective {#-objetivo}

Ensure that all containers are executed in **isolated, controlled and auditable environments**, especially in the context of **CI/CD pipelines and automated execution**, mitigating process risks and technical compromise risks, namely:

- Compromise of the host or of other jobs;
- Privilege escalation;
- Undue persistence of sensitive data between executions;
- Execution of unassessed artefacts in shared environments;
- Implicit acceptance of risk by way of automation.

In a modern SSDLC, runners **are not merely infrastructure**:  
they are **points where trust materialises**, where artefacts move from “built” to “executed”.

---

## 🧬 What runners and execution environments are {#-o-que-são-runners-e-ambientes-de-execução}

**Runners** are execution agents responsible for running CI/CD tasks or container workloads, typically on platforms such as:

- GitHub Actions (`runners`)
- GitLab CI (`runners`)
- Azure DevOps (`agents`)
- Jenkins (`executors`)
- Kubernetes Jobs, CronJobs or temporary pods

Regardless of the platform, a runner always represents an **environment where implicit decisions occur**:  
which image is executed, with which permissions, in which context and with what impact.

An **isolated execution environment** must ensure, at a minimum:

- Separation of namespaces (process, network, filesystem);
- No persistence between executions;
- Execution with a non-root user and minimal permissions;
- Explicit limitation of resources (CPU, memory, storage);
- Inability to affect parallel or future executions.

> ⚠️ Shared and generic runners are **critical points of process risk**, because a successful execution may be interpreted, wrongly, as implicit authorisation.

---

## 📘 Types of runners and risk levels {#-tipos-de-runners-e-níveis-de-risco}

| Type                     | Examples                               | Associated risk                       | Operational notes                                  |
|--------------------------|----------------------------------------|---------------------------------------|-----------------------------------------------------|
| Shared (multi-tenant)| GitHub hosted, GitLab shared            | High – common surface            | Avoid in L2/L3 pipelines                           |
| Self-managed               | Azure DevOps agent, on-prem runners     | Moderate – depends on hardening       | Acceptable if isolated and auditable                    |
| Ephemeral and dedicated       | K8s Jobs, temporary runners           | Low – strong isolation              | Preferred: recreated per execution                 |

The choice of runner type **is a risk decision**, not merely one of operational convenience.

---

## 🛠️ How to apply isolated execution {#️-como-aplicar-execução-isolada}

Secure execution requires that the runner **does not introduce implicit trust** nor amplify upstream errors:

1. **Avoid shared runners** in critical or regulated projects (L3);
2. **Run containers in ephemeral environments**, destroyed after each execution;
3. **Prohibit privileged execution** (`--privileged`, `--cap-add`, access to `/var/run/docker.sock`);
4. **Apply explicit resource limits** (CPU, RAM, storage);
5. **Ensure that the execution user has no administrative permissions**;
6. **Apply additional sandboxing** (e.g. gVisor, Kata Containers) when the risk justifies it;
7. **Restrict the images allowed on the runner** (see `01-imagens-base.md`);
8. **Control and justify any access to the network or external storage**;
9. **Record and monitor executions**, including isolation failures and evasion attempts.

These controls do not replace human decision, but they **reduce the impact of wrong or implicit decisions**.

---

## 📂 Where and how to configure {#-onde-e-como-configurar}

| Platform       | Recommended isolation practice                                  |
|------------------|---------------------------------------------------------------------|
| GitHub Actions   | Self-hosted runners in ephemeral environments (e.g. Kubernetes)         |
| Azure DevOps     | Agents in dedicated containers; no access to the host                 |
| GitLab CI        | Docker/Kubernetes runners with a strict isolation policy         |
| Jenkins          | Execution in ephemeral containers with a read-only filesystem            |
| Kubernetes       | Temporary pods with `securityContext`, PSA and quotas                |

Regardless of the platform, the rule is invariable:  
**the runner must not outlive the execution**.

---

## 🔍 Runners as a point of implicit decision {#-runners-como-ponto-de-decisão-implícita}

Whenever a runner executes a container:

- an image has been implicitly accepted;
- a permissions context has been implicitly authorised;
- a potential impact has been implicitly assumed.

Therefore:
- the execution **must be traceable**;
- the context **must be reproducible**;
- the decision **must be justifiable a posteriori**.

Without these elements, automation turns into systemic risk.

---

## ✅ Good practices {#-boas-práticas}

- Isolate runners by project, domain or namespace;
- Recreate runners on each execution (no persistent cache);
- Monitor resource usage and execution anomalies;
- Prohibit access to the internal network by default;
- Use labels and restrictions to enforce secure execution;
- Integrate technical enforcement (OPA/Kyverno) without replacing governance.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                         | Relation to runners and execution                  |
|----------------------------------|-------------------------------------------------|
| `01-imagens-base.md`             | Images allowed in execution environments    |
| `05-policies-runtime-opa.md`    | Technical enforcement of policies                |
| `06-inventario-sbom.md`         | Inventory of the execution environment              |
| `09-riscos-processo-imagens.md` | Separation between automatic execution and decision   |
| `15-aplicacao-lifecycle.md`     | Operational application in the lifecycle          |

> 🧱 Pipeline security starts at execution.  
> An insecure runner **is not merely a technical risk** - it is a mechanism for implicit acceptance of risk.
