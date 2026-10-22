#!/usr/bin/env python3
"""M2 structural checks. This is a documented JSON Schema subset, not enforcement."""

import argparse
import copy
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'core/controls/controls.json'
SCHEMA_DIR = ROOT / 'core/controls/schema'
CONTRACTS = ('task', 'handoff', 'completion', 'exception')
EXPECTED_FIXTURES = {
    'valid': {'quick-no-task-record', 'material-task', 'high-risk-task', 'handoff',
              'completed-pending-review', 'authorized-exception', 'high-risk-exception',
              'nonmaterial-high-risk-exception', 'low-risk-exception-no-trigger'},
    'invalid': {'duplicate-control', 'unknown-policy-reference', 'missing-task-criteria',
                'missing-approval-boundary', 'missing-authorization-evidence',
                'invalid-status', 'completed-implies-accepted', 'agent-self-authorization',
                'high-risk-missing-trigger', 'unsupported-schema-version',
                'missing-check-result', 'completed-unmet-criteria', 'merge-without-evidence'},
}
SUPPORTED = {'$schema', '$id', 'title', 'description', 'type', 'properties',
             'required', 'additionalProperties', 'enum', 'const', 'minLength',
             'minItems', 'items', 'allOf', 'if', 'then'}
DRAFT = 'https://json-schema.org/draft/2020-12/schema'
POLICY = ROOT / 'core/standards/ENGINEERING_STANDARD.md'
COMPLETION = ROOT / 'core/contracts/COMPLETION_CONTRACT.md'


def issue(code, path, detail):
    return {'code': code, 'path': path, 'detail': detail}


def read_json(path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f'{path}: cannot read JSON: {exc}') from exc


def audit_schema(schema, name):
    """Reject unknown keywords and malformed schema declarations we cannot validate."""
    problems = []
    if not isinstance(schema, dict) or schema.get('$schema') != DRAFT:
        return [issue('schema.declaration', '$', f'{name}: expected Draft 2020-12 declaration')]
    if schema.get('$id') != f'urn:ai-engineering-starter:m2:{name}:1.0':
        problems.append(issue('schema.declaration', '$.$id', f'{name}: unsupported schema identity'))

    def visit(node, path):
        if not isinstance(node, dict):
            problems.append(issue('schema.declaration', path, 'schema node must be an object'))
            return
        for key in sorted(set(node) - SUPPORTED):
            problems.append(issue('schema.unsupported_keyword', f'{path}.{key}', 'keyword is not implemented'))
        if 'type' in node and node['type'] not in ('object', 'array', 'string', 'boolean'):
            problems.append(issue('schema.declaration', f'{path}.type', 'unsupported type'))
        if 'required' in node and (not isinstance(node['required'], list)
                                    or any(not isinstance(x, str) for x in node['required'])):
            problems.append(issue('schema.declaration', f'{path}.required', 'expected string array'))
        if 'enum' in node and (not isinstance(node['enum'], list) or not node['enum']):
            problems.append(issue('schema.declaration', f'{path}.enum', 'expected nonempty array'))
        for key in ('minLength', 'minItems'):
            if key in node and (type(node[key]) is not int or node[key] < 0):
                problems.append(issue('schema.declaration', f'{path}.{key}', 'expected nonnegative integer'))
        if 'additionalProperties' in node and not isinstance(node['additionalProperties'], bool):
            problems.append(issue('schema.declaration', f'{path}.additionalProperties', 'expected boolean'))
        if ('if' in node) != ('then' in node):
            problems.append(issue('schema.declaration', path, 'if and then must occur together'))
        if 'properties' in node:
            if not isinstance(node['properties'], dict):
                problems.append(issue('schema.declaration', f'{path}.properties', 'expected object'))
            else:
                for key, sub in sorted(node['properties'].items()):
                    visit(sub, f'{path}.properties.{key}')
        if 'items' in node:
            visit(node['items'], f'{path}.items')
        if 'allOf' in node:
            if not isinstance(node['allOf'], list):
                problems.append(issue('schema.declaration', f'{path}.allOf', 'expected array'))
            else:
                for index, sub in enumerate(node['allOf']):
                    visit(sub, f'{path}.allOf[{index}]')
        for key in ('if', 'then'):
            if key in node:
                visit(node[key], f'{path}.{key}')

    visit(schema, '$')
    return problems


