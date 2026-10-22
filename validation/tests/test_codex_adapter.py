"""Static M4 adapter checks; no Codex runtime or authorization assertions."""

from pathlib import Path
import re
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'validation'))
import validate_controls as m2


class CodexAdapterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entry = (ROOT / 'AGENTS.md').read_text(encoding='utf-8')
        cls.guide = (ROOT / 'adapters/codex/README.md').read_text(encoding='utf-8')

    def test_native_root_discovery_and_references(self):
        self.assertTrue((ROOT / 'AGENTS.md').is_file())
        self.assertFalse((ROOT / 'AGENTS.override.md').exists())
        refs = re.findall(r'\[[^]\n]+\]\(([^)]+)\)', self.entry)
        for required in ('core/standards/ENGINEERING_STANDARD.md',
                         'core/standards/AUTONOMY_AND_RISK.md',
                         'core/controls/controls.json',
                         'core/contracts/COMPLETION_CONTRACT.md'):
            self.assertIn(required, refs)
        for ref in refs:
            self.assertTrue((ROOT / ref).is_file(), ref)
        self.assertNotRegex(self.entry, r'(?m)^@')  # No Claude import convention.
        self.assertNotRegex(self.entry, r'(?m)^## STD-\d{2} — ')
        self.assertNotRegex(self.guide, r'(?m)^## STD-\d{2} — ')

    def test_quick_and_material_boundaries(self):
        self.assertIn('Quick trivial low-risk work needs no formal task file', self.entry)
        self.assertIn('For material changes', self.entry)
        self.assertIn('acceptance criteria', self.entry)
        self.assertIn('completion contract', self.entry)
        self.assertIn('acceptance, verification, merge, and release remain separate', self.entry)
        schemas = {name: m2.read_json(m2.SCHEMA_DIR / (name + '.schema.json'))
                   for name in m2.CONTRACTS}
        quick = m2.read_json(ROOT / 'validation/fixtures/valid/quick-no-task-record.json')
        self.assertEqual([], m2.fixture_errors(quick, m2.read_json(m2.CATALOG),
                         m2.read_json(m2.SCHEMA_DIR / 'control.schema.json'),
                         m2.policy_sections(), schemas))
        material = m2.read_json(ROOT / 'validation/fixtures/valid/material-task.json')['record']
        self.assertEqual([], m2.record_errors(material, 'task', schemas))

    def test_high_risk_and_completion_states(self):
        self.assertIn('pause those actions until appropriately authorized', self.entry)
        schemas = {name: m2.read_json(m2.SCHEMA_DIR / (name + '.schema.json'))
                   for name in m2.CONTRACTS}
        high = m2.read_json(ROOT / 'validation/fixtures/valid/high-risk-task.json')['record']
        self.assertEqual([], m2.record_errors(high, 'task', schemas))
        self.assertEqual('pending', high['approval_boundaries'][0]['status'])
        missing = m2.read_json(ROOT / 'validation/fixtures/invalid/missing-approval-boundary.json')['record']
        self.assertEqual([('schema.required', '$.approval_boundaries')],
                         [(e['code'], e['path']) for e in m2.record_errors(missing, 'task', schemas)])
        completion = m2.read_json(ROOT / 'validation/fixtures/valid/completed-pending-review.json')['record']
        self.assertEqual([], m2.record_errors(completion, 'completion', schemas))
        self.assertEqual(('Completed', 'Pending review', 'not performed', 'not performed'),
                         (completion['execution_state'], completion['acceptance_state'],
                          completion['merge']['state'], completion['release']['state']))

    def test_optional_records_fail_actionably_when_chosen(self):
        schemas = {name: m2.read_json(m2.SCHEMA_DIR / (name + '.schema.json'))
                   for name in m2.CONTRACTS}
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, 'cannot read JSON'):
                m2.read_json(Path(tmp) / 'missing.json')
            malformed = Path(tmp) / 'bad.json'
            malformed.write_text('{bad', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'cannot read JSON'):
                m2.read_json(malformed)
        bad = m2.read_json(ROOT / 'validation/fixtures/invalid/missing-task-criteria.json')['record']
        self.assertEqual([('schema.required', '$.acceptance_criteria')],
                         [(e['code'], e['path']) for e in m2.record_errors(bad, 'task', schemas)])

    def test_claude_coexistence_and_no_runtime_config(self):
        claude = (ROOT / 'CLAUDE.md').read_text(encoding='utf-8')
        self.assertIn('@core/standards/ENGINEERING_STANDARD.md', claude)
        self.assertIn('@core/standards/AUTONOMY_AND_RISK.md', claude)
        self.assertTrue((ROOT / 'adapters/claude-code/README.md').is_file())
        for path in ('.codex/config.toml', '.codex/rules', '.codex/hooks'):
            self.assertFalse((ROOT / path).exists(), path)
        self.assertIn('Do not copy this distribution\'s entry file over an established one', self.guide)
        self.assertIn('delete only M4-added guidance', self.guide)


if __name__ == '__main__':
    unittest.main()
