"""Tests for ``translate.py`` (front 6): prepare / assemble / check.

Run with::

    python -m unittest discover -s translation/scripts/tests -p 'test_*.py'
"""

from __future__ import annotations

import io
import json
import os
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

import yaml

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))

import common  # noqa: E402
import equivalence  # noqa: E402
import fingerprint  # noqa: E402
import sync_state  # noqa: E402
import terms_lint  # noqa: E402
import translate  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"
SOURCE = FIXTURES / "translate" / "source" / "04-pagina-traducao.md"
NOFM_SOURCE = FIXTURES / "no-frontmatter" / "source" / "25-rastreabilidade.md"
PROMPT = SCRIPTS.parent / "prompts" / "translate-v1.md"
REL = "04-pagina-traducao.md"


def entry(key: str, **overrides) -> dict:
    e = {
        "key": key, "species": 1, "state": "in-record", "owner": "manual-agent", "en": key, "en_variants": [],
        "pt": None, "pt_variants": [], "ontology_id": None, "sense": "", "senses": [], "evidence": None,
        "counts": {}, "change_cost": "baixo", "curator": None, "previous": None, "proposal": None,
        "false_friends": [], "pending_reason": None, "blocks_translation": True, "notes": "",
    }
    e.update(overrides)
    return e


REGISTRY = {
    "meta": {"version": 1, "spelling": "en-GB", "source_locale": "pt", "target_locale": "en"},
    "terms": [
        entry("slice", species=2, state="coined", owner="archon", en="slice", en_variants=["slices"], pt="fatia", pt_variants=["fatias"]),
        entry("coverage", state="pending", pending_reason="polysemy", senses=[{"sense": "x", "where": None}], en="coverage", pt="cobertura", pt_variants=["coberturas"]),
        entry("appsec_core", state="do-not-translate", en="AppSec Core", pt="AppSec Core"),
        entry("requirement", en="requirement", en_variants=["requirements"], pt="requisito", pt_variants=["requisitos"]),
    ],
}

# Mechanical test translation, keyed by the unit text the job carries (markers included).
MECHANICAL = {
    "Fixture para o translate.py — fatia ⟦P0⟧, requisito ⟦P1⟧.": "Fixture for translate.py — slice ⟦P0⟧, requirement ⟦P1⟧.",
    "Página de tradução": "Translation page",
    "Esta página exercita a **fatia** ⟦P0⟧ do ⟦P1⟧ e o requisito ⟦P2⟧ do ⟦P3⟧.⟦P4⟧A segunda linha continua o parágrafo depois de uma quebra dura.": "This page exercises the **slice** ⟦P0⟧ of ⟦P1⟧ and the requirement ⟦P2⟧ of the ⟦P3⟧.⟦P4⟧The second line continues the paragraph after a hard break.",
    "Objectivo": "Objective",
    "Primeiro item com a fatia": "First item with the slice",
    "Segundo item": "Second item",
    "Sub-item aninhado com [ligação interna](⟦P0⟧)": "Nested sub-item with an [internal link](⟦P0⟧)",
    "Tabela": "Table",
    "ID": "ID",
    "Descrição": "Description",
    "Nível": "Level",
    "Inventário de componentes": "Component inventory",
    "L1": "L1",
    "L2": "L2",
    "Como engenheiro": "As an engineer",
    "Como engenheiro, quero a fatia validada no pipeline.": "As an engineer, I want the slice validated in the pipeline.",
    "Nota sem título.": "Note without a title.",
    "Ver a [secção da tabela](⟦P0⟧) e o [capítulo de ⟦P1⟧](⟦P2⟧).": "See the [table section](⟦P0⟧) and the [⟦P1⟧ chapter](⟦P2⟧).",
    "Passo um": "Step one",
    "Sub-secção sem id": "Sub-section without id",
    "Texto final em ⟦P0⟧.": "Closing text at ⟦P0⟧.",
}


def registry_with(**changes) -> dict:
    """Copy of REGISTRY with per-key field overrides (``key={field: value}``) and,
    under ``extra``, additional entries."""
    import copy

    reg = copy.deepcopy(REGISTRY)
    for entry_ in reg["terms"]:
        entry_.update(changes.get(entry_["key"], {}))
    reg["terms"].extend(changes.get("extra", []))
    return reg