def shape(value, schema, path='$'):
    """Validate only the keywords audited above. Report paths in stable order."""
    errors = []
    expected = schema.get('type')
    kinds = {'object': lambda v: isinstance(v, dict),
             'array': lambda v: isinstance(v, list),
             'string': lambda v: isinstance(v, str),
             'boolean': lambda v: isinstance(v, bool)}
    if expected and not kinds[expected](value):
        return [issue('schema.type', path, f'expected {expected}')]
    if 'const' in schema and value != schema['const']:
        errors.append(issue('schema.const', path, f'expected {schema["const"]!r}'))
    if 'enum' in schema and value not in schema['enum']:
        errors.append(issue('schema.enum', path, f'expected one of {schema["enum"]!r}'))
    if isinstance(value, str) and len(value) < schema.get('minLength', 0):
        errors.append(issue('schema.minLength', path, 'nonempty text required'))
    if isinstance(value, list):
        if len(value) < schema.get('minItems', 0):
            errors.append(issue('schema.minItems', path, f'expected at least {schema["minItems"]} item(s)'))
        if 'items' in schema:
            for index, item in enumerate(value):
                errors.extend(shape(item, schema['items'], f'{path}[{index}]'))
    if isinstance(value, dict):
        props = schema.get('properties', {})
        for key in schema.get('required', []):
            if key not in value:
                errors.append(issue('schema.required', f'{path}.{key}', 'required field is missing'))
        if schema.get('additionalProperties') is False:
            for key in sorted(set(value) - set(props)):
                errors.append(issue('schema.additionalProperties', f'{path}.{key}', 'unexpected field'))
        for key, sub in props.items():
            if key in value:
                errors.extend(shape(value[key], sub, f'{path}.{key}'))
    for condition in schema.get('allOf', []):
        errors.extend(shape(value, condition, path))
    if 'if' in schema and not shape(value, schema['if'], path):
        errors.extend(shape(value, schema.get('then', {}), path))
    return errors


def policy_sections():
    body = POLICY.read_text(encoding='utf-8')
    matches = list(re.finditer(r'^## (STD-\d{2}) — (.+)$', body, re.M))
    result = {}
    for index, match in enumerate(matches):
        if match.group(1) in result:
            raise ValueError('duplicate canonical policy heading: ' + match.group(1))
        section = body[match.end():matches[index + 1].start() if index + 1 < len(matches) else len(body)]
        labels = re.findall(r'^\*\*(MUST(?: \(Profile H\))?|SHOULD|MAY):\*\*', section, re.M)
        result[match.group(1)] = (match.group(2), labels)
    return result


