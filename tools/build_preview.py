#!/usr/bin/env python3
"""Build all recipe previews into _site_preview/.

Finds all .md files in ../recipes, loads YAML frontmatter, renders with the existing
Jinja2 template `recipe_template.html.j2`, and writes each output to _site_preview/<slug>.html.
Also creates a simple `index.html` linking to each preview.
"""
from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
import argparse
import re


def load_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm = yaml.safe_load(parts[1]) or {}
            body = parts[2].strip()
            return fm, body
    return {}, text


def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s or "recipe"


def render(page: dict, env: Environment) -> str:
    tmpl = env.get_template("recipe_template.html.j2")
    return tmpl.render(page=page)


def main(recipes_dir: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    env = Environment(
        loader=FileSystemLoader(Path(__file__).parent),
        autoescape=select_autoescape(["html", "xml"]),
    )

    entries = []
    for md in sorted(recipes_dir.glob("*.md")):
        fm, _ = load_frontmatter(md)
        title = fm.get("title") or md.stem
        slug = slugify(title)
        out_file = out_dir / f"{slug}.html"
        html = render(fm, env)
        out_file.write_text(html, encoding="utf-8")
        entries.append({"title": title, "file": out_file.name})

    # write a simple index
    idx = out_dir / "index.html"
    with idx.open("w", encoding="utf-8") as fh:
        fh.write("<!doctype html>\n<html><head><meta charset=\"utf-8\"><title>Recipe Previews</title></head><body>\n")
        fh.write("<h1>Recipe Previews</h1>\n<ul>\n")
        for e in entries:
            fh.write(f"  <li><a href=\"{e['file']}\">{e['title']}</a></li>\n")
        fh.write("</ul>\n</body></html>")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--recipes", default="../recipes", help="Directory containing recipe .md files (relative to tools)")
    parser.add_argument("--out", default="../_site_preview", help="Output directory for HTML previews")
    args = parser.parse_args()
    base = Path(__file__).parent
    recipes_dir = (base / args.recipes).resolve()
    out_dir = (base / args.out).resolve()
    main(recipes_dir, out_dir)
