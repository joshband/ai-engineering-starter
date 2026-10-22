"""M3 structural contract checks; no Claude Code runtime behavior is asserted."""

import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'validation'))
import validate_controls as m2


class ClaudeAdapterTests(unittest.TestCase):
    def test_root_discovery_imports_resolve_to_canonical_sources(self):
        entry = (ROOT / 'CLAUDE.md').read_text(encoding='utf-8')
        imports = re.findall(r'^@([^\s]+)\s*$', entry, re.M)
        self.assertEqual([
            'core/standards/ENGINEERING_STANDARD.md',
            'core/standards/AUTONOMY_AND_RISK.md',
        ], imports)
        for path in imports:
            self.assertTrue((ROOT / path).is_file(), path)
        self.assertNotRegex(entry, r'(?m)^## STD-\d{2} — ')
        self.assertIn('core/controls/controls.json', entry)

    def test_quick_no_record_and_material_contract_boundaries(self):
        schemas = {name: m2.read_json(m2.SCHEMA_DIR / (name + '.schema.json'))
                   for name in m2.CONTRACTS}
        catalog = m2.read_json(m2.CATALOG)
        catalog_schema = m2.read_json(m2.SCHEMA_DIR / 'control.schema.json')
        quick = m2.read_json(ROOT / 'validation/fixtures/valid/quick-no-task-record.json')
        self.assertEqual([], m2.fixture_errors(quick, catalog, catalog_schema,
                                                m2.policy_sections(), schemas))
        material = m2.read_json(ROOT / 'validation/fixtures/invalid/missing-task-criteria.json')
        self.assertEqual([('schema.required', '$.acceptance_criteria')],
                         [(e['code'], e['path']) for e in m2.record_errors(material['record'], 'task', schemas)])

    def test_high_risk_escalation_and_acceptance_separation(self):
        task_schema = m2.read_json(m2.SCHEMA_DIR / 'task.schema.json')
        task = m2.read_json(ROOT / 'validation/fixtures/valid/high-risk-task.json')['record']
        self.assertEqual('pending', task['approval_boundaries'][0]['status'])
        self.assertEqual([], m2.shape(task, task_schema))
        task.pop('approval_boundaries')
        self.assertEqual([('schema.required', '$.approval_boundaries')],
                         [(e['code'], e['path']) for e in m2.shape(task, task_schema)])
        completion_schema = m2.read_json(m2.SCHEMA_DIR / 'completion.schema.json')
        completion = m2.read_json(ROOT / 'validation/fixtures/valid/completed-pending-review.json')['record']
        self.assertEqual(('Completed', 'Pending review', 'not performed'),
                         (completion['execution_state'], completion['acceptance_state'], completion['merge']['state']))
        self.assertEqual([], m2.shape(completion, completion_schema))

    def test_missing_and_malformed_optional_records_report_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            absent = Path(tmp) / 'absent.json'
            with self.assertRaisesRegex(ValueError, 'cannot read JSON'):
                m2.read_json(absent)
            malformed = Path(tmp) / 'bad.json'
            malformed.write_text('{bad', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'cannot read JSON'):
                m2.read_json(malformed)

    def test_no_runtime_extension_required_for_validation(self):
        self.assertFalse((ROOT / '.claude/settings.json').exists())
        self.assertFalse((ROOT / '.claude/hooks').exists())
        env = dict(os.environ, PATH='', PYTHONDONTWRITEBYTECODE='1')
        proc = subprocess.run([sys.executable, 'validation/validate.py'], cwd=ROOT,
                              env=env, capture_output=True, text=True, check=False)
        self.assertEqual(0, proc.returncode, proc.stdout + proc.stderr)


if __name__ == '__main__':
    unittest.main()
