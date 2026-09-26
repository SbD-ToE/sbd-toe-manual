---
id: risco-supply-chain
title: Supply Chain Threats
description: Types of attack via dependencies and practices for detection and mitigation
tags: [dependencias, sbom, sca, supply-chain, risks]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/addon/06-risco-supply-chain.md
  source_sha256: f6189dd97f3211f747dc9b00191637392bf2ad676703ef3b0bed14b24678cad0
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 1e2d5f3193a68f6dc1f1aac1e34426e6f8417b9dcec4b1f1c8ad12fa3759bee3
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [mirror_osf, threat, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 70c50183f862a2db7dfc554f885f28a1b7a0a0e1df94ef2bdc23b3833c110e4c
  translated_at: 2026-09-26T08:45:25Z
  stamped_at: 2026-09-26T18:33:49Z
  reviewed_by: null
---

# Supply Chain Threats

## 🌟 Objective {#-objetivo}

Identify the main attack vectors in the software supply chain, with an emphasis on external dependencies, and establish effective technical and organisational countermeasures.

> ⚠️ Supply chain attacks are among the most critical today, because they exploit the **implicit trust in third-party packages** used at build time or runtime.

---

## 🔧 Common types of attack {#-tipos-comuns-de-ataque}

| Threat Type            | Description                                                        | Real example                    |
|----------------------------|------------------------------------------------------------------|---------------------------------|
| **Typosquatting**          | Package with a name similar to that of a well-known one                        | `lodashs` instead of `lodash`    |
| **Dependency Confusion**  | Resolving packages from the public registry instead of the private one            | `internal-lib` published externally |
| **Account hijack**        | Compromised dev account publishes a malicious update             | `ua-parser-js` (2021)           |
| **Abandoned package**      | Unmaintained library used as a vector                     | `event-stream` (2018)           |
| **Code Injection**         | Malicious payload in the `postinstall` or script                    | `node-ipc` (2022)               |

---

## 🔐 Mitigation strategies {#-estratégias-de-mitigação}

### 1. **Origin verification** {#1-verificação-de-origem}

- Use internal repositories, proxies or mirrors
- Block the installation of packages from outside an approved origin

### 2. **Name monitoring** {#2-monitorização-de-nomes}

- Audit new packages added to `package.json`, `pom.xml`, etc.
- Use typosquatting alerts with tools (e.g. Socket.dev, npm-proxy-check)

### 3. **Review of embedded scripts** {#3-revisão-de-scripts-embutidos}

- Detect `postinstall`, `preinstall`, `install` with executable scripts
- Use flags such as `--ignore-scripts` where appropriate

### 4. **Approval and timeout policies** {#4-políticas-de-aprovação-e-timeout}

- Require review of new packages before use
- Apply a TTL to abandoned dependencies

### 5. **Build isolation and validation** {#5-isolamento-e-validação-de-build}

- Use clean and immutable environments for the build
- Sign artefacts and validate integrity

---

## 📖 Case studies {#-casos-de-estudo}

### `event-stream` {#event-stream}

- Popular npm package with access transferred
- An update introduced the `flatmap-stream` dependency containing malware
- Affected financial applications

### `ua-parser-js` {#ua-parser-js}

- Hijack of the maintainer's npm account
- Version published with a cryptocurrency miner
- Detected by the community via GitHub Actions

---

## ✅ Operational recommendations {#-recomendações-operacionais}

| Practice                                   | Apply in               |
|-------------------------------------------|---------------------------|
| Internal proxy with an origin allowlist  | All projects        |
| Formal approval of new packages        | L2 and L3                  |
| Scan for malicious scripts in packages     | L2 and L3                  |
| TTL for dependencies that are not updated     | L2 and L3                  |
| Alerts for typosquatting and suspicious names| L3 (high)             |

---

## 🔗 Links to other files {#-ligações-com-outros-ficheiros}

| Document                   | Link with the supply chain                           |
|-----------------------------|---------------------------------------------------------|
| `03-governanca-libs-terceiros.md` | Approval of suspicious or risky packages         |
| `04-integracao-ci-cd.md`    | Execution of validators and blocking scripts         |
| `07-controle-registos-origem.md` | Reinforcement of trusted origin and internal mirrors      |

---

> 🚫 Control of the supply chain is inseparable from modern security. Ignoring it means blindly trusting code executed outside the organisation's control.
