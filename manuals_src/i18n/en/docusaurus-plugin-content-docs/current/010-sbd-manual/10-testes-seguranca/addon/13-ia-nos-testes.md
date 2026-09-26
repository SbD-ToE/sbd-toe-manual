---
id: ia-nos-testes
title: AI in the Security Testing Process
description: How to use AI/GenAI to accelerate security testing (planning, triage, regressions, fuzzing and validation) without degrading evidence, confidentiality or human control
tags: [genai, ia, testes, seguranca, triagem, regressao, fuzzing, evidencias, governanca]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/10-testes-seguranca/addon/13-ia-nos-testes.md
  source_sha256: 37bb6648e760a30a67d8a299d52fc659a611b44323e0d12bb3f5e0b737488b5b
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: d1deb28809da0cb0bc7f5a3b1dde1f15509b79a57e9fb7bce98c32d61c5c24ef
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 2ffd43fd37c8802a693f5fa1e43a3d3a9df1ca9d5ea898c88f6f405bedc9d687
  glossary_keys: [avaliacao, chapter_role, como_fazer, deterministic, framework_source_corpus, llm, oracle, practitioner_manual, provenance, requirement_runtime, traceability, transversal, validation_evaluation, verification_taxonomy]
  glossary_sha256: 9a73274c8621d12fbd1aa97ea004f5d677b3c9dc7e616d495614aacf524cf007
  translated_at: 2026-09-26T10:31:33Z
  reviewed_by: null
---

# AI in the Security Testing Process (GenAI)

The pervasive adoption of AI/GenAI in the SSDLC profoundly changes **how evidence is produced and interpreted**.  
In the domain of security testing this is especially critical, because:

- scanner output was already "noisy" (FP/FN), and AI can amplify that noise if it is used as an oracle;
- tests depend on **context** (architecture, authenticated flows, sensitive data, compensating controls);
- security requires a **traceable human decision**, not "automated decision" without a chain of accountability.

This addon prescribes how to use AI to accelerate and increase coverage **without replacing empirical validation** or compromising confidentiality.

---

## 1) Canonical principles {#1-princípios-canónicos}

### P1 - AI is an "assistant", not a "decision-maker" {#p1---ia-é-assistente-não-decisor}
AI may propose: triage, hypotheses, prioritisation, reproduction paths, patch candidates, tests.  
The final decision (fix/accept/suppress/defer) is always human and traceable - see **US-12** and **US-13** in the lifecycle.

### P2 - Evidence must be reproducible without AI {#p2---evidência-tem-de-ser-reprodutível-sem-ia}
Any confirmed finding must be reproducible by:
- an automated test (regression),
- a minimal PoC,
- a deterministic log/artefact (SARIF, HTTP transcript, crash dump, etc.).

### P3 - Sensitive data never enters a model "blindly" {#p3---dados-sensíveis-nunca-entram-às-cegas-num-modelo}
Prompts and contexts must respect:
- minimisation (only what is necessary),
- redaction/masking,
- segregation of secrets (never paste real tokens/headers),
- the organisational AI-use policy (see the cross-cutting policies annex).

### P4 - "Model/supply chain" risk is also a security risk {#p4---risco-modelosupply-chain-também-é-risco-de-segurança}
AI tools (cloud or local) are part of the chain of trust.
Controls equivalent to those applied to dependencies and CI/CD must exist:
- versioning of the model/config,
- logging of prompts/outputs (where permitted),
- review of permissions and access,
- integrity/provenance verification where applicable.

---

## 2) Recommended use cases (and how to do them safely) {#2-casos-de-uso-recomendados-e-como-fazer-com-segurança}

### 2.1 Assisted triage (SAST/DAST/IAST/SCA/Fuzzing) {#21-triagem-assistida-sastdastiastscafuzzing}
**Objective:** reduce analysis time and improve the consistency of the decision.

**Practice:**
- Provide the AI with only:
  - the finding ID + rule/tool,
  - a minimal excerpt of the code path,
  - non-sensitive technical context (authentication pattern, existing WAF, etc.),
  - the L1–L3 severity policy and the gate criteria.
- Require structured output (JSON/Markdown) with:
  - an exploitability hypothesis,
  - the necessary conditions,
  - existing mitigation (if applicable),
  - a recommendation for empirical validation (concrete steps).

**Anti-pattern:** "the AI said it is a false positive" without proof.

**Expected evidence:**
- decision documented via template (US-12 / T1),
- link to empirical validation (US-13 / T1–T5),
- suppression record with rationale and approver (if FP).

---

### 2.2 Assisted generation of security regression tests {#22-geração-assistida-de-testes-de-regressão-de-segurança}
**Objective:** turn fixed findings into future protection.

**Practice:**
- Ask the AI to produce:
  - a test skeleton (unit/integration/e2e),
  - representative payloads,
  - asserts that prove failure before and "pass" after the fix.