def units_of(job: dict):
    for seg in job["segments"]:
        for unit in [seg, *seg.get("cells", []), *seg.get("fields", [])]:
            if "text" in unit:
                yield unit


def mechanical_out(job: dict) -> dict:
    out = []
    for unit in units_of(job):
        if unit["translate"]:
            assert unit["text"] in MECHANICAL, f"fixture changed: no mechanical translation for {unit['id']}: {unit['text']!r}"
            out.append({"id": unit["id"], "text": MECHANICAL[unit["text"]]})
    return {"segments": out}


class Workspace:
    """Temporary docs/i18n/registry/jobs layout for the CLI."""

    def __init__(self, registry: dict = REGISTRY) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.docs = root / "docs"
        self.i18n = root / "i18n"
        self.jobs = root / "jobs"
        self.docs.mkdir()
        shutil.copy(SOURCE, self.docs / REL)
        self.registry = root / "registry.yaml"
        self.registry.write_text(yaml.safe_dump(registry, allow_unicode=True, sort_keys=False), encoding="utf-8")

    def args(self):
        return ["--docs-dir", str(self.docs), "--i18n-dir", str(self.i18n), "--registry", str(self.registry)]

    def prepare(self, path=REL, *extra):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = translate.main(["prepare", "--path", path, "--out", str(self.jobs), "--prompt", str(PROMPT), "--source-commit", "abc1234", *self.args(), *extra])
        return code, buf.getvalue()

    def job(self, rel=REL) -> dict:
        return json.loads((self.jobs / (rel + ".job.json")).read_text(encoding="utf-8"))

    def write_out(self, rel, out: dict) -> Path:
        path = self.jobs / (rel + ".out.json")
        path.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
        return path

    def assemble(self, rel=REL, *extra):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = translate.main(["assemble", "--job", str(self.jobs / (rel + ".job.json")), "--engine", "unit-test", "--translated-at", "2026-09-25T00:00:00Z", *self.args(), *extra])
        return code, buf.getvalue()

    def mirror(self, rel=REL) -> Path:
        return common.mirror_dir(self.i18n, "en") / rel

    def cleanup(self) -> None:
        self.tmp.cleanup()


class ProtectedSpansTests(unittest.TestCase):
    def test_families_and_priority(self):
        dnt = translate.dnt_pattern(REGISTRY, "en")
        text = "Ver `ACO-TSV` e ACO-TSV do AppSec Core em [x](./p#a) e <b>SBOM</b> https://e.org/a."
        kinds = [k for _s, _e, k in translate.protected_spans(text, dnt)]
        self.assertEqual(kinds, ["code_span", "id", "dnt", "link_dest", "html_tag", "acronym", "html_tag", "url"])
        spans = translate.protected_spans(text, dnt)
        self.assertEqual(text[spans[3][0] : spans[3][1]], "./p#a")
        self.assertEqual(text[spans[-1][0] : spans[-1][1]], "https://e.org/a")  # trailing full stop excluded

    def test_restore_fails_on_missing_duplicated_unknown_or_newline(self):
        protected = [{"marker": "⟦P0⟧", "kind": "id", "text": "CIC-001"}, {"marker": "⟦P1⟧", "kind": "acronym", "text": "SBOM"}]
        self.assertEqual(translate.restore("a ⟦P1⟧ b ⟦P0⟧", protected), "a SBOM b CIC-001")
        for bad in ("a ⟦P0⟧", "⟦P0⟧ ⟦P0⟧ ⟦P1⟧", "⟦P0⟧ ⟦P1⟧ ⟦P2⟧", "⟦P0⟧\n⟦P1⟧"):
            with self.assertRaises(translate.TranslateError):
                translate.restore(bad, protected)


class PrepareTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ws = Workspace()
        code, cls.output = cls.ws.prepare()
        assert code == 0, cls.output
        cls.job = cls.ws.job()

    @classmethod
    def tearDownClass(cls):
        cls.ws.cleanup()

    def test_skeleton_kinds_in_order(self):
        kinds = [s["kind"] for s in self.job["segments"]]
        self.assertEqual(kinds[0], "frontmatter")
        self.assertEqual(kinds[1:5], ["blank", "html_comment", "blank", "heading"])
        self.assertIn("code_block", kinds)
        self.assertEqual(kinds.count("admonition_open"), 2)
        self.assertEqual(kinds.count("admonition_close"), 2)
        self.assertEqual(kinds.count("table_row"), 4)
        self.assertEqual(kinds.count("list_item"), 6)
        self.assertEqual(kinds.count("heading"), 4)
        self.assertTrue(set(kinds) <= set(translate.KINDS))
        # Segments reassemble the source verbatim.
        text = common.read_text(SOURCE)
        self.assertEqual("\n".join(s["raw"] for s in self.job["segments"]), text)

    def test_headings_keep_explicit_ids_outside_the_text(self):
        heads = [s for s in self.job["segments"] if s["kind"] == "heading"]
        self.assertEqual((heads[0]["prefix"], heads[0]["text"], heads[0]["suffix"]), ("# ", "Página de tradução", " {#pagina-traducao}"))
        self.assertEqual(heads[-1]["suffix"], "")
        self.assertEqual(heads[-1]["text"], "Sub-secção sem id")

    def test_markers_and_protected(self):
        by_id = {u["id"]: u for u in units_of(self.job)}
        para = by_id["s0007"]
        self.assertEqual([p["kind"] for p in para["protected"]], ["code_span", "dnt", "code_span", "acronym", "line_break"])
        self.assertEqual([p["text"] for p in para["protected"]], ["`ACO-TSV`", "AppSec Core", "`CIC-003`", "SBOM", "  \n"])
        self.assertIn("⟦P4⟧A segunda linha", para["text"])
        link = by_id["s0013"]
        self.assertEqual(link["prefix"], "  - ")
        self.assertEqual(link["protected"][0]["text"], "./outra-pagina#seccao")
        self.assertEqual(link["text"], "Sub-item aninhado com [ligação interna](⟦P0⟧)")
        self.assertEqual(by_id["s0040"]["protected"][0]["kind"], "url")
        self.assertEqual(by_id["s0001.description"]["protected"][0]["text"], "ACO-TSV")
        # Marker numbering restarts per unit and restoring the source text is exact.
        for unit in units_of(self.job):
            self.assertEqual([p["marker"] for p in unit["protected"]], [translate.marker(i) for i in range(len(unit["protected"]))])

    def test_table_cells_and_no_prose(self):
        rows = [s for s in self.job["segments"] if s["kind"] == "table_row"]
        self.assertEqual([r["row"] for r in rows], ["header", "delimiter", "body", "body"])
        self.assertEqual([c["text"] for c in rows[0]["cells"]], ["ID", "Descrição", "Nível"])
        self.assertFalse(rows[1]["translate"])
        id_cell = rows[2]["cells"][0]
        self.assertFalse(id_cell["translate"])
        self.assertEqual(id_cell["reason"], "no-prose")
        self.assertEqual(id_cell["protected"][0]["text"], "CIC-003")

    def test_blocked_by_pending_term(self):
        blocked = {u["id"]: u["blocked_by"] for u in units_of(self.job) if u["blocked_by"]}
        self.assertEqual(blocked, {"s0001.title": ["coverage"], "s0014": ["coverage"], "s0021.c1": ["coverage"], "s0036": ["coverage"]})
        for unit in units_of(self.job):
            if unit["blocked_by"]:
                self.assertFalse(unit["translate"])
        self.assertEqual(self.job["stats"]["blocked_by_key"], {"coverage": 4})
        self.assertNotIn("s0014", self.job["units"])

    def test_glossary(self):
        g = self.job["glossary"]
        self.assertEqual([t["key"] for t in g["terms"]], ["requirement", "slice"])
        self.assertEqual(g["terms"][1]["state"], "coined")
        self.assertEqual(g["terms"][1]["target"], "slice")
        self.assertEqual([d["key"] for d in g["do_not_translate"]], ["appsec_core"])
        self.assertEqual([p["key"] for p in g["pending"]], ["coverage"])
        self.assertEqual(g["pending"][0]["pending_reason"], "polysemy")

    def test_provenance_and_stats(self):
        self.assertEqual(self.job["source_sha256"], common.file_sha256(SOURCE))
        self.assertEqual(self.job["source_commit"], "abc1234")
        self.assertEqual(self.job["terms_sha256"], terms_lint.registry_sha256(self.ws.registry))
        self.assertEqual(self.job["prompt_sha256"], common.file_sha256(PROMPT))
        self.assertEqual(self.job["direction"], {"source_locale": "pt", "target_locale": "en"})
        self.assertEqual(self.job["stats"]["translatable_units"], len(self.job["units"]))
        self.assertGreater(self.job["stats"]["words"], 50)
        self.assertIn("21 units", self.output)

    def test_applied_glossary_keys_and_hash(self):
        keys = self.job["glossary_keys"]
        self.assertEqual(keys, ["appsec_core", "coverage", "requirement", "slice"])  # terms + do-not-translate + pending
        self.assertEqual(self.job["glossary_sha256"], common.glossary_sha256(REGISTRY, keys))
        self.assertEqual(list(self.job)[7:11], ["terms_sha256", "glossary_keys", "glossary_sha256", "prompt_sha256"])

    def _hash_with_registry(self, registry: dict) -> tuple:
        ws = Workspace(registry)
        try:
            code, out = ws.prepare()
            self.assertEqual(code, 0, out)
            job = ws.job()
            return job["glossary_sha256"], job["terms_sha256"], job["glossary_keys"]
        finally:
            ws.cleanup()

    def test_glossary_hash_ignores_notes_but_not_the_translation(self):
        base = self.job["glossary_sha256"]
        # notes/evidence/counts/sense of an applied entry: whole-registry hash moves, applied-glossary hash does not.
        h, terms, keys = self._hash_with_registry(registry_with(slice={"notes": "revised 2026-09-25", "sense": "other", "counts": {"P1": 9}}))
        self.assertEqual(h, base)
        self.assertNotEqual(terms, self.job["terms_sha256"])
        self.assertEqual(keys, self.job["glossary_keys"])
        # `en` of an applied entry changes the hash; so do state, variants and blocks_translation.
        self.assertNotEqual(self._hash_with_registry(registry_with(slice={"en": "partition"}))[0], base)
        self.assertNotEqual(self._hash_with_registry(registry_with(coverage={"blocks_translation": False}))[0], base)
        self.assertNotEqual(self._hash_with_registry(registry_with(requirement={"en_variants": ["requirements", "reqs"]}))[0], base)
        # An entry whose forms do not occur in the file is not applied: changing it never touches the hash.
        extra = entry("threat", en="threat", en_variants=["threats"], pt="ameaça", pt_variants=["ameaças"])
        h, _terms, keys = self._hash_with_registry(registry_with(extra=[extra]))
        self.assertEqual(keys, self.job["glossary_keys"])
        self.assertEqual(h, base)
        self.assertEqual(self._hash_with_registry(registry_with(extra=[dict(extra, en="menace", notes="x")]))[0], base)

    def test_prepare_is_deterministic(self):
        first = (self.ws.jobs / (REL + ".job.json")).read_bytes()
        other = Workspace()
        try:
            code, _ = other.prepare()
            self.assertEqual(code, 0)
            self.assertEqual((other.jobs / (REL + ".job.json")).read_bytes(), first)
        finally:
            other.cleanup()

    def test_sync_state_eligibility_and_force(self):
        ws = Workspace()
        try:
            ws.prepare()
            ws.write_out(REL, mechanical_out(ws.job()))
            code, _ = ws.assemble(REL, "--write")
            self.assertEqual(code, 0)
            code, out = ws.prepare()  # now partial: not eligible
            self.assertEqual(code, 0)
            self.assertIn("skipped (partial)", out)
            code, out = ws.prepare(REL, "--force")
            self.assertIn("1 job(s)", out)
            code, out = ws.prepare(REL, "--only-stale")
            self.assertIn("skipped (partial)", out)
        finally:
            ws.cleanup()


