---
id: recomendacoes-avancadas
title: Advanced Recommendations for CI/CD Security
description: High-maturity practices for the protection of pipelines, with a focus on governance, simulated attack and Zero Trust
tags: [avançado, cicd, pipelines, devsecops, zero trust, deteção, simulação]
sidebar_position: 30
translation:
  source_locale: pt
  source_path: 010-sbd-manual/07-cicd-seguro/recomendacoes-avancadas.md
  source_sha256: e2de172b097353a5d5719f2e5d34cce60ff216be93fd612c07cf026cb92dd203
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 8d5d791b2fd06af9e2abd89cc3586d2dd6474a7d81bea03b8684d0504d227f9f
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [avaliacao, chapter_role, cycle_iteration, deterministic, maturity, provenance, risk_level, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: c70ad3ddb29ec1503e6fbfb2c1c26cdd5b1f543e9736a40d377a344f75c75fe9
  translated_at: 2026-09-26T09:09:23Z
  reviewed_by: null
---

# Advanced Recommendations for CI/CD Security

This file complements the main controls defined in this chapter with **advanced practices**, aimed at organisations with greater maturity, regulated environments or critical needs for traceability, auditability and resistance to sophisticated attacks.

> These recommendations **do not replace** the mandatory controls per risk level, nor do they delegate operational decisions to automatic mechanisms.  
> Their objective is to **reinforce detection, validation and governance**, always maintaining **explicit human decision**, empirical evidence and non-repudiation.

---

## 🔁 Continuous integration of findings into the development cycle {#-integração-contínua-de-findings-no-ciclo-de-desenvolvimento}

- Automatic creation of issues for critical or blocking security findings (e.g. GitHub Issues, Jira);
- Direct link between pipeline findings and the backlog items of product teams;
- Tags and labels on findings to facilitate triage and ownership (e.g. `team:frontend`, `risk:L3`);
- Real-time feedback via Slack, Teams or CI/CD bots.

> **Governance note:**  
> Automatic creation of findings speeds up response, but **does not replace human triage** nor the decision on acceptance, exception or blocking.

---

## 🧪 Attack simulation and adversarial validation of pipelines {#-simulação-de-ataques-e-validação-adversarial-de-pipelines}

- **Intentional bypass tests**: attempting to force a deploy with a failed SAST, without provenance or with ignored findings;
- **Assessment of runner permissions**: executing actions with simulated privilege escalation;
- **Simulated executions with revoked tokens, blocked environments or altered artefacts**;
- **Man-in-the-pipeline attacks** in staging environments (verification of reaction).

These practices make it possible to validate not only technical controls, but also:
- organisational reaction,
- clarity of responsibilities,
- effectiveness of alerts and blocks,
- quality of the evidence produced during simulated incidents.

---

## 🔒 Application of Zero Trust principles in the pipeline {#-aplicação-de-princípios-de-zero-trust-no-pipeline}

- **Zero trust between repositories, runners, artefacts and environments** - each element must be authenticated, validated and isolated;
- All pipeline commands must assume that the runner may be malicious, and vice versa;
- Integration with external authorisation services (e.g. Rego/OPA, ZTA gateways).

> **Canonical principle:**  
> Zero Trust in CI/CD does not mean “automating trust”, but rather **automating continuous verification**, keeping critical decisions outside the implicit control of automatic mechanisms.

---

## 📦 Control of external components used in the pipeline {#-controlo-de-componentes-externos-utilizados-no-pipeline}

- Restrictions on GitHub Actions or third-party scripts:  
  - Allow only internal actions or actions of validated origin;
  - Mandatory use of `@sha` (digest) or `@version` pinning;
- Validation of the integrity of remote files before execution;
- Audit of the artefacts used in scanner tools (e.g. updates of CVE databases, linters).

These practices treat external components as **supply chain dependencies**, subject to:
- explicit approval,
- traceability,
- periodic review.

---

## 🕵️ Monitoring and anomaly detection in pipelines {#️-monitorização-e-deteção-de-anomalias-nos-pipelines}

- Analysis of anomalous behaviour in CI/CD pipelines (e.g. irregular execution time, new step added, new external domain contacted);
- Centralised logging with alerts for events such as:
  - Execution outside usual hours;
  - Changes to pipeline files without an approved pull request;
  - Runners executing jobs outside their defined scope.

> Beyond detection, these capabilities must produce **preservable evidence**, with adequate retention and correlation between event, pipeline, artefact and decision taken.

---

## 📑 Continuous governance and cross-validation {#-governação-contínua-e-validação-cruzada}

- Integration with the organisational catalogue of applications and risk classification;
- Periodic verifications that:
  - L3 applications keep the mandatory controls active;
  - Exceptions are being reviewed;
  - YAML templates and workflows are up to date and signed;
- Formal versioning of the security policies applied in pipelines.

Continuous governance ensures that **automation does not degrade control**, and that deviations are detected before they become structural.

---

## 🧭 Process risks reinforced by these practices {#-riscos-de-processo-reforçados-por-estas-práticas}

Beyond technical risks, these advanced recommendations explicitly mitigate **process** risks, such as:

- Non-determinism of the pipeline and loss of reproducibility;
- Implicit bypass of gates through outputs or recommendations;
- Dilution of responsibility in promotions and exceptions;
- Plausible evidence without underlying empirical execution;
- Lack of early detection of operational deviations.

---

## 📉 Additional mitigated risks {#-riscos-adicionais-mitigados}

- Execution of malicious external code without control (OSC&R: CI0001, CI0011);
- Intentional bypasses with operational impact (OSC&R: CI0002, CI0014);
- Untracked use of outdated or insecure actions/scripts;
- Detection failures due to the absence of a feedback loop (OSC&R: SC0006, CI0016).

---