- The developer validates and adjusts:
  - boundary conditions,
  - mocks/stubs,
  - safe fixtures.

**Restrictions:**
- Never accept generated code without review.
- Require the test to explicitly reference:
  - the finding (ID),
  - the relevant requirement (Ch. 02),
  - the fix commit/PR.

**Expected evidence:**
- versioned test,
- pipeline running the regressions,
- execution report attached to the release.

---

### 2.3 Assistance for authentication in DAST (scripts/flows) {#23-assistência-para-autenticação-em-dast-scriptsflows}
**Objective:** reduce friction in authenticated DAST and increase real coverage.

**Practice:**
- The AI can help build a generic *login flow*, but:
  - real credentials do not enter the prompt,
  - real tokens/cookies are masked,
  - the final flow is tested in staging with a dedicated technical account and rotation.

**Expected evidence:**
- versioned DAST configuration,
- coverage of critical endpoints,
- authenticated DAST report attached to the release.

---

### 2.4 AI-assisted fuzzing (corpora, mutations and prioritisation) {#24-fuzzing-assistido-por-ia-corpora-mutações-e-priorização}
**Objective:** increase the capacity to find useful edge cases and crashes.

**Practice:**
- AI to:
  - generate seeds/corpora from schemas (OpenAPI/GraphQL),
  - suggest mutations (encoding, nesting, size),
  - prioritise endpoints by risk and history.
- Execution always in an isolated environment, with:
  - resource limits,
  - complete logs,
  - non-production data.

**Expected evidence:**
- versioned corpora,
- crash repro + RCA,
- severity adjusted on the basis of real impact (DoS/RCE/etc).

---

### 2.5 Consolidation and deduplication of multi-tool findings {#25-consolidação-e-deduplicação-de-findings-multi-ferramenta}
**Objective:** reduce noise and improve traceability.

**Practice:**
- AI can suggest clusters by:
  - CWE/CVE,
  - component,
  - code path,
  - fingerprint.
- The final dedup rule is configured in the central system (e.g. DefectDojo) and not "in the head" of the model.

**Expected evidence:**
- versioned correlation rules,
- audit of merges/splits of findings,
- FP/FN metrics per tool over time.

---

## 3) Mandatory controls when AI is used in testing {#3-controlos-obrigatórios-quando-se-usa-ia-em-testes}

### C1 - Minimum record of "interaction with AI" (where permitted) {#c1---registo-mínimo-de-interação-com-ia-quando-permitido}
For severity decisions ≥ HIGH (L2/L3), record:
- the objective of the request,
- the context provided (redacted),
- the relevant output,
- the final human decision + evidence (PoC/test/log).

> If the privacy policy prevents logging, record at least: "AI used" + type of support + deterministic evidence without the prompt.

### C2 - Protection against prompt injection / malicious content in artefacts {#c2---proteção-contra-prompt-injection--conteúdo-malicioso-em-artefactos}
When the AI is fed with:
- logs,
- scanner outputs,
- HTML/JS collected by DAST,
- fuzzing payloads,

assume that the content may contain malicious instructions ("ignore rules…", "exfiltrate…").  
Mitigation:
- sanitisation,
- *content filtering*,
- execution in a "no tools / no network" context whenever possible,
- human validation.

### C3 - Separation of environments and credentials {#c3---separação-de-ambientes-e-credenciais}
AI used for tests that interact with the runtime:
- only in isolated staging,
- with dedicated technical accounts,
- with secrets managed by a vault and never copied.

### C4 - Prohibition of "auto-merge" of security fixes {#c4---proibição-de-auto-merge-de-correções-de-segurança}
Any patch generated with AI:
- requires human review,
- requires tests (including security regression),
- may never bypass gates.

### C5 - Continuous *eval suites* for agents in development and production {#c5-eval-suites}

Controls C1–C4 cover the case in which **AI assists** whoever tests. When the system **includes an AI agent in production** (or when the agent is part of the testing process, e.g. an automated PR auditor), **the agent itself** needs to be tested — the same principle that applies to any other critical component. This class of tests is called *eval suites*; they do not replace SAST/DAST/SCA, they complement them for the agentic slice.

#### Principles of *eval suites* {#princípios-das-eval-suites}

1. **Prompt regression as functionality regression.** Every change to the *system prompt*, *skill file*, *agent file* or model version is treated as a change that can degrade behaviour; the *eval suite* is run before the *merge* — exactly as regression tests are run before code changes.
2. **Approximate determinism in the test environment.** LLM models are not deterministic, but in *eval* `temperature=0` or equivalent parameterisation is used, and measurement is made with an explicit tolerance (e.g. *exact match* vs *semantic match* vs *embedding similarity > k*). The tolerance is declared per test.
3. **Assessment by domain.** Three minimum classes are covered: (a) **utility** — the agent accomplishes the task in expected cases; (b) **security** — the agent refuses or escalates in hostile cases (prompt injection, jailbreak, off-policy); (c) **stability** — the agent does not degrade between model / prompt versions.
4. **Versioned and maintained suite.** The *eval suite* has the same status as the system's test suite — it lives in VCS, evolves with the product, and is reviewed periodically.