class AssembleTests(unittest.TestCase):
    def setUp(self):
        self.ws = Workspace()
        code, _ = self.ws.prepare()
        self.assertEqual(code, 0)
        self.job = self.ws.job()

    def tearDown(self):
        self.ws.cleanup()

    def test_mechanical_translation_writes_an_equivalent_file(self):
        self.ws.write_out(REL, mechanical_out(self.job))
        code, out = self.ws.assemble(REL, "--write")
        self.assertEqual(code, 0, out)
        mirror = self.ws.mirror()
        self.assertTrue(mirror.is_file())
        text = common.read_text(mirror)
        # Equivalence with the source.
        self.assertEqual(equivalence.compare_files(SOURCE, mirror, REL), [])
        # Front matter per contract: structural keys copied, title blocked (stays PT), description translated.
        fm, body, _ = common.parse_frontmatter(text)
        self.assertEqual(fm["id"], "pagina-traducao")
        self.assertEqual(fm["sidebar_position"], 4)
        self.assertEqual(fm["tags"], ["fixture", "traducao"])
        self.assertEqual(fm["title"], "Página de tradução com cobertura")
        self.assertEqual(fm["description"], "Fixture for translate.py — slice ACO-TSV, requirement CIC-003.")
        block = fm["translation"]
        self.assertEqual(list(block), ["source_locale", "source_path", "source_sha256", "source_commit", "target_sha256", "engine", "prompt_sha256", "terms_sha256", "glossary_keys", "glossary_sha256", "translated_at", "reviewed_by"])
        self.assertEqual(block["glossary_keys"], ["appsec_core", "coverage", "requirement", "slice"])
        self.assertEqual(block["glossary_sha256"], self.job["glossary_sha256"])
        self.assertEqual(block["glossary_sha256"], common.glossary_sha256(REGISTRY, block["glossary_keys"]))
        self.assertIn("  glossary_keys: [appsec_core, coverage, requirement, slice]\n  glossary_sha256: ", text)
        self.assertEqual(block["source_locale"], "pt")
        self.assertEqual(block["source_path"], REL)
        self.assertEqual(block["source_sha256"], common.file_sha256(SOURCE))
        self.assertEqual(block["source_commit"], "abc1234")
        self.assertEqual(block["engine"], "unit-test")
        self.assertEqual(block["prompt_sha256"], common.file_sha256(PROMPT))
        self.assertEqual(block["terms_sha256"], terms_lint.registry_sha256(self.ws.registry))
        self.assertEqual(block["translated_at"], "2026-09-25T00:00:00Z")
        self.assertIsNone(block["reviewed_by"])
        self.assertEqual(block["target_sha256"], common.content_sha256(common.strip_translation_block(text)))
        # Pending comments where they belong; blocked units stay in the source language.
        lines = text.split("\n")
        close = lines.index("---", 1)
        self.assertEqual(lines[close + 1], "<!-- i18n:pending key=coverage -->")  # front-matter title
        self.assertIn("  <!-- i18n:pending key=coverage -->", lines)
        self.assertEqual(lines[lines.index("  <!-- i18n:pending key=coverage -->") + 1], "- Terceiro item sobre cobertura normativa")
        self.assertEqual(lines[lines.index("<!-- i18n:pending key=coverage -->", close + 2) + 1], "| ID | Description | Level |")
        self.assertIn("| CIC-004 | Cobertura de dependências | L2 |", lines)
        self.assertEqual(lines[lines.index("   <!-- i18n:pending key=coverage -->") + 1], "2. Passo dois com cobertura")
        self.assertEqual(text.count("i18n:pending"), 4)
        # Restored structure around translated text.
        self.assertIn("# Translation page {#pagina-traducao}", text)
        self.assertIn("This page exercises the **slice** `ACO-TSV` of AppSec Core and the requirement `CIC-003` of the SBOM.  \nThe second line", text)
        self.assertIn("  - Nested sub-item with an [internal link](./outra-pagina#seccao)", text)
        self.assertIn(":::userstory As an engineer", text)
        self.assertIn("See the [table section](#tabela) and the [CI/CD chapter](/sbd-toe/sbd-manual/cicd-seguro/intro).", text)
        self.assertIn("```yaml\nfatia: ACO-TSV\n```", text)
        self.assertIn("<!--template: sbdtoe-addon -->", text)
        # sync_state derives `partial` for the pair.
        warnings = []
        entry_ = sync_state.file_entry(REL, self.ws.docs / REL, mirror, terms_lint.registry_sha256(self.ws.registry), "pt", warnings, registry=REGISTRY)
        self.assertEqual(warnings, [])
        self.assertEqual(entry_["state"], "partial")
        self.assertEqual(entry_["pending_blocks"], 4)
        self.assertEqual(entry_["glossary_sha256_at_translation"], block["glossary_sha256"])
        self.assertIn("sync state: partial", out)
        # check: equivalence + spelling + consistency over the written file.
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = translate.main(["check", "--path", REL, *self.ws.args()])
        self.assertEqual(code, 0, buf.getvalue())

    def test_job_without_glossary_provenance_is_refused(self):
        self.ws.write_out(REL, mechanical_out(self.job))
        job_file = self.ws.jobs / (REL + ".job.json")
        legacy = {k: v for k, v in self.job.items() if k not in ("glossary_keys", "glossary_sha256")}
        job_file.write_text(json.dumps(legacy, ensure_ascii=False), encoding="utf-8")
        err = io.StringIO()
        with redirect_stderr(err):
            code, _ = self.ws.assemble(REL, "--write")
        self.assertEqual(code, 2)
        self.assertIn("re-run prepare", err.getvalue())
        self.assertFalse(self.ws.mirror().exists())

    def test_missing_marker_fails_without_writing(self):
        out = mechanical_out(self.job)
        for item in out["segments"]:
            if item["id"] == "s0033":
                item["text"] = "See the [table section](⟦P0⟧) and the chapter."  # ⟦P1⟧ and ⟦P2⟧ dropped
        self.ws.write_out(REL, out)
        code, output = self.ws.assemble(REL, "--write")
        self.assertEqual(code, 1)
        self.assertIn("missing marker(s): ⟦P1⟧, ⟦P2⟧", output)
        self.assertFalse(self.ws.mirror().exists())

    def test_structural_divergence_fails_without_writing(self):
        out = mechanical_out(self.job)
        for item in out["segments"]:
            if item["id"] == "s0012":
                item["text"] = "Second item\n- an extra item"
        self.ws.write_out(REL, out)
        code, output = self.ws.assemble(REL, "--write")
        self.assertEqual(code, 1)
        self.assertIn("literal line break", output)
        self.assertFalse(self.ws.mirror().exists())

    def test_missing_translation_and_unknown_id_fail(self):
        out = mechanical_out(self.job)
        out["segments"] = [i for i in out["segments"] if i["id"] != "s0005"] + [{"id": "s9999", "text": "x"}]
        self.ws.write_out(REL, out)
        code, output = self.ws.assemble(REL)
        self.assertEqual(code, 1)
        self.assertIn("s0005: no translation", output)
        self.assertIn("s9999", output)

    def test_spelling_errors_block_unless_allowed(self):
        out = mechanical_out(self.job)
        for item in out["segments"]:
            if item["id"] == "s0035":
                item["text"] = "Step one, organized"
        self.ws.write_out(REL, out)
        code, output = self.ws.assemble(REL, "--write")
        self.assertEqual(code, 1)
        self.assertIn("'organized' -> 'organised'", output)
        self.assertFalse(self.ws.mirror().exists())
        code, _ = self.ws.assemble(REL, "--write", "--allow-spelling-errors")
        self.assertEqual(code, 0)
        self.assertTrue(self.ws.mirror().is_file())

    def test_source_change_is_detected(self):
        self.ws.write_out(REL, mechanical_out(self.job))
        with open(self.ws.docs / REL, "a", encoding="utf-8") as handle:
            handle.write("\nNova frase.\n")
        code, _ = self.ws.assemble(REL, "--write")
        self.assertEqual(code, 2)
        self.assertFalse(self.ws.mirror().exists())


    def test_job_prepared_from_a_dirty_source_is_refused_on_write(self):
        self.ws.write_out(REL, mechanical_out(self.job))
        job_path = self.ws.jobs / (REL + ".job.json")
        job = json.loads(job_path.read_text(encoding="utf-8"))
        job["source_dirty"] = True
        job_path.write_text(json.dumps(job, ensure_ascii=False), encoding="utf-8")
        code, _ = self.ws.assemble(REL)  # dry run still validates
        self.assertEqual(code, 0)
        with redirect_stderr(io.StringIO()) as err:
            code, _ = self.ws.assemble(REL, "--write")
        self.assertEqual(code, 2)
        self.assertIn("uncommitted source changes", err.getvalue())
        self.assertFalse(self.ws.mirror().exists())


