"""M5 opt-in engineering skill library structural regressions (standard library only)."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
SKILLS = {
    "task-intake": ("TASK_CONTRACT.md", "task.schema.json"),
    "change-verification": ("COMPLETION_CONTRACT.md", None),
    "review-and-acceptance": ("COMPLETION_CONTRACT.md", None),
    "safe-handoff": ("HANDOFF_CONTRACT.md", "handoff.schema.json"),
    "exception-review": ("EXCEPTION_CONTRACT.md", "exception.schema.json"),
}


class M5SkillsTests(unittest.TestCase):
    def test_inventory_and_canonical_contract_references(self):
        for name, (contract, schema) in SKILLS.items():
            with self.subTest(skill=name):
                path = ROOT / "skills" / name / "SKILL.md"
                self.assertTrue(path.is_file())
                body = path.read_text(encoding="utf-8")
                self.assertIn(contract, body)
                if schema:
                    self.assertIn(schema, body)
                self.assertNotRegex(body, r"(?m)^## STD-\d{2} — ")

    def test_all_skill_links_resolve_inside_repository(self):
        for path in (ROOT / "skills").rglob("*.md"):
            body = path.read_text(encoding="utf-8")
            for dest in re.findall(r"\[[^\]\n]+\]\(([^)\s]+)\)", body):
                if "://" in dest:
                    continue
                target = (path.parent / dest.split("#", 1)[0]).resolve()
                with self.subTest(path=path.name, destination=dest):
                    self.assertTrue(target.is_relative_to(ROOT))
                    self.assertTrue(target.is_file())

    def test_skills_are_opt_in_and_not_permission_grants(self):
        index = (ROOT / "skills" / "README.md").read_text(encoding="utf-8")
        self.assertIn("opt-in", index)
        self.assertIn("do not claim automatic discovery", index)
        self.assertIn("do not grant permission", index)

    def test_quick_work_is_not_forced_into_structured_records(self):
        body = (ROOT / "skills" / "task-intake" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("do not require a form", body)
        self.assertIn("a short objective and boundary suffice", body)

    def test_exception_profile_h_condition_is_preserved(self):
        body = (ROOT / "skills" / "exception-review" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("material Profile H exception", body)
        self.assertIn("explicit expiration or review trigger", body)
        self.assertIn("For other exceptions, recommend one", body)
        self.assertIn("never grants one", body)

    def test_acceptance_is_not_merged_or_released(self):
        body = (ROOT / "skills" / "review-and-acceptance" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Separately record execution state", body)
        self.assertIn("whether a merge happened", body)
        self.assertIn("whether a release happened", body)
        self.assertIn("A recommendation is not acceptance", body)


if __name__ == "__main__":
    unittest.main()
