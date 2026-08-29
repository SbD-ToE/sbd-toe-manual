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

### `answer_sbd_toe_manual`

Q&A em linguagem natural — recupera contexto do manual e pede a síntese da resposta ao modelo do cliente via *MCP sampling*.

**Parâmetros:** `question` (string); `topK`, `useVectorRecall`, `debug` (opcionais)

:::info Degradação honesta sem *sampling*
Em clientes **sem suporte de MCP sampling** (ex.: Claude Code), a tool **não inventa** uma síntese: devolve o retrieval formatado com a nota *"MCP sampling not available… use `search_sbd_toe_manual` directly"* e encaminha para `search_sbd_toe_manual`. Nesses clientes, preferir `search_sbd_toe_manual` desde o início.
:::

---

### `consult_security_requirements`

**Determinístico**. Devolve o conjunto de requisitos + controlos activos para um *risk level*, opcionalmente filtrado por *concerns*.

**Parâmetros:**
- `risk_level` (`L1` | `L2` | `L3`) — obrigatório
- `concerns` (string[]) — opcional, valores do **enum fechado** abaixo

**Enum de `concerns` (fechado — 13 valores exatos):**
`auth` · `logging` · `validation` · `api` · `config` · `integrity` · `distribution` · `ide` · `requirements` · `architecture` · `iac` · `encryption` · `agents`.

Valores fora deste enum **não resolvem** (não há *fuzzy match*): usar `logging` para monitorização, `distribution` para *supply-chain* / terceiros, `agents` para os requisitos de agentes AI (`REQ-AGN-001…004`).

**Output:** (formatos de id reais — requisitos `<CAT>-NNN`, controlos `CTRL-<domain>-<slug>-<hash>`)
```json
{
  "requirements": [{"requirement_id": "AUT-001", "name": "MFA obrigatório", "category": "AUT", "type": "base"}],
  "controls": [{
    "control_id": "CTRL-identity-gestao-de-identidades-acessos-e-ownership-d0919c69af",
    "name": "Gestão de identidades, acessos e ownership",
    "domain": "identity", "control_type": "preventive",
    "chapter_ids": ["08-iac-infraestrutura", "14-governanca-contratacao"],
    "_confidence": "direct"
  }],
  "active_domains": ["identity", "governance", "infrastructure"],
  "active_categories": ["ACC", "ARC", "AUT", "SES"],
  "rule_trace": [
    "REQUIREMENT_APPLIES_BY_RISK(risk_level=L2): 39 requirements active",
    "CONCERNS_FILTER_REQUIREMENTS(concerns=[auth])"
  ],
  "coverage_gaps": {
    "requirements_without_control_link": {"count": 0, "requirement_ids": [], "note": "…"}
  }
}
```

`coverage_gaps.requirements_without_control_link` é **sempre devolvido** (hoje `count: 0` em L1, L2 e L3): declara os requisitos activos sem entrada em `requirement_control_links` — uma lacuna declarada, não uma ausência de obrigação (o requisito é servido; os controlos são, no máximo, derivados por domínio, `_confidence: "derived"`).

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

Resolve uma entidade por **id exato** ou, se o token não for um id, faz *fallback* para busca semântica.

**Parâmetros:** `query` (string, obrigatório); `entityType`, `chapterId`, `riskLevel`, `topK` (opcionais)

**Exemplo (id exato):**

```json
query_sbd_toe_entities({"query": "AUT-001"})
```
```json
{
  "entities": [{
    "entity_type": "requirement", "requirement_id": "AUT-001",
    "category": "AUT", "name": "MFA obrigatório",
    "applicable_levels": {"L1": false, "L2": true, "L3": true},
    "source_bundle": "02-requisitos-seguranca"
  }],
  "total": 1, "match": "exact_id"
}
```

:::warning Erro de categoria comum
Um token como `"CTRL-06"` **não é um id** — não existe a forma `CTRL-<capítulo>-<número>`. Passá-lo **não** devolve "os controlos do capítulo 06"; cai em *fallback* semântico (`match` ≠ `"exact_id"`). Os ids reais são `AUT-001`, `LOG-003` (requisitos), `CTRL-<domain>-<slug>-<hash>` (controlos), `MT-NNN` (ameaças), `ART-…` (artefactos). Para **filtrar por tipo/domínio** (em vez de resolver um id), usar `resolve_entities`.
:::