class FrontmatterClosingLineTests(unittest.TestCase):
    def test_closing_line_with_trailing_text_round_trips(self):
        """A front matter closed by an over-long rule ("---" + 85 "-") must not duplicate the rule in the body."""
        ws = Workspace()
        try:
            rel = "sub/03-longa.md"
            (ws.docs / "sub").mkdir()
            rule = "-" * 88
            (ws.docs / rel).write_text(f"---\n\nid: longa\ntitle: Página longa\n{rule}\n\n# Título\n\nUm parágrafo.\n", encoding="utf-8")
            code, _ = ws.prepare(rel)
            self.assertEqual(code, 0)
            job = ws.job(rel)
            self.assertEqual(job["segments"][0]["kind"], "frontmatter")
            self.assertTrue(job["segments"][0]["raw"].endswith(rule))
            self.assertNotIn(rule[3:], [s["raw"] for s in job["segments"][1:]])
            out = {"segments": [{"id": u["id"], "text": u["text"]} for u in units_of(job) if u["translate"]]}
            ws.write_out(rel, out)
            code, output = ws.assemble(rel, "--write", "--allow-spelling-errors")
            self.assertEqual(code, 0, output)
            self.assertEqual(common.read_text(ws.mirror(rel)).count(rule[3:]), 1)
            self.assertEqual(equivalence.compare_files(ws.docs / rel, ws.mirror(rel), rel), [])
        finally:
            ws.cleanup()


