# `translation/scripts/` — ferramentas de equivalência e sincronismo

Python 3 (≥ 3.10), só stdlib + PyYAML (`pip install pyyaml`). Correr a partir da raiz do repositório.

**A direcção é parâmetro.** Todos os scripts aceitam `--source-locale` e `--target-locale`
(omissão: `pt` → `en`) e `--docs-dir` / `--i18n-dir` (omissão: derivados da raiz do repo —
`manuals_src/docs/sbd-toe` e `manuals_src/i18n`). A fonte é sempre o que está em `--docs-dir`;
a tradução é `<i18n-dir>/<target-locale>/docusaurus-plugin-content-docs/current/<caminho relativo>`.
Na Fase 2 trocam-se os locales (no `env` do workflow) sem mudar código. Nenhum script assume PT→EN.

**Caminhos em NFC.** Todos os caminhos relativos ao corpus são normalizados para Unicode NFC antes de
servirem de chave, de serem comparados ou mapeados fonte↔espelho (o APFS devolve
`06-manual-formação-por-capitulo.md` em NFD; o índice de versões e o Linux têm NFC). A ordenação faz-se
sobre a forma NFC, por isso as chaves do `sync-state.json` são idênticas em macOS e no CI.

| script | função |
|---|---|
| `common.py` | hash de conteúdo do contrato (`content_sha256`), hash do glossário aplicado (`glossary_sha256`), raiz do repo, frontmatter, mapeamento fonte↔espelho, iteração do corpus, parser markdown mínimo, slugger do Docusaurus |
| `protected_tokens.py` | lista única de prefixos de identificadores e siglas `do-not-translate` |
| `fingerprint.py` | impressão digital estrutural de uma página, independente da língua |
| `equivalence.py` | compara a impressão digital da fonte com a da tradução; falha em qualquer divergência não-textual |
| `sync_state.py` | deriva o estado de sincronismo por hashes e escreve/verifica `translation/state/sync-state.json` |
| `terms_import.py` | frente 3: semeia/actualiza `translation/terms/registry.yaml` a partir do levantamento do Curator (regras mecânicas do README do registo) |
| `terms_lint.py` | frente 3: `validate` (esquema), `spelling` (en-GB), `pending-blocks` (detector de blocos bloqueados), `consistency` (PT→EN por bloco), `export-pending` (fila para o hub), `hash` |
| `species3_candidates.py` | frente 3: varrimento de frequência da prosa PT → CSV de **candidatos** a espécie 3 (não entra no registo) |
| `translate.py` | frente 6: `prepare` (jobs com esqueleto + marcadores + glossário + proveniência) → tradução por agente externo → `assemble` (reconstrói, valida, grava) → `check` (atalho do CI). Não chama nenhum modelo |
| `tests/` | `unittest` com fixtures em `tests/fixtures/` |

## `fingerprint.py`

```bash
python translation/scripts/fingerprint.py 010-sbd-manual/00-fundamentos/index.md          # resumo legível
python translation/scripts/fingerprint.py 010-sbd-manual/00-fundamentos/index.md --json   # JSON determinista (chaves ordenadas)
python translation/scripts/fingerprint.py manuals_src/i18n/en/docusaurus-plugin-content-docs/current/010-sbd-manual/00-fundamentos/index.md
```

Dimensões: frontmatter (`id` efectivo — declarado ou derivado do nome do ficheiro sem prefixo numérico —,
`sidebar_position`, conjunto de chaves excepto `title`/`description`/`translation`); árvore de cabeçalhos
(nível + id explícito `{#id}` ou derivado pelo slugger do Docusaurus, com sufixos `-N` por página); tabelas
(colunas, linhas, alinhamentos); blocos de código (linguagem + SHA-256 do conteúdo); admonitions (tipo, ordem,
`userstory` incluído); listas (itens de topo, itens totais, profundidade); ligações internas e imagens (multiset,
com linhas); tokens protegidos (multiset, com linhas — corpo fora de código/comentários mais `title`/`description`);
declarações `import`/`export` MDX; comentários HTML (contagem); marcadores `<!-- i18n:pending … -->`.

`--slugger runtime` (omissão) replica o plugin de cabeçalhos do runtime do Docusaurus (ids explícitos não
entram no slugger); `--slugger cli` replica `docusaurus write-heading-ids` (ids explícitos registados primeiro).
No corpus actual os dois produzem ids idênticos.

## `equivalence.py`

