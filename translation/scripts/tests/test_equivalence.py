"""Tests for the extraction-equivalence test and the sync-state derivation.

Run with::

    python -m unittest discover -s translation/scripts/tests -p 'test_*.py'
"""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))

import common  # noqa: E402
import equivalence  # noqa: E402
import fingerprint  # noqa: E402
import sync_state  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"
EQUIV_SOURCE = FIXTURES / "equivalent" / "source" / "03-pagina-exemplo.md"
EQUIV_TARGET = FIXTURES / "equivalent" / "target" / "03-pagina-exemplo.md"
NOFM_SOURCE = FIXTURES / "no-frontmatter" / "source" / "25-rastreabilidade.md"
NOFM_TARGET = FIXTURES / "no-frontmatter" / "target" / "25-rastreabilidade.md"
DIVERGENT = FIXTURES / "divergent"


def dimensions(divergences):
    return sorted({d["dimension"] for d in divergences})


class HashingTests(unittest.TestCase):
    def test_normalisation_is_idempotent_and_strips_noise(self):
        raw = "﻿a \r\nb\t\r\n\r\n\r\n"
        self.assertEqual(common.normalise_text(raw), "a\nb\n")
        self.assertEqual(common.content_sha256(raw), common.content_sha256("a\nb\n"))
        self.assertEqual(common.content_sha256(""), common.content_sha256("\n\n"))

    def test_strip_translation_block_only_removes_that_mapping(self):
        text = common.read_text(EQUIV_TARGET)
        stripped = common.strip_translation_block(text)
        self.assertNotIn("translation:", stripped)
        self.assertNotIn("source_sha256", stripped)
        self.assertIn("id: pagina-exemplo", stripped)
        self.assertIn("tags: [exemplo, ci-cd]", stripped)
        self.assertIn("# Example page", stripped)
        self.assertEqual(common.strip_translation_block(common.read_text(EQUIV_SOURCE)), common.read_text(EQUIV_SOURCE))


class SluggerTests(unittest.TestCase):
    def test_github_slugger_behaviour(self):
        self.assertEqual(common.github_slug("Hello World!"), "hello-world")
        self.assertEqual(common.github_slug("Segurança — Requisitos"), "segurança--requisitos")
        self.assertEqual(common.github_slug("🧠 Filosofia"), "-filosofia")
        self.assertEqual(common.github_slug("a_b c²"), "a_b-c")
        s = common.Slugger()
        self.assertEqual([s.slug("Intro"), s.slug("Intro"), s.slug("Intro")], ["intro", "intro-1", "intro-2"])

    def test_heading_id_parsing(self):
        self.assertEqual(common.parse_heading_id("Título {#meu-id}"), ("Título", "meu-id"))
        self.assertEqual(common.parse_heading_id("Título \\{#meu-id}"), ("Título", "meu-id"))
        self.assertEqual(common.parse_heading_id("Sem id"), ("Sem id", None))

    def test_runtime_vs_cli_modes(self):
        text = "# T\n\n## Intro {#intro}\n\n## Intro\n"
        runtime = common.parse_markdown(text)
        common.assign_heading_ids(runtime, "runtime")
        cli = common.parse_markdown(text)
        common.assign_heading_ids(cli, "cli")
        self.assertEqual([h.id for h in runtime.headings], ["t", "intro", "intro"])
        self.assertEqual([h.id for h in cli.headings], ["t", "intro", "intro-1"])


