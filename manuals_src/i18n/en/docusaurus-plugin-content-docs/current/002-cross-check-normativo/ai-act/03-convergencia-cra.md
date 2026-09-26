---
id: convergencia-cra
title: Note - AI Act & CRA Convergence
description: Guidance for products that are simultaneously a high-risk AI system (AI Act) and a product with digital elements (CRA) - presumption of conformity under Article 12 of the CRA and a single conformity assessment on the cybersecurity axis
sidebar_position: 3
tags: [ai-act, cra, convergencia, presuncao-conformidade, ciberseguranca]
translation:
  source_locale: pt
  source_path: 002-cross-check-normativo/ai-act/03-convergencia-cra.md
  source_sha256: 73d1b51774d51ecd12417ebb39b8485b0dc6c06343ab392c4bd4ee2935e35308
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: a741cf34f5694c301a2d9b460e3bd04f48038fa9decc308b3ee0d088dc9096f3
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 5f18169e44cb78faceac7d31df119020c508135f27e39f4105f054ecf5a72d33
  glossary_keys: [avaliacao, chapter_role, cra_actively_exploited_vulnerability, cra_pde, cycle_iteration, eu_ai_high_risk_system, eu_ai_human_oversight, eu_ai_system, eu_ce_marking, eu_notified_body, framework_source_corpus, layer, lifecycle_phase, practitioner_manual, provenance, requirement_runtime, role_juridico, sbdtoe_sbd, slug_threat_modeling, transversal]
  glossary_sha256: 115a96b7a2c4c9c99d7fbe583336a11973bc44b64520c53c4c85864314ce0afb
  translated_at: 2026-09-26T18:11:54Z
  reviewed_by: null
---

# Note: Products covered by the AI Act and the CRA

## Scope {#âmbito}

This note is intended for manufacturers of **products with digital elements** that are, at the same time, **high-risk AI systems** (AI Act, Art. 6) and products covered by the **Cyber Resilience Act** (Regulation (EU) 2024/2847). Unlike the NIS2 ↔ DORA relationship - two organisational risk management regimes resolved by *lex specialis* -, here the relationship is one of **presumption of conformity** and a **single conformity assessment** on the cybersecurity axis.

The two regulations apply **cumulatively**, but the legislator built an explicit bridge at the technical cybersecurity level to avoid duplicated work.

## The relationship is not *lex specialis* - it is a presumption of conformity {#a-relação-não-é-lex-specialis---é-presunção-de-conformidade}

**Article 12 of the CRA** establishes that a product classified as a high-risk AI system pursuant to Article 6 of the AI Act is **deemed to comply with the cybersecurity requirements set out in Article 15 of the AI Act** where three conditions are cumulatively met:

| Condition (CRA Art. 12) | What it requires | Where SbD-ToE comes in |
|---|---|---|
| Annex I, **Part I** of the CRA | Essential cybersecurity requirements of the **product** | [Ch. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro) (architecture), [Ch. 10](/sbd-toe/sbd-manual/testes-seguranca/intro) (testing), [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) |
| Annex I, **Part II** of the CRA | **Vulnerability handling** requirements (the manufacturer's processes) | [Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) (SBOM/SCA), [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) |
| EU declaration of conformity | Demonstrate in it the level of cybersecurity required by Article 15 of the AI Act | Aggregated technical evidence (Ch. 03–12) |

Once all three are met, **there is no need to demonstrate** Article 15 of the AI Act **separately**: declared conformity with the CRA counts as conformity with that AI Act requirement.

## Single conformity assessment {#avaliação-de-conformidade-única}

CRA Art. 12 refers the assessment to the **conformity assessment procedure of Article 43 of the AI Act**. In addition, the **notified bodies** competent for the high-risk AI system under the AI Act are also competent to control conformity with Annex I of the CRA (subject to Article 39 of the CRA). Practical result: **one assessment, one body, one declaration** - covering the cybersecurity axis of both regulations.

> ⚖️ **Derogation.** Certain important and critical products (CRA, Annexes III and IV) may follow alternative conformity assessment procedures provided for in the CRA, depending on their classification and on any certificates. The choice of procedure is a compliance/legal matter.

## Where the scopes intersect and where they diverge {#onde-os-âmbitos-se-cruzam-e-onde-divergem}

| Topic | AI Act | CRA | Convergence |
|---|---|---|---|
| Product cybersecurity | Art. 15 | Annex I, Parts I and II | **Presumption** (CRA Art. 12) |
| Vulnerability handling | Implicit in Art. 15 | Annex I, Part II (detailed) | Common technical basis — the presumption (CRA Art. 12) is the conformity mechanism, not the mere adoption of the process |
| Supply chain / SBOM | Art. 15 (integrity) | Annex I | Single SBOM ([Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)) |
| Reporting | Art. 73 (serious incidents) | Art. 14 (actively exploited vulnerabilities / severe incidents to ENISA) | **Separate** channels, shared detection basis ([Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)) |
| CE marking / declaration | Art. 43, 47–49 | CRA assessment | Coordinated via Art. 12 |
| Data governance, human oversight, transparency, FRIA | Art. 10, 13, 14, 27 | — | **AI Act only** (outside the CRA and SbD-ToE) |

## What remains specific to each regulation {#o-que-continua-próprio-de-cada-regulamento}

**AI Act only** (not covered by the CRA presumption): risk management (Art. 9), data governance and bias (Art. 10), human oversight (Art. 14), transparency (Art. 13 and 50), fundamental rights impact assessment (Art. 27) and the GPAI obligations (Art. 53/55). The presumption in Article 12 of the CRA **covers only Article 15** (cybersecurity) - all the other high-risk obligations of the AI Act remain in full.

**CRA only**: vulnerability handling throughout the whole lifecycle (Annex I, Part II), coordinated vulnerability disclosure, the obligation to provide security updates and a support period, and the reporting of actively exploited vulnerabilities to ENISA/CSIRT (Art. 14).

## Duplication Risks (Avoid) {#riscos-de-duplicação-evitar}

| Potential duplication | Why avoid it | Recommended single form |
|---|---|---|
| Two cybersecurity conformity assessments | Cost and inconsistency | Invoke the presumption of CRA Art. 12; a single assessment (Art. 43 AI Act) |
| Two *vulnerability handling* processes | Divergence of SLAs/records | Implement the CRA one (Annex I, Part II); it also serves Art. 15 |
| Two SBOM inventories | Overhead, drift | Single SBOM/AI-BOM ([Ch. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)) |
| Two technical evidence bases | Rework | Single cybersecurity evidence ([Ch. 03](/sbd-toe/sbd-manual/threat-modeling/intro), [04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [10](/sbd-toe/sbd-manual/testes-seguranca/intro), [12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)) tagged by source |

## Single Implementation Strategy (SbD-ToE) {#estratégia-de-implementação-única-sbd-toe}

> ✏️ **Refresh 2026-05-30.** Strategy updated after the *agentic release* — several pieces that were "to be implemented" are now within the canon ([`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012), `OPS-012..014`, Policy 38, Policy 39).

1. **Single cybersecurity evidence** ([Ch. 03 agentic playbook](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic), [Ch. 04 `ARC-014`/`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), [Ch. 10 §C5](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites), [Ch. 12 + `OPS-011..014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle)) — serves Article 15 of the AI Act and Annex I (Parts I and II) of the CRA at the same time.
2. **Single vulnerability handling process** ([Ch. 05 `DEP-011..014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011), [Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Policy 39 §7](/sbd-toe/assets/policies/policy-ai-bom-supply-chain)) in accordance with Annex I (Part II) of the CRA — it also covers the robustness required by Art. 15, including the response to *upstream* incidents in the AI supply chain (`AML.T0019`, `AML.T0109`, `AML.T0110`).
3. **Single SBOM + AI BOM** ([Ch. 05 `DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012) in CycloneDX 1.6 *ml-bom* format, [Policy 39](/sbd-toe/assets/policies/policy-ai-bom-supply-chain)) feeding both regulations — satisfies CRA Annex I Part II(1) (SBOM) **and** AI Act Art. 10 (data/provenance) **and** Art. 11/Annex IV (list of components).
4. **EU declaration of conformity** demonstrating the level of cybersecurity of Art. 15, invoking the presumption of Article 12 of the CRA. Contractual clauses with AI *providers* (Ch. 14 US-21 + Policy 33 §10) declare conformity with Art. 53/55 when GPAI.
5. **Single conformity assessment** by the AI Act notified body (Art. 43), extended to Annex I of the CRA.
6. **Regulatory origin matrix** — in the catalogue of [Ch. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), column `Fonte` with enum `AI Act`, `CRA`, `Ambos`, `Outras`.
7. ⚡ **Cross-cutting agentic layer** — [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (agent as *principal*), `REQ-AGN-001..004` (mandate, *kill-switch*, *intent*), `OPS-012..014` (audit per *tool*, *budget*, *jailbreak detection*) and Policy 38 (*mandates lifecycle*) provide technical controls relevant to Art. 14, Art. 15 and Art. 26 of the AI Act and to Annex I (Parts I and II) of the CRA (*cybersec by design*). These controls are **technical evidence, not a declaration of conformity**: the **CRA (Art. 12) establishes** a presumption of conformity **only with Article 15** of the AI Act (cybersecurity) when Annex I is fulfilled and demonstrated in the EU declaration of conformity. Art. 14 (human oversight) and Art. 26 (deployer) are **not** covered by that presumption — they remain obligations in their own right.

## Convergence Checklist (YES = ready) {#checklist-de-convergência-sim--pronto}

- [ ] Cybersecurity evidence mapped simultaneously to Art. 15 (AI Act) and to Annex I, Parts I and II (CRA) — including [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) and *eval suites* (Ch. 10 §C5).
- [ ] *Vulnerability handling* process in accordance with Annex I, Part II (CRA) documented, with an extension to the *upstream* AI supply chain (Policy 39 §7).
- [ ] EU declaration of conformity demonstrates the level of cybersecurity of Art. 15 (CRA Art. 12).
- [ ] Single conformity assessment (Art. 43 AI Act) agreed with the notified body.
- [ ] Single SBOM + AI BOM (CycloneDX 1.6 `ml-bom` for the AI part) covers both regulations.
- [ ] Separate reporting channels (AI Act Art. 73 / CRA Art. 14) with a shared technical detection basis ([`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 30 §9.3).
- [ ] Ch. 02 catalogue with column `Fonte` filled in (AI Act / CRA / Both).
- [ ] *Mandates* (Policy 38) declare both the A0–A4 level (AI Act Art. 14) and *cybersec measures* (CRA Annex I Part I).
- [ ] There are no divergent parallel cybersecurity processes.

## Frequently Asked Questions {#perguntas-frequentes}

**Q1. Is it necessary to carry out two cybersecurity conformity assessments?**
No. CRA Art. 12, read together with Article 43 of the AI Act, allows a single assessment - the same notified body can control both.

**Q2. Does the CRA replace Article 15 of the AI Act?**
It does not replace it. It creates a **presumption of conformity** with Art. 15 when Annex I (Parts I and II) is fulfilled and demonstrated in the declaration. The other high-risk obligations of the AI Act remain.

**Q3. What about vulnerability handling?**
Implement the CRA one (Annex I, Part II) - it is the most detailed and, by construction, satisfies the robustness/cybersecurity expected by Art. 15.

**Q4. Are the reports the same?**
No. The AI Act (Art. 73, serious incidents) and the CRA (Art. 14, actively exploited vulnerabilities/severe incidents to ENISA) have different triggers, deadlines and channels. They share **technical detection** ([Ch. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)); submission is parameterised by regulation.

## References {#referências}

- Regulation (EU) 2024/1689 (AI Act) - Art. 6, 15, 43.
- Regulation (EU) 2024/2847 (CRA) - Art. 12, Art. 14, Annex I (Parts I and II), Annexes III/IV.
- [Cross-check AI Act](/sbd-toe/cross-check-normativo/ai-act/intro) and [Cross-check CRA](/sbd-toe/cross-check-normativo/cra/intro) (in this chapter).
- SbD-ToE Manual ([Ch. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)–[Ch. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)).

## Final Note {#nota-final}

SbD-ToE already abstracts the technical cybersecurity controls. AI Act/CRA convergence materialises by **using the same technical evidence for both** and by invoking the presumption of Article 12 of the CRA: **one assessment, one declaration, two regulations satisfied on the cybersecurity axis** - without redundancy, while keeping the obligations specific to each regime.