class NoFrontmatterAndSymlinkTests(unittest.TestCase):
    def test_source_without_frontmatter_gets_the_minimal_one(self):
        ws = Workspace()
        try:
            rel = "sub/25-rastreabilidade.md"
            (ws.docs / "sub").mkdir()
            shutil.copy(NOFM_SOURCE, ws.docs / rel)
            code, _ = ws.prepare(rel)
            self.assertEqual(code, 0)
            job = ws.job(rel)
            self.assertFalse(job["frontmatter_present"])
            self.assertEqual(job["effective_id"], "rastreabilidade")
            self.assertEqual(job["segments"][0]["kind"], "heading")
            # Identity translation (source text back) keeps the body verbatim.
            out = {"segments": [{"id": u["id"], "text": u["text"]} for u in units_of(job) if u["translate"]]}
            ws.write_out(rel, out)
            code, output = ws.assemble(rel, "--write", "--allow-spelling-errors")
            self.assertEqual(code, 0, output)
            text = common.read_text(ws.mirror(rel))
            self.assertTrue(text.startswith("---\nid: rastreabilidade\ntranslation:\n  source_locale: pt\n"))
            fm, body, _ = common.parse_frontmatter(text)
            self.assertEqual(sorted(fm), ["id", "translation"])
            self.assertEqual(body.lstrip("\n"), common.read_text(NOFM_SOURCE))
            self.assertEqual(equivalence.compare_files(NOFM_SOURCE, ws.mirror(rel), rel), [])
        finally:
            ws.cleanup()

    def test_symlink_is_mirrored_as_the_same_relative_symlink(self):
        ws = Workspace()
        try:
            (ws.docs / "a").mkdir()
            (ws.docs / "b").mkdir()
            shutil.copy(SOURCE, ws.docs / "a" / "page.md")
            os.symlink("../a/page.md", ws.docs / "b" / "link.md")
            code, out = ws.prepare("b")
            self.assertEqual(code, 0)
            self.assertIn("b/link.md: symlink -> ../a/page.md", out)
            job = ws.job("b/link.md")
            self.assertEqual(job["kind"], "symlink")
            self.assertEqual(job["link_target"], "../a/page.md")
            self.assertFalse((ws.jobs / "b/link.md.out.json").exists())
            code, out = ws.assemble("b/link.md", "--write")
            self.assertEqual(code, 0, out)
            mirror = ws.mirror("b/link.md")
            self.assertTrue(mirror.is_symlink())
            self.assertEqual(os.readlink(mirror), "../a/page.md")
            # Idempotent; refuses a different target.
            code, _ = ws.assemble("b/link.md", "--write")
            self.assertEqual(code, 0)
        finally:
            ws.cleanup()


