---
id: assinatura-cadeia-trust
title: Image Signing and Chain of Trust
description: Validation of the provenance and integrity of container images as technical evidence, not as an execution decision
tags: [containers, assinatura, trust, notary, cosign, rekor, supply-chain]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/addon/03-assinatura-cadeia-trust.md
  source_sha256: f895b14dc3558ece17085b6a4b43f4b039ef247b91be4887484b1c3bed7118ab
  source_commit: 0866ff96fdef02aa75e70c17c9ea0a919e437310
  target_sha256: 9433381ad71008ceee2afe0aaaee890ac456daf4514537b99c6f484c174b5ab4
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 58969e2d675e7d50a5a5dfa4be392be5d340a032c3290dc90c7ef1fe2101a3d2
  glossary_keys: [audit_trail, avaliacao, framework_source_corpus, practitioner_manual, provenance, traceability, validation_evaluation, verification_taxonomy]
  glossary_sha256: 5f4946fde7e0d1dc1d2022a032b6aea751e48f5d9e54ad9c1313303a7f55d500
  translated_at: 2026-09-26T12:48:47Z
  reviewed_by: null
---

# Image Signing and Chain of Trust

## 🌟 Objective {#-objetivo}

Ensure that all container images used in pipelines, execution environments and production **have technically verifiable provenance and integrity**, through digital signing mechanisms and an auditable record.

Signing and the chain of trust **do not grant authorisation to execute**.  
They provide **objective evidence** that supports human decisions on the acceptance, promotion and execution of images.

This file defines how to produce and verify that evidence consistently.

---

## 🧬 What the chain of trust in images is {#-o-que-é-a-cadeia-de-confiança-em-imagens}

The **chain of trust** applied to container images makes it possible to answer, verifiably, fundamental questions:

- Who produced this image?
- In what context was it built?
- Was the image modified after the build?
- Is there continuity between build, signing and execution?

Technically, the chain of trust includes:

- **Digital signing of the image** at build time;
- **Verification of the signature** before its use;
- **Immutable record of the signature** (e.g. transparency log);
- **Association between the image, the pipeline and the producing entity**.

> 🎯 Signing guarantees **integrity and provenance**.  
> The decision to execute the image depends on criteria of risk, context and governance, addressed elsewhere in the Manual.

---

## ⚠️ Signing is not authorisation {#️-assinatura-não-é-autorização}

It is essential to avoid an incorrect, yet common, interpretation:

- ✔️ *Signed image* → integrity proven  
- ❌ *Signed image* ≠ automatically approved image

An image may be:
- technically intact,
- from a legitimate source,
- correctly signed,

and **still not be suitable** for the context in which it is intended to run.

The acceptance decision must consider:
- the environment (DEV, QA, PROD);
- the criticality of the application (L1–L3);
- the data processed;
- the residual risk identified in other controls.

This separation is fundamental to avoid **implicit trust induced by automation**.

---

## 📘 Recommended tools and mechanisms {#-ferramentas-e-mecanismos-recomendados}

| Component          | Tool / Standard | Technical function                                             |
|--------------------|---------------------|-------------------------------------------------------------|
| Signing         | Cosign              | Sign images with a key or federated identity (OIDC)     |
| Transparency Log   | Rekor               | Immutable and auditable record of signatures                 |
| Verification        | Cosign + controllers| Technical verification before execution                       |
| OCI alternative    | Notary v2           | Native signing of OCI artefacts                         |

These tools **produce cryptographic evidence**, not decisions.

---

## 🛠️ How to apply signing and verification {#️-como-aplicar-assinatura-e-verificação}

Correct application of the chain of trust must follow a clear sequence:

1. **Sign the image at build time**, using a private key or federated identity;
2. **Publish the signature together with the image**, as OCI metadata;
3. **Record the signature in a transparency log**, ensuring immutability;
4. **Technically verify the signature** before any use;
5. **Associate verification with technical policies**, without replacing governance;
6. **Make the evidence available** to support human decision;
7. **Protect the keys and identities** used for signing.

Automatic verification **does not eliminate** the need for contextual assessment.

---

## 📂 Storage, versioning and traceability {#-armazenamento-versionamento-e-rastreabilidade}

- Signatures must reside **alongside the image** in the registry;
- Use digests and stable identifiers;
- Correlate the signature with:
  - commit,
  - pipeline,
  - build ID;
- Optionally reference the signature in the SBOM.

Traceability must make it possible to reconstruct the complete path of the image.

---

## ✅ Good practices {#-boas-práticas}

- Prefer OIDC identities to reduce manual key management;
- Prohibit execution of unsigned images at L2/L3;
- Clearly separate:
  - technical verification (automatic),
  - risk acceptance (human);
- Use execution policies to **block the absence of evidence**, not to grant implicit trust;
- Review signatures and acceptance criteria in the event of an incident or a change of context.

---

## 📎 Cross-references {#-referências-cruzadas}

| Document                         | Relation to the chain of trust              |
|----------------------------------|------------------------------------------------|
| `01-imagens-base.md`             | Signing after approval of the base image       |
| `05-policies-runtime-opa.md`    | Technical enforcement of verification             |
| `06-inventario-sbom.md`         | Link between composition and integrity         |
| `09-riscos-processo-imagens.md` | Separation between evidence and decision            |
| `25-rastreabilidade.md`         | Auditable demonstration of integrity          |

> 🔐 Image signing is a **technical pillar of trust**,  
> but **operational trust only exists when there is an explicit human decision supported by evidence**.
