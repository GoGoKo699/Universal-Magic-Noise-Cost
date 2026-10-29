"""Check local Markdown navigation, math delimiters and the common learning map.

This is a source check, not a hosted GitHub/MathJax visual inspection.
"""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parents[1]


def without_fences(text: str) -> str:
    result = []
    fence = None
    for line in text.splitlines():
        match = re.match(r'^\s*(`{3,}|~{3,})', line)
        if match:
            token = match.group(1)
            if fence is None:
                fence = token[0]
            elif fence == token[0]:
                fence = None
            result.append('')
        elif fence is None:
            result.append(line)
        else:
            result.append('')
    assert fence is None, 'Unclosed fenced block'
    return '\n'.join(result)


def heading_ids(text: str) -> set[str]:
    seen = {}
    ids = set()
    for heading in re.findall(r'^#{1,6}\s+(.+)$', without_fences(text), re.M):
        slug = re.sub(r'[^\w\- ]', '', heading.strip().lower()).replace(' ', '-')
        index = seen.get(slug, 0)
        seen[slug] = index + 1
        ids.add(slug if index == 0 else f'{slug}-{index}')
    ids.update(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', text))
    return ids


def main() -> None:
    pages = sorted(ROOT.rglob('*.md'))
    pages = [p for p in pages if '.git' not in p.parts and '.venv' not in p.parts]
    content = {p: p.read_text(encoding='utf-8') for p in pages}
    anchors = {p: heading_ids(text) for p, text in content.items()}
    links = 0
    for path, text in content.items():
        plain = without_fences(text)
        assert not re.search(r'\\[()\[\]]', plain), f'Legacy math delimiter in {path}'
        assert plain.count('$`') == plain.count('`$'), f'Inline math mismatch in {path}'
        for target in re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)', plain):
            parts = urlsplit(target)
            if parts.scheme or target.startswith('//'):
                continue
            dest = (path.parent / unquote(parts.path)).resolve() if parts.path else path
            assert dest.is_relative_to(ROOT), f'Escaping link in {path}: {target}'
            assert dest.exists(), f'Missing target in {path}: {target}'
            if parts.fragment and dest.suffix == '.md':
                assert unquote(parts.fragment) in anchors[dest], f'Missing anchor in {path}: {target}'
            links += 1
    milestones = content[ROOT / 'learning/MILESTONES.md']
    blocks = re.split(r'^### (M\d{2})\. ', milestones, flags=re.M)
    ids = blocks[1::2]
    assert ids == [f'M{i:02}' for i in range(1, 31)], 'Milestone count or ordering mismatch'
    phase1, phase2 = milestones.split('## Phase II:', 1)
    assert len(re.findall(r'^### M\d{2}\.', phase1, re.M)) == 12
    assert len(re.findall(r'^### M\d{2}\.', phase2, re.M)) == 18
    for ident, block in zip(ids, blocks[2::2]):
        for field in ('**Question:**', '**Understanding target:**', '**Dependencies and connection:**', '**Sources:**'):
            assert field in block, f'{ident} lacks {field}'
        dep = block.split('**Dependencies and connection:**', 1)[1].split('**Sources:**', 1)[0]
        assert all(int(x) < int(ident[1:]) for x in re.findall(r'\bM(\d{2})\b', dep)), f'Forward dependency in {ident}'
    for path in ('learning/README.md', 'learning/GOTTESMAN_BRIDGE.md', 'learning/MILESTONES.md'):
        assert '0904.2557v1' in content[ROOT / path], f'Anchor missing in {path}'
    assert not (ROOT / 'manuscript').exists(), 'Obsolete manuscript entrypoint'
    assert not list(ROOT.rglob('COACHING.md')), 'Personal coaching contract in source repository'
    print(f'PASS documents: {len(pages)} Markdown pages, {links} local links, 30 milestones (12/18), backward dependencies and one selected anchor.')
    print('Hosted mathematical rendering and semantic proof review are separate checks.')


if __name__ == '__main__':
    main()
