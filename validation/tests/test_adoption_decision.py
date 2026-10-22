"""M7 manual adoption decision kit regressions; no runtime or enforcement claims."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
KIT = ROOT / "docs" / "adoption-decision"
FILES = {"README.md", "INVENTORY.md", "DECISION_MATRIX.md", "EXAMPLE.md", "ROLLBACK.md"}


class M7AdoptionDecisionTests(unittest.TestCase):
    def test_inventory_and_no_extra_policy_definitions(self):
        self.assertEqual(FILES, {p.name for p in KIT.glob("*.md")})
        for path in KIT.glob("*.md"):
            body = path.read_text(encoding="utf-8")
            with self.subTest(path=path.name):
                self.assertNotRegex(body, r"(?m)^## STD-\d{2} — ")
                self.assertNotIn("automatic invocation is guaranteed", body)

    def test_relative_links_exist_within_repository(self):
        for path in KIT.glob("*.md"):
            body = path.read_text(encoding="utf-8")
            for dest in re.findall(r"\[[^\]\n]+\]\(([^)\s]+)\)", body):
                if "://" in dest:
                    continue
                target = (path.parent / dest.split("#", 1)[0]).resolve()
                with self.subTest(path=path.name, destination=dest):
                    self.assertTrue(target.is_relative_to(ROOT))
                    self.assertTrue(target.is_file())

    def test_three_legitimate_decisions_and_conflict_owner(self):
        body = (KIT / "DECISION_MATRIX.md").read_text(encoding="utf-8")
        for phrase in ("No adoption", "Reference only", "Selective adoption",
                       "responsible owner", "Unverified"):
            self.assertIn(phrase, body)

    def test_no_forced_quick_forms_or_permission_claims(self):
        body = (KIT / "EXAMPLE.md").read_text(encoding="utf-8")
        self.assertIn("no mandatory task form", body)
        self.assertIn("not a grant to write or publish", body)
        self.assertIn("not executed", body)
        index = (KIT / "README.md").read_text(encoding="utf-8")
        self.assertIn("not automatically invoked", index)

    def test_rollback_and_acceptance_boundaries(self):
        rollback = (KIT / "ROLLBACK.md").read_text(encoding="utf-8")
        self.assertIn("Remove only pilot-introduced material", rollback)
        self.assertIn("uncommitted changes", rollback)
        self.assertIn("merge, and release states separate", rollback)
        example = (KIT / "EXAMPLE.md").read_text(encoding="utf-8")
        self.assertIn("not **Accepted**", example)


if __name__ == "__main__":
    unittest.main()