def catalog_errors(catalog, schema, policy):
    errors = shape(catalog, schema)
    if not isinstance(catalog, dict) or not isinstance(catalog.get('controls'), list):
        return errors
    seen = set()
    expected = {f'STD-{i:02}' for i in range(1, 17)}
    for index, control in enumerate(catalog['controls']):
        if not isinstance(control, dict):
            continue
        where = f'$.controls[{index}]'
        identifier = control.get('id')
        if not isinstance(identifier, str):
            continue
        if identifier in seen:
            errors.append(issue('catalog.duplicate_id', where + '.id', f'duplicate {identifier}'))
        seen.add(identifier)
        if identifier not in policy:
            errors.append(issue('catalog.unknown_policy', where + '.id', f'unknown {identifier}'))
            continue
        ref = control.get('policy_reference')
        wanted = ('core/standards/ENGINEERING_STANDARD.md#' + identifier.lower() + '--' +
                  re.sub(r'[^\w\- ]', '', policy[identifier][0].lower()).replace(' ', '-'))
        if ref != wanted:
            errors.append(issue('catalog.unknown_policy_reference', where + '.policy_reference',
                                f'{identifier} must reference {wanted}'))
        title, labels = policy[identifier]
        if control.get('title') != title:
            errors.append(issue('catalog.title_drift', where + '.title', f'{identifier} title differs from standard'))
        raw_clauses = control.get('clauses')
        if not isinstance(raw_clauses, list):
            continue
        found = [x.get('source_label') for x in raw_clauses if isinstance(x, dict)]
        if found != labels:
            errors.append(issue('catalog.clause_drift', where + '.clauses',
                                f'{identifier} expected source labels {labels!r}'))
        for ci, clause in enumerate(raw_clauses):
            if not isinstance(clause, dict):
                continue
            source_label = clause.get('source_label')
            label = source_label.split(' ')[0] if isinstance(source_label, str) else ''
            category = {'MUST': 'requirement', 'SHOULD': 'recommendation', 'MAY': 'option'}.get(label)
            if clause.get('strength') != label or clause.get('category') != category:
                errors.append(issue('catalog.strength_drift', f'{where}.clauses[{ci}]',
                                    'strength/category disagree with source label'))
    if seen != expected:
        errors.append(issue('catalog.coverage', '$.controls',
                            f'missing {sorted(expected - seen)}; unexpected {sorted(seen - expected)}'))
    if set(policy) != expected:
        errors.append(issue('catalog.policy_drift', '$.controls',
                            f'canonical headings changed: {sorted(set(policy) ^ expected)}'))
    return errors


def status_errors(schemas):
    """Compare exact M1 status rows to the contract schemas, not just our copies."""
    body = COMPLETION.read_text(encoding='utf-8')
    try:
        mappings = [('Execution state', schemas['completion']['properties']['execution_state']['enum']),
                    ('Acceptance state', schemas['completion']['properties']['acceptance_state']['enum']),
                    ('Verification status', schemas['completion']['properties']['verification']['items']['properties']['status']['enum'])]
        handoff_values = schemas['handoff']['properties']['checks_run']['items']['properties']['status']['enum']
    except (KeyError, TypeError) as exc:
        return [issue('schema.declaration', '$.status', f'missing status schema component: {exc}')]
    errors = []
    for title, values in mappings:
        section = re.search(rf'^## {title}\n(.*?)(?=^## |\Z)', body, re.M | re.S)
        rows = re.findall(r'^\| ([^|]+?) \|', section.group(1), re.M)[2:] if section else []
        if rows != values:
            errors.append(issue('catalog.status_drift', '$.status', f'{title}: M1={rows!r}; schema={values!r}'))
    if mappings[2][1] != handoff_values:
        errors.append(issue('catalog.status_drift', '$.handoff.checks_run', 'verification vocabulary differs'))
    return errors


def record_errors(record, contract, schemas):
    return shape(record, schemas[contract])


def fixture_errors(fixture, catalog, catalog_schema, policy, schemas):
    if not isinstance(fixture, dict) or fixture.get('fixture_version') != '1.0':
        return [issue('fixture.version', '$.fixture_version', 'expected fixture version 1.0')]
    target = fixture.get('target')
    record = fixture.get('record')
    if target == 'none':
        context = fixture.get('context')
        return [] if record is None and context == {'risk_profile':'L','complexity':'T0','workflow':'Quick'} else [
            issue('fixture.no_record', '$.record', 'only a null record with L/T0/Quick context illustrates this case')]
    if target == 'catalog':
        mutated = copy.deepcopy(catalog)
        mutation = fixture.get('mutation', {})
        if not isinstance(mutation, dict):
            return [issue('fixture.mutation', '$.mutation', 'expected mutation object')]
        if mutation.get('op') == 'append_duplicate':
            source = next((x for x in mutated['controls'] if x['id'] == mutation.get('id')), None)
            if source is None:
                return [issue('fixture.mutation', '$.mutation', 'unknown source ID')]
            mutated['controls'].append(copy.deepcopy(source))
        elif mutation.get('op') == 'set_reference':
            source = next((x for x in mutated['controls'] if x['id'] == mutation.get('id')), None)
            if source is None:
                return [issue('fixture.mutation', '$.mutation', 'unknown source ID')]
            source['policy_reference'] = mutation.get('value')
        elif mutation.get('op') == 'remove_control':
            mutated['controls'] = [x for x in mutated['controls'] if x['id'] != mutation.get('id')]
        else:
            return [issue('fixture.mutation', '$.mutation', 'unsupported catalog mutation')]
        return catalog_errors(mutated, catalog_schema, policy)
    if target not in CONTRACTS:
        return [issue('fixture.target', '$.target', 'expected catalog, none, or a known contract')]
    return record_errors(record, target, schemas)


