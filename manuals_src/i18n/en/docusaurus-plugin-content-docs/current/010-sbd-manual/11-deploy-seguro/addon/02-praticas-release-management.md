---
id: 02-praticas-release-management
title: Release Management Practices
description: Strategies for the secure management of releases and the segregation of functionality during continuous delivery.
tags: [tipo:anexo, grupo:execucao, tema:release, segurança, staging]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/11-deploy-seguro/addon/02-praticas-release-management.md
  source_sha256: a445d5f604c674d08941d599d7078956ce9ce6b979e9cd73e16493d1a765325b
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: adee05b906e82da89a759e7c7474809e74eeeed19ba2236c80649e1ad26fed00
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 112d795f9bd927f0d4c24114e389470217eb00c1d6b919ae2df2e4f7bdb4878d
  glossary_keys: [chapter_role, provenance, requirement_runtime, risk_level, traceability, validation_evaluation]
  glossary_sha256: d8ad59c5b1bf9c55e7b2388b5bdbf3adf929c8773ce8df4c22386fd51d6356e9
  translated_at: 2026-09-26T11:00:47Z
  reviewed_by: null
---


# Security-Focused Release Management Practices

## 🌟 Objective {#-objetivo}

To describe and systematise secure practices for **version, release and software distribution management**, with a focus on:

- Reducing risk and impact in production;
- Formal validation and traceability of the decision;
- Reversibility and rapid recovery;
- Alignment with normative frameworks (SSDF, SLSA, SAMM).

---

## 🧬 What Secure Release Management is {#-o-que-é-release-management-seguro}

Release Management is the process of **preparing, approving, distributing and monitoring a new software version**. A secure release must:

- Be predictable, validated and reversible;
- Have defined ownership and approval criteria;
- Be accompanied by technical and security documentation;
- Include formal rollback mechanisms.

---

## 🛠️ How to apply {#️-como-aplicar}

### 🗂️ Essential elements of a secure release {#️-elementos-essenciais-de-uma-release-segura}

| Element                       | Description                                                                 |
|--------------------------------|---------------------------------------------------------------------------|
| **Technical changelog**          | List of relevant changes, including security patches           |
| **Security changelog**     | Highlight of fixed CVEs, changed dependencies or critical features |
| **Release owner**           | Person or team responsible for the release                                |
| **Approval checklist**     | Minimum criteria before production (e.g. findings resolved)            |
| **Rollback plan**          | Clear and tested strategy for returning to the previous version              |
| **Integrated validations**      | Automated tests, reviews, SBOM scan, alerts                    |
| **Activation criteria**      | Toggle conditions, scope and approval of functionality                |

---

### 🧪 Recommended validations by risk level {#-validações-recomendadas-por-nível-de-risco}

| Risk level | Minimum validations before production                                            |
|----------------|---------------------------------------------------------------------------------|
| **L1 (low)** | Manual checklists, basic functional validation                                 |
| **L2 (medium)** | Dual approval, AppSec review, dependency scan                          |
| **L3 (high)**| Formal validation, fuzzing, impact analysis, rollback validated in staging   |

---

### ✅ Example of a release checklist (recommended minimum) {#-exemplo-de-checklist-de-release-mínimo-recomendado}

- [ ] All tests passed in CI/CD
- [ ] Critical findings resolved or justified
- [ ] SBOM updated and signed
- [ ] Rollback plan defined and validated
- [ ] Toggles and feature flags documented
- [ ] Logs and metrics defined for observation
- [ ] Approval by the functional owner and a technical reviewer
- [ ] Release recorded with hash, version and date

> 💡 This checklist can be used as a *gate* in the production pipeline.

---

## 🔁 Versioning and Reversibility {#-versionamento-e-reversibilidade}

### 📁 Secure versioning {#-versionamento-seguro}

- Use **semantic versioning** (`MAJOR.MINOR.PATCH`) with documented conventions;
- Associate with each release:
  - Commit or build hash;
  - Date and time;
  - Owner / responsible team;
  - Justification (e.g. urgent fix, new feature, refactor).

### 📉 Rollback {#-rollback}

- Must be planned as part of the release, not as an exception;
- Must make it possible to:
  - Restore the previous version without loss of state;
  - Deactivate toggles of critical functionality;
  - Reverse database migrations (where feasible);
- Include rollback tests as part of pre-production validation.

---

## 📊 Risk indicators per release {#-indicadores-de-risco-por-release}

- No. of active toggles;
- No. of open findings;
- No. of manual changes (vs automatic);
- Test coverage score;
- Confidence level defined by the owner (`alta / média / experimental`).

---

## 🧰 Supporting tools {#-ferramentas-de-suporte}

| Category        | Recommended tools                          |
|------------------|---------------------------------------------------|
| Versioning    | Git tags, GitHub Releases                         |
| Approval        | Azure DevOps, Jira workflows                      |
| Declarative releases | Argo CD, Flux, Spinnaker                    |
| Observability  | Dashboards with metrics per release (e.g. Grafana) |

---

## ✅ Good practices {#-boas-práticas}

- Integrate security into the release process (shift-left + shift-right);
- Require explicit approval for releases to production;
- Avoid manual releases outside the documented process;
- Document every step, change and decision;
- Ensure rollback and fallback tests before go-live;
- Automate the generation of SBOMs and their association with the release;
- Track each release with versioned artefacts.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document / Chapter         | Relation to this topic                       |
|------------------------------|---------------------------------------------|
| Ch. 07 - Secure CI/CD       | Automated process and controls per stage |
| Ch. 05 - Dependencies and SBOM| SBOM as a requirement for release            |
| Ch. 10 - Security Testing| Validation before deployment                   |
| Ch. 12 - Monitoring and Operations      | Post-release observation                      |
| SLSA L3/L4                   | Release provenance and secure rollback   |
| NIST SSDF PM.3, RV.1         | Formal approval and risk management         |

---

> 🎯 Release management must be treated as a formal and secure process - **not as a mere technical deployment**.  
> A good release process is essential to sustain advanced security practices and to ensure confidence in the changes delivered.