```bash
python translation/scripts/equivalence.py --all                                  # todas as traduções existentes
python translation/scripts/equivalence.py --path 010-sbd-manual/00-fundamentos   # um directório
python translation/scripts/equivalence.py --path 010-sbd-manual/00-fundamentos/index.md
python translation/scripts/equivalence.py --all --json                           # relatório máquina
```

Para cada ficheiro traduzido existente imprime `OK`/`FAIL` e, por divergência, dimensão, esperado, obtido e
linha (fonte/tradução) quando possível. Exit 1 se houver alguma divergência ou um ficheiro órfão no espelho;
`--all` sem traduções é sucesso com aviso. Um ficheiro fonte sem frontmatter aceita no espelho um frontmatter
mínimo só com `id`. Cabeçalhos sem id explícito não têm o id comparado (é derivado da língua), excepto se a
tradução o fixar explicitamente — então tem de ser igual ao derivado da fonte.

## `sync_state.py`

```bash
python translation/scripts/sync_state.py --write   # regenera translation/state/sync-state.json
python translation/scripts/sync_state.py --check   # exit 1 se o ficheiro commitado não for reproduzível (ignora generated_at)
python translation/scripts/sync_state.py           # imprime o estado derivado
```

Estados derivados só de hashes (contrato em `translation/README.md`): `untranslated`, `synced`, `partial`,
`pt-ahead`, `en-ahead`, `drift`, `stale-terms`; precedência `drift > en-ahead > pt-ahead > stale-terms > partial > synced`.
`target_sha256` no ficheiro de estado é o hash **actual** do corpo traduzido (ficheiro sem o bloco `translation`);
o valor gravado no momento da tradução vive no frontmatter do espelho. `terms_sha256` é o hash do registo dado por
`--registry` (omissão: `translation/terms/registry.yaml` na raiz do repo); enquanto esse ficheiro não existir é
`null` e `stale-terms` nunca ocorre.

**`stale-terms` é preciso, não byte a byte.** O frontmatter do espelho grava `glossary_keys` (chaves do registo que o
`prepare` aplicou ao ficheiro) e `glossary_sha256` = `common.glossary_sha256(registo, glossary_keys)` — SHA-256 da
serialização canónica (JSON, chaves ordenadas, `ensure_ascii=False`, sem espaços) da lista, por ordem de chave, de
`{key, state, en, en_variants, pt, pt_variants, blocks_translation}` dessas entradas (variantes como conjunto ordenado;
chave ausente do registo serializa como `{"key": …, "missing": true}`). O `sync_state.py` recalcula esse hash com o
**registo actual** e as `glossary_keys` gravadas: diferente → `stale-terms`. Só esses campos contam — `notes`,
`evidence`, `counts`, `sense`, `proposal`, … nunca tornam uma tradução stale; uma entrada que o ficheiro não usou também
não; uma chave aplicada que saiu do registo conta como mudança. `terms_sha256` (registo inteiro) fica como proveniência.
O estado por ficheiro ganha `glossary_sha256_at_translation` (`null` quando ausente). Um espelho **sem**
`glossary_sha256` (gerado antes deste campo) mantém a regra antiga — `terms_sha256` gravado ≠ hash actual do registo — e
gera o aviso «legacy provenance: re-stamp with assemble» (exit 2, como qualquer aviso) enquanto houver registo; um
`glossary_sha256` sem `glossary_keys` em lista é tratado como legado, com aviso. Um ficheiro no espelho sem bloco
`translation` (feito à mão) gera aviso e exit 2.

## `terms_import.py`

```bash
python translation/scripts/terms_import.py --input translation/terms/input/2026-09-24-levantamento-termos-en-papers-P0-P7.yaml \
    --registry translation/terms/registry.yaml            # semeia ou actualiza
python translation/scripts/terms_import.py --input … --registry … --dry-run   # só o resumo e o estado (new/changed/unchanged)
```