class ParserTests(unittest.TestCase):
    def test_structure_of_fixture(self):
        fp = fingerprint.fingerprint_file(EQUIV_SOURCE, "03-pagina-exemplo.md")
        self.assertEqual(fp["frontmatter"]["id"], "pagina-exemplo")
        self.assertEqual(fp["frontmatter"]["sidebar_position"], 3)
        self.assertEqual(fp["frontmatter"]["keys"], ["id", "sidebar_position", "tags"])
        self.assertEqual([(h["level"], h["id"], h["explicit"]) for h in fp["headings"]][:3], [(1, "página-de-exemplo", False), (2, "objectivo", True), (2, "tabela", True)])
        self.assertEqual(len(fp["tables"]), 1)
        self.assertEqual(fp["tables"][0]["columns"], 3)
        self.assertEqual(fp["tables"][0]["rows"], 2)
        self.assertEqual(fp["tables"][0]["alignments"], ["left", "none", "right"])
        self.assertEqual([c["lang"] for c in fp["code_blocks"]], ["yaml"])
        self.assertEqual([a["type"] for a in fp["admonitions"]], ["userstory", "note"])
        self.assertEqual([(l["ordered"], l["items"], l["total_items"], l["max_depth"]) for l in fp["lists"]], [(False, 3, 4, 2), (True, 2, 2, 1)])
        self.assertEqual(sorted(fp["internal_links"]), ["#tabela", "/sbd-toe/sbd-manual/cicd-seguro/intro"])
        self.assertEqual(len(fp["protected_tokens"]["CIC-001"]), 3)  # description + prose + table
        self.assertEqual(len(fp["protected_tokens"]["CI/CD"]), 2)
        self.assertEqual(fp["html_comments"], 1)
        self.assertEqual(fp["pending_markers"], 0)

    def test_gray_matter_style_long_closing_delimiter(self):
        text = "---\nid: x\n---------\n\n# T\n"
        fm, body, start = common.parse_frontmatter(text)
        self.assertEqual(fm, {"id": "x"})
        self.assertTrue(body.startswith("------"))
        self.assertEqual(start, 3)

    def test_no_frontmatter_effective_id(self):
        fp = fingerprint.fingerprint_file(NOFM_SOURCE, "010-sbd-manual/00-fundamentos/canon/25-rastreabilidade.md")
        self.assertFalse(fp["frontmatter"]["present"])
        self.assertEqual(fp["frontmatter"]["id"], "rastreabilidade")
        self.assertEqual(common.strip_number_prefix("7.0-foo"), "7.0-foo")
        self.assertEqual(common.strip_number_prefix("003 - myDoc"), "myDoc")

    def test_pending_markers_and_json_determinism(self):
        text = "---\nid: p\n---\n\n# T\n\n<!-- i18n:pending key=slice -->\nTexto.\n"
        fp = fingerprint.fingerprint_text(text, "p.md")
        self.assertEqual(fp["pending_markers"], 1)
        self.assertEqual(fp["html_comments"], 0)
        self.assertEqual(fingerprint.to_json(fp), fingerprint.to_json(fingerprint.fingerprint_text(text, "p.md")))


class EquivalenceTests(unittest.TestCase):
    def test_equivalent_pair_passes(self):
        self.assertEqual(equivalence.compare_files(EQUIV_SOURCE, EQUIV_TARGET, "03-pagina-exemplo.md"), [])

    def test_source_without_frontmatter_vs_minimal_frontmatter_passes(self):
        self.assertEqual(equivalence.compare_files(NOFM_SOURCE, NOFM_TARGET, "25-rastreabilidade.md"), [])

    def _divergences(self, name):
        return equivalence.compare_files(EQUIV_SOURCE, DIVERGENT / f"{name}.md", "03-pagina-exemplo.md")

    def test_missing_heading_fails_on_headings(self):
        ds = self._divergences("missing-heading")
        self.assertEqual(dimensions(ds), ["headings.count", "headings.missing"])
        self.assertEqual([d["line_source"] for d in ds if d["dimension"] == "headings.missing"], [15])

    def test_table_with_fewer_columns_fails_on_tables(self):
        ds = self._divergences("table-column")
        self.assertTrue(all(d["dimension"].startswith("tables.") for d in ds))
        self.assertIn("tables.columns", dimensions(ds))

    def test_changed_code_block_fails_on_code_blocks(self):
        self.assertEqual(dimensions(self._divergences("code-changed")), ["code_blocks.sha256"])

    def test_removed_protected_token_fails_on_protected_tokens(self):
        ds = self._divergences("token-removed")
        self.assertEqual(dimensions(ds), ["protected_tokens"])
        self.assertEqual(ds[0]["detail"], "CIC-001")

    def test_changed_internal_link_fails_on_internal_links(self):
        ds = self._divergences("link-changed")
        self.assertEqual(dimensions(ds), ["internal_links"])
        self.assertEqual(sorted(d["detail"] for d in ds), ["/sbd-toe/sbd-manual/cicd-seguro/index", "/sbd-toe/sbd-manual/cicd-seguro/intro"])

    def test_different_heading_id_fails_on_headings_id(self):
        ds = self._divergences("heading-id")
        self.assertEqual(dimensions(ds), ["headings.id"])
        self.assertEqual((ds[0]["expected"], ds[0]["actual"]), ("config", "configuration"))

    def test_target_may_pin_derived_anchor_but_not_another(self):
        src = "# T\n\n## Segunda secção\n"
        ok = fingerprint.fingerprint_text("# T\n\n## Second section {#segunda-secção}\n", "t.md")
        bad = fingerprint.fingerprint_text("# T\n\n## Second section {#second-section}\n", "t.md")
        base = fingerprint.fingerprint_text(src, "t.md")
        self.assertEqual(equivalence.compare_fingerprints(base, ok), [])
        self.assertEqual(dimensions(equivalence.compare_fingerprints(base, bad)), ["headings.id"])


