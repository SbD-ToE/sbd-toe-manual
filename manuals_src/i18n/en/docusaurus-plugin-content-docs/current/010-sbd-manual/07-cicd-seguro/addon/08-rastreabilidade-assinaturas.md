---
id: rastreabilidade-assinaturas
title: Traceability of Executions, Signatures and Deploys
sidebar_position: 8
description: Ensure that each pipeline execution and each artefact can be traced back to the associated commit, origin and person responsible.
tags: [rastreabilidade, cicd, execuções, deploy, logs, auditoria]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/addon/08-rastreabilidade-assinaturas.md
  source_sha256: 78a5c652cf34d6dd554313278dd3986e38af8d8a0deb2cf32e831f59810b8404
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 6b4df8afa4ed68fbe76c5994a8e39c4ce1dd65ad049228fca89774680162cee9
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [audit_trail, practitioner_manual, provenance, risk_level, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: b1891bfcd0e5b4236f47dc9030321a1ff09e909f1a618b17a72d7d6336ed63b3
  translated_at: 2026-09-26T09:09:16Z
  reviewed_by: null
---


# Traceability of signatures and deploys

Traceability is the ability to **prove what was done, by whom, with which artefacts and in what context**. In the context of CI/CD pipelines, this ability is essential to ensure accountability, support for audits and the possibility of safe rollback.

This practice defines the mechanisms needed to ensure that **each critical execution, build, release or deploy is identifiable, verifiable and auditable at any time**.

> A CI/CD chain without traceability cannot be considered trustworthy.

---

## 🎯 Objectives {#-objetivos}

- Record all relevant pipeline executions in a reliable and verifiable way;
- Associate artefacts with specific builds, users, commits and environments;
- Support audits, investigations and rollbacks based on concrete and persistent evidence.

---

## 🛠️ Practices {#️-práticas}

1. **Digital signing of critical builds and releases**  
   - Each published artefact must be digitally signed (e.g. GPG, Sigstore, JWT);
   - The signature must contain the commit hash, author, timestamp and pipeline ID.

2. **Preservation of execution records and metadata**  
   - Relevant logs and variables must be stored in accordance with the retention policy;
   - They must include: user, repository, pipeline, time, result, main parameters.

3. **Formal recording of deploys**  
   - Each deploy must reference the specific artefact by hash;
   - The following must be recorded: the party responsible (human or service), pipeline, environment and timestamp.

4. **End-to-end linkage: commit → build → release → deploy**  
   - The entire chain of events must be traceable, including configuration changes;
   - That traceability must be accessible through audit or API.

5. **Retention of hashes, provenance and associated evidence**  
   - Metadata (e.g. SLSA provenance) must be archived together with the artefacts;
   - They must allow retrospective validation and comparison with future builds.

---

## ⚖️ Proportional application by risk level {#️-aplicação-proporcional-por-nível-de-risco}

| Level | Mandatory records                                 | Enhanced requirements                                      |
|-------|--------------------------------------------------------|-------------------------------------------------------------|
| **L1** | Execution logs and build hash                      | -                                                           |
| **L2** | Recording of pipeline, artefact and deploy               | Simple provenance; release signing                 |
| **L3** | Complete SLSA provenance; auditable deploy          | End-to-end chain; tamper-proof logs; periodic verification |

---

## 📌 Practical examples {#-exemplos-práticos}

- **GitHub Actions**  
  - Use of `github.run_id`, `github.sha`, `GITHUB_ACTOR` in artefacts and tags;  
  - Signatures with `cosign` and provenance with `slsa-github-generator`.

- **GitLab CI**  
  - Inclusion of `pipeline_id`, `commit`, `project.path` in artefacts;  
  - Use of `release-cli` to associate metadata and changes with the release.

- **Azure DevOps**  
  - Identifiers such as `Build.BuildId` and `Release.ReleaseId`;  
  - Signatures with certificates and deployment auditing in `AuditLogs`.

- **Jenkins**  
  - Manual recording with `BUILD_ID`, `BUILD_URL`, `GIT_COMMIT`;  
  - Signing with GPG and structured logs via plugins.

---

## 📉 Mitigated risks {#-riscos-mitigados}

- Ambiguity about the origin of deploys (OSC&R: CI0004);
- Absence of an auditable chain of trust (OSC&R: CI0011, CI0016);
- Difficulty in establishing responsibility in the event of an incident;
- Untraceable, altered or unauthorised releases.

---