Aplica **mecanicamente** as regras de «Espécie 1 — como se semeia» de `translation/terms/README.md` (o YAML do Curator é
autoritativo; o CSV só é hasheado). 157 linhas → 158 entradas (`contract_generic` desdobra em `manual_mapping_contract`
e `consumer_contract`). `key` = `id` do Curator em snake_case ASCII (`ControlObjective` → `control_objective`; única
excepção declarada `AppSecCore` → `appsec_core`, a grafia snake_case que o programa já usa); o id original fica em
`curator.id`. `pt` = `pt_conceito` só quando `pt_status: inequivoco`; se o Curator listar alternativas («ciclo /
iteração»), a primeira forma é `pt` e as restantes vão para `pt_variants` (`--split-pt-alternatives` aplica a mesma
repartição a entradas já semeadas cujo `pt` ainda tenha « / »; idempotente, não toca em mais nada).
Re-executar nunca sobrescreve `state`, `en`, `en_variants`, `pt`, `pt_variants`, `previous`, `proposal`,
`false_friends`, `pending_reason`, `blocks_translation`, `notes` (nem `sense`/`senses`/`owner`/`species`); só
`counts`, `evidence`, `curator`, `change_cost` são refrescados. Entradas do registo que não vêm do levantamento
(espécies 2 e 3) ficam intactas. Saída determinista (ordem de chaves do esquema, entradas por `key`, largura 100,
`\n` final normalizado — o mesmo `normalise_text` do hash).

## `terms_lint.py`

```bash
python translation/scripts/terms_lint.py validate --registry translation/terms/registry.yaml
python translation/scripts/terms_lint.py spelling --path <ficheiro-ou-dir EN> [--registry …] [--fix]
python translation/scripts/terms_lint.py pending-blocks --path manuals_src/docs/sbd-toe --registry … [--json] [--all-files] [--fail-on-block]
python translation/scripts/terms_lint.py consistency --path manuals_src/i18n/en/docusaurus-plugin-content-docs/current --registry …
python translation/scripts/terms_lint.py export-pending --registry … --out translation/terms/pending-export.md
python translation/scripts/terms_lint.py hash --registry …
```

- `validate` — esquema do registo (chaves obrigatórias e desconhecidas, valores de `species`/`state`/`owner`/
  `pending_reason`, `previous` obrigatório em `changed`, `proposal` + `false_friends` obrigatórios em espécie 2
  `pending`, `en` null só em espécie 2 `pending`, `senses` obrigatório em `polysemy`, chaves únicas e em snake_case,
  `false_friends` a apontar para chaves existentes). Exit 1 em falha.
- `spelling` — regra en-GB sobre a prosa EN (fora de código, comentários, frontmatter estrutural — só `title` e
  `description` contam —, destinos de ligações, tags HTML, ids `{#…}`). Isento: tokens protegidos
  (`protected_tokens.py`), `en`/`en_variants` de entradas `do-not-translate` (sensível a maiúsculas, verbatim) e de
  entradas `in-record`/`coined`/`changed` (insensível) **na sua grafia en-GB**: a ortografia é estilo, regra do lint,
  nunca `changed` — o registo guarda a forma dos papers (`normalization`, `normalized ontology`, `Organizational
  view`, `Centralized Logging`) e a prosa EN tem de escrever `normalisation`, `normalised ontology`,
  `organisational view`, `centralised logging`. O lint imprime uma linha única «N registry forms are AmE-spelled;
  en-GB expected in prose». Entradas `pending` **não** isentam nada — não têm autoridade sobre a prosa. As regras
  vivem num único dicionário `SPELLING_RULES` (-ise/-isation com excepções `size`/`prize`/`seize`/`capsize`; -yse;
  -our; -re; -ll-; `programme` — `program` só é aceite em contexto de software: `program code`, `the program runs`,
  `a Python program`; `licence` substantivo por contexto; `artefact` só em minúsculas — `Artifact`,
  `ArtifactRequirement`, `artifact_types` são identificadores; diversos). Palavras `CamelCase`/`ALLCAPS` não são
  prosa. Exit 1 com erros; `--fix` aplica só substituições inequívocas (erros de regras `fixable`, nunca avisos nem
  `programme`).
- `pending-blocks` — para cada bloco da fonte (parágrafo, item de lista, célula de tabela, cabeçalho, título de
  admonition, `title`/`description` do frontmatter; fora de código, de declarações MDX `import`/`export` até à linha em branco seguinte e de blocos `<style>`/`<script>`) que contenha, por palavra inteira sem distinção
  de maiúsculas e em NFC, `pt` ou `pt_variants` de uma entrada `pending` com `blocks_translation: true`, imprime
  `ficheiro:linha  chave  excerto`; resumo por ficheiro (só os bloqueados, salvo `--all-files`) e por chave. Exit 0
  (detector), salvo `--fail-on-block`. `--json` para o `translate.py`/`sync_state.py`.
