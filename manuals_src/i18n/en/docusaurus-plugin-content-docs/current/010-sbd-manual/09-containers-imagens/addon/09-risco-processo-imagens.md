---

id: riscos-processo-imagens
title: Process Risks in the Building, Validation and Promotion of Images
description: Identification and mitigation of the risks introduced by automation in the chain of building, validation and execution of container images
tags: [containers, imagens, risco-processo, pipeline, decisao-humana, evidencias, supply-chain, proveniencia, cicd, sbd-toe]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/addon/09-risco-processo-imagens.md
  source_sha256: 321405787c36d866718c937bfdfd6f4e30b4636efd29f56a990f6d20ac170352
  source_commit: 4430e7c4ca4536589773f3f465bd05857a1e6c38
  target_sha256: 5d71a909aaced6576848fe00336975241f0a636653b6d4d9eeaa45dfcd60d100
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [avaliacao, chapter_role, maturity, prescriptive, provenance, requirement_runtime, sbdtoe_sbd, threat, traceability, transversal, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: f997f93a72f1e91be3b9d1e22be5c159f1bddd9d6112b365dcee2355914c7f9a
  translated_at: 2026-09-26T09:58:48Z
  stamped_at: 2026-09-26T18:34:54Z
  reviewed_by: null
---

# 🛠️ Process Risks in the Building, Validation and Promotion of Images

The building and execution of container images is today, in most organisations, a **heavily automated process**.
Dockerfiles, manifests, pipelines, policies and promotions between environments are frequently **generated, applied and executed without direct human intervention**.

This reality introduces **specific process risks**, distinct from the classic technical risks (vulnerabilities, misconfigurations, CVEs), which must be addressed explicitly.

This file establishes the canonical framework for those risks in SbD-ToE.

---

## 🎯 Scope and fundamental principle {#-âmbito-e-princípio-fundamental}

This document **does not address image vulnerabilities** - those are covered in other files of the chapter.
Here, only the **risk introduced by the way images are produced, assessed and accepted** is addressed.

> **Central principle:**
> Tools produce **signals**.
> Risk acceptance is always a **human decision**, based on verifiable evidence.

Any process that violates this separation is considered **insecure by design**, even if technically “correct”.

---

## 🧩 Typical risk chain in automated environments {#-cadeia-típica-de-risco-em-ambientes-automatizados}

In modern environments, the most common chain of events is:

1. An artefact (Dockerfile, manifest, pipeline) is created or changed.
2. The pipeline automatically builds an image.
3. Automated tools produce signals (scans, policies, signatures).
4. The image is promoted to another environment.
5. The workload is executed in production.

⚠️ In many contexts, **no explicit human decision occurs between steps 2 and 5**.

This file identifies where that model fails.

---

## 🚨 Categories of process risk {#-categorias-de-risco-de-processo}

### 1️⃣ Confusion between automatic signal and decision {#1️⃣-confusão-entre-sinal-automático-e-decisão}

**How it arises**

* “Build passed” is interpreted as “secure image”.
* “No findings” is interpreted as “no risk”.
* “Policy applied” is interpreted as “execution authorised”.

**Risk**

* Implicit acceptance of unassessed risk.
* Absence of an identifiable owner.
* Impossibility of justifying decisions after the fact.

**Prescribed mitigation**

* Define explicit points of human decision (acceptance, exception, promotion).
* Record who decided, and on the basis of what evidence.

**Expected evidence**

* Versioned record of the decision.
* Clear link between the technical signal and the decision taken.

**Relates to.** Violates `CIC-011`; materialises `MT-128`.

---

### 2️⃣ Illusion of security through successful automation {#2️⃣-ilusão-de-segurança-por-automação-bem-sucedida}

**How it arises**

* Excessive trust in scanners or policies.
* Assumption that automated coverage is exhaustive.
* Undervaluing of residual risk.

**Risk**

* Undetected vulnerabilities.
* Context ignored (e.g. real impact, exposure).
* False sense of control.

**Prescribed mitigation**

* Treat automatic signals as **inputs**, not conclusions.
* Require human analysis for relevant residual risk.

**Expected evidence**

* Documented justification for acceptance or mitigation.
* Link to organisational risk criteria.

**Relates to.** No linkable requirement in the current catalogue; materialises `MT-149`.

---

### 3️⃣ Automatic promotion between environments {#3️⃣-promoção-automática-entre-ambientes}

**How it arises**

* Automatic promotions DEV → QA → PROD.
* Uncritical reuse of the same image.
* Lack of contextual revalidation.

**Risk**

* Propagation of errors or wrong decisions.
* Execution in more sensitive contexts without a new assessment.

**Prescribed mitigation**

* Staged promotion with explicit approval at L2/L3.
* Revalidation of policies and provenance per environment.

**Expected evidence**

* Promotion records with an identified owner.
* Evidence of validation per environment.

**Relates to.** Violates `CIC-004`; no linkable threat in the current catalogue.

---

### 4️⃣ Verified provenance ≠ granted trust {#4️⃣-proveniência-verificada--confiança-concedida}

**How it arises**

* Signatures and attestation treated as implicit authorisation.
* Lack of distinction between integrity and suitability.

**Risk**

* Execution of legitimate but unsuitable artefacts.
* Inability to revoke contextual trust.

**Prescribed mitigation**

* Separate integrity verification from the execution decision.
* Define organisational trust criteria.

**Expected evidence**

* Explicit image acceptance policy.
* Decision records associated with provenance.

**Relates to.** Violates `CNT-009`; materialises `MT-162`.

---

### 5️⃣ Absence of decision traceability {#5️⃣-ausência-de-rastreabilidade-decisional}

**How it arises**

* Technical logs without decision context.
* Lack of a link between commit, pipeline, image and execution.

**Risk**

* Inconclusive audits.
* Difficulty in responding to incidents.
* Diffuse accountability.

**Prescribed mitigation**

* Complete traceability:
  **commit → pipeline → image → decision → execution**

**Expected evidence**

* Correlatable identifiers.
* Adequate retention of records.

**Relates to.** Violates `CIC-005`; materialises `MT-155`, `MT-164`.

---

## 🧭 Canonical SbD-ToE rules applicable to images {#-regras-canónicas-sbd-toe-aplicáveis-a-imagens}

This chapter inherits and makes concrete the following global invariants of SbD-ToE:

* Separation between **suggestion** and **decision**
* Evidence above plausibility
* Reproducibility and auditability
* Explicit human accountability
* End-to-end traceability

Any implementation that violates these principles must be considered **non-compliant**, regardless of its apparent technical maturity.

---

## 🔗 Link to the other files of the chapter {#-ligação-aos-restantes-ficheiros-do-capítulo}

This file is **cross-cutting** and must be read together with:

* `01-imagens-base.md` - selection and initial validation
* `03-assinatura-cadeia-trust.md` - integrity and provenance
* `05-policies-runtime-opa.md` - technical enforcement
* `06-inventario-sbom.md` - traceability of components
* `exemplo-pipeline-container.md` / lifecycle - operationalisation

It provides the **semantic framework** that gives prescriptive meaning to the technical controls described in those documents.

---

## ✅ Compliance criterion {#-critério-de-conformidade}

An organisation can only claim that it applies this chapter correctly if it can demonstrate, for any image in execution:

1. Who decided its acceptance.
2. On the basis of what technical evidence.
3. In what risk context.
4. When and for how long that decision is valid.

Without these answers, there is no operational trust - only automation.
