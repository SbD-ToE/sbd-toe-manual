#!/usr/bin/env python3
"""anchors_freeze.py — congelar as âncoras dos cabeçalhos do Manual como ids explícitos `{#slug}`.

Frente 2 da Fase 1 da inversão do canon (brief `.work-drafts/BRIEF-i18n-fase1-desenho-2026-09-24.md` §4).
Objectivo: cada cabeçalho markdown do corpus recebe um id explícito **igual à âncora que o Docusaurus
já deriva hoje** (incluindo os sufixos `-1`, `-2`… dos cabeçalhos repetidos na mesma página). Os ids
ficam na língua da fonte — são identificadores, não rótulos — e a tradução copia-os tal e qual.

Procedimento (cada passo é um sub-comando):

  1. ANTES  — build do site na língua fonte e fotografia das âncoras renderizadas:
        cd manuals_src && npm run build -- --locale pt
        anchors_freeze.py snapshot --build-dir manuals_src/build --locale pt --out anchors-before.json
  2. APLICAR — escrever ` {#slug}` em todos os cabeçalhos ainda sem id:
        anchors_freeze.py apply --docs-dir manuals_src/docs/sbd-toe
  3. DEPOIS — build de novo, nova fotografia, e o diff TEM de ser vazio:
        anchors_freeze.py snapshot --build-dir manuals_src/build --locale pt --out anchors-after.json
        anchors_freeze.py diff anchors-before.json anchors-after.json        # exit 1 se não vazio
  4. VERIFICAR (sem build) — o diff git só toca linhas de cabeçalho sob --docs-dir, nenhum bloco de
     código muda, os ids pré-existentes ficam iguais, contagens, ficheiros com sufixos:
        anchors_freeze.py verify --docs-dir manuals_src/docs/sbd-toe --base <commit-antes-do-apply>

Qualquer diferença no passo 3 é bug do procedimento, nunca do corpus: corrige-se o script e repete-se.

Motor de aplicação (`apply --engine`):

  * `own` (por omissão) — implementação própria que replica o plugin remark `headings` do
    `@docusaurus/mdx-loader` 3.10.1 (o que corre no build): um slugger por ficheiro
    (`@docusaurus/utils` `createSlugger` → github-slugger 1.5.0, `maintainCase: false`, regex portada
    em `github_slugger_regex.py` com prova de equivalência sobre todos os code points), cabeçalhos
    visitados por ordem do documento, **H1 incluído no registo do slugger**, ids explícitos
    **não** registados (o runtime devolve-os sem os passar pelo slugger), texto do cabeçalho =
    `mdast-util-to-string` (code spans, links, imagens, escapes, entidades, ênfase, notas de rodapé,
    directivas de texto), cercas de código ``` e ~~~ com qualquer indentação (o corpus é MDX: não há
    código indentado).
  * `docusaurus` — `npx docusaurus write-heading-ids <docs-dir>`. Não é o motor por omissão porque
    diverge do runtime em três pontos que fazem diferença neste corpus: ignora H1 sem os registar no
    slugger (um H2 com o mesmo texto do H1 ficaria sem `-1`), pré-regista os ids explícitos (um
    cabeçalho derivado que colida com um id explícito levaria `-1` a mais) e só reconhece cercas ```
    no início da linha (cercas indentadas em listas deixariam cabeçalhos de exemplo dentro de código
    com id).

O que NÃO recebe id, e porquê (em ambos os motores o resultado renderizado é o mesmo):

  * H1 — o tema (`@theme/Heading`) renderiza `<h1>` sem `id`, logo não há âncora a congelar; e o
    `contentTitle` do plugin de docs (`parseMarkdownContentTitle`) só sabe retirar `{#id}` ASCII
    (`[\\w-]+`), pelo que um id com acentos no H1 inicial de um doc sem `title:` no frontmatter fugiria
    para o `<title>` e para a sidebar. O slug do H1 é registado no slugger na mesma, como no runtime.
  * Cabeçalhos com texto vazio (`## `) — o slug é `''`, que não se pode escrever como `{#}`; o tema
    renderiza-os sem `id`.
  * Cabeçalhos com id explícito — ficam intactos, byte a byte.
  * Linhas dentro de blocos de código — nunca tocadas.

Só stdlib + PyYAML (PyYAML apenas para ler o frontmatter em `verify`). `--locale` no `snapshot`
permite correr a mesma prova sobre a árvore EN na Fase 2 (`--build-dir manuals_src/build --locale en`).
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import subprocess
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from github_slugger_regex import REMOVE_PATTERN  # noqa: E402

MARKDOWN_SUFFIXES = ('.md', '.mdx')

# --------------------------------------------------------------------------------------------------
# github-slugger 1.5.0 (BananaSlug)
# --------------------------------------------------------------------------------------------------

_REMOVE_RE = re.compile(REMOVE_PATTERN)


def github_slug(value: str, maintain_case: bool = False) -> str:
    """`BananaSlug.slug` estático: minúsculas, remove pontuação, espaço → hífen. Sem trim."""
    if not maintain_case:
        value = value.lower()
    return _REMOVE_RE.sub('', value).replace(' ', '-')


class Slugger:
    """Slugger com estado por ficheiro: repete → `-1`, `-2`… (algoritmo do github-slugger)."""

    def __init__(self) -> None:
        self.occurrences: dict[str, int] = {}

    def slug(self, value: str, maintain_case: bool = False) -> str:
        slug = github_slug(value, maintain_case)
        original = slug
        while slug in self.occurrences:
            self.occurrences[original] += 1
            slug = f'{original}-{self.occurrences[original]}'
        self.occurrences[slug] = 0
        return slug


# --------------------------------------------------------------------------------------------------
# Texto do cabeçalho ≈ mdast-util-to-string sobre o nó `heading` produzido pelo MDX
# --------------------------------------------------------------------------------------------------

_CODE_OPEN, _CODE_CLOSE = '', ''
_ESC_UNDERSCORE, _ESC_HYPHEN = '', ''
_ASCII_PUNCT = r'!"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~'


def _split_code_spans(s: str) -> list[tuple[str, str]]:
    """Divide em tokens ('code', valor) / ('text', bruto), com a regra CommonMark das runs de backticks."""
    tokens: list[tuple[str, str]] = []
    i, n = 0, len(s)
    buf = []
    while i < n:
        if s[i] != '`':
            buf.append(s[i])
            i += 1
            continue
        j = i
        while j < n and s[j] == '`':
            j += 1
        run = j - i
        k, found = j, -1
        while k < n:
            if s[k] == '`':
                m = k
                while m < n and s[m] == '`':
                    m += 1
                if m - k == run:
                    found = k
                    break
                k = m
            else:
                k += 1
        if found < 0:
            buf.append(s[i:j])
            i = j
            continue
        if buf:
            tokens.append(('text', ''.join(buf)))
            buf = []
        val = s[j:found].replace('\n', ' ')
        if len(val) >= 2 and val[0] == ' ' and val[-1] == ' ' and val.strip(' '):
            val = val[1:-1]
        tokens.append(('code', val))
        i = found + run
    if buf:
        tokens.append(('text', ''.join(buf)))
    return tokens


def _text_token_to_text(t: str) -> str:
    # escapes de barra invertida (só pontuação ASCII é escapável)
    t = t.replace('\\_', _ESC_UNDERSCORE).replace('\\-', _ESC_HYPHEN)
    t = re.sub(rf'\\([{_ASCII_PUNCT}])', r'\1', t)
    # entidades HTML/numéricas → carácter
    t = html.unescape(t)
    # elementos JSX/HTML inline sem filhos ou tags de abertura/fecho: contribuem só com os filhos
    t = re.sub(r'</?[A-Za-z][^<>]*>', '', t)
    # autolinks <https://…> → texto do URL
    t = re.sub(r'<((?:https?|mailto):[^<>\s]+)>', r'\1', t)
    # directivas de texto do remark-directive (`:nome`, `:nome[label]`): toString dá só o label
    t = re.sub(r'(?<![\w:]):[A-Za-z][\w-]*(?:\[([^\]]*)\])?(?:\{[^}]*\})?', lambda m: m.group(1) or '', t)
    # ênfase com underscore (não intra-palavra); `*` e `~` são removidos pelo slugger de qualquer modo
    t = re.sub(r'(?<![\w])_{1,3}(?=\S)', '', t)
    t = re.sub(r'(?<=\S)_{1,3}(?![\w])', '', t)
    return t


def heading_text(content: str) -> str:
    """Texto que o runtime passa ao slugger para o conteúdo (já sem `#` e sem `{#id}`) de um cabeçalho."""
    tokens = _split_code_spans(content)
    parts = []
    for kind, val in tokens:
        if kind == 'code':
            parts.append(_CODE_OPEN + val + _CODE_CLOSE)
        else:
            parts.append(_text_token_to_text(val))
    t = ''.join(parts)
    # notas de rodapé [^x] → '' ; imagens ![alt](src) → alt ; links [texto](url) / [texto][ref] → texto
    t = re.sub(r'\[\^[^\]]+\]', '', t)
    link_text = r'((?:[^\[\]]|\[[^\[\]]*\])*)'
    t = re.sub(r'!?\[' + link_text + r'\]\((?:[^()\s]|\([^()]*\))*(?:\s+"[^"]*")?\)', r'\1', t)
    t = re.sub(r'\[' + link_text + r'\]\[[^\]]*\]', r'\1', t)
    t = t.replace(_CODE_OPEN, '').replace(_CODE_CLOSE, '')
    t = t.replace(_ESC_UNDERSCORE, '_').replace(_ESC_HYPHEN, '-')
    return t


# --------------------------------------------------------------------------------------------------
# Leitura dos cabeçalhos de um ficheiro markdown/MDX
# --------------------------------------------------------------------------------------------------

_ATX_RE = re.compile(r'^(?P<indent>[ \t]{0,3})(?P<hashes>#{1,6})(?:(?P<sep>[ \t]+)(?P<rest>.*?))?[ \t]*$')
_FENCE_RE = re.compile(r'^[ \t]*(?P<fence>`{3,}|~{3,})(?P<info>.*)$')
_EXPLICIT_ID_RE = re.compile(r'\s*\{#(?P<id>(?:.(?!\{#|\}))*.)\}$')  # = parseMarkdownHeadingId (classic)
_MDX_COMMENT_ID_RE = re.compile(r'\s*\{/\*\s*#(?P<id>\S+)\s*\*/\}$')


def strip_closing_sequence(rest: str) -> str:
    """Retira a sequência de fecho `## Foo ##` (CommonMark 4.2) para o cálculo do texto."""
    m = re.match(r'^(.*?)(?:[ \t]+#+)?[ \t]*$', rest)
    return m.group(1) if m else rest


def parse_explicit_id(rest: str) -> str | None:
    m = _EXPLICIT_ID_RE.search(rest)
    if m:
        return m.group('id').strip()
    m = _MDX_COMMENT_ID_RE.search(rest)
    if m:
        return m.group('id').strip()
    return None


class Heading:
    __slots__ = ('lineno', 'level', 'rest', 'explicit_id', 'text', 'slug', 'line', 'setext')

    def __init__(self, lineno: int, level: int, rest: str, line: str, setext: bool = False) -> None:
        self.lineno = lineno
        self.level = level
        self.rest = rest
        self.line = line
        self.setext = setext
        self.explicit_id = parse_explicit_id(rest)
        self.text = None if self.explicit_id is not None else heading_text(rest if setext else strip_closing_sequence(rest))
        self.slug: str | None = None


_SETEXT_UNDERLINE_RE = re.compile(r'^ {0,3}(=+|-+)[ \t]*$')
_NOT_PARAGRAPH_RE = re.compile(r'^ {0,3}(?:#{1,6}(?:[ \t]|$)|>|\||<|:::|[-*+][ \t]|\d+[.)][ \t]|`{3,}|~{3,}|(?:[-*_][ \t]*){3,}$)')


def _setext_paragraph(lines: list[str], i: int) -> list[int] | None:
    """Se `lines[i]` é um sublinhado setext, devolve os índices das linhas do parágrafo que o precede."""
    if i == 0 or not _SETEXT_UNDERLINE_RE.match(lines[i].rstrip('\r')):
        return None
    j = i - 1
    para: list[int] = []
    while j >= 0:
        prev = lines[j].rstrip('\r')
        if not prev.strip() or _NOT_PARAGRAPH_RE.match(prev) or _SETEXT_UNDERLINE_RE.match(prev):
            break
        para.append(j)
        j -= 1
    if not para:
        return None
    return list(reversed(para))


def scan_headings(text: str) -> tuple[list[Heading], list[str]]:
    """Cabeçalhos fora de frontmatter e de cercas de código, com o slug que o runtime lhes dá.

    ATX (`#`…`######`) e setext (parágrafo + `===`/`---`): ambos registam o slug no slugger, por ordem,
    como no plugin remark. Só os ATX podem receber id (ver `rewrite_file_text`).
    Devolve também a lista das linhas dentro de blocos de código (para provar que não mudam).
    """
    lines = text.split('\n')
    headings: list[Heading] = []
    code_lines: list[str] = []
    slugger = Slugger()
    i = 0
    # frontmatter YAML — como o remark-frontmatter do MDX: abre com `---` na 1.ª linha e fecha na
    # PRIMEIRA linha que seja exactamente `---`. (Um fecho como `--------` não fecha: o runtime engole
    # tudo até ao próximo `---`, e o corpus tem 6 ficheiros assim; o scanner reproduz esse comportamento
    # de propósito, para que os ids escritos sejam os renderizados.)
    if lines and lines[0].rstrip('\r') == '---':
        for j in range(1, len(lines)):
            if lines[j].rstrip('\r') == '---':
                i = j + 1
                break
    fence_char, fence_len = None, 0
    while i < len(lines):
        line = lines[i].rstrip('\r')
        fm = _FENCE_RE.match(line)
        if fence_char is None:
            if fm:
                fence_char, fence_len = fm.group('fence')[0], len(fm.group('fence'))
                i += 1
                continue
            hm = _ATX_RE.match(line)
            if hm:
                rest = hm.group('rest') or ''
                h = Heading(i, len(hm.group('hashes')), rest, line)
                if h.explicit_id is None:
                    h.slug = slugger.slug(h.text)
                headings.append(h)
            else:
                para = _setext_paragraph(lines, i)
                if para and (not headings or headings[-1].lineno < para[0]):
                    rest = '\n'.join(lines[k].rstrip('\r').strip() for k in para)
                    level = 1 if line.strip().startswith('=') else 2
                    h = Heading(para[-1], level, rest, lines[para[-1]].rstrip('\r'), setext=True)
                    if h.explicit_id is None:
                        h.slug = slugger.slug(h.text)
                    headings.append(h)
        else:
            if fm and fm.group('fence')[0] == fence_char and len(fm.group('fence')) >= fence_len and not fm.group('info').strip():
                fence_char = None
            else:
                code_lines.append(line)
        i += 1
    return headings, code_lines


def rewrite_file_text(text: str) -> tuple[str, list[Heading], list[Heading]]:
    """Devolve (novo texto, cabeçalhos escritos, cabeçalhos saltados) sem tocar em mais nada."""
    headings, _ = scan_headings(text)
    lines = text.split('\n')
    written, skipped = [], []
    for h in headings:
        if h.explicit_id is not None:
            continue
        if h.level == 1 or h.slug == '' or h.setext:
            skipped.append(h)
            continue
        raw = lines[h.lineno]
        cr = '\r' if raw.endswith('\r') else ''
        lines[h.lineno] = raw + ' {#' + h.slug + '}' + cr  # never rstrip: trailing whitespace belongs to the source line
        written.append(h)
    return '\n'.join(lines), written, skipped


def iter_markdown_files(docs_dir: Path):
    """Ficheiros `.md`/`.mdx` regulares, por ordem. Symlinks são saltados: o alvo já é processado pelo
    seu próprio caminho (o corpus tem 1: `002-cross-check-normativo/dora/03-convergencia-nis2.md`)."""
    for p in sorted(docs_dir.rglob('*')):
        if p.is_symlink():
            continue
        if p.is_file() and p.suffix in MARKDOWN_SUFFIXES:
            yield p


# --------------------------------------------------------------------------------------------------
# snapshot — âncoras renderizadas no build
# --------------------------------------------------------------------------------------------------

class _HeadingCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.article_depth = 0
        self.in_title = False
        self.title = ''
        self.headings: list[list] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'article':
            self.article_depth += 1
        elif tag == 'title':
            self.in_title = True
        elif tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            cls = a.get('class') or ''
            if self.article_depth > 0 or 'anchor' in cls.split():
                self.headings.append([tag, a.get('id')])

    def handle_endtag(self, tag):
        if tag == 'article' and self.article_depth:
            self.article_depth -= 1
        elif tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data


def cmd_snapshot(args) -> int:
    build_dir = Path(args.build_dir)
    root = build_dir if args.locale == args.default_locale else build_dir / args.locale
    if not root.is_dir():
        print(f'build dir not found: {root}', file=sys.stderr)
        return 2
    skip = {s for s in (args.skip_subdirs or '').split(',') if s} if args.locale == args.default_locale else set()
    pages = {}
    for p in sorted(root.rglob('index.html')):
        rel = p.relative_to(root)
        if rel.parts and rel.parts[0] in skip:
            continue
        col = _HeadingCollector()
        col.feed(p.read_text('utf-8', errors='replace'))
        url = '/' + '/'.join(rel.parts[:-1]) + ('/' if len(rel.parts) > 1 else '')
        pages[url] = {'title': col.title, 'headings': col.headings}
    out = {'locale': args.locale, 'build_dir': str(build_dir), 'pages': pages,
           'totals': {'pages': len(pages), 'headings': sum(len(v['headings']) for v in pages.values()),
                      'ids': sum(1 for v in pages.values() for h in v['headings'] if h[1] is not None)}}
    Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + '\n', 'utf-8')
    print(f"snapshot {args.locale}: {out['totals']['pages']} pages, {out['totals']['headings']} headings, {out['totals']['ids']} ids → {args.out}")
    return 0


def cmd_diff(args) -> int:
    a = json.loads(Path(args.before).read_text('utf-8'))['pages']
    b = json.loads(Path(args.after).read_text('utf-8'))['pages']
    problems = 0
    for url in sorted(set(a) | set(b)):
        if url not in a:
            print(f'+ page only after: {url}'); problems += 1; continue
        if url not in b:
            print(f'- page only before: {url}'); problems += 1; continue
        if a[url]['title'] != b[url]['title']:
            print(f'~ title {url}: {a[url]["title"]!r} → {b[url]["title"]!r}'); problems += 1
        ha, hb = a[url]['headings'], b[url]['headings']
        if ha != hb:
            problems += 1
            print(f'~ headings {url}: before {len(ha)} after {len(hb)}')
            for i in range(max(len(ha), len(hb))):
                x = ha[i] if i < len(ha) else None
                y = hb[i] if i < len(hb) else None
                if x != y:
                    print(f'    [{i}] {x} → {y}')
    if problems:
        print(f'DIFF NOT EMPTY: {problems} page(s) differ')
        return 1
    print(f'diff empty: {len(a)} pages, {sum(len(v["headings"]) for v in a.values())} headings identical')
    return 0


# --------------------------------------------------------------------------------------------------
# apply
# --------------------------------------------------------------------------------------------------

def cmd_apply(args) -> int:
    docs_dir = Path(args.docs_dir)
    if args.engine == 'docusaurus':
        site_dir = docs_dir
        while site_dir != site_dir.parent and not (site_dir / 'package.json').exists():
            site_dir = site_dir.parent
        rel = docs_dir.resolve().relative_to(site_dir.resolve())
        # assinatura: docusaurus write-heading-ids [siteDir] [files...]
        cmd = ['npx', 'docusaurus', 'write-heading-ids', '.', str(rel)]
        print('$', ' '.join(cmd), f'(cwd {site_dir})')
        return subprocess.call(cmd, cwd=site_dir)
    n_files = n_written = n_skipped_h1 = n_skipped_empty = 0
    setext: list[str] = []
    for p in iter_markdown_files(docs_dir):
        raw = p.read_bytes()
        text = raw.decode('utf-8')
        new, written, skipped = rewrite_file_text(text)
        rel = p.relative_to(docs_dir).as_posix()
        for h in skipped:
            if h.setext:
                setext.append(f'{rel}:{h.lineno + 1}: {h.line[:70]!r} → id `{h.slug[:60]}…`' if len(h.slug) > 60 else f'{rel}:{h.lineno + 1}: {h.line[:70]!r} → id `{h.slug}`')
            elif h.level == 1:
                n_skipped_h1 += 1
            else:
                n_skipped_empty += 1
        if new != text:
            n_files += 1
            n_written += len(written)
            if not args.dry_run:
                p.write_bytes(new.encode('utf-8'))
    print(f'{"dry-run: " if args.dry_run else ""}{n_written} ids written in {n_files} files; '
          f'skipped {n_skipped_h1} H1 + {n_skipped_empty} empty + {len(setext)} setext headings (never written)')
    for s in setext:
        print('  setext:', s)
    return 0


# --------------------------------------------------------------------------------------------------
# verify — passo 4, sem build, contra um commit base
# --------------------------------------------------------------------------------------------------

def _git(root: Path, *args: str) -> str:
    # core.quotePath=false: caminhos com acentos vêm em UTF-8, não como "\303\247" entre aspas
    return subprocess.run(['git', '-C', str(root), '-c', 'core.quotePath=false', *args], check=True, capture_output=True, text=True).stdout


def _count_explicit(text: str) -> int:
    return sum(1 for h in scan_headings(text)[0] if h.explicit_id is not None)


def cmd_verify(args) -> int:
    docs_dir = Path(args.docs_dir).resolve()
    root = Path(_git(docs_dir, 'rev-parse', '--show-toplevel').strip())
    docs_rel = docs_dir.relative_to(root).as_posix()
    base = args.base
    ok = True
    rows: list[tuple[str, bool, str]] = []

    def check(name: str, cond: bool, evidence: str):
        nonlocal ok
        ok = ok and cond
        rows.append((name, cond, evidence))

    status = [l.split('\t') for l in _git(root, 'diff', '--name-status', base, '--').splitlines() if l]
    outside = [s for s in status if not s[-1].startswith(docs_rel + '/')]
    not_modified = [s for s in status if s[0][0] != 'M']
    changed = [s[-1] for s in status if s[0][0] == 'M' and s[-1].startswith(docs_rel + '/')]
    check('diff só sob docs-dir', not outside, f'{len(status)} caminhos no diff; fora de {docs_rel}/: {outside[:5]}')
    check('nenhum ficheiro renomeado/criado/apagado', not not_modified, f'{not_modified[:5]}')

    # linhas alteradas
    bad_lines: list[str] = []
    non_heading_pairs: list[str] = []
    code_changed: list[str] = []
    explicit_changed: list[str] = []
    ids_before = ids_after = 0
    added_ids: dict[str, list[str]] = {}
    for rel in changed:
        before = _git(root, 'show', f'{base}:{rel}')
        after = (root / rel).read_text('utf-8')
        bl, al = before.split('\n'), after.split('\n')
        if len(bl) != len(al):
            bad_lines.append(f'{rel}: número de linhas {len(bl)} → {len(al)}')
            continue
        file_added = []
        for x, y in zip(bl, al):
            if x == y:
                continue
            cr = '\r' if x.endswith('\r') else ''
            m = re.match(r'^[ \t]{0,3}#{2,6}[ \t]', x)
            m2 = re.fullmatch(re.escape(x) + r' \{#(?P<id>[^}]*)\}' + re.escape(cr), y)
            if not m or not m2:
                non_heading_pairs.append(f'{rel}: {x[:80]!r} → {y[:80]!r}')
            else:
                file_added.append(m2.group('id'))
        added_ids[rel] = file_added
        hb, cb = scan_headings(before)
        ha, ca = scan_headings(after)
        if cb != ca:
            code_changed.append(rel)
        eb = [(h.lineno, h.line) for h in hb if h.explicit_id is not None]
        ea = [(h.lineno, h.line) for h in ha if h.explicit_id is not None]
        if any(e not in ea for e in eb):
            explicit_changed.append(rel)
    check('ficheiros alterados têm o mesmo número de linhas', not bad_lines, f'{bad_lines[:5]}')
    check('cada linha alterada é um cabeçalho H2–H6 e só ganhou ` {#id}`', not non_heading_pairs, f'{len(non_heading_pairs)} excepções: {non_heading_pairs[:5]}')
    check('conteúdo dos blocos de código igual antes/depois', not code_changed, f'{code_changed[:5]}')
    check('ids explícitos pré-existentes intactos (mesma linha, mesmo texto)', not explicit_changed, f'{explicit_changed[:5]}')

    # contagens sobre todo o corpus
    files = list(iter_markdown_files(docs_dir))
    tracked = set(_git(root, 'ls-tree', '-r', '--name-only', base, '--', docs_rel).splitlines())
    h_total = h1 = empty = setext = explicit_after = without_id = 0
    suffix_files: dict[str, list[str]] = {}
    explicit_vs_derived: list[str] = []
    for p in files:
        rel = p.resolve().relative_to(root).as_posix()
        text = p.read_text('utf-8')
        hs, _ = scan_headings(text)
        h_total += len(hs)
        # caso CLI≠runtime: id explícito pré-existente (no base) textualmente igual a um slug derivado na
        # mesma página — o `write-heading-ids` daria `-1` ao derivado, o runtime não. Tem de ser 0 para os
        # dois motores coincidirem; com o motor `own` a prova de última instância é o diff do build.
        if rel in tracked:
            hb, _ = scan_headings(_git(root, 'show', f'{base}:{rel}'))
            pre = {h.explicit_id for h in hb if h.explicit_id is not None}
            derived = {h.slug for h in hb if h.explicit_id is None and h.slug}
            hit = sorted(pre & derived)
            if hit:
                explicit_vs_derived.append(f'{rel}: {hit}')
        for h in hs:
            if h.explicit_id is not None:
                explicit_after += 1
            elif h.setext:
                setext += 1
            elif h.level == 1:
                h1 += 1
            elif h.slug == '':
                empty += 1
            else:
                without_id += 1
        if rel in tracked:
            ids_before += _count_explicit(_git(root, 'show', f'{base}:{rel}'))
        ids = [h.explicit_id for h in hs if h.explicit_id is not None]
        idset = set(ids)
        sufs = sorted({i for i in ids if re.search(r'-\d+$', i) and re.sub(r'-\d+$', '', i) in idset and i in added_ids.get(rel, [])})
        if sufs:
            suffix_files[rel] = sufs
    ids_after = explicit_after
    check('todos os H2–H6 ATX não vazios têm id explícito', without_id == 0, f'{without_id} sem id')
    rows.append(('contagem `{#id}` antes → depois', True, f'{ids_before} → {ids_after} (cabeçalhos fora de código: {h_total}; H1 sem id: {h1}; vazios sem id: {empty}; setext sem id: {setext})'))
    check('nenhum id explícito pré-existente coincide com um slug derivado na mesma página (caso CLI≠runtime)', not explicit_vs_derived, f'{explicit_vs_derived[:5]}')
    symlinks = sorted(p.relative_to(root).as_posix() for p in docs_dir.rglob('*') if p.is_symlink())
    symlink_status = [s for s in status if s[-1] in symlinks]
    check('symlinks intactos (não alterados no diff; alvo alterado uma só vez pelo seu caminho)', not symlink_status, f'{len(symlinks)} symlink(s): {symlinks}; no diff: {symlink_status}')
    rows.append(('ficheiros tocados', True, f'{len(changed)} de {len(files)} regulares (+{len(symlinks)} symlink)'))
    rows.append(('ficheiros com sufixos -N gerados', True, f'{len(suffix_files)}'))

    print(f'verify --docs-dir {docs_rel} --base {base}')
    print('| verificação | resultado | evidência |')
    print('|---|---|---|')
    for name, cond, ev in rows:
        print(f'| {name} | {"OK" if cond else "FALHA"} | {ev} |')
    if suffix_files:
        print('\nSufixos gerados (cabeçalhos repetidos na mesma página):')
        for rel, sufs in sorted(suffix_files.items()):
            print(f'- `{rel}`: {", ".join("`" + s + "`" for s in sufs)}')
    if args.json:
        Path(args.json).write_text(json.dumps({'ok': ok, 'rows': rows, 'suffix_files': suffix_files, 'added_ids': added_ids}, ensure_ascii=False, indent=1) + '\n', 'utf-8')
    print('\nVERIFY', 'OK' if ok else 'FAILED')
    return 0 if ok else 1


# --------------------------------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)

    s = sub.add_parser('snapshot', help='fotografar {página → [(hN, id)]} a partir de build/**/index.html')
    s.add_argument('--build-dir', required=True)
    s.add_argument('--locale', default='pt', help='locale a fotografar (sub-pasta do build se não for o default)')
    s.add_argument('--default-locale', default='pt')
    s.add_argument('--skip-subdirs', default='en', help='sub-pastas de outros locales a ignorar quando se fotografa o default')
    s.add_argument('--out', required=True)
    s.set_defaults(fn=cmd_snapshot)

    d = sub.add_parser('diff', help='comparar duas fotografias; exit 1 se diferirem')
    d.add_argument('before')
    d.add_argument('after')
    d.set_defaults(fn=cmd_diff)

    a = sub.add_parser('apply', help='escrever {#slug} nos cabeçalhos sem id')
    a.add_argument('--docs-dir', required=True)
    a.add_argument('--engine', choices=['own', 'docusaurus'], default='own')
    a.add_argument('--dry-run', action='store_true')
    a.set_defaults(fn=cmd_apply)

    v = sub.add_parser('verify', help='passo 4: verificações sobre o diff git contra --base, sem build')
    v.add_argument('--docs-dir', required=True)
    v.add_argument('--base', default='HEAD', help='commit/ref antes do apply')
    v.add_argument('--json', help='escrever o resultado em JSON')
    v.set_defaults(fn=cmd_verify)

    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == '__main__':
    sys.exit(main())
