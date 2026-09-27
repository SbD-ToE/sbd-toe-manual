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

As tools organizam-se por leitura — CONSULT, GUIDE, SETUP, IMPL (vista de implementação), NORMATIVA e PROGRAMA — e têm **semântica diferente**:

- **Determinísticas**: dado o mesmo input, devolvem o mesmo output. Use para grounding citável (`select_sbd_toe_requirements`, `consult_security_requirements`, `get_guide_by_role`, `get_threat_landscape`, `prepare_sbd_toe_codegen_context`).
- **Heurísticas / busca**: ranking textual sobre o manual. Use para narrativa/conceito (`search_sbd_toe_manual`).

Cada tool abaixo lista parâmetros, *output* esperado, e padrão recomendado. A lista completa da versão instalada, com as descrições servidas, é a que `tools/list` devolve.

---

## Porta de entrada — o contrato declarativo {#porta-de-entrada--o-contrato-declarativo}

### `select_sbd_toe_requirements` {#select_sbd_toe_requirements}

**Determinístico e reproduzível.** É a tool que as descrições servidas marcam como *START HERE*: para uma tarefa concreta, seleciona os requisitos aplicáveis a partir do que o agente **declara** — não a partir do que o servidor adivinha.

**O contrato:**

- O agente declara o que leu: `risk_level`, `concerns`, `exposure`, `data_sensitivity`, `technologies`, `changed_files`. Os valores aceites estão em [`sbd://toe/activation-vocabulary`](./06-resources-prompts.md), com o que cada um ativa.
- `changed_files` ativa capítulos pela tabela publicada — é a forma direta de levar um *diff* à seleção.
- O texto da tarefa (`task`) é registado como contexto, não interpretado.
- Sem declaração, a resposta é `needs_input`: devolve o vocabulário, os candidatos a confirmar e, para declarações inertes, os `valid_values`. O agente confirma com o utilizador e volta a chamar com a declaração completa.
- `exposure` aceita quatro valores. `local` é válido e inerte, não activa nada: declarado sozinho, dá `needs_input`, nunca uma seleção vazia em silêncio. `internal` e `authenticated` activam `auth` e `logging`. `public` activa `auth`, `logging`, `api`, `validation` e `architecture`. A fonte é `sbd://toe/activation-vocabulary`.

**A resposta traz:**

- `selection`, com `selected[]`, `narrowed_out` e `excluded_by_level`. Cada entrada de `selected[]` traz `requirement_id`, `name`, `category`, `type`, `source_chapter` e `selection_trace[]`, com a camada, a fonte, o gatilho e o `basis` (`declared` ou `lexical`).
- `context`, com os capítulos e as categorias activados.
- `out_of_scope_chapters`, com o que nenhuma declaração activou, por capítulo e contagem, e o caminho para o trazer.
- `task`, registado como `recorded_context`, com `affects_selection: false`.
- `basis_summary`, `coverage` (total, página, `nextOffset`, e as contagens de `narrowed_out` e `excluded_by_level`), `denominators` (os denominadores nomeados) e `cross_surface_check` (a concordância com `consult_security_requirements` na parte comparável).
- `overlay`, `activation_trace`, `provenance` e `next`.

`selected` é paginado por ordem de id, não por relevância: para chegar a uma categoria, declara-se o *concern* que a activa, ou pede-se por estrutura (`categories`). A linha de `next` que aponta para o prepare anuncia o custo como estimativa.

O `select` tem o mesmo eixo `detail` que o prepare:

- `full`, o nível por omissão, traz o `selection_trace` completo em cada item.
- `standard` move as justificações distintas para `selection_trace_legend`, e cada item referencia-as em `trace`.
- `lista` é o mesmo que `standard`, sem os campos deriváveis `type` e `source_chapter`.

