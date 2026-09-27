---
id: recomendacoes-avancadas
title: Advanced Recommendations - Secure Development
description: Reinforced practices and optional recommendations for organisations with greater maturity in secure development
tags: [desenvolvimento, maturidade, práticas avançadas, DevSecOps, validação]
sidebar_position: 30
translation:
  source_locale: pt
  source_path: 010-sbd-manual/06-desenvolvimento-seguro/recomendacoes-avancadas.md
  source_sha256: edab0e1aeccde5f843640b50780b89039c47191b383fe8bbda506ea76d403b02
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: b1f5dc7963c752c8b10928079d6752f00d3c3daef0d4fdc2fc651da168e49171
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, llm, maturity, plain_rag, traceability, validation_evaluation]
  glossary_sha256: 607c00ddd67baea88c0e21371d0eecd68d2564acdc02e22d6d9b3e9477e9a809
  translated_at: 2026-09-26T08:57:18Z
  stamped_at: 2026-09-26T18:34:12Z
  reviewed_by: null
---

# Advanced Recommendations - Secure Development

This file presents a set of advanced practices that **complement and reinforce** the measures prescribed in this chapter.  
They are especially relevant for organisations with mature pipelines, a DevSecOps culture and teams with a high degree of technical autonomy.

The recommendations described here **do not replace the essential controls**, but they increase the depth, coverage and automation of security validations during development.

---

## 1. ✅ Custom Semgrep rules {#1--regras-semgrep-customizadas}

Adopting organisation-specific rules with **Semgrep** makes it possible to:

- Detect dangerous patterns specific to the application's context (e.g. logic bypasses, exposed sensitive endpoints).
- Implement **domain-based security** (e.g. rules applied only to critical microservices).
- Create a security baseline specific to each repository or stack.

---

## 2. ✅ Semantic linters {#2--linters-semânticos}

Beyond syntax, use **semantic linters** that check for:

- Dangerous business logic patterns.
- Inappropriate use of critical APIs (e.g. cryptography, serialisation).
- Missing defensive structures (e.g. fail-safes, timeouts, appropriate try/catch).

---

## 3. ✅ Data flow analysis (Data Flow Analysis) {#3--análise-de-fluxo-de-dados-data-flow-analysis}

Integrate tools that analyse **how sensitive data travels through the application**, making it possible to:

- Detect unvalidated data paths.
- Trace the use of unsanitised input.
- Identify authorisation flaws caused by propagation.

---

## 4. ✅ Continuous feedback and visibility per pull request {#4--feedback-contínuo-e-visibilidade-por-pull-request}

Implement mechanisms for:

- Security alerts directly in PRs (pull requests).
- Dashboards with findings per project, team and type of flaw.
- Integration with quality tools and engineering metrics.

---

## 5. ✅ AI-assisted analysis (with human validation) {#5--análise-assistida-por-ai-com-validação-humana}

Use tools based on **LLMs (Large Language Models)** to:

- Suggest remediations for common findings.
- Validate the existence of controls in critical functions.
- Detect non-trivial weaknesses - **always with a final human review**.

---

## 6. ✅ Semantic security annotation in code {#6--anotação-semântica-de-segurança-no-código}

Adopt lightweight annotation in the code with tags such as:

```js
// @sec:input-validated
// @sec:auth-required
// @sec:logged-contextual
```

This reinforces traceability, speeds up reviews and supports automated validations.

---

## 7. ✅ Automated, context-based triage {#7--triagem-automatizada-e-baseada-em-contexto}

Automate the classification of findings on the basis of:

- Severity (e.g. CVSS, CWE).
- Context of use in the application.
- History of false positives per project.

This avoids an overload of findings and focuses attention on what matters.

---

## 8. ✅ Blocking policies by type of flaw {#8--políticas-de-bloqueio-por-tipo-de-falha}

Define automatic rules to block merges or releases with critical flaws:

