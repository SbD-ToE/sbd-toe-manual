"""Tests for the terms registry tooling (front 3): importer, lint and export.

Run with::

    python -m unittest discover -s translation/scripts/tests -p 'test_*.py'
"""

from __future__ import annotations

import copy
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))

import common  # noqa: E402
import species3_candidates  # noqa: E402
import sync_state  # noqa: E402
import terms_import  # noqa: E402
import terms_lint  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "terms"
ROOT = common.repo_root()
SURVEY = ROOT / "translation" / "terms" / "input" / "2026-09-24-levantamento-termos-en-papers-P0-P7.yaml"
REGISTRY = ROOT / common.TERMS_REGISTRY_RELPATH

DO_NOT_TRANSLATE = {"control_objective", "appsec_core", "relations", "practice_family", "shacl_owl", "mcp", "sbdtoe_sbd", "mirror_osf"}
POLYSEMY = {
    "grounding", "coverage", "practice", "mechanism", "artifact", "structural_invariance", "integration_substrate",
    "pilot", "tier", "promotion", "governance_protocol", "gate", "completeness_invariant", "apparatus", "harness",
    "control_controls", "baseline", "compliance",
}


def seed(tmp: Path) -> Path:
    registry = tmp / "registry.yaml"
    code = terms_import.main(["--input", str(SURVEY), "--registry", str(registry), "--quiet"])
    assert code == 0
    return registry


def minimal_entry(key: str, **overrides) -> dict:
    entry = {
        "key": key, "species": 1, "state": "in-record", "owner": "manual-agent", "en": key, "en_variants": [],
        "pt": None, "pt_variants": [], "ontology_id": None, "sense": "", "senses": [], "evidence": None,
        "counts": {}, "change_cost": "baixo", "curator": None, "previous": None, "proposal": None,
        "false_friends": [], "pending_reason": None, "blocks_translation": True, "notes": "",
    }
    entry.update(overrides)
    return entry


def registry_with(*entries: dict) -> dict:
    return {"meta": {"version": 1, "spelling": "en-GB", "source_locale": "pt", "target_locale": "en"}, "terms": list(entries)}


class ImporterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.registry_path = seed(Path(cls.tmp.name))
        cls.registry = terms_lint.load_registry(cls.registry_path)
        cls.by_key = {e["key"]: e for e in cls.registry["terms"]}

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_counts_and_states(self):
        terms = self.registry["terms"]
        self.assertEqual(len(terms), 158)
        self.assertEqual({e["key"] for e in terms if e["state"] == "do-not-translate"}, DO_NOT_TRANSLATE)
        pending = {e["key"]: e["pending_reason"] for e in terms if e["state"] == "pending"}
        self.assertEqual(len(pending), 19)
        self.assertEqual({k for k, r in pending.items() if r == "polysemy"}, POLYSEMY)
        self.assertEqual(pending["traversal"], "en-vs-en-collision")
        self.assertTrue(self.by_key["traversal"]["senses"])
        self.assertEqual(sum(1 for e in terms if e["state"] == "in-record"), 131)
        self.assertTrue(all(e["species"] == 1 and e["owner"] == "manual-agent" for e in terms))
        self.assertEqual([e["key"] for e in terms], sorted(e["key"] for e in terms))

    def test_key_normalisation_and_forms(self):
        self.assertEqual(self.by_key["control_objective"]["curator"]["id"], "ControlObjective")
        self.assertEqual(self.by_key["control_objective"]["en"], "ControlObjective")
        self.assertEqual(self.by_key["appsec_core"]["curator"]["id"], "AppSecCore")
        self.assertEqual(self.by_key["appsec_core"]["pt"], "AppSec Core")
        slice_ = self.by_key["slice"]
        self.assertEqual(slice_["en"], "slice")
        self.assertNotIn("slice", slice_["en_variants"])
        self.assertNotIn("Slice", slice_["en_variants"])  # canonical form removed case-insensitively
        self.assertIn("per-slice", slice_["en_variants"])
        self.assertIsNone(slice_["pt"])  # pt_status: colisao
        self.assertEqual(self.by_key["coverage"]["pt"], "cobertura")  # inequivoco
        self.assertIsNone(self.by_key["artifact"]["pt"])  # nao-inequivoco although pt_conceito is filled
        self.assertEqual(self.by_key["slice_contract"]["en"], "slice contract")
        self.assertEqual(self.by_key["bounded"]["en"], "bounded")  # "(genérico)" removed
        self.assertEqual(self.by_key["layer"]["en"], "layer")  # parenthetical containing " / " removed first
        self.assertEqual(self.by_key["slice"]["counts"]["total"], 501)
        self.assertEqual(self.by_key["slice"]["evidence"]["paper"], "P1")
        self.assertEqual(sorted(self.registry["meta"]["curator_input_sha256"]), ["csv", "yaml"])

    def test_pt_alternatives_are_split(self):
        self.assertEqual(self.by_key["cycle_iteration"]["pt"], "ciclo")
        self.assertEqual(self.by_key["cycle_iteration"]["pt_variants"], ["iteração"])
        self.assertEqual(self.by_key["lifecycle_phase"]["pt"], "ciclo de vida")
        self.assertEqual(self.by_key["lifecycle_phase"]["pt_variants"], ["fase"])
        self.assertEqual(self.by_key["mirror_osf"]["pt_variants"], ["OSF", "DOI"])
        self.assertFalse(any(" / " in (e["pt"] or "") for e in self.registry["terms"]))
        self.assertEqual(terms_import.split_pt_alternatives("a / b / a", ["b", "c"]), ("a", ["b", "c"]))
        self.assertEqual(terms_import.split_pt_alternatives("simples", []), ("simples", []))
        self.assertEqual(terms_import.split_pt_alternatives(None, []), (None, []))

    def test_split_flag_migrates_only_unsplit_entries(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "registry.yaml"
            old = copy.deepcopy(self.registry)
            entry = next(e for e in old["terms"] if e["key"] == "cycle_iteration")
            entry["pt"], entry["pt_variants"] = "ciclo / iteração", ["ciclos"]  # pre-split seed, plus a hand-added variant
            other = next(e for e in old["terms"] if e["key"] == "coverage")
            other["pt"], other["notes"] = "cobertura total", "kept"
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(terms_import.dump_registry(old))
            terms_import.main(["--input", str(SURVEY), "--registry", str(path), "--quiet"])
            plain = {e["key"]: e for e in terms_lint.load_registry(path)["terms"]}
            self.assertEqual(plain["cycle_iteration"]["pt"], "ciclo / iteração")  # preserved without the flag
            terms_import.main(["--input", str(SURVEY), "--registry", str(path), "--quiet", "--split-pt-alternatives"])
            first = path.read_bytes()
            split = {e["key"]: e for e in terms_lint.load_registry(path)["terms"]}
            self.assertEqual(split["cycle_iteration"]["pt"], "ciclo")
            self.assertEqual(split["cycle_iteration"]["pt_variants"], ["ciclos", "iteração"])
            self.assertEqual(split["coverage"]["pt"], "cobertura total")  # untouched: no separator
            self.assertEqual(split["coverage"]["notes"], "kept")
            terms_import.main(["--input", str(SURVEY), "--registry", str(path), "--quiet", "--split-pt-alternatives"])
            self.assertEqual(first, path.read_bytes())  # idempotent

    def test_contract_generic_unfolds(self):
        self.assertNotIn("contract_generic", self.by_key)
        for key, en in (("manual_mapping_contract", "manual-mapping contract"), ("consumer_contract", "consumer contract")):
            self.assertEqual(self.by_key[key]["en"], en)
            self.assertEqual(self.by_key[key]["curator"]["id"], "contract_generic")
            self.assertEqual(self.by_key[key]["state"], "in-record")
        self.assertIn("slice_contract", self.by_key)
        self.assertIn("retrieval_contract", self.by_key)

    def test_rerun_is_byte_identical_and_preserves_hand_edits(self):
        before = self.registry_path.read_bytes()
        terms_import.main(["--input", str(SURVEY), "--registry", str(self.registry_path), "--quiet"])
        self.assertEqual(before, self.registry_path.read_bytes())

        edited = copy.deepcopy(self.registry)
        entry = next(e for e in edited["terms"] if e["key"] == "coverage")
        entry.update({"state": "in-record", "pending_reason": None, "pt_variants": ["coberturas"], "notes": "decided", "en": "coverage"})
        entry["counts"] = {"total": 0}  # will be refreshed from the survey
        with open(self.registry_path, "w", encoding="utf-8") as handle:
            handle.write(terms_import.dump_registry(edited))
        terms_import.main(["--input", str(SURVEY), "--registry", str(self.registry_path), "--quiet"])
        after = {e["key"]: e for e in terms_lint.load_registry(self.registry_path)["terms"]}
        self.assertEqual(after["coverage"]["state"], "in-record")
        self.assertIsNone(after["coverage"]["pending_reason"])
        self.assertEqual(after["coverage"]["pt_variants"], ["coberturas"])
        self.assertEqual(after["coverage"]["notes"], "decided")
        self.assertEqual(after["coverage"]["counts"]["total"], self.by_key["coverage"]["counts"]["total"])
        self.assertEqual(len(after), 158)
        # restore the seeded state for the other tests
        with open(self.registry_path, "w", encoding="utf-8") as handle:
            handle.write(terms_import.dump_registry(self.registry))

    def test_committed_registry_matches_the_survey(self):
        """Species-1 entries of the committed registry carry the survey-owned fields verbatim.

        The Manual agent's review may change state, pt, pt_variants, blocks_translation and notes,
        and appends species-2/3 entries, so only survey-owned fields of species-1 entries are compared."""
        self.assertTrue(REGISTRY.is_file(), "translation/terms/registry.yaml must be committed")
        committed = {e["key"]: e for e in terms_lint.load_registry(REGISTRY)["terms"]}
        seeded = {e["key"]: e for e in self.registry["terms"]}
        self.assertTrue(set(seeded) <= set(committed), sorted(set(seeded) - set(committed)))
        for key, fresh in seeded.items():
            for field in ("species", "en", "en_variants", "sense", "senses", "evidence", "counts", "change_cost", "curator"):
                self.assertEqual(committed[key][field], fresh[field], f"{key}.{field}")
        for key, entry in committed.items():
            if key not in seeded:
                self.assertIn(entry["species"], (2, 3), f"{key}: unexpected species-1 entry absent from the survey")


class ValidateTests(unittest.TestCase):
    def test_seeded_registry_is_valid(self):
        with tempfile.TemporaryDirectory() as tmp:
            registry = terms_lint.load_registry(seed(Path(tmp)))
        self.assertEqual(terms_lint.validate_registry(registry), [])

    def test_changed_requires_previous(self):
        registry = registry_with(minimal_entry("alpha", state="changed"))
        problems = terms_lint.validate_registry(registry)
        self.assertTrue(any("previous is required" in p for p in problems))

    def test_species_2_pending_requires_proposal_and_false_friends(self):
        registry = registry_with(
            minimal_entry("piso", species=2, state="pending", en=None, pending_reason="unborn", owner="archon", false_friends=None),
            minimal_entry("floor"),
        )
        problems = terms_lint.validate_registry(registry)
        self.assertTrue(any("proposal is required" in p for p in problems))
        self.assertTrue(any("false_friends must be a list" in p for p in problems))
        ok = registry_with(
            minimal_entry("piso", species=2, state="pending", en=None, pending_reason="unborn", owner="archon", proposal="foundation", false_friends=["floor"]),
            minimal_entry("floor"),
        )
        self.assertEqual(terms_lint.validate_registry(ok), [])

    def test_other_rules(self):
        registry = registry_with(minimal_entry("alpha"), minimal_entry("alpha"))
        self.assertTrue(any("duplicate key" in p for p in terms_lint.validate_registry(registry)))
        registry = registry_with(minimal_entry("alpha", en=None))
        self.assertTrue(any("en may be null only" in p for p in terms_lint.validate_registry(registry)))
        registry = registry_with(minimal_entry("alpha", false_friends=["ghost"]))
        self.assertTrue(any("unknown key 'ghost'" in p for p in terms_lint.validate_registry(registry)))
        registry = registry_with(minimal_entry("alpha", state="pending"))
        self.assertTrue(any("pending_reason is required" in p for p in terms_lint.validate_registry(registry)))


class SpellingTests(unittest.TestCase):
    def findings(self, text: str, registry=None):
        return terms_lint.spelling_findings_for_text(text, "fixture.md", terms_lint.ExemptionIndex(registry))

    def test_fixture_three_findings_and_protected_forms(self):
        text = common.read_text(FIXTURES / "en-spelling.md")
        found = self.findings(text)
        tokens = sorted((f.token, f.suggestion) for f in found)
        self.assertEqual(tokens, [("Organization", "Organisation"), ("analyze", "analyse"), ("color", "colour")])
        self.assertTrue(all(f.severity == "error" for f in found))
        self.assertNotIn("Artifact", [f.token for f in found])  # entity type name, not prose
        # Nothing from the code block or the comment, and the heading id is masked.
        self.assertTrue(all(f.line in (7, 9, 10) for f in found), [f.line for f in found])

    def test_lower_case_artifact_is_prose(self):
        found = self.findings("The artifact is produced; ArtifactRequirement and artifact_types are not.\n")
        self.assertEqual([(f.token, f.suggestion) for f in found], [("artifact", "artefact")])

    def test_exceptions_and_registry_exemptions(self):
        self.assertEqual(self.findings("Size, prize, seize and capsize are fine; normalise too.\n"), [])
        registry = registry_with(
            minimal_entry("normalization", en="normalization", en_variants=["normalized ontology", "Organizational view", "Centralized Logging", "program"]),
            minimal_entry("centre", en="center", en_variants=["colored", "labeled"]),
        )
        # Registry forms exempt only their en-GB spelling: spelling is style, not terminology.
        self.assertEqual(self.findings("The normalisation of the normalised ontology; organisational view; centralised logging; the centre is coloured and labelled; a programme.\n", registry), [])
        found = self.findings("The normalization of the normalized ontology; Organizational view; the center is colored; a program.\n", registry)
        self.assertEqual([f.token for f in found], ["normalization", "normalized", "Organizational", "center", "colored", "program"])
        self.assertEqual(
            terms_lint.ame_registry_forms(registry),
            [
                ("centre", "center", "centre"), ("centre", "colored", "coloured"), ("centre", "labeled", "labelled"),
                ("normalization", "Centralized Logging", "Centralised Logging"), ("normalization", "Organizational view", "Organisational view"),
                ("normalization", "normalization", "normalisation"), ("normalization", "normalized ontology", "normalised ontology"),
                ("normalization", "program", "programme"),
            ],
        )
        self.assertEqual(terms_lint.normalise_form_en_gb("ControlObjective"), "ControlObjective")  # identifiers untouched
        pending = registry_with(minimal_entry("normalization", state="pending", pending_reason="unborn", en="normalisation"))
        self.assertEqual(len(self.findings("The normalisation.\n", pending)), 0)
        self.assertEqual(len(self.findings("The normalization.\n", pending)), 1)  # pending has no authority either way

    def test_programme_and_licence(self):
        found = self.findings("A program under the license; we license it. Colors.\n")
        by_token = {f.token: f for f in found}
        self.assertEqual(by_token["program"].severity, "error")  # not a software context
        self.assertEqual(by_token["program"].suggestion, "programme")
        self.assertEqual(by_token["Colors"].severity, "error")
        licences = [f for f in found if f.token == "license"]
        self.assertEqual([f.severity for f in licences], ["error", "warning"])
        # Software contexts are accepted.
        self.assertEqual(self.findings("The program code; the program runs; a Python program; the programs crashed.\n"), [])
        self.assertEqual([f.token for f in self.findings("The research programs of the programme.\n")], ["programs"])

    def test_fix_applies_only_unambiguous_errors(self):
        text = "The color program.\n"
        fixed = terms_lint.apply_fixes(text, self.findings(text))
        self.assertEqual(fixed, "The colour program.\n")


class PendingBlocksTests(unittest.TestCase):
    def setUp(self):
        self.registry = registry_with(
            minimal_entry("coverage", state="pending", pending_reason="polysemy", senses=[{"sense": "x", "where": None}], pt="cobertura", pt_variants=["coberturas"], en="coverage"),
            minimal_entry("quiet", state="pending", pending_reason="unborn", pt="silêncio", blocks_translation=False),
        )

    def test_fixture_blocks(self):
        needles = terms_lint.pending_needles(self.registry)
        self.assertEqual(sorted(needles), ["coverage"])  # blocks_translation: false is skipped
        text = common.read_text(FIXTURES / "pt-pending.md")
        total, hits = terms_lint.pending_blocks_for_text(text, needles)
        kinds = sorted((b.kind, b.line) for b, key, _ in hits)
        self.assertEqual(kinds, [("admonition", 25), ("cell", 18), ("frontmatter", 3), ("item", 13), ("paragraph", 9)])
        self.assertTrue(total > len(hits))
        # "Descobertura" is not a whole word; the code block and the code span are not prose.
        self.assertNotIn(29, [b.line for b, _, _ in hits])
        self.assertNotIn(21, [b.line for b, _, _ in hits])

    def test_nfc_and_case(self):
        needles = terms_lint.pending_needles(registry_with(minimal_entry("k", state="pending", pending_reason="unborn", pt="ameaça", en="threat")))
        decomposed = "Uma AMEAÇA real.\n"
        _total, hits = terms_lint.pending_blocks_for_text(decomposed, needles)
        self.assertEqual(len(hits), 1)


class ExportAndHashTests(unittest.TestCase):
    def test_export_is_deterministic_and_grouped_by_owner(self):
        registry = registry_with(
            minimal_entry("floor", sense="admissibility floor"),
            minimal_entry("piso", species=2, state="pending", en=None, pending_reason="unborn", owner="archon", proposal="foundation relation", false_friends=["floor"]),
            minimal_entry("coverage", state="pending", pending_reason="polysemy", pt="cobertura", senses=[{"sense": "a", "where": None}, {"sense": "b", "where": None}]),
        )
        one = terms_lint.export_pending_markdown(registry, "abc")
        two = terms_lint.export_pending_markdown(copy.deepcopy(registry), "abc")
        self.assertEqual(one, two)
        self.assertIn("## `owner: archon` (1)", one)
        self.assertIn("## `owner: lead` (0)", one)
        self.assertIn("## `owner: manual-agent` (1)", one)
        self.assertIn("`floor` (admissibility floor)", one)
        self.assertIn("a · b", one)
        self.assertLess(one.index("owner: archon"), one.index("owner: lead"))

    def test_hash_matches_sync_state(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "translation" / "terms").mkdir(parents=True)
            registry = seed(root / "translation" / "terms")
            self.assertEqual(terms_lint.registry_sha256(registry), sync_state.terms_registry_sha256(root))


class Species3Tests(unittest.TestCase):
    def test_lemma_and_ngrams(self):
        self.assertEqual(species3_candidates.lemma("validações"), "validação")
        self.assertEqual(species3_candidates.lemma("requisitos"), "requisito")
        self.assertEqual(species3_candidates.lemma("controladores"), "controlador")
        self.assertEqual(species3_candidates.lemma("nível"), "nível")
        tokens = species3_candidates.tokens_of("o ciclo de vida das aplicações e ACO-TMR-008")
        grams = list(species3_candidates.ngrams_of(tokens))
        self.assertIn("ciclo de vida", grams)
        self.assertIn("aplicação", grams)
        self.assertNotIn("vida das", grams)

    def test_registry_forms_are_excluded(self):
        excluder = species3_candidates.Excluder(registry_with(minimal_entry("k", pt="cobertura", en="coverage")))
        cleaned = excluder.clean("a cobertura e a coverage e ACO-TMR-008 e o resto")
        self.assertNotIn("cobertura", cleaned)
        self.assertNotIn("coverage", cleaned)
        self.assertNotIn("ACO-TMR-008", cleaned)
        self.assertIn("resto", cleaned)


if __name__ == "__main__":
    unittest.main()
