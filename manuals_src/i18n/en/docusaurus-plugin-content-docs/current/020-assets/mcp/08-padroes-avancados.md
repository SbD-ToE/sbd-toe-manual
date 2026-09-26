---
id: padroes-avancados
title: Advanced patterns
description: Multi-tool sequences for complex problems — security plan, per-release checklist, change set analysis, findings sweep.
sidebar_label: Advanced patterns
sidebar_position: 8
tags:
  - mcp
  - padroes
  - workflows
translation:
  source_locale: pt
  source_path: 020-assets/mcp/08-padroes-avancados.md
  source_sha256: 6adc184dac1d541b98aeede8f235b04a1dc45ed90843e200cab54c7fae28b657
  source_commit: 058f86265e07bc86cb7f19162dd2c6b87fbcc0a7
  target_sha256: b054e633dee563b626c1d777eae69919947a5e1f277e4f0f679075b3aa308616
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 211df96a27d713b5934d7534d61f1972d877902236e63b858563d206c67ccaa8
  glossary_keys: [chapter_role, cycle_iteration, deterministic, discipline, lifecycle_phase, mapping, mcp, normative_empirical, practitioner_manual, requirement_runtime]
  glossary_sha256: b8ec3bd5388ea94ee08aeebe95537f90dcc90e808bac6f263d6681ddcab944df
  translated_at: 2026-09-26T16:42:05Z
  reviewed_by: null
---

# Advanced patterns

As the MCP is used in real projects, it becomes evident that some tasks need several chained calls to produce a defensible answer — a *security plan* does not come out of a single *tool*, nor does a periodic audit. This section gathers those chains as named **patterns** with a purpose, so that they need not be rediscovered each time.

All of them combine the same *toolkit*: the deterministic ones (`select_sbd_toe_requirements`, `consult_security_requirements`, `get_threat_landscape`, `get_guide_by_role`, `prepare_sbd_toe_codegen_context`) where stable, citable answers are needed; the search ones (`search_sbd_toe_manual`, `query_sbd_toe_entities`) when what is missing is discovering what exists in the manual.

## The `next` band — suggested chaining {#a-banda-next--encadeamento-sugerido}

Many tools return, in addition to the deterministic `data`, a **`next`** band (up to 3 affordances, *structural* + *semantic*): the suggested next step to chain, already carrying the *tool* and its arguments. It is the thread that links the patterns below — instead of guessing the next step, follow the `next` of the previous response. Paginated tools also carry `coverage.hasMore` / `nextOffset` to continue without truncating.

---

## Entry pattern — which requirements apply to this task {#padrão-de-entrada--que-requisitos-se-aplicam-a-esta-tarefa}

**Goal:** start from a concrete task and arrive at the requirements that cover it, the context to implement it and the expected proof — without the server guessing what was not declared.

```
1. select_sbd_toe_requirements(risk_level, concerns, exposure,
                               data_sensitivity, technologies, changed_files)
   ↳ seleção declarativa e determinística
     (sem declaração → needs_input, com o vocabulário aceite)

2. prepare_sbd_toe_codegen_context(...mesma declaração, detail)
   ↳ contexto para codegen / review / test-plan, com citations

3. get_sbd_toe_verification_matrix(risk_level, requirement_ids)
   ↳ método de validação + evidência esperada por requisito selecionado
     (até 50 requirement_ids por chamada)
```

**Output:** for each selected requirement, the citable id, what the implementation has to guarantee and the evidence the *reviewer* must find.

---

## Pattern 1 — Security plan for a feature {#padrão-1--security-plan-de-uma-feature}

**Goal:** a security plan document for a new feature, before development.

```
1. consult_security_requirements(risk_level, concerns)
   ↳ controlos + requisitos activos para os concerns da feature

2. get_threat_landscape(risk_level, concerns)
   ↳ threats relevantes + mitigações estruturais

3. get_guide_by_role(risk_level, "arquitetos-software", "design")
   ↳ práticas de design + user stories

4. get_guide_by_role(risk_level, "developer", "implement")
   ↳ práticas de implementação + acceptance criteria

5. → gerar plan citando IDs de cada etapa
```

