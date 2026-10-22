"""Regression tests for catalog coverage and conditional exception boundaries."""

import copy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'validation'))
import validate_controls as vc


class ControlsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = vc.read_json(vc.CATALOG)
        cls.catalog_schema = vc.read_json(vc.SCHEMA_DIR / 'control.schema.json')
        cls.exception_schema = vc.read_json(vc.SCHEMA_DIR / 'exception.schema.json')
        cls.policy = vc.policy_sections()
        cls.high = vc.read_json(ROOT / 'validation/fixtures/valid/high-risk-exception.json')['record']

    def test_missing_catalog_control_is_detected(self):
        changed = copy.deepcopy(self.catalog)
        changed['controls'] = changed['controls'][:-1]
        codes = {x['code'] for x in vc.catalog_errors(changed, self.catalog_schema, self.policy)}
        self.assertIn('catalog.coverage', codes)

    def test_material_high_risk_trigger_is_conditional(self):
        high = dict(self.high)
        high.pop('expiration_or_review_trigger')
        self.assertEqual([('schema.required', '$.expiration_or_review_trigger')],
                         [(x['code'], x['path']) for x in vc.shape(high, self.exception_schema)])
        high['material'] = False
        self.assertEqual([], vc.shape(high, self.exception_schema))
        high['material'] = True
        high['risk_profile'] = 'S'
        self.assertEqual([], vc.shape(high, self.exception_schema))

    def test_acceptance_is_independent_of_execution(self):
        schema = vc.read_json(vc.SCHEMA_DIR / 'completion.schema.json')
        record = vc.read_json(ROOT / 'validation/fixtures/valid/completed-pending-review.json')['record']
        self.assertEqual([], vc.shape(record, schema))
        record.pop('acceptance_state')
        self.assertEqual([('schema.required', '$.acceptance_state')],
                         [(x['code'], x['path']) for x in vc.shape(record, schema)])


if __name__ == '__main__':
    unittest.main()