**`citation_note` e `declared_gap`.** A gramática de IDs de requisito é *fullmatch* — `^(?:REQ-[A-Z]{3}-\d{3}|[A-Z]{3}-\d{3})$`; identificadores `EX-…` são ilustrativos e nunca resolvem. Um `REQ-NNN` que o manual cita como exemplo mas não existe no catálogo (ex.: `REQ-010`, num exemplo do Cap. 02) devolve `entities` por *fallback* semântico **e** uma `citation_note` com `status: "informative"` e `cited_in` (onde é citado) — informativo, não é *gap*, e nunca é resolvido por aproximação a outro requisito. Citações legadas com a forma `REQ-<CAT>-NNN` devolvem `declared_gap`; hoje não existem no manual e o campo não aparece.

```json
query_sbd_toe_entities({"query": "REQ-010"})
// → "citation_note": {
//      "requirement_id": "REQ-010", "status": "informative",
//      "note": "`REQ-010` não é um requisito publicado: o Manual cita-o como identificador ilustrativo de exemplo ou é um token não-requisito com a forma <CAT>-NNN (CWE-, SHA-, …). Informativo, não é um gap; nunca resolvido por aproximação a outro requisito.",
//      "cited_in": {"mention_count": 2, "document_ids": ["010-sbd-manual-02-requisitos-seguranca-addon-15-exemplos-aplicacao"]}
//    }
```

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

resolve_entities({"record_type": "requirement", "filters": {"requirement_id": "REQ-010"}})
// → total: 0, com meta.note idêntica à citation_note (identificador ilustrativo; não é gap)
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

**Output:** (ameaças `MT-NNN`; cada ligação cita o `control_id` real)
```json
{
  "threats": [
    {
      "id": "MT-055", "name": "Interfaces expostas sem isolamento",
      "chapter_id": "04-arquitetura-segura", "threat_category": "STRIDE",
      "mitigation_confidence": "derived", "mitigation_strength": "parcial",
      "mitigated_by": [
        {"control_id": "CTRL-infrastructure-segmentacao-e-controlo-arquitetural-dceb3c1f0b", "domain": "infrastructure"}
      ]
    }
  ]
}
```

**Importante:**
- `mitigation_confidence: "derived"` → ligação estrutural (chapter/bundle-match), fiável; `mitigation_strength` é tipicamente `"parcial"`. (Não há valor `"heuristic"` nas ligações estruturais — se aparecer um *fallback* heurístico, rotular como inferido.)
- A tool **corre `consult` internamente** — não chamar `consult_security_requirements` antes.

:::warning Limitação de *routing* conhecida (à data desta versão)
Os *concerns* de **base** (`auth`, `validation`, `api`, …) roteiam para o **cap. 02** e devolvem as meta-ameaças de processo `MT-021..038` (ausência/ambiguidade de requisitos), **não** as ameaças técnicas do domínio. Os *concerns* de **domínio** roteiam bem: `architecture`→cap. 04 (`MT-055..072`), `iac`→cap. 08, `logging`→cap. 12. Para ameaças técnicas de auth/validação, ancorar antes nos **requisitos** (`consult_security_requirements`) e cruzar. *(Fix em curso no servidor — verificar o comportamento ao vivo.)*
:::

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

Gera conteúdo de configuração para o cliente. **Sem `role`** devolve o *agent guide* canónico (`sbd://toe/agent-guide`); **com `role`** devolve uma *skill* ou *subagent* especializado no *slice* desse papel.

**Parâmetros:**
- `role` (opcional) — uma das **13 personas canónicas** (aliases resolvem; papel desconhecido → erro com a lista das 13).
- `format` (`skill` | `subagent`) — `skill` = ficheiro de orientação (`.claude/skills/…`); `subagent` = definição de agente instalável (`.claude/agents/…`).
- `flavour` (`harnessed` | `skilled`) — `harnessed` (default) embebe as tools `mcp__sbd-toe__*` (consulta o manual ao vivo); `skilled` embebe o *slice* congelado, **sem** tools live (offline).
- `risk_level` (default `L2`), `phase`, `include_detail`, `clientType` — opcionais.

