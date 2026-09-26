---
id: epss-kev-priorizacao
title: Vulnerability Prioritisation with EPSS and KEV
description: Remediation prioritisation layer based on the probability of exploitation (EPSS, FIRST.org) and confirmed exploitation (CISA KEV), applied on top of the CVSS-based patching SLAs. EPSS and KEV refine the order of remediation; the SLAs by severity remain as the mandatory floor.
tags: [EPSS, KEV, CVSS, priorizacao, vulnerabilidades, patching, SLA, remediacao, CISA, FIRST, L2, L3]
sidebar_position: 12
translation:
  source_locale: pt
  source_path: 010-sbd-manual/12-monitorizacao-operacoes/addon/12-epss-kev-priorizacao.md
  source_sha256: eb3e940641d8a491c7cdc09b3a3240b4cedb770339cefdf2787e5d2f38244922
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: 05c46d51d6eaab1d72a918b6e0b4d8ba7c7eefa864f6a4a0f912c46df4597c82
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: ebb6c6bf48bf281085379aa982dcfe014d642265f07b08070d51366e58764173
  glossary_keys: [discipline, framework_source_corpus, layer, piso_limiar, piso_relacao, programme_line, regra_de_fecho]
  glossary_sha256: 585b06b5473a5fb253ee162b29aec0ccf27165a22b9028b5718ad91952bb5367
  translated_at: 2026-09-26T11:17:32Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# Vulnerability Prioritisation with EPSS and KEV

## Scope and purpose {#âmbito-e-propósito}

CVSS measures the **severity** of a vulnerability — the potential impact if it is exploited — but it does not measure the **probability** of that exploitation occurring, nor whether it is already happening. A patching SLA based on CVSS alone treats all vulnerabilities of equal severity as equally urgent, when the evidence of exploitation separates them decisively.

This addon integrates two sources that add that missing dimension:

- **EPSS** (*Exploit Prediction Scoring System*), maintained by the EPSS SIG of FIRST.org: it estimates the probability of a vulnerability being exploited *in the wild* within the following 30 days.
- **KEV** (*Known Exploited Vulnerabilities*), the CISA catalogue: it lists vulnerabilities with confirmed evidence of active exploitation.

EPSS and KEV come in as a **prioritisation layer on top of CVSS**, not as a replacement. The patching SLAs by severity defined in the programme remain as the **mandatory floor**: EPSS and KEV may **bring forward** the remediation of an item, never **postpone it** beyond the deadline that its severity already imposes.

Applicability: **L2 and L3**. L1 systems keep prioritisation by severity; the EPSS/KEV layer is recommended where the volume of vulnerabilities exceeds the capacity for immediate remediation and requires careful ordering.

> This integration follows the principle of **anchored reference**: EPSS and KEV are instruments for ordering risk, not an authority that overrides CVSS, the contractual SLA or the formal risk acceptance decision. Neither of the two converts severity into priority automatically.

---

## EPSS — probability of exploitation {#epss--probabilidade-de-exploração}

EPSS assigns each CVE a value between **0 and 1**, corresponding to the estimated probability of exploitation within the following 30 days, and a **percentile** that positions that CVE relative to all the others. The model is updated **daily** from observed exploitation data and from characteristics of the vulnerability itself.

Properties to keep in mind when using it:

- EPSS is **predictive and probabilistic**. A high value indicates a high risk of imminent exploitation; a low value **is no guarantee** that the vulnerability will not be exploited.
- EPSS is **complementary to CVSS**, not an alternative. It measures a different dimension — likelihood, not impact.
- The value changes over time. Prioritisation must consult EPSS **at the moment of the decision**, not a value captured months earlier.

The EPSS threshold that triggers escalation must be defined by the organisation according to its remediation capacity. An initial reference threshold sits at the ≥ 0.95 percentile (among the 5% of CVEs with the highest probability of exploitation), to be calibrated with operational experience.

---

## KEV — confirmed exploitation {#kev--exploração-confirmada}

The CISA KEV catalogue, established by *Binding Operational Directive* 22-01, lists vulnerabilities for which there is **evidence of active exploitation**. Each entry includes a binding remediation deadline for US federal agencies, and works as an authoritative signal of real exploitation for any organisation.

The presence of a CVE in the KEV changes the nature of the decision:

- A vulnerability in the KEV is no longer a hypothetical risk — it is being exploited. **It must be escalated to the programme's shortest remediation deadline, regardless of its CVSS or EPSS.**
- The **absence** of a CVE from the KEV **does not mean absence of exploitation** — it only means that there is, as yet, no confirmed and catalogued exploitation. Absence from the KEV is not proof of safety.

---

## Integration into remediation prioritisation {#integração-na-priorização-de-remediação}

The order of remediation results from the composition of three signals: severity (CVSS), probability (EPSS) and confirmed exploitation (KEV). The SLA by severity sets the maximum deadline; EPSS and KEV determine what is remediated **first** within and below that deadline.

| Signal | Condition | Effect on prioritisation |
|-------|----------|-----------------------|
| KEV | CVE present in the catalogue | Immediate escalation to the shortest deadline, whatever the CVSS |
| High EPSS + high CVSS | Above the defined threshold | Top of the remediation queue within the SLA |
| High EPSS + low/medium CVSS | Above the threshold | Bring forward relative to other items of equal severity |
| Low EPSS + high CVSS | Below the threshold | Keeps the SLA by severity as the floor; does not deprioritise below it |
| Low EPSS + low CVSS | Below the threshold | Remediation within the normal SLA, without bringing forward |

The closure rule is the one that protects the floor: **the EPSS/KEV layer never delays a remediation beyond the deadline that its severity already imposes.** It brings forward; it does not postpone.

---

## Epistemic discipline {#disciplina-epistémica}

- EPSS is an **estimate**, not a measurement of certainty. Risk decisions based on it must record that the value is probabilistic and dated.
- KEV is a signal that is **incomplete by construction** — it catalogues *confirmed* exploitation, not all existing exploitation.
- Neither of the sources dispenses with the **formal exception record** when a vulnerability is not remediated within the SLA (see cross-references). A low EPSS is not, in itself, a justification for an exception.

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|-----------|---------|
| [Ch. 05 — SCA Analysis](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/analise-sca) | Detection of vulnerabilities in dependencies, primary source of CVEs to prioritise |
| [Ch. 05 — Exceptions and risk acceptance](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/excecoes-e-aceitacao-risco) | Formal process when remediation exceeds the SLA |
| [Ch. 10 — Coverage and prioritisation](/sbd-toe/sbd-manual/testes-seguranca/addon/cobertura-e-priorizacao) | Prioritisation of testing effort by risk |
| [Ch. 12 — Alerts and critical events](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/alertas-eventos-criticos) | Operational response SLAs where prioritisation materialises |

> **On curation:** Consolidated from EPSS (FIRST.org EPSS SIG), CISA KEV (*Binding Operational Directive* 22-01), CVSS (FIRST.org) and NIST SP 800-40 Rev. 4 (*Patch Management*). EPSS and KEV are external sources updated continuously; the values must be consulted at the moment of the prioritisation decision. This integration is methodological — it replaces neither the patching SLAs nor the programme's formal risk acceptance decision.
