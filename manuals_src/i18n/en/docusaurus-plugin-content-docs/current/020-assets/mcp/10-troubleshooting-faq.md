---
id: troubleshooting-faq
title: Troubleshooting & FAQ
description: Symptoms, causes and solutions for common problems with the SbD-ToE MCP — content lag, versions, debugging, integration with AI clients.
sidebar_label: Troubleshooting / FAQ
sidebar_position: 10
tags:
  - mcp
  - troubleshooting
  - faq
translation:
  source_locale: pt
  source_path: 020-assets/mcp/10-troubleshooting-faq.md
  source_sha256: 343ef2346d92dcc1d79254c9cde071fd255b9668b8f39b6ec40e140c673336de
  source_commit: 4e04c6c26f9325b8a3515d4ccd3b126f58be3b1e
  target_sha256: fcf8d491b8d2d13f4f6ce64df418a926f2000c6b9ba5ea1c406dffbfc827dc44
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 211df96a27d713b5934d7534d61f1972d877902236e63b858563d206c67ccaa8
  glossary_keys: [appsec_core, chapter_role, cycle_iteration, framework_source_corpus, llm, mcp, normative_empirical, practitioner_manual, sbdtoe_sbd, verification_taxonomy]
  glossary_sha256: b2aded4645437cae2f8533d3fa8cbca79e7c27392514cf033f43ed7a113bac82
  translated_at: 2026-09-26T14:55:23Z
  reviewed_by: null
---

# Troubleshooting & FAQ

Most of the questions that come up in the first weeks of using the MCP are not *bugs* — they are predictable misalignments: a call that returns more (or less) than expected, a client that does not recognise the server, or content that exists in the web manual but does not appear in the MCP search. This page gathers those cases, with symptom, cause and a direct solution.

## Server status {#estado-do-servidor}

### How to find the current version {#como-saber-a-versão-actual}

Read the resource:

```
sbd://toe/version
```

Returns `name`, `version` and the *provenance* of what is served — `manual`, `kg`, `ontology`, `serving_contract` and `surface_history`. The version is incremented with each *publish* to npm.

Local verification:

```bash
npm view @shiftleftpt/sbd-toe-mcp version
```

The package has no `--version` *flag*: `npx -y @shiftleftpt/sbd-toe-mcp` starts the server. For the version the client is actually using, the source is the `sbd://toe/version` resource.

### How to know whether the server is running in the client {#como-saber-se-o-servidor-está-a-correr-no-cliente}

| Client | Verification |
|---|---|
| Claude Code | `claude mcp list` |
| Claude Desktop | The tools panel shows `sbd-toe.*` in the conversation |
| Cursor | Settings → Features → MCP, green *badge* on `sbd-toe` |
| VS Code (Copilot) | In *Agent mode*, `@workspace` shows MCP connected |
| Windsurf | MCP panel, status `running` |

---

## Content lag {#content-lag}

### Symptom {#sintoma}

A page exists in the web manual, but the MCP does not return it (`search_sbd_toe_manual`, `query_sbd_toe_entities` or `inspect_sbd_toe_retrieval` without *hits* in that document).

### Cause {#causa}

The server serves a *snapshot* of the manual and the KG index built from it; the version of the manual, the KG and the ontology is in `sbd://toe/version`. Content added to the web manual **after** that *snapshot* only enters the MCP with the next publication.

### How to confirm what is indexed {#como-confirmar-o-que-está-indexado}

```
inspect_sbd_toe_retrieval({"question": "<nome do regulamento ou da página>", "topK": 5})
```

If the *top-ranked records* point to `002-cross-check-normativo/<framework>/...` (or to the expected document) → indexed. If they point only to other documents, the page may be outside the index — confirm the version in `sbd://toe/version` before concluding; a more specific question (article, section title) improves the *ranking*.

### Solution {#solução}

Read `sbd://toe/version`. If the content sought is later than the indicated *snapshot*, consult the web manual (for example, the [normative cross-check](/sbd-toe/cross-check-normativo/intro) of the regulatory frameworks) until the next MCP publication. For everything that is in the *snapshot*, use the MCP normally.

### When it occurs {#quando-ocorre}