class ExtractProseTests(unittest.TestCase):
    """MDX statements and <style> blocks are not prose (terms_lint + translate agree)."""

    MDX = (
        "---\nid: x\ntitle: T\n---\n\nimport Link from '@docusaurus/Link';\n\nexport const CH = {\n  cap00: '/sbd-toe/threat-modeling/intro',\n};\n\n"
        "<style>{`\n  .a { color: red; }\n`}</style>\n\n<div className=\"pill\">Threat Modeling</div>\n\nA paragraph.\n"
    )

    def test_terms_lint_skips_esm_and_style(self):
        _lines, blocks = terms_lint.extract_prose(self.MDX)
        self.assertEqual([b.text for b in blocks], ["T", "Threat Modeling", "A paragraph."])
        findings = terms_lint.spelling_findings_for_text(self.MDX, "x.mdx", terms_lint.ExemptionIndex(None))
        self.assertEqual([(f.token, f.suggestion) for f in findings], [("Modeling", "Modelling")])

    def test_translate_marks_esm_and_style_as_untranslatable(self):
        seg = translate.segment_document(self.MDX, "x.mdx", None)
        kinds = [(s.kind, s.line) for s in seg.segments if s.kind in ("esm", "raw")]
        self.assertEqual(kinds, [("esm", 6), ("esm", 8), ("raw", 12)])
        translatable = [s.unit.text for s in seg.segments if s.unit is not None and s.unit.translate]
        self.assertEqual(translatable, ["⟦P0⟧Threat Modeling⟦P1⟧", "A paragraph."])


