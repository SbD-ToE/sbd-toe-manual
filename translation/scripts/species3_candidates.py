#!/usr/bin/env python3
"""Frequency scan of the source-locale prose to surface species-3 candidates.

Species 3 is prose vocabulary (``translation/terms/README.md``): terms without
a paper anchor that must nevertheless be rendered consistently. This script
produces a **candidate list** for the Manual agent to review; nothing here is
written to the registry.

Prose is taken outside code, comments and structural front matter (the same
extraction as ``terms_lint.py``), and every protected token
(``protected_tokens.py``) and every registered form (``pt``, ``pt_variants``,
``en``, ``en_variants`` of any entry) is removed before counting. Words are
lower-cased and reduced to an approximate lemma by surface rules (plural
endings only: ``-ções`` -> ``-ção``, ``-ões`` -> ``-ão``, ``-ais`` -> ``-al``,
``-eis`` -> ``-el``, ``-res`` -> ``-r``, trailing ``-s`` after a vowel); no
external NLP. Unigrams need at least four letters; bigrams are two consecutive
content words, optionally joined by ``de/da/do/das/dos`` (``ciclo de vida``,
``nível de risco``). An embedded Portuguese stop-word list removes function
words and generic verbs.

Output: CSV ``termo_pt, docs, total, exemplo_ficheiro, exemplo_linha`` sorted
by document frequency, then total, then term; ``--top N`` keeps the first N.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common  # noqa: E402
import protected_tokens  # noqa: E402
import terms_lint  # noqa: E402

MIN_LETTERS = 4

STOPWORDS: Set[str] = set(
    """
    a à às ao aos as o os um uma uns umas de da do das dos dum duma em na no nas nos num numa por pela pelo pelas
    pelos para com sem sob sobre entre até desde após ante contra perante e ou nem mas porém contudo todavia
    entretanto logo portanto pois porque porquê como quando onde enquanto embora se não sim já ainda também só
    apenas mais menos muito muita muitos muitas pouco pouca poucos poucas tão tanto tanta tantos tantas bem mal
    aqui ali aí lá cá agora então depois antes sempre nunca jamais talvez quase mesmo mesma mesmos mesmas outro
    outra outros outras todo toda todos todas cada qualquer quaisquer algum alguma alguns algumas nenhum nenhuma
    vário vária vários várias certo certa certos certas tal tais que quem qual quais cujo cuja cujos cujas este
    esta estes estas esse essa esses essas aquele aquela aqueles aquelas isto isso aquilo eu tu ele ela nós vós
    eles elas me te se lhe lhes nos vos meu minha meus minhas teu tua teus tuas seu sua seus suas nosso nossa
    nossos nossas vosso vossa vossos vossas ser é são era eram foi foram será serão seria seriam seja sejam sendo
    sido fosse fossem for forem estar está estão estava estavam esteve estiveram estará estarão esteja estejam
    estando estado ter tem têm tinha tinham teve tiveram terá terão teria teriam tenha tenham tendo tido haver há
    havia houve haverá haja havendo fazer faz fazem fez fizeram fará farão faça façam fazendo feito feita feitos
    feitas poder pode podem podia podiam pôde puderam poderá poderão poderia poderiam possa possam podendo dever
    deve devem devia deviam deverá deverão deveria deveriam deva devam devendo devido ir vai vão foi ia iam irá
    irão vá vão indo ido dar dá dão deu dado dada dados dadas ver vê veem viu vendo visto vista vir vem vêm veio
    vindo ficar fica ficam ficou ficará fique fiquem ficando existir existe existem existia existiu existirá
    existindo permitir permite permitem permitiu permitido permitida incluir inclui incluem incluindo incluído
    incluída usar usa usam usado usada usados usadas utilizar utiliza utilizam utilizado utilizada utilizados
    utilizadas tornar torna tornam tornou tornando manter mantém mantêm mantido mantida garantir garante garantem
    garantido garantida definir define definem definido definida considerar considera consideram considerado
    considerada continuar continua continuam apresentar apresenta apresentam apresentado apresentada tratar
    trata tratam querer quer querem saber sabe sabem dizer diz dizem seguir segue seguem seguinte seguintes acima
    abaixo através durante mediante segundo conforme além aliás assim ainda etc forma formas modo modos maneira
    maneiras caso casos vez vezes exemplo exemplos parte partes coisa coisas facto factos ponto pontos geral
    gerais parte pode-se deve-se cerca aproximadamente nomeadamente respetivamente respectivamente sobretudo
    principalmente especialmente simplesmente diretamente directamente apenas anteriormente posteriormente
    frequentemente normalmente geralmente sempre nunca menos mais muito muitos pouco poucos primeiro primeira
    primeiros primeiras segundo segunda terceiro terceira último última últimos últimas novo nova novos novas
    grande grandes pequeno pequena pequenos pequenas maior maiores menor menores melhor melhores pior piores
    bom boa bons boas mau má maus más próprio própria próprios próprias determinado determinada determinados
    determinadas diferente diferentes igual iguais junto juntos possível possíveis necessário necessária
    necessários necessárias importante importantes relevante relevantes específico específica específicos
    específicas adequado adequada adequados adequadas suficiente suficientes total totais único única únicos
    únicas nenhum nenhuma ambos ambas onde aonde donde quanto quanta quantos quantas
    """.split()
)

_LEMMA_RULES: Tuple[Tuple[str, str, int], ...] = (
    # (suffix, replacement, minimum stem letters)
    ("ções", "ção", 3),
    ("sões", "são", 3),
    ("ões", "ão", 3),
    ("ães", "ão", 3),
    ("ais", "al", 3),
    ("éis", "el", 3),
    ("eis", "el", 3),
    ("óis", "ol", 3),
    ("res", "r", 4),
    ("zes", "z", 3),
    ("ses", "s", 4),
    ("ns", "m", 3),
)
_VOWELS = "aeiouáéíóúâêôãõ"
_WORD_RE = re.compile(r"(?<![\w-])([^\W\d_][^\W\d_'’-]*(?:-[^\W\d_]+)*)(?![\w-])")
_CONNECTORS = {"de", "da", "do", "das", "dos"}


def lemma(word: str) -> str:
    """Approximate lemma of a lower-case Portuguese surface form (plurals only)."""
    for suffix, replacement, min_stem in _LEMMA_RULES:
        if word.endswith(suffix) and len(word) - len(suffix) >= min_stem:
            return word[: -len(suffix)] + replacement
    if word.endswith("s") and len(word) > MIN_LETTERS and word[-2] in _VOWELS:
        return word[:-1]
    return word


def _blank(match: re.Match) -> str:
    return " " * len(match.group(0))


class Excluder:
    """Masks protected tokens and every registered form before counting."""

    def __init__(self, registry: Optional[dict]) -> None:
        forms: List[str] = []
        for entry in (registry or {}).get("terms", []):
            if not isinstance(entry, dict):
                continue
            for which in ("pt", "en"):
                forms.extend(terms_lint._forms(entry, which))
        self.patterns: List[re.Pattern] = [protected_tokens.ID_PATTERN, protected_tokens.ACRONYM_PATTERN]
        registered = terms_lint._word_regex(forms, ignore_case=True)
        if registered is not None:
            self.patterns.append(registered)

    def clean(self, text: str) -> str:
        for pattern in self.patterns:
            text = pattern.sub(_blank, text)
        return text


def tokens_of(text: str) -> List[Optional[str]]:
    """Lower-case lemmas in order; ``None`` marks a boundary (stop word, short
    word, identifier) so bigrams never span one."""
    out: List[Optional[str]] = []
    for match in _WORD_RE.finditer(text):
        surface = match.group(1)
        if any(ch.isupper() for ch in surface[1:]):  # CamelCase / ALLCAPS -> identifier
            out.append(None)
            continue
        word = common.nfc(surface.lower())
        if word in _CONNECTORS:
            out.append(word)
            continue
        if len(word.replace("-", "")) < MIN_LETTERS or word in STOPWORDS:
            out.append(None)
            continue
        out.append(lemma(word))
    return out


def ngrams_of(tokens: List[Optional[str]]) -> Iterable[str]:
    """Unigrams, bigrams and ``X de Y`` trigrams over content tokens."""
    n = len(tokens)
    for i, tok in enumerate(tokens):
        if tok is None or tok in _CONNECTORS:
            continue
        yield tok
        if i + 1 < n and tokens[i + 1] is not None and tokens[i + 1] not in _CONNECTORS:
            yield f"{tok} {tokens[i + 1]}"
        if i + 2 < n and tokens[i + 1] in _CONNECTORS and tokens[i + 2] is not None and tokens[i + 2] not in _CONNECTORS:
            yield f"{tok} {tokens[i + 1]} {tokens[i + 2]}"


def scan(docs_dir: Path, excluder: Excluder, root: Optional[Path]) -> Tuple[Counter, Counter, Dict[str, Tuple[str, int]]]:
    total: Counter = Counter()
    docs: Counter = Counter()
    example: Dict[str, Tuple[str, int]] = {}
    for rel in common.iter_corpus(docs_dir):
        path = common.source_path(rel, docs_dir)
        shown = common.nfc(rel)
        lines, _blocks = terms_lint.extract_prose(common.read_text(path), where=shown)
        seen_here: Set[str] = set()
        for prose in lines:
            cleaned = excluder.clean(prose.text)
            for gram in ngrams_of(tokens_of(cleaned)):
                total[gram] += 1
                if gram not in seen_here:
                    seen_here.add(gram)
                    docs[gram] += 1
                if gram not in example:
                    example[gram] = (shown, prose.line)
    return total, docs, example


def rows_for(total: Counter, docs: Counter, example: Dict[str, Tuple[str, int]], top: int, min_docs: int) -> List[List]:
    rows = []
    for gram in total:
        if docs[gram] < min_docs:
            continue
        rows.append([gram, docs[gram], total[gram], example[gram][0], example[gram][1]])
    rows.sort(key=lambda r: (-r[1], -r[2], r[0]))
    return rows[:top] if top else rows


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--docs-dir", type=Path, default=None, help="source corpus root (default: <repo>/manuals_src/docs/sbd-toe)")
    parser.add_argument("--registry", type=Path, default=None, help=f"terms registry whose forms are excluded (default: <repo>/{common.TERMS_REGISTRY_RELPATH} if present)")
    parser.add_argument("--out", type=Path, default=None, help="CSV output (default: stdout)")
    parser.add_argument("--top", type=int, default=300, help="keep the N most frequent candidates (0 = all)")
    parser.add_argument("--min-docs", type=int, default=2, help="minimum document frequency")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        root: Optional[Path] = common.repo_root()
    except common.TranslationToolError:
        root = None
    docs_dir = args.docs_dir or (common.default_docs_dir(root) if root else None)
    if docs_dir is None:
        print("error: --docs-dir is required (repository root not found)", file=sys.stderr)
        return 2
    registry_path = args.registry or ((root / common.TERMS_REGISTRY_RELPATH) if root else None)
    registry = terms_lint.load_registry(registry_path) if registry_path and registry_path.is_file() else None
    excluder = Excluder(registry)
    total, docs, example = scan(docs_dir, excluder, root)
    rows = rows_for(total, docs, example, args.top, args.min_docs)
    header = ["termo_pt", "docs", "total", "exemplo_ficheiro", "exemplo_linha"]
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, "w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle, lineterminator="\n")
            writer.writerow(header)
            writer.writerows(rows)
        print(f"species3-candidates: {len(rows)} candidate(s) written to {args.out} (registry forms excluded: {'yes' if registry else 'no'})")
    else:
        writer = csv.writer(sys.stdout, lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)
    return 0


if __name__ == "__main__":
    sys.exit(main())