- `consistency` — espécie 1/3: uma forma PT (`pt`/`pt_variants`) de entrada `in-record`/`coined`/`changed` presente num
  bloco da fonte tem de sair no bloco espelho com `en` ou uma de `en_variants` (alinhamento por bloco quando fonte
  e espelho têm o mesmo número de blocos; senão por ficheiro). Forma PT deixada no EN = aviso. Sem ficheiros EN:
  sucesso com aviso.
  **Fronteiras (passe único 2026-09-26):** do lado PT um hífen colado conta como parte da palavra («requisito» não casa
  em «pré-requisito»); do lado EN a fronteira é tolerante («personal-data set» contém «personal data»). Formas
  morfológicas do mesmo sentido (validating/validated, assessing, auditably, stage) entram como `en_variants`.
  **Polissemia — limite declarado:** entradas que partilham uma forma PT são sentidos da mesma palavra (piso →
  foundation/floor; verificação → verification taxonomy/check; empírico → empirical knowledge/empirical); um bloco que
  traga a forma EN de QUALQUER dos sentidos passa. O lint NÃO detecta a troca de um sentido pelo outro — o registo não
  tem pistas de contexto legíveis por máquina; essa troca fica à guarda do tradutor e da revisão.
- `export-pending` — Markdown determinista, uma tabela por destinatário (`archon`, `lead`, `manual-agent`): chave,
  espécie, razão, PT, EN actual, `proposal`, `false_friends` (com o `sense` da entrada referida), `senses` resumidos,
  e as instruções de resposta. Inclui o `terms_sha256` do registo.
- `hash` — o SHA-256 que `sync_state.py` grava como `terms_sha256` (`common.file_sha256`, conteúdo normalizado).
  Como o importador escreve bytes já normalizados, coincide com `shasum -a 256`; se não coincidir, avisa.

## `species3_candidates.py`

```bash
python translation/scripts/species3_candidates.py --docs-dir manuals_src/docs/sbd-toe \
    --out translation/terms/species3-candidates.csv --top 300 [--min-docs 2] [--registry …]
```

Frequência da prosa PT (mesma extracção do `terms_lint.py`; tokens protegidos e todas as formas `pt`/`en` já no
registo removidos antes de contar). Lemas aproximados por regras de superfície (só plurais), sem NLP externo;
unigramas com ≥ 4 letras, bigramas de palavras de conteúdo e trigramas `X de Y`; stopwords PT embutidas. Colunas
`termo_pt, docs, total, exemplo_ficheiro, exemplo_linha`, ordenadas por frequência documental, total e termo. É uma
lista de **candidatos** para o Manual agent rever — nada entra no registo por este script.

## `translate.py`

**Não chama nenhum modelo.** Divide o trabalho em três passos deterministas à volta de um passo de tradução feito por
um agente/modelo externo, para que a proveniência e a estrutura sejam reproduzíveis independentemente de quem traduz.

```bash
python translation/scripts/translate.py prepare  --path 010-sbd-manual/00-fundamentos --out /tmp/jobs [--only-stale] [--force] [--json]
# passo externo: o tradutor lê /tmp/jobs/<caminho>.job.json e escreve /tmp/jobs/<caminho>.out.json
python translation/scripts/translate.py assemble --job /tmp/jobs/<caminho>.job.json [--out-json …] --engine <modelo> [--write] [--print]
python translation/scripts/translate.py check    --path 010-sbd-manual/00-fundamentos
```

**`prepare`** — para cada ficheiro fonte seleccionado e elegível pelo `sync_state` (`untranslated`, `pt-ahead`,
`stale-terms`; `--only-stale` restringe aos dois últimos; `--force` ignora o estado; `partial`, `drift` e `en-ahead`
são saltados com aviso) escreve `<out>/<caminho>.job.json`:

- proveniência: `source_path`, `source_sha256`, `source_commit` (último commit que tocou o ficheiro; `source_dirty`
  se há alterações por commitar; `--source-commit` fixa-o), `terms_sha256` (registo inteiro), `glossary_keys` (chaves
  do glossário aplicável — termos, do-not-translate e pending — ordenadas) e `glossary_sha256`
  (`common.glossary_sha256(registo, glossary_keys)`, o hash que decide `stale-terms`; ver `sync_state.py`),
  `prompt_sha256` (de `translation/prompts/translate-v2.md`), `direction`;
