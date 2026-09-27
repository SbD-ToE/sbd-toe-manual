---
id: cross-check-conformidade
title: Normative cross-check
description: Cross-referencing SbD-ToE with the AI Act, CRA, DORA, NIS2, GDPR — with the MCP (canon and indexed cross-checks) and the web manual for content later than the snapshot.
sidebar_label: Normative cross-check
sidebar_position: 6
tags:
  - mcp
  - casos-uso
  - compliance
  - ai-act
  - cra
  - dora
  - nis2
  - gdpr
translation:
  source_locale: pt
  source_path: 020-assets/mcp/07-casos-uso/06-cross-check-conformidade.md
  source_sha256: ff453063fea93cbefbdbf137419b723f90b4e67a3b355fe0a46544e1c1558053
  source_commit: 5caf1bb9d128df1f7fb0b1e5b2a5603db3e6127f
  target_sha256: f86bd543ceb89da10039aa50f62ea0bbd558d8601d9e5faeb1d606953ea84aa8
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 740bf440657434f2680e8b3e2e5b7f069a9b07bceba4d9fc3fab698ab88c4a2f
  glossary_keys: [appsec_core, avaliacao, chapter_role, discipline, eu_notified_body, framework_source_corpus, mcp, normative_empirical, papel_suporte, practitioner_manual, requirement_runtime, sbdtoe_sbd]
  glossary_sha256: 4a0acf899b203bd594e77aef311b79be1dd101b693ad47e580abe900849dd756
  translated_at: 2026-09-27T08:34:24Z
  stamped_at: 2026-09-27T08:34:24Z
  reviewed_by: null
---

# Use case — Normative cross-check

Sooner or later, someone in the company — *legal*, internal audit, a B2B client in the contract — will want to see, on paper, how engineering practices respond to a specific regulation. AI Act, CRA, DORA, NIS2, GDPR. The question is not "are we compliant?" (that one is legal) — it is "how does the SbD-ToE respond to this article?" (that one is technical).

This recipe serves the second. It combines the MCP (where the published normative cross-checks are indexed) with direct reading of the web manual (needed for content later than the published *snapshot*). The result is a technical report that cites the regulation *verbatim*, the SbD-ToE chapters and controls with real IDs, and explicitly marks what is not covered — without ever sliding into a declaration of compliance.

## Current coverage in the MCP — what is in and what is out {#cobertura-actual-no-mcp--o-que-está-dentro-e-fora}

The served *snapshot* includes the canon (chapters 00–14), the *AppSec Core v1* ontology **and** the published cross-checks — **CRA**, **DORA**, **NIS2**, **GDPR**, **AI Act** and **ENISA/CSA** — indexed in the KG; the exact version is in `sbd://toe/version`. For these, the MCP is the recommended source: `get_sbd_toe_playbook` returns the published playbooks per legal instrument, with the declared authority; `map_sbd_toe_regulatory_activation` / `resolve_entities` expose the regulatory overlay (frameworks, obligations, mappings); and `search_sbd_toe_manual` returns the intros, playbooks and convergence notes with citations.

