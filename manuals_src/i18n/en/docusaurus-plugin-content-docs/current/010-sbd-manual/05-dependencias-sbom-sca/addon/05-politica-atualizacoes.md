---
id: politica-atualizacoes
title: Dependency Update Policies
description: Practices for proactive updating, TTL, locking and secure version management
tags: [dependencias, sbom, sca, supply-chain, policies]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/05-dependencias-sbom-sca/addon/05-politica-atualizacoes.md
  source_sha256: 170b7409b566b28280f17485bd0d0c8028eb3bf9d155dde2e47f0b71728fab88
  source_commit: 036d74010f423f247be988e4a417375c74edb9d9
  target_sha256: ecc17e2606d21e8e86d59ff3e4f2c82b5b9479308b20c236f0d40dffa6aa95ec
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [cycle_iteration, practitioner_manual, traceability, validation_evaluation]
  glossary_sha256: 0890addb66b0a1785ebe537d8e6194079c88936b2aab252a8d2f0cc8b5426c0b
  translated_at: 2026-09-27T07:53:41Z
  stamped_at: 2026-09-27T07:53:41Z
  reviewed_by: null
---

# Dependency Update Policies

## 🌟 Objective {#-objetivo}

Establish systematic practices for the **proactive updating of third-party libraries and dependencies**, avoiding the accumulation of technical debt and prolonged exposure to known risks.

> ⚠️ Many vulnerability exploits occur in libraries that already have a patch available but have not been updated. The update policy is an essential defence.

---

## ⏲ Principles of secure updating {#-princípios-de-atualização-segura}

1. Every dependency must have a defined **TTL (Time To Live)**: the maximum period before it is reviewed.
2. Mechanisms for **explicit version locking** must be used, to avoid unaudited updates.
3. Updates must be **automated where possible**, but always **validated** before deploy.
4. Periodic updating must be treated as **part of the development cycle**, not as an exception.

---

## 🛠️ Control mechanisms by language {#️-mecanismos-de-controlo-por-linguagem}

| Stack       | Lockfile / Mechanism           | Update tools         |
|-------------|----------------------------------|------------------------------------|
| Node.js     | `package-lock.json`, `npm ci`   | `npm-check-updates`, RenovateBot   |
| Python      | `requirements.txt`, `pip-tools` | `pip-review`, Dependabot           |
| Java (Maven)| `pom.xml`, fixed version          | Versions Maven Plugin              |
| .NET        | `packages.lock.json`, `*.csproj`| `dotnet outdated`, NuKeeper        |
| Go          | `go.sum`, `go.mod`              | `go get -u`, Dependabot            |

> 🔐 The use of lockfiles is essential for reproducibility and traceability.

---

## 🔧 Recommended review frequency {#-frequência-recomendada-de-revisão}

| Project type         | Minimum frequency of automated dependency review (scan) |
|--------------------------|------------------------------------------------|
| Critical production (L3)    | Weekly (automatic + manual validation)      |
| Backend / API (L2)       | Fortnightly                                     |
| Internal / Tools (L1)| Monthly                                       |

> SCA findings must be handled **outside this cycle**, in a reactive regime (e.g. a CVE with an alert).

---

## 📅 Update strategies {#-estratégias-de-atualização}

- **Automated proactive**: bots that open update PRs with tests
- **Grouped per sprint**: a periodic "library update" task
- **Semantic control**: defined `^` and `~` limits and ranges
- **Pinning of critical versions**: e.g. `express@4.18.2` vs `express@latest`

---

## 📄 Checklist for applying updates {#-checklist-de-aplicação-de-updates}

| Item                                                           | Verified? |
|----------------------------------------------------------------|-------------|
| Is there a lockfile and is it versioned?                              | ☑         |
| Are periodic updates carried out traceably? | ☑         |
| Do all updates go through CI/CD with tests?           | ☑         |
| Are the versions audited by SCA after an update?                 | ☑         |
| Are critical updates triaged within ≤ 24h and fixed within the level SLA (Policy 19 §4.3)? | ☑         |

---

## 🔗 Links to other files {#-ligações-com-outros-ficheiros}

| Document                   | Link with updates                            |
|-----------------------------|-------------------------------------------------------------|
| `02-analise-sca.md`         | Detects vulnerabilities that may require an update      |
| `04-integracao-ci-cd.md`    | Automates updates and applies validators in the pipeline         |
| `03-governanca-libs-terceiros.md` | Defines which dependencies may or may not be updated |

---

> ✅ Updating dependencies is a technical and risk management process. It must not be postponed indefinitely, nor carried out without adequate validation and traceability.
