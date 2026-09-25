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

## Testes

```bash
python -m unittest discover -s translation/scripts/tests -p 'test_*.py'
```

## CI

`.github/workflows/i18n-equivalence.yml` corre, em PRs que toquem `manuals_src/**` ou `translation/**`:
testes → `equivalence.py --all` → `sync_state.py --check` → build Docusaurus do locale alvo (ou do locale fonte
enquanto o alvo não estiver em `docusaurus.config.ts`). Os locales lêem-se de `env` no topo do workflow.
