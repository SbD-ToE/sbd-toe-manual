---
id: policies-runtime-opa
title: Technical Enforcement of Runtime Policies with OPA and Kyverno
description: Automatic application of formal policies to block non-compliant executions, without replacing human decision
tags: [opa, kyverno, policies, enforcement, kubernetes, runtime, containers]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/addon/05-policies-runtime-opa.md
  source_sha256: f9c5235b889e7351d74ba316255ff1964f3c0221fdc2859acec7a12bafa3b7fa
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 7c3889e69b6328404ddd017f37e5835755c7e61c3604aabaaa7ab28294ed2338
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [avaliacao, chapter_role, cycle_iteration, lifecycle_phase, papel_suporte, requirement_runtime, sbdtoe_sbd, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 77f25fbd7507df5a9b2412df320d942d7fc4ec436de09ff10ab5c913ddae2f1d
  translated_at: 2026-09-26T09:58:16Z
  stamped_at: 2026-09-26T18:34:51Z
  reviewed_by: null
---

# Technical Enforcement of Runtime Policies with OPA and Kyverno

## 🌟 Objective {#-objetivo}

Ensure that *containers* **that do not meet the minimum security requirements defined by the organisation cannot be executed**, through formal and automatic enforcement mechanisms, namely in **Kubernetes and CI/CD pipelines**.

The policies described in this chapter **do not decide whether a container is acceptable**.  
They **prevent manifestly non-compliant executions**, providing a **technical blocking mechanism** that supports - but does not replace - governance and human decision.

This file defines how to use OPA, Kyverno and equivalent mechanisms **as technical guardrails**, not as a risk authority.

---

## 🧬 What execution policies are (in the SbD-ToE model) {#-o-que-são-políticas-de-execução-no-modelo-sbd-toe}

**Execution policies** are formal rules evaluated automatically at the moment a workload is created. In the SbD-ToE model, they serve to:

- **Block known insecure configurations**;
- **Impose non-negotiable minimum requirements**;
- **Produce objective evidence of non-compliance**;
- **Reduce the margin of operational error** in automated environments.

> 🔒 A policy **never grants authorisation** - it only **refuses the absence of minimum requirements**.

Risk acceptance, the granting of exceptions and promotion between environments **are always explicit human decisions**, handled outside the policy mechanism.

---

## ⚠️ Enforcement is not risk acceptance {#️-enforcement-não-é-aceitação-de-risco}

A common conceptual error is to assume that:

- workload approved by policy = secure workload
- execution allowed = risk accepted

In SbD-ToE, this equivalence is **explicitly prohibited**.

Policies:
- validate **objective minimum conditions**;
- do not assess context, impact or residual risk;
- do not replace analysis or accountability.

An execution may:
- comply with all policies,
- be technically correct,
- and **still not be acceptable** for a given context (e.g. PROD, sensitive data, L3).

---

## 📘 Recommended tools and mechanisms {#-ferramentas-e-mecanismos-recomendados}

| Tool              | Technical function                                         | Role in SbD-ToE                    |
|-------------------------|--------------------------------------------------------|-------------------------------------|
| **OPA (Gatekeeper)**    | Evaluation of Rego rules at admission time             | Technical blocking                    |
| **Kyverno**             | Declarative policies in YAML                         | Blocking and controlled mutation       |
| **Admission Webhooks** | Custom validation                                  | Specific enforcement              |
| **CI/CD validators**  | Early checks (e.g. OPA, Checkov, Semgrep)        | Reduction of failures before runtime  |

These tools **produce binary technical decisions (allow / deny)** - not risk decisions.

---

## 🛠️ How to apply policies correctly {#️-como-aplicar-políticas-de-forma-correta}

### 1️⃣ Define non-negotiable minimum requirements {#1️⃣-definir-requisitos-mínimos-não-negociáveis}

Typical examples:
- Execution as a non-root user;
- Prohibition of privileged containers;
- Use of images from authorised registries;
- Signature verification (integrity);
- Application of a minimum `securityContext`.

These requirements must be:
- clear,
- objective,
- technically verifiable.

---

### 2️⃣ Implement policies as code {#2️⃣-implementar-políticas-como-código}

- Use Rego (OPA) or YAML (Kyverno);
- Version them in Git, alongside the infrastructure;
- Apply them via GitOps;
- Associate each policy with an explicit organisational requirement.

---

### 3️⃣ Test and apply progressive enforcement {#3️⃣-testar-e-aplicar-enforcement-progressivo}

- Start in `audit` mode;
- Analyse rejections and false positives;
- Communicate the rules to the teams;
- Activate `enforce` only after validation.

The aim is to **reduce error**, not to create opaque blockages.

---

## 📂 Where to keep policies and how to govern them {#-onde-manter-políticas-e-como-governar}

- Dedicated Git repository (`policies/`);
- Versioning and change history;
- Differentiated application per environment;
- Immutable logs of rejections and compliant executions;
- Formal process for temporary exceptions.

Any exception **outside the policy** must be:
- explicitly approved;
- time-limited;
- traceable.

---

## 🔍 Relation to human decision {#-relação-com-decisão-humana}

In the SbD-ToE model:

- **Policies** block what is objectively insecure;
- **People** decide what is acceptable.

This separation ensures:
- clear accountability;
- real auditability;
- prevention of implicit trust induced by automation.

Without this distinction, the policy becomes an undue substitute for governance.

---

## ✅ Good practices {#-boas-práticas}

- Treat policies as *guardrails*, not as a seal of approval;
- Keep policies simple, objective and justified;
- Clearly separate:
  - technical enforcement,
  - risk decision,
  - formal exception;
- Review policies after incidents or platform changes;
- Document the rationale for each rule applied.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                         | Relation to enforcement                        |
|----------------------------------|------------------------------------------------|
| `01-imagens-base.md`             | Blocking of unapproved images              |
| `03-assinatura-cadeia-trust.md` | Integrity verification as evidence      |
| `04-hardening-containers.md`    | Enforcement of minimum restrictions              |
| `09-riscos-processo-imagens.md` | Separation between signal, blocking and decision      |
| `15-aplicacao-lifecycle.md`     | Operational integration into the lifecycle        |

> 🧩 Policies are **technical limits**, not trust decisions.  
> When a policy decides on people's behalf, governance has already failed.
