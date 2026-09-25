# `translation/terms/` — registo de termos

**Instrumento do épico §2 e do brief da frente 0 §5.** Um registo em dados, não em prosa. É a única fonte de
terminologia que `translate.py` e `terms_lint.py` consultam. O seu SHA-256 (`registry.yaml`, bytes tal como
commitados) fica gravado em cada ficheiro traduzido.

**Ortografia da prosa EN:** British English (-isation, -our, -re, -ll-; decisão do lead 2026-09-25). É uma regra
do lint, não uma entrada do registo. Identificadores não são inglês, são ids: ficam intactos (`do-not-translate`).

## Ficheiros

| ficheiro | o que é | quem escreve |
|---|---|---|
| `input/…-levantamento-termos-en-papers-P0-P7.{yaml,csv}` | input do Curator, **imutável** (SHA-256 no brief) | ninguém |
| `registry.yaml` | **o registo** | `terms_import.py` semeia; depois só o Manual agent (espécies 1 e 3) e, por ratificação, Archon/lead (espécie 2) |
| `pending-export.md` | fila exportada por `terms_lint.py --export-pending` para o hub | gerado |

## Esquema de `registry.yaml`

```yaml
meta:
  version: 1
  spelling: en-GB
  source_locale: pt
  target_locale: en
  curator_input_sha256: {yaml: "fa265af8…", csv: "ded69c97…"}
terms:
  - key: slice                      # chave estável do registo; snake_case ASCII; nunca muda
    species: 1                      # 1 = já no registo científico · 2 = por nascer · 3 = vocabulário de prosa
    state: in-record                # in-record · coined · pending · changed · do-not-translate
    owner: manual-agent             # manual-agent · archon · lead
    en: slice                       # forma EN canónica (null enquanto pending na espécie 2)
    en_variants: [slices, per-slice, cross-slice]   # formas aceites na prosa EN (lint)
    pt: fatia                       # forma PT canónica (null quando o Manual usa o EN sem tradução)
    pt_variants: [fatias]           # formas PT que o detector reconhece no texto fonte
    ontology_id: null               # id ontológico/KG quando existe (ex.: ACO-ATB, ACA-*), senão null
    sense: "Partição de domínio da ontologia AppSec Core …"   # uma frase; a do Curator para a espécie 1
    senses: []                      # quando polissémico: lista de {sense, where}; obrigatório se state=pending por polissemia
    evidence: {paper: P1, line: 16, section: Abstract, quote: "…"}   # âncora que justifica (espécie 1: do Curator)
    counts: {P0: 8, P1: 82, …, total: 501}        # do Curator; informativo
    change_cost: medio              # do Curator: baixo · medio · alto (alto = em título/DOI/slug)
    curator: {id: slice, grupo: A-semente, origem: emprestado-especializado, pt_status: colisao}  # rastreio ao input
    previous: null                  # obrigatório se state=changed: {en, used_in, reason, date, ratified_by}
    proposal: null                  # espécie 2: EN proposto pelo Manual agent para decisão; NUNCA copiado para `en` sem ratificação
    false_friends: []               # espécie 2: EN óbvio que já tem outro sentido nos papers, com a chave do registo que o prova
    pending_reason: null            # obrigatório se state=pending: polysemy · en-vs-en-collision · unborn · v26-collision
    blocks_translation: true        # se true e state=pending, bloqueia blocos que contenham pt/pt_variants
    notes: ""
```

## Regras de estado

- **`in-record`**: termo dos papers, revisto e mantido. É a **tradução obrigatória** de `pt`/`pt_variants`.
- **`pending`**: bloqueia a tradução de qualquer bloco (parágrafo, item, célula) da fonte que contenha `pt` ou
  `pt_variants` (`blocks_translation: true`). Quem levanta: espécie 1 → Manual agent com ratificação do lead;
  espécie 2 → Archon (ontologia) ou lead (programa), via `pending-export.md` encaminhado pelo Orchestrator.
- **`coined`**: espécie 2 com EN decidido e registado (`ratified_by`, `date` em `notes` ou `previous`).
- **`changed`**: espécie 1 cujo EN foi alterado face aos papers; `previous` obrigatório — é a reconciliação
  («o que em [P1] chamámos X passa a Y»).
- **`do-not-translate`**: ids, códigos de categoria, chaves de dados, nomes nascidos em inglês. `translate.py`
  protege-os antes do modelo e o `equivalence.py` conta-os. A lista de padrões vive em
  `translation/scripts/protected_tokens.py`; entradas do registo desta classe cobrem **nomes**, não padrões.

## Espécie 1 — como se semeia a partir do Curator

- Uma entrada por linha do CSV (157), `species: 1`, `owner: manual-agent`, `state: in-record`, salvo:
  - `origem: nao-traduzir` → `state: do-not-translate`;
  - `multiplos_sentidos: sim` (19) → `state: pending`, `pending_reason: polysemy`, `senses` preenchido do YAML;
  - `traversal` → `pending`, `pending_reason: en-vs-en-collision`;
  - `contract_generic` → **desdobra-se** em `manual_mapping_contract` e `consumer_contract` (mais `slice_contract` e
    `retrieval_contract` já existentes) — quatro entradas;
  - `floor_closure_dependency`, `mandatory`, `carried_forward_deferred`, `absence`, `scope_non_goals` → ficam
    `in-record` **no sentido dos papers**, e são citados em `false_friends` das entradas de espécie 2.
- `pt` = `pt_conceito` quando `pt_status: inequivoco`; caso contrário `null` e `pt_variants` vazio — o Manual agent
  preenche na revisão. `en` = primeira forma de `termo_en` antes de ` / `; `en_variants` = `variantes` do YAML.
- Re-executar o importador **nunca** sobrescreve `state`, `en`, `pt`, `pt_variants`, `previous`, `proposal`,
  `notes` de uma entrada existente; só actualiza `counts`, `evidence`, `curator`, `change_cost`.

## Espécie 2 — autorada pelo Manual agent, decidida por Archon/lead

Entradas com `state: pending`, `pending_reason: unborn`, `en: null`, `proposal` preenchido, `false_friends`
preenchido. Nunca passam a `coined` por acção do Manual agent.

## Espécie 3 — vocabulário de prosa

`owner: manual-agent`, `state: in-record`, sem `evidence` de paper. Semeadas por varrimento de frequência do
corpus e fechadas pelo Manual agent. O lint exige consistência (mesma forma PT → mesma forma EN).
