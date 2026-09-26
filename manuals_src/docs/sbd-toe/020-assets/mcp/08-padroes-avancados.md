---
id: padroes-avancados
title: Padrões avançados
description: Sequências multi-tool para problemas complexos — security plan, checklist por release, análise de change set, sweep de findings.
sidebar_label: Padrões avançados
sidebar_position: 8
tags:
  - mcp
  - padroes
  - workflows
---

# Padrões avançados

Com o uso do MCP em projectos reais, torna-se evidente que algumas tarefas precisam de várias chamadas encadeadas para dar uma resposta defensável — um *security plan* não nasce de uma só *tool*, nem uma auditoria periódica. Esta secção junta esses encadeamentos como **padrões** com nome e propósito, para evitar redescobri-los cada vez.

Todos combinam o mesmo *toolkit*: as determinísticas (`select_sbd_toe_requirements`, `consult_security_requirements`, `get_threat_landscape`, `get_guide_by_role`, `prepare_sbd_toe_codegen_context`) onde são precisas respostas estáveis e citáveis; as de pesquisa (`search_sbd_toe_manual`, `query_sbd_toe_entities`) quando o que falta é descobrir o que existe no manual.

## A banda `next` — encadeamento sugerido {#a-banda-next--encadeamento-sugerido}

Muitas tools devolvem, além do `data` determinístico, uma banda **`next`** (até 3 afordances, *structural* + *semantic*): o passo seguinte sugerido para encadear, já com a *tool* e os argumentos. É o fio que liga os padrões abaixo — em vez de adivinhar o próximo passo, seguir o `next` da resposta anterior. As tools paginadas trazem ainda `coverage.hasMore` / `nextOffset` para continuar sem truncar.

---

## Padrão de entrada — que requisitos se aplicam a esta tarefa {#padrão-de-entrada--que-requisitos-se-aplicam-a-esta-tarefa}

**Objetivo:** partir de uma tarefa concreta e chegar aos requisitos que a cobrem, ao contexto para a implementar e à prova esperada — sem que o servidor adivinhe o que não foi declarado.

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

**Output:** para cada requisito selecionado, o id citável, o que a implementação tem de garantir e a evidência que o *reviewer* deve encontrar.

---

## Padrão 1 — Security plan de uma feature {#padrão-1--security-plan-de-uma-feature}

**Objetivo:** documento de plano de segurança para uma feature nova, antes do desenvolvimento.

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

**Estrutura do output:**

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

## Padrão 2 — Release checklist (deploy gate) {#padrão-2--release-checklist-deploy-gate}

**Objetivo:** checklist de pré-release alinhado com o capítulo 11 (Deploy Seguro) + concerns activos.

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

**Output:** `CHECKLIST-release-v<X>.md` com gates marcáveis (`[ ]`) e referência aos `CTRL-*` / `ART-*` que cada gate satisfaz.

---

## Padrão 3 — Análise de change set (PR grande) {#padrão-3--análise-de-change-set-pr-grande}

Para PRs que tocam **múltiplos capítulos** simultaneamente. Versão expandida da [auditoria de PR](./casos-uso/auditoria-pr).

```
1. map_sbd_toe_review_scope(changed_files)
   ↳ bundles N a rever

2. Para cada bundle:
   a. get_sbd_toe_chapter_brief(chapter_id)        # contexto
   b. consult_security_requirements(risk_level, concerns_inferred)
   c. Examinar hunks relevantes do PR

3. consolidar findings agrupados por chapter
```

**Quando dividir o PR em vez de auditar inteiro:**

- Se `map_sbd_toe_review_scope` devolver > 3 bundles + áreas tematicamente distintas → sugerir *PR split* ao autor antes de auditar.

---

## Padrão 4 — Sweep de findings (auditoria periódica) {#padrão-4--sweep-de-findings-auditoria-periódica}

**Objetivo:** auditoria periódica do repo inteiro — não só do PR, mas do estado actual.

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

**Output:** dashboard com 3 colunas:

| Estado | Significado |
|---|---|
| ✅ **Coberto** | Artefacto/control com evidência |
| ⚠️ **Em risco** | Artefacto existe, mas desactualizado/incompleto |
| ❌ **Gap** | Não existe / evidência ausente |

---

## Padrão 5 — Iteração de codegen com falhas {#padrao-5}

Quando `prepare_sbd_toe_codegen_context` devolve `needs_decomposition` repetidamente.

Se a causa é a seleção ter ultrapassado o tecto do nível de `detail`, a resposta já traz a decomposição: os lotes executáveis de `requirement_ceiling.batches` (`categories` + os ativadores preservados), cuja união é a seleção inteira. Seguir esses lotes, um de cada vez — não redesenhar a decomposição à mão. O padrão abaixo aplica-se ao resto dos casos:

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

**Anti-pattern:** *brute-force* — re-chamar com tweaks cosméticos para evitar o gate. O gate é por design.

---

## Padrão 6 — Cross-check normativo (via MCP ou manual web) {#padrão-6--cross-check-normativo-via-mcp-ou-manual-web}

Para perguntas que envolvem regulamentos UE:

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

Detalhe completo em [Caso de uso — Cross-check normativo](./casos-uso/cross-check-conformidade).

---

## Padrão 7 — Discovery de roles para uma fase {#padrão-7--discovery-de-roles-para-uma-fase}

**Objetivo:** "Quem faz o quê na fase X?" — útil para *retrospectives*, RACI, mapeamento RACI por feature.

```
1. get_guide_by_role(risk_level)                    # contagens
   ↳ role_summary{} + phase_summary{}

2. Para cada role com > 0 atribuições na fase X:
   get_guide_by_role(risk_level, role, phase=X)
   ↳ assignments[]

3. Agrupar por practice_id — mostrar overlapping (mais de 1 role para a mesma practice)
```

**Output:** matriz role × practice para a fase X.

---

## Quando usar `inspect_sbd_toe_retrieval` {#quando-usar-inspect_sbd_toe_retrieval}

Diagnóstico para queries que devolvem resultados inesperados:

- `search_sbd_toe_manual` devolve resultados *off-topic*
- `consult_security_requirements` tem `rule_trace` incompleto
- `get_threat_landscape` devolve `threats: []` quando esperavas o contrário

```
inspect_sbd_toe_retrieval({question: "<pergunta original>"})
```

Devolve ranking, *scores*, `rule_trace` completo. Útil para perceber se o problema é:
- *Vocabulary mismatch* (`auth` em vez de `authentication`) → ajustar
- *Risk level* errado → re-classificar
- *Content lag* (ver [troubleshooting](./10-troubleshooting-faq.md#content-lag)) → consultar manual web

## A seguir {#a-seguir}

- [Disciplina epistémica e anti-patterns](./09-epistemica-anti-patterns.md) — o que **não** fazer com os outputs.
- [Casos de uso](./casos-uso/) — para versões mais focadas destes padrões.
