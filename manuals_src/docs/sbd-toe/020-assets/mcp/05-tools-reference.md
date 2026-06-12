---
id: tools-reference
title: Tools — referência completa
description: Cada tool do SbD-ToE MCP — parâmetros, semântica determinística vs heurística, exemplos input/output, e quando preferir uma sobre outra.
sidebar_label: Tools reference
sidebar_position: 5
tags:
  - mcp
  - tools
  - referencia
---

# Tools — referência completa

As tools dividem-se em **três modos** (CONSULT / GUIDE / SETUP) com **semântica diferente**:

- **Determinísticas**: dado o mesmo input, devolvem o mesmo output. Use para grounding citável (`consult_security_requirements`, `get_guide_by_role`, `get_threat_landscape`, `prepare_sbd_toe_codegen_context`).
- **Heurísticas / busca**: ranking textual sobre o manual. Use para narrativa/conceito (`search_sbd_toe_manual`).

Cada tool abaixo lista parâmetros, *output* esperado, e padrão recomendado.

---

## CONSULT mode

### `search_sbd_toe_manual`

Pesquisa narrativa com citações — quando o utilizador faz perguntas conceptuais ("o que é threat modeling?", "como funciona SBOM").

**Parâmetros:** `query` (string)

**Output:** lista de excertos com `chapter_id`, `section`, `score`, `text`.

**Quando preferir:** perguntas abertas / explicativas.
**Quando NÃO usar:** quando há filtros estruturados (risk_level, concern, role) — preferir `consult_security_requirements`.

---

### `consult_security_requirements`

**Determinístico**. Devolve o conjunto de requisitos + controlos activos para um *risk level*, opcionalmente filtrado por *concerns*.

**Parâmetros:**
- `risk_level` (`L1` | `L2` | `L3`) — obrigatório
- `concerns` (string[]) — opcional, *lowercase* da tabela de vocabulário

**Output:**
```json
{
  "requirements": [{"id": "REQ-...", "category": "AUT", "text": "..."}],
  "controls": [{"id": "CTRL-04-1", "domain": "architecture", "description": "..."}],
  "active_domains": ["architecture", "development", ...],
  "active_categories": ["AUT", "ACC", ...],
  "rule_trace": ["L2_RULESET_LOADED", "CONCERNS_FILTER_REQUIREMENTS", ...]
}
```

**Tamanhos típicos:** L1 ≈ 22k chars · L2 ≈ 36k chars · L3 ≈ 36k chars.
**Regra prática:** **sempre** passar `concerns` em L2/L3 (reduz para ~9k por *concern set*).

#### Exemplo

```json
consult_security_requirements({"risk_level": "L2", "concerns": ["auth", "logging"]})
```

Devolve apenas requisitos das categorias **AUT/ACC/SES** (auth) + **LOG** (logging), com `rule_trace` a confirmar `CONCERNS_FILTER_REQUIREMENTS`.

---

### `map_sbd_toe_applicability`

Que capítulos / controlos se aplicam ao projecto dado o seu perfil.

**Parâmetros:** atributos do projecto (exposição, dados, *stack*, regulação aplicável).

**Output:** capítulos activos/condicionais/excluídos + *rationale*.

**Quando preferir:** decidir *risk level* ou perfilar um projecto novo.

---

### `get_sbd_toe_chapter_brief`

Resumo estruturado de um capítulo — fases, artefactos (`ART-*`), tópicos.

**Parâmetros:** `chapter_id` (ex.: `06-desenvolvimento-seguro`)

**Output:** `phases`, `artifact_ids[]`, `topics[]`, `controls[]`.

---

### `list_sbd_toe_chapters`

Índice — `chapter_id`, `title`, `min_level`, `domains`.

**Parâmetros:** `risk_level` (opcional — filtra)

---

### `query_sbd_toe_entities`

Procura controlos, artefactos, práticas por padrão textual ou prefixo.

**Parâmetros:** `query` (string), `entity_type` (`control` | `artifact` | `practice`)

**Exemplo:**

```json
query_sbd_toe_entities({"query": "CTRL-06", "entity_type": "control"})
```

Devolve todos os controlos do capítulo 06.

---

### `resolve_entities`

Filtro de baixo nível sobre a ontologia — *dot-notation* nos `filters`.

**Parâmetros:** `record_type` (`control` | `requirement` | `role` | `practice`), `filters` (objecto *dot-path*), `limit` (opcional)

**Exemplos:**

```json
resolve_entities({"record_type": "role"})
// → lista os 13 roles canónicos

resolve_entities({"record_type": "control", "filters": {"domain": "architecture"}})
// → controlos do domínio architecture
```

---

## GUIDE mode

### `get_guide_by_role`

**Determinístico**. Práticas atribuídas por *role* e/ou fase do SDLC.

**Parâmetros:**
- `risk_level` (`L1` | `L2` | `L3`) — obrigatório
- `role` (string) — opcional
- `phase` (string) — opcional (`requirements` | `design` | `implement` | `test` | `deploy` | `operate` | `governance`)

**Output sem `role`/`phase`:** `role_summary{}` + `phase_summary{}` (contagens) — útil para discovery.
**Output com `role` ou `phase`:** `assignments[]` + *user stories*.

**Regra crítica:** **sempre passar `role` ou `phase`** para obter detalhes — sem nenhum dos dois, devolve só contagens.

---

