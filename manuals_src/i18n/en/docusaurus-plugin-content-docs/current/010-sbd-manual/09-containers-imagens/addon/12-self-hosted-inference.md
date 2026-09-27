---
id: self-hosted-inference
title: Self-Hosted AI Inference — Runtimes, Isolation and Weights
description: Operational patterns for serving self-hosted AI models (vLLM, Ollama, TGI, llama.cpp, NVIDIA Triton) — workload isolation, weight management, protection of inference, AI-specific container hardening.
sidebar_position: 12
tags: [ai, ml, inference, runtime, vllm, ollama, tgi, triton, gpu, hardening, self-hosted, weights]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/addon/12-self-hosted-inference.md
  source_sha256: d049f3df8a7e680b4ce1b91172da6801ff91c4f41e2ceb01acee6a6463eb1c75
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: c0d5b1625618cb4602e6bfa75b363c531f33c4fa9620903ac1ff80cdd0689e9e
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [cycle_iteration, framework_source_corpus, lifecycle_phase, llm, maturity, risk_level, verificacao_check, verification_taxonomy]
  glossary_sha256: b1a57ddada5120e0dc38882dbf7de3f9d588fbd9bceebe6e93f4fc1fd477dcac
  translated_at: 2026-09-26T09:58:20Z
  stamped_at: 2026-09-26T18:34:55Z
  reviewed_by: null
---

# Self-Hosted AI Inference — Runtimes, Isolation and Weights

## Why *self-hosted* inference is treated as a case of its own {#porque-trata-se-a-inferência-self-hosted-como-caso-próprio}

In 2026 many teams operate healthy mixes of **models consumed via an external *provider*** (Anthropic, OpenAI, Google) with **models served internally** — whether because the data is sensitive and cannot leave the perimeter, because the economics change when usage is high, or because the team wants full control over the model's lifecycle. *vLLM*, *Ollama*, *Text Generation Inference (TGI)*, *llama.cpp* and *NVIDIA Triton Inference Server* have become mainstream *runtimes* for that use.

What changes compared with a traditional web application is not the category of the problem — it is still runtime *hardening* — but three concrete elements:

1. **The model weights are a critical asset** that lives *at rest* in the infrastructure. They are not "configuration"; they are the *core of the product* materialised in bytes.
2. **The workload typically runs on a GPU** (or an equivalent accelerator). Shared GPUs have an operational isolation posture that is still maturing — caution is worthwhile.
3. **The *runtime* exposes APIs with new semantics** — *chat completions*, *embeddings*, *tool use*, *streaming* via SSE/WebSocket. Conventional *hardening* covers a good part; the rest requires adaptation.

This section complements [`ARC-014`](../../arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014), [`ARC-015`](../../arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) and [§4 — Container *Hardening*](./hardening-containers) with the specialisation for *inference runtimes*.

---

## Inventory of relevant runtimes (2026) {#inventário-de-runtimes-relevantes-2026}

| Runtime | Consumption model | Typical use |
|---|---|---|
| **vLLM** | OpenAI-compatible API; Python server | Serving LLMs at large scale with *paged attention* |
| **Text Generation Inference (TGI)** | HF-compatible API; *gRPC* / HTTP | Serving HuggingFace models in production |
| **Ollama** | Simple REST API; local model management | Workstations and *air-gapped* environments; *edge* use |
| **llama.cpp** (server) | Minimalist REST API | CPU-only or minimal GPU; single binary |
| **NVIDIA Triton Inference Server** | gRPC/HTTP; multi-framework (TF, PyTorch, ONNX, TensorRT) | Enterprise-class multi-model inference |
| ***Custom* serving** (FastAPI + transformers) | Bespoke API | Cases with specific requirements not covered by the above |

No prescription is made between runtimes — they are chosen on the basis of scale, available *hardware*, the model's licence requirements and the team's operational maturity. The patterns below apply to all of them.

---

## Operational patterns {#padrões-operacionais}

### 1. The model weights are a critical asset {#1-os-pesos-do-modelo-são-activo-crítico}

The model weights — `.safetensors`, `.gguf`, `.bin`, `.onnx`, *checkpoints* — receive **the same treatment as secrets at runtime**, with three specialisations:

- **Encryption *at rest*** on the *volume* / *object store* where they live; keys managed in the organisation's vault (cross-link [Policy 18](/sbd-toe/assets/policies/policy-gestao-segredos)).
- **Integrity verified before loading** — SHA-256 hash of the artefact declared in the AI BOM ([`DEP-012`](../../dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012)) and validated at runtime *startup*. It mitigates `AML.T0109` *Supply Chain Rug Pull* locally: if someone swaps the file in *storage*, the runtime refuses to load it.
- **Access control to the *artefact registry*** that serves the weights — not the whole team needs direct *download* of the `.safetensors` files. Limit it to the runtimes' *service accounts* + a restricted set of operators.

