---
id: riscos-processo-threat-modeling
title: Process Risks in Threat Modelling
description: Identification and treatment of the risks inherent to the Threat Modelling process, regardless of the method used
tags: [threat-modeling, risco-processo, decisao, validacao]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/addon/02-riscos-processo-threat-modeling.md
  source_sha256: 7f43aed46de256d40039f60920035e06b8d2b61e1e436a61a1541b67668602ad
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 4acb6781e89ae5499a97f14d3eb11828dab567ba200f0abd089b20bc7805b049
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [chapter_role, requirement_runtime, sbdtoe_sbd, threat, validation_evaluation]
  glossary_sha256: bf305000167a80b99fae282496e83115fa92f7fbf3b982b4addab50d96d62c60
  translated_at: 2026-09-25T20:16:58Z
  reviewed_by: null
---

# Process Risks in Threat Modelling

Threat Modelling is a **structured decision process** that aims to identify, analyse and prioritise the threats relevant to a concrete system, in a given context.

Like any complex decision process, it is subject to **risks of its own**, independent of:
- the method used (STRIDE, PASTA, LINDDUN, etc.),
- the supporting tools,
- the individual experience of the participants.

Failing to identify these risks explicitly compromises the reliability of the threat model produced.

---

## 1. Structural omission of threats {#1-omissão-estrutural-de-ameaças}

Not all relevant threats are necessarily identified during a Threat Modelling session.

Omissions may result from:
- limitations of the adopted method;
- excessive focus on visible components;
- lack of knowledge of adjacent domains;
- uncritical reuse of previous models.

The absence of a threat from a model **is not evidence that the threat does not exist**.

**Relates to.** Violates `THR-003`; materialises `MT-039`.

---

## 2. Perspective bias {#2-enviesamento-de-perspetiva}

Threat Modelling inevitably reflects the perspectives, experience and assumptions of the participants.

Common risks include:
- undervaluing threats outside the immediate technical domain;
- normalising known risks (“it has always been like this”);
- overvaluing improbable scenarios at the expense of systemic failures.

This bias must be assumed as an **inherent risk**, not as an exceptional failure.

**Relates to.** No linkable requirement in the current catalogue; materialises `MT-043`.

---

## 3. Confusion between intermediate analysis and formal decision {#3-confusão-entre-análise-intermédia-e-decisão-formal}

During the process, multiple intermediate artefacts are produced:
- lists of potential threats;
- session notes;
- exploratory diagrams;
- attack hypotheses.

These artefacts **do not, by themselves, constitute** an approved threat model.

The absence of a clear distinction between:
- supporting material,
- and validated decision,

introduces ambiguity and weakens risk governance.

**Relates to.** Violates `THR-004`; no linkable threat in the current catalogue.

---

## 4. Uncritical dependence on previous models {#4-dependência-acrítica-de-modelos-prévios}

Reusing previous models is a common and legitimate practice, but it introduces risks when:
- the context has changed;
- the architecture has evolved;
- new dependencies have been introduced;
- the risk profile has been altered.

Inherited models must be treated as **starting hypotheses**, never as validated truth.

**Relates to.** Violates `THR-006`; materialises `MT-049`.

---

## 5. Uncontrolled use of sensitive information {#5-uso-não-controlado-de-informação-sensível}

The Threat Modelling process frequently involves:
- detailed architectural diagrams;
- sensitive data flows;
- critical mitigation decisions.

These artefacts are **high-value assets**, subject to confidentiality, access control and retention requirements.

**Relates to.** No linkable requirement or threat in the current catalogue.

---

## 6. Plausible but incorrect results {#6-resultados-plausíveis-mas-incorretos}

A threat model may appear:
- coherent,
- complete,
- technically well articulated,

and still be incorrect or incomplete.

Plausibility is no substitute for validation, review and evidence.

**Relates to.** Violates `THR-007`; materialises `MT-045`.

---

## 7. Implications for the SbD-ToE {#7-implicações-para-o-sbd-toe}

The SbD-ToE explicitly assumes that:
- Threat Modelling is a fallible process;
- process risks must be treated systematically;
- mitigating these risks requires human validation, explicit decision and verifiable evidence.

The controls associated with these demands are defined in this chapter's validation and evidence file.