The boundary is the *snapshot*: content added to the web manual **after** it lives only in the web manual until the next publication. The served version is in `sbd://toe/version` (see [content lag](../10-troubleshooting-faq.md#content-lag)).

| Question | Recommended source |
|---|---|
| "Which `CTRL-*` controls apply to `auth` at L2?" | **MCP** (`consult_security_requirements`) |
| "What threats exist for `encryption` at L3?" | **MCP** (`get_threat_landscape`) |
| "Which playbook does the manual publish for NIS2?" | **MCP** (`get_sbd_toe_playbook`) — playbook per legal instrument, declared authority |
| "Is there a published cross-check for ISO, PCI or SOC2?" | **MCP** (`get_sbd_toe_playbook`) — for ISO, PCI, SOC2, … the response declares `no_cross_check` |
| "How does the SbD-ToE respond to CRA Art. 12?" | **MCP** (`search_sbd_toe_manual`) — **CRA** cross-check indexed |
| "How does the SbD-ToE map NIS2 Art. 21?" | **MCP** (`search_sbd_toe_manual`) — **NIS2** cross-check indexed |
| "Which DORA / GDPR obligations apply to my project?" | **MCP** — **DORA** and **GDPR** cross-checks indexed |
| "How does the SbD-ToE respond to Art. 15 of the AI Act?" | **MCP** (`search_sbd_toe_manual`) — **AI Act** cross-check indexed; the [web cross-check](/sbd-toe/cross-check-normativo/ai-act/intro) for a full reading |

### How to confirm before answering {#como-confirmar-antes-de-responder}

When in doubt about whether a framework is in the KG, run:

```json
inspect_sbd_toe_retrieval({"question": "<framework>", "topK": 5})
```

If the top-ranked records point to `002-cross-check-normativo/<framework>/...` → indexed. Otherwise → consult the web manual.

## Flow {#fluxo}

### 1. Identify the regulatory obligation {#1-identificar-a-obrigação-regulatória}

From the primary source (EUR-Lex / text of the regulation), extract:
- Article (e.g. AI Act Art. 15 — «Accuracy, robustness and cybersecurity»)
- Key concepts (e.g. «adversarial examples or model evasion», «data poisoning» — Article 15(5))

### 2. Locate the answer {#2-localizar-a-resposta}

Two routes depending on the framework:

**Via MCP — main path** (CRA, DORA, NIS2, GDPR, AI Act, ENISA/CSA — indexed):

1. `get_sbd_toe_playbook` — the published playbook for the legal instrument, with the declared authority. For frameworks without a published cross-check (ISO, PCI, SOC2, …), the response declares `no_cross_check`: it is the signal not to improvise a correspondence.
2. `map_sbd_toe_regulatory_activation(framework)` — which chapters of the manual the *framework* activates.
3. `search_sbd_toe_manual` for the cross-check excerpts on a specific article:

```json
search_sbd_toe_manual({"question": "Art. 12 CRA presumição de conformidade", "topK": 8})
```

Returns the relevant cross-check excerpts with `chapter_id`, `Document path`, `Localização` (lines) and a link to the web manual.

**Web manual** (always available; for a full reading and for content later than the *snapshot*):

- [AI Act](/sbd-toe/cross-check-normativo/ai-act/intro) · [Playbook](/sbd-toe/cross-check-normativo/ai-act/playbook) · [CRA convergence](/sbd-toe/cross-check-normativo/ai-act/convergencia-cra)
- [CRA](/sbd-toe/cross-check-normativo/cra/intro) · [Playbook](/sbd-toe/cross-check-normativo/cra/playbook)
- [DORA](/sbd-toe/cross-check-normativo/dora/intro) · [Playbook](/sbd-toe/cross-check-normativo/dora/playbook) · [Convergence](/sbd-toe/cross-check-normativo/dora/convergencia-dora)
- [NIS2](/sbd-toe/cross-check-normativo/nis2/intro) · [Playbook](/sbd-toe/cross-check-normativo/nis2/playbook)
- [GDPR](/sbd-toe/cross-check-normativo/gdpr/intro)
- [ENISA & CSA](/sbd-toe/cross-check-normativo/enisa-csa/intro)

### 3. Anchor in the canon's controls (via MCP) {#3-anchorar-nos-controlos-do-canon-via-mcp}

For the controls that the cross-check refers to:

```json
query_sbd_toe_entities({"query": "ARC-001"})
```

→ resolves the exact id (requirement/control) and extracts name + domain + chapter. For derived controls, use `consult_security_requirements(risk_level, concerns)`.

### 4. Structure the report {#4-estruturar-o-relatório}

```markdown
# Cross-check SbD-ToE × <Regulamento> Art. <N>

## Obrigação regulatória
- **Fonte:** <regulamento, artigo, número, alínea>
- **Texto:** <verbatim do regulamento>
- **Conceitos-chave:** <lista>

## Resposta SbD-ToE (manual-grounded)

### Cobertura por capítulo
- Cap. <N> "<título>" — <controlos relevantes CTRL-*>
- ...

### Controlos citáveis
| ID | Descrição | Capítulo |
|---|---|---|
| CTRL-... | ... | ... |

## Convergências
<se aplicável — ex.: CRA Art. 12 + AI Act Art. 15>

## Resíduo / gap
<o que o SbD-ToE não cobre directamente>
```

### 5. **Do not declare compliance** {#5-não-declarar-conformidade}

The cross-check **shows how the manual responds** to the regulation — it does **not** declare legal compliance. Compliance requires:

- **Operational evidence** (logs, attestations, audit reports)
- **Decision by *legal counsel*** or DPO/CISO
- **External assessment** when regulation so requires (e.g. AI Act, Article 43, in cases where the conformity assessment procedure involves a notified body — Annex VII; systems in Annex III, points 2 to 8, follow the internal control of Annex VI — Article 43(2))

**Always** mark the report as *"technical cross-check — not a declaration of compliance"*.

## Output discipline {#disciplina-de-output}

- `CTRL-*` IDs only if returned by `query_sbd_toe_entities` or `consult_security_requirements`.
- Citations of the regulation **verbatim** with a precise reference (article, paragraph, point).
- Differentiate:
  - **manual-grounded** (from the SbD-ToE canon or from an indexed cross-check, via MCP — cite exact `Document path` and `chapter_id`)
  - **cross-check-web-grounded** (from the web manual — use when the content **is not** in the MCP, because it is later than the *snapshot*)
  - **inferred** (deduced — mark it)
  - **not verified** (unconfirmed — do not use as fact)

## Skill / subagent — Claude Code {#skill--subagent--claude-code}

`.claude/agents/sbd-toe-compliance.md`:

```markdown
---
name: sbd-toe-compliance
description: Cross-check SbD-ToE × regulamento UE. Usa MCP para os frameworks indexados (CRA, DORA, NIS2, GDPR, AI Act, ENISA-CSA); usa manual web para conteúdo posterior ao snapshot. NUNCA declara conformidade.
tools: WebFetch, Read, mcp__sbd-toe__*
---

# Workflow

1. Identificar regulamento + artigo alvo. Validar contra EUR-Lex se possível.
2. Validar indexação no MCP com inspect_sbd_toe_retrieval(question="<framework>", topK=5).
3. Se indexado: get_sbd_toe_playbook para o playbook do diploma (no_cross_check → não improvisar), map_sbd_toe_regulatory_activation para os capítulos ativados, search_sbd_toe_manual para excertos do cross-check.
4. Se NÃO indexado (conteúdo posterior ao snapshot): WebFetch a /sbd-toe/cross-check-normativo/<framework>/.
5. Para cada CTRL-* / capítulo referido, validar via MCP (query_sbd_toe_entities).
6. Estruturar relatório com 4 rótulos: manual-grounded, cross-check-web-grounded, inferred, not verified.
7. Marcar como "cross-check técnico — não declaração de conformidade".
8. Em dúvida: preferir "not verified" a inventar uma ligação.
```

## Anti-patterns {#anti-patterns}

- ❌ Inventing SbD-ToE ↔ regulation links that are not in the published cross-check.
- ❌ Declaring "compliant with X" — the cross-check **demonstrates technical coverage**, not legal compliance.
- ❌ Relying **only** on the MCP for content later than the *snapshot* — confirm in `sbd://toe/version`; consult the web manual for what has not yet been published.
- ❌ Forgetting to search via the MCP for the cross-checks that **are** indexed (CRA, DORA, NIS2, GDPR, AI Act, ENISA/CSA) — it duplicates work needlessly.
- ❌ Forgetting convergences (AI Act ↔ CRA, NIS2 ↔ DORA) — duplicated work and invisible *gaps*.

## Related {#relacionado}

- [Use cases — Governance bootstrap](./governance-bootstrap) — to create the repo with placeholders for the regulatory artefacts already in place.
- [Troubleshooting / FAQ](../10-troubleshooting-faq.md#content-lag) — on the MCP *content lag*.