class RealCorpusSmokeTests(unittest.TestCase):
    """The segmenter must agree with the fingerprint parser on every page of the
    pilot chapter and restoring the untranslated units must be verbatim (the
    self-check inside ``segment_document`` raises otherwise)."""

    def test_pilot_chapter_segments_and_identity_assembles(self):
        try:
            root = common.repo_root()
        except common.TranslationToolError:
            self.skipTest("repository root not found")
        docs = common.default_docs_dir(root)
        chapter = docs / "010-sbd-manual" / "00-fundamentos"
        if not chapter.is_dir():
            self.skipTest("pilot chapter not present")
        registry_path = root / common.TERMS_REGISTRY_RELPATH
        registry = terms_lint.load_registry(registry_path) if registry_path.is_file() else None
        for rel in translate.select_sources(docs, "010-sbd-manual/00-fundamentos"):
            source = common.source_path(rel, docs)
            if source.is_symlink():
                continue
            text = common.read_text(source)
            job = translate.build_job(text=text, rel=rel, source_locale="pt", target_locale="en", registry=registry, terms_sha256=None, prompt_sha256="0" * 64, source_commit=None)
            translations = {u["id"]: u["text"] for u in units_of(job) if u["translate"]}
            meta = {"source_locale": "pt", "source_path": rel, "source_sha256": job["source_sha256"], "source_commit": None, "engine": "identity", "prompt_sha256": "0" * 64, "terms_sha256": None, "translated_at": "2026-09-25T00:00:00Z", "reviewed_by": None}
            final, _without, problems = translate.assemble_text(job, translations, meta)
            self.assertEqual(problems, [], rel)
            divergences = equivalence.compare_fingerprints(fingerprint.fingerprint_text(text, rel), fingerprint.fingerprint_text(final, rel))
            self.assertEqual(divergences, [], rel)


if __name__ == "__main__":
    unittest.main()


class PagesPluginTests(unittest.TestCase):
    """`--plugin pages` (2026-09-26): standalone pages (manuals_src/src/pages) mirror under
    docusaurus-plugin-content-pages; a job prepared for one plugin is never assembled into the other's mirror."""

    def tearDown(self):
        common.use_plugin("docs")

    def test_mirror_dir_follows_the_selected_plugin(self):
        i18n = Path("/x/i18n")
        self.assertEqual(common.mirror_dir(i18n, "en"), i18n / "en" / "docusaurus-plugin-content-docs" / "current")
        common.use_plugin("pages")
        self.assertEqual(common.mirror_dir(i18n, "en"), i18n / "en" / "docusaurus-plugin-content-pages")
        self.assertTrue(str(common.default_docs_dir(Path("/r"))).endswith("manuals_src/src/pages"))

    def test_unknown_plugin_is_rejected(self):
        with self.assertRaises(ValueError):
            common.use_plugin("blog")

    def test_assemble_refuses_a_job_prepared_for_another_plugin(self):
        import io
        from contextlib import redirect_stderr
        with tempfile.TemporaryDirectory() as t:
            job = Path(t) / "about.mdx.job.json"
            job.write_text(json.dumps({"schema": translate.JOB_SCHEMA, "kind": "document", "source_path": "about.mdx", "plugin": "pages"}), encoding="utf-8")
            err = io.StringIO()
            with redirect_stderr(err):
                code = translate.main(["assemble", "--job", str(job), "--engine", "test"])
            self.assertEqual(code, 2)
            self.assertIn("--plugin pages", err.getvalue())