**Encadeamento típico:** `select_sbd_toe_requirements` → `prepare_sbd_toe_codegen_context` (para gerar código com esses requisitos) → [`get_sbd_toe_verification_matrix(requirement_ids)`](#get_sbd_toe_verification_matrix) (a prova esperada para cada requisito selecionado).

---

## CONSULT mode {#consult-mode}

### `search_sbd_toe_manual` {#search_sbd_toe_manual}

Pesquisa narrativa com citações — quando o utilizador faz perguntas conceptuais ("o que é threat modeling?", "como funciona SBOM"). A descrição servida marca-a como **não normativa**: serve para orientar a leitura, não para fundamentar uma obrigação.

**Parâmetros:** `question` (string, obrigatório); `topK`, `useVectorRecall`, `debug` (opcionais)

**Output:** lista de excertos com `chapter_id`, `section`, `score`, `text`.

**Quando preferir:** perguntas abertas / explicativas.
**Quando NÃO usar:** quando há filtros estruturados (risk_level, concern, role) — preferir `consult_security_requirements`.

---

### `answer_sbd_toe_manual` {#answer_sbd_toe_manual}

Q&A em linguagem natural — recupera contexto do manual e pede a síntese da resposta ao modelo do cliente via *MCP sampling*.

**Parâmetros:** `question` (string); `topK`, `useVectorRecall`, `debug` (opcionais)

:::info Degradação honesta sem *sampling*
Em clientes **sem suporte de MCP sampling** (ex.: Claude Code), a tool **não inventa** uma síntese: devolve o retrieval formatado com a nota *"MCP sampling not available… use `search_sbd_toe_manual` directly"* e encaminha para `search_sbd_toe_manual`. Nesses clientes, preferir `search_sbd_toe_manual` desde o início.
:::

---

### `explain_sbd_toe_topic` {#explain_sbd_toe_topic}

Leitura CONSULT: «o que é que o manual diz sobre X», sem tarefa e sem projecto. Pergunta-se por conceito (`concern`) ou por estrutura (`category` ou `chapter`). A resposta percorre os requisitos (com `applies_at`), a orientação (práticas), a prova, as ameaças, os anti-padrões («o que NÃO fazer») e o lugar no ciclo de vida, distinguindo requisito de orientação e marcando a proveniência. `risk_level` é opcional e só anota: não filtra, e a resposta é a mesma sem ele. É paginada sobre os requisitos.

---

### `consult_security_requirements` {#consult_security_requirements}

**Determinístico**. Devolve o conjunto de requisitos + controlos activos para um *risk level*, opcionalmente filtrado por *concerns*. É o catálogo do nível; para a seleção que serve uma tarefa concreta, a porta de entrada é [`select_sbd_toe_requirements`](#select_sbd_toe_requirements).

**Parâmetros:**
- `risk_level` (`L1` | `L2` | `L3`) — obrigatório
- `concerns` (string[]) — opcional, valores do **vocabulário fechado** abaixo
- `exposure`, `data_sensitivity` — opcionais (`exposure`: `local`, `internal`, `authenticated` ou `public` — ver [`select_sbd_toe_requirements`](#select_sbd_toe_requirements))
- `mode` (`full` | `index`) — opcional

**Vocabulário de `concerns` (fechado):** os valores aceites, e o que cada um ativa, estão publicados em `sbd://toe/activation-vocabulary` — é aí que se confirmam, em vez de numa lista copiada.

Valores fora do vocabulário são **declarados, não aproximados** (não há *fuzzy match*): usar `logging` para monitorização, `distribution` para *supply-chain* / terceiros, `agents` para os requisitos de agentes AI (`REQ-AGN-001…004`).

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

`coverage_gaps.requirements_without_control_link` é **sempre devolvido**. Com o conhecimento servido actual, `count` é 0 nos três níveis. Se aparecer um requisito sem ligação a controlos, é listado aqui como lacuna declarada, não como ausência de obrigação (o requisito é servido; os controlos são, no máximo, derivados por domínio, `_confidence: "derived"`).

**Tamanho:** a resposta completa de L2/L3 pode exceder o contexto do cliente. O guia (`sbd://toe/agent-guide`) publica os tamanhos medidos na *build* servida, e cada resposta declara o seu em `size_estimate`.
**Regra prática:** **sempre** passar `concerns` em L2/L3 — a resposta fica muito mais pequena.

#### Exemplo {#exemplo}

```json
consult_security_requirements({"risk_level": "L2", "concerns": ["auth", "logging"]})
```

Devolve apenas requisitos das categorias **AUT/ACC/SES** (auth) + **LOG** (logging), com `rule_trace` a confirmar `CONCERNS_FILTER_REQUIREMENTS`.

---

### `map_sbd_toe_applicability` {#map_sbd_toe_applicability}

A exigência de cada capítulo para um *risk level* e o perfil do projeto. A aplicabilidade é graduada: todos os capítulos se aplicam a todos os níveis, e o que muda é a exigência.

**Parâmetros:** `riskLevel` (obrigatório); `technologies`, `hasPersonalData`, `isPublicFacing`, `projectRole` (opcionais).

**Output:** `chapters` (com a exigência por capítulo), `conditional`, `activatedBundles`.

**Quando preferir:** perfilar um projeto novo e comparar o efeito de cada nível. A tool não decide o *risk level* — exige-o; a decisão segue o método do cap. 01.

---

### `get_sbd_toe_chapter_brief` {#get_sbd_toe_chapter_brief}

Resumo estruturado de um capítulo — objetivo, papel, fases, artefactos (`ART-*`).

**Parâmetros:** `chapterId` (ex.: `06-desenvolvimento-seguro`)

**Output:** `id`, `found`, `title`, `objective`, `role`, `phases`, `artifacts`, `artifacts_basis`.

---

### `list_sbd_toe_chapters` {#list_sbd_toe_chapters}

Índice — `id`, `title`, `readableTitle`, `applicability`, `demand_by_level`.

**Parâmetros:** `riskLevel` (opcional). Não exclui capítulos: todos aparecem, com a exigência por nível.

---

### `query_sbd_toe_entities` {#query_sbd_toe_entities}

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

### `resolve_entities` {#resolve_entities}

Filtro de baixo nível sobre a ontologia — *dot-notation* nos `filters`.

**Parâmetros:** `record_type` (por exemplo `control`, `requirement`, `role`, `practice`, `threat`, `artifact`, `evidence_pattern`, os `appsec_*` do AppSec Core v1 e os `regulatory_*` do overlay — um valor desconhecido devolve a lista válida), `filters` (objecto *dot-path*), `limit` (opcional)

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

## GUIDE mode {#guide-mode}

### `get_guide_by_role` {#get_guide_by_role}

**Determinístico**. Práticas atribuídas por *role* e/ou fase do SDLC.

**Parâmetros:**
- `risk_level` (`L1` | `L2` | `L3`) — obrigatório
- `role` (string) — opcional
- `phase` (string) — opcional; fases canónicas `plan` | `design` | `develop` | `build` | `test` | `deploy` | `operate` | `govern` (os *aliases* resolvem: `implement`→`develop`, `requirements`→`plan`, `governance`→`govern`)

**Output sem `role`/`phase`:** `role_summary{}` + `phase_summary{}` (contagens) — útil para discovery.
**Output com `role` ou `phase`:** `assignments[]` + *user stories*.

**Regra crítica:** **sempre passar `role` ou `phase`** para obter detalhes — sem nenhum dos dois, devolve só contagens.

---

### `get_threat_landscape` {#get_threat_landscape}

**Determinístico**. *Threats* relevantes para um *risk level* / *concern*, com mitigações.

**Parâmetros:**
- `risk_level` (`L1` | `L2` | `L3`) — obrigatório
- `concerns` (string[]) — opcional
- `detail` (`lista` | `standard` | `full`) — opcional; `minimal` é recusado, com o mesmo aviso que no prepare
- `limit` — opcional, 25 por omissão; `coverage` e `size_estimate` vêm sempre

**Ordem:** as ameaças vêm ordenadas por pertença ao âmbito declarado. Primeiro vêm os capítulos de domínio dos *concerns* declarados. Os capítulos 01 e 02, com as meta-ameaças de processo, vêm no fim. Dentro de cada grupo, a ordem é por `mitigation_confidence`, capítulo e id. Por isso, a primeira página é a parte relevante, e as seguintes acrescentam o geral.

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

:::info *Routing* dos *concerns* — `routing_basis`
Todos os *concerns* do vocabulário são aceites, mas só uma parte tem capítulo de ameaças próprio (por exemplo `architecture`, `iac`, `logging`, `supply_chain` e `threat_modeling`). Para os outros, as ameaças chegam pelos capítulos que definem os controlos activados. Cada resposta declara, por *concern*, a base do *routing* em `routing_basis`: `domain_chapter` quando o *concern* tem um capítulo de ameaças próprio, `activated_controls` quando as ameaças chegam pelos capítulos que definem os controlos activados. Um *concern* que não tem rota vai para `unsupported_concerns`.
:::

---

### `plan_sbd_toe_repo_governance` {#plan_sbd_toe_repo_governance}

Lista os artefactos que o manual identifica para um repositório, agrupados por capítulo.

**Parâmetros:** `riskLevel`, `offset`, `limit` (paginado).

**Output:**

- `riskLevel` e `risk_level_effect`, que é `{filters, basis, note, asserts}` e diz quanto o nível filtra, e porquê;
- `totalArtefacts`, o número de linhas capítulo↔artefacto;
- `artefact_totals`, com `distinct_count` (artefactos distintos) e `chapter_relation_count` (linhas). Nunca se somam linhas para contar artefactos;
- `byChapter[]`, em que cada entrada é `{chapterId, artefacts[]}` e cada artefacto é `{artefactId, chapterId, riskLevels[]}`, com ids na forma `ART-<slug>-<hash>`;
- `coverage`, que pagina sobre os capítulos, mais `size_estimate`, `note` e `next`.

A relação capítulo↔artefacto é uma projecção: não diz quem possui o artefacto nem obriga a produzi-lo.

**Padrão:** *bootstrap* de governança num repo novo — gerar a partir da lista artefactos por capítulo, criar os ficheiros vazios + READMEs.

---

### `map_sbd_toe_review_scope` {#map_sbd_toe_review_scope}

Dado um conjunto de ficheiros alterados, devolve que **bundles do manual** rever.

**Parâmetros:** `changed_files` (string[])

**Output:** capítulos / bundles a rever + *rationale* (ex.: "ficheiros sob `iac/` → cap. 08").

**Padrão:** *PR auditor*. Combinar com `consult_security_requirements` para enumerar controlos por capítulo.

---

### `prepare_sbd_toe_codegen_context` {#prepare_sbd_toe_codegen_context}

A tool **mais sofisticada** — devolve contexto determinístico para *codegen*, *review* ou *test-plan*.

**Parâmetros:**
- `task` (string) — em modo declarativo (o *default*) é contexto **registado** e opcional; só é motor da seleção em `selection_mode: "discover"`
- `risk_level`, `mode` (`codegen` | `review` | `test-plan`), `concerns`, `exposure`, `data_sensitivity` (`low` | `personal` | `regulated` | `secrets`), `technologies`, `changed_files` — a declaração (passar tudo o que se sabe; valores em `sbd://toe/activation-vocabulary`)
- `stack` — texto livre; só conta quando traz um *token* do vocabulário, por isso é preferível declarar `technologies`
- `chapters`, `categories`, `selection_mode`, `detail` (`lista` | `standard` | `full`), `include_relations`, `debug` — opcionais
- `regulatory_frameworks`, `include_regulatory_overlay` — opcionais

**Output (campo `status`):**

| `status` | Significado | Acção |
|---|---|---|
| `ready_for_codegen` | Scope claro, contexto pronto | Proceder — preencher `security_rationale` |
| `needs_input` | Nada foi declarado | **STOP** — a resposta traz o vocabulário, os candidatos a confirmar e, para declarações inertes, os `valid_values`; confirmar com o utilizador e declarar |
| `needs_clarification` | Inputs ambíguos | **STOP** — perguntar ao utilizador, não gerar código |
| `needs_decomposition` | Scope demasiado largo, ou seleção acima do que o nível de `detail` promete caber | **STOP** — nesse caso, executar os lotes medidos de `requirement_ceiling.batches`, cuja união é a seleção inteira (os lotes podem partilhar requisitos) |
| `unsupported_scope` | Capacidade ausente no servidor | **STOP** — reportar verbatim |

**Forma da resposta:**

- **Um objeto por requisito** — `{id, name, type, description, verify, evidence}`: o requisito, como se verifica e que evidência se espera, num só sítio.
- **`detail`** — os três níveis servem o mesmo conjunto de ids citáveis e o mesmo requisito completo, e a descrição nunca é cortada em nenhum nível. Muda o que vem *inline* e o que vem por referência:
  - **`lista`** traz inline os requisitos, os controlos e as entidades do grafo agrupadas por *slice*, o bloco `citations`, as instruções de geração e o *template* de `security_rationale`. Por referência vêm o `manual_grounding` (contagens por grupo e `entries_ref` para `full`), as relações (`relations_summary`, com a contabilidade exacta) e o *trace* de activação (só com `debug: true`). A `adjacency` vem em resumo, com `detail_ref`.
  - **`standard`** é o mesmo que `lista`, mais o detalhe da `adjacency` inline, com todos os sinais.
  - **`full`** é o nível por omissão. Traz o mesmo que `standard`, mais o `manual_grounding` verbatim, o `activation_trace` e uma `relations_ref` executável em `trace_sbd_toe_graph`. Com `include_relations: true`, as relações vêm inline.
- **Envelope** — `lista` e `standard` prometem caber num envelope de tokens, medido sobre o *payload* que o cliente recebe. Acima dele, a resposta é `needs_decomposition` com lotes medidos que, juntos, cobrem a seleção inteira. `full` não tem envelope e declara o preço em `size_estimate`.
- **`adjacency`** — o que não foi declarado e mudaria o conjunto selecionado (por exemplo, declarar a exposição pública).
- **`completeness_report.verification`** — a cobertura de verificação, com os ids de padrão em `verification.by_ref`.
- **`size_estimate`** — o tamanho da própria resposta; `within_envelope: false` avisa que excede o envelope previsto.
- **Notas por referência** — os `note_id` resolvem-se em `sbd://toe/notes/{id}`, em vez de repetidos em cada resposta.

**Disciplina obrigatória após `ready_for_codegen`:**

- O bloco `citations` devolvido é o **mundo fechado** de ids válidos — não inventar ids.
- Preencher `security_rationale.decisions[].cited_ids` com pelo menos 1 ID por decisão não-trivial.
- Preencher `security_rationale.validations[]` (validações concretas implementadas).
- Preencher `security_rationale.expected_evidence[]` (artefactos para o reviewer — código sozinho **não** é evidência).
- Preencher `security_rationale.residual_risk` (o que não foi endereçado).
- Sinalizar `completeness_report.m_recall < 1.0` ao utilizador (cobertura parcial).

Ver guia detalhado em [Caso de uso — codegen grounded](./casos-uso/codegen-grounded) e no resource [`sbd://toe/grounded-codegen-guide`](./06-resources-prompts.md#sbdtoegrounded-codegen-guide).

---

## SETUP mode {#setup-mode}

### `generate_sbd_toe_skill` {#generate_sbd_toe_skill}

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

### `setup_sbd_toe_agent` (prompt) {#setup_sbd_toe_agent-prompt}

Tecnicamente um *prompt*, não uma *tool* — mas funciona como inicializador da sessão.

**Parâmetros:** `riskLevel`, `projectRole`

**Output:** a exigência dominante de cada capítulo no nível (aplicabilidade graduada — nenhum capítulo excluído) + regras específicas do papel. Clientes sem suporte de *prompts* (como o Claude Desktop) não o expõem.

---

## Vista de implementação {#implementation-view-v5}

Estas tools respondem a **"como pôr de pé e governar o SbD"** — distinta da vista operacional ("o que fazer em cada fase do SDLC"). Todas são *coverage-preserving* (paginação com `coverage.hasMore`/`nextOffset`; nada truncado em silêncio) e devolvem uma banda `next` com os próximos passos sugeridos.

### `get_sbd_toe_chapter_implementation_checklist` {#get_sbd_toe_chapter_implementation_checklist}

A narrativa de implementação canon/20 de um capítulo (o "como implementar"), distinta do DoD estruturado de *user story* (esse está em `get_guide_by_role(include_detail=true)`).

**Parâmetros:** `chapter` (id ou número), `risk_level?`, `limit?`, `offset?`
**Output:** `data.items[]` (prosa com `chunk_id` rastreável) + `next`.

### `get_sbd_toe_chapter_capability` {#get_sbd_toe_chapter_capability}

Leitura IMPL: para implementar o capítulo N, que capacidade é precisa, como se sabe que existe e como se mede. Devolve os KPIs que o manual define para o capítulo, com `thresholds_by_level` (L1/L2/L3) como dados, e os artefactos que a capacidade deve produzir. Alcança-se por `chapter`, `metric_id` ou `dimension`. `risk_level` acrescenta `target_at_level`, e sem `chapter` devolve todos os KPIs publicados. Fecha o ciclo com [`assess_sbd_toe_implementation`](#assess_sbd_toe_implementation). Não é a leitura GUIDE: essa é [`select_sbd_toe_requirements`](#select_sbd_toe_requirements).

### `get_sbd_toe_operating_model` {#get_sbd_toe_operating_model}

RACI, *decision-rights*, cadências de governança e modelos de organização, promovidos do *rollout playbook*.

**Parâmetros:** `orgScope?`, `limit?`, `offset?`
**Output:** `data.sections[]` (prosa, paginado). Declara a fronteira: **não prescreve organigrama** (varia por setor/dimensão).

### `plan_sbd_toe_rollout` {#plan_sbd_toe_rollout}

Roadmap por fases — as fases canónicas do ciclo de vida mapeadas a capítulos.

**Parâmetros:** `orgProfile?`, `horizon?`, `limit?`, `offset?`
**Output:** `data.phases[]` (`order`, `phase_id`, `label`, `chapter`), `model: "phase-ordered-mvp"`. O DAG de dependências é **deferido** (declarado, não fingido).

### `get_sbd_toe_verification_matrix` {#get_sbd_toe_verification_matrix}

O lado **EXPECTED** da verificação: por requisito/controlo, o método de validação + evidência esperada + referência a *EvidencePattern*. Complemento determinístico do auditor e do plano de testes.

**Parâmetros:** `risk_level` (obrigatório), `requirement_ids?` (até 50 por chamada — o fecho requisito→prova a partir de uma seleção), `limit?`, `offset?`
**Output:** `data.rows[]` (`evidence_pattern_id` `EP-*`, `requirement_id`, `control_id`, `validation_method`, `expected_evidence`, `evidence_type`, `expected_artifact_type_ids[]`, `source`) + `coverage_gaps` (requisitos sem padrão — declarados).

### `assess_sbd_toe_implementation` {#assess_sbd_toe_implementation}

Auto-relato de postura: compara valores de KPI submetidos contra os *thresholds* por nível.

**Parâmetros:** `kpi_values` (mapa `metric_id`→número; vazio é recusado com `-32602`), `risk_level`, `chapter?` (restringe o universo), `offset?`, `limit?`
**Output:** `posture` (`below`/`at`/`above`) + `totals{applicable, meets, gaps, not_reported}` + `per_kpi` + `unknown_metrics`. **Stateless** (nada é guardado); um KPI aplicável sem valor é `not_reported`, **nunca** *pass*.

:::note Payload
Devolve todos os KPIs aplicáveis, o que pode tornar o output grande — `chapter` restringe o universo e `offset`/`limit` percorrem-no. Submeter os `kpi_values` que se tem; os em falta vêm marcados `not_reported`.
:::

### `map_sbd_toe_regulatory_activation` {#map_sbd_toe_regulatory_activation}

Lente regulatória (o inverso da *provenance*): dado um *framework*, que áreas/capítulos do manual ele activa.

**Parâmetros:** `framework` (`DORA` | `NIS2` | `CRA` | `RGPD`; ou `EXT-DORA`…), `limit?`, `offset?`
**Output:** `data.activated[]` por capítulo (`mapping_count`, `obligation_count`, `by_target_type`, `example_citation`) + `totals`. *Framework* desconhecido → erro `-32602`. Provenance declara: **cross-check ≠ atestação de conformidade**.

---

## Leituras NORMATIVA e PROGRAMA {#leituras-normativa-e-programa}

### `get_sbd_toe_playbook` {#get_sbd_toe_playbook}

Leitura **NORMATIVA**: devolve os playbooks publicados por diploma, com a autoridade declarada. Para referenciais sem cross-check publicado (ISO, PCI, SOC2, …), a resposta declara `no_cross_check` em vez de improvisar uma correspondência. É o caminho principal do [caso de uso de cross-check normativo](./casos-uso/cross-check-conformidade), a par de `map_sbd_toe_regulatory_activation`.

Todos os parâmetros são opcionais:

- Sem argumentos, devolve o índice.
- `framework`, por código (`DORA`, `NIS2`, `CRA`, `RGPD`, `AI-ACT`, `ENISA-CSA`) ou id (`EXT-DORA`…), devolve os playbooks desse diploma.
- `playbook_id`, um id vindo do índice (ex.: `OVR-DORA-playbook`), devolve as secções paginadas.
- `kind` filtra o índice por tipo: `normative_cross_check`, `implementation_playbook`, `convergence_note`, `illustrative_example` ou `illustrative_index`.
- `offset` e `limit` (por omissão 10) paginam as secções.

Os exemplos ilustrativos vêm numa banda separada, e um diploma sem cross-check publicado devolve `no_cross_check`. O índice traz `delimitation`, `scope`, `normative_playbooks`, `illustrative_examples`, `covered_frameworks`, `roadmap_declared_by_manual` e `coverage`.

### `get_sbd_toe_macro_processes` {#get_sbd_toe_macro_processes}

Leitura **PROGRAMA**: por onde começar e em que sequência. Sem argumentos, devolve a ordem de adopção publicada, derivada só das arestas de dependência, os macro-processos e os pré-requisitos. Com `mp_id` (ex.: `MP-01`), devolve um macro-processo em detalhe: pergunta, continuidade, invariante, dono, participantes, percurso de capítulos, indicadores, pontos de controlo, evidência esperada e proporcionalidade L1–L3. Declara os seus limites: não há entidade «programa», a travessia MP↔fase do SDLC é uma lacuna publicada, e `traverses_bundles` é um percurso, não uma relação de pertença.

---

## Rastreio e leitura de resources {#rastreio-e-leitura-de-resources}

### `read_sbd_toe_resource` {#read_sbd_toe_resource}

Espelho de `resources/read` para clientes sem suporte a *resources* MCP, como o Claude Desktop. Devolve qualquer resource por URI, incluindo os que têm *template*, com o valor já na URI (ex.: `sbd://toe/notes/prepare.repeat_call_hint`). `slot` devolve um só slot de um recurso JSON com slots (`codegen-instructions`). `char_offset` e `char_limit` paginam o texto. Uma URI desconhecida devolve um erro declarado com a lista válida.

```
read_sbd_toe_resource(uri="sbd://toe/version")
```

### `trace_sbd_toe_requirement_sources` · `trace_sbd_toe_graph` {#trace_sbd_toe_requirement_sources--trace_sbd_toe_graph}

**`trace_sbd_toe_requirement_sources`** diz de onde vem cada requisito. As fontes directas (`source_anchors`, o marcador «Fontes» do próprio manual) vêm separadas da cadeia compensada REQ→CTRL→ACO→fontes, que tem tipo e confiança por salto. Essa cadeia leva o rótulo `coverage_compensated`: é cobertura por correspondência entre modelos, não autoria, e `related` não cobre. Aceita 1 a 50 `requirement_ids` e é paginada. `include_chains: false` devolve só contagens e referência. Requisitos sem fonte declarada e ids desconhecidos são declarados.

**`trace_sbd_toe_graph`** faz travessia multi-salto, curada, sobre o grafo de relações da AppSec Core (slices, objectivos de controlo, mecanismos, práticas), para perguntas de rastreabilidade que as tools de alto nível não expõem. Escolhe-se uma lente com `lens`:

- `slice_implementation`: slice → objectivos → mecanismos e práticas;
- `objective_realization`: objectivo → mecanismos e práticas;
- `mechanism_provenance`: mecanismo ou prática → objectivos → slices.

`anchor` restringe a travessia a uma entidade. A travessia é determinística e paginada (`page`, `pageSize` até 200, `total` e `cursor`), e nunca trunca em silêncio. É o destino das `relations_ref` do prepare.

---

## Diagnóstico {#diagnóstico}

### `inspect_sbd_toe_retrieval` {#inspect_sbd_toe_retrieval}

Diagnóstico do retriever — útil quando uma query devolve resultados inesperados. Mostra ranking, scores, e *rule_trace* completo.

**Parâmetros:** `question` (string)

---

## Combinatória — padrões recomendados {#combinatória--padrões-recomendados}

### Pergunta estruturada {#pergunta-estruturada}

```
consult_security_requirements(L2, ["auth"])
```

### Pergunta narrativa {#pergunta-narrativa}

```
search_sbd_toe_manual("threat modeling stride")
```

### Resposta complexa (threat model / security plan) {#resposta-complexa-threat-model--security-plan}

```
1. consult_security_requirements(L2, concerns)   # requisitos + controlos
2. get_threat_landscape(L2, concerns)             # threats relevantes
3. get_guide_by_role(L2, role)                    # práticas do role
4. → gerar documento citando IDs dos 3 passos
```

### PR review {#pr-review}

```
1. map_sbd_toe_review_scope(changed_files)        # que capítulos
2. consult_security_requirements(risk_level, concerns)  # controlos activos
3. → enumerar findings citando CTRL-* + chapter_id
```

### Codegen grounded {#codegen-grounded}

```
1. prepare_sbd_toe_codegen_context(task, mode="codegen", detail, ...declaração)
2. ramificar por status (ver tabela acima)
   - needs_input → confirmar a declaração com o utilizador e voltar a chamar
   - needs_decomposition → seguir requirement_ceiling.batches, um lote de cada vez
3. se ready_for_codegen → gerar código + tests + security_rationale
```

## A seguir {#a-seguir}

[Resources e prompts](./06-resources-prompts.md) — URIs `sbd://toe/*` para *grounding* estrutural e prompts pré-empacotados.