#### Minimum composition by level {#composição-mínima-por-nível}

| Component | A1 (assistant) | A2 (executes with confirmation) | A3 (autonomous + revert) | A4 (autonomous in prod) |
|---|---|---|---|---|
| **Prompt regression tests** | Recommended | Mandatory | Mandatory | Mandatory (run on every change) |
| **Abuse / red-team corpus** (*prompt injection*, *jailbreak*, *off-policy*) | — | Recommended | Mandatory | Mandatory (with periodic manual red-team) |
| **Drift detection** between versions (model, prompt, skill) | — | Recommended | Mandatory | Mandatory (short windows) |
| **A/B testing** before skill promotion | — | Recommended | Mandatory | Mandatory (with pre-agreed criteria) |
| **Test telemetry in production** (correlate offline evals with real signals) | — | — | Recommended | Mandatory (cross-link Ch. 12) |

#### Operational landing {#aterragem-operacional}

- **The eval suite lives in VCS** alongside the code that operates the agent. Changes to the suite go through the same *code review* as changes to the code.
- **Runs in CI** before the *merge* of changes to *system prompts*, *skill files*, *agent files*, or after a *bump* of the model version. Failure blocks the *merge* (or lowers the autonomy level until resolved).
- **Results archived** with `eval_run_id` linked to `mandate_ref` — an audit can reconstruct which version of the suite confirmed which autonomy level.
- **Coverage proportional to the autonomy level** declared in the *mandate*. Raising the level without a matching *eval suite* is prohibited (cross-link Policy 38 §5.4).

#### Anti-patterns {#anti-padrões}

- ❌ "*Vibe checks*" as the only validation — a few manual prompts are run and that is deemed sufficient. No record remains, no regression is detected.
- ❌ *Eval suite* that never fails — a sign of insufficient coverage, not of excellence. Known adversarial cases are added to guarantee useful coverage.
- ❌ Aggregate metrics without inspection of the corpus — a high *score* can hide catastrophic failures in critical sub-categories.
- ❌ *Eval suite* in a repository separate from the skill/prompt — opens the door to silent *drift*.

#### Where it lands in the rest of the Manual {#onde-aterra-no-resto-do-manual}

- **Ch. 02** — [`REQ-AGN-002`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn) requires a justified autonomy level; the *eval suite* is the evidence that the level is defensible.
- **Ch. 07** — mandatory *eval run* as a *gate* before the *merge* of skill/prompt changes (cross-link US-19).
- **Ch. 12** — agentic signals in production (real jailbreaks, off-policy actions) feed back into the offline *eval suite*.
- **Policy 19 — Testing Strategy** adds the `eval suites` chapter to the scope of mandatory tests.

> 🧭 In short: testing the agent is testing a component of the system. The *eval suite* is not extra work — it is the normal testing work applied to the slice that operates through language. Without it, there is no way to sustain an A2+ classification over time.

---

## 4) Explicit integration with this chapter {#4-integração-explícita-com-este-capítulo}

This addon directly reinforces:

- **US-10/US-11** (centralisation and feedback) - AI can accelerate triage and reduce noise, without losing traceability.
- **US-12** (assisted decision) - AI feeds the hypothesis; the decision is human and documented.
- **US-13** (empirical validation) - AI suggests how to validate; confirmation is always by PoC/test.

---

## 5) Adoption checklist (binary) {#5-checklist-de-adoção-binário}

| Item | Yes/No |
|------|:------:|
| Use of AI in testing is covered by an organisational policy (minimisation, data, logging) |  |
| A human-decision template exists (FIX/ACCEPT/SUPPRESS/DEFER) applied to critical/high findings |  |
| An empirical validation procedure exists per type of test (SAST/DAST/IAST/Fuzzing/PenTest) |  |
| There is segregation of environments and technical accounts for DAST/IAST/fuzzing with credential rotation |  |
| Prompts never include secrets/PII; a redaction/masking process exists |  |
| AI outputs are not used as "proof" without a reproducible deterministic artefact |  |
| AI-generated patches never auto-merge and go through review + tests |  |
| An FP/FN metric and decision/validation time exist per severity and per L1–L3 |  |

---

## 6) Final notes {#6-notas-finais}

AI can be a brutal productivity multiplier in security testing - **if** it is used as an accelerator of analysis and artefact generation, and not as a substitute for evidence and accountability.

The success criterion is not "less human work", but rather:
- **more coverage**, 
- **less time to confirmation**, 
- **better traceability**, 
- **fewer unfounded decisions**.
