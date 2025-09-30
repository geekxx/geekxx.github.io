Recipe preview tools

Run the preview builder to render all recipes in `recipes/` to HTML files under `_site_preview/`.

Quick start:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python tools/build_preview.py
```

This will create `_site_preview/index.html` and one HTML file per recipe.
