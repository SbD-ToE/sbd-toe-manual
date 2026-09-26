---
id: validacao-codigo
title: Code Validation as a Process Risk Control
description: Why code validation is a central risk-control mechanism in modern development
translation:
  source_locale: pt
  source_path: 010-sbd-manual/06-desenvolvimento-seguro/addon/06-validacao-codigo.md
  source_sha256: 469391f2028f63dc4c3c3f232913554970a4250515a305ff2aa7614301db2cac
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 883d7532248e5fbd593003edb6184028c93ef2dfa767938874dabc5259957b88
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 056f81fc0221610254c3eefaa182065e249abe5f887f679635bef5554d85ef95
  glossary_keys: [chapter_role, cycle_iteration, lifecycle_phase, practitioner_manual, sbdtoe_sbd, validation_evaluation]
  glossary_sha256: 4826757d999df585b5dec40b7290be5603f412e56291be04439ce9eecdcd7e23
  translated_at: 2026-09-26T08:57:11Z
  reviewed_by: null
---

# Code Validation as a Process Risk Control

In modern development, the main risk no longer lies only in the **complexity of the code**, but in **the way that code is introduced into the system**.

As teams turn to extensive reuse, automation, assisted generation and frequent refactoring, the act of “writing code” ceases to be an exclusively deliberate process and becomes, in many cases, a **mediated**, **accelerated** and **non-linear** process.

In this context, code validation ceases to be an optional good practice and comes to play a central role:  
**controlling the risk of the development process**.

---

## Code is not trust - it is input {#código-não-é-confiança---é-input}

One of the fundamental assumptions of this chapter is simple, but structural:

> **Code is not trustworthy by default, regardless of its origin.**

The origin of code - human authorship, internal reuse, external libraries or support tools - is not a valid criterion for trust.  
The only factor that turns code into an acceptable artefact is **technical validation proportionate to risk**.

This principle is consistent with the treatment given to:
- external dependencies (Ch. 5),
- architectural decisions (Ch. 4),
- and security requirements (Ch. 2).

Secure development extends that logic to the code produced internally itself.

---

## Validation as a process, not as an event {#validação-como-processo-não-como-evento}

Another common mistake is to treat validation as a **one-off event** - typically a final review before the merge.

In SbD-ToE, validation is understood as a **progressive process**, in which code passes through well-defined states, each one reducing the risk introduced:

1. **Proposed code**  
   Code not yet understood or validated, subject to plausible error.

2. **Reviewed code**  
   Code analysed by a human with technical knowledge, but not yet empirically validated.

3. **Validated code**  
   Code subjected to relevant technical validations (tests, static analysis, automated checks).

4. **Accepted code**  
   Code whose incorporation is an explicit decision, taken on by an identifiable role.

The absence of any one of these transitions **is not neutral**: it represents unmitigated risk.

---

## Plausible error: the greatest enemy of secure development {#erro-plausível-o-maior-inimigo-do-desenvolvimento-seguro}

A large share of modern vulnerabilities do not result from obviously incorrect code, but from **plausible error**:
- logic that “makes sense” but fails in edge cases;
- undocumented implicit assumptions;
- incorrect use of secure APIs;
- subtle omissions of validation or error control.

These errors easily go unnoticed when:
- the review is superficial;
- trust in the origin of the code is excessive;
- empirical validation is insufficient.

That is why validation in secure development does not look only for *bugs*, but for **understanding**.

---

## Evidence as an acceptance criterion {#evidência-como-critério-de-aceitação}

In SbD-ToE, no validation exists without evidence.

Accepting code implies being able to answer, after the fact:
- who reviewed it;
- what validations were run;
- with what results;
- and on the basis of what criteria the decision was taken.

That evidence does not exist for “future audits”;  
it exists to **discipline the present process** and reduce systemic error.

---

## Link to the lifecycle {#ligação-ao-ciclo-de-vida}

This addon defines the **technical rationale** for code validation.  
Its practical application - gates, responsibilities and artefacts - is described in the chapter's `15-aplicacao-lifecycle.md`.

Validation does not replace other practices of the Manual;  
it works as a **point of convergence** between development, testing and governance.

---