**Output structure:**

```markdown
# Security Plan — <feature>

## 1. Escopo
- Risk level, concerns, surface técnica

## 2. Requisitos aplicáveis (CONSULT)
- Lista CTRL-* + REQ-* com origem

## 3. Threat model (THREATS)
- MT-* + mitigações + confidence

## 4. Práticas por fase (GUIDE)
- Design: practice IDs + user stories
- Implement: practice IDs + acceptance criteria

## 5. Acceptance gates
- Critérios objectivos derivados de 2+3+4

## 6. Resíduo
- O que não está coberto
```

---

## Pattern 2 — Release checklist (deploy gate) {#padrão-2--release-checklist-deploy-gate}

**Goal:** a pre-release checklist aligned with chapter 11 (Secure Deployment) + active concerns.

```
1. get_sbd_toe_chapter_brief("11-deploy-seguro")
   ↳ objective, role, phases, artifacts e artifacts_basis do capítulo 11

2. consult_security_requirements(risk_level, ["distribution", "integrity"])
   ↳ requisitos + controlos cross-chapter relevantes ao deploy
     (ids reais CTRL-<domain>-<slug>-<hash>)

3. Artefactos de deploy: o campo artifacts do passo 1
   ↳ (resolve_entities com filters.chapter não serve: chapter não é campo
      de artifact e a resposta declara unknown_filter_fields)

4. → consolidar como checklist
```

**Output:** `CHECKLIST-release-v<X>.md` with tickable gates (`[ ]`) and a reference to the `CTRL-*` / `ART-*` that each gate satisfies.

---

## Pattern 3 — Change set analysis (large PR) {#padrão-3--análise-de-change-set-pr-grande}

For PRs that touch **multiple chapters** at the same time. An expanded version of the [PR audit](./casos-uso/auditoria-pr).

```
1. map_sbd_toe_review_scope(changed_files)
   ↳ bundles N a rever

2. Para cada bundle:
   a. get_sbd_toe_chapter_brief(chapter_id)        # contexto
   b. consult_security_requirements(risk_level, concerns_inferred)
   c. Examinar hunks relevantes do PR

3. consolidar findings agrupados por chapter
```

**When to split the PR instead of auditing it whole:**

- If `map_sbd_toe_review_scope` returns > 3 bundles + thematically distinct areas → suggest a *PR split* to the author before auditing.

---

## Pattern 4 — Findings sweep (periodic audit) {#padrão-4--sweep-de-findings-auditoria-periódica}

**Goal:** a periodic audit of the whole repo — not just of the PR, but of the current state.

```
1. plan_sbd_toe_repo_governance()
   ↳ artefactos requeridos

2. Verificar quais existem no repo (Glob / Read)

3. Para artefactos em falta:
   a. get_sbd_toe_chapter_brief(chapter_id) — para conhecer o conteúdo esperado
   b. flag como gap

4. Para artefactos existentes mas desactualizados:
   a. Verificar last-updated vs version do MCP
   b. flag para revisão

5. Para CTRL-* críticos (L3 / regulado):
   a. consult_security_requirements(risk_level, all_concerns)
   b. Procurar evidência no repo (logs/, tests/, attestations/)
   c. flag não-cobertos
```

**Output:** a dashboard with 3 columns:

| Status | Meaning |
|---|---|
| ✅ **Covered** | Artefact/control with evidence |
| ⚠️ **At risk** | Artefact exists, but outdated/incomplete |
| ❌ **Gap** | Does not exist / evidence missing |

---

## Pattern 5 — Codegen iteration with failures {#padrao-5}

When `prepare_sbd_toe_codegen_context` returns `needs_decomposition` repeatedly.

