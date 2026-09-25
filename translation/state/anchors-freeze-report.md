# Relatório de prova — âncoras congeladas (frente 2, Fase 1 i18n)

**Data:** 2026-09-25
**Ramo:** `wt/i18n-anchors` a partir de `feat/i18n-en-phase1` @ `7521f679` (commit base; corpus = esse commit)
**Script:** `translation/scripts/anchors_freeze.py` (+ `github_slugger_regex.py`, gerado)
**Motor aplicado:** `own` (implementação própria que replica o plugin remark `headings` do `@docusaurus/mdx-loader` 3.10.1)
**Docusaurus:** 3.10.1 · github-slugger 1.5.0 · Node v25.8.2 · Python 3.10

## Resultado em uma linha

O diff entre as âncoras renderizadas antes e depois é **vazio**: 1 121 páginas, 7 476 elementos `h1`–`h6` (com o `id` de cada um e o `<title>` de cada página) idênticos. 4 272 cabeçalhos H2–H6 receberam `{#slug}` igual ao id que já renderizavam; 403 ficheiros tocados; nenhuma linha que não seja um cabeçalho mudou.

## Contagens

| medida | antes | depois |
|---|---:|---:|
| ficheiros `.md`/`.mdx` em `manuals_src/docs/sbd-toe` | 412 regulares + 1 symlink | idem (nenhum renomeado/criado/apagado) |
| cabeçalhos fora de blocos de código (ATX + setext) | 4 761 | 4 761 |
| cabeçalhos com `{#id}` explícito | 87 | **4 359** (= 87 + 4 272) |
| H1 (sem id, ver §Decisões) | 398 | 398 |
| cabeçalhos com texto vazio (`## `) | 1 | 1 (sem id) |
| cabeçalhos setext (parágrafo + `---`) | 3 | 3 (sem id) |
| páginas no build PT · `h1`–`h6` no `<article>` · com `id` | 1 121 · 7 476 · 4 439 | 1 121 · 7 476 · 4 439 |
| tempo de build (`npm run build -- --locale pt`) | 112 s | 64 s (cache do webpack já quente) |

`git diff --stat HEAD`: **403 files changed, 4 272 insertions(+), 4 272 deletions(-)** — cada inserção é a mesma linha com ` {#slug}` no fim.

## Procedimento executado (brief §4)

1. `npm ci || npm install` (caiu em `npm install`, 15 s) → `npm run build -- --locale pt` (112 s, 0 warnings/errors) → `anchors_freeze.py snapshot --build-dir manuals_src/build --locale pt --out anchors-before.json`.
2. `anchors_freeze.py apply --docs-dir manuals_src/docs/sbd-toe` (motor `own`): 4 272 ids em 403 ficheiros.
3. `npm run build -- --locale pt` (64 s, 0 warnings/errors) → `snapshot … --out anchors-after.json` → `anchors_freeze.py diff anchors-before.json anchors-after.json` → **`diff empty: 1121 pages, 7476 headings identical`, exit 0** (à primeira; nenhuma discrepância no build).
4. `anchors_freeze.py verify --docs-dir manuals_src/docs/sbd-toe --base 7521f679` → **VERIFY OK** (tabela abaixo).
5. Idempotência: `apply --dry-run` sobre o corpus já aplicado → 0 ids; `rewrite(HEAD) == disco` para os 403 ficheiros.

Os JSON de snapshot não foram commitados (ficaram no scratch da sessão).

## Verificações do passo 4 (saída do `verify`)

| verificação | resultado | evidência |
|---|---|---|
| diff só sob `manuals_src/docs/sbd-toe/` | OK | 403 caminhos no diff; fora: nenhum |
| nenhum ficheiro renomeado/criado/apagado | OK | só estados `M` |
| ficheiros alterados têm o mesmo número de linhas | OK | — |
| cada linha alterada é um cabeçalho H2–H6 e só ganhou ` {#id}` (`linha_antes.rstrip() + " {#id}" == linha_depois`) | OK | 0 excepções em 4 272 pares |
| conteúdo dos blocos de código igual antes/depois (parser de cercas, não grep) | OK | 0 ficheiros com diferença |
| 87 ids explícitos pré-existentes intactos (mesma linha, mesmo texto) | OK | — |
| todos os H2–H6 ATX não vazios têm id explícito | OK | 0 sem id |
| contagem `{#id}` antes → depois | OK | 87 → 4 359 |
| nenhum id explícito pré-existente coincide com um slug derivado na mesma página (caso CLI ≠ runtime, aviso da frente 4+5) | OK | 0 páginas |
| symlink intacto; alvo alterado uma só vez pelo seu caminho | OK | `002-cross-check-normativo/dora/03-convergencia-nis2.md → ../nis2/03-convergencia-dora.md` continua symlink (`120000`) e não aparece no diff |
| ficheiros tocados | — | 403 de 412 regulares |
| ficheiros com sufixos `-N` gerados | — | 7 (lista abaixo) |

