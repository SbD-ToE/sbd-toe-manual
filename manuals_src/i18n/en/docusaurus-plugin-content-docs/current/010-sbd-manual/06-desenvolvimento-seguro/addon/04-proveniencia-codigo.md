---
id: proveniencia-codigo
title: Code Origin and Provenance
description: Treating code as an artefact of controlled provenance in secure development
translation:
  source_locale: pt
  source_path: 010-sbd-manual/06-desenvolvimento-seguro/addon/04-proveniencia-codigo.md
  source_sha256: ed4d235136896e8ed78ec8c51a99138a76124676a8eb97f9e225b637b6a69dc6
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: e70994a786e1e6c7e0d5592b474f2e53d1eecbcb970cb10c3f1542636fffd3dd
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, provenance, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: f64f284e0cebb5212ad494fa3373ecadaa8b0ad7b3f70f0d72fdfe598073480b
  translated_at: 2026-09-26T08:57:10Z
  stamped_at: 2026-09-26T18:34:02Z
  reviewed_by: null
---

# Code Origin and Provenance

For many years, secure development rested on an implicit assumption:  
code was written mostly by the team itself, deliberately and with understanding.

That assumption is no longer valid.

Today, a typical codebase results from a combination of:
- code written locally;
- code reused across projects;
- adapted examples;
- automated transformations;
- suggestions and acceleration from support tools.

The result is that **code now has multiple provenance**, even when it resides in the same repository.

---

## Why provenance matters {#porque-a-proveniência-importa}

Code provenance is not a philosophical question; it is a question of risk.

Without a clear understanding of the origin and context of a code fragment, risks arise such as:
- inadvertent use of insecure patterns;
- introduction of implicit dependencies;
- incompatibilities with architectural decisions;
- conflicts with existing security requirements;
- legal or licensing risks.

Treating code of unknown provenance as “normal” is equivalent to accepting an external dependency without analysis - something that SbD-ToE explicitly rejects.

---

## Internal code as an internal supply chain {#código-interno-como-supply-chain-interno}

This addon introduces a key concept:

> **Code produced internally must be treated as part of the internal supply chain.**

Just like external dependencies:
- code has an origin,
- a context,
- a history,
- and associated risk.

The difference is only the perimeter of control, not the need for validation.

This perspective creates direct coherence with Chapter 05 - Dependencies and Supply Chain, without duplicating its mechanisms.

---

## Provenance is not authorship {#proveniência-não-é-autoria}

It is important to distinguish:
- **authorship**: who wrote the code;
- **provenance**: in what context it arose, under what assumptions, and with what degree of understanding.

A code fragment can be:
- correctly written,
- functional,
- and still unsuitable for the context in which it is incorporated.

Secure development is concerned with **suitability**, not only with syntactic correctness.

---

## Practical implications for development {#implicações-práticas-no-desenvolvimento}

Assuming provenance implies that:
- incorporated code must be understood, not merely tested;
- incorporation decisions must be explicit;
- exceptions must be recorded when understanding is partial;
- human review becomes a governance mechanism, not only a quality one.

These implications are reflected directly:
- in the validation rules,
- in the lifecycle gates,
- and in the evidence required for acceptance.

---

## Closing {#encerramento}

By treating code as an artefact of controlled provenance, secure development no longer depends on the “average quality” of contributions and comes to depend on **robust and verifiable processes**.

This is the only model that scales when development becomes fast, distributed and assisted by advanced tooling.

---