- E.g. `merge blocked if CWE-078 detected and not justified`
- Integration with lists of blocking flaws defined by the organisation.

---

## 9. ✅ Playbooks and auto-patch {#9--playbooks-e-auto-patch}

Maintain playbooks for frequent flaws with:

- Technical explanation.
- Fix template.
- Scripts or links for patch automation.

Integrate them as automatic actions on repeated findings.

---

## 10. ✅ Adaptive training driven by findings {#10--formação-adaptativa-orientada-por-findings}

Use the team's real findings as the basis for:

- Individualised microlearning.
- Training reinforcement adapted to the stack and technical profile.
- Records of continuous improvement.

---

## 11. ✅ Defence against prompt injection in LLM applications {#11--defesa-contra-prompt-injection-em-aplicações-llm}

Applications that **integrate LLMs** (conversational interfaces, RAG, agents with tool invocation) have a specific attack surface that is not covered by traditional input validation. Section 5 (AI-assisted analysis) deals with the LLM as a **static analysis tool**; this section deals with the opposite case — when the **application in production uses LLMs** and processes input that may contain malicious prompts.

### Principles {#princípios}

- **Treat all input that reaches the model's context as untrusted** — this includes direct user input, retrieval-augmented content (RAG retrievals), uploaded files, web content fetched by the agent and the outputs of tools called by the agent.
- **Separate the system prompt from user input by channel** — use APIs with structured messages (`system` / `user` / `assistant` roles) instead of string concatenation; in RAG pipelines, explicitly mark the "start and end of retrieval context" so that the model can tell them apart.
- **Output filtering** — detect and block system prompt exfiltration patterns (`AML.T0069.002`), command patterns that indicate a successful jailbreak, and content that exceeds the scope of the original question.

### Operational practices {#práticas-operacionais}

- **Pre-model input validation**: maximum prompt size, known patterns of jailbreak attempts (DAN, malicious role-playing prompts), encoding tricks (Base64, Unicode obfuscation) — useful but insufficient on its own; it is defence in depth, not a single control.
- **Output sanitisation for the rendering destination** — LLM outputs placed in HTML are a vector for persistent XSS; apply VAL-008 (contextual encoding; see Ch. 02 §VAL) to the model's output as if it were untrusted user input.
- **Aggressive per-session rate limiting** — prompt injection requires multiple iterations in many cases; thresholds must distinguish normal use from exploitation attempts.
- **Complete logging of model inputs and outputs** — with PII sanitisation; see Ch. 12 §OPS-011 for the observability framing.
- **Out-of-band human approval for tool calls with critical impact** — in autonomous agents, any write/mutating action (delete, transfer, send, deploy) must require explicit confirmation; the associated architecture is in Ch. 04 §AI/ML.

### Relevant catalogues {#catálogos-relevantes}

- **OWASP LLM Top 10 (2025)** — particularly LLM01 (Prompt Injection) and LLM02 (Sensitive Information Disclosure); referenced in Ch. 03 §AI/ML.
- Relevant **MITRE ATLAS** techniques: `AML.T0051.001` Indirect Prompt Injection, `AML.T0086` Exfiltration via AI Agent Tool Invocation, `AML.T0069.002` System Prompt extraction.

> These practices complement (and do not replace) the VAL- (input validation) and ENC- (output encoding) requirements of Ch. 02. In particular, **VAL-008** (output encoding at rendering, against XSS) applies to LLM outputs placed on rendered surfaces (HTML, terminal, logs).

---

> 💡 Many of the advanced practices described here are supported natively by commercial tools established on the market.  
> Platforms such as **Checkmarx**, **Kiuwan**, **Xygeni**, **Snyk**, among others, integrate features that cover everything from SAST and SCA, semantic tagging and policy enforcement to direct feedback in pipelines and PRs.  
> It is therefore **not necessary to resort to a scattered ecosystem of open source tools** to apply these recommendations - what matters is to guarantee **the security function**, regardless of the tool chosen.
