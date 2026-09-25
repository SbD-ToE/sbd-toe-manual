---
id: abuse-misuse-cases
title: Abuse and Misuse Case Method
description: Method for deriving abuse and misuse cases — cross-functional workshop, adversarial user stories and integration into the requirements backlog. Adversarial elicitation technique that feeds the threat model and the security requirements; it complements structured threat modelling, it does not replace it.
tags: [abuse-case, misuse-case, threat-modeling, requisitos, user-story, backlog, OWASP, elicitacao, L2, L3]
sidebar_position: 12
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/addon/12-abuse-misuse-cases.md
  source_sha256: 57341753eed660a3e811c96476ddd06144aedb6a03d36612113023fa3cbb2599
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 2f11a67104926ca3f5b0af7e79bd789bdf7856322bd0fdabbd136a65ae15629c
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5c08c8e5a6891162c9e9f50251c6496da3b47913a0ecfd9a53dfce59ec6cbaf0
  glossary_keys: [cycle_iteration, practitioner_manual, programme_line, requirement_runtime]
  glossary_sha256: 8fe774ee879e33c0ec8438dc2f612be40280f017674ca17909e8de2b99461035
  translated_at: 2026-09-25T20:17:02Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Abuse and Misuse Case Method

## Scope and purpose {#âmbito-e-propósito}

The manual refers to abuse cases at several points, but without a method for producing them. This addon provides one.

An **abuse case** describes how an adversary uses the system **in an intentionally hostile way** — the reverse of a *use case*. Where the functional user story captures what a legitimate user wants to do, the abuse case captures what an attacker wants to achieve against the system. The **misuse case** is its formalisation (in the tradition of Sindre and Opdahl): a use case driven by a hostile actor, modelled in parallel with the legitimate use cases.

The function of the method is to make adversarial an activity that, by default, is centred on the legitimate user. Abuse cases are an **elicitation technique** that feeds the threat model and the security requirements.

Applicability: **L2 and L3**, in the requirements and threat modelling phases.

> Abuse cases are a **creative and non-exhaustive** technique. They complement structured threat modelling (STRIDE, LINDDUN) — they do not replace it. The absence of an abuse case is not proof of the absence of an abuse path.

---

## The method {#o-método}

1. **Cross-functional workshop.** Bring together product, development, security and QA. The diversity of perspectives is what distinguishes useful abuse cases from a predictable list — whoever knows the business rule identifies abuses that the generic attacker does not reveal.
2. **Derive the adversarial reverse.** For each relevant user story or functional flow, formulate its hostile counterpart: "As an attacker, I want *&lt;objective&gt;*, exploiting *&lt;weakness&gt;*". An upload flow generates the abuse "upload a file that executes code on the server"; an authentication flow generates "enumerate valid accounts from the error messages".
3. **Prioritise by risk.** Order the abuse cases by the system's risk classification (Ch. 01) and by plausibility against the threat model (Ch. 03). Not every abuse justifies a control; proportionality applies here as it does throughout the manual.
4. **Translate into adversarial requirements and acceptance criteria.** Each prioritised abuse case becomes a security requirement with a verifiable acceptance criterion, and enters the **backlog** with the same rigour as a functional user story (Ch. 02).
5. **Feed tests and the threat model.** The prioritised abuse cases become test cases (Ch. 10) and inputs to the threat model, closing the cycle between what is feared and what is validated.

---

## Integration into the backlog {#integração-no-backlog}

An adversarial user story is not an informal note — it is a traceable requirement. It must have an owner, an acceptance criterion and a status, and be handled in the same backlog as the functional requirements. An abuse case that stays outside the backlog is a concern that gets lost between sprints.

Integration into the backlog is what separates this method from a one-off exercise: the abuse identified in a workshop only changes the product if it materialises as prioritised and tracked work.

---

## Relation to structured threat modelling {#relação-com-o-threat-modeling-estruturado}

Abuse cases and structured threat modelling answer different and complementary questions. The abuse case starts from the **function** ("how is this flow abused?"); STRIDE starts from the **security property** ("where do integrity, confidentiality and availability fail?"). Applied together, they cover what each one on its own lets slip. Abuse cases are typically the most accessible entry point for teams without a practice of formal threat modelling.

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|-----------|---------|
| [Ch. 02 — Requirements Catalogue](/sbd-toe/sbd-manual/requisitos-seguranca/addon/catalogo-requisitos) | Where the derived adversarial requirements enter as traceable items |
| [Ch. 02 — Application examples](/sbd-toe/sbd-manual/requisitos-seguranca/addon/exemplos-aplicacao) | Examples of abuses already translated into requirements and tests |
| [Ch. 03 — Methodologies and tools](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas) | Structured threat modelling that the abuse cases feed |
| [Ch. 01 — Application classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro) | Basis for prioritisation by risk |
| [Ch. 10 — Testing strategy](/sbd-toe/sbd-manual/testes-seguranca/addon/estrategia-testes) | Where the prioritised abuse cases become test cases |

> **On curation:** Consolidated from OWASP (Abuse Case guidance) and the misuse case tradition (Sindre & Opdahl). Adversarial elicitation method — it complements, and does not replace, structured threat modelling and the programme's risk analysis.