> 💡 Commercial *self-hosted* models under licence (e.g. licences with usage restrictions) add the obligation to **audit who performed a *download*** — the organisation's *artefact registry* must be able to answer "who downloaded this model, when, in which environment". The licence may require it; even when it does not, it is good hygiene.

### 2. Isolation of the inference workload {#2-isolamento-do-workload-de-inferência}

Inference typically runs on a GPU, and shared GPUs have an isolation posture that deserves careful consideration:

- ***Hard isolation*** when possible — a pod with a dedicated GPU via the *NVIDIA GPU Operator* + *MIG (Multi-Instance GPU)* or equivalent on AMD/Intel hardware. Two different *tenants* do not share the same SM/CU.
- ***Process-level isolation* when *hard isolation* is not viable** — *MPS (Multi-Process Service)* + cgroup limits + namespaces. Defence in depth is important here, given that *side-channels* on shared GPUs are an area of active research (e.g. work on *cross-tenant timing* since 2023). Academic paranoia is not required in production, but operational awareness of the risk is.
- **Do not mix sensitive inference with user workloads on the same node** — if the end user can execute code on the same *host* where inference runs (a common case in *notebook* platforms such as *JupyterHub*), this is a co-located adversary. Separate them.
- **Explicit resource limits** — `--gpu-memory-utilization`, VRAM *quota*, batch size *quota*. Without limits, a malicious *prompt* with an extreme `max_tokens` can degrade the service (a specialised case of the classic DoS category).

### 3. Hardening of the inference container {#3-hardening-do-container-de-inferência}

The principles of [§4 — Container *Hardening*](./hardening-containers) apply, with the following specialisations:

- ***Read-only* filesystem** except for *paths* explicitly required by the runtime (cache, profiling). vLLM and TGI support a *read-only root*.
- ***Drop capabilities*** — `cap_drop: ALL`; add **only** what is necessary (no privileged capability should be required by a modern *inference runtime*).
- ***Non-root* user** — verify that the runtime image runs as a non-root UID; several *upstream* images still use root by default (historical HF *transformers*, some *Ollama base images*) — overriding is necessary.
- **Restrictive *network policy*** — the inference pod accepts traffic only from the *gateway* / *load balancer* of the consuming application; egress only to the *artefact registry* (weights), telemetry (Ch. 12) and — when applicable — the secrets vault. No arbitrary *internet* egress; in particular, **no access to public *registries* at runtime** (the transfer of weights takes place at *startup*, not at *runtime*).
- **Curated base image** — prefer the runtime *vendor*'s official images; apply [§3 — Signing and Chain of Trust](./assinatura-cadeia-trust). *Third-party* images without a signature are quarantined (a non-trivial number of popular Docker Hub images for AI inference have been reported with *artefacts* or *malicious payloads* since 2024).

### 4. Inference APIs — specific *hardening* {#4-apis-de-inferência--hardening-específico}

The *runtime* exposes APIs with a new surface. Beyond conventional HTTP *hardening* (TLS, *rate limiting*, *auth*), the following apply:

- **Mandatory authentication** on all *endpoints*, even in "internal" environments. Several runtimes (classic Ollama, *llama.cpp server*) start **without authentication** by default — a defensible choice for a *workstation* but catastrophic on a shared network. Configure it before exposing them.
- **Consumption-based *rate limiting*** — not only requests per second; also tokens per window and total inference time. Cross-reference with [`OPS-013`](../../monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013) (*token budget*).
- ***Streaming endpoints* (SSE / WebSocket)** — verify the management of long connections; impose a maximum *timeout*; limit concurrent connections per *principal*.
- **Server-side `max_tokens` limit** — do not rely on the client alone. A *prompt* with `max_tokens=1000000` on a large model without a server imposing a limit is a ready-made DoS.
- ***Prompt size limit*** — a limit on the size of the accepted `prompt`. For models with a long context window (≥ 200k tokens in 2026), extremely long *prompts* have a non-linear computational cost; the server should refuse them above an operational limit.
- **Audit of consumption per *principal*** — who invoked, with what prompt size, with what `max_tokens`, on which *model / version*. It feeds [`OPS-011..014`](../../monitorizacao-operacoes/addon/catalogo-requisitos-operacoes).

### 5. *Pinned* runtime version {#5-versão-do-runtime-pinned}

