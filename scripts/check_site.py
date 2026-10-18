"""Check static routes, local references, and common accidental private files."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re

root = Path(__file__).resolve().parents[1]
site = root / "site"
errors = []
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.ids = set(); self.base = None
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a: self.ids.add(a["id"])
        if tag == "base": self.base = a.get("href")
        else:
            for key in ("src", "href"):
                if a.get(key): self.links.append(a[key])

pages = {}
for file in site.rglob("*.html"):
    page = Page(); page.feed(file.read_text()); pages[file.resolve()] = page
for file, page in pages.items():
    parent = (file.parent / page.base).resolve() if page.base else file.parent
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc: continue
        target = ((site / unquote(url.path).lstrip("/")) if url.path.startswith("/") else parent / unquote(url.path)).resolve() if url.path else file
        if not target.is_relative_to(site.resolve()):
            errors.append(f"Outside site: {file.name}: {link}"); continue
        if target.is_dir(): target /= "index.html"
        if not target.exists(): errors.append(f"Missing: {file.name}: {link}")
        if url.fragment and target in pages and url.fragment not in pages[target].ids:
            errors.append(f"Missing anchor: {file.name}: {link}")
patterns = [r"gh[pousr]_[A-Za-z0-9]{20,}", r"github_pat_[A-Za-z0-9_]{30,}", r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"]
for path in root.rglob("*"):
    if ".git" in path.parts: continue
    if path.is_symlink(): errors.append(f"Symlink not allowed: {path.relative_to(root)}")
    if path.name == ".openai" or path.name.startswith(".env") or path.suffix in {".key", ".pem"}:
        errors.append(f"Private configuration: {path.relative_to(root)}")
    if path.is_file() and path.suffix in {".html", ".css", ".js", ".json", ".yml", ".md"}:
        text = path.read_text()
        if any(re.search(pattern, text) for pattern in patterns): errors.append(f"Possible secret: {path.relative_to(root)}")
for required in ["index.html", "resume.html", "resume/index.html", "Dhyey-Radadia-Resume.pdf", "Dhyey-Radadia-Resume.docx"]:
    if not (site / required).is_file(): errors.append(f"Missing required file: {required}")
if errors: raise SystemExit("\n".join(errors))
print(f"PASS: {len(pages)} HTML pages, local assets and anchors, required downloads, and basic secret checks.")