If the cause is the selection going beyond what the `detail` level promises to fit, the response already carries the decomposition: the executable batches of `requirement_ceiling.batches` (`categories` + the preserved activators), whose union is the whole selection (batches may share requirements). Follow those batches, one at a time — do not redesign the decomposition by hand. The pattern below applies to the remaining cases:

```
1. Primeira chamada com a task original
   → needs_decomposition

2. Tomar uma das sub-tarefas (ou um dos lotes) sugeridas (apenas UMA)
   2.a. Re-chamar com a sub-task isolada
   2.b. Se ready_for_codegen → gerar
   2.c. Se needs_clarification → dialogar com utilizador
   2.d. Se needs_decomposition de novo → STOP, escalar com o utilizador
       (sinal de que o conceito-mãe precisa de reformulação prévia)

3. NUNCA re-chamar com o mesmo payload após needs_*
```

**Anti-pattern:** *brute force* — calling again with cosmetic tweaks to avoid the gate. The gate is by design.

---

## Pattern 6 — Normative cross-check against regulatory frameworks (via MCP or the web manual) {#padrão-6--cross-check-normativo-via-mcp-ou-manual-web}

For questions that involve EU regulations:

```
1. Identificar a obrigação no regulamento (EUR-Lex)

2. Verificar se o framework está indexado no MCP:
   inspect_sbd_toe_retrieval({question: "<framework>", topK: 5})

   Indexados:      os cross-checks publicados no snapshot servido
                   (CRA, DORA, NIS2, GDPR, AI Act, ENISA-CSA)
   Fora do índice: só conteúdo posterior ao snapshot (ver sbd://toe/version)

3. Se indexado:
   get_sbd_toe_playbook — playbook do diploma (no_cross_check → não improvisar)
   search_sbd_toe_manual({question: "<artigo + tópico>"})

   Se NÃO indexado (conteúdo posterior ao snapshot):
   consultar /sbd-toe/cross-check-normativo/<framework>/ no manual web

4. Validar cada CTRL-* referido via MCP (resolução por id exato):
   query_sbd_toe_entities({query: "<CTRL-id exato>"})

5. Estruturar relatório com 4 rótulos epistémicos
   (ver disciplina-epistemica)
```

The full detail of the normative check is in [Use case — Normative cross-check](./casos-uso/cross-check-conformidade).

---

## Pattern 7 — Role discovery for a phase {#padrão-7--discovery-de-roles-para-uma-fase}

**Goal:** "Who does what in phase X?" — useful for *retrospectives*, RACI, RACI mapping per feature.

```
1. get_guide_by_role(risk_level)                    # contagens
   ↳ role_summary{} + phase_summary{}

2. Para cada role com > 0 atribuições na fase X:
   get_guide_by_role(risk_level, role, phase=X)
   ↳ assignments[]

3. Agrupar por practice_id — mostrar overlapping (mais de 1 role para a mesma practice)
```

**Output:** a role × practice matrix for phase X.

---

## When to use `inspect_sbd_toe_retrieval` {#quando-usar-inspect_sbd_toe_retrieval}

Diagnosis for queries that return unexpected results:

- `search_sbd_toe_manual` returns *off-topic* results
- `consult_security_requirements` has an incomplete `rule_trace`
- `get_threat_landscape` returns `threats: []` when the opposite was expected

```
inspect_sbd_toe_retrieval({question: "<pergunta original>"})
```

Returns the ranking, *scores*, the complete `rule_trace`. Useful to understand whether the problem is:
- *Vocabulary mismatch* (`auth` instead of `authentication`) → adjust
- Wrong *risk level* → re-classify
- *Content lag* (see [troubleshooting](./10-troubleshooting-faq.md#content-lag)) → consult the web manual

## Next steps {#a-seguir}

- [Epistemic discipline and anti-patterns](./09-epistemica-anti-patterns.md) — what **not** to do with the outputs.
- [Use cases](./casos-uso/) — for more focused versions of these patterns.
