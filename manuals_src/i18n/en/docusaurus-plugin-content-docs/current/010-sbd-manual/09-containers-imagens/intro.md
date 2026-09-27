---
id: intro
title: Containers and Isolated Execution
description: Principles, practices and controls for building, validating and running images in a secure, auditable and traceable way
tags:
  [containers, imagens, supply-chain, proveniencia, assinatura, slsa, ssdf,
   registry, runtime-hardening, admission-control, kubernetes, cicd, dSOMM]
sidebar_position: 0
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/intro.md
  source_sha256: f858d32630ac43798d22070cc21fb99bd0537f6cd12643f1e95367c190a1e197
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: bd747d1f37c095a16c8938692819306701bcc07c94a60678e90687b44bc15868
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [audit_trail, basilar, chapter_role, cycle_iteration, discipline, papel_suporte, provenance, sbdtoe_sbd, traceability, transversal, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: 855fad3feb18e4ab4c0f258285e9e08ece188014987b04a5acfcebaf47904d37
  translated_at: 2026-09-26T09:58:24Z
  stamped_at: 2026-09-26T18:35:00Z
  reviewed_by: null
---

import ChapterTypeCallout from '@site/src/components/ChapterTypeCallout';

<ChapterTypeCallout kind="operacional" title="Capítulo Operacional">

This chapter is considered **operational** in the *Security by Design – Theory of Everything (SbD-ToE)* model.
Its function is to **apply, automate and validate** the practices defined in the foundational chapters, guaranteeing their continuous, measurable and auditable execution.

The operational chapters explicitly assume the extensive use of automation in the modern SSDLC and address the **risks introduced by the execution process itself**, not only by the technology used.

</ChapterTypeCallout>


# Containers and Isolated Execution

Execution in containers has become the norm in CI/CD pipelines and in production.  
This ubiquity has brought significant gains in agility and portability, but it has introduced **new process risks** when the building, validation and promotion of images come to be heavily mediated by automated pipelines.

Today, images are frequently **derived, generated, recombined or promoted automatically**, often without direct human intervention.  
In this context, governance failures - and not only technical failures - become the dominant vector of compromise.

Real cases illustrate this risk: *typosquatting* attacks on public registries, secrets embedded in images exploited in Kubernetes environments (as in the **Tesla Kubernetes breach, 2018**), and supply chain incidents such as **SolarWinds** demonstrate that **apparently valid artefacts can be operationally insecure**.

This chapter therefore establishes the foundations for **trustworthy, traceable and auditable** execution, treating containers as **complete software artefacts**, subject to explicit human decision, independent validation and verifiable evidence throughout the entire cycle.

👉 The objective is not only to ensure that “the container runs”, but to ensure that **it runs by conscious decision, with known risk and sufficient evidence**.


The requirements prescribed here apply both to:
- pipeline images (*builders*, *runners*, technical jobs),
- and to application images executed at runtime (services, workloads, batch jobs).

In both cases, automation **produces signals**, not decisions.  
Risk acceptance, promotion between environments and the authorisation of execution are **non-delegable human responsibilities**.

This chapter is directly linked with:
- **Ch. 05 - Dependencies, SBOM and SCA**, treating images as *supply chain artefacts* with verifiable provenance;
- **Ch. 07 - Secure CI/CD**, where the pipeline is recognised as a critical risk actor;
- **Ch. 12 - Monitoring and Operations**, which ensures detection and response at runtime.

---

## 🧭 What it covers technically {#-o-que-cobre-tecnicamente}

Container security depends on a **continuous chain of controls**, from the design of the pipeline to execution in production.  
Any break in this chain compromises overall trust.

This chapter covers, in an integrated way:

- Selection, validation and **deterministic pinning** of base images.
- Execution in controlled environments (builders, runners, clusters).
- Signing and verification of provenance (e.g. SLSA, Sigstore).
- Runtime hardening (non-root, minimal capabilities, read-only FS).
- Execution and admission policies (OPA, Kyverno).
- Secure integration with Kubernetes (RBAC, dedicated ServiceAccounts, NetworkPolicy).
- Generation of SBOM and **commit → pipeline → image → execution** traceability.

These practices do not replace human decision; they provide **technical evidence** that supports that decision.

---

## 🧪 Governance pillars {#-pilares-de-governação}

Without explicit governance, automation quickly degrades into implicit trust.  
This chapter defines minimum pillars that guarantee **continuous operational discipline**:

1. **Registry allowlist and execution by digest**, preventing silent substitutions.
2. **Secrets management outside the image**, with ephemeral and auditable credentials.
3. **Minimal RBAC and dedicated ServiceAccounts**, never the *default SA* at L2/L3.
4. **NetworkPolicies with controlled egress**, limiting the *blast radius*.
5. **Golden Base Images per stack**, with a patching and discontinuation SLA.
6. **Ephemeral, minimal and signed builders and runners**, protecting the build chain.

🔬 In L3 contexts, reinforced controls also apply, such as **advanced isolation (gVisor, Kata, Firecracker)**, *drift* detection and **staged promotion with explicit approval**.

---

## ⚙️ How it must be done {#️-como-deve-ser-feito}

Secure practice requires **formal, repeatable and auditable** mechanisms.  
“Plausible” or “green” results do not replace empirical validation.

In a non-exhaustive way:

- Use minimalist, maintained and verified base images.
- Sign images and verify provenance before execution.
- Integrate scanners into CI/CD as a **signal**, with gates defined by policy.
- Run containers with minimum privileges.
- Apply admission policies on origin, digest, identity and context.
- Generate an SBOM at every build and link the results to the pipeline.
- Keep auditable records of the acceptance and promotion decision.

These steps are mandatory because they **reduce uncertainty**, not because they eliminate risk.

---

## 📆 When to apply {#-quando-aplicar}

The controls must exist from the design of the pipeline and be maintained throughout the cycle:

- Design and evolution of CI/CD.
- Selection and maintenance of base images.
- Every build and release.
- Before any promotion or deploy.
- After critical CVEs or structural changes.

Continuous application avoids the silent accumulation of risk.

---

## 👥 Who is involved {#-quem-está-envolvido}

Container security is cross-cutting:

| Role                   | Main responsibility |
|-------------------------|----------------------------|
| **DevOps / SRE** | Define approved images, secure runners and enforcement |
| **Developer**       | Use validated images and integrate controls into manifests |
| **AppSec Engineer**  | Validate the chain of trust and analyse technical signals |
| **DevOps / SRE**     | Guarantee isolation and policies in the cluster |
| **GRC / Compliance** | Maintain evidence, traceability and policies |

The absence of any one of these roles compromises the entire chain.

---

## 🎯 What for {#-para-quê}

Insecure containers directly compromise organisational integrity.

This chapter makes it possible to:
- Prevent the execution of tampered code.
- Reduce the attack surface in the pipeline and in production.
- Support audits with verifiable evidence.
- Meet requirements such as NIS2, SSDF and SLSA.
- Respond quickly to incidents at runtime.

Agility is only an advantage when accompanied by **operational trust**.

---

## 🧮 Proportional application L1–L3 {#-aplicação-proporcional-l1l3}

Not all applications need the same level of control, but all of them need some.  
Proportionality makes it possible to balance cost, risk and complexity:

| Practice                  | L1 (low) | L2 (medium) | L3 (high/crit.) |
|---------------------------|------------|------------|-----------------|
| Image scanner        | Warning      | Blocking High/Critical | Blocking Medium+ |
| Signing + SLSA         | Recommended| Recommended| Mandatory |
| Digest-only / allowlist   | Warning      | Blocking by origin | Blocking + digest-only |
| Secrets outside the image   | Recommended| Mandatory| Mandatory + automatic rotation |
| Dedicated RBAC/SA         | Recommended| Mandatory| Mandatory + periodic review |
| NetworkPolicy egress      | Basic ingress | Ingress + critical egress | Ingress + full egress + audit |
| Golden base + patch SLA   | Recommended| Mandatory| Mandatory + accelerated rollout |
| Ephemeral builders       | Recommended| Mandatory| Mandatory + network segmentation |
| Sandboxes (gVisor/Kata)   | -          | -          | Recommended for sensitive data |
| Drift & staged promotion | -          | -          | Mandatory in regulated environments |

---

## 📜 Relevant Organisational Policies {#-políticas-organizacionais-relevantes}

Formal policies give these practices sustainability.  
They ensure that the practices do not depend solely on individual discipline, but on collective and auditable rules.

| Organisational policy         | Mandatory | Application | Minimum content |
|---------------------------------|-------------|-----------|-----------------|
| [Secure Containers Policy](/sbd-toe/assets/policies/policy-containers-seguros)  | Yes         | All projects | Allowlist + digest-only, scanners, signing/provenance, RBAC/SA, NetworkPolicy |
| [Secrets Management Policy](/sbd-toe/assets/policies/policy-gestao-segredos)  | Yes         | DevOps / SRE, AppSec Engineer | OIDC/short TTL, prohibition of secrets in the image, rotation |
| [Traceability Policy](/sbd-toe/assets/policies/policy-rastreabilidade)     | Recommended | GRC / Compliance | commit→pipeline→deploy logs, retention, immutable export |
| [Golden Base Images Policy](/sbd-toe/assets/policies/policy-golden-base-images)  | Yes         | DevOps / SRE, AppSec Engineer | Catalogue, patching SLA, deprecation |
| [Secure CI/CD Policy — Builders/Runners](/sbd-toe/assets/policies/policy-cicd-seguro)    | Recommended | DevOps / SRE | Ephemeral, minimal, signed, controlled cache |

---
