"""Inspect this public repository's actual GitHub mathematics in Chromium.

Run separately from the offline scientific suite. This checks the live hosting
renderer, records DOM/layout evidence and saves screenshots for inspection.
It neither authenticates to GitHub nor submits any page action.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

from playwright.sync_api import sync_playwright

REPOSITORY = 'GoGoKo699/Universal-Magic-Noise-Cost'
PAGES = ('README.md', 'learning/GOTTESMAN_BRIDGE.md', 'science/converse.md')

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
  const errors = collect(article, 'mjx-merror, merror, .katex-error, [data-mjx-error]');
  const math = hosts.map((host) => {
    const root = host.shadowRoot || host;
    const box = host.getBoundingClientRect();
    const rendered = collect(root, 'mjx-container, svg, math, img');
    const failed = collect(root, '[data-mjx-error], mjx-merror, merror, .katex-error');
    return {display: host.getAttribute('display-mode'), width: box.width,
      height: box.height, rendered: rendered.length, errors: failed.map(x => x.textContent),
      sample: host.textContent.trim().slice(0, 120),
      root_sample: root.innerHTML.slice(0, 350)};
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--revision', required=True)
    parser.add_argument('--output', default='hosted-check')
    args = parser.parse_args()
    if not re.fullmatch(r'[0-9a-f]{40}', args.revision):
        raise ValueError('Use the exact 40-character source commit, not an arbitrary URL')
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    reports = []
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
            page.locator('article.markdown-body, .markdown-body').first.wait_for(timeout=60000)
            # Scroll the rendered article to activate lazy math components.
            height = page.evaluate('document.documentElement.scrollHeight')
            for offset in range(0, height, 700):
                page.evaluate('(y) => window.scrollTo(0, y)', offset)
                page.wait_for_timeout(100)
            page.wait_for_timeout(2500)
            page.evaluate('window.scrollTo(0, 0)')
            report = page.evaluate(INSPECT)
            report.update({'page': relative, 'revision': args.revision, 'http_status': status})
            reports.append(report)
            name = relative.replace('/', '_').replace('.md', '')
            page.screenshot(path=str(output / f'{name}.png'), full_page=True)
            (output / f'{name}.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
            print(json.dumps(report), flush=True)
        browser.close()
    (output / 'report.json').write_text(json.dumps(reports, indent=2), encoding='utf-8')
    for report in reports:
        assert report.get('math_count', 0) > 0, f'No math components found in {report["page"]}'
        assert report['rendered_count'] == report['math_count'], f'Unrendered math in {report["page"]}'
        assert report['error_count'] == 0, f'Math renderer error in {report["page"]}'
        assert all(m['width'] > 0 and m['height'] > 0 for m in report['math']), 'Zero-size rendered math'
        assert report['document_width'] <= report['viewport_width'] + 2, 'Page-wide horizontal overflow'
    print('PASS actual GitHub Chromium DOM/layout checks for README, Gottesman bridge and converse.')
    print('Screenshots and detailed DOM evidence are saved separately; no manual pixel review is implied.')


if __name__ == '__main__':
    main()