def run_suite():
    try:
        catalog = read_json(CATALOG)
        catalog_schema = read_json(SCHEMA_DIR / 'control.schema.json')
        schemas = {name: read_json(SCHEMA_DIR / (name + '.schema.json')) for name in CONTRACTS}
        policy = policy_sections()
    except ValueError as exc:
        return [issue('input.json', '$', str(exc))], 0, 0
    errors = audit_schema(catalog_schema, 'control-catalog')
    for name, entry in schemas.items():
        errors.extend(audit_schema(entry, name))
    if errors:
        return errors, 0, 0
    errors.extend(catalog_errors(catalog, catalog_schema, policy))
    errors.extend(status_errors(schemas))
    counts = [0, 0]
    for folder, slot in [('valid', 0), ('invalid', 1)]:
        paths = sorted((ROOT / 'validation/fixtures' / folder).glob('*.json'))
        names = {path.stem for path in paths}
        if names != EXPECTED_FIXTURES[folder]:
            errors.append(issue('fixture.inventory', f'validation/fixtures/{folder}',
                                f'missing {sorted(EXPECTED_FIXTURES[folder] - names)}; '
                                f'unexpected {sorted(names - EXPECTED_FIXTURES[folder])}'))
        for path in paths:
            counts[slot] += 1
            try:
                fixture = read_json(path)
            except ValueError as exc:
                errors.append(issue('fixture.json', str(path.relative_to(ROOT)), str(exc)))
                continue
            found = fixture_errors(fixture, catalog, catalog_schema, policy, schemas)
            expected_error = fixture.get('expected_error')
            actual = [{'code': x['code'], 'path': x['path']} for x in found]
            wanted = [] if folder == 'valid' else [expected_error]
            if actual != wanted:
                errors.append(issue('fixture.outcome', str(path.relative_to(ROOT)),
                                    f'expected {wanted!r}; actual {actual!r}'))
    return errors, *counts


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--contract', choices=CONTRACTS, help='validate raw record paths for this contract')
    parser.add_argument('paths', nargs='*', type=Path, help='raw records with --contract, otherwise fixture envelopes')
    args = parser.parse_args(argv)
    errors, valid_count, invalid_count = run_suite()
    if args.paths and not errors:
        catalog = read_json(CATALOG)
        catalog_schema = read_json(SCHEMA_DIR / 'control.schema.json')
        policy = policy_sections()
        schemas = {name: read_json(SCHEMA_DIR / (name + '.schema.json')) for name in CONTRACTS}
        for path in args.paths:
            try:
                value = read_json(path)
                problems = (record_errors(value, args.contract, schemas) if args.contract else
                            fixture_errors(value, catalog, catalog_schema, policy, schemas))
                errors.extend({**item, 'detail': f'{path}: {item["detail"]}'} for item in problems)
            except ValueError as exc:
                errors.append(issue('input.json', str(path), str(exc)))
    if errors:
        print('Failed: M2 structural validation')
        for item in errors:
            print(f'- {item["code"]} {item["path"]}: {item["detail"]}')
        return 1
    print(f'Passed: 16 controls; 5 schema declarations; {valid_count} valid and '
          f'{invalid_count} intentionally failing fixtures; policy labels and statuses match M1.'
          + (f' {len(args.paths)} supplied record(s) valid.' if args.paths else ''))
    print('Unverified: semantic policy equivalence, real authorization, actual checks, runtime enforcement.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
