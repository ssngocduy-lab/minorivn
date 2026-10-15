from pathlib import Path
from html.parser import HTMLParser

root = Path(__file__).parent / 'dist'
pages = list(root.rglob('index.html'))

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src') and value:
                if not (value.startswith('http://') or value.startswith('https://') or value.startswith('#') or value.startswith('mailto:') or value.startswith('tel:')):
                    self.refs.append(value.split('#')[0])

missing = []
for page in pages:
    parser = PageParser()
    parser.feed(page.read_text(encoding='utf-8'))
    for ref in parser.refs:
        if not ref:
            continue
        if ref.startswith('/'):
            target = (root / ref.lstrip('/')).resolve()
        else:
            target = (page.parent / ref).resolve()

        if not target.exists() and not (target / 'index.html').exists():
            missing.append((str(page), ref))

forbidden = [p for p in root.rglob('*') if any(x in p.name.lower() for x in ['tham khao', 'thao khao'])]
assert len(pages) == 5, pages
assert not missing, f"Missing references: {missing}"
assert not forbidden, forbidden
print('5 pages, all local links resolved, no partner reference images')
