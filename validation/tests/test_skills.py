"""M5 opt-in engineering skill library structural regressions (standard library only)."""
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "validation"))
import validate_controls as m2
SKILLS = {
    "task-intake": ("TASK_CONTRACT.md", "task.schema.json"),
    "change-verification": ("COMPLETION_CONTRACT.md", None),
    "review-and-acceptance": ("COMPLETION_CONTRACT.md", None),
    "safe-handoff": ("HANDOFF_CONTRACT.md", "handoff.schema.json"),
    "exception-review": ("EXCEPTION_CONTRACT.md", "exception.schema.json"),
}


class M5SkillsTests(unittest.TestCase):
    def test_inventory_and_canonical_contract_references(self):
        self.assertEqual(set(SKILLS), {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()})
        for name, (contract, schema) in SKILLS.items():
            with self.subTest(skill=name):
                path = ROOT / "skills" / name / "SKILL.md"
                self.assertTrue(path.is_file())
                body = path.read_text(encoding="utf-8")
                self.assertIn(f"](../../core/contracts/{contract})", body)
                self.assertIn("](../../core/standards/ENGINEERING_STANDARD.md)", body)
                if schema:
                    self.assertIn(f"](../../core/controls/schema/{schema})", body)
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
        self.assertIn("do not link, install, discover, or invoke these procedures automatically", index)
        for entry in ("AGENTS.md", "CLAUDE.md"):
            self.assertTrue((ROOT / entry).is_file())

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
        schema = {name: m2.read_json(m2.SCHEMA_DIR / (name + ".schema.json"))
                  for name in m2.CONTRACTS}
        valid_h = m2.read_json(ROOT / "validation/fixtures/valid/high-risk-exception.json")["record"]
        valid_lower = m2.read_json(ROOT / "validation/fixtures/valid/low-risk-exception-no-trigger.json")["record"]
        missing_h = m2.read_json(ROOT / "validation/fixtures/invalid/high-risk-missing-trigger.json")["record"]
        self.assertEqual([], m2.record_errors(valid_h, "exception", schema))
        self.assertEqual([], m2.record_errors(valid_lower, "exception", schema))
        self.assertEqual([("schema.required", "$.expiration_or_review_trigger")],
                         [(e["code"], e["path"]) for e in m2.record_errors(missing_h, "exception", schema)])

    def test_acceptance_is_not_merged_or_released(self):
        body = (ROOT / "skills" / "review-and-acceptance" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Separately record execution state", body)
        self.assertIn("whether a merge happened", body)
        self.assertIn("whether a release happened", body)
        self.assertIn("A recommendation is not acceptance", body)
        completion = m2.read_json(ROOT / "validation/fixtures/valid/completed-pending-review.json")["record"]
        self.assertEqual(("Completed", "Pending review", "not performed", "not performed"),
                         (completion["execution_state"], completion["acceptance_state"],
                          completion["merge"]["state"], completion["release"]["state"]))


if __name__ == "__main__":
    unittest.main()