### `get_threat_landscape`

**Determinístico**. *Threats* relevantes para um *risk level* / *concern*, com mitigações.

**Parâmetros:**
- `risk_level` (`L1` | `L2` | `L3`) — obrigatório
- `concerns` (string[]) — opcional

**Output:**
```json
{
  "threats": [
    {
      "id": "THR-...",
      "description": "...",
      "mitigated_by": ["CTRL-04-1", "CTRL-06-3"],
      "mitigation_confidence": "derived" | "heuristic"
    }
  ]
}
```

**Importante:**
- `mitigation_confidence: "derived"` → ligação estrutural (chapter-match), fiável.
- `mitigation_confidence: "heuristic"` → ligação inferida, **rotular como tal** na resposta ao utilizador.
- A tool **corre `consult` internamente** — não chamar `consult_security_requirements` antes.

---

### `plan_sbd_toe_repo_governance`

Lista os artefactos que o manual identifica para um repositório, agrupados por capítulo.

**Output:** lista de `artifact_id` + `chapter_id` + `description`.

**Padrão:** *bootstrap* de governança num repo novo — gerar a partir da lista artefactos por capítulo, criar os ficheiros vazios + READMEs.

---

### `map_sbd_toe_review_scope`

Dado um conjunto de ficheiros alterados, devolve que **bundles do manual** rever.

**Parâmetros:** `changed_files` (string[])

**Output:** capítulos / bundles a rever + *rationale* (ex.: "ficheiros sob `iac/` → cap. 08").

**Padrão:** *PR auditor*. Combinar com `consult_security_requirements` para enumerar controlos por capítulo.

---

### `prepare_sbd_toe_codegen_context`

A tool **mais sofisticada** — devolve contexto determinístico para *codegen*, *review* ou *test-plan*.

**Parâmetros:**
- `task` (string) — obrigatório
- `risk_level`, `mode` (`codegen` | `review` | `test-plan`), `stack`, `exposure`, `data_sensitivity`, `concerns`, `changed_files`, `regulatory_frameworks`, `include_regulatory_overlay` — opcionais (passar tudo que se sabe)

**Output (campo `status`):**

| `status` | Significado | Acção |
|---|---|---|
| `ready_for_codegen` | Scope claro, contexto pronto | Proceder — preencher `security_rationale` |
| `needs_clarification` | Inputs ambíguos | **STOP** — perguntar ao utilizador, não gerar código |
| `needs_decomposition` | Scope demasiado largo | **STOP** — propor 2–4 sub-tarefas |
| `unsupported_scope` | Capacidade ausente no servidor | **STOP** — reportar verbatim |

**Disciplina obrigatória após `ready_for_codegen`:**

- O `citation_map` devolvido é o **mundo fechado** de IDs válidos — não inventar IDs.
- Preencher `security_rationale.decisions[].cited_ids` com pelo menos 1 ID por decisão não-trivial.
- Preencher `security_rationale.validations[]` (validações concretas implementadas).
- Preencher `security_rationale.expected_evidence[]` (artefactos para o reviewer — código sozinho **não** é evidência).
- Preencher `security_rationale.residual_risk` (o que não foi endereçado).
- Sinalizar `completeness_report.m_recall < 1.0` ao utilizador (cobertura parcial).

Ver guia detalhado em [Caso de uso — codegen grounded](./casos-uso/codegen-grounded) e no resource [`sbd://toe/grounded-codegen-guide`](./06-resources-prompts.md#sbdtoegrounded-codegen-guide).

---

## SETUP mode

### `generate_sbd_toe_skill`

Devolve conteúdo canónico da *skill* para guardar no cliente. Sem parâmetros.

**Output:** Markdown completo do *agent guide*, com cabeçalho identificador.

Ver [Skills e agentes](./04-skills-agentes.md).

---

### `setup_sbd_toe_agent` (prompt)

Tecnicamente um *prompt*, não uma *tool* — mas funciona como inicializador da sessão.

**Parâmetros:** `riskLevel`, `projectRole`

**Output:** capítulos activos + regras específicas.

---

## Diagnóstico

### `inspect_sbd_toe_retrieval`

Diagnóstico do retriever — útil quando uma query devolve resultados inesperados. Mostra ranking, scores, e *rule_trace* completo.

---

## Combinatória — padrões recomendados

### Pergunta estruturada

```
consult_security_requirements(L2, ["auth"])
```

### Pergunta narrativa

```
search_sbd_toe_manual("threat modeling stride")
```

### Resposta complexa (threat model / security plan)

```
1. consult_security_requirements(L2, concerns)   # requisitos + controlos
2. get_threat_landscape(L2, concerns)             # threats relevantes
3. get_guide_by_role(L2, role)                    # práticas do role
4. → gerar documento citando IDs dos 3 passos
```

### PR review

```
1. map_sbd_toe_review_scope(changed_files)        # que capítulos
2. consult_security_requirements(risk_level, concerns)  # controlos activos
3. → enumerar findings citando CTRL-* + chapter_id
```

### Codegen grounded

```
1. prepare_sbd_toe_codegen_context(task, mode="codegen", ...)
2. ramificar por status (ver tabela acima)
3. se ready_for_codegen → gerar código + tests + security_rationale
```

## A seguir

[Resources e prompts](./06-resources-prompts.md) — URIs `sbd://toe/*` para *grounding* estrutural e prompts pré-empacotados.