- **esqueleto**: a sequência de segmentos do ficheiro na ordem original, cada um com `id`, `kind`, `line`, `raw`
  (linhas verbatim) e, quando traduzível, `text` (com marcadores), `protected`, `translate`, `blocked_by`, `prefix`/
  `suffix` (o que o script repõe à volta do texto: `## `, ` {#id}`, marcador e indentação de item, `:::note `).
  Kinds: `frontmatter` (só `title`/`description` traduzem, em `fields`; o resto copia), `heading` (` {#id}` fica no
  `suffix`, nunca no texto), `paragraph` (inclui blockquotes e linhas JSX/HTML com prosa — as tags ficam marcadores),
  `list_item` (marcador e indentação no `prefix`; linhas de continuação no texto com marcadores de quebra),
  `table_row` (`cells[]` com `id` `sNNNN.cK`, `start`/`end` na linha; cabeçalho traduz; linha delimitadora não),
  `admonition_open` (tipo no `prefix`; título traduz) / `admonition_close`, `code_block`, `html_comment`, `esm`
  (`import`/`export` até à linha em branco), `blank`, `raw` (`---`, blocos `<style>`, expressões `{…}`);
- **marcadores** `⟦P0⟧, ⟦P1⟧…` (numeração por unidade) substituem, no texto enviado ao tradutor, os tokens protegidos:
  code spans, comentários inline, destinos de ligação (`[texto](⟦P0⟧)`), referências `[ref]`, tags HTML/JSX, URLs,
  ids (`protected_tokens.ID_PATTERN`), siglas (`ACRONYM_PATTERN`), formas EN de entradas `do-not-translate` do registo
  e quebras de linha dentro do segmento (com o espaço final da linha e a indentação da seguinte). `protected[]` guarda
  o original de cada um; uma unidade só com marcadores (`| CIC-001 |`, `<div>`) fica `translate: false`, `reason: no-prose`;
- **glossário aplicável**: `terms` (entradas `in-record`/`coined`/`changed` cujas formas fonte ocorrem na prosa:
  `source → target` + variantes + `sense`), `do_not_translate` (nomes presentes em qualquer das línguas) e `pending`
  (as que bloqueiam unidades neste ficheiro, com razão e dono). Uma unidade cujo texto contém `pt`/`pt_variants` de uma
  entrada `pending` com `blocks_translation: true` fica `translate: false` com `blocked_by` (mesma segmentação por
  bloco e mesmas agulhas do `terms_lint.py pending-blocks`; o `prepare` cruza os dois e avisa se divergirem);
- `units` (ids de tudo o que o tradutor tem de devolver) e `stats`; o resumo do `prepare` dá ficheiros, unidades,
  palavras, marcadores, bloqueios por chave e entradas de glossário (`--json` para máquina).

O `prepare` é determinista (mesmo job byte a byte) e auto-verifica-se: os segmentos têm de reconstituir a fonte
verbatim, e a contagem de cabeçalhos/tabelas/blocos de código/admonitions tem de coincidir com `common.parse_markdown`
(o mesmo parser do `fingerprint.py`) — senão falha em vez de produzir um job errado. Um symlink na fonte produz um job
`{"kind": "symlink", "link_target": …}` sem nada a traduzir.

**Passo externo** — o tradutor (agente) segue `translation/prompts/translate-v2.md` (só `text` das unidades
`translate: true`; marcadores intactos e uma vez cada; glossário obrigatório; British English; registo do Manual) e
escreve `<out>/<caminho>.out.json` = `{"segments": [{"id", "text"}, …]}`.