Confirmação equivalente com `git diff -U0 HEAD -- manuals_src/docs/sbd-toe | grep '^[-+]' | grep -v '^[-+][-+]' | grep -v '^[-+] *#'` → vazio.

## Os ficheiros com cabeçalhos repetidos na mesma página (sufixos gerados)

7 ficheiros / 7 páginas com ids `-N` cujo id base existe na mesma página (contagem do build, igual antes e depois):

| ficheiro | ids com sufixo | exemplos |
|---|---:|---|
| `010-sbd-manual/00-fundamentos/macro-processos.md` | 57 | `finalidade-e-invariante-1..4`, `âmbito-1..4`, `gatilhos-1..4`, `referências-cruzadas-1..5` |
| `010-sbd-manual/07-cicd-seguro/addon/10-riscos-processo-cicd.md` | 20 | `descrição-1..4`, `como-surge-1..4`, `impacto-1..4`, `mitigações-prescritas-1..4` |
| `020-assets/mcp/10-troubleshooting-faq.md` | 12 | `solução-1..7`, `causa-1..3`, `causas-1`, `diagnóstico-1` |
| `010-sbd-manual/04-arquitetura-segura/addon/04-diagramas-referencia.md` | 8 | `-descrição-1..2`, `️-diagrama-sugerido-1..2`, `-ameaças-mitigadas-1..2` |
| `002-cross-check-normativo/exemplo-playbook/02-exemplo-kpis-targets.md` | 5 | `contexto-1..3`, `kpis-e-targets-1..2` |
| `010-sbd-manual/06-desenvolvimento-seguro/addon/10-genia-e-seguranca.md` | 2 | `-princípios-1`, `-onde-aterra-no-resto-do-manual-1` |
| `010-sbd-manual/10-testes-seguranca/addon/10-evidencia-reprodutibilidade.md` | 1 | `prescrição-1` |

O brief contava «107 em 8 ficheiros»; o 8.º (`002-cross-check-normativo/exemplo-playbook/01-exemplo-toolchain-options.md`) tem cabeçalhos *numerados* («Opção 1», «Opção 2»…) que uma heurística de «retirar `-N`» junta, mas não são repetidos — o build não lhes dá sufixo. 157 cabeçalhos partilham base de slug com outro na mesma página (contagem por membros, não por excedentes).

## Decisões e desvios ao brief (todos com efeito nulo nas âncoras renderizadas)

