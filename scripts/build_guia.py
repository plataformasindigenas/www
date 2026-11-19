"""Render terradoc's editing guide (docs/guia/ in plataformasindigenas/terradoc) as
terradoc.org/guia/. The guide's source stays in terradoc; the publish workflow runs this on every
push, so the page follows the latest guide.

    python scripts/build_guia.py <terradoc checkout> <output dir>

Writes <output>/guia/index.html and copies the screenshots to <output>/guia/img/. Needs
markdown-it-py (installed with terradoc).
"""
import html
import re
import shutil
import sys
import unicodedata
from pathlib import Path

from markdown_it import MarkdownIt

REPO = "https://github.com/plataformasindigenas/terradoc/blob/master/docs/"


def slug(text: str) -> str:
    """GitHub's heading anchors: lower case, punctuation dropped (letters with accents kept),
    spaces to hyphens. The guide's table of contents uses these."""
    text = unicodedata.normalize("NFC", text.strip().lower())
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def render(md_text: str) -> tuple[str, str]:
    md = MarkdownIt("gfm-like", {"html": False, "linkify": False})
    tokens = md.parse(md_text)
    title = "Guia"
    for i, tok in enumerate(tokens):
        if tok.type == "heading_open":
            text = tokens[i + 1].content
            tok.attrSet("id", slug(text))
            if tok.tag == "h1":
                title = text
        if tok.type == "inline":
            for child in tok.children or []:
                if child.type == "link_open":
                    href = child.attrGet("href") or ""
                    if href.startswith("../"):  # other docs: read them on GitHub
                        child.attrSet("href", REPO + href[3:])
    return title, md.renderer.render(tokens, md.options, {})


PAGE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · Terradoc</title>
<meta name="description" content="Guia passo a passo para alterar as plataformas da Plataforma de Línguas Indígenas e publicar as alterações.">
<link rel="icon" type="image/svg+xml" href="../logo.svg">
<style>
*,*::before,*::after{{box-sizing:border-box}}
body{{margin:0;font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;color:#2c2520;background:#faf9f7;line-height:1.65;-webkit-font-smoothing:antialiased}}
header{{border-bottom:1px solid #e5e0da;padding:1rem 1.5rem}}
header a{{color:#5c534b;font-weight:600;text-decoration:none}}
main{{max-width:46rem;margin:0 auto;padding:2rem 1.5rem 4rem}}
a{{color:#a85d33}} a:hover{{color:#8f4e2b}}
h1{{font-size:2rem;line-height:1.2;letter-spacing:-0.02em}}
h2{{margin-top:3rem;padding-top:1rem;border-top:1px solid #e5e0da}}
h3{{margin-top:2rem}}
img{{max-width:100%;height:auto;border:1px solid #e5e0da;border-radius:6px;display:block;margin:1rem 0}}
code{{font-family:ui-monospace,'SFMono-Regular',Menlo,Consolas,monospace;font-size:0.9em;background:#f5f3ef;padding:0.1em 0.35em;border-radius:4px}}
pre{{background:#f5f3ef;border:1px solid #efe9e2;border-radius:8px;padding:1rem 1.25rem;overflow-x:auto}}
pre code{{background:none;padding:0}}
table{{border-collapse:collapse;width:100%;display:block;overflow-x:auto;font-size:0.92rem}}
th,td{{border:1px solid #e5e0da;padding:0.4rem 0.6rem;text-align:left;vertical-align:top}}
th{{background:#f5f3ef}}
blockquote{{margin:1rem 0;padding:0.5rem 1rem;border-left:4px solid #a85d33;background:#f5f3ef}}
hr{{border:0}}
footer{{max-width:46rem;margin:0 auto;padding:0 1.5rem 3rem;color:#8a8078;font-size:0.85rem}}
</style>
</head>
<body>
<header><a href="../">← Terradoc</a></header>
<main>
{body}
</main>
<footer>Este guia é mantido no repositório do terradoc:
<a href="https://github.com/plataformasindigenas/terradoc/tree/master/docs/guia">docs/guia</a>.</footer>
</body>
</html>
"""


def main(terradoc: Path, out: Path) -> None:
    src = terradoc / "docs" / "guia"
    title, body = render((src / "README.md").read_text(encoding="utf-8"))
    dest = out / "guia"
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src / "img", dest / "img")
    (dest / "index.html").write_text(PAGE.format(title=html.escape(title), body=body), encoding="utf-8")
    print(f"guia: {dest / 'index.html'} ({len(list((dest / 'img').iterdir()))} images)")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
