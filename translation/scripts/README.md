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
| `common.py` | hash de conteúdo do contrato (`content_sha256`), raiz do repo, frontmatter, mapeamento fonte↔espelho, iteração do corpus, parser markdown mínimo, slugger do Docusaurus |
| `protected_tokens.py` | lista única de prefixos de identificadores e siglas `do-not-translate` |
| `fingerprint.py` | impressão digital estrutural de uma página, independente da língua |
| `equivalence.py` | compara a impressão digital da fonte com a da tradução; falha em qualquer divergência não-textual |
| `sync_state.py` | deriva o estado de sincronismo por hashes e escreve/verifica `translation/state/sync-state.json` |
| `terms_import.py` | frente 3: semeia/actualiza `translation/terms/registry.yaml` a partir do levantamento do Curator (regras mecânicas do README do registo) |
| `terms_lint.py` | frente 3: `validate` (esquema), `spelling` (en-GB), `pending-blocks` (detector de blocos bloqueados), `consistency` (PT→EN por bloco), `export-pending` (fila para o hub), `hash` |
| `species3_candidates.py` | frente 3: varrimento de frequência da prosa PT → CSV de **candidatos** a espécie 3 (não entra no registo) |
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
o valor gravado no momento da tradução vive no frontmatter do espelho. Enquanto `translation/terms/registry.yaml`
não existir, `terms_sha256` é `null` e `stale-terms` nunca ocorre. Um ficheiro no espelho sem bloco `translation`
(feito à mão) gera aviso e exit 2.

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
  (`protected_tokens.py`), `en`/`en_variants` de entradas `do-not-translate` (sensível a maiúsculas) e de entradas
  `in-record`/`coined`/`changed` (insensível). Entradas `pending` **não** isentam nada — não têm autoridade sobre a
  prosa. As regras vivem num único dicionário `SPELLING_RULES` (-ise/-isation com excepções `size`/`prize`/`seize`/
  `capsize`; -yse; -our; -re; -ll-; `programme` só aviso; `licence` substantivo por contexto; `artefact` só em
  minúsculas — `Artifact`, `ArtifactRequirement`, `artifact_types` são identificadores; diversos). Palavras
  `CamelCase`/`ALLCAPS` não são prosa. Formas do próprio registo que violem a regra (ex.: `normalization`) saem como
  aviso «registry form is not en-GB» — o lint não briga com o registo; o Manual agent decide `changed`. Exit 1 com
  erros; `--fix` aplica só substituições inequívocas (erros de regras `fixable`, nunca avisos).
- `pending-blocks` — para cada bloco da fonte (parágrafo, item de lista, célula de tabela, cabeçalho, título de
  admonition, `title`/`description` do frontmatter; fora de código) que contenha, por palavra inteira sem distinção
  de maiúsculas e em NFC, `pt` ou `pt_variants` de uma entrada `pending` com `blocks_translation: true`, imprime
  `ficheiro:linha  chave  excerto`; resumo por ficheiro (só os bloqueados, salvo `--all-files`) e por chave. Exit 0
  (detector), salvo `--fail-on-block`. `--json` para o `translate.py`/`sync_state.py`.
- `consistency` — espécie 1/3: uma forma PT (`pt`/`pt_variants`) de entrada `in-record`/`coined`/`changed` presente num
  bloco da fonte tem de sair no bloco espelho com `en` ou uma de `en_variants` (alinhamento por bloco quando fonte
  e espelho têm o mesmo número de blocos; senão por ficheiro). Forma PT deixada no EN = aviso. Sem ficheiros EN:
  sucesso com aviso.
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

## Testes

```bash
python -m unittest discover -s translation/scripts/tests -p 'test_*.py'
```

`test_terms.py` verifica o importador contra o levantamento real (158 entradas, 8 `do-not-translate`, 19 `pending`,
desdobramento, idempotência com edição manual preservada, registo commitado igual ao gerado), o `validate`, o
`spelling` (fixture `tests/fixtures/terms/en-spelling.md`), o `pending-blocks` (fixture `pt-pending.md`), o
`export-pending` (determinista) e o `hash` (igual ao de `sync_state.py`).

## CI

`.github/workflows/i18n-equivalence.yml` corre, em PRs que toquem `manuals_src/**` ou `translation/**`:
testes → `terms_lint.py validate` → (se existirem ficheiros no espelho) `terms_lint.py spelling` e
`terms_lint.py consistency` sobre o espelho → `equivalence.py --all` → `sync_state.py --check` → build Docusaurus do
locale alvo (ou do locale fonte enquanto o alvo não estiver em `docusaurus.config.ts`). Os locales lêem-se de `env`
no topo do workflow.
