---
id: gestao-segredos-pipeline
title: Secure Secrets Management and Injection
sidebar_position: 3
description: Strategies to protect secrets in pipelines, avoid hardcoding and ensure secure injection via vaults or variables.
tags: [segredos, cicd, vault, pipelines, segurança, variáveis]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/addon/03-gestao-segredos-pipeline.md
  source_sha256: a0bd1a82d2ac56d50a86d2eac4e2cc8a7e7dc3f3f59c28f9d0d837f793633b04
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: a01f2febb6cfba5e22f0faacbc17ba9a6700523d4601128ba8bf346e8f51cc6f
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [framework_source_corpus, risk_level]
  glossary_sha256: 42eae61398e9357269172e245bbe273f76d4133f8a445ea86d8e814265727e23
  translated_at: 2026-09-26T09:09:13Z
  reviewed_by: null
---


# Secure secrets management and injection

Secrets management in CI/CD pipelines is one of the most critical attack vectors in the development chain. Access tokens, API keys, deploy credentials and other secrets are frequently exposed by accident in variables, logs or versioned files.

This practice defines the mandatory controls to ensure the **confidentiality, minimum scope and controlled injection** of secrets during pipeline execution.

> The confidentiality of secrets must be preserved even in the event of a pipeline failure.

---

## 🎯 Objectives {#-objetivos}

- Prevent unauthorised access to secrets used by pipelines;
- Prevent the accidental exposure of secrets in logs, repositories or temporary files;
- Reduce the impact of partial compromises, through segregation, limited scope and periodic rotation.

---

## 🛠️ Practices {#️-práticas}

1. **Complete separation between code and secrets**  
   - Secrets must never be stored directly in source code or in pipeline YAML files;
   - Injection must be done through external mechanisms (e.g. `secrets.*`, vaults, variable groups).

2. **Segregation by environment, application and function**  
   - Secrets must have minimum scope (e.g. read-only, only for a specific job);
   - Avoid the use of “global secrets” shared between pipelines or environments.

3. **Temporary, runtime injection**  
   - Secrets must be injected only during execution;
   - They must never be persisted to disk or in generated artefacts;
   - They must be deleted automatically after use.

4. **Protection of logs and sensitive variables**  
   - Variables containing secrets must be marked as protected (`masked`, `secureString`);
   - The output of commands that access secrets must be hidden in the logs (`stdout` disabled if necessary).

5. **Periodic rotation and automatic revocation**  
   - There must be a formal secrets rotation policy;
   - Compromised secrets must be revoked immediately, with minimised impact;
   - L3 applications must use external vaults with automatic rotation and auditing.

---

## ⚖️ Proportional application by risk level {#️-aplicação-proporcional-por-nível-de-risco}

| Level | Mandatory requirements                              | Enhanced requirements                                  |
|-------|--------------------------------------------------------|---------------------------------------------------------|
| **L1** | Secrets as secure variables; protected logs       | -                                                       |
| **L2** | Segregation by environment and job; runtime injection      | Centralised revocation; roaming disabled          |
| **L3** | External vault; automatic rotation; fine-grained segregation     | Usage auditing; alerts on improper access            |

---

## 📌 Practical examples {#-exemplos-práticos}

- **GitHub Actions**  
  - Use of `secrets.*` with minimum scope and `masked: true` protection;  
  - Enabling audit logs in GitHub Enterprise.

- **GitLab CI**  
  - `CI/CD Variables` with `masked`, `protected` and scope per environment;  
  - Integration with HashiCorp Vault.

- **Azure DevOps**  
  - `Variable Groups` with scope per pipeline and environment;  
  - Use of `SecureString` and `Key Vault References`.

- **Jenkins**  
  - Credentials management with the `Credentials Plugin`;  
  - Injection via `withCredentials` and integration with an external Vault.

---

## 📉 Mitigated risks {#-riscos-mitigados}

- Leakage of secrets via logs or temporary files (OSC&R: CI0013);
- Improper use of tokens with excessive permissions (OSC&R: CI0007, CI0012);
- Improper persistence of credentials on disk;
- Lateral access by unauthorised pipelines or malicious jobs.

---
