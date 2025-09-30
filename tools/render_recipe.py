#!/usr/bin/env python3
import sys
from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


def load_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm = yaml.safe_load(parts[1])
            body = parts[2].strip()
            return fm, body
    return {}, text


def render_recipe(md_path: str, out_path: str = None):
    p = Path(md_path)
    fm, body = load_frontmatter(p)
    env = Environment(
        loader=FileSystemLoader(Path(__file__).parent),
        autoescape=select_autoescape(["html", "xml"]),
    )
    tmpl = env.get_template("recipe_template.html.j2")
    html = tmpl.render(page=fm)
    if out_path:
        Path(out_path).write_text(html, encoding="utf-8")
    else:
        print(html)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: render_recipe.py <recipe.md> [out.html]")
        sys.exit(2)
    render_recipe(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
