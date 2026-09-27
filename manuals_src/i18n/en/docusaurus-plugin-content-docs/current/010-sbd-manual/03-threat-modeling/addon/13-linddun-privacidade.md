---
id: linddun-privacidade
title: LINDDUN — Privacy Threat Modelling
description: The LINDDUN methodology for privacy threat modelling — the seven threat categories, mapping to data flow diagrams and application to any system with personal or regulated data, at all levels. It complements security threat modelling (STRIDE); it does not replace the legal compliance assessment.
tags: [LINDDUN, privacidade, threat-modeling, RGPD, DPIA, dados-pessoais, DFD, KU-Leuven, L1, L2, L3]
sidebar_position: 13
translation:
  source_locale: pt
  source_path: 010-sbd-manual/03-threat-modeling/addon/13-linddun-privacidade.md
  source_sha256: f9cb00175e50543d01296a1ed33d6bdf262f4a17861fca5dce0d2c481bc08cd3
  source_commit: 44d2d3451e163f3ad4ab710e3ee2ec8d02f9e02d
  target_sha256: 78924f59516027d7aff592261bc2d1918781accc40a3e9dabb017de389337ec9
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [avaliacao, chapter_role, framework_source_corpus, instrument, layer, mapping, papel_suporte, practitioner_manual, slug_threat_modeling, threat]
  glossary_sha256: a88ae20b313c3760a5d3bd210d1a79e3d1ce60974a6b6aae415c78c3563da897
  translated_at: 2026-09-27T18:03:20Z
  stamped_at: 2026-09-27T18:03:20Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# LINDDUN — Privacy Threat Modelling

## Scope and purpose {#âmbito-e-propósito}

Security threat modelling (STRIDE) protects the system against an adversary. **Privacy** threat modelling protects the person whose data the system processes — a distinct problem, with threats that STRIDE does not capture. LINDDUN, developed at KU Leuven, is the reference methodology for that problem.

The manual already includes an [applied example of LINDDUN](/sbd-toe/sbd-manual/threat-modeling/exemplo-privacidade-lindunn). This addon provides the **method** behind it, so that it can be applied to any system, and not merely followed as an example.

Applicability: any system that processes **personal or regulated data**, at all levels (`THR-003`). At L1, in lightweight form: the seven categories worked through over the personal-data flows. At L2 and L3, as a formal analysis; at L3, with independent review by the DPO. Where there is an obligation to carry out a *Data Protection Impact Assessment* (DPIA) under the GDPR, LINDDUN is the instrument that structures its technical component.

> LINDDUN structures the **elicitation** of privacy threats. It does not replace the legal compliance assessment or the DPO's opinion — the *Non-compliance* category points to legal obligations; it does not resolve them.

---

## The seven threat categories {#as-sete-categorias-de-ameaça}

The acronym names seven types of privacy threat:

| Category | Threat |
|-----------|--------|
| **Linking** | Relating two items of interest (data or actions) that refer to the same person, without necessarily identifying them |
| **Identifying** | Identifying a specific person from a set of data |
| **Non-repudiation** | Making it impossible for the person to deny an action or claim attributed to them |
| **Detecting** | Inferring the existence of an item of interest about the person, even without accessing its content |
| **Data Disclosure** | Exposing or improperly accessing personal data |
| **Unawareness** | The person is not informed about the collection, processing or sharing of their data |
| **Non-compliance** | The system does not comply with data protection principles and obligations |

> The current nomenclature (*Linking, Identifying, Detecting, Data Disclosure*) replaces the earlier terms still found in older material (*Linkability, Identifiability, Detectability, Disclosure of information*). They are equivalent.
>
> The *Non-repudiation* category is, in privacy, a **threat** — the opposite of its role in security, where non-repudiation is an objective. For the person, the impossibility of denying an action can be a risk (for example, exposing a political or health orientation). The inversion is deliberate and must be understood when applying the model.

---

## The method {#o-método}

1. **Model the system in a DFD.** Represent the system in a *data flow diagram* — external entities, processes, data stores and data flows. The DFD is the basis onto which the threats are mapped; without it, elicitation is diffuse.
2. **Map categories to the DFD elements.** Each element type is susceptible to a subset of the seven categories. The element–category mapping is what makes the analysis systematic rather than dependent on intuition.
3. **Elicit concrete threats.** From each (element, category) pair, derive specific threats, supported by the LINDDUN *threat trees* or, in a lighter approach, by the **LINDDUN GO** cards.
4. **Prioritise and mitigate.** Order the threats by risk to the person and by data sensitivity (Ch. 01), and derive privacy requirements and mitigation measures — minimisation, anonymisation, consent, transparency.
5. **Link to legal obligations.** Anchor the threats and mitigations to the applicable obligations (GDPR, DPIA), in coordination with the DPO. The *Non-compliance* category is the bridge to this layer.

---

## Relation to security threat modelling {#relação-com-o-threat-modeling-de-segurança}

LINDDUN and STRIDE are complementary, not interchangeable. A system can be secure and, at the same time, violate privacy — collecting excessive data, retaining without a legal basis, allowing re-identification. Privacy is not a subset of security. Systems that process personal data must apply both, on the same DFD.

---

## Cross-references {#referências-cruzadas}

| Document | Relation |
|-----------|---------|
| [Ch. 03 — Privacy example (LINDDUN)](/sbd-toe/sbd-manual/threat-modeling/exemplo-privacidade-lindunn) | Concrete application of this method |
| [Ch. 03 — Methodologies and tools](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas) | Security threat modelling (STRIDE), complementary |
| [Ch. 01 — Application classification](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro) | Data sensitivity as the basis for prioritisation |

> **On curation:** Consolidated from LINDDUN (KU Leuven, linddun.org), the GDPR (DPIA and minimisation obligations) and the NIST Privacy Framework. Privacy threat elicitation methodology — it complements security threat modelling and does not replace the legal compliance assessment.