1. **Motor próprio em vez de `npx docusaurus write-heading-ids`.** Verificado no código (`@docusaurus/utils/lib/markdownHeadingIdUtils.js` vs `@docusaurus/mdx-loader/lib/remark/headings/index.js`) e confirmado por triangulação — corri o CLI numa cópia scratch do corpus original e comparei com a saída do motor próprio: **7 ficheiros / 28 linhas diferem, e em todos os casos o build dá razão ao motor próprio**:
   - o CLI só reconhece cercas ``` no início da linha (`line.startsWith('```')`, um toggle), sem indentação nem regra de comprimento/info-string. Em `13-formacao-onboarding/addon/13-guia-preparacao-sandbox.md` um bloco ```` ```markdown ```` contém cercas indentadas (`   ```bash`); pela regra CommonMark (que o MDX segue) a cerca indentada sem info-string fecha o bloco exterior. O CLI teria injectado `{#…}` em 4 linhas **dentro de código** (`## 🎓 Integration com Cap. 13…`, `## 🏁 Checklist…`, …) e deixado **sem id 4 cabeçalhos reais** (`### Exercícios`, `### Pedir Ajuda`, `### Logs de Atividade`, `### Deadline`) que o build renderiza com id;
   - o CLI teria escrito `## {#}` no cabeçalho vazio de `12-monitorizacao-operacoes/intro.md` (o build renderiza-o sem id);
   - em 5 ficheiros com o frontmatter «fechado» por uma linha de 80+ hífens (ver §Achados), o CLI teria posto `{#-objetivo}` num cabeçalho que o runtime não renderiza (está dentro do frontmatter, para o `remark-frontmatter`);
   - diferenças de algoritmo que **não** se manifestaram neste corpus (0 casos, verificados): o CLI pré-regista os ids explícitos no slugger (o runtime não) e ignora H1 sem registar o seu slug (o runtime regista).
   O `apply --engine docusaurus` continua disponível no script para comparação.
2. **H1 não recebe `{#id}`** (398 cabeçalhos; o brief dizia «todos os cabeçalhos», ≈ 4 908). Razões: (a) o tema (`@theme/Heading`) renderiza `<h1>` **sem `id`** — não há âncora de H1 para congelar, e o `write-heading-ids` do próprio Docusaurus também os salta («we don't create anchor links for those»); (b) o `contentTitle` do plugin de docs (`parseMarkdownContentTitle`) só sabe retirar `{#id}` ASCII (`[\w-]+`): um id com acentos no H1 inicial dos **46 docs sem `title:` no frontmatter** (todos com H1 inicial, 45 com acentos) fugiria para o `<title>`, breadcrumbs e sidebar. O slug do H1 é registado no slugger na mesma (como no runtime), por isso um H2 com o texto do H1 leva `-1` correctamente. **Implicação para a Fase 2:** o H1 EN deriva o seu próprio slug; o `equivalence.py` (frente 4) deve comparar ids explícitos/H2–H6, não o H1. Se o lead quiser H1 congelado, o caminho é dar `title:` aos 46 docs primeiro (fora do âmbito desta frente).
3. **1 cabeçalho vazio** (`## ` em `010-sbd-manual/12-monitorizacao-operacoes/intro.md:23`) fica sem id: o slug é `''`, inexprimível como `{#}`; renderiza `<h2>` sem id.
4. **3 cabeçalhos setext** (parágrafo seguido de `---`, provavelmente acidentais) ficam sem id porque não são linhas `#`: `02-requisitos-seguranca/addon/01-catalogo-requisitos.md:60`, `09-containers-imagens/aplicacao-lifecycle.md:1261`, `13-formacao-onboarding/aplicacao-lifecycle.md:446`. O runtime dá-lhes ids longuíssimos (o parágrafo inteiro); o scanner regista-os no slugger para manter a ordem dos sufixos. Candidatos a correcção editorial (pôr uma linha em branco antes do `---`), fora do âmbito.
5. **Symlink**: `dora/03-convergencia-nis2.md` é um symlink git para `nis2/03-convergencia-dora.md`; o script salta symlinks (o alvo é processado pelo seu caminho, uma só vez) e o `verify` confirma que o symlink não entra no diff. Explica o «413» do brief vs 412 ficheiros regulares.
6. Não corri `--overwrite` nem `--maintain-case`; os 87 ids existentes ficaram byte a byte (incluindo `{#pilares-de-governação}` com acento e os 8 ids explícitos em H1 do `tldr.md`, que o tema também não renderiza).

## Achados sobre o corpus (fora do âmbito; para o Manual agent)

- **6 ficheiros com frontmatter fechado por uma linha de 88 hífens** (`010-sbd-manual/08-iac-infraestrutura/addon/03-governanca-modulos.md`, `04-principios-sbd-iac.md`, `05-exemplos-praticas-boas.md`, `06-controle-enforcement.md`, `010-sbd-manual/09-containers-imagens/addon/08-kubernetes-execucao.md`, `09-risco-processo-imagens.md`). O `gray-matter` (metadados) aceita esse fecho, mas o `remark-frontmatter` do MDX exige `---` exacto e engole tudo até ao primeiro `---` seguinte — nestes ficheiros o H1, a secção «🌟 Objetivo» e o parágrafo de abertura **não são renderizados** (verificado no HTML: 0 ocorrências de «Objetivo» na página `governanca-modulos`). O script reproduz este comportamento de propósito; o defeito é editorial (trocar a linha de hífens por `---`).
- Ids que começam por `-` ou por U+FE0F (`-o-que-cobre-tecnicamente`, `️-como-aplicar-na-prática`): consequência de emoji no início do cabeçalho (o github-slugger remove o emoji mas mantém o variation selector U+FE0F). São as âncoras actuais; ficaram congeladas tal e qual, como decidido.

## Prova do slugger portado

`github_slugger_regex.py` é gerado a partir de `node_modules/github-slugger/regex.js` (1.5.0), convertendo pares de surrogates em code points. Prova: para cada um dos 1 114 112 code points (excluindo surrogates), `s.replace(regex,'') === ''` em Node e `re.sub(PATTERN,'',s) == ''` em Python coincidem — 977 500 removidos em ambos, diferença simétrica vazia. Texto do cabeçalho ≈ `mdast-util-to-string` (code spans, links, imagens, escapes, entidades, ênfase `_`, notas de rodapé, directivas de texto); a prova de última instância é o diff do build, vazio.

## Como repetir (Fase 2, árvore EN)

```
cd manuals_src && npm run build
python3 translation/scripts/anchors_freeze.py snapshot --build-dir manuals_src/build --locale en --out before.json
python3 translation/scripts/anchors_freeze.py apply --docs-dir manuals_src/i18n/en/docusaurus-plugin-content-docs/current
cd manuals_src && npm run build
python3 translation/scripts/anchors_freeze.py snapshot --build-dir manuals_src/build --locale en --out after.json
python3 translation/scripts/anchors_freeze.py diff before.json after.json
python3 translation/scripts/anchors_freeze.py verify --docs-dir manuals_src/i18n/en/docusaurus-plugin-content-docs/current --base <sha>
```
(Na Fase 1 a tradução copia os `{#id}` PT; o `apply` sobre EN só faria falta se um ficheiro EN chegasse sem ids.)