**Output:** `content` (markdown) + `suggested_path` + `meta.coverage{chapters, of_total_chapters, assignments, user_stories, checklist_items}` — a cobertura é **declarada** ("nothing silently truncated").

Resources paralelos: `sbd://toe/skill/{role}` e `sbd://toe/subagent/{role}` devolvem o mesmo conteúdo.

Ver [Skills e agentes](./04-skills-agentes.md).

---

### `setup_sbd_toe_agent` (prompt)

Tecnicamente um *prompt*, não uma *tool* — mas funciona como inicializador da sessão.

**Parâmetros:** `riskLevel`, `projectRole`

**Output:** capítulos activos + regras específicas.

---

## Implementation view (V5)

Estas tools respondem a **"como pôr de pé e governar o SbD"** — distinta da vista operacional ("o que fazer em cada fase do SDLC"). Todas são *coverage-preserving* (paginação com `coverage.hasMore`/`nextOffset`; nada truncado em silêncio) e devolvem uma banda `next` com os próximos passos sugeridos.

### `get_sbd_toe_chapter_implementation_checklist`

A narrativa de implementação canon/20 de um capítulo (o "como implementar"), distinta do DoD estruturado de *user story* (esse está em `get_guide_by_role(include_detail=true)`).

**Parâmetros:** `chapter` (id ou número), `risk_level?`, `limit?`, `offset?`
**Output:** `data.items[]` (prosa com `chunk_id` rastreável) + `next`.

### `get_sbd_toe_operating_model`

RACI, *decision-rights*, cadências de governança e modelos de organização, promovidos do *rollout playbook*.

**Parâmetros:** `orgScope?`, `limit?`, `offset?`
**Output:** `data.sections[]` (prosa, paginado). Declara a fronteira: **não prescreve organigrama** (varia por setor/dimensão).

### `plan_sbd_toe_rollout`

Roadmap por fases — as fases canónicas do ciclo de vida mapeadas a capítulos.

**Parâmetros:** `orgProfile?`, `horizon?`, `limit?`, `offset?`
**Output:** `data.phases[]` (`order`, `phase_id`, `label`, `chapter`), `model: "phase-ordered-mvp"`. O DAG de dependências é **deferido** (declarado, não fingido).

### `get_sbd_toe_verification_matrix`

O lado **EXPECTED** da verificação: por requisito/controlo, o método de validação + evidência esperada + referência a *EvidencePattern*. Complemento determinístico do auditor e do plano de testes.

**Parâmetros:** `risk_level` (obrigatório), `limit?`, `offset?`
**Output:** `data.rows[]` (`evidence_pattern_id` `EP-*`, `requirement_id`, `control_id`, `validation_method`, `expected_evidence`, `evidence_type`, `expected_artifact_type_ids[]`, `source`) + `coverage_gaps` (requisitos sem padrão — declarados).

### `assess_sbd_toe_implementation`

Auto-relato de postura: compara valores de KPI submetidos contra os *thresholds* por nível.

**Parâmetros:** `kpi_values` (mapa `metric_id`→número), `risk_level`
**Output:** `posture` (`below`/`at`/`above`) + `totals{applicable, meets, gaps, not_reported}` + `per_kpi` + `unknown_metrics`. **Stateless** (nada é guardado); um KPI aplicável sem valor é `not_reported`, **nunca** *pass*.

:::note Payload
Devolve os KPIs aplicáveis **todos** (sem paginação) — em L2 são ~92, o que torna o output grande. Submeter os `kpi_values` que se tem; os em falta vêm marcados `not_reported`.
:::

### `map_sbd_toe_regulatory_activation`

Lente regulatória (o inverso da *provenance*): dado um *framework*, que áreas/capítulos do manual ele activa.

**Parâmetros:** `framework` (`DORA` | `NIS2` | `CRA` | `RGPD`; ou `EXT-DORA`…), `limit?`, `offset?`
**Output:** `data.activated[]` por capítulo (`mapping_count`, `obligation_count`, `by_target_type`, `example_citation`) + `totals`. *Framework* desconhecido → erro `-32602`. Provenance declara: **cross-check ≠ atestação de conformidade**.

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
