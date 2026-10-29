"""Guard against valid-looking but incomplete hosted mathematical expressions.

Source lint and fixtures run offline. The Chromium check supplies full MathML
text, in document order, to validate_rendered. This is a completeness regression
check for relations and equation labels, not a mathematical equivalence prover.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
MATH = re.compile(r'^```math\s*\n(.*?)^```\s*$|\$`([^\n]*?)`\$', re.M | re.S)
RELATIONS = {
    'lt': '<', 'gt': '>', 'le': '≤', 'leq': '≤', 'ge': '≥', 'geq': '≥',
    'ne': '≠', 'neq': '≠', 'in': '∈', 'subseteq': '⊆',
}
COMMAND = re.compile(r'\\(' + '|'.join(sorted(RELATIONS, key=len, reverse=True)) + r')(?![A-Za-z])')
LABEL = re.compile(r'\\(?:text|tag)\{\(?([A-Z]\d+)\)?\}')


def expressions(text: str) -> list[str]:
    return [m.group(1) if m.group(1) is not None else m.group(2) for m in MATH.finditer(text)]


def validate_source(text: str, name: str) -> int:
    formulas = expressions(text)
    for index, formula in enumerate(formulas, 1):
        if re.search(r'<\s*[A-Za-z]', formula):
            raise AssertionError(f'{name}, expression {index}: HTML-like inequality; use \\lt with a separator')
    return len(formulas)


def expected_relations(tex: str) -> Counter[str]:
    expected = Counter(COMMAND.sub(lambda m: RELATIONS[m.group(1)], tex))
    return Counter({symbol: expected[symbol] for symbol in '<>=≤≥≠∈⊆' if expected[symbol]})


def validate_rendered(source: str, rendered: list[dict], name: str) -> dict:
    formulas = expressions(source)
    if len(formulas) != len(rendered):
        raise AssertionError(f'{name}: {len(formulas)} source expressions but {len(rendered)} rendered hosts')
    labels_checked = 0
    for index, (tex, item) in enumerate(zip(formulas, rendered), 1):
        text = item.get('text', '')
        if not text.strip():
            raise AssertionError(f'{name}, expression {index}: missing full MathML text')
        expected = expected_relations(tex)
        actual = Counter({symbol: text.count(symbol) for symbol in '<>=≤≥≠∈⊆' if text.count(symbol)})
        if actual != expected:
            raise AssertionError(f'{name}, expression {index}: relation mismatch: expected {dict(expected)}, got {dict(actual)}; {text!r}')
        compact = re.sub(r'\s+', '', text)
        for label in LABEL.findall(tex):
            if f'({label})' not in compact:
                raise AssertionError(f'{name}, expression {index}: missing equation label ({label})')
            labels_checked += 1
    return {'expressions_checked': len(formulas), 'equation_labels_checked': labels_checked}


class ContractTests(unittest.TestCase):
    def test_expression_order(self):
        self.assertEqual(expressions('$`x`$\n\n```math\na=b\n```\n\n$`y`$'), ['x', 'a=b\n', 'y'])

    def test_unsafe_source_is_rejected(self):
        with self.assertRaises(AssertionError):
            validate_source('```math\n|A|<d\n```', 'fixture')

    def test_explicit_relation_survives(self):
        source = '```math\n|A|\\lt d.\\qquad\\text{(C1)}\n```'
        report = validate_rendered(source, [{'text': '| A | < d . ( C1 )'}], 'fixture')
        self.assertEqual(report['equation_labels_checked'], 1)

    def test_missing_inequality_is_rejected(self):
        source = '```math\nw(P)\\lt d.\\qquad\\text{(C6)}\n```'
        with self.assertRaises(AssertionError):
            validate_rendered(source, [{'text': 'w(P)'}], 'fixture')

    def test_missing_label_is_rejected(self):
        with self.assertRaises(AssertionError):
            validate_rendered('```math\na=b\\qquad\\text{(C2)}\n```', [{'text': 'a=b'}], 'fixture')

    def test_missing_host_is_rejected(self):
        with self.assertRaises(AssertionError):
            validate_rendered('$`x`$', [], 'fixture')

    def test_command_boundaries(self):
        self.assertEqual(expected_relations(r'0\le x\lt\infty,\quad s\in S'), Counter({'≤': 1, '<': 1, '∈': 1}))


def main() -> None:
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ContractTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    count = 0
    for path in sorted(ROOT.rglob('*.md')):
        if '.git' in path.parts or '.venv' in path.parts:
            continue
        count += validate_source(path.read_text(encoding='utf-8'), str(path.relative_to(ROOT)))
    print(f'PASS mathematical source contract: {count} expressions; all completeness regression fixtures pass.')


if __name__ == '__main__':
    main()