**`assemble`** — reconstrói o ficheiro alvo a partir do esqueleto + traduções: repõe os protegidos (**falha** se um
marcador faltar, estiver duplicado, for desconhecido, ou se o texto trouxer uma quebra de linha literal; uma célula não
pode conter `|` sem escape); unidades bloqueadas ficam na língua fonte com `<!-- i18n:pending key=<chaves> -->`
imediatamente antes — na linha anterior para parágrafos, cabeçalhos e admonitions; indentado dentro da lista para itens
(para não partir a lista); antes da tabela (uma vez, com as chaves de todas as células bloqueadas) para células; na
primeira linha do corpo para `title`/`description`. Gera o frontmatter do contrato (`translation/README.md`): cópia
estrutural, `title`/`description` traduzidos (aspas mantidas se a fonte as tinha), bloco `translation:` com
`source_locale`, `source_path`, `source_sha256`, `source_commit`, `target_sha256` (hash do ficheiro sem o bloco, via
`common.strip_translation_block`), `engine` (`--engine`, obrigatório), `prompt_sha256`, `terms_sha256`, `glossary_keys`
(lista em fluxo, `[a, b]`) e `glossary_sha256` copiados do job, `translated_at` (`--translated-at` para testes), `stamped_at` (sempre agora; com
`--restamp` o `translated_at` do espelho existente mantém-se — re-estampa só de proveniência, texto reutilizado),
`reviewed_by: null`. Fonte sem frontmatter → mínimo (`id` efectivo + bloco). Recusa montar se a fonte mudou desde o
`prepare` (`--ignore-source-change` para forçar) e recusa um job sem `glossary_keys`/`glossary_sha256` (preparado antes
desta proveniência): re-correr o `prepare` (`--force`) dá o mesmo job com os mesmos ids, e o `.out.json` reutiliza-se —
é assim que se re-estampa um espelho legado. Corre `equivalence` (em memória) e o
`terms_lint spelling` sobre o resultado e **não grava se falhar** (`--allow-spelling-errors` deixa passar a ortografia);
com `--write` grava no caminho espelho e imprime o estado derivado por `sync_state` para o ficheiro; job de symlink com
`--write` cria o mesmo symlink relativo no espelho (nunca uma cópia).

**`check`** — `equivalence.py --path` + `terms_lint spelling` + `terms_lint consistency` sobre os ficheiros alvo já
existentes para o caminho dado; exit 1 se algum falhar. É o que o CI corre por partes.

Limites conhecidos: `sidebar_label` não é traduzido (o contrato só nomeia `title`/`description`; a lista vive em
`common.TRANSLATED_FRONTMATTER_KEYS`); valores `title`/`description` em escalar de bloco (`|`, `>`) ficam por traduzir
(`reason: block-scalar`); `consistency` não corre no `assemble` (só no `check`); um symlink no espelho aponta a uma
tradução cujo `source_path` é o alvo do link, o que o `sync_state.py` hoje assinala como aviso.

## Testes

```bash
python -m unittest discover -s translation/scripts/tests -p 'test_*.py'
```

`test_terms.py` verifica o importador contra o levantamento real (158 entradas, 8 `do-not-translate`, 19 `pending`,
desdobramento, idempotência com edição manual preservada, registo commitado igual ao gerado), o `validate`, o
`spelling` (fixture `tests/fixtures/terms/en-spelling.md`), o `pending-blocks` (fixture `pt-pending.md`), o
`export-pending` (determinista) e o `hash` (igual ao de `sync_state.py`).

`test_translate.py` verifica o `prepare` sobre a fixture `tests/fixtures/translate/source/04-pagina-traducao.md`
(esqueleto, marcadores, glossário, `blocked_by`, determinismo byte a byte, elegibilidade por `sync_state`,
`glossary_keys`/`glossary_sha256` — insensível a `notes`/`sense`/`counts` e a entradas não aplicadas, sensível a `en`,
`en_variants`, `state`, `blocks_translation` de uma entrada aplicada), o `assemble` com uma tradução mecânica (ficheiro
EN passa `equivalence`, comentários `pending` no sítio certo, frontmatter conforme o contrato com os dois campos do
glossário, `sync_state` deriva `partial`, `check` verde), as falhas sem gravar (marcador em falta, quebra de linha
literal, id desconhecido, ortografia, fonte alterada, job sem proveniência de glossário), fonte sem frontmatter →
mínimo, symlink → symlink, o `terms_lint` a ignorar ESM e `<style>`, e um smoke test sobre o capítulo piloto real
(segmentação coerente com o parser + montagem de identidade equivalente). `test_equivalence.py` cobre
`common.glossary_sha256` (canónico; chave ausente; variantes como conjunto) e a derivação de `stale-terms` pelo
glossário aplicado (`synced` quando só `notes` mudou ou mudou uma entrada não aplicada; `stale-terms` quando o `en`
de uma chave aplicada mudou ou a chave saiu do registo; precedência intacta; espelho legado → regra antiga + aviso).

## CI

`.github/workflows/i18n-equivalence.yml` corre, em PRs que toquem `manuals_src/**` ou `translation/**`:
testes → `terms_lint.py validate` → (se existirem ficheiros no espelho) `terms_lint.py spelling` e
`terms_lint.py consistency` sobre o espelho → `equivalence.py --all` → `sync_state.py --check` → build Docusaurus do
locale alvo (ou do locale fonte enquanto o alvo não estiver em `docusaurus.config.ts`). Os locales lêem-se de `env`
no topo do workflow.