class TreeTestCase(unittest.TestCase):
    """Builds a throw-away corpus + mirror tree that mimics the repository layout."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="i18n-equiv-"))
        self.root = self.tmp
        (self.root / "manuals_src").mkdir()
        (self.root / "translation").mkdir()
        self.docs = self.root / "manuals_src" / "docs" / "sbd-toe"
        self.i18n = self.root / "manuals_src" / "i18n"
        self.docs.mkdir(parents=True)
        self.i18n.mkdir(parents=True)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def put_source(self, rel, src=EQUIV_SOURCE):
        dest = self.docs / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(src, dest)
        return dest

    def put_target(self, rel, src=EQUIV_TARGET, locale="en"):
        dest = common.mirror_path(rel, self.i18n, locale)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(src, dest)
        return dest

    def args(self, *extra, locale="en"):
        return ["--source-locale", "pt", "--target-locale", locale, "--docs-dir", str(self.docs), "--i18n-dir", str(self.i18n), *extra]


class PathNormalisationTests(TreeTestCase):
    def test_keys_are_nfc_and_nfd_names_resolve(self):
        import unicodedata

        nfd_name = unicodedata.normalize("NFD", "06-manual-formação-por-capitulo.md")
        nfc_name = unicodedata.normalize("NFC", nfd_name)
        self.assertNotEqual(nfd_name, nfc_name)
        self.put_source(f"cap/{nfd_name}")
        keys = common.iter_corpus(self.docs)
        self.assertEqual(keys, [f"cap/{nfc_name}"])
        self.assertTrue(unicodedata.is_normalized("NFC", keys[0]))
        self.assertTrue(common.source_path(keys[0], self.docs).is_file())
        self.assertTrue(common.resolve_corpus_path(f"cap/{nfd_name}", self.docs).is_file())
        self.assertEqual(common.rel_to_docs(common.source_path(keys[0], self.docs), self.docs), keys[0])
        # The mirror is looked up by the same NFC key whatever the on-disk spelling.
        self.put_target(f"cap/{nfc_name}")
        self.assertTrue(common.mirror_path(keys[0], self.i18n, "en").is_file())
        state, _ = sync_state.build_state(self.root, self.docs, self.i18n, "pt", "en", generated_at="x")
        self.assertEqual(list(state["files"]), [f"cap/{nfc_name}"])


class EquivalenceCliTests(TreeTestCase):
    def test_all_without_translations_succeeds_with_warning(self):
        self.put_source("cap/a.md")
        self.assertEqual(equivalence.main(self.args("--all")), 0)

    def test_all_reports_divergent_and_equivalent_files(self):
        self.put_source("cap/a.md")
        self.put_target("cap/a.md")
        self.put_source("cap/b.md")
        self.put_target("cap/b.md", DIVERGENT / "code-changed.md")
        self.assertEqual(equivalence.main(self.args("--all")), 1)
        self.assertEqual(equivalence.main(self.args("--path", "cap/a.md")), 0)
        self.assertEqual(equivalence.main(self.args("--path", "cap/b.md")), 1)
        self.assertEqual(equivalence.main(self.args("--path", "cap")), 1)

    def test_orphan_in_mirror_is_a_failure(self):
        self.put_source("cap/a.md")
        self.put_target("cap/renamed.md")
        self.assertEqual(equivalence.main(self.args("--all")), 1)

    def test_direction_is_a_parameter(self):
        # Source in docs/, target under i18n/<locale>: the locale names are only labels.
        self.put_source("cap/a.md", EQUIV_TARGET)
        self.put_target("cap/a.md", EQUIV_SOURCE, locale="pt")
        self.assertEqual(equivalence.main(self.args("--all", locale="pt")), 0)


class SyncStateTests(TreeTestCase):
    def write_target(self, rel, *, source_hash, target_hash=None, terms_hash="null", pending=0, body="# Example\n\nText.\n"):
        """Write a mirror file whose translation block records the given hashes.
        ``target_hash=None`` records the hash of the body actually written."""
        fm_head = "---\nid: a\n"
        fm_tail = "---\n\n"
        content = fm_head + fm_tail + body + ("<!-- i18n:pending key=x -->\n" * pending)
        if target_hash is None:
            target_hash = common.content_sha256(content)
        block = (
            "translation:\n  source_locale: pt\n  source_path: {rel}\n  source_sha256: {sh}\n  source_commit: abc\n"
            "  target_sha256: {th}\n  engine: test\n  prompt_sha256: p\n  terms_sha256: {terms}\n  translated_at: 2026-09-25T10:00:00Z\n  reviewed_by: null\n"
        ).format(rel=rel, sh=source_hash, th=target_hash, terms=terms_hash)
        dest = common.mirror_path(rel, self.i18n, "en")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(fm_head + block + fm_tail + body + ("<!-- i18n:pending key=x -->\n" * pending), encoding="utf-8")
        return dest

    def state_of(self, rel):
        state, warnings = sync_state.build_state(self.root, self.docs, self.i18n, "pt", "en", generated_at="2026-09-25T00:00:00Z")
        return state["files"][rel], state, warnings

    def test_untranslated_and_contract_shape(self):
        self.put_source("cap/a.md")
        entry, state, warnings = self.state_of("cap/a.md")
        self.assertEqual(warnings, [])
        self.assertEqual(entry["state"], "untranslated")
        self.assertEqual(list(entry), ["state", "source_sha256", "translated_source_sha256", "target_sha256", "terms_sha256_at_translation", "translated_at", "pending_blocks"])
        self.assertEqual(list(state), ["generated_at", "source_locale", "target_locale", "terms_sha256", "files", "totals"])
        self.assertEqual(state["terms_sha256"], None)
        self.assertEqual(state["totals"], {"untranslated": 1, "synced": 0, "partial": 0, "pt-ahead": 0, "en-ahead": 0, "drift": 0, "stale-terms": 0})

    def test_synced_partial_and_precedence(self):
        src = self.put_source("cap/a.md")
        sh = common.file_sha256(src)
        self.write_target("cap/a.md", source_hash=sh)
        self.assertEqual(self.state_of("cap/a.md")[0]["state"], "synced")

        self.write_target("cap/a.md", source_hash=sh, pending=2)
        entry = self.state_of("cap/a.md")[0]
        self.assertEqual((entry["state"], entry["pending_blocks"]), ("partial", 2))

        # Source changed after translation -> pt-ahead (beats partial).
        src.write_text(src.read_text(encoding="utf-8") + "\nMais texto.\n", encoding="utf-8")
        self.assertEqual(self.state_of("cap/a.md")[0]["state"], "pt-ahead")

        # Target edited after generation -> en-ahead; both -> drift.
        sh2 = common.file_sha256(src)
        self.write_target("cap/a.md", source_hash=sh2, target_hash="0" * 64)
        self.assertEqual(self.state_of("cap/a.md")[0]["state"], "en-ahead")
        self.write_target("cap/a.md", source_hash="1" * 64, target_hash="0" * 64)
        self.assertEqual(self.state_of("cap/a.md")[0]["state"], "drift")

    def test_stale_terms_only_when_registry_exists(self):
        src = self.put_source("cap/a.md")
        sh = common.file_sha256(src)
        self.write_target("cap/a.md", source_hash=sh, terms_hash="old")
        self.assertEqual(self.state_of("cap/a.md")[0]["state"], "synced")  # no registry yet
        registry = self.root / common.TERMS_REGISTRY_RELPATH
        registry.parent.mkdir(parents=True, exist_ok=True)
        registry.write_text("terms: []\n", encoding="utf-8")
        entry, state, _ = self.state_of("cap/a.md")
        self.assertEqual(entry["state"], "stale-terms")
        self.assertEqual(state["terms_sha256"], common.file_sha256(registry))
        self.write_target("cap/a.md", source_hash=sh, terms_hash=common.file_sha256(registry), pending=1)
        self.assertEqual(self.state_of("cap/a.md")[0]["state"], "partial")

    def test_missing_translation_block_is_reported(self):
        self.put_source("cap/a.md")
        self.put_target("cap/a.md", EQUIV_SOURCE)  # a hand-made mirror without a translation block
        entry, _, warnings = self.state_of("cap/a.md")
        self.assertEqual(entry["state"], "drift")
        self.assertTrue(any("translation" in w for w in warnings))

    def test_write_then_check_roundtrip(self):
        src = self.put_source("cap/a.md")
        self.put_source("cap/b.md", NOFM_SOURCE)
        self.write_target("cap/a.md", source_hash=common.file_sha256(src))
        state_file = self.root / "translation" / "state" / "sync-state.json"
        # The throw-away tree has no terms registry, so terms_sha256 is null (never stale-terms).
        argv = self.args("--state-file", str(state_file), "--registry", str(self.root / common.TERMS_REGISTRY_RELPATH))
        self.assertEqual(sync_state.main(argv + ["--write"]), 0)
        written = json.loads(state_file.read_text(encoding="utf-8"))
        self.assertEqual(written["totals"]["synced"], 1)
        self.assertEqual(written["totals"]["untranslated"], 1)
        self.assertEqual(sync_state.main(argv + ["--check"]), 0)
        # Any source change makes the committed state stale.
        src.write_text(src.read_text(encoding="utf-8") + "\nx\n", encoding="utf-8")
        self.assertEqual(sync_state.main(argv + ["--check"]), 1)
        self.assertEqual(sync_state.main(argv + ["--write"]), 0)
        self.assertEqual(sync_state.main(argv + ["--check"]), 0)


if __name__ == "__main__":
    unittest.main()