The runtime (vLLM, TGI, etc.) is a supply-chain dependency like any other — explicit *pinning* (cross-link [`DEP-003`](../../dependencias-sbom-sca/addon/catalogo-requisitos-dependencias)), SCA active on base images, ongoing *vulnerability scanning*. Some critical dependencies in inference runtimes (`torch`, `transformers`, `vllm`, `cuda-toolkit`) have CVEs at a relevant cadence — they enter the normal flow of Ch. 05.

---

## Cross-checks and dependencies {#cross-checks-e-dependências}

- **Weights as an AI supply-chain dependency** — they enter the AI BOM ([`DEP-011`/`DEP-012`](../../dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011)) with hash, *provider*, licence and *pinned* version. A major version change requires an *eval suite* (Ch. 10 §C5) and a *threat review* (Ch. 03 US-11).
- **Inference cluster as an environment** — dedicated *workload identity* for the runtime ([`ARC-015`](../../arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) applied to the self-hosted case); the *runtime*'s identity is distinct from the identities of consuming applications.
- **Operations** — runtime telemetry enters [`OPS-011..014`](../../monitorizacao-operacoes/addon/catalogo-requisitos-operacoes); the operational *budget* may include GPU-hours (not only tokens) when the cost is the organisation's own compute.

---

## Proportionality by risk level {#proporcionalidade-por-nível-de-risco}

| Pattern | L1 | L2 | L3 |
|---|:--:|:--:|:--:|
| Weights encrypted *at rest* | Recommended | Mandatory | Mandatory |
| Hash verified at *startup* | Recommended | Mandatory | Mandatory |
| Hard GPU isolation | Not required | Recommended | Mandatory when sensitive workloads share hardware |
| *Read-only* container + *drop capabilities* + *non-root* | Recommended | Mandatory | Mandatory |
| Restrictive network policy | Recommended | Mandatory | Mandatory |
| Authentication on the *runtime API* | Mandatory (always — regardless of level) | Mandatory | Mandatory |
| *Rate limit* + *token budget* + server-side `max_tokens` | Recommended | Mandatory | Mandatory |
| Audit of weight *downloads* | Recommended | Recommended | Mandatory |
| *Pinned* runtime version + active SCA | Mandatory (same rule as for any dependency) | Mandatory | Mandatory |

---

## Frequent anti-patterns {#anti-padrões-frequentes}

- ❌ **Runtime exposed without authentication because "it is an internal network"** — in modern architectures the "internal network" includes too many *principals* for that boundary to be trusted as the only defence.
- ❌ **Weights in the Git repository** — a 70 GB `.safetensors` file in LFS solves one problem but creates another; prefer a dedicated *artefact registry* with access control and auditing.
- ❌ **GPU shared between *tenants* without configured isolation** — *side-channels* are under active research; even if unlikely in practice, the absence of explicit configuration is a posture gap.
- ❌ **`latest` runtime image** — violates [`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013) (cross-link with [`ARC-015`](../../arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)); inference becomes vulnerable to an unannounced *upgrade*.
- ❌ **`max_tokens` entrusted only to the client** — a server without an operational limit is a DoS ready to be exploited.
- ❌ ***Streaming endpoints* without a maximum *timeout*** — long connections consume GPU resources in models that keep a KV cache; without a limit, an attacker keeps the channel open and blocks capacity.

---

## References {#referências}

- **vLLM** — *paged attention* + inference server (OpenAI-compatible)
- **Hugging Face TGI** — Text Generation Inference
- **Ollama** — local runtime + model manager
- **llama.cpp** — CPU/GPU inference in C++
- **NVIDIA Triton Inference Server** — enterprise-class multi-framework inference
- **NVIDIA MIG (Multi-Instance GPU)** — *hard isolation* on Ampere/Hopper GPUs
- **NIST SP 800-190** — *Application Container Security Guide*
- **CIS Benchmarks — Docker, Kubernetes** — basis for container *hardening*
- **MITRE ATLAS** `AML.T0109` (*AI Supply Chain Rug Pull*) — mitigated by local verification of the weights' hash
- **OWASP LLM Top 10 (2025)** — LLM02 (*Sensitive Information Disclosure*), LLM04 (*Data and Model Poisoning*), LLM10 (*Unbounded Consumption*) — vectors covered by the patterns above

---

> 🧭 In summary: serving *self-hosted* AI models is not a new category of problem — it is the classic runtime *hardening* problem, with three irreducible specialisations: **weights are a critical asset**, **a shared GPU needs explicit isolation**, and ***inference APIs have consumption semantics** that conventional HTTP *rate limiting* does not cover*.
