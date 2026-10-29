"""Inspect actual GitHub mathematics, including equation completeness.

The public pages are read without authentication or page actions. Full MathML
text is compared with the exact checked-out source, in addition to renderer and
layout checks. Screenshots and a tracked-source archive support visual review.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import zipfile

from check_math_contract import ROOT, validate_rendered, validate_source

REPOSITORY = 'GoGoKo699/Universal-Magic-Noise-Cost'
PAGES = ('README.md', 'learning/GOTTESMAN_BRIDGE.md', 'science/model.md', 'science/results.md', 'science/converse.md', 'science/construction.md', 'science/finite_protocols.md')

INSPECT = r"""() => {
  const article = document.querySelector('article.markdown-body') || document.querySelector('.markdown-body');
  if (!article) return {error: 'No rendered Markdown article', title: document.title};
  const collect = (root, selector) => {
    const hits = [...root.querySelectorAll(selector)];
    for (const element of root.querySelectorAll('*')) {
      if (element.shadowRoot) hits.push(...collect(element.shadowRoot, selector));
    }
    return hits;
  };
  const hosts = [...article.querySelectorAll('math-renderer')];
  const errors = collect(article, 'mjx-merror, merror, .katex-error, [data-mjx-error], .flash-error');
  const math = hosts.map((host) => {
    const root = host.shadowRoot || host;
    const box = host.getBoundingClientRect();
    const rendered = collect(root, 'mjx-container, svg, math, img');
    const mathml = collect(root, 'math');
    const failed = collect(root, '[data-mjx-error], mjx-merror, merror, .katex-error, .flash-error');
    return {display: mathml[0]?.getAttribute('display') || host.getAttribute('display-mode'),
      width: box.width, height: box.height, rendered: rendered.length,
      errors: failed.map(x => x.textContent),
      text: mathml.length ? mathml[0].textContent : host.textContent,
      sample: host.textContent.trim().slice(0, 120), root_sample: root.innerHTML.slice(0, 350)};
  });
  const tables = [...article.querySelectorAll('table')].map(table => {
    const box = table.getBoundingClientRect();
    const style = getComputedStyle(table);
    return {width: box.width, client_width: table.clientWidth, scroll_width: table.scrollWidth,
      overflow_x: style.overflowX};
  });
  return {title: document.title, heading: article.querySelector('h1')?.textContent,
    article_width: article.getBoundingClientRect().width,
    viewport_width: innerWidth, document_width: document.documentElement.scrollWidth,
    math_count: hosts.length, rendered_count: math.filter(x => x.rendered > 0).length,
    error_count: errors.length, errors: errors.map(x => x.textContent), math, tables,
    links: article.querySelectorAll('a[href]').length};
}"""


def main() -> None:
    from playwright.sync_api import sync_playwright

    parser = argparse.ArgumentParser()
    parser.add_argument('--revision', required=True)
    parser.add_argument('--output', default='hosted-check')
    args = parser.parse_args()
    if not re.fullmatch(r'[0-9a-f]{40}', args.revision):
        raise ValueError('Use the exact 40-character source commit, not an arbitrary URL')
    checked_out = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    if checked_out != args.revision:
        raise ValueError('Check out the specified revision before comparing source and hosted mathematics')
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    sources = {relative: (ROOT / relative).read_text(encoding='utf-8') for relative in PAGES}
    for relative, source in sources.items():
        validate_source(source, relative)
    tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
    with zipfile.ZipFile(output / 'source.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        for relative in tracked:
            if relative:
                archive.write(ROOT / relative, relative)
    reports = []
    failures = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={'width': 1440, 'height': 1000}, device_scale_factor=1)
        for relative in PAGES:
            url = f'https://github.com/{REPOSITORY}/blob/{args.revision}/{relative}'
            response = page.goto(url, wait_until='domcontentloaded', timeout=60000)
            status = response.status if response else None
            print(json.dumps({'page': relative, 'http_status': status}), flush=True)
            if status != 200:
                raise RuntimeError(f'Hosted page request failed: {relative}: {status}')
            article = page.locator('article.markdown-body, .markdown-body').first
            article.wait_for(timeout=60000)
            height = page.evaluate('document.documentElement.scrollHeight')
            for offset in range(0, height, 700):
                page.evaluate('(y) => window.scrollTo(0, y)', offset)
                page.wait_for_timeout(100)
            page.wait_for_timeout(2500)
            page.evaluate('window.scrollTo(0, 0)')
            report = page.evaluate(INSPECT)
            report.update({'page': relative, 'revision': args.revision, 'http_status': status})
            try:
                report['completeness'] = validate_rendered(sources[relative], report.get('math', []), relative)
            except AssertionError as error:
                report['completeness_error'] = str(error)
                failures.append(str(error))
            reports.append(report)
            name = relative.replace('/', '_').replace('.md', '')
            page.screenshot(path=str(output / f'{name}.png'), full_page=True)
            if relative == 'science/converse.md':
                for index, item in enumerate(report.get('math', [])):
                    compact = re.sub(r'\s+', '', item.get('text', ''))
                    for label in ('C1', 'C6'):
                        if f'({label})' in compact:
                            article.locator('math-renderer').nth(index).screenshot(path=str(output / f'{label}_detail.png'))
            (output / f'{name}.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
            print(json.dumps({k: v for k, v in report.items() if k != 'math'} | {
                'unrendered': [m for m in report.get('math', []) if not m['rendered'] or m['errors']],
                'display_heights': [m['height'] for m in report.get('math', []) if m['width'] >= 0.9 * report['article_width']]}), flush=True)
        browser.close()
    (output / 'report.json').write_text(json.dumps(reports, indent=2), encoding='utf-8')
    if failures:
        raise AssertionError('\n'.join(failures))
    for report in reports:
        assert report.get('math_count', 0) > 0, f'No math components found in {report["page"]}'
        assert report['rendered_count'] == report['math_count'], f'Unrendered math in {report["page"]}'
        assert report['error_count'] == 0, f'Math renderer error in {report["page"]}'
        assert all(m['width'] > 0 and m['height'] > 0 for m in report['math']), 'Zero-size rendered math'
        assert report['document_width'] <= report['viewport_width'] + 2, 'Page-wide horizontal overflow'
    print('PASS actual GitHub Chromium layout, relations and equation-label checks on seven pages.')
    print('Full MathML text and screenshots are retained; automated success does not imply manual pixel review.')


if __name__ == '__main__':
    main()
