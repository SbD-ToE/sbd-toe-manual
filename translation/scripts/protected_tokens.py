"""Protected (``do-not-translate``) token patterns.

This is the single place where the identifier prefixes and the acronyms that
must survive translation verbatim are declared. ``fingerprint.py`` counts their
occurrences; the terms registry (front 3) is expected to reuse these lists.

Identifiers are ids, not English (README rule 4): ``ACO-TMR-008``, ``CIC-011``,
``EX-REQ-001`` … Acronyms are matched case-sensitively as whole words.
"""

from __future__ import annotations

import re
from collections import Counter
from typing import Dict, Iterable, Tuple

# Identifier families: prefix followed by ``-`` and a suffix that starts with an
# upper-case letter or digit (``ACO-TSV``, ``ACO-IVF-008``, ``CIC-K02``).
ID_PREFIXES: Tuple[str, ...] = (
    "ACO",
    "ACC",
    "ACP",
    "ACM",
    "CIC",
    "ASC",
    "EX",
    "VAL",
    "ACA",
    "ACR",
    "MP",  # MacroProcess instance ids MP-01..05 (lead, 2026-09-25)
    # requirement-domain ids of the base catalogue (chapter 02): AUT-001, LOG-003, SEC-L2-AUT-MFA …
    "AUT", "LOG", "SES", "FIL", "ERR", "CFG", "ENC", "PRI", "API", "INT", "REQ", "DST", "IDE", "SEC", "GOV", "ARC", "DEP", "MT",
)

# Acronyms and fixed spellings that are never translated.
ACRONYMS: Tuple[str, ...] = (
    "ASVS",
    "SSDF",
    "SLSA",
    "SBOM",
    "SCA",
    "SAST",
    "DAST",
    "IaC",
    "CI/CD",
    "MCP",
    "OWASP",
    "CWE",
    "CAPEC",
    "NIST",
)

ID_PATTERN = re.compile(
    r"(?<![A-Za-z0-9_-])(?:" + "|".join(ID_PREFIXES) + r")-[A-Z0-9][A-Za-z0-9_-]*[A-Za-z0-9]|"
    r"(?<![A-Za-z0-9_-])(?:" + "|".join(ID_PREFIXES) + r")-[A-Z0-9](?![A-Za-z0-9_-])"
)

ACRONYM_PATTERN = re.compile(
    r"(?<![A-Za-z0-9])(?:" + "|".join(re.escape(a) for a in sorted(ACRONYMS, key=len, reverse=True)) + r")(?![A-Za-z0-9])"
)


def find_protected_tokens(text: str) -> Counter:
    """Multiset of protected tokens occurring in ``text``."""
    found: Counter = Counter()
    for match in ID_PATTERN.finditer(text):
        found[match.group(0)] += 1
    for match in ACRONYM_PATTERN.finditer(text):
        found[match.group(0)] += 1
    return found


def count_protected_tokens(lines: Iterable[str]) -> Dict[str, int]:
    """Sorted mapping token -> occurrences over an iterable of prose lines."""
    total: Counter = Counter()
    for line in lines:
        total.update(find_protected_tokens(line))
    return dict(sorted(total.items()))