With each npm publication the *snapshot* moves forward. The difference between the manual tag and the server version is expected and is documented in [versioning & roadmap](./11-versionamento-roadmap.md#relação-com-versões-do-manual).

---

## Performance {#performance}

### Symptom — `consult_security_requirements(L3)` is slow or overflows the context {#sintoma--consult_security_requirementsl3-é-lento-ou-estoura-o-contexto}

L3 output without `concerns` may exceed the client's context. Each response declares its size in `size_estimate`, and the guide (`sbd://toe/agent-guide`) publishes the sizes measured on the served *build*.

### Solution {#solução-1}

**Always pass `concerns`** at L2 / L3:

```json
consult_security_requirements({"risk_level": "L3", "concerns": ["auth", "encryption"]})
```

The response becomes much smaller. When full coverage is needed, iterate by *concern*.

---

## Unexpected results {#resultados-inesperados}

### Symptom — `search_sbd_toe_manual` returns *off-topic* results {#sintoma--search_sbd_toe_manual-devolve-resultados-off-topic}

### Possible cause(s) {#causas-possíveis}

1. *Vocabulary mismatch* — `authentication` was used instead of `auth` (ontological vocabulary)
2. Narrative question too vague
3. Structured question that should go to `consult_security_requirements`

### Diagnosis {#diagnóstico}

```json
inspect_sbd_toe_retrieval({"question": "<pergunta original>"})
```

Returns ranking, *scores*, *rule_trace*. Identifies whether it is *vocabulary* or *intent*.

### Solution {#solução-2}

- For *vocabulary*: use canonical terms (see [concerns](./01-intro.md#vocabul%C3%A1rio-controlado))
- For *structured intent*: prefer `consult_security_requirements` or `get_*`

---

### Symptom — `get_guide_by_role(L2)` returns only counts {#sintoma--get_guide_by_rolel2-devolve-só-contagens}

### Cause {#causa-1}

The call was made without `role` or `phase`. By design, without either of them, it returns only `role_summary{}` + `phase_summary{}`.

### Solution {#solução-3}

```json
get_guide_by_role({"risk_level": "L2", "role": "developer"})
// ou
get_guide_by_role({"risk_level": "L2", "phase": "implement"})
```

---

### Symptom — `get_threat_landscape` returns `threats: []` {#sintoma--get_threat_landscape-devolve-threats-}

### Cause(s) {#causas}

1. *Risk level* / *concerns* combination too restrictive
2. The scope genuinely has no threats catalogued in the canon
3. The *concerns* are not in the vocabulary (typo)

### Solution {#solução-4}

1. Broaden — remove *concerns*, or raise the *risk level* if applicable
2. If it remains empty: **do not invent threats** — write in the response *"Manual-grounded: no threats in the canon for this scope. Not to be confused with absence of risk — human inspection recommended."*
3. Validate the *concerns* against the [canonical table](./01-intro.md#vocabul%C3%A1rio-controlado)

---

## `prepare_sbd_toe_codegen_context` {#prepare_sbd_toe_codegen_context}

### Symptom — returns `needs_decomposition` cycle after cycle {#sintoma--devolve-needs_decomposition-em-ciclo}

### Cause {#causa-2}

Two possible causes. The declared selection exceeds the ceiling of the `detail` level — and then the response carries, in `requirement_ceiling.batches`, the executable batches whose union is the whole selection. Or the parent task is too conceptual / open-ended. In both cases, *brute force* (calling again with small *tweaks*) does not get past the gate.

### Solution {#solução-5}

1. If the response carries `requirement_ceiling.batches`: follow the batches, one at a time — do not redesign the decomposition by hand. Otherwise, accept one of the suggested sub-tasks and call again **only for that one**
2. If the sub-task also returns `needs_decomposition` → **STOP**, escalate with the user
3. Restart the session with a manual decomposition before the first call

See [Pattern 5 — Codegen iteration with failures](./08-padroes-avancados.md#padrao-5).

---

### Symptom — `unsupported_scope` {#sintoma--unsupported_scope}

### Meaning {#significado}

The installed server does not have the capability that was requested. Possible sub-causes:

| Cause | Action |
|---|---|
| `AppSec Core v1 runtime ausente` | Incomplete installation — reinstall or update the published package and report to the operator. |
| `Overlay regulatório ausente` | Remove `regulatory_frameworks` / `include_regulatory_overlay`, or wait for publication. |
| `Framework regulatório desconhecida` | List the supported *short codes* in `regulatory_overlay.frameworks`. |

**Do not fabricate** IDs to "continue" — the gate is by design.

---

### Symptom — returns `needs_input` {#sintoma--devolve-needs_input}

**Cause.** Nothing was declared. In declarative mode (the *default*), the server does not infer *concerns* or other fields from the `task`: the `task` is recorded, not interpreted.

**Solution.** The response carries the accepted vocabulary, the candidates to confirm and, for inert declarations, the `valid_values`. Confirm the candidates with the user and call again with the complete declaration — `risk_level`, `concerns`, `exposure`, `data_sensitivity`, `technologies`, `changed_files`, depending on what is known. The accepted values are in `sbd://toe/activation-vocabulary`.

---

### Symptom — `detail: "minimal"` or `detail: "ultrathin"` is rejected {#sintoma--detail-minimal-ou-detail-ultrathin-é-recusado}

**Cause.** Those levels were withdrawn. The accepted `detail` levels are `lista`, `standard` and `full`.

**Solution.** Use one of the three accepted levels. What each one puts *inline* is in the served description of `prepare_sbd_toe_codegen_context`.

---

### Symptom — `size_estimate.within_envelope: false` {#sintoma--size_estimatewithin_envelope-false}

**Cause.** The response declares that its size exceeds the expected envelope. It is a declaration, not an error: the server warns instead of truncating silently.

**Solution.** Do not ignore the warning. A more compact `detail` level, or a narrower declaration (fewer *concerns*, fewer categories), reduces the response. If the selection exceeds the level's ceiling, the response becomes `needs_decomposition` with batches — see above.

---

## Installation / client {#instalação--cliente}

### Symptom — `claude mcp add` fails with `Cannot find package` {#sintoma--claude-mcp-add-falha-com-cannot-find-package}

### Cause {#causa-3}

Node.js `< 20.9.0` or npm without access to the public registry.

### Solution {#solução-6}

```bash
node --version          # confirmar ≥ 20.9.0
npm config get registry # confirmar https://registry.npmjs.org/
```

---

### Symptom — Cursor / Claude Desktop does not recognise the server {#sintoma--cursor--claude-desktop-não-reconhece-o-servidor}

### Cause(s) {#causas-1}

1. Configuration file in the wrong path
2. Invalid JSON (trailing comma, wrong quotes)
3. Client not restarted after editing

### Solution {#solução-7}

1. Confirm the path (see [Installation](./03-instalacao.md))
2. Validate the JSON: `jq . < /path/to/config.json` — errors show up
3. **Restart the client** after each change to the MCP configuration

---

### Symptom — `sbd-toe.*` tools appear but every call fails {#sintoma--tools-sbd-toe-aparecem-mas-todas-as-chamadas-falham}

### Diagnosis {#diagnóstico-1}

Run the command manually to isolate the problem:

```bash
npx -y @shiftleftpt/sbd-toe-mcp
```

The server writes nothing to *stderr* on start-up — silence is not a sign of error. To validate it, send it an `initialize` message of the MCP protocol or, in Claude Code, run `claude mcp list`. If the `initialize` message gets no response, the problem lies with the server / Node / dependencies.

---

## Operational {#operacional}

### Symptom — the MCP output is in PT, but the user writes in EN {#sintoma--output-do-mcp-é-em-pt-mas-o-utilizador-escreve-en}

### It is not a bug — it is architecture {#não-é-bug--é-arquitectura}

The canonical content of the manual is in PT. The *agent guide* says explicitly:

> *Always respond in the user's language. The manual content is in Portuguese — translate, summarise, and explain in whatever language the user writes in.*

**Solution:** the LLM must **translate / summarise** the PT content into the user's language. It should not switch to PT just because the manual is in PT.

---

### Symptom — the user disagrees with the *risk level* {#sintoma--utilizador-discorda-do-risk-level}

### Action {#acção}

Do not decide unilaterally. Present:

1. What `map_sbd_toe_applicability` suggests
2. What would change if `risk_level` were X vs Y (cost: the demand of each chapter changes; the set of chapters is the same)
3. Who signs off the decision (`CISO`, `executive_management`, `appsec`)

Mark as `inferred` while there is no decision.

---

## *Upgrades* and versioning {#upgrades-e-versionamento}

### When to re-run `generate_sbd_toe_skill` {#quando-re-correr-generate_sbd_toe_skill}

After each *upgrade* of the MCP server (minor/patch releases on npm). The content of the *agent guide* may change; the skill on disk is outdated until it is regenerated.

### How to know whether the skill is outdated {#como-saber-se-a-skill-está-desactualizada}

The skill on disk starts with:

```
<!-- SbD-ToE skill content — source: sbd://toe/agent-guide (@shiftleftpt/sbd-toe-mcp) -->
```

It does not include an explicit version — compare `sbd://toe/version` with the version used in the last generation (keep it as a project *changelog* entry).

---

## When to report a bug {#quando-reportar-bug}

Report at [github.com/SbD-ToE/sbd-toe-mcp/issues](https://github.com/SbD-ToE/sbd-toe-mcp/issues) if:

- `inspect_sbd_toe_retrieval` shows an incoherent *rule_trace*
- The output directly contradicts what the web manual says for a canon chapter
- A tool returns a *schema* different from the documented one
- Tools listed as available fail 100% of calls

Include in the report:
- The MCP version (`sbd://toe/version`)
- Client and version
- Exact input of the call
- Output received
- Expected output

## Next steps {#a-seguir}

- [Versioning and roadmap](./11-versionamento-roadmap.md) — release notes + the future.
