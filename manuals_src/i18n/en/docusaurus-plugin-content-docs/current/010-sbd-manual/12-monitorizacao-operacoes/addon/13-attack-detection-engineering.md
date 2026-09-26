---
id: attack-detection-engineering
title: MITRE ATT&CK as a Detection Engineering Vocabulary
description: Use of MITRE ATT&CK as the reference vocabulary for detection engineering — mapping of detections to adversarial techniques and tactics and measurement of coverage. ATT&CK is a shared vocabulary and a threat-informed reference, not a complete authority nor a checklist for total coverage.
tags: [ATT&CK, MITRE, detection-engineering, detecao, cobertura, SIEM, correlacao, threat-informed, L2, L3]
sidebar_position: 13
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/addon/13-attack-detection-engineering.md
  source_sha256: 32bd8f612d0b47a0b30f04e373647c82e05a1f2e99c7bf1e3f6cda607c76aedd
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: b461ccd0c2b299e94f91d993edf380495b8b1e5ef2fb5efa22dc707075a94432
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [atlas_defense_evasion, discipline, framework_source_corpus, mapping, mcp_reading_programa, programme_line, risk_level, slug_threat_modeling, threat, validation_evaluation]
  glossary_sha256: 1fbcbd542a2a710a49560a8f0ed7e334b5fb661208e6077a856b7076c35c79a2
  translated_at: 2026-09-26T11:17:33Z
  stamped_at: 2026-09-26T18:35:45Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# MITRE ATT&CK as a Detection Engineering Vocabulary

## Scope and purpose {#âmbito-e-propósito}

Detection engineering needs a common vocabulary to describe **what** is detected. Without it, detections are described in ad-hoc language by each team, and coverage becomes impossible to measure or compare. MITRE ATT&CK provides that vocabulary: a structured catalogue of observed adversarial behaviour, organised into tactics (the adversary's objective) and techniques (the way it is achieved).

This addon integrates ATT&CK as a **reference vocabulary** for correlation and detection — mapping each detection to the techniques it covers, and measuring coverage against the relevant adversarial behaviour. It does not integrate it as a complete authority over detection nor as a checklist whose goal is to "cover everything".

Applicability: **L2 and L3**. ATT&CK formalises the mentions already present in Ch. 12 (requirements catalogue, examples of events) into a measurable coverage method.

> This integration is **threat-informed and anchored**: ATT&CK describes observed adversarial behaviour, not the universe of what is possible. Technique coverage is an indicator of visibility, not proof of effective detection.

---

## What ATT&CK provides {#o-que-o-attck-fornece}

- **Tactics** — the adversary's objective at a given moment of the intrusion. The Enterprise matrix has 14 reference tactics: Reconnaissance, Resource Development, Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, Impact.
- **Techniques and sub-techniques** — the concrete way in which each tactic is executed, with a stable identifier (for example, `T1059` — *Command and Scripting Interpreter*).
- **Procedures** — specific implementations of a technique observed in real groups and malware.

> ATT&CK is versioned and evolves. Version v19 (2026) began the restructuring of the *Defense Evasion* tactic. The programme must pin the **version of ATT&CK in use** when reporting coverage, so that measurements from different periods are comparable.

---

## Integration into the detection programme {#integração-no-programa-de-deteção}

The integration rests on three steps:

1. **Map detections to techniques.** Each detection rule, alert or correlation content must declare the ATT&CK technique(s) it covers, by identifier. The mapping is metadata of the rule, not separate documentation.
2. **Prioritise in a threat-informed way.** Not all techniques are equally relevant to a given system. Prioritisation must start from the system's threat model (Ch. 03) and its risk level (Ch. 01) — covering first the techniques that the threat model identifies as plausible for that context.
3. **Measure coverage.** Coverage is the percentage of **relevant** techniques with at least one validated detection. The denominator is the set of techniques prioritised by the threat model, not the complete ATT&CK catalogue.

---

## Epistemic discipline {#disciplina-epistémica}

- **Mapped is not detected.** A rule associated with a technique only counts as coverage when it has been validated — tested against the real or simulated execution of the technique. Without validation, the mapping measures intention, not capability.
- **One detection per technique is rarely total coverage.** A technique has multiple procedures; a rule typically covers a subset. Coverage by technique count overestimates real detection.
- **The absence of a technique from ATT&CK is not the absence of a threat.** The catalogue records observed behaviour; new behaviour always precedes its cataloguing.

---

## Associated metrics {#métricas-associadas}

The `OPS-K06` indicator (correlation coverage between sources) gains precision when expressed in ATT&CK terms: correlation between sources must cover the prioritised techniques, not an abstract number of rules. Technique coverage by tactic reveals structural gaps — an entire tactic without detection is a blind spot.

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|-----------|---------|
| [Ch. 12 — Correlation and anomalies](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/correlacao-anomalias) | Where the mapping to techniques structures the correlation rules |
| [Ch. 12 — Examples of events](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/exemplos-eventos) | Events already related to OSC&R / ATT&CK |
| [Ch. 12 — Integration with SIEM](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/integracao-siem) | Platform where the mapped detections are operationalised |
| [Ch. 12 — KPIs and Metrics](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/kpis-metricas-operacoes) | OPS-K06, correlation coverage |
| [Ch. 03 — Threat Modelling](/sbd-toe/sbd-manual/threat-modeling/intro) | Source of the threat-informed prioritisation of the techniques to cover |

> **On curation:** Consolidated from MITRE ATT&CK Enterprise (attack.mitre.org) and from threat-informed detection engineering practice. ATT&CK is a versioned external reference; the version in use must be recorded in coverage measurements. This integration is methodological — it does not replace detection based on the system's own threat model.
